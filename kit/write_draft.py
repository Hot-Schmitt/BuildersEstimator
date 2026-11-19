"""
The one draft writer. Every draft estimate is built here, through the shared format
(estimate_format), and is checked before it is written. A file that is not in the
format, or that still holds a listed name, cannot be produced.

Judgement stays outside this script, in the decisions file Claude writes for a job
(which lines apply, each quantity and where it came from, the reasons). This script
applies the fixed rules of "03 Method" to those decisions, the same way every time:
  - a line with no decision is Ask, never Out; nothing is dropped or added silently
  - his headings stay headings; his total rows are replaced by the totals block
  - every In, Out and Ask carries a reason; every quantity carries its source
  - the mark on a line is never higher than the Method allows (step 7): a proposed
    mark above the rule is lowered and reported
  - overlapping lines stay one Ask question until he confirms his usual line
  - sub bids and client choices stay blank, with the last known figure beside them
  - only his prices and his rates go in; a blank is a correct answer

Usage:
  python3 -I write_draft.py --lines his_lines.json --decisions decisions.json --codes cost_codes.json
        --names names.json --made-at 2026-11-16T15:00:00-05:00 --out draft.json
        [--code-rows code_rows.json] [--prices prices.json]

  his_lines.json   his line list, from checklist.py
  decisions.json   this job, written by Claude:
     {"job":   {"id", "job", "job_type", "parts", "definition_level", "note"},
      "cover": {"missing_pages": [...], "assumptions": [...], "exclusions": [...], "range": null or {"low", "high", "basis"}},
      "lines": {"<row>": {"scope": "in|out|ask", "reason": "...",
                          "qty": 12, "source": {"type": "counted", "page": "A-1", "rule": "..."},
                          "cross_checked": true, "plan_minimum": false, "confidence": "medium",
                          "kind": "sub_bid|allowance|client_choice", "flags": [...], "last_known": {...}}},
      "overlaps":  [{"rows": [260, 265], "question": "...", "usual_row": 265, "confirmed": false}],
      "new_lines": [{"description": "...", "division": 12, "why": "..."}]}
  code_rows.json   his usual cost code, filing and splits by row (optional)
  prices.json      his prices and rates by row, from his price list (optional; without it the draft carries no prices):
     {"date": "2022-06-01", "job": "Job A",
      "lines": {"<row>": {"material": 1.5, "labor": null, "ml": null, "type": "his_price", "mark": "medium", "reason": "..."}},
      "rates": {"<row>": {"rate": 0.089, "mark": "medium", "reason": "..."}}}
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import estimate_format as F  # noqa: E402
import redaction  # noqa: E402

ORDER = {"low": 0, "medium": 1, "high": 2}
# "03 Method" step 7, quantity mark by where the quantity came from.
QUANTITY_RULE = {"written": "high", "counted": "medium", "dimensions": "medium", "calculated": "medium",
                 "assumed": "low", "his_entry": "high"}
DRAFT_KINDS = {"item", "sub_bid", "allowance", "client_choice"}
BLANK_PRICE_KINDS = {"sub_bid", "client_choice"}  # the price cell stays blank; last known figure sits beside it
FLAGS = {"plans_vs_estimate", "engineering", "hidden_condition"}
NO_RULE = "No rule for this line yet. His call whether it applies."
NO_RATE = "His rate for this line is not set on this draft."
# Proposed settings (the user can change them): how doubt weighs dollars in "check these first", and its length.
DOUBT = {"low": 1.0, "medium": 0.5}
CHECK_FIRST_LINES = 10


def lowest(*marks):
    marks = [m for m in marks if m]
    return min(marks, key=ORDER.get) if marks else None


def text(v):
    return isinstance(v, str) and v.strip() != ""


def decided_line(row, d, kinds, problems):
    """Test one decision against the Method's rules before it is used. Returns True when it is sound."""
    before = len(problems)
    if not isinstance(d, dict):
        problems.append(f"row {row}: decision is not a record")
        return False
    if d.get("scope") not in ("in", "out", "ask"):
        problems.append(f"row {row}: scope must be in, out or ask")
    if not text(d.get("reason")):
        problems.append(f"row {row}: every In, Out and Ask needs a reason")
    if kinds.get(row) == "heading":
        problems.append(f"row {row}: a heading takes no decision")
    if d.get("kind") is not None and d["kind"] not in DRAFT_KINDS:
        problems.append(f"row {row}: kind {d['kind']!r} not allowed on a draft line")
    if d.get("confidence") is not None and d["confidence"] not in F.CONFIDENCE:
        problems.append(f"row {row}: confidence {d['confidence']!r}")
    if d.get("scope") == "out" and d.get("confidence") not in F.CONFIDENCE:
        problems.append(f"row {row}: an Out line needs a confidence word (how sure it does not apply)")
    if not set(d.get("flags") or []) <= FLAGS:
        problems.append(f"row {row}: flags must come from {sorted(FLAGS)}")
    if d.get("qty") is not None:
        src = d.get("source")
        if d.get("scope") == "out":
            problems.append(f"row {row}: an Out line carries no quantity")
        if not (isinstance(src, dict) and src.get("type") in F.QTY_SOURCES):
            problems.append(f"row {row}: quantity has no source")
        elif src["type"] in ("calculated", "assumed") and not text(src.get("rule")):
            problems.append(f"row {row}: a calculated or assumed quantity must state its rule")
    return len(problems) == before


def quantity_mark(d):
    """Step 7 quantity mark. A blank quantity is Low: nothing is known yet."""
    if d.get("qty") is None:
        return "low"
    kind = d["source"]["type"]
    if d.get("plan_minimum"):
        return "low"  # bare plan count; his ordering rule is not recorded
    if kind == "counted" and d.get("cross_checked"):
        return "high"
    return QUANTITY_RULE[kind]


def build(his, decisions, code_file, made_at, code_rows=None, prices=None):
    """Turn his line list and one job's decisions into an estimate in the shared format.
    Returns (estimate, problems, notes). With problems the estimate must not be written."""
    problems, notes = [], []
    code_rows = code_rows or {}
    job, cover = decisions.get("job") or {}, decisions.get("cover") or {}
    for key in ("missing_pages", "assumptions", "exclusions"):
        if not isinstance(cover.get(key), list):
            problems.append(f"cover.{key} must be a list (an empty list says there are none)")
    if prices is not None and not isinstance(cover.get("range"), dict):
        problems.append("a priced draft needs a range (cover.range), not just a total")

    rows = {ln["row"]: ln for ln in his["lines"]}
    kinds = {r: ln["kind"] for r, ln in rows.items()}
    decided = {}
    for key, d in (decisions.get("lines") or {}).items():
        row = int(key) if str(key).isdigit() else None
        if row not in rows:
            problems.append(f"decision for row {key}, which is not on his line list")
        elif decided_line(row, d, kinds, problems):
            decided[row] = d

    # Overlapping lines: one group, one question. No line in the group is In until he confirms his usual line.
    question_for = {}
    for g in decisions.get("overlaps") or []:
        members = g.get("rows") or []
        if len(members) < 2 or any(kinds.get(r) != "item" for r in members) or not text(g.get("question")):
            problems.append(f"overlap {members}: needs two or more of his lines and a question")
            continue
        chosen = [r for r in members if decided.get(r, {}).get("scope") == "in"]
        if chosen and not g.get("confirmed"):
            problems.append(f"overlap {members}: rows {chosen} are In, but his usual line is not confirmed. Mark the group Ask")
        if len(chosen) > 1:
            problems.append(f"overlap {members}: more than one line is In")
        for r in members:
            others = ", ".join(f"'{rows[x]['description']}'" for x in members if x != r)
            usual = g.get("usual_row")
            note = f" On {his.get('made_from', 'a past job')} he used '{rows[usual]['description']}'." if usual in rows else ""
            question_for[r] = f"{g['question'].strip()} Same work as: {others}.{note}"

    priced = (prices or {}).get("lines") or {}
    rates = (prices or {}).get("rates") or {}
    when = {"date": (prices or {}).get("date"), "job": (prices or {}).get("job")}
    ids = {r: f"L{r:04d}" for r in rows}
    lines = []
    for ln in his["lines"]:
        r, kind = ln["row"], ln["kind"]
        out = {"id": ids[r], "row": r, "division": ln["division"], "group": ln.get("group"),
               "description": ln["description"]}
        d = decided.get(r)
        if kind == "heading":
            out["kind"] = "heading"
        elif kind == "percent":
            markup = ln["percent_role"] == "markup"
            rate = rates.get(str(r))
            out.update(kind="percent", percent_role=ln["percent_role"], rate=rate["rate"] if rate else None,
                       base=F.ALL_COST if markup else [ids[x] for x in ln["base_rows"] if x in ids and x != r],
                       scope="in" if markup else (d or {}).get("scope", "ask"))
            if not markup:
                out["cost_type"] = "material"  # as on his sheet: his tax and contingency rows sit on material
            mark = lowest((d or {}).get("confidence"), rate.get("mark") if rate else "low",
                          "low" if out["scope"] == "ask" else None)
            why = [(d or {}).get("reason") or (None if markup or d else NO_RULE), rate.get("reason") if rate else NO_RATE]
            out["confidence"] = {"line": mark, "qty": None, "price": mark, "reason": " ".join(w.strip() for w in why if w)}
            if (d or {}).get("last_known"):
                out["last_known"] = d["last_known"]
        else:
            if d is None:  # no rule for this line: his call, never a silent Out
                d = {"scope": "ask", "reason": NO_RULE}
            line_kind = d.get("kind") or "item"
            out.update(kind=line_kind, scope=d["scope"], qty=d.get("qty"), unit=F.tidy_unit(ln.get("unit")),
                       unit_as_written=ln.get("unit"))
            why = ("Plan minimum: " if d.get("plan_minimum") and d.get("qty") is not None else "") + d["reason"].strip()
            if d.get("qty") is not None:
                src = d["source"]
                out["qty_source"] = {"type": src["type"], "page": src.get("page"), "rule": src.get("rule")}
            price, price_mark = priced.get(str(r)), None
            if prices is not None and d["scope"] != "out":
                if price and line_kind in BLANK_PRICE_KINDS:
                    out["last_known"] = {k: price.get(k) for k in F.PRICE_COLUMNS} | when
                    price_mark = "low"
                elif price:
                    out.update({k: price.get(k) for k in F.PRICE_COLUMNS})
                    out["price_source"] = {"type": price.get("type", "his_price")} | when
                    price_mark = price.get("mark")
                    if price_mark not in F.CONFIDENCE:
                        problems.append(f"row {r}: his price needs a mark from the price list")
                    if text(price.get("reason")):
                        why += " " + price["reason"].strip()
                else:
                    price_mark = "low"
                    why += " No price of his for this line."
            if d.get("last_known"):
                out["last_known"] = d["last_known"]
            if d.get("flags"):
                out["flags"] = sorted(d["flags"])
            if r in question_for and d["scope"] != "out":
                why += " " + question_for[r]
            if d["scope"] == "out":
                conf = {"line": d["confidence"], "qty": None, "price": None, "reason": why}
            else:
                qty_mark = quantity_mark(d)
                automatic = "low" if (d["scope"] == "ask" or line_kind != "item"
                                      or "hidden_condition" in (d.get("flags") or [])) else None
                ceiling = lowest(qty_mark, price_mark, automatic)
                mark = lowest(d.get("confidence"), ceiling)
                if d.get("confidence") and mark != d["confidence"]:
                    notes.append(f"row {r}: proposed {d['confidence']} lowered to {mark} (Method step 7)")
                conf = {"line": mark, "qty": qty_mark, "price": price_mark, "reason": why}
            out["confidence"] = conf
        if kind != "heading":
            filing = code_rows.get("filed_as", {}).get(str(r))
            if str(r) in code_rows.get("splits", {}):
                out["cost_split"] = code_rows["splits"][str(r)]
            elif code_rows.get("rows", {}).get(str(r)):
                out["cost_code"] = code_rows["rows"][str(r)]
            if filing and kind != "percent":
                out["filed_as"] = filing
        lines.append(out)

    # What the plans show that is not on his list: its own section, never slipped into his lines.
    markup_at = next((n for n, ln in enumerate(lines) if F.is_markup(ln)), len(lines))
    for n, new in enumerate(decisions.get("new_lines") or [], 1):
        if not (isinstance(new, dict) and text(new.get("description")) and text(new.get("why"))):
            problems.append(f"new line {n}: needs a description and a reason")
            continue
        add = {"id": f"N{n:03d}", "row": None, "division": new.get("division"), "group": None,
               "description": new["description"].strip(), "kind": "item", "scope": "new", "qty": new.get("qty"),
               "unit": F.tidy_unit(new.get("unit")), "unit_as_written": new.get("unit"),
               "confidence": {"line": "low", "qty": "low", "price": None if prices is None else "low",
                              "reason": "Not on his list. " + new["why"].strip()}}
        if new.get("qty") is not None:
            add["qty_source"] = new.get("source")
        lines.insert(markup_at, add)
        markup_at += 1

    used = {ln.get("cost_code") for ln in lines} | {s["code"] for ln in lines for s in ln.get("cost_split") or []}
    est = {
        "format": F.FORMAT_NAME, "format_version": F.FORMAT_VERSION,
        "estimate": {"id": job.get("id"), "job": job.get("job"), "job_type": job.get("job_type"),
                     "parts": job.get("parts"), "definition_level": job.get("definition_level"),
                     "status": "draft", "version": 1, "parent_version": None, "made_by": "estimator",
                     "made_at": made_at, "price_basis": when["date"], "currency": "USD",
                     "note": job.get("note") or "Draft estimate. Not a bid."},
        "divisions": his["divisions"],
        "cost_codes": [{k: c[k] for k in ("code", "name", "category")} for c in code_file["codes"] if c["code"] in used],
        "groups": [{"id": g["id"], "lines": [ids[x] for x in g["rows"] if x in ids]} for g in his.get("groups", [])],
        "cover": {"missing_pages": cover.get("missing_pages"), "assumptions": cover.get("assumptions"),
                  "exclusions": cover.get("exclusions"), "range": cover.get("range"), "check_first": [],
                  "check_first_note": ""},
        "lines": lines,
        "changes": [],
    }
    problems += F.structure(est)
    if not problems:
        F.fill_totals(est)
        est["cover"]["check_first"], est["cover"]["check_first_note"] = check_first(est)
    return est, problems, notes


def check_first(est):
    """'Check these first': Medium and Low lines ranked by dollars times doubt, biggest first.
    A line with no dollars yet cannot be ranked; it is counted in the note, never given a made-up place.
    His markup is left out: it is its own visible line and would head every list."""
    ranked, unranked = [], 0
    for ln in est["lines"]:
        mark = (ln.get("confidence") or {}).get("line")
        if ln["kind"] == "heading" or F.is_markup(ln) or ln.get("scope") == "out" or mark not in DOUBT:
            continue
        if ln.get("cost"):
            ranked.append({"line": ln["id"], "mark": mark, "dollars": ln["cost"],
                           "weight": F.money(abs(ln["cost"]) * DOUBT[mark]), "reason": ln["confidence"]["reason"]})
        else:
            unranked += 1
    ranked.sort(key=lambda x: -x["weight"])
    note = f"{unranked} more Medium, Low or Ask lines carry no dollars yet, so they cannot be ranked." if unranked else ""
    return ranked[:CHECK_FIRST_LINES], note


def main():
    ap = argparse.ArgumentParser(description="Write a draft estimate in the shared format.")
    for name in ("lines", "decisions", "codes", "names", "made-at", "out"):
        ap.add_argument(f"--{name}", required=True)
    ap.add_argument("--code-rows")
    ap.add_argument("--prices")
    a = ap.parse_args()

    def read(path):
        return json.load(open(path)) if path else None

    names = redaction.load(a.names)
    est, problems, notes = build(read(a.lines), read(a.decisions), read(a.codes), a.made_at,
                                 read(a.code_rows), read(a.prices))
    problems = problems or F.save(est, a.out, names)
    if problems:
        print(f"NOT WRITTEN. {len(problems)} problems:", *problems[:40], sep="\n  ")
        return 1
    by = {}
    for ln in est["lines"]:
        key = "heading" if ln["kind"] == "heading" else ln["scope"]
        by[key] = by.get(key, 0) + 1
    still_open = F.open_items(est)
    print(f"draft written: {len(est['lines'])} lines {by}")
    print(f"in scope but not finished: {len(still_open)} (blank quantity, price or rate)")
    print(f"total so far {est['totals']['total']:,.2f}; marks lowered to follow the Method: {len(notes)}")
    print(*notes, sep="\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
