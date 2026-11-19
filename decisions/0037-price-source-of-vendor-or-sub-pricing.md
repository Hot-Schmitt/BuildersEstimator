---
number: 0037
title: A price source of vendor or sub pricing, with who confirmed it
status: accepted
date: 2026-11-16
decided_by: owner
area: format
supersedes:
superseded_by:
---

## Decision

The format gains a price source, "vendor or sub pricing", recording who confirmed it and
keeping the earlier figure beside it. It names its vendor or sub: a contact from the
read-only contacts copy, or a name typed for this job and marked as not in his contact
list. Part of version 0.5.

## Why

The screens show "Current: figure, where it came from", and rule 1 (his prices only)
needs a record of who confirmed a price while the owner confirms on the builder's
behalf. The format's price sources could not say either.

## Considered instead

**Recording applied pricing under an existing source such as "his entry".** It would
lose where the price came from and who confirmed it.

## What it costs us

Vendor and sub names are real data inside an estimate file: they stay on the owner's
computer and are redacted on test files.

## His words

> lock all and go

One reply locked all nine decisions that came out of the screens self-review of
2026-11-16; this was number 4.

The vendor or sub name was added the next day:

> lock 4a

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 3,
  checked against the working log, part 3, section 2 and part 4, section 2.
- `docs/format.md`, section 11, item 7.
- Decision 0024: choosing the vendor or sub.
