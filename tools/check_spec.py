#!/usr/bin/env python3
"""Check the spec/ folder for breaks: ids that point nowhere, things with no home,
records that disagree with each other or with the decisions.

It always fails, naming the file and the id, when:
  a. a file cannot be read, sits where no reader looks, or holds an id of the wrong
     kind or shape (reported by tools/spec_lib.py as it reads);
  b. an id is defined twice, or cited and defined nowhere (wording ids included);
  c. a status, slice, provenance or rule-area word is not one of the allowed words;
  d. a field says it is shown on a control that does not list it, or the reverse;
  e. an action has no home control, is not marked "deliberately none" and is not open;
  f. a "decisions:" entry is not a D-NNNN that exists, or an "acceptance:" entry is
     not a defined AC- id;
  g. anything cites a decision that is superseded or withdrawn;
  h. a decision's "affects:" line and the records' "decisions:" lists disagree;
  i. a feature build note is marked decided and names no decision;
  j. spec/INDEX.md or spec/OPEN.md is out of step with the folder;
  k. something LOCKED is incomplete: a locked screen's control changes data and has
     no acceptance case; a locked rule has no acceptance case or cites no decision;
     a locked first-release story reaches anything still waiting.

"Waiting" means status open, proposed or options, or a field carrying an open note.
A story "reaches" everything it cites, everything those records cite, and so on.

With --gate (the test for leaving phase 5, before any build) the completeness checks
in k apply to everything, locked or not. Without it they are printed as "still to do
before lock" and do not fail, so the folder can be checked while it is being written.

Two checks from the design wait for later phases and are not here yet: control ids
in a locked drawing's code against the controls table (phase 5), and acceptance ids
against test names (the build).

Run:  python3 tools/check_spec.py [--gate]
"""

import argparse
import re
import sys

import build_spec_index
import spec_lib

FIRST_RELEASE = {"skeleton", "first"}
DECISION_ID = re.compile(r"D-\d{4}")


def is_waiting(record):
    return record["status"] in spec_lib.WAITING or bool(record.get("open_note"))


def reach(start, by_id):
    """Every record a record cites, directly or through other records."""
    seen, queue = set(), [start["id"]]
    while queue:
        current = queue.pop()
        if current in seen or current not in by_id:
            continue
        seen.add(current)
        queue.extend(by_id[current]["cites"])
    return seen


def check(spec, gate=False):
    """Return (problems that fail the check, things still to do before lock)."""
    problems, todo = list(spec.problems), []
    by_id = {}

    def incomplete(message, locked):
        (problems if locked or gate else todo).append(message)

    # b. defined twice
    for record in spec.records:
        if record["id"] in by_id:
            problems.append(f"{record['id']} is defined twice: {by_id[record['id']]['file']} "
                            f"and {record['file']}")
        else:
            by_id[record["id"]] = record

    # b and g. cited and defined nowhere; a retired decision cited anywhere.
    # Reported once per file, not once per table row.
    reported = set()
    for record in spec.records:
        for cited in sorted(record["cites"]):
            if (record["file"], cited) in reported:
                continue
            reported.add((record["file"], cited))
            kind = spec_lib.kind_of(cited)
            where = f"{record['file']}: {record['id']} cites {cited}"
            if kind == "D":
                decision = spec.decisions.get(cited[2:])
                if decision is None:
                    problems.append(f"{where}, and there is no such decision file")
                elif decision["status"] in ("superseded", "withdrawn"):
                    problems.append(f"{where}, which is {decision['status']}")
            elif kind == "Q":
                if str(int(cited[2:])) not in spec.questions:
                    problems.append(f"{where}, and docs/builder/questions.md has no question "
                                    "with that number")
            elif cited not in by_id:
                problems.append(f"{where}, which is defined nowhere")

    # c. allowed words
    for record in spec.records:
        where = f"{record['file']}: {record['id']}"
        allowed = (spec_lib.FEATURE_STATUS_WORDS if record["kind"] == "FT"
                   else spec_lib.STATUS_WORDS)
        if record["kind"] != "ACT" and record["status"] not in allowed:
            problems.append(f"{where} has status {record['status']!r}; use one of "
                            + ", ".join(sorted(allowed)))
        if record.get("provenance") and record["provenance"] not in spec_lib.PROVENANCE_WORDS:
            problems.append(f"{where} has provenance {record['provenance']!r}; use one of "
                            + ", ".join(sorted(spec_lib.PROVENANCE_WORDS)))
        if record["kind"] == "US" and record["slice"] not in spec_lib.SLICE_WORDS:
            problems.append(f"{where} has slice {record['slice']!r}; use one of "
                            + ", ".join(sorted(spec_lib.SLICE_WORDS)))
        if record["kind"] == "R" and record["id"].split("-")[1] not in spec_lib.RULE_AREAS:
            problems.append(f"{where} uses a rule area that is not in the list "
                            "(spec/README.md; tools/spec_lib.py RULE_AREAS)")

    # d. fields and controls agree, both ways
    for record in spec.records:
        if record["kind"] == "F":
            for control in sorted(record["shown_on"]):
                if control in by_id and record["id"] not in by_id[control].get("fields", ()):
                    problems.append(f"{record['file']}: {record['id']} says it is shown on "
                                    f"{control}, but that control's row does not list it")
        if record["kind"] == "C":
            for field in sorted(record["fields"]):
                if field in by_id and record["id"] not in by_id[field].get("shown_on", ()):
                    problems.append(f"{record['file']}: {record['id']} reads or writes {field}, "
                                    "but that field's shown_on does not list this control")

    # e. every action has a home, or says why not
    for record in spec.records:
        if record["kind"] == "A" and record["status"] != "open":
            has_control = any(spec_lib.kind_of(i) == "C" for i in spec_lib.ids_in(record["home"]))
            if not has_control and "deliberately none" not in record["home"].lower():
                problems.append(f"{record['file']}: {record['id']} has no home control and is "
                                'not marked "deliberately none"')

    # f. entries in decisions: and acceptance: are real ids of the right kind
    for record in spec.records:
        where = f"{record['file']}: {record['id']}"
        for entry in record.get("decisions", ()):
            if not DECISION_ID.fullmatch(entry):
                problems.append(f"{where} lists {entry!r} under decisions; write it as D-NNNN")
        for entry in record.get("acceptance", ()):
            if spec_lib.kind_of(entry) != "AC" or entry not in by_id:
                problems.append(f"{where} lists {entry!r} under acceptance, which is not a "
                                "defined AC- id")

    # h. decisions, both ways. A control, state, action or acceptance case has no
    # decisions list of its own: it is covered by the file or rule it sits in.
    cited_by = {}
    for record in spec.records:
        for entry in record.get("decisions", ()):
            if DECISION_ID.fullmatch(entry):
                cited_by.setdefault(entry[2:], set()).add(record["id"])
    for number, decision in sorted(spec.decisions.items()):
        if decision["affects"] is None:
            continue  # the affects line is optional; older decisions have none
        citing = cited_by.get(number, set())
        for affected in sorted(decision["affects"]):
            parent = by_id.get(affected, {}).get("parent")
            if affected not in citing and parent not in citing:
                problems.append(f"{decision['file']}: affects {affected}, but neither it nor "
                                f"the file it sits in cites D-{number} in its decisions")
        parents_named = {by_id[a].get("parent") for a in decision["affects"] if a in by_id}
        for missing in sorted(citing - decision["affects"] - parents_named):
            problems.append(f"{by_id[missing]['file']}: {missing} cites D-{number}, but that "
                            "decision's affects line does not list it")

    # i. a decided feature note names its decision
    for record in spec.records:
        if record["kind"] == "FT" and record["status"] == "decided" and not record["decisions"]:
            problems.append(f"{record['file']}: {record['id']} is marked decided but "
                            "decided_in is blank")

    # j. the generated pages are current
    for name, text in build_spec_index.pages(spec).items():
        path = spec.root / name
        if not path.is_file() or path.read_text(encoding="utf-8") != text:
            problems.append(f"spec/{name} is out of date; run python3 tools/build_spec_index.py")

    # k. completeness: fails on something locked, or on everything at the gate
    cases = [r for r in spec.records if r["kind"] == "AC"]
    for record in spec.records:
        locked = record["status"] == "locked"
        if record["kind"] == "C" and record["changes_data"]:
            if not any(case.get("owner") == record["id"] or record["id"] in case["cites"]
                       for case in cases):
                incomplete(f"{record['file']}: {record['id']} changes data and has no "
                           "acceptance case", locked)
        if record["kind"] == "R":
            if not record["acceptance"]:
                incomplete(f"{record['file']}: {record['id']} has no acceptance case", locked)
            if locked and not record["decisions"]:
                problems.append(f"{record['file']}: {record['id']} is locked but cites no decision")
        if record["kind"] == "US" and record["slice"] in FIRST_RELEASE:
            waiting = sorted(i for i in reach(record, by_id) if is_waiting(by_id[i]))
            if waiting:
                incomplete(f"{record['file']}: {record['id']} is in the first release and "
                           f"reaches things still waiting: {', '.join(waiting)}", locked)

    return problems, todo


def main():
    parser = argparse.ArgumentParser(description="Check the spec/ folder for breaks.",
                                     allow_abbrev=False)
    parser.add_argument("--gate", action="store_true",
                        help="also fail on anything incomplete, locked or not")
    args = parser.parse_args()

    spec = spec_lib.load()
    problems, todo = check(spec, gate=args.gate)
    if todo:
        print(f"Still to do before lock ({len(todo)}):")
        for item in todo:
            print(f"  - {item}")
    if problems:
        print(f"\nProblems found ({len(problems)}):\n", file=sys.stderr)
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        sys.exit(1)
    print(f"Spec check passed: {len(spec.records)} id(s), {len(spec.decisions)} decision(s) read"
          + (", gate checks included." if args.gate else "."))


if __name__ == "__main__":
    main()
