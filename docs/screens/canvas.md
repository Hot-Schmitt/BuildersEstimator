# The design canvas: where the drawings live

**Purpose:** says where the four screen drawings are and how to read them. The drawings' code is **not** copied into this repository (Decided by Claude, Nov 19, 2026; reversible).

- **Canvas:** "Estimate screen - laptop", https://claude.ai/artifact/GjPdu5gWFBHuPJGB8kaTgu
- **Version when this note was written:** 1795033492-e548 (Checked, Nov 19, 2026). The design document was written from version 1794889583-320a; what changed between the two was not checked.
- **Which wins:** `laptop-screens-design.md`, beside this file, wins over the canvas wherever they differ, and the decisions in `decisions/` win over both.

## The drawings (Checked against the canvas file list, Nov 19, 2026)

| File on the canvas | Drawing | Size in bytes | sha256 |
|---|---|---|---|
| `project/Main.dc.html` | The estimate, working on one division | 28,937 | c9bf7960e7d35daa0dbabd4c0e98117f4050b3b26e926c311597792ae03a581f |
| `project/LineItemDetails.dc.html` | Line item details pop-out | 6,038 | e8f05b7f9ebfcaa038723b8416666632e0a394800f6f563f1dda84a472c6c0fd |
| `project/RemoveConfirm.dc.html` | Remove a line item (confirmation) | 1,904 | 6397dbfc31699b9982a1d1ac5bc3d6d4520168fff0145526c08453d193107a0f |
| `project/FinalizeWarning.dc.html` | Finalize warning | 3,421 | 8238d31cce070ead577c985b2301e8d4fcf4d2685e3df5136ef24dba99238067 |
| `project/canvas.json` | How the four are laid out on the canvas | 729 | 64ecb19bb2c3ac9e7e9a78b483ed181ace7dd82fd9630e1a7c9255586f7f6998 |

## Why the code is not copied here

- The canvas is the one place the drawings are edited. A copy here would be a second source that goes stale the first time the canvas changes.
- The canvas files reach a chat as text, one at a time, so a copy would have to be retyped by hand (about 41 KB), which is how copying slips happened before.
- The drawings are a direction, not a locked build source, and a rough clickable version comes before any lock (decision 0011).

**What this costs:** the drawings can be read only from a Claude session signed in to the owner's account. A session that has the repository alone (an editor on another machine, for example) sees the design document and not the pictures. If that becomes a problem, copy the five files here and check each against the sha256 above.
