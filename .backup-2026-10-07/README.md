# MinerCreator

Intent miners for Telegraph: find APIs → capture sample output → **you approve** → host YAML → `registerMiner` on Base Sepolia.

## Register path (default) — Semantic V2

**Doctrine:** [`SEMANTIC_REGISTER_V2.md`](./SEMANTIC_REGISTER_V2.md)

Answer must match the intent **description**. Output **format is free** (JSON, prose, any unit/currency/language). Usman's LLM normalizes. You must **manually approve** each API sample before gas.

```bash
# 1) Capture live API output
python3 scripts/capture_api_output.py \
  --intent WEATHER_CURRENT \
  --slug open-meteo-wx \
  --url 'https://…' \
  --description '…' \
  --requirement 'Must convey current weather/temperature'

# 2) You read apiOutputSamples/<INTENT>/<slug>.md, then approve
python3 scripts/set_sample_status.py \
  --file apiOutputSamples/WEATHER_CURRENT/open-meteo-wx.md \
  --status approved \
  --note 'Clear temperature answer'

# 3) Host YAML, then register (fail-closed)
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

## Inventory / docs

| Doc | Role |
|-----|------|
| [`SEMANTIC_REGISTER_V2.md`](./SEMANTIC_REGISTER_V2.md) | **Current** register doctrine |
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
