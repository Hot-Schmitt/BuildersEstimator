#!/usr/bin/env python3
"""Read the spec/ folder into one list of records.

The one reader of spec/. Both tools/check_spec.py (which looks for breaks) and
tools/build_spec_index.py (which writes spec/INDEX.md and spec/OPEN.md) call
load() here, so the two can never disagree about what the folder holds.

What lives where, and the id scheme, are set out in spec/README.md.

Needs PyYAML (pip install pyyaml). It is the one dependency of the housekeeping
tools; tools/build_index.py still needs none.
"""

from pathlib import Path
import re
import sys

import build_index

try:
    import yaml
except ImportError:  # say what to do rather than show a traceback
    sys.exit("The spec tools need PyYAML. Run:  pip install pyyaml")

REPO = Path(__file__).resolve().parent.parent

# One pattern per kind of id. Order matters only for reading: longer prefixes first.
# A control id needs at least two parts after "C-" (C-top-finalize), so an ordinary
# word such as "C-channel" is not read as an id.
ID_PATTERNS = {
    "ACT": r"ACT-\d{2}",
    "AC": r"AC-[A-Z]+-\d{2}",
    "US": r"US-\d{3}",
    "FT": r"FT-[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*",
    "ST": r"ST-[A-Z]+(?:-[A-Z0-9]+)+",
    "A": r"A-[A-Z]+(?:-[A-Z0-9]+)+",
    "F": r"F-[A-Z]+(?:-[A-Z0-9]+)+",
    "R": r"R-[A-Z]+-\d{3}",
    "O": r"O-[A-Z]+",
    "S": r"S-[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*",
    "C": r"C-[a-z0-9]+(?:-(?:[a-z0-9]+|\([a-z0-9]+\)))+",
    "E": r"E-\d{3}",
    "W": r"W-[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*",
    "D": r"D-\d{4}",
    "Q": r"Q-\d+",
}
ANY_ID = re.compile(
    r"(?<![A-Za-z0-9-])(?:"
    + "|".join(f"(?P<{kind}>{pattern})" for kind, pattern in ID_PATTERNS.items())
    + r")(?![A-Za-z0-9])"
)

# The order kinds are listed in the index.
KIND_ORDER = ["ACT", "US", "O", "ST", "A", "F", "R", "S", "C", "AC", "E", "W", "FT"]
KIND_NAMES = {
    "ACT": "Activities", "US": "Stories", "O": "Objects", "ST": "States",
    "A": "Actions", "F": "Fields", "R": "Rules", "S": "Screens, dialogs and panels",
    "C": "Controls", "AC": "Acceptance cases", "E": "Edge cases", "W": "Wording",
    "FT": "Feature build notes",
}

STATUS_WORDS = {"open", "proposed", "locked", "parked", "retired"}
FEATURE_STATUS_WORDS = {"options", "decided", "parked"}
WAITING = {"open", "proposed", "options"}   # not yet decided; these fill spec/OPEN.md
# The areas a rule can belong to: the middle part of R-<area>-NNN. spec/README.md says
# what each stands for.
RULE_AREAS = {"SAVE", "FIN", "TAX", "MKP", "CTG", "PRC", "VSP", "SCP", "QTY", "CONF",
              "VER", "TPL", "CLI", "PRIV"}
PROVENANCE_WORDS = {"said", "checked", "inferred", "proposed"}
SLICE_WORDS = {"skeleton", "first", "later", "not-doing"}

FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
ACCEPTANCE_LINE = re.compile(r"^\s*[-*]\s+\*\*(" + ID_PATTERNS["AC"] + r")\*\*(.*)$")
CONTROL_HEADING = re.compile(r"^#{2,4}\s+(" + ID_PATTERNS["C"] + r")\s*$")
# What a controls table may say under "Reads / writes": nothing, or parts that each
# open with one of these two words, split by ";".
READS_WRITES_PART = re.compile(r"^(reads|writes)\b", re.I)


def kind_of(an_id):
    """Return the kind code of an id ("F" for F-LI-UNIT-PRICE), or None."""
    match = ANY_ID.fullmatch(an_id)
    return match.lastgroup if match else None


def ids_in(value):
    """Every id cited anywhere inside a string, list or dict."""
    if isinstance(value, dict):
        found = set()
        for item in value.values():
            found |= ids_in(item)
        return found
    if isinstance(value, (list, tuple, set)):
        found = set()
        for item in value:
            found |= ids_in(item)
        return found
    return {m.group(0) for m in ANY_ID.finditer(str(value))} if value is not None else set()


def as_list(value):
    """A YAML value that should be a list, as a list of strings."""
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def short(text, limit=90):
    text = " ".join(str(text or "").split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


class Spec:
    """Everything read from spec/, plus the decisions and questions it may cite."""

    def __init__(self, repo):
        self.repo = Path(repo)
        self.root = self.repo / "spec"
        self.records = []        # every defined id: dict(id, kind, title, status, file, cites, ...)
        self.problems = []       # files or records that could not be read as intended
        self.decisions = {}      # "0050" -> dict(status, affects, file)
        self.questions = set()   # question numbers in docs/builder/questions.md, as strings

    def add(self, kind, an_id, title, status, file, cites=(), **extra):
        """Record one defined id. An id of the wrong kind or shape is reported, not kept."""
        an_id = str(an_id).strip()
        if kind_of(an_id) != kind:
            self.problems.append(f"{file}: {an_id!r} is not a {kind}- id, so it does not "
                                 "belong here (or is not written as an id)")
            return None
        record = {
            "id": an_id, "kind": kind, "title": short(title), "status": str(status or ""),
            "file": file, "cites": set(cites) - {an_id},
        }
        record.update(extra)
        self.records.append(record)
        return record

    def rel(self, path):
        return path.relative_to(self.repo).as_posix()


# --- reading the pieces -------------------------------------------------------

class StrictLoader(yaml.SafeLoader):
    """A YAML loader that refuses a key written twice in one record. Without it the
    second value quietly wins, and a missing "- " before "id:" merges two records."""


def _strict_mapping(loader, node, deep=False):
    seen = set()
    for key_node, _ in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in seen:
            raise yaml.YAMLError(f"the key {key!r} is written twice in one record "
                                 f"(line {key_node.start_mark.line + 1})")
        seen.add(key)
    return yaml.SafeLoader.construct_mapping(loader, node, deep)


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _strict_mapping)


def read_text(spec, path):
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        spec.problems.append(f"{spec.rel(path)}: not readable as UTF-8 text")
        return None


def parse_yaml(spec, path, text):
    try:
        return yaml.load(text, Loader=StrictLoader)
    except yaml.YAMLError as error:
        spec.problems.append(f"{spec.rel(path)}: not readable as YAML ({short(error, 160)})")
        return None


def read_yaml(spec, path):
    text = read_text(spec, path)
    return None if text is None else parse_yaml(spec, path, text)


def record_list(spec, path, data):
    """Check a data file is a flat list of records that each start with id."""
    if data is None:
        return []
    if not isinstance(data, list):
        spec.problems.append(f"{spec.rel(path)}: must be a flat list of records")
        return []
    good = []
    for position, item in enumerate(data, 1):
        if not isinstance(item, dict) or not item.get("id"):
            spec.problems.append(f"{spec.rel(path)}: record {position} has no id")
        else:
            good.append(item)
    return good


def split_markdown(spec, path):
    """Return (frontmatter dict, body text) of a Markdown spec file."""
    text = read_text(spec, path)
    if text is None:
        return None, ""
    match = FRONTMATTER.match(text)
    if not match:
        spec.problems.append(f"{spec.rel(path)}: no frontmatter block")
        return None, text
    front = parse_yaml(spec, path, match.group(1))
    if front is None:
        return None, text
    if not isinstance(front, dict) or not front.get("id"):
        spec.problems.append(f"{spec.rel(path)}: frontmatter has no id")
        return None, text
    return front, text[match.end():]


def tables(body):
    """Every Markdown table in a text, as (header cells, list of row dicts)."""
    found, block = [], []
    for line in body.splitlines() + [""]:
        if line.strip().startswith("|"):
            block.append(line.strip())
            continue
        if len(block) >= 2 and re.fullmatch(r"[|\s:-]+", block[1]):
            header = [cell.strip() for cell in block[0].strip("|").split("|")]
            rows = []
            for row in block[2:]:
                cells = [cell.strip() for cell in row.strip("|").split("|")]
                cells += [""] * (len(header) - len(cells))
                rows.append(dict(zip(header, cells)))
            found.append((header, rows))
        block = []
    return found


def filled(rows):
    """Table rows that have anything in them."""
    return [row for row in rows if any(cell for cell in row.values())]


def column(row, *starts):
    """The cell whose column name starts with one of the given words (any case)."""
    for name, cell in row.items():
        lowered = name.lower()
        if any(lowered.startswith(start) for start in starts):
            return cell
    return ""


def load_stories(spec):
    path = spec.root / "stories.yaml"
    if not path.is_file():
        return
    data = read_yaml(spec, path)
    if data is None:
        return
    if not isinstance(data, dict):
        spec.problems.append(f"{spec.rel(path)}: must hold jobs, activities and stories")
        return
    file = spec.rel(path)
    for item in record_list(spec, path, data.get("activities") or []):
        spec.add("ACT", item["id"], item.get("name"), "", file)
    for item in record_list(spec, path, data.get("stories") or []):
        spec.add("US", item["id"], item.get("story"), item.get("status"), file, ids_in(item),
                 slice=str(item.get("slice") or ""), decisions=as_list(item.get("decisions")),
                 provenance=item.get("provenance"))


def load_data_files(spec):
    """wording.yaml, edge-cases.yaml, fields/*.yaml and rules/*.yaml."""
    sources = [("W", spec.root / "wording.yaml"), ("E", spec.root / "edge-cases.yaml")]
    sources += [("F", p) for p in sorted((spec.root / "fields").glob("*.yaml"))]
    sources += [("R", p) for p in sorted((spec.root / "rules").glob("*.yaml"))]
    title_key = {"W": "on_screen", "E": "situation", "F": "note", "R": "rule"}
    for kind, path in sources:
        if not path.is_file():
            continue
        file = spec.rel(path)
        for item in record_list(spec, path, read_yaml(spec, path)):
            record = spec.add(kind, item["id"], item.get(title_key[kind]), item.get("status"),
                              file, ids_in(item), decisions=as_list(item.get("decisions")),
                              provenance=item.get("provenance"))
            if record is None:
                continue
            if kind == "F":
                record["shown_on"] = set(as_list(item.get("shown_on")))
                record["open_note"] = str(item.get("open") or "")
            if kind == "R":
                record["acceptance"] = as_list(item.get("acceptance"))
                # A rule with no screen of its own may define its acceptance cases here.
                # A case defined here counts as one of the rule's acceptance cases.
                cases = item.get("cases") or []
                if not isinstance(cases, list):
                    spec.problems.append(f"{file}: {record['id']} cases must be a list")
                    cases = []
                for case in cases:
                    if not isinstance(case, dict) or not case.get("id"):
                        spec.problems.append(f"{file}: {record['id']} has a case with no id")
                        continue
                    made = spec.add("AC", case["id"], case.get("case"), item.get("status"),
                                    file, ids_in(case), owner=None, parent=record["id"])
                    if made and made["id"] not in record["acceptance"]:
                        record["acceptance"].append(made["id"])


def load_objects(spec):
    for path in sorted((spec.root / "objects").glob("*.md")):
        front, body = split_markdown(spec, path)
        if front is None:
            continue
        file, status = spec.rel(path), front.get("status")
        parent = spec.add("O", front["id"], front.get("name"), status, file,
                          ids_in(front) | ids_in(body), decisions=as_list(front.get("decisions")))
        if parent is None:
            continue
        for header, rows in tables(body):
            names = [name.lower() for name in header]
            if any(name.startswith("home control") for name in names):
                for row in filled(rows):
                    spec.add("A", column(row, "id"), column(row, "action"),
                             column(row, "status") or status, file, ids_in(row),
                             home=column(row, "home control"), parent=parent["id"])
            elif any(name.startswith("state id") for name in names):
                for row in filled(rows):
                    spec.add("ST", column(row, "state id"), column(row, "name on screen"),
                             status, file, ids_in(row), parent=parent["id"])


def load_screens(spec):
    for path in sorted((spec.root / "screens").glob("*.md")):
        front, body = split_markdown(spec, path)
        if front is None:
            continue
        file, status = spec.rel(path), front.get("status")
        parent = spec.add("S", front["id"], front.get("name"), status, file,
                          ids_in(front) | ids_in(body), decisions=as_list(front.get("decisions")))
        if parent is None:
            continue
        if path.stem != parent["id"]:
            spec.problems.append(f"{file}: holds {parent['id']}, so the file must be "
                                 f"named {parent['id']}.md")
        for header, rows in tables(body):
            if not any(name.lower().startswith("reads") for name in header):
                continue  # only the controls table has a "Reads / writes" column
            for row in filled(rows):
                control_id = column(row, "id")
                reads_writes = column(row, "reads")
                parts = [part.strip() for part in reads_writes.split(";") if part.strip()]
                if reads_writes.strip().lower() in ("", "none", "—", "-"):
                    parts = []
                elif not all(READS_WRITES_PART.match(part) for part in parts):
                    spec.problems.append(
                        f"{file}: {control_id} has {reads_writes!r} under Reads / writes; "
                        'leave it blank, or open each part with "reads" or "writes" '
                        '(split parts with ";")')
                # "Does", not "Does NOT do": the first is what the control runs.
                does = next((cell for name, cell in row.items()
                             if name.lower().startswith("does")
                             and not name.lower().startswith("does not")), "")
                spec.add("C", control_id, column(row, "label"), status, file, ids_in(row),
                         fields={i for i in ids_in(reads_writes) if kind_of(i) == "F"},
                         changes_data=any(part.lower().startswith("writes") for part in parts)
                         or any(kind_of(i) == "A" for i in ids_in(does)),
                         parent=parent["id"])
        owner = None
        for line in body.splitlines():
            heading = CONTROL_HEADING.match(line)
            if heading:
                owner = heading.group(1)
            elif line.startswith("#"):
                owner = None
            case = ACCEPTANCE_LINE.match(line)
            if case:
                spec.add("AC", case.group(1), case.group(2), status, file, ids_in(line),
                         owner=owner, parent=parent["id"])


def load_features(spec):
    for path in sorted((spec.root / "features").glob("*.md")):
        front, body = split_markdown(spec, path)
        if front is None:
            continue
        decided_in = str(front.get("decided_in") or "")
        record = spec.add("FT", front["id"], front.get("title"), front.get("status"),
                          spec.rel(path), ids_in(front) | ids_in(body),
                          decisions=[decided_in] if decided_in else [])
        if record and path.stem != record["id"]:
            spec.problems.append(f"{spec.rel(path)}: holds {record['id']}, so the file must "
                                 f"be named {record['id']}.md")


def load_decisions(spec):
    """The frontmatter of each decision file: its status and its optional affects line."""
    for path in sorted((spec.repo / "decisions").glob("[0-9][0-9][0-9][0-9]-*.md")):
        if path.name.startswith("0000-"):
            continue
        fields, error = build_index.parse_file(path)   # the one reader of decision files
        if error:
            spec.problems.append(f"decisions/{path.name}: {error}")
            continue
        spec.decisions[path.name[:4]] = {
            "status": fields.get("status", ""),
            "affects": ids_in(fields["affects"]) if fields.get("affects") else None,
            "file": f"decisions/{path.name}",
        }


def load_questions(spec):
    path = spec.repo / "docs" / "builder" / "questions.md"
    if path.is_file():
        spec.questions = set(re.findall(r"^(\d+)\.\s", path.read_text(encoding="utf-8"), re.M))


def report_unread(spec):
    """A file in a folder the loaders read, that no loader matched, would be ignored
    silently (a .yml ending, a file one folder too deep). Report each one."""
    expected = {"fields": ".yaml", "rules": ".yaml", "objects": ".md", "screens": ".md",
                "features": ".md"}
    for folder, ending in expected.items():
        for path in sorted((spec.root / folder).rglob("*")):
            if not path.is_file() or (folder == "screens" and "source" in path.parts):
                continue  # screens/source/ holds locked drawing code, not spec files
            if path.parent != spec.root / folder or path.suffix != ending:
                spec.problems.append(f"{spec.rel(path)}: not read; files here must be "
                                     f"directly in spec/{folder}/ and end in {ending}")


def load(repo=REPO):
    """Read everything. spec/templates, the generated pages and the README are not read."""
    spec = Spec(repo)
    load_decisions(spec)
    load_questions(spec)
    if spec.root.is_dir():
        load_stories(spec)
        load_data_files(spec)
        load_objects(spec)
        load_screens(spec)
        load_features(spec)
        report_unread(spec)
    return spec
