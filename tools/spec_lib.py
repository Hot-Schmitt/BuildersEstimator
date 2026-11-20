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
    "C": r"C-[a-z0-9]+(?:-[a-z0-9()]+)+",
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
PROVENANCE_WORDS = {"said", "checked", "inferred", "proposed"}
SLICE_WORDS = {"skeleton", "first", "later", "not-doing"}

FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
ACCEPTANCE_LINE = re.compile(r"^\s*[-*]\s+\*\*(AC-[A-Z]+-\d{2})\*\*(.*)$")
CONTROL_HEADING = re.compile(r"^#{2,4}\s+(C-[a-z0-9()-]+)\s*$")


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

    def add(self, an_id, title, status, file, cites=(), **extra):
        record = {
            "id": str(an_id), "kind": kind_of(str(an_id)), "title": short(title),
            "status": str(status or ""), "file": file, "cites": set(cites) - {str(an_id)},
        }
        record.update(extra)
        self.records.append(record)
        return record

    def by_id(self):
        return {record["id"]: record for record in self.records}

    def rel(self, path):
        return path.relative_to(self.repo).as_posix()


# --- reading the pieces -------------------------------------------------------

def read_yaml(spec, path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as error:
        spec.problems.append(f"{spec.rel(path)}: not readable as YAML ({short(error, 120)})")
        return None


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
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        spec.problems.append(f"{spec.rel(path)}: no frontmatter block")
        return None, text
    try:
        front = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as error:
        spec.problems.append(f"{spec.rel(path)}: frontmatter not readable ({short(error, 120)})")
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
        spec.add(item["id"], item.get("name"), "", file)
    for item in record_list(spec, path, data.get("stories") or []):
        spec.add(item["id"], item.get("story"), item.get("status"), file, ids_in(item),
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
            if kind_of(str(item["id"])) != kind:
                spec.problems.append(f"{file}: {item['id']} is not a {kind}- id, so it does not belong here")
                continue
            record = spec.add(item["id"], item.get(title_key[kind]), item.get("status"), file,
                              ids_in(item), decisions=as_list(item.get("decisions")),
                              provenance=item.get("provenance"))
            if kind == "F":
                record["shown_on"] = set(as_list(item.get("shown_on")))
                record["open_note"] = str(item.get("open") or "")
            if kind == "R":
                record["acceptance"] = as_list(item.get("acceptance"))
                # A rule with no screen of its own may define its acceptance cases here.
                for case in item.get("cases") or []:
                    if isinstance(case, dict) and case.get("id"):
                        spec.add(case["id"], case.get("case"), item.get("status"), file,
                                 ids_in(case), owner=None)


def load_objects(spec):
    for path in sorted((spec.root / "objects").glob("*.md")):
        front, body = split_markdown(spec, path)
        if front is None:
            continue
        file, status = spec.rel(path), front.get("status")
        spec.add(front["id"], front.get("name"), status, file, ids_in(front) | ids_in(body),
                 decisions=as_list(front.get("decisions")))
        for header, rows in tables(body):
            names = [name.lower() for name in header]
            if any(name.startswith("home control") for name in names):
                for row in rows:
                    action_id = column(row, "id")
                    if kind_of(action_id) != "A":
                        continue
                    spec.add(action_id, column(row, "action"), column(row, "status") or status,
                             file, ids_in(row), home=column(row, "home control"))
            elif any(name.startswith("state id") for name in names):
                for row in rows:
                    state_id = column(row, "state id")
                    if kind_of(state_id) == "ST":
                        spec.add(state_id, column(row, "name on screen"), status, file, ids_in(row))


def load_screens(spec):
    for path in sorted((spec.root / "screens").glob("*.md")):
        front, body = split_markdown(spec, path)
        if front is None:
            continue
        file, status = spec.rel(path), front.get("status")
        spec.add(front["id"], front.get("name"), status, file, ids_in(front) | ids_in(body),
                 decisions=as_list(front.get("decisions")))
        for header, rows in tables(body):
            if not any(name.lower().startswith("reads") for name in header):
                continue  # only the controls table has a "Reads / writes" column
            for row in rows:
                control_id = column(row, "id")
                if kind_of(control_id) != "C":
                    continue
                reads_writes = column(row, "reads")
                # "Does", not "Does NOT do": the first is what the control runs.
                does = next((cell for name, cell in row.items()
                             if name.lower().startswith("does")
                             and not name.lower().startswith("does not")), "")
                spec.add(control_id, column(row, "label"), status, file, ids_in(row),
                         fields={i for i in ids_in(reads_writes) if kind_of(i) == "F"},
                         changes_data=bool(re.search(r"\bwrites\b", reads_writes, re.I))
                         or any(kind_of(i) == "A" for i in ids_in(does)))
        owner = None
        for line in body.splitlines():
            heading = CONTROL_HEADING.match(line)
            if heading:
                owner = heading.group(1)
            elif line.startswith("#"):
                owner = None
            case = ACCEPTANCE_LINE.match(line)
            if case:
                spec.add(case.group(1), case.group(2), status, file, ids_in(line), owner=owner)


def load_features(spec):
    for path in sorted((spec.root / "features").glob("*.md")):
        front, body = split_markdown(spec, path)
        if front is None:
            continue
        decided_in = str(front.get("decided_in") or "")
        spec.add(front["id"], front.get("title"), front.get("status"), spec.rel(path),
                 ids_in(front) | ids_in(body), decisions=[decided_in] if decided_in else [])


def load_decisions(spec):
    """The frontmatter of each decision file: its status and its optional affects line."""
    for path in sorted((spec.repo / "decisions").glob("[0-9][0-9][0-9][0-9]-*.md")):
        if path.name.startswith("0000-"):
            continue
        match = FRONTMATTER.match(path.read_text(encoding="utf-8"))
        fields = {}
        for line in (match.group(1).splitlines() if match else []):
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
        spec.decisions[path.name[:4]] = {
            "status": fields.get("status", ""),
            "affects": ids_in(fields["affects"]) if fields.get("affects") else None,
            "file": f"decisions/{path.name}",
        }


def load_questions(spec):
    path = spec.repo / "docs" / "builder" / "questions.md"
    if path.is_file():
        spec.questions = set(re.findall(r"^(\d+)\.\s", path.read_text(encoding="utf-8"), re.M))


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
    return spec
