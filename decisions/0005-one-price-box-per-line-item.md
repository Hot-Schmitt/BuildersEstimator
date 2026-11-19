---
number: 0005
title: A line item shows one price box; the material and labor split lives in Details
status: accepted
date: 2026-11-18
decided_by: owner
area: screens
supersedes:
superseded_by:
---

## Decision

On the estimate screen a line item always shows one price box. Where a line item has
both a material price and a labor price, the split shows only in Details.

## Why

It keeps every line item looking the same and the screen calm, in line with the
owner's standard quoted below.

## Considered instead

The working log does not record an alternative that was put to the owner. The obvious
one is showing separate material and labor boxes on the line item, as his sheet's
columns do; that is the look this decision avoids.

## What it costs us

On a combined line item he cannot see the material part from the estimate screen. That
matters for the Tax chip, which taxes the material part only (decision 0003): the chip
taxes a number he has to open Details to see.

The file still keeps his three price columns; this is a screen choice only.

## His words

> Lock 1 to 7

This was lock 4 of seven put to him together on 2026-11-18. The standard he set for all of them, the same day:

> Make sure that what you're proposing isn't overly complicated, yet still allows this estimator to be incredibly accurate... will appear simple on the surface, intuitive to use, and not busy for a 50-year-old man to use

## Links

- Backfilled on 2026-11-18 from the project's working log, part 5, section 2.
- Decision 0003, "What it costs us".
- `docs/format.md`, section 3 (the three price columns) and the note under section 11.
