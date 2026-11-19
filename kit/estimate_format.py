"""
Shared estimate format, version 0.4.

One estimate version = one JSON file. This module holds the format's fixed
rules: the allowed values, how a line's cost is worked out, and the check
every reader (screen, export, operations app) runs before trusting a file.
Totals are never trusted from the file; they are recomputed here and must
match what the file says. The written spec is project doc 10.

Every script that writes an estimate file goes through fill_totals() and
save() below, so a file that is not in the format cannot be written.
"""
import json
import math
from decimal import Decimal, ROUND_HALF_UP

FORMAT_NAME = "builder-estimate"
FORMAT_VERSION = "0.4"

JOB_TYPES = {"new_build", "adu", "renovation", "mixed"}
DEFINITION_LEVELS = {"sketch", "permit_plans", "plans_with_selections"}
# draft -> builder_editing -> final (builder done) -> signed (client signed, read-only)
STATUSES = {"draft", "builder_editing", "final", "signed"}
# Still being worked on. Only these may hold a percent line with a blank rate,
# or an In line with a price and no quantity (version 0.4).
OPEN_STATUSES = {"draft", "builder_editing"}
MADE_BY = {"estimator", "builder", "import"}

# What kind of row a line is.
#   heading       a label row in his sheet (keeps his layout); no money
#   item          a normal priced line
#   sub_bid       price is a sub's bid; blank until he has it
#   allowance     a carried amount for something not chosen yet
#   client_choice waiting on the client; blank, last known figure beside it
#   percent       a rate on other lines (his tax, contingency, OH&P)
#   alternate     priced separately; counts only when "included" is true
LINE_KINDS = {"heading", "item", "sub_bid", "allowance", "client_choice", "percent", "alternate"}
PERCENT_ROLES = {"tax", "contingency", "markup", "other"}
ALL_COST = "all_cost"  # the base of a markup line: every cost line, always

# in = priced on this job; out = on his checklist, not used; ask = needs his call;
# new = not on his checklist (shown in its own section, never slipped in)
SCOPES = {"in", "out", "ask", "new"}
QTY_SOURCES = {"written", "dimensions", "counted", "calculated", "assumed", "his_entry"}
PRICE_SOURCES = {"his_price", "sub_bid", "allowance", "his_entry", "none"}
CONFIDENCE = {"high", "medium", "low"}
CHANGE_KINDS = {"quantity", "price", "missing_line", "extra_line", "scope", "cost_code", "filing", "other"}
CHANGE_FIELDS = ("line", "field", "from", "to", "by", "at", "kind")

# Where a dollar is filed under a cost code. He files by who does the work, not by
# sheet column, so each price column of a line can be filed under any type
# (filed_as). Unless he says otherwise a column files as below.
COST_TYPES = {"labor", "material", "subcontract"}
DEFAULT_FILING = {"material": "material", "labor": "labor", "ml": "subcontract"}
PRICE_COLUMNS = tuple(DEFAULT_FILING)
UNCODED = "uncoded"

UNIT_SPELLINGS = {"DAYS": "DAY", "HRS": "HR"}


def money(x):
    """Round to cents, halves up (as Excel shows them). Every stored dollar figure goes through here."""
    return float(Decimal(repr(round(float(x), 6))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def tidy_unit(unit):
    """His unit in capitals with plural spellings merged; None stays None."""
    if unit is None:
        return None
    u = str(unit).strip().upper()
    return UNIT_SPELLINGS.get(u, u)


def is_markup(line):
    return line.get("kind") == "percent" and line.get("percent_role") == "markup"


def counts(line):
    """Does this line carry money on this estimate?"""
    if line["kind"] == "heading" or line.get("scope") in ("out", "ask"):
        return False
    return line["kind"] != "alternate" or bool(line.get("included"))


def compute(est):
    """Work out every line cost and the totals. Returns (costs_by_id, totals). Run structure() first.
    A blank quantity or a blank rate adds nothing; open_items() lists those lines."""
    lines = est["lines"]
    costs = {}
    for ln in lines:  # plain lines
        if ln["kind"] != "percent":
            qty = ln.get("qty")
            unit_price = sum(ln.get(k) or 0 for k in PRICE_COLUMNS)
            costs[ln["id"]] = money(qty * unit_price) if counts(ln) and qty is not None else 0.0
    for ln in lines:  # his tax and contingency, in file order (one may sit on an earlier one)
        if ln["kind"] == "percent" and not is_markup(ln):
            rate = ln.get("rate")
            on = counts(ln) and rate is not None
            costs[ln["id"]] = money(rate * sum(costs[i] for i in ln["base"])) if on else 0.0
    cost = money(sum(costs.values()))
    markups = []
    for ln in lines:  # markup always sits on all cost
        if is_markup(ln):
            costs[ln["id"]] = money((ln.get("rate") or 0) * cost)
            markups.append({"line": ln["id"], "amount": costs[ln["id"]]})
    by_div = {}
    for ln in lines:
        if not is_markup(ln):
            d = str(ln["division"])
            by_div[d] = money(by_div.get(d, 0) + costs[ln["id"]])
    totals = {"cost": cost, "markups": markups, "total": money(cost + sum(m["amount"] for m in markups)),
              "by_division": by_div, "by_code": by_code(est, costs)}
    return costs, totals


def share_out(total, weights):
    """Split a dollar amount by weights into cents that add up exactly; the remainder goes to the biggest share."""
    whole = sum(weights.values())
    parts = {k: money(total * w / whole) for k, w in weights.items() if w}
    biggest = max(parts, key=lambda k: abs(parts[k]))
    parts[biggest] = money(parts[biggest] + total - sum(parts.values()))
    return parts


def by_code(est, costs):
    """Budget by cost code and cost type: what the operations app tracks actuals against.
    Each line's rounded cost is shared out, so the budget always adds up to the cost."""
    out = {}
    for ln in est["lines"]:
        cost = costs.get(ln["id"], 0)
        if not cost or is_markup(ln):
            continue
        if ln["kind"] == "percent":
            by_type = {ln["cost_type"]: cost}
        else:
            filing = {**DEFAULT_FILING, **(ln.get("filed_as") or {})}
            raw = {}
            for column, cost_type in filing.items():
                raw[cost_type] = raw.get(cost_type, 0) + ln["qty"] * (ln.get(column) or 0)
            by_type = share_out(cost, raw)
        codes = {s["code"]: s["share"] for s in ln.get("cost_split") or []} or {ln.get("cost_code") or UNCODED: 1}
        for cost_type, amount in by_type.items():
            for code, part in share_out(amount, codes).items():
                row = out.setdefault(code, {t: 0.0 for t in sorted(COST_TYPES)})
                row[cost_type] = money(row[cost_type] + part)
    return dict(sorted(out.items()))


def fill_totals(est):
    """What every writer does on save: store each line's cost and the totals block. Run structure() first."""
    costs, est["totals"] = compute(est)
    for ln in est["lines"]:
        if ln["kind"] != "heading":
            ln["cost"] = costs[ln["id"]]
    return est


def open_items(est):
    """In-scope lines that add nothing yet because a quantity, a price or a rate is blank.
    For the 'not finished' list on a draft. Never stored. Run on a file that passes structure()."""
    out = []
    for ln in est["lines"]:
        if ln["kind"] == "heading" or not counts(ln):
            continue
        if ln["kind"] == "percent":
            if ln.get("rate") is None:
                out.append({"line": ln["id"], "missing": "rate"})
        elif ln.get("qty") is None:
            out.append({"line": ln["id"], "missing": "quantity"})
        elif not any(ln.get(k) for k in PRICE_COLUMNS):
            out.append({"line": ln["id"], "missing": "price"})
    return out


# ---- the check. Nothing below may assume a value has the right type: every value is tested before it is used.

def _number(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)


def _word(v, allowed):
    """A string from an allowed list. Also safe on lists and records, which cannot be looked up in a set."""
    return isinstance(v, str) and v in allowed


def _key(v):
    """A value usable as an id, a code or a division number."""
    return (isinstance(v, str) and v != "") or (isinstance(v, int) and not isinstance(v, bool))


def _records(est, key, p):
    """A top-level list of records (it may be absent). Anything else is reported and read as empty."""
    v = est.get(key, [])
    if not isinstance(v, list) or any(not isinstance(x, dict) for x in v):
        p.append(f"{key} must be a list of records")
        return []
    return v


def _typed(v, allowed):
    """A source record such as {"type": "counted", ...} with an allowed type."""
    return isinstance(v, dict) and _word(v.get("type"), allowed)


def structure(est):
    """Check the file's shape and allowed values. Returns a list of problems."""
    p = []
    if not isinstance(est, dict) or not isinstance(est.get("lines"), list):
        return ["no list of lines"]
    if est.get("format") != FORMAT_NAME:
        p.append("not a builder-estimate file")
    if est.get("format_version") != FORMAT_VERSION:
        p.append(f"format version {est.get('format_version')!r} not {FORMAT_VERSION}")
    e = est.get("estimate")
    if not isinstance(e, dict):
        p.append("no estimate header block")
        e = {}
    for field, allowed in (("job_type", JOB_TYPES), ("status", STATUSES), ("made_by", MADE_BY),
                           ("definition_level", DEFINITION_LEVELS)):
        if not _word(e.get(field), allowed):
            p.append(f"estimate.{field} = {e.get(field)!r} not allowed")
    version = e.get("version")
    if not (isinstance(version, int) and not isinstance(version, bool) and version >= 1):
        p.append("estimate.version must be a whole number from 1")
    if e.get("job_type") == "mixed":
        parts = e.get("parts")
        if not (isinstance(parts, list) and parts and all(_word(x, JOB_TYPES - {"mixed"}) for x in parts)):
            p.append("a mixed job must list its parts")
    is_draft = e.get("made_by") == "estimator" or e.get("status") == "draft"
    is_open = _word(e.get("status"), OPEN_STATUSES)
    for block in ("cover", "signed", "totals"):
        if est.get(block) is not None and not isinstance(est[block], dict):
            p.append(f"{block} must be a record")

    codes = [c.get("code") for c in _records(est, "cost_codes", p)]
    if any(not _key(c) for c in codes):
        p.append("a cost code in the estimate's code list has no code")
        codes = [c for c in codes if _key(c)]
    if len(set(codes)) != len(codes):
        p.append("duplicate cost code in the estimate's code list")
    numbers = [d.get("number") for d in _records(est, "divisions", p)]
    if any(not _key(n) for n in numbers):
        p.append("a division in the division list has no number")
    divisions = {n for n in numbers if _key(n)}
    _records(est, "groups", p)

    above = {}  # id -> is it a markup line, for every sound line already passed
    for n, ln in enumerate(est["lines"], 1):
        if not isinstance(ln, dict):
            p.append(f"line {n} is not a record")
            continue
        i = ln.get("id")
        if not (isinstance(i, str) and i) or i in above:
            p.append(f"line {n}: missing or duplicate line id {i!r}")
            continue
        kind = ln.get("kind")
        if not _word(kind, LINE_KINDS):
            p.append(f"{i}: kind {kind!r}")
            continue
        markup = is_markup(ln)
        if not markup and not (_key(ln.get("division")) and ln["division"] in divisions):
            p.append(f"{i}: division {ln.get('division')!r} not in the division list")
        if kind == "heading":
            above[i] = False
            continue
        if not _word(ln.get("scope"), SCOPES):
            p.append(f"{i}: scope {ln.get('scope')!r}")
        if ln.get("cost_code") is not None and not (_key(ln["cost_code"]) and ln["cost_code"] in codes):
            p.append(f"{i}: cost code {ln['cost_code']!r} not in the estimate's code list")
        if kind == "percent":
            if not _word(ln.get("percent_role"), PERCENT_ROLES):
                p.append(f"{i}: percent_role missing")
            rate = ln.get("rate")
            if not (_number(rate) and 0 <= rate <= 1) and not (rate is None and is_open):
                p.append(f"{i}: rate must be a number from 0 to 1 (0.25 for 25%); "
                         "it may be blank only while the estimate is a draft or being edited")
            if markup:
                if ln.get("base") != ALL_COST:
                    p.append(f"{i}: markup must sit on all cost")
                if ln.get("scope") != "in":
                    p.append(f"{i}: a markup line is always in scope; to charge no markup set its rate to 0")
            else:
                base = ln.get("base")
                if not isinstance(base, list) or not base:
                    p.append(f"{i}: percent line with no base lines")
                else:
                    for b in base:  # a base is a plain line, or a tax or contingency line above this one
                        if not (isinstance(b, str) and b in above) or above[b]:
                            p.append(f"{i}: base line {b!r} not found above it")
                if not _word(ln.get("cost_type"), COST_TYPES):
                    p.append(f"{i}: percent line needs a cost type")
        else:
            for f in ("qty",) + PRICE_COLUMNS:
                if ln.get(f) is not None and not _number(ln[f]):
                    p.append(f"{i}: {f} is not a number")
            qty = ln.get("qty")
            if _number(qty) and qty < 0:
                p.append(f"{i}: quantity below zero (a credit is a negative price)")
            unit = ln.get("unit")
            if unit is not None and not (isinstance(unit, str) and unit == tidy_unit(unit)):
                p.append(f"{i}: unit {unit!r} not tidied")
            filed = ln.get("filed_as")
            if filed is not None and not (isinstance(filed, dict) and all(
                    k in DEFAULT_FILING and _word(v, COST_TYPES) for k, v in filed.items())):
                p.append(f"{i}: filed_as must name a price column and a cost type")
            split = ln.get("cost_split")
            if split is not None:
                ok = (isinstance(split, list) and len(split) >= 2 and ln.get("cost_code") is None
                      and all(isinstance(s, dict) and _key(s.get("code")) and s["code"] in codes
                              and _number(s.get("share")) and s["share"] > 0 for s in split)
                      and len({s["code"] for s in split}) == len(split)
                      and abs(sum(s["share"] for s in split) - 1) < 1e-9)
                if not ok:
                    p.append(f"{i}: cost split needs two or more listed codes with shares adding to 1, and no single cost code")
            if qty is not None and not _typed(ln.get("qty_source"), QTY_SOURCES):
                p.append(f"{i}: quantity has no source (a record with an allowed type)")
            if "price_source" in ln and not _typed(ln["price_source"], PRICE_SOURCES):
                p.append(f"{i}: price source not allowed")
            if (not is_open and qty is None and counts(ln)
                    and any(_number(ln.get(k)) and ln[k] for k in PRICE_COLUMNS)):
                p.append(f"{i}: in scope with a price but no quantity; allowed only while the estimate is a draft or being edited")
        conf = ln.get("confidence")
        if conf is None:
            if is_draft:
                p.append(f"{i}: draft line without confidence")
        elif not isinstance(conf, dict):
            p.append(f"{i}: confidence must be a record with a word and a reason")
        else:
            if not _word(conf.get("line"), CONFIDENCE):
                p.append(f"{i}: confidence word missing")
            elif conf["line"] != "high" and not (isinstance(conf.get("reason"), str) and conf["reason"].strip()):
                p.append(f"{i}: medium/low needs a reason")
            for part in ("qty", "price"):
                if conf.get(part) is not None and not _word(conf[part], CONFIDENCE):
                    p.append(f"{i}: confidence {part} mark not allowed")
        above[i] = markup

    for c in _records(est, "changes", p):
        missing = [f for f in CHANGE_FIELDS if f not in c]
        if missing:
            p.append(f"change entry missing {', '.join(missing)}")
        elif not _word(c["kind"], CHANGE_KINDS):
            p.append(f"change kind {c['kind']!r}")
        elif not (isinstance(c["line"], str) and c["line"] in above) and c["kind"] != "extra_line":
            p.append(f"change on unknown line {c['line']!r}")
    return p


def _check(est):
    p = structure(est)
    if p:
        return p
    costs, totals = compute(est)
    stored = est.get("totals") or {}
    for key in ("cost", "total", "markups", "by_division", "by_code"):
        if stored.get(key) != totals[key]:
            p.append(f"stored {key} does not match the recomputed figure")
    for ln in est["lines"]:
        if "cost" in ln:
            if not _number(ln["cost"]):
                p.append(f"{ln['id']}: stored cost is not a number")
            elif abs(ln["cost"] - costs[ln["id"]]) > 0.005:
                p.append(f"{ln['id']}: stored cost {ln['cost']} vs recomputed {costs[ln['id']]}")
    coded = money(sum(v for row in totals["by_code"].values() for v in row.values()))
    if coded != totals["cost"]:
        p.append(f"budget by cost code {coded} does not add up to cost {totals['cost']}")
    if est["estimate"]["status"] == "signed":
        s = est.get("signed") or {}
        if not (str(s.get("by") or "").strip() and str(s.get("at") or "").strip()):
            p.append("signed estimate needs who signed and when")
        if s.get("total") != totals["total"]:
            p.append("signed total does not match the estimate total")
    return p


def check(est):
    """Every reader runs this. Returns a list of problems; empty means the file is sound.
    It never raises: structure() tests every value before use, and the guard below turns
    anything it still missed into a rejected file, never a crash and never a pass."""
    try:
        return _check(est)
    except Exception as err:
        return [f"check could not finish ({type(err).__name__}); file rejected"]


def save(est, path, names=()):
    """The only way an estimate file is written. Runs the check, then looks for any listed
    name (client, vendor, sub) left in the text. Writes nothing and returns the problems
    if either fails; returns [] once the file is written."""
    problems = check(est)
    if not problems:
        text = json.dumps(est, separators=(",", ":"))
        low = text.lower()
        problems = [f"name not redacted: {n}" for n in names if str(n).lower() in low]
        if not problems:
            with open(path, "w") as f:
                f.write(text)
    return problems


# Change log
# Nov 16, 2026 · version 0.3 -> 0.4 (approved by the user: review decisions 1, 2 and 5).
#   - A percent line may have a blank rate, and an In line may have a price with no quantity, only while
#     the estimate is a draft or being edited. A final or signed estimate may have neither.
#   - The check tests every value before using it and cannot be crashed by a bad file (NaN included).
#   - Newly enforced: a markup line is always in scope; a mixed job lists its parts; a base may not be a
#     markup line; confidence, quantity source and price source must be records.
#   - Added fill_totals(), open_items() and save(): the one way a file is totalled, listed as unfinished, and written.
#   - Removed percent_all() (no longer needed).
