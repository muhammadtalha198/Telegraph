"""End-to-end per intent with mocked APIs: one source per format (JSON, XML, text, HTML, CSV).
Only the correct answer may pass, whatever the format."""
from __future__ import annotations

import unittest
from datetime import datetime, timezone
from decimal import Decimal

from tests.fixtures.formats import (BODIES, CTYPE, EXPECT_LAYER, EXPECT_OVERRIDE, FORMATS, QUESTION, SOURCES,
                                    TRUTH)
from tests.helpers import MockTransport, fetcher, ok, registry, spec_with

from minercheck.verify import verify

REG = registry()
INTENTS = sorted(SOURCES)


def run(intent: str, bodies: dict[str, object], *, formats=FORMATS, now=None, question=None):
    spec = spec_with(intent, sources=[s for s in SOURCES[intent] if s["id"][2:] in formats])
    routes = {}
    for fmt in formats:
        b = bodies.get(fmt, BODIES[intent](fmt, "correct"))
        routes[f"{fmt}.example"] = b if isinstance(b, (tuple, BaseException)) else ok(b, CTYPE[fmt])
    kw = {"now": now} if now else {}
    return spec, verify(spec, question or QUESTION[intent], fetcher=fetcher(MockTransport(routes), **kw),
                        shared=REG.shared, stop_early=False)


def assert_truth(tc: unittest.TestCase, intent: str, res) -> None:
    t = TRUTH[intent]
    if intent == "DATE_TODAY":
        tc.assertEqual(res.value.isoformat(), t)
    elif intent == "TIME_IN_CITY":
        tc.assertEqual(res.value.astimezone(__import__("zoneinfo").ZoneInfo("Asia/Tokyo")).strftime("%Y-%m-%dT%H:%M"), t)
    else:
        tc.assertAlmostEqual(float(res.canonical), t, delta=abs(t) * 0.01)


class EveryFormatCorrect(unittest.TestCase):
    def test_all_five_formats_agree(self):
        for intent in INTENTS:
            with self.subTest(intent=intent):
                _, res = run(intent, {})
                bad = {c.source.id: f"{c.layer}: {c.reason}" for c in res.candidates if c.status != "valid"}
                self.assertEqual(bad, {}, f"{intent}: correct answers rejected")
                self.assertTrue(res.verified, res.reason)
                self.assertEqual({c.doc_format for c in res.candidates}, set(FORMATS))
                self.assertEqual(len(res.agreeing), 5)
                assert_truth(self, intent, res)
                self.assertGreaterEqual(res.confidence, 0.85)
                self.assertNotIn("{", res.answer_text)

    def test_each_format_alone_with_one_partner(self):
        """Each format's correct answer verifies together with one other format."""
        for intent in INTENTS:
            for fmt in FORMATS:
                partner = "json" if fmt != "json" else "csv"
                with self.subTest(intent=intent, fmt=fmt):
                    _, res = run(intent, {}, formats=(fmt, partner))
                    self.assertTrue(res.verified, res.reason)


class BadCasesRejected(unittest.TestCase):
    """For every intent x format x {wrong_type, wrong_entity, stale}: that answer is rejected at the
    right layer, the reason is logged, and the other formats still give the right answer."""

    def test_matrix(self):
        for intent in INTENTS:
            for fmt in FORMATS:
                for case, layer in EXPECT_LAYER.items():
                    layer = EXPECT_OVERRIDE.get((intent, fmt, case), layer)
                    with self.subTest(intent=intent, fmt=fmt, case=case):
                        _, res = run(intent, {fmt: BODIES[intent](fmt, case)})
                        c = next(c for c in res.candidates if c.source.id == f"m-{fmt}")
                        self.assertEqual(c.status, "rejected", f"{case} answer was accepted: {c.parsed and c.parsed.detail}")
                        self.assertEqual(c.layer, layer, c.reason)
                        self.assertTrue(c.reason)
                        self.assertTrue(res.verified, res.reason)       # fallback to the other sources
                        assert_truth(self, intent, res)
                        self.assertNotIn(c, res.agreeing)

    def test_wrong_type_reasons_are_explicit(self):
        _, res = run("DATE_TODAY", {"json": BODIES["DATE_TODAY"]("json", "wrong_type")})
        c = next(c for c in res.candidates if c.source.id == "m-json")
        self.assertIn("weekday only", c.reason)
        _, res = run("TIME_IN_CITY", {"json": BODIES["TIME_IN_CITY"]("json", "wrong_type")})
        self.assertIn("date alone", next(c for c in res.candidates if c.source.id == "m-json").reason)
        _, res = run("CRYPTO_PRICE", {"json": BODIES["CRYPTO_PRICE"]("json", "wrong_type")})
        self.assertIn("percent change", next(c for c in res.candidates if c.source.id == "m-json").reason)
        _, res = run("WEATHER_CHECK", {"json": BODIES["WEATHER_CHECK"]("json", "wrong_type")})
        self.assertIn("no number", next(c for c in res.candidates if c.source.id == "m-json").reason)

    def test_only_wrong_answers_means_could_not_verify(self):
        for intent in INTENTS:
            with self.subTest(intent=intent):
                _, res = run(intent, {f: BODIES[intent](f, "wrong_type") for f in FORMATS})
                self.assertEqual(res.status, "unverified")
                self.assertIsNone(res.value)
                self.assertIn("could not verify", res.answer_text.lower())
                self.assertIn("no source gave a usable answer", res.reason)


class Conflicts(unittest.TestCase):
    CONFLICT = {
        "WEATHER_CHECK": ("xml", lambda b: b.replace("<temp>31.0</temp>", "<temp>45.0</temp>")),
        "CRYPTO_PRICE": ("xml", lambda b: b.replace("82,500.12", "91,000.00")),
        "FX_NOW": ("xml", lambda b: b.replace("1.11982", "1.0526")),
    }

    def test_two_sources_disagree(self):
        for intent, (fmt, mutate) in self.CONFLICT.items():
            with self.subTest(intent=intent):
                bodies = {fmt: mutate(BODIES[intent](fmt, "correct"))}
                _, res = run(intent, bodies, formats=("json", fmt))
                self.assertEqual(res.status, "unverified")
                self.assertIn("sources disagree", res.reason)
                self.assertIn("could not verify", res.answer_text.lower())

    def test_one_outlier_is_outvoted(self):
        for intent, (fmt, mutate) in self.CONFLICT.items():
            with self.subTest(intent=intent):
                _, res = run(intent, {fmt: mutate(BODIES[intent](fmt, "correct"))})
                c = next(c for c in res.candidates if c.source.id == f"m-{fmt}")
                self.assertEqual(c.consensus, "disagreed")
                self.assertTrue(res.verified)
                assert_truth(self, intent, res)

    def test_dates_straddling_midnight_conflict(self):
        near_midnight = datetime(2026, 10, 8, 18, 59, 30, tzinfo=timezone.utc)   # 23:59:30 in Karachi
        bodies = {"json": '{"date": "2026-10-08", "timezone": "Asia/Karachi"}',
                  "xml": "<clock><zone>Asia/Karachi</zone><today>Friday, 9 October 2026</today></clock>"}
        _, res = run("DATE_TODAY", bodies, formats=("json", "xml"), now=near_midnight)
        self.assertTrue(all(c.status == "valid" for c in res.candidates), [c.reason for c in res.candidates])
        self.assertEqual(res.status, "unverified")

    def test_clocks_90s_apart_conflict(self):
        bodies = {"json": '{"datetime": "2026-10-08T15:30:00+09:00", "timezone": "Asia/Tokyo"}',
                  "xml": "<time><zone>Asia/Tokyo</zone><local>2026-10-08T15:31:30</local></time>"}
        _, res = run("TIME_IN_CITY", bodies, formats=("json", "xml"))
        self.assertTrue(all(c.status == "valid" for c in res.candidates))
        self.assertEqual(res.status, "unverified")


class BrokenResponses(unittest.TestCase):
    BROKEN = {
        "json": ok(b"", "application/json"),
        "xml": ok("<weather><obs><temp>31", "application/xml"),
        "text": (500, {"content-type": "text/plain"}, b"Internal Server Error"),
        "html": ok("<html><body><h1>502 Bad Gateway</h1></body></html>", "text/html"),
        "csv": TimeoutError("read timed out"),
    }

    def test_all_broken_never_crashes_and_says_so(self):
        for intent in INTENTS:
            with self.subTest(intent=intent):
                _, res = run(intent, dict(self.BROKEN))
                self.assertEqual(res.status, "unverified")
                self.assertTrue(all(c.status in ("rejected", "error") for c in res.candidates))
                layers = {c.source.id: c.layer for c in res.candidates}
                self.assertEqual(layers["m-text"], "fetch")      # HTTP 500 (after retries)
                self.assertEqual(layers["m-csv"], "fetch")       # timeout
                self.assertEqual(layers["m-json"], "E1")         # empty body
                self.assertIn("I could not verify", res.answer_text)

    def test_each_broken_source_falls_back(self):
        for intent in INTENTS:
            for fmt, broken in self.BROKEN.items():
                with self.subTest(intent=intent, fmt=fmt):
                    _, res = run(intent, {fmt: broken})
                    self.assertTrue(res.verified, res.reason)
                    assert_truth(self, intent, res)

    def test_truncated_json_is_noted_not_guessed(self):
        _, res = run("WEATHER_CHECK", {"json": ok('{"lat": 31.55, "now": {"temp_c": 3', "application/json")})
        c = next(c for c in res.candidates if c.source.id == "m-json")
        self.assertEqual((c.status, c.layer), ("rejected", "E1"))
        self.assertIn("text", c.doc_format)

    def test_lying_content_type(self):
        """JSON served as text/html still parses as JSON: the body decides."""
        body = BODIES["WEATHER_CHECK"]("json", "correct")
        _, res = run("WEATHER_CHECK", {"json": ok(body, "text/html; charset=utf-8")})
        c = next(c for c in res.candidates if c.source.id == "m-json")
        self.assertEqual((c.status, c.doc_format), ("valid", "json"))


class Rendering(unittest.TestCase):
    def test_plain_english_with_extras(self):
        _, res = run("WEATHER_CHECK", {})
        self.assertTrue(res.answer_text.startswith("The temperature in Lahore, Pakistan is 31"))
        self.assertIn("°C", res.answer_text)
        self.assertIn("Humidity is 56%", res.answer_text)
        self.assertNotIn("Wind speed", res.answer_text)          # no source gave wind: sentence dropped

    def test_fahrenheit_requested(self):
        _, res = run("WEATHER_CHECK", {}, question={"location": "Lahore", "unit": "fahrenheit"})
        self.assertIn("87.8°F", res.answer_text)

    def test_price_and_time_text(self):
        _, res = run("CRYPTO_PRICE", {})
        self.assertRegex(res.answer_text, r"^Bitcoin \(BTC\) is \$82,5\d\d\.\d\d\.")
        _, res = run("TIME_IN_CITY", {})
        self.assertRegex(res.answer_text, r"^The time in Tokyo, Japan is 15:30 \(JST, UTC\+09:00\) on Thursday, 8 October 2026\.")
        _, res = run("DATE_TODAY", {})
        self.assertTrue(res.answer_text.startswith("Today's date in Asia/Karachi is Thursday, 8 October 2026."))
        _, res = run("FX_NOW", {})
        self.assertTrue(res.answer_text.startswith("1 USD = 0.8930 EUR."))

    def test_canonical_is_exact_decimal(self):
        _, res = run("CRYPTO_PRICE", {}, formats=("json", "xml"))
        self.assertIsInstance(res.canonical, Decimal)
        self.assertEqual(res.canonical, Decimal("82500.12"))     # no float noise


if __name__ == "__main__":
    unittest.main()
