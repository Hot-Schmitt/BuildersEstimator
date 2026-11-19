---
number: 0025
title: Tax and delivery read from a pricing document are never assigned by the tool
status: accepted
date: 2026-11-16
decided_by: owner
area: pricing
supersedes:
superseded_by:
---

## Decision

Tax and delivery amounts read from a vendor's or sub's pricing document are never
assigned to a line item by the tool. They land in "Needs you" for him to place.

## Why

His sheet adds sales tax and contingency as percent lines. If a vendor's total already
includes tax and is applied to a line item his tax sits on, tax is charged twice. Found
as a High gap in the screens self-review, checked against his sheet.

## Considered instead

**Assigning them with the rest of the document.** What the sketches did before the self-
review; it is the double count described above.

## What it costs us

One more thing for him to place by hand on most pricing documents. How he wants a
vendor's tax and delivery handled against his own tax line is a question only he can
answer.

## His words

> lock all and go

One reply locked all nine decisions that came out of the screens self-review of
2026-11-16; this was number 5.

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 6,
  checked against the working log, part 3, section 2.
- Decision 0003: applying pricing also asks "Does this price include sales tax?".
- `docs/builder/questions.md` (owed): how he handles a vendor's tax and delivery.
