---
number: 0072
title: A vendor's quantity comes in with the vendor's price on Apply; the comparison is parked
status: accepted
date: 2026-11-19
decided_by: owner
area: pricing
supersedes: 0026
superseded_by:
---

## Decision

When a pricing document carries its own quantities (a lumber list, for example), the
vendor's quantity comes in with the vendor's price when he presses Apply. There is no
second quantity beside it, no flag, and nothing for him to pick.

Comparing the tool's own counts with vendors' quantities is parked. It can be added once
the tool has collected both for real jobs and its counts have been tested (decision
0071).

## Why

A vendor's price belongs to the vendor's quantity, so there is nothing real to pick
between. He already sees every change before he presses Apply (decision 0023), so
nothing is swapped silently. The owner did not see the benefit of showing both: the
builder is unlikely to dispute quantities with most of the vendors he works with.

## Considered instead

**Showing the vendor's quantity beside ours, flagged, and he picks (decision 0026).**
Decided by Claude on 2026-11-16 and never locked by the owner. It adds a flag to clear
on every pricing document that carries quantities, for a comparison whose worth is not
proven until the tool's counts are.

**Keeping the pick only on line items not set to "vendor's takeoff" (decision 0070).**
Claude's first recommendation on 2026-11-19. Still a second number on his screen with
nothing behind it yet.

## What it costs us

Until the comparison is added, a vendor's list that is short against the plans is caught
only by his own eye.

## His words

Dictated on 2026-11-19, when asked whether decision 0026 should stand:

> Would it just be in case he wants to dispute a vendors or subs quantity he probably
> won't do this with most of the vendors he works with we can add the future in later
> [...] once the application has been collecting data so we can see how much it
> estimated versus how much has vendors have been putting in

("the future" reads as "the feature".) He then chose "Yes, replace it" for the rule
above.

## Links

- Decision 0026: superseded by this one.
- Decision 0023: nothing changes until Apply.
- Decision 0070: who figures each line item's quantity.
- Decision 0071: the timed test of the tool's counts, which the parked comparison waits on.
