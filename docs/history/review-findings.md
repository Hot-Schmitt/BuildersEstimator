# Review findings: where each one stands

**Purpose:** one status for every finding in the two reviews of Nov 19, 2026, so nothing in them is forgotten or found again by the next review. The reviews themselves are not changed: `2026-11-19-full-review.md` and the three reports in `2026-11-19-method-audit/`.
**Written:** Nov 20, 2026 (phase 0, step 4). Every "Fixed" was checked against the repository on that day (Checked). Readings of which phase owns a finding are the agent's (Inferred).
**Keeping it current:** when a parked finding is dealt with, change its status here and say where. A finding leaves this page only by getting a status, never by being deleted.

## The status words

| Status | Means |
|---|---|
| **Fixed** | Done in the repository. The note says where. |
| **Decision NNNN** | The owner decided it; the decision file is the record. |
| **Question N** | Only the builder knows. It is in `docs/builder/questions.md` under that number. |
| **Parked** | Not now, on purpose. The note names the phase that owns it (decision 0067) and why it waits. |
| **Owner** | A small call that is the owner's alone and is not tied to a phase. Listed in `STATUS.md`, "Waiting on the owner". |

"Test track" means the blind accuracy testing that runs beside the phases and waits on more finished jobs from the builder. "Code tidy" means the kit clean-up owed in `STATUS.md`, done before phase 4 picks the technical base.

## The count

| | Fixed | Decision | Question | Parked | Owner | Total |
|---|---|---|---|---|---|---|
| Full review | 8 | 7 | 5 | 33 | 1 | 54 |
| Repository audit | 24 | 6 | 0 | 25 | 3 | 58 |
| Method audit, gaps and contradictions | 10 | 2 | 0 | 16 | 0 | 28 |
| **All** | **42** | **15** | **5** | **74** | **4** | **140** |

A finding with two parts takes the status of the part still open, and the note says what is already done. The same problem often appears in more than one review; each mention has its own row so every review can be traced, and the note points to the first row.

---

## 1. Full review (`2026-11-19-full-review.md`)

The "short version" at its top is a summary of the findings below and has no rows of its own.

### 1.1 New-chat reader

| Id | Finding | Status | Note |
|---|---|---|---|
| FR-1.1 | `CURRENT.md` held 8 decisions, not all of them | Fixed | 72 decision files; `CURRENT.md` is the full list |
| FR-1.2 | No home for where we are, what is next, what is open | Fixed | `STATUS.md`; proposed decisions are listed in `CURRENT.md` |
| FR-1.3a | Privacy rule conflicted, with no decision file | Decision 0012 | Replaces 0057 |
| FR-1.3b | Say where blind-test answers sit so a blind run cannot open them | Decision 0062 | |
| FR-1.4 | Screen build source is stale and the drawings are not in the repository | Parked | Phase 5. Done so far: the design document says "do not build from this" and lists where it is behind; decision 0001 no longer says "as he types". Its control lists move to `spec/screens/` with the decisions applied, and the drawing source is copied in at lock |
| FR-1.5 | Format is 0.4 with twelve changes layered on; write 0.5 clean | Parked | Phase 4 (decision 0040). Depends on the technical choices made there |
| FR-1.6a | Hard rules on his habits and on plan-against-estimate conflicts were in neither file | Fixed | `AGENTS.md` rules 7 and 8; `docs/method.md`, "What the tool must never do" |
| FR-1.6b | Missing: nothing reaches the builder without the owner's OK, no account sharing, hand-off rules | Fixed | `AGENTS.md`, "Working with the owner" |
| FR-1.6c | Reviewer roles existed three ways | Fixed | `docs/reviewers.md` is the one home; `docs/standards.md` section 4 points to it |
| FR-1.6d | `AGENTS.md` cited files that did not exist | Fixed | `docs/builder/questions.md`, `docs/history/mistakes.md` and `kit/redaction.py` all exist |
| FR-1.7 | Material only in the old project and at risk | Parked | Done: questions, kit and the process rules are in. Left: the cost code list document, the old working log (five parts) and the screens self-review. `STATUS.md`, "Still open from the move"; not needed for phases 0 to 2 |
| FR-1.8 | The list of what a builder of the software would still have to ask the owner (about twenty topics) | Parked | This list is the work of phases 1 to 5. Each topic becomes records in `spec/`: objects and file shapes (1), client view, signing, allowances, alternates (2), undrawn screens (3, 5), stack, storage, read hand-off, undo (4), settings and defaults, range method (5) |
| FR-1.9 | Documents, contacts and email are a second product beside estimating | Parked | Phase 1. The owner approves what is in the first release from the story map; decision 0019 stands until then |

### 1.2 General builder

| Id | Finding | Status | Note |
|---|---|---|---|
| FR-2.1 | Nothing shows what the client gets | Decision 0010 | Designed in phase 2. What he sends a client today: Question 49 |
| FR-2.2 | Allowances and client selections have no home on screen | Parked | Phase 2 (decision 0010). His practice: Question 12 |
| FR-2.3 | One markup on everything; wants at least a "no markup" switch per line item | Parked | Phase 2. Decision 0002 parked per-line-item markup. What he passes through unmarked: Question 43 |
| FR-2.4 | Sub pricing is one number per line item; real jobs get several bids | Question 51 | Design waits in phase 2 on his answer; decision 0022 stands until then |
| FR-2.5 | Nothing shows what changed between versions; no alternates | Question 50 | Alternates: Question 50. Revisions: Question 52. Designed in phase 2 |
| FR-2.6 | Cannot see how a quantity was built; wants a waste percent he can set | Parked | Phase 1 shows who figures each quantity (decision 0070); hard rule 3 keeps a source on every quantity. His waste figures: Questions 14 and 34 |
| FR-2.7 | Tax, contingency and the split are shaped around one builder; let each be switched off | Decision 0009 | His habits are settings in one builder profile. A typed zero satisfies a rate he does not carry (decisions 0033, 0053). The profile file itself is built with the code tidy |
| FR-2.8 | Small annoyances: similar button names, stepping through divisions, no cost per square foot, no multi-copy, unclear "Your own number", cost codes in Details | Parked | Phase 3. They are tried on the rough clickable version, where they can be felt and not argued |
| FR-2.9 | Left column busy at 768 high; "Needs your decision" and "Double-check these first" sound alike | Parked | Phase 3 for the layout; the two labels go into the first wording table in phase 1 |

### 1.3 Pricing and estimating checker

| Id | Finding | Status | Note |
|---|---|---|---|
| FR-3.1 | "80% done" is counted in lines, not dollars or his time | Parked | Test track. Done: every score report leads with dollars on the blind-measured lines (decision 0061). His time today: Question 21. Minutes-to-finish is first measured by the timed test in decision 0071 |
| FR-3.2 | Testing cannot yet support trust: one job, no longer blind; pass marks not dollar-weighted | Parked | Test track. Waits on more finished jobs (Question 4). The pass marks in `docs/method.md` are still Proposed and go to the owner when the second job is scored |
| FR-3.3 | His "contingency" percents may be a waste allowance, so overage could be counted twice | Question 53 | With Questions 10, 34 and 44. Until he answers, an oddity is flagged, not treated as his rule (decision 0060) |
| FR-3.4 | Old prices will be invisible; show a price's age | Parked | Phase 2, once phase 1 has named the price record. How he refreshes prices: Questions 3 and 7 |
| FR-3.5 | Three undefined cases in how totals add up (tax with contingency, tax rounding, dollar markup and late lines) | Parked | Phase 4, written into format 0.5 with sample files that prove it. His order of tax and markup: Question 40 |
| FR-3.6 | Client view hides markup, with no rule for spreading it; allowances need a client-facing amount | Parked | Phase 2 (decision 0010) |
| FR-3.7 | Show margin as well as markup | Parked | Phase 2, with the cost summary |
| FR-3.8 | Keep the tool's first draft as an unchangeable version 1; add a price date and "valid until" at Finalize | Parked | Phase 4 for the frozen first draft (it is part of saving and versions); phase 2 for "valid until" |
| FR-3.9 | Applied sub bids need inclusions, exclusions and expiry | Question 51 | Designed in phase 2 |
| FR-3.10a | The "suggested cushion" percents in the method are invented numbers | Fixed | Nov 20: labelled "outside reference, not the builder's figure" in `docs/method.md`, step 1 |
| FR-3.10b | The estimated range has no method | Parked | Phase 5: written as a rule with test cases before any screen that shows it is locked |
| FR-3.10c | General conditions have no job-duration fact to drive them | Question 54 | With Questions 11 and 15 |
| FR-3.11 | Parts tied to this builder belong in a per-builder profile | Decision 0009 | |

### 1.4 Designer

| Id | Finding | Status | Note |
|---|---|---|---|
| FR-4.1 | Most main tasks have no laptop screen; draw the cost summary first | Parked | Phase 3 (rough, clickable), then phase 5 (real size) |
| FR-4.2 | No single source shows the current design | Parked | Phase 5: one source per screen in `spec/screens/`. Done so far: the design document is marked as behind |
| FR-4.3 | Details probably covers the numbers it edits at 1366 wide | Parked | Phase 3 trial |
| FR-4.4 | Every line item is still a spreadsheet row | Parked | Phase 3 trial. Decision 0044 is the bar it is judged against |
| FR-4.5 | Unclear labels and controls | Parked | Phase 1 starts the wording table (`spec/wording.yaml`); sources are checked in phase 5 (decision 0052) |
| FR-4.6 | Where he lands first is not recorded; "Needs your decision" has no way to answer | Parked | Phase 1 (the story map covers the whole journey) |
| FR-4.7 | Missing whole-screen states (empty, loading, error, read-only and more) | Parked | Phase 5. The screen template now requires them (`spec/templates/screen.md`) |
| FR-4.8 | No component system | Parked | Phase 5, once, after the clickable trial |
| FR-4.9 | Precision is being written ahead of proof; build one rough clickable version first | Decision 0011 | |

### 1.5 Engineer

| Id | Finding | Status | Note |
|---|---|---|---|
| FR-5.1 | The hand-off from an AI read to the screen is not designed | Parked | Phase 4. Decision 0027 keeps reading a Claude step until then |
| FR-5.2 | Stack, where data lives and how the screen saves are undecided | Parked | Phase 4, from options with a recommendation |
| FR-5.3 | Autosave and undo need more than the current change list | Parked | Phase 4 |
| FR-5.4 | No upgrade path between format versions, no shared sample files, no delivery steps for a signed file | Parked | Phase 4, with format 0.5 |
| FR-5.5 | Real-service files conflict with the redaction guard; no backup recorded | Parked | Phase 4, with storage |
| FR-5.6a | Add a cheap second read for the top-dollar lines; measure cost per estimate | Parked | Test track, on the next blind run |
| FR-5.6b | Check that running a paid service on a personal subscription is allowed | Owner | It is the owner's account and agreement (decision 0013) |
| FR-5.7 | Builder-specific choices are hard-coded | Decision 0009 | The profile file is built with the code tidy |
| FR-5.8a | `kit/` and `tests/` were empty; the test file would fail under pytest | Fixed | Eleven scripts in `kit/`; `python3 -m pytest tests/` passes |
| FR-5.8b | The format says files are stored compressed; the code writes plain text | Parked | Phase 4, settled when 0.5 is written (`STATUS.md`) |

---

## 2. Repository audit (`2026-11-19-method-audit/repository-audit.md`)

### 2.1 Contradictions and dangling references

| Id | Finding | Status | Note |
|---|---|---|---|
| RA-C1 | `AGENTS.md` still said `CURRENT.md` was not the full list | Fixed | |
| RA-C2 | Three addresses for mistakes, and no file | Fixed | `docs/history/mistakes.md` exists and is the one home |
| RA-C3 | `AGENTS.md` says `method.md` wins, but two hard rules were not in it | Fixed | Same as FR-1.6a |
| RA-C4 | `README.md` described history that was not there | Fixed | |
| RA-C5 | `README.md` described `jobs/` as full; Job A data sits in `kit/` | Parked | Code tidy moves the Job A files into `jobs/job-a/`. Done: `README.md` says the folder is empty for now |
| RA-C6 | `README.md` said tests are in `tests/`; they are in `kit/` | Fixed | `README.md` now says so |
| RA-C7 | Decision 0001 said "as he types" | Fixed | |
| RA-C8 | `format.md` body still says every save makes a version | Parked | Phase 4: the body keeps version 0.4 until 0.5 replaces it in one step (decision 0040) |
| RA-C9 | The design document body contradicts seven decisions | Parked | Same as FR-1.4 |
| RA-C10 | `method.md` still described colored cells under a "Changed" banner | Fixed | The old text is gone |
| RA-C11 | Reviewer roles three ways | Fixed | Same as FR-1.6c |
| RA-C12 | Three stories about where the name list lives | Fixed | All now say: never saved here, rebuilt each time (decision 0059). Rebuilding the list itself is RA-8l |
| RA-C13 | "Stored compressed" against plain text | Parked | Same as FR-5.8b |
| RA-C14 | No hand-off rule an agent reads at start | Fixed | `AGENTS.md`, "Working with the owner" |
| RA-C15 | `standards.md` took its authority from the old project instructions | Fixed | |
| RA-C16 | Two files said the questions document was still "to become" | Fixed | |
| RA-C17 | "doc NN" references to documents not in the repository | Parked | Cut from 54 to 32. The rest cite the old working log as evidence and are fixed when it is moved in |
| RA-C18 | Code comments and generated text cite project document numbers | Parked | Code tidy (`STATUS.md`) |
| RA-C19 | Decision 0026 stood without the owner's lock | Decision 0072 | Replaced on Nov 19 |
| RA-C20 | The design document was written from an older canvas version, never compared | Parked | Phase 5: the drawings are redrawn and their source copied in at lock, so the comparison stops mattering |
| RA-C21 | The old project instructions are still in force beside `AGENTS.md` | Owner | Repository side fixed: `AGENTS.md` says it is the only instruction set. The owner replaces the project's instructions with a pointer (`STATUS.md`) |
| RA-D | The same rule stated in several homes (saving, privacy, review, hard rules, wording) | Fixed | `AGENTS.md`, "Where things are recorded": a document states a rule only if it owns it. The saving wording left in the format and design documents is RA-C8 and RA-C9 |

### 2.2 Findings 1 to 7

| Id | Finding | Status | Note |
|---|---|---|---|
| RA-1 | No structure for mapped screens, fields, stories, rules, states, edge cases | Decision 0067 | The empty `spec/` folder, its templates and its checker were set up on Nov 20; phases 1 to 5 fill it |
| RA-2a | Rules in the old instructions that never reached `AGENTS.md` | Fixed | Craft calls, parked ideas, the four labels, hand-off, one step at a time are in. "A job that built the prices cannot test them" is decision 0062 |
| RA-2b | Replace the project instructions with a pointer; freeze the project's copies of the scripts | Owner | Same as RA-C21 |
| RA-3 | No phase path, gates or feasibility step | Decision 0067 | |
| RA-4 | The one screen document is knowingly wrong; keep a picture of each drawing at lock | Parked | Same as FR-1.4, phase 5 |
| RA-5 | Open items have no single list; the full review's findings are untracked | Fixed | This page for review findings; `spec/OPEN.md` for the specification; `STATUS.md` for the rest |
| RA-6a | The builder's answers are the hidden critical path | Decision 0069 | |
| RA-6b | Mark each question with what it blocks; record what has been sent; mark decisions that rest on an unconfirmed reading | Parked | Done on Nov 20: each question placed, with what it holds up and a "Sent" column (`docs/builder/questions.md`, "The sort"). Left: the `assumes:` mark on decisions 0002 to 0004, added when the builder answers items C and D or phase 1 opens, whichever is first |
| RA-7a | One owner per rule | Fixed | Same as RA-D |
| RA-7b | Say who decides what | Fixed | `AGENTS.md`: the owner decides what the tool does; the agent decides craft and reports it |
| RA-7c | Rules marked Proposed inside documents have no path to a decision (the method's own status, pass marks, reviewer briefs, "premium", the cost code picker) | Parked | Each is put to the owner in the phase that first relies on it: pass marks on the test track, the picker and "premium" in phase 5, reviewer briefs with RA-10a |
| RA-7d | Batch proposed decisions to the owner | Fixed | Done Nov 19 for 0061 and 0063 to 0066 |

### 2.3 Finding 8: code layout

| Id | Finding | Status | Note |
|---|---|---|---|
| RA-8a | Cache files tracked by git | Fixed | None tracked now |
| RA-8b | No dependency file | Fixed | Nov 20: `requirements.txt` |
| RA-8c | Seven kit scripts have no tests, the privacy gate among them; the importer cannot be re-proved without his workbooks | Parked | Code tidy (`STATUS.md`). A made-up workbook in his layout is the fix |
| RA-8d | One job's data and judgement sit beside the code, named three ways | Parked | Code tidy. Same as RA-C5 |
| RA-8e | Builder-specific choices hard-coded; no profile file | Parked | Code tidy. Decision 0009 sets the direction |
| RA-8f | Two defaults set in code with no recorded approval (how doubt is weighted, ten lines in "check these first") | Parked | Phase 5: both become records in `spec/` with status proposed, so they reach the owner through `spec/OPEN.md` |
| RA-8g | Two scripts run on import with nothing to call | Parked | Code tidy |
| RA-8h | The name check is written twice, can be skipped silently, and several writers do not use it | Parked | Code tidy, and before any job is imported again (`STATUS.md`) |
| RA-8i | Not a package | Parked | Code tidy, shaped by the phase 4 choice of technical base |
| RA-8j | `build_index.py` stamps the date, does not check the area word, nothing enforces "never hand-edit" | Parked | Code tidy. Small |
| RA-8k | Privacy: the builder's first name in decision 0009 | Fixed | No match in the repository |
| RA-8l | Privacy: could not check whether a vendor or sub name survives in his line wording, because the name list exists nowhere | Parked | Test track: the list is rebuilt from his two workbooks and kept outside the repository (`STATUS.md`). It matters more while the repository is public |
| RA-8m | Privacy: a retail chain is named in the owner's quoted words in decision 0003 | Fixed | Kept as it is, by the owner (Said, Nov 20): it is his own made-up example, not one of the builder's vendors, and his words stay exact |
| RA-8n | Privacy: city and market in `README.md` and `AGENTS.md`; a link into the owner's account in `canvas.md`; a personal name and company email on commits | Owner | These matter only while the repository is public (`STATUS.md`) |

### 2.4 Findings 9 and 10

| Id | Finding | Status | Note |
|---|---|---|---|
| RA-9a | Searching decisions by area misses screen behaviour filed elsewhere | Fixed | `AGENTS.md` step 4 says to search `CURRENT.md` by keyword too |
| RA-9b | Nothing links a decision to the screens, controls and fields it governs | Fixed | Optional `affects:` line on a decision, checked both ways by `tools/check_spec.py` |
| RA-9c | The area word is not checked | Parked | Same as RA-8j |
| RA-9d | Evidence for 59 decisions is the old working log, which is not here | Parked | Same as FR-1.7 |
| RA-9e | Some decisions bundle several rules (0023, 0051, 0054) | Parked | Split only when one part is reversed; splitting now would renumber nothing and gain nothing |
| RA-10a | Reviewer briefs have no fixed inputs, output shape or pass line; five roles for the coming phases are missing | Parked | Each role is written when its phase starts: story mapper (1), feasibility-only developer (2), builder blind reader (3), edge-case breaker and contract reviewer (5) |
| RA-10b | Much of the new-chat reader's work could be a script | Parked | Done for `spec/` (`tools/check_spec.py`). A check for missing paths and "doc NN" in `docs/` comes with the code tidy |
| RA-10c | The self-check should be one command | Parked | Code tidy |
| RA-10d | Rules 0063, 0065 and 0066 are checklists, not decisions | Decision 0063 | The owner approved them as decisions (0063, 0065, 0066) on Nov 19 |
| RA-10e | Screen reviews run on text descriptions do not count | Decision 0042 | Already the rule |

The audit's closing table ("the five things most likely to cause rework") repeats RA-6, RA-2 with RA-4, RA-1, RA-3 and RA-5.

---

## 3. Method audit (`2026-11-19-method-audit/method-and-structure.md`)

Sections 1 to 5 of that report are proposals, not findings. The owner took the phases and the `spec/` folder as decision 0067. Its storage advice (section 5.5, ten points to settle early) is input to phase 4 and is tracked there as one row, MS-G3. The market research is evidence, not findings; what it changed is decision 0068.

### 3.1 Gaps (its section 6.2)

| Id | Finding | Status | Note |
|---|---|---|---|
| MS-G1 | Only the estimate has a defined shape | Parked | Phase 1 names the objects; phase 5 completes their fields |
| MS-G2 | The back half is undesigned | Decision 0010 | Phase 2 |
| MS-G3 | The technical base is undecided | Parked | Phase 4, with the ten early storage points of section 5.5 |
| MS-G4 | Format 0.5 is 0.4 plus layered changes | Parked | Same as FR-1.5 |
| MS-G5 | No evidence from the builder on any screen; 48 questions unanswered | Decision 0069 | And the test track |
| MS-G6 | 4 of about 20 screens drawn; the design document is behind; the source lives outside the repository | Parked | Phases 3 and 5. Same as FR-1.4 |
| MS-G7 | Nothing has an address except decisions and controls | Fixed | The `spec/` id scheme and checker (decision 0067). Filling it is phases 1 to 5 |
| MS-G8 | No whole-journey map, no edge-case register, no tracker for review findings | Parked | Phase 1 for the map and the register (blank templates exist). The tracker is this page |
| MS-G9 | Reviewer roles three ways; none is feasibility-only or an edge-case breaker | Parked | One set is fixed (FR-1.6c). The missing roles are RA-10a |
| MS-G10 | One price box over three stored price columns, with no decision | Parked | Phase 2, as an owner decision with options. Listed in `STATUS.md`, "Owed by the agent" |
| MS-G11 | Wording table unverified | Parked | Phase 5 |
| MS-G12 | No tokens or component list | Parked | Phase 5. Same as FR-4.8 |
| MS-G13 | The redaction name list exists nowhere | Parked | Same as RA-8l |

### 3.2 Contradictions and duplicates (its section 6.3)

| Id | Finding | Status | Note |
|---|---|---|---|
| MS-X1 | `AGENTS.md` against `method.md` on two hard rules | Fixed | Same as FR-1.6a |
| MS-X2 | Stale caveat about `CURRENT.md` | Fixed | Same as RA-C1 |
| MS-X3 | `mistakes.md` did not exist | Fixed | Same as RA-C2 |
| MS-X4 | `standards.md` pointed to project documents for mistakes, hand-off and its own authority | Fixed | The two "doc 07" mentions left are in its change log, as history |
| MS-X5 | Standards want the drawing's code kept; `canvas.md` keeps it out. "Which wins" said three ways | Parked | Phase 5 copies the source in at lock. The order is now said once: decisions, then the design document, then the canvas |
| MS-X6 | Saving wording in three versions | Parked | Decision 0001 is fixed. The design document's body is FR-1.4 |
| MS-X7 | `format.md` describes two versions at once | Parked | Same as RA-C8 |
| MS-X8 | Decimals: the design document's body is behind decision 0007 | Parked | Same as FR-1.4; flagged in its header |
| MS-X9 | Duplicate: the design document's body is behind decision 0006 | Parked | Same as FR-1.4; flagged in its header |
| MS-X10 | Reviewer roles, three sets | Fixed | Same as FR-1.6c |
| MS-X11 | Two homes for tests | Fixed | Same as RA-C6 |
| MS-X12 | Tracked build leftovers | Fixed | Same as RA-8a |
| MS-X13 | `jobs/job-a/` is empty while `README.md` described it as full | Fixed | `README.md` says it is empty for now. Moving the data is RA-C5 |
| MS-X14 | `STATUS.md` said decision 0009 quoted the builder's first name | Fixed | Same as RA-8k |
| MS-X15 | Scope drift: documents, contacts and email | Parked | Same as FR-1.9 |

## Change log
| Date | What changed |
|---|---|
| Nov 20, 2026 | New document (phase 0, step 4). Same day: RA-8m closed by the owner's answer |
