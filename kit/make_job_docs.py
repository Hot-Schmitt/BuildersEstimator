"""
Write the Job A reference documents from the data, so no figure is typed by hand:
  04  the builder's estimate, every line (from the imported estimate file)
  05  estimate against budget against actual (estimate file + his cost workbook)
  11  the builder's cost code list
Usage: python3 -I make_job_docs.py <jobA.json> <cost_workbook.json> <cost_codes.json> <out_dir>
"""
import json
import sys

est, wbk, code_list, out = json.load(open(sys.argv[1])), json.load(open(sys.argv[2])), json.load(open(sys.argv[3])), sys.argv[4]
T = est["totals"]
lines = est["lines"]
by_id = {ln["id"]: ln for ln in lines}
div_name = {d["number"]: d["name"] for d in est["divisions"]}
code_name = {c["code"]: c for c in code_list["codes"]}


def n0(x):
    return f"{round(x):,}"


def code_of(ln):
    return " / ".join(s["code"] for s in ln.get("cost_split") or []) or ln.get("cost_code", "")


def price(x):
    return "" if x is None else f"{x:,.2f}".rstrip("0").rstrip(".")


# ---------------------------------------------------------------- doc 04
priced = sum(1 for ln in lines if ln.get("cost"))
d = [f"""# 04 · The builder's estimate format and price list seed (Job A, 2022)

**What this is:** every line of the builder's own Excel estimate for Job A, in his order and wording. It is the starting point for the price list and the layout every estimate must follow.
**Source:** the builder's estimate workbook dated June 1, 2022. This document is written by script from the imported estimate file (doc 10), whose totals equal his sheet's own total cells to the cent (Checked, Nov 16, 2026). It replaces the first version, whose totals left out his tax and contingency rows (doc 07, section 8). Client, address, vendor and sub names removed.
**Prices are 2022 prices.** Do not use them for a current estimate without the builder's update (see doc 06).

## How his sheet works (Checked)
- Columns: Description · Qty · Unit · Material per unit · Labor per unit · M&L per unit (a combined price, usually a sub's price) · Estimated cost.
- Cost of a line = Qty × (Material + Labor + M&L).
- Lines are grouped in numbered divisions (old 16-division style; he skips 11 and 13), plus an appliances block with no number. Division names below are **Inferred** from the lines; his sheet only numbers them.
- **Tax and contingency are their own rows inside a block.** The Qty cell holds the rate and the row sits on the material lines above it: 8.9% tax on framing, siding and cabinet material; 20% contingency on framing material; 33% contingency on siding material plus its tax.
- One line at the bottom adds overhead and profit: exactly 25% of cost.
- **{len(lines) - 1} rows, {priced - 1} of them priced on this job.** The rest are a standing checklist he carries from job to job. A blank line still has meaning: it is something he considered and left out.
- Units he uses: LS (lump sum), EA, SF, LF, SQ (roofing square), CY, DAY, HRS, MO.
- Side maths (rebar runs, slab area) sits in far-right columns of his sheet, not shown here.
- Some lines hold a unit price but no quantity. That is his remembered price, kept for next time.
- One row (Install cabinets, 2 days at 350) has a quantity and a price but shows no cost in his sheet. His cost workbook budgets it at 700.

## Totals on this estimate (Checked against his sheet's total cells)
| | Amount |
|---|---|
| Cost of all lines | {T['cost']:,.2f} |
| Overhead and profit at 25% | {T['markups'][0]['amount']:,.2f} |
| Estimate total | {T['total']:,.2f} |

| Division | Cost |
|---|---|"""]
for num, name in div_name.items():
    d.append(f"| {num} {name} | {n0(T['by_division'].get(str(num), 0))} |")
d.append(f"| **Total** | **{n0(T['cost'])}** |")
d.append(f"""
## Cost by trade as he billed it (pay application sheet, Checked)
Cost × 1.25 = price. Contract alternates added on top.

| Trade line | Cost | Alternates added |
|---|---|---|
| General conditions | 10,325 | |
| Demo house / driveway | 6,400 | |
| Grading / underground / French drain | 5,200 | |
| Fence | 2,500 | |
| Concrete slab / sidewalks | 16,571 | |
| Permeable pavers / concrete apron | 15,689 | |
| Steel garage header | 1,400 | |
| Framing | 44,719 | −2,000 |
| Interior trim | 2,300 | |
| Insulation | 2,000 | 1,350 |
| Roofing / skylights | 5,750 | 1,100 |
| Siding / cornice | 22,466 | 1,500 |
| Screen system | 1,425 | |
| Gutters | 1,254 | |
| Interior doors / hardware | 2,980 | 150 |
| Exterior doors | 1,700 | |
| Windows | 10,672 | |
| Garage doors | 2,775 | |
| Drywall | 6,800 | |
| Tile | 2,376 | |
| Flooring | 3,138 | |
| Paint | 12,000 | 5,300 |
| Cabinetry | 3,673 | 4,422 |
| Countertops | 1,800 | |
| HVAC | 7,035 | |
| Plumbing labor | 8,000 | |
| Plumbing fixtures | 3,500 | |
| Sewer pump | 11,000 | |
| Electrical | 16,500 | 300 |
| **Total** | **231,947** | → contract **302,056** |

Note (Checked): the pay application cost (231,947) is {n0(231947 - T['cost'])} above the June 1 estimate sheet ({n0(T['cost'])}). The cabinet install his sheet did not count (700) is the whole difference.

## Contract alternates he priced separately (Checked)
Stair screen · paint existing house (5,300) · car charging outlet (300) · two venting skylights (1,100) · kitchen cabinets · pantry and wall cabinet · pocket door (150) · 4\" filter (450) · I-joists instead of truss joists (−2,000) · foam attic (1,350) · ceiling registers. Small alternates carry their own 10–20% markup line.

## All lines, by division
"Row" is the row in his sheet. Rows with no cost are checklist lines he did not use on this job. "Code" is his cost code where the row has been matched to his cost workbook (doc 11).
""")
for num, name in div_name.items():
    d.append(f"### Division {num} — {name}\n" if num != 17 else "### Appliances (no division number)\n")
    d.append("| Row | Description | Qty | Unit | Matl/unit | Labor/unit | M&L/unit | Est. cost | Code |\n|---|---|---|---|---|---|---|---|---|")
    for ln in lines:
        if ln["division"] != num:
            continue
        if ln["kind"] == "heading":
            d.append(f"| {ln['row']} | **{ln['description']}** | | | | | | | |")
        elif ln["kind"] == "percent":
            base = sum(by_id[b].get("cost", 0) for b in ln["base"])
            d.append(f"| {ln['row']} | {ln['description']} | {ln['rate'] * 100:g}% | | on {n0(base)} | | | {n0(ln['cost'])} | {code_of(ln)} |")
        else:
            d.append(f"| {ln['row']} | {ln['description'] or '(no wording)'} | {price(ln['qty'])} | {ln['unit_as_written'] or ''} | {price(ln['material'])} | {price(ln['labor'])} | {price(ln['ml'])} | {n0(ln['cost'])} | {code_of(ln)} |")
    d.append(f"| | **Subtotal** | | | | | | **{n0(T['by_division'].get(str(num), 0))}** | |\n")
open(f"{out}/04.md", "w").write("\n".join(d))

# ---------------------------------------------------------------- doc 05
LABEL = {"labor": "Labor", "material": "Material", "subcontract": "Sub"}
wdiv = {}
for c in wbk:
    w = wdiv.setdefault(c["division"], {"budget": 0, "adjusted": 0, "paid": 0})
    for t in c["types"]:
        for k in w:
            w[k] += t[k]
tot = {k: sum(w[k] for w in wdiv.values()) for k in ("budget", "adjusted", "paid")}
names18 = {**div_name, 18: "Miscellaneous (no budget)"}


def pct(actual, est_cost):
    return f"{(actual / est_cost - 1) * 100:+.0f}%" if est_cost else ""


rows = []
for num in sorted(wdiv):
    e = T["by_division"].get(str(num), 0)
    w = wdiv[num]
    rows.append(f"| {num} {names18[num]} | {n0(e)} | {n0(w['budget'])} | {n0(w['adjusted'])} | {n0(w['paid'])} | {pct(w['paid'], e)} |")
# The notes below quote these figures; fail loudly if the data ever disagrees with the words.
chk = {n: pct(wdiv[n]["paid"], T["by_division"][str(n)]) for n in (1, 2, 6, 7, 9, 12)}
assert chk == {1: "-54%", 2: "+32%", 6: "-17%", 7: "+21%", 9: "+17%", 12: "+45%"}, chk
assert pct(tot["paid"], T["cost"]) == "+5%" and n0(tot["adjusted"]) == "257,473" and n0(tot["paid"]) == "243,633"
assert n0(tot["budget"]) == "231,747" and n0(T["cost"]) == "231,247"

f = [f"""# 05 · Job A: what was built, what it cost, and the test target

**What this is:** the one finished job we have with plans, the builder's estimate and the real costs. It is the first test for the estimator.
**Sources:** the builder's job-cost workbook, his estimate sheet and the stamped plan set. The tables are written by script from the files (Checked, Nov 16, 2026). This replaces the first version, which understated his estimate by leaving out his tax and contingency rows and missed the workbook's Sub lines (doc 07, section 8). Client, address, vendor and sub names removed.

## The job (Checked, from the plan cover sheet)
- **Scope as written on the plans:** rear addition to an existing house; convert the rear patio to a sunroom and screen porch; build a covered walkway and a two-car garage with a guest house above; new fences and a driveway extension.
- **Areas on the plans:** garage 566 sf · guest house 576 sf · stairs 53 sf · accessory structure total 1,195 sf. Sunroom addition 123 sf. Existing house 3,103 sf (not rebuilt).
- Two stories, 19.9 ft high, wood frame. City of Atlanta permit, 2022. Stormwater handled with permeable pavers.
- So this is a **mixed job**: mostly a new small building (garage with living space above), plus a small renovation and site work at the main house.

## The plan set (Checked by viewing every page)
14 pages, 24×36 in. Pages 1, 4, 6: site plan (three versions) · 2–3: city permeable-paver sheets · 5: cover sheet with codes, scope, area table and drawing index · 7: floor plans · 8: foundation and roof plans · 9–10: elevations · 11: sections and details · 12: roof framing plan · 13–14: lumber supplier's engineered-wood layouts with a joist and stud list.
- **The architect's sheets have no text layer.** Every number has to be read from a picture of the page.
- Only the city pages and the lumber supplier's pages have real text. The lumber pages are 2 of 4 sheets, carry another job's title block and a 2020 date, and are marked "not released": treat them as Medium at best.
- **The cover sheet shows the owners' names and phone number.** Keep the PDF out of anything shared.

## Money summary (Checked)
| | Amount |
|---|---|
| Contract price | 302,055 |
| Seven change orders | 15,553 |
| Contract plus change orders | 317,608 |
| Actual cost | {n0(tot['paid'])} |
| Profit | 73,975 (23.3%) |

Actual cost works out to about $204 per sf of the accessory structure, and the price to about $266 per sf (**Inferred**, 2022 dollars). These are rough: the totals include the sunroom, walkway, fence and driveway work.

## Estimate against budget against actual, by division
"June estimate" is his estimate sheet (doc 04). "Starting budget" is what his cost workbook carried before change orders. "Final budget" is after alternates and change orders. The last column compares actual to the June estimate.

| Division | June estimate | Starting budget | Final budget | Actual | Actual vs June estimate |
|---|---|---|---|---|---|
""" + "\n".join(rows) + f"""
| **Total** | **{n0(T['cost'])}** | **{n0(tot['budget'])}** | **{n0(tot['adjusted'])}** | **{n0(tot['paid'])}** | **{pct(tot['paid'], T['cost'])}** |

**How the estimate became the budget (Checked):** the workbook's starting budget is the estimate plus 700 for a cabinet install his sheet did not count, less 200 of door and window tape he did not budget. He also moved the screen porch (1,425) from division 7 to division 8. Code by code and type by type, the estimate rows add up to his budget on 38 of his 39 budgeted codes; the one that differs is kitchen cabinets, with the install.

What this shows (**Inferred**):
- Against his final budget he finished about 5% under. Against the June estimate, actual cost was about 5% higher, and scope added through alternates and change orders (25,726) is more than the whole gap. **Scope growth, not bad measuring, moved the number.**
- Biggest misses against the June estimate: cabinets (+45%), site work (+32%), roofing/siding/insulation (+21%), finishes (+17%). Concrete, doors and windows, plumbing, HVAC and electrical landed within about 8%.
- Framing came in 17% under. His estimate carried 20% contingency and tax on framing material, and material cost came in well below that budget.
- General conditions came in at less than half the estimate. Either he pads it or costs landed elsewhere (ask, doc 06).
- About 5,700 of cost sat in codes with no budget at all (divisions 17 and 18).

## Detail by cost code
Each cost code can carry three kinds of cost in his workbook: **Labor, Material and Sub**. Rows with no budget, change order or payment are left out. Payees are counted, not named.
"""]
for num in sorted(wdiv):
    f.append(f"### Division {num} — {names18[num]}\n\n| Code | Item | Type | Budget | CO | Adjusted | Paid | Gain/loss | Payments |\n|---|---|---|---|---|---|---|---|---|")
    for c in wbk:
        if c["division"] != num:
            continue
        for t in c["types"]:
            if t["budget"] or t["co"] or t["paid"]:
                pay = f"{t['payments']} to {t['payees']} payee{'s' if t['payees'] != 1 else ''}" if t["payments"] else ""
                f.append(f"| {c['code']} | {code_name[c['code']]['name']} | {LABEL[t['type']]} | {n0(t['budget'])} | {n0(t['co'])} | {n0(t['adjusted'])} | {n0(t['paid'])} | {n0(t['adjusted'] - t['paid'])} | {pay} |")
    f.append("")
open(f"{out}/05.md", "w").write("\n".join(f))

# ---------------------------------------------------------------- doc 11
used = {c["code"] for c in wbk if any(t["budget"] or t["co"] or t["paid"] for t in c["types"])}
g = [f"""# 11 · The builder's cost code list

**Purpose:** the one list of the builder's cost codes. The estimate format (doc 10), the cost code picker and the operations app all use it. He can add, rename, re-categorise or retire a code; nothing is deleted.
**Source:** read by script from his Job A cost workbook (Checked, Nov 16, 2026): {len(wbk)} codes, {len(used)} of them used on Job A. Categories start as his divisions (names **Inferred**). Two code names that were store names are replaced. Whether this is his standing list for every job is his to say (doc 06, question 27).

## How he files cost (Checked on Job A)
- His workbook keeps three kinds of cost under each code: **Labor, Material and Sub**. That matches the three types in doc 10.
- He files by who does the work, not by which column of his estimate the price sat in. Examples: framing labor (12,000, his Labor column) is budgeted as Sub; tile labor (1,620) is Sub; a plumbing sink priced in his Labor column is Material; concrete slab materials and labor (15,471) are all Sub.
- So each line carries its own filing choice for every price column, remembered for the next job (format version 0.3, approved by the user Nov 16).
- One estimate line can feed two codes: his paint line (12,000) is budgeted half to interior paint and half to exterior paint. The user's reading (Said, Nov 16): his sub most likely quoted the whole house, and he halved it so each code had a figure. Version 0.3 lets a line split across codes.
- With his filing recorded for Job A, the format's budget by code and type equals his workbook's on every code but one: kitchen cabinets, where his workbook adds a 700 install his sheet did not count.

## The list
| Code | Name | Category | Used on Job A |
|---|---|---|---|"""]
for c in code_list["codes"]:
    g.append(f"| {c['code']} | {c['name']} | {c['category']} | {'yes' if c['code'] in used else ''} |")
open(f"{out}/11.md", "w").write("\n".join(g) + "\n")
print("docs written")
