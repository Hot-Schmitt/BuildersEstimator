"""
Tests for the spec tools (tools/spec_lib.py, tools/check_spec.py, tools/build_spec_index.py).

Each test writes a small made-up specification into a temporary folder: one story, one
object, one field, one rule, one screen with two controls, one edge case, two wordings and
one feature note, all agreeing with each other. The first tests show it passes. The rest
break it one way at a time and check the checker names the break.
"""
import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "tools"))
import build_spec_index  # noqa: E402
import check_spec  # noqa: E402
import spec_lib  # noqa: E402

DECISION = """---
number: {number}
title: Made-up decision {number}
status: {status}
date: 2026-01-01
decided_by: owner
area: screens
supersedes:
superseded_by:
{extra}---
"""

FILES = {
    "docs/builder/questions.md": "# Questions\n1. First question?\n2. Second question?\n",
    "spec/stories.yaml": """
jobs:
  - who: "builder"
    job: "Finish an estimate."
activities:
  - id: ACT-01
    name: "Finish and finalize"
stories:
  - id: US-001
    activity: ACT-01
    who: "builder"
    story: "The builder can finalize an estimate."
    slice: "skeleton"
    screens: [S-EST]
    actions: [A-EST-FINALIZE]
    acceptance: [AC-FIN-01]
    decisions: [D-0001]
    status: "locked"
""",
    "spec/wording.yaml": """
- id: W-FINALIZE
  on_screen: "Finalize estimate"
  status: "locked"
  decisions: [D-0001]
- id: W-TOTAL
  on_screen: "Total"
  status: "locked"
""",
    "spec/edge-cases.yaml": """
- id: E-001
  area: "FIN"
  situation: "Every line item is unpriced."
  expected: "He is warned (Q-2 asks the builder)."
  touches: [S-EST, C-top-finalize]
  status: "locked"
""",
    "spec/fields/estimate.yaml": """
- id: F-EST-STATUS
  label: W-TOTAL
  note: "Whether the estimate is a draft or final."
  shown_on: [C-top-finalize]
  provenance: "said"
  status: "locked"
""",
    "spec/rules/finalize.yaml": """
- id: R-FIN-001
  rule: "A blank rate blocks finalizing."
  applies_to: [A-EST-FINALIZE, F-EST-STATUS]
  acceptance: [AC-FIN-01]
  decisions: [D-0001]
  status: "locked"
""",
    "spec/objects/estimate.md": """---
id: O-EST
name: Estimate
status: locked
decisions: [D-0001]
---
## Actions
| Id | Action | Who | Allowed in states | Home control(s) | Rules | Status |
|---|---|---|---|---|---|---|
| A-EST-FINALIZE | Finalize | builder | ST-EST-EDITING | C-top-finalize | R-FIN-001 | locked |
| A-EST-REOPEN | Reopen | none | none | deliberately none: he duplicates instead | | locked |

## Lifecycle
| State id | Name on screen | Meaning | Who may edit |
|---|---|---|---|
| ST-EST-EDITING | Draft estimate | He is changing it | builder |
""",
    "spec/screens/S-EST.md": """---
id: S-EST
name: Estimate
kind: screen
status: locked
stories: [US-001]
objects: [O-EST]
decisions: [D-0001]
---
## Controls
| Id | Type | Label (W-) | Does (A- or plain words) | Reads / writes (F-) | Rules (R-) | States | Does NOT do |
|---|---|---|---|---|---|---|---|
| C-top-finalize | Button | W-FINALIZE | A-EST-FINALIZE | writes F-EST-STATUS | R-FIN-001 | | Does not send |
| C-top-total | Text | W-TOTAL | Nothing | | | | |

## Control detail
### C-top-finalize
- **AC-FIN-01** Given a blank rate, when he presses Finalize estimate, then nothing is finalized.
""",
    "spec/features/FT-SAVE.md": """---
id: FT-SAVE
title: Saving
status: decided
decided_in: D-0001
stories: [US-001]
---
## The need
A change is kept.
""",
}


def make(tmp_path, changes=None, decisions=None):
    """Write the made-up repository, with some files replaced, and return the loaded spec."""
    files = dict(FILES)
    files.update(changes or {})
    for name, text in files.items():
        if text is None:
            continue
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text.lstrip("\n"), encoding="utf-8")
    for number, (status, extra) in (decisions or {"0001": ("accepted", "")}).items():
        path = tmp_path / "decisions" / f"{number}-made-up.md"
        path.parent.mkdir(exist_ok=True)
        path.write_text(DECISION.format(number=number, status=status, extra=extra), encoding="utf-8")
    spec = spec_lib.load(tmp_path)
    for name, text in build_spec_index.pages(spec).items():
        (tmp_path / "spec" / name).write_text(text, encoding="utf-8")
    return spec


def problems(tmp_path, gate=False, **kwargs):
    return check_spec.check(make(tmp_path, **kwargs), gate=gate)[0]


def swap(name, old, new):
    assert FILES[name].count(old) == 1, f"{old!r} must appear once in {name}"
    return {name: FILES[name].replace(old, new)}


def test_empty_folder_passes(tmp_path):
    (tmp_path / "spec").mkdir()
    spec = spec_lib.load(tmp_path)
    for name, text in build_spec_index.pages(spec).items():
        (tmp_path / "spec" / name).write_text(text, encoding="utf-8")
    assert check_spec.check(spec, gate=True) == ([], [])


def test_good_spec_passes_with_and_without_the_gate(tmp_path):
    spec = make(tmp_path)
    assert check_spec.check(spec) == ([], [])
    assert check_spec.check(spec, gate=True) == ([], [])


def test_every_kind_of_id_is_read(tmp_path):
    ids = {record["id"] for record in make(tmp_path).records}
    assert ids == {
        "ACT-01", "US-001", "W-FINALIZE", "W-TOTAL", "E-001", "F-EST-STATUS", "R-FIN-001",
        "O-EST", "A-EST-FINALIZE", "A-EST-REOPEN", "ST-EST-EDITING", "S-EST",
        "C-top-finalize", "C-top-total", "AC-FIN-01", "FT-SAVE",
    }


def test_index_lists_every_id_and_open_page_lists_what_waits(tmp_path):
    spec = make(tmp_path, changes=swap("spec/edge-cases.yaml", 'status: "locked"', 'status: "open"'))
    pages = build_spec_index.pages(spec)
    for record in spec.records:
        assert f"| {record['id']} |" in pages["INDEX.md"]
    assert "| E-001 |" in pages["OPEN.md"] and "| US-001 |" not in pages["OPEN.md"]


def test_ordinary_words_are_not_read_as_ids():
    assert spec_lib.ids_in("a C-channel, an A-frame, R-13 batts, a W-2 and US-made nails") == set()


BREAKS = [
    ("defined twice",
     {"spec/wording.yaml": FILES["spec/wording.yaml"] + '- id: W-TOTAL\n  on_screen: "Sum"\n  status: "locked"\n'},
     "W-TOTAL is defined twice"),
    ("cited and defined nowhere",
     swap("spec/rules/finalize.yaml", "F-EST-STATUS", "F-EST-MISSING"),
     "cites F-EST-MISSING, which is defined nowhere"),
    ("wording id that does not exist",
     swap("spec/screens/S-EST.md", "| C-top-total | Text | W-TOTAL", "| C-top-total | Text | W-NOPE"),
     "cites W-NOPE, which is defined nowhere"),
    ("decision that does not exist",
     swap("spec/wording.yaml", "decisions: [D-0001]", "decisions: [D-0099]"),
     "cites D-0099, and there is no such decision file"),
    ("question that does not exist",
     swap("spec/edge-cases.yaml", "Q-2", "Q-77"),
     "cites Q-77"),
    ("status word",
     swap("spec/fields/estimate.yaml", 'status: "locked"', 'status: "done"'),
     "F-EST-STATUS has status 'done'"),
    ("slice word",
     swap("spec/stories.yaml", 'slice: "skeleton"', 'slice: "soon"'),
     "US-001 has slice 'soon'"),
    ("provenance word",
     swap("spec/fields/estimate.yaml", 'provenance: "said"', 'provenance: "guessed"'),
     "has provenance 'guessed'"),
    ("field names a control that does not list it",
     swap("spec/fields/estimate.yaml", "[C-top-finalize]", "[C-top-finalize, C-top-total]"),
     "F-EST-STATUS says it is shown on C-top-total"),
    ("control names a field that does not list it",
     swap("spec/fields/estimate.yaml", "[C-top-finalize]", "[]"),
     "C-top-finalize reads or writes F-EST-STATUS"),
    ("action with no home",
     swap("spec/objects/estimate.md", "deliberately none: he duplicates instead", "not drawn yet"),
     "A-EST-REOPEN has no home control"),
    ("locked control that changes data, no acceptance case",
     swap("spec/screens/S-EST.md", "### C-top-finalize\n", "### C-top-total\n"),
     "C-top-finalize changes data and has no acceptance case"),
    ("locked rule with no acceptance case",
     swap("spec/rules/finalize.yaml", "acceptance: [AC-FIN-01]", "acceptance: []"),
     "R-FIN-001 has no acceptance case"),
    ("locked rule with no decision",
     swap("spec/rules/finalize.yaml", "decisions: [D-0001]", "decisions: []"),
     "R-FIN-001 is locked but cites no decision"),
    ("record in the wrong data file",
     swap("spec/rules/finalize.yaml", "- id: R-FIN-001", "- id: E-002"),
     "E-002 is not a R- id"),
    ("record with no id",
     {"spec/wording.yaml": FILES["spec/wording.yaml"] + '- on_screen: "Nameless"\n'},
     "record 3 has no id"),
    ("file that is not YAML",
     {"spec/edge-cases.yaml": "- id: E-001\n  situation: \"unclosed\n"},
     "not readable as YAML"),
    ("screen with no frontmatter",
     {"spec/screens/S-EST.md": "## Controls\n"},
     "spec/screens/S-EST.md: no frontmatter block"),
]


@pytest.mark.parametrize("name, changes, expected", BREAKS, ids=[b[0] for b in BREAKS])
def test_each_break_is_named(tmp_path, name, changes, expected):
    found = problems(tmp_path, changes=changes)
    assert any(expected in problem for problem in found), found


def test_superseded_decision_is_named(tmp_path):
    found = problems(tmp_path, decisions={"0001": ("superseded", "")})
    assert any("cites decision 0001, which is superseded" in problem for problem in found)


def test_affects_line_must_agree_both_ways(tmp_path):
    everything = "affects: US-001, W-FINALIZE, R-FIN-001, O-EST, S-EST, FT-SAVE\n"
    assert problems(tmp_path, decisions={"0001": ("accepted", everything)}) == []

    found = problems(tmp_path, decisions={"0001": ("accepted", "affects: US-001, C-top-total\n")})
    assert any("affects C-top-total, but C-top-total does not cite D-0001" in p for p in found)
    assert any("R-FIN-001 cites D-0001, but that decision's affects line does not list it" in p
               for p in found)


def test_stale_generated_page_is_named(tmp_path):
    spec = make(tmp_path)
    (tmp_path / "spec" / "INDEX.md").write_text("old\n", encoding="utf-8")
    assert any("spec/INDEX.md is out of date" in p for p in check_spec.check(spec)[0])


def test_unlocked_gaps_wait_until_the_gate(tmp_path):
    """Before lock, a missing acceptance case or an open item is a to-do, not a failure."""
    changes = swap("spec/rules/finalize.yaml", "acceptance: [AC-FIN-01]", "acceptance: []")
    changes["spec/rules/finalize.yaml"] = changes["spec/rules/finalize.yaml"].replace(
        'status: "locked"', 'status: "proposed"')
    changes.update(swap("spec/edge-cases.yaml", 'status: "locked"', 'status: "open"'))
    changes["spec/stories.yaml"] = FILES["spec/stories.yaml"].replace(
        "acceptance: [AC-FIN-01]", "acceptance: [AC-FIN-01]\n    note: \"See E-001.\"")

    spec = make(tmp_path, changes=changes)
    failing, todo = check_spec.check(spec)
    assert failing == []
    assert any("R-FIN-001 has no acceptance case" in item for item in todo)
    assert any("US-001 is in the first release and touches things still open: E-001" in item
               for item in todo)

    failing, todo = check_spec.check(spec, gate=True)
    assert todo == [] and len(failing) == 2
