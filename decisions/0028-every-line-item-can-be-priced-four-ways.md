---
number: 0028
title: Every line item can be priced four ways, with a note
status: accepted
date: 2026-11-16
decided_by: owner
area: pricing
supersedes:
superseded_by:
---

## Decision

Every line item has "Priced by", with four single-choice options:

- by quantity: quantity times unit price (the default);
- per area: he picks a job measure such as heated square feet, roof area or wall area
  and types his rate; the area comes from the plans;
- lump sum: a sub's bid or his own figure;
- his own number: a typed amount with a note.

His choice is saved in the template. All four total the same way underneath. Format 0.5
carries the pricing way with its job measure, and a note on the line item.

## Why

He prices his own way, and the tool must not force another on him. Where the tool
measures a line item and he has no recorded way, it uses the industry-standard way to
measure it; the prices stay his.

## Considered instead

**One fixed way, quantity times unit price, for every line item.** How his sheet's
columns read, and what the first sketch showed. It cannot hold a per-square-foot rate or
a figure he simply types.

**Looking up market prices in the background from retailers.** Parked for a second
phase. Under rule 1 such a price could only ever be a note labelled "outside reference".

## What it costs us

Two more fields in the shared format. The label "By the square foot" does not fit a
measure in linear feet or roofing squares. Which job measures are offered, and where
each is read from, is not settled; which line items he prices per area, and by which
measure, only he can say.

## His words

> the app needs to have the flexibility for him to calculate cost on his own way or even
> to just enter it in with a note... Lock 1

> the most accurate way to create this AI pricing system is to overtime build a data set
> of his prices or prices that he confirms

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, sections 3
  and 4, checked against the working log, part 3, section 2 (9 pm).
- `docs/format.md`, section 11, item 8.
- Decision 0048: "Priced by" as drawn in the details pop-out.
