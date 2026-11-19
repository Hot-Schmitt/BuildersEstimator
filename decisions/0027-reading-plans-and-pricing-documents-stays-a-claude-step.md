---
number: 0027
title: Reading plans and pricing documents stays a Claude step, run by the owner
status: accepted
date: 2026-11-16
decided_by: owner
area: product
supersedes:
superseded_by:
---

## Decision

Reading a plan set and reading a vendor's or sub's pricing document stay a Claude step
that the owner runs. The screens show "Waiting to be read", then the result. The paid
API is not used.

## Why

A screen running on a computer cannot read a document by itself. The only alternative is
the paid API, which costs money, and the service model (decision 0013) does not need it.

## Considered instead

**Calling the paid API from the screen, so reading happens when he drops a file.** Set
aside because it costs money; revisit if the tool is hosted or the builder gets his own
access.

## What it costs us

Reading is not instant and the builder cannot do it himself: someone has to run the
step. Creating an estimate is allowed with no documents, but reading the plans waits and
the screen says why.

## His words

> lock all and go

One reply locked all nine decisions that came out of the screens self-review of
2026-11-16; this was number 2.

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 6,
  checked against the working log, part 3, section 2.
- Decision 0013: run as a service.
