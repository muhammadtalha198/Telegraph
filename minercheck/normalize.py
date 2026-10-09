"""User inputs in any reasonable form -> one canonical form, before any API call.

  location   "Lahore" | "Paris, Texas" | "Paris, FR" | "31.55,74.34"  -> lat, lon, place, country, timezone
  asset      "BTC" | "bitcoin" | "btc-bitcoin" | "XBT"                  -> symbol + per-API ids (from the spec table)
  currency   "usd" | "US dollar" | "$"                                   -> ISO 4217 code
  timezone   "Asia/Tokyo" | "UTC" | "Tokyo"                              -> IANA zone
  enum/text

Ambiguous names are resolved deterministically (exact qualifier first, then the
largest population) and the choice is reported in `notes`, never silently.
"""
from __future__ import annotations

import difflib
import math
import re
import unicodedata
from dataclasses import dataclass, field
from typing import Any, Callable
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from .errors import InputError
from .spec import IntentSpec

Geocoder = Callable[[str], list[dict]]

_COORDS = re.compile(r"^\s*(-?\d{1,2}(?:\.\d+)?)\s*[, ]\s*(-?\d{1,3}(?:\.\d+)?)\s*$")


@dataclass
class Normalized:
    values: dict[str, Any] = field(default_factory=dict)   # canonical input values by input name
    vars: dict[str, Any] = field(default_factory=dict)     # placeholders for URLs/rules/templates
    entity: dict[str, Any] = field(default_factory=dict)   # what a correct answer must be about
    notes: list[str] = field(default_factory=list)


def fold(s: str) -> str:
    """Case- and accent-insensitive key: 'Zürich' -> 'zurich'."""
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c)).strip().lower()


def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    r = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = p2 - p1, math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def _place_label(p: dict) -> str:
    bits = [p.get("name", "")]
    if p.get("country_code") == "US" and p.get("admin1"):
        bits.append(p["admin1"])
    if p.get("country"):
        bits.append(p["country"])
    return ", ".join(b for b in bits if b)


def _matches_qualifier(p: dict, q: str) -> bool:
    q = fold(q)
    keys = [p.get("country"), p.get("country_code"), p.get("admin1"), p.get("admin1_code")]
    return any(k and fold(str(k)) == q for k in keys)


def resolve_place(raw: str, places: list[dict], geocoder: Geocoder | None) -> tuple[dict, list[str]]:
    """Name or 'name, qualifier' -> place dict. Gazetteer first, then the geocoder."""
    notes: list[str] = []
    name, _, qual = raw.partition(",")
    name, qual = name.strip(), qual.strip()
    if not name:
        raise InputError("location is empty")
    cands = [p for p in places if fold(p["name"]) == fold(name) or fold(name) in [fold(a) for a in p.get("aliases", [])]]
    if not cands and geocoder is not None:
        cands = [g for g in geocoder(name) if fold(g.get("name", "")) == fold(name)] or geocoder(name)
    if qual:
        q = [p for p in cands if _matches_qualifier(p, qual)]
        if not q:
            seen = "; ".join(_place_label(p) for p in cands[:5]) or "no places with that name"
            raise InputError(f"no place {name!r} in {qual!r} (found: {seen})")
        cands = q
    if not cands:
        raise InputError(f"unknown place {raw!r}; pass 'lat,lon' or add it to intents/_shared.yaml places")
    cands = sorted(cands, key=lambda p: -(p.get("population") or 0))
    best = cands[0]
    others = [_place_label(p) for p in cands[1:4] if _place_label(p) != _place_label(best)]
    if others and not qual:
        notes.append(f"'{name}' resolved to {_place_label(best)} (largest); also: {'; '.join(others)}. "
                     f"Add a qualifier like '{name}, {others[0].split(', ')[-1]}' to pick another.")
    return best, notes


def nearest_place(lat: float, lon: float, places: list[dict], max_km: float = 300) -> dict | None:
    best = min(places, key=lambda p: haversine_km(lat, lon, p["lat"], p["lon"]), default=None)
    if best is None or haversine_km(lat, lon, best["lat"], best["lon"]) > max_km:
        return None
    return best


def _location(raw: Any, shared: dict, geocoder: Geocoder | None) -> Normalized:
    places = shared.get("places") or []
    out = Normalized()
    m = _COORDS.match(str(raw))
    if m:
        lat, lon = float(m.group(1)), float(m.group(2))
        if not (-90 <= lat <= 90 and -180 <= lon <= 180):
            raise InputError(f"coordinates out of range: {raw!r}")
        near = nearest_place(lat, lon, places)
        place = {"name": f"{lat:.4f}, {lon:.4f}", "lat": lat, "lon": lon,
                 "country": (near or {}).get("country", ""), "timezone": (near or {}).get("timezone", "")}
        if near:
            out.notes.append(f"coordinates are near {_place_label(near)}")
        label = f"{lat:g}, {lon:g}" + (f" (near {near['name']})" if near else "")
    else:
        place, notes = resolve_place(str(raw), places, geocoder)
        out.notes += notes
        lat, lon = float(place["lat"]), float(place["lon"])
        label = _place_label(place)
    out.vars.update(lat=f"{lat:.4f}", lon=f"{lon:.4f}", place=label,
                    bbox=f"{lat - 0.3:.3f},{lon - 0.3:.3f},{lat + 0.3:.3f},{lon + 0.3:.3f}",
                    country=place.get("country", ""), timezone=place.get("timezone", ""))
    out.entity.update(lat=lat, lon=lon, place=label, country=place.get("country", ""),
                      timezone=place.get("timezone", ""))
    return out


def _asset(raw: Any, table: dict) -> Normalized:
    key = fold(str(raw))
    for sym, row in table.items():
        row = row or {}
        ids = {fold(sym)} | {fold(a) for a in row.get("aliases", [])} | \
              {fold(str(v)) for k, v in row.items() if k not in ("aliases", "name") and isinstance(v, str)}
        if key in ids:
            out = Normalized()
            out.vars.update({k: v for k, v in row.items() if k != "aliases" and v is not None})
            out.vars.update(symbol=sym.upper(), symbol_lower=sym.lower(), asset_name=row.get("name", sym.upper()))
            out.entity.update(symbol=sym.upper(), asset_name=row.get("name", sym.upper()))
            return out
    hint = difflib.get_close_matches(str(raw).upper(), list(table), n=1)
    raise InputError(f"unknown asset {raw!r}" + (f" (did you mean {hint[0]}?)" if hint else "") +
                     "; add it to normalize.assets in the intent spec")


def _table_row(raw: Any, table: dict, what: str) -> tuple[str, dict]:
    """Row key + row for a raw value matching the key, an alias, or any string field."""
    key = fold(str(raw))
    for k, row in table.items():
        row = row or {}
        ids = {fold(str(k))} | {fold(a) for a in row.get("aliases", [])} | \
              {fold(str(v)) for f, v in row.items() if f != "aliases" and isinstance(v, (str, int))}
        if key in ids:
            return str(k), row
    hint = difflib.get_close_matches(str(raw), [str(k) for k in table], n=1)
    raise InputError(f"unknown {what} {raw!r}" + (f" (did you mean {hint[0]}?)" if hint else "") +
                     f"; known: {', '.join(map(str, list(table)[:8]))}")


def _currency(raw: Any, shared: dict) -> str:
    cur = shared.get("currencies") or {}
    codes = {c.upper() for c in cur.get("codes", [])}
    s = str(raw).strip()
    if s.upper() in codes:
        return s.upper()
    names = {fold(k): v for k, v in (cur.get("names") or {}).items()}
    v = names.get(fold(s))
    if v is None:
        raise InputError(f"unknown currency {raw!r}; use an ISO code like USD, EUR, PKR")
    if isinstance(v, list):
        raise InputError(f"currency {raw!r} is ambiguous: {', '.join(v)}")
    return str(v).upper()


def _timezone(raw: Any, shared: dict, geocoder: Geocoder | None) -> tuple[str, str, list[str]]:
    s = str(raw).strip()
    if s.upper() in ("UTC", "GMT", "Z", "ETC/UTC"):
        return "UTC", "UTC", []
    try:
        ZoneInfo(s)
        if "/" in s:
            return s, s, []
    except (ZoneInfoNotFoundError, ValueError):
        pass
    place, notes = resolve_place(s, shared.get("places") or [], geocoder)
    tz = place.get("timezone")
    if not tz:
        raise InputError(f"no timezone known for {s!r}")
    return tz, _place_label(place), notes


def normalize(spec: IntentSpec, raw: dict[str, Any], shared: dict, geocoder: Geocoder | None = None) -> Normalized:
    unknown = [k for k in raw if k not in spec.inputs]
    if unknown:
        hint = difflib.get_close_matches(unknown[0], list(spec.inputs), n=1)
        raise InputError(f"unknown input {unknown[0]!r}" + (f" (did you mean {hint[0]!r}?)" if hint else "") +
                         f"; {spec.intent} takes {', '.join(spec.inputs)}")
    out = Normalized()
    for name, inp in spec.inputs.items():
        v = raw.get(name)
        if v is None or (isinstance(v, str) and not v.strip()):
            if inp.required and inp.default is None:
                raise InputError(f"missing required input {name!r} ({inp.description or inp.kind})")
            v = inp.default
        if v is None:
            continue
        if inp.kind == "location":
            part = _location(v, shared, geocoder)
            out.vars.update(part.vars); out.entity.update(part.entity); out.notes += part.notes
            out.values[name] = part.entity
        elif inp.kind == "asset":
            part = _asset(v, (spec.normalize or {}).get("assets") or {})
            out.vars.update(part.vars); out.entity.update(part.entity)
            out.values[name] = part.entity["symbol"]
        elif inp.kind == "currency":
            code = _currency(v, shared)
            out.values[name] = code
            out.vars.update({name: code, f"{name}_lower": code.lower()})
            out.entity[name] = code
        elif inp.kind == "timezone":
            tz, label, notes = _timezone(v, shared, geocoder)
            out.values[name] = tz
            out.vars.update(timezone=tz, tz_label=label)
            out.entity["timezone"] = tz
            out.notes += notes
        elif inp.kind == "enum":
            s = str(v).strip()
            canon = inp.aliases.get(s.lower()) or next((x for x in inp.values if x.lower() == s.lower()), None)
            if canon is None:
                raise InputError(f"input {name!r}: {v!r} is not one of {', '.join(inp.values)}")
            out.values[name] = canon
            out.vars.update({name: canon, f"{name}_lower": canon.lower()})
        elif inp.kind == "table":
            k, row = _table_row(v, (spec.normalize or {}).get(inp.table) or {}, inp.description or name)
            out.values[name] = k
            out.vars.update({f: x for f, x in row.items() if f != "aliases" and x is not None})
            out.vars.update({name: k, f"{name}_lower": k.lower()})
            if row.get("name"):
                out.entity["name"] = row["name"]          # what the answer must be about (E5)
        else:  # text
            s = str(v).strip()
            out.values[name] = s
            out.vars.update({name: s, f"{name}_lower": s.lower()})
    if "timezone" in out.vars and "tz_label" not in out.vars:
        out.vars["tz_label"] = out.vars.get("place") or out.vars["timezone"]
    return out
