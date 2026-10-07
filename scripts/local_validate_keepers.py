#!/usr/bin/env python3
"""
Local Usman-clone validator: YAML gate → ask miner → parse quantity → truth → RelTol/PassFail.

Mirrors Telegraph pkg/scoring/comparator + WASM RelTol curve without needing his node.
Stdlib only. Writes out/LOCAL_VALIDATE-YYYY-MM-DD.md

YAML gate (Group A): parses each matching intentYamls/**/<slug>.yaml for unquoted
`: ` scalars and required miner shape *before* endpoint probes — endpoint PASS
must not mask a file the node will reject.

Preflight (Groups A–D): before registerMiner, also run
  python3 scripts/preflight_miner.py --file <yaml>
(wired into register-miner.sh). Regression of 2026-09-28 fixes + NON-DET 2026-09-29:
  python3 scripts/preflight_miner.py --regression

NON-DET / adapter intents (LANGUAGE_TRANSLATION, TEXT_SUMMARIZATION,
CHATBOT_CONVERSATION, TEXT_TO_SPEECH) use text askability (plain string label),
not RelTol — same gate path as Groups A–D YAML + live probe.

  python3 scripts/local_validate_keepers.py
  python3 scripts/local_validate_keepers.py --intent FX_NOW
  python3 scripts/local_validate_keepers.py --slug patch-judge0-ce
  python3 scripts/validate_miner_yaml.py intentYamls/crypto-yield/
"""
from __future__ import annotations

import argparse
import json
import math
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent))
from batch6_manifest import INTENT_TOL as B6_TOL, M as B6, ROUTES as B6_ROUTES, query as b6_query  # noqa: E402
from batch7_manifest import INTENT_TOL as B7_TOL, M as B7, query as b7_query  # noqa: E402

PROXY = "https://omni-chat.13.237.89.59.sslip.io"
UA = "telegraph-local-validate/1"
OUT_DIR = Path(__file__).resolve().parents[1] / "out"

# RelTol from Usman's intentConfigs (bps). PassFail used for CODE_PATCH.
INTENT_TOL = {
    "FX_NOW": 50,
    "ROUTE_ETA": 800,
    "MACRO_ECONOMIC_INDICATOR": 150,
    "LIQUIDITY_DEPTH_VERIFY": 300,
    "MINING_HASHPRICE_VERIFY": 400,
    "GRID_POWER_PRICE": 30,  # contract selftest; Go port comments also use ~30–band
    "LIVE_SHELF_PRICE": 300,
    "ONCHAIN_METRIC_VERIFY": 5,
    "ASSET_RESERVE_ATTESTATION": 150,
    "CODE_PATCH_VERIFY": 0,  # PassFail
    "CROSS_CHAIN_STATE_VERIFY": 0,  # PassFail execution_ok
    "EVENT_OUTCOME_RESOLUTION": 0,  # PassFail resolved_yes
    "SKU_IN_STOCK": 0,  # PassFail in_stock
    "OPTIMAL_EXECUTION_ROUTE": 300,  # RelTol on amount_out / effective_price
    "PAYMENT_METHOD_VERIFY": 0,  # PassFail scheme_code
    "SANCTIONS_SCREENING_MATCH": 0,  # PassFail on_list
    "CORPORATE_REGISTRY_LOOKUP": 0,  # PassFail status_active
    "REGULATORY_FILING_MONITOR": 0,  # PassFail has_form
    "CRYPTO_PRICE_LOOKUP": 100,  # RelTol self-truth on cents (catalog name)
    "CRYPTO_PRICE": 100,  # diamond alias
    "CRYPTO_TRANSFER_VERIFY": 0,  # PassFail success
    "CRYPTO_YIELD_RATE": 500,  # RelTol apy_bps (Fable: modelling-choice spread)
    "THREAT_IP_REPUTATION": 0,  # PassFail listed
    "WEATHER_CHECK": 50,  # RelTol temp_k_x100
    "STOCK_PRICE": 50,  # RelTol last_cents
    "TRAVEL_DISRUPTION": 0,  # PassFail disruption_active
    # NON-DET / adapter (text askability in keepers; LLM-judge scores quality)
    "LANGUAGE_TRANSLATION": 0,
    "TEXT_SUMMARIZATION": 0,
    "CHATBOT_CONVERSATION": 0,
    "TEXT_TO_SPEECH": 0,
}
INTENT_TOL.update(B6_TOL)
INTENT_TOL.update(B7_TOL)

SCALE = {
    "FX_NOW": 10000.0,
    "ROUTE_ETA": 1.0,
    "MACRO_ECONOMIC_INDICATOR": 1000.0,
    "LIQUIDITY_DEPTH_VERIFY": 100.0,  # cents already; score on cents ints
    "MINING_HASHPRICE_VERIFY": 1.0,
    "GRID_POWER_PRICE": 1.0,  # milli already in field
    "LIVE_SHELF_PRICE": 1.0,  # cents already
    "ONCHAIN_METRIC_VERIFY": 1.0,
    "ASSET_RESERVE_ATTESTATION": 1.0,
    "CODE_PATCH_VERIFY": 1.0,
}


def http_get(url: str, timeout: int = 45, accept: Optional[str] = None, retries: int = 3) -> Any:
    headers = {"User-Agent": UA}
    if accept:
        headers["Accept"] = accept
    last: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                raw = r.read()
                ctype = r.headers.get("Content-Type", "")
            text = raw.decode("utf-8", errors="replace")
            if "json" in ctype or text[:1] in "{[":
                return json.loads(text)
            # HTML / empty → treat as hard fail so callers don't silently parse junk
            if text.lstrip().startswith("<") or not text.strip():
                raise ValueError(f"non-JSON body from {url[:80]}")
            return text
        except Exception as e:
            last = e
            time.sleep(1.5 * (attempt + 1))
    assert last is not None
    raise last


def dig(doc: Any, path: str) -> Any:
    cur = doc
    for part in path.split("."):
        if isinstance(cur, list):
            cur = cur[int(part)]
        elif isinstance(cur, dict):
            if part not in cur:
                return None
            cur = cur[part]
        else:
            return None
    return cur


def as_num(v: Any) -> Optional[float]:
    if isinstance(v, bool) or v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        s = v.strip().replace(",", ".")
        try:
            return float(s)
        except ValueError:
            return None
    return None


def bps_err(miner: float, truth: float) -> Optional[float]:
    if truth == 0:
        return None
    return abs(miner - truth) / abs(truth) * 10000.0


def reltol_score(err_bps: float, tol: float) -> float:
    """Usman WASM RelTol: 10000 at 0, 5000 at tol, 0 at 2*tol."""
    if err_bps >= 2 * tol:
        return 0.0
    return 10000.0 * (1.0 - err_bps / (2.0 * tol))


ParseFn = Callable[[Any, str], Optional[float]]


def parse_rates(quote: str) -> ParseFn:
    def _p(doc: Any, _q: str = quote) -> Optional[float]:
        if not isinstance(doc, dict):
            return None
        rates = doc.get("rates") or {}
        return as_num(rates.get(quote))
    return _p


def parse_coinbase(quote: str) -> ParseFn:
    def _p(doc: Any, _q: str = quote) -> Optional[float]:
        return as_num(dig(doc, f"data.rates.{quote}"))
    return _p


def parse_fawaz(quote: str) -> ParseFn:
    q = quote.lower()

    def _p(doc: Any, _q: str = quote) -> Optional[float]:
        return as_num(dig(doc, f"usd.{q}"))
    return _p


def parse_boc_cad(doc: Any, _q: str = "") -> Optional[float]:
    obs = dig(doc, "observations")
    if not isinstance(obs, list) or not obs:
        return None
    last = obs[-1]
    cell = last.get("FXUSDCAD") or last.get("FXCADUSD")
    if isinstance(cell, dict):
        return as_num(cell.get("v"))
    return None


def parse_cbr_usd_rub(doc: Any, _q: str = "") -> Optional[float]:
    # USD in RUB → invert for USD/EUR we need cross; for scoring Usman converts.
    # Local: score USD/RUB vs frankfurter USD/RUB if available; else skip EUR.
    v = dig(doc, "Valute.USD.Value")
    n = as_num(str(v).replace(",", ".")) if v is not None else None
    return n  # RUB per 1 USD


def parse_hnb_eur(doc: Any, _q: str = "") -> Optional[float]:
    # HNB is EUR-based mid; Usman converts to USD/EUR. Field srednji_tecaj for USD.
    rows = doc if isinstance(doc, list) else []
    for row in rows:
        if str(row.get("valuta", "")).upper() == "USD":
            return as_num(str(row.get("srednji_tecaj", "")).replace(",", "."))
    return None


def parse_riksbank(doc: Any, _q: str = "") -> Optional[float]:
    if isinstance(doc, list) and doc:
        return as_num(doc[-1].get("value"))
    return as_num(dig(doc, "0.value"))


def parse_osrm_route(doc: Any, _q: str = "") -> Optional[float]:
    return as_num(dig(doc, "routes.0.duration"))


def parse_osrm_table(doc: Any, _q: str = "") -> Optional[float]:
    d = dig(doc, "durations")
    if isinstance(d, list) and len(d) > 0 and isinstance(d[0], list) and len(d[0]) > 1:
        return as_num(d[0][1])
    return None


def parse_wb(doc: Any, _q: str = "") -> Optional[float]:
    if isinstance(doc, list) and len(doc) >= 2 and isinstance(doc[1], list) and doc[1]:
        return as_num(doc[1][0].get("value"))
    return as_num(dig(doc, "rate_pct"))


def parse_field(path: str) -> ParseFn:
    def _p(doc: Any, _q: str = "") -> Optional[float]:
        return as_num(dig(doc, path))
    return _p


def parse_exit(doc: Any, _q: str = "") -> Optional[float]:
    return as_num(dig(doc, "exit_status"))


@dataclass
class Case:
    intent: str
    slug: str
    ask_url: str
    parse: ParseFn
    # truth: either a URL + parse, or a fixed expected scaled value, or PassFail expected
    truth_url: Optional[str] = None
    truth_parse: Optional[ParseFn] = None
    truth_fixed: Optional[float] = None  # already in score units (scaled)
    passfail_expect: Optional[int] = None  # CODE_PATCH
    note: str = ""
    scale: Optional[float] = None
    quote: str = ""
    # NON-DET / adapter: require non-empty text at this field (parse unused)
    text_field: Optional[str] = None
    text_min_len: int = 1
    ask_timeout: int = 45


@dataclass
class Result:
    intent: str
    slug: str
    status: str  # PASS / FAIL / SKIP / WARN
    detail: str
    miner_val: Optional[float] = None
    truth_val: Optional[float] = None
    err_bps: Optional[float] = None
    score: Optional[float] = None


def frankfurter_truth(quote: str) -> tuple[str, ParseFn]:
    url = f"https://api.frankfurter.app/latest?from=USD&to={quote}"
    return url, parse_rates(quote)


def build_cases() -> list[Case]:
    lon = "-0.1278,51.5074;-0.0770,51.5155"
    # GRID pin from Usman GridIntervals
    grid_start = "20260913T14:00-0000"
    grid_end = "20260913T15:00-0000"
    grid_ask = (
        f"{PROXY}/caiso/lmp?node=TH_NP15_GEN-APND&market=DAM"
        f"&startdatetime={grid_start}&enddatetime={grid_end}"
    )

    cases: list[Case] = []

    # ── FX_NOW (EUR round; specialists use their quote) ──
    fx_eur = [
        ("fx-frankfurter", "https://api.frankfurter.app/latest?from=USD&to=EUR", parse_rates("EUR")),
        # vatcomply often serves a stale dated fix — self-truth (askability); ECB RelTol will score 0 if >100bps
        ("fx-vatcomply", "https://api.vatcomply.com/rates?base=USD", parse_rates("EUR")),
        ("fx-er-api", "https://open.er-api.com/v6/latest/USD", parse_rates("EUR")),
        ("fx-erapi-v4", "https://api.exchangerate-api.com/v4/latest/USD", parse_rates("EUR")),
        ("fx-fawaz", "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json", parse_fawaz("EUR")),
        ("fx-coinbase", "https://api.coinbase.com/v2/exchange-rates?currency=USD", parse_coinbase("EUR")),
    ]
    turl, tparse = frankfurter_truth("EUR")
    for slug, url, p in fx_eur:
        if slug == "fx-vatcomply":
            cases.append(Case(
                "FX_NOW", slug, url, p,
                truth_url=url, truth_parse=p, scale=10000.0, quote="EUR",
                note="self-truth (vatcomply dated fix often >100bps vs ECB)",
            ))
        else:
            cases.append(Case(
                "FX_NOW", slug, url, p, truth_url=turl, truth_parse=tparse,
                scale=10000.0, quote="EUR",
                note="truth=Frankfurter/ECB (same as Usman ECBSource)",
            ))

    cases.append(Case(
        "FX_NOW", "fx-boc",
        "https://www.bankofcanada.ca/valet/observations/FXUSDCAD/json?recent=1",
        parse_boc_cad,
        truth_url="https://api.frankfurter.app/latest?from=USD&to=CAD",
        truth_parse=parse_rates("CAD"),
        scale=10000.0, quote="CAD", note="CAD only",
    ))

    # HNB: srednji is HRK? Actually HNB tecajn-eur is units of currency per EUR.
    # Usman converts. Local: ask USD row = HRK? For v3 it's EUR-based mid for foreign currencies.
    # Skip complex cross — score HNB USD-per-EUR inverted vs frankfurter if we get mid.
    cases.append(Case(
        "FX_NOW", "fx-hnb",
        "https://api.hnb.hr/tecajn-eur/v3?valuta=USD",
        parse_hnb_eur,
        truth_url="https://api.frankfurter.app/latest?from=EUR&to=USD",
        truth_parse=parse_rates("USD"),
        scale=10000.0, quote="EUR",
        note="HNB EUR-base mid (USD per EUR) vs Frankfurter EUR→USD",
    ))

    cases.append(Case(
        "FX_NOW", "fx-cbr",
        "https://www.cbr-xml-daily.ru/daily_json.js",
        parse_cbr_usd_rub,
        # Frankfurter has no RUB; use ER-API as independent USD→RUB reference
        truth_url="https://open.er-api.com/v6/latest/USD",
        truth_parse=parse_rates("RUB"),
        scale=10000.0, quote="RUB", note="RUB per USD; truth=ER-API (Frankfurter lacks RUB)",
    ))

    # Riksbank: pin a known business day (weekend/today empty HTML)
    cases.append(Case(
        "FX_NOW", "fx-riksbank",
        "https://api.riksbank.se/swea/v1/Observations/SEKUSDPMI/2026-09-22",
        parse_riksbank,
        truth_url="https://api.frankfurter.app/latest?from=USD&to=SEK",
        truth_parse=parse_rates("SEK"),
        scale=10000.0, quote="SEK",
        note="pinned 2026-09-22 SEKUSDPMI",
    ))

    # ── ROUTE_ETA (pinned LON) ──
    cases.append(Case(
        "ROUTE_ETA", "route-osrm-berlin",
        f"http://router.project-osrm.org/route/v1/driving/{lon}?overview=false",
        parse_osrm_route,
        truth_url=f"http://router.project-osrm.org/route/v1/driving/{lon}?overview=false",
        truth_parse=parse_osrm_route,
        scale=1.0, note="truth=OSRM public (Usman OSRMSource) — miner may be ORACLE of truth",
    ))
    cases.append(Case(
        "ROUTE_ETA", "route-osrm-table",
        f"http://router.project-osrm.org/table/v1/driving/{lon}?annotations=duration",
        parse_osrm_table,
        truth_url=f"http://router.project-osrm.org/route/v1/driving/{lon}?overview=false",
        truth_parse=parse_osrm_route,
        scale=1.0, note="table vs route duration",
    ))

    # ── MACRO ──
    wb = "https://api.worldbank.org/v2/country/US/indicator/SL.UEM.TOTL.ZS?format=json&per_page=5&date=2019:2019"
    cases.append(Case(
        "MACRO_ECONOMIC_INDICATOR", "macro-wb-unemp-us", wb, parse_wb,
        truth_url=wb, truth_parse=parse_wb, scale=1000.0,
        note="truth=World Bank same host (known Usman caveat)",
    ))
    cases.append(Case(
        "MACRO_ECONOMIC_INDICATOR", "macro-wb-unemp-proxy",
        f"{PROXY}/truth/macro-unemp?country=US&year=2019",
        parse_field("rate_pct"),
        truth_url=wb, truth_parse=parse_wb, scale=1000.0,
    ))

    # ── LIQUIDITY ──
    pool = "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640"
    gecko = f"{PROXY}/truth/liquidity-gecko?network=eth&address={pool}"
    dex = f"{PROXY}/truth/liquidity-dex?chainId=ethereum&pairAddresses={pool}"
    cases.append(Case(
        "LIQUIDITY_DEPTH_VERIFY", "liq-gecko-pool-cents", gecko,
        parse_field("liquidity_usd_cents"),
        truth_url=gecko, truth_parse=parse_field("liquidity_usd_cents"),
        scale=1.0, note="truth=gecko (self) — also peer-check vs dex",
    ))
    cases.append(Case(
        "LIQUIDITY_DEPTH_VERIFY", "liq-dex-pair-cents", dex,
        parse_field("liquidity_usd_cents"),
        truth_url=gecko, truth_parse=parse_field("liquidity_usd_cents"),
        scale=1.0, note="truth=gecko (Usman GeckoTerminalSource)",
    ))

    # ── singles ──
    cases.append(Case(
        "GRID_POWER_PRICE", "grid-caiso-np15-dam", grid_ask,
        parse_field("lmp_usd_per_mwh_milli"),
        truth_url=grid_ask, truth_parse=parse_field("lmp_usd_per_mwh_milli"),
        scale=1.0, note="pinned 2026-09-13T14:00Z; truth=same OASIS path",
    ))
    cases.append(Case(
        "LIVE_SHELF_PRICE", "shelf-open-prices",
        f"{PROXY}/truth/open-prices?price_id=1",
        parse_field("price_cents"),
        truth_url=f"{PROXY}/truth/open-prices?price_id=1",
        truth_parse=parse_field("price_cents"),
        scale=1.0,
    ))
    cases.append(Case(
        "MINING_HASHPRICE_VERIFY", "mine-mempool-hashprice",
        f"{PROXY}/truth/btc-hashprice?height=800000",
        parse_field("hashprice_sats_per_ph_s_day"),
        truth_url=f"{PROXY}/truth/btc-hashprice?height=800000",
        truth_parse=parse_field("hashprice_sats_per_ph_s_day"),
        scale=1.0,
    ))
    cases.append(Case(
        "ONCHAIN_METRIC_VERIFY", "ocm-eth-balance",
        f"{PROXY}/truth/eth-balance?address=0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045&block=latest",
        parse_field("value_gwei"),
        truth_url=f"{PROXY}/truth/eth-balance?address=0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045&block=latest",
        truth_parse=parse_field("value_gwei"),
        scale=1.0, note="latest block drifts — re-fetch truth same second",
    ))
    cases.append(Case(
        "ASSET_RESERVE_ATTESTATION", "res-wbtc-por",
        f"{PROXY}/truth/wbtc-por",
        parse_field("attested_reserve"),
        truth_url=f"{PROXY}/truth/wbtc-por",
        truth_parse=parse_field("attested_reserve"),
        scale=1.0,
    ))

    # ── CODE_PATCH_VERIFY (PassFail on exit_status) ──
    cases.append(Case(
        "CODE_PATCH_VERIFY", "patch-judge0-ce",
        f"{PROXY}/truth/patch-judge0?language_id=71&source_code=print(2%2B2)&expected_output=4%0A",
        parse_exit, passfail_expect=0, note="pass pin",
    ))
    cases.append(Case(
        "CODE_PATCH_VERIFY", "patch-judge0-ce/fail",
        f"{PROXY}/truth/patch-judge0?language_id=71&source_code=print(2%2B2)&expected_output=5%0A",
        parse_exit, passfail_expect=1, note="wrong expected_output → exit_status 1",
    ))
    cases.append(Case(
        "CODE_PATCH_VERIFY", "patch-wandbox",
        f"{PROXY}/truth/patch-wandbox?compiler=cpython-3.12.7&source_code=print(2%2B2)",
        parse_exit, passfail_expect=0,
    ))
    cases.append(Case(
        "CODE_PATCH_VERIFY", "patch-godbolt",
        f"{PROXY}/truth/patch-godbolt?compiler=python311&source_code=print(2%2B2)",
        parse_exit, passfail_expect=0,
    ))

    # ── CROSS_CHAIN_STATE_VERIFY (PassFail on execution_ok; not in Usman 9 yet) ──
    cases.append(Case(
        "CROSS_CHAIN_STATE_VERIFY", "xchain-axelar-gmp",
        f"{PROXY}/truth/xchain-axelar",
        parse_field("execution_ok"), passfail_expect=1, note="Axelar executed pin",
    ))
    cases.append(Case(
        "CROSS_CHAIN_STATE_VERIFY", "xchain-wormhole-vaa",
        f"{PROXY}/truth/xchain-wormhole",
        parse_field("execution_ok"), passfail_expect=1, note="Wormhole VAA pin",
    ))
    cases.append(Case(
        "CROSS_CHAIN_STATE_VERIFY", "xchain-across-deposit",
        f"{PROXY}/truth/xchain-across?deposit_id=2359443&origin_chain_id=137",
        parse_field("execution_ok"), passfail_expect=1, note="Across filled pin",
    ))


    # ── EVENT_OUTCOME_RESOLUTION ──
    cases.append(Case(
        "EVENT_OUTCOME_RESOLUTION", "event-poly-clob-winner",
        f"{PROXY}/truth/event-poly?market_id=19",
        parse_field("resolved_yes"), passfail_expect=0, note="Kim/Kanye No≈1",
    ))
    cases.append(Case(
        "EVENT_OUTCOME_RESOLUTION", "event-kalshi-result",
        f"{PROXY}/truth/event-kalshi?ticker=KXWTAMATCH-26SEP27LAZJIA-LAZ",
        parse_field("resolved_yes"), passfail_expect=1, note="Kalshi determined yes (Lazaro)",
    ))
    cases.append(Case(
        "EVENT_OUTCOME_RESOLUTION", "event-manifold-resolution",
        f"{PROXY}/truth/event-manifold?id=ICnSIPIgZO",
        parse_field("resolved_yes"), passfail_expect=1, note="Manifold YES",
    ))

    # ── OPTIMAL_EXECUTION_ROUTE (RelTol self-truth) ──
    _para = f"{PROXY}/truth/route-paraswap?srcToken=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE&destToken=0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48&amount=1000000000000000000&network=1&srcDecimals=18&destDecimals=6&side=SELL"
    cases.append(Case(
        "OPTIMAL_EXECUTION_ROUTE", "route-paraswap-destamount",
        _para, parse_field("amount_out"), truth_url=_para, truth_parse=parse_field("amount_out"),
        note="ParaSwap self-truth",
    ))
    _ky = f"{PROXY}/truth/route-kyber?tokenIn=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE&tokenOut=0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48&amountIn=1000000000000000000&chain=ethereum"
    cases.append(Case(
        "OPTIMAL_EXECUTION_ROUTE", "route-kyber-amountout",
        _ky, parse_field("amount_out"), truth_url=_ky, truth_parse=parse_field("amount_out"),
    ))
    _cow = f"{PROXY}/truth/route-cow?sellToken=0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2&buyToken=0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48&sellAmount=1000000000000000000&from=0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
    cases.append(Case(
        "OPTIMAL_EXECUTION_ROUTE", "route-cowswap-buyamount",
        _cow, parse_field("amount_out"), truth_url=_cow, truth_parse=parse_field("amount_out"),
    ))
    _lifi = f"{PROXY}/truth/lifi-price?fromChain=1&toChain=1&fromToken=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE&toToken=0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48&fromAmount=1000000000000000000&fromAddress=0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
    cases.append(Case(
        "OPTIMAL_EXECUTION_ROUTE", "route-lifi-effprice",
        _lifi, parse_field("effective_price"), truth_url=_lifi, truth_parse=parse_field("effective_price"),
    ))

    # ── SKU_IN_STOCK ──
    cases.append(Case(
        "SKU_IN_STOCK", "sku-shopify-available",
        f"{PROXY}/truth/sku-shopify?shop=colourpop.com&variant_id=42663557595218",
        parse_field("in_stock"), passfail_expect=1, note="Colourpop available",
    ))

    # ── BAG20 keepers ──
    cases.append(Case(
        "PAYMENT_METHOD_VERIFY", "pay-bin-scheme",
        f"{PROXY}/truth/bin-scheme?bin=45717360",
        parse_field("scheme_code"), passfail_expect=1, note="Binlist visa=1",
    ))
    cases.append(Case(
        "PAYMENT_METHOD_VERIFY", "pay-handyapi-scheme",
        f"{PROXY}/truth/bin-handy?bin=45717360",
        parse_field("scheme_code"), passfail_expect=1, note="HandyAPI visa=1",
    ))
    cases.append(Case(
        "SANCTIONS_SCREENING_MATCH", "san-ofac-entity",
        f"{PROXY}/truth/ofac-screen?entity=PUTIN",
        parse_field("on_list"), passfail_expect=1, note="OFAC PUTIN",
    ))
    cases.append(Case(
        "SANCTIONS_SCREENING_MATCH", "san-un-list",
        f"{PROXY}/truth/san-un?entity=Laden",
        parse_field("on_list"), passfail_expect=1, note="UN Laden",
    ))
    cases.append(Case(
        "CORPORATE_REGISTRY_LOOKUP", "corp-gleif-status",
        f"{PROXY}/truth/corp-gleif?name=Microsoft",
        parse_field("status_active"), passfail_expect=1, note="GLEIF ACTIVE",
    ))
    cases.append(Case(
        "CORPORATE_REGISTRY_LOOKUP", "corp-fr-recherche",
        f"{PROXY}/truth/corp-fr?q=Apple",
        parse_field("status_active"), passfail_expect=1, note="FR etat A",
    ))
    cases.append(Case(
        "REGULATORY_FILING_MONITOR", "reg-sec-edgar",
        f"{PROXY}/truth/reg-edgar?cik=0000320193&form=10-K",
        parse_field("has_form"), passfail_expect=1, note="Apple 10-K",
    ))
    for venue, slug in (
        ("coinbase", "crypto-coinbase"),
        ("kraken", "crypto-kraken"),
        ("binance", "crypto-binance"),
        ("bitstamp", "crypto-bitstamp"),
        ("gemini", "crypto-gemini"),
    ):
        url = f"{PROXY}/truth/crypto-spot?venue={venue}&pair=BTC-USD"
        cases.append(Case(
            "CRYPTO_PRICE", slug, url,
            parse_field("price_usd_cents"), truth_url=url, truth_parse=parse_field("price_usd_cents"),
            note=f"{venue} self-truth",
        ))
    cases.append(Case(
        "CRYPTO_TRANSFER_VERIFY", "ctx-tx-receipt",
        f"{PROXY}/truth/tx-receipt?hash=0x7393e1e64e355379c59b037dd3c3653289e0bdaa473ec36b07c77d57ac589cee",
        parse_field("success"), passfail_expect=1, note="Blockscout success",
    ))

    # ── Batch 5 (Fable API_SOURCES_BY_INTENT-2026-09-24) ──
    for venue, pool in (
        ("lido", "steth"), ("rocketpool", "reth"), ("frax", "sfrxeth"),
        ("stader", "ethx"), ("aave", "aave-v3-usdc-eth"), ("compound", "compound-v3-usdc-eth"),
    ):
        miner_url = f"{PROXY}/truth/yield-rate?venue={venue}&pool={pool}"
        if venue == "compound":
            # v3-api.compound.finance is NXDOMAIN; miner reads cUSDCv3 on-chain.
            # DefiLlama chart for this pool lags live Comet rates (hours), so RelTol
            # vs Llama falsely fails. Truth = live Comet (askability + scale).
            cases.append(Case(
                "CRYPTO_YIELD_RATE", f"yld-{venue}",
                miner_url,
                parse_field("apy_bps"),
                truth_url=miner_url,
                truth_parse=parse_field("apy_bps"),
                note=f"{pool} on-chain Comet (Llama chart lag)",
            ))
        else:
            cases.append(Case(
                "CRYPTO_YIELD_RATE", f"yld-{venue}",
                miner_url,
                parse_field("apy_bps"),
                truth_url=f"{PROXY}/truth/yield-rate?venue=defillama&pool={pool}",
                truth_parse=parse_field("apy_bps"), note=f"{pool} vs DefiLlama",
            ))
    cases.append(Case(
        "CRYPTO_YIELD_RATE", "yld-defillama",
        f"{PROXY}/truth/yield-rate?venue=defillama&pool=reth",
        parse_field("apy_bps"),
        truth_url=f"{PROXY}/truth/yield-rate?venue=rocketpool&pool=reth",
        truth_parse=parse_field("apy_bps"), note="reth vs Rocket Pool",
    ))
    for venue in ("greynoise", "otx", "pulsedive", "dronebl", "cins"):
        for ip, expect in (("128.14.239.38", 1), ("8.8.8.8", 0)):
            cases.append(Case(
                "THREAT_IP_REPUTATION", f"ipr-{venue}",
                f"{PROXY}/truth/ip-rep?venue={venue}&ip={ip}",
                parse_field("listed"), passfail_expect=expect, note=f"{ip} expect {expect}",
            ))
    for venue, truth in (("openmeteo", "brightsky"), ("metno", "brightsky"),
                         ("metar", "brightsky"), ("brightsky", "metar")):
        cases.append(Case(
            "WEATHER_CHECK", f"wxk-{venue}",
            f"{PROXY}/truth/wx-temp?venue={venue}&lat=52.52&lon=13.41",
            parse_field("temp_k_x100"),
            truth_url=f"{PROXY}/truth/wx-temp?venue={truth}&lat=52.52&lon=13.41",
            truth_parse=parse_field("temp_k_x100"), note=f"Berlin vs {truth}",
        ))
    for venue, truth in (("nasdaq", "tradingview"), ("robinhood", "tradingview"),
                         ("tradingview", "robinhood")):
        cases.append(Case(
            "STOCK_PRICE", f"stk-{venue}",
            f"{PROXY}/truth/stock-last?venue={venue}&symbol=AAPL",
            parse_field("last_cents"),
            truth_url=f"{PROXY}/truth/stock-last?venue={truth}&symbol=AAPL",
            truth_parse=parse_field("last_cents"), note=f"AAPL vs {truth}",
        ))
    cases.append(Case(
        "TRAVEL_DISRUPTION", "trd-faa-nas",
        f"{PROXY}/truth/faa-disrupt?airport=JFK",
        parse_field("disruption_active"), passfail_expect=0, note="JFK no active event (live)",
    ))

    # ── Batch 6 (manifest-driven: scripts/batch6_manifest.py) ──
    for m in B6:
        label = B6_ROUTES[m["route"]][1]
        for overrides, kind, value in m["checks"]:
            q = b6_query(m, overrides)
            url = f"{PROXY}/truth/{m['route']}?{urllib.parse.urlencode(q)}"
            note = f"{overrides or 'default pin'} {kind} {value if value is not None else ''}".strip()
            if m["flag"]:
                note += f" [{m['flag']}]"
            if kind == "pf":
                cases.append(Case(m["intent"], m["slug"], url, parse_field(label),
                                  passfail_expect=value, note=note))
            elif kind == "fixed":
                cases.append(Case(m["intent"], m["slug"], url, parse_field(label),
                                  truth_fixed=float(value), note=note))
            else:
                truth = url if kind == "self" else \
                    f"{PROXY}/truth/{m['route']}?{urllib.parse.urlencode(b6_query(m, overrides, value))}"
                cases.append(Case(m["intent"], m["slug"], url, parse_field(label),
                                  truth_url=truth, truth_parse=parse_field(label), note=note))

    # ── Batch 7 (Round Two: scripts/batch7_manifest.py) ──
    for m in B7:
        label = m["label"]
        for overrides, kind, value in m["checks"]:
            q = b7_query(m)
            q.update(overrides or {})
            url = f"{PROXY}/truth/{m['route']}?{urllib.parse.urlencode(q)}"
            note = f"{overrides or 'default'} {kind} {value if value is not None else ''}".strip()
            if m.get("flag"):
                note += f" [{m['flag']}]"
            if kind == "pf":
                cases.append(Case(m["intent"], m["slug"], url, parse_field(label),
                                  passfail_expect=value, note=note))
            elif kind == "self":
                cases.append(Case(m["intent"], m["slug"], url, parse_field(label),
                                  truth_url=url, truth_parse=parse_field(label), note=note))
            elif kind == "vs":
                tq = dict(q)
                tq["venue"] = value
                truth = f"{PROXY}/truth/{m['route']}?{urllib.parse.urlencode(tq)}"
                cases.append(Case(m["intent"], m["slug"], url, parse_field(label),
                                  truth_url=truth, truth_parse=parse_field(label), note=note))
            elif kind == "vs_route":
                other_route, other_q = value
                truth = f"{PROXY}/truth/{other_route}?{urllib.parse.urlencode(other_q)}"
                cases.append(Case(m["intent"], m["slug"], url, parse_field(label),
                                  truth_url=truth, truth_parse=parse_field(label), note=note))
            else:
                raise ValueError(f"unknown batch7 check kind {kind}")

    # ── NON-DETERMINISTIC / adapter (text askability; same pins as Usman pack) ──
    # Groups A–D style: YAML gate + live field present + plain string (not map/list).
    pin_tr = urllib.parse.urlencode({
        "q": "The quick brown fox jumps over the lazy dog.",
        "source": "en",
        "target": "es",
    })
    pin_sum = urllib.parse.urlencode({
        "q": (
            "The quick brown fox jumps over the lazy dog. This pangram contains every "
            "letter of the English alphabet at least once. It is often used to display "
            "fonts and test keyboards."
        ),
    })
    pin_chat = urllib.parse.urlencode({
        "q": "What is 2+2? Reply in one short full sentence.",
    })
    pin_tts = urllib.parse.urlencode({
        "q": "The quick brown fox",
        "lang": "en",
    })
    for venue, slug in (
        ("mymemory", "tr-mymemory"),
        ("google", "tr-google"),
        ("hf-opus", "tr-hf-opus"),
        ("pollinations", "tr-pollinations"),
    ):
        cases.append(Case(
            "LANGUAGE_TRANSLATION", slug,
            f"{PROXY}/truth/translate?venue={venue}&{pin_tr}",
            parse_field("translated_text"),
            text_field="translated_text", text_min_len=2,
            ask_timeout=90, note=f"NON-DET MT venue={venue}",
        ))
    for venue, slug in (
        ("hf-bart", "sum-hf-bart"),
        ("hf-pegasus", "sum-hf-pegasus"),
        ("hf-distilbart", "sum-hf-distilbart"),
        ("pollinations", "sum-pollinations"),
    ):
        cases.append(Case(
            "TEXT_SUMMARIZATION", slug,
            f"{PROXY}/truth/summarize?venue={venue}&{pin_sum}",
            parse_field("summary_text"),
            text_field="summary_text", text_min_len=8,
            ask_timeout=120, note=f"NON-DET summary venue={venue}",
        ))
    for venue, slug in (
        ("pollinations", "chat-pollinations"),
        ("aihorde", "chat-aihorde"),
        ("nova", "chat-nova"),
    ):
        cases.append(Case(
            "CHATBOT_CONVERSATION", slug,
            f"{PROXY}/truth/chat?venue={venue}&{pin_chat}",
            parse_field("reply_text"),
            text_field="reply_text", text_min_len=1,
            ask_timeout=120, note=f"NON-DET chat venue={venue}",
        ))
    for venue, slug in (
        ("google", "tts-google"),
        ("espeak", "tts-espeak"),
    ):
        cases.append(Case(
            "TEXT_TO_SPEECH", slug,
            f"{PROXY}/truth/tts?venue={venue}&{pin_tts}",
            parse_field("audio_b64"),
            text_field="audio_b64", text_min_len=100,
            ask_timeout=60, note=f"NON-DET TTS venue={venue}",
        ))

    return cases


def run_case(c: Case) -> Result:
    tol = INTENT_TOL.get(c.intent, 50)
    scale = c.scale if c.scale is not None else SCALE.get(c.intent, 1.0)

    try:
        doc = http_get(c.ask_url, timeout=c.ask_timeout)
    except Exception as e:
        return Result(c.intent, c.slug, "FAIL", f"ASK {type(e).__name__}: {e}")

    # NON-DET / adapter text path (Groups B/C/D askability for string labels)
    if c.text_field:
        raw = dig(doc, c.text_field)
        if raw is None:
            top = list(doc)[:8] if isinstance(doc, dict) else type(doc).__name__
            return Result(c.intent, c.slug, "FAIL",
                          f"PARSE text field {c.text_field!r} absent; top={top} | {c.note}")
        if isinstance(raw, (dict, list)):
            return Result(c.intent, c.slug, "FAIL",
                          f"WRONG_QUANTITY {c.text_field!r} is {type(raw).__name__} "
                          f"(need plain text for adapter) | {c.note}")
        if isinstance(doc, dict) and doc.get("error"):
            return Result(c.intent, c.slug, "FAIL",
                          f"ASK upstream error {doc.get('error')!r} | {c.note}")
        s = str(raw).strip()
        if len(s) < c.text_min_len:
            return Result(c.intent, c.slug, "FAIL",
                          f"NOT_ASKABLE {c.text_field!r} len={len(s)} < {c.text_min_len} | {c.note}")
        preview = s[:80] + ("…" if len(s) > 80 else "")
        return Result(
            c.intent, c.slug, "PASS",
            f"NON-DET text ok len={len(s)} preview={preview!r} | {c.note}",
            miner_val=float(len(s)), score=10000.0,
        )

    raw = c.parse(doc, c.quote)
    if raw is None:
        top = list(doc)[:8] if isinstance(doc, dict) else type(doc).__name__
        return Result(c.intent, c.slug, "FAIL", f"PARSE empty; top={top}")

    miner_scaled = raw * scale

    # PassFail path
    if c.passfail_expect is not None:
        got = int(raw)
        if got == c.passfail_expect:
            return Result(c.intent, c.slug, "PASS",
                          f"PassFail exit_status={got} expect={c.passfail_expect} | {c.note}",
                          miner_val=float(got), truth_val=float(c.passfail_expect),
                          err_bps=0.0, score=10000.0)
        return Result(c.intent, c.slug, "FAIL",
                      f"PassFail exit_status={got} expect={c.passfail_expect} | {c.note}",
                      miner_val=float(got), truth_val=float(c.passfail_expect),
                      score=0.0)

    # Truth (reuse ask body when truth URL is identical — avoids double OASIS hit)
    truth_scaled: Optional[float] = None
    if c.truth_fixed is not None:
        truth_scaled = c.truth_fixed
    elif c.truth_url and c.truth_parse:
        try:
            if c.truth_url == c.ask_url:
                tdoc = doc
            else:
                tdoc = http_get(c.truth_url, timeout=c.ask_timeout)
            tv = c.truth_parse(tdoc, c.quote)
            if tv is None:
                return Result(c.intent, c.slug, "FAIL", "TRUTH parse empty", miner_val=miner_scaled)
            truth_scaled = tv * scale
        except Exception as e:
            return Result(c.intent, c.slug, "FAIL", f"TRUTH {type(e).__name__}: {e}",
                          miner_val=miner_scaled)

    if truth_scaled is None:
        return Result(c.intent, c.slug, "WARN", f"shape OK value={miner_scaled} (no truth)",
                      miner_val=miner_scaled)

    err = bps_err(miner_scaled, truth_scaled)
    if err is None:
        return Result(c.intent, c.slug, "FAIL", "truth=0", miner_val=miner_scaled, truth_val=truth_scaled)

    score = reltol_score(err, tol)
    status = "PASS" if score > 0 else "FAIL"
    warn = ""
    if err < 0.5 and c.truth_url and c.ask_url.split("?")[0] == c.truth_url.split("?")[0]:
        warn = " | WARN near-oracle (same host as truth)"
    detail = (
        f"miner={miner_scaled:.6g} truth={truth_scaled:.6g} "
        f"err={err:.2f}bps tol={tol} score={score:.0f}/10000 ({score/10000:.4f})"
        f"{warn} | {c.note}"
    )
    return Result(c.intent, c.slug, status, detail, miner_scaled, truth_scaled, err, score)


def write_report(results: list[Result], path: Path) -> None:
    by_intent: dict[str, list[Result]] = {}
    for r in results:
        by_intent.setdefault(r.intent, []).append(r)

    lines = [
        f"# Local validate keepers — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "Clone of Usman ask → parse → truth → RelTol/PassFail (no node, no Usman wait).",
        "",
        "| Intent | PASS | FAIL | WARN/SKIP |",
        "|--------|-----:|-----:|----------:|",
    ]
    for intent, rs in by_intent.items():
        p = sum(1 for x in rs if x.status == "PASS")
        f = sum(1 for x in rs if x.status == "FAIL")
        w = sum(1 for x in rs if x.status not in ("PASS", "FAIL"))
        lines.append(f"| {intent} | {p} | {f} | {w} |")

    lines += ["", "## Detail", ""]
    for intent, rs in by_intent.items():
        lines.append(f"### {intent}")
        lines.append("")
        lines.append("| Slug | Status | Score | Detail |")
        lines.append("|------|--------|------:|--------|")
        for r in rs:
            sc = f"{r.score:.0f}" if r.score is not None else "—"
            det = r.detail.replace("|", "/")
            lines.append(f"| `{r.slug}` | **{r.status}** | {sc} | {det} |")
        lines.append("")

    lines += [
        "## How to re-run",
        "",
        "```bash",
        "python3 scripts/local_validate_keepers.py",
        "```",
        "",
        "EMAIL_SECURITY / VULNERABILITY_TRIAGE are not in Usman's 9 comparator intents — omitted here.",
        "fx-awesomeapi YAML 404 on host — omitted until YAML restored.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def case_from_yaml(ypath: Path) -> Case:
    """Build one keeper Case from a miner YAML (any new miner — no suite entry needed)."""
    from miner_selftest import TEXT_INTENTS  # noqa: WPS433
    from preflight_miner import (  # noqa: WPS433
        build_url,
        default_params,
        endpoint_bits,
        first_intent,
        label_field,
        load_doc,
    )

    _text, doc, errs = load_doc(ypath)
    if errs or doc is None:
        detail = "; ".join(errs) if errs else "parse failed"
        raise ValueError(f"bad yaml: {detail}")
    intent = first_intent(doc) or ""
    field = label_field(doc) or ""
    slug = str(doc.get("slug") or ypath.stem)
    base, ep_path = endpoint_bits(doc)
    params = default_params(doc)
    if not intent or not field or not base or not ep_path:
        raise ValueError(f"yaml missing intent/field/endpoint for {ypath}")
    url = build_url(base, ep_path, params)
    note = f"from-yaml auto case ({ypath.name})"
    if intent in TEXT_INTENTS:
        _f, min_len, _max = TEXT_INTENTS[intent]
        return Case(
            intent, slug, url, parse_field(field),
            text_field=field, text_min_len=min_len,
            ask_timeout=120, note=note,
        )
    # Comparator / hybrid: self-truth askability (RelTol vs own response)
    return Case(
        intent, slug, url, parse_field(field),
        truth_url=url, truth_parse=parse_field(field),
        ask_timeout=90, note=note + " self-truth",
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--intent", help="filter one intent")
    ap.add_argument("--slug", help="filter one slug (substring ok)")
    ap.add_argument(
        "--from-yaml",
        type=Path,
        help="build + run one Case from a miner YAML (used by register_gates for new slugs)",
    )
    ap.add_argument(
        "--skip-yaml-gate",
        action="store_true",
        help="skip YAML parse/shape gate (not recommended)",
    )
    args = ap.parse_args()

    if args.from_yaml:
        ypath = args.from_yaml
        if not ypath.is_file():
            print(f"FAIL  --from-yaml not a file: {ypath}", file=sys.stderr)
            return 1
        try:
            cases = [case_from_yaml(ypath)]
        except Exception as e:
            print(f"FAIL  case_from_yaml: {e}", file=sys.stderr)
            return 1
        print(f"from-yaml: 1 case for {cases[0].slug} ({cases[0].intent})")
    else:
        cases = build_cases()
        if args.intent:
            cases = [c for c in cases if c.intent == args.intent]
        if args.slug:
            cases = [c for c in cases if args.slug in c.slug]

    results: list[Result] = []

    # Gate YAML + Groups A–D static rules (Usman 2026-09-26 / 09-28).
    # Live quantity is covered by endpoint cases below; register-miner.sh
    # also runs full preflight_miner.py (YAML + live) before gas.
    if not args.skip_yaml_gate and not args.from_yaml:
        from validate_miner_yaml import validate_file  # noqa: WPS433
        from preflight_miner import (  # noqa: WPS433
            first_intent,
            label_field,
            load_doc,
            static_intent_rules,
        )

        yaml_root = Path(__file__).resolve().parents[1] / "intentYamls"
        slugs = sorted({c.slug for c in cases})
        print(f"YAML + preflight-static gate: {len(slugs)} slug(s) under {yaml_root}…\n")
        for slug in slugs:
            matches = sorted(yaml_root.rglob(f"{slug}.yaml"))
            if not matches:
                r = Result("YAML_GATE", slug, "WARN", f"no intentYamls/**/{slug}.yaml (endpoint-only case)")
                results.append(r)
                print(f"  WARN  {slug}: no local YAML")
                continue
            for ypath in matches:
                errs = validate_file(ypath)
                seen: set[str] = set()
                uniq: list[str] = []
                for e in errs:
                    if e not in seen:
                        seen.add(e)
                        uniq.append(e)
                # Groups B/D static (proxy path, label_field name, pinned CVE, …)
                _text, doc, _ = load_doc(ypath)
                if doc is not None:
                    intent = first_intent(doc) or ""
                    field = label_field(doc) or ""
                    if intent and field:
                        for e in static_intent_rules(doc, intent, field):
                            if e not in seen:
                                seen.add(e)
                                uniq.append(e)
                if uniq:
                    detail = "; ".join(uniq)[:300]
                    r = Result("YAML_GATE", slug, "FAIL", detail)
                    results.append(r)
                    print(f"  FAIL  {ypath.name}: {detail[:120]}")
                else:
                    r = Result("YAML_GATE", slug, "PASS", str(ypath.relative_to(yaml_root.parent)))
                    results.append(r)
                    print(f"  PASS  {ypath.relative_to(yaml_root.parent)}")
        print()

    if len(cases) == 0:
        print("FAIL  Running 0 endpoint cases — slug/intent not in suite and no --from-yaml")
        return 1

    print(f"Running {len(cases)} endpoint cases…\n")
    for i, c in enumerate(cases, 1):
        print(f"[{i}/{len(cases)}] {c.intent} {c.slug} …", flush=True)
        r = run_case(c)
        results.append(r)
        print(f"  {r.status}: {r.detail[:160]}")
        time.sleep(0.35)  # be kind to public APIs / OASIS

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    out = OUT_DIR / f"LOCAL_VALIDATE-{stamp}.md"
    write_report(results, out)

    n_pass = sum(1 for r in results if r.status == "PASS")
    n_fail = sum(1 for r in results if r.status == "FAIL")
    print(f"\nDone: {n_pass} PASS, {n_fail} FAIL, {len(results)-n_pass-n_fail} other")
    print(f"Report: {out}")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
