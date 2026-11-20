# Where we are and what is next

**Purpose:** the one page that says what stage the project is at, what is next, what is waiting on the owner and what the agent owes. Written by hand; update it whenever any of those change. Decisions themselves live in `decisions/` and are listed in `CURRENT.md`.

**Last updated:** Nov 19, 2026.

## Stage
The project is moving from a claude.ai Project into this repository. Nothing of the screens is built. One job (Job A) has been tested; it is no longer blind.

## Done
- The method, standards and format documents are in `docs/`.
- 69 decisions are recorded: 60 standing, 5 proposed, 4 superseded. The older decisions held in the project's "17 Current state" document were brought in on Nov 19 (0013 to 0066), each checked against the old working log for its date and the owner's words. `CURRENT.md` is now the full list.
- All eleven scripts are in `kit/`, with the cost code list and the Job A cost code rows. They were re-created from the project copies on Nov 19 (the owner holds no other copy) and checked by running them: both test scripts pass (4,275 damaged files tried, as recorded on Nov 16); the importer reproduces his sheet to the cent (471 lines, cost 231,247.05, total 289,058.81); the budget by cost code matches his cost workbook; the document maker's own checks pass; and the Job A remake reproduces the recorded scope and score figures.
- First pass of moving the documents, Nov 19: the questions for the builder are in `docs/builder/questions.md` (ten owed questions added, 39 to 48), and the screen design document is in `docs/screens/laptop-screens-design.md` (moved as it was; the lines that are behind the decisions are listed at its top). The canvas drawings were not copied: `docs/screens/canvas.md` points to them and says why (Decided by Claude; reversible).
- A method audit by three fresh researchers was run on Nov 19 at the owner's request (`docs/history/2026-11-19-method-audit/`): a cold audit of this repository, method and documentation structure, and market research on estimating software. Findings are not decisions.
- A full review by five fresh reviewers was run on Nov 19 (`docs/history/2026-11-19-full-review.md`).

## Next, in order
The owner approved the phase path on Nov 19 (decision 0067). Phases 0 to 6 are set out in that decision.

**Now: phase 0, close the records.**
1. Fix the contradictions and dangling references listed in `docs/history/2026-11-19-method-audit/repository-audit.md` (two instruction sets, rules repeated with different wording, "doc NN" pointers, `README.md` describing folders that are empty).
2. Put the five proposed decisions (0061, 0063 to 0066) and decision 0026 to the owner in one short batch.
3. Create the empty `spec/` folder, its templates and its checking script, from `method-and-structure.md`, section 3.
4. Give every finding in the two review documents one status: fixed, a decision, a question, or parked with a reason.
5. Sort `docs/builder/questions.md` into: the owner can answer (general trade practice); only the builder can answer and it blocks design; can wait. Bring the short blocking list to the owner (decision 0069).

**Then phase 1, map and name:** the story map, the objects and their states, and who figures each quantity (Proposed in decision 0068).

**Still open from the move:** the cost code list document and the old working log (five parts) are not in the repository yet. Not needed for phases 0 to 2.

## Waiting on the owner
- Five decisions are recorded as proposed and need a yes or no: 0061 (score reports lead with the unseen measured lines), 0063 (check a recommendation three ways before a lock), 0064 (sketch sample figures from one made-up data set), 0065 (walk the five tasks before showing a layout), 0066 (carry an earlier review's accepted fixes into a redraw).
- Decision 0026 (a vendor's own quantity shown beside ours) is recorded as decided by Claude: the old log shows no lock of the owner's on it. Say if it should not stand.

## Owed by the agent
- From the method audit: nothing decides what happens when he types into the one price box (decision 0005) on a line item with a stored material and labor split; hard rules 7 and 8 in `AGENTS.md` are not in `docs/method.md`, which `AGENTS.md` says wins; seven kit scripts have no tests, including `kit/redaction.py`; the name check in the format module's save is skipped silently when no names are passed.
- The list of real names to remove (client, vendor and sub names) exists nowhere now. It must be rebuilt from the builder's two workbooks, and kept outside this repository, before Job A can be imported or drafted again with names removed.
- Review findings not yet answered: every item in `docs/history/2026-11-19-full-review.md` is fixed, turned into a decision or a question for the builder, or parked with a reason.
- `docs/standards.md`: a line for the rough clickable step (decision 0011); one set of reviewer roles (it and `docs/reviewers.md` differ).
- `docs/format.md`: write version 0.5 as one clean specification before it is built.
- Decision 0001 still says "as he types"; decision 0008 is the current wording.
- Standing choices the backfill did not turn into decision files, because they already live as rules in `docs/method.md`: the five changes locked after the first blind draft (his usual line as a one-job note, overlapping lines as one question, "plan minimum" on calculated lumber and trim). Say if they should have files too.
- `docs/screens/laptop-screens-design.md` is behind decisions 0002 to 0008; it is brought into line when the screens are next drawn (after decisions 0010 and 0011).
- `docs/builder/questions.md`: questions 18 and 19 are out of date (Excel output, colored cells) and wait on the owner's rewording; questions from the full review (what he sends a client today, allowances, alternates) are not added yet.
