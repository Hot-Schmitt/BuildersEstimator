---
number: 0018
title: Signed estimates go to the operations app through one shared estimate format
status: accepted
date: 2026-11-16
decided_by: owner
area: format
supersedes:
superseded_by:
---

## Decision

Signed (locked) estimates go to the operations app the owner is building separately,
through one shared estimate format, by direct send or by export and upload. The two are
joined by the builder's own cost codes.

The operations app receives signed estimates only. Changes after signing are its change
orders, not new estimates here.

## Why

One format avoids building two editors, and the owner wants the estimate readable by the
other software he is building for the same builder.

## Considered instead

**Each tool keeping its own estimate layout.** Never proposed as such; it is what one
shared format exists to avoid.

**Keeping every locked estimate as a version findable by address or client name, inside
this tool.** Parked on 2026-11-16: it belongs in the operations app.

## What it costs us

The format is a contract. It cannot change without the owner's OK, a version number and
a notice to the operations app (decision 0040).

## His words

> should be readable by the other software that I'm building for him

> send any locked estimates that the client has signed directly to the software... or to
> export it and then upload it

On signed-only and change orders:

> I approve everything else

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, sections 1
  and 3, checked against the working log, part 1, sections 2 and 3.
- `docs/format.md`.
- Decision 0029: the cost codes that join the two.
