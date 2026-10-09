"""Test helpers: mocked HTTP, fixed clock, spec builders. No network in any test."""
from __future__ import annotations

import copy
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from minercheck.fetch import Fetcher, Request  # noqa: E402
from minercheck.spec import DEFAULT_DIR, IntentSpec, Registry, build  # noqa: E402

NOW = datetime(2026, 10, 8, 6, 30, 0, tzinfo=timezone.utc)

Response = tuple[int, dict[str, str], bytes]


class MockTransport:
    """Route by host (or full URL). A value may be a Response, an Exception, or a callable(req)."""

    def __init__(self, routes: dict[str, Any] | None = None) -> None:
        self.routes: dict[str, Any] = dict(routes or {})
        self.calls: list[Request] = []

    def __call__(self, req: Request) -> Response:
        self.calls.append(req)
        target = self.routes.get(req.url, self.routes.get(urlparse(req.url).hostname or ""))
        if target is None:
            raise OSError(f"no mock route for {req.url}")
        if callable(target) and not isinstance(target, tuple):
            target = target(req)
        if isinstance(target, BaseException):
            raise target
        return target


def ok(body: str | bytes, ctype: str = "application/json", headers: dict | None = None, status: int = 200) -> Response:
    b = body.encode() if isinstance(body, str) else body
    return status, {"content-type": ctype, **(headers or {})}, b


def fetcher(transport: MockTransport, now: datetime = NOW) -> Fetcher:
    return Fetcher(transport, sleep=lambda s: None, clock=lambda: now)


def registry() -> Registry:
    return Registry(DEFAULT_DIR)


def spec_doc(intent: str) -> dict:
    return yaml.safe_load((DEFAULT_DIR / f"{intent}.yaml").read_text(encoding="utf-8"))


def spec_with(intent: str, mutate: Callable[[dict], None] | None = None, sources: list[dict] | None = None) -> IntentSpec:
    """Real spec, optionally with sources replaced / doc mutated."""
    doc = copy.deepcopy(spec_doc(intent))
    if sources is not None:
        doc["sources"] = sources
    if mutate:
        mutate(doc)
    return build(doc)
