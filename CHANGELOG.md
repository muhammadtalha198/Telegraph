# Changelog

## 2026-10-08 (pm): the Intent Catalog drives verification

Specs are no longer trusted on their own — they are derived from, and audited against, the full
Intent Catalog (`Intent Catalog v2 25-Sept (1).xlsx`). Details: `docs/INTENT_SPEC_GUIDE.md` §5.

### Added
- **`minercheck/catalog.py`** + `minercheck catalog build|table|audit|show`. The workbook becomes
  `intents/_catalog.json` (119 intents, every column). Tiers (`intents/_catalog_policy.yaml`):
  83 `required`, 14 `judgment`, 22 `unverifiable`. Build-sheet descriptions cross-checked (0 differ).
- **Catalog binding in every spec** (`catalog:` block): verbatim Description, per-clause **facets**,
  `allowed_kinds`. `catalog audit` reports ALIGNED/DRIFT; all 14 catalog specs ALIGNED.
- **9 new catalog specs**, each source checked live 2026-10-08: CRYPTO_YIELD_RATE,
  LIQUIDITY_DEPTH_VERIFY, TOKEN_TOTAL_SUPPLY_VERIFY, VALIDATOR_PERFORMANCE_VERIFY,
  DNS_RECORD_LOOKUP, CORPORATE_REGISTRY_LOOKUP, MACRO_ECONOMIC_INDICATOR, LOAN_INTEREST_RATE_QUOTE,
  REGULATORY_FILING_MONITOR, CARRIER_SERVICEABILITY, COLLATERAL_HAIRCUT_VALUATION.
- **Engine features:** answer types `boolean` and `record_set`; input kind `table`; reader
  JSONP unwrap, list rules (`each`/`where`/`aggregate: notional`/`hex`/`map`/`exists`); source
  `kind` + `allowed_kinds`; `authority: true` (official record holder verifies alone); source
  `when:` filter. `minercheck gate --sample` (miner with no YAML) and `minercheck batch`.
- `tests/test_catalog.py`; live replay fixtures for all 16 specs. 83 tests pass, no network.

### Changed behaviour
- **`register_gates_v2` → `minercheck gate` now fails closed for catalog-`required` intents without
  a spec** (was SKIP). judgment-tier SKIP, unverifiable-tier BLOCKED. This surfaces, rather than
  silently skips, every deterministic intent that still lacks a spec.
- The LLM judge in `auto_review` is now given the **catalog Description** (not the sample's
  "PACK READY…" note) as the definition of correct.
- FX_NOW enforces the catalog's "real-time": feeds >1 h old (ECB/er-api/fawaz daily fixes) are
  stale and fail; CURRENCY_EXCHANGE (a separate catalog intent) is where daily fixes belong.

### Removed
- The miner **scoring/ranking** module, `intents/_scoring.yaml`, the `score` command and run-history
  recorder. Ranking is Usman's; out of scope here. This repo now only asks: is the API's output the
  right answer to its catalog intent, in any shape.

### Wave2 — 28 approved miners re-gated against the catalog
19 PASS · 8 FAIL · 1 BLOCKED (`out/wave2_catalog_gate_report.md`). Every FAIL cites the catalog:
6 LIQUIDITY miners answer CEX/perp **order-book depth**, not "liquidity across decentralized pools"
(wrong `kind`); `coll-dia-eth` returns a price but not the required **risk haircut**;
`car-zippopotam` is a postcode geocoder, not a **carrier**; `corp-sk-rpo` — RPO upstream timed out
(flaky; verified fine while probing). BLOCKED: `port-imf-portwatch` — catalog marks
LIVE_PORT_CONGESTION `Verifiable=No`.

### Still weak
- Still deterministic for ~14 of 83 required catalog intents; the rest FAIL closed until a spec is
  added. That is intentional (visible gap), not silent.
- `corp-sk-rpo`: the Slovak RPO endpoint is slow/flaky; GLEIF (authority) carries the intent, but
  the miner's own gate depends on RPO responding.
- CORPORATE active-status: a present RPO record is treated as active; dissolved-company detection
  (a `validTo` on the current name) is not implemented.


## 2026-10-08: deterministic answer verification (`minercheck`)

Full findings are in `docs/ANALYSIS_REPORT.md`. How to extend this with YAML only: `docs/INTENT_SPEC_GUIDE.md`.

### Why
Before this change, no code in this repo extracted or checked an answer value.
- One response, judged by a 3B LLM, decided "correct".
- There was no range check, no freshness check, no entity check, no answer-type check, and no cross-check at gas time.
- Two Active on-chain miners (`cp-kraken` 4683, `cp-redstone` 4670) were serving broken answers.

### Added
- **`minercheck/`** (stdlib + PyYAML). Modules:

  | Module | Role |
  |---|---|
  | `spec` | Strict loader |
  | `normalize` | City/coords/coin/currency/timezone, including lookalikes like Paris, Texas |
  | `fetch` | Timeouts, retries, 429/Retry-After, TTL cache, no cross-host redirects |
  | `reader` | JSON/XML/HTML/CSV/text/header; format taken from the body, not the header |
  | `units` | Decimal; °C/°F/K, km/h, m/s, mph, kn, cents, USDT≈USD |
  | `answers` | Answer types |
  | `validate` | E1, E2, E4, E5 |
  | `verify` | E3 majority of independent publishers, confidence, "could not verify" |
  | `render` | Plain-English templates |
  | `scoring` | YAML-configured ranking with copy detection |
  | `gate` | Register gate |
  | `sample_check` | Deterministic check of captured samples for auto_review |
  | `cli` | Command line |
- **`intents/*.yaml`**: the single source of truth for verification. Five specs:
  - WEATHER_CHECK (5 sources)
  - CRYPTO_PRICE (7)
  - FX_NOW (6)
  - DATE_TODAY (5)
  - TIME_IN_CITY (5)

  Every source was checked live on 2026-10-08. Together they cover JSON, XML, HTML, text, and header-only responses.

  `_shared.yaml` holds the gazetteer and currency tables. `_scoring.yaml` holds the miner scoring rules.
- **Tests: 76 unittest cases, no network.**
  - Per-layer unit tests.
  - Replay of real responses recorded on 2026-10-08 (`tests/fixtures/live`, IPs scrubbed).
  - Per-intent matrix: one mock source per format (JSON/XML/text/HTML/CSV) × {correct, wrong type, wrong entity, stale}, plus conflicts and broken/empty/500/timeout responses.
  - Regression tests for every script bug fixed below.
- `scripts/sample_file.py`: one sample reader/writer, replacing four copies.

### Changed behaviour
1. **`register_gates_v2.py` has two new fail-closed gates:**
   - The sample must ask the same question as the YAML. The sample's `request_url` must equal the request the node sends.
   - `minercheck gate`: the miner's live answer must pass E1–E5 and agree with independent sources. Intents without a spec SKIP this gate. **A spec'd intent whose miner slug is not mapped in the spec FAILS** until you add it.
2. The live probe builds URLs like the node: `{param}` path placeholders are filled. It used to probe `/addresses/{address}?address=…`. Content family is now judged from the body.
3. `--skip-live` now requires `ALLOW_UNSAFE_REGISTER=1`, like every other skip. `--skip-verify` is new and gated the same way.
4. `auto_review_samples.py`:
   - A deterministic pre-LLM check rejects spec'd samples whose captured body fails E1/E2/E4/E5. Rejections get `mode: deterministic`.
   - `hard_check` no longer rejects structured JSON because a data field contains words like "rate_limit" or "not found". Only error-ish fields are scanned.
5. `register-miner-v2.sh` runs gates with `.venv/bin/python` when present. System `python3` has no PyYAML, so the gates failed closed there.
6. `capture_api_output.py` and `generate_yamls_from_approved_samples.py` refuse URLs that still contain `{placeholder}`.

### Fixed
- `generate_yamls_from_approved_samples.py`: `slug` was used before assignment (NameError on the first manual-approved sample).
- The sample parser cut bodies at a ```` ``` ```` inside a JSON string. Three samples were read truncated (`patch-gh-compare`, `secrev-pypi-requests`, `vuln-redhat-cve`).
- `set_sample_status.py`: a note containing `\1` or `\g` broke the regex replacement.
- `pin_consistency_check.py --file`: one unparsable YAML elsewhere crashed the gate.
- Three local miner YAMLs. These changes are **local only**; each needs re-host plus `register-miner-v2.sh --update <id>`:
  - `cp-kraken.yaml`: default `pair: "{kraken_pair}"` → `XBTUSD`. The live gate now PASSes; it FAILed before.
  - `fx-frankfurter.yaml`: `api.frankfurter.app/latest` (now a cross-host 301) → `api.frankfurter.dev/v1/latest`. The gate now PASSes.
  - `fx-hnb.yaml`: duplicate id 31004 (shared with fx-awesomeapi) → 190175. The miner is deregistered, so there is no live clash.

### Still weak
- **Only 5 of 56 intents have a spec.** The other 51 still rely on the LLM judge alone; the gate SKIP says so. Judgment intents (translation, summarisation, chat) need a different verifier.
- The LLM gate can block correct answers. qwen2.5:3b called a correct USD→EUR rate "partial" because the catalog description also asks for spreads. Policy decision for you: should a deterministic PASS outrank an LLM "partial"? Not changed, because CLAUDE.md makes LLM approval mandatory.
- Three garbage-description problems are left as-is:
  - 41 registered YAMLs (and 33 samples) carry pack notes ("PACK READY…") as their description. Not rewritten, because each change needs an on-chain update.
  - 24 slugs are sampled under two intent folders, and 21 of them have conflicting statuses.
  - 85 approved samples have no LLM record.
- On-chain, still serving broken answers until you act:
  - `cp-redstone` (4670): its approved sample body is `[]`. Deregister it or recapture and update it through the gates.
  - `cp-kraken` (4683) and `fx-frankfurter`: update them with the fixed YAMLs above.
- Scoring needs history. Every source currently has fewer than `min_runs` judged runs. Run `python -m minercheck run-tests` on a schedule to build it.
- Copy detection is statistical: identical values where others differ, with the slower source flagged as the relay. A relay that adds noise can evade it.
- Some false positives remain:
  - HTTP 404 for an unsupported input (Frankfurter has no PKR) counts against uptime the same as an outage.
  - Free time APIs are flaky (worldtimeapi resets connections). The specs carry five clocks so one failure does not block an answer.
- The truth proxy (`semantic-truth-proxy.py`) is untouched. It still hard-codes per-venue extraction in Python and is the live answer source for about 141 miners. Moving it onto intent specs is the next big step.
