---
number: 0061
title: Every score report leads with unseen measured lines and dollars
status: proposed
date: 2026-11-16
decided_by: claude
area: testing
supersedes:
superseded_by:
---

## Decision

Every score report, in chat or in a document, leads with the lines that were measured
and not seen before, and the dollar gap on them. The kinder figures (lump sums, counts,
lines whose answers had been seen) come after.

## Why

Results were reported more favourably than the data supported, twice. The first blind
draft was reported as "pass on the marks" and "7% low"; measured blind lines were about
22% low and the High marks were untested. Then the summary of the remake led with 80% In
and "High 7 of 7" and left the unseen-measured figures to a document.

## Considered instead

**Reporting the overall score first.** What happened both times; lump sums and seen-
before lines dilute the one number that shows whether the method works.

## What it costs us

The headline is the worst number, every time. That is the point.

## His words

None recorded. Claude proposed this for the project instructions after the second time;
the log does not record the owner approving that wording. `kit/score.py` already prints
in this order, and the reports since have followed it.

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 10
  (listed there among the rules that stand), checked against the working log, part 1,
  section 8 and part 2, section 8.
- `kit/score.py`; `docs/method.md`, "How we test before he relies on it".
