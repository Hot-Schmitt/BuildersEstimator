---
number: 0024
title: The vendor or sub is picked from the read-only contacts copy, or typed for this job
status: accepted
date: 2026-11-17
decided_by: owner
area: pricing
supersedes:
superseded_by:
---

## Decision

When pricing is added, the tool suggests the vendor or sub name it read from the pricing
document, and he picks from the contacts copy by search.

If they are not there, he types the name. It is kept for this job only, marked "Not in
your contact list", and added to a short reminder list of contacts to add to his real
list. When a later export contains them, the tool offers to link the two. The contacts
copy stays read-only.

## Why

Pricing needs a source name, for "where it came from" and for "this supplier went here
last time". The operations app owns the contact list, so the copy here stays read-only,
and nothing blocks him from adding pricing.

## Considered instead

**(b) The tool keeps its own editable contact list.** Rejected: two lists to keep in
step, against one source of truth.

**(c) Pricing cannot be added until the contact is in a fresh export.** Rejected: it
blocks his work.

## What it costs us

Typed names can pile up unlinked if the reminder list is ignored. Names are real data:
they stay on the owner's computer and are redacted on test files. The reminder list
lives in the job's own records, not in the estimate file.

## His words

> lock 4a

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 6,
  checked against the working log, part 4, sections 2 and 3 (decision 4).
- `docs/format.md`, section 11, item 7.
- Decision 0019: the contacts copy.
