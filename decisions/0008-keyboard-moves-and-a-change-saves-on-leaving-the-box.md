---
number: 0008
title: Keyboard moves, and a change saves when he leaves the box
status: accepted
date: 2026-11-18
decided_by: owner
area: screens
supersedes:
superseded_by:
---

## Decision

- **Enter** moves down the same column, to the next box that exists.
- **Tab** goes quantity, price, then the next line item.
- **Esc** restores the box.
- **Ctrl+Z** undoes.
- A change saves when he leaves the box, not on each keystroke.

## Why

It lets him work down a column the way a spreadsheet user expects, and Esc can only
restore a box if the change has not been saved yet.

## Considered instead

**Saving on each keystroke.** Decision 0001 and the earlier design document say changes
save "as he types". This decision narrows that: the change is saved, and logged in the
change list, once, when he leaves the box. Everything else in 0001 stands, so 0001 is
not superseded.

## What it costs us

A change he has typed but not left is not yet saved if the window closes.

## His words

> Lock 1 to 7

This was lock 7 of seven put to him together on 2026-11-18. The standard he set for all of them, the same day:

> Make sure that what you're proposing isn't overly complicated, yet still allows this estimator to be incredibly accurate... will appear simple on the surface, intuitive to use, and not busy for a 50-year-old man to use

## Links

- Backfilled on 2026-11-18 from the project's working log, part 5, section 2.
- Decision 0001: where "as he types" in that file is read as "when he leaves the box".
- `docs/format.md`, section 11, item 1; `docs/standards.md`, section 2.
