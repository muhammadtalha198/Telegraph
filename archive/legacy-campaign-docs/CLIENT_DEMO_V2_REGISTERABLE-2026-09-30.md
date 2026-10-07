# Client-demo miners — v2 register list

**Date:** 2026-09-30  
**Folder screened:** `MinerCreator/client-demo-miners/` (1386 YAMLs, demo regs 2972–4347)  
**Bar:** `PROJECT_CONTEXT.md` fail-closed path — YAML shape, Groups A–D preflight, `miner_selftest` RelTol or NON-DET text, `local_validate_keepers --from-yaml`, plus one miner = one upstream.

## Verdict

**Register none of these on real project v2.**

The folder is the old padded demo bag (`clientDemoMinors.md`: not production keepers). After the contract checks, every miner that can pass the gates is a second copy of a source already Active. The one distinct venue that is not already a keeper, Yahoo stock (`stk-yahoo`), fails live (HTTP 502 wrapping Yahoo 429).

No YAML edits were made. The files that pass already name the contract `label_field`. The files that fail are the wrong quantity (a list, a title, a raw object) or an intent the selftest does not score. Pointing those labels at a nearby number would make Validate green and still be the wrong quantity.

## What was checked

| Step | Result |
|------|--------|
| YAML parse + required shape (`validate_miner_yaml.py`) | 1386 / 1386 PASS |
| Intent is in `miner_selftest` `INTENTS` or `TEXT_INTENTS` | 507 |
| That intent **and** the contract `label_field` | 62 files, **30** distinct path+pin groups, **10** intents |
| Live `/truth` or `/caiso` probe of those groups | see table below |
| Full `register_gates.py` on three representatives | `val-beacon-eb` PASS, `wxfv-om-archive-wind` PASS, `mine-blockstream-hashprice` PASS, `stk-yahoo` FAIL |

Unknown intent is a hard fail in `register_gates.py`. The other ~879 demo files (academic search, plagiarism, chatbot-as-Hacker-News, and the Dead judgment intents) cannot be registered until the intent is added to `INTENTS` / `TEXT_INTENTS` **and** the response is the catalog quantity. Most of those are Dead on the sheet because no honest source exists. This folder does not add one.

## Live quantity vs already-Active keeper

Values probed 2026-09-30 against `https://omni-chat.13.237.89.59.sslip.io`.

| Intent | Demo slug (one per source) | Live value | Gates | Already on v2 | Why it is not a new miner |
|--------|----------------------------|------------|-------|----------------|---------------------------|
| `VALIDATOR_PERFORMANCE_VERIFY` | `val-beacon-eb` | `effective_balance_gwei` = 32000000000 | **PASS** (full gates) | `vlp-publicnode` reg **2917**, `vlp-quicknode` reg **2918** | Same beacon effective balance. Selftest warns near-oracle. |
| `WEATHER_FORECAST_VERIFY` | `wxfv-om-archive-wind` | `wind_kmh_milli` = 16500 | **PASS** (full gates) | `wnd-era5` reg **2908** (Open-Meteo ERA5) plus Bright Sky, METAR, ECCC, JMA | Same publisher family as the Active ERA5 wind miner. |
| `MINING_HASHPRICE_VERIFY` | `mine-blockstream-hashprice`, `mine-btc-mempool-space`, `mine-mempool-emzy`, `mine-mempool-ninja`, `mine-mempool-c` | all `hashprice_sats_per_ph_s_day` = **233214** | **PASS** on blockstream (full gates); peers match on the live probe | `mine-mempool-hashprice` reg **2764** | 0 bps apart. RelTol is 400 bps, so tol/10 duplicate line is 40 bps. Listed for removal in `out/same-source-cleanup-plan.md` (regs 2781, 2803–2810). |
| `GRID_POWER_PRICE` | `grid-caiso-np15-b` (and `-c`…`-j`) | `lmp_usd_per_mwh_milli` = 49518 | live quantity OK | `grid-caiso-np15-dam` reg **2758** | Same CAISO NP15 pin. Cleanup plan 2786, 2819–2826. |
| `LIVE_SHELF_PRICE` | `shelf-open-prices-b` (and `-c`…`-j`) | `price_cents` = 2770 | live quantity OK | `shelf-open-prices` reg **2759** | Same Open Prices id. Cleanup plan 2783, 2827–2834. |
| `MACRO_ECONOMIC_INDICATOR` | `macro-wb-unemp-usa`, `macro-wb-unemp-proxy-b` | both `rate_pct` = 3.669 | live quantity OK | `macro-wb-unemp-us` reg **2753**, `macro-wb-unemp-proxy` reg **2784** | Same World Bank unemployment print. Cleanup plan 2835–2842. |
| `ONCHAIN_METRIC_VERIFY` | `ocm-eth-balance-*` (8 RPC names) | `value_gwei` ≈ 5.72e9 on publicnode | live quantity OK | `ocm-eth-balance` reg **2761** | Same address and block, different RPC mirrors. Cleanup plan 2780, 2786–2794. |
| `ASSET_RESERVE_ATTESTATION` | `res-wbtc-por-*` (8 RPC names) | `attested_reserve` = 116144650225 | live quantity OK | `res-wbtc-por` reg **2763** | Same Chainlink WBTC feed. Cleanup plan 2782, 2795–2802. |
| `VULNERABILITY_TRIAGE` | `vuln-nvd-c`, `vuln-cveorg-b` | `cvss_base_score` = 10.0 for CVE-2021-44228 | live quantity OK (field alias accepted) | `vuln-nvd` reg **4371**, `vuln-cveorg-cvss` reg **2785** | Same CVE pin, same CVSS. Cleanup plan 2813–2818. |
| `STOCK_PRICE` | `stk-yahoo` | — | **FAIL** Group B HTTP 502 (Yahoo 429) | not a keeper; deferred in `newlyRegisteredMiners.md` | Distinct venue, not askable today. YAML shape is already valid. |

Letter-suffix peers (`-b` through `-j`, `pool-c`) share one path and one pin. They are not extra sources.

## Close, still not registerable

| Slug | What came back | Block |
|------|----------------|-------|
| `cyield-llama-apy` | HTTP 200, `apy` = 2.245, no `apy_bps` | `CRYPTO_YIELD_RATE` requires `apy_bps`. DefiLlama is already Active as `yld-defillama`. |
| `ven-ofac-entity` | HTTP 200, `sanctioned` = 1, no `id_valid` | OFAC list membership is not `VENDOR_VERIFY`. Sanctions already has its own Active miners. |
| `threat-otx-ip`, `tip-otx-abuse` | read timeout; YAML field is `abuse_confidence` | Contract fields are `ioc_flagged` and `listed`. Threat intents already have Active miners. |

## Why the rest of the bag stays out

- **Wrong field.** Examples from the static pass: `CHATBOT_CONVERSATION` labeled `title` / `feed`, `LANGUAGE_TRANSLATION` labeled `responseData`, `DNS_RECORD_LOOKUP` labeled `Answer`, `STOCK_PRICE` labeled `chart`, `WEATHER_CHECK` labeled `current`. HTTP 200 on those bodies is the Group D failure (list or object, not the scored quantity).
- **Dead intents.** Commerce purchase, wash trading, fraud, code review, plagiarism, speech-to-text, and the other Dead rows are absent from `INTENTS` / `TEXT_INTENTS` on purpose. A demo YAML that scrapes Crossref or Hacker News does not become a scorer.
- **NON-DET already shipped.** Translation, summary, chat, and TTS Pre-active miners are `tr-*`, `sum-*`, `chat-pollinations` / `chat-aihorde` / `chat-nova`, and `tts-google` / `tts-espeak`. The demo `chat-*`, `tts-*`, and `tr` files point at news and metadata, not `reply_text` / `audio_b64` / `translated_text`.

## If a later source should be added

Use only `./scripts/register-miner.sh` after the four gates pass, and only when the upstream is not already an Active slug above. `stk-yahoo` is the only demo file that is a real extra venue; retry it when `/truth/stock-last?venue=yahoo&symbol=AAPL` returns `last_cents` inside the stock range, then run the register script. Do not register the RPC mirrors or the letter-suffix clones.
