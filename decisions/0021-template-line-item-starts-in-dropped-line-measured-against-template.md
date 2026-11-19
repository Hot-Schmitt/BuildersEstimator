---
number: 0021
title: A template line item starts In; a dropped line is measured against the template
status: accepted
date: 2026-11-16
decided_by: owner
area: format
supersedes:
superseded_by:
---

## Decision

A line item in the chosen template starts **In**, with the reason "in your template" and
a blank quantity until the plans give one.

Lines found outside the template are shown as a count with a link ("On the plans, not in
your template") for him to answer. They are never added silently.

The estimate records the template it was made from, and format 0.5 measures a dropped
line against that template, not against his full list.

## Why

Templates collided with two standing rules. A template leaves most of his lines out on
purpose, and one of the Method rules moving into the shared check (decision 0034)
refuses a dropped line, so format 0.5 as first written would have refused every template
estimate. And under the default that a line with no decision is Ask (decision 0039), a
template would still have produced a wall of Ask lines. Found as a High gap in the
screens self-review.

## Considered instead

**A "questions for this job" list on the setup screen, and three settings on every
template line (Always, Ask each job, Off).** Drawn in the second sketches and dropped
the same evening: a template is a plain list of line items, and questions come only from
reading the plans, inside the estimate.

**Choosing the template and never raising work outside it.** A High review finding: the
template is chosen before the plans are read, so work on the plans outside the template
would never come up. Answered by the "not in your template" list.

## What it costs us

A line he usually carries but left out of the template is no longer an Ask on the
estimate; it shows only if the plans raise it. The method's step 4 has to say the same;
the current-state document lists that edit as owed.

## His words

> lock all and go

One reply locked all nine decisions that came out of the screens self-review of
2026-11-16; this was number 3.

The "not in your template" list was one of six review calls locked earlier the same day:

> say yes to review decisions 1 to 6

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 5,
  checked against the working log, part 3, section 2.
- `docs/format.md`, section 11, item 6.
- Decisions 0020 (templates), 0034 (rules in the shared check) and 0039 (Ask, never
  Out).
