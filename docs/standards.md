# Build, design and review standards

**Moved here Nov 18, 2026** from project document "09 Estimator - Build, design and review standards". See the change log at the foot for what changed on the way and after.
**Reading the references:** `method.md` and `format.md` are the two files beside this one. "doc NN" means a project document that is not in this repository yet: 01 Start here · 04 Builder estimate format and price list seed · 05 Job A actual costs · 07 Working log · 11 Builder cost code list. They are kept as history. Where a line here once told you to write to one of them, it now names the place in this repository. In this repository, decisions are recorded in `decisions/` and mistakes in `docs/history/mistakes.md` (see `AGENTS.md`).

**Purpose:** how the estimator software is built, how it should look and feel, and how every big piece of work is checked before the user sees it. Written to avoid what went wrong on an earlier build (Said): lost context, broken databases, duplicate code and files, inconsistent design, fixes that broke other parts, and documents that contradicted each other.
**Status:** in force since Nov 16, 2026. A change needs the owner's OK and a decision file.

## 1. Build rules
1. **One source of truth per thing.** One shared estimate format, one price list, one cost code list, one copy of each plan set, one copy of each script. Before creating a file, check whether one already does the job, and change that file instead.
2. **Build the real thing, not patches.** Fix the cause, not the symptom. If a fix touches something else, check that other thing too.
3. **Small, reversible steps.** One change at a time. Every change can be undone (the code is kept in git), and every notable change is described in its commit message.
4. **Fixed steps in code, judgement in Claude.** Anything that must come out the same every time is a tested script: reading page images, quantity rules, pricing lookups, totals, exports and checks. Reading plans and deciding scope stay with Claude, marked by confidence.
5. **Clean, commented code.** Plain names. A short note at the top of each file says what it does. No dead code left behind.
6. **Built to move.** Everything runs on the user's computer with no server, laid out so it can move to a server or into the operations app without a rewrite.
7. **The shared estimate format is a contract.** Changing it needs the user's OK. It carries a version number, and the operations app must be told of any change.
8. **Settings are suggestions.** Defaults, limits and thresholds go to the user as proposals. Reviewers do not set them.
9. **Real data stays private.** The privacy rules in `AGENTS.md` apply to code, test files and screenshots too. Redaction runs from a name list, which is real data: it is never saved in this repository and is rebuilt from the builder's own estimate file each time it is needed (decision 0059), with an automatic check that no listed name survives; never from hand-picked rows (Said, approved Nov 16).
10. **Figures from his files come from a script.** Any figure taken from the builder's files is produced by script and checked against his own total cells before it goes in a document. Documents that mirror his files (docs 04, 05, 11) are written by script, not typed (Said, approved Nov 16).

## 2. Storage rules
- One copy of each plan PDF. Page images are temporary and deleted after reading.
- Each estimate version is one small data file (tens of KB). **Changed (Said, Nov 17):** changes save into the current version when he leaves the box, not on each keystroke (Said, Nov 18), and each change is logged in that version's change list. A new version is made only by Duplicate or Finalize. A finalized or signed version is never changed.
- Job folders are named by job (address only on the user's own computer, never in project documents).
- No duplicate exports kept: Excel and CSV are made when asked, not stored.
- Check the folder size after every test and report it if it grows unexpectedly.

## 3. Design standard (premium, simple)
**Order of work (Said, from the operations app project):** first layout, the information shown, navigation, statuses and actions. Only then fonts and colours.

**Laptop first (Said, Nov 16, 10:20 pm).** The screens are a web app designed for a laptop first. The phone layout is a second pass.

**Do not force him (Said, Nov 17).** The tool does not force him to work in a way, or use the system in a way, that he does not want, within our limits.

**Simple on the surface (Said, Nov 18).** Every proposal is checked against this: not overly complicated, yet still very accurate; simple on the surface, intuitive to use, and not busy for a man of about 50.

**What "premium" means here (Proposed, except where marked Said):**
- Calm and uncluttered. One clear thing per screen; detail opens on demand.
- The draft total, the estimated range and what the total leaves out are always visible. "Double-check these first" starts on (Said, Nov 16, 10:45 pm) and he can switch it off.
- Confidence shown as a word and a colour, never colour alone. **Changed (Said, Nov 16, 9 pm):** two flags on screen, High and Low; off by default; turned on in settings. Medium is stored and not shown.
- Every number can be traced: tap it to see where it came from (plans, his price, assumption).
- Editing a number is one tap. Changes save automatically; there is no save button and no "unsaved" marker (Said, Nov 16, 11:25 pm). The change and its reason (optional, two words) are kept.
- The screen draws the eye to what needs attention and to what he is working on, and guides him through building the estimate. It must not feel like a spreadsheet (Said, Nov 16, 11 pm).
- Buttons look like buttons, never like containers. Text does not wrap or stack (Said, Nov 16, 11 pm).
- **For the build (Said, Nov 16, 11:34 pm):** a more premium button style and colour theme than the canvas drawing; icons wherever they help him read less.
- Sub-lines collapse under their division; the client view hides cost and markup.
- Consistent everywhere: one set of spacing, type sizes, colours and components, written down once and reused. If the operations app has a design system, use it so the two products feel like one.
- Works on a laptop and a phone, and in print or PDF for the client copy.
- Plain builder language. No software jargon.

**Not premium:** dense spreadsheet grids, tabs on tabs, decorative charts, fake-precise percentages, inconsistent buttons.

**Screen wording rule (Said, Nov 16, 9 pm).** Every word on a screen is the term a builder or mainstream residential estimating software uses, or close to it.
- Each label is checked against dated sources and listed in a wording table in the design document: label, why, source.
- No project working words on a screen (for example "plan minimum", "Medium") unless the wording table gives them a plain form.
- A sketch holds only real screen text. Notes to the user go in the chat, never inside the drawing.
- The user's fixed wording wins over an industry term: "line item", never "row"; "quote" is not used for vendor or sub pricing; "estimated range", not "likely range".

**Spacing and buttons (Said, Nov 16, 9 pm).** One spacing scale and one set of button sizes, written once in the design document and used on every screen. A group of actions follows one layout rule, so buttons never wrap unevenly.

**Sketches (Said, Nov 16, 9 pm).** Screens are drawn with a design reviewer's help. A locked sketch is kept as its own source, not only as a description: the drawing's code, with every control given an id, and a control list (id, label, what it does, its states). The two must match exactly. The screens are built by re-creating the locked source, so what was approved is what is built. A screen is drawn at its real size, on a design canvas, not inside the chat's narrow panel (Said, Nov 16, 11 pm: the narrow sketches read as scrunched). Before any screen is locked, one rough clickable version is built on made-up data and the five tasks are run on it; the lock and the detailed write-up come after (decision 0011).

## 4. Review after every big build or change
A big build is a new screen, a new script, a change to the shared format, or a full estimate run.

**Step 1 · Self-check (Claude):**
- Run it. Test it on Job A data.
- Look at every screen as a real screenshot at three widths: laptop, small window and phone. Check print too. The report says which widths were checked (Said, Nov 16, 11 pm).
- Check totals in code against the Excel export.
- Confirm no duplicate files and no leftover temporary files, and check the folder size.

**Step 2 · Fresh review:** separate reviewers with no chat history check the work against this document. The roles, and what each one is asked, are in `docs/reviewers.md`; that file is the one home for them.

**Screens are reviewed in two lanes, by two separate reviewers (Said, Nov 16, 11 pm):**
1. **Usability and logic:** function, logic and button mapping. Does every control do what its label says, and can he do each task without help?
2. **Visual design:** does the screen guide him through building the estimate, draw the eye to what matters, and not feel like a spreadsheet?

Both reviewers work from the same real screenshots at the three widths. A review does not count unless the reviewer looked at a rendered picture.

**Step 3 · Report:** findings go to the user in the update, ranked by impact, each fixed or raised as a decision. Nothing is called done while a reviewer's finding is open.

## 5. Learning from Claude's mistakes
When a mistake is found (by the user, a reviewer, or a test):
1. Fix it.
2. Log it in `docs/history/mistakes.md`: what happened, why, the fix, and whether a rule should change.
3. If a rule would have prevented it, propose the change to the user in one line. Once approved, update the rule here, in `method.md` or in `AGENTS.md`, and record it as a decision.
4. If the same kind of mistake happens twice, a rule change is required.

## 6. Keeping context (hand-offs)
Chats lose detail as they grow, but every new chat costs usage to start (rereading the documents). So hand off only at a good stopping point (Said, Nov 16):
- The chat is long enough that detail is at risk: roughly two or three big tasks, or many long tool steps.
- Claude notices it is unsure of something said earlier in the chat.
- Never after a small run just because it finished. A finished task is the best moment to hand off, but only when one of the two points above also holds.

To hand off: update `STATUS.md`, then give the starter line (decision 0056). The starter line is given in a code block the user can copy. The documents are the memory; the chat is not.

## 7. Spending the user's usage
- Warn before anything that will use a lot (a full plan read, a large build, a review round). A two-lane screen review is two reviewers, each roughly 85,000 to 125,000 tokens by past rounds.
- Read only the pages and zoom areas a step needs.
- Do not reread documents already read in the same chat unless they changed.
- Measure and log the usage of each full estimate run, so the running cost is known.

## Change log
| Date | What changed |
|---|---|
| Nov 16, 2026 (9 pm) | Section 3: three rules added at the user's request (screen wording checked against industry terms, with a wording table and no notes inside a sketch; one spacing scale and one button layout rule; a locked sketch kept as its own source with control ids and a matching control list). The confidence line now records two flags, off by default. The "always visible" line is marked under review. This change log added |
| Nov 17, 2026 (10:35 am) | Brought into line with what the user said on Nov 16 and 17 (doc 07 parts 3 and 4). Section 2: the version rule changed (changes save into the current version; a new version only by Duplicate or Finalize). Section 3: laptop first; the "always visible" line settled ("Double-check these first" starts on); automatic saving; eye drawn to what needs attention; buttons that look like buttons; the build note on premium buttons, colour theme and icons; "estimated range" added to the fixed wording; screens drawn at real size on a canvas; "works on a phone and a laptop" reordered. Section 4: self-check uses real screenshots at three widths; the two-lane screen review added. Section 7: the cost of a two-lane review. Not added: rules that are still only Proposed in doc 07 section 8 (sample figures from one made-up data set; walking the five tasks before showing a layout; carrying earlier accepted fixes into a redraw) |
| Nov 18, 2026 | Moved into the repository as `docs/standards.md` from project document 09. Title lost its number; a note on reading the references added at the top; "doc 03" now reads `method.md`. No rule changed. **Known to be behind, not changed here** (working log part 5): section 3 is owed the "do not force him to work a way he does not want" principle (Said, Nov 17) and the "simple on the surface, not busy" standard (Said, Nov 18); section 2's "as he types" is now "when he leaves the box" (lock 7, Nov 18) |
| Nov 18, 2026 (later) | Brought into line with working log part 5, approved by the user ("lock all your recommendations"). Section 2: a change saves when he leaves the box. Section 3: two standing lines added in the user's words, "do not force him" (Nov 17) and "simple on the surface" (Nov 18). The points listed as behind in the row above are now closed |
| Nov 19, 2026 | Phase 0, records clean-up. No rule changed. Status no longer rests on the old project instructions. Instructions that pointed to project documents 01 and 07 now name their place in this repository. Build rule 9 says where the name list lives, as decision 0059 has it. Section 3: the rough clickable step added (decision 0011). Section 4: the four review views, which were only Proposed, replaced by a pointer to `docs/reviewers.md` so the roles have one home (Decided by Claude) |
