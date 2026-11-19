"""
Import the builder's own Excel estimate into the shared estimate format.

Used to prove the format on a real job: every row of his sheet becomes a
line in his order, his tax and contingency rows become percent lines with
their base written out, and OH&P becomes a separate markup line. The
result must pass estimate_format.check(); nothing is written if it fails.

This file also holds the one reading of his sheet's layout (layout, sheet_rows,
row_kind). checklist.py uses the same functions to list his lines without
quantities or prices, so an import and a draft always have the same lines.

Usage: python3 -I import_builder_sheet.py <estimate.xlsx> <cost_codes.json> <code_rows.json> <names.json> <made_at> <out.json>
  cost_codes.json  the builder's one cost code list
  code_rows.json   this job: which rows sit under which code, how each is filed, and any split across codes
  names.json  vendor, sub and client names to redact: {"name": "replacement"}. Kept with the
              job's data on the user's computer, never in code or project documents.
"""
import json
import os
import re
import sys

import openpyxl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import estimate_format as F  # noqa: E402
import redaction  # noqa: E402

# Everything specific to this one sheet lives here. A second job gets its own block.
JOB_A = {
    "id": "jobA-builder-2022-06-01", "job": "Job A", "job_type": "mixed", "parts": ["adu", "renovation"],
    "definition_level": "permit_plans", "price_basis": "2022-06-01",
    "unlabelled_total_rows": {502: 14},      # his HVAC total row has no label
    "after_total_rows": {598, 599, 600, 601, 604, 605},  # grand total block, handled below
    "markup_row": 599,
    # Division names are Inferred from the lines (his sheet only numbers them).
    "division_names": {1: "General conditions", 2: "Site work and demo", 3: "Concrete", 4: "Masonry",
                       5: "Metals", 6: "Framing and carpentry", 7: "Roofing, siding, insulation",
                       8: "Doors and windows", 9: "Finishes", 10: "Specialties",
                       12: "Cabinets and countertops", 14: "HVAC", 15: "Plumbing", 16: "Electrical",
                       17: "Appliances"},
    "not_imported": ["other worksheets (contract alternates, alternate backup, allowance adjustments, pay applications, concrete side maths)",
                     "row 601 price per SF", "rows 604-605 basement finish (blank on this job)",
                     "his side maths in the far-right columns",
                     "row 580 (a unit only, no wording or price, outside his division totals)"],
}

RANGE = re.compile(r"^=SUM\(G(\d+):G(\d+)\)$")
ONE = re.compile(r"^=(?:SUM\()?G(\d+)\)?$")


def rows_in(formula):
    """Rows a subtotal formula covers, or None if it is not a subtotal."""
    formula = formula if isinstance(formula, str) else ""
    m = RANGE.match(formula)
    if m:
        return list(range(int(m.group(1)), int(m.group(2)) + 1))
    m = ONE.match(formula)
    return [int(m.group(1))] if m else None


def num(v):
    return v if isinstance(v, (int, float)) else None


def layout(wf, job):
    """His sheet's structure, read from formulas only: the division of each row (from his
    "TOTAL - Division n" rows), which rows are those total rows, and his subtotal blocks (column H)."""
    div_of, total_rows = {}, set()
    for r in range(1, wf.max_row + 1):
        m = re.match(r"TOTAL - (Division (\d+)|Appliances)", str(wf.cell(r, 1).value or ""))
        n = job["unlabelled_total_rows"].get(r)
        if m:
            n = 17 if m.group(1) == "Appliances" else int(m.group(2))
        if n:
            for x in rows_in(wf.cell(r, 7).value):
                div_of.setdefault(x, n)
            total_rows.add(r)
    groups = []
    for r in range(1, wf.max_row + 1):
        span = rows_in(wf.cell(r, 8).value)
        if span and r not in total_rows:
            groups.append({"id": f"G{r}", "rows": span})
    return div_of, total_rows, groups


def group_of(groups, r):
    """The smallest of his subtotal blocks that holds this row."""
    inner = [g for g in groups if r in g["rows"]]
    return min(inner, key=lambda g: len(g["rows"]))["id"] if inner else None


def row_kind(cells):
    """What a row of his sheet is, from its six cells (wording, qty, unit, material, labor, M&L)."""
    desc, qty, unit, d, e, f = cells
    if all(v is None for v in cells):
        return "blank"  # an empty spacer row
    if isinstance(d, str) and d.startswith("="):
        return "percent"  # his tax / contingency rows: Qty holds the rate, his Material column points at the base
    if all(v is None for v in (qty, unit, d, e, f)):
        return "heading"
    return "item"


def sheet_rows(wf, job, div_of, total_rows):
    """Every row that becomes a line, in his order: (row number, its six cells, its kind).
    His total rows are not lines: the totals block replaces them."""
    for r in range(3, wf.max_row + 1):
        if r in total_rows or r in job["after_total_rows"] or r not in div_of:
            continue
        cells = tuple(wf.cell(r, c).value for c in range(1, 7))
        kind = row_kind(cells)
        if kind != "blank":
            yield r, cells, kind


def percent_parts(wf, description, d):
    """Role and base rows of one of his tax or contingency rows."""
    base_rows = rows_in(d)
    if base_rows is None and re.match(r"^=D(\d+)$", d):
        base_rows = rows_in(wf.cell(int(d[2:]), 4).value)
    role = "tax" if description.lower().startswith("tax") else "contingency"
    return role, base_rows


def main(xlsx, codes_path, rows_path, names_path, made_at, out_path, job=JOB_A):
    wf = openpyxl.load_workbook(xlsx).worksheets[0]                  # formulas
    wv = openpyxl.load_workbook(xlsx, data_only=True).worksheets[0]  # his cached values
    code_file = json.load(open(codes_path))
    job_codes = json.load(open(rows_path))
    codes = job_codes["rows"]
    names = redaction.load(names_path)
    notes = []

    div_of, total_rows, groups = layout(wf, job)
    lines, row_to_id = [], {}
    for r, (desc, qty, unit, d, e, f), kind in sheet_rows(wf, job, div_of, total_rows):
        if desc is None:
            notes.append(f"row {r}: no description in his sheet; kept as a blank-named line")
        lid = f"L{r:04d}"
        row_to_id[r] = lid
        ln = {"id": lid, "row": r, "division": div_of[r], "group": group_of(groups, r),
              "description": redaction.redact(str(desc), names) if desc is not None else ""}
        if kind == "percent":
            role, base_rows = percent_parts(wf, ln["description"], d)
            ln.update(kind="percent", percent_role=role, rate=qty, base_rows=base_rows,
                      scope="in", cost_type="material")
        elif kind == "heading":
            ln.update(kind="heading")
        else:
            if isinstance(qty, str):
                notes.append(f"row {r}: quantity is a formula ({qty}); left blank")
            ln.update(kind="item", qty=num(qty), unit=F.tidy_unit(unit), unit_as_written=unit,
                      material=num(d), labor=num(e), ml=num(f))
            # On his finished sheet a line with no cost is one he left out of this job.
            ln["scope"] = "in" if num(wv.cell(r, 7).value) else "out"
            if ln["scope"] == "out" and ln["qty"] and any(num(v) for v in (d, e, f)):
                notes.append(f"row {r}: has a quantity and a price but his sheet shows no cost; kept as he has it")
            if ln["qty"] is not None:
                ln["qty_source"] = {"type": "his_entry"}
            if any(num(v) for v in (d, e, f)):
                ln["price_source"] = {"type": "his_entry", "date": job["price_basis"], "job": job["job"]}
        if str(r) in job_codes.get("splits", {}):
            ln["cost_split"] = job_codes["splits"][str(r)]
        elif codes.get(str(r)):
            ln["cost_code"] = codes[str(r)]
        if str(r) in job_codes.get("filed_as", {}) and ln["kind"] != "percent":
            ln["filed_as"] = job_codes["filed_as"][str(r)]
        lines.append(ln)

    for ln in lines:
        if ln["kind"] == "percent":
            ln["base"] = [row_to_id[x] for x in ln.pop("base_rows") if x in row_to_id and x != ln["row"]]

    # His OH&P: a separate visible markup line on all cost.
    r = job["markup_row"]
    lines.append({"id": f"L{r:04d}", "row": r, "division": None, "group": None,
                  "description": str(wf.cell(r, 1).value), "kind": "percent", "percent_role": "markup",
                  "rate": wf.cell(r, 2).value, "base": F.ALL_COST, "scope": "in"})

    used = set(codes.values()) | {s["code"] for split in job_codes.get("splits", {}).values() for s in split}
    est = {
        "format": F.FORMAT_NAME, "format_version": F.FORMAT_VERSION,
        "estimate": {
            "id": job["id"], "job": job["job"], "job_type": job["job_type"], "parts": job["parts"],
            "definition_level": job["definition_level"], "status": "final", "version": 1,
            "parent_version": None, "made_by": "import", "made_at": made_at,
            "price_basis": job["price_basis"], "currency": "USD",
            "note": "Builder's own estimate sheet imported to prove the format. Not a draft.",
        },
        "divisions": [{"number": n, "name": job["division_names"][n], "name_source": "Inferred"}
                      for n in sorted({ln["division"] for ln in lines if ln["division"] is not None})],
        "cost_codes": [{k: c[k] for k in ("code", "name", "category")}
                       for c in code_file["codes"] if c["code"] in used],
        "groups": [{"id": g["id"], "lines": [row_to_id[x] for x in g["rows"] if x in row_to_id]}
                   for g in groups],
        "lines": lines,
        "changes": [],
    }
    problems = F.structure(est)
    if not problems:
        problems = F.save(F.fill_totals(est), out_path, names)
    if problems:
        print("NOT WRITTEN. Problems:", *problems, sep="\n  ")
        return 1

    t = est["totals"]
    his_cost, his_total = wv.cell(598, 7).value, wv.cell(600, 7).value
    print(f"cost  ours {t['cost']:>12,.2f}  his sheet {his_cost:>12,.2f}  diff {t['cost']-his_cost:+.2f}")
    print(f"total ours {t['total']:>12,.2f}  his sheet {his_total:>12,.2f}  diff {t['total']-his_total:+.2f}")
    kinds = {}
    for ln in lines:
        kinds[ln["kind"]] = kinds.get(ln["kind"], 0) + 1
    print("lines:", len(lines), kinds, "in scope:", sum(1 for ln in lines if ln.get("scope") == "in"))
    print("uncoded cost:", F.money(sum(t["by_code"].get(F.UNCODED, {}).values())))
    print("notes:", *notes, sep="\n  ")
    print("not imported:", *job["not_imported"], sep="\n  ")
    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:7]))


# Change log
# Nov 16, 2026 · The reading of his sheet's layout moved into layout(), sheet_rows(), row_kind() and
#   percent_parts() so checklist.py shares it. Redaction now comes from redaction.py (an empty name list is
#   refused). The file is totalled and written through estimate_format.fill_totals() and save().
#   Output unchanged: 471 lines, cost 231,247.05, total 289,058.81 (checked on his sheet).
