---
number: 0012
title: The builder's figures and line wording may be in the repository; names never
status: accepted
date: 2026-11-19
decided_by: owner
area: data
supersedes:
superseded_by:
---

## Decision

The builder's own cost figures and his line wording may be stored in this repository.
Client names, street addresses, phone numbers, tax and bank details, and vendor or
subcontractor names may not, and the original plan sets never come in. Every writer
goes through the one redaction step, and nothing is written while a listed name
survives.

## Why

The scripts and the test job cannot be moved, tested or reviewed here without his
figures. The repository is private. What could harm someone else, the personal and
third-party identifying data, stays out.

## Considered instead

**No real or redacted job data in the repository at all; code and made-up test data
only.** This was the rule in the old project documents (the start page, the screens
build plan and the current-state document). It was replaced on 2026-11-18, when the
owner approved figures and wording, and confirmed on 2026-11-19 after the full review
found the two rules in conflict. The older rule has no decision file of its own; when
it is backfilled, mark it superseded by this one.

## What it costs us

His margins and prices sit in a hosted repository, so who has access to it matters.
Blind-test answers for a job now live beside the tools that run blind tests; where they
sit, so a blind run cannot open them, still has to be laid out before the job files
move in.

## His words

> lock 4

## Links

- `AGENTS.md`, "What never enters this repository".
- `docs/history/2026-11-19-full-review.md`, section 1, item 3.
- `docs/method.md`, "Keeping a blind test blind".
