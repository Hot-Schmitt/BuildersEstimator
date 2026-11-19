---
number: 0042
title: Screens are drawn at real size, and a review counts only from rendered pictures at three widths
status: accepted
date: 2026-11-16
decided_by: owner
area: process
supersedes:
superseded_by:
---

## Decision

A screen is drawn at its real size on a design canvas, not inside the chat. Before it is
sent, every screen is looked at as a real screenshot at three widths: laptop, small
window and phone. Reviewers get all three, and the report says which widths were
checked. A review does not count unless the reviewer looked at a rendered picture.

## Why

Three laptop sketches were drawn inside the chat's narrow panel, in the chat's own
button style; the owner saw scrunched text and buttons that looked like containers,
after a review round had passed them. A later drawing re-flowed and collapsed at 900
wide and at phone width (one word per line, boxes over text), and the owner said his
confidence was low. Both reviewers had seen one picture at one width.

## Considered instead

**Judging a laptop layout at 720 wide inside the chat.** What was done; a laptop screen
cannot be judged at that width.

**Checking one render at one width.** What Claude did before telling the owner it had
looked at the screen.

## What it costs us

Three screenshots per screen per round, for Claude and for each reviewer, which adds to
the usage of every review.

## His words

What he saw on the sketches that led to the rule:

> A lot of the text looks very scrunched together... all your buttons look just like
> your containers

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, sections 4
  and 10, checked against the working log, part 4, sections 2 and 8.
- `docs/standards.md`, section 4 (recorded there as Said, Nov 16, 11 pm).
