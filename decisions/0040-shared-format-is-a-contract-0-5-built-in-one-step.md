---
number: 0040
title: The shared format is a contract; version 0.5 is built in one step with one notice
status: accepted
date: 2026-11-16
decided_by: owner
area: format
supersedes:
superseded_by:
---

## Decision

The shared estimate format is a contract with the operations app. It changes only with
the owner's OK and a version number, and the operations app is told.

Version 0.5 (twelve approved changes) is built in one step, with one notice to the
operations app for all of it.

## Why

The operations app reads what this tool writes. Telling it once about one finished
version is cheaper and safer than a string of notices about half-built ones.

## Considered instead

**Building each change as it is approved, with a notice each time.** Never proposed; the
changes arrived over three days and were gathered so the other side hears once. The
notice owed for 0.4 was folded into the 0.5 notice for the same reason.

## What it costs us

0.5 is a large step: twelve changes land together and none of them works until all of
them do. The specification for it is still spread across decisions and has to be written
as one clean document first.

## His words

> lock all and go

One reply locked all nine decisions that came out of the screens self-review of
2026-11-16; this was number 4.

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 3,
  checked against the working log, part 3, section 2, and the project instructions
  ("Building the software").
- `docs/format.md`, section 11.
- Decision 0018: why there is a shared format.
