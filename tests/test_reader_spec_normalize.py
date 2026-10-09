"""reader.py (format detection + extraction), spec.py (loader fails loudly), normalize.py (inputs)."""
from __future__ import annotations

import copy
import unittest

from tests.helpers import registry, spec_doc, spec_with

from minercheck.errors import ExtractError, InputError, SpecError
from minercheck.normalize import normalize
from minercheck.reader import detect_format, extract, json_path, read
from minercheck.spec import build


class Detection(unittest.TestCase):
    def test_body_beats_header(self):
        cases = {
            ('{"a": 1}', "text/html"): "json",
            ("[1, 2]", ""): "json",
            ('<?xml version="1.0"?><a><b>1</b></a>', "text/plain"): "xml",
            ("<a><b>1</b></a>", "application/json"): "xml",
            ("<!DOCTYPE html><html><body>x</body></html>", "application/json"): "html",
            ("<div><span>1</span>", "text/html"): "html",
            ("<weather><temp>31", "application/xml"): "text",          # broken XML is not "repaired"
            ("a,b\n1,2\n", "text/plain"): "csv",
            ("a;b\n1;2\n3;4\n", ""): "csv",
            ("+35°C|27%|4km/h", "text/csv"): "text",                     # one line is not a table
            ("ts=1791440219.000\nloc=XX\n", "text/plain"): "text",
            ("   ", "application/json"): "empty",
        }
        for (body, ct), want in cases.items():
            with self.subTest(body=body[:20]):
                self.assertEqual(detect_format(body, ct), want)
        self.assertEqual(read(b"PK\x03\x04zip", "application/zip").format, "binary")
        doc = read('{"a": 1}', "text/html")
        self.assertIn("Content-Type says html, body is json", doc.notes[0])

    def test_json_keeps_decimal(self):
        self.assertEqual(str(read('{"p": 82846.985}').json["p"]), "82846.985")


class Extraction(unittest.TestCase):
    def test_json_path(self):
        obj = {"result": {"XXBTZUSD": {"c": ["82856.7", "0.002"]}}, "Rates": {"EUR": 0.89}, "l": [1, 2, 3]}
        self.assertEqual(json_path(obj, "result.*.c.0"), "82856.7")
        self.assertEqual(json_path(obj, "rates.eur"), 0.89)                 # single case-insensitive match
        self.assertEqual(json_path(obj, "l[-1]"), 3)
        for bad in ("result.x", "l.a", "l.9", "Rates.EUR.x"):
            with self.subTest(bad=bad), self.assertRaises(KeyError):
                json_path(obj, bad)

    def test_rules_by_format(self):
        xml = read('<?xml version="1.0"?><channel xmlns="urn:x"><item><targetCurrency>EUR</targetCurrency>'
                   '<exchangeRate>0.89</exchangeRate></item><item a="7"><targetCurrency>JPY</targetCurrency>'
                   "<exchangeRate>151</exchangeRate></item></channel>")
        self.assertEqual(extract(xml, [{"xpath": ".//item[targetCurrency='{q}']/exchangeRate"}], {"q": "JPY"}).value, "151")
        self.assertEqual(extract(xml, [{"xpath": "/channel/item[2]/@a"}], {}).value, "7")
        html = read('<html><body><div id="x" class="a b"><p>skip</p><span class="v" data-n="9">0.89<span>30</span> EUR'
                    "</span></div><ul><li>1</li><li>2</li></ul><script>var p=1;</script></body></html>")
        self.assertEqual(extract(html, [{"css": "div#x.a > span.v"}], {}).value, "0.8930 EUR")
        self.assertEqual(extract(html, [{"css": "span[data-n=9]", "attr": "data-n"}], {}).value, "9")
        self.assertEqual(extract(html, [{"css": "ul li:nth-of-type(2)"}], {}).value, "2")
        self.assertEqual(extract(html, [{"css": "li", "index": -1}], {}).value, "2")
        self.assertEqual(extract(html, [{"xpath": ".//ul/li[1]"}], {}).value, "1")
        csv = read("sym,price\nETH,2550\nBTC,82500\n")
        self.assertEqual(extract(csv, [{"csv": "price", "where": {"sym": "{s}"}}], {"s": "btc"}).value, "82500")
        self.assertEqual(extract(csv, [{"csv": "price", "row": -1}], {}).value, "82500")
        txt = read("fl=1\nts=1791440219.000\n")
        self.assertEqual(extract(txt, [{"regex": r"(?m)^ts=(?P<value>\S+)$"}], {}).value, "1791440219.000")
        hdr = read(b"", headers={"Date": "Thu, 08 Oct 2026 06:33:32 GMT"})
        self.assertEqual(extract(hdr, [{"header": "date"}], {}).value, "Thu, 08 Oct 2026 06:33:32 GMT")
        js = read('{"msg": "price is 82,500.12 USD"}')
        self.assertEqual(extract(js, [{"json": "msg", "regex": r"is (\S+)"}], {}).value, "82,500.12")

    def test_fallback_order_and_reasons(self):
        doc = read('{"price": "1.5"}')
        loc = extract(doc, [{"xpath": ".//price"}, {"json": "last"}, {"json": "price"}], {})
        self.assertEqual((loc.value, loc.index), ("1.5", 2))
        with self.assertRaises(ExtractError) as e:
            extract(doc, [{"json": "a.b"}, {"css": "p"}, {"json": "{missing}"}], {})
        msg = str(e.exception)
        self.assertIn("rule 1: json a.b", msg)
        self.assertIn("css rule, but body is json", msg)
        self.assertIn("no input/normalized value is named 'missing'", msg)
        with self.assertRaisesRegex(ExtractError, "points to an object"):
            extract(read('{"a": {"b": 1}}'), [{"json": "a"}], {})


class SpecLoader(unittest.TestCase):
    def test_real_specs_load(self):
        reg = registry()
        # the 5 original local/price intents plus the catalog-derived Wave2 specs all load
        self.assertLessEqual({"WEATHER_CHECK", "CRYPTO_PRICE", "FX_NOW", "DATE_TODAY", "TIME_IN_CITY",
                              "TOKEN_TOTAL_SUPPLY_VERIFY", "DNS_RECORD_LOOKUP", "CARRIER_SERVICEABILITY"},
                             set(reg.specs))
        self.assertIs(reg.get("crypto_price_lookup"), reg.get("CRYPTO_PRICE"))     # alias, case-insensitive
        self.assertIsNone(reg.get("NOT_AN_INTENT"))

    def bad(self, mutate, expect):
        doc = copy.deepcopy(spec_doc("WEATHER_CHECK"))
        mutate(doc)
        with self.assertRaises(SpecError) as e:
            build(doc)
        self.assertIn(expect, str(e.exception))

    def test_fails_loudly(self):
        self.bad(lambda d: d.pop("answer_type"), "missing required key 'answer_type'")
        self.bad(lambda d: d.update(answer_type="weather"), "is not one of")
        self.bad(lambda d: d.update(answr="x"), "did you mean 'answer")
        self.bad(lambda d: d["sources"][0].update(valeu=[]), "did you mean 'value'")
        self.bad(lambda d: d["sources"][0]["value"][0].update(xpath="//x"), "needs exactly one of")
        self.bad(lambda d: d["sources"][0]["value"][0].update(jsn="a"), "did you mean 'json'")
        self.bad(lambda d: d["sources"][0]["request"].update(url="https://x/{latt}"), "unknown placeholder(s) {latt}")
        self.bad(lambda d: d["sources"][1].update(id="open-meteo"), "duplicate source id")
        self.bad(lambda d: d["sources"][0]["extras"].update(pressure=[{"json": "p"}]), "not declared in top-level extras")
        self.bad(lambda d: d["sources"][0]["miner"].update(question={}), "missing required input(s)")
        self.bad(lambda d: d["validation"]["cross_check"].update(min_sources=1), "must be >= 2")
        self.bad(lambda d: d["validation"]["cross_check"].update(min_sources=9), "can never verify")
        self.bad(lambda d: d["validation"]["sanity"].update(min=True), "must be int/float/str")
        self.bad(lambda d: d["template"].update(answer="{nope}"), "template.answer: unknown placeholder")
        self.bad(lambda d: d["inputs"]["location"].update(kind="city"), "is not one of")
        self.bad(lambda d: d["tests"].append({"id": "x", "inputs": {"city": "x"}}), "is not a declared input")
        self.bad(lambda d: d["sources"][0]["value"][0].update(epoch="sec"), "epoch: must be s or ms")

    def test_spec_with_helper(self):
        full = spec_with("FX_NOW")
        s = spec_with("FX_NOW", mutate=lambda d: d["sources"].pop())
        self.assertEqual(len(s.sources), len(full.sources) - 1)


class Inputs(unittest.TestCase):
    reg = registry()

    def norm(self, intent, **kw):
        return normalize(self.reg.get(intent), kw, self.reg.shared)

    def test_lookalike_places(self):
        n = self.norm("WEATHER_CHECK", location="Paris")
        self.assertEqual(n.vars["place"], "Paris, France")
        self.assertIn("Paris, Texas", n.notes[0])
        for q in ("Paris, Texas", "Paris, TX", "paris, us"):
            with self.subTest(q=q):
                n = self.norm("WEATHER_CHECK", location=q)
                self.assertEqual(n.entity["timezone"], "America/Chicago")
                self.assertEqual(n.notes, [])
        self.assertEqual(self.norm("WEATHER_CHECK", location="zürich").vars["place"], "Zurich, Switzerland")
        with self.assertRaisesRegex(InputError, "no place 'Paris' in 'Germany'"):
            self.norm("WEATHER_CHECK", location="Paris, Germany")
        with self.assertRaisesRegex(InputError, "unknown place"):
            self.norm("WEATHER_CHECK", location="Atlantis")

    def test_coordinates_and_geocoder(self):
        n = self.norm("WEATHER_CHECK", location="31.55, 74.34")
        self.assertEqual((n.vars["lat"], n.vars["lon"], n.entity["timezone"]), ("31.5500", "74.3400", "Asia/Karachi"))
        with self.assertRaisesRegex(InputError, "out of range"):
            self.norm("WEATHER_CHECK", location="95,10")
        geo = lambda name: [{"name": "Multan", "lat": 30.19, "lon": 71.47, "country": "Pakistan",  # noqa: E731
                             "country_code": "PK", "timezone": "Asia/Karachi", "population": 1871843}]
        n = normalize(self.reg.get("TIME_IN_CITY"), {"location": "Multan"}, self.reg.shared, geo)
        self.assertEqual(n.vars["timezone"], "Asia/Karachi")

    def test_assets_currencies_timezones_enums(self):
        for q in ("BTC", "bitcoin", "XBT", "btc-bitcoin", "Bitcoin"):
            with self.subTest(q=q):
                n = self.norm("CRYPTO_PRICE", asset=q)
                self.assertEqual((n.vars["symbol"], n.vars["coingecko"], n.vars["quote"]), ("BTC", "bitcoin", "USD"))
        with self.assertRaisesRegex(InputError, "did you mean ETH"):
            self.norm("CRYPTO_PRICE", asset="ETHH")
        n = self.norm("FX_NOW", base="euro", quote="japanese yen")
        self.assertEqual((n.vars["base"], n.vars["quote"], n.vars["base_lower"]), ("EUR", "JPY", "eur"))
        self.assertEqual(self.norm("FX_NOW", base="$", quote="€").vars["quote"], "EUR")
        with self.assertRaisesRegex(InputError, "ambiguous: INR, PKR"):
            self.norm("FX_NOW", quote="rupee")
        with self.assertRaisesRegex(InputError, "unknown currency"):
            self.norm("FX_NOW", quote="XYZ")
        self.assertEqual(self.norm("DATE_TODAY", timezone="Tokyo").vars["timezone"], "Asia/Tokyo")
        self.assertEqual(self.norm("DATE_TODAY").vars["timezone"], "UTC")             # default
        self.assertEqual(self.norm("WEATHER_CHECK", location="Lahore", unit="Fahrenheit").values["unit"], "F")
        with self.assertRaisesRegex(InputError, "is not one of"):
            self.norm("WEATHER_CHECK", location="Lahore", unit="R")
        with self.assertRaisesRegex(InputError, "did you mean 'location'"):
            self.norm("WEATHER_CHECK", locaton="Lahore")
        with self.assertRaisesRegex(InputError, "missing required input 'quote'"):
            self.norm("FX_NOW", base="USD")


if __name__ == "__main__":
    unittest.main()
