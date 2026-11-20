---
id: O-XXX
name:
status: open            # open | proposed | locked | parked | retired
decisions: []           # D-NNNN
---
<!-- Template for spec/objects/<name>.md: one file per object (estimate, line item,
     template and so on). Keep the column names of the two id tables exactly as they
     are: tools/check_spec.py reads them. Delete this comment. -->

## What it is
One paragraph. What the user would call it (W- id).

## Relationships
| Relates to | How | Note |
|---|---|---|

## Actions
Every action a person or the system can take on it. Each has a home control, or says
"deliberately none" and why, or is marked open.

| Id | Action | Who | Allowed in states | Home control(s) | Rules | Status |
|---|---|---|---|---|---|---|

## Lifecycle
| State id | Name on screen | Meaning | Who may edit |
|---|---|---|---|

| From | Action | Guard (rules) | To | Side effects |
|---|---|---|---|---|

## Stored
Where it lives and in what form (a section of docs/format.md, or an FT- note).
Fields: `spec/fields/<name>.yaml`.

## Open points
