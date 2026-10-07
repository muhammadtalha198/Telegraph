#!/usr/bin/env python3
"""
Free / no-wallet miner smoke tests (Alexandria + upstream).

Docs used:
  alexandria/docs/payments.md          — anon free quota + admin/custodial x402
  alexandria/docs/api-reference.md     — POST /api/core/chat/paid, GET /api/anon/usage
  alexandria/docs/miners-and-yaml.md   — Direct Request body (subnetId + direct.*)
  Telegraph/docs/x402-payment.md       — engine /v1/ask/{id} is paid (402 without signature)

Modes:
  upstream  Hit each miner's public API directly. $0 everywhere. Best for testing ALL miners.
  anon      Alexandria Direct Request WITHOUT connecting a wallet.
            Uses free anon quota (~5 / 12h). Terminal Backend pays via Admin custodial wallet
            (matches Talha: test via Admin Wallet / not connecting your wallet).
  both      upstream first, then anon for a small sample (respects remaining quota).

Examples:
  python3 scripts/test-miners-free.py --mode upstream
  python3 scripts/test-miners-free.py --mode anon --limit 4
  python3 scripts/test-miners-free.py --mode both --intent CRYPTO_PRICE
"""

from __future__ import annotations

import argparse
import http.cookiejar
import json
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "out"
UA = "TeleGraphMinerFreeTest/1.0 (+docs:alexandria/payments.md)"
DEFAULT_ALEXANDRIA = "https://alexandria.telegraphprotocol.com"
DEFAULT_NODE = "https://devnode.telegraphprotocol.com"

# YAML id (Alexandria subnetId) — NOT the on-chain registration id.
# Defaults + example Direct Request payloads (same fields as Alexandria UI).
CATALOG: list[dict[str, Any]] = [
    # CRYPTO_PRICE
    {
        "intent": "CRYPTO_PRICE",
        "yaml_id": "32001",
        "slug": "crypto-coingecko",
        "question": "What is the current price of Bitcoin in USD?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"ids": "bitcoin", "vs_currencies": "usd"}},
        "upstream": "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd",
    },
    {
        "intent": "CRYPTO_PRICE",
        "yaml_id": "32002",
        "slug": "crypto-coinbase",
        "question": "What is the current price of Bitcoin in USD?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"pair": "BTC-USD"}},
        "upstream": "https://api.coinbase.com/v2/prices/BTC-USD/spot",
    },
    {
        "intent": "CRYPTO_PRICE",
        "yaml_id": "32003",
        "slug": "crypto-binance",
        "question": "What is BTCUSDT spot price?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"symbol": "BTCUSDT"}},
        "upstream": "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT",
    },
    {
        "intent": "CRYPTO_PRICE",
        "yaml_id": "32004",
        "slug": "crypto-kraken",
        "question": "What is XBTUSD on Kraken?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"pair": "XBTUSD"}},
        "upstream": "https://api.kraken.com/0/public/Ticker?pair=XBTUSD",
    },
    {
        "intent": "CRYPTO_PRICE",
        "yaml_id": "32005",
        "slug": "crypto-coinpaprika",
        "question": "What is the current price of Bitcoin?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"id": "btc-bitcoin"}},
        "upstream": "https://api.coinpaprika.com/v1/tickers/btc-bitcoin",
    },
    {
        "intent": "CRYPTO_PRICE",
        "yaml_id": "32006",
        "slug": "crypto-defillama",
        "question": "What is Bitcoin price via DefiLlama?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"coins": "coingecko:bitcoin"}},
        "upstream": "https://coins.llama.fi/prices/current/coingecko:bitcoin",
    },
    {
        "intent": "CRYPTO_PRICE",
        "yaml_id": "32007",
        "slug": "crypto-gemini",
        "question": "What is btcusd on Gemini?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"pair": "btcusd"}},
        "upstream": "https://api.gemini.com/v1/pubticker/btcusd",
    },
    {
        "intent": "CRYPTO_PRICE",
        "yaml_id": "32008",
        "slug": "crypto-bitstamp",
        "question": "What is btcusd on Bitstamp?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"pair": "btcusd"}},
        "upstream": "https://www.bitstamp.net/api/v2/ticker/btcusd/",
    },
    {
        "intent": "CRYPTO_PRICE",
        "yaml_id": "32009",
        "slug": "crypto-bybit",
        "question": "What is BTCUSDT on Bybit spot?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"category": "spot", "symbol": "BTCUSDT"}},
        "upstream": "https://api.bybit.com/v5/market/tickers?category=spot&symbol=BTCUSDT",
    },
    {
        "intent": "CRYPTO_PRICE",
        "yaml_id": "32010",
        "slug": "crypto-kucoin",
        "question": "What is BTC-USDT on KuCoin?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"symbol": "BTC-USDT"}},
        "upstream": "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT",
    },
    # FX_NOW
    {
        "intent": "FX_NOW",
        "yaml_id": "31001",
        "slug": "fx-frankfurter",
        "question": "What is the current EUR/USD mid-market rate?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"from": "USD", "to": "EUR"}},
        "upstream": "https://api.frankfurter.app/latest?from=USD&to=EUR",
    },
    {
        "intent": "FX_NOW",
        "yaml_id": "31002",
        "slug": "fx-er-api",
        "question": "What is the current USD FX table?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"base": "USD"}},
        "upstream": "https://open.er-api.com/v6/latest/USD",
    },
    {
        "intent": "FX_NOW",
        "yaml_id": "31003",
        "slug": "fx-fawaz",
        "question": "What is the current USD FX table?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"base": "usd"}},
        "upstream": "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json",
    },
    {
        "intent": "FX_NOW",
        "yaml_id": "31004",
        "slug": "fx-hnb",
        "question": "What is the HNB mid rate for USD?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"valuta": "USD"}},
        "upstream": "https://api.hnb.hr/tecajn-eur/v3?valuta=USD",
    },
    {
        "intent": "FX_NOW",
        "yaml_id": "31005",
        "slug": "fx-boc",
        "question": "What is FXCADUSD from Bank of Canada?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"series": "FXUSDCAD", "recent": "1"}},
        "upstream": "https://www.bankofcanada.ca/valet/observations/FXUSDCAD/json?recent=1",
    },
    {
        "intent": "FX_NOW",
        "yaml_id": "31006",
        "slug": "fx-riksbank",
        "question": "What is SEK/USD from Riksbank?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"series": "SEKUSDPMI", "date": "2026-09-11"}},
        "upstream": "https://api.riksbank.se/swea/v1/Observations/SEKUSDPMI/2026-09-11",
    },
    {
        "intent": "FX_NOW",
        "yaml_id": "31007",
        "slug": "fx-cbr",
        "question": "What are CBR daily FX rates?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {}},
        "upstream": "https://www.cbr-xml-daily.ru/daily_json.js",
    },
    {
        "intent": "FX_NOW",
        "yaml_id": "31008",
        "slug": "fx-vatcomply",
        "question": "What is the current USD FX table?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"base": "USD"}},
        "upstream": "https://api.vatcomply.com/rates?base=USD",
    },
    {
        "intent": "FX_NOW",
        "yaml_id": "31009",
        "slug": "fx-coinbase",
        "question": "What are Coinbase exchange rates for USD?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"currency": "USD"}},
        "upstream": "https://api.coinbase.com/v2/exchange-rates?currency=USD",
    },
    {
        "intent": "FX_NOW",
        "yaml_id": "31010",
        "slug": "fx-erapi-v4",
        "question": "What is the current USD FX table?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"base": "USD"}},
        "upstream": "https://api.exchangerate-api.com/v4/latest/USD",
    },
    # WEATHER_CHECK
    {
        "intent": "WEATHER_CHECK",
        "yaml_id": "33001",
        "slug": "wx-openmeteo",
        "question": "What is the current temperature in Miami, Florida right now?",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {"latitude": "25.7617", "longitude": "-80.1918", "current_weather": "true"},
        },
        "upstream": "https://api.open-meteo.com/v1/forecast?latitude=25.7617&longitude=-80.1918&current_weather=true",
    },
    {
        "intent": "WEATHER_CHECK",
        "yaml_id": "33002",
        "slug": "wx-openmeteo-flood",
        "question": "What is the current temperature in Miami, Florida right now?",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {"latitude": "25.7617", "longitude": "-80.1918", "daily": "river_discharge"},
        },
        "upstream": "https://flood-api.open-meteo.com/v1/flood?latitude=25.7617&longitude=-80.1918&daily=river_discharge",
    },
    {
        "intent": "WEATHER_CHECK",
        "yaml_id": "33003",
        "slug": "wx-wttr",
        "question": "What is the current temperature in Miami, Florida right now?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"location": "Miami", "format": "j1"}},
        "upstream": "https://wttr.in/Miami?format=j1",
    },
    {
        "intent": "WEATHER_CHECK",
        "yaml_id": "33004",
        "slug": "wx-7timer",
        "question": "What is the current temperature in Miami, Florida right now?",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {"lat": "25.7617", "lon": "-80.1918", "product": "civil", "output": "json"},
        },
        "upstream": "https://www.7timer.info/bin/api.pl?lat=25.7617&lon=-80.1918&product=civil&output=json",
    },
    {
        "intent": "WEATHER_CHECK",
        "yaml_id": "33005",
        "slug": "wx-brightsky",
        "question": "Current weather conditions in Berlin — temperature and wind?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"lat": "52.52", "lon": "13.40"}},
        "upstream": "https://api.brightsky.dev/current_weather?lat=52.52&lon=13.40",
    },
    {
        "intent": "WEATHER_CHECK",
        "yaml_id": "33006",
        "slug": "wx-sunrise",
        "question": "What is the current temperature in Miami, Florida right now?",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {"lat": "25.7617", "lng": "-80.1918", "formatted": "0"},
        },
        "upstream": "https://api.sunrise-sunset.org/json?lat=25.7617&lng=-80.1918&formatted=0",
    },
    {
        "intent": "WEATHER_CHECK",
        "yaml_id": "33007",
        "slug": "wx-openmeteo-aq",
        "question": "What is the humidity and temperature in Tokyo right now?",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {"latitude": "35.6762", "longitude": "139.6503", "current": "pm2_5,us_aqi"},
        },
        "upstream": "https://air-quality-api.open-meteo.com/v1/air-quality?latitude=35.6762&longitude=139.6503&current=pm2_5,us_aqi",
    },
    {
        "intent": "WEATHER_CHECK",
        "yaml_id": "33008",
        "slug": "wx-nws-alerts",
        "question": "What is the current temperature in Miami, Florida right now?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"point": "25.7617,-80.1918"}},
        "upstream": "https://api.weather.gov/alerts/active?point=25.7617,-80.1918",
    },
    {
        "intent": "WEATHER_CHECK",
        "yaml_id": "33009",
        "slug": "wx-openmeteo-marine",
        "question": "What is the current temperature in Miami, Florida right now?",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {"latitude": "25.7617", "longitude": "-80.1918", "current": "wave_height"},
        },
        "upstream": "https://marine-api.open-meteo.com/v1/marine?latitude=25.7617&longitude=-80.1918&current=wave_height",
    },
    {
        "intent": "WEATHER_CHECK",
        "yaml_id": "33010",
        "slug": "wx-canada",
        "question": "Current weather conditions in London — temperature and wind?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"q": "Toronto", "limit": "1"}},
        "upstream": "https://api.weather.gc.ca/collections/citypageweather-realtime/items?q=Toronto&limit=1",
    },
    # IP_GEOLOCATION
    {
        "intent": "IP_GEOLOCATION",
        "yaml_id": "34001",
        "slug": "ipgeo-ipapi",
        "question": "Where is the IP address 8.8.8.8 located?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"ip": "8.8.8.8"}},
        "upstream": "http://ip-api.com/json/8.8.8.8",
    },
    {
        "intent": "IP_GEOLOCATION",
        "yaml_id": "34002",
        "slug": "ipgeo-ipwho",
        "question": "Where is the IP address 8.8.8.8 located?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"ip": "8.8.8.8"}},
        "upstream": "https://ipwho.is/8.8.8.8",
    },
    {
        "intent": "IP_GEOLOCATION",
        "yaml_id": "34003",
        "slug": "ipgeo-seeip",
        "question": "What city and country is IP 1.1.1.1 in?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"ip": "1.1.1.1"}},
        "upstream": "https://api.seeip.org/geoip/1.1.1.1",
    },
    {
        "intent": "IP_GEOLOCATION",
        "yaml_id": "34004",
        "slug": "ipgeo-geojs",
        "question": "Where is the IP address 8.8.8.8 located?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"ip": "8.8.8.8"}},
        "upstream": "https://get.geojs.io/v1/ip/geo/8.8.8.8.json",
    },
    {
        "intent": "IP_GEOLOCATION",
        "yaml_id": "34005",
        "slug": "ipgeo-reallyfree",
        "question": "Geolocate 9.9.9.9 — country, region, and city?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"ip": "9.9.9.9"}},
        "upstream": "https://reallyfreegeoip.org/json/9.9.9.9",
    },
    {
        "intent": "IP_GEOLOCATION",
        "yaml_id": "34006",
        "slug": "ipgeo-ipinfo",
        "question": "Where is the IP address 8.8.8.8 located?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"ip": "8.8.8.8"}},
        "upstream": "https://ipinfo.io/8.8.8.8/json",
    },
    {
        "intent": "IP_GEOLOCATION",
        "yaml_id": "34007",
        "slug": "ipgeo-ipapiis",
        "question": "What city and country is IP 1.1.1.1 in?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"q": "1.1.1.1"}},
        "upstream": "https://api.ipapi.is?q=1.1.1.1",
    },
    {
        "intent": "IP_GEOLOCATION",
        "yaml_id": "34008",
        "slug": "ipgeo-dbip",
        "question": "Where is the IP address 8.8.8.8 located?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"ip": "8.8.8.8"}},
        "upstream": "https://api.db-ip.com/v2/free/8.8.8.8",
    },
    {
        "intent": "IP_GEOLOCATION",
        "yaml_id": "34009",
        "slug": "ipgeo-ifconfig",
        "question": "Geolocate 9.9.9.9 — country, region, and city?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"ip": "9.9.9.9"}},
        "upstream": "https://ifconfig.co/json?ip=9.9.9.9",
    },
    {
        "intent": "IP_GEOLOCATION",
        "yaml_id": "34010",
        "slug": "ipgeo-countryis",
        "question": "Where is the IP address 8.8.8.8 located?",
        "direct": {"method": "GET", "endpoint": "/query", "payload": {"ip": "8.8.8.8"}},
        "upstream": "https://api.country.is/8.8.8.8",
    },

    # BATCH5: WEATHER_FORECAST / CVE_LOOKUP / STORM_ALERT / TVL_LOOKUP / MACRO_ECONOMIC_INDICATOR
    {
        "intent": "WEATHER_FORECAST",
        "yaml_id": "35001",
        "slug": "wxf-openmeteo",
        "question": "Hourly forecast Miami?",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "latitude": "25.7617",
                "longitude": "-80.1918",
                "hourly": "temperature_2m,precipitation_probability,wind_speed_10m",
                "forecast_days": "1"
            }
        },
        "upstream": "https://api.open-meteo.com/v1/forecast?latitude=25.7617&longitude=-80.1918&hourly=temperature_2m,precipitation_probability,wind_speed_10m&forecast_days=1"
    },
    {
        "intent": "WEATHER_FORECAST",
        "yaml_id": "35002",
        "slug": "wxf-openmeteo-daily",
        "question": "3-day daily forecast London?",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "latitude": "51.5074",
                "longitude": "-0.1278",
                "daily": "temperature_2m_max,precipitation_sum",
                "forecast_days": "3"
            }
        },
        "upstream": "https://api.open-meteo.com/v1/forecast?latitude=51.5074&longitude=-0.1278&daily=temperature_2m_max,precipitation_sum&forecast_days=3"
    },
    {
        "intent": "WEATHER_FORECAST",
        "yaml_id": "35003",
        "slug": "wxf-openmeteo-ens",
        "question": "Ensemble temp forecast Miami?",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "latitude": "25.7617",
                "longitude": "-80.1918",
                "hourly": "temperature_2m",
                "models": "icon_seamless"
            }
        },
        "upstream": "https://ensemble-api.open-meteo.com/v1/ensemble?latitude=25.7617&longitude=-80.1918&hourly=temperature_2m&models=icon_seamless"
    },
    {
        "intent": "WEATHER_FORECAST",
        "yaml_id": "35004",
        "slug": "wxf-openmeteo-aq",
        "question": "Tokyo air quality forecast?",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "latitude": "35.6762",
                "longitude": "139.6503",
                "hourly": "pm2_5",
                "forecast_days": "1"
            }
        },
        "upstream": "https://air-quality-api.open-meteo.com/v1/air-quality?latitude=35.6762&longitude=139.6503&hourly=pm2_5&forecast_days=1"
    },
    {
        "intent": "WEATHER_FORECAST",
        "yaml_id": "35005",
        "slug": "wxf-openmeteo-marine",
        "question": "Miami wave height forecast?",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "latitude": "25.7617",
                "longitude": "-80.1918",
                "hourly": "wave_height",
                "forecast_days": "1"
            }
        },
        "upstream": "https://marine-api.open-meteo.com/v1/marine?latitude=25.7617&longitude=-80.1918&hourly=wave_height&forecast_days=1"
    },
    {
        "intent": "WEATHER_FORECAST",
        "yaml_id": "35006",
        "slug": "wxf-7timer",
        "question": "7Timer civil light forecast Miami?",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "lat": "25.7617",
                "lon": "-80.1918",
                "product": "civillight",
                "output": "json"
            }
        },
        "upstream": "https://www.7timer.info/bin/api.pl?lat=25.7617&lon=-80.1918&product=civillight&output=json"
    },
    {
        "intent": "WEATHER_FORECAST",
        "yaml_id": "35007",
        "slug": "wxf-wttr",
        "question": "wttr.in Miami forecast JSON?",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "location": "Miami",
                "format": "j1"
            }
        },
        "upstream": "https://wttr.in/Miami?format=j1"
    },
    {
        "intent": "WEATHER_FORECAST",
        "yaml_id": "35008",
        "slug": "wxf-openmeteo-hist",
        "question": "Archive daily max temp Miami Jan 2024?",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "latitude": "25.7617",
                "longitude": "-80.1918",
                "start_date": "2024-01-01",
                "end_date": "2024-01-02",
                "daily": "temperature_2m_max"
            }
        },
        "upstream": "https://archive-api.open-meteo.com/v1/archive?latitude=25.7617&longitude=-80.1918&start_date=2024-01-01&end_date=2024-01-02&daily=temperature_2m_max"
    },
    {
        "intent": "WEATHER_FORECAST",
        "yaml_id": "35009",
        "slug": "wxf-brightsky",
        "question": "Bright Sky current Berlin?",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "lat": "52.52",
                "lon": "13.40"
            }
        },
        "upstream": "https://api.brightsky.dev/current_weather?lat=52.52&lon=13.40"
    },
    {
        "intent": "WEATHER_FORECAST",
        "yaml_id": "35010",
        "slug": "wxf-canada",
        "question": "Environment Canada Toronto forecast?",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "q": "Toronto",
                "limit": "1"
            }
        },
        "upstream": "https://api.weather.gc.ca/collections/citypageweather-realtime/items?q=Toronto&limit=1"
    },
    {
        "intent": "CVE_LOOKUP",
        "yaml_id": "36001",
        "slug": "cve-nvd",
        "question": "Look up CVE-2021-44228",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "cveId": "CVE-2021-44228"
            }
        },
        "upstream": "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2021-44228"
    },
    {
        "intent": "CVE_LOOKUP",
        "yaml_id": "36002",
        "slug": "cve-nvd-keyword",
        "question": "NVD keyword openssl",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "keywordSearch": "openssl",
                "resultsPerPage": "1"
            }
        },
        "upstream": "https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=openssl&resultsPerPage=1"
    },
    {
        "intent": "CVE_LOOKUP",
        "yaml_id": "36003",
        "slug": "cve-osv",
        "question": "OSV CVE-2021-44228",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "id": "CVE-2021-44228"
            }
        },
        "upstream": "https://api.osv.dev/v1/vulns/CVE-2021-44228"
    },
    {
        "intent": "CVE_LOOKUP",
        "yaml_id": "36004",
        "slug": "cve-circl",
        "question": "CIRCL CVE-2021-44228",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "id": "CVE-2021-44228"
            }
        },
        "upstream": "https://cve.circl.lu/api/cve/CVE-2021-44228"
    },
    {
        "intent": "CVE_LOOKUP",
        "yaml_id": "36005",
        "slug": "cve-mitre",
        "question": "MITRE CVE-2021-44228",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "id": "CVE-2021-44228"
            }
        },
        "upstream": "https://cveawg.mitre.org/api/cve/CVE-2021-44228"
    },
    {
        "intent": "CVE_LOOKUP",
        "yaml_id": "36006",
        "slug": "cve-depsdev",
        "question": "deps.dev GHSA-jfh8-c2jp-5v3q",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "id": "GHSA-jfh8-c2jp-5v3q"
            }
        },
        "upstream": "https://api.deps.dev/v3alpha/advisories/GHSA-jfh8-c2jp-5v3q"
    },
    {
        "intent": "CVE_LOOKUP",
        "yaml_id": "36007",
        "slug": "cve-epss",
        "question": "EPSS CVE-2021-44228",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "cve": "CVE-2021-44228"
            }
        },
        "upstream": "https://api.first.org/data/v1/epss?cve=CVE-2021-44228"
    },
    {
        "intent": "CVE_LOOKUP",
        "yaml_id": "36008",
        "slug": "cve-nvd-cvss",
        "question": "NVD CRITICAL CVEs",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "cvssV3Severity": "CRITICAL",
                "resultsPerPage": "1"
            }
        },
        "upstream": "https://services.nvd.nist.gov/rest/json/cves/2.0?cvssV3Severity=CRITICAL&resultsPerPage=1"
    },
    {
        "intent": "CVE_LOOKUP",
        "yaml_id": "36009",
        "slug": "cve-osv-ghsa",
        "question": "OSV GHSA-jfh8-c2jp-5v3q",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "id": "GHSA-jfh8-c2jp-5v3q"
            }
        },
        "upstream": "https://api.osv.dev/v1/vulns/GHSA-jfh8-c2jp-5v3q"
    },
    {
        "intent": "CVE_LOOKUP",
        "yaml_id": "36010",
        "slug": "cve-nvd-cpe",
        "question": "NVD log4j CPE match",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "virtualMatchString": "cpe:2.3:a:apache:log4j:*",
                "resultsPerPage": "1"
            }
        },
        "upstream": "https://services.nvd.nist.gov/rest/json/cves/2.0?virtualMatchString=cpe:2.3:a:apache:log4j:*&resultsPerPage=1"
    },
    {
        "intent": "STORM_ALERT",
        "yaml_id": "37001",
        "slug": "storm-nws-point",
        "question": "NWS alerts Miami",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "point": "25.7617,-80.1918"
            }
        },
        "upstream": "https://api.weather.gov/alerts/active?point=25.7617,-80.1918"
    },
    {
        "intent": "STORM_ALERT",
        "yaml_id": "37002",
        "slug": "storm-nws-area",
        "question": "NWS alerts Florida",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "area": "FL"
            }
        },
        "upstream": "https://api.weather.gov/alerts/active?area=FL"
    },
    {
        "intent": "STORM_ALERT",
        "yaml_id": "37003",
        "slug": "storm-nws-types",
        "question": "NWS alert event types",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {}
        },
        "upstream": "https://api.weather.gov/alerts/types"
    },
    {
        "intent": "STORM_ALERT",
        "yaml_id": "37004",
        "slug": "storm-noaa-scales",
        "question": "NOAA space weather scales",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {}
        },
        "upstream": "https://services.swpc.noaa.gov/products/noaa-scales.json"
    },
    {
        "intent": "STORM_ALERT",
        "yaml_id": "37005",
        "slug": "storm-noaa-kp",
        "question": "NOAA planetary K-index",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {}
        },
        "upstream": "https://services.swpc.noaa.gov/json/planetary_k_index_1m.json"
    },
    {
        "intent": "STORM_ALERT",
        "yaml_id": "37006",
        "slug": "storm-noaa-rtsw",
        "question": "NOAA RTSW magnetometer",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {}
        },
        "upstream": "https://services.swpc.noaa.gov/json/rtsw/rtsw_mag_1m.json"
    },
    {
        "intent": "STORM_ALERT",
        "yaml_id": "37007",
        "slug": "storm-gdacs-tc",
        "question": "GDACS tropical cyclones",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "eventlist": "TC"
            }
        },
        "upstream": "https://www.gdacs.org/gdacsapi/api/events/geteventlist/SEARCH?eventlist=TC"
    },
    {
        "intent": "STORM_ALERT",
        "yaml_id": "37008",
        "slug": "storm-gdacs-eq",
        "question": "GDACS earthquakes",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "eventlist": "EQ"
            }
        },
        "upstream": "https://www.gdacs.org/gdacsapi/api/events/geteventlist/SEARCH?eventlist=EQ"
    },
    {
        "intent": "STORM_ALERT",
        "yaml_id": "37009",
        "slug": "storm-usgs-sig",
        "question": "USGS significant quakes week",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {}
        },
        "upstream": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_week.geojson"
    },
    {
        "intent": "STORM_ALERT",
        "yaml_id": "37010",
        "slug": "storm-usgs-m25",
        "question": "USGS M2.5+ day",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {}
        },
        "upstream": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    },
    {
        "intent": "TVL_LOOKUP",
        "yaml_id": "38001",
        "slug": "tvl-llama-protocols",
        "question": "DefiLlama protocols TVL",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {}
        },
        "upstream": "https://api.llama.fi/protocols"
    },
    {
        "intent": "TVL_LOOKUP",
        "yaml_id": "38002",
        "slug": "tvl-llama-chains",
        "question": "DefiLlama chains TVL",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {}
        },
        "upstream": "https://api.llama.fi/v2/chains"
    },
    {
        "intent": "TVL_LOOKUP",
        "yaml_id": "38003",
        "slug": "tvl-llama-protocol",
        "question": "Aave protocol detail",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "name": "aave"
            }
        },
        "upstream": "https://api.llama.fi/protocol/aave"
    },
    {
        "intent": "TVL_LOOKUP",
        "yaml_id": "38004",
        "slug": "tvl-llama-tvl",
        "question": "Aave TVL number",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "name": "aave"
            }
        },
        "upstream": "https://api.llama.fi/tvl/aave"
    },
    {
        "intent": "TVL_LOOKUP",
        "yaml_id": "38005",
        "slug": "tvl-llama-hist-chain",
        "question": "Ethereum historical TVL",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "chain": "Ethereum"
            }
        },
        "upstream": "https://api.llama.fi/v2/historicalChainTvl/Ethereum"
    },
    {
        "intent": "TVL_LOOKUP",
        "yaml_id": "38006",
        "slug": "tvl-llama-charts",
        "question": "Ethereum chain charts",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "chain": "Ethereum"
            }
        },
        "upstream": "https://api.llama.fi/charts/Ethereum"
    },
    {
        "intent": "TVL_LOOKUP",
        "yaml_id": "38007",
        "slug": "tvl-llama-yields",
        "question": "DefiLlama yield pools",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {}
        },
        "upstream": "https://yields.llama.fi/pools"
    },
    {
        "intent": "TVL_LOOKUP",
        "yaml_id": "38008",
        "slug": "tvl-llama-stables",
        "question": "DefiLlama stablecoins",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "includePrices": "true"
            }
        },
        "upstream": "https://stablecoins.llama.fi/stablecoins?includePrices=true"
    },
    {
        "intent": "TVL_LOOKUP",
        "yaml_id": "38009",
        "slug": "tvl-llama-volumes",
        "question": "DefiLlama DEX volumes",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {}
        },
        "upstream": "https://api.llama.fi/overview/dexs"
    },
    {
        "intent": "TVL_LOOKUP",
        "yaml_id": "38010",
        "slug": "tvl-llama-fees",
        "question": "DefiLlama fees overview",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {}
        },
        "upstream": "https://api.llama.fi/overview/fees"
    },
    {
        "intent": "MACRO_ECONOMIC_INDICATOR",
        "yaml_id": "39001",
        "slug": "macro-wb-gdp-us",
        "question": "US GDP World Bank",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "country": "US",
                "format": "json",
                "per_page": "1",
                "MRV": "1"
            }
        },
        "upstream": "https://api.worldbank.org/v2/country/US/indicator/NY.GDP.MKTP.CD?format=json&per_page=1&MRV=1"
    },
    {
        "intent": "MACRO_ECONOMIC_INDICATOR",
        "yaml_id": "39002",
        "slug": "macro-wb-infl-us",
        "question": "US inflation World Bank",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "country": "US",
                "format": "json",
                "per_page": "1",
                "MRV": "1"
            }
        },
        "upstream": "https://api.worldbank.org/v2/country/US/indicator/FP.CPI.TOTL.ZG?format=json&per_page=1&MRV=1"
    },
    {
        "intent": "MACRO_ECONOMIC_INDICATOR",
        "yaml_id": "39003",
        "slug": "macro-wb-unemp-us",
        "question": "US unemployment World Bank",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "country": "US",
                "format": "json",
                "per_page": "1",
                "MRV": "1"
            }
        },
        "upstream": "https://api.worldbank.org/v2/country/US/indicator/SL.UEM.TOTL.ZS?format=json&per_page=1&MRV=1"
    },
    {
        "intent": "MACRO_ECONOMIC_INDICATOR",
        "yaml_id": "39004",
        "slug": "macro-wb-pop-us",
        "question": "US population World Bank",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "country": "US",
                "format": "json",
                "per_page": "1",
                "MRV": "1"
            }
        },
        "upstream": "https://api.worldbank.org/v2/country/US/indicator/SP.POP.TOTL?format=json&per_page=1&MRV=1"
    },
    {
        "intent": "MACRO_ECONOMIC_INDICATOR",
        "yaml_id": "39005",
        "slug": "macro-wb-gdp-de",
        "question": "Germany GDP World Bank",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "country": "DE",
                "format": "json",
                "per_page": "1",
                "MRV": "1"
            }
        },
        "upstream": "https://api.worldbank.org/v2/country/DE/indicator/NY.GDP.MKTP.CD?format=json&per_page=1&MRV=1"
    },
    {
        "intent": "MACRO_ECONOMIC_INDICATOR",
        "yaml_id": "39006",
        "slug": "macro-wb-infl-gb",
        "question": "UK inflation World Bank",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "country": "GB",
                "format": "json",
                "per_page": "1",
                "MRV": "1"
            }
        },
        "upstream": "https://api.worldbank.org/v2/country/GB/indicator/FP.CPI.TOTL.ZG?format=json&per_page=1&MRV=1"
    },
    {
        "intent": "MACRO_ECONOMIC_INDICATOR",
        "yaml_id": "39007",
        "slug": "macro-wb-gdp-jp",
        "question": "Japan GDP World Bank",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "country": "JP",
                "format": "json",
                "per_page": "1",
                "MRV": "1"
            }
        },
        "upstream": "https://api.worldbank.org/v2/country/JP/indicator/NY.GDP.MKTP.CD?format=json&per_page=1&MRV=1"
    },
    {
        "intent": "MACRO_ECONOMIC_INDICATOR",
        "yaml_id": "39008",
        "slug": "macro-wb-gdp-growth",
        "question": "US GDP growth World Bank",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "country": "US",
                "format": "json",
                "per_page": "1",
                "MRV": "1"
            }
        },
        "upstream": "https://api.worldbank.org/v2/country/US/indicator/NY.GDP.MKTP.KD.ZG?format=json&per_page=1&MRV=1"
    },
    {
        "intent": "MACRO_ECONOMIC_INDICATOR",
        "yaml_id": "39009",
        "slug": "macro-ecb-exr",
        "question": "ECB USD/EUR",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "lastNObservations": "1",
                "format": "jsondata"
            }
        },
        "upstream": "https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?lastNObservations=1&format=jsondata"
    },
    {
        "intent": "MACRO_ECONOMIC_INDICATOR",
        "yaml_id": "39010",
        "slug": "macro-bis-eer",
        "question": "BIS US effective exchange rate",
        "direct": {
            "method": "GET",
            "endpoint": "/query",
            "payload": {
                "format": "sdmx-json",
                "detail": "dataonly",
                "lastNObservations": "1"
            }
        },
        "upstream": "https://stats.bis.org/api/v2/data/dataflow/BIS/WS_EER/1.0/D.N.B.US?format=sdmx-json&detail=dataonly&lastNObservations=1"
    },
]


def http_json(
    url: str,
    *,
    method: str = "GET",
    body: dict | None = None,
    headers: dict | None = None,
    cookie_jar: http.cookiejar.CookieJar | None = None,
    timeout: int = 60,
) -> tuple[int, Any, str]:
    data = None if body is None else json.dumps(body).encode()
    hdrs = {"User-Agent": UA, "Accept": "application/json"}
    if body is not None:
        hdrs["Content-Type"] = "application/json"
    if headers:
        hdrs.update(headers)
    req = urllib.request.Request(url, data=data, headers=hdrs, method=method)
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar or http.cookiejar.CookieJar()))
    # Some corporate/dev boxes need default context
    ctx = ssl.create_default_context()
    try:
        with opener.open(req, timeout=timeout, context=ctx) as resp:  # type: ignore[call-arg]
            raw = resp.read().decode("utf-8", errors="replace")
            code = resp.getcode()
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", errors="replace")
        code = e.code
    except TypeError:
        # Older Python: opener.open has no context kw
        try:
            with opener.open(req, timeout=timeout) as resp:
                raw = resp.read().decode("utf-8", errors="replace")
                code = resp.getcode()
        except urllib.error.HTTPError as e:
            raw = e.read().decode("utf-8", errors="replace")
            code = e.code
    try:
        parsed: Any = json.loads(raw) if raw.strip() else None
    except json.JSONDecodeError:
        parsed = raw
    return code, parsed, raw


def probe_upstream(item: dict[str, Any]) -> dict[str, Any]:
    url = item.get("upstream")
    if not url:
        return {"slug": item["slug"], "ok": None, "skipped": True, "reason": "no upstream URL"}
    code, parsed, raw = http_json(url, timeout=20)
    ok = 200 <= code < 300
    snippet = raw[:180].replace("\n", " ")
    return {
        "slug": item["slug"],
        "intent": item["intent"],
        "ok": ok,
        "http": code,
        "snippet": snippet,
        "mode": "upstream",
    }


def anon_usage(alexandria: str, jar: http.cookiejar.CookieJar) -> dict[str, Any]:
    code, parsed, _ = http_json(f"{alexandria.rstrip('/')}/api/anon/usage", cookie_jar=jar, timeout=20)
    if not isinstance(parsed, dict):
        return {"http": code, "remaining": None, "limit": None}
    return {
        "http": code,
        "remaining": parsed.get("remaining"),
        "limit": parsed.get("limit"),
        "exhausted": parsed.get("exhausted"),
    }


def probe_anon(alexandria: str, item: dict[str, Any], jar: http.cookiejar.CookieJar, network: str) -> dict[str, Any]:
    body = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": item["question"]}],
        "network": network,
        # IMPORTANT: Alexandria / Engine expect YAML `id`, not on-chain reg id
        "subnetId": str(item["yaml_id"]),
        "direct": item["direct"],
    }
    code, parsed, raw = 0, None, ""
    for attempt in range(4):
        code, parsed, raw = http_json(
            f"{alexandria.rstrip('/')}/api/core/chat/paid",
            method="POST",
            body=body,
            cookie_jar=jar,
            timeout=90,
        )
        err_txt = ""
        if isinstance(parsed, dict):
            err_txt = str(parsed.get("error") or parsed.get("message") or "")
        if code == 429 or "rate_limited" in err_txt.lower():
            time.sleep(8 * (attempt + 1))
            continue
        break
    ok = False
    err = None
    text = None
    receipt = None
    logs = []
    if isinstance(parsed, dict):
        err = parsed.get("error") or parsed.get("message")
        text = parsed.get("assistantText")
        receipt = parsed.get("terminalReceipt")
        logs = parsed.get("terminalLogs") or []
        # Success shapes: assistantText present, or ok true, or upstreamStatus 200
        ok = bool(text) or parsed.get("ok") is True or parsed.get("upstreamStatus") == 200
        if parsed.get("error") == "free_quota_exhausted":
            ok = False
            err = "free_quota_exhausted"
    else:
        err = raw[:300]
    admin = any(
        isinstance(L, dict) and "admin" in str(L.get("detail", "")).lower()
        for L in logs
    )
    return {
        "slug": item["slug"],
        "intent": item["intent"],
        "yaml_id": item["yaml_id"],
        "ok": ok,
        "http": code,
        "error": err,
        "assistant_snippet": (str(text)[:220] if text else None),
        "admin_wallet_used": admin,
        "receipt_subnet": (receipt or {}).get("subnet") if isinstance(receipt, dict) else None,
        "mode": "anon",
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Free miner smoke tests (no user wallet / no user payment)")
    ap.add_argument("--mode", choices=("upstream", "anon", "both"), default="upstream")
    ap.add_argument("--intent", choices=("CRYPTO_PRICE", "FX_NOW", "WEATHER_CHECK", "IP_GEOLOCATION", "WEATHER_FORECAST", "CVE_LOOKUP", "STORM_ALERT", "TVL_LOOKUP", "MACRO_ECONOMIC_INDICATOR", "ALL"), default="ALL")
    ap.add_argument("--limit", type=int, default=0, help="Max miners to test (0 = all / remaining quota)")
    ap.add_argument("--alexandria", default=DEFAULT_ALEXANDRIA)
    ap.add_argument("--network", default="base-sepolia", help="Alexandria payment network label")
    ap.add_argument("--sleep", type=float, default=0.4)
    args = ap.parse_args()

    items = [x for x in CATALOG if args.intent == "ALL" or x["intent"] == args.intent]
    if args.limit and args.limit > 0:
        items = items[: args.limit]

    OUT.mkdir(exist_ok=True)
    report: dict[str, Any] = {
        "mode": args.mode,
        "intent_filter": args.intent,
        "note": (
            "upstream = $0 direct API probes. "
            "anon = Alexandria Direct Request without connecting a wallet; "
            "Admin custodial wallet pays x402 (free to you, limited by anon quota ~5/12h)."
        ),
        "results": [],
    }

    print(f"mode={args.mode} miners={len(items)} intent={args.intent}")
    print("NOTE: Engine /v1/ask/{id} always requires x402; free user path is Alexandria anon + Admin wallet.")
    print()

    if args.mode in ("upstream", "both"):
        print("=== UPSTREAM (no payment) ===")
        for item in items:
            row = probe_upstream(item)
            report["results"].append(row)
            status = "SKIP" if row.get("skipped") else ("PASS" if row["ok"] else "FAIL")
            print(f"  {status:4} {item['slug']:22} http={row.get('http')} {row.get('snippet','')[:80]}")
            time.sleep(args.sleep)

    if args.mode in ("anon", "both"):
        print("=== ALEXANDRIA ANON DIRECT (Admin wallet pays; you do not) ===")
        jar = http.cookiejar.CookieJar()
        usage = anon_usage(args.alexandria, jar)
        report["anon_usage_before"] = usage
        print(f"  quota remaining={usage.get('remaining')}/{usage.get('limit')}")
        remaining = usage.get("remaining")
        if remaining is None:
            print("  WARN: could not read anon usage; continuing anyway")
            remaining = args.limit or 5
        if int(remaining) <= 0:
            print("  STOP: free_quota_exhausted — wait for reset or use --mode upstream")
        else:
            # Don't burn more than remaining quota
            anon_items = items[: int(remaining)]
            if args.mode == "both":
                # Prefer a small representative sample when both modes run
                prefer = ["crypto-coingecko", "crypto-binance", "fx-frankfurter", "fx-er-api"]
                ranked = [x for x in items if x["slug"] in prefer] + [x for x in items if x["slug"] not in prefer]
                anon_items = ranked[: min(len(ranked), int(remaining), args.limit or 4)]
            for item in anon_items:
                row = probe_anon(args.alexandria, item, jar, args.network)
                report["results"].append(row)
                status = "PASS" if row["ok"] else "FAIL"
                extra = row.get("assistant_snippet") or row.get("error") or ""
                admin = " admin-wallet" if row.get("admin_wallet_used") else ""
                print(f"  {status:4} {item['slug']:22} yaml_id={item['yaml_id']}{admin} {str(extra)[:100]}")
                time.sleep(max(args.sleep, 1.0))
            report["anon_usage_after"] = anon_usage(args.alexandria, jar)
            print(f"  quota after={report['anon_usage_after'].get('remaining')}/{report['anon_usage_after'].get('limit')}")

    out_path = OUT / "miner-free-test.json"
    out_path.write_text(json.dumps(report, indent=2) + "\n")
    ups = [r for r in report["results"] if r.get("mode") == "upstream" and not r.get("skipped")]
    ans = [r for r in report["results"] if r.get("mode") == "anon"]
    print()
    if ups:
        print(f"upstream: {sum(1 for r in ups if r.get('ok'))}/{len(ups)} PASS")
    if ans:
        print(f"anon:     {sum(1 for r in ans if r.get('ok'))}/{len(ans)} PASS")
    print(f"wrote {out_path}")
    fails = [r for r in report["results"] if r.get("ok") is False]
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
