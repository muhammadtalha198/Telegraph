#!/usr/bin/env python3
"""Round-2 API probes. Loads MinerCreator/.env; never prints secret values."""
from __future__ import annotations

import json
import os
import ssl
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = Path("/tmp/round2-probe.jsonl")


def load_env() -> None:
    for line in (ROOT / ".env").read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k, v.strip().strip('"').strip("'"))


CTX = ssl.create_default_context()


def req(url: str, method: str = "GET", headers: dict | None = None, data=None, timeout: int = 25):
    h = dict(headers or {})
    h.setdefault("User-Agent", "TeleGraph-Round2/1.0")
    body = None
    if data is not None:
        if isinstance(data, (dict, list)):
            body = json.dumps(data).encode()
            h.setdefault("Content-Type", "application/json")
        else:
            body = data if isinstance(data, bytes) else str(data).encode()
    r = urllib.request.Request(url, data=body, headers=h, method=method)
    try:
        with urllib.request.urlopen(r, timeout=timeout, context=CTX) as resp:
            raw = resp.read()[:1200]
            return resp.status, raw.decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        raw = e.read()[:600].decode("utf-8", "replace")
        return e.code, raw
    except Exception as e:  # noqa: BLE001
        return None, str(e)[:240]


def main() -> None:
    load_env()
    rows: list[dict] = []

    def add(intent: str, name: str, st, body: str, note: str = "") -> None:
        rows.append(
            {
                "intent": intent,
                "name": name,
                "status": st,
                "note": note,
                "body": (body or "")[:500],
            }
        )
        print(f"{intent:22} {name:30} HTTP={st}  {(body or '')[:100].replace(chr(10), ' ')}")

    hf = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACE_HUB_TOKEN")
    jina = os.environ.get("JINA_API_KEY")
    voy = os.environ.get("VOYAGE_API_KEY")
    uclass = os.environ.get("UCLASSIFY_READ_KEY")
    ab = os.environ.get("ABUSEIPDB_API_KEY")

    # --- SEMANTIC_SIMILARITY (keys) ---
    st, body = req(
        "https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2/pipeline/sentence-similarity",
        "POST",
        {"Authorization": f"Bearer {hf}"},
        {
            "inputs": {
                "source_sentence": "a sunny day in berlin",
                "sentences": ["a bright day in berlin", "the stock market crashed"],
            }
        },
    )
    add("SEMANTIC_SIMILARITY", "hf-minilm-sim", st, body, "cosine scores array")

    st, body = req(
        "https://api-inference.huggingface.co/pipeline/sentence-similarity/sentence-transformers/all-MiniLM-L6-v2",
        "POST",
        {"Authorization": f"Bearer {hf}"},
        {
            "inputs": {
                "source_sentence": "a sunny day in berlin",
                "sentences": ["a bright day in berlin", "crash"],
            }
        },
    )
    add("SEMANTIC_SIMILARITY", "hf-api-inference-sim", st, body)

    st, body = req(
        "https://api.jina.ai/v1/embeddings",
        "POST",
        {"Authorization": f"Bearer {jina}"},
        {
            "model": "jina-embeddings-v3",
            "task": "text-matching",
            "input": ["a sunny day in berlin", "a bright day in berlin"],
        },
    )
    add("SEMANTIC_SIMILARITY", "jina-embeddings-v3", st, body, "proxy must cosine")

    st, body = req(
        "https://api.voyageai.com/v1/embeddings",
        "POST",
        {"Authorization": f"Bearer {voy}"},
        {"model": "voyage-3-lite", "input": ["a sunny day in berlin", "a bright day in berlin"]},
    )
    add("SEMANTIC_SIMILARITY", "voyage-3-lite", st, body, "proxy must cosine")

    # --- TEXT_CLASSIFICATION (keys) ---
    st, body = req(
        "https://router.huggingface.co/hf-inference/models/facebook/bart-large-mnli",
        "POST",
        {"Authorization": f"Bearer {hf}"},
        {"inputs": "I love this product", "parameters": {"candidate_labels": ["positive", "negative"]}},
    )
    add("TEXT_CLASSIFICATION", "hf-bart-mnli", st, body, "zero-shot top label")

    st, body = req(
        "https://router.huggingface.co/hf-inference/models/distilbert-base-uncased-finetuned-sst-2-english",
        "POST",
        {"Authorization": f"Bearer {hf}"},
        {"inputs": "I love this product"},
    )
    add("TEXT_CLASSIFICATION", "hf-sst2", st, body)

    st, body = req(
        "https://router.huggingface.co/hf-inference/models/cardiffnlp/twitter-roberta-base-sentiment-latest",
        "POST",
        {"Authorization": f"Bearer {hf}"},
        {"inputs": "I love this product"},
    )
    add("TEXT_CLASSIFICATION", "hf-twitter-roberta", st, body)

    st, body = req(
        "https://api.uclassify.com/v1/uClassify/Sentiment/classify/?text=I%20love%20this%20product",
        headers={"Authorization": f"Token {uclass}"},
    )
    add("TEXT_CLASSIFICATION", "uclassify-sentiment", st, body)

    # Topics classifier (distinct from sentiment)
    st, body = req(
        "https://api.uclassify.com/v1/uClassify/Topics/classify/?text=The%20stock%20market%20rose%20today",
        headers={"Authorization": f"Token {uclass}"},
    )
    add("TEXT_CLASSIFICATION", "uclassify-topics", st, body, "topics ≠ sentiment; pin carefully")

    # --- THREAT_IP ---
    st, body = req(
        "https://api.abuseipdb.com/api/v2/check?ipAddress=8.8.8.8&maxAgeInDays=90",
        headers={"Key": ab, "Accept": "application/json"},
    )
    add("THREAT_IP_REPUTATION", "abuseipdb-8.8.8.8", st, body, "abuseConfidenceScore")

    st, body = req(
        "https://api.abuseipdb.com/api/v2/check?ipAddress=185.220.101.1&maxAgeInDays=90",
        headers={"Key": ab, "Accept": "application/json"},
    )
    add("THREAT_IP_REPUTATION", "abuseipdb-tor", st, body)

    # --- keyless candidates ---
    doh_h = {"Accept": "application/dns-json"}
    keyless = [
        ("WEATHER_CHECK", "met-norway", "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=52.52&lon=13.41", {}),
        ("WEATHER_CHECK", "open-meteo-current", "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m", {}),
        ("WEATHER_CHECK", "7timer", "http://www.7timer.info/bin/api.pl?lon=13.41&lat=52.52&product=civil&output=json", {}),
        ("WEATHER_CHECK", "wttr-j1", "https://wttr.in/Berlin?format=j1", {}),
        ("AIR_QUALITY_INDEX", "cerns-berlin", "https://cerns.io/api/v1/public/city/berlin/aqi", {}),
        ("AIR_QUALITY_INDEX", "infranode-uba", "https://infranode.dev/api/v1/cities/berlin/air-uba", {}),
        ("DNS_RECORD_LOOKUP", "quad9-doh", "https://dns.quad9.net:5053/dns-query?name=example.com&type=A", doh_h),
        ("DNS_RECORD_LOOKUP", "mullvad-doh", "https://doh.mullvad.net/dns-query?name=example.com&type=A", doh_h),
        ("DNS_RECORD_LOOKUP", "controld-doh", "https://freedns.controld.com/dns-query?name=example.com&type=A", doh_h),
        ("DNS_RECORD_LOOKUP", "alidns", "https://dns.alidns.com/resolve?name=example.com&type=A", {}),
        ("DNS_RECORD_LOOKUP", "dns-sb-json", "https://doh.dns.sb/dns-query?name=example.com&type=A", doh_h),
        ("CRYPTO_PRICE", "okx", "https://www.okx.com/api/v5/market/ticker?instId=BTC-USDT", {}),
        ("CRYPTO_PRICE", "htx", "https://api.huobi.pro/market/detail/merged?symbol=btcusdt", {}),
        ("CRYPTO_PRICE", "mexc", "https://api.mexc.com/api/v3/ticker/price?symbol=BTCUSDT", {}),
        ("CRYPTO_PRICE", "gate", "https://api.gateio.ws/api/v4/spot/tickers?currency_pair=BTC_USDT", {}),
        ("CRYPTO_PRICE", "bitfinex", "https://api-pub.bitfinex.com/v2/ticker/tBTCUSD", {}),
        ("CRYPTO_PRICE", "bybit", "https://api.bybit.com/v5/market/tickers?category=spot&symbol=BTCUSDT", {}),
        ("CRYPTO_PRICE", "kucoin", "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT", {}),
        ("STOCK_PRICE", "stooq-aapl", "https://stooq.com/q/l/?s=aapl.us&f=sd2t2ohlcv&h&e=csv", {}),
        ("STOCK_PRICE", "yahoo-chart", "https://query1.finance.yahoo.com/v8/finance/chart/AAPL?interval=1d&range=1d", {}),
        ("STOCK_PRICE", "finnhub-needkey", "https://finnhub.io/api/v1/quote?symbol=AAPL", {}),
        ("SSL_VERIFICATION", "crtsh-identrust", "https://crt.sh/?q=%.badssl.com&output=json", {}),
        ("GAS_PRICE", "blocknative-137", "https://api.blocknative.com/gasprices/blockprices?chainid=137", {}),
        ("GAS_PRICE", "eth-rpc-feehist", "https://polygon-rpc.com", {}),  # special POST below
        ("WEB_SEARCH", "searx-privau", "https://priv.au/search?q=telegraph+protocol&format=json", {}),
        ("WEB_SEARCH", "searx-ononoki", "https://search.ononoki.org/search?q=telegraph&format=json", {}),
        ("FX_NOW", "fawaz-jsdelivr", "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json", {}),
        ("FX_NOW", "exchangerate-host", "https://api.exchangerate.host/latest?base=USD&symbols=EUR", {}),
        ("FX_NOW", "open-er-api", "https://open.er-api.com/v6/latest/USD", {}),
        ("SANCTIONS_SCREENING_MATCH", "opensanctions-noauth", "https://api.opensanctions.org/search/default?q=putin", {}),
        ("CORPORATE_REGISTRY_LOOKUP", "gleif-lei", "https://api.gleif.org/api/v1/lei-records?filter[entity.legalName]=Apple&page[size]=1", {}),
        ("CORPORATE_REGISTRY_LOOKUP", "brreg-enhet", "https://data.brreg.no/enhetsregisteret/api/enheter?navn=Equinor&size=1", {}),
        ("REGULATORY_FILING_MONITOR", "sec-submissions", "https://data.sec.gov/submissions/CIK0000320193.json", {"User-Agent": "TeleGraph Round2 research contact@example.com"}),
        ("EMAIL_SECURITY", "quad9-dmarc", "https://dns.quad9.net:5053/dns-query?name=_dmarc.gmail.com&type=TXT", doh_h),
        ("EMAIL_SECURITY", "mullvad-mx", "https://doh.mullvad.net/dns-query?name=gmail.com&type=MX", doh_h),
        ("VULNERABILITY_TRIAGE", "ghsa", "https://api.github.com/advisories?cve_id=CVE-2024-3094", {"Accept": "application/vnd.github+json"}),
        ("VULNERABILITY_TRIAGE", "redhat-cve", "https://access.redhat.com/hydra/rest/securitydata/cve/CVE-2024-3094.json", {}),
        ("VULNERABILITY_TRIAGE", "debian-tracker", "https://security-tracker.debian.org/tracker/CVE-2024-3094", {}),
        ("MACRO_ECONOMIC_INDICATOR", "fred-needkey", "https://api.stlouisfed.org/fred/series/observations?series_id=UNRATE&file_type=json", {}),
        ("MACRO_ECONOMIC_INDICATOR", "oecd-sdmx", "https://sdmx.oecd.org/public/rest/data/OECD.SDD.TPS,DSD_LFS@DF_IALFS_INDIC,1.0/USA.UNE_LF_M.Y.M.?startPeriod=2023&dimensionAtObservation=AllDimensions&format=jsondata", {}),
        ("ROUTE_ETA", "graphhopper-demo", "https://graphhopper.com/api/1/route?point=52.5,13.4&point=52.52,13.41&vehicle=car&type=json&key=", {}),
        ("ROUTE_ETA", "valhalla-demo", "https://valhalla1.openstreetmap.de/route", {}),
        ("PORT_SCAN_AUDIT", "hackertarget-ports", "https://api.hackertarget.com/nmap/?q=scanme.nmap.org", {}),
        ("CONTENT_EXTRACTION", "r-jina", "https://r.jina.ai/http://example.com", {}),
        ("CONTENT_EXTRACTION", "defuddle", "https://r.jina.ai/http://example.com", {}),  # placeholder skip dup
        ("SENTIMENT_ANALYSIS", "hf-sst2-key", "skip", {}),
        ("GRAMMAR_SPELL_CHECK", "languagetool-org", "https://api.languagetool.org/v2/check", {}),
        ("CODE_PATCH_VERIFY", "glot-run", "https://glot.io/snippets", {}),
        ("CODE_PATCH_VERIFY", "onecompiler-needkey", "https://onecompiler.com/api", {}),
        ("SSL_VERIFICATION", "sslmate-ct", "https://api.certspotter.com/v1/issuances?domain=badssl.com&include_subdomains=true&expand=dns_names", {}),
        ("THREAT_INTELLIGENCE", "urlhaus-host", "https://urlhaus-api.abuse.ch/v1/host/", {}),
        ("THREAT_INTELLIGENCE", "malwarebazaar-need", "https://mb-api.abuse.ch/api/v1/", {}),
        ("CRYPTO_YIELD_RATE", "defillama-pools", "https://yields.llama.fi/pools", {}),
        ("CRYPTO_YIELD_RATE", "aave-v3-apr", "https://aave-api-v2.aave.com/data/liquidity/v2?poolId=0xb53c1a33016b2dc2ff3653530dfe2960cd57fc55", {}),
        ("TOKEN_TOTAL_SUPPLY_VERIFY", "eth-supply-rpc", "https://eth.llamarpc.com", {}),
        ("VALIDATOR_PERFORMANCE_VERIFY", "beaconcha", "https://beaconcha.in/api/v1/validator/1", {}),
        ("LOAN_INTEREST_RATE_QUOTE", "rba-f5", "https://www.rba.gov.au/statistics/tables/csv/f5-data.csv", {}),
        ("LOAN_INTEREST_RATE_QUOTE", "boe-bankrate", "https://www.bankofengland.co.uk/boeapps/database/_iadb-fromshowcolumns.asp?csv.x=yes&Datefrom=01/Jan/2024&Dateto=now&SeriesCodes=IUMABEDR&CSVF=TN&UsingCodes=Y&VPD=Y&VFD=N", {}),
        ("API_HEALTH_CHECK", "isup-downfor", "https://www.downforeveryoneorjustme.com/status/example.com", {}),
        ("SERVER_UPTIME_MONITOR", "isiton-check", "https://isiton.app/api/check?url=https://example.com", {}),
        ("VENDOR_VERIFY", "iban-com-calc", "https://openiban.com/validate/DE89370400440532013000", {}),
        ("VENDOR_VERIFY", "vatcomply-vat", "https://api.vatcomply.com/vat?vat_number=DE811111125", {}),
        ("CARRIER_SERVICEABILITY", "usps-needkey", "https://secure.shippingapis.com/ShippingAPI.dll", {}),
        ("TRAVEL_DISRUPTION", "faa-nas", "https://nasstatus.faa.gov/api/airport-status-information", {}),
        ("TRAVEL_DISRUPTION", "aviationstack-need", "http://api.aviationstack.com/v1/flights", {}),
        ("EVENT_OUTCOME_RESOLUTION", "polymarket-gamma", "https://gamma-api.polymarket.com/markets?limit=1&closed=true", {}),
        ("EVENT_OUTCOME_RESOLUTION", "metaculus", "https://www.metaculus.com/api2/questions/?limit=1&status=resolved", {}),
        ("OPTIMAL_EXECUTION_ROUTE", "1inch-quote", "https://api.1inch.dev/swap/v6.0/1/quote?src=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE&dst=0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48&amount=1000000000000000000", {}),
        ("OPTIMAL_EXECUTION_ROUTE", "0x-quote", "https://api.0x.org/swap/v1/quote?buyToken=USDC&sellToken=ETH&sellAmount=1000000000000000000", {}),
        ("SKU_IN_STOCK", "fakestore", "https://fakestoreapi.com/products/1", {}),
        ("SKU_IN_STOCK", "dummyjson", "https://dummyjson.com/products/1", {}),
        ("PAYMENT_METHOD_VERIFY", "binlist", "https://lookup.binlist.net/45717360", {}),
        ("PAYMENT_METHOD_VERIFY", "handyapi-bin", "https://data.handyapi.com/bin/45717360", {}),
        ("CROSS_CHAIN_STATE_VERIFY", "layerzero-scan", "https://api-mainnet.layerzero-scan.com/tx/0x0", {}),
        ("LIVE_SHELF_PRICE", "openfoodfacts", "https://world.openfoodfacts.org/api/v2/product/737628064502.json", {}),
        ("GRID_POWER_PRICE", "entsoe-need", "https://web-api.tp.entsoe.eu/api", {}),
        ("MINING_HASHPRICE_VERIFY", "hashrateindex-need", "https://api.hashrateindex.com", {}),
        ("ONCHAIN_METRIC_VERIFY", "defillama-tvl", "https://api.llama.fi/tvl/aave", {}),
        ("ASSET_RESERVE_ATTESTATION", "tether-transparency", "https://app.tether.to/transparency.json", {}),
        ("ASSET_RESERVE_ATTESTATION", "circle-attest", "https://api.circle.com/v1/stablecoins", {}),
        ("LIQUIDITY_DEPTH_VERIFY", "birdeye-need", "https://public-api.birdeye.so", {}),
        ("LIQUIDITY_DEPTH_VERIFY", "geckoterminal-token", "https://api.geckoterminal.com/api/v2/networks/eth/tokens/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", {}),
    ]

    for intent, name, url, headers in keyless:
        if url == "skip":
            continue
        if name == "eth-rpc-feehist":
            st, body = req(
                url,
                "POST",
                {"Content-Type": "application/json"},
                {"jsonrpc": "2.0", "id": 1, "method": "eth_feeHistory", "params": ["0x1", "latest", [50]]},
            )
            add(intent, name, st, body)
            continue
        if name == "eth-supply-rpc":
            # USDT totalSupply on eth
            st, body = req(
                url,
                "POST",
                {"Content-Type": "application/json"},
                {
                    "jsonrpc": "2.0",
                    "id": 1,
                    "method": "eth_call",
                    "params": [
                        {
                            "to": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
                            "data": "0x18160ddd",
                        },
                        "latest",
                    ],
                },
            )
            add(intent, name, st, body)
            continue
        if name == "valhalla-demo":
            st, body = req(
                url,
                "POST",
                {"Content-Type": "application/json"},
                {
                    "locations": [
                        {"lat": 52.5, "lon": 13.4},
                        {"lat": 52.52, "lon": 13.41},
                    ],
                    "costing": "auto",
                },
            )
            add(intent, name, st, body)
            continue
        if name == "languagetool-org":
            st, body = req(
                url,
                "POST",
                {"Content-Type": "application/x-www-form-urlencoded"},
                b"text=This%20are%20wrong.&language=en-US",
            )
            add(intent, name, st, body)
            continue
        if name == "urlhaus-host":
            st, body = req(url, "POST", {"Content-Type": "application/x-www-form-urlencoded"}, b"host=example.com")
            add(intent, name, st, body)
            continue
        st, body = req(url, headers=headers)
        add(intent, name, st, body)

    OUT.write_text("\n".join(json.dumps(r) for r in rows) + "\n")
    print(f"\nWROTE {OUT} lines={len(rows)}")

    # summary counts by HTTP class
    ok = [r for r in rows if isinstance(r["status"], int) and 200 <= r["status"] < 300]
    print(f"HTTP_2xx={len(ok)} / {len(rows)}")


if __name__ == "__main__":
    main()
