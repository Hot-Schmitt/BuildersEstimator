---
number: 0059
title: Redaction runs from a name list with an automatic check, in one shared step
status: accepted
date: 2026-11-16
decided_by: owner
area: data
supersedes:
superseded_by:
---

## Decision

Redaction runs from a list of names, never from hand-picked rows. One shared redaction
step serves every script, matching whole names, longest first, and nothing is written
while a listed name survives.

- The name list is real data. It is never saved with the kit; it is rebuilt from the
  builder's own estimate file each time it is needed, and the owner is not asked to
  attach it.
- Product brands in his line wording are not vendor names and are kept. Subs, suppliers
  and clients are redacted.

## Why

A sub's name survived into a test file when redaction was a hand list of two row
numbers. Later four more names survived into a draft file, because a new script did not
reuse the redaction. Two misses of the same kind.

## Considered instead

**Hand-picking the rows to redact.** The first method, and the first miss.

**Each script carrying its own redaction.** The second miss.

**The owner keeping the name list and attaching it each time.** Replaced when a hand-off
asked him for a file he could not find.

**Treating product brands as vendor names.** Put to the owner as a choice; he kept them.

## What it costs us

A name the builder adds to a future sheet is caught only if it is spotted when the list
is rebuilt. And the list has to exist before any real file can be written: as of
2026-11-19 it exists nowhere and must be rebuilt, outside this repository (`STATUS.md`).

## His words

> For two, yes

On rebuilding the list each time:

> go with your proposal of making it the standard method

On brands, picked from the options offered:

> No, keep brands (Recommended)

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, sections 7
  and 10, checked against the working log, part 1, sections 2 and 8, and part 2,
  sections 2 and 6.
- `kit/redaction.py`; `AGENTS.md`, "What never enters this repository".
- Decision 0012: what may be in the repository.
