"""Plain-English answers from the YAML template. No raw JSON, no jargon.

Values are rendered in the unit the user asked for (units.render_input + units.render
in the spec). Extra sentences whose facts are missing are dropped, not shown empty.
"""
from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from typing import TYPE_CHECKING, Any

from . import units as U
from .answers import zone
from .spec import IntentSpec

if TYPE_CHECKING:
    from .verify import Result

TEMP_SUFFIX = {"C": "°C", "F": "°F", "K": " K"}
CURRENCY_PREFIX = {"USD": "$", "EUR": "€", "GBP": "£", "JPY": "¥"}


class _Missing(dict):
    def __missing__(self, key: str) -> str:
        raise KeyError(key)


def _money(v: Decimal, code: str) -> str:
    s = U.fmt(v, 2, grouping=True) if abs(v) >= 1 else U.fmt(v, sig=6)
    pre = CURRENCY_PREFIX.get(code.upper())
    return f"{pre}{s}" if pre else f"{s} {code.upper()}"


def render_units(spec: IntentSpec, res: "Result") -> dict[str, str]:
    """{quantity: unit} for display, chosen by the render_input (e.g. unit=F -> F and mph)."""
    choice = None
    if spec.render_input and res.norm:
        choice = res.norm.values.get(spec.render_input)
    table = spec.render_units.get(str(choice)) if choice is not None else None
    return dict(table or {})


def format_value(spec: IntentSpec, value: Any, res: "Result", disp: dict[str, str]) -> str:
    t = spec.answer_type
    if t == "temperature":
        u = disp.get("temperature", "C")
        return f"{U.fmt(U.from_canonical(value, u, 'temperature'), 1)}{TEMP_SUFFIX.get(u, ' ' + u)}"
    if t == "price":
        return _money(value, str(res.norm.vars.get("quote", "USD")) if res.norm else "USD")
    if t == "fx_rate":
        return U.fmt(value, 4) if abs(value) >= Decimal("0.01") else U.fmt(value, sig=4)
    if t == "percent":
        return f"{U.fmt(value, 2)}%"
    if t == "date" and isinstance(value, date):
        return f"{value.strftime('%A')}, {value.day} {value.strftime('%B %Y')}"
    if t == "datetime_tz" and isinstance(value, datetime):
        return value.astimezone(_tz(res)).strftime("%H:%M")
    if t == "boolean":
        return spec.template.get("yes" if value else "no") or ("yes" if value else "no")
    if t == "record_set":
        return ", ".join(value)
    return U.fmt(value) if isinstance(value, Decimal) else str(value)


def _tz(res: "Result"):
    name = (res.norm.vars.get("timezone") if res.norm else None) or "UTC"
    return zone(name)


def format_extra(spec: IntentSpec, name: str, value: Any, disp: dict[str, str]) -> str:
    x = spec.extras[name]
    q = x["quantity"]
    if q == "percent":
        return f"{'+' if x.get('signed') and value > 0 else ''}{U.fmt(value, 2 if x.get('signed') else 0)}%"
    if q == "speed":
        u = disp.get("speed", "km/h")
        return f"{U.fmt(U.from_canonical(value, u, 'speed'), 1)} {u}"
    if q == "temperature":
        u = disp.get("temperature", "C")
        return f"{U.fmt(U.from_canonical(value, u, 'temperature'), 1)}{TEMP_SUFFIX.get(u, ' ' + u)}"
    if q == "datetime" and isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M UTC")
    if q == "direction":
        names = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        return f"{U.fmt(value, 0)}° ({names[int((float(value) % 360 + 22.5) // 45) % 8]})"
    if q == "precipitation":
        return f"{U.fmt(value, 1)} mm/h"
    if q == "boolean":
        return "yes" if value else "no"
    if q == "number" and x.get("unit"):
        return f"{U.fmt(value)} {x['unit']}"
    if isinstance(value, Decimal):
        return U.fmt(value)
    return str(value)


def _vars(spec: IntentSpec, res: "Result", disp: dict[str, str]) -> dict[str, str]:
    v: dict[str, str] = {}
    if res.norm:
        v.update({k: str(x) for k, x in res.norm.vars.items()})
    v["as_of"] = res.as_of.strftime("%H:%M UTC")
    v["confidence"] = f"{res.confidence:.2f}"
    v["queried_count"] = str(len(res.candidates))
    v["answered_count"] = str(len({c.source.publisher for c in res.candidates if c.status == "valid"}))
    v["agreeing_count"] = str(len(res.agreeing))
    v["agreeing_sources"] = ", ".join(c.source.name for c in res.agreeing)
    if res.basis == "authority" and res.primary:
        rest = [c.source.name for c in res.agreeing if c is not res.primary]
        v["verified_by"] = f"the official record holder ({res.primary.source.name})" + (
            f", confirmed by {', '.join(rest)}" if rest else "")
    else:
        v["verified_by"] = f"{len(res.agreeing)} agreeing independent sources ({v['agreeing_sources']})"
    v["reason"] = res.reason
    if res.primary:
        v["primary_source"] = res.primary.source.name
    if res.status == "verified":
        v["value"] = format_value(spec, res.value, res, disp)
        if spec.answer_type == "fx_rate" and res.norm and "amount" in res.norm.values:
            amount, _ = U.parse_number(str(res.norm.values["amount"]))
            if amount is not None:
                v["amount"] = U.fmt(amount)
                v["converted"] = U.fmt(amount * res.value, 2 if amount * res.value >= 1 else None, grouping=True)
        if spec.answer_type == "date":
            v.update(iso_date=res.value.isoformat(), weekday=res.value.strftime("%A"))
        if spec.answer_type == "datetime_tz":
            local = res.value.astimezone(_tz(res))
            off = local.strftime("%z")
            v.update(time=local.strftime("%H:%M"), date=f"{local.day} {local.strftime('%B %Y')}",
                     weekday=local.strftime("%A"), tz_abbr=local.tzname() or "",
                     utc_offset=f"UTC{off[:3]}:{off[3:]}", iso=local.isoformat(timespec="seconds"))
        # extras: first agreeing source (priority order) that has the fact
        for name in spec.extras:
            for c in sorted(res.agreeing, key=lambda c: c.source.priority):
                if name in c.extras:
                    v[name] = format_extra(spec, name, c.extras[name], disp)
                    break
    return v


def _fill(template: str, v: dict[str, str]) -> str | None:
    try:
        return template.format_map(_Missing(v))
    except KeyError:
        return None


def render(spec: IntentSpec, res: "Result") -> str:
    if res.status == "invalid_input":
        return f"I could not understand the question: {res.reason}."
    disp = render_units(spec, res)
    v = _vars(spec, res, disp)
    t = spec.template
    if res.status == "verified" and spec.answer_type == "boolean":
        v["value"] = _fill(v["value"], v) or v["value"]   # yes/no template may itself hold {input} placeholders
    if res.status != "verified":
        return (_fill(t["unverified"], v) or f"I could not verify this. {res.reason}").strip()
    parts = [_fill(t["answer"], v) or ""]
    for sentence in t.get("extras") or []:
        s = _fill(sentence, v)
        if s:
            parts.append(s)
    if t.get("footer"):
        parts.append(_fill(t["footer"], v) or "")
    return " ".join(p.strip() for p in parts if p and p.strip())
