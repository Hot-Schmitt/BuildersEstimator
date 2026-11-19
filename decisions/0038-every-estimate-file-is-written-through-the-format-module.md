---
number: 0038
title: Every estimate file is built and written through the format module
status: accepted
date: 2026-11-16
decided_by: owner
area: format
supersedes:
superseded_by:
---

## Decision

Every script that writes an estimate file builds it through the format module, which
runs the shared check before it writes. The module's save is the only way a file is
written. The check itself is hardened so no bad file can crash it, and it enforces every
rule the format document states.

## Why

The first blind draft file carried the format's name and version but failed the shared
check with 1,015 problems: it was a worksheet borrowing the format's field names,
written by a script in a chat that did not have the format module. No reader of the
format could have opened it.

## Considered instead

**Each script writing its own file and labelling it with the format's name.** What
happened; the third mistake traced to the scripts not living in one kit.

## What it costs us

No quick one-off file can be written outside the module, even for a test. The module's
save also carries the redaction name check, so writing a real file needs the name list.

## His words

Picked from the options offered:

> Yes to 1-4 (Recommended)

Review decisions 1 and 2 of six from the second independent review.

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 10,
  checked against the working log, part 1, sections 2, 4 and 8.
- `kit/estimate_format.py`, `kit/write_draft.py`; `docs/format.md`, section 1.
- Decision 0034: the Method's rules join the same check in 0.5.
