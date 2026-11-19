---
number: 0055
title: A big build gets a self-check and then a fresh review; two review rounds for the screens build
status: accepted
date: 2026-11-16
decided_by: owner
area: process
supersedes:
superseded_by:
---

## Decision

A big build is a new screen, a new script, a change to the shared format, or a full
estimate run. Each gets:

- a **self-check**: run it, test it on real job data, look at every screen as a picture,
  check totals in code, check for leftover files;
- then a **fresh review** by a reviewer with no chat history.

Findings are reported ranked by impact, and nothing is called done while a finding is
open. For the screens build there are two fresh review rounds: one after the foundations
plus the first screen, one after the last screen.

## Why

Fresh reviewers have found what self-checks missed every time one has run: a wrong
total, a name that survived redaction, results reported too kindly, a check that could
be crashed.

## Considered instead

**A fresh review after every screen.** More rounds than two for the screens build would
cost more usage than the owner was asked for; two was the number locked.

**Self-check only.** The build of 2026-11-16 was reported "pass on self-check" and the
review that followed found three High problems in it.

## What it costs us

Usage. Past reviewers have used between about 85,000 and 184,000 tokens each, and the
owner is warned before a round. Work also waits on open findings.

## His words

> make sure that you are set up to build this project effectively and accurately...

The two rounds for the screens build:

> lock all and go

One reply locked all nine decisions that came out of the screens self-review of
2026-11-16; this was number 9.

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 7,
  checked against the working log, part 1, section 2 and part 3, section 2, and the
  project instructions ("Review after every big build or change").
- `docs/standards.md`, section 4; `docs/reviewers.md`.
- Decisions 0042 and 0043: how screens in particular are reviewed.
