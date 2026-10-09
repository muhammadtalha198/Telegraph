"""Verification: run sources, validate each, cross-check (E3) or official record holder, confidence.

E3 rule, in plain words:
  * One vote per publisher (Frankfurter and VATcomply are both ECB -> one vote).
  * Find the biggest group of publishers whose answers sit within the YAML tolerance of
    one of them. Its median is the consensus; a publisher "agrees" if it is within
    tolerance of that consensus.
  * Verified only if at least `min_sources` publishers agree AND they are a strict
    majority of the publishers that gave a valid answer. Otherwise: "could not verify".
    A source never agrees with itself: a group needs 2+ independent publishers.

Example (temperature, tolerance 3 C): Open-Meteo 31.0, MET Norway 30.8, wttr 35.0
  biggest group: {31.0, 30.8} (35.0 is 4.0 away) -> consensus median 30.9 C
  Open-Meteo off 0.1, MET Norway off 0.1 -> agree; wttr off 4.1 -> disagrees
  -> 2 of 3 agree (a majority): answer 30.9 C
"""
from __future__ import annotations

import logging
import statistics
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Iterable
from urllib.parse import quote

from .errors import ExtractError, InputError
from .fetch import Fetcher, Request
from .normalize import Geocoder, Normalized, normalize
from .reader import interpolate
from .spec import IntentSpec, SourceSpec
from .validate import Candidate, validate

log = logging.getLogger("minercheck.verify")


@dataclass
class Result:
    intent: str
    status: str                        # verified | unverified | invalid_input
    question: dict[str, Any] = field(default_factory=dict)
    value: Any = None                  # consensus display value (Decimal canonical unit | date | datetime)
    canonical: Decimal | None = None
    confidence: float = 0.0
    candidates: list[Candidate] = field(default_factory=list)
    agreeing: list[Candidate] = field(default_factory=list)
    primary: Candidate | None = None
    reason: str = ""
    notes: list[str] = field(default_factory=list)
    as_of: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    answer_text: str = ""
    run_id: str = field(default_factory=lambda: uuid.uuid4().hex[:12])
    norm: Normalized | None = None
    basis: str = ""                    # consensus | authority

    @property
    def verified(self) -> bool:
        return self.status == "verified"

    def to_dict(self) -> dict:
        def val(x: Any) -> Any:
            return x.isoformat() if hasattr(x, "isoformat") else (str(x) if isinstance(x, Decimal) else x)
        return {
            "intent": self.intent, "status": self.status, "basis": self.basis, "question": self.question,
            "answer": self.answer_text, "value": val(self.value),
            "canonical": None if self.canonical is None else str(self.canonical),
            "confidence": self.confidence, "reason": self.reason, "notes": self.notes,
            "as_of": self.as_of.isoformat(), "run_id": self.run_id,
            "agreeing_sources": [c.source.id for c in self.agreeing],
            "sources": [{
                "id": c.source.id, "publisher": c.source.publisher, "miner": c.source.miner_slug,
                "status": c.status, "layer": c.layer, "reason": c.reason, "consensus": c.consensus,
                "value": None if c.parsed is None else val(c.parsed.display),
                "format": c.doc_format, "latency_ms": c.fetch.latency_ms if c.fetch else None,
                "checks": [{"layer": layer, "ok": ok, "detail": d} for layer, ok, d in c.checks],
            } for c in self.candidates],
        }


def build_request(src: SourceSpec, variables: dict[str, Any]) -> Request:
    """Fill {placeholders}. URL values are percent-encoded; headers/body are not."""
    enc = {k: quote(str(v), safe="/:,@") for k, v in variables.items()}
    return Request(url=interpolate(src.url, enc), method=src.method,
                   headers={k: interpolate(v, variables) for k, v in src.headers.items()},
                   body=interpolate(src.body, variables).encode() if src.body else None, timeout_s=src.timeout_s)


def _median(xs: list[Decimal]) -> Decimal:
    return statistics.median(xs)  # Decimal in, Decimal out (even count = mean of the middle two)


def cross_check(spec: IntentSpec, cands: Iterable[Candidate]) -> tuple[list[Candidate], Decimal | None]:
    """E3. Marks candidate.consensus; returns (agreeing, consensus_value)."""
    by_pub: dict[str, Candidate] = {}
    for c in sorted((c for c in cands if c.status == "valid"), key=lambda c: c.source.priority):
        if c.source.publisher in by_pub:
            c.consensus = "duplicate_publisher"
            c.checks.append(("E3", False, f"same publisher as {by_pub[c.source.publisher].source.id}; not an independent vote"))
            continue
        by_pub[c.source.publisher] = c
    voters = list(by_pub.values())
    if len(voters) < 2:
        for c in voters:
            c.checks.append(("E3", False, "no other independent source to compare with"))
        return [], None
    val = lambda c: c.parsed.canonical  # noqa: E731
    best: list[Candidate] = []
    for center in voters:  # biggest group within tolerance of one member; ties -> tighter group
        tol = spec.validation.tolerance(val(center))
        group = [o for o in voters if abs(val(o) - val(center)) <= tol]
        spread = max(val(o) for o in group) - min(val(o) for o in group)
        if len(group) > len(best) or (len(group) == len(best) and best and
                                      spread < max(map(val, best)) - min(map(val, best))):
            best = group
    value = _median([val(c) for c in best])
    tol = spec.validation.tolerance(value)
    agreeing = [c for c in voters if abs(val(c) - value) <= tol]
    for c in voters:
        c.deviation, c.tolerance = abs(val(c) - value), tol
    if len(agreeing) >= spec.validation.min_sources and len(agreeing) * 2 > len(voters):
        value = _median([val(c) for c in agreeing])
        for c in voters:
            c.consensus = "agreed" if c in agreeing else "disagreed"
            c.checks.append(("E3", c in agreeing, f"{val(c)} vs consensus {value}: off {c.deviation} (tolerance {tol})"))
        return agreeing, value
    for c in voters:
        c.consensus = "disagreed"
        c.checks.append(("E3", False, f"{val(c)}: no majority of independent sources agrees within tolerance"))
    return [], None


def confidence(spec: IntentSpec, agreeing: list[Candidate], voters: int, value: Decimal) -> float:
    """unanimity x support x tightness x freshness, each in [0,1]. Plain and explainable:
      unanimity = agreeing / independent valid answers
      support   = agreeing / target_sources (capped at 1)
      tightness = 1 - 0.5 * (worst agreeing deviation / tolerance)
      freshness = 0.9 + 0.1 * share of agreeing answers with a proven timestamp/clock"""
    if not agreeing or not voters:
        return 0.0
    unanimity = len(agreeing) / voters
    support = min(1.0, len(agreeing) / spec.validation.target_sources)
    tol = spec.validation.tolerance(value)
    worst = max(abs(c.parsed.canonical - value) for c in agreeing)
    tight = 1.0 if tol == 0 else max(0.5, 1 - 0.5 * float(worst / tol))
    proven = sum(1 for c in agreeing if c.timestamp is not None or spec.answer_type in ("date", "datetime_tz"))
    fresh = 0.9 + 0.1 * proven / len(agreeing)
    return round(unanimity * support * tight * fresh, 2)


def run_candidate(spec: IntentSpec, src: SourceSpec, norm: Normalized, fetcher: Fetcher) -> Candidate:
    cand = Candidate(source=src)
    try:
        req = build_request(src, norm.vars)
    except ExtractError as e:
        return cand.reject("fetch", f"cannot build request: {e}", error=True)
    cand.fetch = fetcher.fetch(req, cache_ttl_s=src.cache_ttl_s, rate_limit_per_min=src.rate_limit_per_min)
    return validate(spec, cand, norm)


def verify(spec: IntentSpec, inputs: dict[str, Any], *, fetcher: Fetcher, shared: dict,
           geocoder: Geocoder | None = None, only: Iterable[str] | None = None, stop_early: bool = True,
           extra_candidates: Iterable[Candidate] = ()) -> Result:
    """Answer one question. Sources are tried in YAML priority order; once `target_sources`
    independent publishers agree we stop (saves free-tier calls). A failing or wrong source
    simply means the next one is tried."""
    res = Result(intent=spec.intent, status="unverified")
    try:
        norm = normalize(spec, inputs, shared, geocoder)
    except InputError as e:
        res.status, res.reason = "invalid_input", str(e)
        return res
    res.norm, res.question, res.notes = norm, norm.values, list(norm.notes)
    cands: list[Candidate] = list(extra_candidates)
    pinned = {c.source.id for c in cands}
    wanted = set(only) if only else None
    for src in spec.sources:
        if not src.enabled or src.id in pinned or (wanted is not None and src.id not in wanted):
            continue
        if any(str(norm.values.get(k)) != v for k, v in src.when.items()):
            continue   # source does not apply to this question (e.g. wrong market/authority)
        try:
            build_request(src, norm.vars)
        except ExtractError as e:
            # the asked asset/series has no id for this source (e.g. no Kraken pair): not asked, not a failure
            res.notes.append(f"{src.name} not asked: {e}")
            continue
        cands.append(run_candidate(spec, src, norm, fetcher))
        if stop_early:
            agreeing, _ = cross_check(spec, [c for c in cands if c.status == "valid"])
            for c in cands:  # cross_check is re-run at the end; drop interim marks
                c.checks = [x for x in c.checks if x[0] != "E3"]
                c.consensus = ""
            if len({c.source.publisher for c in agreeing}) >= spec.validation.target_sources:
                break
    res.candidates = cands
    agreeing, value = cross_check(spec, cands)
    voters = len({c.source.publisher for c in cands if c.status == "valid"})
    authority = authority_check(spec, cands)
    if authority is not None:
        agreeing, value = authority
        res.basis = "authority"
        res.primary = agreeing[0]
        others = len(agreeing) - 1
        res.confidence = round(0.8 + 0.2 * min(1.0, others / max(1, spec.validation.target_sources - 1)), 2)
    elif agreeing and value is not None:
        res.basis = "consensus"
        res.primary = min(agreeing, key=lambda c: c.source.priority)
        res.confidence = confidence(spec, agreeing, voters, value)
    if res.basis:
        res.status, res.canonical, res.agreeing = "verified", value, agreeing
        res.value = _display(spec, value, res.primary)
    else:
        res.reason = _why_unverified(spec, cands, voters)
    res.as_of = max((c.fetch.fetched_at for c in cands if c.fetch), default=res.as_of)
    from .render import render  # local import: render depends on verify.Result
    res.answer_text = render(spec, res)
    return res


def authority_check(spec: IntentSpec, cands: list[Candidate]) -> tuple[list[Candidate], Decimal] | None:
    """An official record holder (source.authority, reviewed in the spec) that gives a valid answer
    defines the answer: a company register for its companies, an exchange for its own notices.
    Other publishers are then marked agreed/disagreed against it. Returns (agreeing, value) or None."""
    auth = sorted((c for c in cands if c.status == "valid" and c.source.authority), key=lambda c: c.source.priority)
    if not auth:
        return None
    a = auth[0]
    value = a.parsed.canonical
    tol = spec.validation.tolerance(value)
    seen: set[str] = set()
    agreeing = []
    for c in sorted((c for c in cands if c.status == "valid"), key=lambda c: (c is not a, c.source.priority)):
        if c.source.publisher in seen:
            continue
        seen.add(c.source.publisher)
        c.deviation, c.tolerance = abs(c.parsed.canonical - value), tol
        ok = c.deviation <= tol
        c.consensus = "agreed" if ok else "disagreed"
        c.checks = [x for x in c.checks if x[0] != "E3"]
        c.checks.append(("E3", ok, "official record holder" if c is a else
                         f"{c.parsed.canonical} vs official {a.source.name} {value}: off {c.deviation} (tolerance {tol})"))
        if ok:
            agreeing.append(c)
    return agreeing, value


def _display(spec: IntentSpec, value: Decimal, primary: Candidate) -> Any:
    if spec.answer_type == "boolean":
        return bool(int(value))
    if spec.answer_type == "record_set":
        return primary.parsed.display
    if spec.answer_type == "date":
        from datetime import date
        return date.fromordinal(int(value))
    if spec.answer_type == "datetime_tz":
        from datetime import timedelta
        return primary.fetch.fetched_at + timedelta(seconds=float(value))
    return value


def _why_unverified(spec: IntentSpec, cands: list[Candidate], voters: int) -> str:
    valid = [c for c in cands if c.status == "valid"]
    if not cands:
        return "no source is enabled for this question"
    if not valid:
        worst = "; ".join(f"{c.source.name}: {c.reason}" for c in cands[:4])
        return f"no source gave a usable answer ({worst})"
    if voters < spec.validation.min_sources:
        c = valid[0]
        return (f"only {voters} independent source answered ({c.source.name}); "
                f"{spec.validation.min_sources} must agree")
    vals = ", ".join(f"{c.source.name} {c.parsed.canonical}" for c in valid if c.consensus != "duplicate_publisher")
    return f"sources disagree ({vals})"
