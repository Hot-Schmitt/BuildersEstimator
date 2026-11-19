---
number: 0003
title: Sales tax is a chip on any line item with a material price, taxing the material part
status: accepted
date: 2026-11-18
decided_by: owner
area: pricing
supersedes:
superseded_by:
---

## Decision

A small **Tax** chip sits under the price box of any line item that carries a material
price. One click turns it on or off. It is also available inside Details.

- It taxes the **material part only**. On a line item carrying both a material and a
  labor price, the chip still appears, taxes the material part, and says so.
- Line items the builder already taxed in his template start with tax **on**. New ones
  start off. His choice is kept in the template.
- The rate comes from settings and is **stored on each estimate**, because jobs in
  different counties differ. It is blank until he gives it, with his last known rate
  shown beside it.
- Tax is calculated per line item and counted in **that line item's own division and
  cost code**.
- One quiet line at the foot of each division shows that division's tax, for example
  "Sales tax on 14 line items · $1,240". There is no tax figure under each amount.
- Applying vendor or subcontractor pricing asks "Does this price include sales tax?"

## Why

The builder prices some material by the piece from a store — his example was lumber
priced per piece — and he has his area's rate to hand. A per-line toggle lets him add
tax where it belongs without touching labor lines or subcontractor bids.

Tax has to be counted inside each line item's own division and cost code because that
is what his sheet does: it carries three separate tax rows, each counted within its
own division. A single sales tax line in the cost summary would break his division
totals and his budget by cost code, both of which currently reconcile with his cost
workbook to the dollar.

A tax figure under every amount would be busy, and the division foot line keeps the
numbers on screen adding up without it.

## Considered instead

**No format change at all.** Claude first told the owner this toggle fitted the shared
format as it stood. That was wrong, and it was caught only because the owner asked for
the logic to be checked. His sheet's per-division tax structure means the format has
to carry a tax mark per line item. Recorded in `docs/history/mistakes.md`.

**Show the chip only where a line item is priced by quantity or by area.** Proposed
first and rejected on its own merits: a lump-sum appliance package may well need tax,
and framing labor priced by the square foot does not. How a line is priced says nothing
about whether it is taxable; what it is made of does.

**Show the chip only on material-only line items**, handling combined lines inside
Details. Rejected by the owner in favour of showing it everywhere a material price
exists. Hiding it would mean a taxable material part with no visible way to tax it.

**Start every line item with tax off.** Rejected because it would silently drop the
tax his template already carries.

**Tax off by default on applied vendor pricing.** Rejected: a lumber yard often quotes
before tax, so assuming either way is a guess. Asking is one click and removes the
guess.

**A matching contingency chip on every line item.** Withdrawn by Claude before it
reached the owner. A second switch on every line item is busy, and contingency by
group in the cost summary does the same work.

## What it costs us

On a combined material-and-labor line item, the amount being taxed is not visible on
the estimate screen — the split only shows in Details. So the chip taxes a number he
cannot see from where he clicks it. The chip's own label has to carry that, and it is
worth watching in the first review.

The rate living in settings and being stored per estimate is two homes for one value.
It is a default and a stored copy rather than a contradiction, but it needs writing
down precisely in the format, or it will read as a one-source-of-truth problem later.

## His words

> For tags, I think that should be a clickable toggle on line items. The idea is that
> if he is pricing up something, say by quantity, other than a vendor giving it to him,
> like lumber from Lowe's or something, and he has the price per piece of wood, and he
> has entered in sales tax in the settings for his area, so Georgia. He can toggle the
> button to automatically include sales tax. For that line item.

("tags" is transcription for "tax"; confirmed in chat and not corrected.)

## Links

- Shared estimate format, `docs/format.md`: the per-line tax mark, the material-part
  rule and the rate stored on the estimate are three of the twelve changes approved
  for version 0.5.
- `docs/builder/questions.md` — whether he taxes materials only, why his sheet carries
  three tax rows, and whether he means to mark up tax.
- `docs/history/mistakes.md` — the wrong "no format change needed" claim.
- Decision 0002 — markup sits on all cost, tax included.
