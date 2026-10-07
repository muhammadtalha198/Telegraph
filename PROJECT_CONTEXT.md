# PROJECT_CONTEXT — TeleGraph MinerCreator (handoff)

**Generated:** 2026-09-30  
**Last updated:** 2026-10-07  
**Workspace:** `/Users/mrmacbook/Documents/TeleGraph`  
**Primary chat transcript:** `agent-transcripts/9e012a38-5259-4212-8f67-b90fe0e2d5ca/`  
**Prior chat (pre-limit handoff):** `agent-transcripts/5e4ae417-af1d-4432-a537-0b914e3e9e9a/`  

> Note: `Telegraph/documentation/PROJECT_CONTEXT.md` is a **separate** doc for the Go node architecture. This file is the MinerCreator campaign handoff (Sep 23–30 base + Oct 2–7 Semantic V2 / pack / shared-pin updates).

---

## 1. PROJECT OVERVIEW

**What:** TeleGraph MinerCreator — build, validate, host, and register **intent miners** (YAML → public URL → on-chain `registerMiner` on Base Sepolia Diamond) so Usman’s scoring stack can rank them.

**Goal:** Register **quantity-correct, askable, distinct-source** miners that match each intent’s catalog description. Never optimize for Validate=PASS alone. **One miner = one upstream source.** Prefer fewer correct over padding (“Ahmed rule”).

**Who it’s for:**
- **Usman Siddiqui** — scoring contract, RelTol/PassFail comparators, adapter / LLM-judge / semantic WASM ranking.
- **Muhammad Talha / team** — hunt APIs, write YAMLs, run fail-closed register pipeline, keep lifecycle docs.
- **Ahmed Ali** — doctrine pressure: correct over quantity; unblock Usman on NON-DET.
- **Haider (∑)** — semantic path: GT in plain English → LLM normalizes miner output → semantic WASM scores 0–1.
- **CEO** — inventory status (Active / Pre-active / Dead counts).

**Diamond (Base Sepolia):** `0x5a2324aA18613FAD4e44bDF0d6c73Ec1f6D87ff8`  
**YAML host:** `https://omni-chat.13.237.89.59.sslip.io/miner-yamls/<slug>.yaml` (Active legacy; ~**280** files on EC2 as of 2026-10-06) · **paste.rs** for many Semantic V2 / Pack V2 registrations (Dropbox token empty).  
**Truth / adapter proxy:** `https://omni-chat.13.237.89.59.sslip.io/truth/...` (served by `scripts/semantic-truth-proxy.py` on the Omni host) — still required for ~141 YAMLs with `base_url: https://omni-chat…`.  
**Omni SSH:** `ubuntu@13.237.89.59` with key `telegraphNode1.pem` (reachable again 2026-10-06; disk ~**38%**).

**Two scoring paths (do not conflate):**
1. **Deterministic / RelTol–PassFail** — exact `label_field`, scale, pin. Legacy `register-miner.sh` path.
2. **Semantic / adapter / LLM-normalize (V2)** — answer-correct, format-agnostic; Usman/Haider LLM normalize → semantic WASM 0–1. Register via `register-miner-v2.sh` + `auto_review` (+ local Ollama, OmniRoute, OpenAI, or any OpenAI-compatible `/v1/chat/completions` judge). Lifecycle docs (2026-10-06): **no Pre-active bucket** — all registered miners listed as Active in sheet/Excel.

**Rankability rule (Usman 2026-10-06):** LLM normalize fixes **output shape**, not **different questions**. Rankable miners for an intent must share one pin (same place/time/params). Same param name with different meanings (e.g. AQI `site` = DE station vs NL station vs lat,lon) = **`diff-question`** → not comparable.

---

## 2. TIMELINE

### 2026-09-23 — Continuity + lifecycle + first new intents

- Chat hit context limit; built handoff prompt into this session from prior ~2 weeks of work.
- Canonical doctrine: `MINER_BUILD_PLAN-2026-09-23.md` + Usman `MINER_SCORING_CONTRACT` (upload / `fable-handler/02_MINER_SCORING_CONTRACT.md`).
- Built **`INTENT_BUILD_SHEET-2026-09-23.md`** from `Intent Catalog v2 25-Sept (1).xlsx` (skip verifiable=no / obsolete).
- **Same-source cleanup:** deregister duplicates so one miner = one source (Usman: ranking needs distinct sources).
- Explained **Active** = Usman-approved / scorable keepers.
- Colored lifecycle tables + miner counts on sheet.
- **`CODE_PATCH_VERIFY`:** hunted APIs; Ahmed rule → **3** honest sources (not fake 10); built + registered; Usman note file (later deleted preference: use `newlyRegisteredMiners.md` only for Usman packs until approved).
- Deep-read Usman / Telegraph scoring: YAML → ask pin → extract `label_field` → RelTol/PassFail WASM → rank.
- Confirmed **`local_validate_keepers.py` + `miner_selftest.py`** as local pre-register checks.
- **`CROSS_CHAIN_STATE_VERIFY` + Stripe commerce** path: register YAMLs; smoke via `/truth/xchain-*` returning `execution_ok: 1`.
- Established lifecycle buckets: **Active → Pre-active → Not registered → Dead**.
- Pre-active = in `newlyRegisteredMiners.md` awaiting Usman; Dead = rejected **or** zero honest sources.
- Started bag of Priority-10 intents (commerce / event / route / SKU / travel / wash / fraud / LLM eval…).

### 2026-09-24 — BAG20 + Fable research + Batches 5–6

- Day-end status format established (completed / in progress / blockers / next) — **no tables** when asked.
- Many intents → Dead (0–3 APIs max); padded “Scale to 10+” banned.
- Built **Fable deep research prompt** + portable pack in `MinerCreator/fable-handler/`.
- Fable returned `API_SOURCES_BY_INTENT-2026-09-24.md`; used for build/register waves.
- Batches **5 and 6** registered after keepers + selftest PASS.
- Updated sheet Pre-active / Dead; “Not registered ~30” = Fable found nothing usable.
- Clarified: **~1400 Omni mass regs** are a different cohort — restore possible via OmniRoute registry but **do not count** as new-method gated miners.

### 2026-09-25 — Omni / public-apis / Alexandria / integrate UI

- Deep-searched OmniRoute, `public-apis`, Alexandria for mechanisms and leftover APIs.
- Integrate UI: `https://integrate.telegraphprotocol.com/register?mode=create` (YAML create/register UX).
- Confirmed post-~120/30 new-method miners are meant to match description + Usman askability (unlike many of the 1400).
- Inventory snapshots (Active / Pre-active / left / Dead) iterated as docs changed.
- Round-two pre-active notes: `ROUND2_PREACTIVE-2026-09-25.md`.

### 2026-09-26 — Close remaining hunt work

- Continued registration / Dead marking; “how many left” tracking.
- Usman review artifact: repo-root `USMAN_REVIEW-2026-09-26.md` / non-working report used later.

### 2026-09-28 — Usman feedback Groups A–D + resubmission

- Confirmed intents must match Google sheet / catalog (CEO/Usman pressure).
- Promoted **working** CRYPTO_PRICE / WEATHER_CHECK / STOCK_PRICE into Active with **date separator rows** (`—— 2026-09-28 ——`).
- Removed promoted rows from `newlyRegisteredMiners.md`.
- **Group A — CRYPTO_YIELD_RATE:** YAML syntax / pool-key issues on `yld-*` → fix + re-register → **resubmission** file for Usman.
- Made YAML syntax / shape checks part of validation so the issue can’t recur silently.
- **Group B — dead upstreams:** `event-kalshi-result` (proxy 502 wrapping **HTTP 404**); `yld-compound` upstream dead → re-pin / replace (Compound path later live as reg **4375** in campaign notes).
- **Group C — VESSEL:** `ves-digitraffic` “no recent position for mmsi …” = live-data absent, not a code defect; re-pin to MMSI with data (`230981000` / reg **4365**).
- **Group D — VULNERABILITY_TRIAGE:** 9 miners HTTP 200 but **WRONG_QUANTITY** (listings/CVE pages, not CVSS base score). Intent needs CVSS numeric @ ~50 bps — not browse HTML.
- Quote Usman: yld `Pool key:` description must match; highest ROI fix.
- Built separate “intent names we changed” note for Usman.
- Day-end: wire yesterday’s fixes into **automatic** pre-register gates.

### 2026-09-29 — Fail-closed gates + NON-DET campaign

- Wired Groups A–D lessons into `preflight_miner.py`, `validate_miner_yaml.py`, `local_validate_keepers.py`, `miner_selftest.py`, and **`register-miner.sh`** (blocks gas unless PASS).
- Cursor rule: `.cursor/rules/miner-register-gates.mdc`.
- Usman: need **any** working NON-DET for adapter path → shipped **`LANGUAGE_TRANSLATION`** first (`tr-mymemory` **4383**, `tr-google` **4384**).
- Deep NON-DET hunt → campaign **13 miners / 4 intents**:
  - Translation 4 · Summarization 4 · Chatbot 3 · TTS 2  
  - Reg IDs **4383–4384, 4388–4389, 4391–4393, 4395, 4399, 4401–4404**
- Docs: `USMAN_NONDET_TRANSLATION-2026-09-29.md`, `USMAN_NONDET_CAMPAIGN-2026-09-29.md`.
- Proxy routes: `/truth/translate|summarize|chat|tts`.
- `TEXT_INTENTS` added to `miner_selftest.py` / `preflight_miner.py` (text / `audio_b64` askability, not RelTol).
- Chat pin lengthened after reply `"4"` failed min length; `min_len` for chat → **1**.
- Pollinations **402** flake observed on some LLM venues.
- Promoted yield / event / vessel into Active (`—— 2026-09-29 ——`) after Groups A–D closed.

### 2026-09-30 — Auto pipeline confirmation + lifecycle flip + CEO messaging

- Confirmed register path is fully automatic fail-closed (no manual “run tests then cast”).
- Counts: only **new-method gated** miners (~158 active / ~169 probed with IDs earlier); **exclude ~1400 / Omni mass**.
- Usman verified former pre-active bag → **promote to Active**:
  - **96 miners / 32 intents** archived in `newlyRegisteredMiners.md`.
  - Current Pre-active = **NON-DET only: 13 miners / 4 intents**.
- Sheet totals: **Active 153 · 49**; **Pre-active 13 · 4**; **Not registered 0**; **Dead 46** (four NON-DET removed from Dead → Pre-active).
- CEO inventory email drafted; explained **“not given the exact output”** (quantity/field/scale/pin ≠ API down); combined with NON-DET “no single exact answer.”
- Haider semantic WASM path clarified vs Usman RelTol path.
- This handoff file written.

### 2026-10-02 — Semantic Register V2 path landed

- Ahmed/Usman: answer-correct / format-agnostic path (LLM normalize on Usman side).
- Docs: `SEMANTIC_REGISTER_V2.md`; samples under `apiOutputSamples/<INTENT>/<slug>.md`.
- Scripts: `capture_api_output.py`, `auto_review_samples.py`, `generate_yamls_from_approved_samples.py`, `register-miner-v2.sh`, `register_gates_v2.py`.
- Early V2 note: capture → approve → register. Later hardened so **manual approve alone cannot unlock gas** (auto_review+LLM mandatory).
- Cursor rule `.cursor/rules/miner-register-gates.mdc` updated for V2 path (keep legacy RelTol path too).
- First V2 register batch artifacts under `out/V2_REGISTER_BATCH*.md` / jsonl (sample-approved Semantic V2 wave — later counted as Pre-active then promoted).

### 2026-10-04 — Pack Excel classify / dedup / smoke

- Source pack: `files/Intent_Coverage_and_Candidates.xlsx` + `miner_pack/` candidates/golden harness.
- Built pack pipeline scripts: `pack_v2_pipeline.py`, `v2_intent_folders.py`, docs `PACK_V2_REGISTER_PIPELINE.md`.
- Classified ~372 candidates → already registered / same-host / same-publisher / needs key / smoke.
- Dedup notes: `out/PACK_REMAINING_AFTER_DEDUP.md`, `out/PACK_VS_REGISTERED.md`.
- Part of pack registered earlier without LLM gas unlock on V2 (later gates tightened).

### 2026-10-05 — Golden + Ollama auto_review + Pack V2 register (61)

- Ran `miner_pack/run_golden_tests.py` live → ~176 golden PASS rows; after strict dedup → **93 NEW** with samples (`out/PACK_GOLDEN_NEW.json`).
- Auto_review+LLM gate made **mandatory** for V2 gas (`register_gates_v2.py` re-runs review; `set_sample_status.py approved` alone ≠ gas).
- Cloud LLM failed: OpenAI **no credits / 429**; OmniRoute chat **502/disk full** on host.
- Installed **Ollama** locally (`qwen2.5:3b`); wired `auto_review_samples.py` OpenAI-compatible judge (`OLLAMA_BASE_URL`, prefer Ollama, disable OpenAI preference).
- Judge fixes: truncated CEX books (`bids` without `asks`); require `verdict` JSON extract (3B models echoed API JSON); catalog aliases `GAS_PRICE_ESTIMATION`→`GAS_PRICE`, `CRYPTO_PRICE_LOOKUP`→`CRYPTO_PRICE` for on-chain intents.
- JSON-RPC live probe: GET 400 → POST `eth_blockNumber` fallback in `register_gates_v2.py`.
- LLM+golden registerable: **66**; registered via `register_approved_v2_batch.py` / `register-miner-v2.sh`: **61 PASS**, **5 FAIL** gates:
  - `filing-sec-atom` SEC **403**; `macro-bls` golden FAIL; `route-cow` **405** (needs POST); `val-beacon-chainsafe` / `xchain-beacon-lodestar` **429**.
- Hosting: Dropbox token empty; omni-chat YAML sync often unavailable → **paste.rs** with retries (rate limits).
- Rewrote `MinerCreator/newlyRegisteredMiners.md` to **only Pack 61** (removed old bag already on sheet).
- Added Class column (DETERMINISTIC / HYBRID / NON-DETERMINISTIC) to sheet tables + `out/ACTIVE_PREACTIVE_MINERS.xlsx`.
- Omni host SSH **port 22 timeout** from laptop (HTTPS still 200) — wrote `scripts/safe_omni_disk_cleanup.sh` but could not run cleanup until SG opens SSH.
- Stopped local Ollama after EOD (not needed for live miner answers).

### 2026-10-06 — Pre-active bucket removed; all → Active in docs

- User ask: promote Pre-active → Active; no Pre-active column anymore.
- Merged Pre-active tables (NON-DET 13 + Semantic V2 63 + Pack 61, deduped) into Active in `INTENT_BUILD_SHEET-2026-09-23.md`.
- Sheet totals: **Active 289 miners · 56 intents**; Pre-active section removed; lifecycle **Active → Not registered → Dead**.
- Excel `out/ACTIVE_PREACTIVE_MINERS.xlsx`: dropped **Status** and Pre-active columns; **289** Active rows; Class kept.
- `newlyRegisteredMiners.md` wording → Active (promoted pack).

### 2026-10-06 (later) — Path to 1000 + Omni cohort audit + SSH restored

- Goal pressure: register toward **1000** miners under current V2 gates; prefer DET/HYBRID; skip NON-DET pad for this push.
- Honest math: Active **289** → need ~**711** more; pack DET keyless remaining ~**67** + free-key DET ~**40–70** ⇒ **cannot** hit 1000 from current pack alone without new research (Ahmed rule intact).
- Ranked next Wave 1 DET candidates (CEX/DNS/on-chain/FX/grid/corp/etc.) from `PACK_REMAINING_AFTER_DEDUP.md` / pending_review samples — exclude already registered + LLM-rejected + CORS extractors + Open-Meteo variants.
- Rechecked **Omni ~1400** cohort for V2 salvage:
  - `out/registry.jsonl`: **647** `omni-*` chat models (one publisher); **278** `host_fetch_failed`; live node has **0** `omni-*` slugs.
  - `out/response-registry.jsonl`: **312** OmniRoute response miners (same publisher).
  - Live node `/api/miners`: **1896** active; ~**1581** slugs not in our `intentYamls`; many clones / `WRONG_QUANTITY` / junk hubs (ngrok/vercel/onrender mega-miners).
  - Verdict: V2 can **sieve** salvage (~**50–150** DET/HYBRID realistic); **not** reclaim 1400 as inventory. Same-publisher Omni chat bag ≤1 for ranking.
- Omni SSH worked again: `ssh -i telegraphNode1.pem ubuntu@13.237.89.59` → disk **38%** (73G/194G), `/var/www/miner-yamls` **280** files, `http://127.0.0.1:8765/health` → `semantic-truth-proxy` **ok**.
- Documented remote auto_review judge: any OpenAI-compatible `POST …/v1/chat/completions` via `BASE_URL`+`OMNIROUTE_API_KEY`+`AUTO_REVIEW_PREFER_OMNI=1` (or `OLLAMA_BASE_URL` for keyless Ollama-compatible hosts). Judge only scores **captured samples**, not live miner traffic.

### 2026-10-07 — Usman: AIR_QUALITY_INDEX still `diff-question`

- Usman Discord (21:25): AQI miners answer **different regions** under the same param name `site` — DE station / NL station / Singapore / sensor ID / lat,lon / city — so one shared ask is impossible → **not rankable**.
- Confirmed against our YAMLs (`intentYamls/air-quality/aqi-*.yaml`): all use `venue`+`site` with different defaults (e.g. `aqi-uba` `DEBE034`, `aqi-openmeteo` `52.52,13.41`).
- Matches his 2026-09-26 review row: `AIR_QUALITY_INDEX` = **`diff-question`**.
- Decision locked: LLM-normalize **cannot** fix different questions; need **one shared pin** (propose Berlin `52.52,13.41` + PM2.5) and keep only miners that can answer that place; regional-only sources stay out of rank set.
- Same pattern still applies to other `diff-question` intents in Usman’s review (loan, yield, weather forecast, route, etc.).

---

## 3. SOLUTIONS

| Decision | Why | Alternatives rejected |
|----------|-----|------------------------|
| **One miner = one upstream** | Usman ranks sources against each other; clones can’t be ranked honestly | Keep multi-clone Omni bag as “coverage” |
| **Ahmed: fewer correct > pad to 10** | Catalog “Scale to 10+” caused WRONG_QUANTITY / fake sources | Force 10 APIs per intent |
| **Lifecycle: Active / Pre-active / Not registered / Dead** | Separates Usman approval from “we found zero APIs” | Only registered vs not |
| → **Status 2026-10-06:** docs dropped **Pre-active**; registered miners = Active in sheet/Excel. Scoring “wired vs not” still separate. | Lifecycle clarity for CEO/docs | Keep Pre-active forever |
| **Usman packs live only in `newlyRegisteredMiners.md` until approved** | Don’t pollute `workingMiners.md` / Active sheet early | Update all three docs on every register |
| → **Status 2026-10-06:** Pack V2 pack lives in `newlyRegisteredMiners.md` + merged into sheet Active; `workingMiners.md` still wired-keepers-only. | | |
| **Date separator rows in Active** (`—— YYYY-MM-DD ——`) | See which promotions landed which day | Flat Active list |
| **Fable portable pack** (`fable-handler/`) | Offline research on another PC with full doctrine + sheet | Ad-hoc chat prompts |
| **Honest Dead when 0 sources** | Zero APIs is a valid research answer | Leave forever in “Not registered” |
| **Do not count Omni ~1400 in inventory** | Different method; many wrong quantity / clones | Inflate Active with mass regs |
| **Fail-closed `register-miner.sh`** | Sep 28 Groups A–D: Validate green ≠ Usman-scorable | Manual selftest then raw `cast send` |
| **Ban batch register scripts for intent miners** | `register-bag20.sh` / `register-batch*.sh` bypass gates | Fast gas path |
| **`TEXT_INTENTS` for NON-DET** | Adapter path needs text/`audio_b64`, not RelTol scalar | Force NON-DET into RelTol |
| **Shared pins across venues** | Same question → rank engines, not different questions | Per-miner free-form queries |
| → **Status 2026-10-07:** Usman reconfirmed — same param name with different meanings (`AIR_QUALITY_INDEX` `site`) = **`diff-question`**, not rankable; LLM parse of outputs does not fix it. | | |
| **Proxy `/truth/*` venues** | One host URL pattern; YAML points at venue param | Each YAML hits raw third-party only |
| **Promote bag → Active only after Usman verify** | Pre-active was explicitly “awaiting Usman” | Auto-Active on register |
| → **Status 2026-10-06:** team promoted **all** Pre-active rows to Active in **docs** (sheet/Excel); does **not** mean every intent is comparator/WASM-wired. | | |
| **NON-DET stay Pre-active until adapter wire** | Haider/Usman semantic path not fully wired for these yet | Mark Active because HTTP 200 |
| → **Status 2026-10-06:** lifecycle Pre-active removed; NON-DET listed Active in docs; **adapter wire still open** (see blockers). | | |
| **Semantic V2 `register-miner-v2.sh`** | Format-agnostic; Usman LLM-normalize; no RelTol milli gate on V2 | Force all new miners through RelTol only |
| **auto_review+LLM mandatory before V2 gas** | Manual `set_sample_status approved` was bypassing quality | Heuristics-only approve |
| **Local Ollama as auto_review judge** | OpenAI quota empty; OmniRoute LLM disk/502 | Block register until cloud credits |
| → **Status 2026-10-06:** Omni disk recovered (~38%); can prefer OmniRoute or any OpenAI-compatible remote `/v1/chat/completions` via `BASE_URL` + `OMNIROUTE_API_KEY` + `AUTO_REVIEW_PREFER_OMNI=1`. Ollama still valid local fallback. | | |
| **Omni ~1400 = sieve not inventory** | Mass Validate-green / clones / one-publisher chat | Count as gated Active without V2+distinct-source pass |
| **paste.rs YAML host fallback** | Omni disk full + empty Dropbox token | Fail register when omni sync fails |
| → **Status 2026-10-06:** Omni disk OK + 280 hosted YAMLs; paste.rs still used for many V2/Pack rows; Dropbox token still empty. | | |
| **Catalog → on-chain intent aliases** (`v2_intent_folders.py`) | Diamond rejects `GAS_PRICE_ESTIMATION` / `CRYPTO_PRICE_LOOKUP` | Register with catalog names as-is |
| **Class column (DET/HYBRID/NON-DET)** on sheet + Excel | CEO/Usman inventory readability | Class only in narrative intent detail |

---

## 4. PROBLEMS

| Problem | Manifestation | Resolution |
|---------|---------------|------------|
| Same-source clones | Ranking meaningless | Deregister extras; keep one per source |
| Intent sheet stale / wrong subtotals | e.g. “74 left” when 55 listed | Recount; Fable appendix with exact name list |
| `CODE_REVIEW` / pure judgment | No scalar GT | Mark Dead / Gate 0 until adapter |
| YAML syntax / flow-map / `{type: string…}` false+ | Group A yield miners | Tighten `validate_miner_yaml.py`; fix YAMLs; re-register |
| Self-truth / dated rates | Looks correct but ORACLE / wrong pin | Pin explicit dates; don’t echo GT source |
| `event-kalshi-result` | Proxy **502** wrapping **HTTP 404** | Re-pin Kalshi market that exists (reg **4364** path) |
| `yld-compound` dead upstream | 502 / missing pool | Replace / re-register (**4375** in notes); later some yield IDs deregistered live |
| Vessel MMSI with no AIS | `digitraffic: no recent position for mmsi 354540000` | Re-pin live MMSI `230981000` |
| VULN Group D WRONG_QUANTITY | HTTP 200 HTML/listings, not CVSS | Require `cvss_base` (or equivalent) in selftest/preflight; don’t treat 200 as success |
| “not given the exact output” | Validate green, scorer empty/wrong | Teach: field + scale + quantity + pin |
| Chat selftest `len < 2` on `"4"` | Fail NON-DET text gate | Longer pin + `min_len=1` for `CHATBOT_CONVERSATION` |
| Pollinations **402** | Intermittent LLM venue flake | Keep alternate venues; don’t rely on one paid/flake host |
| List API pagination ~100 | Inflated/deflated live counts | ID probe for new-method inventory |
| Live deregisters (yield 4356–4361 / 4375) | Node `deregistered` while docs said live | Prefer node probe over docs for “live active” |
| README still points at missing `MINERS.md` | Stale Omni-era README | Use `newlyRegisteredMiners.md` + `out/registry.json(l)` |
| Context overflow mid-INTENT_BUILD_SHEET edit | Promo incomplete once | Finished Active/Pre-active/Dead + detail badges 2026-09-30 |
| OpenAI auto_review 429 / no credits | `HTTP 429` insufficient_quota on `api.openai.com` | Prefer Ollama (`qwen2.5:3b`); set `AUTO_REVIEW_PREFER_OPENAI=0` |
| OmniRoute LLM / host disk 100% | Chat completions 502; YAML sync unreliable | Local Ollama for review; paste.rs for V2 YAML host; keep nginx+`miner-yamls`+`/truth` |
| Manual sample approve unlocked V2 gas | `set_sample_status approved` without LLM | `register_gates_v2` requires `auto_review` + `llm_used=true` |
| Small Ollama model echoed API JSON | Judge returned tx JSON, no `verdict` | `_extract_judge_json` requires `verdict`; truncate prompt; optional `response_format` |
| Truncated CEX order books in samples | Heuristic rejected Coinbase book (no `"asks"` in 20k cut) | Treat large `"bids"` + book URL as depth; re-capture later if needed |
| On-chain `unsupported intent` | `GAS_PRICE_ESTIMATION` / `CRYPTO_PRICE_LOOKUP` | Canonicalize via `v2_intent_folders.canonical_intent` in YAML gen + `register-miner-v2.sh` |
| Arbitrum/Base/Optimism RPC live probe GET 400 | Gate failed after approve | POST `eth_blockNumber` fallback when sample looks JSON-RPC |
| paste.rs rate limits | Host step fail mid-batch | Retries + sleep; host-retry pass registered remaining 8 |
| Pack register gate fails (5 left) | SEC 403, golden FAIL, 405 POST, 429×2 | Left unregistered; listed in `newlyRegisteredMiners.md` notes |
| Omni SSH timeout port 22 | `ssh: Operation timed out` while HTTPS 200 | **Resolved 2026-10-06:** SSH works; disk **38%**; cleanup optional now (not urgent) |
| Repo-root vs MinerCreator `newlyRegisteredMiners.md` | Root file still shows old **107** BAG summary | Use **`MinerCreator/newlyRegisteredMiners.md`** for Pack 61 |
| Omni ~1400 / node 1896 “free” inventory | Tempting to count toward 1000 | Audited 2026-10-06: mostly clones / wrong quantity / one-publisher chat; V2 sieve only (~50–150 realistic) |
| `AIR_QUALITY_INDEX` 7 miners not rankable | Same `site` param, different places/ID types (Usman Discord 2026-10-06) | **Open:** lock shared pin (propose Berlin lat,lon); keep only miners that cover it; re-pin/re-register |

**Unresolved / partial:** see §5.

---

## 5. CURRENT BLOCKERS

1. **Shared-pin / `diff-question` (Usman)** — `AIR_QUALITY_INDEX` (and other Sep-26 `diff-question` intents) not rankable until one shared ask; LLM-normalize does not fix different questions. AQI: lock pin + remap/drop regional-only miners.
2. **Usman/Haider scoring wire** — sheet **Active 289** ≠ wired in comparator/adapter/WASM. Docs Active ≠ ranked.
3. **Path to 1000 under doctrine** — pack leftovers + keys ≈ **~120–150** more DET max; need **new distinct-source research**, not Omni mass / NON-DET pad.
4. **5 Pack candidates still unregistered** — `filing-sec-atom` (SEC 403), `macro-bls` (golden FAIL), `route-cow` (405 POST), `val-beacon-chainsafe` / `xchain-beacon-lodestar` (429).
5. **YAML hosting** — Dropbox token empty; many V2/Pack on paste.rs; omni host healthy but sync process still informal.
6. **`workingMiners.md` ~39 keepers** — not aligned to full Active 289; sheet/Excel are count SoT.
7. **Omni mass / node extras policy** — audit done (sieve, don’t count); deregister/quarantine decision still open.
8. **Dead pool (~46)** — no re-hunt without new keys/evidence.
9. **OpenAI credits** — still empty; use Ollama and/or OmniRoute / remote OpenAI-compatible judge.

---

## 6. CODEBASE MAP

*Verified on disk 2026-10-07 (diffed vs 2026-10-06 map).*

### Repo root (`TeleGraph/`)

| Path | Role |
|------|------|
| `MinerCreator/` | Intent miners, gates, docs, YAMLs, registration artifacts |
| `Telegraph/` | Go node: scoring, WASM, API, contracts |
| `OmniRoute/` | Omni chat router (mass model miners; separate cohort) |
| `tg-miner-integration/` | Next.js integrate/register wizard |
| `alexandria/` | UI / ask tooling |
| `public-apis-master/` | Public API catalog reference |
| `files/Intent_Coverage_and_Candidates.xlsx` | Pack coverage + candidates (Oct pack pipeline) |
| `files/run_golden_tests.py` / `files/KEYS_NEEDED.md` | Pack helpers / keyless notes |
| `miner_pack/` | Pack candidates JSON + `run_golden_tests.py` + `results/` |
| `UsmanRsponse/` | Usman scoring contract / fitness / fail sheets (`USMAN_REVIEW-2026-09-26.md` has `diff-question` table) |
| `yamls/` | Misc YAML tree (separate from MinerCreator intentYamls) |
| `telegraphNode1.pem` | Omni EC2 SSH key (`ubuntu@13.237.89.59`) — never commit secrets elsewhere |
| `newlyRegisteredMiners.md` (repo root) | **Stale** old 107 BAG summary — do not use for Pack 61 |
| `.cursor/rules/miner-register-gates.mdc` | Fail-closed register rule (legacy + **V2**) |

*Removed from disk since 2026-09-30 map:* root `Intent Catalog v2 25-Sept (1).xlsx`, `MinerCreator/fable-handler/`, `USMAN_NONDET_*.md`, `ROUND2_PREACTIVE-2026-09-25.md` (content superseded by sheet / `UsmanRsponse/` / timeline).

### `MinerCreator/` docs & data

| Path | Role |
|------|------|
| `PROJECT_CONTEXT.md` | **This handoff** |
| `MINER_BUILD_PLAN-2026-09-23.md` | Gates 0–8 doctrine (canonical) |
| `SEMANTIC_REGISTER_V2.md` | Semantic V2 doctrine (answer-correct / format-agnostic) |
| `PACK_V2_REGISTER_PIPELINE.md` | Pack → V2 register tracker |
| `INTENT_BUILD_SHEET-2026-09-23.md` | Lifecycle + Active miner tables (**289** / 56; Pre-active removed 2026-10-06) |
| `newlyRegisteredMiners.md` | Pack Semantic V2 **61** (promoted Active in docs); not the repo-root old 107 file |
| `workingMiners.md` | Wired keepers subset (~39) |
| `README.md` | Register pipeline (stale MINERS.md link still) |
| `.env` / `.env.example` | Keys/RPC/Diamond + auto_review LLM prefs (secrets by name only) |
| `intentYamls/` | **56** intent dirs, **327** YAMLs (verified 2026-10-07) |
| `intentYamls/air-quality/` | **7** AQI YAMLs — Usman flagged **`diff-question`** (shared pin needed) |
| `apiOutputSamples/` | V2 captured samples + front-matter review status |
| `additions/` | Extra research JSON (e.g. `v2_endpoints_research.json`) |
| `archive/` | Legacy batch register scripts, etc. |
| `templates/` | YAML templates |
| `out/` | Pack/V2 register reports, `ACTIVE_PREACTIVE_MINERS.xlsx`, golden/register logs, `registry.jsonl` (Omni chat regs) |
| `client-demo-miners/` | Demo batches |

### `MinerCreator/scripts/` (critical)

| Script | Role |
|--------|------|
| **`register-miner.sh`** | Legacy RelTol fail-closed register |
| **`register_gates.py`** | Legacy gates 1–4 |
| **`register-miner-v2.sh`** | **Semantic V2** register (auto_review+LLM + golden-if-any + yaml + live + byte-match) |
| **`register_gates_v2.py`** | V2 gate orchestration |
| `auto_review_samples.py` | Hard/heuristic/LLM judge (Ollama / OmniRoute `BASE_URL` / OpenAI — OpenAI-compatible `/v1/chat/completions`) |
| `capture_api_output.py` | Write `apiOutputSamples/*.md` |
| `generate_yamls_from_approved_samples.py` | Sample → YAML (canonical intents) |
| `register_approved_v2_batch.py` | Batch host + `register-miner-v2.sh` |
| `pack_v2_pipeline.py` / `pack_post_golden_registerable.py` | Pack classify/smoke/capture/review; post-golden registerable list |
| `v2_golden_gate.py` / `v2_intent_folders.py` | Golden suite gate; catalog→canonical intent map |
| `smoke_v2_endpoints.py` | Endpoint smoke helper |
| `set_sample_status.py` | Manual status (**does not** unlock V2 gas alone) |
| `create_miner_v2.sh` | V2 create helper |
| `validate_miner_yaml.py` | YAML parse/shape |
| `preflight_miner.py` | Groups A–D + TEXT_INTENTS (legacy) |
| `miner_selftest.py` | RelTol **or** NON-DET text/`audio_b64` (legacy) |
| `local_validate_keepers.py` | Keeper suite / `--from-yaml` |
| `semantic-truth-proxy.py` | `/truth/*` adapters |
| `upload-host.sh` | Host YAML (omni / Dropbox / paste.rs) |
| `safe_omni_disk_cleanup.sh` | **Safe** server disk cleanup (keep nginx/yamls/truth) |
| `create-miner.sh` / `generate-yaml.sh` | Host/generate helpers |
| Archived batch scripts | Under `archive/` — do not run (bypass gates) |

### NON-DET campaign YAML folders

| Folder | Campaign slugs (registered) |
|--------|-----------------------------|
| `intentYamls/language-translation/` | `tr-mymemory`, `tr-google`, `tr-hf-opus`, `tr-pollinations` |
| `intentYamls/text-summarization/` | `sum-hf-bart`, `sum-hf-pegasus`, `sum-hf-distilbart`, `sum-pollinations` |
| `intentYamls/chatbot-conversation/` | `chat-pollinations`, `chat-aihorde`, `chat-nova` |
| `intentYamls/text-to-speech/` | `tts-google`, `tts-espeak` |

### `Telegraph/` scoring (Usman/Haider side)

| Path | Role |
|------|------|
| `Telegraph/pkg/scoring/` | Epoch scoring, hybrid scorer, GT store |
| `Telegraph/pkg/scoring/comparator/` | Per-intent RelTol/PassFail |
| `Telegraph/pkg/scoring/hybrid_scorer.go` | Hybrid / adapter path |
| `Telegraph/pkg/wasm/` | Deterministic + hybrid WASM runtime |
| `Telegraph/documentation/PROJECT_CONTEXT.md` | Node architecture handoff (different doc) |

---

## 7. TASKS DONE

- [x] Intent catalog → `INTENT_BUILD_SHEET-2026-09-23.md`
- [x] Same-source cleanup doctrine applied
- [x] Lifecycle buckets Active / Pre-active / Not registered / Dead *(Pre-active later removed 2026-10-06 in docs)*
- [x] CODE_PATCH_VERIFY (3), CROSS_CHAIN + commerce waves, BAG20, Batch 5/6/7 campaigns
- [x] Fable research pack + consume Fable API sources
- [x] Groups A–D fixes (YAML, Kalshi, Compound, vessel pin, CVSS quantity rules)
- [x] Fail-closed auto register pipeline (`register-miner.sh` + gates + Cursor rule)
- [x] `TEXT_INTENTS` for NON-DET in selftest/preflight/keepers `--from-yaml`
- [x] NON-DET campaign: 13 miners registered (4383–4404 set) with shared pins + proxy routes
- [x] Usman pack docs: `USMAN_NONDET_*.md`
- [x] Promote verified bag (96 / 32) Pre-active → Active (2026-09-30)
- [x] Flip 4 rescued NON-DET Dead → Pre-active in sheet + detail badges
- [x] CEO inventory + “exact output” + Haider semantic-path explanations drafted
- [x] This `PROJECT_CONTEXT.md` handoff (2026-09-30)
- [x] Semantic Register V2 path (`SEMANTIC_REGISTER_V2.md`, capture/auto_review/generate/register-v2)
- [x] Harden V2: auto_review+LLM mandatory; manual approve ≠ gas
- [x] Pack golden + dedup + Ollama auto_review
- [x] Pack V2 register **61** miners (fail-closed); document 5 remaining fails
- [x] Class column on sheet + `ACTIVE_PREACTIVE_MINERS.xlsx`
- [x] Promote all Pre-active → Active in sheet/Excel; remove Pre-active columns (2026-10-06)
- [x] Rewrite `MinerCreator/newlyRegisteredMiners.md` to Pack 61 only
- [x] Omni SSH restored + host health check (disk 38%, 280 yamls, truth proxy ok) — 2026-10-06
- [x] Path-to-1000 honesty analysis + Wave 1 DET candidate shortlist (chat; not yet registered)
- [x] Omni ~1400 / node 1896 salvage audit (sieve ~50–150; do not count mass as gated Active)
- [x] Document remote OpenAI-compatible auto_review judge env (`BASE_URL` / `OMNIROUTE_*` / `OLLAMA_*`)

---

## 8. TASKS REMAINING (priority)

1. **Fix `AIR_QUALITY_INDEX` shared pin** with Usman (propose Berlin `52.52,13.41` + PM2.5); remap/drop miners that cannot answer that place; re-pin/re-register keepers.
2. **Audit other `diff-question` intents** from `UsmanRsponse/USMAN_REVIEW-2026-09-26.md` (loan, yield, weather forecast, route, etc.) — same shared-pin doctrine before more registers.
3. **Usman/Haider:** wire scoring for NON-DET + V2/pack Active that are docs-Active but not ranked.
4. **Register Wave 1 DET** from pack remaining (keyless distinct sources) via V2 auto_review+LLM — only after pin semantics OK for that intent.
5. **New source research** toward 1000 (doctrine-safe); do not pad with Omni mass / clones / NON-DET unless Usman asks.
6. **Finish or drop 5 pack fails** — SEC UA/403, BLS golden, CoW POST, Lodestar 429.
7. **Stable YAML hosting** — Dropbox token or formal omni sync; reduce paste.rs.
8. **Probe live node** vs sheet Active 289; align/label `workingMiners.md`; fix README `MINERS.md` pointer.
9. **Decide Omni mass policy** (deregister / quarantine / leave) given sieve audit; Dead reopen only with new evidence.
10. **Optional:** run `safe_omni_disk_cleanup.sh` on Omni (disk already OK); archive root `newlyRegisteredMiners.md` (old 107).

---


## 9. DELIVERABLES

### Docs (paths)

| Deliverable | Path |
|-------------|------|
| Handoff | `MinerCreator/PROJECT_CONTEXT.md` |
| Doctrine | `MinerCreator/MINER_BUILD_PLAN-2026-09-23.md` |
| Lifecycle sheet | `MinerCreator/INTENT_BUILD_SHEET-2026-09-23.md` |
| Pack Active list (61) | `MinerCreator/newlyRegisteredMiners.md` |
| Keepers | `MinerCreator/workingMiners.md` |
| Semantic V2 doctrine | `MinerCreator/SEMANTIC_REGISTER_V2.md` |
| Pack V2 pipeline tracker | `MinerCreator/PACK_V2_REGISTER_PIPELINE.md` |
| Usman scoring authority | `UsmanRsponse/` (contract / fitness / fail sheets) |
| Cursor gate rule | `.cursor/rules/miner-register-gates.mdc` |
| Register audits | `MinerCreator/out/*-register.json(l)`, `out/last-registration.json` |
| Excel inventory | `MinerCreator/out/ACTIVE_PREACTIVE_MINERS.xlsx` (Active-only + Class; filename historical) |

### Hosted / on-chain

| Item | Link / ID |
|------|-----------|
| YAML host (legacy Active) | `https://omni-chat.13.237.89.59.sslip.io/miner-yamls/<slug>.yaml` |
| YAML host (many V2/Pack) | paste.rs URLs recorded per row in register jsonl / `newlyRegisteredMiners.md` |
| Truth proxy | `https://omni-chat.13.237.89.59.sslip.io/truth/{translate,summarize,chat,tts,…}` |
| Diamond | `0x5a2324aA18613FAD4e44bDF0d6c73Ec1f6D87ff8` (Base Sepolia) |
| NON-DET reg IDs | 4383, 4384, 4388, 4389, 4391, 4392, 4393, 4395, 4399, 4401, 4402, 4403, 4404 |
| Integrate UI | `https://integrate.telegraphprotocol.com/register?mode=create` |
| Node miner lookup | `https://devnode.telegraphprotocol.com/api/miners/<REG_ID>` |

### Oct 2–6 pack / V2 artifacts (append)

| Artifact | Path |
|----------|------|
| Pack register report | `MinerCreator/out/PACK_V2_REGISTER.md` (+ `_COMBINED.md`, `.jsonl`, `.log`) |
| Pack golden NEW | `MinerCreator/out/PACK_GOLDEN_NEW.json` |
| Pack registerable | `MinerCreator/out/PACK_REGISTERABLE.md`, `PACK_REGISTERABLE_SLUGS.txt` |
| Dedup notes | `MinerCreator/out/PACK_REMAINING_AFTER_DEDUP.md`, `PACK_VS_REGISTERED.md` |
| Ollama review logs | `MinerCreator/out/PACK_OLLAMA_REVIEW.log`, `PACK_OLLAMA_REVIEW2.log` |
| Earlier V2 batch | `MinerCreator/out/V2_REGISTER_BATCH.md` / `.jsonl` / `V2_REGISTER_BATCH-2026-10-05.log` |
| Pack source Excel | `files/Intent_Coverage_and_Candidates.xlsx` |
| Pack candidates | `miner_pack/` |
| Omni chat register log | `MinerCreator/out/registry.jsonl` (**647** `omni-*`) |
| Omni response register log | `MinerCreator/out/response-registry.jsonl` (**312**) |
| Usman `diff-question` table | `UsmanRsponse/USMAN_REVIEW-2026-09-26.md` (includes AQI) |

### Oct 6–7 analysis / ops (append)

| Item | Note |
|------|------|
| Omni SSH | `ssh -i telegraphNode1.pem ubuntu@13.237.89.59` — restored 2026-10-06 |
| Omni host check | disk **38%**; `/var/www/miner-yamls` **280**; truth proxy health **ok** |
| Live node snapshot | `https://devnode.telegraphprotocol.com/api/miners` → **1896** active (2026-10-06 probe) |
| Path-to-1000 / Wave 1 / Omni sieve | Session analysis in chat transcript `9e012a38-5259-4212-8f67-b90fe0e2d5ca` (no separate PR) |
| Usman AQI Discord | 2026-10-06 21:25 — shared `site` ≠ shared question |

### Git / PR

- Workspace git state at handoff time: **not a clean single-branch PR workflow** for this campaign (local docs + YAMLs; `git` at repo root returned non-zero in probe). Treat markdown/YAML on disk as source of truth unless a remote PR is created later.
- Do **not** invent commit SHAs here.

### Inventory snapshot (docs, 2026-09-30) — historical

| Bucket | Intents | Miners |
|--------|--------:|-------:|
| Active | 49 | 153 |
| Pre-active (NON-DET) | 4 | 13 |
| Not registered | 0 | 0 |
| Dead | 46 | 0 |
| **Registered coverage** | **53** | **166** |

### Inventory snapshot (docs, 2026-10-06) — still current 2026-10-07

| Bucket | Intents | Miners |
|--------|--------:|-------:|
| Active (sheet/Excel) | 56 | 289 |
| Pre-active | — | removed from docs |
| Not registered | 0 | 0 |
| Dead | ~46 | 0 |
| Pack V2 registered (this wave) | (in Active) | **61** PASS / **5** gate FAIL left |
| Live node (probe 2026-10-06) | many intents | **1896** active (includes non-gated mass) |

---

## 10. SETUP TO RESUME

```bash
cd /Users/mrmacbook/Documents/TeleGraph/MinerCreator
cp .env.example .env   # if missing
# Fill (names only — never commit values):
#   MINER_PRIVATE_KEY, FEE_ADDRESS, OMNIROUTE_API_KEY (and/or OPENAI_API_KEY for V2)
#   DIAMOND, RPC_URL, NODE_URL, INTERNAL_SECRET
#   BASE_URL, HOST_PREFIX_CHAT, HOST_PREFIX_RESP
# Optional host: DROPBOX_ACCESS_TOKEN, ALLOW_PASTE_FALLBACK
#
# V2 auto_review judge — pick ONE primary:
# (A) Local Ollama:
#   OLLAMA_BASE_URL=http://127.0.0.1:11434
#   OLLAMA_REVIEW_MODEL=qwen2.5:3b
#   AUTO_REVIEW_PREFER_OLLAMA=1
# (B) OmniRoute or any OpenAI-compatible server LLM:
#   AUTO_REVIEW_PREFER_OMNI=1
#   AUTO_REVIEW_PREFER_OLLAMA=0
#   AUTO_REVIEW_DISABLE_OLLAMA=1
#   BASE_URL=https://<host-with-/v1/chat/completions>
#   OMNIROUTE_API_KEY=<server key>
#   OMNIROUTE_REVIEW_MODEL=<model id>
# (C) OpenAI cloud:
#   AUTO_REVIEW_PREFER_OPENAI=1
#   OPENAI_API_KEY=...
#   OPENAI_REVIEW_MODEL=gpt-4o-mini
# Optional: AUTO_REVIEW_ALLOW_CLOUD_FALLBACK=1
# Never put ALLOW_UNSAFE_REGISTER=1 unless explicit emergency.

chmod +x scripts/*.sh
# Optional local judge: brew/install ollama; ollama pull qwen2.5:3b; ollama serve
# Python 3 stdlib is enough for most gates; proxy deps live on Omni host.

# Legacy RelTol register ONLY via:
./scripts/register-miner.sh \
  --file intentYamls/<intent>/<slug>.yaml \
  --url https://omni-chat.13.237.89.59.sslip.io/miner-yamls/<slug>.yaml

# Semantic V2 / pack register ONLY via:
./scripts/register-miner-v2.sh \
  --file intentYamls/<intent>/<slug>.yaml \
  --url <hosted-yaml-url> \
  --sample apiOutputSamples/<INTENT>/<slug>.md
# or batch: python3 scripts/register_approved_v2_batch.py …

# After register, check node:
curl -s https://devnode.telegraphprotocol.com/api/miners/<REG_ID> \
  | jq '.miner | {slug, activation_status, rejection_reason}'

# Omni EC2 (SSH restored 2026-10-06):
#   ssh -i /Users/mrmacbook/Documents/TeleGraph/telegraphNode1.pem ubuntu@13.237.89.59
# Optional cleanup on box: bash safe_omni_disk_cleanup.sh  # keep nginx, miner-yamls, /truth
```

**Read first (order):**
1. This file  
2. `MINER_BUILD_PLAN-2026-09-23.md` + `SEMANTIC_REGISTER_V2.md`  
3. `UsmanRsponse/MINER_SCORING_CONTRACT.md` (or fitness docs in that folder)  
4. `INTENT_BUILD_SHEET-2026-09-23.md` + `newlyRegisteredMiners.md` (Pack 61)  
5. `.cursor/rules/miner-register-gates.mdc`  
6. `scripts/register_gates_v2.py` + `auto_review_samples.py` (+ legacy `miner_selftest.py` / `semantic-truth-proxy.py`)

**Never:**
- `cast send … registerMiner` / `updateMiner` directly  
- `register-batch*.sh` / `register-bag20.sh` / `register-eight-batch.sh` for intent miners  
- `--skip-gates` / `--skip-auto-review` / `--no-llm` without `ALLOW_UNSAFE_REGISTER=1` and explicit human emergency  
- Treat `set_sample_status.py approved` as gas unlock (V2 re-runs auto_review+LLM)

**Proxy deploy note:** changes to `semantic-truth-proxy.py` must be deployed on the Omni host (nginx → proxy) for `/truth/*` smoke URLs to match local edits. Omni **LLM** stack is optional for miners; **nginx + miner-yamls + `/truth`** must stay.

---

## 11. OPEN QUESTIONS

1. **AQI shared pin:** confirm Berlin `52.52,13.41` (or another place all keepers can hit) + field `pm25_ugm3_x10` with Usman before re-pin?
2. Which other Sep-26 **`diff-question`** intents does Usman want fixed next (loan / yield / weather / route / …)?
3. Has Usman/Haider **confirmed** semantic WASM / LLM-normalize is **live** for NON-DET + V2/pack, or only described?
4. Of sheet **Active 289**, which are **actually comparator-/adapter-wired** vs Active-in-docs-only?
5. Should **`workingMiners.md`** expand toward full Active 289, or stay “wired keepers only”?
6. Omni mass after sieve audit: **deregister**, quarantine, or leave on-chain unused?
7. CEO inventory: **doc 289** vs **live node 1896** — which number to report (gated vs all active)?
8. Any **Dead** intents forced reopen with paid keys?
9. Stable YAML host: Dropbox token vs formal omni sync vs paste.rs?
10. Path to **1000**: approve new research wave size, or accept doctrine-capped inventory below 1000?

*Answered / closed since 2026-10-06:* Omni SSH reachable again (Q7 old); disk no longer full; Omni ~1400 not usable as free 1000 pad (audit).

---



## Appendix A — NON-DET shared pins (copy/paste)

| Intent | Field | Pin |
|--------|-------|-----|
| `LANGUAGE_TRANSLATION` | `translated_text` | `q=The quick brown fox jumps over the lazy dog.` · `source=en` · `target=es` |
| `TEXT_SUMMARIZATION` | `summary_text` | long pangram document `q` (see campaign md) |
| `CHATBOT_CONVERSATION` | `reply_text` | `q=What is 2+2? Reply in one short full sentence.` |
| `TEXT_TO_SPEECH` | `audio_b64` | `q=The quick brown fox` · `lang=en` |

## Appendix B — “Not given the exact output” (team wording)

Validate green / HTTP 200 ≠ Usman-scorable. Scorer needs the **exact quantity**, in the **exact field**, at the **exact scale**, for the **exact pin**. Failure modes: WRONG_QUANTITY, wrong shape vs `label_field`, wrong scale, NOT_ASKABLE. For NON-DET, there is also **no single exact answer** — semantic/LLM path required.


---

## 12. Semantic Register V2 (2026-10-02+) — Ahmed / Usman LLM-normalize path

**Doctrine:** `SEMANTIC_REGISTER_V2.md` · pack tracker `PACK_V2_REGISTER_PIPELINE.md`  
**Sample store:** `apiOutputSamples/<INTENT>/<slug>.md`  
**Flow (hardened 2026-10-05):**  
`capture_api_output.py` → `auto_review_samples.py` (**hard + heuristic + LLM**; Ollama preferred locally) → golden suite if `files/candidates` / pack defines slug → `generate_yamls_from_approved_samples.py` → host URL → `register-miner-v2.sh` / `register_gates_v2.py` (re-runs review; **manual `set_sample_status approved` alone ≠ gas**).

Kept: one-source, description-correct, YAML parse, hosted byte-match, fail-closed gas, Ahmed fewer-correct.  
New: format-agnostic answers; LLM normalize on Usman/Haider side; auto_review+LLM gate; no RelTol milli-field enforcement on V2 path; catalog→canonical intent aliases.  
Legacy RelTol path remains: `register-miner.sh` + `register_gates.py`.  
Pack wave result: **61** registered, **5** gate fails documented in §4/§5.


## Appendix C — Haider semantic path vs our work

Haider: GT plain English → LLM converts miner output to plain English → semantic WASM ranks 0–1 (schema-flexible).  
**Applies to** NON-DET + Semantic V2 / Pack miners (listed Active in docs 2026-10-06; scoring wire may still be pending).  
**Does not relax** RelTol `label_field`/scale rules for deterministic RelTol-path miners.

---

## Appendix D — Usman required OUTPUT vs old miners vs our automated gates

**Authority folder:** `/Users/mrmacbook/Documents/TeleGraph/UsmanRsponse/`  
Key files: `MINER_SCORING_CONTRACT.md`, `miner-semantic-fitness-2026-09-21.md`, `intent_truth_specs.csv`, `intent_miner_failsheet.csv`, `WrittenText.md`, `USMAN_REVIEW-2026-09-26.md`, `non-working-miners-report-2026-09-26.md`.

### D.1 What Usman needs as “output”

For **deterministic** intents — a value he can **extract and compare** to ground truth on a **pinned question**:

| Need | GRID example (WrittenText + fitness) |
|------|--------------------------------------|
| Correct **quantity** | LMP USD/MWh — not gCO₂ / fuel mix / MW |
| **Askable** pins | CAISO + node `TH_NP15_GEN-APND` + DAM + hour |
| Extractable via YAML mapping | `.lmp_usd_per_mwh_milli` (×1000) → ~`38095` |
| Correct **scale** | Wrong scale → score ~0 (looks like wrong answer) |
| **Same question**, distinct sources to rank | One source → all 1.0 ties |

Usman (WrittenText Discord): agnostic to JSON **shape** (each YAML maps its own keys) — **not** agnostic to whether the answer can be found. No extractable value → not scored.

For **NON-DET**: text/audio a judge/WASM can score 0–1 (no single number GT).

### D.2 What previous miners returned instead (Validate still green)

GRID — all 10 old miners HTTP 200, all FAIL semantics: carbon, fuel mix, FR/DE EUR prices, generation MW, UK region duplicates (WrittenText).  
Elsewhere: wrong field (VULN list/id vs CVSS), YAML parse bugs (`Pool key:`), diff-question pins (yield each pool), ORACLE ties, intents not in catalog.

### D.3 Gates we automated so new miners must pass this (`PROJECT_CONTEXT` § scripts)

`./scripts/register-miner.sh` → `register_gates.py` → only then gas. Rule: `.cursor/rules/miner-register-gates.mdc`.

| # | Script | Blocks |
|---|--------|--------|
| 1 | `validate_miner_yaml.py` | Unparseable YAML |
| 2 | `preflight_miner.py` A–D | Dead upstream; missing `label_field`; non-numeric where number required; wrong VULN field |
| 3 | `miner_selftest.py` | RelTol / range / NON-DET text |
| 4 | `local_validate_keepers.py` | Keeper / from-yaml suite |
| 5 | Hosted YAML byte-compare | Hash ≠ public file |
| 6 | `registerMiner` | Only if all PASS |

Plus: truth proxy, clone cleanup, build sheet.  
V2 parallel: `register-miner-v2.sh` → `register_gates_v2.py` (auto_review+LLM, golden-if-any, live probe, byte-match) — see §12.

### D.4 — why this takes time

1. Old metric was **API alive**; Usman proved that ≠ **scorable answer** (e.g. GRID 0/10).  
2. Each intent needs research + pin + extractable field (+ often proxy) + gates + Usman wiring/coverage.  
3. Ranking needs **≥2 distinct sources on one question** — clones forbidden.  
4. Catalog/alias/comparator wiring is often on Usman’s side after we register.  
5. Gates make each registration slower **on purpose** so we don’t re-pay for mass WRONG_QUANTITY.
