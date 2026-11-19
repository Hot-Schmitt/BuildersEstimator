---
number: 0053
title: The tool does not force him to work in a way he does not want
status: accepted
date: 2026-11-17
decided_by: owner
area: product
supersedes:
superseded_by:
---

## Decision

A standing design principle: within its limits, the tool does not force the builder to
work in a way, or use the system in a way, that he does not want. A rule that stops him
has to be one of the few where going on would silently change his numbers.

## Why

He prices by gut and will overwrite anything he disagrees with. A tool that makes him do
things its way will not get used.

## Considered instead

**Hard blocks wherever the data is incomplete.** Claude's first proposal for a blank
rate was a plain block; the owner turned it into "a typed zero satisfies it" and stated
this principle while doing so. The same thinking is behind warning, not blocking, on
unpriced line items and on a missing cost code.

## What it costs us

"Within our limits" is a judgement each time. Every warning that could have been a block
is a place a mistake can get through if he clicks past it.

## His words

> keeping with the design of not forcing a user to work in a way or use the system that
> requires them to do something they don't want to do, or in a way that they don't want
> to do it within our limitations

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 3,
  checked against the working log, part 5, section 2 (10:44 am).
- `docs/standards.md`, section 3 ("Do not force him").
- Decisions 0030, 0032 and 0033: where it has been applied.
