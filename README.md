# Builders Estimator

An estimating helper for a luxury home builder in Atlanta. It reads a job's plans and drafts most of his estimate, with his own line items and his own prices, and tells him which numbers it is least sure about.

This repository holds the code, the decisions behind it, and the test results. It is private.

## Where things are

| Folder | What's in it |
|---|---|
| `CURRENT.md` | Every decision that stands right now. Generated — don't edit it by hand. |
| `decisions/` | One file per decision, numbered. Nothing here is ever deleted; a replaced decision is marked superseded and points at what replaced it. |
| `docs/` | How an estimate is made (`method.md`), the shared data format (`format.md`), build and design standards (`standards.md`), screen designs (`screens/`), what we know and still need from the builder (`builder/`). |
| `docs/history/` | The old working log, kept as history, and the record of mistakes. |
| `jobs/` | Per-job facts, costs and test scores. Redacted. Job A, Job B and so on. |
| `kit/` | The scripts: the estimate format and its check, the draft writer, the importer, scoring. |
| `tests/` | Tests for the kit. They run on made-up data, never real jobs. |
| `tools/` | Housekeeping scripts, including the one that builds `CURRENT.md`. |
| `AGENTS.md` | Instructions for AI agents working in here. |

## Reading a decision

Each file in `decisions/` opens with its number, title, status, date, and the area it belongs to, then four short sections: what was decided, why, what we considered instead, and what it costs us. Where the owner said something in his own words, those words are quoted. The filename tells you the subject.

To see only what's current, read `CURRENT.md`. To find out why something is the way it is, search `decisions/`.

## Regenerating the index

```
python3 tools/build_index.py
```

## Privacy

The builder's cost figures and his line wording are in here. Client names, addresses, phone numbers, banking details and vendor or subcontractor names are not, and the original stamped plan sets are not. Jobs are named Job A, Job B and so on.
