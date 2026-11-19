# Mistakes and what changed because of them

**Purpose:** one row per mistake the agent makes, found by the owner, a reviewer or a test: what happened, why, the fix, and whether a rule should change. The same kind of mistake twice means a rule must change (`AGENTS.md`, "Mistakes").
**Older mistakes** (Nov 16 to 18, 2026) are in the old working log, section 8 of each part, which has not been moved into this repository yet. The ones that changed a rule are recorded as decisions 0038, 0039, 0042, 0052, 0058, 0059, 0061 and 0063 to 0066.

| Date | What happened | Why | Fix | Rule change proposed / approved |
|---|---|---|---|---|
| Nov 19, 2026 | The workspace restarted just after three researchers were started. The agent assumed they were lost and started all three again. They had survived, so six ran for a few minutes before the three extras were stopped. Usage was wasted; the amount was not measured | The restart notice said running commands had ended, and their report folder was missing; the agent did not check whether the agents themselves were still running. The reports were also being written to a temporary folder | The extras were stopped when the first report arrived. Reports now go to a folder that survives a restart, and are saved early | **Proposed:** after a restart, check whether a task is still running before starting it again; a researcher saves its report early, outside temporary folders |
| Nov 19, 2026 | Running the tests changed four cache files that are tracked in the repository, and they were committed with the decision backfill, then restored in a second commit | The cache files were tracked despite `.gitignore`; the agent used "add everything" | The cache files are no longer tracked | None: one-off, cause removed |
