---
number: 0068
title: The AI's job is to speed up his estimate: count what it can, check his numbers, organize the rest
status: accepted
date: 2026-11-19
decided_by: owner
area: product
supersedes:
superseded_by:
---

## Decision

The product leads with what makes his estimating faster, not with "it reads your plans":

- It starts from his own sheet and line items, with almost no setup.
- It catches forgotten items and carries sub and vendor pricing forward.
- The AI behind it does the counting and reading it is reliable at, **checks** his
  numbers and a vendor's numbers against the plans, and organizes what has to be asked of
  vendors and subs. Where it does not estimate a quantity, it must still speed up his
  process and his organization.

Plan reading stays, as one input among these. The prices and the lines stay his.

## Why

Two sources agree. The market research of 2026-11-19 found that builders distrust prices
they did not set, that AI plan reading is unproven on custom residential drawings, that
missed scope is where money is lost, and that setup effort is the top complaint about
every tool. Our own Job A test found the same shape: reading and counting passed
exactly, scope passed, measured quantities ran 21% low because the plans do not show how
much he buys.

The owner, a builder himself, added the working picture: builders work from their own
lines, but calculations and takeoffs without dedicated software take real time. Some
quantities he sends to his lumber supplier or other vendors with the plans; for what he
buys himself he already knows how much to get. So the value of the AI is in checking
numbers and in speed and organization, at the very least.

## Considered instead

**Plan reading as the centrepiece, drafting 80% of the estimate from the drawings.** The
original pitch. Not dropped, but no longer what the product leads with, because the
evidence for it is the weakest.

**No AI estimating of quantities at all; a faster spreadsheet only.** Rejected by the
owner: takeoffs take time, and an AI that can at least check numbers is worth having.

**Automatic market prices.** Out, as before (hard rule 1).

## What it costs us

"It reads your plans" is the more exciting promise, and this is a quieter one. The
evidence on where a small builder's estimating time actually goes is partly inference;
the market researcher found no data. The split of work this implies (which quantities
the tool counts, which come from a vendor's takeoff, which he enters, which wait for a
sub's bid) is not designed yet. **Proposed by Claude, not decided:** each line item
records who figures its quantity, so the tool knows whether to count, check, ask or stay
out of the way. The owner likes the idea and added that it needs a default,
so a line item works before he has set it up (his words below). **Proposed default:** a
line his sheet already marks as a sub's bid starts as "sub's bid"; every other line starts
as "he enters it", with the tool's own count shown beside it as a check wherever it has
one. He changes any line when he wants to, and the choice is kept in his template. To be
decided in phase 1, when it can be seen in the flow.

It is tested on the rough clickable version (decision 0011), including whether typing
prices is as fast as a spreadsheet.

## His words

> Yes to all, but for number two builders work for our own lines, but doing the
> calculations and takeoffs without a dedicated software takes time

> some things they just [send] the plans over to their lumber guys or vendors, but if
> he's picking up stuff from a hardware store or whatever he's gonna know how much to get

> some type of AI behind the system that could at least help him go check numbers might
> be valuable. At the very least if it doesn't estimate certain things it has to at least
> speed up his process and organization.

> I'm just trying to think of a way of how to get the AI we have behind this [to] speed
> [up] his process of estimating the most, to give them the most value.

On who figures each quantity:

> I like your proposed idea, but I think it needs a default state for him to use until he
> does set each line item up

(Dictated; bracketed words added for sense.)

## Links

- `docs/history/2026-11-19-method-audit/README.md` (proposal 3) and `market-research.md`
  beside it.
- Decisions 0020 (templates from his lines), 0022 (sub bids are not modelled), 0026 (a
  vendor's quantity beside ours) and 0046 (double-check these first).
- `docs/method.md`, steps 4 and 5.
