# Where we are and what is next

**Purpose:** the one page that says what stage the project is at, what is next, what is waiting on the owner and what the agent owes. Written by hand; update it whenever any of those change. Decisions themselves live in `decisions/` and are listed in `CURRENT.md`.

**Last updated:** Nov 19, 2026.

## Stage
The project is moving from a claude.ai Project into this repository. Nothing of the screens is built. One job (Job A) has been tested; it is no longer blind.

## Done
- The method, standards and format documents are in `docs/`.
- Twelve decisions are recorded.
- All eleven scripts are in `kit/`, with the cost code list and the Job A cost code rows. They were re-created from the project copies on Nov 19 (the owner holds no other copy) and checked by running them: both test scripts pass (4,275 damaged files tried, as recorded on Nov 16); the importer reproduces his sheet to the cent (471 lines, cost 231,247.05, total 289,058.81); the budget by cost code matches his cost workbook; the document maker's own checks pass; and the Job A remake reproduces the recorded scope and score figures.
- A full review by five fresh reviewers was run on Nov 19 (`docs/history/2026-11-19-full-review.md`).

## Next, in order
1. Bring the older standing decisions (roughly 40, held in the project's "17 Current state" document) into `decisions/`. Until this is done, `CURRENT.md` is **not** the full list.
2. Move the rest: the questions for the builder into `docs/builder/`, the cost code list document, the screen design document and canvas code into `docs/screens/`, and the old working log into `docs/history/`. The large Job A data files (the draft and the blind draft) stay in the project for now; the scripts can rebuild the draft.
3. Design the back half of the estimate (decision 0010), then a rough clickable version (decision 0011).
4. Technical setup: bring options to the owner (how a plan read reaches the screen, the stack, where data lives, saving and undo).
5. More blind tests before the builder relies on it.

## Waiting on the owner
- Nothing right now.

## Owed by the agent
- The list of real names to remove (client, vendor and sub names) exists nowhere now. It must be rebuilt from the builder's two workbooks, and kept outside this repository, before Job A can be imported or drafted again with names removed.
- Review findings not yet answered: every item in `docs/history/2026-11-19-full-review.md` is fixed, turned into a decision or a question for the builder, or parked with a reason.
- `docs/standards.md`: a line for the rough clickable step (decision 0011); one set of reviewer roles (it and `docs/reviewers.md` differ).
- `docs/format.md`: write version 0.5 as one clean specification before it is built.
- Decision 0001 still says "as he types"; decision 0008 is the current wording.
- Files `AGENTS.md` names that do not exist yet: `docs/builder/questions.md`, `docs/history/mistakes.md`.
