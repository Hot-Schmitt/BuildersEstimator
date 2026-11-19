---
number: 0030
title: Signing with a priced line item that has no cost code warns and does not block
status: accepted
date: 2026-11-16
decided_by: owner
area: format
supersedes:
superseded_by:
---

## Decision

When an estimate is signed while a priced line item has no cost code, the system prompts
a warning. It does not block the signing.

## Why

A missing cost code is worth his attention, because the operations app budgets by code,
but it is not a reason to stop him finishing an estimate.

## Considered instead

**Blocking until every priced line item has a code.** The other way the question could
have gone; the owner chose the prompt.

## What it costs us

Cost with no code can reach the operations app, where it has no budget line to land on.

## His words

> yes, the system should prompt

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 3,
  checked against the working log, part 1, section 2.
- Decision 0029: cost codes. Decision 0053: do not force him.
