#!/usr/bin/env python3
"""Build CURRENT.md from the decision files in decisions/.

Every decision lives in exactly one file under decisions/. This script reads the
frontmatter of each and writes CURRENT.md: the decisions that stand right now,
grouped by area, with superseded and withdrawn ones listed separately so the
chain stays visible.

CURRENT.md is generated. Editing it by hand is pointless: the next run overwrites it.

Run:  python3 tools/build_index.py
"""

from datetime import date
from pathlib import Path
import re
import sys

REPO = Path(__file__).resolve().parent.parent
DECISIONS = REPO / "decisions"
OUTPUT = REPO / "CURRENT.md"

# Order areas deliberately: what the thing is, then how it prices, then its data,
# then its screens, then how we work. Anything unrecognised is appended at the end.
AREA_ORDER = ["product", "pricing", "format", "data", "screens", "testing", "process"]
AREA_TITLES = {
    "product": "What the tool is",
    "pricing": "Pricing, markup and tax",
    "format": "The shared estimate format",
    "data": "Job data and privacy",
    "screens": "Screens and design",
    "testing": "Testing and accuracy",
    "process": "How we work",
}
VALID_STATUS = {"proposed", "accepted", "superseded", "withdrawn"}

# Keys we expect in frontmatter. Everything is a plain "key: value" line; no YAML
# library is used, so the repo has no dependency for its own housekeeping.
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_file(path):
    """Return a dict of frontmatter fields, or None with a reason if unparseable."""
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        return None, "no frontmatter block"

    fields = {}
    for line in match.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            return None, f"frontmatter line is not key: value -> {line!r}"
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()

    fields["path"] = path.name
    return fields, None


def check(fields):
    """Return a list of problems with one decision's frontmatter."""
    problems = []

    for key in ("number", "title", "status", "date", "area"):
        if not fields.get(key):
            problems.append(f"{fields['path']}: missing {key}")

    number = fields.get("number", "")
    if number and not re.fullmatch(r"\d{4}", number):
        problems.append(f"{fields['path']}: number {number!r} is not four digits")
    if number and not fields["path"].startswith(number + "-"):
        problems.append(
            f"{fields['path']}: filename does not start with its number {number}"
        )

    status = fields.get("status", "")
    if status and status not in VALID_STATUS:
        problems.append(
            f"{fields['path']}: status {status!r} is not one of "
            + ", ".join(sorted(VALID_STATUS))
        )

    if status == "superseded" and not fields.get("superseded_by"):
        problems.append(
            f"{fields['path']}: superseded but superseded_by is blank, "
            "so the chain is broken"
        )

    stamp = fields.get("date", "")
    if stamp and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", stamp):
        problems.append(f"{fields['path']}: date {stamp!r} is not YYYY-MM-DD")

    return problems


def check_pairs(decisions):
    """Supersession has two ends. Check both agree."""
    problems = []
    by_number = {d["number"]: d for d in decisions}

    for d in decisions:
        target = d.get("superseded_by")
        if target:
            other = by_number.get(target)
            if not other:
                problems.append(
                    f"{d['path']}: superseded_by {target} does not exist"
                )
            elif other.get("supersedes") != d["number"]:
                problems.append(
                    f"{d['path']}: says it was superseded by {target}, but "
                    f"{other['path']} does not say it supersedes {d['number']}"
                )

        target = d.get("supersedes")
        if target:
            other = by_number.get(target)
            if not other:
                problems.append(f"{d['path']}: supersedes {target} does not exist")
            elif other.get("status") != "superseded":
                problems.append(
                    f"{d['path']}: supersedes {target}, but {other['path']} "
                    f"still has status {other.get('status')!r}"
                )

    return problems


def table(rows):
    lines = ["| # | Decision | Decided | By |", "|---|---|---|---|"]
    for d in rows:
        lines.append(
            f"| [{d['number']}](decisions/{d['path']}) | {d['title']} "
            f"| {d['date']} | {d.get('decided_by', '')} |"
        )
    return lines


def main():
    if not DECISIONS.is_dir():
        sys.exit(f"no decisions directory at {DECISIONS}")

    decisions, problems = [], []
    for path in sorted(DECISIONS.glob("*.md")):
        if path.name.startswith("0000-"):
            continue  # the template is not a decision
        fields, error = parse_file(path)
        if error:
            problems.append(f"{path.name}: {error}")
            continue
        problems.extend(check(fields))
        decisions.append(fields)

    problems.extend(check_pairs(decisions))

    numbers = [d["number"] for d in decisions]
    for number in sorted(set(numbers)):
        if numbers.count(number) > 1:
            problems.append(f"number {number} is used by more than one file")

    if problems:
        print("Problems found. CURRENT.md was NOT written:\n", file=sys.stderr)
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        sys.exit(1)

    standing = [d for d in decisions if d["status"] == "accepted"]
    proposed = [d for d in decisions if d["status"] == "proposed"]
    retired = [d for d in decisions if d["status"] in ("superseded", "withdrawn")]

    out = [
        "# Decisions that stand right now",
        "",
        "**Generated by `tools/build_index.py`. Do not edit by hand.**",
        f"Built {date.today().isoformat()} from {len(decisions)} decision "
        f"file(s) in `decisions/`.",
        "",
        f"{len(standing)} standing · {len(proposed)} proposed · "
        f"{len(retired)} superseded or withdrawn",
        "",
        "Each row links to the decision's own file, which carries the reason, the "
        "alternative that was rejected, and what the choice costs us.",
        "",
    ]

    areas = AREA_ORDER + sorted(
        {d["area"] for d in standing} - set(AREA_ORDER)
    )
    for area in areas:
        rows = sorted(
            (d for d in standing if d["area"] == area),
            key=lambda d: d["date"],
        )
        if not rows:
            continue
        out += ["## " + AREA_TITLES.get(area, area.title()), ""]
        out += table(rows)
        out += [""]

    if proposed:
        out += [
            "## Proposed, not yet decided",
            "",
            "Waiting on the owner or the builder.",
            "",
        ]
        out += table(sorted(proposed, key=lambda d: d["date"]))
        out += [""]

    if retired:
        out += [
            "## Superseded and withdrawn",
            "",
            "Kept on purpose. These are the paths that were tried and dropped; "
            "the file says what replaced each one and why.",
            "",
            "| # | Decision | Status | Replaced by |",
            "|---|---|---|---|",
        ]
        for d in sorted(retired, key=lambda d: d["number"]):
            replacement = d.get("superseded_by") or "—"
            out.append(
                f"| [{d['number']}](decisions/{d['path']}) | {d['title']} "
                f"| {d['status']} | {replacement} |"
            )
        out += [""]

    OUTPUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(
        f"Wrote {OUTPUT.relative_to(REPO)}: {len(standing)} standing, "
        f"{len(proposed)} proposed, {len(retired)} retired."
    )


if __name__ == "__main__":
    main()
