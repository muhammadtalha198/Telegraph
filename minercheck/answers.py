"""Answer types (E5 "is it the right KIND of answer?") and time parsing.

Each answer_type turns a located raw value into a Parsed answer, or raises
Reject with the reason. Parsed.canonical is always a Decimal so one cross-check
works for every type:

  temperature  degrees C
  price        amount in the requested quote currency (USDT/USDC count as USD)
  fx_rate      units of quote per 1 base
  number / percent
  date         date.toordinal() in the requested timezone
  datetime_tz  clock skew in seconds: (reported instant - our fetch time)
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta, timezone
from decimal import Decimal
from email.utils import parsedate_to_datetime
from typing import Any
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from . import units as U

ANSWER_TYPES = ("temperature", "price", "fx_rate", "number", "percent", "date", "datetime_tz", "boolean", "record_set")
QUANTITY = {"temperature": "temperature", "price": "money", "fx_rate": "ratio", "number": "number",
            "percent": "percent", "date": "date", "datetime_tz": "datetime", "boolean": "boolean",
            "record_set": "set"}
TRUE_WORDS = {"true", "yes", "y", "1", "active", "valid", "deliverable", "listed", "issued", "ok", "up", "open",
              "success", "on", "active_ongoing", "serviceable"}
FALSE_WORDS = {"false", "no", "n", "0", "inactive", "invalid", "dissolved", "terminated", "lapsed", "retired",
               "down", "closed", "off", "none", "not serviceable", "undeliverable"}

WEEKDAYS = {"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",
            "mon", "tue", "tues", "wed", "thu", "thur", "thurs", "fri", "sat", "sun"}
MONTHS = {m: i for i, names in enumerate(
    [("jan", "january"), ("feb", "february"), ("mar", "march"), ("apr", "april"), ("may",),
     ("jun", "june"), ("jul", "july"), ("aug", "august"), ("sep", "sept", "september"),
     ("oct", "october"), ("nov", "november"), ("dec", "december")], 1) for m in names}
RELATIVE = {"today", "tomorrow", "yesterday", "now", "tonight"}
_MONTH_RE = "|".join(sorted(MONTHS, key=len, reverse=True))


class Reject(Exception):
    """Candidate answer is not acceptable. args[0] = reason in plain words."""


@dataclass
class Context:
    """What the question asked, for parsing answers relative to it."""
    fetched_at: datetime                 # aware UTC
    tz: ZoneInfo | None = None           # requested timezone (date / time intents)
    quote: str = "USD"                   # requested quote currency (price)


@dataclass
class Parsed:
    canonical: Decimal
    display: Any            # Decimal in canonical unit | date | aware datetime
    unit: str               # unit as reported (or declared by the spec rule)
    detail: str             # what we understood, for logs
    tz_seen: str = ""       # timezone stated by the response (date/datetime answers)


def zone(name: str) -> ZoneInfo:
    try:
        return ZoneInfo(name)
    except (ZoneInfoNotFoundError, ValueError, TypeError) as e:
        raise Reject(f"unknown timezone {name!r}") from e


# ------------------------------------------------------------------ numbers
def _number(raw: Any, what: str) -> tuple[Decimal, str]:
    if isinstance(raw, bool):
        raise Reject(f"{what}: got a yes/no value ({raw}), not a number")
    if isinstance(raw, (int, float, Decimal)):
        return U.to_decimal(raw), ""
    n, unit = U.parse_number(str(raw))
    if n is None:
        raise Reject(f"{what}: {str(raw)[:40]!r} has no number in it")
    return n, unit


def parse_temperature(raw: Any, rule: dict, ctx: Context) -> Parsed:
    n, tok = _number(raw, "temperature")
    if U.has_percent(raw):
        raise Reject(f"temperature: {raw!r} is a percentage, not a temperature")
    unit = U.unit_of(tok, "temperature") if tok else None
    if tok and unit is None and U.unit_of(tok, "speed"):
        raise Reject(f"temperature: {raw!r} is a speed, not a temperature")
    unit = unit or rule.get("unit")
    if not unit:
        raise Reject(f"temperature: {raw!r} has no unit and the spec declares none")
    c = U.to_canonical(n, unit, "temperature")
    return Parsed(c, c, unit, f"{n} {unit}")


def parse_price(raw: Any, rule: dict, ctx: Context) -> Parsed:
    if U.has_percent(raw):
        raise Reject(f"price: {raw!r} is a percent change, not a price")
    n, tok = _number(raw, "price")
    unit = (U.unit_of(tok, "money") if tok else None) or rule.get("unit") or ctx.quote
    if rule.get("scale") is not None:
        n = n * Decimal(str(rule["scale"]))
    try:
        v = U.to_canonical(n, unit, "money", quote=ctx.quote)
    except ValueError as e:
        raise Reject(f"price: {e}") from None
    return Parsed(v, v, unit, f"{n} {unit}")


def parse_fx_rate(raw: Any, rule: dict, ctx: Context) -> Parsed:
    if U.has_percent(raw):
        raise Reject(f"fx rate: {raw!r} is a percentage, not an exchange rate")
    n, _tok = _number(raw, "fx rate")
    if rule.get("invert"):
        if n == 0:
            raise Reject("fx rate: 0 cannot be inverted")
        n = Decimal(1) / n
    return Parsed(n, n, "", f"{n}")


def parse_number_answer(raw: Any, rule: dict, ctx: Context) -> Parsed:
    n, tok = _number(raw, "number")
    if rule.get("scale") is not None:
        n = n * Decimal(str(rule["scale"]))
    return Parsed(n, n, tok or rule.get("unit", ""), f"{n}")


def parse_percent(raw: Any, rule: dict, ctx: Context) -> Parsed:
    n, tok = _number(raw, "percent")
    if rule.get("scale") is not None:          # e.g. scale: 100 for a fraction like 0.0235
        n = n * Decimal(str(rule["scale"]))
    return Parsed(n, n, "%", f"{n}%")


def parse_boolean(raw: Any, rule: dict, ctx: Context) -> Parsed:
    if isinstance(raw, bool):
        v = raw
    elif isinstance(raw, (int, Decimal)) and raw in (0, 1):
        v = bool(raw)
    else:
        s = U.clean_text(str(raw)).lower()
        if s in TRUE_WORDS:
            v = True
        elif s in FALSE_WORDS:
            v = False
        else:
            raise Reject(f"{str(raw)[:40]!r} is not a yes/no answer (map it with map: in the spec rule)")
    return Parsed(Decimal(int(v)), v, "", f"{raw!r} -> {'yes' if v else 'no'}")


def _record(x: Any) -> str:
    return str(x).strip().strip('"').rstrip(".").lower()


def parse_record_set(raw: Any, rule: dict, ctx: Context) -> Parsed:
    """A set of records (DNS A/MX/TXT ...). Order and case do not matter; the set must match exactly."""
    items = raw if isinstance(raw, list) else re.split(r"[,;\s]+", str(raw))
    recs = sorted({_record(x) for x in items if _record(x)})
    if not recs:
        raise Reject("empty record set")
    if any(isinstance(x, (dict, list)) for x in items):
        raise Reject("record set items must be values")
    digest = hashlib.sha256("\n".join(recs).encode()).hexdigest()[:12]
    return Parsed(Decimal(int(digest, 16)), tuple(recs), "", f"{len(recs)} record(s): {', '.join(recs)[:80]}")


# -------------------------------------------------------------------- times
_ISO_DT = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2})[T ](?P<time>\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?)\s*(?P<tz>Z|[+-]\d{2}:?\d{2}|UTC|GMT)?",
    re.I)
_ISO_D = re.compile(r"(?<!\d)(\d{4})-(\d{2})-(\d{2})(?!\d)")
_TIME = re.compile(r"(?<!\d)(\d{1,2}):(\d{2})(?::(\d{2})(?:\.\d+)?)?\s*([AaPp][Mm])?")
_WEEK = re.compile(r"\b\d{4}-?W\d{2}\b|\bthis (?:week|month|year)\b|\bweek \d{1,2}\b", re.I)


def _tz_from_suffix(s: str | None) -> timezone | None:
    if not s:
        return None
    s = s.upper()
    if s in ("Z", "UTC", "GMT"):
        return timezone.utc
    m = re.fullmatch(r"([+-])(\d{2}):?(\d{2})", s)
    if not m:
        return None
    off = timedelta(hours=int(m.group(2)), minutes=int(m.group(3)))
    return timezone(-off if m.group(1) == "-" else off)


def _epoch(raw: Any, unit: str | None) -> datetime:
    # strict: '2026-10-08' must not become epoch 2026 (1970-01-01T00:33)
    if isinstance(raw, str) and not re.fullmatch(r"\s*-?\d+(?:\.\d+)?\s*", raw):
        raise Reject(f"epoch: {raw!r} is not a number")
    n = U.to_decimal(raw)
    if n is None:
        raise Reject(f"epoch: {raw!r} is not a number")
    if unit == "ms" or (unit is None and n > Decimal("1e11")):
        n = n / 1000
    return datetime.fromtimestamp(float(n), tz=timezone.utc)


def _iso_datetime(s: str) -> datetime | None:
    m = _ISO_DT.search(s)
    if not m:
        return None
    t = m.group("time")
    frac = ""
    if "." in t:
        t, frac = t.split(".", 1)
        frac = (frac + "000000")[:6]
    fmt = "%Y-%m-%dT%H:%M:%S" if t.count(":") == 2 else "%Y-%m-%dT%H:%M"
    dt = datetime.strptime(f"{m.group('date')}T{t}", fmt)
    if frac:
        dt = dt.replace(microsecond=int(frac))
    tz = _tz_from_suffix(m.group("tz"))
    return dt.replace(tzinfo=tz) if tz else dt


def _rfc2822(s: str) -> datetime | None:
    if not re.search(r"\d{1,2}\s+[A-Za-z]{3}\s+\d{4}\s+\d{2}:\d{2}", s):
        return None
    try:
        return parsedate_to_datetime(s)
    except (TypeError, ValueError):
        return None


def _words_date(s: str) -> date | None:
    """'8 October 2026', 'October 8, 2026', 'Thu, 8 Oct 2026'."""
    m = re.search(rf"\b(\d{{1,2}})(?:st|nd|rd|th)?\s+({_MONTH_RE})\.?,?\s+(\d{{4}})\b", s, re.I)
    if m:
        return date(int(m.group(3)), MONTHS[m.group(2).lower()], int(m.group(1)))
    m = re.search(rf"\b({_MONTH_RE})\.?\s+(\d{{1,2}})(?:st|nd|rd|th)?,?\s+(\d{{4}})\b", s, re.I)
    if m:
        return date(int(m.group(3)), MONTHS[m.group(1).lower()], int(m.group(2)))
    return None


def _numeric_date(s: str, order: str | None) -> date | None:
    m = re.search(r"(?<!\d)(\d{1,2})[/.](\d{1,2})[/.](\d{4})(?!\d)", s)
    if not m:
        return None
    a, b, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
    if order is None:
        if a > 12 >= b:
            order = "DMY"
        elif b > 12 >= a:
            order = "MDY"
        elif a == b:
            order = "DMY"
        else:
            raise Reject(f"date: {s!r} is ambiguous (MM/DD or DD/MM?); the spec must set date_order")
    mo, d = (a, b) if order.upper() == "MDY" else (b, a)
    return date(y, mo, d)


def _scope_guard(s: str, what: str) -> None:
    low = s.strip().lower().rstrip(".")
    if _WEEK.search(s):
        raise Reject(f"{what}: {s!r} is a week/month span, not a single day (wrong scope)")
    if low in WEEKDAYS:
        raise Reject(f"{what}: {s!r} is a weekday only, not a full calendar date")
    if low in RELATIVE:
        raise Reject(f"{what}: {s!r} is a relative word, not a date")


def parse_date(raw: Any, rule: dict, ctx: Context) -> Parsed:
    tz = ctx.tz or timezone.utc
    if rule.get("epoch") or (isinstance(raw, (int, Decimal)) and not isinstance(raw, bool)):
        inst = _epoch(raw, rule.get("epoch"))
        d = inst.astimezone(tz).date()
        return Parsed(Decimal(d.toordinal()), d, "", f"epoch {raw} -> {d} in {tz}", "UTC")
    s = U.clean_text(str(raw))
    _scope_guard(s, "date")
    tz_seen = ""
    d: date | None = None
    if rule.get("format"):
        try:
            dt = datetime.strptime(s, rule["format"])
        except ValueError:
            raise Reject(f"date: {s!r} does not match format {rule['format']!r}") from None
        d = dt.date()
    else:
        dt = _iso_datetime(s) or _rfc2822(s)
        if dt is not None and dt.tzinfo is not None:
            d, tz_seen = dt.astimezone(tz).date(), dt.tzname() or "offset"
        elif dt is not None:
            d = dt.date()
        else:
            m = _ISO_D.search(s)
            if m:
                d = date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
            else:
                d = _words_date(s) or _numeric_date(s, rule.get("date_order"))
    if d is None:
        if re.search(rf"\b({_MONTH_RE})\b", s, re.I) or re.search(r"\d{1,2}[/.]\d{1,2}(?![/.]\d)", s):
            raise Reject(f"date: {s!r} has no year; a full date needs day, month and year")
        raise Reject(f"date: {s!r} is not a calendar date")
    return Parsed(Decimal(d.toordinal()), d, "", f"{s!r} -> {d.isoformat()}", tz_seen)


def parse_datetime_tz(raw: Any, rule: dict, ctx: Context, *, source_tz: str | None = None) -> Parsed:
    """A time of day with a timezone. The zone must come from the RESPONSE: an offset/Z in the
    value, an epoch, an RFC-2822 GMT date, or a timezone field the spec extracts (source_tz)."""
    if rule.get("epoch") or (isinstance(raw, (int, Decimal)) and not isinstance(raw, bool)):
        inst = _epoch(raw, rule.get("epoch"))
        return _skew(inst, ctx, f"epoch {raw}", "UTC")
    s = U.clean_text(str(raw))
    _scope_guard(s, "time")
    dt = _iso_datetime(s) or _rfc2822(s)
    if dt is None:
        if not _TIME.search(s):
            if _ISO_D.search(s) or _words_date(s):
                raise Reject(f"time: {s!r} is a date alone, no time of day")
            raise Reject(f"time: {s!r} has no time of day")
        if not source_tz:
            raise Reject(f"time: {s!r} has no timezone")
        tz = zone(source_tz)
        h, mi, sec, ampm = _clock(s)
        local_today = ctx.fetched_at.astimezone(tz).date()
        best = None
        for day in (local_today - timedelta(days=1), local_today, local_today + timedelta(days=1)):
            cand = datetime.combine(day, time(h, mi, sec), tz)
            if best is None or abs((cand - ctx.fetched_at).total_seconds()) < abs((best - ctx.fetched_at).total_seconds()):
                best = cand
        return _skew(best, ctx, f"{s!r} in {source_tz}", source_tz)
    if dt.tzinfo is None:
        if not source_tz:
            raise Reject(f"time: {s!r} has no timezone")
        return _skew(dt.replace(tzinfo=zone(source_tz)), ctx, f"{s!r} in {source_tz}", source_tz)
    return _skew(dt, ctx, s, dt.tzname() or "offset")


def _clock(s: str) -> tuple[int, int, int, str]:
    m = _TIME.search(s)
    h, mi, sec, ampm = int(m.group(1)), int(m.group(2)), int(m.group(3) or 0), (m.group(4) or "").lower()
    if ampm == "pm" and h < 12:
        h += 12
    if ampm == "am" and h == 12:
        h = 0
    return h, mi, sec, ampm


def _skew(inst: datetime, ctx: Context, detail: str, tz_seen: str) -> Parsed:
    skew = Decimal(str(round((inst - ctx.fetched_at).total_seconds(), 3)))
    return Parsed(skew, inst, "s", f"{detail} -> {inst.isoformat()} (skew {skew}s)", tz_seen)


def parse_timestamp(raw: Any, rule: dict, fetched_at: datetime) -> datetime:
    """Freshness timestamp -> aware UTC datetime. Naive values need `tz:` on the rule."""
    if rule.get("format"):  # explicit format wins: '2026100800' is %Y%m%d%H, not an epoch
        try:
            dt = datetime.strptime(U.clean_text(str(raw)), rule["format"])
        except ValueError:
            raise Reject(f"timestamp: {raw!r} does not match {rule['format']!r}") from None
        if dt.tzinfo is None:
            if not rule.get("tz"):
                raise Reject(f"timestamp: {raw!r} has no timezone and the spec rule declares no tz")
            dt = dt.replace(tzinfo=zone(rule["tz"]))
        return dt.astimezone(timezone.utc)
    if rule.get("epoch") or (isinstance(raw, (int, Decimal)) and not isinstance(raw, bool)):
        return _epoch(raw, rule.get("epoch"))
    s = U.clean_text(str(raw))
    if re.fullmatch(r"\d{9,13}(?:\.\d+)?", s):
        return _epoch(s, rule.get("epoch"))
    declared = rule.get("tz")
    if rule.get("time_of_day"):
        if not declared:
            raise Reject("timestamp: time_of_day rule needs tz")
        tz = zone(declared)
        h, mi, sec, _ = _clock(s) if _TIME.search(s) else (None, None, None, None)
        if h is None:
            raise Reject(f"timestamp: {s!r} has no time of day")
        cand = datetime.combine(fetched_at.astimezone(tz).date(), time(h, mi, sec), tz)
        if cand - fetched_at > timedelta(hours=1):
            cand -= timedelta(days=1)
        return cand.astimezone(timezone.utc)
    dt = _iso_datetime(s) or _rfc2822(s)
    if dt is None:
        m = _ISO_D.search(s)
        d = date(int(m.group(1)), int(m.group(2)), int(m.group(3))) if m else _words_date(s)
        if d is None:
            raise Reject(f"timestamp: cannot read {s!r}")
        dt = datetime.combine(d, time(0, 0))
    if dt.tzinfo is None:
        if not declared:
            raise Reject(f"timestamp: {s!r} has no timezone and the spec rule declares no tz")
        dt = dt.replace(tzinfo=zone(declared))
    return dt.astimezone(timezone.utc)


PARSERS = {
    "boolean": parse_boolean,
    "record_set": parse_record_set,
    "temperature": parse_temperature,
    "price": parse_price,
    "fx_rate": parse_fx_rate,
    "number": parse_number_answer,
    "percent": parse_percent,
    "date": parse_date,
}


def parse_answer(answer_type: str, raw: Any, rule: dict, ctx: Context, *, source_tz: str | None = None) -> Parsed:
    if answer_type == "datetime_tz":
        return parse_datetime_tz(raw, rule, ctx, source_tz=source_tz)
    if answer_type not in PARSERS:
        raise Reject(f"unknown answer_type {answer_type!r}")
    return PARSERS[answer_type](raw, rule, ctx)
