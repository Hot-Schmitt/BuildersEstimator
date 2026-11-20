# Repository audit: buildersestimator

Audited 2026-11-19 at commit `da2073a` (main, clean tree). Read only. Auditor had no project history.
Labels: **Checked** = I opened the file or ran the command. **Inferred** = my reading.

## Verdict in five lines

1. The decision records are the strongest part of this repository and should be kept as they are.
2. A new agent can find *what is decided* in about 3 steps. It cannot find *what is open* in one place (it is spread over at least 7 files) and it cannot build or review a screen from the repository alone (the drawings are not here and the one design document is knowingly stale).
3. Nothing exists yet that meets the owner's bar of "every button and field mapped, with logic and back end planned". Four of roughly twenty screens have a control table; no screen, story, rule, state or edge case has an addressable home except those 56 control ids and the decision numbers.
4. There is a "next" list but no phase path: no gates, no definition of done per phase, no feasibility step.
5. Two instruction sets are in force at once (the old claude.ai project instructions and `AGENTS.md`) and they disagree on where to start, where to log mistakes and where scripts live.

---

## 1. Cold start (audit question 1)

**Steps I took, following `AGENTS.md` literally**

| Step | Read | Lines | What I had after it |
|---|---|---|---|
| 1 | `AGENTS.md` | 74 | Purpose, 8 hard rules, privacy, how to record a decision |
| 2 | `STATUS.md` | 37 | Stage, next list, 10 "owed" items |
| 3 | `CURRENT.md` | 124 | Titles of 57 standing decisions |
| 4 | area decisions (`grep "area: screens"`) | 14 files | Screen decisions, but not the tax chip, finalize rules or review rules (filed under other areas) |
| 5 | `docs/standards.md`, `docs/method.md`, `docs/format.md` | 482 | The rules, with "doc NN" pointers to documents not here |
| 6+ | `docs/screens/*`, `docs/builder/questions.md`, the full review | 450 | The rest of what is open |

- **What is decided:** 3 steps. Good.
- **Why:** 4 steps (open the decision file). Good; the files are short and carry the rejected alternative.
- **What is open:** not answerable in one place. Open items live in `STATUS.md` (waiting, owed), `CURRENT.md` (proposed), `docs/format.md` section 10, `docs/screens/laptop-screens-design.md` sections 9 and 11, `docs/builder/questions.md` (48 questions, none answered), `docs/history/2026-11-19-full-review.md` (about 45 findings, tracked only by one blanket line at `STATUS.md:29`), and items marked Proposed inside `method.md`, `standards.md` and `reviewers.md`.
- **What to do next:** `STATUS.md:20` says "Design the back half of the estimate", with no brief, no list of outputs and no test for done.

**Contradictions, stale statements, dangling references (all Checked)**

| # | Where | Problem |
|---|---|---|
| C1 | `AGENTS.md:15` vs `STATUS.md:12` | AGENTS still says `CURRENT.md` "is not the full list" until the backfill is finished; STATUS says it is the full list. Stale clause. |
| C2 | `AGENTS.md:74`, `docs/standards.md:4`, `decisions/0003…:50` and `:100` | All point to `docs/history/mistakes.md`. The file does not exist (`STATUS.md:35` admits it). Decision 0003 says a mistake is "Recorded in" it; that is untrue today. `docs/standards.md:92` sends mistakes to "doc 07, section 8" instead. Three addresses, no file. |
| C3 | `AGENTS.md:34` | "The full set is `docs/method.md`. Where this file and that one differ, that one wins." Hard rules 7 and 8 (his habits; plans against past estimates) are not in `method.md` at all (grep finds neither). The pointer is wrong for two of the eight rules. |
| C4 | `README.md:17` | Says `docs/history/` holds "the old working log … and the record of mistakes". It holds one review file. |
| C5 | `README.md:18` vs `kit/` | Says `jobs/` holds per-job facts, costs and scores. `jobs/job-a/` holds only `.gitkeep`; the Job A data is in `kit/jobA_code_rows.json` and `kit/job_a_decisions.py`. |
| C6 | `README.md:20` vs `kit/test_*.py` | Says tests are in `tests/`. The real tests are two scripts in `kit/`; `tests/` holds a 20-line wrapper. |
| C7 | `decisions/0001…:15` | "as he types"; decision 0008 changed it to "when he leaves the box" (`STATUS.md:32` admits it). |
| C8 | `docs/format.md:11`, `:91` | "Every save makes a new version" still in the body, with a pointer to section 11. A reader must apply twelve overrides by hand. |
| C9 | `docs/screens/laptop-screens-design.md:43`, `:100-101`, `:135`, `:137`, `:173`, `:210`, `:212`, `:247-250` | Body contradicts decisions 0006, 0007, 0008 and lacks 0002 to 0005. The header (`:5-11`) lists this honestly, but the body is unpatched, and line 13 still calls the file "the build source". |
| C10 | `docs/method.md:113` | "A colored cell and a word on every line: green High, yellow Medium, red Low" sits under a note saying the screen shows two flags, off by default (decision 0045). Old text kept under a "Changed" banner. |
| C11 | `docs/standards.md:72-85`, `docs/reviewers.md:16-36`, decisions 0043 and 0055 | Reviewer roles exist three ways: four views, two lanes, five roles (`STATUS.md:30` admits it). |
| C12 | `docs/standards.md:19`, `kit/redaction.py:4-5`, `docs/format.md:137` vs `decisions/0059…` vs `STATUS.md:28` | Where the name list lives: "kept with the job's data" (three files) against "never saved … rebuilt each time" (decision 0059) against "exists nowhere now" (STATUS). |
| C13 | `docs/format.md:13` vs `kit/estimate_format.py:393-397` | Spec says files are "Stored compressed". `save()` writes plain JSON. Raised in the full review (engineer, item 8); still open. |
| C14 | `docs/standards.md:102` | "Hand-off steps are in doc 01." Doc 01 is not in the repository and `AGENTS.md` has no hand-off rule. Decision 0056 holds the rule, but nothing an agent reads at start tells it to hand off. |
| C15 | `docs/standards.md:7`, `:12`, `:18`, `:93` | "In force through project instructions version 1.1", "a line in doc 07", "redaction rules in the project instructions". The standards still take their authority from the old project. |
| C16 | `docs/method.md:4`, `docs/format.md:4` | Both say doc 06 is "to become `docs/builder/questions.md`". It already has. |
| C17 | "doc NN" references | `format.md` 21, `method.md` 12, `laptop-screens-design.md` 12, `standards.md` 9. They name docs 01, 02, 04, 05, 07 (five parts), 08, 11, 12, 14, 17, none of which are in the repository. 59 of 66 decision files also cite the old working log or "17 Current state" as their evidence. |
| C18 | `docs/format.md:140`, `kit/estimate_format.py:8`, `kit/write_draft.py:8`, `kit/job_a_decisions.py:6` and `:20-30`, `kit/make_job_docs.py:31-219` | Code comments and generated text still say "project doc 10", "03 Method", "doc 08", "doc 06". `make_job_docs.py` writes files named `04.md`, `05.md`, `11.md`. |
| C19 | `decisions/0026…` vs `STATUS.md:25` | Status is `accepted` and it is listed as standing, yet STATUS says the owner never locked it. A product behaviour decided by the agent is shown as standing. |
| C20 | `docs/screens/canvas.md:6` | The design document was written from an older canvas version; "what changed between the two was not checked". |
| C21 | Old project instructions v1.1 (visible in my session context) vs `AGENTS.md` | See finding 2 below. |

**Duplicated rules (same rule, several homes)**

- Saving rule: decisions 0001, 0008, 0050; `format.md` section 11 item 1; `standards.md:23`; `method.md:128`; `laptop-screens-design.md` section 8. Seven places, three wordings.
- Privacy rule: `AGENTS.md:36-40`, `README.md:34-36`, decision 0012, decision 0059, `standards.md:18`.
- Review process: `standards.md` section 4, decisions 0042, 0043, 0055, `reviewers.md`.
- Hard accuracy rules: `AGENTS.md:21-34`, `method.md:171-178`, and the old project instructions (14 rules against 8 here).
- Screen wording: `standards.md:53-57`, decision 0052, `laptop-screens-design.md` section 10.

---

## Findings, ranked by impact

### 1. No structure exists for the owner's goal: mapped screens, fields, stories, rules, states, edge cases (question 3)

**Found (Checked).** What has an addressable id today:

| Thing | Has ids? | Where | Coverage |
|---|---|---|---|
| Decisions | Yes, 0001-0066 | `decisions/` | Good |
| Controls | Yes, 56 ids | `laptop-screens-design.md` sections 5-7 | 4 screens of about 20; 13 controls point to something "not drawn"; 15 lines are still Proposed; body stale against 7 decisions |
| Builder questions | Yes, 1-48 | `docs/builder/questions.md` | Good, none answered |
| Format fields | Names only, one line each | `format.md` sections 2-3 | Version 0.4 only. For 0.5, "how each is held in the file is Claude's craft and is written here when 0.5 is built" (`format.md:156`) |
| Check rules | No ids | `format.md` section 4 (13 bullets) | Tests do not name the rule they prove |
| Screens | Letters A-D only | design doc section 2 | The other screens are 11 bullets (`:216-228`). The three "locked" earlier screens exist only as one paragraph in decision 0051; their sketches and control lists are not in the repository |
| User stories | None | "five tasks" are named in decision 0054, without ids | grep for "user stor", "edge case", "acceptance" returns nothing |
| States | Partly | estimate statuses in `format.md` section 5; per-control states in the design doc | No transition rules; the designer's list of missing states (full review 4.7) is tracked nowhere |
| Settings | None | mentioned in decisions 0003, 0009, 0045, 0046 | No list |
| Other data | None | | No spec for template, job record, plan-read result, pricing-document read, pricing request, price list, contacts copy, builder profile |
| Back end | None | | Stack, storage, save and undo undecided (`STATUS.md:21`) |

No control links to the field it reads or writes, the rule it triggers or the decision behind it. The link runs one way only, from prose to a decision number.

**Why it matters.** This is the owner's stated bar. Today a developer would have to decide dozens of things; the full review's own list of "what a builder of the software would still have to ask" (`2026-11-19-full-review.md:25`) runs to about 20 topics.

**Smallest fix (Proposed).** One `spec/` folder with four plain files and one checker. Do not build more than this.

- `spec/screens.md`: every screen, one row: id (`S-estimate`, `S-cost-summary`…), status (not drawn · rough · locked · built), link to its file.
- `spec/screens/<id>.md`: one table per screen: control id · label · does · states · field read or written · rule ids · decision numbers · edge cases. The existing 56 rows move here.
- `spec/stories.md`: `U-01…`, one line each (who, does what, done when), each listing the screens it crosses. Start with the five tasks.
- `spec/rules.md`: `R-001…` for every business rule and check rule, each with its decision number and the test that proves it.
- `tools/check_spec.py`: fails if an id is referenced and not defined, or a control has no field, rule or decision. This replaces a reviewer's cross-reading.

**Sequencing caution.** Decision 0011 (rough clickable version before any lock) is right. Writing control-level tables for every screen before that would repeat the "precision ahead of proof" mistake the designer found. Fill `screens.md`, `stories.md` and `rules.md` now; fill control tables per screen only as each is locked.

### 2. Two instruction sets are in force and they disagree

**Found (Checked for the repository side; the project side is what my session was shown).** The old project instructions v1.1 tell an agent to start from "01 Start here" and "07 Working log", log mistakes in "07 section 8", report under four fixed headers, and save every script into the project's `kit/` folder. `AGENTS.md` says start from `STATUS.md`, log to `mistakes.md`, and uses a different reply order. The project still lists its own copies of all the kit scripts, so there are two copies of each script, against `standards.md:10` ("one copy of each script"). `standards.md:7` still takes its authority from the project instructions.

Rules in the project instructions that never reached `AGENTS.md`: "Claude decides the craft … report notable calls", "new feature ideas are parked; keep the tool small", the Said / Checked / Inferred / Proposed labels (AGENTS has two of the four), the hand-off rule, "one step at a time; edit rather than regenerate", and "a job used to build the price list cannot test prices" (it is in `method.md` only).

**Why it matters.** Any session opened from the project gets both sets and must guess. This is the classic source of "documents that contradicted each other" that `standards.md:6` says the project was set up to avoid.

**Smallest fix.** Replace the project instructions with three lines: "The repository is the source. Read `AGENTS.md`. Project documents are frozen history as of (date)." Move the five missing rules into `AGENTS.md`. Delete or freeze the project's `kit/` copies.

### 3. No phase path, no gates, no feasibility step (question 2)

**Found.** `STATUS.md:18-22` is a four-item "next" list. The order of work is spread across decisions 0010, 0011, 0041, 0055. Nowhere does it say what each phase produces, who signs it off, or what must be true before the next one starts. Technical setup is item 3, after design, though the engineer reviewer found that format 0.5, saving and undo depend on it. The owner wants developers to answer only "feasible, yes or no"; no step, brief or record exists for that. Item 4 (more blind tests) depends on the builder sending jobs, and nothing records what has been asked of him or when.

**Why it matters.** Without gates, "locked" has no fixed meaning (the three "locked" screens of decision 0051 must all be redrawn), and screens can be locked before anyone has checked they can be built or that the builder's answers support them.

**Smallest fix.** One page, `docs/phases.md`, a table: phase · output (named files) · who decides · reviewer roles · gate to leave. Proposed phases: (1) records clean; (2) stories and screen inventory; (3) back half designed; (4) rough clickable version plus five tasks; (5) feasibility pass on stack, data and each screen; (6) lock per screen with its spec table; (7) format 0.5 written as one spec with sample files; (8) build with two review rounds. `STATUS.md` then names the current phase and nothing else.

### 4. The one screen document is knowingly wrong and the drawings are not in the repository

**Found.** See C9 and C20. `canvas.md:23-25` says the drawings can be read only from a session signed in to the owner's account. A reviewer or developer with the repository alone sees no picture, against decision 0042 ("a review counts only from rendered pictures"). The reason given for not copying (retyping 41 KB by hand) is about the tool, not the design.

**Why it matters.** An agent told to work on screens will read a 257-line document, then have to subtract seven decisions from it in its head. That is where repeated questions to the owner come from.

**Smallest fix.** Do not patch it line by line. Mark the file "superseded direction, do not build from" in its first line, move its 56 control rows into the `spec/screens/` tables (finding 1) with the seven decisions applied, and store a PNG of each drawing in `docs/screens/img/` at each lock. Pictures do not go stale the way copied code does.

### 5. Open items have no single list and the full review's findings are untracked

**Found.** About 45 findings in `docs/history/2026-11-19-full-review.md` are covered by one line (`STATUS.md:29`). Four became decisions (0009-0012). The rest (several bids per line, margin against markup, frozen first draft, tax rounding order, migration path, missing states, and so on) have no status. `STATUS.md` "Owed by the agent" already holds 10 items of mixed size.

**Why it matters.** The same findings will be re-found by the next review round at about 690,000 tokens a round, and re-asked of the owner.

**Smallest fix.** One file `OPEN.md` (or a table in `STATUS.md`): id · item · source · owner (owner / agent / builder) · blocks which phase · status. Seed it from the review, `format.md` section 10, the design doc sections 9 and 11, and the Proposed items. `STATUS.md` keeps only stage and next.

### 6. The builder's answers are the hidden critical path

**Found.** 48 questions, empty answers log (`questions.md:78-81`). Standing decisions rest on readings of one 2022 sheet: tax counted per division (0003), contingency by group (0004), markup on everything (0002), filing "by who does the work" (`format.md:126`). The pricing reviewer's point that his "contingency" may be a waste allowance, risking double counting, is unanswered. Questions 18 and 19 are out of date (`STATUS.md:37`). No record says which questions have been sent.

**Why it matters.** If he answers differently, decisions 0002 to 0004 and four of the twelve format changes move, after screens are drawn around them. This is the largest rework risk that no amount of agent work removes.

**Smallest fix.** Mark each question with the decision or phase it blocks, sort the ten that block design to the top, and put one line in `STATUS.md`: "sent to the builder on (date) / not sent". Mark decisions that rest on an unconfirmed reading with `assumes: Q41, Q42` in the frontmatter.

### 7. Rules are not in one place each; "Proposed" rules have no path to a decision

**Found.** See the duplicated-rules list above. Also: `method.md:6` is still "Status: Proposed"; pass marks are Proposed (`method.md:169`) with no decision file, though the reviewer asked for dollar-weighted marks; `reviewers.md:5` is Proposed; the four review views are Proposed (`standards.md:72`); the cost code picker is Proposed (`format.md:117`). Decision files 0061, 0063-0066 are proposed since Nov 16-18 with only a line in STATUS to move them. Decision 0026 is the reverse case (C19).

Who decides what is clear in spirit (`AGENTS.md:9`, `:61-70`; `reviewers.md:14`) but there is no single table, and the "agent decides the craft and reports it" half is missing from the repository.

**Smallest fix.** (a) One rule: a document states a rule only if it owns it; every other mention is a link. Owners: hard rules in `AGENTS.md`; estimating in `method.md`; build and review in `standards.md`; who reviews in `reviewers.md`. (b) A three-row table in `AGENTS.md`: owner decides (what the tool does, anything the builder sees, settings and defaults, the format contract) · agent decides and reports (wording, layout detail, test method, code structure) · reviewer comments only. (c) Every Proposed rule in a document gets a proposed decision file, so `CURRENT.md` is the one list awaiting a yes or no. (d) Batch proposed decisions to the owner as one numbered list; five process rules do not need five conversations.

### 8. Code layout will need a reshuffle before it can sit behind a web app (question 4)

**Found (Checked; tests run: `2 passed in 1.06s`; `build_index.py` ran clean and reproduced `CURRENT.md` byte for byte).**

- **Tracked cache files.** Four `.pyc` files are tracked though `.gitignore` lists them. Running the tests dirtied all four (I restored them). Commit `5dcddbf` left them in on purpose. Fix: `git rm --cached` once.
- **No dependency file.** `openpyxl` and `pytest` are needed and declared nowhere; no Python version stated (the cache files say 3.13).
- **Tests.** Two pytest items, each a subprocess running a whole assert script (`tests/test_kit_scripts.py:17-20`), so a failure says "script failed", not which rule. The format check and draft writer are well covered, including a 4,275-file damage sweep. No tests at all for `redaction.py` (the privacy gate), `import_builder_sheet.py`, `checklist.py`, `score.py`, `read_cost_workbook.py`, `make_job_docs.py` or `tools/build_index.py`. The importer and scorer need his real workbooks, which are not here, so no agent in this repository can re-run the "to the cent" proof in `STATUS.md:13`. Fix: a small made-up `.xlsx` fixture in his layout.
- **Job data beside code.** `kit/job_a_decisions.py` (412 lines, the largest file) is one job's judgement and plan facts written as code; `kit/jobA_code_rows.json` is one job's filing; the `JOB_A` block is inside the importer (`import_builder_sheet.py:31-47`) and is the default argument in `checklist.py:27`. Naming differs three ways: `jobA_`, `job_a_`, `jobs/job-a/`. Fix: move all three into `jobs/job-a/`.
- **Builder-specific choices hard-coded**, against decision 0009 (no profile file exists; grep finds none): sheet columns G and H and the "TOTAL - Division" and "Appliances → 17" patterns (`import_builder_sheet.py:49-50`, `:72-74`); division names (`:37-41`); `DEFAULT_FILING`, `PRICE_COLUMNS`, `UNIT_SPELLINGS` (`estimate_format.py:54-58`).
- **Defaults set in code without a recorded approval:** `DOUBT = {"low": 1.0, "medium": 0.5}` and `CHECK_FIRST_LINES = 10` (`write_draft.py:58-59`). `standards.md:17` says defaults go to the owner. Inferred: I found no decision for either.
- **Two scripts run at import with no functions to call:** `score.py` and `make_job_docs.py`. They cannot be tested or reused by a server.
- **Name-survival check exists twice and can be skipped.** `estimate_format.save(est, path, names=())` (`:386`) skips the check silently when the caller passes no names; `checklist.py:50` re-implements it; `read_cost_workbook.py:51`, `job_a_decisions.py:394` and `make_job_docs.py:122`, `:209`, `:230` write files with no check. `AGENTS.md:40` says "every writer uses it". Also `redact()` matches whole words while the survival check matches substrings, so a short listed name found inside an ordinary word would block every write (plausible, not reproduced).
- **Not a package.** `sys.path.insert` in four files; scripts called by path with `-I`.
- **`build_index.py`** stamps today's date into `CURRENT.md` (`:178`), so the file changes daily with no decision change; it does not validate `area` or `decided_by` values or that linked paths exist; nothing enforces "never hand-edit". No CI.

**Can it grow into a web app without a reshuffle?** No, but the reshuffle is small if done before more code lands: `src/estimator/` (format, draft, importers, redaction, scoring as importable modules with `main()` functions), `profiles/<builder>.json`, `jobs/<job>/`, real pytest files in `tests/`, a `pyproject.toml`. The format module is sound and is the piece to build the back end around; whether the back end is Python is still the owner's open decision.

**Privacy search (Checked by pattern; names not repeated here).**
- The builder's first name appears at `decisions/0009-this-builder-first-his-habits-kept-as-settings.md:33` and `:50`. `STATUS.md:34` knows about the quote on line 50 but not line 33.
- A named retail chain appears in the owner's quoted words at `decisions/0003-sales-tax-chip-on-line-items-with-a-material-price.md:87`. It is a hypothetical example, not one of the builder's vendors, but it is a vendor name by the letter of `AGENTS.md:38`. Owner's call.
- `README.md:3` and `AGENTS.md:7` give the builder's city and market; `docs/screens/canvas.md:5` holds a live link into the owner's account.
- Outside the files: commit author lines carry a personal name and a company email domain, and the remote carries an organisation name.
- No phone numbers, emails or street addresses matched. No person-like names in `kit/cost_codes.json`, `kit/jobA_code_rows.json` or `kit/job_a_decisions.py` by a capitalised-word scan.
- **Could not check:** whether a real vendor or sub name survives in his line wording. The name list "exists nowhere" (`STATUS.md:28`), so the automatic check the rule relies on cannot be run on what is in the repository today.

### 9. Decision records: good files, weak retrieval for someone working on one screen (question 5)

**Found (16 files read in full: 0001, 0003, 0009-0012, 0023, 0026, 0041, 0043, 0051, 0054, 0055, 0059, 0062, 0065).**

- Quality is high: specific decision, rejected alternative, cost, the owner's words. Titles read as the rule itself. Keep.
- **The area taxonomy misfiles screen behaviour.** `AGENTS.md:16` tells a screen worker to grep `area: screens` (14 files). That misses the Tax chip (0003, pricing), markup switch (0002, pricing), contingency in the cost summary (0004, pricing), Apply rules (0023, pricing), finalize warnings and blocks (0030, 0032, 0033, format), saving (0001, format), templates (0020, 0021) and all screen-review rules (0041-0043, process). One area per file is too coarse.
- `decisions/0000-template.md:15` and `build_index.py` allow any area string; no value check.
- Evidence for 59 files is the old working log, which is not in the repository (C17). If the project is retired before `docs/history/` is filled, the evidence chain breaks.
- Some decisions bundle several rules (0051 holds three screens; 0023 holds four rules; 0054 two tests), so "one decision, one file" is not quite true and a later reversal of one part will be awkward.
- No direct conflict between two standing decisions found in the sample. Conflicts are between decisions and documents (C7-C10).
- Is 66 files plus a generated index the right mechanism? Yes at this size. It stops scaling for a screen worker at roughly 150.

**Smallest fix.** Add one optional frontmatter line, `touches:`, holding screen ids, control ids and field names (for example `touches: S-estimate, li-tax, format.tax_rate`). Have `build_index.py` also write a per-screen list ("decisions touching S-cost-summary"). Add `assumes:` for builder questions (finding 6). Validate `area`. Drop the date stamp or use the newest decision date.

### 10. Reviewer briefs cover the last phase, not the next ones (question 6)

**Found.** `reviewers.md` has five roles, each one paragraph of questions. It is enough to run the same broad gut-check again. It is not enough for consistent, comparable reviews: no fixed input list per role, no output template with severity, no pass or fail line, no rule on what a reviewer may read (the builder persona should not read the decisions at all).

**Missing roles for the phases ahead (Proposed):**
1. **Story mapper.** Turns decisions and screens into the `U-` list and reports every story with no screen and every control with no story.
2. **Edge-case breaker.** Takes one screen spec and tries to break it: empty, huge, zero, negative, blank rate, final and read-only, two tabs, lost connection, undo after apply, 500 lines.
3. **Feasibility developer (front and back).** May answer only: feasible, feasible with this cost, or not feasible because. May not redesign. This is the owner's stated model and no brief exists.
4. **Builder-persona blind read.** Sees only pictures of the mock screens and the five tasks. No repository access. Reports where he stalls.
5. **Contract reviewer for the operations app**, when format 0.5 is written.

**Where usage could be replaced by a script or checklist.**
- The "new-chat reader" role (166k tokens last round) mostly found dangling references, stale lines and duplicates. A link-and-id checker (`tools/check_spec.py` plus a "doc NN" and missing-path grep) finds most of that for nothing. It would have found C1-C6 and C14-C18 in this audit.
- The self-check in `standards.md:66-70` (totals, duplicates, leftover files, folder size) should be one command.
- "Check a recommendation three ways" (0063), "walk the five tasks" (0065) and "carry earlier fixes" (0066) are checklists, not decisions; put them in one pre-show checklist the orchestrator ticks.
- Two-lane screen reviews on text descriptions are spent usage: the Nov 19 round ran with no reviewer seeing a picture (`full-review.md:4`), which by decision 0042 does not count.

---

## The five things most likely to cause rework or repeated questions (question 7)

| Rank | Risk | Smallest fix |
|---|---|---|
| 1 | Screens get locked on readings of one 2022 sheet before the builder answers (tax, contingency, markup, filing) | Tag the blocking questions, send them, and record `assumes:` on decisions 0002-0004 (finding 6) |
| 2 | Agents work from the stale design document or from the old project instructions, and re-ask what was decided | Freeze the project instructions to a pointer; retire the design document into per-screen spec tables with the seven decisions applied (findings 2 and 4) |
| 3 | No home for stories, rules, fields and edge cases, so each is re-derived per session and developers end up deciding | The four-file `spec/` skeleton and its checker (finding 1) |
| 4 | Technical base decided after design; format 0.5, saving and undo then force screen changes | Add the feasibility gate and move the stack options ahead of any lock (finding 3) |
| 5 | Open findings and Proposed rules sit in seven places; each review round re-finds them at high cost | One `OPEN.md` and a proposed decision file for every Proposed rule (findings 5 and 7) |

## What I could not check

- The claude.ai project documents (working log parts, docs 01-17) and whether the backfilled decisions match them.
- The design canvas drawings; no rendered screen was seen.
- The importer, scorer, checklist and document maker against real workbooks (the files are not in the repository).
- Whether any real vendor or sub name survives in line wording (no name list exists).
- Repository access settings on the host.
- I read 16 of 66 decision files in full and the front matter of all 66.

## What is good and should be kept as is

- **The decision file shape**: decision, why, considered instead, what it costs, his words. The "what it costs us" section is unusually honest. Do not change it.
- **Never-deleted, superseded-both-ends decisions**, with `build_index.py` checking the chain and refusing to write on an error.
- **`STATUS.md` naming its own debts**, including the files that do not exist. Most projects hide these.
- **`kit/estimate_format.py`**: one way in (`fill_totals`, `save`), a check that cannot be crashed, totals always recomputed. This is the right core for a back end.
- **The split of fixed steps in code and judgement in a decisions file** (`write_draft.py` and the per-job decisions input).
- **Tests on made-up data**, and the rule that blind-test answers stay out of what a run reads.
- **Decisions 0010 and 0011**: design the back half, then try a rough clickable version, before any lock.
- **The hard rules** (blank over invented, a source on every quantity, his prices only) and the `Said / Checked / Inferred / Proposed` labels.
- **`docs/builder/questions.md`** as the one place for facts only the builder knows, with new questions tied to decision numbers.
- **The reviewer ground rules** (`reviewers.md:7-14`): start cold, report only, say what could not be checked.
