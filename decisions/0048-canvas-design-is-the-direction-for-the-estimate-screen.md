---
number: 0048
title: The canvas design is the direction for the estimate screen
status: accepted
date: 2026-11-16
decided_by: owner
area: screens
supersedes: 0047
superseded_by:
---

## Decision

The design on the canvas "Estimate screen - laptop" is the direction: four drawings at
real size (the working screen on one division, the line item details pop-out, the remove
confirmation and the finalize warning). No redraw; small edits wait until it is built
and he can see it.

- Line item details are a **pop-out**, opened only when needed, not a permanent column.
- "Priced by" is four single-choice options inside it.
- Back and next between divisions stay.
- **For the build:** a more premium button style and colour theme than the drawing, and
  icons wherever they help draw attention, so he has to read less.

## Why

The owner accepted it in the words below. It answers what he found wrong with the sketch
he had locked earlier that evening (decision 0047).

## Considered instead

**The locked third sketch with a permanent details side panel.** Decision 0047;
withdrawn at 11 pm. On the pop-out he leaned on Claude's recommendation.

**A formal lock on the canvas design.** Not asked for: it was accepted as the direction,
not put to him as a lock.

## What it costs us

Most of the estimate screen is still not drawn: the cost summary, the three "needs
attention" lists, search results, adding a line item, the removed list, settings,
version history, the Duplicate choice, the other three "Priced by" states, the template
actions, the cost code picker, and laptop layouts of the three earlier screens. The
premium theme is not yet proposed. Decisions 0010 and 0011 have since changed what
happens before anything more is locked.

## His words

> this looks pretty good. We can make small edits and it later after it's built... make
> sure that you opt to use a more premium button and color theme... make sure you plan
> to use the icons or you can to help draw the attention so he doesn't have to read so
> much

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 4,
  checked against the working log, part 4, sections 1 to 3.
- Decision 0047, which this supersedes.
- The canvas and the design document are due in `docs/screens/` (step 2 in `STATUS.md`).
- Decisions 0005 to 0008: the Nov 18 locks made on top of this design.
