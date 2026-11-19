---
number: 0011
title: Build one rough clickable version, and try it, before screens are locked
status: accepted
date: 2026-11-19
decided_by: owner
area: process
supersedes:
superseded_by:
---

## Decision

Before the screen designs are locked and written up in detail, one rough clickable
version is built on made-up data, covering an estimate from start to finalize. The
five tasks are run on it. Only then are the screens locked and the component and
spacing system written, once.

## Why

The designer in the full review of 2026-11-19 found precision being written ahead of
proof: pixel tables exist for a flow nobody has clicked through, only four screens are
drawn, and the design document disagrees with the canvas and with newer decisions.

## Considered instead

**Keep drawing each screen at real size, review it, lock it, then build from the locked
source.** The process in `docs/standards.md`, section 3. Not thrown away: a locked
sketch is still the build source. What changes is the order; the rough version comes
before the lock.

## What it costs us

The rough version is throwaway work, and it has to be kept from quietly becoming the
product. `docs/standards.md` needs a line for this step; that edit is owed.

## His words

> lock 3

## Links

- `docs/history/2026-11-19-full-review.md`, section 4, "Process".
- `docs/standards.md`, sections 3 and 4.
