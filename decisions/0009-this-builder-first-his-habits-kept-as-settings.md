---
number: 0009
title: This builder first, with his habits kept as settings and not hard-wired
status: accepted
date: 2026-11-19
decided_by: owner
area: product
supersedes:
superseded_by:
---

## Decision

The estimator is built for the one builder it serves first. Where his way of pricing
differs from how most builders work, his way is what we build. But his habits are kept
as settings in one builder profile, not written into the core, so a second builder
could be served later without a rewrite.

What belongs in the profile: his three price columns and how each is filed, his unit
spellings, where tax is counted, how contingency is carried, and how markup is applied.

## Why

Asked after the full review of 2026-11-19, where a "general builder" reviewer and the
pricing reviewer both found that much of what is locked copies his sheet (one markup on
everything, contingency by group, tax counted inside each division), and the engineer
found those choices hard-coded in the scripts. Keeping them in one profile is cheap
now and expensive to add after the screens and the service are built.

## Considered instead

**Built for this builder only, with no settings layer.** Claude first read the owner's
short answer ("for 1 [the builder]") this way and recorded it; the owner corrected it the same
night. It keeps the tool smallest today, at the price of rework for any second builder.

**Build for builders in general now.** Never proposed as the first step; it would mean
per-line markup, one contingency line, switchable tax and more, before the tool has
been proven on one builder.

## What it costs us

A little more structure now: one profile file and the discipline to read from it.
The profile only holds what this builder needs. Options other builders would want are
not built until a second builder exists: a "no markup" switch per line item, a single
contingency line, and switching tax or contingency off. Those review findings are
parked, not answered.

## His words

> [the builder] first

## Links

- `docs/history/2026-11-19-full-review.md`, sections 2, 3 and 5 (item 7).
- Decisions 0002 (markup on the total) and 0004 (contingency by group): both stand as they are, as this builder's settings.
- The builder's first name in the two quotes above was replaced with "[the builder]" on 2026-11-19, to keep the rule in `AGENTS.md`. Nothing else in the quotes changed.
