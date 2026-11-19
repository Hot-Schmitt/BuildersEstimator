"""
The one redaction step, shared by every script that reads the builder's files.

Names of clients, vendors and subs are replaced from a name list kept with the
job's data on the user's computer: {"name": "replacement", ...}. The list is real
data and never goes into code or project documents. Product brands are not on the
list: a brand is part of the spec (decided by the user, Nov 16, 2026).

Redaction happens once, where his wording is first read. Every later write is
guarded by estimate_format.save(), which refuses a file in which a listed name survives.
"""
import json
import re


def load(path):
    """Read a name list. An empty or malformed list is refused, so nothing is written unredacted by accident."""
    names = json.load(open(path))
    if not (isinstance(names, dict) and names and all(isinstance(k, str) and k.strip() and isinstance(v, str)
                                                      for k, v in names.items())):
        raise SystemExit(f"{path}: the name list must be a non-empty record of name: replacement")
    return names


def redact(text, names):
    """Replace every listed name, whatever its capitals. Whole names only, so a short name (initials)
    cannot change an ordinary word; longest first, so a name inside a longer name is not cut in two."""
    for name in sorted(names, key=len, reverse=True):
        text = re.sub(r"(?<!\w)" + re.escape(name) + r"(?!\w)", names[name], text, flags=re.I)
    return text.strip()


# Change log
# Nov 16, 2026 (after the fresh review) · redact() now matches whole names only and works longest name first.
#   Before, a two- or three-letter name could be replaced inside an ordinary word.
