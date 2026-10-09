"""Response reader: any body -> one Document -> value by YAML rule.

Format is detected from the BODY first. The Content-Type header is only a
tie-breaker, because headers lie (text/plain JSON, text/html XML, ...).

Extraction rule kinds (exactly one per rule, see docs/INTENT_SPEC_GUIDE.md):
  json:   current.temperature_2m     dot path; '*' = first key/item; {var} interpolation
  xpath:  .//item[targetCurrency='EUR']/exchangeRate   (XML or HTML; '/@attr' for attributes)
  css:    span.ccOutputRslt          (HTML; optional attr:, index:)
  csv:    price   + where: {symbol: BTC} | row: 0
  header: Date                       (response header)
  regex:  'ts=(\\d+(?:\\.\\d+)?)'    (whole body when used alone)
`regex:` next to another kind post-filters the located text. Rules are tried in
order; the first that yields a scalar wins. A rule that does not fit the detected
format is skipped with a reason, never guessed.
"""
from __future__ import annotations

import csv
import io
import json
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Any

from .errors import ExtractError
from .htmltree import SelectorError, parse_html, select, text_of

LOCATORS = ("json", "xpath", "css", "csv", "header", "regex")
_JSONP = re.compile(r"[\w$.]+\s*\((.*)\)\s*;?", re.S)


def _json_payload(t: str) -> str | None:
    """JSON text of a body, unwrapping JSONP ('cb({...});'). None if it is not JSON."""
    for cand in (t, (_JSONP.fullmatch(t) or [None, None])[1]):
        if cand and cand.strip()[:1] in "{[\"":
            try:
                json.loads(cand)
                return cand.strip()
            except ValueError:
                continue
    return None
FORMATS = ("json", "xml", "html", "csv", "text", "empty", "binary")


@dataclass
class Document:
    format: str
    text: str
    headers: dict[str, str] = field(default_factory=dict)
    json: Any = None
    xml: ET.Element | None = None  # synthetic <document> wrapping the XML root
    html: ET.Element | None = None
    rows: list[dict[str, str]] | None = None
    notes: list[str] = field(default_factory=list)


@dataclass
class Located:
    value: Any
    rule: dict
    index: int


# ------------------------------------------------------------------ detection
def _decode(body: bytes | str, content_type: str) -> str | None:
    if isinstance(body, str):
        return body
    if not body:
        return ""
    if body[:2] == b"PK" or body.count(b"\x00") > len(body) // 10:
        return None  # zip / binary
    m = re.search(r"charset=([\w-]+)", content_type or "", re.I)
    enc = m.group(1) if m else "utf-8"
    try:
        return body.decode(enc, errors="replace").lstrip("﻿")
    except LookupError:
        return body.decode("utf-8", errors="replace").lstrip("﻿")


def _strip_ns(root: ET.Element) -> ET.Element:
    for el in root.iter():
        if isinstance(el.tag, str) and "}" in el.tag:
            el.tag = el.tag.split("}", 1)[1]
        for k in list(el.attrib):
            if "}" in k:
                el.attrib[k.split("}", 1)[1]] = el.attrib.pop(k)
    return root


def _looks_like_csv(text: str) -> str | None:
    lines = [ln for ln in text.splitlines() if ln.strip()][:20]
    if len(lines) < 2:
        return None
    for delim in (",", ";", "\t", "|"):
        counts = {ln.count(delim) for ln in lines}
        if len(counts) == 1 and next(iter(counts)) >= 1:
            return delim
    return None


def detect_format(text: str | None, content_type: str = "") -> str:
    if text is None:
        return "binary"
    t = text.strip()
    if not t:
        return "empty"
    ct = (content_type or "").lower()
    head = t[:1000].lower()
    if _json_payload(t) is not None:
        return "json"
    if t[0] == "<":
        if head.startswith("<!doctype html") or "<html" in head or ("html" in ct and not head.startswith("<?xml")):
            return "html"
        try:
            ET.fromstring(t)
            return "xml"
        except ET.ParseError:
            # Broken/truncated XML must not be "repaired" by the tolerant HTML parser:
            # '<temp>31' may have been '<temp>31.5</temp>'. Regex rules can still read it.
            return "text"
    if _looks_like_csv(t):
        return "csv"
    return "text"


def read(body: bytes | str, content_type: str = "", headers: dict[str, str] | None = None) -> Document:
    """Parse any body. Never raises: parse problems become doc.notes."""
    hdrs = {k.lower(): v for k, v in (headers or {}).items()}
    if not content_type:
        content_type = hdrs.get("content-type", "")
    text = _decode(body, content_type)
    fmt = detect_format(text, content_type)
    doc = Document(format=fmt, text=text or "", headers=hdrs)
    ct = content_type.split(";")[0].strip().lower()
    claimed = ("json" if "json" in ct else "xml" if "xml" in ct else "html" if "html" in ct
               else "csv" if "csv" in ct else "text" if ct.startswith("text/") else "")
    if claimed and claimed != fmt and fmt not in ("empty", "binary"):
        doc.notes.append(f"Content-Type says {claimed}, body is {fmt}; using body")
    if fmt == "json":
        payload = _json_payload(text.strip())
        if payload != text.strip():
            doc.notes.append("JSONP callback unwrapped")
        doc.json = json.loads(payload, parse_float=Decimal)
    elif fmt == "xml":
        wrapper = ET.Element("document")
        wrapper.append(_strip_ns(ET.fromstring(text.strip())))
        doc.xml = wrapper
    elif fmt == "html":
        doc.html = parse_html(text)
    elif fmt == "csv":
        delim = _looks_like_csv(text) or ","
        doc.rows = [{(k or "").strip(): (v or "").strip() for k, v in r.items()}
                    for r in csv.DictReader(io.StringIO(text.strip()), delimiter=delim)]
    elif text and text.strip()[:1] in "{[":
        doc.notes.append("body starts like JSON but does not parse (truncated or broken)")
    elif text and text.strip()[:1] == "<" and fmt == "text":
        doc.notes.append("body starts like XML but does not parse (truncated or broken)")
    return doc


# ----------------------------------------------------------------- extraction
_VAR = re.compile(r"\{(\w+)\}")


def interpolate(s: str, variables: dict[str, Any]) -> str:
    def sub(m: re.Match) -> str:
        k = m.group(1)
        if k not in variables:
            raise ExtractError(f"rule uses {{{k}}} but no input/normalized value is named {k!r}")
        return str(variables[k])
    return _VAR.sub(sub, s)


def json_path(obj: Any, path: str) -> Any:
    """Dot path. '*' = first key/item. Integers index lists (negative allowed).
    Key match is exact, else the single case-insensitive match. Raises KeyError with the failing step."""
    cur = obj
    steps = [p for p in re.sub(r"\[(-?\d+)\]", r".\1", path).split(".") if p != ""]
    for i, step in enumerate(steps):
        where = ".".join(steps[: i + 1])
        if isinstance(cur, list):
            if step == "*":
                if not cur:
                    raise KeyError(f"empty list at {where}")
                cur = cur[0]
                continue
            if not re.fullmatch(r"-?\d+", step):
                raise KeyError(f"list at {'.'.join(steps[:i]) or '$'} needs an index, got {step!r}")
            idx = int(step)
            if not -len(cur) <= idx < len(cur):
                raise KeyError(f"index {idx} out of range at {where}")
            cur = cur[idx]
        elif isinstance(cur, dict):
            if step == "*":
                if not cur:
                    raise KeyError(f"empty object at {where}")
                cur = next(iter(cur.values()))
            elif step in cur:
                cur = cur[step]
            else:
                ci = [k for k in cur if str(k).lower() == step.lower()]
                if len(ci) != 1:
                    raise KeyError(f"no key {step!r} at {where}")
                cur = cur[ci[0]]
        else:
            raise KeyError(f"{'.'.join(steps[:i]) or '$'} is a value, cannot go to {step!r}")
    return cur


def _xpath(root: ET.Element, path: str) -> list[tuple[ET.Element, str | None]]:
    attr = None
    m = re.search(r"/@([\w-]+)$", path)
    if m:
        attr, path = m.group(1), path[: m.start()]
    path = re.sub(r"/text\(\)$", "", path)
    if path.startswith("/"):
        path = "." + path
    try:
        return [(el, attr) for el in root.findall(path)]
    except (SyntaxError, KeyError) as e:
        raise ExtractError(f"unsupported xpath {path!r}: {e}") from e


def _el_value(doc: Document, el: ET.Element, attr: str | None) -> str | None:
    if attr:
        return el.get(attr)
    if doc.format == "html":
        return text_of(el)
    return re.sub(r"\s+", " ", "".join(el.itertext())).strip()


def _apply_regex(text: str, pattern: str, rule: dict) -> str | None:
    flags = re.S | (re.I if "i" in str(rule.get("flags", "")) else 0)
    m = re.search(pattern, text, flags)
    if not m:
        return None
    if "value" in m.groupdict():
        return m.group("value")
    return m.group(int(rule.get("group", 1))) if m.groups() else m.group(0)


def locate(doc: Document, rule: dict, variables: dict[str, Any]) -> Any:
    """Apply one rule. Returns a scalar or raises ExtractError with the reason."""
    kind = next((k for k in LOCATORS if k in rule and not (k == "regex" and any(x in rule for x in LOCATORS[:-1]))), None)
    if kind is None:
        raise ExtractError(f"rule has no locator ({', '.join(LOCATORS)})")
    target = interpolate(str(rule[kind]), variables)
    val: Any = None
    if kind == "json":
        if doc.format != "json":
            raise ExtractError(f"json rule, but body is {doc.format}")
        if rule.get("exists"):
            try:
                found = json_path(doc.json, target)
            except KeyError:
                found = None
            return _post(found not in (None, "", [], {}), rule)
        try:
            # 'bids+asks' concatenates two lists (order-book sides)
            parts = [json_path(doc.json, t) for t in target.split("+")]
        except KeyError as e:
            raise ExtractError(f"json {target}: {e.args[0]}") from None
        if len(parts) > 1:
            # explicit field concatenation (a+b) -> a list, e.g. for a record_set of {scheme, country}
            flat = [x for part in parts for x in (part if isinstance(part, list) else [part])]
            flat = [x for x in flat if x not in (None, "", [], {})]
            if not flat:
                raise ExtractError(f"json {target}: all parts empty")
            return flat
        val = parts[0]
        if "each" in rule or "aggregate" in rule:
            return _post(_list_value(val, rule, variables, target), rule)
    elif kind in ("xpath", "css"):
        root = doc.xml if doc.format == "xml" else doc.html if doc.format == "html" else None
        if root is None:
            raise ExtractError(f"{kind} rule, but body is {doc.format}")
        try:
            hits = _xpath(root, target) if kind == "xpath" else [(e, rule.get("attr")) for e in select(root, target)]
        except SelectorError as e:
            raise ExtractError(f"css {target!r}: {e}") from None
        if kind == "xpath" and rule.get("attr"):
            hits = [(e, rule["attr"]) for e, _ in hits]
        idx = int(rule.get("index", 0))
        if not hits or not -len(hits) <= idx < len(hits):
            raise ExtractError(f"{kind} {target!r}: no match")
        val = _el_value(doc, *hits[idx])
    elif kind == "csv":
        if doc.format != "csv" or doc.rows is None:
            raise ExtractError(f"csv rule, but body is {doc.format}")
        where = {interpolate(str(k), variables): interpolate(str(v), variables)
                 for k, v in (rule.get("where") or {}).items()}
        rows = [r for r in doc.rows if all(str(r.get(k, "")).lower() == v.lower() for k, v in where.items())]
        if not rows:
            raise ExtractError(f"csv: no row where {where}")
        idx = int(rule.get("row", 0))
        if not -len(rows) <= idx < len(rows):
            raise ExtractError(f"csv: row {idx} out of range")
        row = rows[idx]
        if target not in row:
            raise ExtractError(f"csv: no column {target!r} (have {list(row)[:8]})")
        val = row[target]
    elif kind == "header":
        val = doc.headers.get(target.lower())
        if val is None:
            raise ExtractError(f"header {target!r} missing")
    elif kind == "regex":
        val = _apply_regex(doc.text, target, rule)
        if val is None:
            raise ExtractError(f"regex {target!r}: no match")
        return _post(val.strip(), rule)
    if isinstance(val, (dict, list)):
        raise ExtractError(f"{kind} {target}: points to an {'object' if isinstance(val, dict) else 'array'}, not a value"
                           + (" (use each: or aggregate: to read a list)" if isinstance(val, list) else ""))
    if "regex" in rule and val is not None:
        got = _apply_regex(str(val), interpolate(str(rule["regex"]), variables), rule)
        if got is None:
            raise ExtractError(f"{kind} {target}: value {str(val)[:40]!r} does not match regex")
        val = got.strip()
    if val is None or (isinstance(val, str) and not val.strip()):
        raise ExtractError(f"{kind} {target}: empty value")
    return _post(val.strip() if isinstance(val, str) else val, rule)


def _post(val: Any, rule: dict) -> Any:
    """hex: and map: modifiers, applied after a value is located."""
    if rule.get("hex") and isinstance(val, str):
        try:
            val = str(int(val, 16))
        except ValueError:
            raise ExtractError(f"value {val[:20]!r} is not hex") from None
    m = rule.get("map")
    if isinstance(m, dict):
        key = str(val).lower() if isinstance(val, bool) else str(val).strip().lower()
        hit = next((v for k, v in m.items() if str(k).lower() == key), None)
        if hit is not None:
            val = hit
    return val


def _list_value(val: Any, rule: dict, variables: dict[str, Any], target: str) -> Any:
    """each: -> list of scalars (optionally filtered by where:); aggregate: notional -> sum(price*size)."""
    if not isinstance(val, list):
        raise ExtractError(f"json {target}: expected a list")
    items = val
    where = {interpolate(str(k), variables): interpolate(str(v), variables) for k, v in (rule.get("where") or {}).items()}
    if where:
        def ok(item: Any) -> bool:
            try:
                return all(str(json_path(item, k)).lower() == v.lower() for k, v in where.items())
            except KeyError:
                return False
        items = [i for i in items if ok(i)]
    if rule.get("aggregate") == "notional":
        if rule.get("flat"):                         # [p, s, p, s, ...]
            items = [items[i:i + 2] for i in range(0, len(items) - 1, 2)]
        pk, sk = str(rule.get("price", 0)), str(rule.get("size", 1))
        total = Decimal(0)
        for lvl in items:
            try:
                total += Decimal(str(json_path(lvl, pk))) * Decimal(str(json_path(lvl, sk)))
            except (KeyError, ArithmeticError, ValueError):
                raise ExtractError(f"json {target}: level {str(lvl)[:40]} has no price/size") from None
        if not items:
            raise ExtractError(f"json {target}: empty order book")
        return total
    if rule.get("aggregate"):
        raise ExtractError(f"unknown aggregate {rule['aggregate']!r} (supported: notional)")
    each = str(rule.get("each", "."))
    out = []
    for item in items:
        try:
            v = item if each == "." else json_path(item, each)
        except KeyError:
            continue
        if not isinstance(v, (dict, list)) and v not in (None, ""):
            out.append(v)
    if not out:
        raise ExtractError(f"json {target}: no list items" + (f" where {where}" if where else ""))
    return out


def extract(doc: Document, rules: list[dict], variables: dict[str, Any]) -> Located:
    """First rule that yields a scalar wins. Raises ExtractError listing why each rule failed."""
    reasons = []
    for i, rule in enumerate(rules):
        try:
            return Located(locate(doc, rule, variables), rule, i)
        except ExtractError as e:
            reasons.append(f"rule {i + 1}: {e}")
    raise ExtractError("; ".join(reasons) if reasons else "no rules")
