---
number: 0034
title: The Method's rules move into the shared check
status: accepted
date: 2026-11-16
decided_by: owner
area: format
supersedes:
superseded_by:
---

## Decision

The Method's fixed rules are enforced by the shared check, so a file that breaks them is
refused whoever wrote it: a heading carrying money, an assumed quantity marked High, a
mark above its own quantity mark, a sub bid with a typed price, a dropped line, no
cover. A format change, part of version 0.5.

## Why

The rules lived only in the draft writer. The check passed files that broke them, so the
operations app could have been handed a bad file from any other writer. A High finding
in the fresh review of 2026-11-16.

## Considered instead

**Leaving the rules in the draft writer.** How it was built; safe only for as long as
there is exactly one writer.

## What it costs us

The dropped-line rule collided with templates, which leave lines out on purpose;
decision 0021 is the fix. The operations app must be told when 0.5 ships.

## His words

> lock review decisions 1 and 2 (yes each)

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 3,
  checked against the working log, part 2, sections 2 and 4.
- `docs/format.md`, sections 4 and 11 (item 3).
- Decision 0038: one way in for every estimate file.
