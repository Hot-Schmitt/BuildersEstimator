---
number: 0010
title: Design what the client receives before any more screens are locked
status: accepted
date: 2026-11-19
decided_by: owner
area: screens
supersedes:
superseded_by:
---

## Decision

Before any more screens are locked, the back half of the estimate is designed: what the
client receives (the proposal or client copy), where allowances and client selections
show, alternates, more than one sub or vendor bid on a line item, and what changed
between one version and the next.

## Why

The full review of 2026-11-19 found that the flow stops at Finalize. The builder
reviewer would trust the tool for a draft but not to get an estimate to a client; the
pricing reviewer found the client view undefined (it hides markup, and no rule says how
the prices the client sees are made up); the designer found most main tasks undrawn.
Designing these after the screens are locked would reopen them.

## Considered instead

**Lock the estimate screens first and design the client side later.** The order the
project was on. Rejected because allowances, alternates and competing bids change what
a line item has to show, so they change the screens that would have been locked.

## What it costs us

More to draw before anything is locked, and so a later first build. Several of these
need facts only the builder knows (what he sends a client today, how he presents
allowances and alternates); those go to `docs/builder/questions.md`.

## His words

> lock 2

## Links

- `docs/history/2026-11-19-full-review.md`, sections 2 (items 1, 2, 4, 5), 3 (items 6, 9) and 4 (item 1).
- Decision 0011: the rough clickable version these designs are tried in.
