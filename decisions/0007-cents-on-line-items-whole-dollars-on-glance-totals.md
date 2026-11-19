---
number: 0007
title: Line item amounts and subtotals show cents; the big glance totals show whole dollars
status: accepted
date: 2026-11-18
decided_by: owner
area: screens
supersedes:
superseded_by:
---

## Decision

Line item amounts and subtotals show cents, drawn smaller and lighter so the dollars
read first. The big glance totals show whole dollars. Unit prices show cents.

## Why

The numbers on screen have to add up to the cent, as his sheet does, without the cents
making the screen busy.

## Considered instead

**Whole dollars on line item amounts.** The earlier design document had line item
amounts without cents (Inferred from the working log, which says that line no longer
holds). Changed before the lock.

## What it costs us

A glance total in whole dollars can differ by under a dollar from the sum of the
amounts shown beneath it. The file always stores money to the cent.

## His words

> Lock 1 to 7

This was lock 6 of seven put to him together on 2026-11-18. The standard he set for all of them, the same day:

> Make sure that what you're proposing isn't overly complicated, yet still allows this estimator to be incredibly accurate... will appear simple on the surface, intuitive to use, and not busy for a 50-year-old man to use

## Links

- Backfilled on 2026-11-18 from the project's working log, part 5, section 2.
- `docs/format.md`, section 1 (money is stored to the cent).
