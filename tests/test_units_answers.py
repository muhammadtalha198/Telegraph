"""units.py and answers.py: numbers, units, answer types, time parsing."""
from __future__ import annotations

import unittest
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from zoneinfo import ZoneInfo

from tests.helpers import NOW  # noqa: F401  (sets sys.path)

from minercheck import units as U
from minercheck.answers import Context, Reject, parse_answer, parse_timestamp

CTX = Context(fetched_at=NOW, tz=ZoneInfo("Asia/Karachi"), quote="USD")


def ans(t, raw, **rule):
    return parse_answer(t, raw, rule, CTX, source_tz=rule.pop("source_tz", None) if "source_tz" in rule else None)


class Numbers(unittest.TestCase):
    def test_parse_number(self):
        self.assertEqual(U.parse_number("+35°C"), (Decimal("35"), "°C"))
        self.assertEqual(U.parse_number("82,846.985 USD"), (Decimal("82846.985"), "USD"))
        self.assertEqual(U.parse_number("$82,500.12")[0], Decimal("82500.12"))
        self.assertEqual(U.parse_number("$82,500.12")[1], "$")
        self.assertEqual(U.parse_number("−4.5 km/h"), (Decimal("-4.5"), "km/h"))
        self.assertEqual(U.parse_number("1e-5")[0], Decimal("0.00001"))
        self.assertEqual(U.parse_number("hot"), (None, ""))

    def test_to_decimal_keeps_precision(self):
        self.assertEqual(U.to_decimal(0.1), Decimal("0.1"))
        self.assertEqual(U.to_decimal("82846.985"), Decimal("82846.985"))
        self.assertIsNone(U.to_decimal(True))

    def test_conversions(self):
        self.assertEqual(U.to_canonical(Decimal("87.8"), "F", "temperature"), Decimal("31"))
        self.assertEqual(U.to_canonical(Decimal("304.15"), "K", "temperature"), Decimal("31.00"))
        self.assertEqual(U.to_canonical(Decimal("10"), "m/s", "speed"), Decimal("36.0"))
        self.assertEqual(U.to_canonical(Decimal("10"), "kn", "speed"), Decimal("18.520"))
        self.assertEqual(U.to_canonical(Decimal("8250012"), "cents", "money"), Decimal("82500.12"))
        self.assertEqual(U.to_canonical(Decimal("1"), "USDT", "money", quote="USD"), Decimal("1"))
        with self.assertRaises(ValueError):
            U.to_canonical(Decimal("1"), "EUR", "money", quote="USD")
        self.assertEqual(U.from_canonical(Decimal("31"), "F", "temperature"), Decimal("87.8"))

    def test_fmt(self):
        self.assertEqual(U.fmt(Decimal("82500.1"), 2, grouping=True), "82,500.10")
        self.assertEqual(U.fmt(Decimal("31.0")), "31")
        self.assertEqual(U.fmt(Decimal("0.000123456"), sig=3), "0.000123")


class AnswerTypes(unittest.TestCase):
    def test_temperature(self):
        self.assertEqual(ans("temperature", "87.8°F").canonical, Decimal("31"))
        self.assertEqual(ans("temperature", 31.5, unit="C").canonical, Decimal("31.5"))
        for bad, why in [("hot", "no number"), ("56%", "percentage"), ("4 km/h", "speed"), (30, "no unit")]:
            with self.subTest(bad=bad), self.assertRaisesRegex(Reject, why):
                ans("temperature", bad)
        with self.assertRaisesRegex(Reject, "yes/no"):
            ans("temperature", True, unit="C")

    def test_price(self):
        self.assertEqual(ans("price", "$82,500.12").canonical, Decimal("82500.12"))
        self.assertEqual(ans("price", "8250012 cents").canonical, Decimal("82500.12"))
        self.assertEqual(ans("price", "82500", unit="USDT").canonical, Decimal("82500"))
        for bad in ("-2.5%", "up 2.5 percent", "2.5 pct"):
            with self.subTest(bad=bad), self.assertRaisesRegex(Reject, "percent change"):
                ans("price", bad)
        with self.assertRaisesRegex(Reject, "EUR"):
            ans("price", "75000 EUR")

    def test_fx_rate_invert_and_percent(self):
        self.assertEqual(ans("fx_rate", "1.25", invert=True).canonical, Decimal("0.8"))
        with self.assertRaises(Reject):
            ans("fx_rate", "0.89%")
        with self.assertRaises(Reject):
            ans("fx_rate", "0", invert=True)

    def test_date_full_calendar_date_only(self):
        ok = {"2026-10-08": "2026-10-08", "Thursday, 8 October 2026": "2026-10-08",
              "October 8, 2026": "2026-10-08", "Thu, 08 Oct 2026 06:18:48 GMT": "2026-10-08",
              "2026-10-07T23:30:00-04:00": "2026-10-08"}  # converted to Karachi
        for raw, want in ok.items():
            with self.subTest(raw=raw):
                self.assertEqual(ans("date", raw).display.isoformat(), want)
        self.assertEqual(ans("date", "10/08/2026", date_order="MDY").display, date(2026, 10, 8))
        self.assertEqual(ans("date", "13/10/2026").display, date(2026, 10, 13))       # unambiguous D/M
        self.assertEqual(ans("date", str(int(NOW.timestamp())), epoch="s").display, date(2026, 10, 8))
        bad = {"Wednesday": "weekday only", "wed": "weekday only", "2026-W41": "week", "this week": "week",
               "today": "relative", "October 8": "no year", "08/10": "no year", "10/08/2026": "ambiguous",
               "soon": "not a calendar date"}
        for raw, why in bad.items():
            with self.subTest(raw=raw), self.assertRaisesRegex(Reject, why):
                ans("date", raw)

    def test_datetime_needs_time_and_zone(self):
        p = parse_answer("datetime_tz", "2026-10-08T15:30:02+09:00", {}, CTX)
        self.assertEqual(p.canonical, Decimal("2.0"))
        p = parse_answer("datetime_tz", "2026-10-08T15:30:01", {}, CTX, source_tz="Asia/Tokyo")
        self.assertEqual(p.canonical, Decimal("1.0"))
        p = parse_answer("datetime_tz", "15:30:03", {}, CTX, source_tz="Asia/Tokyo")    # time only, zone field
        self.assertEqual(p.canonical, Decimal("3.0"))
        p = parse_answer("datetime_tz", "11:29 PM", {}, Context(datetime(2026, 10, 8, 14, 30, tzinfo=timezone.utc)),
                         source_tz="Asia/Tokyo")                                         # 23:29 JST same day
        self.assertEqual(p.canonical, Decimal("-60.0"))
        p = parse_answer("datetime_tz", str(int(NOW.timestamp()) + 5), {"epoch": "s"}, CTX)
        self.assertEqual(p.canonical, Decimal("5.0"))
        for raw, why in [("2026-10-08", "date alone"), ("8 October 2026", "date alone"),
                         ("2026-10-08T15:30:01", "no timezone"), ("15:30", "no timezone"), ("noon", "no time of day")]:
            with self.subTest(raw=raw), self.assertRaisesRegex(Reject, why):
                parse_answer("datetime_tz", raw, {}, CTX)
        with self.assertRaisesRegex(Reject, "not a number"):
            parse_answer("datetime_tz", "2026-10-08", {"epoch": "s"}, CTX)          # strict epoch


class Timestamps(unittest.TestCase):
    def test_forms(self):
        self.assertEqual(parse_timestamp("2026100800", {"format": "%Y%m%d%H", "tz": "UTC"}, NOW),
                         datetime(2026, 10, 8, 0, tzinfo=timezone.utc))
        self.assertEqual(parse_timestamp(1791440970000, {"epoch": "ms"}, NOW), NOW - timedelta(seconds=30))
        self.assertEqual(parse_timestamp("2026-10-08T06:15", {"tz": "UTC"}, NOW), NOW - timedelta(minutes=15))
        self.assertEqual(parse_timestamp("06:18 AM", {"tz": "UTC", "time_of_day": True}, NOW),
                         NOW - timedelta(minutes=12))
        late = datetime(2026, 10, 8, 0, 5, tzinfo=timezone.utc)
        self.assertEqual(parse_timestamp("11:50 PM", {"tz": "UTC", "time_of_day": True}, late).date(), date(2026, 10, 7))
        with self.assertRaisesRegex(Reject, "declares no tz"):
            parse_timestamp("2026-10-08T06:15", {}, NOW)


if __name__ == "__main__":
    unittest.main()
