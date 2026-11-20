---
number: 0001
title: Changes save into the current version; only Duplicate or Finalize makes a new one
status: accepted
date: 2026-11-17
decided_by: owner
area: format
supersedes: 0031
superseded_by:
---

## Decision

On an estimate that has already been created, every change the builder makes saves
into the version he is working on, when he leaves the box (decision 0008; this file
first said "as he types"). Each change is still written to that
version's change list, so the system can learn from his edits.

A new version is created in only two ways:

- **Duplicate**, which asks whether he wants it with data (quantities and prices kept)
  or without (line items only).
- **Finalize**, which closes the version so it cannot be changed.

Applying vendor or subcontractor pricing does **not** create a version. Undo reverses
that one apply as a group, from the change list.

## Why

The owner's reason, in his words below: a builder collecting ten subcontractor quotes
on one job would end up with ten versions of his estimate and no way to tell them
apart. Version history is only useful if a version means something.

## Considered instead

**Every save makes a new version.** This was the rule in shared format 0.4 and it was
locked earlier. It came from a sound instinct — nothing is overwritten, every edit is
recoverable — but it treats a keystroke and a milestone as the same event.

**Apply vendor pricing makes a version.** Claude proposed this as an addition, on the
grounds that undo needs a version to roll back to. The owner turned it down for the
same reason as above. Undo was rebuilt on the change list instead, which works and
does not multiply versions.

## What it costs us

Rolling back is now a change-list operation rather than switching to an earlier file,
which is more code and more that can go wrong. A version is also no longer a snapshot
of every intermediate state, so if a builder makes a mess inside one version, undo is
the only way back rather than reverting to a clean earlier copy.

## His words

> that wouldn't be very easy to use if he gets say 10 subcontractor and vendor quote
> that he wants to add to the current estimate and he ends up having 10 versions that
> gets confusing for a builder

On when saving applies:

> Yes, when he's on the actual estimate that's already been created from a template

## Links

- Shared estimate format, `docs/format.md` — this is one of the twelve changes
  approved for version 0.5, which is built in one step.
- Decision 0031: the earlier "every save makes a new version" rule, which this
  supersedes (backfilled 2026-11-19).
- The operations app must be told when 0.5 ships; the format is a contract with it.
