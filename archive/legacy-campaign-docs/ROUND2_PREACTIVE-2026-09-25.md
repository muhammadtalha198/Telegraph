# Round Two — Pre-active candidates

**Date:** 2026-09-25  
**Goal:** Find new distinct publishers for every intent still under **10 miners** (Active + Pre-active count together). Dead intents included in the hunt; most stay Dead after re-probe.  
**Keys used (names only):** `HF_TOKEN`, `HUGGINGFACE_HUB_TOKEN`, `JINA_API_KEY`, `VOYAGE_API_KEY`, `UCLASSIFY_READ_KEY`, `ABUSEIPDB_API_KEY`, `OPENAI_API_KEY` (not needed for probes below).  
**Probe log:** `/tmp/round2-probe.jsonl` (92 unique candidates, **57** HTTP 2xx). Script: `scripts/round2_probe.py`.  
**Doctrine:** Gates 0–8. One miner = one publisher. Same quantity + units. No RapidAPI wrappers. No re-register of WRONG_QUANTITY / duplicates.

**Status of this file:** research + probe table. **Batch 7 registered 18 ACCEPT miners** (ids 2953–2970) on 2026-09-25. Dropped Yahoo. See `newlyRegisteredMiners.md` Batch 7 section.

---

## Gap snapshot (have / need to reach 10)

| Bucket | Intent | Have | Need | Round-2 ACCEPT (new) | Notes |
|--------|--------|-----:|-----:|---------------------:|-------|
| Active | `FX_NOW` | 11 | 0 | 0 | Already ≥10; open-er-api likely DUPLICATE of `fx-er-api` |
| Active | `VULNERABILITY_TRIAGE` | 4 | 6 | 2 | GHSA + Red Hat CVSS; Debian HTML = reject |
| Active | `EMAIL_SECURITY` | 2 | 8 | 0 | Extra DoH timed out this run; retry Quad9/Mullvad |
| Active | `ROUTE_ETA` | 2 | 8 | 1 | Valhalla OSM demo OK; GraphHopper needs key |
| Active | `MACRO_ECONOMIC_INDICATOR` | 2 | 8 | 0 | FRED/OECD need key or better series URL |
| Active | `LIQUIDITY_DEPTH_VERIFY` | 2 | 8 | 0 | GeckoTerminal token call is liquidity-adjacent — **confirm field** vs pool depth |
| Active | `ASSET_RESERVE_ATTESTATION` | 1 | 9 | 2 | Tether transparency + Circle stablecoin totals |
| Active | `GRID_POWER_PRICE` | 1 | 9 | 0 | ENTSO-E keyed |
| Active | `LIVE_SHELF_PRICE` | 1 | 9 | 0 | Open Food Facts = product, **WRONG_QUANTITY** for shelf price |
| Active | `MINING_HASHPRICE_VERIFY` | 1 | 9 | 0 | HashrateIndex needs correct keyed path |
| Active | `ONCHAIN_METRIC_VERIFY` | 1 | 9 | 0 | DefiLlama TVL may be wrong quantity vs catalog metric — **confirm** |
| Pre | `CODE_PATCH_VERIFY` | 3 | 7 | 0 | glot timeout; OneCompiler keyed |
| Pre | `CROSS_CHAIN_STATE_VERIFY` | 3 | 7 | 0 | LayerZero host NXDOMAIN this run |
| Pre | `EVENT_OUTCOME_RESOLUTION` | 3 | 7 | 1 | Polymarket gamma OK (closed markets); Metaculus 403 |
| Pre | `OPTIMAL_EXECUTION_ROUTE` | 4 | 6 | 0 | 1inch/0x need keys or new URL |
| Pre | `SKU_IN_STOCK` | 1 | 9 | 0 | FakeStore/DummyJSON = demo stock, **WRONG_QUANTITY** for real SKU |
| Pre | `PAYMENT_METHOD_VERIFY` | 2 | 8 | 0 | binlist + handyapi **already registered** |
| Pre | `SANCTIONS_SCREENING_MATCH` | 2 | 8 | 0 | OpenSanctions needs key |
| Pre | `CORPORATE_REGISTRY_LOOKUP` | 2 | 8 | 1 | Brreg enhet OK; GLEIF **already** `corp-gleif-status` |
| Pre | `REGULATORY_FILING_MONITOR` | 1 | 9 | 1 | SEC submissions Apple CIK OK |
| Pre | `CRYPTO_PRICE` | 5 | 5 | 5 | HTX, MEXC, Gate, Bitfinex, Bybit (KuCoin may already exist in old yamls — use Bybit/Gate/HTX/MEXC/Bitfinex) |
| Pre | `CRYPTO_TRANSFER_VERIFY` | 1 | 9 | 0 | not re-probed this round |
| Pre | `CRYPTO_YIELD_RATE` | 7 | 3 | 0 | DefiLlama already used; Aave URL returned sandbox HTML |
| Pre | `THREAT_IP_REPUTATION` | 5 | 5 | 1 | **AbuseIPDB** with key — both 0 and 100 confidence pins |
| Pre | `WEATHER_CHECK` | 4 | 6 | 2 | MET Norway + 7Timer; Open-Meteo **already**; wttr = DUPLICATE reseller |
| Pre | `STOCK_PRICE` | 3 | 7 | 1 | Yahoo chart OK; Stooq 404; Finnhub keyed |
| Pre | `TRAVEL_DISRUPTION` | 1 | 9 | 0 | FAA already registered; Aviationstack keyed |
| Pre | `DNS_RECORD_LOOKUP` | 6 | 4 | 1 | AliDNS JSON OK; DNS.SB **already**; Control D wire-format only |
| Pre | `SSL_VERIFICATION` | 2 | 8 | 0 | Cert Spotter already; crt.sh 502 |
| Pre | `PORT_SCAN_AUDIT` | 2 | 8 | 0 | HackerTarget now requires key |
| Pre | `THREAT_INTELLIGENCE` | 3 | 7 | 0 | URLhaus/MalwareBazaar unauthorized without auth header |
| Pre | `AIR_QUALITY_INDEX` | 5 | 5 | 2 | CERNS + InfraNode UBA proxy (distinct HTTP publishers; pin Berlin) |
| Pre | `WEATHER_FORECAST_VERIFY` | 5 | 5 | 0 | not expanded this round |
| Pre | `GAS_PRICE` | 2 | 8 | 0 | Blocknative TLS fail; polygon-rpc tenant disabled |
| Pre | `TOKEN_TOTAL_SUPPLY_VERIFY` | 2 | 8 | 0 | eth call 525 |
| Pre | `VALIDATOR_PERFORMANCE_VERIFY` | 2 | 8 | 0 | beaconcha.in now keyed |
| Pre | `LOAN_INTEREST_RATE_QUOTE` | 6 | 4 | 0 | BoE CSV OK but may duplicate `lnr-boe`; RBA 403 |
| Pre | `API_HEALTH_CHECK` / `SERVER_UPTIME` | 2/2 | 8 | 0 | HTML only |
| Pre | `VENDOR_VERIFY` | 3 | 7 | 1 | VATComply VAT; OpenIBAN already registered |
| Pre | `GRAMMAR_SPELL_CHECK` | 2 | 8 | 0 | LanguageTool already registered |
| Pre | `CONTENT_EXTRACTION` | 2 | 8 | 0 | r.jina.ai = same Jina as `cex-jina` |
| Pre | `SENTIMENT_ANALYSIS` | 2 | 8 | 0 | see TEXT_CLASS / HF models below if intent allows |
| Pre | `WEB_SEARCH` | 1 | 9 | 0 | SearX instances 429 / dead |
| Open | `SEMANTIC_SIMILARITY` | 0 | 10 | 1+ | **HF MiniLM similarity 200** with key; Jina key invalid; Voyage timeout |
| Open | `TEXT_CLASSIFICATION` | 0 | 10 | 2 | **HF BART-MNLI** + **Twitter-RoBERTa**; uClassify needs POST (405 on GET) |
| Dead ×46 | (all) | 0 | — | 0 | Re-confirmed: no new honest keyless scalar for judgment / keyed / not-on-chain intents |

**Round-2 ACCEPT count (honest new publishers to build next):** **~23**  
**Still short of “10 per intent” and far from 1400** — filling Dead to 10 is not possible under Gates.

---

## Round Two Pre-active table (ACCEPT — build these)

These passed live probe and are **not** already on-chain under the same publisher for that intent.

| # | Intent | Proposed slug | Publisher | Auth | Field / quantity | Pin | Probe | Gap after |
|--:|--------|---------------|-----------|------|------------------|-----|-------|----------:|
| 1 | `SEMANTIC_SIMILARITY` | `sem-hf-minilm` | Hugging Face Inference (all-MiniLM-L6-v2 sentence-similarity) | `HF_TOKEN` | `similarity_x10000` (cosine×1e4) | source=`a sunny day in berlin` vs similar/dissimilar | **200** `[0.85, 0.15]` | 1/10 |
| 2 | `TEXT_CLASSIFICATION` | `cls-hf-bart-mnli` | HF zero-shot BART-MNLI | `HF_TOKEN` | `top_label_match` 0/1 | text + labels + expected | **200** positive | 1/10 |
| 3 | `TEXT_CLASSIFICATION` | `cls-hf-twitter-roberta` | HF cardiffnlp twitter-roberta-sentiment | `HF_TOKEN` | `is_positive` 0/1 **or** top_label_match | “I love this product” | **200** positive | 2/10 |
| 4 | `THREAT_IP_REPUTATION` | `tip-abuseipdb` | AbuseIPDB v2 `/check` | `ABUSEIPDB_API_KEY` | `listed` 0/1 from `abuseConfidenceScore≥threshold` | 8.8.8.8 → 0; 185.220.101.1 → 100 | **200** both | 6/10 |
| 5 | `CRYPTO_PRICE` | `crypto-htx` | HTX (Huobi) | none | `price_usd_cents` from `tick.close` | BTC-USDT | **200** | |
| 6 | `CRYPTO_PRICE` | `crypto-mexc` | MEXC | none | `price_usd_cents` | BTCUSDT | **200** | |
| 7 | `CRYPTO_PRICE` | `crypto-gate` | Gate.io | none | `price_usd_cents` from `last` | BTC_USDT | **200** | |
| 8 | `CRYPTO_PRICE` | `crypto-bitfinex` | Bitfinex | none | `price_usd_cents` ticker[6] | tBTCUSD | **200** | |
| 9 | `CRYPTO_PRICE` | `crypto-bybit` | Bybit spot | none | `price_usd_cents` `lastPrice` | BTCUSDT | **200** | → **10/10** if all five ship |
| 10 | `WEATHER_CHECK` | `wxk-metnorway` | MET Norway Locationforecast | none | `temp_k_x100` | 52.52,13.41 | **200** 12.6°C | |
| 11 | `WEATHER_CHECK` | `wxk-7timer` | 7Timer civil | none | `temp_k_x100` from `temp2m` | same lat/lon | **200** | |
| 12 | `AIR_QUALITY_INDEX` | `aqi-cerns` | CERNS.io public city AQI | none | `pm25_ugm3_x10` from `pollutants.pm25` | berlin | **200** pm25=8.1 | |
| 13 | `AIR_QUALITY_INDEX` | `aqi-infranode` | InfraNode UBA JSON proxy | none | `pm25_ugm3_x10` from `payload.pm25` | berlin | **200** pm25=6.0 | |
| 14 | `DNS_RECORD_LOOKUP` | `dns-alidns` | Alibaba Public DNS JSON | none | `has_record` | example.com A | **200** | 7/10 |
| 15 | `STOCK_PRICE` | `stk-yahoo` | Yahoo Finance chart API | none | `last_cents` from `regularMarketPrice` | AAPL | **200** 335.92 | |
| 16 | `VULNERABILITY_TRIAGE` | `vuln-ghsa` | GitHub Advisories API | none | CVSS / severity scalar **match existing label_field** | CVE-2024-3094 | **200** | |
| 17 | `VULNERABILITY_TRIAGE` | `vuln-redhat` | Red Hat securitydata CVE JSON | none | same scored field as NVD keepers | CVE-2024-3094 | **200** Critical | |
| 18 | `ROUTE_ETA` | `route-valhalla` | Valhalla OSM.de public | none | duration seconds (same as OSRM keepers) | Berlin pin | **200** trip | |
| 19 | `ASSET_RESERVE_ATTESTATION` | `res-tether` | Tether transparency.json | none | reserve / circulating scalar **must match PoR field** | USDT | **200** | confirm Gate 1 vs Chainlink PoR |
| 20 | `ASSET_RESERVE_ATTESTATION` | `res-circle` | Circle `/v1/stablecoins` | none | totalAmount for USDC/EURC | USDC | **200** | confirm same quantity |
| 21 | `EVENT_OUTCOME_RESOLUTION` | `event-poly-gamma` | Polymarket Gamma | none | `resolved_yes` on **closed** market pin | closed market id | **200** | may overlap poly-clob — check distinctness |
| 22 | `CORPORATE_REGISTRY_LOOKUP` | `corp-brreg` | Brønnøysund enhetsregisteret | none | `status_active` | Equinor | **200** | |
| 23 | `REGULATORY_FILING_MONITOR` | `reg-sec-submissions` | SEC data.sec.gov submissions | none+UA | `has_form` for pinned form | CIK 0000320193 | **200** | may extend `reg-sec-edgar` |
| 24 | `VENDOR_VERIFY` | `vnd-vatcomply` | VATComply VAT | none | `id_valid` | DE VAT pin | **200** (false on bad pin — good) | |

---

## NEEDS_FIX (keys / method) — do not register until fixed

| Intent | Candidate | Issue | Action |
|--------|-----------|-------|--------|
| `SEMANTIC_SIMILARITY` | Jina embeddings | **401 Invalid API key** | Rotate `JINA_API_KEY` then re-probe |
| `SEMANTIC_SIMILARITY` | Voyage 3-lite | timeout | Retry; if 200, third distinct embedder |
| `TEXT_CLASSIFICATION` | uClassify Sentiment/Topics | **405 GET** | Use POST `/classify` with `texts:[]` + `UCLASSIFY_READ_KEY` |
| `TEXT_CLASSIFICATION` | HF SST-2 | 400 model not on hf-inference | Pick another SST model or skip |
| `SANCTIONS_SCREENING_MATCH` | OpenSanctions | 401 | Needs paid/free key |
| `MACRO_ECONOMIC_INDICATOR` | FRED | 400 no api_key | Signup free FRED key |
| `OPTIMAL_EXECUTION_ROUTE` | 1inch / 0x | 401/404 | Keys or public quote mirrors |
| `GAS_PRICE` | Blocknative | TLS EOF | Retry from EC2 |
| `WEB_SEARCH` | SearX mirrors | 429 / NXDOMAIN | Self-host SearX or Brave free key |
| `PORT_SCAN_AUDIT` | HackerTarget | “valid key required” | Free key or drop |
| `VALIDATOR_PERFORMANCE_VERIFY` | beaconcha.in | now keyed | Free key signup |
| `EMAIL_SECURITY` | Quad9 / Mullvad DoH | timeout / closed | Retry with Accept dns-json from EC2 |

---

## REJECTED this round (do not ship)

| Candidate | Intent | Why |
|-----------|--------|-----|
| wttr.in | WEATHER_CHECK | DUPLICATE reseller (WorldWeatherOnline); bad geocode history |
| open-meteo-current | WEATHER_CHECK | Already `wxk-openmeteo` |
| dns-sb-json | DNS_RECORD_LOOKUP | Already `dns-dnssb` |
| gleif-lei | CORPORATE | Already `corp-gleif-status` |
| binlist / handyapi | PAYMENT | Already registered |
| languagetool-org | GRAMMAR | Already `grm-languagetool` |
| r.jina.ai | CONTENT_EXTRACTION | Same publisher as `cex-jina` |
| sslmate-ct / certspotter | SSL | Already registered |
| defillama-pools | CRYPTO_YIELD | Already used |
| FakeStore / DummyJSON | SKU_IN_STOCK | WRONG_QUANTITY (demo catalog ≠ real merchant stock) |
| Open Food Facts | LIVE_SHELF_PRICE | WRONG_QUANTITY (product DB ≠ shelf price) |
| debian-tracker | VULN | HTML page, not askable JSON scalar |
| isiton / downforeveryone | UPTIME/HEALTH | HTML, not API |
| faa-nas | TRAVEL | Already registered |
| openiban | VENDOR | Already `vnd-openiban` |
| Control D DoH (wire) | DNS | Returned binary DNS wire, not JSON — needs different client |
| KuCoin | CRYPTO_PRICE | Likely already in old intentYamls tree — prefer HTX/MEXC/Gate/Bitfinex/Bybit as clear new CEX set |

---

## Dead intents (46) — Round-2 result

Re-probed samples where a public URL existed (ENTSO-E, HashrateIndex root, LayerZero, OpenSanctions, Metaculus, aviationstack, etc.). **None** unlocked a new Gate-clean keyless miner.

To put *any* miners on Dead intents you need one of:

1. **Product change** — Usman wires adapter/LLM-judge (Gate 0), or  
2. **New free key** held by Telegraph + proxy, or  
3. **New canonical intent** with a different quantity that public APIs actually expose.

Padding Dead to 10 with GitHub/npm/HTML scrapers = the old 1400 failure. **Not done.**

---

## Math vs CEO “~1400 working”

| Item | Number |
|------|-------:|
| Intents in sheet | 97 |
| Already on-chain keepers (Active+Pre) | 135 miners / 49 intents |
| Round-2 ACCEPT to build | **~23** |
| After Round-2 (if all register) | ~158 miners |
| Intents that can honestly reach 10 soon | few (CRYPTO_PRICE can hit 10; most cannot) |
| Dead ×10 | **not honest** |

Honest path to large N: more **distinct publishers on scoring intents** + **new intents your CEO adds**, not 10 clones per Dead row.

---

## Recommended build order (next session)

1. **Unlock the 2 open intents with keys you already have:** `sem-hf-minilm`, `cls-hf-bart-mnli`, `cls-hf-twitter-roberta` (+ fix uClassify POST).  
2. **AbuseIPDB** `tip-abuseipdb` (key works; both outcomes).  
3. **Five CEX** → `CRYPTO_PRICE` reaches 10.  
4. **Weather / AQI / DNS Ali / Yahoo stock / Valhalla / Brreg / VATComply / GHSA / Red Hat.**  
5. Confirm Gate 1 for Tether/Circle vs existing PoR field before register.

Say when to start **Batch 7 registration** for the ACCEPT table (proxy + YAML + validate + cast).
