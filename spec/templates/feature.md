---
id: FT-NAME
title:
status: options         # options | decided | parked
decided_in:             # D-NNNN once the owner has picked
stories: []             # US- ids
rules: []               # R- ids
---
<!-- Template for spec/features/FT-<name>.md: the options considered for building one
     feature. Developers and reviewers give options, build time and feasibility; the
     owner picks; the pick becomes a decision file and this note points at it.
     Delete this comment. -->

## The need
What must be true for the user, in two sentences. No technology.

## Appetite
How much build time this is worth (small: under a day · medium: days · large: a week or more).

## Options
| # | How it would be built | Build time | What it makes easy | What it makes hard or risky | Feasibility (FE / BE) |
|---|---|---|---|---|---|

## Recommendation
Which, and the one-line reason. Labelled Proposed until the owner answers.

## Rabbit holes
Details that could swallow time, each closed with a sentence.

## No-gos
What this feature will deliberately not do in the first release.

## Edge cases it must survive
E- ids.
