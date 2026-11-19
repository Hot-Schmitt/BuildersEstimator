---
number: 0017
title: He can change any number by hand, on screen, and his edits are kept
status: accepted
date: 2026-11-16
decided_by: owner
area: product
supersedes:
superseded_by:
---

## Decision

The builder can change any number on the estimate by hand, on screen. Every edit is kept
in the estimate's change list, so the system learns from what he changes.

## Why

He prices largely by gut and will overwrite anything he disagrees with. The tool has to
work within that, and his corrections are the best source there is for what it got
wrong.

## Considered instead

The log records no alternative. How an edit is kept did change: first every save was to
make a new version (decision 0031), now edits save into the current version and are
logged there (decision 0001).

## What it costs us

Every number on screen has to be editable in place, and every edit has to be logged, or
the learning this decision is for does not happen.

## His words

> He needs to be able... to easily change numbers manually

> he can do that on a screen... so that when things are saved, my system gets the
> updated copy

> we would learn where we went wrong

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 1,
  checked against the working log, part 1, section 2.
- Decisions 0001 and 0008: how and when a change saves.
- `docs/method.md`, step 9 (learning from what he changes).
