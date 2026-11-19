"""
His line list: every line of the builder's sheet in his order, with its wording, unit,
kind, division and subtotal block. No quantities, no prices and no rates, so it can be
read in a blind run (a filled price would give away which lines he used on a job).

It is the standing list of his lines that write_draft.py drafts onto. It uses the same
reading of his sheet as the import (import_builder_sheet.layout and sheet_rows), so a
draft and an import always have the same lines and line ids.

Limit: whether a row is a heading or a line is read from whether its unit and price
cells are empty on the sheet it was made from. Make the list from one past job and keep it;
do not remake it from the sheet of a job under blind test.

Usage: python3 -I checklist.py <estimate.xlsx> <names.json> <his_lines.json>
"""
import json
import os
import sys

import openpyxl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import import_builder_sheet as S  # noqa: E402
import redaction  # noqa: E402


def line_list(xlsx, names, job=S.JOB_A):
    """Read his sheet into the line list (a record; nothing is written here)."""
    wf = openpyxl.load_workbook(xlsx).worksheets[0]
    div_of, total_rows, groups = S.layout(wf, job)
    lines = []
    for r, (desc, _qty, unit, d, _e, _f), kind in S.sheet_rows(wf, job, div_of, total_rows):
        ln = {"row": r, "description": redaction.redact(str(desc), names) if desc is not None else "",
              "unit": unit, "kind": kind, "division": div_of[r], "group": S.group_of(groups, r)}
        if kind == "percent":
            ln["percent_role"], ln["base_rows"] = S.percent_parts(wf, ln["description"], d)
        lines.append(ln)
    r = job["markup_row"]  # his OH&P: a separate markup line on all cost
    lines.append({"row": r, "description": redaction.redact(str(wf.cell(r, 1).value), names), "unit": None,
                  "kind": "percent", "division": None, "group": None, "percent_role": "markup"})
    used = sorted({ln["division"] for ln in lines if ln["division"] is not None})
    return {"made_from": job["job"],
            "divisions": [{"number": n, "name": job["division_names"][n], "name_source": "Inferred"} for n in used],
            "groups": groups, "lines": lines}


def main(xlsx, names_path, out_path):
    names = redaction.load(names_path)
    text = json.dumps(line_list(xlsx, names), indent=0)
    left = [n for n in names if n.lower() in text.lower()]
    if left:
        print("NOT WRITTEN. A listed name survived:", len(left))
        return 1
    with open(out_path, "w") as f:
        f.write(text)
    kinds = {}
    for ln in json.loads(text)["lines"]:
        kinds[ln["kind"]] = kinds.get(ln["kind"], 0) + 1
    print("his line list written:", sum(kinds.values()), "lines", kinds)
    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:4]))


# Change log
# Nov 16, 2026 · Was a list of row, wording and unit. Now his full line list: kind, division, subtotal block
#   and the base rows of his tax and contingency lines, read with the import's own layout functions, and
#   redacted at the source. Still no quantities, prices or rates. Usage changed: it now needs the name list.
#   draft_job_a.py (to be retired) read the old shape.
