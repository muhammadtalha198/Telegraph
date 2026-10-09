# PROJECT_CONTEXT — TeleGraph MinerCreator

**Last updated:** 2026-10-08  
**Workspace:** `/Users/mrmacbook/Documents/TeleGraph`  
**This file:** MinerCreator campaign handoff (current state only).  
**Separate doc:** `Telegraph/documentation/PROJECT_CONTEXT.md` = Go node architecture.

---

## 1. Overview

Build, validate, host, and register **intent miners** (YAML → public URL → on-chain `registerMiner` on Base Sepolia) for Usman’s scoring stack.

- **Doctrine:** one miner = one upstream source; answer must match intent description; fewer correct > pad (“Ahmed rule”).
- **Diamond:** `0x5a2324aA18613FAD4e44bDF0d6c73Ec1f6D87ff8` (Base Sepolia)
- **YAML host:** `https://omni-chat.13.237.89.59.sslip.io/miner-yamls/<slug>.yaml`
- **Truth proxy:** `https://omni-chat.13.237.89.59.sslip.io/truth/…` ← `scripts/semantic-truth-proxy.py` on Omni (`ubuntu@13.237.89.59`, key `telegraphNode1.pem`)
- **Inventory:** `ACTIVE_MINERS.xlsx` — **329** Active miners (xlsx not yet re-synced with the +6 below) · **56** intents · **23** still on paste.rs (no true_id)
- **On-chain total is 335** after the 2026-10-09 miner hunt (+6: reg 4804–4809, see `newlyRegisteredMiners.md` → "New miner hunt — 2026-10-09"). `ACTIVE_MINERS.xlsx` needs a re-sync to pick these up.

**People:** Usman (scoring/ranking) · Talha/team (APIs/YAML/register) · Ahmed (correct > quantity) · Haider (semantic WASM)

**Answer verification (`minercheck/`, 2026-10-08):** scope = the RIGHT output from each API, any shape; Usman scoring/ranking is out of scope (ranking module removed). The **Intent Catalog is law**: `Intent Catalog v2 25-Sept (1).xlsx` → `intents/_catalog.json` (`python -m minercheck catalog build`; 119 intents). Tiers from `intents/_catalog_policy.yaml`: **required** 71 (DETERMINISTIC/HYBRID with a comparator truth — spec required, gate FAILS "no spec for catalog intent X"), **judgment** 26 (NON-DETERMINISTIC + 12 HYBRID overrides whose catalog Evaluation Mechanism is LLM/heuristic-scored: SKIP, LLM judge gets the catalog Description), **unverifiable** 22 (Verifiable=No: BLOCKED). **17 of 71 required have specs; remaining 54 bucketed in `docs/CATALOG_COVERAGE.md` (≈14 feasible with free APIs · ≈20 single-source/regional · ≈20 need private/paid data).** 17 specs bound to catalog rows (`catalog:` block, verbatim Description, facets, `allowed_kinds`): CRYPTO_PRICE, FX_NOW, WEATHER_CHECK, STOCK_PRICE_QUOTE, ONCHAIN_METRIC_VERIFY, PAYMENT_METHOD_VERIFY, CRYPTO_YIELD_RATE, LIQUIDITY_DEPTH_VERIFY, TOKEN_TOTAL_SUPPLY_VERIFY, VALIDATOR_PERFORMANCE_VERIFY, DNS_RECORD_LOOKUP, CORPORATE_REGISTRY_LOOKUP, MACRO_ECONOMIC_INDICATOR, LOAN_INTEREST_RATE_QUOTE, CARRIER_SERVICEABILITY, REGULATORY_FILING_MONITOR, COLLATERAL_HAIRCUT_VALUATION; DATE_TODAY/TIME_IN_CITY are local-only. `python -m minercheck catalog audit` checks alignment (all ALIGNED). FX_NOW is real-time (data >1 h stale, so ECB/er-api/fawaz daily fixes fail). Scope = the right output from each API, any shape; Usman ranking is out of scope.

**Stack:** Python 3.14 stdlib + PyYAML (`.venv`; system `python3` has no PyYAML, so always use `.venv/bin/python`). Node = Go in `../Telegraph` (miner YAML schema `modules/miner-dispatcher/schemas/integration.schema.json`, `additionalProperties: false`).

---

## 2. Two register paths

| Path | When | Entry |
|------|------|--------|
| **Semantic V2** (default) | Format-agnostic; answer matches description | `register-miner-v2.sh` → `register_gates_v2.py` |
| **Legacy RelTol** | Exact `label_field` + scale | `register-miner.sh` → `register_gates.py` |

**V2 flow:**  
`capture_api_output.py` → `auto_review_samples.py --apply --require-llm` → (golden if suite) → `generate_yamls_from_approved_samples.py` → `upload-host.sh` (Omni SSH) → `register-miner-v2.sh`  
Gates re-run auto_review+LLM at gas time. Manual `set_sample_status approved` ≠ unlock.

**`register_gates_v2.py` order:** auto_review (hard check → minercheck sample check → heuristics → LLM) → golden-if-any → `validate_miner_yaml` → `pin_consistency_check --file` → **sample `request_url` == node request** → **`python -m minercheck gate`** (live answer verified vs independent sources; SKIP if no spec; FAIL if spec'd intent but slug not mapped in `sources[].miner`) → live probe → (sh) hosted byte-match → gas.

**Hard bans:** no direct `cast send registerMiner/updateMiner`; no `--skip-gates` / `--no-llm` / `--skip-live` / `--skip-verify`; no paste.rs unless `ALLOW_PASTE_FALLBACK=true`; no batch scripts under `archive/`.

**Rankability (Usman):** same intent + rank set must share **one question/pin**. Same param name, different meaning = `diff-question` (not rankable). LLM normalize fixes shape, not different questions. Pins: `shared_pins.json` + `pin_consistency_check.py`.

---

## 3. Current inventory & wave status

| Item | State |
|------|--------|
| `ACTIVE_MINERS.xlsx` | 329 rows (All miners sheet); README tab totals updated 2026-10-08 |
| `intentYamls/` | ~327 YAMLs / 56 intents |
| Pack V2 (earlier) | 61 registered; 5 gate fails left unregistered |
| **Paste → Omni (2026-10-07)** | **141** `updateMiner` OK → new IDs; log `out/PASTE_MIGRATION.jsonl`. **23** still paste.rs (broken tx hashes / no true_id). Backup: `out/paste_backup/` (164) |
| Reg ID bug | Fixed: ID from receipt (`reg_id_from_receipt.py`), not `minerCount()`. Reconcile: `out/RECONCILED_REG_IDS.md` (93 wrong logged IDs) |
| **Wave2 (2026-10-08)** | Golden 93 → capture 68 → auto-review **28 approved**. Minercheck gate on those 28: **10 PASS** (8 crypto + 2 FX, mapped into `intents/CRYPTO_PRICE.yaml` + `FX_NOW.yaml`), **16 SKIP** (no intent spec), **2 NO_YAML** (`coll-dia-eth`, `port-imf-portwatch` — no folder map). Report: `out/wave2_minercheck_gate_report.json`. **Not registered yet.** |
| Omni ~1400 | Two cohorts, not inventory: OmniRoute chat/response ≈959; client-demo re-regs 1367. Sieve only. |

**Wave2 skip reasons (capture):** POST/JSON-RPC, DoH binary (needs proxy decoder), custom headers, pack row not in candidates.

**Lifecycle (docs):** Active only (Pre-active removed 2026-10-06). `workingMiners.md` = wired keepers subset. New Usman packs → `newlyRegisteredMiners.md` then Excel.

---

## 4. Critical commands

```bash
cd ~/Documents/TeleGraph/MinerCreator
# venv + PyYAML required (validator fail-closed without it)
.venv/bin/python -c "import yaml"

# V2 single miner
python3 scripts/capture_api_output.py --intent … --slug … --url '…'
python3 scripts/auto_review_samples.py --apply --require-llm --file apiOutputSamples/<I>/<slug>.md
python3 scripts/generate_yamls_from_approved_samples.py
./scripts/upload-host.sh …   # Omni SSH first
./scripts/register-miner-v2.sh --file intentYamls/…/<slug>.yaml \
  --url https://omni-chat.13.237.89.59.sslip.io/miner-yamls/<slug>.yaml \
  --sample apiOutputSamples/<I>/<slug>.md

# Wave2 helpers
python3 scripts/wave2_capture.py [--limit N] [--dry]
# queue: out/wave2_queue.jsonl

# Paste migration (mostly done for 141)
python3 scripts/migrate_paste_to_omni.py backup|rehost|repoint [--execute] [--limit N]

# Proxy deploy (NOT live yet — dry-run only as of 2026-10-07)
./scripts/deploy_truth_proxy.sh --dry-run
./scripts/deploy_truth_proxy.sh

# Consistency
python3 scripts/pin_consistency_check.py --same-source   # 37 extras
python3 scripts/pin_consistency_check.py --fixed         # path-baked / no params
python3 scripts/reconcile_reg_ids.py

# Answer verification (minercheck; always the venv python)
.venv/bin/python -m minercheck validate-spec                       # load + validate intents/*.yaml
.venv/bin/python -m minercheck ask WEATHER_CHECK location=Lahore unit=F [-v] [--json] [--all-sources]
.venv/bin/python -m minercheck run-tests [--intent X]              # live spec tests
.venv/bin/python -m minercheck catalog build|table|audit|show X    # catalog index, gap table, spec alignment
.venv/bin/python -m minercheck gate --file intentYamls/…/<slug>.yaml --intent X   # or --sample <md> (no YAML)
.venv/bin/python -m minercheck batch                               # Wave2 approved → out/wave2_catalog_gate_report.{json,md}
.venv/bin/python tests/record_live.py [INTENT]                     # refresh replay fixtures (IPs scrubbed)

# Tests (no network): 83 cases
.venv/bin/python -m unittest discover -s tests -t .
```

**auto_review LLM:** prefer local Ollama (`OLLAMA_BASE_URL`, `qwen2.5:3b`, `AUTO_REVIEW_PREFER_OLLAMA=1`). If `OLLAMA_BASE_URL` is set but Ollama is down, cloud is **not** tried unless `AUTO_REVIEW_ALLOW_CLOUD_FALLBACK=1`. OpenAI often **no credits**; OmniRoute judge often 502/401. Start Ollama.app before batch review. `--apply` writes only `approved`/`rejected`; `needs_human` leaves file as `pending_review`.

**Env (names):** `DIAMOND`, `RPC_URL`, `MINER_PRIVATE_KEY`, `FEE_ADDRESS`, `OMNI_SSH_KEY`, `OMNI_SSH_TARGET`, `HOST_PREFIX_CHAT`, `OMNIROUTE_API_KEY` / `OPENAI_API_KEY`, `OLLAMA_*`.

---

## 5. Key decisions (current)

- **Intent specs ≠ miner YAMLs.** The node rejects unknown keys in miner YAMLs, so answer_type/extraction/templates live in `intents/<INTENT>.yaml` and point at miners by `sources[].miner.slug` + `question`. Hosted miner YAMLs stay node-format.
- **Correct = verified, not "LLM said answers".** E1 extract → E5 answer type → E2 sanity → E4 freshness → E5 entity/scope → E3 cross-check. E3: one vote per publisher; the biggest group within the YAML tolerance is the consensus; verified only if ≥ `min_sources` agree **and** they are a strict majority. Otherwise "could not verify" (never a silent guess).
- **Format never decides.** The reader detects JSON/XML/HTML/CSV/text from the body, not Content-Type. Broken/truncated XML or JSON becomes text (only a regex rule can read it), never "repaired".
- **Catalog facets:** every Description clause is listed in the spec (`covered_by: value | extra:x | input:x | none`); exactly one is the verified value; `required` facets must be in the miner's answer. Source `kind` must be in `catalog.allowed_kinds` (e.g. CEX book ≠ "decentralized pools"). `authority: true` sources (official record holder) verify on their own.

- Fail-closed gates on every register; Cursor rule `.cursor/rules/miner-register-gates.mdc`.
- Shared pins for rankable intents; AQI locked to Berlin `52.52,13.41` + PM2.5 in `shared_pins.json` (proxy + gates). Rank set: openmeteo, uba, sensorcommunity. Out of rank: cerns (Open-Meteo clone), infranode, luchtmeetnet (NL), neasg (SG) — **on-chain cleanup still pending Usman**.
- Proxy substitutions **fail closed** (`TRUTH_ALLOW_SUBSTITUTES=1` restores old cheat paths: CVE→NVD, wrong ship MMSI, cerns→OM, textprocessing→HF/Twinword).
- Same-publisher + duplicate-slug blocked at V2 gate (`pin_consistency_check.py`).
- Live probe calls YAML as the node will (no GET-on-POST-RPC false pass; no cross-host redirect follow).
- YAML validator requires PyYAML.
- Registration IDs from tx receipt events (`MinerRegistered` / `MinerUpdated`); `updateMiner` mints a **new** ID.
- Hosting: Omni SSH only by default (paste.rs = public DELETE).

---

## 6. Open / blocked

| Item | Status |
|------|--------|
| **2026-10-09 miner hunt — 6 registered** | 5 new CRYPTO_PRICE CEX sources (phemex, xt, bitrue, hitbtc, digifinex) + 1 STOCK_PRICE source (stockanalysis.com); reg 4804–4809, all `active`. Added as `sources:` in `intents/CRYPTO_PRICE.yaml` / `STOCK_PRICE_QUOTE.yaml` first so `minercheck gate` could verify pre-gas. Detail: `newlyRegisteredMiners.md`. |
| ACTIVE_MINERS.xlsx stale by +6 | Needs a re-sync pass to add reg 4804–4809 (currently only in `newlyRegisteredMiners.md`). |
| wx-brightsky-de not registered | Sample **rejected by the Ollama LLM judge** (qwen2.5:3b false-negative — `weather.temperature` IS present in the capture). Not force-approved (manual override ≠ unlock gas, per CLAUDE.md). Candidate kept in `miner_candidates/2026-10-09/`; retry auto_review later. |
| dns.sb / DNSPod candidates dropped | Found to be **duplicates** during dedupe: `dns-dnspod` (reg 4671, Active) is the literal same `doh.pub/dns-query` endpoint; `dns-dnssb` slug is taken (reg 2894, unrelated truth-proxy signal). Caught before capture/gas — lesson: dedupe must check the full `intentYamls/` tree + `ACTIVE_MINERS.xlsx`, not just `intents/*.yaml` spec sources. |
| Deploy truth proxy + systemd | Code + `deploy_truth_proxy.sh` ready; **dry-run only** — local md5 ≠ server; still bare `python3` on Omni |
| AQI on-chain cleanup | Needs Usman: Berlin pin confirm; deregister cerns / NL / SG; update uba/sensorcommunity |
| Same-publisher families (37) | Decide keep-one per family before re-register/update through gates |
| 9 RPC miners (POST-only) | Repair via proxy adapter **or** deregister |
| 23 paste.rs left | Need true IDs (bad log tx hashes) before repoint |
| Wave2 28 approved | YAML → host → `register-miner-v2.sh` not started |
| Wave2 28 needs_human | Fix captures / human glance (e.g. wrong symbol) |
| Wave2 DoH / POST / headers | Need proxy decoder or POST capture before register |
| NON-DET scoring wire | Translation/summarize/chat/TTS not in node judgment/hybrid set — Usman/Haider |
| Dropbox token | Empty; not used |
| **cp-kraken (4683) / fx-frankfurter on-chain** | Broken / cross-host-redirect answers live. Local YAMLs fixed 2026-10-08 (`pair: XBTUSD`; `api.frankfurter.dev/v1/latest`), minercheck gate PASS → re-host + `register-miner-v2.sh --update <id>` (needs fresh samples) |
| **cp-redstone (4670)** | Approved sample body was `[]`; deregister or recapture + update through gates |
| fx-hnb id | Local id 31004 → 190175 (was duplicate of fx-awesomeapi); miner is deregistered |
| LLM gate vs correct answers | qwen2.5:3b rated a correct USD→EUR rate "partial" (catalog description asks for spreads). Decide: may a minercheck PASS outrank LLM "partial"? (unchanged: LLM approval still mandatory) |
| **Catalog answer-verification (DONE 2026-10-08)** | `minercheck catalog build` → `intents/_catalog.json` (119 intents; tiers: 83 required, 14 judgment, 22 unverifiable). 14 catalog specs written + audited ALIGNED. Engine: boolean/record_set answer types, `table` input kind, JSONP unwrap, list `each`/`where`/`aggregate:notional`/`hex`/`map`/`exists` rules, source `kind` + `allowed_kinds`, `authority:true` (single-source verify), source `when:` filter, catalog facets. Report: `out/wave2_catalog_gate_report.{json,md}`. Tests: 83 pass (`.venv/bin/python -m unittest discover -s tests -t .`). |
| **Wave2 28 approved re-gated (2026-10-08)** | **19 PASS · 8 FAIL · 1 BLOCKED** (all `catalog`-grounded). FAIL: 6 LIQUIDITY miners (CEX books + dYdX = orderbook depth ≠ decentralized-pool liquidity, wrong `kind`); `coll-dia-eth` (price only, missing required `risk haircut`); `car-zippopotam` (postcode geocoder, not a `carrier`); `corp-sk-rpo` (RPO upstream timed out — flaky, verified fine during probing). BLOCKED: `port-imf-portwatch` (catalog Verifiable=No). |
| Gate behaviour change | `register_gates_v2` → `minercheck gate` now **FAILS closed** for any catalog-required intent with no `intents/<INTENT>.yaml` (was SKIP). judgment-tier intents SKIP (LLM judge); unverifiable-tier BLOCKED. |
| 41 YAML / 33 sample "PACK READY…" descriptions | Garbage intent description fed to LLM judge; not rewritten (each change = on-chain update) |

---

## 7. Paths that matter

| Path | Role |
|------|------|
| `CLAUDE.md` | Agent rules (Rule 1 = keep this file current) |
| `SEMANTIC_REGISTER_V2.md` | V2 doctrine |
| `README.md` | Register + hosting + ID notes |
| `INTENT_BUILD_SHEET-2026-09-23.md` | Intent tables / descriptions |
| `ACTIVE_MINERS.xlsx` | Live inventory (All miners / By intent / README) |
| `newlyRegisteredMiners.md` | Recent pack notes |
| `workingMiners.md` | Wired keepers only |
| `shared_pins.json` | Locked ask pins |
| `intents/` | Intent specs (`<INTENT>.yaml`), `_shared.yaml` (places/currencies), `_catalog.json` (generated catalog index), `_catalog_policy.yaml` (tiers, aliases, source kinds) |
| `minercheck/` | Verifier package: spec · normalize · fetch · reader · units · answers · validate · verify · render · catalog · gate · sample_check · cli |
| `tests/` | unittest suite; `fixtures/live/` (real responses 2026-10-08), `fixtures/formats.py` (5-format mocks) |
| `docs/` | `ANALYSIS_REPORT.md`, `INTENT_SPEC_GUIDE.md` |
| `out/minercheck/` | `cache/` (gitignored) |
| `intentYamls/` | On-disk YAMLs |
| `apiOutputSamples/` | V2 samples + status |
| `scripts/` | Gates, proxy, migrate, wave2_capture, deploy |
| `out/` | Keep lean: paste backup, reconcile, migration log, pack/V2 reports, wave2_* reports, last-registration*.json, registry.jsonl |
| `.backup-2026-10-07/` | Snapshots of Oct-7 edits |
| `miner_pack/` | Wave2 candidates + `results/` (golden) |
| `UsmanRsponse/` | Scoring contract / fail sheets |
| `Telegraph/` | Node scoring / WASM / contracts |
| `telegraphNode1.pem` | Omni SSH (repo root) |

**Scripts (new/critical since 2026-10-07):**  
`reg_id_from_receipt.py` · `reconcile_reg_ids.py` · `migrate_paste_to_omni.py` · `pin_consistency_check.py` · `deploy_truth_proxy.sh` · `wave2_capture.py` · `sample_file.py` (the one sample parser/writer used by auto_review, gates, generate, golden, set_sample_status)

---

## 8. Omni / proxy ops

- SSH: `ssh -i ~/Documents/TeleGraph/telegraphNode1.pem ubuntu@13.237.89.59`
- Proxy listen `:8765`; nginx `/truth` → proxy. **Supervision:** deploy script installs `semantic-truth-proxy.service` (`Restart=always`); until then bare process dies on reboot (~141 `/truth` YAMLs).
- Disk was ~38% (2026-10-06). Cleanup helper: `scripts/safe_omni_disk_cleanup.sh`.

---

## 9. Conventions

- Intent description is law; Validate/HTTP 200 ≠ Usman-scorable.
- Catalog intent names may alias on-chain via `v2_intent_folders.py` (e.g. `CRYPTO_PRICE_LOOKUP` → diamond name).
- Class on sheet/Excel: DETERMINISTIC | HYBRID | NON-DETERMINISTIC.
- Cursor sandbox often cannot reach public APIs / Omni SSH; run capture/register/deploy from real Terminal with network (`required_permissions: all` / local shell).
- Do not ask the user to “run tests manually” — the register pipeline is the test.
