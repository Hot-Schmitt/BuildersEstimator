---
number: 0033
title: A blank tax, contingency or markup rate blocks finalizing; a typed zero satisfies it
status: accepted
date: 2026-11-17
decided_by: owner
area: format
supersedes:
superseded_by:
---

## Decision

A blank tax, contingency or markup rate blocks finalizing. A typed $0 or 0%, whichever
markup type he chose, satisfies it. Only a blank stops him.

## Why

A missing rate changes the whole total without showing on any line item, so it is the
one kind of blank worth stopping for. But if he means zero he can say zero; the tool
does not force him to charge a markup or a contingency.

## Considered instead

**A plain block on a blank rate, with no way through.** Claude's first proposal. The
owner locked it with the condition in his words below.

## What it costs us

A typed zero is accepted without question, so a zero entered by mistake finalizes like
any other rate.

## His words

> lock 5 but... We should allow $0 or 0%, whichever markup type he chooses, to satisfy
> the condition

> keeping with the design of not forcing a user to work in a way or use the system that
> requires them to do something they don't want to do, or in a way that they don't want
> to do it within our limitations

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 3,
  checked against the working log, part 5, section 2 (10:44 am).
- `docs/format.md`, section 11, item 2.
- Decision 0053: do not force him. Decision 0002: markup as a percent or a dollar
  amount.
