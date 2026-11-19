---
number: 0023
title: Nothing changes until Apply; unassigned money blocks it; only High matches apply in one tap
status: accepted
date: 2026-11-16
decided_by: owner
area: pricing
supersedes:
superseded_by:
---

## Decision

On "Add vendor or sub pricing":

- Nothing on the estimate changes until he presses **Apply to estimate**.
- Apply is blocked while any money in the pricing document is not assigned. He assigns
  it to a line item, splits it across line items, or leaves it out with a reason.
- High-confidence matches apply in one tap. Medium and Low matches each need his tap
  first.
- An applied line item shows where its price came from, with the earlier figure kept
  beside it.

## Why

A price enters his estimate only when he confirms it, which is what keeps rule 1 (his
prices only). Blocking on unassigned money stops dollars dropping silently.

## Considered instead

**One "Apply all" for every suggested match.** Drawn in the second sketch on a design
consult's advice. A fresh review found it would push low-confidence matches in as his
price (a High finding), so it became one tap for High and a tap each for the rest.

**Side-by-side bid grids, match percentages, drag and drop on a phone.** A design
consult on 2026-11-16 judged them not worth building.

## What it costs us

More taps when a pricing document has many uncertain matches. A second price for the
same line item (replace or add) still needs its own state.

## His words

> say yes to review decisions 1 to 6

Call 2 of six from the logic and layout review. The screen itself was locked with:

> I lock the three sketches (new estimate, add vendor or sub pricing, request pricing)

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 6,
  checked against the working log, part 2, section 3 and part 3, section 2.
- Decision 0001: applying pricing does not make a new version; undo reverses that one
  apply.
