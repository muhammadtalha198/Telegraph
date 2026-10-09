"""HTTP for free APIs: timeouts, bounded retries, 429/Retry-After, per-host pacing,
TTL cache (so we don't burn free limits), and a pluggable transport for tests.

A fetch never raises. It returns FetchResult with status:
  ok | http_error | rate_limited | timeout | network_error
"""
from __future__ import annotations

import hashlib
import json
import logging
import socket
import threading
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable
from urllib.parse import urlparse

log = logging.getLogger("minercheck.fetch")
UA = "minercheck/1.0 (+https://github.com/telegraph; MinerCreator verifier)"


@dataclass
class Request:
    url: str
    method: str = "GET"
    headers: dict[str, str] = field(default_factory=dict)
    body: bytes | None = None
    timeout_s: float = 15.0


@dataclass
class FetchResult:
    status: str
    url: str
    http_status: int | None = None
    headers: dict[str, str] = field(default_factory=dict)
    body: bytes = b""
    latency_ms: int = 0
    fetched_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    from_cache: bool = False
    error: str = ""
    attempts: int = 1

    @property
    def ok(self) -> bool:
        return self.status == "ok"


# transport(req) -> (http_status, headers, body). Raise TimeoutError / OSError on failure.
Transport = Callable[[Request], tuple[int, dict[str, str], bytes]]


class _NoCrossHostRedirect(urllib.request.HTTPRedirectHandler):
    """Same-host redirects only: a cross-host 30x is not the API answering."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if urlparse(newurl).hostname != urlparse(req.full_url).hostname:
            raise urllib.error.HTTPError(req.full_url, code, f"cross-host redirect to {newurl}", headers, fp)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


_OPENER = urllib.request.build_opener(_NoCrossHostRedirect)


def urllib_transport(req: Request) -> tuple[int, dict[str, str], bytes]:
    headers = {"User-Agent": UA, "Accept": "*/*", **req.headers}
    r = urllib.request.Request(req.url, data=req.body, headers=headers, method=req.method)
    try:
        with _OPENER.open(r, timeout=req.timeout_s) as resp:
            return resp.status, {k.lower(): v for k, v in resp.headers.items()}, resp.read(5_000_000)
    except urllib.error.HTTPError as e:
        body = b""
        try:
            body = e.read(200_000)
        except Exception:  # noqa: BLE001 - body of an error page is best effort
            pass
        return e.code, {k.lower(): v for k, v in (e.headers or {}).items()}, body
    except urllib.error.URLError as e:
        if isinstance(e.reason, (socket.timeout, TimeoutError)):
            raise TimeoutError(str(e.reason)) from e
        raise OSError(str(e.reason)) from e


class Fetcher:
    def __init__(self, transport: Transport | None = None, *, cache_dir: Path | None = None,
                 max_retries: int = 2, max_retry_after_s: float = 10.0, sleep: Callable[[float], None] = time.sleep,
                 clock: Callable[[], datetime] = lambda: datetime.now(timezone.utc)) -> None:
        self.transport = transport or urllib_transport
        self.cache_dir = cache_dir
        self.max_retries = max_retries
        self.max_retry_after_s = max_retry_after_s
        self.sleep = sleep
        self.clock = clock
        self._mem: dict[str, FetchResult] = {}
        self._last_call: dict[str, float] = {}
        self._lock = threading.Lock()
        self.calls = 0  # real network calls (for free-tier accounting)

    # ------------------------------------------------------------ cache
    @staticmethod
    def _key(req: Request) -> str:
        h = hashlib.sha256()
        h.update(json.dumps([req.method, req.url, sorted(req.headers.items()),
                             (req.body or b"").decode("utf-8", "replace")]).encode())
        return h.hexdigest()[:32]

    def _cache_get(self, key: str, ttl_s: int) -> FetchResult | None:
        if ttl_s <= 0:
            return None
        now = self.clock()
        hit = self._mem.get(key)
        if hit is None and self.cache_dir:
            p = self.cache_dir / f"{key}.json"
            if p.is_file():
                try:
                    d = json.loads(p.read_text())
                    hit = FetchResult(status="ok", url=d["url"], http_status=d["http_status"], headers=d["headers"],
                                      body=bytes.fromhex(d["body"]), latency_ms=d["latency_ms"],
                                      fetched_at=datetime.fromisoformat(d["fetched_at"]))
                except (ValueError, KeyError, OSError):
                    hit = None
        if hit and (now - hit.fetched_at).total_seconds() <= ttl_s:
            # fetched_at is kept: freshness / clock-skew checks stay honest on cached answers
            return FetchResult(**{**hit.__dict__, "from_cache": True, "latency_ms": 0})
        return None

    def _cache_put(self, key: str, res: FetchResult) -> None:
        self._mem[key] = res
        if self.cache_dir:
            try:
                self.cache_dir.mkdir(parents=True, exist_ok=True)
                (self.cache_dir / f"{key}.json").write_text(json.dumps({
                    "url": res.url, "http_status": res.http_status, "headers": res.headers, "body": res.body.hex(),
                    "latency_ms": res.latency_ms, "fetched_at": res.fetched_at.isoformat()}))
            except OSError as e:
                log.warning("cache write failed: %s", e)

    # ------------------------------------------------------------ fetch
    def _pace(self, host: str, per_min: int | None) -> None:
        if not per_min:
            return
        gap = 60.0 / per_min
        with self._lock:
            last = self._last_call.get(host)
            wait = 0.0 if last is None else gap - (time.monotonic() - last)
            self._last_call[host] = time.monotonic() + max(wait, 0)
        if wait > 0:
            self.sleep(wait)

    def fetch(self, req: Request, *, cache_ttl_s: int = 0, rate_limit_per_min: int | None = None) -> FetchResult:
        key = self._key(req)
        cached = self._cache_get(key, cache_ttl_s)
        if cached:
            log.debug("cache hit %s", req.url)
            return cached
        host = urlparse(req.url).hostname or ""
        attempts = 0
        last: FetchResult | None = None
        while attempts <= self.max_retries:
            attempts += 1
            self._pace(host, rate_limit_per_min)
            started = time.monotonic()
            fetched_at = self.clock()
            self.calls += 1
            try:
                code, headers, body = self.transport(req)
            except TimeoutError as e:
                last = FetchResult("timeout", req.url, error=f"timed out after {req.timeout_s}s: {e}",
                                   fetched_at=fetched_at, attempts=attempts)
                continue  # retry timeouts
            except OSError as e:
                last = FetchResult("network_error", req.url, error=str(e)[:200], fetched_at=fetched_at, attempts=attempts)
                continue
            latency = int((time.monotonic() - started) * 1000)
            res = FetchResult("ok", req.url, code, headers, body, latency, fetched_at, attempts=attempts)
            if code == 429:
                res.status, res.error = "rate_limited", "HTTP 429 Too Many Requests"
                retry_after = headers.get("retry-after", "")
                wait = float(retry_after) if retry_after.replace(".", "", 1).isdigit() else 2.0 * attempts
                if wait > self.max_retry_after_s or attempts > self.max_retries:
                    return res  # do not hammer a free tier
                self.sleep(wait)
                last = res
                continue
            if code >= 500:
                res.status, res.error = "http_error", f"HTTP {code}"
                last = res
                self.sleep(0.5 * attempts)
                continue
            if not 200 <= code < 300:
                # 4xx will not fix itself; a 3xx here is a refused cross-host redirect
                res.status, res.error = "http_error", f"HTTP {code}"
                if 300 <= code < 400:
                    res.error += f" cross-host redirect to {headers.get('location', '?')} (refused: not the API answering)"
                return res
            self._cache_put(key, res)
            return res
        assert last is not None
        return last
