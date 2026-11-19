# Method audit, Nov 19, 2026: the short version

**Purpose:** what three fresh researchers found when the owner asked whether this project has the right pieces, method and structure to reach "every button mapped, every field planned" before the build. His request is in `../2026-11-19-owner-brief-method-audit.md`. The three full reports are beside this file. Findings are the researchers' own and are **not yet decisions**; the proposals at the end are Proposed by Claude and wait on the owner.
**Usage (Checked from the run records):** 616,474 tokens across the three (repository audit 204,073; method 190,777; market 221,624), plus an unmeasured amount wasted on three duplicates (see `../mistakes.md`).
**Limits:** none of the three saw a rendered screen or the canvas drawings. The market researcher could not read Reddit directly, saw only the first pages of reviews per product, and found no independent test of AI plan reading on custom homes. An AI researcher is not a builder.

## The reports

| File | Asked | By |
|---|---|---|
| `repository-audit.md` | Read the repository cold and judge it against the owner's bar | A reviewer with no history, no web |
| `method-and-structure.md` | Which methods fit, the phases, the documentation structure with templates, agent roles, data storage | A reviewer with no history, web and repository |
| `market-research.md` | What small builders praise, complain about and ask for in estimating software | A researcher with no repository access, web only, dated sources |

## What they agree on (Inferred: the orchestrator's reading)

1. **The foundations are sound and should be kept:** the decision records and their generated index, the status page, the one-way-in format code, tests on made-up data, the hard rules, decisions 0010 and 0011.
2. **The mapping the owner asked for does not exist yet.** 56 control ids cover 4 of about 20 screens. Stories, rules, fields, states and edge cases have no home and no ids, and nothing links a control to a field or a decision.
3. **There is a "next" list but no phase path:** no gates, no definition of done, no feasibility step, and the technical choices sit after design.
4. **Only the estimate has a defined shape.** Templates, the job record, pricing documents, price history, read results and settings have none, and the back half of the estimate (client copy, allowances, alternates, several bids, revisions) changes what a line item stores.
5. **The builder's answers are the hidden critical path:** 48 questions, none answered, and decisions 0002 to 0004 rest on one 2022 sheet.
6. **Records need a tidy:** two instruction sets in force (the old project instructions and `AGENTS.md`), rules repeated with different wording, references to files that do not exist, open items spread over seven files.

## What the market evidence adds

1. **Setup effort is the top complaint about every conventional tool.** Starting from his own sheet with almost no setup is the opening.
2. **Builders distrust prices they did not set.** This supports "his prices only" (decision rule 1).
3. **AI plan reading is unproven on custom residential drawings,** and missed scope is where money is lost. A check for forgotten items built from his own sheet may be worth more to him than measurement.
4. **Trust comes from traceable numbers, the same answer every run, and no changes he did not ask for.**
5. **Excel survives because it is his, flexible and fast.** "Not like a spreadsheet" (decision 0044) is a risk if it makes editing slower than a cell.
6. **Custom builders need allowances, alternates, sub-bid placeholders and a client view that hides markup,** which is decision 0010's subject.
7. **Lock-in, price rises and no export draw the angriest reviews.** Export of everything is worth promising.
8. **Breadth overwhelms small shops.** Stay narrow.

## Two holes found on the way

- Nothing decides what happens when he types into the one price box (decision 0005) on a line item that stores a material and labor split.
- `AGENTS.md` says `docs/method.md` wins where they differ, but its hard rules 7 and 8 are not in `method.md`.

## Proposed (Claude), waiting on the owner

1. **Adopt the phase path with gates** from `method-and-structure.md`, section 2: close the records; map stories and objects; design the back half; rough clickable version and trial; technical options; lock and write the spec; a readiness gate where fresh agents given one build slice must have no questions for the owner.
2. **Add a `spec/` folder with ids and a checking script** (`method-and-structure.md`, section 3): one home each for screens and their controls, fields, rules, stories, edge cases and wording, with a generated index, filled in as each screen locks.
3. **Change the emphasis of the product:** starting from his own sheet, carrying sub bids forward and checking for missed scope become first-class; plan reading becomes one input among them, not the centrepiece. Editing speed is tested against a spreadsheet on the rough clickable version.
4. **Unblock the builder's answers:** the owner, a builder himself, answers the general trade questions; a short list of the blocking ones goes to the builder with the owner's OK.
5. **Storage direction (no decision needed now):** one estimate version as one JSON file behind a single storage module, with safe writes and a change journal; price history as its own records; a hosted database only when it is hosted. JSONB is a database column type for that later stage, not a file format.

## Change log
| Date | What changed |
|---|---|
| Nov 19, 2026 | New document, with the three reports saved beside it unchanged |
