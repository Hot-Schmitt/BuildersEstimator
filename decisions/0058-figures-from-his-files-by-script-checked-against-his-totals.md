---
number: 0058
title: Any figure from his files is produced by script and checked against his own totals
status: accepted
date: 2026-11-16
decided_by: owner
area: data
supersedes:
superseded_by:
---

## Decision

Any figure taken from the builder's files is produced by script and checked against his
own total cells before it goes in a document. Documents that mirror his files are
written by script, not typed.

## Why

Two project documents reported his Job A cost as 220,903 against a true 231,247.05,
because they were built from cell values that read his formula rows (tax and
contingency) as zero. Then a second document missed every "Sub" line in his cost
workbook. Same cause both times: a partial reading of his file, not tied to the file's
own totals.

## Considered instead

**Reading values from his sheet and typing or adding them up by hand.** How the two
wrong documents were made.

## What it costs us

A script per kind of file he sends. The Job A import is written for that one sheet, and
a second job needs its own settings block.

## His words

> For two, yes

One reply approved two rules together: this one, and redaction from a name list
(decision 0059).

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, sections 7
  and 10, checked against the working log, part 1, sections 2 and 8.
- `docs/standards.md`, section 1; `kit/make_job_docs.py`, `kit/read_cost_workbook.py`.
