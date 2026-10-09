# MinerCreator

Intent miners for Telegraph: find APIs → capture sample output → **you approve** → host YAML → `registerMiner` on Base Sepolia.

## Register path (default) — Semantic V2

**Doctrine:** [`SEMANTIC_REGISTER_V2.md`](./SEMANTIC_REGISTER_V2.md)

Answer must match the intent **description**. Output **format is free** (JSON, prose, any unit/currency/language). Usman's LLM normalizes. **auto_review + LLM must approve** each sample; `register_gates_v2` re-runs it at gas time, so a manual `set_sample_status approved` does **not** unlock gas.

**Same question:** miners ranked together must answer one question (Usman 2026-10-06). Locked pins live in `shared_pins.json` and are enforced at register.

```bash
# 1) Capture live API output
python3 scripts/capture_api_output.py \
  --intent WEATHER_CURRENT \
  --slug open-meteo-wx \
  --url 'https://…' \
  --description '…' \
  --requirement 'Must convey current weather/temperature'

# 2) Auto-review (heuristics + LLM judge); read the result in the sample file
python3 scripts/auto_review_samples.py --apply --require-llm --all

# 3) Host YAML on omni (scripts/upload-host.sh), then register (fail-closed)
./scripts/register-miner-v2.sh \
  --file intentYamls/<intent>/<slug>.yaml \
  --url https://omni-chat.13.237.89.59.sslip.io/miner-yamls/<slug>.yaml \
  --sample apiOutputSamples/WEATHER_CURRENT/open-meteo-wx.md
```

Do **not** call `cast registerMiner` directly. Do **not** use scripts under `archive/legacy-batch-register/`.

## Legacy RelTol path (numeric field + scale only)

Use only when Usman still wants exact comparator fields (milli/cents RelTol):

```bash
./scripts/register-miner.sh \
  --file intentYamls/<intent>/<slug>.yaml \
  --url https://omni-chat.13.237.89.59.sslip.io/miner-yamls/<slug>.yaml
```

Runs: `validate_miner_yaml` → `preflight` → `miner_selftest` → `local_validate_keepers` → hosted byte-match → gas.

## Hosting (2026-10-07)

`upload-host.sh` hosts on **our omni nginx over SSH** (`OMNI_SSH_KEY` in `.env`), then Dropbox. **paste.rs is off** unless `ALLOW_PASTE_FALLBACK=true`: anyone can `curl -X DELETE` a paste.rs URL, and the URL is public on-chain. Existing paste-hosted miners: `scripts/migrate_paste_to_omni.py` (backup → rehost → repoint).

## Truth proxy deploy (2026-10-07)

`scripts/deploy_truth_proxy.sh --dry-run`, then without the flag. Installs a systemd unit on first run (the proxy used to be a bare process with no restart), health-checks, and rolls back on failure.

## Registration IDs (2026-10-07)

IDs come from the tx receipt event (`scripts/reg_id_from_receipt.py`). Logs before 2026-10-07 used `minerCount()` and have **43 IDs claimed by two txs**. Run `scripts/reconcile_reg_ids.py` for true IDs before any update/deregister.

## Gates added 2026-10-07

| Check | Blocks |
|---|---|
| live probe calls the YAML as the node will (method, path, params) | GET-only YAML on a POST-only RPC; HTML pages; cross-host redirects |
| `validate_miner_yaml.py` fails if PyYAML missing | unparseable YAML passing silently |
| `pin_consistency_check.py --file` | different question than the intent's locked pin; same publisher as an existing miner; duplicate slug |
| proxy fails closed (`TRUTH_ALLOW_SUBSTITUTES` off) | a venue silently answering from another source / another ship |
| auto_review: echoed enum ≠ verdict; verdict vs. reason check | judge "approves" while saying the answer is missing |

## Gates added 2026-10-08 (answer verification)

| Check | Blocks |
|---|---|
| sample `request_url` == the request the node sends | an approved sample that answers a different question than the registered YAML |
| `python -m minercheck gate` (intents with a spec in `intents/`) | wrong value (disagrees with independent sources), wrong type ("Wednesday" for a date), wrong entity (Paris, Texas), stale data, broken body |
| auto_review deterministic pre-LLM check | captured body that fails extraction / type / range / freshness / entity |
| `--skip-live` / `--skip-verify` need `ALLOW_UNSAFE_REGISTER=1` | quiet bypass of the live checks |

Ask a question with the verifier (plain English, with confidence and agreeing sources):

```bash
.venv/bin/python -m minercheck ask CRYPTO_PRICE asset=BTC
.venv/bin/python -m unittest discover -s tests -t .     # 76 tests, no network
```

## Inventory / docs

| Doc | Role |
|-----|------|
| [`SEMANTIC_REGISTER_V2.md`](./SEMANTIC_REGISTER_V2.md) | **Current** register doctrine |
| [`docs/INTENT_SPEC_GUIDE.md`](./docs/INTENT_SPEC_GUIDE.md) | Add an intent / source / miner to the verifier with YAML only |
| [`docs/ANALYSIS_REPORT.md`](./docs/ANALYSIS_REPORT.md) | 2026-10-08 audit: how "correct" was decided, what was broken |
| [`CHANGELOG.md`](./CHANGELOG.md) | What changed, behaviour changes, what is still weak |
| [`INTENT_BUILD_SHEET-2026-09-23.md`](./INTENT_BUILD_SHEET-2026-09-23.md) | Lifecycle + descriptions |
| [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) | Pre-active / recent regs |
| [`workingMiners.md`](./workingMiners.md) | Keepers |
| [`PROJECT_CONTEXT.md`](./PROJECT_CONTEXT.md) | Full handoff |
| [`MINER_BUILD_PLAN-2026-09-23.md`](./MINER_BUILD_PLAN-2026-09-23.md) | Legacy RelTol doctrine (still useful) |
| [`apiOutputSamples/`](./apiOutputSamples/) | Captured API outputs (approve here) |
| [`archive/`](./archive/) | Old batch scripts + dated campaign notes |

**YAML host:** `https://omni-chat.13.237.89.59.sslip.io/miner-yamls/<slug>.yaml`  
**On-disk YAMLs:** `intentYamls/`

## Setup

```bash
cd MinerCreator
cp .env.example .env
# edit: MINER_PRIVATE_KEY, FEE_ADDRESS, OMNIROUTE_API_KEY
chmod +x scripts/*.sh
```

## After register

```bash
curl -s https://devnode.telegraphprotocol.com/api/miners/<REG_ID> \
  | jq '.miner | {slug, activation_status, rejection_reason}'
```
