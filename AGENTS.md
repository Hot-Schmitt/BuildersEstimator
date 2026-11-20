# AGENTS.md

Instructions for any AI agent working in this repository. Read this first, every session.

This file is the only instruction set. The instructions and documents of the claude.ai project this work started in are frozen history; where they differ from this repository, the repository wins.

## What this is

An estimating helper for a luxury home builder in Atlanta. It reads a job's plans and drafts about 80% of his estimate, using his own line items and his own prices, and flags what it is not confident about. The output is an on-screen estimate, laptop first. Signed estimates hand off to a separate operations app through one shared estimate format.

Two people are involved. **The owner** is who you talk to; he decides what the tool does. **The builder** is his client; he never sees internal notes, test scores or margin analysis unless the owner chooses to share them.

## Start of session

1. Read this file.
2. Read `STATUS.md` — where we are, what is next, what is waiting on the owner.
3. Read `CURRENT.md` — the decisions that stand right now, generated from `decisions/`. It is the full list.
4. Read only the decision files for the area you are working in (`grep -l "area: screens" decisions/*.md`). Screen behaviour is also filed under pricing, format and process, so search `CURRENT.md` by keyword as well.
5. For what a screen, button, field or rule is: `spec/`. Do not read the whole folder. Find the id in `spec/INDEX.md`, open the one file on that line, and follow its `decisions:` for the why. `spec/OPEN.md` lists what is still undecided. `spec/README.md` explains the ids.
6. Read `docs/method.md` before any estimating, `docs/standards.md` before any build or design work, `docs/format.md` before writing or reading an estimate file.

Do not read the whole of `decisions/` or the history in `docs/history/`. Search them when you need to know why something was decided.

## Hard rules

These are not negotiable and they outrank convenience.

1. **His lines, his prices.** Never put in a price that is not the builder's. A generic or market price may appear only as a note labelled "outside reference".
2. **Never invent a number.** If a quantity or price is not known, leave it blank and mark it. A blank is a correct answer; a made-up number is a failure.
3. **Every quantity carries its source** — written on the plans, read from dimensions, counted, calculated, or assumed. Never show a guess as a measurement.
4. **Scope before quantity before price.** A missed line costs more than a mismeasured one. Never drop or add a line silently.
5. **Arithmetic runs in code, never in your head.** Check totals before showing them.
6. **Engineering decisions are not ours.** Flag them.
7. **His building habits count.** Where he builds differently from the drawings (bigger footings, for example), his recorded rule wins over the drawn minimum. Until a rule is recorded, the line stays Medium at best.
8. **When the plans and his past estimates disagree, flag it.** Do not pick one.

The full set is `docs/method.md`. Where this file and that one differ, that one wins.

## What never enters this repository

Client names, street addresses, phone numbers, tax and bank details, and vendor or subcontractor names. The builder's own cost figures and line wording are allowed — the owner approved that on 2026-11-18 (decision 0012) — but personal and third-party identifying data is not, and the original plan PDFs never come in at all.

Jobs are referred to as Job A, Job B and so on. Documents say "the builder", not his name. `kit/redaction.py` is the one redaction step; every writer uses it, and nothing is written while a listed name survives.

## Recording a decision

One decision, one file, never deleted. Copy `decisions/0000-template.md`, take the next free number, and fill it in.

- Filename: `NNNN-kebab-case-title.md`, zero-padded.
- Numbers are assigned in the order decisions are **recorded**, not the order they were made. A backfilled older decision gets the next free number and carries its real date. Never renumber an existing file.
- When a decision replaces an earlier one: set the old file's `status` to `superseded` and its `superseded_by` to the new number, and set the new file's `supersedes` to the old number. Both ends, or the chain breaks.
- Quote the owner's own words in `his_words` wherever you have them. His sentence outlives your paraphrase of his reasoning.
- Record the alternative that was rejected and why. That is the point of the file.

Then run `python3 tools/build_index.py` to regenerate `CURRENT.md`. **Never hand-edit `CURRENT.md`.**

## Commands

```
python3 tools/build_index.py     # regenerate CURRENT.md from decisions/
python3 -m pytest tests/         # run the kit's tests and the spec tools' tests
python3 tools/build_spec_index.py   # regenerate spec/INDEX.md and spec/OPEN.md
python3 tools/check_spec.py         # check spec/ for breaks (add --gate before a build)
```

Run the last two after any change in `spec/`. They need PyYAML (`pip install pyyaml`). **Never hand-edit `spec/INDEX.md` or `spec/OPEN.md`.**

## Working with the owner

- Lead replies with direct answers to what he asked, then action items, then explanation. Work already done goes last and collapsed. No walls of text.
- Bring choices as short numbered or clickable options with a recommendation. For each: the decision he needs to make, why it matters, the pros and cons, and the recommendation.
- End every reply with the decision that is his to make, as clickable options where the tool allows, even when it is only "go". The one exception is a reply that ends with a hand-off (Said, Nov 19, 2026).
- The owner decides what the tool does and anything the builder sees. The agent decides the craft (wording, layout detail, how a test is run, code structure) and reports notable calls so they can be reversed.
- An idea he gives as an example is context, not a requirement.
- New feature ideas are noted and parked unless he says to include them. Keep the tool small.
- One step at a time. Edit rather than regenerate.
- Push back with a one-line reason when a request is weaker than an alternative. Label your own ideas Proposed and your readings Inferred. In documents, label lines Said (the owner or the builder), Checked (verified against a file or a dated source), Inferred or Proposed.
- Nothing is sent or shown to the builder without the owner's OK. Anything for the builder is labelled a draft estimate, never a bid or a price.
- Do not share the owner's Claude account with the builder or build his access on it.
- Do not fill in facts only the builder knows. Add them to `docs/builder/questions.md`.
- Warn before anything that will take a long time or a lot of usage.
- Hand off to a fresh chat at a good stopping point, not after every small run (decision 0056): update `STATUS.md` first, then give the starter line in a copy-ready code block.
- He often dictates; read past transcription slips and ask in one line if a slip could change the meaning.

## Where things are recorded

One home per thing. A document states a rule only if it owns it; every other mention is a pointer.

- Hard rules: this file. Estimating rules: `docs/method.md`. Build, design and review rules: `docs/standards.md`. Who reviews and what each is asked: `docs/reviewers.md`.
- A choice the owner made: a file in `decisions/`.
- What a screen, control, field, rule, story or edge case is: its record in `spec/`, by id.
- Stage, next steps, what is waiting: `STATUS.md`.
- A job's test results and the builder's corrections: that job's folder in `jobs/`.
- Mistakes: `docs/history/mistakes.md`.

## Mistakes

When you get something wrong: fix it, record it in `docs/history/mistakes.md` with what happened, why, and the fix, and propose a rule change if one would have prevented it. The same kind of mistake twice means a rule must change.
