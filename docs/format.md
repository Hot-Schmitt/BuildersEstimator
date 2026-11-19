# Shared estimate format (version 0.4 built · version 0.5 approved, not built)

**Moved here Nov 18, 2026** from project document "10 Estimator - Shared estimate format", and brought into line with working log part 5 on the way (see the change log at the foot).
**Reading the references:** `method.md` and `standards.md` are the two files beside this one; `decisions/` holds the decision records. "doc NN" means a project document that is not in this repository yet: 01 Start here · 06 Questions for the builder (to become `docs/builder/questions.md`) · 07 Working log, parts 1 to 5 (to become `docs/history/`) · 11 Builder cost code list.

**Purpose:** the one data format every part of the system reads and writes: the estimator writes it, the editing screen edits it, the client view and Excel/CSV exports are made from it, and the operations app receives signed estimates in it. It is a contract: it changes only with the user's OK, with a new version number, and the operations app is told.
**Status:** version 0.1 approved by the user, Nov 16, 2026. Version 0.2 added his cost code and cost type rules (Said, Nov 16; section 8) and the fixes from the first independent review (doc 07, section 4). Version 0.3, approved by the user Nov 16, adds a filing choice for every price column and lets a line split across cost codes. Proven on Job A (section 9). **Version 0.4, approved by the user Nov 16 (review decisions 1, 2 and 5): a draft may hold a blank rate; the check cannot be crashed; every estimate file is written through the format module.** The operations app project must be told of 0.4 (not yet done; folded into the 0.5 notice).
**Version 0.5 is approved and not built: twelve changes, all listed in section 11.** Sections 1 to 9 describe 0.4 as built; where section 11 differs, section 11 is what will be built.

## 1. The file
- One estimate version = one JSON file. Every save makes a new version; nothing is overwritten. **(Changes in 0.5: section 11, item 1.)**
- Every version is a full file, so any reader needs only that one file. Each also lists what changed since the version before it (section 7).
- Size (Checked on Job A, 471 lines): about 141 KB as written, about 14 KB compressed. Stored compressed.
- Money in dollars, rounded to cents with halves rounded up, as his sheet shows them. Quantities as entered.
- Totals in the file are a convenience only. **Every reader recomputes them** with the shared check and rejects a file that does not match.
- **One way in (version 0.4):** every script that writes an estimate file totals it with the format module (fill_totals) and writes it with the format module (save). Save runs the check and looks for any listed name first; if either fails, nothing is written.

## 2. Top of the file
| Field | Meaning |
|---|---|
| format, format_version | "builder-estimate", "0.4" |
| estimate.id, job | Estimate id; job name (Job A on test files; the real address only on the user's computer) |
| job_type, parts | new_build · adu · renovation · mixed; a mixed job lists its parts |
| definition_level | sketch · permit_plans · plans_with_selections (sets the range) |
| status | draft → builder_editing → final → signed |
| version, parent_version | Version number (from 1) and the one it came from |
| made_by, made_at | estimator · builder · import; date and time |
| price_basis, currency, note | Date of the prices used; USD; a free note |
| divisions | His division numbers, with names and where each name came from (Inferred until he confirms) |
| groups | His subtotal blocks (the side subtotals in his sheet), so his layout survives |
| cost_codes | The cost codes this estimate uses: code, name, category (section 8) |
| cover | Drafts only, written by the draft writer: missing_pages, assumptions, exclusions, range (low, high, basis; blank on a draft with no prices), check_first (Medium and Low lines ranked by dollars × doubt) and check_first_note (how many doubtful lines have no dollars yet and so are not ranked) |
| signed | by, at, total. Required when status is signed; the total must equal the estimate total |
| totals | cost · markups (one per markup line) · total · by_division · by_code (budget by cost code and type) |

**(Changes in 0.5: the estimate will also hold its sales tax rate and the template it was made from; section 11, items 6 and 11.)**

## 3. Each line
One line per row of his sheet, in his order, his wording, his units. His own total rows are not lines: the totals block replaces them.

| Field | Meaning |
|---|---|
| id | Line id within the estimate |
| row, division, group | Where it sits in his layout. A markup line has no division |
| description | His wording (vendor, sub and client names redacted on test files; product brands are kept, Said Nov 16) |
| kind | heading · item · sub_bid · allowance · client_choice · percent · alternate |
| scope | in · out (on his checklist, not used) · ask (his call) · new (not on his list; shown in its own section) |
| qty, unit, unit_as_written | Quantity (never below zero; a credit is a negative price). Unit in capitals with DAYS and HRS merged into DAY and HR; his original spelling kept beside it |
| material, labor, ml | His three price columns, per unit. Cost = qty × (material + labor + ml) |
| qty_source | A record: type (written · dimensions · counted · calculated · assumed · his_entry), page and rule |
| price_source | A record: type (his_price · sub_bid · allowance · his_entry · none), job and date |
| confidence | A record: line (high · medium · low), the qty and price marks behind it, and a one-line reason. Required on every draft line; a reason is required for medium and low |
| cost_code | His cost code. He can change it on any line; the change is logged |
| cost_split | Used in place of cost_code when one line feeds two or more codes: each code with its share, shares adding to 1 (his paint line: half interior, half exterior) |
| filed_as | How each price column of this line is filed: labor · material · subcontract. Unless he says otherwise, material files as Material, labor as Labor and the combined column as Subcontract. He can change any of the three on any line |
| included | Alternates only: counts toward the total only when true |
| last_known | Beside a blank sub bid, client choice or rate: the last figure, its date and job |
| flags | plans_vs_estimate · engineering · hidden_condition |
| cost | Worked out by the check, never typed |

**Percent lines** (his tax, contingency and OH&P) carry percent_role (tax · contingency · markup · other), rate (0.25 for 25%) and base. For tax and contingency the base is the exact list of lines above it that it sits on, and the line has a cost type and may have a cost code. For markup the base is always all cost, so a line added later carries his markup. Markup is its own visible line, never folded into prices, and is always in scope (to charge none, the rate is 0). **(Changes in 0.5: markup may be a dollar amount; sales tax becomes a mark on the line item; contingency's base is given by group. Section 11, items 9 to 12.)**

**Blanks while the estimate is open (version 0.4).** While the status is draft or builder_editing, a percent line may have a blank rate, and an In line may carry a price with no quantity. Each adds nothing to the total, and the format module lists them (open_items) so the screen can show the estimate is not finished. A final or signed estimate may have neither. **(Changes in 0.5: section 11, item 2.)**

**Not in files yet:** price_key (the line's key in his price list). The Job A import marks every priced row as an item; which rows are sub bids or allowances is his to say (doc 06, question 6).

## 4. What the shared check enforces
Every reader runs it before trusting a file. It reports problems and never crashes on a bad file: every value is tested before it is used (Checked Nov 16: 4,275 damaged files, none crashed it). It fails a file when:
- any stored total (cost, markups, total, by division, by cost code) or line cost differs from the recomputed figure, or is not a number;
- the budget by cost code does not add up exactly to the cost;
- a quantity has no source record, is not a number, or is below zero;
- a draft (status draft, or made by the estimator) has a line with no confidence record, or a medium or low line has no reason;
- a tax or contingency line has no base, a base that is not above it or is a markup line, no cost type, or a rate outside 0 to 1;
- a rate is blank, or an In line has a price and no quantity, on a final or signed estimate;
- a markup line sits on anything other than all cost, or is not in scope;
- a mixed job does not list its parts;
- a line uses a cost code or division that is not in the estimate's lists;
- a filing choice names something other than a price column and a cost type;
- a cost split has fewer than two codes, an unlisted or repeated code, shares that do not add to 1, or sits beside a single cost code;
- a signed file lacks who signed and when, or its signed total differs from the estimate total;
- a change entry is missing a field; an id is missing or duplicated; a line or a block is not a record; a value is outside the allowed lists.

**Known limit:** from one file alone the check cannot see an edit that was saved without a change entry. The editing screen writes the entries; comparing a version with its parent comes with the local kit.

This is the 0.4 check as built. What the 0.5 check adds or changes follows from section 11 (items 2, 3, 9 to 12) and is written here when 0.5 is built.

## 5. Statuses and who may change what
| Status | Who edits | Meaning |
|---|---|---|
| draft | estimator | Made by the tool; never called a bid |
| builder_editing | builder | He is changing it on screen; every save is a version **(changes in 0.5: section 11, item 1)** |
| final | nobody | He is done; ready for the client |
| signed | nobody | Client signed; read-only; sent to the operations app |

The operations app receives signed estimates only (Said, Nov 16). Changes after signing are change orders and belong to the operations app (Said, Nov 16).

## 6. Made from it, never stored
Client view (hides cost and markup, collapses sub-lines), Excel export in his layout, CSV export. All made on request.

## 7. Change list (how the system learns)
Each version lists its changes against the version before: line, field, from, to, by, at, kind, and an optional two-word reason. Kinds: quantity · price · missing_line · extra_line · scope · cost_code · filing · other. These feed "07 Working log" section 5.

## 8. Cost codes and cost types (the join with the operations app)

### What the user asked for (Said, Nov 16)
- Track cost by the builder's own cost codes, split labor and material.
- He can edit cost codes and categories.
- When he picks a code: suggested codes first, his most-used codes at the top, and type to search what he already has.
- Sub prices follow the industry standard, but he can choose. In his practice they are filed mostly as labor; sometimes a sub's bid covers material and labor together.

### The cost code list (one list, shared with the operations app)
- One small file holds his codes: code, name, category, and whether it is still in use. It starts from his cost workbook's codes (1100 Fees and services, 6080 Framing general, 7410 Cornice, soffit and fascia…). Categories start as his divisions.
- He can add a code, rename it, move it to another category, or retire it. A retired code is hidden from the picker but never deleted, so old estimates still read correctly.
- Every estimate carries a copy of the codes it uses, so a signed estimate still makes sense after the list changes.
- "Most used" is counted from saved estimates when the picker opens. It is not stored anywhere, so it cannot go stale.

### The picker (screen behaviour, Proposed)
1. **Suggested:** the code this line had on his past jobs.
2. **Most used:** his top codes, most used first.
3. **Type to search:** by number or name, filling in from his list as he types. If nothing matches, one tap adds a new code.

### Cost types
- Three types: **Labor · Material · Subcontract**.
- Industry practice (Checked, Nov 16, 2026: Viewpoint, Sage and CrewCost job-costing guides) splits job cost into labor, material, equipment, subcontract and other, with a subcontractor's work filed under Subcontract. Equipment and Other are left out until he needs them (Decided by Claude; easy to add).
- **His own cost workbook keeps the same three types** under every code: Labor, Material and Sub (Checked, Nov 16; corrects an earlier note here that it had only two).
- **He files by who does the work, not by sheet column** (Checked on Job A): framing labor from his Labor column is Sub, a sink priced in his Labor column is Material, a whole concrete slab is Sub. So every price column on a line has its own filing choice (filed_as). The starting point is Material, Labor, and Subcontract for the combined column; his choice is kept on that line for the next job.
- One line can split across codes (cost_split). His paint line feeds interior and exterior paint. See doc 11.

### Budget by cost code
The check works out the budget for every code and type from the lines. His full list (93 codes) is doc 11. On Job A every priced row is matched to a code except 200 of door and window tape he did not budget. With his filing recorded for Job A, the budget by code and by type equals his cost workbook's to the dollar on 38 of his 39 budgeted codes (6080 Framing general: Material 32,719, Sub 12,000; 15100 Plumbing: Material 3,500, Sub 19,000…). The one that differs is kitchen cabinets, where his workbook adds a 700 install his sheet did not count.

## 9. Proof on Job A (Checked, Nov 16, 2026)
His Job A estimate sheet was imported into this format by a script and checked.
- 471 lines kept in his order: 432 items, 33 headings, 6 percent lines (tax ×3, contingency ×2, OH&P). 168 lines in scope. Three rows with a price but no wording are kept as blank-named lines.
- Cost 231,247.05 and total with OH&P 289,058.81: the same as his sheet, to the cent. Every division matches. **Re-checked on version 0.4, Nov 16:** same lines, same totals, and the imported file passes the 0.4 check.
- **Not imported, on purpose:** his other worksheets (contract alternates, alternate backup, allowance adjustments, pay applications, concrete side maths), the price-per-SF row, the blank basement-finish rows, and his side maths in the far-right columns. Alternates and allowances are still to come.
- Names are redacted from a list kept with the job's data on the user's computer; nothing is written while a listed name survives. One shared redaction step (kit/redaction.py) now serves the import, his line list and the draft writer.
- Tests pass: edits recompute correctly (a new 10,000 line moves the total by 12,500), re-filing a sub price moves the budget and not the total, an uneven three-way split still adds up, and bad files are caught without a crash. The tests now run on a made-up estimate, so they need no real data; the Job A file adds the comparison with his cost workbook.
- **Not re-run on 0.4:** the comparison of the budget by cost code with his cost workbook (the Job A code files were not on disk in that chat). The code that works it out did not change.
- The scripts are in the project under "kit/".

## 10. Still open
1. The independent review of version 0.4 and the draft writer is owed (`standards.md`, section 4). **Run Nov 16: 9 findings (doc 07 part 2, section 4); the open ones are answered by section 11.**
2. Whether "who does the work" is his filing rule (doc 06, question 26).
3. Decided (Said, Nov 16): signing an estimate while a priced line has no cost code prompts a warning; it does not block. Built with the screens.
4. Where the editing screen lives (doc 01).
5. Tell the operations app project about version 0.4. **Folded into one notice for all of 0.5** (Nov 18).
6. **Proposed:** a place in the cover for overlapping-line questions (one question, the lines it covers). Today the question is written into each line's reason, which works but repeats it.
7. **Open for the 0.5 build (Claude's craft unless marked; none decided yet):**
   - What becomes of the 0.4 tax percent lines (Job A has three) once sales tax is a mark on the line item. Whatever is chosen, Job A's division totals and budget by cost code must still match his sheet and cost workbook.
   - Whether the answer to "Does this price include sales tax?" is kept in the file with the vendor or sub pricing record (item 7), or only acted on when asked.
   - **For the user:** whether a blank sales tax rate blocks finalizing when no line item is taxed. As said on Nov 17, any blank tax rate blocks.
8. **Facts only the builder knows that could move items 9 to 12** (owed to doc 06): whether he means to mark up sales tax and contingency; whether he taxes materials only; why his sheet has three tax rows; pass-through costs he does not mark up; which groups carry contingency as a habit.

## 11. Approved for version 0.5 (not built): twelve changes
Built in one step, with one notice to the operations app. Each item is Said unless marked. How each is held in the file is Claude's craft and is written here when 0.5 is built.

| # | Change | Approved |
|---|---|---|
| 1 | **Saving.** On an estimate that has been created, changes save into the current version. **A change saves when he leaves the box, not on each keystroke (Nov 18, lock 7).** Each change is still logged in that version's change list (section 7), so the system learns. A new version is made only by Duplicate or Finalize. Duplicate offers "with data" (quantities and prices kept) or "without" (line items only; Inferred reading). Applying vendor or sub pricing does not make a new version; undo reverses that one apply from the change list (undo method: Decided by Claude). A final or signed version is never changed | Nov 17 (doc 07 part 4, section 2; decision 0001); Nov 18 (doc 07 part 5, lock 7) |
| 2 | **Finalizing with unpriced line items** is allowed after a warning. Those line items are listed on the estimate as not included, and add nothing to the total. This replaces, for unpriced line items, the 0.4 rule that a final estimate may hold no blanks. **A blank tax, contingency or markup rate still blocks finalizing; a typed 0% or $0, whichever markup type he chose, satisfies it. Only a blank stops him** (Said, Nov 17, 10:44 am; this settles the line that was Proposed here) | Nov 17 (doc 07 part 4; part 5, decision 5) |
| 3 | The Method's rules move into the shared check, so a file that breaks them is refused whoever wrote it (a heading carrying money, an assumed quantity marked High, a mark above its own quantity mark, a sub bid with a typed price, a dropped line, no cover) | Nov 16 (doc 07 part 2, section 2) |
| 4 | The five rows read as headings on Job A become lines, through a short list in the sheet's settings block | Nov 16 (same) |
| 5 | Every line item in his list has a lasting id that holds across estimates and templates; a one-off line item gets its own | Nov 16 (doc 07 part 3, self-review decision 4) |
| 6 | The estimate records the template it was made from. A dropped line is measured against that template, not against his full list. A line item in the template starts In with the reason "in your template" and a blank quantity | Nov 16 (self-review decisions 3 and 4) |
| 7 | A new price source, "vendor or sub pricing", with who confirmed it and the earlier figure kept beside it. It names its vendor or sub: either a contact from the read-only contacts copy, or a name typed for this job and marked as not in his contact list (decision 4a). Names are real data: they stay on the user's computer and are redacted on test files | Nov 16 (self-review decision 4); Nov 17 (decision 4a) |
| 8 | Each line item carries how it is priced (by quantity, per area with its job measure, lump sum, or a typed amount) and a note. All four total the same way | Nov 16, 9 pm (doc 07 part 3, section 2) |
| 9 | **Markup as a percent or a dollar amount**, his choice, on the estimate total. It sits on all cost, tax and contingency included, as his sheet does. A dollar markup does not grow when cost is added. Markup per line item or per cost type is parked; known limit: a pass-through such as a permit fee cannot be left out of a percent markup | Nov 18 (doc 07 part 5, lock 1; decision 0002) |
| 10 | **A sales tax mark on a line item.** Tax sits on the line item's material part only. It is worked out per line item and counted in that line item's own division and cost code, as his sheet counts it, so division totals and the budget by cost code still hold. Line items he taxed in his template start on; new ones start off | Nov 18 (doc 07 part 5, lock 2; decision 0003) |
| 11 | **The sales tax rate is stored on the estimate.** Settings holds his default; the estimate holds the rate its totals used (a default and a stored copy, decision 0003). It is blank until he gives it, with his last known rate beside it | Nov 18 (lock 2; decision 0003) |
| 12 | **Contingency's base is given by group** (for example "applies to Framing materials"), as his template has it. No contingency mark on line items | Nov 18 (doc 07 part 5, lock 3) |

**Not in the estimate file, by decision:** "requested, waiting" marks and the reminder list of contacts to add to his real list. Both live in the job's own records (self-review decision 7; decision 4a). His standing choice of which line items are taxed is kept in the template (lock 2); the estimate holds the mark for that estimate.

**Screen-only locks of Nov 18 that do not change the file:** one price box per line item with the material and labor split in Details (lock 4; the three price columns in section 3 stay); the top bar (lock 5); how cents are drawn (lock 6; money is still stored to the cent); the keyboard rules (lock 7, apart from when a change saves, item 1).

## Change log
| Date | What changed |
|---|---|
| Nov 16, 2026 | Version 0.3 → 0.4, approved by the user (review decisions 1, 2 and 5). Section 1: one way in (fill_totals and save). Section 2: cover fields written out. Section 3: total rows are not lines; qty_source, price_source and confidence stated as records; last_known and flags now in files; blanks allowed while the estimate is open; markup always in scope. Section 4: the check cannot be crashed, plus the newly enforced rules. Section 9: re-check on 0.4 and what was not re-run. Section 10: review owed, operations app to be told, one Proposed item. Brands are kept in wording (review decision 6) |
| Nov 17, 2026 (10:35 am) | No change to version 0.4 as built. Section 11 added: the eight changes approved for version 0.5, gathered from doc 07 parts 2 to 4, including the new saving rule, finalizing with unpriced line items, and the vendor or sub named on pricing (decision 4a). Status line, sections 1, 3 and 5 now point to section 11 where 0.5 will differ. Section 10: items 1 and 5 updated. One Proposed line added in section 11, item 2 (a blank rate still blocks finalizing), not yet put to the user |
| Nov 18, 2026 | Moved into the repository as `docs/format.md` from project document 10, and brought into line with working log part 5. No change to version 0.4 as built. **Section 11 is now twelve changes:** items 9 to 12 added (markup as a percent or a dollar amount; the sales tax mark on a line item, on its material part, counted in its own division and cost code; the tax rate stored on the estimate; contingency by group). Item 1: a change saves when he leaves the box (lock 7). Item 2: the Proposed line is settled as Said (a blank rate blocks finalizing; a typed 0 satisfies it). Two notes added under section 11 (the template keeps his tax choices; which Nov 18 locks are screen-only). Status line, sections 2, 3 and 4 point to the new items. Section 10: item 5 updated; items 7 and 8 added (open points for the 0.5 build; facts owed from the builder). Title lost its number; a note on reading the references added; "doc 09" now reads `standards.md`. **Decided by Claude:** on where the Tax chip shows, working log part 5 (material-filed line items only) and decision 0003 (any line item with a material price) differ; this is a screen matter, so item 10 states only what both agree on. **Settled the same day (Said):** decision 0003 is the standing rule; the chip shows on any line item with a material price |
