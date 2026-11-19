"""
Tests for the draft writer, on a small made-up line list (no real data).
Usage: python3 -I test_write_draft.py
Each test says what the writer must do with one kind of decision.
"""
import copy
import json
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import estimate_format as F  # noqa: E402
import write_draft as W  # noqa: E402

HIS = {"made_from": "Made-up job",
       "divisions": [{"number": n, "name": f"Division {n}", "name_source": "Inferred"} for n in (1, 6, 16)],
       "groups": [{"id": "G20", "rows": [12, 13, 14]}],
       "lines": [
           {"row": 4, "description": "Division 1", "unit": None, "kind": "heading", "division": 1, "group": None},
           {"row": 6, "description": "Permit", "unit": "LS", "kind": "item", "division": 1, "group": None},
           {"row": 7, "description": "Survey", "unit": "LS", "kind": "item", "division": 1, "group": None},
           {"row": 10, "description": "Division 6", "unit": None, "kind": "heading", "division": 6, "group": None},
           {"row": 12, "description": "2x4x8", "unit": "ea", "kind": "item", "division": 6, "group": "G20"},
           {"row": 13, "description": "Windows", "unit": "EA", "kind": "item", "division": 6, "group": "G20"},
           {"row": 14, "description": "Siding installation", "unit": "LS", "kind": "item", "division": 6, "group": "G20"},
           {"row": 15, "description": "Siding by the square", "unit": "SQ", "kind": "item", "division": 6, "group": None},
           {"row": 16, "description": "TAX", "unit": None, "kind": "percent", "division": 6, "group": None,
            "percent_role": "tax", "base_rows": [12, 13]},
           {"row": 20, "description": "Bid - electrical", "unit": "LS", "kind": "item", "division": 16, "group": None},
           {"row": 21, "description": "Days", "unit": "DAYS", "kind": "item", "division": 16, "group": None},
           {"row": 30, "description": "OH&P", "unit": None, "kind": "percent", "division": None, "group": None,
            "percent_role": "markup"}]}
CODES = {"codes": [{"code": "6080", "name": "Framing", "category": "6"}, {"code": "16100", "name": "Electrical", "category": "16"}]}
CODE_ROWS = {"rows": {"12": "6080", "20": "16100"}, "filed_as": {"20": {"ml": "subcontract"}}, "splits": {}}
DECISIONS = {
    "job": {"id": "made-up-draft", "job": "Made-up job", "job_type": "adu", "definition_level": "permit_plans"},
    "cover": {"missing_pages": ["No electrical plan"], "assumptions": [], "exclusions": [], "range": None},
    "lines": {
        "6": {"scope": "in", "qty": 1, "source": {"type": "assumed", "rule": "New building needs a permit"},
              "confidence": "medium", "reason": "New building needs a permit"},
        "12": {"scope": "in", "qty": 76, "source": {"type": "calculated", "page": "A-1", "rule": "one stud per foot of wall"},
               "plan_minimum": True, "confidence": "medium", "reason": "76 LF of wall"},
        "13": {"scope": "in", "qty": 9, "source": {"type": "counted", "page": "A-1"}, "cross_checked": True,
               "reason": "Counted on plan and elevations"},
        "20": {"scope": "in", "qty": 1, "source": {"type": "written", "page": "A-0"}, "kind": "sub_bid",
               "reason": "Whole-job electrical bid"},
        "21": {"scope": "out", "confidence": "high", "reason": "No such work on the plans"}},
    "overlaps": [{"rows": [14, 15], "question": "Which line do you use for siding labor?", "usual_row": 15}],
    "new_lines": [{"description": "Cat door", "division": 6, "why": "Drawn at the porch"}]}
PRICES = {"date": "2022-06-01", "job": "Made-up job",
          "lines": {"12": {"material": 4.5, "type": "his_price", "mark": "medium", "reason": "His 2022 price."},
                    "13": {"ml": 900, "type": "his_price", "mark": "high"},
                    "20": {"ml": 16500, "type": "sub_bid", "mark": "low"}},
          "rates": {"16": {"rate": 0.089, "mark": "medium", "reason": "His 2022 rate."},
                    "30": {"rate": 0.25, "mark": "medium", "reason": "His 2022 rate."}}}
AT = "2026-11-16T15:00:00-05:00"


def build(decisions=DECISIONS, prices=None):
    return W.build(copy.deepcopy(HIS), copy.deepcopy(decisions), CODES, AT, CODE_ROWS, copy.deepcopy(prices))


def changed(**lines):
    d = copy.deepcopy(DECISIONS)
    for row, value in lines.items():
        d["lines"][row.lstrip("r")] = value
    return d


def refused(decisions, words, prices=None):
    _, problems, _ = build(decisions, prices)
    assert any(words in p for p in problems), (words, problems[:3])


est, problems, notes = build()
assert problems == [] and F.check(est) == [], (problems, F.check(est))
L = {ln["row"]: ln for ln in est["lines"] if ln["row"]}
assert est["estimate"]["status"] == "draft" and est["format_version"] == F.FORMAT_VERSION

# a line with no decision is Ask and Low, never Out; headings stay headings
assert L[7]["scope"] == "ask" and L[7]["confidence"] == {"line": "low", "qty": "low", "price": None, "reason": W.NO_RULE}
assert L[4]["kind"] == "heading" and "scope" not in L[4]
assert not any(ln.get("scope") == "out" for ln in est["lines"] if ln["row"] not in (21,))

# marks never sit above the Method's rule
assert L[6]["confidence"]["line"] == "low" and any("row 6" in n for n in notes)          # assumed: Low, and reported
assert L[12]["confidence"]["line"] == "low" and L[12]["confidence"]["reason"].startswith("Plan minimum: ")
assert L[13]["confidence"]["line"] == "high"                                              # counted and cross-checked
assert L[20]["kind"] == "sub_bid" and L[20]["confidence"]["line"] == "low"                # a sub bid is always Low
assert L[21]["scope"] == "out" and L[21]["confidence"]["line"] == "high"
assert L[12]["qty_source"] == {"type": "calculated", "page": "A-1", "rule": "one stud per foot of wall"}
assert L[21]["unit"] == "DAY" and L[21]["unit_as_written"] == "DAYS" and L[12]["cost_code"] == "6080"

# overlapping lines: one Ask question on each line of the group
assert L[14]["scope"] == L[15]["scope"] == "ask" and "Which line do you use" in L[14]["confidence"]["reason"]
assert "'Siding by the square'" in L[14]["confidence"]["reason"] and "he used 'Siding by the square'" in L[14]["confidence"]["reason"]

# blank rates are allowed on a draft; markup is always in; "not on his list" sits apart, before the markup line
assert L[16]["rate"] is None and L[16]["scope"] == "ask" and L[30]["rate"] is None and L[30]["scope"] == "in"
assert L[16]["base"] == ["L0012", "L0013"]
new = next(ln for ln in est["lines"] if ln.get("scope") == "new")
assert new["id"] == "N001" and est["lines"][-1]["id"] == "L0030" and est["totals"]["total"] == 0
assert est["cover"]["check_first"] == [] and "no dollars yet" in est["cover"]["check_first_note"]
assert {o["missing"] for o in F.open_items(est)} == {"price", "rate", "quantity"}

# with his prices: only his figures go in, a sub bid stays blank, and "check these first" is ranked by dollars
priced_decisions = changed(r16={"scope": "in", "reason": "Material lines above are in"})
priced_decisions["cover"]["range"] = {"low": 9000, "high": 11000, "basis": "made up"}
est, problems, _ = build(priced_decisions, PRICES)
assert problems == [] and F.check(est) == [], problems
L = {ln["row"]: ln for ln in est["lines"] if ln["row"]}
assert L[12]["material"] == 4.5 and L[12]["cost"] == 342 and L[12]["price_source"]["date"] == "2022-06-01"
assert L[20].get("ml") is None and L[20]["last_known"]["ml"] == 16500 and L[20]["cost"] == 0
assert L[13]["confidence"] == {"line": "high", "qty": "high", "price": "high", "reason": "Counted on plan and elevations"}
assert L[6]["confidence"]["reason"].endswith("No price of his for this line.") and L[6]["confidence"]["price"] == "low"
assert L[16]["cost"] == F.money(0.089 * (342 + 8100)) and est["totals"]["total"] == F.money(1.25 * est["totals"]["cost"])
assert [c["line"] for c in est["cover"]["check_first"]] == ["L0016", "L0012"]  # 751.34 x 0.5 outranks 342 x 1.0; markup is left out
refused(DECISIONS, "needs a range", PRICES)

# decisions the writer refuses, so nothing wrong is written
refused(changed(r6={"scope": "in", "qty": 1, "source": {"type": "written"}}), "needs a reason")
refused(changed(r6={"scope": "in", "qty": 1, "reason": "x"}), "no source")
refused(changed(r6={"scope": "in", "qty": 1, "source": {"type": "calculated"}, "reason": "x"}), "state its rule")
refused(changed(r21={"scope": "out", "reason": "x"}), "Out line needs a confidence")
refused(changed(r21={"scope": "out", "confidence": "high", "qty": 2, "source": {"type": "written"}, "reason": "x"}), "carries no quantity")
refused(changed(r4={"scope": "in", "reason": "x"}), "heading takes no decision")
refused(changed(r99={"scope": "in", "reason": "x"}), "not on his line list")
refused(changed(r6={"scope": "maybe", "reason": "x"}), "scope must be")
refused(changed(r14={"scope": "in", "qty": 1, "source": {"type": "written"}, "reason": "x"}), "usual line is not confirmed")
d = copy.deepcopy(DECISIONS); d["cover"].pop("missing_pages"); refused(d, "cover.missing_pages")
d = copy.deepcopy(DECISIONS); d["job"]["job_type"] = "shed";  refused(d, "estimate.job_type")

# saving: the check runs first, and a listed name stops the write
est, problems, _ = build()
with tempfile.TemporaryDirectory() as folder:
    path = os.path.join(folder, "draft.json")
    assert F.save(est, path, {"permit": "[x]"}) == ["name not redacted: permit"] and not os.path.exists(path)
    broken = copy.deepcopy(est); broken["lines"][1]["qty"] = "one"
    assert F.save(broken, path) and not os.path.exists(path)
    assert F.save(est, path, {"nobody": "[x]"}) == [] and F.check(json.load(open(path))) == []

# the Nov 16 blind draft's flat layout (format name on top, bare lines below) is not a format file
flat = {"format": F.FORMAT_NAME, "format_version": "0.3", "job": "Job A", "status": "draft",
        "lines": [{"row": 4, "description": "Division 1", "scope": "out", "qty": None, "qty_source": "", "confidence": ""}]}
assert any("no estimate header block" in p for p in F.check(flat))
print("all draft writer tests pass")
