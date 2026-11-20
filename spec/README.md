# The specification

**Purpose:** the one home for every screen, button, field, rule, story and edge case of the estimator, each with an id, so the build can start with nothing left to re-decide. Set up on Nov 20, 2026 (decision 0067, phase 0). It is empty until phase 1 fills it.

Decisions stay in `decisions/`. This folder says *what the tool is*; a decision file says *why*. Every record here points at the decisions behind it.

## How to use it

Do not read the whole folder. Find one thing, open one file.

- **What is this, and where is it defined?** `grep -n "C-top-finalize" spec/INDEX.md`, then open the file on that line.
- **Where is it used?** `grep -rn "F-LI-UNIT-PRICE" spec/ decisions/`
- **Why is it this way?** The `decisions:` on its record.
- **What is still undecided?** `spec/OPEN.md`. It is also the owner's list for the next round of decisions.

After any change in this folder:

```
python3 tools/build_spec_index.py   # rewrite INDEX.md and OPEN.md
python3 tools/check_spec.py         # look for breaks; add --gate before a build starts
```

Never hand-edit `INDEX.md` or `OPEN.md`. The tools need PyYAML (`pip install pyyaml`).

## What goes where

| Thing | Id | Example | Its one home |
|---|---|---|---|
| Decision | `D-NNNN` when cited | `D-0050` | `decisions/0050-...md` |
| Activity | `ACT-NN` | `ACT-07` | `spec/stories.yaml` |
| Story | `US-NNN` | `US-031` | `spec/stories.yaml` |
| Object | `O-XXX` | `O-EST` estimate, `O-LI` line item | `spec/objects/<name>.md` |
| State | `ST-<object>-<state>` | `ST-EST-FINAL` | the object's file, lifecycle table |
| Action on an object | `A-<object>-<verb>` | `A-EST-FINALIZE` | the object's file, actions table |
| Field | `F-<object>-<name>` | `F-LI-UNIT-PRICE` | `spec/fields/<object>.yaml` |
| Rule | `R-<area>-NNN` | `R-FIN-002` | `spec/rules/<area>.yaml` |
| Screen, dialog or panel | `S-XXX` | `S-EST`, `S-FINWARN` | `spec/screens/S-XXX.md` |
| Control | `C-<control id>` | `C-top-finalize` | the controls table in its screen's file |
| Acceptance case | `AC-<area>-NN` | `AC-FIN-03` | the screen that owns it, or the rule's `cases:` |
| Edge case | `E-NNN` | `E-017` | `spec/edge-cases.yaml` |
| Wording | `W-<term>` | `W-LINE-ITEM` | `spec/wording.yaml` |
| Feature build note | `FT-<name>` | `FT-SAVE-UNDO` | `spec/features/FT-<name>.md` |
| Builder question | `Q-NN` | `Q-12` | `docs/builder/questions.md`, by its number |

Folders that come later: `flows/` (rough flows, phase 2), `samples/` (made-up estimates with expected totals, phase 4), `design/` and `screens/source/` (phase 5). `templates/` holds one blank of each kind; copy one to start a file.

Prose kinds (objects, screens, feature notes) are Markdown with a frontmatter block. Uniform kinds (stories, fields, rules, edge cases, wording) are YAML: a flat list, every record starting with `id:`, text in quotes, nothing clever.

## Rules for ids

- **An id never changes and is never reused.** A retired thing keeps its record with `status: retired`.
- **The part of a control id after `C-` is the id used in the built screen.** One name from sketch to code. It has at least two parts (`C-top-finalize`).
- **Anything written in the shape of an id is read as one**, anywhere in this folder, and must be defined. Do not write placeholder ids in real files. To point at something not written yet, give it a short record of its own with `status: open`; it then shows in `OPEN.md` until it is filled in.
- **Rule areas:** `SAVE`, `FIN` (finalize), `TAX`, `MKP` (markup), `CTG` (contingency), `PRC` (pricing a line item), `VSP` (vendor or sub pricing), `SCP` (scope), `QTY`, `CONF` (confidence), `VER` (versions), `TPL` (templates), `CLI` (client copy), `PRIV` (privacy).

## Status and where a line came from

- **Status, on every record:** `open` (not decided), `proposed` (the agent's recommendation, waiting on the owner), `locked` (decided, and cites the decision), `parked` (not in the first release, and says why), `retired`. A feature build note uses `options`, `decided` or `parked`. Controls, states and acceptance cases take the status of their file.
- **Provenance**, where a record carries it: `said`, `checked`, `inferred`, `proposed`, as in `AGENTS.md`.
- **Decisions link both ways.** A record cites `decisions: [D-0050]`. A decision file may carry one optional frontmatter line, `affects: C-top-finalize, R-FIN-001`; when it does, the checker makes sure both ends agree.

## What the checker fails on

The list is at the top of `tools/check_spec.py`, which is its one home. In short: an id defined twice or cited and defined nowhere; a field and a control that disagree about each other; an action with no home; a locked screen or rule missing its acceptance cases; a decision link that is one-sided, or points at a superseded decision; a generated page that is out of date. With `--gate` it also fails on anything in the first release that is still open.

Design and reasons: `docs/history/2026-11-19-method-audit/method-and-structure.md`, section 3.
