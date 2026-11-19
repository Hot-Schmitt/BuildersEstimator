---
number: 0032
title: Finalizing with unpriced line items warns and allows; they are listed as not included
status: accepted
date: 2026-11-17
decided_by: owner
area: format
supersedes:
superseded_by:
---

## Decision

Finalizing an estimate while some line items have no price is allowed, after a warning
that lists them with their last known prices and offers "Price them now" or "Finalize
anyway". Those line items are listed on the estimate as not included, and add nothing to
the total.

## Why

He should not be blocked from finishing, and the estimate says plainly what is missing.
An unpriced sub bid on a final estimate needed a stated rule either way.

## Considered instead

**(b) Block finalizing until every line item is priced.** The other option put to the
owner. For unpriced line items this also replaces the format 0.4 rule that a final
estimate may hold no blanks.

## What it costs us

An estimate can go out with work not priced in it. The "not included" list is the only
thing standing between that and a missed cost, so it has to be impossible to overlook,
on screen and on whatever the client receives (decision 0010).

## His words

> to finalize with your option a

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 3,
  checked against the working log, part 4, sections 2 and 3 (decision 2).
- `docs/format.md`, section 11, item 2.
- Decision 0033: what does still block finalizing.
