---
number: 0057
title: The kit moves to a private repository, with no real or redacted job data in it
status: superseded
date: 2026-11-16
decided_by: owner
area: data
supersedes:
superseded_by: 0012
---

## Decision

The kit's code and made-up test data go in a private online code repository. No real or
redacted job data goes in.

## Why

Kit scripts saved in the claude.ai project came back to a chat as text, so running one
meant copying it to disk by hand. That cost was logged three times and caused one
mistake. A repository removes it. Keeping all job data out was the cautious first rule
for a hosted copy.

## Considered instead

**Keeping the scripts only in the project, or only on the owner's computer.** The first
is the copying cost above; the second meant chats could not open them.

## What it costs us

The data half of this rule could not hold: the scripts and the test job cannot be moved,
tested or reviewed without the builder's figures. The owner approved figures and line
wording on 2026-11-18 and confirmed it on 2026-11-19 (decision 0012). The repository
half stands and is done: this is that repository.

## His words

> lock all and go

One reply locked all nine decisions that came out of the screens self-review of
2026-11-16; this was number 8.

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 7,
  checked against the working log, part 3, section 2 and part 5, section 2.
- Decision 0012, which supersedes this one.
