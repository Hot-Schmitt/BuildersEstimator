---
number: 0041
title: Every screen is drawn for the owner first; a locked design becomes the build source
status: accepted
date: 2026-11-16
decided_by: owner
area: process
supersedes:
superseded_by:
---

## Decision

Before any screen is built, Claude draws it for the owner. Once he locks a design, it is
written down in a form the build can re-create directly: layout, parts, states, actions,
sizes and colours, with every control named. Screens are built from that document.

Button spacing is standardised, a design expert helps draw the screens, and approved
drawings are annotated.

## Why

The owner decides how the tool looks and works, and he can only decide on something he
can see. A locked drawing with no written form would be re-interpreted at build time.

## Considered instead

**Building screens straight from a description.** Not proposed; this rule exists to
prevent it.

## What it costs us

Drawing, annotating and documenting each screen before any of it runs is slow, and it
produced precise documents for a flow nobody had clicked through. Decision 0011 changes
the order: one rough clickable version comes before the lock. The locked sketch is still
the build source.

## His words

> before you build any screens or how it's going to look, make sure that you draw it out
> here for me. And when I lock the design, make sure that it's formatted in a way that
> you can use when drafting and building the actual screens

> standardize spacing on buttons so they're not stacked all odd... use a design expert
> to help you draw these and make sure that you're drawings after I approve them are
> notated and the information is in the format that when you build the actual screens,
> you're able to use whatever we lock on the sketch and re-create

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, sections 4
  and 7, checked against the working log, part 1, section 2 and part 3, section 2 (9:15
  pm).
- `docs/standards.md`, section 3.
- Decisions 0010 and 0011: what now comes before a lock.
