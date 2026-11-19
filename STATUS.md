# Where we are and what is next

**Purpose:** the one page that says what stage the project is at, what is next, what is waiting on the owner and what the agent owes. Written by hand; update it whenever any of those change. Decisions themselves live in `decisions/` and are listed in `CURRENT.md`.

**Last updated:** Nov 19, 2026.

## Stage
The project is moving from a claude.ai Project into this repository. Nothing of the screens is built. One job (Job A) has been tested; it is no longer blind.

## Done
- The method, standards and format documents are in `docs/`.
- Twelve decisions are recorded.
- A full review by five fresh reviewers was run on Nov 19 (`docs/history/2026-11-19-full-review.md`).

## Next, in order
1. Bring the older standing decisions (roughly 40, held in the project's "17 Current state" document) into `decisions/`. Until this is done, `CURRENT.md` is **not** the full list.
2. Move the rest: the scripts and their tests into `kit/` and `tests/`, the questions for the builder into `docs/builder/`, the cost code list, the screen design document and canvas code into `docs/screens/`, and the old working log into `docs/history/`.
3. Design the back half of the estimate (decision 0010), then a rough clickable version (decision 0011).
4. Technical setup: bring options to the owner (how a plan read reaches the screen, the stack, where data lives, saving and undo).
5. More blind tests before the builder relies on it.

## Waiting on the owner
- Nothing right now.

## Owed by the agent
- Review findings not yet answered: every item in `docs/history/2026-11-19-full-review.md` is fixed, turned into a decision or a question for the builder, or parked with a reason.
- `docs/standards.md`: a line for the rough clickable step (decision 0011); one set of reviewer roles (it and `docs/reviewers.md` differ).
- `docs/format.md`: write version 0.5 as one clean specification before it is built.
- Decision 0001 still says "as he types"; decision 0008 is the current wording.
- Files `AGENTS.md` names that do not exist yet: `docs/builder/questions.md`, `docs/history/mistakes.md`, `kit/redaction.py`.
