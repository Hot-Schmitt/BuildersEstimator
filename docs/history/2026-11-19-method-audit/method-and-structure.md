# Method audit: from locked mock screens to "build can start with no re-deciding"

**Purpose:** answers six questions for the owner of the estimating helper: which practices to use, the phases from today to a build-ready specification, the exact documentation layout and templates, the agent roles, where data should live, and what the repository is missing today.
**Date:** 2026-11-19. **Basis:** a read of the repository (AGENTS.md, STATUS.md, CURRENT.md, README.md, docs/standards.md, docs/reviewers.md, docs/format.md, docs/screens/, docs/history/2026-11-19-full-review.md, decisions 0000, 0010, 0011, 0041, 0050, 0054, 0065, the layout of decisions/, kit/, tests/, tools/) plus web sources, each given with its URL and date. Nothing in the repository was changed.
**Labels:** "Checked" = seen in the repository or on a cited page. "Judgement" = my own view. The owner's ideas (including JSONB) are treated as context, not requirements.

**The one-paragraph answer (Judgement).** The repository already has the hardest habit right: one decision per file with the rejected alternative, a generated index, a hard rule that totals are recomputed in code, and fresh reviewers. What it lacks is a *specification with addresses*. Decisions say why; nothing yet says, in one findable place each, what every screen, control, field, state and rule *is*. Add a small `spec/` folder with ids and a checker script, fill it in five short phases that end in a cold-reader test, keep estimates as JSON files behind one storage module, and skip most named methodologies beyond the six listed below.

---

## 1. Methodology: what fits, what is overkill

### 1.1 The test I applied (Judgement)
A practice earns its place here only if it (a) removes a question a building agent would otherwise have to ask the owner, (b) can be written and checked by agents without the owner in the loop, and (c) costs less to keep current than the rework it prevents. The owner pays per token, so every standing document is a recurring cost: agents re-read it each session.

### 1.2 Comparison

| Practice | What it gives | Fit here | Verdict |
|---|---|---|---|
| **User story mapping** (Patton): a backbone of activities left to right, tasks under each, sliced into releases | The whole journey on one page, so missing steps are visible; a natural build order | High. The only workflow definition today is "five tasks" (decision 0054), all inside one screen. The full review found the flow "stops at Finalize" | **Use, small.** One file, about 10 activities and 40 to 60 stories. No workshop, no sticky notes |
| **Jobs-to-be-done** | Why the user "hires" the tool; guards against feature creep | Low marginal value. The job is already stated in one sentence in AGENTS.md ("drafts about 80% of his estimate... flags what it is not confident about") | **Skip the method.** Keep one job statement per persona (builder, owner-as-operator, client receiving the estimate) at the top of the story map |
| **Shape Up pitches** (problem, appetite, solution, rabbit holes, no-gos; source: basecamp.com/shapeup/1.5-chapter-06, read 2026-11-19) | A bounded write-up per feature with explicit exclusions | Partial. Cycles, betting tables and team hand-offs do not apply to one owner and agents. Three parts are valuable: *appetite* (the owner wants a small tool), *rabbit holes* and *no-gos* | **Borrow three fields** into the per-feature build note (section 3.7). Skip the rest |
| **Spec-driven development with AI agents** (GitHub Spec Kit: constitution, specify, plan, tasks; source: developer.microsoft.com/blog/spec-driven-development-spec-kit, 2025-09-15. Kiro: requirements, design, tasks. Critique: Böckeler, martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html, 2025-10-15) | Spec written before code and used to steer agents. Spec Kit separates "what and why" from technology choices, which matches the owner's rule that developers do not decide | High in principle; the tools as shipped are a poor fit. Böckeler found Spec Kit produced many verbose, repetitive Markdown files per feature, that agents still ignored or over-applied instructions, and that one fixed workflow did not suit different problem sizes. She distinguishes spec-first, spec-anchored (spec kept and maintained) and spec-as-source (humans never touch code) | **Use the idea, not the tooling.** Aim for *spec-anchored*: the spec is kept and maintained and wins over code. Do not install Spec Kit or Kiro (they would create a second structure beside `decisions/`). Do not attempt spec-as-source |
| **AGENTS.md convention** (agents.md, read 2026-11-19: plain Markdown, no required fields, nearest file in the tree wins, stewarded under the Linux Foundation) | A known place agents read first | Already used and well written | **Keep.** Add nested `spec/AGENTS.md` and `kit/AGENTS.md` only if the root file passes about 150 lines |
| **Architecture decision records** | Why a choice was made, and what lost | Already in place (`decisions/`, 66 files), better than most teams' | **Keep unchanged.** Add one frontmatter line, `affects:`, listing spec ids (section 3.2) |
| **Domain-driven design** | Ubiquitous language; a domain model; (full DDD adds bounded contexts, aggregates, events) | The language part is essential: the code says `line`, `ml`, `builder_editing`; the screen says "line item", "Finalize"; decisions say "lock". The model part is essential too: only the estimate has a defined shape | **Use two pieces only:** a wording table that maps screen word, code name and meaning; an object model. Skip aggregates, bounded contexts, event storming |
| **State machines for lifecycles** | Every status, every allowed move, who may make it, what blocks it | High. The estimate has four statuses in the format and several screen behaviours hang on them (read-only on final, buttons off, blank-rate block). A pricing document, a pricing request and a plan read each have a lifecycle nobody has written | **Use.** A transitions table per object, not a diagram tool. This is the cheapest way to find edge cases |
| **Given / When / Then acceptance criteria** | Testable behaviour in plain words; maps one to one onto automated tests | High for rules and for controls that change data. Low for labels and layout. Böckeler's "4 stories and 16 criteria for a small bug" is the warning | **Use, rationed:** only on controls that change data or state, and on every rule. Plain text; no Cucumber or BDD tooling |
| **Design tokens and a component inventory** (W3C community group format, first stable version 2025-10-28; source: w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version) | One written set of spacing, type, colour, radius; a named list of parts | Needed (standards.md asks for "one set... written down once") but **late**. The designer reviewer found precision was being written ahead of proof | **Use after the rough clickable version, once.** One `tokens.json` in the community-group shape and a component list of about a dozen parts. No token build pipeline |
| **Object-oriented UX** (ORCA: objects, relationships, calls to action, attributes; source: blog.logrocket.com/ux-design/object-oriented-ux-ooux, 2025-03-03) | Starts from the things the user handles, lists what can be done to each, then draws screens | High, and it is the same artefact as the domain model. It answers "what does every button do" from the object side: every call to action on an object must appear as a control somewhere, or be deliberately absent | **Use, merged with the domain model.** One file per object: relationships, fields, actions, lifecycle |
| **Requirement traceability** | Proof that every requirement is designed, built and tested | The classic hand-kept matrix is overkill and goes stale. The need is real: the owner wants "every field... a note you can easily access" | **Use as ids plus a checker script, never as a hand-kept matrix.** The index is generated, the way CURRENT.md is |
| **Risk-first prototyping** | Spend first on what could sink the product | Already decided (0011). The riskiest things are not on screen, though: measured quantities ran 22% low and prices are untested (full review) | **Keep 0011.** Add: the prototype also carries the riskiest *flow* (applying vendor or sub pricing; finalize; the client copy), not only the estimate grid |
| **Golden-file and contract tests** | Sample files with known answers that any reader must reproduce or refuse | High. The format is a contract with a second app; totals exist only in Python; the engineer reviewer asked for exactly this | **Use.** A folder of made-up sample estimates with expected totals and expected refusals. This is the most valuable test asset in the project |

### 1.3 The recommended small set (Judgement)
1. **A story map** on one page (journey and build order).
2. **An object model with lifecycles** (OOUX and the two useful pieces of DDD, as one artefact).
3. **A spec with addresses**: screens with control tables, a field dictionary, a rules list, an edge-case register, a wording table, all with ids, checked by a script, index generated.
4. **Given / When / Then**, only on rules and on controls that change data.
5. **Decision records** as they are, plus a short "options for the build" note per feature where there is a real choice.
6. **Golden sample files** as the contract test, and the **rough clickable version** before any lock.

Tokens and the component list come once, after the clickable version.

### 1.4 What to skip, and why
- Jobs-to-be-done interviews, forces diagrams, opportunity trees: the job is known; the missing evidence is the builder using it, not a framework.
- Shape Up cycles and betting; sprint ceremonies; estimation points.
- Spec Kit, Kiro or similar tooling; "specs as source" where code is never touched.
- Full DDD; event storming; UML; C4 diagrams beyond one boxes-and-arrows picture of the parts.
- BDD tooling (Cucumber, Gherkin runners). Plain pytest named by acceptance id is enough.
- A hand-maintained traceability matrix; a separate product requirements document (the story map plus the spec is that document).
- Pixel tables for screens before the clickable version has been tried (already recognised in decision 0011).
- A token build pipeline (Style Dictionary and the like), a component library site, visual regression tooling. Revisit only if a second product shares the design.
- Personas beyond two short paragraphs. A persona agent is a reviewer, not evidence (section 4.3).

---

## 2. Phases from today to "build can start with no re-deciding"

Where the repository is (Checked, STATUS.md): moving in from a claude.ai Project; nothing of the screens built; one job tested and no longer blind; five decisions proposed and waiting; review findings unanswered; next steps are finish the move, design the back half (0010), rough clickable (0011), technical setup, more blind tests.

The phases below keep that order and add what is missing: a records clean-up first, a map before drawing, and a readiness gate at the end. **Owner decisions are batched: one batch per phase, numbered options with a recommendation, so a "yes 1, 2, 4" is enough.** Blind accuracy testing (STATUS item 4) runs as a separate track beside these phases; it does not gate the screen specification, but it does gate anything reaching the builder as a real estimate.

### Phase 0 · Close the records and lay the skeleton
- **Purpose:** remove known contradictions so nothing is specified on top of them; create the empty `spec/` structure and its checker.
- **Inputs:** STATUS.md "Owed by the agent"; the full review; section 6 of this report.
- **Outputs:** the five proposed decisions answered; `docs/history/review-findings.md` (every review finding with a status: fixed, decision NNNN, question N, parked with reason); one set of reviewer roles (`docs/reviewers.md` wins, `standards.md` section 4 points to it); AGENTS.md and method.md agreeing on the hard rules; `spec/README.md` (id scheme and templates); `tools/check_spec.py` and `tools/build_spec_index.py` running on an empty spec; `docs/history/mistakes.md` created.
- **Who decides:** owner, on the five proposed decisions and decision 0026 only. Orchestrator on everything else (it is record-keeping).
- **Exit test:** a fresh "new-chat reader" finds no two documents in conflict and no file named that does not exist; `python3 tools/check_spec.py` exits clean.
- **Must not happen:** drawing screens; starting the prototype; rewriting documents that phase 4 will replace (the laptop design document is marked historical, not edited).

### Phase 1 · Map the whole job and name the things
- **Purpose:** agree what the tool covers from "a job arrives" to "the signed estimate is in the operations app and later revised", and what objects exist, before any more drawing.
- **Inputs:** decisions; method.md; format.md; the full review sections 2 and 3; docs/builder/questions.md.
- **Outputs:** `spec/stories.yaml` (the story map, each story marked skeleton, first release, later, or not doing); `spec/objects/*.md` (one per object: relationships, actions, lifecycle table; fields named but not yet detailed); `spec/wording.yaml` first pass; additions to `docs/builder/questions.md`.
- **Who decides:** owner on scope (which stories are in the first release; the "not doing" list). Orchestrator on structure and naming of ids. The estimating checker reviews; it does not decide.
- **Exit test:** every decision in CURRENT.md that describes behaviour is attached to at least one story or object; every action on every object is marked "has a home", "deliberately none" or "open"; the owner has approved the release slice in one reply.
- **Must not happen:** screen layouts; technology choices; inventing how the builder works (those become questions).

### Phase 2 · Design the back half, rough (decision 0010)
- **Purpose:** decide how the client copy, allowances, client selections, alternates, more than one bid per line item, and revisions between versions behave, at the level of objects, rules and rough flows.
- **Inputs:** phase 1 outputs; the builder's answers where available (what he sends a client today is a fact only he has).
- **Outputs:** updated objects and lifecycles; `spec/rules/*.yaml` entries for the new behaviour, marked proposed; `spec/features/FT-*.md` notes for each area with options; rough flows (boxes and arrows, or fat-marker sketches) under `spec/flows/`; edge cases added to `spec/edge-cases.yaml`.
- **Who decides:** owner, per feature, from options with a recommendation. The estimating checker and the builder-persona reader comment. Feasibility reviewers say only "simple / moderate / hard, and why".
- **Exit test:** each of the five back-half areas has either an accepted decision, a "not in first release" marking, or a named question to the builder that blocks it; no line-item behaviour is left that could change the estimate screen later.
- **Must not happen:** real-size drawings; locking any screen; guessing the builder's client paperwork. If his answers are not in, the area is designed to the point where his answer picks between two prepared options.

### Phase 3 · Rough clickable version, and try it (decision 0011)
- **Purpose:** find out whether the flow works when clicked, before precision is written.
- **Inputs:** stories marked skeleton and first release; objects; made-up data (decision 0064, if accepted).
- **Outputs:** a throwaway clickable version in `prototype/` (its README says in the first line that it is disposable and is never the build base); `docs/history/YYYY-MM-DD-clickable-trial.md` recording each story walked, where it stalled, and what changed; changes fed back into stories, objects, rules and edge cases.
- **Who decides:** owner on what he saw (he clicks it himself). With his OK, the builder tries it once (section 4.3). Orchestrator on how it is built.
- **Exit test:** the five tasks and every first-release story can be completed without help by the owner, and by the builder if the owner has allowed the session; each stall is fixed or recorded as an edge case or decision.
- **Must not happen:** real job data; real arithmetic re-implemented in the prototype beyond what is needed to click through (totals may be canned); polish; the prototype's code being carried into the build; treating the prototype as the specification.

### Phase 4 · Technical options (STATUS "technical setup")
- **Purpose:** choose the stack, where data lives, how a plan read and a pricing read reach the screen, and how saving and undo work.
- **Inputs:** phase 3 findings; section 5 of this report; the engineer's findings in the full review.
- **Outputs:** `spec/features/FT-STORAGE.md`, `FT-READ-HANDOFF.md`, `FT-SAVE-UNDO.md`, `FT-STACK.md`, each with two or three options, cost in build time, what each makes harder, a recommendation; then one decision file each. `docs/format.md` rewritten as version 0.5 in one clean specification (owed already), with `spec/samples/` golden files.
- **Who decides:** owner, from the options. Front-end and back-end reviewers give feasibility and build-time only. Orchestrator recommends.
- **Exit test:** a fresh engineer reviewer can answer "where is each object stored, how is it written safely, how is it upgraded, how does the other app verify a file" from the documents alone; the 0.5 samples pass and fail as expected under the shared check.
- **Must not happen:** building the app; choosing hosting, sign-in or multi-builder features (deferred, section 5.6); changing the format without the owner's OK and a version number.
- **Note (Judgement):** the research for this phase can run beside phase 3, because the prototype does not depend on it. The *decisions* are taken after phase 3, because what the trial shows about saving, undo and applying pricing changes the answer.

### Phase 5 · Lock and write the specification
- **Purpose:** turn what survived the trial into the build source.
- **Inputs:** everything above.
- **Outputs:** every first-release screen drawn at real size and locked (decision 0041), with its `spec/screens/S-*.md`; `spec/fields/*.yaml` complete; `spec/rules/*.yaml` with every rule accepted or parked; `spec/edge-cases.yaml` with no open item on a first-release story; `spec/wording.yaml` with sources; `spec/design/tokens.json` and `spec/design/components.md`; the locked drawing source copied into `spec/screens/source/` with checksums (the canvas stops being the only copy at this point).
- **Who decides:** owner locks each screen and each owner-level rule. Orchestrator decides craft and reports notable calls. Reviewers: two-lane screen review from rendered pictures at three widths; estimating checker on rules and totals; QA breaker on edge cases; feasibility reviewers mark each control and rule simple, moderate or hard.
- **Exit test:** `check_spec.py` passes with zero open items in the first-release slice; every control in a locked drawing has a row, and every row a control; every data-changing control has acceptance cases; every field shown on a screen is in the dictionary.
- **Must not happen:** new features (they go to "later" in the story map); silent rule changes (a rule changes only through a decision file); reviewers setting defaults.

### Phase 6 · Build-readiness gate
- **Purpose:** prove "no re-deciding" before spending on the build.
- **Inputs:** the locked spec.
- **Outputs:** `docs/build-plan.md`: thin slices in build order, each naming the story ids, screen ids, rule ids and acceptance ids it delivers and the test that proves it; the first slice is a walking skeleton (create an estimate from a template, edit one price, see the total, finalize) end to end on the real storage and the real shared check. `docs/history/YYYY-MM-DD-readiness.md`.
- **Who decides:** owner gives the go. Orchestrator writes the plan.
- **Exit test (the cold-reader test):** three fresh agents, each given only AGENTS.md and one slice, each write the list of questions they would have to ask the owner before building it. The gate passes when the lists are empty, or contain only items the owner agrees are build-time craft. Any real question is answered in the spec, not in chat, and the test is re-run for that slice only.
- **Must not happen:** starting the build "to see"; answering a cold reader's question only in conversation.

**What this costs (Judgement).** Phases 0 and 1 are a few sessions. The expensive ones are 3 and 5. Review rounds run about 85,000 to 125,000 tokens per reviewer by the repository's own figures (standards.md section 7), and the full review used about 690,000. Section 4.4 gives a rule for when a review is worth that.

---

## 3. Documentation structure: one home per thing, findable by id

### 3.1 Format: Markdown, data files, or both? (Recommendation: both, split by kind)

| Kind of thing | Count expected | Shape | Recommended form | Why |
|---|---|---|---|---|
| Decisions | 66 and growing | Argument in prose | **Markdown with frontmatter** (as now) | The reasoning is the content |
| Objects, screens, feature build notes | About 10, 20 and 10 | Prose plus a few tables | **Markdown with frontmatter**; tables with fixed column names so the checker can read them | Agents and the owner both read them; a screen's layout and states need sentences |
| Fields, rules, edge cases, wording, stories | About 150, 80, 100, 60, 60 | Many uniform small records | **YAML data files**, one record per id | Uniform records are where prose drifts. A data file can be checked, sorted, filtered ("every open edge case on the finalize flow") and, later, *used by the app itself*: field help text, validation limits and on-screen labels can be read from the same file, so the note the owner wants on every field is the note the user sees |
| Indexes | 2 | Lists | **Generated Markdown**, never hand-edited | Same rule as CURRENT.md |

Considered and not recommended (Judgement):
- **Everything in Markdown.** Easiest to read on GitHub, but 150 fields in tables with eleven columns are hard for an agent to edit without breaking a row, and cannot feed the app.
- **Everything in JSON or YAML.** Easy to check, but screen behaviour and option write-ups read badly as data, and the owner cannot skim them.
- **JSON for the data files.** No extra dependency, but no comments and noisy to edit by hand. **TOML** is a fair alternative (Python 3.13, which this machine runs, reads it from the standard library). YAML is recommended because agents write it reliably and it is the common choice; it costs one dependency (PyYAML). If the "no dependency for housekeeping" stance in `tools/build_index.py` matters more, use TOML with the same record shapes. This is the orchestrator's craft call, not the owner's.

Rules for the YAML so it stays checkable: a flat list of records; every record starts with `id:`; plain keys; text values in quotes; no anchors or clever features.

### 3.2 The id scheme

| Thing | Id form | Example | Home (the one place it is defined) |
|---|---|---|---|
| Decision | `D-NNNN` when cited; the file keeps its number | `D-0050` | `decisions/0050-...md` |
| Story | `US-NNN` | `US-031` | `spec/stories.yaml` |
| Object | `O-XXX` | `O-EST` estimate, `O-LI` line item | `spec/objects/<name>.md` |
| State | `ST-<object>-<state>` | `ST-EST-FINAL` | the object's file, lifecycle table |
| Action on an object | `A-<object>-<verb>` | `A-EST-FINALIZE` | the object's file, actions table |
| Field | `F-<object>-<name>` | `F-LI-UNIT-PRICE` | `spec/fields/<object>.yaml` |
| Rule | `R-<area>-NNN` | `R-FIN-002` | `spec/rules/<area>.yaml` |
| Screen (or dialog, panel) | `S-XXX` | `S-EST`, `S-FINWARN` | `spec/screens/S-XXX.md` |
| Control | `C-<existing control id>` | `C-top-finalize` | controls table in its screen's file |
| Acceptance case | `AC-<area>-NN` | `AC-FIN-03` | the screen or rule that owns it |
| Edge case | `E-NNN` | `E-017` | `spec/edge-cases.yaml` |
| Wording | `W-<term>` | `W-LINE-ITEM` | `spec/wording.yaml` |
| Feature build note | `FT-<name>` | `FT-SAVE-UNDO` | `spec/features/FT-<name>.md` |
| Builder question | `Q-NN` | `Q-12` | `docs/builder/questions.md` (numbers as they are) |

Conventions:
- **Ids never change and are never reused.** A retired thing keeps its record with `status: retired`.
- **The part of a control id after `C-` is the id used in the built screen** (the element's test id). The design document already names controls this way (`top-finalize`, `li-(id)-price`, `fin-anyway`); keep those names. One name, from sketch to code.
- **Areas for rules** follow the decision areas where possible: `SAVE`, `FIN` (finalize), `TAX`, `MKP` (markup), `CTG` (contingency), `PRC` (pricing a line item), `VSP` (vendor or sub pricing), `SCP` (scope), `QTY`, `CONF` (confidence), `VER` (versions), `TPL` (templates), `CLI` (client copy), `PRIV` (privacy).
- **Status on every record:** `open` (not decided), `proposed` (agent's recommendation, awaiting owner), `locked` (decided; cites the decision), `parked` (not in first release; says why), `retired`.
- **Provenance on every record**, keeping the repository's own labels: `said`, `checked`, `inferred`, `proposed`.
- **Linking to decisions, both ways.** Spec records cite `decisions: [D-0050, D-0032]`. Decision files gain one optional frontmatter line, `affects: C-top-finalize, R-FIN-001, R-FIN-002`. The checker confirms both ends agree, the way `build_index.py` already checks both ends of a supersede chain (Checked: lines 86 to 125 of that script).
- **Finding anything:** `grep -rn "F-LI-UNIT-PRICE" spec/ decisions/` returns the home and every use. The generated `spec/INDEX.md` gives id, title, status and file on one line each, so an agent reads one line and opens one file.

### 3.3 The file layout

```
spec/
  README.md               how to read this folder, the id scheme, status words (short)
  INDEX.md                GENERATED: every id, title, status, home file
  OPEN.md                 GENERATED: everything open or proposed = the owner's queue
  stories.yaml            US-  the story map: activities, stories, release slice
  wording.yaml            W-   screen word, code name, meaning, never-say, source
  edge-cases.yaml         E-   the register
  objects/                O-, ST-, A-   one file per object
    estimate.md  line-item.md  template.md  job.md  job-document.md
    pricing-document.md  pricing-request.md  contact.md  cost-code.md
    price-record.md  plan-read.md  builder-profile.md
  fields/                 F-   one data file per object (the data dictionary)
    estimate.yaml  line-item.yaml  ...
  rules/                  R-   one data file per area
    finalize.yaml  saving.yaml  tax.yaml  markup.yaml  ...
  screens/                S-, C-, AC-   one file per screen, dialog or panel
    S-EST.md  S-DETAILS.md  S-FINWARN.md  S-COSTSUM.md  ...
    source/               locked drawing code, with checksums (from phase 5)
  features/               FT-  options considered for the build, one per feature
  flows/                  rough flows from phase 2 (pictures or text)
  design/
    tokens.json           after the clickable trial, once
    components.md         the named parts, about a dozen
  samples/                golden files: made-up estimates + expected totals / refusals
  templates/              the blank templates below
tools/
  build_index.py          as now (decisions -> CURRENT.md)
  build_spec_index.py     spec -> spec/INDEX.md and spec/OPEN.md
  check_spec.py           broken references, orphans, missing parts (section 3.11)
prototype/                phase 3 only; throwaway; removed after phase 5
docs/                     as now: method.md, format.md, standards.md, reviewers.md,
                          builder/questions.md, history/
```

What moves: `docs/screens/laptop-screens-design.md` becomes history once its control tables are split into `spec/screens/`; its wording table becomes `spec/wording.yaml`. `docs/format.md` stays the contract; field *meanings* move to `spec/fields/`, and format.md keeps structure, versioning and the check, citing `F-` ids, so a field is described once.

### 3.4 Template and example: story map (`spec/stories.yaml`)

Template:
```yaml
jobs:            # one sentence per persona, replaces a JTBD exercise
  - who: ""
    job: ""
activities:      # the backbone, in the order the work happens
  - id: ACT-NN
    name: ""
stories:
  - id: US-NNN
    activity: ACT-NN
    who: ""              # builder | owner-as-operator | client
    story: ""            # "<who> can <do> so that <why>"
    slice: ""            # skeleton | first | later | not-doing
    screens: []          # S- ids
    actions: []          # A- ids
    acceptance: []       # AC- ids
    decisions: []
    status: ""           # open | proposed | locked | parked
    note: ""
```

Example:
```yaml
jobs:
  - who: "builder"
    job: "Get from a set of plans to an estimate I trust enough to send, in minutes not days, without changing how I price."
activities:
  - id: ACT-07
    name: "Finish and finalize"
stories:
  - id: US-031
    activity: ACT-07
    who: "builder"
    story: "The builder can finalize an estimate that still has unpriced line items, after a warning, so that a missing sub bid does not hold up the client."
    slice: "skeleton"
    screens: [S-EST, S-FINWARN]
    actions: [A-EST-FINALIZE]
    acceptance: [AC-FIN-01, AC-FIN-02, AC-FIN-03]
    decisions: [D-0032, D-0033, D-0050]
    status: "locked"
    note: "Unpriced line items are listed on the estimate as not included."
```

### 3.5 Template and example: object with lifecycle (`spec/objects/<name>.md`)

Template:
```markdown
---
id: O-XXX
name:
status: open | proposed | locked
decisions: []
---
## What it is
One paragraph. What the user would call it (W- id).

## Relationships
| Relates to | How | Note |

## Actions
Every action a person or the system can take on it. Each has a home, or says why not.
| Id | Action | Who | Allowed in states | Home control(s) | Rules | Status |

## Lifecycle
| State id | Name on screen | Meaning | Who may edit |

| From | Action | Guard (rules) | To | Side effects |

## Stored
Where it lives and in what form (points to format.md section or FT- note). Fields: `spec/fields/<name>.yaml`.

## Open points
```

Example (shortened), `spec/objects/estimate.md`:
```markdown
---
id: O-EST
name: Estimate
status: proposed
decisions: [D-0001, D-0018, D-0032, D-0033, D-0050]
---
## What it is
One priced version of a job's cost, made of line items in the builder's divisions and groups, with a cost summary. Screen word: W-ESTIMATE.

## Relationships
| Relates to | How | Note |
|---|---|---|
| O-JOB | belongs to one | A job has many estimate versions |
| O-LI | has many | In the builder's order |
| O-TPL | made from at most one | Recorded on the estimate (format 0.5, item 6) |

## Actions
| Id | Action | Who | Allowed in states | Home control(s) | Rules | Status |
|---|---|---|---|---|---|---|
| A-EST-FINALIZE | Finalize | builder | ST-EST-EDITING | C-top-finalize | R-FIN-001, R-FIN-002, R-FIN-003 | locked |
| A-EST-DUPLICATE | Duplicate, with or without data | builder | any | C-top-duplicate | R-VER-002 | locked |
| A-EST-REOPEN | Reopen a final estimate | none | none | deliberately none: a final version is never changed; he duplicates instead | R-VER-001 | locked |
| A-EST-SIGN | Record the client's signature | OPEN | ST-EST-FINAL | OPEN (not drawn) | OPEN | open |

## Lifecycle
| State id | Name on screen | Meaning | Who may edit |
|---|---|---|---|
| ST-EST-DRAFT | Draft estimate | Made by the tool, not yet opened by him | tool |
| ST-EST-EDITING | Draft estimate | He is changing it | builder |
| ST-EST-FINAL | Final | He is done; read-only | nobody |
| ST-EST-SIGNED | Signed | Client signed; sent to the operations app | nobody |

| From | Action | Guard (rules) | To | Side effects |
|---|---|---|---|---|
| ST-EST-EDITING | A-EST-FINALIZE | R-FIN-001 passes; R-FIN-002 warned and accepted | ST-EST-FINAL | New version made (D-0001); unpriced line items listed as not included |
| ST-EST-FINAL | A-EST-DUPLICATE | none | new estimate in ST-EST-EDITING | Parent version recorded |

## Open points
- Draft and Editing show the same words on screen; is the difference ever visible to him? (inferred from format.md section 5 and the design document's version pill)
- A-EST-SIGN has no screen, no rule and no delivery step. See E-041.
```

### 3.6 Template and example: field in the data dictionary (`spec/fields/<object>.yaml`)

Template:
```yaml
- id: F-OBJ-NAME
  label: W-                 # the on-screen word, by wording id
  note: ""                  # what it is, when to use it, when NOT to. This is the help text.
  type: ""                  # money | quantity | percent | text | choice | date | id | flag | record
  unit: ""                  # USD per unit, SF, %, none
  precision: ""             # stored and shown, with rounding
  allowed: ""               # range or list
  required_when: ""
  default: ""
  source: []                # who or what can set it: plan-read | template | price-history | vendor-sub-pricing | builder | computed
  editable_by: ""           # who, and in which states
  validation: []            # R- ids
  stored_at: ""             # object path in the format, with format version
  shown_on: []              # C- ids
  logged_as: ""             # change kind in the change list, or "not logged"
  exports: ""               # where it lands in Excel / CSV / client copy / operations app
  privacy: ""               # none | builder-figure | real-name
  decisions: []
  provenance: ""            # said | checked | inferred | proposed
  status: ""
  open: ""                  # anything undecided, in one line, with Q- or E- id
```

Example. This one is deliberately honest about a hole it exposes:
```yaml
- id: F-LI-UNIT-PRICE
  label: W-UNIT-PRICE
  note: "The builder's price for one unit of this line item, material and labor together, as he sees it in the one price box. Use for line items priced by quantity. Not used when the line item is a lump sum (see F-LI-LUMP-AMOUNT) or priced per area (see F-LI-AREA-RATE). Never filled from a market or generic price: a blank is correct when he has no price (hard rules 1 and 2)."
  type: "money"
  unit: "USD per F-LI-UNIT"
  precision: "stored to the cent, halves rounded up; always shown with cents"
  allowed: "blank, or any amount; a credit is a negative price (quantity is never negative)"
  required_when: "never required; a blank makes the line item 'Needs pricing' and keeps it out of the total"
  default: "blank, with the last known price shown beside it when there is one"
  source: [price-history, vendor-sub-pricing, builder]
  editable_by: "builder, in ST-EST-EDITING only; read-only in ST-EST-FINAL and ST-EST-SIGNED"
  validation: [R-PRC-001, R-PRC-004]
  stored_at: "line.material + line.labor + line.ml (format 0.4 section 3); the box shows their sum"
  shown_on: [C-li-price, C-det-split-material, C-det-split-labor]
  logged_as: "price"
  exports: "Excel: his three price columns; client copy: hidden (cost is not shown to the client)"
  privacy: "builder-figure"
  decisions: [D-0005, D-0007, D-0008, D-0028]
  provenance: "inferred"
  status: "open"
  open: "E-012: when he types a new figure in the one price box on a line item that has a material and labor split, which of the three stored columns changes? Not decided anywhere (D-0005 puts the split in Details but does not say). Needs an owner decision before lock."
```

### 3.7 Template and example: rule (`spec/rules/<area>.yaml`)

Template:
```yaml
- id: R-AREA-NNN
  rule: ""                  # one sentence, testable
  kind: ""                  # block | warn | compute | default | permission | privacy
  applies_to: []            # A-, F-, O- ids
  enforced_in: ""           # shared check | screen | both | process
  message: W-               # the words he sees, if any
  acceptance: []            # AC- ids
  decisions: []
  status: ""
```

Example:
```yaml
- id: R-FIN-001
  rule: "An estimate cannot be finalized while any tax, contingency or markup rate is blank. A typed 0% or $0 counts as a figure."
  kind: "block"
  applies_to: [A-EST-FINALIZE, F-EST-TAX-RATE, F-EST-MARKUP, F-GRP-CONTINGENCY-RATE]
  enforced_in: "both"
  message: W-MSG-BLANK-RATE
  acceptance: [AC-FIN-01]
  decisions: [D-0033, D-0053]
  status: "locked"

- id: R-FIN-002
  rule: "Finalizing with unpriced line items is allowed after a warning that lists them. They add nothing to the total and are listed on the estimate as not included."
  kind: "warn"
  applies_to: [A-EST-FINALIZE]
  enforced_in: "both"
  message: W-MSG-UNPRICED
  acceptance: [AC-FIN-02, AC-FIN-03]
  decisions: [D-0032]
  status: "locked"
```

### 3.8 Template and example: screen (`spec/screens/S-XXX.md`)

Template:
```markdown
---
id: S-XXX
name:
kind: screen | panel | dialog
status: open | proposed | locked
stories: []
objects: []
decisions: []
drawing: source/<file> sha256:<...>      # filled at lock
---
## Purpose
One or two sentences: what he comes here to do. What this screen is NOT for.

## Entry and exit
| Comes from | By | Lands on |
| Leaves to | By |

## States of the whole screen
| State | When | What he sees | What he can do |
(always cover: first use / empty · loading · normal · error · read-only · too narrow)

## Controls
One row per control. Fixed columns; the checker reads this table.
| Id | Type | Label (W-) | Does (A- or plain words) | Reads / writes (F-) | Rules (R-) | States | Does NOT do |

## Control detail
Only for controls that change data or state. Given / When / Then.

## Keyboard and focus

## Edge cases
E- ids that touch this screen, one line each.

## Feasibility notes
Filled by the front-end and back-end reviewers: simple | moderate | hard, and why. No decisions.

## Open points
```

Example, `spec/screens/S-FINWARN.md`, with the Finalize button's own row shown from `S-EST.md`:
```markdown
---
id: S-FINWARN
name: Finalize warning (line items not priced)
kind: dialog
status: proposed
stories: [US-031]
objects: [O-EST, O-LI]
decisions: [D-0032, D-0033, D-0050]
drawing: (not locked)
---
## Purpose
Tells him which line items have no price before he finalizes, and lets him go ahead or go back and price them. It is not where prices are entered and it does not explain blank rates (that is a separate message, R-FIN-001).

## Entry and exit
| Comes from | By | Lands on |
|---|---|---|
| S-EST | C-top-finalize, when R-FIN-001 passes and at least one in-scope line item is unpriced | focus on C-fin-price-now |

| Leaves to | By |
|---|---|
| S-EST, estimate now Final and read-only | C-fin-anyway |
| S-NEEDS-PRICING list | C-fin-price-now |
| S-EST, unchanged | Esc, or a press outside |

## States of the whole screen
| State | When | What he sees | What he can do |
|---|---|---|---|
| Normal | 1 or more unpriced | Count in the title, the list, two buttons | Either button |
| Long list | More than fits | List scrolls inside the dialog; buttons stay in view | Either button |
| Finalizing | After "Finalize anyway", until saved | Buttons off, "Finalizing…" | Wait |
| Could not finalize | Save failed | Says why; estimate stays in Editing | Try again, or close |
| Read-only | Never shown: C-top-finalize is off on a final or signed estimate | | |

## Controls
| Id | Type | Label (W-) | Does | Reads / writes | Rules | States | Does NOT do |
|---|---|---|---|---|---|---|---|
| C-fin-title | Heading, warning icon | "(n) line items are not priced" | Nothing | reads count of unpriced in-scope O-LI | | n = 1 uses singular | |
| C-fin-text | Text | W-MSG-UNPRICED | Nothing | reads F-EST-TOTAL | R-FIN-002 | | |
| C-fin-list | List | Line item, division, last price or "no last price" | Nothing | reads F-LI-NAME, F-LI-LAST-KNOWN | | Scrolls when long | Is not clickable; does not open a line item |
| C-fin-anyway | Outlined button | "Finalize anyway" | A-EST-FINALIZE | writes F-EST-STATUS, makes a version | R-FIN-002, R-VER-001 | Off while finalizing | Does not price anything; does not send anything to the client or the operations app |
| C-fin-price-now | Filled button | "Price them now" | Closes; opens the Needs pricing list | none | | | Does not finalize |

From `S-EST.md`, the button that opens it:
| C-top-finalize | Button, strong outline | "Finalize estimate" | Runs R-FIN-001, then R-FIN-002, then asks one plain confirmation; on yes A-EST-FINALIZE | writes F-EST-STATUS | R-FIN-001, R-FIN-002, R-FIN-003 | Off when ST-EST-FINAL or ST-EST-SIGNED | Does not send, sign, export or tell the operations app. Does not check prices for sense. Cannot be undone by Undo (he duplicates instead) |

## Control detail
### C-top-finalize
- **AC-FIN-01** Given an estimate in Editing whose sales tax rate is blank, when he presses Finalize estimate, then nothing is finalized, a message names each blank rate, and one button takes him to the cost summary. Given he types 0 there and presses Finalize estimate again, the blank-rate message does not appear.
- **AC-FIN-02** Given all rates filled and four in-scope line items unpriced, when he presses Finalize estimate, then S-FINWARN opens listing those four and the total shown excludes them.
- **AC-FIN-03** Given S-FINWARN is open, when he presses Finalize anyway, then the estimate becomes Final, a new version exists whose parent is the edited one, the four line items are stored as not included, every price and quantity box is read-only, and C-top-finalize, C-top-request and C-top-add-pricing are off.
- **AC-FIN-04** Given a priced line item with no cost code, when he finalizes, then he is warned and may continue (D-0030).

## Keyboard and focus
Opens with focus on "Price them now" (the safe choice; proposed). Tab moves between the two buttons only. Esc closes with no change. Enter presses the focused button.

## Edge cases
- E-014: every line item is unpriced. Is "Finalize anyway" still offered on an estimate with a $0 total? (open)
- E-015: a line item is priced while the dialog is open in another window. (parked: one window in first release)
- E-016: the save fails halfway through finalizing. The estimate must be either fully Final or still Editing, never between. (locked; see FT-SAVE-UNDO)

## Feasibility notes
(front end) simple. (back end) moderate: finalize must be one all-or-nothing write; see FT-SAVE-UNDO.

## Open points
- Order of the cost-code warning (AC-FIN-04) relative to this dialog is not decided.
```

### 3.9 Template and example: options considered for the build (`spec/features/FT-<name>.md`)

This is where "developers do not decide" is enforced: the note holds options and costs; the owner picks; the pick becomes a decision file; the note then points at it.

Template:
```markdown
---
id: FT-NAME
title:
status: options | decided | parked
decided_in:            # D-NNNN once picked
stories: []
rules: []
---
## The need
What must be true for the user, in two sentences. No technology.

## Appetite
How much build time this is worth (small: under a day · medium: days · large: a week or more).

## Options
| # | How it would be built | Build time | What it makes easy | What it makes hard or risky | Feasibility (FE / BE) |

## Recommendation
Which, and the one-line reason. Labelled Proposed until the owner answers.

## Rabbit holes
Details that could swallow time, each closed with a sentence.

## No-gos
What this feature will deliberately not do in the first release.

## Edge cases it must survive
E- ids.
```

Example, `spec/features/FT-SAVE-UNDO.md`:
```markdown
---
id: FT-SAVE-UNDO
title: Saving on leaving the box, and Undo
status: options
decided_in:
stories: [US-018, US-019]
rules: [R-SAVE-001, R-SAVE-002, R-VER-001]
---
## The need
A change is kept the moment he leaves the box, with nothing for him to press, and he can take back his last change. A crash or a closed lid never leaves an estimate half-written.

## Appetite
Medium. It is used on every edit; it is worth getting right once.

## Options
| # | How it would be built | Build time | Easy | Hard or risky | Feasibility |
|---|---|---|---|---|---|
| 1 | Each change rewrites the whole estimate file through the format module, written to a temporary file and then renamed | Small | Uses what exists; the shared check runs on every save | Undo must be worked out by reversing change-list entries; a 141 KB rewrite per change is fine on one computer, wasteful when hosted | FE simple / BE simple |
| 2 | Each change is appended to a small change journal beside the version file; the full file is rewritten every so often and at Finalize; one "apply change" function with an inverse serves edit, undo and the learning log | Medium | Undo and the learning log are the same record; nothing is lost on a crash; moves to a database unchanged | Two things to keep in step (journal and file); needs a replay test | FE simple / BE moderate |
| 3 | A local database holds line items as rows; saving is a database transaction | Medium to large | Crash safety for free | The estimate file stops being the thing that is stored; export to the contract format becomes a separate step that can drift | FE simple / BE moderate |

## Recommendation
Option 2 (Proposed): it makes the change list, which the format already requires, the single mechanism for saving, undo and learning.

## Rabbit holes
- Undo depth: last change only in the first release (the design document says "reverses the last change"). Closed.
- Undo after applying a pricing document reverses the whole apply as one step (format 0.5, item 1). Closed.
- Two windows open on one estimate: not supported in first release; the second opens read-only. Proposed.

## No-gos
No redo. No undo across sessions. No undo of Finalize.

## Edge cases it must survive
E-016 (failure during finalize), E-020 (power loss mid-save), E-021 (disk full).
```

### 3.10 Template and example: edge-case register and wording table

`spec/edge-cases.yaml` template:
```yaml
- id: E-NNN
  area: ""                 # same areas as rules
  situation: ""            # what happens, concretely
  harm: ""                 # wrong-money | lost-work | blocked | confusing | privacy
  expected: ""             # what the tool does, or OPEN
  touches: []              # S-, C-, F-, R-, A- ids
  found_by: ""             # full review, QA breaker, clickable trial, builder
  status: ""               # open | locked | parked
  test: ""                 # AC- id or test name once written
  decisions: []
```

Example:
```yaml
- id: E-012
  area: "PRC"
  situation: "A line item has a material price and a labor price stored separately. He types one new figure into the single price box."
  harm: "wrong-money"
  expected: "OPEN. Options: (1) the box is read-only when a split exists and opens Details; (2) the new figure replaces the split and is filed as his default column; (3) the change is spread in the old proportion."
  touches: [F-LI-UNIT-PRICE, C-li-price, S-DETAILS]
  found_by: "this audit, writing the field entry"
  status: "open"
  test: ""
  decisions: [D-0005]

- id: E-031
  area: "MKP"
  situation: "Markup is a dollar amount. He adds a $10,000 line item afterwards."
  harm: "wrong-money"
  expected: "The markup does not grow (D-0002). The cost summary shows a note that the markup is a fixed amount and gives the percent it now works out to."
  touches: [F-EST-MARKUP, S-COSTSUM]
  found_by: "full review 2026-11-19, pricing checker, item 5"
  status: "proposed"
  test: "AC-MKP-03"
  decisions: [D-0002]
```

`spec/wording.yaml` template and example:
```yaml
- id: W-TERM
  on_screen: ""            # exactly as shown
  means: ""
  code_name: ""            # the name in the format and the code
  never_say: []
  used_on: []              # C- ids (the checker fills or verifies)
  source: ""               # dated source, or "said <date>"
  decisions: []
  status: ""

- id: W-LINE-ITEM
  on_screen: "line item"
  means: "One priced thing on the estimate: a material, a labor task, a sub's work, an allowance."
  code_name: "line"
  never_say: ["row", "item" on its own]
  source: "said 2026-11-16"
  decisions: [D-0052]
  status: "locked"

- id: W-UNIT-PRICE
  on_screen: "Unit price"
  means: "His price for one unit of the line item."
  code_name: "material + labor + ml"
  never_say: ["rate" (kept for per-area pricing), "quote"]
  source: "column heading in the design document, section 5; not checked against a dated source (the design document says this check is owed)"
  decisions: []
  status: "proposed"
```

### 3.11 What the checker enforces (`tools/check_spec.py`)
Small, in the style of `build_index.py`. It fails, with the file and id named, when:
1. an id is defined twice, or cited and defined nowhere;
2. a control's `Label` or a field's `label` cites a wording id that does not exist;
3. a field is `shown_on` a control that does not list it, or the reverse;
4. an action in an object file has no home control and is not marked "deliberately none";
5. a control that writes a field or runs an action has no acceptance case;
6. a rule has no acceptance case, or a locked rule cites no decision;
7. a decision's `affects:` and the cited records' `decisions:` disagree;
8. a record cites a superseded decision;
9. a story in the first-release slice touches anything with status `open`;
10. (from phase 5) a control id in a locked drawing's code has no row, or a row has no control in the code; a checksum differs;
11. (in the build) an acceptance id has no test whose name carries it.

Checks 9 to 11 are the machine form of "nothing is re-decided in the build". The checker replaces a hand-kept traceability matrix.

### 3.12 How an agent uses it
- "What does this button do?" → `grep -n "C-top-finalize" spec/INDEX.md` → open one screen file → the row, including "Does NOT do".
- "What is this field, who can change it?" → one record in `spec/fields/`.
- "Why?" → the `decisions:` on that record.
- "What is still open?" → `spec/OPEN.md`, generated, which is also the owner's batch for the next decision round.
- AGENTS.md gains four lines telling agents to do exactly this and never to read the whole of `spec/`.

---
**Note on the examples in this section.** The ids, story numbers and acceptance cases are illustrations of the shape, written from the repository's decisions and design document; they are not locked content. Two of them expose real holes found while writing them: E-012 (one price box over three stored price columns) and the missing sign action on the estimate.

## 4. Roles and hand-offs

### 4.1 Principles (Judgement)
- **Three kinds of authority, never mixed.** The owner decides what the tool is and does. The orchestrator decides craft and keeps the records. Reviewers and feasibility readers *report*; they never decide and never edit. This is already the repository's rule (docs/reviewers.md: "Do not edit anything. Report only."); keep it.
- **A role is a saved brief, not a personality.** Each brief names what to read, the questions, and the return format. A reviewer that reads everything costs about 100,000 tokens or more; a reviewer given three files costs a fraction.
- **Every return has the same shape:** findings ranked by impact; for each, the id it concerns, what is wrong, why it matters, what to change; then what could not be checked; then what is good and should be kept. Findings cite spec ids so they can be filed without rereading.
- **One set of roles.** Today there are three overlapping sets (section 6, gap 9). `docs/reviewers.md` becomes the only one.

### 4.2 The roles

| Role | Use it when | Do NOT use it when | Reads | Returns |
|---|---|---|---|---|
| **Orchestrator** (the agent talking to the owner) | Always. Plans, writes the spec, builds, files findings, batches decisions for the owner | Never reviews its own work; never answers a builder-only fact | AGENTS.md, STATUS.md, CURRENT.md, `spec/INDEX.md`, then only the files a task names | Updates to the spec and records; to the owner, short numbered options with a recommendation |
| **Product and requirements writer** (may be the orchestrator in a separate session) | Phases 1, 2 and 5: turning decisions and trial findings into stories, objects, fields and rules | During the build; for visual questions | Decisions for the area, method.md, the relevant object and rule files | Draft spec records marked proposed, plus the list of things it could not specify without an owner or builder answer |
| **Designer, lane 1: usability and logic** | Any new or changed flow or screen; phase 3 (on the clickable version) and phase 5 (on rendered pictures) | A wording-only or colour-only change | The screen file, its objects and rules, rendered pictures at three widths or the running prototype | Per control: does it do what its label says; per story: the click path and where it stalls; missing states |
| **Designer, lane 2: visual** | Phase 5, after lane 1 findings are fixed; and once on tokens and components | Before the clickable trial (precision ahead of proof); when only logic changed | Rendered pictures only, plus standards.md section 3 and `spec/design/` | Where the eye goes first, what feels like a spreadsheet, inconsistencies against the tokens |
| **Estimating and domain checker** | Any rule touching money (tax, markup, contingency, allowances, alternates, rounding, the range); method changes; phase 2 throughout | Layout questions | method.md, format.md, `spec/rules/` for the area, sample files | Whether the arithmetic and the practice are sound; cases that would bite on a real job, as edge cases with a harm rating |
| **Builder-persona blind reader** | To catch confusing wording and missing everyday steps *before* spending the real builder's time; phase 2 flows, phase 3 prototype, phase 5 pictures | As proof that the builder will like it or use it; for prices, habits or anything only he knows; to settle a disagreement between options | Only what a builder would see: pictures or the prototype, and the wording. Not decisions, not the spec | What he would try first, where he hesitated, what he expected and did not find, what he would refuse to do |
| **Front-end feasibility reviewer** | Phase 2 (rough), phase 4 and phase 5: each screen and feature note | To choose between product options; to propose features | The screen file, the feature note, tokens and components | For each control or option: simple, moderate or hard; the reason; what would make it simpler. Nothing else |
| **Back-end feasibility reviewer** | Same points, plus any change to the format, storage or the AI read hand-off | Same | Feature note, format.md, object and rule files, kit code where relevant | Same shape, plus data-safety risks (lost writes, upgrade path, contract breakage) |
| **QA and edge-case breaker** | After a lifecycle table or a rules file is written (cheap, text only); on the prototype; before the phase 6 gate; in the build on every slice | On unfinished drafts the orchestrator already knows are incomplete | Object lifecycles, rules, the screen file; in the build, the running thing | New edge cases in register form (situation, harm, what it touched), each with a concrete sequence that produces it. No fixes |
| **Cold reader** (the "new-chat reader" already in reviewers.md) | Phase 0 exit and the phase 6 gate | Mid-phase | AGENTS.md and one build slice | The questions it would have to ask the owner before building |

**Hand-off rule.** A role's findings are filed by the orchestrator within the same session into exactly one of: a spec record changed, an edge case added, a decision proposed, a builder question added, or "not accepted" with a one-line reason in the review record. Nothing stays only in a review report. This closes the gap the repository has today, where the full review's findings sit in a history file with no status (STATUS.md lists answering them as owed).

**The feasibility brief, in full, because it is the role most likely to drift into deciding:**
> You are a senior front-end (or back-end) engineer. You do not choose what the product does. For each item you are given, answer only: (1) Is it feasible as written? (2) simple, moderate or hard, with the main reason. (3) If hard, the smallest change to the requirement that would make it moderate, stated as a question for the owner. Do not recommend technologies unless the item is a technology option note. Do not comment on whether the feature is a good idea.

### 4.3 The limits of a builder-persona agent, and the real evidence still needed (Judgement)
A persona agent is a language model predicting what a builder might say. It is useful as a cheap first reader because it reliably catches jargon, missing steps that any text on estimating mentions, and labels that sound alike. It cannot stand in for the builder, for specific reasons:
- **It reads; he glances.** A model reads every word on a screen with equal attention. A person of about 50 on a laptop sees the top-left, the biggest number, and whatever is coloured. Whether the eye is drawn correctly (decision 0044) can only be seen with a person.
- **It is agreeable and articulate.** It will produce a tidy list of concerns for any design, and will rate most designs as acceptable. A real user's strongest signal is silence, a wrong click, or closing the laptop.
- **It knows the average builder, not this one.** His habits (pricing by gut, a paint quote halved across two lines, cushions inside general conditions) are exactly what the tool must fit, and they are not in any training data. The full review's "general builder" was explicitly told to set aside how this builder prices.
- **It cannot feel time.** "Finish it in minutes" is the product promise. Only a stopwatch on a real estimate tests it.
- **It shares the designer's blind spots.** Orchestrator and persona are the same underlying model reading the same documents; errors correlate.

Real-user evidence needed, and when:

| When | Evidence | Why then |
|---|---|---|
| Before or during phase 2 | The builder's answers on what he sends a client today, allowances, alternates, how many bids he collects (questions already owed in STATUS.md). One real client-facing estimate of his, names removed | The back half cannot be designed from inference; a wrong guess here reshapes the line item |
| Phase 3 | The owner clicks the prototype himself. Then, with the owner's OK, **one sitting with the builder, 20 to 30 minutes, five tasks, nobody explaining**; note where he stops. Labelled a rough draft, made-up figures | The cheapest moment to be wrong. One real sitting is worth more than several persona rounds |
| Before the phase 5 lock | His reaction to the client copy layout (a picture is enough) | It carries his name to his clients |
| Beside all phases | Three or more blind jobs including a renovation, scored in dollars against actual cost (already owed; full review, pricing checker) | The screens can be perfect and the tool still fail on quantities |
| After the first build slice | He finishes one real estimate in the tool, timed | The only test of the product promise |

If the owner prefers not to put a rough version in front of the builder, say so in a decision and accept the risk knowingly; the owner himself (who is not a builder) plus persona agents is weaker evidence than it looks.

### 4.4 When a review is worth its cost (Judgement)
- **Text-only breaker pass** on a lifecycle or rules file: cheap; run every time.
- **Two-lane screen review:** only on rendered pictures of a screen about to be locked, never on a description (the repository already says a review from a description does not count).
- **Full multi-role review:** at the phase 6 gate only. Not again before then.
- Give every reviewer the smallest reading list that lets it do its job; the spec's ids make that possible.

---

## 5. Data storage and file types

### 5.1 What has to be stored

| Thing | Shape | Size and count (one builder) | Notes |
|---|---|---|---|
| Estimate versions | One nested document | About 141 KB each as written (Checked, format.md); tens per year, a few versions each | The contract with the operations app; final and signed versions never change |
| Change log | Small records per edit | Hundreds per estimate | "How the system learns"; also the basis for Undo |
| Templates | A list of line items with defaults | A handful | Shape not yet defined |
| Price history | One record per price per line item per job | Thousands over time | The learning asset; must be queried *across* jobs |
| Job documents | PDFs, images | Megabytes each | One copy; carry client names and addresses |
| Job record | Client name, address, contacts used, requests sent | Small | Real personal data; must stay apart from anything that enters the repository |
| Contacts copy, cost codes, settings / builder profile | Small lists | Small | |
| Plan-read and pricing-read results | Documents with evidence per entry | Per job | Shape not yet defined (engineer review, item 1) |

Two facts drive the choice (Judgement): the data is **small**, and it is **two different shapes**: documents that travel whole (estimates) and facts that are compared across jobs (prices).

### 5.2 What JSONB is, exactly
- **In PostgreSQL**, `jsonb` is a column type. The database parses the JSON once and keeps a binary form. Compared with the plain `json` text type it does not keep whitespace, key order or duplicate keys; it is faster to query because it is not re-parsed on each read; and it can be indexed (GIN indexes make "has this key" and "contains this fragment" lookups fast). Source: Neon documentation, "Postgres JSON data types", updated 2026-06-05, neon.com/docs/data-types/json. (The PostgreSQL manual page itself could not be opened from this session.)
- **In SQLite**, "JSONB" is a different thing with the same name: an internal binary encoding available from version 3.45, "slightly smaller (by between 5% and 10% in most cases)" and processed "in less than half the number of CPU cycles", and "not in any way binary compatible" with PostgreSQL's. It is "designed for internal use by SQLite only". Source: sqlite.org/jsonb.html, read 2026-11-19.

**What it is good for here (Judgement):**
- Holding a whole estimate version as one value in a hosted database, so the document that is the contract is stored as it is, with no splitting into dozens of tables and no reassembly.
- Per-builder settings and profiles whose keys differ between builders.
- Occasional questions inside documents ("which estimates use cost code 6080?") without writing a loader.

**What it is not:**
- **Not a file format.** Nothing on the owner's computer or in the exchange with the operations app becomes "JSONB". It exists only inside a database. The contract stays JSON text.
- **Not "easier to read".** It is binary; people and agents read it only after the database turns it back into JSON. A JSON file in a folder is the more readable form. The "faster" claim is true in one sense only: faster *for a database to search inside* than JSON stored as text.
- **Not a schema or a check.** It accepts any valid JSON. The shared check in `kit/estimate_format.py` and the format version do that job, whatever the storage.
- **Not the right home for price history.** Comparing a line item's price across fifty jobs is ordinary rows-and-columns work (line item id, date, unit, price, source). Digging those out of fifty documents on each question is slower and more awkward than a plain table.
- **Not an exact copy.** Because key order and spacing are not kept, a signed estimate stored only as `jsonb` cannot be shown to be byte-for-byte what was signed. A signed version should also be kept as its exact text with a checksum.
- **Not needed at this size.** At tens of estimates a year, none of its speed matters.

### 5.3 The three options compared

| | A. JSON files in folders | B. SQLite (one file; JSON functions built in) | C. Postgres with JSONB |
|---|---|---|---|
| **Simplicity today** | Highest. Already how the kit works. Agents and the owner can open, diff and repair a file | High. No server; one file. But contents are opaque without a tool | Lowest on one computer: a server process to install, run, upgrade and back up |
| **Safety against corruption** | Only as good as the writing code. Today `save()` opens the real file and writes into it (Checked: kit/estimate_format.py), so a crash mid-write can leave half a file. Fixable in a few lines: write a temporary file, flush, rename; keep the previous copy | Strong: all-or-nothing transactions are its core feature. Risky only if the file sits in a cloud-synced folder or is copied mid-write | Strongest, including many users at once |
| **Price history across jobs** | Weak directly (open every file). Fine with a small derived index rebuilt by script | Good: plain tables and SQL; can also look inside stored JSON | Best: tables, indexes, and JSONB lookups when needed |
| **Migrations and versions of the shared contract** | Natural: each file carries `format_version`; an upgrade step per version rewrites files; old files remain readable evidence. The file *is* the contract | Two layers to version: the database's own tables, and the format of the documents inside | Same two layers, with mature migration tools |
| **Backup** | Copy the folder; any backup tool or private git repository works; easy to verify by eye | One file, but must be copied with SQLite's own backup command while in use | Database dumps or the host's automatic backups; needs someone to check restores |
| **Many builders, hosted** | Poor: no concurrency control, no per-builder isolation | Workable for a few (one writer at a time, which the SQLite project says suits most low-traffic sites), awkward beyond | Designed for it |
| **Cost of moving later** | Low. Files import into either database with a loader script, because every file is already checked and versioned | Moderate. Plain tables move easily; SQLite's JSON queries must be rewritten for Postgres | Nothing to move, but the cost was paid up front |

Source for SQLite's fit: sqlite.org/whentouse.html, read 2026-11-19 ("SQLite competes with fopen()"; one writer at a time; "For device-local storage with low writer concurrency and less than a terabyte of content, SQLite is almost always a better solution"; a client/server database when many clients write over a network).

### 5.4 Recommended path (Judgement)

**(a) Today, one owner on his own computer: files are the truth, a small database is a disposable index.**
1. Keep "one estimate version = one JSON file, written only through the format module" (decisions 0018 and 0038; good, keep).
2. Fix the write: temporary file, flush to disk, rename over the old one; keep the last good copy. Add an append-only change journal beside each open version (the change list the format already requires), so Undo, crash recovery and learning share one record. See the FT-SAVE-UNDO example.
3. Keep final and signed versions as exact text with a checksum recorded in the job record.
4. Split a **private job record** (client name, address, contact names, requests sent) from the estimate file, so estimate files can stay free of names whether or not they are test files. The engineer reviewer raised the conflict between the redaction guard and real service use; this resolves it.
5. Build price history as its own **price record** (one per price observed: lasting line item id, job, date, unit, price, price type, source, who confirmed it, whether he later corrected it). Write the records to a plain file per job; rebuild a small SQLite index from them by script whenever needed. The index can be deleted at any time and rebuilt; it is never the truth.
6. Put all reading and writing behind **one storage module** (load, save, list, history, price lookup). Screens and scripts never touch files directly. This is the single thing that makes the later move cheap.
7. Backup: a scheduled copy of the data folder to a second place, and a restore tried once. Do not keep the live data folder inside a file-sync service's folder while the app is writing to it.

**(b) Later, hosted, several builders: Postgres, with the document in JSONB and the facts in tables.**
- `estimate_versions`: builder id, estimate id, version, status, format version, the document as `jsonb`, and the exact signed text with checksum for final and signed versions.
- `price_records`, `templates`, `cost_codes`, `contacts`: ordinary tables with a builder id on every row.
- Job documents in file storage, with a table of pointers.
- The move is a loader script: read each file through the storage module, run the shared check, insert.

**Why not SQLite as the truth now?** It is a reasonable alternative, and the right one if the build shows frequent small writes are awkward with files. It is not recommended as the starting point because it adds a second thing to version, hides the data from the agents who will debug it, and is a stop on the way rather than the destination. **Why not Postgres now?** It puts server administration on a non-technical owner to solve a many-users problem he does not have.

### 5.5 Decide now (cheap now, expensive later)
1. The estimate file stays the unit of storage and of exchange, whatever engine holds it.
2. One storage module; nothing else reads or writes data.
3. Safe writes and the change journal (FT-SAVE-UNDO).
4. Private job record separate from the estimate file.
5. The shape of a price record, and that line items carry lasting ids (decision 0036 already).
6. A `builder_id` on every stored thing from the first file, even with one builder (decision 0009 points this way).
7. Ids that are unique everywhere (not "line 12 of this file"), so merging data later cannot collide.
8. How money is written in the file. The module computes with exact decimals (Checked) but writes ordinary JSON numbers; say in format 0.5 whether money is a decimal string or whole cents, so a second app in another language cannot round differently.
9. An upgrade step per format version, and the golden sample files with expected totals and refusals.
10. Whether files are stored compressed. format.md says they are; `save()` writes plain text (Checked). Plain is recommended at this size; fix the sentence.

### 5.6 Defer (no cost to waiting)
Hosting provider; sign-in and accounts; several builders at once; JSONB indexes; search across documents; live sync between devices; storing page images (already ruled out); how the operations app receives a file beyond "it gets a checked file and answers accepted or refused".

---

## 6. Gaps: what the repository is missing or has in the wrong shape

### 6.1 What is good and should be kept (Checked)
- `decisions/` with the rejected alternative, the cost, and the owner's own words; the supersede chain checked at both ends by `tools/build_index.py`; CURRENT.md generated, never hand-edited.
- AGENTS.md: short, with hard rules and "do not read the whole of decisions/".
- The format as a contract: one way in (`fill_totals`, `save`), totals recomputed by every reader, a check that cannot be crashed (4,275 damaged files), tests on made-up data; both tests pass today (run 2026-11-19: 2 passed).
- Provenance labels (Said, Checked, Inferred, Proposed) and "Decided by Claude; reversible".
- Honest status: STATUS.md lists what is owed, including its own inconsistencies.
- Decisions 0010 and 0011: the right order, taken at the right time.
- Control ids already in the design document (`top-finalize`, `fin-anyway`): the seed of the control tables.
- Fresh reviewers who report and do not edit; reviews from descriptions declared not to count.

### 6.2 Gaps, ranked by the re-deciding or rework each would cause in the build

| # | Gap | Evidence | What it would cost in the build | Fix (phase) |
|---|---|---|---|---|
| 1 | **Only the estimate has a defined shape.** Templates, the job record, pricing documents, pricing requests, price history, plan-read and pricing-read results, settings and the builder profile have no object definition, fields or lifecycle | Full review, reader's list of what a builder of the software would still have to ask; format.md "Not in the estimate file, by decision" names records that live nowhere | Every one is a mid-build question to the owner, and each answer can change the format | Objects and fields (1, 5) |
| 2 | **The back half is undesigned**: client copy, allowances, client selections, alternates, several bids per line item, what changed between versions, signing and delivery to the operations app | Decision 0010; format has `allowance`, `alternate`, `signed` with no screen, rule or action behind them | Changes what a line item shows and stores, so it reopens locked screens and the format | Phase 2 |
| 3 | **The technical base is undecided**: stack, storage, how an AI read reaches the screen, how saving and undo work; totals and the check exist only in Python | STATUS "Next" item 3; engineer review items 1 to 3; `save()` overwrites in place | The first week of the build would be spent deciding, and format 0.5 depends on the answers | Phase 4 |
| 4 | **Format 0.5 is 0.4 plus twelve layered changes**, with eight open sub-points, no upgrade step, no sample files, and unstated arithmetic order (tax and contingency on the same lines; per-line tax rounding; dollar markup and late lines) | format.md sections 10 and 11; pricing checker item 5; "stored compressed" against plain-text `save()` | Two apps implementing a contract from a patchwork will disagree to the cent | Phase 4 |
| 5 | **No evidence from the builder on any screen**, 48 questions to him unanswered, one tested job that is no longer blind, quantities 22% low | questions.md; full review short version, item 5 | The largest possible rework: building the right spec for the wrong workflow | Section 4.3; beside all phases |
| 6 | **Screens: 4 drawn of roughly 20; the design document is behind seven decisions; the drawing source lives outside the repository**, readable only from a session on the owner's account, at a version that was "not checked" against the one the document was written from; whole-screen states (empty, loading, error, read-only) are absent | laptop-screens-design.md header and section 9; canvas.md; designer review items 1, 2, 7 | Builders would fill the undrawn majority by guesswork | Phases 3 and 5 |
| 7 | **Nothing has an address except decisions and controls.** Rules live in five places (AGENTS.md, method.md, format.md section 4, standards.md, decisions) with no ids; fields are described in format.md tables and again in the design document; nothing links a decision to the controls, fields or rules it governs; the only checker covers the supersede chain | Read of the files; decision template has no `affects` | Agents re-derive, and sometimes re-decide, what a rule is each session; contradictions are found late | `spec/`, ids, checker (0, 1, 5) |
| 8 | **No whole-journey map, no edge-case register, no tracker for review findings.** The "five tasks" are all inside one screen; edge cases are scattered through review prose; the full review's findings have no status | Decision 0054; full-review file; STATUS "Review findings not yet answered" | Missing steps surface as surprises; known problems are forgotten | Phases 0 and 1 |
| 9 | **Reviewer roles exist three ways**, and none is feasibility-only or an edge-case breaker. The Engineer brief asks whether "the structure is right", which invites deciding | standards.md section 4 (four views, plus two lanes); reviewers.md (five roles); STATUS lists it as owed | Inconsistent reviews; developers drifting into product decisions, against the owner's stated rule | Phase 0; section 4.2 |
| 10 | **A screen-level rule with no decision behind it: one price box over three stored price columns** (and how "Priced by" options map to stored fields) | Decision 0005 title; format.md section 3; format 0.5 item 8 "how each is held in the file is Claude's craft" | Wrong money, or a format change mid-build | Owner decision via E-012 (phase 2) |
| 11 | **Wording table unverified.** Most labels are marked "not checked"; standards.md requires dated sources | laptop-screens-design.md section 10 | Relabelling after build; low cost each, many places | Phase 5 |
| 12 | **No tokens or component list**, and a premium theme owed | Designer item 8; design document section 11 point 5 | Inconsistent first screens. Correctly deferred until after the clickable trial | Phase 5 |
| 13 | **The redaction name list exists nowhere**, so Job A cannot be re-imported with names removed | STATUS "Owed by the agent" | Blocks the test track, not the screens | Test track |

### 6.3 Contradictions and duplicates found (Checked unless marked)
1. **AGENTS.md against method.md.** AGENTS.md lists eight hard rules and says "The full set is `docs/method.md`. Where this file and that one differ, that one wins." Rules 7 (his building habits win over the drawn minimum) and 8 (flag plan-against-estimate conflicts) do not appear in method.md (searched for "habits" and "disagree": the only match is unrelated). By its own tie-break, AGENTS.md's two rules lose. The full review flagged this and it is still so.
2. **AGENTS.md start-of-session step 3** still says CURRENT.md "is not the full list" until STATUS.md says the backfill is finished. STATUS.md now says it is the full list. Remove the caveat.
3. **AGENTS.md "Mistakes"** and standards.md name `docs/history/mistakes.md`, which does not exist. README says `docs/history/` holds "the old working log... and the record of mistakes"; it holds one review file.
4. **standards.md section 5** says to log mistakes "in doc 07, section 8"; AGENTS.md says `docs/history/mistakes.md`. standards.md section 6 says "Hand-off steps are in doc 01", which is not in the repository. Its Status line says it is in force "through project instructions version 1.1", a document outside the repository. method.md still carries seven "doc NN" references.
5. **standards.md section 3 against canvas.md.** Standards: a locked sketch "is kept as its own source... the drawing's code, with every control given an id". canvas.md: the code is deliberately not in the repository. Acceptable only because nothing is locked; it must be resolved at the lock (phase 5 copies the source in). Also "which wins" is stated three ways: the design document says it wins over the canvas; canvas.md says decisions win over both; the design document's own header lists where it is behind the decisions.
6. **Saving wording, three versions.** Decision 0001 "as he types" (STATUS notes it); the design document's control rows and section 8 "saves as typed" / "as you type"; decision 0008 and standards.md "when he leaves the box". Only the last stands.
7. **format.md describes two versions at once**: section 1 says "Every save makes a new version; nothing is overwritten", section 5 says of builder editing "every save is a version", both overridden by section 11 item 1. Section 1 says "Stored compressed"; the code writes plain text.
8. **Decimals.** The design document's fix 4 (amounts in whole dollars) is overridden by decision 0007 (line item amounts and subtotals show cents); flagged in its header but the body is unchanged.
9. **Duplicate.** The design document's top bar table lists `top-duplicate` as a menu entry inside "More"; decision 0006 makes it a visible button.
10. **Reviewer roles**, three sets (gap 9).
11. **Two homes for tests.** The kit's tests sit in `kit/test_*.py` and are run by a wrapper in `tests/`; README says tests are in `tests/`. Works, but a reader will look in the wrong place. Minor.
12. **Tracked build leftovers.** Four cache files are tracked by git (`kit/__pycache__/*.pyc` and others) although `.gitignore` excludes them; a commit message says they were left on purpose. standards.md section 1 says no leftover files. Minor.
13. **`jobs/job-a/` is empty** while README describes `jobs/` as holding "per-job facts, costs and test scores". Either note that it is empty for now, or fill it.
14. **STATUS.md says decision 0009 quotes the builder's first name.** A search of the Markdown files for the name known to this session found nothing, so either it has been fixed and STATUS.md is behind, or the quote uses a different form. Worth one look.
15. **Scope drift worth an explicit decision (Judgement).** Job documents, a contacts copy and drafted pricing emails (decision 0019) are a second small product beside estimating; the new-chat reader said the same. The story map's "later" and "not doing" columns are where to settle it.

### 6.4 The shortest path from these gaps to the phases
Gaps 7, 8, 9 and all of 6.3 close in phase 0. Gaps 1 and 8 in phase 1. Gaps 2 and 10 in phase 2. Gap 6 in phases 3 and 5. Gaps 3 and 4 in phase 4. Gaps 11 and 12 in phase 5. Gaps 5 and 13 run beside everything and are the ones no amount of documentation can close.

---

## Sources
| Source | Date | Used for |
|---|---|---|
| Birgitta Böckeler, "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl", https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html | 2025-10-15 | Spec-first, spec-anchored, spec-as-source; critique of tooling |
| Den Delimarsky, "Spec-driven development with Spec Kit", https://developer.microsoft.com/blog/spec-driven-development-spec-kit/ | 2025-09-15 | Spec Kit steps; "what" kept apart from technology choices |
| AGENTS.md, https://agents.md/ | read 2026-11-19 | The convention; nearest file wins |
| Shape Up, chapter 6 "Write the Pitch", https://basecamp.com/shapeup/1.5-chapter-06 | read 2026-11-19 | Pitch ingredients; rabbit holes; no-gos |
| "Object-oriented UX", LogRocket, https://blog.logrocket.com/ux-design/object-oriented-ux-ooux/ | 2025-03-03 | ORCA: objects, relationships, calls to action, attributes |
| Design Tokens Community Group announcement, https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/ | 2025-10-28 | First stable token format |
| SQLite, "The JSONB Format", https://sqlite.org/jsonb.html | read 2026-11-19 | What SQLite JSONB is and is not |
| SQLite, "Appropriate Uses For SQLite", https://www.sqlite.org/whentouse.html | read 2026-11-19 | Where SQLite fits; one writer at a time |
| Neon, "Postgres JSON data types", https://neon.com/docs/data-types/json | updated 2026-06-05 | json against jsonb; GIN indexes |

Not opened, and so stated from general knowledge only (Judgement): Jeff Patton's story mapping (backbone, slices, walking skeleton), Michael Nygard's decision-record format, the PostgreSQL manual page on JSON types, and Given/When/Then from behaviour-driven development.
