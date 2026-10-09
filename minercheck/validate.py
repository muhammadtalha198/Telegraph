"""Per-candidate validation. One candidate = one source's answer to one question.

Layers (every result keeps a full audit trail in Candidate.checks):
  fetch  the call itself (HTTP status, timeout, rate limit)
  E1     extraction: a non-empty scalar was pulled out by a YAML rule
  E5     answer type: the scalar is the right KIND of answer (runs right after E1,
         because E2/E4 need the parsed value: "hot" has no number to range-check)
  E2     sanity: believable range (no 200 C, no negative price, no 1970 date)
  E4     freshness: timestamp age / clock skew / today's date
  E5     entity + scope: right city, coin, pair, timezone
E3 (cross-check) needs all candidates and lives in verify.py.
"""
from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from typing import Any

from . import units as U
from .answers import Context, Parsed, Reject, parse_answer, parse_timestamp, zone
from .errors import ExtractError
from .fetch import FetchResult
from .normalize import Normalized, fold, haversine_km
from .reader import Document, extract, interpolate, read
from .spec import IntentSpec, SourceSpec

log = logging.getLogger("minercheck.validate")
_STR_MODS = ("unit", "tz", "scale")


@dataclass
class Candidate:
    source: SourceSpec
    fetch: FetchResult | None = None
    doc_format: str = ""
    raw_value: Any = None
    parsed: Parsed | None = None
    timestamp: datetime | None = None
    age_s: float | None = None
    entity_seen: dict[str, Any] = field(default_factory=dict)
    extras: dict[str, Any] = field(default_factory=dict)
    checks: list[tuple[str, bool, str]] = field(default_factory=list)
    status: str = "pending"          # valid | rejected | error
    layer: str = ""                  # layer that stopped it
    reason: str = ""
    consensus: str = ""              # agreed | disagreed | duplicate_publisher | ""
    deviation: Decimal | None = None
    tolerance: Decimal | None = None
    max_age_s: int | None = None     # effective freshness limit (source override or spec)

    @property
    def name(self) -> str:
        return self.source.name

    def ok(self, layer: str, detail: str) -> None:
        self.checks.append((layer, True, detail))

    def reject(self, layer: str, reason: str, *, error: bool = False) -> "Candidate":
        self.checks.append((layer, False, reason))
        self.status, self.layer, self.reason = ("error" if error else "rejected"), layer, reason
        log.info("%s rejected at %s: %s", self.source.id, layer, reason)
        return self


def _rule_vars(rule: dict, variables: dict) -> dict:
    """Interpolate {placeholders} inside string modifiers (unit: '{quote}', tz: '{timezone}')."""
    out = dict(rule)
    for k in _STR_MODS:
        if isinstance(out.get(k), str):
            out[k] = interpolate(out[k], variables)
    return out


def unit_label(spec: IntentSpec, norm: Normalized) -> str:
    """Canonical unit with placeholders filled ('{quote}' -> 'USD')."""
    try:
        return interpolate(spec.canonical_unit, norm.vars)
    except ExtractError:
        return spec.canonical_unit


def _first(doc: Document, rules: list[dict], variables: dict) -> tuple[Any, dict] | None:
    if not rules:
        return None
    try:
        loc = extract(doc, rules, variables)
    except ExtractError:
        return None
    return loc.value, _rule_vars(loc.rule, variables)


def _key(s: str) -> str:
    """'SLOVNAFT , a.s.' == 'Slovnaft, A.S.': accents, case, spaces and punctuation ignored."""
    return re.sub(r"[^0-9a-z]", "", fold(s))


def _api_error_hint(doc: Document) -> str:
    j = doc.json
    if isinstance(j, dict):
        for k in ("error", "errors", "message", "msg", "detail", "retMsg"):
            if j.get(k) not in (None, "", [], {}):
                return f" (API says {k}={str(j[k])[:80]!r})"
    return ""


def _parse_extra(quantity: str, raw: Any, rule: dict, ctx: Context) -> Any:
    if quantity == "text":
        s = re.sub(r"\s+", " ", str(raw)).strip()
        if not s:
            raise Reject("empty text")
        return s[:80]
    if quantity == "temperature":
        return parse_answer("temperature", raw, rule, ctx).canonical
    if quantity == "datetime":
        return parse_timestamp(raw, rule, ctx.fetched_at)
    if quantity == "boolean":
        return parse_answer("boolean", raw, rule, ctx).display
    n, tok = U.parse_number(str(raw)) if not isinstance(raw, (int, Decimal)) else (U.to_decimal(raw), "")
    if n is None:
        raise Reject(f"{raw!r} has no number")
    if rule.get("scale") is not None:
        n *= Decimal(str(rule["scale"]))
    if quantity == "speed":
        unit = U.unit_of(tok, "speed") or rule.get("unit")
        if not unit:
            raise Reject(f"speed {raw!r} has no unit")
        return U.to_canonical(n, unit, "speed")
    return n


def _entity_checks(spec: IntentSpec, cand: Candidate, norm: Normalized, fetched_at: datetime) -> str | None:
    want, seen, v = norm.entity, cand.entity_seen, spec.validation
    if "lat" in seen and "lon" in seen and "lat" in want:
        try:
            km = haversine_km(float(want["lat"]), float(want["lon"]), float(seen["lat"]), float(seen["lon"]))
        except (TypeError, ValueError):
            return f"answer coordinates {seen['lat']},{seen['lon']} are not numbers"
        if v.max_km is not None and km > v.max_km:
            return (f"answer is for {seen['lat']},{seen['lon']}, {km:.0f} km from {want.get('place')} "
                    f"(max {v.max_km:g} km): wrong place")
        cand.ok("E5", f"place within {km:.1f} km")
    if "name" in seen and want.get("name"):
        a, b = _key(str(seen["name"])), _key(str(want["name"]))
        if not a or not (a in b or b in a):
            return f"answer is about {seen['name']!r}, asked {want['name']!r}: wrong entity"
        cand.ok("E5", f"entity {seen['name']}")
    if "country" in seen and want.get("country"):
        if fold(str(seen["country"])) != fold(str(want["country"])):
            return f"answer is for {seen['country']!r}, asked {want['country']!r}: wrong place"
    if "symbol" in seen and "symbol" in want:
        raw = str(seen["symbol"]).upper()
        s = re.sub(r"[-_/ ]", "", raw)
        sym = str(want["symbol"]).upper()
        # every known id/alias for the asked asset (coingecko id, wrapped-token alias, etc.)
        ids = {re.sub(r"[-_/ ]", "", str(x)).upper() for k, x in norm.vars.items()
               if isinstance(x, str) and k not in ("asset_name", "place", "symbol_lower", "quote", "quote_lower")}
        quotes = U.USD_EQUIVALENT | {str(norm.vars.get("quote", "")).upper()}
        tokens = {re.sub(r"[-_/ ]", "", t).upper() for t in re.split(r"[-_/ ]", raw) if t}
        ok = (s == sym or s in ids                                   # exact / known id
              or any(s == i + q or s == q + i for i in ids | {sym} for q in quotes)  # BASEQUOTE or QUOTEBASE pair
              or bool(tokens & (ids | {sym})))                       # asked symbol is one side of the pair
        if not ok:
            return f"answer is for {seen['symbol']!r}, asked {sym}: wrong asset"
        cand.ok("E5", f"asset {seen['symbol']} matches {sym}")
    for side in ("base", "quote"):
        if side in seen and side in want:
            if str(seen[side]).upper() != str(want[side]).upper():
                return f"answer {side} is {seen[side]!r}, asked {want[side]}: wrong currency pair"
            cand.ok("E5", f"{side} {want[side]}")
    if spec.answer_type in ("date", "datetime_tz"):
        named = seen.get("timezone")
        want_tz = want.get("timezone") or "UTC"
        if named:
            # The API says which zone it answered for: it must be the one asked (or share its offset now).
            if str(named) != want_tz:
                try:
                    a = zone(str(named)).utcoffset(fetched_at.replace(tzinfo=None))
                except Reject:
                    return f"answer timezone {named!r} is not a known zone"
                if a != zone(want_tz).utcoffset(fetched_at.replace(tzinfo=None)):
                    return f"answer is for timezone {named}, asked {want_tz}: wrong place"
                cand.ok("E5", f"timezone {named} has the same UTC offset as {want_tz}")
            else:
                cand.ok("E5", f"timezone {named}")
        elif cand.parsed and cand.parsed.tz_seen:
            # Absolute instant (offset, Z, GMT, epoch): converted to the asked zone like a unit.
            cand.ok("E5", f"absolute time ({cand.parsed.tz_seen}) converted to {want_tz}")
        else:
            return "answer does not say which timezone it is for"
    return None


def validate(spec: IntentSpec, cand: Candidate, norm: Normalized) -> Candidate:
    """Run fetch, E1, E5-type, E2, E4, E5-entity on one candidate. Mutates and returns it."""
    f, v = cand.fetch, spec.validation
    if f is None or not f.ok:
        return cand.reject("fetch", f.error if f else "not fetched", error=True)
    cand.ok("fetch", f"HTTP {f.http_status} in {f.latency_ms} ms" + (" (cache)" if f.from_cache else ""))
    doc = read(f.body, headers=f.headers)
    cand.doc_format = doc.format
    header_only = all("header" in r for r in cand.source.value)
    if doc.format == "binary" or (doc.format == "empty" and not header_only):
        return cand.reject("E1", f"{doc.format} response body")
    for n in doc.notes:
        cand.ok("read", n)

    # ---- E1 extraction
    try:
        loc = extract(doc, cand.source.value, norm.vars)
    except ExtractError as e:
        return cand.reject("E1", f"no value: {e}{_api_error_hint(doc)}")
    rule = _rule_vars(loc.rule, norm.vars)
    cand.raw_value = loc.value
    cand.ok("E1", f"{doc.format} rule {loc.index + 1} -> {str(loc.value)[:60]!r}")

    for key, rules in cand.source.entity.items():
        got = _first(doc, rules, norm.vars)
        if got is not None:
            cand.entity_seen[key] = got[0]

    # ---- E5 answer type (parse)
    tz_name = norm.vars.get("timezone") or None
    ctx = Context(fetched_at=f.fetched_at, tz=zone(tz_name) if tz_name else timezone.utc,
                  quote=str(norm.vars.get("quote", "USD")))
    try:
        cand.parsed = parse_answer(spec.answer_type, loc.value, rule, ctx,
                                   source_tz=str(cand.entity_seen.get("timezone") or "") or None)
    except Reject as e:
        return cand.reject("E5", f"wrong answer type: {e}")
    except (ValueError, ArithmeticError) as e:
        return cand.reject("E5", f"wrong answer type: {e}")
    cand.ok("E5", f"{spec.answer_type}: {cand.parsed.detail}")
    p = cand.parsed

    # ---- E2 sanity
    if spec.answer_type == "date":
        today = f.fetched_at.astimezone(ctx.tz).date()
        days = (p.display - today).days
        limit = v.max_days_from_today if v.max_days_from_today is not None else (1 if spec.scope == "today" else None)
        if p.display.year < 1971 or days > 1:          # epoch-zero / future dates are never right
            return cand.reject("E2", f"date {p.display} is not believable (today is {today})")
        if limit is not None and abs(days) > limit:
            return cand.reject("E2", f"date {p.display} is {abs(days)} days from today ({today}): not believable")
    elif spec.answer_type == "datetime_tz":
        if not 2000 <= p.display.year <= 2100:
            return cand.reject("E2", f"time {p.display.isoformat()} is not believable")
    else:
        shown = f"{p.canonical} {unit_label(spec, norm)}".strip()
        if v.sanity_min is not None and p.canonical < v.sanity_min:
            return cand.reject("E2", f"{shown} is below the believable minimum {v.sanity_min}")
        if v.sanity_max is not None and p.canonical > v.sanity_max:
            return cand.reject("E2", f"{shown} is above the believable maximum {v.sanity_max}")
    cand.ok("E2", "in believable range")

    # ---- E4 freshness
    max_age = cand.source.freshness_max_age_s or v.max_age_s
    cand.max_age_s = max_age
    if spec.answer_type == "datetime_tz":
        if max_age is not None and abs(p.canonical) > max_age:
            return cand.reject("E4", f"clock is {p.canonical}s off our fetch time (max {max_age}s): stale or wrong")
        cand.ok("E4", f"clock skew {p.canonical}s")
    elif spec.answer_type == "date" and spec.scope != "today":
        if max_age is not None:
            age = (f.fetched_at.astimezone(ctx.tz).date() - p.display).days * 86400
            if age > max_age:
                return cand.reject("E4", f"latest date {p.display} is {age // 86400} days old (max {max_age // 86400}): stale")
        cand.ok("E4", f"latest date {p.display}")
    elif spec.answer_type == "date":
        edge = timedelta(seconds=max_age or 120)
        ok_days = {(f.fetched_at + d).astimezone(ctx.tz).date() for d in (-edge, timedelta(0), edge)}
        if p.display not in ok_days:
            return cand.reject("E4", f"date {p.display} is not today ({f.fetched_at.astimezone(ctx.tz).date()} "
                                     f"in {tz_name or 'UTC'}): stale")
        cand.ok("E4", "date is today")
    if cand.source.timestamp:
        got = None
        try:
            loc_ts = extract(doc, cand.source.timestamp, norm.vars)
            got = parse_timestamp(loc_ts.value, _rule_vars(loc_ts.rule, norm.vars), f.fetched_at)
        except (ExtractError, Reject) as e:
            if v.require_timestamp:
                return cand.reject("E4", f"no usable timestamp: {e}")
            cand.ok("E4", f"timestamp unreadable ({e}); freshness unknown")
        if got is not None:
            cand.timestamp = got
            cand.age_s = (f.fetched_at - got).total_seconds()
            if -cand.age_s > v.max_future_s:
                return cand.reject("E4", f"timestamp {got.isoformat()} is {-cand.age_s:.0f}s in the future")
            if max_age is not None and cand.age_s > max_age:
                return cand.reject("E4", f"stale: data is {cand.age_s / 60:.0f} min old (max {max_age / 60:.0f} min)")
            cand.ok("E4", f"data age {cand.age_s:.0f}s")
    elif v.require_timestamp and spec.answer_type not in ("date", "datetime_tz"):
        return cand.reject("E4", "source has no timestamp to prove freshness")

    # ---- E5 entity / scope
    why = _entity_checks(spec, cand, norm, f.fetched_at)
    if why:
        return cand.reject("E5", why)

    # ---- extras (never reject the main answer; bad extras are dropped)
    for name, rules in cand.source.extras.items():
        got = _first(doc, rules, norm.vars)
        if got is None:
            continue
        x = spec.extras[name]
        try:
            val = _parse_extra(x["quantity"], got[0], {**got[1], "unit": got[1].get("unit") or x.get("unit")}, ctx)
        except (Reject, ValueError, ArithmeticError) as e:
            cand.ok("extra", f"{name} dropped: {e}")
            continue
        s = x.get("sanity") or {}
        if isinstance(val, Decimal) and (("min" in s and val < Decimal(str(s["min"]))) or ("max" in s and val > Decimal(str(s["max"])))):
            cand.ok("extra", f"{name} dropped: {val} outside {s}")
            continue
        cand.extras[name] = val
    cand.status = "valid"
    return cand
