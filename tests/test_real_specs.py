"""Real intent specs vs. real API responses recorded on 2026-10-08 (tests/fixtures/live,
refresh with tests/record_live.py). Proves every YAML path matches the live API shape."""
from __future__ import annotations

import json
import unittest
from datetime import datetime

from tests.helpers import ROOT, MockTransport, fetcher, registry  # noqa: F401

from minercheck.verify import build_request, verify
from minercheck.normalize import normalize

LIVE = ROOT / "tests" / "fixtures" / "live"


def replay(intent: str, test_id: str):
    rows = [r for r in json.loads((LIVE / f"{intent}.json").read_text()) if r["test"] == test_id]
    by_url = {}
    for r in rows:
        if r["status"] == "timeout" or (r["status"] != "ok" and r["http_status"] is None):
            by_url[r["url"]] = TimeoutError(r["error"] or "timed out")
        elif r["status"] == "network_error":
            by_url[r["url"]] = OSError(r["error"] or "connection reset")
        else:
            by_url[r["url"]] = (r["http_status"], r["headers"], r["body"].encode())
    when = max(datetime.fromisoformat(r["fetched_at"]) for r in rows)
    return MockTransport(by_url), when


class RealSpecReplay(unittest.TestCase):
    reg = registry()

    def run_case(self, intent: str, test_id: str):
        spec = self.reg.get(intent)
        t = next(x for x in spec.tests if x["id"] == test_id)
        transport, when = replay(intent, test_id)
        res = verify(spec, t["inputs"], fetcher=fetcher(transport, when), shared=self.reg.shared, stop_early=False)
        return spec, res

    def test_every_recorded_case_verifies(self):
        for intent, spec in sorted(self.reg.specs.items()):
            for t in spec.tests:
                with self.subTest(intent=intent, test=t["id"]):
                    _, res = self.run_case(intent, t["id"])
                    self.assertTrue(res.verified, f"{intent}/{t['id']}: {res.reason}")
                    floor = 1 if res.basis == "authority" else 2
                    self.assertGreaterEqual(len(res.agreeing), floor)
                    self.assertNotIn("{", res.answer_text, "unfilled placeholder in answer")

    def test_every_live_source_is_handled_without_crashing(self):
        """Every source's real response reaches a decision (valid or a reasoned reject),
        never an unhandled error. A reject is legitimate (stale daily feed, absent pair);
        the point is that the reader + validators handle every real shape."""
        for intent, spec in sorted(self.reg.specs.items()):
            for t in spec.tests:
                rows = {x["source"]: x for x in json.loads((LIVE / f"{intent}.json").read_text()) if x["test"] == t["id"]}
                _, res = self.run_case(intent, t["id"])
                for c in res.candidates:
                    with self.subTest(intent=intent, test=t["id"], source=c.source.id):
                        self.assertIn(c.status, ("valid", "rejected", "error"))
                        if c.status != "valid":
                            self.assertTrue(c.reason, "a non-valid candidate must say why")
                        # a source that fetched ok must not fail at fetch (would mean replay/transport bug)
                        if rows.get(c.source.id, {}).get("status") == "ok":
                            self.assertNotEqual(c.layer, "fetch", f"{c.source.id}: {c.reason}")

    def test_lahore_weather_verifies_in_range(self):
        # the recorded Lahore snapshot: independent stations agree on a believable temperature
        _, res = self.run_case("WEATHER_CHECK", "lahore")
        self.assertTrue(res.verified, res.reason)
        self.assertTrue(20 <= float(res.canonical) <= 40, res.canonical)

    def test_formats_seen_live(self):
        formats = set()
        for intent in self.reg.specs:
            for t in self.reg.get(intent).tests:
                _, res = self.run_case(intent, t["id"])
                formats |= {c.doc_format for c in res.candidates if c.status == "valid"}
        self.assertLessEqual({"json", "xml", "html", "text", "empty"}, formats)  # empty = header-only clock

    def test_registered_miner_question_builds_known_urls(self):
        spec = self.reg.get("CRYPTO_PRICE")
        src = spec.by_miner("cp-coinbase")
        norm = normalize(spec, src.miner_question, self.reg.shared)
        self.assertEqual(build_request(src, norm.vars).url, "https://api.coinbase.com/v2/prices/BTC-USD/spot")


if __name__ == "__main__":
    unittest.main()
