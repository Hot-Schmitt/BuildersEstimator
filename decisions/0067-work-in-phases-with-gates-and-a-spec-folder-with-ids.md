---
number: 0067
title: Work in seven phases with gates, and give every screen, control, field and rule one home with an id
status: accepted
date: 2026-11-19
decided_by: owner
area: process
supersedes:
superseded_by:
---

## Decision

The project moves through seven phases, each with a test that says it is done:

- **0 Close the records.** Fix contradictions, settle the proposed decisions, create the
  empty `spec/` folder and its checking script.
- **1 Map and name.** The whole journey as a story map, the objects and their states, a
  first wording table. The owner approves what is in the first release.
- **2 The back half, rough** (decision 0010): client copy, allowances, alternates, several
  bids, revisions, as rules and flows.
- **3 Rough clickable version and trial** (decision 0011), on made-up data.
- **4 Technical options:** stack, storage, how an AI read reaches the screen, saving and
  undo; format 0.5 as one clean specification with sample files.
- **5 Lock and write the spec:** real-size drawings; every control, field, rule and edge
  case written down; two-lane review.
- **6 Readiness gate:** fresh agents given one slice of the build must have no questions
  for the owner.

Alongside, a `spec/` folder gives every screen and its controls, every field, rule, user
story, edge case and screen word one home with an id, checked by a script, with a
generated index. It is filled in as each screen locks. Developers reviewing it say what
is feasible and what adds build time; they do not decide.

## Why

The owner's bar: by the time mock screens are locked, every button is mapped, every field
and its back end is planned, edge cases have been looked at, and the build needs no
re-deciding. Three fresh researchers found on 2026-11-19 that the foundations are sound
but this mapping does not exist: 56 control ids cover 4 of about 20 screens, nothing
links a control to a field or a decision, and there was a "next" list but no phase path.

## Considered instead

**Carrying on screen by screen from the "next" list.** How the project was running. Each
screen would be drawn, reviewed and locked with its logic recorded only in a design
document and scattered decisions, and the technical choices would come after design.

**Heavier methods** (full domain-driven design, Shape Up cycles, spec tooling,
a hand-kept traceability matrix). The method researcher judged them overkill for one
owner working with agents.

## What it costs us

Two phases of closing records and mapping come before any new screen is drawn. More
files to keep in step, which is why a script checks them. The phase list and the `spec/`
layout are the researcher's proposal; details are the agent's craft and can change as
they are used.

## His words

> Yes to all

His bar, from the brief of the same day:

> by the time we get done locking some mock screens, every button's been mapped, all
> logic has been tested, we know what every button does, what it doesn't do, we know what
> every field is, and its back end has been planned.

## Links

- `docs/history/2026-11-19-method-audit/README.md` (proposals 1 and 2) and
  `method-and-structure.md`, sections 2 and 3, beside it.
- `docs/history/2026-11-19-owner-brief-method-audit.md`.
- Decisions 0010 and 0011 (now phases 2 and 3), 0041 (a locked design is the build
  source) and 0055 (reviews).
