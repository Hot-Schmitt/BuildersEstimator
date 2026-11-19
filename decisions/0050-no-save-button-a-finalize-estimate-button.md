---
number: 0050
title: No save button and no unsaved marker; a Finalize estimate button instead
status: accepted
date: 2026-11-16
decided_by: owner
area: screens
supersedes:
superseded_by:
---

## Decision

Changes save automatically. The screen has no save button and no "unsaved changes"
marker; it shows "All changes saved". A **Finalize estimate** button pushes him to
finish, with a warning when any line item has no price. A small **Duplicate** button is
there because several draft versions can exist.

## Why

The owner asked for all three in the words below.

## Considered instead

**A "Save draft" button.** The owner first noticed there was none on the locked sketch;
shortly after, he said changes should simply save, which removes the need for one.

## What it costs us

Automatic saving changed the format's version rule (decision 0001) and needed a decision
on exactly when a change saves (decision 0008).

## His words

> A few things changed should save automatically... I don't see any button that pushes
> him to finalize the bid within warning in case any line items he added, don't have
> pricing and it might be nice to have a small duplicate button

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 4,
  checked against the working log, part 4, section 2 (11:25 pm).
- Decisions 0001 and 0008 (saving), 0006 (Duplicate stays visible), 0032 (the finalize
  warning).
