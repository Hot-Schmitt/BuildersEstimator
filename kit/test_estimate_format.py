"""
Tests for the shared estimate format.
Usage: python3 -I test_estimate_format.py [jobA.json]
With no file the tests run on a small made-up estimate built below (no real data).
With the Job A import they run on his real sheet, plus the checks against his cost workbook.
Each test changes a copy of a sound file and says what the check must do with it.
"""
import copy
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import estimate_format as F  # noqa: E402


def made_up():
    """A small sound estimate with the same line names the tests use on Job A. Every figure is invented."""
    def item(i, division, description, qty, unit, code=None, **prices):
        ln = {"id": i, "row": int(i[1:]), "division": division, "group": None, "description": description,
              "kind": "item", "scope": "in", "qty": qty, "unit": unit, "unit_as_written": unit, **prices}
        if qty is not None:
            ln["qty_source"] = {"type": "his_entry"}
        if code:
            ln["cost_code"] = code
        return ln

    def heading(i, division, description):
        return {"id": i, "row": int(i[1:]), "division": division, "group": None,
                "description": description, "kind": "heading"}

    paint = item("L0441", 9, "Paint-interior and exterior", 1, "LS", ml=12000)
    paint["cost_split"] = [{"code": "9910", "share": 0.5}, {"code": "9920", "share": 0.5}]
    unused = item("L0149", 6, "2x4x8", None, "EA", "6080", material=4.5)
    unused["scope"] = "out"
    lines = [
        heading("L0004", 1, "Division 1"),
        item("L0006", 1, "Permit", 1, "LS", "1100", ml=1450),
        heading("L0047", 3, "Division 3"),
        item("L0057", 3, "2 days labor", 2, "DAY", "3420", labor=300),
        item("L0070", 3, "Concrete - slab", 25, "CY", "3420", ml=195),
        heading("L0124", 6, "Division 6"),
        item("L0148", 6, "2x6x16PT", 10, "EA", "6080", material=20.335),
        unused,
        {"id": "L0204", "row": 204, "division": 6, "group": None, "description": "TAX", "kind": "percent",
         "percent_role": "tax", "rate": 0.089, "base": ["L0148"], "scope": "in", "cost_type": "material",
         "cost_code": "6080"},
        {"id": "L0205", "row": 205, "division": 6, "group": None, "description": "Contingency",
         "kind": "percent", "percent_role": "contingency", "rate": 0.2, "base": ["L0148", "L0204"],
         "scope": "in", "cost_type": "material", "cost_code": "6080"},
        paint,
        item("L0569", 16, "Bid - electrical sub", 1, "LS", "16100", ml=16500),
        {"id": "L0599", "row": 599, "division": None, "group": None, "description": "OH&P", "kind": "percent",
         "percent_role": "markup", "rate": 0.25, "base": F.ALL_COST, "scope": "in"},
    ]
    est = {
        "format": F.FORMAT_NAME, "format_version": F.FORMAT_VERSION,
        "estimate": {"id": "made-up-1", "job": "Made-up job", "job_type": "mixed", "parts": ["adu", "renovation"],
                     "definition_level": "permit_plans", "status": "final", "version": 1, "parent_version": None,
                     "made_by": "import", "made_at": "2026-11-16T12:00:00-05:00", "price_basis": "2022-06-01",
                     "currency": "USD", "note": "Made-up test estimate."},
        "divisions": [{"number": n, "name": f"Division {n}", "name_source": "Inferred"} for n in (1, 3, 6, 9, 16)],
        "cost_codes": [{"code": c, "name": c, "category": "x"} for c in ("1100", "3420", "6080", "9910", "9920", "16100")],
        "groups": [], "lines": lines, "changes": [],
    }
    assert F.structure(est) == [], F.structure(est)
    return F.fill_totals(est)


EST = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else made_up()
ON_JOB_A = str(EST["estimate"]["id"]).startswith("jobA")


def line(est, description):
    return next(ln for ln in est["lines"] if ln["description"] == description)


def caught(est, words):
    problems = F.check(est)
    assert any(words in p for p in problems), (words, problems[:3])


def fresh():
    return copy.deepcopy(EST)


assert F.check(EST) == [], F.check(EST)

# --- edits that must pass
e = fresh(); ln = line(e, "Concrete - slab")
e["changes"].append({"line": ln["id"], "field": "qty", "from": ln["qty"], "to": 22, "by": "builder",
                     "at": "2026-11-16T12:00:00-05:00", "reason": "less waste", "kind": "quantity"})
ln["qty"] = 22
assert F.check(F.fill_totals(e)) == []
assert F.money(e["totals"]["total"] - EST["totals"]["total"]) == -731.25  # 3 CY x 195 x 1.25

e = fresh()  # a new 10,000 line carries his markup: total moves by 12,500
e["lines"].insert(5, {"id": "N1", "row": None, "division": 1, "group": None, "description": "Added line",
                      "kind": "item", "scope": "new", "qty": 1, "unit": "LS", "ml": 10000,
                      "qty_source": {"type": "his_entry"}})
assert F.check(F.fill_totals(e)) == [] and F.money(e["totals"]["total"] - EST["totals"]["total"]) == 12500

e = fresh()  # he re-files a sub's bid as labor: the budget moves type, the total does not
assert EST["totals"]["by_code"]["16100"]["subcontract"] == 16500
line(e, "Bid - electrical sub")["filed_as"] = {"ml": "labor"}
assert F.check(F.fill_totals(e)) == [] and e["totals"]["by_code"]["16100"]["labor"] == 16500
assert e["totals"]["total"] == EST["totals"]["total"]

e = fresh()  # an uneven three-way split still adds up to the line's cost
ln = line(e, "Bid - electrical sub"); ln.pop("cost_code")
ln["cost_split"] = [{"code": c, "share": 1 / 3} for c in ("16100", "9910", "9920")]
assert F.check(F.fill_totals(e)) == []

e = fresh()  # many lines that each round: budget by code still adds up to cost
for n in range(40):
    e["lines"].insert(5, {"id": f"R{n}", "row": None, "division": 1, "group": None, "description": "r",
                          "kind": "item", "scope": "new", "qty": 3, "unit": "EA", "material": 0.335,
                          "labor": 0.335, "qty_source": {"type": "his_entry"}})
assert F.check(F.fill_totals(e)) == []

e = fresh()  # signed, with a proper signature block
e["estimate"]["status"] = "signed"
e["signed"] = {"by": "client", "at": "2026-11-16T12:00:00-05:00", "total": e["totals"]["total"]}
assert F.check(e) == []

# --- version 0.4: blanks are allowed while the estimate is open, and never in a finished one
e = fresh(); e["estimate"]["status"] = "builder_editing"
line(e, "OH&P")["rate"] = None; line(e, "TAX")["rate"] = None; line(e, "Concrete - slab")["qty"] = None
line(e, "Concrete - slab").pop("qty_source")
assert F.check(F.fill_totals(e)) == [] and e["totals"]["markups"][0]["amount"] == 0
assert {(o["line"], o["missing"]) for o in F.open_items(e)} >= {
    (line(e, "OH&P")["id"], "rate"), (line(e, "TAX")["id"], "rate"), (line(e, "Concrete - slab")["id"], "quantity")}
e = fresh(); line(e, "OH&P")["rate"] = None;                      caught(e, "from 0 to 1")
e = fresh(); line(e, "Concrete - slab")["qty"] = None;            caught(e, "price but no quantity")
e = fresh(); line(e, "OH&P")["scope"] = "out";                    caught(e, "always in scope")
e = fresh(); e["estimate"]["parts"] = [];                         caught(e, "list its parts")

# --- budget by cost code and type equals his cost workbook's budgets (doc 05), to the dollar
if ON_JOB_A:
    BC = EST["totals"]["by_code"]
    for code, labor, material, sub in [("6080", 0, 32719, 12000), ("7410", 0, 9466, 13000), ("3420", 0, 0, 15471),
                                       ("15100", 0, 3500, 19000), ("9500", 0, 1956, 1182), ("1760", 1500, 0, 0),
                                       ("6500", 1500, 800, 0), ("8950", 0, 675, 750), ("9910", 0, 0, 6000),
                                       ("9920", 0, 0, 6000), ("1100", 0, 1450, 0), ("16100", 0, 0, 16500)]:
        got = BC[code]
        assert (round(got["labor"]), round(got["material"]), round(got["subcontract"])) == (labor, material, sub), (code, got)
    assert BC[F.UNCODED] == {"labor": 0.0, "material": 200.0, "subcontract": 0.0}

# --- bad files that must be caught, never crash
e = fresh(); e["totals"]["total"] += 100;                         caught(e, "stored total")
e = fresh(); e["totals"]["by_division"]["3"] += 1;                caught(e, "stored by_division")
e = fresh(); e["totals"]["markups"][0]["amount"] += 1;            caught(e, "stored markups")
e = fresh(); line(e, "Concrete - slab")["cost"] += 0.01;          caught(e, "stored cost")
e = fresh(); line(e, "Concrete - slab").pop("qty_source");        caught(e, "no source")
e = fresh(); line(e, "Concrete - slab")["qty"] = "25";            caught(e, "not a number")
e = fresh(); line(e, "Concrete - slab")["qty"] = -1;              caught(e, "below zero")
e = fresh(); line(e, "Concrete - slab")["unit"] = "cy";           caught(e, "not tidied")
e = fresh(); line(e, "Concrete - slab")["price_source"] = {"type": "x"}; caught(e, "price source")
e = fresh(); line(e, "Concrete - slab")["cost_code"] = "9999";    caught(e, "not in the estimate's code list")
e = fresh(); line(e, "Concrete - slab")["division"] = 99;         caught(e, "not in the division list")
e = fresh(); line(e, "OH&P")["base"] = ["L0008"];                 caught(e, "all cost")
e = fresh(); line(e, "OH&P")["rate"] = 25;                        caught(e, "from 0 to 1")
e = fresh(); line(e, "TAX").pop("rate");                          caught(e, "from 0 to 1")
e = fresh(); t = line(e, "TAX"); t["base"] = [t["id"]];           caught(e, "not found above")
e = fresh(); line(e, "TAX")["base"] = [line(e, "Contingency")["id"]]; caught(e, "not found above")
e = fresh(); line(e, "TAX").pop("cost_type");                     caught(e, "needs a cost type")
e = fresh(); e["estimate"]["status"] = "draft";                   caught(e, "without confidence")
e = fresh(); e["estimate"]["made_by"] = "estimator";              caught(e, "without confidence")
e = fresh(); line(e, "Concrete - slab")["confidence"] = {"line": "low", "reason": " "}; caught(e, "needs a reason")
e = fresh(); e["estimate"]["status"] = "signed";                  caught(e, "who signed")
e = fresh(); e["estimate"]["status"] = "signed"; e["signed"] = {"by": "c", "at": "now", "total": 1}; caught(e, "signed total")
e = fresh(); e["estimate"]["version"] = "one";                    caught(e, "whole number")
e = fresh(); e["changes"].append({"line": "L0070", "kind": "price"}); caught(e, "change entry missing")
e = fresh(); line(e, "Concrete - slab")["filed_as"] = {"ml": "equipment"}; caught(e, "filed_as")
e = fresh(); line(e, "Concrete - slab")["filed_as"] = {"qty": "labor"};    caught(e, "filed_as")
e = fresh(); line(e, "Paint-interior and exterior")["cost_split"][0]["share"] = 0.6; caught(e, "cost split")
e = fresh(); line(e, "Paint-interior and exterior")["cost_code"] = "9910"; caught(e, "cost split")
e = fresh(); line(e, "Paint-interior and exterior")["cost_split"][1]["code"] = "9999"; caught(e, "cost split")
e = fresh(); e.pop("lines");                                      caught(e, "no list of lines")

# --- the files that crashed the 0.3 check in the Nov 16 review: each must now be reported, not raised
e = fresh(); line(e, "Concrete - slab")["confidence"] = "low";    caught(e, "confidence must be a record")
e = fresh(); line(e, "Concrete - slab")["qty_source"] = "counted"; caught(e, "no source")
e = fresh(); e["lines"][1] = None;                                caught(e, "is not a record")
e = fresh(); e["cost_codes"] = None;                              caught(e, "cost_codes must be a list")
e = fresh(); line(e, "Concrete - slab")["cost"] = "4875";         caught(e, "stored cost is not a number")
e = fresh(); line(e, "Concrete - slab")["qty"] = float("nan");    caught(e, "not a number")
e = fresh(); e["estimate"] = "draft";                             caught(e, "no estimate header block")
e = fresh(); line(e, "TAX")["base"] = [line(e, "OH&P")["id"]];    caught(e, "not found above")
e = fresh(); e["lines"][1]["id"] = ["L1"];                        caught(e, "missing or duplicate line id")

# --- no bad file can crash it: put every kind of wrong value in every place, and take every field away
JUNK = (None, "x", "", 7, -1, 1.5, True, [], {}, [None], ["x"], {"type": "x"}, float("nan"), float("inf"))


def places(node, path=()):
    """Every place in the file, as a path of keys and positions."""
    if isinstance(node, dict):
        for k, v in node.items():
            yield path + (k,)
            yield from places(v, path + (k,))
    elif isinstance(node, list):
        for k, v in enumerate(node):
            yield path + (k,)
            yield from places(v, path + (k,))


SMALL = EST if not ON_JOB_A else made_up()  # the sweep runs on the small file to keep it quick
tried = rejected = 0
for path in list(places(SMALL)):
    for junk in JUNK + ("<removed>",):
        e = copy.deepcopy(SMALL)
        node = e
        for k in path[:-1]:
            node = node[k]
        if junk == "<removed>":
            del node[path[-1]]
        else:
            node[path[-1]] = junk
        problems = F.check(e)  # must return, whatever the file holds
        assert isinstance(problems, list), path
        assert not any("could not finish" in x for x in problems), (path, junk, problems)  # the guard is never needed
        tried += 1
        rejected += bool(problems)
assert F.check(None) and F.check([]) and F.check({"lines": [None]})

assert F.money(117.925) == 117.93 and F.money(0.089 * 1325) == 117.93  # halves round up, as in his sheet
print(f"all tests pass ({'Job A' if ON_JOB_A else 'made-up estimate'}; {tried} damaged files tried, "
      f"none crashed the check, {rejected} rejected)")

# Change log
# Nov 16, 2026 · Runs without real data on a made-up estimate (the Job A file is optional). Added the 0.4 rules,
#   the nine files that crashed the 0.3 check, and a sweep that damages every place in a file. Uses F.fill_totals.
