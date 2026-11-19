---
number: 0045
title: Confidence on screen is two flags, High and Low, off by default
status: accepted
date: 2026-11-16
decided_by: owner
area: screens
supersedes:
superseded_by:
---

## Decision

On screen, confidence is two flags only: High and Low. They are off by default and
turned on in settings. The estimate file still stores High, Medium and Low, so the
shared format and the Method do not change; a Medium line item shows no flag.

## Why

When the owner first saw "Medium", "Low" and "plan minimum" on a sketch, he did not know
what they meant. They are the project's own working words, not a builder's.

## Considered instead

**Showing the Method's three marks on every line item.** What the first sketch did, and
what accuracy rule 7 in the project instructions still describes.

## What it costs us

With flags off, nothing on a line item says how sure the tool is; "Double-check these
first" carries that instead (decision 0046). The project instructions' rule 7 still says
a mark shows on every line; the replacement text was given to the owner on 2026-11-16
and the current-state document lists pasting it as owed.

## His words

> we just go with a high flag for confidence and a low flag for confidence and they're
> turned off by default on the system. You can turn them on through the settings

On the file still storing all three:

> lock 2A

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 4,
  checked against the working log, part 3, section 2 (9 pm).
- `docs/method.md`, step 7 (the three marks, unchanged).
