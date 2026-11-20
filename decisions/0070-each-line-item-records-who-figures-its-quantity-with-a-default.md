---
number: 0070
title: Each line item records who figures its quantity, with a default that needs no setup
status: accepted
date: 2026-11-19
decided_by: owner
area: product
supersedes:
superseded_by:
---

## Decision

Each line item records who figures its quantity: the tool counts it, a vendor's takeoff
supplies it, a sub's bid covers it, or he enters it. From that the tool knows whether to
count, check, ask a vendor, or stay out of the way.

**The default, until he sets a line item up:**

- a line his sheet already treats as a sub's bid starts as "sub's bid": blank, with the
  last known price beside it;
- every other line starts as "he enters it", with the tool's own count shown beside his
  box as a check wherever it has one.

He changes a line only when he wants to, and the choice is kept in his template, so it is
set once. How it looks and where it sits are drawn in phase 1.

## Why

It follows from decision 0068: builders send some quantities to their lumber supplier or
other vendors, know others by heart, and want the AI to check numbers and speed up the
rest. Without a default, every line item would be a setup chore before he could use the
tool at all, which is the top complaint about every estimating product.

The default cannot put a wrong quantity into his estimate, which keeps hard rule 2
(never invent a number).

## Considered instead

**No default: he sets every line item before using it.** The idea as first proposed. The
owner pointed out it needs a default state.

**"The tool counts it" as the default wherever the tool has a count.** More filled in on
day one, but it puts the tool's number in his estimate before one job has shown he
agrees with it. Kept as a possible upgrade for the reliable counts only (decision 0071).

## What it costs us

On day one the tool fills in fewer quantities than it could; he gets the speed-up line by
line as he switches lines over. One more setting per line item, hidden unless he looks
for it. The names of the four choices are working words and need checking against
builder wording (decision 0052).

## His words

> I like your proposed idea, but I think it needs a default state for him to use until he
> does set each line item up

> Go with default

## Links

- Decision 0068: the AI's job is to count, check and organize.
- Decision 0071 (proposed): starting reliable counts as "the tool counts it".
- Decisions 0020 (templates), 0022 (sub bids) and 0026 (a vendor's quantity beside ours).
