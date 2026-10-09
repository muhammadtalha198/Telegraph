"""One mock source per format (json, xml, text, html, csv) for every intent, and bodies for
each test case: correct, wrong_type, wrong_entity, stale. The mock sources plug into the
REAL intent spec (same answer_type, validation, template), only `sources:` is replaced.

Question asked in every case (see QUESTION) and the clock is tests.helpers.NOW
(2026-10-08 06:30:00 UTC).
"""
from __future__ import annotations

from datetime import datetime, timezone

FORMATS = ("json", "xml", "text", "html", "csv")
CTYPE = {"json": "application/json", "xml": "application/xml", "text": "text/plain",
         "html": "text/html", "csv": "text/csv"}
EPOCH_NOW = int(datetime(2026, 10, 8, 6, 30, tzinfo=timezone.utc).timestamp())

QUESTION = {
    "WEATHER_CHECK": {"location": "Lahore"},
    "CRYPTO_PRICE": {"asset": "BTC"},
    "FX_NOW": {"base": "USD", "quote": "EUR"},
    "DATE_TODAY": {"timezone": "Asia/Karachi"},
    "TIME_IN_CITY": {"location": "Tokyo"},
}


# a kind in each intent's allowed_kinds, so mock sources satisfy the schema + catalog audit
MOCK_KIND = {"WEATHER_CHECK": "weather_model", "CRYPTO_PRICE": "cex", "FX_NOW": "fx_feed",
             "DATE_TODAY": "clock", "TIME_IN_CITY": "clock"}


def src(intent: str, fmt: str, **rules) -> dict:
    return {"id": f"m-{fmt}", "name": f"Mock {fmt.upper()}", "publisher": f"{fmt}.example",
            "kind": MOCK_KIND.get(intent, "cex"),
            "request": {"url": f"https://{fmt}.example/{intent.lower()}"}, "cache_ttl_s": 0, **rules}


# ------------------------------------------------------------------ sources
SOURCES = {
    "WEATHER_CHECK": [
        src("WEATHER_CHECK", "json", value=[{"json": "now.temp_c", "unit": "C"}], timestamp=[{"json": "now.time"}],
            entity={"lat": [{"json": "lat"}], "lon": [{"json": "lon"}]},
            extras={"humidity": [{"json": "now.humidity"}]}),
        src("WEATHER_CHECK", "xml", value=[{"xpath": ".//obs/temp", "unit": "C"}], timestamp=[{"xpath": ".//obs/time"}],
            entity={"lat": [{"xpath": ".//station/@lat"}], "lon": [{"xpath": ".//station/@lon"}]}),
        src("WEATHER_CHECK", "text", value=[{"regex": r"Temperature:\s*([^\n]+)"}],
            timestamp=[{"regex": r"Observed:\s*(\S+)"}],
            entity={"lat": [{"regex": r"Location:\s*([-\d.]+),"}], "lon": [{"regex": r"Location:\s*[-\d.]+,([-\d.]+)"}]}),
        src("WEATHER_CHECK", "html", value=[{"css": "div.wx span#temp"}], timestamp=[{"css": "time", "attr": "datetime"}],
            entity={"lat": [{"css": "span.lat"}], "lon": [{"css": "span.lon"}]}),
        src("WEATHER_CHECK", "csv", value=[{"csv": "temperature_k", "unit": "K"}], timestamp=[{"csv": "observed"}],
            entity={"lat": [{"csv": "lat"}], "lon": [{"csv": "lon"}]}),
    ],
    "CRYPTO_PRICE": [
        src("CRYPTO_PRICE", "json", value=[{"json": "price", "unit": "{quote}"}], timestamp=[{"json": "updated", "epoch": "s"}],
            entity={"symbol": [{"json": "symbol"}]}),
        src("CRYPTO_PRICE", "xml", value=[{"xpath": ".//last"}], timestamp=[{"xpath": ".//ts"}],
            entity={"symbol": [{"xpath": ".//symbol"}]}),
        src("CRYPTO_PRICE", "text", value=[{"regex": r"last=(\S+)"}], timestamp=[{"regex": r" at (.+)$"}],
            entity={"symbol": [{"regex": r"^(\w+)/"}]}),
        src("CRYPTO_PRICE", "html", value=[{"css": "span.px"}], timestamp=[{"css": "span.px", "attr": "data-ts"}],
            entity={"symbol": [{"css": "span.px", "attr": "data-symbol"}]}),
        src("CRYPTO_PRICE", "csv", value=[{"csv": "price_usdt", "row": -1, "unit": "USDT"}],
            timestamp=[{"csv": "time", "row": -1}], entity={"symbol": [{"csv": "symbol", "row": -1}]}),
    ],
    "FX_NOW": [
        src("FX_NOW", "json", value=[{"json": "rates.{quote}"}], timestamp=[{"json": "time"}], entity={"base": [{"json": "base"}]}),
        src("FX_NOW", "xml", value=[{"xpath": ".//item[targetCurrency='{quote}']/inverseRate", "invert": True}],
            timestamp=[{"xpath": ".//item[targetCurrency='{quote}']/pubDate"}],
            entity={"base": [{"xpath": ".//item[targetCurrency='{quote}']/baseCurrency"}]}),
        src("FX_NOW", "text", value=[{"regex": r"=\s*([^\s]+)\s+{quote}"}], timestamp=[{"regex": r"updated (\S+)\)"}],
            entity={"base": [{"regex": r"^1\s+(\w+)"}]}),
        src("FX_NOW", "html", value=[{"css": "span.ccOutputRslt"}], timestamp=[{"css": "span.updated"}],
            entity={"base": [{"css": "span.base"}]}),
        src("FX_NOW", "csv", value=[{"csv": "rate", "where": {"quote": "{quote}"}}],
            timestamp=[{"csv": "updated", "where": {"quote": "{quote}"}}],
            entity={"base": [{"csv": "base", "where": {"quote": "{quote}"}}]}),
    ],
    "DATE_TODAY": [
        src("DATE_TODAY", "json", value=[{"json": "date"}], entity={"timezone": [{"json": "timezone"}]}),
        src("DATE_TODAY", "xml", value=[{"xpath": ".//today"}], entity={"timezone": [{"xpath": ".//zone"}]}),
        src("DATE_TODAY", "text", value=[{"regex": r"(?m)^ts=(\S+)$", "epoch": "s"}]),
        src("DATE_TODAY", "html", value=[{"css": "time", "attr": "datetime"}]),
        src("DATE_TODAY", "csv", value=[{"csv": "date", "date_order": "DMY"}], entity={"timezone": [{"csv": "zone"}]}),
    ],
    "TIME_IN_CITY": [
        src("TIME_IN_CITY", "json", value=[{"json": "datetime"}], entity={"timezone": [{"json": "timezone"}]}),
        src("TIME_IN_CITY", "xml", value=[{"xpath": ".//local"}], entity={"timezone": [{"xpath": ".//zone"}]}),
        src("TIME_IN_CITY", "text", value=[{"regex": r"(?m)^ts=(\S+)$", "epoch": "s"}]),
        src("TIME_IN_CITY", "html", value=[{"css": "span#clock"}], entity={"timezone": [{"css": "span#tz"}]}),
        src("TIME_IN_CITY", "csv", value=[{"csv": "unixtime", "epoch": "s"}], entity={"timezone": [{"csv": "zone"}]}),
    ],
}

# Truth in canonical units, for assertions.
TRUTH = {"WEATHER_CHECK": 31.0, "CRYPTO_PRICE": 82500.12, "FX_NOW": 0.893, "DATE_TODAY": "2026-10-08",
         "TIME_IN_CITY": "2026-10-08T15:30"}


# ------------------------------------------------------------------ bodies
def weather(fmt: str, case: str) -> str:
    lat, lon = ("33.66", "-95.56") if case == "wrong_entity" else ("31.55", "74.35")   # Paris, Texas
    t = "2026-10-06T06:20:00Z" if case == "stale" else "2026-10-08T06:20:00Z"
    wrong = case == "wrong_type"
    if fmt == "json":
        temp = '"hot"' if wrong else "31.0"
        return f'{{"lat": {lat}, "lon": {lon}, "now": {{"temp_c": {temp}, "time": "{t}", "humidity": 56}}}}'
    if fmt == "xml":
        temp = "56%" if wrong else "31.0"
        return f'<?xml version="1.0"?><weather><station lat="{lat}" lon="{lon}"/><obs><temp>{temp}</temp><time>{t}</time></obs></weather>'
    if fmt == "text":
        temp = "pleasant" if wrong else "87.8°F"
        return f"Location: {lat},{lon}\nObserved: {t}\nTemperature: {temp}\n"
    if fmt == "html":
        temp = "4 km/h" if wrong else "31 °C"
        return (f'<!DOCTYPE html><html><body><div class="wx"><span id="temp">{temp}</span>'
                f'<time datetime="{t}">now</time><span class="lat">{lat}</span><span class="lon">{lon}</span></div></body></html>')
    temp = "warm" if wrong else "304.15"
    return f"lat,lon,observed,temperature_k\n{lat},{lon},{t},{temp}\n"


def crypto(fmt: str, case: str) -> str:
    sym = "ETH" if case == "wrong_entity" else "BTC"
    ep = EPOCH_NOW - 86400 if case == "stale" else EPOCH_NOW - 30
    iso = "2026-10-07T06:29:30Z" if case == "stale" else "2026-10-08T06:29:30Z"
    wrong = case == "wrong_type"
    if fmt == "json":
        price = '"-2.5%"' if wrong else ('"2550.10"' if sym == "ETH" else '"82500.12"')
        return f'{{"symbol": "{sym}", "price": {price}, "updated": {ep}}}'
    if fmt == "xml":
        price = "+2.5%" if wrong else ("2,550.10" if sym == "ETH" else "82,500.12")
        return f"<ticker><symbol>{sym}</symbol><last>{price} USD</last><ts>{iso}</ts></ticker>"
    if fmt == "text":
        price = "+2.50%" if wrong else ("$2,550.10" if sym == "ETH" else "$82,500.12")
        when = "2026-10-07 06:29:30 UTC" if case == "stale" else "2026-10-08 06:29:30 UTC"
        return f"{sym}/USD last={price} at {when}"
    if fmt == "html":
        price = "up 2.5 percent" if wrong else ("255010 cents" if sym == "ETH" else "8250012 cents")
        return f'<html><body><p>Price: <span class="px" data-symbol="{sym}" data-ts="{iso}">{price}</span></p></body></html>'
    price = "2.5%" if wrong else ("2550.1" if sym == "ETH" else "82510.5")
    return f"symbol,price_usdt,time\nXRP,0.52,2026-10-08T06:29:00Z\n{sym},{price},{iso}\n"


def fx(fmt: str, case: str) -> str:
    base = "GBP" if case == "wrong_entity" else "USD"
    rate = "1.0610" if base == "GBP" else "0.8930"
    wrong = case == "wrong_type"
    t = "2026-09-20T06:00:00Z" if case == "stale" else "2026-10-08T06:00:00Z"
    if fmt == "json":
        r = '"0.89%"' if wrong else rate
        return f'{{"base": "{base}", "rates": {{"EUR": {r}, "JPY": 151.2}}, "time": "{t}"}}'
    if fmt == "xml":
        inv = "12%" if wrong else ("0.94251" if base == "GBP" else "1.11982")
        pub = "Sun, 20 Sep 2026 06:00:00 GMT" if case == "stale" else "Thu, 08 Oct 2026 06:00:00 GMT"
        return (f'<?xml version="1.0"?><channel><item><baseCurrency>{base}</baseCurrency><targetCurrency>JPY</targetCurrency>'
                f'<inverseRate>0.0066</inverseRate><pubDate>{pub}</pubDate></item><item><baseCurrency>{base}</baseCurrency>'
                f'<targetCurrency>EUR</targetCurrency><inverseRate>{inv}</inverseRate><pubDate>{pub}</pubDate></item></channel>')
    if fmt == "text":
        r = "0.89%" if wrong else rate
        return f"1 {base} = {r} EUR (updated {t})"
    if fmt == "html":
        r = "about EUR" if wrong else f"{rate[:5]}<span class='ccOutputTrail'>{rate[5:]}</span> EUR"
        return (f'<html><body><span class="base">{base}</span>=<span class="ccOutputRslt">{r}</span>'
                f'<span class="updated">{t}</span></body></html>')
    r = "1%" if wrong else rate
    return f"base,quote,rate,updated\n{base},JPY,151.2,{t}\n{base},EUR,{r},{t}\n"


def date_today(fmt: str, case: str) -> str:
    zone = "Asia/Tokyo" if case == "wrong_entity" else "Asia/Karachi"
    stale = case == "stale"
    wrong = case == "wrong_type"
    if fmt == "json":
        d = "Thursday" if wrong else ("2026-10-07" if stale else "2026-10-08")
        return f'{{"date": "{d}", "timezone": "{zone}", "day_of_week": "Thursday"}}'
    if fmt == "xml":
        d = "2026-W41" if wrong else ("Wednesday, 7 October 2026" if stale else "Thursday, 8 October 2026")
        return f"<clock><zone>{zone}</zone><today>{d}</today></clock>"
    if fmt == "text":
        if wrong:
            return "fl=1\nts=Thursday\n"
        ts = EPOCH_NOW - 86400 if stale else EPOCH_NOW
        if case == "wrong_entity":  # an epoch is absolute: there is no wrong zone, so send 1970 (E2)
            ts = 0
        return f"fl=1\nts={ts}.000\nvisit_scheme=https\n"
    if fmt == "html":
        dt = "October 8" if wrong else ("2026-10-07T11:30:00+05:00" if stale else
                                        ("1970-01-01T00:00:00+00:00" if case == "wrong_entity" else "2026-10-08T11:30:00+05:00"))
        return f'<html><body><p>Today is <time datetime="{dt}">Thursday</time></p></body></html>'
    d = "this week" if wrong else ("07/10/2026" if stale else "08/10/2026")
    return f"zone,date\n{zone},{d}\n"


def time_city(fmt: str, case: str) -> str:
    wrong = case == "wrong_type"
    stale = case == "stale"
    zone = "Europe/Paris" if case == "wrong_entity" else "Asia/Tokyo"
    if fmt == "json":
        dt = ("2026-10-08" if wrong else "2026-10-08T14:30:02+09:00" if stale else
              "2026-10-08T08:30:02+02:00" if case == "wrong_entity" else "2026-10-08T15:30:02+09:00")
        return f'{{"datetime": "{dt}", "timezone": "{zone}"}}'
    if fmt == "xml":
        dt = ("8 October 2026" if wrong else "2026-10-08T14:30:01" if stale else
              "2026-10-08T08:30:01" if case == "wrong_entity" else "2026-10-08T15:30:01")
        return f"<time><zone>{zone}</zone><local>{dt}</local></time>"
    if fmt == "text":
        if wrong:
            return "fl=1\nts=2026-10-08\n"
        ts = EPOCH_NOW - 3600 if stale else (0 if case == "wrong_entity" else EPOCH_NOW + 1)
        return f"fl=1\nts={ts}\n"
    if fmt == "html":
        clock = "Thursday" if wrong else ("14:30:03" if stale else "08:30:03" if case == "wrong_entity" else "15:30:03")
        return f'<html><body><span id="clock">{clock}</span><span id="tz">{zone}</span></body></html>'
    ts = "2026-10-08" if wrong else str(EPOCH_NOW - 3600 if stale else EPOCH_NOW + 2)
    return f"zone,unixtime\n{zone},{ts}\n"


BODIES = {"WEATHER_CHECK": weather, "CRYPTO_PRICE": crypto, "FX_NOW": fx, "DATE_TODAY": date_today,
          "TIME_IN_CITY": time_city}

# Which layer must reject each bad case (wrong-entity epochs have no zone, so they fail E2 as 1970).
EXPECT_LAYER = {"wrong_type": "E5", "wrong_entity": "E5", "stale": "E4"}
EXPECT_OVERRIDE = {("DATE_TODAY", "text", "wrong_entity"): "E2", ("DATE_TODAY", "html", "wrong_entity"): "E2",
                   ("TIME_IN_CITY", "text", "wrong_entity"): "E2"}
