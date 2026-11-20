# Where we are and what is next

**Purpose:** the one page that says what stage the project is at, what is next, what is waiting on the owner and what the agent owes. Written by hand; update it whenever any of those change. Decisions themselves live in `decisions/` and are listed in `CURRENT.md`.

**Last updated:** Nov 20, 2026.

## Stage
The project is moving from a claude.ai Project into this repository. Nothing of the screens is built. One job (Job A) has been tested; it is no longer blind.

## Done
- The method, standards and format documents are in `docs/`.
- 72 decisions are recorded: 66 standing, 1 proposed, 5 superseded. The older decisions held in the project's "17 Current state" document were brought in on Nov 19 (0013 to 0066), each checked against the old working log for its date and the owner's words. `CURRENT.md` is now the full list.
- All eleven scripts are in `kit/`, with the cost code list and the Job A cost code rows. They were re-created from the project copies on Nov 19 (the owner holds no other copy) and checked by running them: both test scripts pass (4,275 damaged files tried, as recorded on Nov 16); the importer reproduces his sheet to the cent (471 lines, cost 231,247.05, total 289,058.81); the budget by cost code matches his cost workbook; the document maker's own checks pass; and the Job A remake reproduces the recorded scope and score figures.
- First pass of moving the documents, Nov 19: the questions for the builder are in `docs/builder/questions.md` (ten owed questions added, 39 to 48), and the screen design document is in `docs/screens/laptop-screens-design.md` (moved as it was; the lines that are behind the decisions are listed at its top). The canvas drawings were not copied: `docs/screens/canvas.md` points to them and says why (Decided by Claude; reversible).
- A method audit by three fresh researchers was run on Nov 19 at the owner's request (`docs/history/2026-11-19-method-audit/`): a cold audit of this repository, method and documentation structure, and market research on estimating software. Findings are not decisions.
- A full review by five fresh reviewers was run on Nov 19 (`docs/history/2026-11-19-full-review.md`).
- The `spec/` folder is set up and empty (Nov 20): the id scheme and how to use it in `spec/README.md`, a blank of each kind in `spec/templates/`, an index builder and a checker in `tools/`. Decided by Claude, reversible: the data files are YAML, which adds one dependency (PyYAML) for these two tools only; and a missing acceptance case or an open item fails the check only on something locked, or with `--gate`, so the folder can be checked while phases 1 to 4 fill it. A fresh engineering reviewer checked the tools on Nov 20; its four High and nine smaller findings are fixed (`docs/history/mistakes.md`). Known limits, accepted: a capitalised trade term shaped like an id is read as one and fails loudly; a rule filed in the wrong area's file is not caught; a control counts as covered when any acceptance case names it.

## Next, in order
The owner approved the phase path on Nov 19 (decision 0067). Phases 0 to 6 are set out in that decision.

**Now: phase 0, close the records.**
1. Fix the contradictions and dangling references listed in `docs/history/2026-11-19-method-audit/repository-audit.md` (two instruction sets, rules repeated with different wording, "doc NN" pointers, `README.md` describing folders that are empty). *Done on Nov 19 for the documents. What is left is listed under "Owed by the agent" and "Waiting on the owner".*
2. Put the five proposed decisions (0061, 0063 to 0066) and decision 0026 to the owner in one short batch. *Done on Nov 19: all five approved, 0065 for drawings only. Decision 0026 was replaced by 0072.*
3. Create the empty `spec/` folder, its templates and its checking script, from `method-and-structure.md`, section 3. *Done on Nov 20: `spec/README.md`, eight blank templates, `tools/check_spec.py` and `tools/build_spec_index.py`, with tests. Both run clean on the empty folder.*
4. Give every finding in the two review documents one status: fixed, a decision, a question, or parked with a reason. *Done on Nov 20: `docs/history/review-findings.md`, 140 findings (42 fixed, 15 decided, 5 turned into questions for the builder, 74 parked with the phase that owns each, 4 for the owner).*
5. **Next.** Sort `docs/builder/questions.md` (54 questions) into: the owner can answer (general trade practice); only the builder can answer and it blocks design; can wait. Bring the short blocking list to the owner (decision 0069).

**Then phase 1, map and name:** the story map, the objects and their states, and how "who figures each quantity" is shown (decision 0070). When the work reaches that step: decide decision 0071 (reliable counts filled in from day one), with a timed feasibility test designed and run before anything is built.

**Still open from the move:** the cost code list document and the old working log (five parts) are not in the repository yet. Not needed for phases 0 to 2.

## Waiting on the owner
- **The repository is public on GitHub.** `README.md` and decision 0057 say it is private, and it holds the builder's cost figures (decision 0012). Found on Nov 19. The owner makes it private in the repository's settings, or says it should stay public.
- The claude.ai project's instructions still tell a chat to start from the old documents. The owner replaces them with a short pointer to this repository (text given to him on Nov 19).
- Two small calls from the review findings (`docs/history/review-findings.md`): whether running a paid service on a personal Claude subscription is allowed, which is the owner's to check against his own agreement (FR-5.6b); and, only if the repository stays public, the city, the canvas link and the name and email on commits (RA-8n).
- Decision 0071 is proposed and waits for phase 1 and a timed test; it does not need an answer now.

## Owed by the agent
- From the method audit: nothing decides what happens when he types into the one price box (decision 0005) on a line item with a stored material and labor split; seven kit scripts have no tests, including `kit/redaction.py`; the name check in the format module's save is skipped silently when no names are passed.
- The list of real names to remove (client, vendor and sub names) exists nowhere now. It must be rebuilt from the builder's two workbooks, and kept outside this repository, before Job A can be imported or drafted again with names removed.
- Parked review findings: `docs/history/review-findings.md` names the phase that owns each. When a phase starts, read its parked rows first; when one is dealt with, change its status there.
- The code tidy that many parked findings wait on (tests for seven kit scripts, Job A files out of `kit/`, the builder profile file, one name check used by every writer, a package layout): done before phase 4 picks the technical base.
- `docs/format.md`: write version 0.5 as one clean specification before it is built.
- Standing choices the backfill did not turn into decision files, because they already live as rules in `docs/method.md`: the five changes locked after the first blind draft (his usual line as a one-job note, overlapping lines as one question, "plan minimum" on calculated lumber and trim). Say if they should have files too.
- `docs/screens/laptop-screens-design.md` is behind decisions 0002 to 0008; it is brought into line when the screens are next drawn (after decisions 0010 and 0011).
- `docs/builder/questions.md`: questions 18 and 19 are out of date (Excel output, colored cells) and wait on the owner's rewording; questions from the full review were added on Nov 20 (49 to 54).
- Parked by decision 0072: comparing the tool's own counts with vendors' quantities, once the tool has collected both and its counts are tested (decision 0071).
- Left from the records clean-up (phase 0, step 1): comments and generated text in seven kit scripts still cite project document numbers (fixed with the code tidy-up the audit lists, not before); `docs/format.md` keeps its version 0.4 body until 0.5 is written; history citations such as "doc 07 part 4" stay as evidence until the old working log is moved in; `docs/screens/canvas.md` still says the design document was written from an older canvas version.
- Two checks of `tools/check_spec.py` wait for their phase: control ids in a locked drawing's code against the controls table (phase 5), and acceptance ids against test names (the build).
- `docs/format.md` says estimate files are stored compressed; the format module writes plain JSON. Settle when 0.5 is written.
