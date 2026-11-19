---
number: 0056
title: Hand off at a good stopping point, with decisions locked first and nothing for the owner to find
status: accepted
date: 2026-11-16
decided_by: owner
area: process
supersedes:
superseded_by:
---

## Decision

The written record is the memory, not the chat. A hand-off to a fresh chat happens at a
good stopping point (after a big step), not after every small run.

- The starter line comes in a copy-ready code block.
- When decisions are waiting, they are locked in the same chat first, or the starter
  says to lock them in the new one.
- A starter never asks the owner to attach or find a file. If he truly must do
  something, it says exactly what and where.

## Why

Each new chat costs usage to start, so hand-offs are rationed; but a chat that runs long
loses detail, so they cannot be skipped. A hand-off once told the owner to attach two
files without saying what or where they were, and he could not act on it.

## Considered instead

**A new chat after every small run.** Turned down by the owner: it drives up cost.

**Changing the hand-off wording in the project instructions.** The owner chose to leave
them as they were.

## What it costs us

Choosing "a good point" is a judgement, and a chat can run past the point where a hand-
off would have been clean. In this repository `STATUS.md` now does most of what the
hand-off documents did.

## His words

> give it to me in a code block... don't require a new chat after every small run

> don't give me the handoff until after I've locked it here, or tell me to lock it in
> the new chat

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 7,
  checked against the working log, part 1, section 2 and part 2, section 8.
- `docs/standards.md`, section 6; `STATUS.md`.
