"""
Score a draft in the shared format against his estimate sheet. Opens his answers: never run during a blind draft.

Reports, in this order (review rule: blind and measured first, lump sums apart):
scope by line and by his dollars; how many of his priced lines carry a number; quantities within 10%
(measured, plan minimum, lump sums; first-draft blind rows apart); marks; dollars at his prices.

Usage: python3 -I score.py <estimate.xlsx> <draft.json> <decisions.json>
  decisions.json gives "seen_before" (rows whose answer was visible before the draft) and the overlap groups.
"""
import json
import sys

import openpyxl

ws = openpyxl.load_workbook(sys.argv[1]).worksheets[0]
draft = json.load(open(sys.argv[2]))
dec = json.load(open(sys.argv[3]))
seen = set(dec.get("seen_before") or [])
usual = {g["usual_row"]: g["rows"] for g in dec.get("overlaps") or [] if g.get("usual_row")}
grouped = {r for g in dec.get("overlaps") or [] for r in g["rows"]}


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


his = {}  # row -> (qty, unit price, cost): the rows he priced, read the same way as the first score
for r in range(3, 598):
    q = num(ws.cell(r, 2).value)
    p = sum(num(ws.cell(r, c).value) or 0 for c in (4, 5, 6))
    if q and q > 0 and p > 0:
        his[r] = (q, p, q * p)
L = {ln["row"]: ln for ln in draft["lines"] if ln.get("row")}
NO_RULE = "No rule for this line yet"


def bucket(r):
    ln = L.get(r)
    if ln is None:
        return "not on the line list"
    if ln["kind"] == "heading":
        return "heading"
    if ln["scope"] == "ask":
        if r in usual:
            return "ask, on his usual line"
        if r in grouped:
            return "ask, in a group"
        return "ask, no rule" if ln["confidence"]["reason"].startswith(NO_RULE) else "ask, with a reason"
    return ln["scope"]


total = sum(v[2] for v in his.values())
print(f"He priced {len(his)} lines, {total:,.0f}")
cats = {}
for r in his:
    cats.setdefault(bucket(r), []).append(r)
for k in sorted(cats):
    rows = cats[k]
    print(f"  {k:24} {len(rows):3} lines ({len(rows)/len(his):.0%})  {sum(his[r][2] for r in rows):>10,.0f} ({sum(his[r][2] for r in rows)/total:.0%})")
for k in ("ask, no rule", "out", "heading"):
    for r in sorted(cats.get(k, []), key=lambda r: -his[r][2])[:20]:
        print(f"     {k}: row {r} {L[r]['description'][:36]:36} {his[r][2]:>9,.0f}")
ours_in = [r for r, ln in L.items() if ln["kind"] not in ("heading", "percent") and ln["scope"] == "in"]
print(f"Our In lines: {len(ours_in)}; he did not price {sum(1 for r in ours_in if r not in his)}")
carry = [r for r in his if L[r]["kind"] != "heading" and L[r].get("qty") is not None]
print(f"His priced lines where the draft carries a number: {len(carry)} ({len(carry)/len(his):.0%}); "
      f"In with a number: {sum(1 for r in carry if L[r]['scope'] == 'in')}")
blank_in = [r for r in ours_in if L[r].get("qty") is None]
print(f"In lines left blank: {len(blank_in)}, of which he priced {sum(1 for r in blank_in if r in his)}")
in_his = [r for r in his if L[r]["kind"] != "heading" and L[r]["scope"] == "in"]
print(f"Of his priced lines we marked In: {len(in_his)}; with a number {sum(1 for r in in_his if L[r].get('qty') is not None)}, blank {sum(1 for r in in_his if L[r].get('qty') is None)}")

rows = []
for r in carry:
    ln = L[r]
    src = ln["qty_source"]["type"]
    lump = (ln.get("unit") or "") == "LS" or src == "assumed"
    rows.append({"r": r, "ln": ln, "d": (ln["qty"] - his[r][0]) / his[r][0], "lump": lump, "src": src,
                 "pm": ln["confidence"]["reason"].startswith("Plan minimum"), "trivial": ln["qty"] == 1 and his[r][0] == 1})


def show(name, sel):
    ok = sum(1 for x in sel if abs(x["d"]) <= 0.10)
    print(f"  {name:46} {ok:3} of {len(sel):3}" + (f" ({ok/len(sel):.0%})" if sel else ""))
    return sel


print("\nQuantities within 10% (lines where both have a number)")
meas = [x for x in rows if not x["lump"]]
show("HEADLINE: measured, not seen before", [x for x in meas if x["r"] not in seen])
show("measured, all", meas)
show("measured, without 1 = 1 counts", [x for x in meas if not x["trivial"]])
show("measured, seen before", [x for x in meas if x["r"] in seen])
show("lump sums and assumed (match almost by design)", [x for x in rows if x["lump"]])
show("plan minimum lines", [x for x in meas if x["pm"]])
show("measured, not plan minimum", [x for x in meas if not x["pm"]])
show("calculated, not seen before", [x for x in meas if x["src"] == "calculated" and x["r"] not in seen])
print("By line mark (measured)")
for m in ("high", "medium", "low"):
    show(f"marked {m}", [x for x in meas if x["ln"]["confidence"]["line"] == m])
print("By quantity mark (measured)")
for m in ("high", "medium", "low"):
    show(f"quantity {m}", [x for x in meas if x["ln"]["confidence"]["qty"] == m])
marks = {}
for ln in draft["lines"]:
    if ln["kind"] not in ("heading",) and ln.get("scope") in ("in", "ask"):
        marks[ln["confidence"]["line"]] = marks.get(ln["confidence"]["line"], 0) + 1
print("Line marks on In and Ask lines:", marks)
high = [ln for ln in draft["lines"] if ln["kind"] != "heading" and ln.get("scope") == "in" and ln["confidence"]["line"] == "high"]
print(f"High In lines: {len(high)}; he priced {sum(1 for ln in high if ln['row'] in his)}; seen before {sum(1 for ln in high if ln['row'] in seen)}")


def dollars(name, sel):
    ours = sum(x["ln"]["qty"] * his[x["r"]][1] for x in sel)
    theirs = sum(his[x["r"]][2] for x in sel)
    print(f"  {name:46} ours {ours:>10,.0f} his {theirs:>10,.0f} ({ours/theirs-1:+.1%})" if theirs else f"  {name}: none")


print("\nDollars at his prices")
dollars("HEADLINE: measured, not seen before", [x for x in meas if x["r"] not in seen])
dollars("measured", meas)
dollars("all lines with a number (lump sums dilute this)", rows)
dollars("plan minimum lines", [x for x in meas if x["pm"]])
print("\nMeasured lines off by more than 10%:", sum(1 for x in meas if abs(x["d"]) > 0.10))
for x in sorted(meas, key=lambda x: -abs(x["d"] * his[x["r"]][2]))[:14]:
    if abs(x["d"]) > 0.10:
        print(f"   {x['r']} {x['ln']['description'][:28]:28} ours {x['ln']['qty']:g} his {his[x['r']][0]:g} {x['d']:+.0%} {x['ln']['confidence']['line']}")


# Change log
# Nov 16, 2026 · Rewritten for drafts in the shared format (0.4); the old version read the flat Nov 16 draft,
#   which it can no longer score (those scores are kept in doc 12). Reads his priced rows the same way as before.
#   New: Ask lines split by why they are Ask; his priced lines that carry a number; plan-minimum lines and
#   1 = 1 counts scored apart; results by line mark and by quantity mark; dollars on measured lines first.
# Nov 16, 2026 (after the fresh review) · Output order changed so the unseen measured lines lead, in counts and in
#   dollars, and the lump sums come last. Added: how many of his priced In lines are blank.
