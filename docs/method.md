# Method: how a draft estimate gets made, marked and improved

**Moved here Nov 18, 2026** from project document "03 Estimator - Method". See the change log at the foot for what changed on the way and after.
**Reading the references:** `format.md` and `standards.md` are the two files beside this one. "doc NN" means a project document that is not in this repository yet: 01 Start here · 02 Research · 04 Builder estimate format and price list seed · 05 Job A actual costs · 06 Questions for the builder (to become `docs/builder/questions.md`) · 07 Working log (to become `docs/history/`).

**Status:** Proposed, Nov 16, 2026. Brought into line with standing decisions Nov 18 (change log at the foot). Built from the research in doc 02 and the builder's files. Change it when a test shows something better; note the change in doc 07. Changed Nov 16 after the first blind draft (approved by the user): overlapping lines in step 4, "plan minimum" in steps 5 and 7, and where test answers are kept. Changed Nov 16 (approved by the user): step 8 now describes the on-screen estimate, with Excel and CSV as exports.

## The idea in one paragraph
An estimate is three questions: **what is being built** (scope), **how much of it** (quantity) and **what it costs him** (price). Each goes wrong in a different way, so each is handled, marked and corrected separately. The draft is always his lines, his order, his prices. The tool's job is to fill what it can prove, mark what it cannot, and point him at the money that is least certain.

## Step 1 · Sort the job
Decide the job type first. It changes everything after.

| | New build | ADU / garage apartment | Renovation / addition | Mixed |
|---|---|---|---|---|
| Needs | Plans | Plans | Plans **and** a scope list | Split it into parts and treat each by its type |
| Scope starts from | His full checklist | His full checklist, small-building version | The scope list only | |
| Extra questions | Site, finish level | Utility tie-ins, sewer, power, access | Age of house, what stays, what is hidden | |
| Suggested cushion | 5–10% | 5–10%, more for tie-ins | 15–25% | Per part |

Job A is mixed: a new garage apartment plus a small renovation at the main house.

## Step 2 · Check what came in
Before any estimating:
- List every page and what it is. Report any page that could not be read.
- Note what is missing: no structural sheets, no door and window schedule, no finish selections, no site plan, no scope list.
- Grade how defined the job is: **Sketch**, **Permit plans**, or **Plans with selections**. This sets the range shown on the draft (doc 02, section 2).
- For a renovation with no scope list: stop and ask for one. Do not draft.

### The renovation scope list (what to ask for)
Room by room or area by area:
- What is torn out. What stays. What is new.
- Finish level, or the allowance to carry.
- Who supplies what (builder, client, sub).
- Known problems: water, rot, old wiring, old plumbing, foundation, hazardous material.
- Age of the house and when it was last worked on.
- Access and living conditions: occupied or empty, parking, dumpster spot.
- Photos, if there are any.

## Step 3 · Collect the facts from the plans
Make a **job facts sheet** before touching the estimate. One row per fact, each with its source.

Facts to collect, in this order of trust:
1. **Written on the plans:** area tables, drawing notes, door and window schedules, supplier lists (lumber, trusses), wall heights, roof pitch, code data.
2. **Read from dimension strings:** building length and width, room sizes, opening sizes.
3. **Counted from the drawings:** doors, windows, fixtures, outlets.
4. **Calculated from the above:** wall area, roof area, footing length, drywall area.
5. **Assumed:** anything else. Marked as an assumption, with the reason.

Rules:
- Read each sheet from a clear image, zoomed in on the part that matters. One full-page glance is not a reading.
- Never scale off a picture when a written dimension exists.
- Cross-check: floor area from dimensions should match the area table; window count on the plan should match the elevations; the lumber list should make sense against the wall lengths. A mismatch is reported, not averaged away.
- Read important numbers twice, in two separate passes. If the passes differ, mark the fact Low and show both.
- Do not invent a number to fill a row. An empty row with "not on the plans" is a correct answer.
- The job facts sheet holds only what the plans say. None of his estimate figures go in it.

The core facts for most jobs: floor area by level · footprint and perimeter · wall heights · exterior wall area · roof area and pitch · foundation type and length · slab area · counts of doors, windows, garage doors · kitchens and baths · fixture count · stairs · site items (driveway, fence, walls, trees, utilities).

## Step 4 · Build the scope (which lines apply)
- Start from his checklist (doc 04). For each line decide: **In**, **Out**, or **Ask**.
- Give a reason for every In and every Ask ("two baths on plan", "site plan shows new fence").
- A line he usually carries but the plans do not show goes to **Ask**, not Out.
- **Estimates made from a template (Said, locked Nov 16).** A line item in the chosen template starts In, with the reason "in your template" and a blank quantity until the plans give one. Lines outside the template are shown as a count with a link, not as a wall of Ask. A dropped line is measured against the template the estimate records, not against his full checklist (`format.md`, section 11, item 6). Anything the plans show that is outside the template is listed as "Not in your template" for his answer; never added silently.
- **Overlapping lines (approved Nov 16).** His sheet often has two or three lines for the same work (a lump sum and a per-unit line; a main bid and a part bid; a heading he prices directly and the lines under it). Do not mark several of them In. Show them as one group with one question: "which line do you use for this?" If his usual line for that work is recorded, put the draft on that line and name the others in the note. Until he confirms it, a recorded usual line from one job is a note, and the group stays Ask.
- Things the plans show that are not on his checklist go in a separate "not on your list" section. Never slip them into his divisions unannounced.
- This step matters more than any other. A missed line costs more than a mismeasured one.

## Step 5 · Fill quantities
- Each quantity comes from the job facts sheet through a stated rule ("drywall = wall area both sides + ceiling area, plus his waste").
- The rules live in the price list beside each line, so they can be corrected once and reused.
- **Plan minimum (approved Nov 16).** A calculated lumber, sheathing, trim, concrete or rebar quantity is the bare count from the plans. He orders more than that. Until his ordering rule for the line is recorded, the quantity is labelled "plan minimum" and no waste factor is guessed for him.
- Lump-sum lines get 1 only when the line clearly applies. Otherwise leave blank and mark Ask.
- Sub bid lines: leave the price blank, show the last known bid and its date beside it, mark Low.

## Step 6 · Price from his price list
The price list is one clean table made from his sheets. For each line:

| Field | Meaning |
|---|---|
| Line name | His wording |
| Division | His number |
| Unit | His unit |
| Material / Labor / M&L price | His last price |
| Price date and job | When and where it was last used |
| Price type | Unit price, lump sum, sub bid, or allowance |
| Quantity rule | How the quantity is worked out from the job facts |
| Times used / times corrected | Track record |

Rules:
- Only his prices. If he has no price for a line, leave it blank and mark it Low. A generic number may sit in a note as "outside reference", never in the price cell.
- Show the age of every price. Old prices lower the confidence mark.
- No automatic inflation. If prices need bringing forward, propose a method and get it approved first.
- Markup, allowances and contingency are separate visible lines, following his practice once he tells us what it is (doc 06).

## Step 7 · Mark confidence
Each line gets two marks, then the lower of the two becomes the line's mark.

**Quantity mark**
- High: written on the plans, or counted and cross-checked.
- Medium: calculated from written dimensions where no ordering rule of his is involved (areas, lengths), or counted once.
- Low: measured off a drawing with no written dimension, assumed, or the two readings disagreed. **Also Low (approved Nov 16):** any "plan minimum" quantity, until his ordering rule for that line is recorded.

**Price mark**
- High: his price, used on a recent job, not corrected last time.
- Medium: his price but old, or from one job only, or scaled from a different size job.
- Low: sub bid not in hand, allowance, no price history, or a line he has corrected before.

**Automatic Low**, whatever else is true: anything hidden (existing conditions), anything the client has not chosen, anything on the Ask list, site work on a job with no site plan.

**What he sees**
**Changed (Said, Nov 16, 9 pm; `standards.md`, section 3):** all three marks are still worked out and stored on every line, but the screen shows two flags, High and Low, off by default and turned on in settings. Medium is stored and not shown. "Check these first" appears on screen as "Double-check these first"; it starts on and he can switch it off. The list below is what the marks carry; the screen shows it within those limits.
- A colored cell and a word on every line: green High, yellow Medium, red Low. Always the word as well as the color.
- A one-line reason on every Medium and Low.
- A summary at the top by division: total dollars, and how many of those dollars are High, Medium and Low.
- **"Check these first":** the ten or so lines ranked by dollars × doubt, so a small shaky line does not outrank a large one.
- A low and high figure for the total, wider when more of the money is Low and when the job is less defined.

Do not show percentages like "87% confident". They look exact and are not. Three levels and a reason are honest.

## Step 8 · The draft he receives
Changed Nov 16 (Said: the output is a modern on-screen estimate; Excel and CSV are exports only).
- An on-screen estimate, not an Excel file. It keeps his lines, his order, his units and his divisions. Sub-lines collapse under their division.
- Always visible at the top: the draft total, the estimated range and what the total leaves out. "Double-check these first" starts on.
- On every line, when he has the flags turned on: the confidence word and colour, High or Low. One tap on a number shows the reason, the source of the quantity and the price date.
- A cover section: job type, how defined the job is, what was missing, assumptions and exclusions.
- A job facts view, so he can see every measurement and where it came from.
- Nothing is locked while he is working on it. He can overwrite any number on screen. **Changed (Said, Nov 17; decision 0001):** his changes save into the current version, when he leaves the box (Said, Nov 18), and each change is logged in that version's change list (`format.md`, section 7), which is what step 9 learns from. A new version is made only by Duplicate or Finalize; a final or signed version is never changed.
- Excel in his layout and CSV are exports, made on request from the same data and not stored.
- The data behind the screen is the shared estimate format (`format.md`). The screen follows the design standard in `standards.md`, section 3.

## Step 9 · Learn from what he changes
When he sends back his finished estimate:
1. Compare it to the draft line by line.
2. Log every difference in doc 07, sorted into one kind:
   - **Quantity:** we measured or calculated wrong.
   - **Price:** his price has moved, or he priced by gut.
   - **Missing line:** he added something we left out.
   - **Extra line:** he removed something we put in.
   - **Scope:** the job itself changed.
3. Ask for a reason only if he is willing; two words is enough.
4. **One correction is a note. The same correction twice is a pattern.** Only a pattern, or a rule he states outright, changes the price list or a quantity rule, and only after approval.
5. Keep job-specific changes ("steep lot", "client's cousin does the tile") out of the standing rules.
6. Lines he corrects often drop to Low until they stop being corrected.

When a job finishes and real costs are in, repeat the comparison against actual cost by cost code. That is the stronger signal: his estimate can be wrong too.

## How we test before he relies on it
**Blind test on a finished job:**
1. Give the tool only what he had on estimate day: plans and, for a renovation, the scope.
2. It produces a draft without seeing his estimate.
3. Score it against his real estimate:
   - **Scope:** of the lines he priced, how many did we include? Of the lines we included, how many did he not use?
   - **Quantities:** on measurable lines, how far off, line by line?
   - **Dollars:** difference by division and in total.
   - **Marks:** were the lines we got wrong the ones we marked Low? If errors hide under High marks, the marking is broken.
4. Then compare both to actual cost.
5. Write the result in doc 07.

**Keeping a blind test blind (approved Nov 16):**
- His lines are listed for the run by script, with quantities and prices hidden. A filled price gives away which lines he used.
- The draft file is frozen before his estimate is opened. Scoring is done by script.
- His answers for the job under test (his quantities, his line choices, his costs) live only in that job's results document and in docs 04 and 05. A blind run does not open them.
- Scored figures never go into "01 Start here", "07 Working log" or a job facts sheet. The log carries the score and a pointer to the results document.
- A job whose answers have been seen cannot be used for a blind test again. Say so in the results.

**Honest limits of the first test:** Job A's estimate is also where the price list comes from, so on Job A the prices will match by design. Job A tests reading, scope and quantities only. Prices can only be tested on a second job, with the price list built from different jobs than the one under test.

**Pass marks (Proposed):** at least 80% of his priced lines included · measured quantities within 10% · no more than one in ten wrong lines carrying a High mark.

## What the tool must never do
- Show a guessed quantity as measured.
- Put a price in that is not his.
- Drop a line silently, or add one silently.
- Change his lines, order, units or divisions.
- Draft a renovation without a scope list.
- Decide engineering questions (beam sizes, footing design).
- Call a draft a bid. It is a draft until he finishes it.

## Change log
| Date | What changed |
|---|---|
| Nov 18, 2026 | Moved into the repository as `docs/method.md` from project document 03. Title lost its number; a note on reading the references added at the top; "doc 09" and "doc 10" now read `standards.md` and `format.md`. No rule changed. **Known to be behind, not changed here:** step 8 still says every save is a new version (decision 0001 replaced that); step 7's "what he sees" still shows three marks (the screens show two flags, `standards.md` section 3); step 4 is owed an update (working log part 5, section 3) |
| Nov 18, 2026 (later) | Brought into line with standing decisions, approved by the user ("lock all your recommendations"). Step 4: the template rule added (self-review decision 3, locked Nov 16). Step 7: a note that the screen shows two flags, off by default, with Medium stored and not shown; the three marks themselves are unchanged. Step 8: what is always visible now matches `standards.md`; the confidence word shows when flags are on; saving follows decision 0001 and the Nov 18 keyboard lock. The three "known to be behind" points in the row above are now closed |
