# Design document: laptop screens

**Moved here Nov 19, 2026** from project document "16 Estimator - Design document, laptop screens". The text below is unchanged apart from the title (see the change log at the foot).
**Reading the references:** "doc 07" is the old working log (not in this repository yet), "doc 09" is `docs/standards.md`, "doc 10" is `docs/format.md`. `decisions/` holds the decision records.
**Behind the decisions on these lines; the decision wins until this document is brought into line:**
- Section 3, fix 4, and the price and amount rows in section 5: line item amounts and subtotals now show cents (decision 0007).
- Section 3, fix 6, and the top bar table: Duplicate is a visible small button, not an entry in the More menu (decision 0006).
- "Saves as typed" on the quantity and price boxes, "Changes save as you type", and section 8: a change saves when he leaves the box (decision 0008). The keyboard rules in section 8 are locked, no longer Proposed.
- Section 11, points 1 to 4, are answered (decisions 0002 and 0006 to 0008).
- **Missing:** the Tax chip and its states and the division tax line (decision 0003); the material and labor split in Details (decision 0005); the percent or dollar switch and the "does not grow" note on the cost summary (decision 0002); contingency by group (decision 0004); the tax question when pricing is applied (decision 0003).
- **Order of work has changed:** the back half of the estimate is designed, and one rough clickable version is tried, before any more of this is locked (decisions 0010 and 0011).

**Purpose:** the build source for the estimator's laptop screens. It says what each screen shows, names every control, gives its states and what it must do, and records the sizes, colours and wording. The screens are built by re-creating this document together with the drawings on the design canvas.
**Status:** first pass, Nov 17, 2026. Covers only what is already drawn on the canvas "Estimate screen - laptop" (four drawings), with the eight fixes and the Nov 17 decisions written in. **Not reviewed by a fresh reviewer and not locked.** Screens not yet drawn are listed in section 9.
**Sources:** the canvas code, read Nov 17 (files Main, LineItemDetails, RemoveConfirm, FinalizeWarning; canvas version 1794889583-320a). Decisions: doc 07 parts 2 to 5. Standards: doc 09.
**Which wins:** the canvas was not redrawn (Said, Nov 16: no redraw now). Where this document and the canvas differ, **this document wins**; every difference is listed in section 3. The canvas is brought into line when the undrawn screens are added (Decided by Claude; reversible).
**Labels:** lines are Checked against the canvas code unless marked Said, Proposed, Inferred or Decided by Claude.

## 1. Principles for these screens
1. **He is never forced to work a way he does not want (Said, Nov 17).** Within our limits, the tool accepts his way of doing a thing. A rule that blocks him must have a way through that he controls (example: a typed 0 satisfies a required rate).
2. Laptop first, phone second (Said). Target windows: 1366 × 768 and 1440 × 900 (Proposed).
3. The screen guides him through the estimate and draws the eye to what needs attention and what he is working on. It must not feel like a spreadsheet (Said).
4. Changes save automatically. No save button, no "unsaved" marker (Said).
5. His lines, his prices. Nothing on screen is a price that is not his; a blank stays blank and is marked (accuracy rules 1, 2 and 10).
6. Wording: "line item", never "row"; "quote" is not used for vendor or sub pricing; "estimated range" (Said).

## 2. The screens in this pass
| # | Screen | Canvas drawing | Size as drawn |
|---|---|---|---|
| A | Estimate, working on one division | Main | 1360 wide |
| B | Line item details (opens over the right side) | LineItemDetails | 480 × 800 |
| C | Remove a line item (confirmation) | RemoveConfirm | 480 × 280 |
| D | Finalize warning (line items not priced) | FinalizeWarning | 560 × 460 |

## 3. Where this document differs from the canvas
Fixes 1 to 8 were approved Nov 17 ("yes to all"). 9 to 12 were found by Claude while reading the code for this document and follow from decisions already made. How each is done is Proposed unless marked.

| # | On the canvas | In the build | Why |
|---|---|---|---|
| 1 | One tall page, 1340 high; back and next, the cost summary and lower divisions fall below a laptop screen | The page fills the window and never scrolls as a whole. The top bar is fixed. The left column scrolls on its own. The line item area scrolls on its own. The back and next bar is pinned to the bottom of the line item area, always visible | Known issue 1 |
| 2 | A division with nothing priced shows "$0" (Electrical, Plumbing) | It shows "Not priced". A division that is partly priced shows its amount, with the needs-pricing icon and count beside its name | Known issue 2 |
| 3 | A lump-sum line item shows a quantity box with "1" and the unit "LS" | A lump-sum line item shows no quantity box and no unit. The words "Lump sum" sit across those two columns and the price box holds the amount | Known issue 3 |
| 4 | Unit prices show cents ("$10.50", "$3,500.00"); amounts show whole dollars | **Decided by Claude:** a unit price always shows cents. Amounts, subtotals and totals show whole dollars on screen. A lump-sum price shows whole dollars unless he types cents. The file and the exports keep cents | Known issue 4 |
| 5 | The price cell of an unpriced line item says "Add pricing" | It says "Enter price" (Said, Nov 17). Pressing it turns the cell into a price box with the cursor in it. "Request pricing" (emails vendors and subs) and "Add vendor or sub pricing" (a pricing document received) keep their names | Known issue 5 |
| 6 | No way to reach settings, the job's documents or the plans status | A plans status line under the job name ("Plans read Nov 12 · 14 pages" or "Plans waiting to be read"), which opens the job's documents. A "More" menu at the right of the top bar holding Job documents, Duplicate, Export and Settings. Request pricing, Add vendor or sub pricing and Finalize estimate stay as buttons | Known issue 6. Also takes the top bar from five buttons to three plus a menu |
| 7 | "Needs your decision" and "Double-check these first" are not explained | Each list opens with one sentence under its title, and the same sentence shows when the pointer rests on the entry in the left column. Needs your decision: "Things found on the plans or in pricing that only you can answer." Double-check these first: "Line items where the number is most likely to be off, biggest dollars first." | Known issue 7 |
| 8 | No undo | An "Undo" link beside "All changes saved" reverses the last change; Ctrl+Z does the same. After a remove or an apply of pricing, a short message at the bottom offers "Undo" for that one action. Undo works from the change list | Known issue 8; doc 07 part 4 (undo method) |
| 9 | The details pop-out's foot reads "Changes apply as you type. Save draft keeps them." | "Changes save as you type." There is no save draft action | Saving decision, Nov 17 |
| 10 | The finalize warning says "If you finalize now, the estimate goes out without them." | "If you finalize now, they are listed on the estimate as not included." | Decision 2a, Nov 17 |
| 11 | The finalize warning has no state for a blank rate | A second finalize message, section 7: a blank tax, contingency or overhead and profit rate blocks finalizing until he types a figure. A typed 0 counts | Decision 5, Nov 17 |
| 12 | Controls carry no ids, except the input boxes | Every control has the id given in sections 5 to 8 | Doc 09, section 3 (sketches) |

## 4. Look, as drawn
The user asked for a more premium button style and colour theme in the build, and icons wherever they help him read less (Said, Nov 16). The values below are the canvas as drawn. They are the starting point; a premium theme is proposed to the user before the first screen is built.

**Type.** Inter for text (400, 500, 600). Space Grotesk for the job name, headings and big money figures (500, 600). Sizes in use: 12, 13, 14, 15 (body), 16, 20, 22, 24, 28, 30, 32. Money uses tabular figures and is right-aligned on one edge.

**Spacing scale:** 4, 8, 12, 16, 24, 32. Page padding 32. Left column 280 wide; 32 between it and the main area. Main area padding 32.

**Sizes.** Every button, box and list entry is 44 high. Group bands and the back and next buttons are 48. The cost summary entry is 60. Corner radius: 8 (boxes in a line item), 10 (buttons), 12 (a tinted line item), 16 (cards), full (pills).

**Line item columns:** Line item (takes the spare width), Quantity 104, Unit 56, Unit price 132, Amount 112, actions 132; 16 between columns.

| Colour | Value | Used for |
|---|---|---|
| Page | #F3F4F6 | Background; group bands; the sum strip |
| Surface | #FFFFFF | Cards, top bar, boxes |
| Text | #17212F | Main text |
| Muted text | #566173 | Labels, counts, secondary lines |
| Secondary text | #3B4758 | Sub-lines on a tinted line item; dialog text |
| Line | #E3E6EB | Hairlines; #D5DAE1 for the divider above Cost summary |
| Box border | #7F8A99 | Input boxes, outlined buttons in the main area; #B6BEC9 on top bar buttons |
| Blue | #1D4ED8 | The one main action (Next); focus ring; chosen option |
| Blue tint | #EAF0FE | The line item being edited; the chosen "Priced by" option. #DCE6FD for the current division |
| Amber text | #9A4A06 | Needs pricing: text and icon |
| Amber tint | #FFF8EC | An unpriced line item; the "needs pricing" button. Pill #FFE3B8 with #8A4206; count badge #FFF1DC |
| Red | #B42318 | Remove line item (confirm) only |
| Grey | #6B7686 | The trash icon; chip #EEF0F3 for the version button |

**Colour rules (from the Nov 16 visual review, kept):** blue marks only where he is and the one main action. Amber marks only "needs pricing". Red only confirms a removal. One filled blue button per screen.

**Icons as drawn:** warning triangle (needs pricing), chevrons (open, closed, next, back, details), plus (add), trash (remove). More icons are added in the build where they help him read less (Said).

## 5. Screen A: the estimate, working on one division

### Layout
Top bar across the window. Under it, two columns: the left column (280) and the main area. Behaviour on a laptop window is fix 1 in section 3.

### Top bar
| Id | Control | Shows | Does | States |
|---|---|---|---|---|
| top-job | Text | Job name; under it client and job type | Nothing | |
| top-plans | Link (fix 6) | Plans status | Opens the job's documents | Read (date, pages; names pages that could not be read) · Waiting to be read (says why) |
| top-version | Pill button | "Draft estimate · Version 3" | Opens version history (not drawn) | Draft · Final · Signed |
| top-saved | Text | "All changes saved" | Nothing | Saving… · All changes saved · Could not save (says why, keeps trying) |
| top-undo | Link (fix 8) | "Undo" | Reverses the last change | Hidden when there is nothing to undo |
| top-request | Button | "Request pricing" | Opens request pricing | Off on a final or signed estimate |
| top-add-pricing | Button | "Add vendor or sub pricing" | Opens add vendor or sub pricing | Off on a final or signed estimate |
| top-finalize | Button, strong outline | "Finalize estimate" | Runs the finalize checks (section 7) | Off on a final or signed estimate |
| top-more | Menu (fix 6) | "More" | Job documents · Duplicate · Export · Settings | Export warns when line items are unpriced (Proposed) |
| top-duplicate | Menu entry | "Duplicate" | Asks: with data, or without (Said, Nov 17; not drawn) | |

### Left column
| Id | Control | Shows | Does | States |
|---|---|---|---|---|
| nav-total | Card | "Draft total", the amount, "Estimated range (low) to (high)" | Nothing | The range is blank when no prices are in |
| nav-not-in-total | Line in the card | Warning icon, "4 line items need pricing", "Not in this total yet" | Opens the Needs pricing list | Hidden when the count is 0 |
| nav-find | Box | Label "Find a line item", hint "Type a name" | Shows matching line items across all divisions (results not drawn) | |
| nav-needs-pricing | List entry | "Needs pricing" and an amber count | Opens that list in the main area (not drawn) | Count 0: entry stays, badge shows a tick (Proposed) |
| nav-needs-decision | List entry | "Needs your decision" and an amber count | Opens that list (not drawn); sentence per fix 7 | Same |
| nav-double-check | List entry | "Double-check these first" and a grey count | Opens that list (not drawn); sentence per fix 7 | Hidden when he has switched the list off |
| nav-div-(n) | List entry, one per division | Division name; needs-pricing icon and count where any; amount at the right | Opens that division in the main area | Current (blue tint, bold) · Has unpriced (icon and count) · Nothing priced ("Not priced", fix 2) |
| nav-cost-summary | List entry, last, under a divider | "Cost summary", "Tax, contingency, overhead and profit" | Opens the cost summary (not drawn) | Marked when a rate is blank (Proposed) |

### Main area, top
| Id | Control | Shows | Does |
|---|---|---|---|
| div-title | Heading | Division name, "23 line items" | Nothing |
| div-needs-pricing | Amber button | Warning icon, "1 needs pricing", chevron | Jumps to the first unpriced line item in this division and opens its group. Hidden when the count is 0 |
| div-total | Figure | "Division total" and the amount | Nothing |
| col-head | Column headings | Line item · Quantity · Unit · Unit price · Amount | Nothing |

### Groups
His own subtotal blocks inside a division (Framing materials, Framing labor, Trusses).

| Id | Control | Shows | Does | States |
|---|---|---|---|---|
| grp-(name) | Band button, 48 high | Chevron, group name, "19 line items", a needs-pricing mark where any, subtotal at the right | Opens or closes the group | Closed · Open · A group holding an unpriced line item opens by itself (Proposed) |
| grp-(name)-add | Text button under the group | Plus icon, "Add a line item to (group)" | Starts adding a line item (steps not drawn) | |

### A line item
| Id | Control | Shows | Does | States |
|---|---|---|---|---|
| li-(id)-name | Text | Line item name; under it one quiet line: how it is priced when not by quantity ("By the square foot · heated area"), or his note ("Note: …") | Nothing | |
| li-(id)-qty | Box, right-aligned | Quantity | Typed in place; saves as typed | Under it "From plans" when the quantity came from the plans; "Changed by you" once typed over (Proposed). Absent on a lump sum (fix 3) |
| li-(id)-unit | Text | Unit | Nothing | Absent on a lump sum (fix 3) |
| li-(id)-price | Box, right-aligned | Unit price, or the lump-sum amount | Typed in place; saves as typed | Decimals per fix 4 |
| li-(id)-amount | Figure | Amount | Nothing; worked out, never typed | "Not priced" when there is no price |
| li-(id)-details | Text button | "Details" and a chevron | Opens screen B for this line item | |
| li-(id)-remove | Icon button | Trash icon; spoken label "Remove (name)" | Opens screen C | |
| li-(id)-enter-price | Amber outlined button in the price cell (fix 5) | "Enter price" | Turns the cell into a price box with the cursor in it | Only on a line item with no price |

**Line item states**
| State | Looks like |
|---|---|
| Resting | White, a hairline under it |
| Being edited | Blue tint, rounded; the box in use has a 2-wide blue border and a soft blue ring; name in bold |
| Needs pricing | Amber tint, rounded; a "Needs pricing" pill with the warning icon beside the name; under the name its kind and last price ("Sub bid · last price $6,400 in 2022"); a third line when pricing was requested ("Pricing requested Nov 12"); "Enter price" in the price cell; "Not priced" as the amount |
| Removed | Gone from the group; listed under "removed line items" |

### Foot of the main area
| Id | Control | Shows | Does |
|---|---|---|---|
| div-removed | Quiet text button | "2 removed line items" and a chevron | Opens the list of line items removed from this division, each with "Put back" (list not drawn). Hidden when 0 |
| div-back | Outlined button, 48 high | Chevron, "Back to (previous division)" | Opens the previous division. Hidden on the first |
| div-position | Text | "Division 2 of 12" | Nothing |
| div-next | Filled blue button, 48 high | "Next: (next division)", chevron | Opens the next division, in his sheet's order. On the last division it reads "Next: Cost summary" (Proposed) |

## 6. Screen B: line item details
Opens over the right side of screen A, 480 wide, full height, with a soft shadow on its left edge. Screen A stays visible behind it. Opened by "Details"; closed by Close, Esc, or a press outside it (Proposed).

| Id | Control | Shows | Does | States |
|---|---|---|---|---|
| det-where | Text | "(Division) · (group)" | Nothing | |
| det-title | Heading and figure | Line item name; its amount | Nothing | Amount follows every change |
| det-priced-by | Four single-choice options, two by two | "By quantity" · "By the square foot" · "Lump sum" · "Your own number" | Changes how this line item is priced. The choice is kept in his template (Said) | Chosen one: blue border, blue tint, bold. Only "By the square foot" is drawn; the other three are owed (section 9) |
| det-area | Drop-down | "Area"; each choice is a job measure with its size ("Heated area · 1,150 SF") | Sets the measure | Shown for "By the square foot" only |
| det-rate | Box, right-aligned | "Price per SF" | Sets his rate | Shown for "By the square foot" only |
| det-sum | Strip | "1,150 SF × $10.50" and the amount | Nothing | |
| det-note | Text box, two lines | "Note", hint "Add a note" | Keeps a note on the line item; it shows under the name on screen A | |
| det-sources | Two lines | "Where the numbers came from": each number with its source ("Plans, page A-1"; "Entered by you, Nov 16") | Nothing | One line per number in use. Sources: plans with page · his past price with job and date · vendor or sub pricing with name and date · entered by you with date · assumed |
| det-cost-code | Line with a link | "Cost code": code, name and cost type; "Change" | Opens the cost code picker (doc 10, section 8; not drawn) | |
| det-foot | Text | "Changes save as you type." (fix 9) | Nothing | |
| det-close | Outlined button | "Close" | Closes the pop-out | |

**Open point:** "By the square foot" does not fit a measure in linear feet or roofing squares (doc 07 part 3). The label and the measure list are proposed with the cost summary drawing.

## 7. Screens C and D: confirmations

### C. Remove a line item
A dialog, centred, over a dimmed screen A.

| Id | Control | Shows | Does |
|---|---|---|---|
| rm-title | Heading | "Remove (name)?" | |
| rm-text | Text | "It comes off this estimate and the draft total. You can put it back any time from the removed line items at the bottom of (division)." | |
| rm-keep | Outlined button | "Keep it" | Closes; nothing changes. Esc does the same |
| rm-remove | Filled red button | "Remove line item" | Removes it, logs the change, closes, and offers "Undo" (fix 8) |

Removing is never silent and never final: the line item moves to the removed list with who removed it and when (accuracy rule 4).

### D. Finalize estimate
"Finalize estimate" runs two checks, in this order.

**Check 1: rates (decision 5, Said Nov 17).** If any tax, contingency or overhead and profit rate is blank, finalizing stops with a message naming each blank one and a button "Go to cost summary". A typed 0 counts as a figure, so he is never made to charge something he does not want to. Only a blank stops him. (Message not drawn.)

**Check 2: line items not priced (decision 2a, Said Nov 17).** If any are unpriced, this dialog opens:

| Id | Control | Shows | Does |
|---|---|---|---|
| fin-title | Heading with a warning icon | "4 line items are not priced" | |
| fin-text | Text | "They are not in the $262,500 total. If you finalize now, they are listed on the estimate as not included." (fix 10) | |
| fin-list | List | Each unpriced line item with its division, and "last price $6,400" or "no last price" | Nothing |
| fin-anyway | Outlined button | "Finalize anyway" | Finalizes. The estimate lists those line items as not included |
| fin-price-now | Filled blue button | "Price them now" | Closes and opens the Needs pricing list |

With no blanks and nothing unpriced, finalizing asks for one plain confirmation (not drawn), since a final version cannot be changed. A priced line item with no cost code prompts a warning and does not block (Said, Nov 16; doc 10).

## 8. Behaviour that a drawing cannot show
**Saving and versions (Said, Nov 17).** Changes save into the current version as he types; each is logged. A new version comes only from Duplicate or Finalize. Applying vendor or sub pricing does not make a version.

**Keyboard (Proposed, carried from doc 07 part 4; not yet put to the user):** Enter moves down the same column. Tab goes quantity, then price, then the next line item, and skips the icon buttons. Esc restores the box to what it held, or closes a dialog or the pop-out. Ctrl+Z undoes.

**Other (Proposed):** a quantity from the plans is labelled "From plans" and changes to "Changed by you" when typed over; a group with an unpriced line item opens by itself; Export warns when line items are unpriced; the version button opens version history; "Next" on the last division goes to the cost summary.

## 9. Not in this pass
Each is drawn at real size on the canvas for the user's lock, then added here.
- Cost summary (tax, contingency, overhead and profit), with the blank-rate message
- The three lists: Needs pricing, Needs your decision, Double-check these first (with its five checks and "Looks right", still open)
- Search results
- Adding a line item
- The removed line items list
- Settings; version history; the Duplicate choice; the plain finalize confirmation
- The other three "Priced by" states
- "Save as new template" and "Update this template"
- Cost code picker
- Laptop layouts of new estimate, add vendor or sub pricing (with choosing the vendor or sub, decision 4a) and request pricing
- Then the phone layout

## 10. Wording table
Doc 09 asks for every label to be checked against dated sources. **Owed:** no source was opened for this pass. "Source" below says where the label came from.

| Label | Why this word | Source |
|---|---|---|
| Line item | The user's fixed word | Said, Nov 16 |
| Estimated range | Replaces "likely range" | Said, Nov 16, 11 pm |
| Request pricing | Avoids "quote" | Said, Nov 16; a reviewer opened one help article, not re-checked |
| Add vendor or sub pricing | Avoids "quote" and "estimate" | Decided by Claude, Nov 16; kept by the user Nov 17 |
| Enter price | He types his own number | Said, Nov 17 |
| Draft total, Needs pricing, Needs your decision, Double-check these first, Priced by, By quantity, By the square foot, Lump sum, Your own number | From the Nov 16 design review; carried through the canvas the user accepted | Reviewer, "common usage, not checked" except Lump sum |
| Cost summary; Overhead and profit | Names the last entry by what it holds | Nov 16 usability review; not checked |
| Not priced; Not in this total yet | Says plainly what the total leaves out | Nov 16 usability review; not checked |
| Finalize estimate, Duplicate | The user's words | Said, Nov 16, 11:25 pm |
| Keep it / Remove line item | The action named on the button | Canvas; not checked |

## 11. Open points for the user
1. Section 3, fixes 6 and 8: the "More" menu, the plans status line, and where "Undo" sits (Proposed).
2. Section 3, fix 4: the decimals rule (Decided by Claude).
3. Section 8: the keyboard rules and the other Proposed behaviours.
4. Whether tax, contingency and overhead and profit can each be entered as a percent or as a dollar amount (raised Nov 17; doc 07 part 5).
5. The premium theme for the build (owed by Claude before the first screen).

## Change log
| Date | What changed |
|---|---|
| Nov 17, 2026 (11 am) | New document. First pass from the four canvas drawings, with the eight approved fixes, four more differences found while reading the code, the Nov 17 decisions, control ids, states, the look as drawn, a wording table with its sources owed, and the list of what is not drawn yet |
| Nov 19, 2026 | Moved into the repository as `docs/screens/laptop-screens-design.md` from project document 16. Title lost its number; a note on reading the references and a list of the lines that are behind the Nov 18 and Nov 19 decisions added at the top (the list is from working log part 5, section 3, with decision numbers added). No other line changed; the document was not brought into line |
