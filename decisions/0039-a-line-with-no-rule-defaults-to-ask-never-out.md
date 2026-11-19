---
number: 0039
title: A line with no rule defaults to Ask, never Out
status: accepted
date: 2026-11-16
decided_by: owner
area: testing
supersedes:
superseded_by:
---

## Decision

A line the draft has no rule for defaults to Ask, never Out. Section headings are
carried as headings. Nothing is dropped silently, and every In, Out and Ask needs a
reason. The draft writer applies this, not a person.

## Why

The first blind draft marked every row it had no rule for as Out with one blanket reason
(all 247 Out lines). That is how his electrical bid, plumbing install and framing labor
were missed: about 40,000 of his cost sitting on lines the draft had thrown out.

## Considered instead

**Out as the default for a line with no rule.** Written for speed in the first draft
script, against the method's own step 4.

## What it costs us

Ask as the default produced 183 identical Ask lines on the Job A remake, too many for
him to answer. Templates by job type are the answer to that (decisions 0020 and 0021).

## His words

Picked from the options offered:

> Yes to 1-4 (Recommended)

Review decision 3 of six from the second independent review. **Decided by Claude, and
different from the decision's wording:** his total rows are not carried as headings.
They are left out of the line list, because the totals block replaces them.

## Links

- Backfilled on 2026-11-19 from the project's "17 Current state" document, section 10,
  checked against the working log, part 1, sections 2, 3, 4 and 8.
- `docs/method.md`, step 4; `kit/write_draft.py`.
