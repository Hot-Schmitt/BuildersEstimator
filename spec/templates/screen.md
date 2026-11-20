---
id: S-XXX
name:
kind: screen            # screen | panel | dialog
status: open            # open | proposed | locked | parked | retired
stories: []             # US- ids
objects: []             # O- ids
decisions: []           # D-NNNN
drawing: (not locked)   # source/<file> sha256:<...>, filled at lock
---
<!-- Template for spec/screens/S-XXX.md: one file per screen, dialog or panel.
     Keep the column names of the Controls table exactly as they are:
     tools/check_spec.py reads them. Delete this comment. -->

## Purpose
One or two sentences: what he comes here to do. What this screen is NOT for.

## Entry and exit
| Comes from | By | Lands on |
|---|---|---|

| Leaves to | By |
|---|---|

## States of the whole screen
Always cover: first use or empty, loading, normal, error, read-only, too narrow.

| State | When | What he sees | What he can do |
|---|---|---|---|

## Controls
One row per control. The part of the id after "C-" is the id used in the built screen.
Under "Reads / writes": leave blank, or open each part with "reads" or "writes" and split
parts with ";" (for example: reads F-EST-TOTAL; writes F-EST-STATUS).

| Id | Type | Label (W-) | Does (A- or plain words) | Reads / writes (F-) | Rules (R-) | States | Does NOT do |
|---|---|---|---|---|---|---|---|

## Control detail
Only for controls that change data or state. One heading per control ("### C-…"), then
its acceptance cases as bullets that open with the id in bold:
"- **AC-AREA-NN** Given … when … then …". A case written under another control's
heading covers this control too if its text names this control's id.

## Keyboard and focus

## Edge cases
E- ids that touch this screen, one line each.

## Feasibility notes
Filled by the front-end and back-end reviewers: simple | moderate | hard, and why.
No decisions.

## Open points
