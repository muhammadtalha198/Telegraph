# Miner doctrine + build plan

> **2026-10-02 — registration default changed.**  
> New miner work uses **Semantic Register V2** (answer matches intent description; output format free; LLM normalize on Usman’s side; **manual sample approve** before gas).  
> See **[`SEMANTIC_REGISTER_V2.md`](./SEMANTIC_REGISTER_V2.md)** and `./scripts/register-miner-v2.sh`.  
> This file remains the **RelTol / exact-field** doctrine for the legacy numeric comparator path (`register-miner.sh`). Do not use archived batch scripts under `archive/legacy-batch-register/`.

**Date:** 2026-09-23 (RelTol era; still authoritative for field/scale/pin when on that path)  
**Authority:** Usman's `MINER_SCORING_CONTRACT.md` (Telegraph `feature/v2-integration` @ `9fc0df8`). This supersedes `intent_truth_specs.csv` and `miner-semantic-fitness-2026-09-21.md` wherever they disagree.  
**Supersedes:** `MINER_SEMANTIC_PLAYBOOK.md` (merged into Part I), `newTestingMiners.md` scale plan, `usmanRankableSources-2026-09-23.md` ASSET proposal.  
**Hard rule (Ahmed):** fewer correct miners > many wrong. Callable ≠ correct. Ten near-identical miners is strictly worse than two distinct ones.

**Part I is permanent doctrine** — how to judge any miner, ever.  
**Part II is the current campaign** — what we do now; it expires when the phases are done.  
**Part III is reference data** — the per-intent contract.

---
---

# PART I — DOCTRINE

## 1. Root cause: why ~12 worked and ~1400 did not

We optimised for **`Validate=PASS`** (HTTP 200 + YAML parses + intent tag). Scoring needs **the same physical quantity the catalog describes**, askable with the **pinned question**, mapped to the **comparator field**, from a **distinct source**.

So we registered theme-adjacent free APIs: carbon intensity under "power price", geocoders under "ETA", 24h volume under "wash trading". They all went green and all failed semantics.

Then we made the second mistake: once we had a correct source, we cloned it ten times to hit a miner count. Clones can't rank (§4.5) and they came from following the catalog's own advice (§7.2).

**The blunder was process, both times.** First we measured "the API is alive" instead of "the API answers the intent question". Then we measured "how many miners" instead of "how many sources".

## 2. How scoring actually works

Seven mechanics. Most of our wrong assumptions came from not knowing these.

**2.1 Only nine intents are scored.** `FX_NOW`, `ROUTE_ETA`, `MACRO_ECONOMIC_INDICATOR`, `LIQUIDITY_DEPTH_VERIFY`, `MINING_HASHPRICE_VERIFY`, `GRID_POWER_PRICE`, `LIVE_SHELF_PRICE`, `ONCHAIN_METRIC_VERIFY`, `ASSET_RESERVE_ATTESTATION`. Wired at `pkg/scoring/comparator/comparator.go:294`. Anything else is not scored by this path.

**2.2 Score is mean accuracy only.** `RankedFromPairScores` in `comparator_scorer.go:160`. No latency, uptime, agreement or stake term in the deterministic path. **Operator diversity and fast responses buy nothing.** Only the number matters.

**2.3 Tolerance is the half-score point, not a pass gate.** All nine use `rel_tol`. The curve is 10000 bps at zero error, **5000 at the tolerance**, 0 at twice the tolerance. Ranking happens *inside* the band — in a 30 bps band, 2 bps beats 25 bps. Being "within tolerance" is not the goal; being closest is.

**2.4 Ties break alphabetically by slug.** `comparator_scorer.go:199`. No dedup, no penalty. Miners on one upstream return the same number, tie, and sort by name. That produces an alphabetised list that looks like a ranking, which is worse than an empty leaderboard.

**2.5 An unregistered slug is invisible, not zero.** `coverageByIntent` is a hardcoded per-slug registry checked by `CanServeKey`. A slug Usman hasn't added is **silently skipped**. Absent from the leaderboard does not mean bad miner — it may mean unseen. **Every new slug must be sent to Usman the day it registers.**

**2.6 Scale mismatch scores 0 silently** and is indistinguishable from a wrong answer. Highest-frequency silent failure. A parse failure is likewise skipped rather than zeroed.

**2.7 There is no shared-upstream detection in the code** (§1.7 of the contract). Nothing stops us registering ten clones. The distinct-source rule is **manual and entirely ours to enforce**.

## 3. Fail taxonomy — memorise these codes

Every rejection gets one of these. Distribution across Usman's 150-miner audit in brackets.

| Code | Meaning | Classic bad example |
|---|---|---|
| `WRONG_QUANTITY` **[72, 48%]** | A different physical thing | Carbon gCO2 under GRID; Photon geocode under ROUTE_ETA; h24 volume under WASH |
| `NOT_ASKABLE` **[21, 14%]** | Cannot take the pinned question | Missing `mmsi` / market id / year; latest-only endpoint against a historical pin |
| `ORACLE` **[18, 12%]** | Works, but *is* the truth source → ranking tautology | Google DoH under EMAIL; OSRM under ROUTE_ETA; World Bank under MACRO |
| `OK` **[14, 9%]** | Passes | — |
| `DUPLICATE` **[12, 8%]** | Same upstream, different default or host only | Two carbon regional defaults; eight RPC providers on one chain |
| `NO_JUDGMENT` **[9, 6%]** | Intent needs inference; miner returns raw docs | LLM-eval intents backed by search APIs |
| `WRONG_MARKET` **[4, 3%]** | Right kind of number, wrong market/unit/region | EU EUR/MWh when the pin is CAISO USD LMP |

An earlier, looser audit scored 36 OK out of 150. The criteria have tightened since; use the numbers above.

## 4. The gates — the only allowed creation process

Run in order. Stop at the first failure and record the code.

### Gate YAML — file parse (before host/register)
Run `scripts/validate_miner_yaml.py` on every miner YAML. Catches unquoted scalars that contain `: ` (Group A: `description: Pool key: …` → node `YAML schema validation failed`) and missing `label_field` / `kind` / `slug`. **Wired into** `generate-yaml.sh`, `register-miner.sh`, and `local_validate_keepers.py` (YAML gate runs before endpoint cases). Endpoint PASS alone is not enough.

### Gate Preflight — Groups A–D live quantity (before registerMiner)
Run `scripts/preflight_miner.py --file <yaml>`. After YAML parse: builds the default pin URL, fetches live JSON, and requires `label_field` to be a **number** Usman’s `toNumber` can score (rejects lists/objects/id strings — Group D). Also blocks VULNERABILITY_TRIAGE miners that hit NVD/GHSA/OSV/CIRCL **directly** instead of `/truth/*-cvss` on the omni-chat proxy, and catches dead upstreams / empty live pins (Groups B/C). Re-check yesterday’s fixes anytime with `python3 scripts/preflight_miner.py --regression`.

**Automation:** `./scripts/register-miner.sh --file … --url …` calls `scripts/register_gates.py` first (validate_miner_yaml → preflight → miner_selftest → local_validate --slug). Gas is spent only if every gate PASS. Intent is taken from the YAML when `--intents` is omitted. Use `--skip-keepers` / `--skip-gates` only for emergencies.

### Gate 0 — Intent eligibility
Is the intent one of the nine in §2.1? If not, it is not scored and we do not build for it. Check the catalog `Class` and `Scoring path` too — `comparator only` is the buildable class.

### Gate 1 — Quantity sentence
Write one sentence: *"This miner returns **\<quantity\>** in **\<units\>** for **\<pinned params\>**."* If you cannot fill it from the contract's §3 row, stop.

### Gate 2 — Description check
Read the catalog `description` in `realIntentYamls/<intent>.yaml` and confirm the candidate answers that question. **Necessary but not sufficient** — see §7.1, where three descriptions actively contradict the scored quantity.

### Gate 3 — Dimension check
Write the unit the contract expects (dollars per MWh, satoshis per PH/s per day, Gwei, cents). Write the candidate's unit. If no fixed multiplier converts one into the other, it is `WRONG_QUANTITY`. **"Same topic" is not a unit.** This one test would have killed most of the 1400.

### Gate 4 — Askability across three pins
Every pinned param must be a real request input in `input_schema.required`. Change the pin, get a correspondingly different and correct answer. Watch for: a "latest" flag that overrides an explicit pin, a pin hardcoded into the path, positional retrieval from a list, forecast endpoints that reject historical dates, and **a pinned param carrying a default** — the default silently wins and the miner is `NOT_ASKABLE`.

### Gate 5 — Distinctness
Run the divergence test against every already-registered miner on the intent, across **three** pins. Identical values, or divergence consistently under tolerance/10, means **one source**. Different host, different CDN, v1 vs v2, a mirror, a different TLD, a different default in the slug — all still one source. The question to ask is: *could these two disagree if one of them were wrong?*

### Gate 6 — Oracle check
Zero divergence from truth, on a quantity where §2.5 of the contract expects non-zero divergence, means the candidate is redistributing Usman's own truth source. That is an `ORACLE`: allowed by the code, but it **does not count as a distinct source**. At most one per intent, as a canary, recognisable from its slug.

### Gate 7 — Accuracy and scale
Run `scripts/miner_selftest.py --truth`. Aim far inside the band, not merely inside it. A value 1000× or 1e6× out is a scale bug to fix with `signal_mapping.scale`, not a reason to discard the upstream.

### Gate 8 — Both outcomes (pass_fail intents only)
**Dormant** — `CmpPassFail` is not implemented, so no pass_fail intent is scored today. When Usman wires it: prove you can produce both a true and a false case. If the API always returns "found", do not ship.

**Only then:** host YAML → `run-gates.py` green → Validate → `registerMiner` → send Usman the slug.

## 5. Why Validate lies

Validate checks the YAML schema, an upstream HTTP 200 **on defaults**, and that the intent string is present.

It does not check whether the number is LMP or carbon intensity, whether you can pass the pinned params at all, whether `label_field` matches the comparator field, or whether the scale is right. A green Validate on a default request tells you the server was up. **Shipping on Validate alone is a process bug, not bad luck.**

## 6. What good and bad output look like

Good miner JSON exposes a **scalar the comparator can compare**: `lmp_usd_per_mwh_milli`, `value_gwei`, `price_cents`, `rate_pct`, `eta_seconds`, `attested_reserve`.

Bad, even at HTTP 200: a GeoJSON FeatureCollection, question text or a title, fuel-mix percentages, an always-32e9 constant effective balance, a single aggregator quote labelled "optimal route", an empty `[]`.

**If the scored path is a blob or a constant, it cannot rank.**

One more shape rule: integers and strings survive the round trip, large floats do not. The `ONCHAIN_METRIC_VERIFY` BEACON key exceeds 2^53, so `value_gwei` must be a **truncated integer** carried as an integer or decimal string.

## 7. Catalog pitfalls

The catalog (`Intent Catalog v2 25-Sept (1).xlsx`, 119 intents) is a useful map and a dangerous instruction manual.

### 7.1 The description is broader than the pin, and sometimes contradicts it

**`ROUTE_ETA` is a trap.** The description says *"multimodal routing itineraries, **live traffic** transit times."* The truth engine is OSRM, which uses **static speed profiles and no live traffic**. A genuinely traffic-aware provider returns an ETA 20–50% above OSRM on a congested route — past 2× the 800 bps band — and scores **zero for being more realistic**. The second source here must be another **free-flow** engine (GraphHopper, Valhalla, ORS).

**`LIQUIDITY_DEPTH_VERIFY` — description and code disagree.** Description says *"bid-ask order book depth, cumulative slippage bands"*; the code scores `liquidity_usd_cents`, which is pool TVL. This is Usman's own §8 Q8 and it determines what we go looking for.

**`LIVE_SHELF_PRICE` — description and pin disagree.** Description says *"online merchant catalogs and marketplaces"*; the pin is an Open Food Facts contributed price id. Related to his §8 Q4.

**Three descriptions are broader than the pin**, so a miner can match the description perfectly and still score zero: `MACRO` (covers CPI and central-bank rates; the pin is unemployment), `ONCHAIN` (covers gas, logs and tx state; the pin is native balance), `ASSET` (covers stablecoin backing generally; the pin is one WBTC feed at one block).

**Three match cleanly:** `FX_NOW`, `GRID_POWER_PRICE`, `MINING_HASHPRICE_VERIFY`.

**Rule:** the description tells us which *neighbourhood* to search; the pin and `label_field` decide whether a candidate is right. When they conflict, the pin wins and we raise the conflict with Usman.

### 7.2 The "How to Scale to 10+ Miners Instantly" column is where the clones came from

The catalog has a column with that literal title, and for most of the nine it advises exactly what the distinctness test rejects. We followed it. That is the root cause of the clone waves.

- **`ONCHAIN`** — *"query independent RPC providers and archive nodes to prevent single-provider spoofing."* We did that; all eight operators returned a **byte-identical value** at the pin. RPC providers don't compute the balance, they read the same chain. This advice can never produce a distinct source.
- **`ROUTE_ETA`** — *"different routing engines (TomTom, Mapbox, OSRM)."* Both named alternatives are traffic-aware against a free-flow truth. Scores zero.
- **`GRID`** — *"query independent regional ISOs."* A different ISO is a different node, so a different question. Confuses coverage with distinctness.
- **`FX_NOW`** — *"RapidAPI hosts 40+ FX APIs."* Most resell the same ECB reference rate. Forty endpoints, one source.
- **`LIVE_SHELF_PRICE`** — *"50+ e-commerce scrapers."* Keyed, paid, and unable to answer an Open Food Facts price id.
- **`MINING`** — *"different mempool explorers."* Explorers agree exactly; only a different methodology diverges, and that's a different quantity.

Sound advice on only two: **`MACRO`** (statistical agencies do compile independently — still needs the divergence test, since FRED and World Bank may both republish BLS) and **`LIQUIDITY`** (different subgraphs, pending Q8).

**Rule: the "Scale to 10+" column is not a source of truth and must never be used to generate miners.** Distinctness is decided only by Gate 5.

### 7.3 Scope

Of the 119 intents: 55 are `DETERMINISTIC` / "comparator only", 48 are `HYBRID` / "comparator + adapter", 16 are `NON-DETERMINISTIC` / "adapter only".

**Only 9 of the 55 comparator-only intents are wired.** The other 46 are catalog-ready and unscored — the medium-term backlog. Worth asking Usman which he wires next so our research goes where it counts.

**The catalog independently confirms VULN and EMAIL are not scoreable:** both are `HYBRID` / "comparator + adapter" with `Evaluation Mechanism: None` and `Ranking Supported: False`, matching §7.3 of the contract. Two documents agree, so the Discord "rankable" claim was the error.

Note that every row shows `Miners Integrated: 0.0` and `Status: Not Supported`. Stale columns, but consistent with `coverageByIntent` not containing our slugs.

## 8. Forbidden shortcuts

- Registering because Validate is green.
- Generating miners from the "Scale to 10+" column or any free-API list without a live quantity check.
- Ten variants of one upstream with different defaults, hosts, or letter suffixes.
- Tagging `supported_intents: [X]` onto an unrelated working endpoint.
- Re-registering a deregistered `WRONG_QUANTITY` miner under a new slug.
- Inventing a field that feels "close enough" to the comparator field.
- Building for an intent with no wired comparator.

## 9. Standing rules

- No registration without a green `run-gates.py`.
- One miner per distinct source. Never a letter-suffix clone.
- The slug names the source, because ties sort on it and because it is how both sides tell sources apart.
- Send Usman the slug the day it registers, or it is invisible.
- If an intent honestly supports one source, register one and say so.
- Validate green is not evidence of anything.

---
---

# PART II — CURRENT CAMPAIGN

## 10. Live audit (probed 2026-09-23)

### 10.1 Values that are already exactly right

Our live proxy against his exact pinned questions:

| Intent | Pin | Our value | His expected | Verdict |
|---|---|---|---|---|
| `ASSET_RESERVE_ATTESTATION` | feed `0xa81FE040…`, block `0x18d20a9` | raw `11614464922334` → `116144649223` | `116144649223` | **exact** |
| `MACRO_ECONOMIC_INDICATOR` | USA / `SL.UEM.TOTL.ZS` / 2019 | `3.669` | `3.669` | **exact** |
| `LIVE_SHELF_PRICE` | price_id 1 / 100 / 331088 / 331090 | `2770` / `373` / `523` / `99`, all EUR | same | **exact, all four** |
| `MINING_HASHPRICE_VERIFY` | height 800000 | `233214` | `233214` | **exact** |

Our truth math is correct. The problem was never the numbers — it is the **request contract** and **source duplication**.

### 10.2 Confirmed defects

**ONCHAIN emits a float.** `/truth/eth-balance` returns `value_gwei: 4779587126.345731`. The contract requires `wei // 1e9`, a truncated integer. At the BEACON pin our value is `6.546321870353653e+16`, above 2^53 — the exact case §6 warns breaks parsers. Must emit `65463218703536528` as an integer.

**All 8 RPCs return the identical value at the pin.** drpc, publicnode, 1rpc, merkle, flashbots, mew, blastapi, mevblocker → all `4779587126.345731` at block 23000000. Hard evidence that `ONCHAIN_METRIC_VERIFY` is one source. Send it to him.

**WBTC OpenAPI cannot be pinned to a block.** `openapi.wbtc.network/public/v1/proof-of-reserve` has no block parameter, latest only, so it is `NOT_ASKABLE` against a block pin. **Yesterday's ASSET proposal is withdrawn** unless he re-pins to "latest".

### 10.3 Parameter-name mismatches

His §5.5 `input_schema.required` vs what we registered:

| Intent | He requires | We registered | Action |
|---|---|---|---|
| `GRID_POWER_PRICE` | `node`, `market`, `interval_start_utc` | `node`, `market`, `startdatetime`, `enddatetime` | add `interval_start_utc`; proxy derives the OASIS window |
| `ASSET_RESERVE_ATTESTATION` | `feed_address`, `block` | `feed`, `block`, `rpc` | rename `feed`; `rpc` must not be required |
| `MACRO_ECONOMIC_INDICATOR` | `country`, `indicator`, `year` | `country`, `date` | add `indicator` and `year` |
| `LIQUIDITY_DEPTH_VERIFY` | `network`, `pool_address` | `network`, `address` | rename `address` |
| `ONCHAIN_METRIC_VERIFY` | `address`, `block` | `address`, `block`, `rpc` | `rpc` must not be required |
| `MINING_HASHPRICE_VERIFY` | `height` | `height`, `source` | `source` must not be required |
| `LIVE_SHELF_PRICE` | `price_id` | `price_id` | OK |

Defaults on pinned params must equal his pinned values so Validate probes the real question, and an explicit param must always win.

## 11. Where ranking is winnable

**High headroom — work here first:**

- **`ROUTE_ETA`** — target 2–3 engines. Our six are the same OSRM server as his truth, so they are oracles. Must be free-flow engines, not traffic-aware (§7.1). **Best opportunity in the set.**
- **`MACRO_ECONOMIC_INDICATOR`** — target 2. Ours reads his truth publisher (oracle, `comparator.go:349`). Need an independent compiler, pinnable by country + indicator + year.
- **`FX_NOW`** — 3+ sources already, target up to 10 distinct publishers. Safe and incremental; the reference for what rankable looks like.
- **`LIQUIDITY_DEPTH_VERIFY`** — 2 today (GeckoTerminal, DexScreener), target 3. Pool address must be a direct lookup key, not a list index.

**Capped — stop building, await his §8 answers:**

- **`ASSET_RESERVE_ATTESTATION`** — needs a block-pinnable independent attestation. Open.
- **`GRID`**, **`MINING`**, **`LIVE_SHELF_PRICE`** — he says 1–2. A distinct second source means a different methodology, which is a different quantity and needs his sign-off.
- **`ONCHAIN_METRIC_VERIFY`** — 1. Proven by our own 8-RPC probe.

**Do not build:** the nine judgment intents (§7.1 of the contract), the three spec-ready-but-unwired (`VALIDATOR_PERFORMANCE_VERIFY`, `VESSEL_TELEMETRY_VERIFY`, `WEATHER_FORECAST_VERIFY`), and all nine `pass_fail` hybrids including VULN and EMAIL.

## 12. Phase 0 — send Usman today (blocks everything else)

1. **The slug list** for all 63 registered miners, so `coverageByIntent` can see them. Without it nothing we have is scored.
2. **The VULN/EMAIL contradiction** — Discord said rankable, his §7.3 and the catalog both say not wired.
3. **The ONCHAIN evidence** — 8 operators, identical value at his pin. Closes his §8 Q2.
4. **Withdraw the WBTC OpenAPI proposal**, and ask whether ASSET can be re-pinned to "latest".
5. **Answers to §8 Q1, Q3, Q4, Q5** — oracle handling, widening GRID/MINING/SHELF, and whether keyed providers are acceptable. Q5 gates a lot of source research.
6. **Truth values for each pin**, so we can score locally — his live probes are uncommitted and we cannot run them.
7. **Which of the 46 unwired comparator-only intents he wires next.**

## 13. Phase 1 — fix what is already registered

A fixed miner he can see is worth more than a new one.

**Proxy** (`scripts/semantic-truth-proxy.py`):
- `eth-balance` — emit `value_gwei` as a truncated integer, serialised as an integer. Keep `value_wei` integral.
- `wbtc-por` — accept `feed_address`; emit `decimals` so the micro-unit rescale is auditable.
- `macro-unemp` — accept `indicator` and `year`; reject a latest/MRV request rather than silently answering the wrong period.
- `caiso/lmp` — accept `interval_start_utc` and derive the OASIS window.
- `liquidity-gecko` / `liquidity-dex` — accept `pool_address`.
- All handlers — an explicit param always beats a default.

**YAML**, for keepers only (one per source):
- `input_schema.required` exactly matches §5.5.
- Defaults on pinned params set to his pinned values.
- Add `asserts` that prevent silent wrong answers: `{field: currency, equals: EUR}` on SHELF, `{field: market, equals: DAM}` on GRID.
- Use `signal_mapping.scale` rather than reshaping a response.
- Keep the slug stable; re-registering under a new slug loses scoring history.

Then re-register the fixed keepers and send him the new slugs.

## 14. Phase 2 — the test harness

**In place:** `scripts/miner_selftest.py` (his §6 script, saved verbatim).

```bash
python3 scripts/miner_selftest.py --intent GRID_POWER_PRICE \
  --url "https://omni-chat.13.237.89.59.sslip.io/caiso/lmp?node=TH_NP15_GEN-APND&market=DAM&interval_start_utc=2026-09-13T14:00:00Z" \
  --truth 38095

python3 scripts/miner_selftest.py --intent LIQUIDITY_DEPTH_VERIFY \
  --url "<candidate>" --peer-url "<registered peer>"
```

**To build:**
- `out/pins.json` — the three pinned questions per intent from Part III, so every test runs the same ones.
- `scripts/run-gates.py` — wraps the self-test into Gates 2–7: three-pin askability, range, peer divergence across all three pins, Validate, then a register decision. Writes `out/gates/<slug>.json`.
- A `PASS` from `run-gates.py` is the **only** thing that authorises a `registerMiner` call.

## 15. Phase 3 — source research

Run Gates 0–7 from Part I on each candidate. Priority order: `ROUTE_ETA`, then `MACRO`, then `LIQUIDITY` and `FX_NOW`. Leave the capped intents alone until his §8 answers land.

## 16. Phase 4 — registration runbook

1. Probe the upstream directly; capture raw JSON for three pins.
2. Add a `/truth/<name>` handler only if the shape is awkward. **Never route two upstreams through one handler** — that recreates the clone problem.
3. Deploy the proxy to EC2; smoke the public URL.
4. Write the YAML: unique id, slug naming the source, `input_schema.required` per §5.5, `label_field` per §5.2, no silent defaults. **Run `python3 scripts/validate_miner_yaml.py <file>` — must PASS.**
5. Host under `/var/www/miner-yamls/`.
6. `local_validate_keepers.py` / `run-gates.py` → PASS (includes YAML gate).
7. Node Validate → `valid: true`.
8. `registerMiner` (also re-runs the YAML gate inside `register-miner.sh`).
9. Append to `newlyRegisteredMiners.md`.
10. **Send Usman the slug the same day.**

Slug convention: `<intent-prefix>-<source-name>`, e.g. `route-graphhopper`, never `route-osrm-c`.

## 17. Phase 5 — cleanup

The clone waves are liabilities: they cannot rank, they alphabetise the leaderboard, and each one we ask him to add to `coverageByIntent` costs him a code change.

**Proposal:** keep one miner per distinct source, deregister the rest of wave2 — the letter clones on GRID, SHELF and MACRO, the RPC variants on ONCHAIN and ASSET, the mirror variants on MINING. Keep at most one designated oracle per intent as a canary. Park the 8 VULN miners pending `CmpPassFail`.

Confirm the list with him first; he may want some retained.

## 18. Targets

| Intent | Registered now | Honest target | Blocker |
|---|---|---|---|
| `FX_NOW` | 11 | up to 10 distinct publishers | none — proceed |
| `ROUTE_ETA` | 6 (OSRM oracles) | 2–3 free-flow engines | none — proceed |
| `LIQUIDITY_DEPTH_VERIFY` | 2 | 3 | none — proceed |
| `MACRO_ECONOMIC_INDICATOR` | 9 (1 source, oracle) | 2 | none — proceed |
| `ASSET_RESERVE_ATTESTATION` | 9 (1 source) | 2–3 | needs block-pinnable attestation |
| `GRID_POWER_PRICE` | 9 (1 source) | 1–2 | §8 Q3 |
| `MINING_HASHPRICE_VERIFY` | 9 (1 source) | 1–2 | §8 Q3 |
| `LIVE_SHELF_PRICE` | 9 (1 source) | 1–2 | §8 Q4 |
| `ONCHAIN_METRIC_VERIFY` | 9 (1 source) | 1 | §8 Q2 |
| `VULNERABILITY_TRIAGE` | 9 | **0 until wired** | §7.3 |
| `EMAIL_SECURITY` | 10 | **0 until wired** | §7.3 |

The realistic near-term win is **ROUTE_ETA, MACRO, LIQUIDITY and FX** — four intents where a genuinely distinct source exists and ranking becomes real.

## 19. Sequence

**Today** — Phase 0 to Usman.  
**Next** — Phase 1 proxy and YAML fixes; re-register; send slugs.  
**Then** — Phase 2 harness.  
**Then** — Phase 3 research, ROUTE_ETA and MACRO first.  
**Then** — Phase 4, one source at a time, slug sent same day.  
**Then** — Phase 5 cleanup once he confirms the list.

---
---

# PART III — REFERENCE

## 20. Per-intent contract

From `MINER_SCORING_CONTRACT.md` §3 and §5.5.

| Intent | `label_field` | Scale | Tolerance | Required params |
|---|---|---|---|---|
| `FX_NOW` | `rate` | ×10000 | 50 bps | `base`, `quote` |
| `ROUTE_ETA` | `eta_seconds` | ×1 | 800 bps | `origin_lat`, `origin_lon`, `dest_lat`, `dest_lon` |
| `MACRO_ECONOMIC_INDICATOR` | `rate_pct` | ×1000 | 150 bps | `country`, `indicator`, `year` |
| `LIQUIDITY_DEPTH_VERIFY` | `liquidity_usd_cents` | ×100 | 300 bps | `network`, `pool_address` |
| `MINING_HASHPRICE_VERIFY` | `hashprice_sats_per_ph_s_day` | ×1 | 400 bps | `height` |
| `GRID_POWER_PRICE` | `lmp_usd_per_mwh_milli` | ×1000 | 30 bps | `node`, `market`, `interval_start_utc` |
| `LIVE_SHELF_PRICE` | `price_cents` | ×100 | 300 bps | `price_id` |
| `ONCHAIN_METRIC_VERIFY` | `value_gwei` | ×1, pre-scaled | 5 bps | `address`, `block` |
| `ASSET_RESERVE_ATTESTATION` | `attested_reserve` | ×1, pre-scaled | 150 bps | `feed_address`, `block` |

## 21. Pinned test values

- **`ONCHAIN`** — block 23000000. Keys: VITALIK `0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045`, BEACON `0x00000000219ab540356cBB839Cbe05303d7705Fa` (**value exceeds 2^53**), EXCHANGE `0x742d35Cc…`.
- **`ASSET`** — feed `0xa81FE04086865e63E12dD3776978E49DEEa2ea4e`, block `0x18d20a9` (26026153). Raw `11614464922334` → `attested_reserve` `116144649223`.
- **`GRID`** — node `TH_NP15_GEN-APND`, market DAM, `2026-09-13T14:00:00Z` → `38095`.
- **`SHELF`** — price_id 1 → 2770, 100 → 373, 331088 → 523, 331090 → 99. All EUR.
- **`MINING`** — heights 800000, 840000, 900000. 800000 → `233214`.
- **`MACRO`** — USA / `SL.UEM.TOTL.ZS` / 2019 → `3.669`.
- **`LIQUIDITY`** — network `eth`, pool `0x88e6a0c2…5640`.
- **`FX_NOW`** — USD→EUR, USD→CAD, USD→SEK.
- **`ROUTE_ETA`** — three origin/destination coordinate pairs.

## 22. YAML contract essentials

`semantics.signal_mapping.label_field` is **required with no default**. Optional: `verbs`, `asserts` (`{field, equals}`), and a per-miner `scale` applied **before** the intent scale. `supported_intents` holds exactly one name. `input_schema.required` must match the pins. A pinned param carrying a default is `NOT_ASKABLE`. Scoring joins on **`slug`**.

## 23. Related files

- `MINER_SCORING_CONTRACT.md` (Usman) — the authority
- `Intent Catalog v2 25-Sept (1).xlsx` — 119 intents; read §7 before trusting it
- `scripts/miner_selftest.py` — his test script
- `scripts/semantic-truth-proxy.py` — normalises upstream into the comparator field
- `newlyRegisteredMiners.md` — the 63 awaiting coverage registration
- `ALL_INTENT_MINERS.md` — inventory
- `usmanRankableSources-2026-09-23.md` — ASSET proposal **withdrawn**, see §10.2
