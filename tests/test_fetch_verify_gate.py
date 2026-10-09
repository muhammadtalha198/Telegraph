"""fetch.py, verify.py (E3 + confidence), scoring.py, gate.py."""
from __future__ import annotations

import json
import tempfile
import unittest
from datetime import timedelta
from decimal import Decimal
from pathlib import Path

import yaml

from tests.fixtures.formats import BODIES, CTYPE, SOURCES
from tests.helpers import NOW, MockTransport, fetcher, ok, registry, spec_with

from minercheck.answers import Parsed
from minercheck.fetch import Fetcher, Request
from minercheck.gate import gate_miner, node_request
from minercheck.spec import DEFAULT_DIR
from minercheck.validate import Candidate
from minercheck.verify import cross_check, verify

REG = registry()


class Fetching(unittest.TestCase):
    def test_cache_keeps_original_fetch_time(self):
        t = MockTransport({"a.example": ok("{}")})
        clock = [NOW]
        f = Fetcher(t, sleep=lambda s: None, clock=lambda: clock[0])
        r1 = f.fetch(Request("https://a.example/x"), cache_ttl_s=60)
        clock[0] = NOW + timedelta(seconds=30)
        r2 = f.fetch(Request("https://a.example/x"), cache_ttl_s=60)
        self.assertTrue(r2.from_cache)
        self.assertEqual(r2.fetched_at, r1.fetched_at)          # freshness stays honest
        clock[0] = NOW + timedelta(seconds=61)
        self.assertFalse(f.fetch(Request("https://a.example/x"), cache_ttl_s=60).from_cache)
        self.assertEqual(len(t.calls), 2)

    def test_disk_cache(self):
        with tempfile.TemporaryDirectory() as d:
            t = MockTransport({"a.example": ok("{\"v\": 1}")})
            Fetcher(t, cache_dir=Path(d), clock=lambda: NOW).fetch(Request("https://a.example/"), cache_ttl_s=60)
            r = Fetcher(MockTransport(), cache_dir=Path(d), clock=lambda: NOW).fetch(Request("https://a.example/"), cache_ttl_s=60)
            self.assertTrue(r.from_cache)
            self.assertEqual(r.body, b'{"v": 1}')

    def test_429_retry_after_then_ok(self):
        seq = [(429, {"retry-after": "1"}, b""), ok("{}")]
        slept = []
        f = Fetcher(MockTransport({"a.example": lambda req: seq.pop(0)}), sleep=slept.append, clock=lambda: NOW)
        r = f.fetch(Request("https://a.example/"))
        self.assertTrue(r.ok)
        self.assertEqual((r.attempts, slept), (2, [1.0]))

    def test_429_long_retry_after_is_not_waited(self):
        slept = []
        f = Fetcher(MockTransport({"a.example": (429, {"retry-after": "3600"}, b"")}), sleep=slept.append, clock=lambda: NOW)
        r = f.fetch(Request("https://a.example/"))
        self.assertEqual((r.status, slept), ("rate_limited", []))

    def test_5xx_and_timeout_retried_4xx_not(self):
        t = MockTransport({"a.example": (503, {}, b""), "b.example": TimeoutError("slow"), "c.example": (404, {}, b"")})
        f = fetcher(t)
        self.assertEqual((f.fetch(Request("https://a.example/")).status, f.fetch(Request("https://b.example/")).status),
                         ("http_error", "timeout"))
        self.assertEqual(f.fetch(Request("https://c.example/")).attempts, 1)
        self.assertEqual(sum(1 for c in t.calls if "a.example" in c.url), 3)       # 1 + max_retries

    def test_redirect_error_says_where(self):
        f = fetcher(MockTransport({"a.example": (301, {"location": "https://b.example/"}, b"")}))
        self.assertIn("redirect to https://b.example/", f.fetch(Request("https://a.example/")).error)


def cand(spec, sid: str, value: str, publisher: str | None = None) -> Candidate:
    src = next(s for s in spec.sources if s.id == sid)
    if publisher:
        src = type(src)(**{**src.__dict__, "publisher": publisher})
    c = Candidate(source=src, status="valid")
    c.parsed = Parsed(Decimal(value), Decimal(value), "C", value)
    return c


class CrossCheck(unittest.TestCase):
    spec = REG.get("WEATHER_CHECK")      # tolerance abs 3, min_sources 2

    def test_docstring_example(self):
        cs = [cand(self.spec, "open-meteo", "31.0"), cand(self.spec, "met-norway", "30.8"), cand(self.spec, "wttr", "35.0")]
        agreeing, value = cross_check(self.spec, cs)
        self.assertEqual([c.source.id for c in agreeing], ["open-meteo", "met-norway"])
        self.assertEqual(value, Decimal("30.9"))
        self.assertEqual(cs[2].consensus, "disagreed")

    def test_split_and_single_are_not_verified(self):
        cs = [cand(self.spec, "open-meteo", "10"), cand(self.spec, "met-norway", "10"),
              cand(self.spec, "wttr", "30"), cand(self.spec, "noaa-metar", "30")]
        self.assertEqual(cross_check(self.spec, cs), ([], None))
        self.assertEqual(cross_check(self.spec, [cand(self.spec, "open-meteo", "10")]), ([], None))

    def test_one_vote_per_publisher(self):
        cs = [cand(self.spec, "open-meteo", "40"), cand(self.spec, "met-norway", "40", publisher="open-meteo.com"),
              cand(self.spec, "wttr", "20"), cand(self.spec, "noaa-metar", "20.5")]
        agreeing, value = cross_check(self.spec, cs)
        self.assertEqual(cs[1].consensus, "duplicate_publisher")
        self.assertEqual({c.source.id for c in agreeing}, {"wttr", "noaa-metar"})   # the clone does not outvote

    def test_minority_cannot_win(self):
        cs = [cand(self.spec, s, v) for s, v in
              [("open-meteo", "10"), ("met-norway", "11"), ("wttr", "40"), ("noaa-metar", "60"), ("7timer", "80")]]
        self.assertEqual(cross_check(self.spec, cs), ([], None))

    def test_stop_early_saves_calls(self):
        spec = spec_with("WEATHER_CHECK", sources=SOURCES["WEATHER_CHECK"],
                         mutate=lambda d: d["validation"]["cross_check"].update(target_sources=2))
        t = MockTransport({f"{f}.example": ok(BODIES["WEATHER_CHECK"](f, "correct"), CTYPE[f]) for f in ("json", "xml", "text", "html", "csv")})
        res = verify(spec, {"location": "Lahore"}, fetcher=fetcher(t), shared=REG.shared)
        self.assertTrue(res.verified)
        self.assertEqual(len(t.calls), 2)   # stopped after target_sources=2 agreed


class Gate(unittest.TestCase):
    def test_node_request_matches_node(self):
        doc = {"base_url": "https://open.er-api.com", "endpoints": [{"external_path": "/v6/latest/{base}"}],
               "input_schema": {"properties": {"base": {"default": "USD"}, "x": {"default": "a b"}}}}
        self.assertEqual(node_request(doc), ("GET", "https://open.er-api.com/v6/latest/USD?x=a+b"))
        doc = {"base_url": "https://h", "endpoints": [{"external_path": "/addresses/{address}", "method": "post",
                                                         "endpoint_base_url": "https://e/"}],
               "input_schema": {"properties": {"address": {"default": "0xAb/1"}}}}
        self.assertEqual(node_request(doc), ("POST", "https://e/addresses/0xAb%2F1"))

    def _yaml(self, d: str, slug: str, url_path: str, default: str) -> Path:
        p = Path(d) / f"{slug}.yaml"
        p.write_text(yaml.safe_dump({
            "version": "1", "kind": "miner", "id": 1, "slug": slug, "base_url": "https://api.coinbase.com",
            "endpoints": [{"path": "/query", "external_path": url_path, "method": "GET"}],
            "input_schema": {"properties": {"pair": {"type": "string", "default": default}}}}))
        return p

    def transport(self, coinbase_body: str) -> MockTransport:
        return MockTransport({
            "api.coinbase.com": ok(coinbase_body),
            "api.coingecko.com": ok('{"bitcoin": {"usd": 82500, "last_updated_at": %d}}' % int(NOW.timestamp())),
            "api.kraken.com": ok('{"error": [], "result": {"XXBTZUSD": {"c": ["82510.0", "1"]}}}'),
            "api.binance.com": ok('{"symbol": "BTCUSDT", "lastPrice": "82520.0", "closeTime": %d}' % (int(NOW.timestamp()) * 1000)),
        })

    def gate(self, y, intent, transport):
        return gate_miner(y, intent, REG, fetcher=fetcher(transport))

    def test_pass_right_answer(self):
        with tempfile.TemporaryDirectory() as d:
            y = self._yaml(d, "cp-coinbase", "/v2/prices/{pair}/spot", "BTC-USD")
            r = self.gate(y, "CRYPTO_PRICE", self.transport('{"data": {"amount": "82505.5", "base": "BTC", "currency": "USD"}}'))
            self.assertEqual(r.verdict, "PASS", "\n".join(r.lines))
            self.assertIn("https://api.coinbase.com/v2/prices/BTC-USD/spot", "\n".join(r.lines))

    def test_fail_wrong_entity(self):
        with tempfile.TemporaryDirectory() as d:
            y = self._yaml(d, "cp-coinbase", "/v2/prices/{pair}/spot", "BTC-USD")
            r = self.gate(y, "CRYPTO_PRICE", self.transport('{"data": {"amount": "2550.1", "base": "ETH", "currency": "USD"}}'))
            self.assertEqual(r.verdict, "FAIL")
            self.assertIn("wrong asset", r.reason)

    def test_fail_disagrees(self):
        with tempfile.TemporaryDirectory() as d:
            y = self._yaml(d, "cp-coinbase", "/v2/prices/{pair}/spot", "BTC-USD")
            r = self.gate(y, "CRYPTO_PRICE", self.transport('{"data": {"amount": "95000", "base": "BTC", "currency": "USD"}}'))
            self.assertEqual(r.verdict, "FAIL")
            self.assertIn("disagree", r.reason)

    def test_skip_judgment_intent(self):
        # LANGUAGE_TRANSLATION is NON-DETERMINISTIC -> judgment tier -> SKIP (LLM judge, no deterministic truth)
        with tempfile.TemporaryDirectory() as d:
            y = self._yaml(d, "cp-coinbase", "/v2/prices/{pair}/spot", "BTC-USD")
            r = self.gate(y, "LANGUAGE_TRANSLATION", self.transport('{}'))
            self.assertEqual(r.verdict, "SKIP")
            self.assertTrue(r.ok)

    def test_fail_unmapped_slug(self):
        with tempfile.TemporaryDirectory() as d:
            y = self._yaml(d, "cp-unmapped", "/v2/prices/{pair}/spot", "BTC-USD")
            r = self.gate(y, "CRYPTO_PRICE", self.transport('{"data": {"amount": "82505.5", "base": "BTC", "currency": "USD"}}'))
            self.assertEqual(r.verdict, "FAIL")
            self.assertIn("no source with miner.slug: cp-unmapped", r.reason)

    def test_fail_no_spec_for_required_catalog_intent(self):
        # a deterministic catalog intent with no intents/*.yaml must FAIL closed (not SKIP)
        with tempfile.TemporaryDirectory() as d:
            y = self._yaml(d, "sku-x", "/x", "1")
            r = self.gate(y, "SKU_IN_STOCK", self.transport('{}'))
            self.assertEqual(r.verdict, "FAIL")
            self.assertIn("no spec for catalog intent", r.reason)

    def test_blocked_unverifiable_catalog_intent(self):
        with tempfile.TemporaryDirectory() as d:
            y = self._yaml(d, "port-x", "/x", "1")
            r = self.gate(y, "LIVE_PORT_CONGESTION", self.transport('{}'))
            self.assertEqual(r.verdict, "BLOCKED")
            self.assertIn("Verifiable=No", r.reason)

    def test_fail_wrong_kind_per_catalog(self):
        # a CEX order book mapped under LIQUIDITY (decentralized pools) fails the kind check
        with tempfile.TemporaryDirectory() as d:
            y = Path(d) / "liq-bingx-book.yaml"
            y.write_text(yaml.safe_dump({"version": "1", "kind": "miner", "id": 1, "slug": "liq-bingx-book",
                "base_url": "https://open-api.bingx.com",
                "endpoints": [{"path": "/q", "external_path": "/openApi/spot/v1/market/depth", "method": "GET"}],
                "input_schema": {"properties": {}}}))
            r = self.gate(y, "LIQUIDITY_DEPTH_VERIFY", MockTransport({}))
            self.assertEqual(r.verdict, "FAIL")
            self.assertIn("cex source", r.reason)


if __name__ == "__main__":
    unittest.main()
