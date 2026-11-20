#!/usr/bin/env python3
"""Check the spec/ folder for breaks: ids that point nowhere, things with no home,
records that disagree with each other or with the decisions.

It fails, naming the file and the id, when:
  1. an id is defined twice, or cited and defined nowhere (wording ids included);
  2. a status, slice or provenance word is not one of the allowed words;
  3. a field says it is shown on a control that does not list it, or the reverse;
  4. an action has no home control, is not marked "deliberately none" and is not open;
  5. a locked screen has a control that changes data and no acceptance case for it;
  6. a locked rule has no acceptance case, or cites no decision;
  7. a decision's "affects:" line and the records' "decisions:" lists disagree;
  8. a record cites a decision that is missing, superseded or withdrawn;
  9. spec/INDEX.md or spec/OPEN.md is out of step with the folder.

With --gate (the test for leaving phase 5, before any build) it also fails when:
 10. any control that changes data, or any rule, has no acceptance case, locked or not;
 11. a story in the first release touches anything still open.

Without --gate, 10 and 11 are printed as "still to do before lock" and do not fail,
so the folder can be checked while it is being written.

Two checks wait for later phases and are not here yet: control ids in a locked
drawing's code against the controls table (phase 5), and acceptance ids against
test names (the build).

Run:  python3 tools/check_spec.py [--gate]
"""

import sys

import build_spec_index
import spec_lib

FIRST_RELEASE = {"skeleton", "first"}


def check(spec, gate=False):
    """Return (problems that fail the check, things still to do before lock)."""
    problems, todo = list(spec.problems), []
    later = problems if gate else todo
    by_id = {}

    # 1. defined twice
    for record in spec.records:
        if record["id"] in by_id:
            problems.append(f"{record['id']} is defined twice: {by_id[record['id']]['file']} "
                            f"and {record['file']}")
        else:
            by_id[record["id"]] = record

    # 1 and 8. cited and defined nowhere (reported once per file, not once per row)
    reported = set()
    for record in spec.records:
        for cited in sorted(record["cites"]):
            if (record["file"], cited) in reported:
                continue
            reported.add((record["file"], cited))
            kind = spec_lib.kind_of(cited)
            if kind == "D":
                if cited[2:] not in spec.decisions:
                    problems.append(f"{record['file']}: {record['id']} cites {cited}, "
                                    "and there is no such decision file")
            elif kind == "Q":
                if cited[2:] not in spec.questions:
                    problems.append(f"{record['file']}: {record['id']} cites {cited}, and "
                                    "docs/builder/questions.md has no question with that number")
            elif cited not in by_id:
                problems.append(f"{record['file']}: {record['id']} cites {cited}, "
                                "which is defined nowhere")

    # 2. allowed words
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

    # 3. fields and controls agree, both ways
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

    # 4. every action has a home, or says why not
    for record in spec.records:
        if record["kind"] == "A" and record["status"] != "open":
            has_control = any(spec_lib.kind_of(i) == "C" for i in spec_lib.ids_in(record["home"]))
            if not has_control and "deliberately none" not in record["home"].lower():
                problems.append(f"{record['file']}: {record['id']} has no home control and is "
                                'not marked "deliberately none"')

    # 5 and 10. a control that changes data has an acceptance case
    cases = [r for r in spec.records if r["kind"] == "AC"]
    for record in spec.records:
        if record["kind"] == "C" and record["changes_data"]:
            covered = any(case.get("owner") == record["id"] or record["id"] in case["cites"]
                          for case in cases)
            if not covered:
                message = (f"{record['file']}: {record['id']} changes data and has no "
                           "acceptance case")
                (problems if record["status"] == "locked" else later).append(message)

    # 6 and 10. a rule has an acceptance case; a locked rule cites its decision
    for record in spec.records:
        if record["kind"] == "R":
            if not record["acceptance"]:
                message = f"{record['file']}: {record['id']} has no acceptance case"
                (problems if record["status"] == "locked" else later).append(message)
            if record["status"] == "locked" and not record["decisions"]:
                problems.append(f"{record['file']}: {record['id']} is locked but cites no decision")

    # 7 and 8. decisions, both ways
    cited_by = {}
    for record in spec.records:
        for cited in record.get("decisions", ()):
            number = cited[2:] if cited.startswith("D-") else cited
            decision = spec.decisions.get(number)
            if decision is None:
                continue  # already reported under check 1
            cited_by.setdefault(number, set()).add(record["id"])
            if decision["status"] in ("superseded", "withdrawn"):
                problems.append(f"{record['file']}: {record['id']} cites decision {number}, "
                                f"which is {decision['status']}")
    for number, decision in sorted(spec.decisions.items()):
        if decision["affects"] is None:
            continue  # the affects line is optional; older decisions have none
        citing = cited_by.get(number, set())
        for missing in sorted(decision["affects"] - citing):
            problems.append(f"{decision['file']}: affects {missing}, but {missing} does not "
                            f"cite D-{number} in its decisions")
        for missing in sorted(citing - decision["affects"]):
            problems.append(f"{by_id[missing]['file']}: {missing} cites D-{number}, but that "
                            "decision's affects line does not list it")

    # 9. the generated pages are current
    for name, text in build_spec_index.pages(spec).items():
        path = spec.root / name
        if not path.is_file() or path.read_text(encoding="utf-8") != text:
            problems.append(f"spec/{name} is out of date; run python3 tools/build_spec_index.py")

    # 11. nothing open in the first release
    for record in spec.records:
        if record["kind"] == "US" and record["slice"] in FIRST_RELEASE:
            touched = set(record["cites"])
            for cited in list(touched):  # a screen brings everything its file cites
                if spec_lib.kind_of(cited) == "S" and cited in by_id:
                    touched |= by_id[cited]["cites"]
            still_open = sorted(i for i in touched | {record["id"]}
                                if i in by_id and by_id[i]["status"] in ("open", "options"))
            if still_open:
                later.append(f"{record['file']}: {record['id']} is in the first release and "
                             f"touches things still open: {', '.join(still_open)}")

    return problems, todo


def main():
    gate = "--gate" in sys.argv[1:]
    spec = spec_lib.load()
    problems, todo = check(spec, gate=gate)
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
          + (", gate checks included." if gate else "."))


if __name__ == "__main__":
    main()
