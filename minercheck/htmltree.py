"""Tolerant HTML -> ElementTree, plus a small CSS selector engine. Stdlib only.

Supported selectors (enough for "find the number on this page"):
  tag  #id  .class  [attr]  [attr=v]  [attr^=v]  [attr$=v]  [attr*=v]  [attr~=v]
  descendant (space) and child (>) combinators, comma groups,
  :first-child  :last-child  :nth-of-type(n)
"""
from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta",
        "param", "source", "track", "wbr"}
# Content of these is not page text.
SKIP_TEXT = {"script", "style", "template", "noscript"}


class _Builder(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = ET.Element("document")
        self.stack: list[ET.Element] = [self.root]

    def handle_starttag(self, tag, attrs):
        el = ET.SubElement(self.stack[-1], tag.lower(), {k.lower(): (v or "") for k, v in attrs})
        if tag.lower() not in VOID:
            self.stack.append(el)

    def handle_startendtag(self, tag, attrs):
        ET.SubElement(self.stack[-1], tag.lower(), {k.lower(): (v or "") for k, v in attrs})

    def handle_endtag(self, tag):
        tag = tag.lower()
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return
        # stray end tag: ignore (browsers do too)

    def handle_data(self, data):
        cur = self.stack[-1]
        if len(cur):
            last = cur[-1]
            last.tail = (last.tail or "") + data
        else:
            cur.text = (cur.text or "") + data


def parse_html(text: str) -> ET.Element:
    b = _Builder()
    b.feed(text)
    b.close()
    return b.root


def text_of(el: ET.Element) -> str:
    """Visible text of an element (script/style skipped), whitespace collapsed."""
    parts: list[str] = []

    def walk(e: ET.Element) -> None:
        if e.tag in SKIP_TEXT:
            return
        if e.text:
            parts.append(e.text)
        for c in e:
            walk(c)
            if c.tail:
                parts.append(c.tail)

    walk(el)
    return re.sub(r"\s+", " ", "".join(parts)).strip()


# ----------------------------------------------------------------- selectors
_COMPOUND = re.compile(
    r"(?P<tag>[a-zA-Z][\w-]*|\*)?"
    r"(?P<rest>(?:#[\w-]+|\.[\w-]+|\[[^\]]+\]|:[\w-]+(?:\([^)]*\))?)*)"
)
_PART = re.compile(r"#[\w-]+|\.[\w-]+|\[[^\]]+\]|:[\w-]+(?:\([^)]*\))?")
_ATTR = re.compile(r"""^\[\s*([\w-]+)\s*(?:([~^$*]?=)\s*["']?(.*?)["']?)?\s*\]$""")


class SelectorError(ValueError):
    pass


def _parse_compound(s: str) -> dict:
    m = _COMPOUND.fullmatch(s)
    if not m or not s:
        raise SelectorError(f"unsupported CSS selector part {s!r}")
    c = {"tag": (m.group("tag") or "*").lower(), "id": None, "classes": [], "attrs": [], "pseudo": []}
    for p in _PART.findall(m.group("rest") or ""):
        if p.startswith("#"):
            c["id"] = p[1:]
        elif p.startswith("."):
            c["classes"].append(p[1:])
        elif p.startswith("["):
            am = _ATTR.match(p)
            if not am:
                raise SelectorError(f"bad attribute selector {p!r}")
            c["attrs"].append((am.group(1).lower(), am.group(2), am.group(3)))
        else:
            c["pseudo"].append(p)
    return c


def _parse_group(sel: str) -> list[tuple[str, dict]]:
    """'div.a > span b' -> [(' ', div.a), ('>', span), (' ', b)]; first combinator is unused."""
    tokens = re.findall(r">|[^\s>]+", sel.strip())
    out: list[tuple[str, dict]] = []
    comb = " "
    for t in tokens:
        if t == ">":
            comb = ">"
            continue
        out.append((comb, _parse_compound(t)))
        comb = " "
    if not out:
        raise SelectorError(f"empty selector {sel!r}")
    return out


def _match_compound(el: ET.Element, c: dict, parents: dict) -> bool:
    if c["tag"] != "*" and el.tag != c["tag"]:
        return False
    if c["id"] is not None and el.get("id") != c["id"]:
        return False
    if c["classes"]:
        have = set((el.get("class") or "").split())
        if not all(k in have for k in c["classes"]):
            return False
    for name, op, val in c["attrs"]:
        got = el.get(name)
        if got is None:
            return False
        if op is None:
            continue
        if op == "=" and got != val:
            return False
        if op == "^=" and not got.startswith(val):
            return False
        if op == "$=" and not got.endswith(val):
            return False
        if op == "*=" and val not in got:
            return False
        if op == "~=" and val not in got.split():
            return False
    for p in c["pseudo"]:
        parent = parents.get(el)
        sibs = list(parent) if parent is not None else [el]
        if p == ":first-child" and sibs[0] is not el:
            return False
        if p == ":last-child" and sibs[-1] is not el:
            return False
        m = re.fullmatch(r":nth-of-type\((\d+)\)", p)
        if m:
            same = [s for s in sibs if s.tag == el.tag]
            n = int(m.group(1))
            if n < 1 or n > len(same) or same[n - 1] is not el:
                return False
        elif p not in (":first-child", ":last-child"):
            raise SelectorError(f"unsupported pseudo-class {p}")
    return True


def _match_chain(el: ET.Element, chain: list[tuple[str, dict]], parents: dict) -> bool:
    comb, c = chain[-1]
    if not _match_compound(el, c, parents):
        return False
    if len(chain) == 1:
        return True
    rest = chain[:-1]
    p = parents.get(el)
    if comb == ">":
        return p is not None and _match_chain(p, rest, parents)
    while p is not None:
        if _match_chain(p, rest, parents):
            return True
        p = parents.get(p)
    return False


def select(root: ET.Element, selector: str) -> list[ET.Element]:
    """All elements matching any comma group, in document order."""
    groups = [_parse_group(g) for g in selector.split(",") if g.strip()]
    if not groups:
        raise SelectorError("empty selector")
    parents = {c: p for p in root.iter() for c in p}
    return [el for el in root.iter() if el is not root and any(_match_chain(el, g, parents) for g in groups)]
