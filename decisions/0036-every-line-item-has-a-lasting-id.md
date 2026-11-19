---
number: 0036
title: Every line item has a lasting id that holds across estimates and templates
status: accepted
date: 2026-11-16
decided_by: owner
area: format
supersedes:
superseded_by:
---

## Decision

Every line item in his list has a lasting id that holds across estimates and templates.
A one-off line item gets its own. Part of version 0.5, done before any template work.

## Why

Templates, combining templates, assigning pricing, pricing requests and "went here last
time" all need to point at the same line item across estimates. Until now a line's id
lived inside one estimate, and decisions were keyed to his sheet's row numbers, so
adding or moving a row in his template would break every decisions file.

## Considered instead

**Keeping ids inside each estimate and keying decisions to sheet row numbers.** How the
kit works today; an open review finding since the first independent review.

## What it costs us

His line list and the Job A decisions have to be re-keyed, and Job A re-run and re-
scored, before anything else in 0.5 can be trusted.

## His words

> lock all and go

One reply locked all nine decisions that came out of the screens self-review of
2026-11-16; this was number 4.

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 3,
  checked against the working log, part 3, section 2.
- `docs/format.md`, section 11, item 5.
