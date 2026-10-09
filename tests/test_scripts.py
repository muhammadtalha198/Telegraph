"""Regression tests for the bugs fixed in scripts/ (see docs/ANALYSIS_REPORT.md)."""
from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tests.helpers import ROOT

sys.path.insert(0, str(ROOT / "scripts"))

import auto_review_samples as ar  # noqa: E402
import capture_api_output as cap  # noqa: E402
import generate_yamls_from_approved_samples as gen  # noqa: E402
import pin_consistency_check as pin  # noqa: E402
import register_gates_v2 as rg  # noqa: E402
import set_sample_status as sss  # noqa: E402
from sample_file import parse_front_matter, parse_sample, raw_body, replace_or_add  # noqa: E402

from minercheck.sample_check import check_sample  # noqa: E402


def sample_text(url: str, body: str, *, status="approved", captured="2026-10-08T06:00:00Z", fence="json",
                slug="x", intent="CRYPTO_PRICE", extra="") -> str:
    lines = ["---", f"intent: {intent}", f"slug: {slug}", f"status: {status}", f"captured_at: {captured}",
             f"request_url: {url}", "content_type: application/json", "inputs: |", "  (none)"]
    lines += [x for x in extra.splitlines() if x]
    lines += ['reviewer_note: ""', 'reviewed_at: ""', "---", "", "## Raw API output", "", f"```{fence}", body, "```",
              "", "## Why this matches (or not)", "", "_pending_", ""]
    return "\n".join(lines)


def quiet(fn, *a, **kw):
    with contextlib.redirect_stdout(io.StringIO()) as out, contextlib.redirect_stderr(io.StringIO()):
        rc = fn(*a, **kw)
    return rc, out.getvalue()


class GateRequestShape(unittest.TestCase):
    def test_path_params_are_substituted_like_the_node(self):
        _m, url = rg.yaml_request(ROOT / "intentYamls/onchain-metric/ocm-blockscout-gnosis.yaml")
        self.assertEqual(url, "https://gnosis.blockscout.com/api/v2/addresses/0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045")
        _m, url = rg.yaml_request(ROOT / "intentYamls/fx-now/fx-er-api.yaml")
        self.assertEqual(url, "https://open.er-api.com/v6/latest/USD")

    def test_same_question(self):
        self.assertTrue(rg.same_question("https://mainnet.base.org", "https://mainnet.base.org/"))
        self.assertTrue(rg.same_question("https://h/p?b=2&a=1&c=", "https://h/p?a=1&b=2"))
        self.assertFalse(rg.same_question("https://api.coingecko.com/x?ids=bitcoin", "https://api.coingecko.com/x?ids=ethereum"))
        self.assertFalse(rg.same_question("https://services.nvd.nist.gov/x?cveId=1", "https://omni/truth/nvd-cvss?cve_id=1"))

    def test_family_body_beats_header(self):
        self.assertEqual(rg._family("text/html", b'{"a": 1}'), "json")
        self.assertEqual(rg._family("image/png", b"\x89PNG"), "binary")

    def test_skip_flags_need_unsafe(self):
        y = ROOT / "intentYamls/fx-now/fx-er-api.yaml"
        s = ROOT / "apiOutputSamples/FX_NOW/fx-er-api.md"
        for flag in ("--skip-live", "--skip-verify"):
            with self.subTest(flag=flag), mock.patch.object(sys, "argv", ["x", "--file", str(y), "--sample", str(s), flag]), \
                    mock.patch.dict("os.environ", {"ALLOW_UNSAFE_REGISTER": ""}), mock.patch.object(rg, "run_cmd") as run:
                rc, out = quiet(rg.main)
                self.assertEqual(rc, 1)
                self.assertIn("requires ALLOW_UNSAFE_REGISTER=1", out)
                run.assert_not_called()                      # refused before any gate ran


class SampleFiles(unittest.TestCase):
    def test_any_fence_and_inner_backticks(self):
        t = sample_text("u", "<a>1</a>", fence="xml")
        self.assertEqual(raw_body(t), "<a>1</a>")
        t = sample_text("u", '{"d": "see:\\n```\\nzip -d x\\n```\\nend"}')
        self.assertEqual(raw_body(t), '{"d": "see:\\n```\\nzip -d x\\n```\\nend"}')   # not cut at the inner fence

    def test_notes_with_backslashes(self):
        fm = parse_front_matter(sample_text("u", "{}"))
        self.assertEqual(fm["status"], "approved")
        block = "status: pending\nreviewer_note: \"\"\n"
        out = replace_or_add(block, "reviewer_note", r"regex \1 and \g<0> and C:\path")
        self.assertIn(r"\\1", out)
        (ROOT / "out").mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=ROOT / "out") as d:     # the script prints paths relative to the repo
            p = Path(d) / "s.md"
            p.write_text(sample_text("u", "{}"))
            with mock.patch.object(sys, "argv", ["x", "--file", str(p), "--status", "rejected", "--note", r"bad \1 \g<x>"]):
                rc, _ = quiet(sss.main)
            self.assertEqual(rc, 0)
            self.assertEqual(parse_sample(p)["meta"]["status"], "rejected")


class HardCheck(unittest.TestCase):
    def test_structured_payload_keys_do_not_trigger(self):
        self.assertIsNone(ar.hard_check('{"resources": {"rate_limit": {"limit": 60}}, "title": "Not Found Fixer"}'))
        self.assertIsNotNone(ar.hard_check('{"status": "error", "message": "Rate limit exceeded", "code": 429, "x": 1}'))
        self.assertEqual(ar.hard_check('{"error": "bad", "code": 1}'), "JSON error object")
        self.assertIsNotNone(ar.hard_check("<!DOCTYPE html><html>Too Many Requests</html>"))
        self.assertEqual(ar.hard_check("[]"), "empty body")


class Generate(unittest.TestCase):
    def run_gen(self, samples: dict[str, str]):
        with tempfile.TemporaryDirectory() as d:
            sdir, ydir = Path(d) / "samples" / "CRYPTO_PRICE", Path(d) / "yamls"
            sdir.mkdir(parents=True)
            ydir.mkdir()
            for name, text in samples.items():
                (sdir / f"{name}.md").write_text(text)
            with mock.patch.object(gen, "SAMPLES", sdir.parent), mock.patch.object(gen, "OUT_YAMLS", ydir), \
                    mock.patch.object(gen, "ROOT", Path(d)), mock.patch.object(sys, "argv", ["x", "--dry-run"]), \
                    mock.patch.dict("os.environ", {"ALLOW_UNSAFE_REGISTER": ""}):
                (Path(d) / "out").mkdir()
                return quiet(gen.main)

    def test_manual_approve_first_does_not_crash(self):
        manual = sample_text("https://a/x?q=1", "{}", slug="manual-one", extra="review_source: manual\n")
        rc, out = self.run_gen({"a-manual": manual})
        self.assertIn("SKIP  manual-one: approved without auto_review+LLM", out)   # was NameError

    def test_placeholder_url_refused(self):
        llm = "review_source: auto_review\nllm_used: true\n"
        rc, out = self.run_gen({"cp-kraken": sample_text("https://api.kraken.com/0/public/Ticker?pair={kraken_pair}",
                                                         "{}", slug="cp-kraken", extra=llm)})
        self.assertEqual(rc, 1)
        self.assertIn("unfilled {placeholder}", out)


class CaptureAndPin(unittest.TestCase):
    def test_capture_refuses_placeholder_before_fetching(self):
        with mock.patch.object(sys, "argv", ["x", "--intent", "CRYPTO_PRICE", "--slug", "cp-x",
                                             "--url", "https://api.kraken.com/0/public/Ticker?pair={kraken_pair}"]), \
                mock.patch.object(cap, "fetch") as f:
            rc, _ = quiet(cap.main)
        self.assertEqual(rc, 1)
        f.assert_not_called()

    def test_pin_check_survives_a_broken_yaml_elsewhere(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "intentYamls" / "a").mkdir(parents=True)
            good = root / "intentYamls" / "a" / "good.yaml"
            good.write_text((ROOT / "intentYamls/fx-now/fx-er-api.yaml").read_text())
            (root / "intentYamls" / "a" / "broken.yaml").write_text("slug: [unclosed\n")
            with mock.patch.object(pin, "ROOT", root), mock.patch.object(pin, "PINS", root / "none.json"), \
                    mock.patch.object(sys, "argv", ["x", "--file", str(good)]):
                rc, out = quiet(pin.main)
            self.assertEqual(rc, 0, out)
            self.assertIn("does not parse", out)


class SampleCheck(unittest.TestCase):
    def test_wrong_asset_stale_and_ok(self):
        url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"         # cp-coinbase.yaml's node request
        meta = parse_front_matter(sample_text(url, "{}", slug="cp-coinbase"))
        v = check_sample(meta, '{"data": {"amount": "2550.1", "base": "ETH", "currency": "USD"}}',
                         slug="cp-coinbase", intent="CRYPTO_PRICE")
        self.assertEqual(v[0], "rejected")
        self.assertIn("wrong asset", v[1])
        v = check_sample(meta, '{"data": {"amount": "82500.1", "base": "BTC", "currency": "USD"}}',
                         slug="cp-coinbase", intent="CRYPTO_PRICE")
        self.assertEqual(v[0], "valid")
        wx = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m"
        meta = parse_front_matter(sample_text(wx, "{}", slug="wx-openmeteo", intent="WEATHER_CHECK"))
        stale = '{"latitude": 52.52, "longitude": 13.41, "current": {"time": "2026-10-06T06:00", "temperature_2m": 12.0}}'
        v = check_sample(meta, stale, slug="wx-openmeteo", intent="WEATHER_CHECK")
        self.assertEqual(v[0], "rejected")
        self.assertIn("[E4] stale", v[1])
        self.assertIsNone(check_sample(meta, stale, slug="wx-openmeteo", intent="TEXT_SUMMARIZATION"))  # no spec
        other = parse_front_matter(sample_text(wx.replace("52.52", "1.35"), "{}", slug="wx-openmeteo"))
        self.assertIsNone(check_sample(other, stale, slug="wx-openmeteo", intent="WEATHER_CHECK"))  # not its question

    def test_auto_review_rejects_deterministically_before_llm(self):
        url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "cp-coinbase.md"
            p.write_text(sample_text(url, '{"data": {"amount": "-2.5%", "base": "BTC", "currency": "USD"}}', slug="cp-coinbase"))
            s = ar.parse_sample(p)
            with mock.patch.object(ar, "llm_judge") as judge:
                v, _j = ar.decide("CRYPTO_PRICE", s["meta"], s, True, 0.75)
            self.assertEqual((v.status, v.mode), ("rejected", "deterministic"))
            self.assertIn("percent change", v.reason)
            judge.assert_not_called()


if __name__ == "__main__":
    unittest.main()
