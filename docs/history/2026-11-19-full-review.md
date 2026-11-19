# Full review before the move, Nov 19, 2026

**Purpose:** the record of the one-time gut-check review the owner asked for before the rest of the project moves into this repository. Five fresh reviewers, no chat history, briefs in `docs/reviewers.md`. Findings are the reviewers' own and are **not yet decisions**; each is either fixed, or put to the owner, before it is closed.
**Limits:** no reviewer saw a rendered screen (descriptions and drawing code only), and none ran code. By `docs/standards.md` this does not count as the visual review of any screen.
**Usage:** about 690,000 tokens across the five reviewers (166k, 120k, 127k, 126k, 150k).
**References:** "doc NN" is a project document not yet in this repository.

## The short version (the orchestrator's reading, Inferred)
1. **The core idea holds.** All five would keep: blank over invented, a source on every quantity, totals that say what they leave out, decisions recorded with the rejected alternative.
2. **The records are not ready for a build.** `CURRENT.md` holds 8 decisions; doc 17 holds roughly 40 more. Rules, open questions and "what is next" are still only in the old project.
3. **The back half of an estimate is not designed:** what the client receives, allowances, alternates, competing sub bids, revisions.
4. **The technical base is undecided:** how an AI read reaches the screen, the stack, where data lives, saving and undo.
5. **Proof is thin:** one job, no longer blind, measured quantities 22% low, prices untested.
6. **Much is shaped around one builder's sheet** and would need to be settings to suit a general builder.

## 1. New-chat reader (records and readiness)
1. `CURRENT.md` says it holds every standing decision but holds 8. Doc 17 carries roughly 40 more (service model, laptop-first, templates, two confidence flags, finalize rules, vendor pricing rules, lasting ids, reading stays a Claude step). Backfill before retiring doc 17, or say the backfill is incomplete in the generated header.
2. No home for "where we are, what is next, what is open". Add one status file; record open owner questions as proposed decisions and list them in `CURRENT.md`.
3. The privacy rule conflicts. Docs 01, 14 and 17 lock "no real or redacted job data goes in" the repository; `AGENTS.md` and README allow the builder's cost figures and a `jobs/` folder, citing a Nov 18 approval with no decision file. Record that decision, and say where blind-test answers sit so a blind run cannot open them.
4. The screen build source is stale and not in the repository. Doc 16 contradicts decisions 0006, 0007 and 0008 and lacks the Tax chip, division tax line, cost summary switch and contingency by group. Doc 17 has the old Tax chip rule. Decision 0001 still says "as he types". Correct doc 16 as it moves into `docs/screens/` and bring the canvas code with it.
5. `format.md` is 0.4 with twelve changes layered on top. Write 0.5 as one clean spec before building.
6. Rules lost or duplicated in the move: accuracy rules 13 (his habits beat the drawn minimum) and 14 (flag plan-versus-estimate conflicts) are in neither `AGENTS.md` nor `method.md`; also absent are "nothing reaches the builder without the owner's OK", "no sharing the Claude account" and the hand-off rules. Reviewer roles exist three ways (`standards.md` four views, two lanes, `reviewers.md` five roles). `AGENTS.md` cites files that do not exist yet (`questions.md`, `mistakes.md`, `kit/redaction.py`).
7. Only in the old project, at risk: doc 14's click-through table and its Medium and Low proposals; working log parts 1 to 5 with open review findings; docs 06 and 11; the kit files; the Proposed process rules.

**What a builder of the software would still have to ask the owner:** where the editing screen lives, the stack, how local data is stored and backed up; how Claude's reading result reaches the screen; every undrawn screen (cost summary, three lists, search, add line item, removed list, settings, version history, Duplicate choice, template actions, cost code picker, the three earlier screens); the settings list and defaults; the theme; how the estimated range and "dollars × doubt" are calculated; file shapes for templates, job, pricing and request records and the price list; what happens to the 0.4 tax lines; client view, print and Excel layouts; how signing happens and how the file reaches the operations app; alternates and allowances; how deep undo goes; the mail program and contact export format.

**Thinking about it right?** Mostly yes. The bigger risk is scope: documents, contacts and email are a second product beside estimating, while quantities fail and prices are untested.

## 2. General builder (not this builder)
Gut answer: would trust it as a draft and probably enjoy the pricing part; would not yet trust it to get an estimate to a client, because the back half of the job is not designed.
1. Nothing shows what the client gets: no proposal view, no choice of what the client sees, no exclusions or terms. Draw the client-facing output before building.
2. Allowances and client selections have no home on screen. Add an "Allowance" mark on a line item and an allowance list on the output.
3. One markup on everything will not suit most builders. At a minimum, a "no markup" switch per line item.
4. Sub pricing is one number per line item. In practice two or three bids per trade arrive over a week or two, each with exclusions and an expiry. Allow several bids per line item with one chosen.
5. Finalized is frozen but estimates get revised. Nothing shows what changed between versions; no alternates (add or deduct).
6. Cannot see how a quantity was built: wants the math and a waste percent he can set.
7. Tax, contingency and the material/labor split are shaped around one builder's sheet: blank rates block finalizing even for builders who never carry them; contingency by group is unusual; the Tax chip taxes a number he cannot see. Let a builder switch each off in settings.
8. Small annoyances: three pricing buttons with similar names; stepping through 12 divisions with no all-on-one-page view; no cost per square foot; no copy and paste of several line items and no scratch math in a box; "Your own number" unclear beside "Lump sum"; cost codes in every line item's details is bookkeeping, not estimating.

Simple or busy? Mostly simple. The left column is the busy spot at 768 high. "Needs your decision" and "Double-check these first" sound alike.

## 3. Pricing and estimating checker
1. "80% done" is counted in lines, not dollars or time. Score by dollars filled and correct, and by his minutes to finish.
2. Testing cannot yet support trust: one job, no longer blind, prices untested, High marks untested, no renovation; scoring against his estimate inherits his slips and cushions. Require three or more blind jobs including a renovation, scored against actual cost, with dollar-weighted pass marks.
3. Biggest accuracy risk: his habits, learned from one sheet. His "contingency" (20% framing, 33% siding material) looks like a waste allowance stacked on quantities already 15 to 45% over plan; if buying rules are learned and those percents stay, overage is counted twice. Ask him what each percent is for; keep waste, contingency and cushion as separate named things.
4. Stale prices will be invisible: 2022 prices are Medium at best and Medium is not shown. Show price age independently of the flags, with an escalation method he approves.
5. Totals walk, three undefined cases: the order of tax and contingency on the same lines; per-line tax rounded to cents may not equal his three tax rows (sum unrounded, round per group); a dollar markup leaves an included alternate or late line with no markup. No double counting found in the main chain.
6. Allowances, alternates and the client view are thin: the client view hides markup, so markup must be spread into the prices shown and no rule says how; an allowance needs a stated client-facing amount.
7. Markup versus margin: a 25% markup is a 20% margin; show both.
8. The saving rule loses the baseline: freeze the tool's draft as an unchangeable version 1. Add a price date and "valid until" at Finalize.
9. Applied sub bids need inclusions, exclusions and expiry recorded.
10. Method contradictions: the "suggested cushion" percents in step 1 are invented numbers (label them outside reference); the range has no method; general conditions have no job-duration fact to drive them.

For a general builder the core would work. Tied to this builder and belonging in a per-builder profile: the three price columns and filing by column; tax counted inside divisions; contingency as a percent of material groups; one markup on everything; "only his prices", which leaves a builder with no price history starting from nothing.

## 4. Designer
1. Most of the main tasks have no laptop screen. Four drawings exist (one division, Details, Remove, the Finalize warning). Draw the cost summary first.
2. No single source shows the current design: the design document differs from the canvas in 12 places and from the newer decisions in at least six; the earlier sketch uses different sizes again. Redraw once, put one source in the repository, retire the rest.
3. Details probably covers the numbers it edits at 1366 wide. Push the list, or narrow the panel.
4. Every line item is still a spreadsheet row: two boxes, Details, trash, soon a Tax chip. Show borders, Details and trash on hover or focus, or move Remove into Details.
5. Unclear labels and controls: "Enter price" on a sub bid; "Lump sum" versus "Your own number"; "By the square foot" for linear feet; "Undo" does not say what; the version pill looks like a status; Esc inside Details; the top bar holds about ten items.
6. Where he lands first is not recorded, and "Needs your decision" has no designed way to answer.
7. Missing states: before the plans are read; empty division; no search matches; invalid entry; could not save; long names; read-only final; flags on; pricing requested; loading; print, client copy and phone.
8. No component system yet: cut to about six type sizes and three radii, name the components once.

Process: precision is being written ahead of proof. Build one rough clickable prototype on made-up data from start to finalize, run the five tasks on it, then lock and write the system once.

## 5. Engineer (front end, back end, where AI fits)
1. The hand-off from an AI read to the screen is not designed. Define two small read-result formats (plan read, pricing read) with their own checks; each entry carries its evidence and each file a run record; key them to lasting line ids.
2. The stack, where data lives and how the screen saves are undecided, and format 0.5 depends on them. Totals and the check exist only in Python. Suggested: a small local Python service that owns compute, check and save, with a thin screen.
3. Autosave and undo need more than the current change list: entries have no id, order or group; save overwrites in place. Route every edit through one "apply change" function with an inverse; write to a temporary file, then rename.
4. The format has no upgrade path and no way to share the contract: add a migration step per version; publish made-up sample files with expected totals and refusals as the contract test; define how a signed file is delivered, acknowledged, refused and re-sent.
5. Real-service files conflict with the redaction guard: split a private job record from the estimate file, or make test and live modes explicit. No backup is recorded.
6. Checking the AI's work is thin where it failed: add a cheap second independent read for the top-dollar lines only, compared in code. Measure cost per estimate on the next run. Check that running a paid service on a personal subscription is allowed.
7. Builder-specific choices are hard-coded: move them to one builder profile file now.
8. Repository gaps: `kit/` and `tests/` empty; the test file reads the command line on import and will likely fail under pytest; the format document says files are stored compressed but save writes plain text.

## Change log
| Date | What changed |
|---|---|
| Nov 19, 2026 | New document. The five reports, lightly shortened, with the orchestrator's short version |
