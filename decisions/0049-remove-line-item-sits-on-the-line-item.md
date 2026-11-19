---
number: 0049
title: Remove line item sits on the line item itself, with a confirmation
status: accepted
date: 2026-11-16
decided_by: owner
area: screens
supersedes:
superseded_by:
---

## Decision

Every line item carries its own remove control (a trash icon). Removing asks first:
"Keep it" or "Remove line item". Removed line items go to a "removed line items" list on
the estimate, so nothing is dropped silently.

## Why

It is where the owner expected to find it: on the thing he is editing.

## Considered instead

**"Remove line item" inside the details panel only.** How the locked third sketch had it
(decision 0047).

## What it costs us

A destructive control sits on every line item, one slip away from the price box; the
confirmation and the removed list are what make that safe. The removed list is not drawn
yet.

## His words

> if I'm editing trust and I wanted to remove... I would think I would do it there

("trust" is a transcription slip; his example was a line item he was editing.)

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 4,
  checked against the working log, part 4, section 2 (11 pm).
- Decision 0048: the canvas design this is drawn in.
