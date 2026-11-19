---
number: 0009
title: The tool is built for this one builder, not for builders in general
status: accepted
date: 2026-11-19
decided_by: owner
area: product
supersedes:
superseded_by:
---

## Decision

The estimator is built for the one builder it serves. Where his way of pricing differs
from how most builders work, his way is what we build.

**Reading, Inferred:** the owner was offered "this builder first, with his habits stored
as settings so other builders could be served later" and answered with the builder's
name only. That is read as: for him, without building for the general case now. The
owner can correct this reading; nothing built so far depends on it.

## Why

Asked after the full review of 2026-11-19, where a "general builder" reviewer and the
pricing reviewer both found that much of what is locked copies his sheet (one markup on
everything, contingency by group, tax counted inside each division). The owner chose to
stay with the builder the tool exists for. It also keeps the tool small.

## Considered instead

**This builder first, with his habits kept in a per-builder profile of settings.**
Claude's recommendation, on the grounds that it is cheap now and expensive later. Not
taken.

**Build for builders in general.** Never proposed as the first step; it would mean
per-line markup, one contingency line, switchable tax and more, before the tool has
been proven on one builder.

## What it costs us

Serving a second builder later means reworking what is hard-wired to his sheet: the
three price columns, filing by who does the work, tax inside divisions, contingency by
group, one markup on the total. The review findings that only matter for other builders
are parked, not answered: a "no markup" switch per line item, a single contingency
line, and settings to switch tax or contingency off.

Findings that would help him too are not parked by this decision (see 0010).

## His words

> for 1 steve

## Links

- `docs/history/2026-11-19-full-review.md`, sections 2, 3 and 5.
- Decision 0002 (markup on the total) and 0004 (contingency by group): both stand as they are.
