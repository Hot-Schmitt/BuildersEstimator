---
number: 0029
title: Cost is tracked by his own cost codes, in three cost types, filed by his choice
status: accepted
date: 2026-11-16
decided_by: owner
area: format
supersedes:
superseded_by:
---

## Decision

Cost is tracked by the builder's own cost codes (93, read from his cost workbook), in
three cost types: Labor, Material and Subcontract. Subcontract can include materials.

- Every price column on a line item has a filing choice, because he files by who does
  the work, not by sheet column.
- One line item can split across cost codes (his paint line is half interior, half
  exterior).
- Sub prices follow the industry standard for where they are filed, with his own choice
  per line item.
- He can edit cost codes and categories. The picker shows suggested codes, puts his
  most-used codes first, and fills in from his list as he types.

## Why

The owner asked for it, and his cost codes are what join an estimate to his job budget
and to the operations app. With per-column filing and splitting, the estimate reproduces
his cost workbook's budget by code and type to the dollar on 38 of his 39 budgeted codes
(Checked on Job A; the one that differs is a cabinet install his sheet did not count).

## Considered instead

**The industry's five cost types (labor, material, equipment, subcontract, other).**
Checked 2026-11-16. We use his three and leave Equipment and Other until he needs them.

**Filing each price by its sheet column.** Format 0.2 did this; by type, 17 of his codes
did not match his workbook, because he files by who does the work.

## What it costs us

The Job A filing is read from one job. It becomes his default only when he confirms that
"who does the work" is his rule, which is a question for him.

## His words

> It should track cost by his cost codes, but allow him to edit cost codes and
> categories. Cost codes that are used most often appear at the top of the list...
> suggested cost codes and then the ability to type in

> Use industry standards for where sub prices go. But give a dynamic ability for him to
> choose... mostly labor, but sometimes a subcontractor includes materials and labor in
> their bid

On filing per price column and splitting (format 0.3):

> I approve your decision number one

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, sections 3
  and 9, checked against the working log, part 1, sections 2 and 4.
- `docs/format.md`, section 8; `kit/cost_codes.json`.
- Decision 0030: a priced line item with no cost code.
