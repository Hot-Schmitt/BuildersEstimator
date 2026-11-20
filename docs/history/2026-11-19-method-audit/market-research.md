# Market research: what small residential builders say about estimating software

Purpose: evidence for the design of a plan-reading estimating helper that drafts in the builder's own lines and own prices. Web research only, done 2026-11-19.

How to read this
- Checked = I read it on the page named (through a page-reading tool that returns a close paraphrase, so wording is paraphrase, not quotation). Inferred = my reading across sources.
- Review sites show only the first 10-30 reviews per page; I read one to three pages per product. Counts such as "7 of 20" refer to the visible sample only, never the whole review base.
- Many review-site reviews are vendor-invited with a small incentive, which pushes scores up. I weighted low-star and detailed reviews more heavily.
- Dates are the review or article date shown on the page. "Date not shown" where absent.

---

## 1. The ten findings that should most change this app's design (ranked)

### 1. Setup is the number one complaint about every conventional tool. Importing his own sheet with near-zero setup is the wedge.
Evidence (Checked)
- JobTread, small shops: 7 of 20 visible reviews from firms of 1-10 people mention learning curve, training or switching effort; one owner says templates cut an estimate to about 15 minutes but data clean-up and learning cost types and margins fell on him (May 2026). https://www.softwareadvice.com/construction/jobtread-profile/reviews/
- JobTread: setup "time-consuming" or needing a lot of training (Oct 15 2025; Oct 16 2025; Nov 18 2026). https://capterra.com/p/218503/JobTread/reviews/
- PlanSwift: fast once assemblies exist, but big setup, not plug-and-play (Mar 2026). https://capterra.com/p/70808/PlanSwift/reviews/ ; an Atlanta contractor spent about two years customising PlanSwift and then could not hand it off (thread about 2020-2024, relative dates only). https://www.biggerpockets.com/forums/24/topics/799869-what-are-contractors-using-for-bidding-software
- Bolster: about two months to load supplier pricing (Mar 10 2026); two 1-star onboarding reviews (Feb 12 2025; Nov 19 2026). https://www.capterra.com/p/199769/CostCertified/reviews/
- Contractor Foreman: cost database takes real effort before use (Oct 7 and Oct 30 2026). https://www.capterra.com/p/166113/Contractor-Foreman/reviews/
- Buildertrend: one-person operator found learning a real challenge (Feb 6 2020); three 45-minute trainings not enough (Sep 9 2022). https://www.capterra.com/p/70092/Buildertrend/reviews/?page=3
- G2 reviewers report average go-live of about one month (JobTread) and three months (Buildertrend), per GetApp's Oct 22 2026 comparison (GetApp earns referral fees). https://www.getapp.com/resources/buildertrend-vs-jobtread-for-remodelers/
What it means for this app
- The first estimate must come out of his existing sheet with no catalogue-building by him. If he has to "set up" anything, the app has reproduced the main reason people quit the incumbents.
- Treat "time from first login to first usable draft" as the headline measure for the wider market. Inferred.

### 2. Users distrust prices they did not set. Database and AI prices are the most common accuracy complaint; labour is the worst. This supports "his prices only".
Evidence (Checked)
- Handoff (AI estimating, residential): most numbers need changing (Mar 11 2025, 3 stars); AI pricing not accurate enough (Mar 24); accurate apart from labour (Feb 18 2025); misses real labour costs and local permit/code rules (Apr 15); retailer prices off or from the wrong chain (Apr 25, Jun 10); one bid wildly high, eight doors at about $7,500 (May 6). https://www.capterra.com/p/10026318/Handoff/reviews/ and https://www.capterra.com/p/10026318/Handoff/reviews/?page=2
- Clear Estimates: labour costs can be very inaccurate (Jun 16 2025); task values inconsistent, some low, some high, and its AI misses items and crashes on large PDFs (Oct 30 2026); database needs frequent updating to match real prices (Apr 28 2026); automatic price updates cannot be used because they overwrite custom tasks (Feb 19 2026). https://www.capterra.com/p/24826/Clear-Estimates/
- Contractor Foreman: item database lacks common items, team falls back on vendor sheets (Feb 11 2026). https://www.capterra.com/p/166113/Contractor-Foreman/reviews/
- One Handoff owner notes he must set his own prices and let it learn them (Apr 4 2025); another wants to choose the supplier (Feb 15 2025). Same Handoff page 2.
What it means for this app
- The "no market prices" stance matches what users say. Keep it.
- Never let any update overwrite a price he typed. The Clear Estimates overwrite complaint is the exact failure to avoid.
- Labour is where automated numbers are least trusted, so labour lines deserve the most conservative confidence marking. Inferred.

### 3. AI plan reading is unproven on custom residential drawings. Failures cluster in derived quantities, poor scans, elevations/sections, and scope that is not drawn.
Evidence (Checked unless marked)
- No independent benchmark on a residential custom or addition set exists that I could find; the one multi-tool test (Feb 19 2026) used a single 200+ sheet multi-discipline set, one run, with the scorecard not shown. https://roboticsandautomationnews.com/2026/02/19/6-ai-construction-estimating-software-tested-on-complex-project-accuracy/ ; the gap is also noted by two trade blogs (Jun 16 2026; Sep 16 2026). https://aihomebuilding.pages.dev/articles/ai-takeoff-estimating-residential-gap.html , https://aihomebuilding.com/stories/ai-takeoff-shootout-residential-estimating-2026
- Kreo users: output so messy that tidying took as long as manual takeoff (Nov 2023); hit-and-miss on dense drawings (Sep 2023); works on vector floor plans, struggles on scans (May 2024); errors sometimes need heavy editing (Nov 2026); wants AI beyond floor plans, e.g. elevations (Aug 2023). https://www.capterra.com/p/231342/Kreo-2D-Takeoff/reviews/
- Togal users: auto takeoff suits simple floor-plan counts, not work needing plans, sections and elevations together (Jan 29 2026); cannot tell rated from non-rated walls (May 7 2026). https://g2.com/products/togal-ai/reviews?page=3
- Vendors' own admissions: Handoff says it is tuned to residential up to about 7,000 sq ft, does not calculate engineering values, and one-off custom work needs the user's pricing (date not shown). https://handoff.ai/blog/seven-things-ai-takeoffs-can-and-cant-read-on-your-construction-plans ; STACK says AI cannot know whether this contractor includes blocking or adds labour for complexity (date not shown). https://www.stackct.com/blog/what-ai-gets-right-about-construction-takeoffs-and-what-it-still-gets-wrong/ ; Togal lists incomplete drawings, scope gaps and constructability (date not shown). https://www.togal.ai/blog/estimators-edge-where-ai-wins ; ConstructConnect lists scans, handwritten marks, irregular geometry, revisions across sheets, incomplete sets (Aug 18 2026). https://www.constructconnect.com/blog/are-ai-takeoffs-accurate-in-2026
- A newsletter (Jul 22 2026) says errors concentrate in quantities that must be derived rather than read off the sheet, and that general language models can describe a sheet yet miscount windows; unverified figures. https://bricks-bytes.beehiiv.com/p/ai-reads-the-blueprint-what-it-reads-next
What it means for this app
- Prefer written information (area tables, schedules, notes) over measuring, and say which was used on every quantity. The project's existing rule on quantity sources is well aimed.
- Derived quantities (framing, roofing, drywall, anything from elevations) should default to a lower confidence than counted or stated ones.
- A luxury custom home is the hardest case in this category, not the easiest. Expect the blind tests to show it. Inferred.

### 4. Missed scope is where estimates lose money, and "it caught things I forget" is one of the few things users praise in AI tools. A scope checklist built from his own sheet may be worth more than measurement.
Evidence (Checked)
- Handoff praise: covers items people often miss (Mar 5); auto-adds fasteners and similar (Mar 17); often adds items he would forget (Mar 23 2025). Same Handoff pages.
- JobTread: estimating caught missed items (Oct 2025). https://www.softwareadvice.com/construction/jobtread-profile/reviews/ ; Clear Estimates: templates stop omissions (Nov 2018). https://www.softwareadvice.com/construction/clear-estimates-profile/
- JLC, D. Gerstel (Feb 13 2019): the costly omissions are things not on the plans (permits, scaffolding, cleanup, supervision, blocking, items between trades); advises a self-built, living checklist. https://www.jlconline.com/business/estimating-job-costing/the-greased-pigs-of-estimating_o
- A Clear Estimates user asks outright for an error-check feature (Mar 2020). Same Software Advice page.
What it means for this app
- "Which of his lines apply, and which usual lines are absent from this job" is a core output, not a side feature. The project's scope-before-quantity rule fits the evidence.
- An "estimate reviewer" pass (Buildxact ships one, see finding 10) is a cheap, high-trust feature: it reads, it does not write numbers.

### 5. Trust comes from traceable numbers, visible and fixable errors, consistency, and the tool never changing things unasked.
Evidence (Checked)
- Handoff: same product priced differently across estimates, units and descriptions change, pricing rules not always followed (Jan 20 2025); adjustments often wrong or unrequested (Apr 23); basic maths errors and forgotten presets (Apr 9); asks questions but generates before the user can answer (Mar 26 2025). Handoff pages above.
- For Construction Pros (Oct 13 2026, author linked to an AI vendor): record missed scope, extra scope, wrong classification and wrong scale separately; a reviewer must be able to trace a quantity to sheet and revision; a visible, recoverable error is safer than one that looks right; test on your own finished jobs. https://www.forconstructionpros.com/construction-technology/automation-and-ai/article/22975238/buildvision-ai-test-ai-takeoff-tools-before-using-them-for-bids
- STACK users ask for version history, a record of who changed what, a lock on bid sets, and handling of replaced sheets (May 2026). https://www.capterra.com/p/147181/STACK-Takeoff/reviews/
- Clear Estimates: screen layout differs from the printed view, which invites errors (Feb 19 2026). https://www.capterra.com/p/24826/Clear-Estimates/
What it means for this app
- Same plans plus same price list must give the same draft every time. Keep pricing and totals in fixed scripts (already the plan) and say so on screen.
- Every quantity one tap from its source sheet. Blank beats guess.
- Ask scope questions before drafting, not after.
- What he sees, what prints and what exports must be identical.
- Score tests by error type (missed line, extra line, quantity, price), not one accuracy number. Proposed.

### 6. Price rises, annual lock-in and data that cannot be exported produce the angriest reviews. Simple, month-to-month, export-everything is a selling point.
Evidence (Checked)
- Buildertrend: pushed into annual term, refused month-to-month (Oct 7 2026); paid six months with no jobs, no pause allowed (May 2026); no export-all on cancelling, vendor confirmed (Dec 4 2025); price up about 80% in three years (May 28 2022); 75% rise without notice (Mar 15 2023); $59 to about $1,300 a month (Nov 1 2022). https://www.capterra.com/p/70092/Buildertrend/reviews/ , https://www.capterra.com/p/70092/Buildertrend/reviews/?page=3 , https://www.capterra.com/p/70092/Buildertrend/reviews/?page=8 , https://www.bbb.org/us/ne/omaha/profile/computer-software/buildertrend-solutions-0714-300027310/customer-reviews
- Houzz Pro: locked 12-month contracts and charges after cancelling (Feb 10, Feb 19, Apr 3, May 16, Jun 17 2025); renewal up over 400% (Mar 12 2025). https://capterra.com/p/199689/Houzz-Pro/reviews/
- STACK: yearly rises tied to features the team does not use (May 18 2026). https://www.capterra.com/p/147181/STACK-Takeoff/reviews/
- Switchers name price as the reason for leaving Buildertrend (JobTread reviews Jul 5 and Aug 22 2024; Contractor Foreman Jan 19 2026).
- Clear Estimates user asks for a cheaper "light" version for small firms (Feb 19 2026).
What it means for this app
- If this becomes a product: flat price, monthly, no onboarding fee, one-click export of every estimate. Say it plainly on the first screen.
- Excel export is also an exit door, which is itself a reason to trust the tool.

### 7. Excel survives because it is his, flexible and nearly free. Estimating modules get abandoned for Excel. Do not fight the spreadsheet; match its speed and round-trip to it.
Evidence (Checked)
- PlanSwift estimator: takeoff is easy, estimating side is not, team prices in Excel (Jul 2023). https://capterra.com/p/70808/PlanSwift/reviews/
- STACK: estimating workbook does not match their process and exports badly to Excel (May 18 2026). STACK page above.
- Buildertrend: an owner's praise is precisely that estimating is spreadsheet-style with easy on-the-fly changes and no locking (Jan 31 2022); an employee user would go back to Excel because of extra menus and two-step actions (Reddit r/Construction, Apr 2025, read via mirror). https://redlib.cypherpunktools.com/r/Construction/comments/1jrbtp8/project_management_software
- Reddit digest (no per-comment dates, mostly r/estimators): a commenter holds that a well-built Excel sheet beats anything on the market; Excel is commonly paired with Bluebeam or PlanSwift for quantities. https://gummysearch.com/tools/best-products/estimating-software/
- Contractor Foreman: reports exported to Excel because built-in ones are basic (Jul 24 2026).
- Pro Remodeler editor (May 11 2016, anecdotal): nearly all firms in two peer groups still estimated in spreadsheets; reasons were nothing better, switching disruption, cost. https://www.proremodeler.com/news/blog/55190135/for-remodelers-the-more-things-change-
What it means for this app
- Editing a line must be as fast as typing in a cell: one tap, type, tab. Any modal, submenu or save button loses to Excel.
- "Calm, premium, not a spreadsheet" is a look, not a slower interaction. If the premium screen is slower than his sheet he will go back. This is the main risk in the design brief. Inferred.
- Export to his exact Excel layout at any time, and accept his edited sheet back.

### 8. Custom builders need allowances, alternates/options, sub-bid placeholders and a client-facing proposal with markup hidden. Selections modules are the incumbents' weak spot, but that does not mean build one.
Evidence (Checked)
- JobTread: built for cost-plus and T&M; a fixed-price design-build firm hits limits on selection approvals and allowances (Dec 27 2024); selections called clunky or the main gap in four small-shop reviews (Oct 2025); cannot simply hide a line or make it optional (Oct 16 2025, 3 stars). https://capterra.com/p/218503/JobTread/reviews/?page=3 , https://capterra.com/p/218503/JobTread/reviews/?page=2
- Buildertrend: estimating too complicated, cannot group lines into categories, specs do not carry to selections, feels built for production builders (Dec 20 2023); wants several proposals per customer, accepted separately (Mar 20 2017). Buildertrend pages 3 and 8.
- Bolster: the interactive proposal where the client toggles options and sees the price move is the top praise (Nov 5 2026; Mar 10 2026). Bolster page above.
- Clear Estimates: alternates confusing (Nov 2018); a remodeler values showing labour and material as separate lines to defend the price (Pro Remodeler, Jun 7 2023). https://www.proremodeler.com/home/article/55189142/pros-picks-software-for-thorough-transparent-estimating
- Markup asks: separate labour and material markup (Handoff, Apr 9); margin and markup options on the costing screen (Buildxact, Apr 4 2023); labour margin per line (Procore Estimating, May 2019); Buildxact praised for hidden markup on quotes (Sep 15 2025). https://capterra.com/p/173135/buildXACT/reviews/ , https://www.capterra.com/p/157661/Esticom/reviews/?page=2
- Allowance conventions: remodeler hides markup on fixed-price work and applies a separate rate to allowance overages and credits (JLC, Aug 1 2006). https://www.jlconline.com/business/sales-marketing/big50-discuss-markup-questions/
What it means for this app
- Give each line a small set of states: included, allowance, alternate/option, sub bid awaited, excluded. That covers most of what people ask for without a selections module.
- Keep markup as separate visible lines for him, with a client view that folds it in. Support markup by cost type (labour, material, sub).
- A client-facing view matters for the wider market. For the first builder, confirm whether he shows clients line detail at all (a builder question, not ours to assume).

### 9. All-in-one breadth is what overwhelms small shops. They want one job done well and a clean hand-off to QuickBooks, and integrations that half-work are worse than none.
Evidence (Checked)
- Buildertrend: feature count overwhelming (Apr 10 2026; Jan 30 2026); too many steps, clunky navigation (Oct 12 2026). Buildertrend page 1. JobTread: "all-encompassing" for a small team (Apr 2025); heavy customisation complicates things (Jul 2 2025). Contractor Foreman: overwhelming at first (Jun 17 2026). Buildxact: may be more than a small contractor needs (Oct 15 2026).
- ContractorTalk thread (dates not shown): a solo operator found Jobber messy and overcomplicated and paid for the simplest tool that links to QuickBooks; a one-person shop runs everything, estimating included, in QuickBooks Desktop; a former $10M contractor says no single program does everything well. https://www.contractortalk.com/threads/looking-for-software-recommendations-for-my-business.461125
- QuickBooks sync trouble: Buildertrend integration never worked even with a hired expert (May 28 2022), partial sync and duplicate entry (Feb 10 2021); Contractor Foreman sync not as expected (Nov 9 2026; Sep 2 2026); JobTread payments not showing correctly (Nov 3 2023); Houzz Pro no sync (Mar 12 2025).
What it means for this app
- Stay an estimating tool. Scheduling, CRM, client portal, time clock and invoicing are where the incumbents are both strongest and most resented.
- Carry his cost codes on every line so the estimate can become a budget elsewhere. Export, do not live-sync, until someone asks twice. Inferred.

### 10. The window is narrower than it looks: incumbents now draft estimates with AI from the builder's own data, and residential pricing often happens before final drawings exist.
Evidence (Checked)
- JobTread AI Connector (Apr 16 2026): lets Claude or ChatGPT build estimates and budgets from the firm's own job data, with actions logged. https://www.jobtread.com/news/jobtread-launches-ai-connector-giving-contractors-a-new-way-to-run-their-business
- Buildxact "Blu" (page date not shown, 2026): takeoff assistant, estimate generator, estimate reviewer, assembly assistant, said to be trained on residential jobs; full AI tools sit in the $599/month tier ($509 on annual billing). https://www.buildxact.com/us/?p=30581 ; a trade blog says Buildxact's whole-house generation had been "coming soon" since Jun 2025 (Jun 16 2026, unverified by me at source).
- Togal user mentions a Claude connector pushing takeoffs into his estimating software (Oct 8 2026). Togal G2 page above.
- Houzz Pro user asks for automatic takeoff from uploaded plans (Mar 24 2025); Houzz has since announced "AutoMate" AI tools (seen in search results only, not read).
- Residential builders price early from concepts, months before construction documents (trade blog opinion, Jun 16 2026). https://aihomebuilding.pages.dev/articles/ai-takeoff-estimating-residential-gap.html
What it means for this app
- "AI drafts from your own prices" is no longer unique. What remains distinctive is the combination: his exact sheet, plan reading with sources, honest blanks and confidence, and almost no setup.
- Honest view: for a builder who prices by gut, takeoff time may not be the bottleneck. Much of a custom-home estimate is sub bids, allowances and judgement lines that plans cannot fill. The time saved may come mainly from pre-filling his sheet, carrying last-known figures, and catching omissions. The blind tests should measure minutes saved per estimate, not only line accuracy. Inferred.
- Consider a mode that drafts from an earlier similar job plus a few facts (size, garage or not, finish level) for the early budget conversation. Proposed; park unless wanted.

---

## 2. Complaints by theme

Setup and learning curve (strongest theme; see finding 1)
- Building the catalogue or assemblies before any payoff: JobTread, PlanSwift, Bolster, Contractor Foreman, Buildxact (pricing setup complex for new users, Jul 7 2025).
- Training that moves too fast or is not enough: JobTread bootcamp (Apr 16 2025); Buildertrend (Sep 9 2022).
- Rarely used software is forgotten between uses (Fine Homebuilding thread, 2007, old). https://finehomebuilding.com/forum/how-do-you-speed-up-estimating

Cost, contracts and lock-in (see finding 6)
- Annual terms, refusal to pause, surprise renewals, no bulk export: Buildertrend, Houzz Pro.
- Tier jumps: Handoff "big price jump between tiers" (Apr 23 2025); proposals cost extra and single-user only (Apr 11 2025).
- Per-seat AI takeoff pricing out of reach: Togal about $3,600 first year called overpriced (Reddit digest, no date); list prices as of Jul 2026: Togal from $299/user/month, STACK $249-299/user/month, PlanSwift from $2,000/year (vendor-biased source). https://www.constructconnect.com/blog/ai-powered-takeoff-and-estimating-software-a-contractors-guide-to-the-top-players-in-2026

Price data and AI accuracy (see findings 2 and 3)

Rigidity and forced workflow
- Buildxact restrictive for non-standard estimates and slow on large jobs (Apr 8 2026); quote template changes need coding (Apr 21 2026).
- Bolster hard to bend to own process (Jul 17 2026).
- JobTread: everything starts as a job, not an estimate that converts (Apr 15 2024); catalogue edits do not flow to existing cost groups (Oct 16 2025).
- Contractor Foreman: one estimate per project (Oct 17 2025).
- Buildertrend: must create a project for an unsure lead (Houzz Pro has the same complaint, Mar 24 2025).

Clunky interaction
- Extra menus and two-step actions (Buildertrend, Reddit Apr 2025; Capterra Oct 12 2026); no reliable auto-save (Oct 12 2026); back button resets (Buildxact, Mar 26 2025); frequent UI changes force relearning (Contractor Foreman May 21 2026; STACK May 19 2026).

Reliability
- Handoff crashes, freezes, time-outs, lost data (Feb 26, Apr 9, May 29 2025); Kreo lag and cloud dependence; Clear Estimates AI crashes on large PDFs (Oct 30 2026).

Fit for custom work
- Buildertrend weak for custom builds, suits cookie-cutter homes (Nov 6 2025; Dec 20 2023).
- CoConstruct users: updates slowed after the acquisition (Oct 16 2024); support declined (Dec 12 2024). CoConstruct is being retired into Buildertrend according to a competitor's press release (Jun 19 2026); no shutdown date found. https://www.jobtread.com/news/jobtread-opens-a-migration-path-for-builders-facing-the-coconstruct-phase-out

Support and sales
- Demos overselling, onboarding that feels like more selling (Buildertrend BBB, Jan 30 2024; Mar 6 2024); slow support (Houzz Pro, several 2025).

---

## 3. Praise by theme

- Templates and assemblies once built: proposals in minutes (JobTread, Aug 1 2024); estimate in about 15 minutes (May 2026); Buildxact recipes (Apr 4 2023); Clear Estimates templates (several). CoConstruct estimate templates were easier to learn than rivals (Oct 16 2024).
- Speed to a first number: Handoff 15-30 minutes instead of 2-5 hours (May 6 2025); on-site quotes (Mar 6 2025). Users accept "a good starting point" framing when the tool is fast.
- Catching forgotten items (see finding 4).
- Professional client-facing documents: Buildxact quotes with hidden markup (Sep 15 2025); Bolster interactive proposal; Houzz Pro client-facing look (May 8 2025); CoConstruct proposals (Mar 23 2021).
- One connected flow from estimate to budget, bids, change orders and invoices: JobTread "budget is the core" (Feb 8 2023); Buildertrend change-order tracking and on-site approvals (Dec 19 2024; Jan 8 2018).
- Sub bid requests and comparison inside the tool: JobTread (Oct 24 2025; Reddit Apr 2025); Buildertrend (Feb 27 2017).
- Supplier price feeds, for those who buy at list from big dealers: Buildxact (Mar 30 2026). Less relevant to a builder with his own prices.
- Low price and simple pricing: Contractor Foreman; JobTread versus Buildertrend.
- Good human support during setup: JobTread success manager sessions (Reddit Apr 2025); Buildxact training.
- Spreadsheet-like editing and unlocked estimates (Buildertrend, Jan 31 2022).
- Plain takeoff tools that "just work": Bluebeam cheap, easy to learn, pairs with Excel; On-Screen Takeoff reliable if dated (Reddit digest, no dates). https://gummysearch.com/tools/best-products/takeoff-software/

---

## 4. What users explicitly ask for

Estimating
- Hide a line or mark it optional without restructuring the estimate (JobTread, Oct 16 2025).
- Several estimates or proposals per job or customer (Contractor Foreman, Oct 17 2025; Buildertrend, Mar 20 2017).
- One-time items typed straight into an estimate without creating a catalogue item (Procore Estimating, Jan 13 2020 and May 2019).
- Group lines into categories with subtotals (Buildertrend, Dec 20 2023; Handoff users praise category subtotals).
- Separate labour and material markup; margin and markup both shown; tax-exclusive total (Handoff Apr 9; Buildxact Apr 4 2023).
- Preset cost codes (Buildxact, Mar 30 2026).
- Bulk edits across templates (Buildxact, Mar 30 2026; Aug 18 2025).
- Catalogue changes that flow, by choice, into existing estimates (JobTread, Oct 16 2025).
- A lock on a sent estimate, version history, who changed what (STACK, May 2026).
- Error check and AI suggestions on a finished estimate (Clear Estimates, Mar 2020).
- Compare this estimate with recent similar jobs (Handoff, Mar 14 2025; he asked for local market jobs, the builder's own past jobs are the honest version of this).
- Choose my supplier, use my prices (Handoff, Feb-Apr 2025).
- Answer the tool's questions before it generates (Handoff, Mar 26 2025).
- Line-item detail when needed, e.g. for insurance (Handoff, Mar 17).

Takeoff and plans
- Automatic takeoff from uploaded plans (Houzz Pro, Mar 24 2025); measuring built into the estimating tool (Clear Estimates, May 15 2025).
- AI that reads elevations, not only floor plans (Kreo, Aug 2023; STACK, May 19 2026).
- Proper handling of replaced sheets and addenda (STACK, May 2026).
- Import my own assembly library (Togal, Jun 18 2026).

Output and money
- Control of proposal look: logo size, fonts, where disclaimers sit (JobTread Oct 16 2025; Clear Estimates Dec 2020; Buildertrend BBB Mar 6 2024).
- Print view identical to screen (Clear Estimates, Feb 19 2026).
- Clean Excel export (STACK, May 18 2026).
- Working QuickBooks sync, including progress billing (Buildertrend, Sep 5 2018; many others).
- Cheaper light tier, month-to-month, pause when there is no work, export everything on leaving (Clear Estimates Feb 2026; Buildertrend 2025-2026).

---

## 5. AI estimating: where it fails and what earns trust

Where it fails (Checked in user reviews unless marked)
1. Prices: wrong labour, wrong store, stale or generic material prices, inconsistent price for the same item across runs (Handoff 2025; Clear Estimates 2025-2026).
2. Invented or drifting detail: units and descriptions change between estimates, presets forgotten, basic maths errors (Handoff, Jan 20 and Apr 9 2025).
3. Unrequested changes: the tool "adjusts" things nobody asked it to (Handoff, Apr 23 2025).
4. Messy output that costs as much time to tidy as to do by hand (Kreo, Nov 2023).
5. Drawing types: fine on clean vector floor plans; weak on scans, dense sheets, elevations, sections, hand sketches (Kreo; Togal; Robotics & Automation News test; vendor blogs).
6. Scope that is not drawn: general requirements, local code and permit items, site conditions, sub arrangements, what this builder habitually includes (Handoff, Apr 15; STACK and Togal blogs; JLC 2019).
7. Large or heavy files: crashes and time-outs (Clear Estimates Oct 30 2026; Handoff; Togal slow on high-resolution pages, Feb 13 2026).
8. Marketing accuracy figures: the 95-97% claims are vendor-reported or from one commercial-style test; none is a residential custom-home result (Inferred from the sources in finding 3).

What makes users trust the numbers (Checked where sourced, otherwise Inferred)
- The prices are theirs (Handoff Apr 4 2025; the general pattern in finding 2).
- The result lands close to their own figure on a job they already priced; "within about $100 of my own" is the most persuasive thing a reviewer says (Handoff, Mar 28). This is exactly the blind test on finished jobs.
- They can see where each quantity came from and fix it in place (For Construction Pros, Oct 13 2026; STACK version-history asks).
- The tool admits what it assumed and where sheets conflict (Handoff's own blog presents this as a feature).
- A human-checked first pass is the accepted model; nobody credible sells unsupervised output (Beam AI puts its own reviewers on output; ConstructConnect recommends tiered review). 
- Framing as a starting point. Users who expected a finished bid rated low; users who expected a draft rated high even while noting errors (Handoff ratings pattern; Inferred).

What makes them distrust it
- One absurd number (the $7,500 doors) colours the whole estimate. Inferred from review tone.
- Inconsistency between runs.
- Having to change "most of the numbers" (Mar 11 2025).
- Paying a high monthly price for something that feels unfinished (Handoff, Mar 20 2025).

Implication: a single wild quantity will cost more trust than ten blanks. An outlier check against his own past jobs (cost per square foot by division, quantity per square foot) before showing a draft is cheap insurance. Proposed.

---

## 6. Essential versus bloat for a builder with fewer than five people

Rated from the evidence above; my judgement, so Inferred throughout.

Essential
- His own line items, cost codes and prices, imported not rebuilt.
- Templates by job type (new build, garage apartment/ADU, renovation) made from his past estimates.
- Scope checklist and omission check.
- Fast in-place editing; add a one-off line by typing.
- Line states: included, allowance, alternate, sub bid awaited (with last known figure), excluded.
- Markup, overhead, contingency and allowances as separate visible lines; markup by cost type; margin shown alongside markup.
- Revisions with history: what changed since the last version and why.
- Export to his Excel layout; clean PDF/print; same numbers everywhere.
- Cost codes carried on every line so the estimate can become a budget.

Important, second step
- Client-facing proposal view that hides markup and can group or summarise lines.
- Sub and vendor bid tracking against lines (who was asked, what came back). Users praise in-tool bid requests, but a simple "awaiting / received / chosen" field covers most of it.
- Estimate versus actual comparison when a job closes; this is how his price list improves.
- QuickBooks: export of the estimate as a budget by cost code. Many ask for sync; many report sync breaking.

Called bloat, or a source of pain, by small shops
- Scheduling, Gantt, daily logs, time clock, CRM and lead pipeline, client portal, warranty, marketing/website, payments, 3D design.
- Full selections module with client approvals. Needed by some custom builders, but it is the feature incumbents most often get wrong; out of scope for an estimating helper.
- Supplier price feeds and national cost databases (for a builder who uses his own prices).
- Heavy customisation engines (formulas, automations) that need a specialist.
- Live two-way accounting sync as a first-version feature.

Split opinion
- On-screen takeoff tools. Estimators want them; a gut-pricing owner mostly wants the answer and a way to check it. A viewer that shows the measured region is enough.
- Change orders. Clearly valued (Buildertrend praise), but they belong to the job-running app, not the estimate draft. Hand over cleanly.

---

## 7. Things this app should deliberately NOT build

1. Market or database prices in his sheet. The evidence backs the current stance. An "outside reference" note at most.
2. Automatic price updates of any kind that can overwrite his entries.
3. A selections, client-portal or approvals module.
4. Scheduling, CRM, time tracking, invoicing, payments.
5. Live two-way QuickBooks sync (export first).
6. Supplier catalogue integrations.
7. A general manual takeoff toolset to rival Bluebeam or PlanSwift. Those are cheap, liked and already paired with Excel.
8. A single "accuracy %" badge. Sources warn against it and users are burned by it; use High/Medium/Low with a reason.
9. Auto-adjusting or "smart" rewrites of lines he has touched.
10. Annual contracts, onboarding fees, per-seat pricing, tier-gated proposals, if this is ever sold.
11. Formula or automation builders that need training.
12. A chat-only interface as the main way to build an estimate. One Handoff user disliked being questioned mid-flow; the estimate itself should be the interface. Inferred, thin evidence.

Where my view cuts against the current approach
- Plan reading may be the least reliable and least valuable part for this builder; pre-filling his sheet, sub-bid carry-over and omission checks may deliver most of the time saved. Test that directly.
- "Not spreadsheet-feeling" is a risk if it costs editing speed. Users praise spreadsheet-style estimating by name.
- "His prices beat anything automated" is supported for prices. It is not evidence that his scope memory beats a checklist; the omission literature suggests the opposite.
- For the wider market, a client-facing proposal is closer to essential than optional; the first builder may not need it, others will.

---

## 8. What could not be verified

- Reddit threads directly. Reddit and its search were not reachable from this session; I read one r/Construction thread through a mirror and two third-party digests of Reddit comments that carry no per-comment dates and lean towards commercial estimators. First-hand Reddit voice from residential builders is thinner than I wanted.
- ContractorTalk and JLC forums: one ContractorTalk thread read (no dates shown); JLC forum threads not found. Fine Homebuilding threads read are from 2004-2008 and used only for attitudes.
- No statistic on how many small residential builders estimate in Excel. The only source is anecdotal and from 2016. I did not find an NAHB or trade-press survey with this figure.
- No independent accuracy benchmark for AI takeoff on custom residential plans. All percentage accuracy claims trace to vendors or one commercial-style test.
- Buildertrend's actual prices (not published; figures seen are third-party or competitor reports), and the date CoConstruct shuts down.
- User reviews of the newest AI features specifically: Buildxact Blu, Houzz Pro AutoMate, STACK IQ, JobTread AI Connector. I found announcements, almost no dated user verdicts.
- Bluebeam user reviews were not read directly; Bluebeam evidence is from the Reddit digest only.
- Procore Estimating: the reviews visible were mostly electrical and low-voltage subs from 2019-2020 (the Esticom era). That it is a poor fit for a small residential builder is my inference from price comments and absence of residential reviewers.
- Review dates and company sizes were transcribed by a page-reading tool; a small number may be mis-read. Company size was often not shown, so "small builder" is sometimes inferred from role (owner) alone.
- Whether the handful of low-star reviews represent many users. They are a minority of visible reviews on every product; I weighted them for content, not frequency.
- Kreo reviews are mostly UK quantity surveyors; Togal and STACK reviews are mostly commercial trades. Their failure modes are relevant, their satisfaction levels are not transferable.

---

## 9. Source list

User reviews and forums (first-hand)
- Capterra, Buildertrend reviews p1, p3, p8 (reviews 2011-Nov 2026). https://www.capterra.com/p/70092/Buildertrend/reviews/
- BBB, Buildertrend customer reviews (Nov 2023-Sep 2026). https://www.bbb.org/us/ne/omaha/profile/computer-software/buildertrend-solutions-0714-300027310/customer-reviews
- Capterra, JobTread reviews p1-p3 (2022-Nov 2026). https://capterra.com/p/218503/JobTread/reviews/
- Software Advice, JobTread reviews (2022-Nov 2026). https://www.softwareadvice.com/construction/jobtread-profile/reviews/
- Capterra, Handoff reviews p1-p2 (2025). https://www.capterra.com/p/10026318/Handoff/reviews/
- Capterra, Buildxact reviews (2019-Oct 2026). https://capterra.com/p/173135/buildXACT/reviews/
- Capterra, Houzz Pro reviews (Feb-Aug 2025). https://capterra.com/p/199689/Houzz-Pro/reviews/
- Software Advice and Capterra, Clear Estimates (2017-Oct 2026). https://www.softwareadvice.com/construction/clear-estimates-profile/ , https://www.capterra.com/p/24826/Clear-Estimates/
- Capterra, Contractor Foreman reviews (Oct 2025-Nov 2026). https://www.capterra.com/p/166113/Contractor-Foreman/reviews/
- Capterra, STACK reviews (2021-Nov 2026). https://www.capterra.com/p/147181/STACK-Takeoff/reviews/
- Capterra, PlanSwift reviews (2017-Jul 2026). https://capterra.com/p/70808/PlanSwift/reviews/
- Capterra, Kreo reviews (2022-Nov 2026). https://www.capterra.com/p/231342/Kreo-2D-Takeoff/reviews/
- G2, Togal.AI reviews p3 (Jan-Oct 2026). https://g2.com/products/togal-ai/reviews?page=3
- Capterra, Procore Estimating (ex-Esticom) reviews p2 (2019-2026). https://www.capterra.com/p/157661/Esticom/reviews/?page=2
- Capterra, Bolster (ex-CostCertified) reviews (2025-Nov 2026). https://www.capterra.com/p/199769/CostCertified/reviews/
- Reddit r/Construction, "Project management software" (Apr 2025), via mirror. https://redlib.cypherpunktools.com/r/Construction/comments/1jrbtp8/project_management_software
- GummySearch digests of Reddit comments on estimating and takeoff software (no per-comment dates). https://gummysearch.com/tools/best-products/estimating-software/ , https://gummysearch.com/tools/best-products/takeoff-software/
- BiggerPockets forum, bidding software thread (about 2020-2024, relative dates). https://www.biggerpockets.com/forums/24/topics/799869-what-are-contractors-using-for-bidding-software
- ContractorTalk, software recommendations thread (dates not shown). https://www.contractortalk.com/threads/looking-for-software-recommendations-for-my-business.461125
- Fine Homebuilding forum threads (2004, 2007, 2008; attitudes only). https://finehomebuilding.com/forum/is-estimating-an-art-or-a-science , https://finehomebuilding.com/forum/how-do-you-speed-up-estimating , https://finehomebuilding.com/forum/estimating-software-pros-cons

Trade press and independent
- JLC, D. Gerstel, "The Greased Pigs of Estimating" (Feb 13 2019). https://www.jlconline.com/business/estimating-job-costing/the-greased-pigs-of-estimating_o
- JLC, Big50 markup Q&A (Aug 1 2006). https://www.jlconline.com/business/sales-marketing/big50-discuss-markup-questions/
- Pro Remodeler, S. Alfano (May 11 2016). https://www.proremodeler.com/news/blog/55190135/for-remodelers-the-more-things-change-
- Pro Remodeler, Pro's Picks, Clear Estimates (Jun 7 2023). https://www.proremodeler.com/home/article/55189142/pros-picks-software-for-thorough-transparent-estimating
- For Construction Pros, V. Gebarski, testing AI takeoff tools (Oct 13 2026; author linked to an AI vendor). https://www.forconstructionpros.com/construction-technology/automation-and-ai/article/22975238/buildvision-ai-test-ai-takeoff-tools-before-using-them-for-bids
- Robotics & Automation News, six-tool test (Feb 19 2026; method thin). https://roboticsandautomationnews.com/2026/02/19/6-ai-construction-estimating-software-tested-on-complex-project-accuracy/
- Bricks & Bytes newsletter (Jul 22 2026). https://bricks-bytes.beehiiv.com/p/ai-reads-the-blueprint-what-it-reads-next
- AI Home Building blog (Jun 16 and Sep 16 2026; opinion, leans on vendor figures). https://aihomebuilding.pages.dev/articles/ai-takeoff-estimating-residential-gap.html , https://aihomebuilding.com/stories/ai-takeoff-shootout-residential-estimating-2026
- GetApp, Buildertrend vs JobTread for remodelers (Oct 22 2026; referral-fee site). https://www.getapp.com/resources/buildertrend-vs-jobtread-for-remodelers/

Vendor material (used for what exists and for admissions against interest only)
- JobTread press releases (Apr 16 2026; Jun 19 2026). 
- Buildxact US product/pricing page (date not shown, 2026). https://www.buildxact.com/us/?p=30581
- Handoff blogs (May 27 2026; one date not shown). https://handoff.ai/blog/is-ai-construction-estimating-accurate-enough-to-trust-here-s-what-the-data-says
- STACK blog (date not shown); Togal blog (date not shown).
- ConstructConnect blogs (Aug 3 and Aug 18 2026; owns On-Screen Takeoff and PlanSwift).
- Bluebeam press release on its AEC survey (Oct 28 2025; 1,000+ larger-firm decision makers; 27% of firms use AI). https://press.bluebeam.com/2025/10/new-bluebeam-report-shows-early-ai-adopters-in-aec-seeing-significant-roi-despite-uneven-adoption/

Read and set aside as weak
- JLC "Guide to estimating software" (Oct 30 2020): sponsored by Buildxact.
- dev.to "tested 8 AI tools" (May 25, year not shown): no method, author sells a related product.
- SuperDupr Buildertrend review (Sep 8 2026): agency blog, third-party price figures.
- sagnikbhattacharya.com (Sep 27 2026): consultant opinion with illustrative scenarios.
- Projul, Buildern and similar comparison blogs seen in search results: competitor marketing, not read as evidence.

---

## Appendix: working notes by source

### Buildertrend - Capterra reviews page (https://www.capterra.com/p/70092/Buildertrend/reviews/) read 2026-11-19, ~33 of 2,490 reviews visible
- Owner-operator, 1 star, Oct 7 2026: pushed into annual contract, could not go back to month-to-month, locked to May 2027; ex-CoConstruct user.
- CEO 2-10 staff, May 2026: paid 6 months with no active jobs, vendor would not pause contract.
- Owner 2-10, Dec 2025: no bulk export of files/photos/proposals/customer data on cancelling; long learning time; poor support.
- CEO, Oct 12 2026 (4 star): steep learning curve, clunky navigation, lag, no reliable auto-save, high price.
- Accounts payable, Nov 6 2025 (2 star): hard to navigate, data re-entry, weak for custom builds, suits cookie-cutter homes.
- Owner (CoConstruct), Oct 16 2024: estimate templates good, easier to learn; updates slowed after Buildertrend acquisition.
- Office admin (CoConstruct) Mar 2021: long setup + learning curve; templates/RFP/QuickBooks sync gave professional proposals.
- Several 2026: price rises periodically, add-on upsell, feature count overwhelming.
### Reddit r/Construction "Project management software" Apr 2025 (mirror https://redlib.cypherpunktools.com/r/Construction/comments/1jrbtp8/project_management_software)
- Ex-CoConstruct user moving to JobTread: estimating excellent, bid requests useful, but configuring took a long time; client comms weaker.
- Buildertrend employee user: terrible UX, extra submenus/two-step actions, would go back to Excel.
- Builder of CAD 10-20M homes ran on Excel/Google Sheets.
### JobTread - Capterra (https://capterra.com/p/218503/JobTread/reviews/) ~25 of 144 visible
- Owner Aug 1 2024: once catalog built, proposals in minutes. Setup time-consuming (Greg D. Oct 15 2025; remodeler Nov 18 2026; Zach B. Oct 16 2025). Bootcamp too fast (Apr 16 2025). Estimator Oct 24 2025: takeoff measurements don't always line up. Selections hardest part (Oct 16 2025). QuickBooks sync still being refined (Feb 26 2024).
### AI takeoff
- For Construction Pros, V. Gebarski (BuildVision AI linked), Oct 13 2026, https://www.forconstructionpros.com/construction-technology/automation-and-ai/article/22975238/buildvision-ai-test-ai-takeoff-tools-before-using-them-for-bids : test on own finished jobs; track missed scope / extra scope / wrong class / wrong scale separately; traceability to sheet+revision; visible recoverable error safer than one that looks right; measure correction effort not just speed. No measured numbers.
- aihomebuilding.pages.dev, F. DeLuca, Jun 16 2026 (independent blog, unknown authority): accuracy benchmarks are commercial plan sets; no independent residential benchmark; Buildxact whole-house AI "coming soon" since Jun 2025; residential builders price early from concepts, before final drawings.
### Handoff - Capterra (https://www.capterra.com/p/10026318/Handoff/reviews/) 27 of 42 visible; most dated 2025 (year shown only on some; months Feb-Jul)
- Owner 2-10, Jan 20 2025: inconsistent prices for same item, wrong units/descriptions, pricing rules not always followed.
- Self-employed owner, Mar 11: most numbers need changing, don't match real costs. Remodeler Mar 24: AI pricing not accurate enough.
- Co-owner Apr 9: basic math errors, forgets presets and small items, times out.
- Foreman Apr 15: misses real labour costs and local permit/code rules.
- President Apr 23: adjustments often wrong or unrequested.
- GC May 6: 15-30 min instead of 2-5 hrs, but some bids wildly high (8 doors priced around $7,500).
- Painter Jun 10: prices pulled from wrong store chain; owner Apr 25: retailer prices off.
- Praise: speed, on-site quotes, catches forgotten items (fasteners etc), professional proposals, one-person shops.
- Asks: separate labour/material markup, takeoffs, line-item detail, templates, answer questions before it generates.
### Buildxact - Capterra (https://capterra.com/p/173135/buildXACT/reviews/) 25 of 185 visible
- Praise: templates/recipes (assemblies), supplier price feeds, professional quotes with hidden markup, support/training.
- Complaints: learning curve (about 6 of 25), restrictive for non-standard estimates and slow on large jobs (Apr 8 2026), manual plan scaling inaccurate (Mar 12 2025), quote template changes need coding (Apr 21 2026), no preset cost codes (Mar 30 2026), wants margin/markup options on costing screen (Apr 4 2023), bulk edit missing (Mar 30 2026). Some reviewer roles look unrelated to construction - weigh lightly.
### Houzz Pro - Capterra (https://capterra.com/p/199689/Houzz-Pro/reviews/) 25 of 1,089 visible, Feb-Aug 2025
- Locked 12-month contracts, cannot cancel mid-term, charged after cancel (Feb 10, Feb 19, Apr 3, May 16, Jun 17 2025); renewal up over 400% (Mar 12 2025); no QuickBooks sync (Mar 12); estimate writing cumbersome, takeoff behind dedicated tools (Apr 24); asks for automatic takeoff from uploaded plans (Mar 24). Praise: client-facing look, 3D, easy invoices.
### Clear Estimates - Software Advice (https://www.softwareadvice.com/construction/clear-estimates-profile/) 10 of 117 visible, many vendor-invited
- Templates stop omissions (2018); price database needs constant updating to match real prices (Apr 2026); automatic price updates unusable because they overwrite custom tasks (Feb 2026); layout on screen differs from print, invites errors (Feb 2026); alternates confusing (2018); sales tax clunky (2021); wants error check + AI suggestions (2020).
### JLC guide (https://www.jlconline.com/business/guide-to-estimating-software-for-small-builders-remodelers-and-contractors) Oct 30 2020 - sponsored by Buildxact, marketing only; not used as evidence.
### GummySearch Reddit digest, estimating software (https://gummysearch.com/tools/best-products/estimating-software/) - aggregate of Reddit comments, no per-comment dates; mostly r/estimators (commercial-leaning)
- One commenter: a well-built Excel sheet outperforms anything on the market; Excel commonly paired with Bluebeam or PlanSwift for quantities. Procore: price out of budget. PlanSwift: needs heavy assembly/database setup. Togal: fast, auto-classifies walls, but ~$3,600 first year called overpriced.
### Togal.AI - G2 page 3 (https://g2.com/products/togal-ai/reviews?page=3) 2026 reviews, commercial trades
- May 7 2026: cannot reliably find MEP penetrations or tell rated from non-rated walls. Jan 29 2026: auto takeoff fits simple floor-plan counts, not work needing plans+sections+elevations together. Jun 18 2026: cannot import own ~4,000-item assembly library. Apr 9 2026: wants pricing and local code awareness. G2 lists $299/user/month billed yearly.
### STACK - Capterra (https://www.capterra.com/p/147181/STACK-Takeoff/reviews/) ~25 of 1,400 visible
- May 2026 cluster: yearly price rises bundled with unused features; rigid pricing; estimating workbook doesn't match own process and exports badly to Excel (May 18 2026); wants bid-set lock, version history, record of who changed what, addendum sheet handling; AI limited on messy plans (May 19 2026).
### Contractor Foreman - Capterra (https://www.capterra.com/p/166113/Contractor-Foreman/reviews/) 25 of 843 visible
- Price is the main praise; switchers from Buildertrend after price rise (Jan 19 2026; May 26 2026). Cost database setup is real work (Oct 30 2026; Oct 7 2026). Estimate database lacks common items (Feb 11 2026). One estimate per project only (Oct 17 2025). QuickBooks sync problems (Nov 9 2026; Sep 2 2026). Overwhelming at first (Jun 17 2026). Dated UI, reports exported to Excel (Jul 24 2026).
### CoConstruct phase-out
- JobTread press release Jun 19 2026 (competitor; https://www.jobtread.com/news/jobtread-opens-a-migration-path-for-builders-facing-the-coconstruct-phase-out): Buildertrend bought CoConstruct 2021, is retiring it, users pushed to Buildertrend pricing (revenue-tiered, unpublished). No shutdown date given. Competitor source - treat pricing claims as unverified.
- SuperDupr review Sep 8 2026 upd Nov 2 2026 (agency blog; https://superdupr.com/blog/buildertrend-review): Buildertrend has no public price list; third-party reports ~$339-499 / $699-799 / $829-1,099 per month, onboarding ~$400-1,500, estimating sits in the middle tier. JobTread list price $199/mo first user + $20/user (read from jobtread.com/pricing Oct 15 2026 by that author). UNVERIFIED by me first-hand.
### Vendor admissions on AI limits
- STACK blog (date not shown; https://www.stackct.com/blog/what-ai-gets-right-about-construction-takeoffs-and-what-it-still-gets-wrong/): AI cannot know contractor-specific context (whether he includes blocking, labour adders, sub arrangements), misses buried spec notes/addenda, arch vs structural conflicts; finding an item is not understanding it.
- Handoff blog (date not shown; https://handoff.ai/blog/seven-things-ai-takeoffs-can-and-cant-read-on-your-construction-plans): tuned for residential up to ~7,000 sq ft; does not calculate engineering values; one-off custom work needs user's pricing; poor scans need more review; it flags assumptions and sheet conflicts for the user to verify.
### Fine Homebuilding forum 2008 (https://finehomebuilding.com/forum/estimating-software-pros-cons) - old; one poster claims packaged estimators off by factor of two; another prefers own local prices in a spreadsheet. Background only.
### Robotics & Automation News test, D. Edwards, Feb 19 2026 (https://roboticsandautomationnews.com/2026/02/19/6-ai-construction-estimating-software-tested-on-complex-project-accuracy/)
- One 200+ sheet multi-discipline commercial-style set, single run; scorecard not shown. Togal needs manual tracing on hand-sketched plans and counts only (no costs); Kreo tripped on plumbing symbols; STACK does not auto-classify everything. No residential test. Treat as weak-to-moderate evidence.
### dev.to "tested 8 tools" (date: May 25, year not shown) - no method, author sells an estimating kit: NOT used as evidence. sagnikbhattacharya.com Sep 27 2026 - consultant opinion, illustrative scenarios only: used only for the idea "load your own rates first".
### BiggerPockets thread (https://www.biggerpockets.com/forums/24/topics/799869-what-are-contractors-using-for-bidding-software) relative dates "6y" to "2y" (about 2020-2024)
- Atlanta contractor: bought PlanSwift, spent about two years customising it, then hard to hand off; spreadsheets grew complex over years. Another contractor: off-the-shelf estimating software is not useful until customised. GC with detailed cost-code spreadsheet wants something better and quicker, expects Buildertrend setup to take time.
### BBB Buildertrend (https://www.bbb.org/us/ne/omaha/profile/computer-software/buildertrend-solutions-0714-300027310/customer-reviews) 10 reviews, avg 1.1
- Annual lock-in, refused pause (Sep 28 2026; May 1 2026); renewal charged much higher than expected + double entry (Mar 3 2026); no export-all, vendor confirmed (Dec 4 2025); no trial before year commitment (Dec 3 2025); promised proposal formatting did not work (Mar 6 2024); demo oversold (Jan 30 2024).
### Buildertrend Capterra page 3 (https://www.capterra.com/p/70092/Buildertrend/reviews/?page=3)
- President Dec 20 2023 (3 star): estimating too complicated, cannot group lines into categories, specs do not carry to selections, feels built for production not custom builders. Owner May 28 2022: price up about 80% after three years; QuickBooks integration never worked even with hired expert. CEO Feb 10 2021: QuickBooks sync partial, duplicate entry. One-person operator Feb 6 2020: learning was a real challenge, payback in about 90 days. President Sep 9 2022: three 45-min trainings not enough.
### JobTread Capterra page 3 (https://capterra.com/p/218503/JobTread/reviews/?page=3)
- PM Dec 27 2024: built for cost-plus/T&M; fixed-price design-build firm hits limits on selection approvals and allowances, uses workarounds. Designer Nov 6 2024: selections/specs underdeveloped. Builder Aug 22 2024: left Buildertrend after cost more than doubled; QuickBooks-only. Owner Jul 5 2024: price main reason to leave Buildertrend. Commercial VP Apr 15 2024: dislikes that everything starts as a job, not an estimate that converts.
### Togal blog "Where AI whiffs" (date not shown, (c) 2026; https://www.togal.ai/blog/estimators-edge-where-ai-wins): AI does not grasp intent behind incomplete drawings, trade judgement, local market, scope gaps, constructability, client expectations.
### Pro Remodeler, S. Alfano, May 11 2016 (https://www.proremodeler.com/news/blog/55190135/for-remodelers-the-more-things-change-): nearly all firms in two remodeler peer groups (up to $34M revenue) still estimated in spreadsheets: nothing better found, switching disruption, IT cost. Anecdotal, old.
### AI Home Building, J. Kowalski, Sep 16 2026 (https://aihomebuilding.com/stories/ai-takeoff-shootout-residential-estimating-2026) - trade blog, leans on vendor claims
- No published head-to-head on a residential addition/custom set; stale price books a named risk; AI measures but does not judge sub reliability, allowances, site conditions; cites a Bluebeam (vendor-run) survey of 1,000+ AEC people saying 73% of firms do not use AI - NOT verified by me at source. Names STACK IQ, Buildxact Blu, Beam AI (human QA before delivery).
### PlanSwift - Capterra (https://capterra.com/p/70808/PlanSwift/reviews/) 25 of 402 visible
- Estimator Jul 2023 (2 star): takeoff easy, estimating side not user-friendly, team prices in Excel instead. PM Mar 2026: fast once assemblies set up, but big setup + training, not plug and play. Jul 2026: dated interface. No residential-specific reviews seen.
### Kreo - Capterra (https://www.capterra.com/p/231342/Kreo-2D-Takeoff/reviews/) 26 reviews, mostly UK QS/commercial
- Nov 2023 flooring: auto-measure output messy, tidying took as long as manual takeoff. Sep 2023 QS: AI hit-and-miss on dense drawings. May 2024: best on vector/modern floor plans, struggles on scans. Nov 2026: measurement errors sometimes need heavy editing. Aug 2023: wants AI beyond floor plans (elevations, steel). Dec 2023 (1 star): lost a day, no usable measurements.
### Procore Estimating (ex-Esticom) - Capterra p2 (https://www.capterra.com/p/157661/Esticom/reviews/?page=2): mostly electrical/low-voltage subs, 2019-2026; nothing residential-builder. Asks: one-time/temporary items on an estimate, labour margin per line. Evidence that Procore Estimating is not aimed at the target user is Inferred from absence + Reddit digest "out of budget".
### JLC Big50 markup Q&A, Aug 1 2006 (https://www.jlconline.com/business/sales-marketing/big50-discuss-markup-questions/): remodeler does not disclose markup on fixed-price; allowance overage/credit handled with a separate markup rate; another walks clients through the spreadsheet line by line to reduce anxiety. Old but shows allowance + hidden-markup conventions.
### GetApp Buildertrend vs JobTread for remodelers, Oct 22 2026 (https://www.getapp.com/resources/buildertrend-vs-jobtread-for-remodelers/) - GetApp earns referral fees
- Theme analysis of Capterra/Software Advice reviews Oct 2024-Oct 2026: Buildertrend = cost for small firms, overwhelming, too many steps; JobTread = setup effort building templates/budgets, selections need work. G2 reviewers report average go-live about one month (JobTread) vs three months (Buildertrend). No per-theme counts.
### Bluebeam press release Oct 28 2025 (https://press.bluebeam.com/2025/10/new-bluebeam-report-shows-early-ai-adopters-in-aec-seeing-significant-roi-despite-uneven-adoption/) - vendor survey, 1,000+ AEC tech decision-makers, 5 countries, July 2025; mostly larger firms
- 27% of firms use AI; 52% still use paper in design, 49% in planning; only 11% fully digital. No trust/accuracy barrier figure. Not specific to small residential builders.
### JobTread AI Connector press release Apr 16 2026 (https://www.jobtread.com/news/jobtread-launches-ai-connector-giving-contractors-a-new-way-to-run-their-business): MCP server letting Claude/ChatGPT build estimates and budgets from the firm's own job data; actions logged. Means incumbents now let a general assistant draft estimates from the builder's own catalogue - direct overlap with this app's idea (minus plan reading).
### JLC, D. Gerstel, Feb 13 2019 "greased pigs" (https://www.jlconline.com/business/estimating-job-costing/the-greased-pigs-of-estimating_o): omissions that hurt most are items not on the plans - general requirements, permits, scaffolding, cleanup, supervision, blocking, between-trade gaps; build and keep your own checklist; included/not-included forms with subs.
### Fine Homebuilding 2004 thread (https://finehomebuilding.com/forum/is-estimating-an-art-or-a-science): small operators keep the database in their head and doubt software pays off for a handful of jobs; others want a template that mirrors how they already think plus estimate-vs-actual comparison. Old; attitudes only.
### JobTread - Software Advice (https://www.softwareadvice.com/construction/jobtread-profile/reviews/) 25 of 144; 20 from 2-10 staff/self-employed; 11 of those vendor-invited with incentive
- 7 of 20 mention learning curve/training/switching effort. Owner May 2026: templates cut estimates to about 15 min, but learning curve on cost types/margins/selections and data cleanup falls on user. Oct 2025 (3 star): catalogue changes do not flow to existing cost groups; cannot simply hide a line or make it optional; little control of document branding. Oct 2025: estimating caught missed items. Selections clunky (4 reviews).
### Handoff Capterra p2 (https://www.capterra.com/p/10026318/Handoff/reviews/?page=2) all 2025
- CEO Feb 18 2025: accurate apart from labour. Owner Mar 11 2025 (3 star): changes most numbers. GC Mar 14 2025: wants comparison to recent similar local jobs. Owner Apr 4 2025: must set own prices and let it learn them. Owners Feb 15 / Mar 19 2025: want to choose supplier. Mar 26 2025: asks questions but generates before he can answer. Mar 23 2025: often adds items he'd forget, sometimes forgets items.
### Bolster (ex-CostCertified) - Capterra (https://www.capterra.com/p/199769/CostCertified/reviews/) ~30 of 83
- Interactive client proposal where client toggles options/upgrades and sees price change is the top praise (Nov 5 2026; Mar 10 2026; Jun 10 2026). Setup pain: about two months to load supplier pricing (Mar 10 2026); 1-star reviews on onboarding, one told to key prices in by hand (Feb 12 2025; Nov 19 2026). Hard to bend to own process (Jul 17 2026).
### Fine Homebuilding 2007 thread (https://finehomebuilding.com/forum/how-do-you-speed-up-estimating): owner-operators hate office time, lose time waiting on supplier calls, struggle to refile old estimates, forget rarely-used software between uses; one who moved to dedicated software says customising took months; another asks whether actual hours are fed back into estimates. Old; attitudes only.
### ConstructConnect (owns OST + PlanSwift) blogs
- Aug 18 2026 (https://www.constructconnect.com/blog/are-ai-takeoffs-accurate-in-2026): fail cases - poor scans, handwritten markups, unusual symbols, irregular geometry, revisions across sheets, scope that depends on specs/exclusions, incomplete or conflicting sets. Recommends tiered review (spot-check / full / always). Numbers are vendor-study only.
- Aug 3 2026 guide (https://www.constructconnect.com/blog/ai-powered-takeoff-and-estimating-software-a-contractors-guide-to-the-top-players-in-2026): prices as of Jul 2026 - PlanSwift from $2,000/yr first seat; STACK $249-299/user/mo; Togal from $299/user/mo; Beam AI done-for-you $15-25K/yr per trade; xBuild chat-based residential roofing. Vendor-biased.
### Bricks & Bytes, O. Drury, Jul 22 2026 (https://bricks-bytes.beehiiv.com/p/ai-reads-the-blueprint-what-it-reads-next) newsletter
- Vendor accuracy claims (95%+) self-reported; accuracy said to fall on scans, dense annotation, overlapping trades; errors cluster in quantities that must be derived rather than read; general language models can describe a sheet yet miscount windows; no fully unsupervised end-to-end tool; warns against black-box outputs with hidden assumptions. Figures unverified.
### Buildertrend Capterra p8 (https://www.capterra.com/p/70092/Buildertrend/reviews/?page=8)
- Owner Jan 31 2022: likes spreadsheet-style estimating, easy on-the-fly changes, estimates not locked; dislikes low intro price then rises. Owner Sep 10 2024: takeoff excellent but price too high for small firm, steep curve. Owner Nov 1 2022: price went from $59/mo to about $1,300/mo. President Mar 15 2023: 75% rise without notice. Small custom builder 2013: selections page cut repeat client questions. Office manager 2012: still kept a separate Excel tracking sheet. 2017: wants several proposals per customer accepted separately.
