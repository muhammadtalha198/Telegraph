"""apiOutputSamples/<INTENT>/<slug>.md: one reader/writer for every script.

Front matter is a loose YAML subset (block scalars written by capture_api_output.py are not
always indented correctly), so it is parsed by hand, the same way the gates always did.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

# First fenced block after the front matter, any (or no) language tag: ```json, ```text, ```xml ...
_FENCE = re.compile(r"^```[\w+-]*[ \t]*\n(.*?)^```[ \t]*$", re.S | re.M)


def parse_front_matter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    out: dict[str, str] = {}
    key = None
    buf: list[str] = []
    for line in parts[1].splitlines():
        if re.match(r"^[a-z_]+:", line) and not line.startswith(" "):
            if key is not None:
                out[key] = "\n".join(buf).strip().strip('"')
            key, _, rest = line.partition(":")
            key, rest = key.strip(), rest.strip()
            if rest == "|":
                buf = []
            else:
                out[key] = rest.strip('"')
                key, buf = None, []
        elif key is not None:
            buf.append(line)
    if key is not None:
        out[key] = "\n".join(buf).strip().strip('"')
    return out


def raw_body(text: str) -> str:
    """The captured API output: first fenced block of the document body."""
    body = text.split("---", 2)[2] if text.startswith("---") and text.count("---") >= 2 else text
    m = _FENCE.search(body)
    return m.group(1).strip() if m else ""


def parse_sample(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError("missing front matter")
    raw = raw_body(text)
    try:
        parsed = json.loads(raw)
    except ValueError:
        parsed = None
    return {"meta": parse_front_matter(text), "raw": raw, "json": parsed, "path": path, "full": text}


def replace_or_add(fm: str, key: str, value: str) -> str:
    """Set `key: value` in a front-matter block. Notes are quoted; the value is inserted
    literally (a callable replacement: backslashes in notes are never regex escapes)."""
    pat = re.compile(rf"(?m)^{re.escape(key)}:\s*.*$")
    if key in ("reviewer_note", "capture_note"):
        line = f'{key}: "' + value.replace("\\", "\\\\").replace('"', "'") + '"'
    else:
        line = f"{key}: {value}"
    return pat.sub(lambda _m: line, fm, count=1) if pat.search(fm) else fm.rstrip() + "\n" + line + "\n"
