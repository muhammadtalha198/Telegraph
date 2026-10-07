# Semantic Register V2 — answer-correct, format-agnostic

**Date:** 2026-10-02  
**Drivers:** Ahmed + Usman discussion (LLM normalizes miner outputs) · Alexandria uses miners to answer user questions  
**Status:** New registration path. **auto_review + LLM must APPROVE** the sample before gas (automatic inside `register_gates_v2`). Manual `set_sample_status` alone does **not** unlock register.

---

## What changed (simple)

| | **Old (RelTol gates)** | **New (Semantic V2)** |
|---|------------------------|------------------------|
| What must be right | Exact field name + exact scale (e.g. `38095` milli) | The **answer meaning** matches the intent description |
| Output shape | Forced number / yes-no in `label_field` | **Any shape OK** — JSON, text, °C or °F, USD or USDT, any language |
| Who normalizes | Our proxy / YAML scale | **LLM on Usman’s side** → plain English → semantic WASM |
| Before register | Auto RelTol/PassFail keepers | **auto_review + LLM must APPROVE** (hard/reject/needs_human = no gas); golden PASS if suite exists |
| Store | Mostly in YAML + keepers | **`apiOutputSamples/<INTENT>/<slug>.md`** — one file per API |

**Alexandria link:** User asks in Terminal → engine routes to a miner by intent → miner returns whatever JSON/text → UI shows it (string/`answer` preferred; raw JSON also works). Correct answer matters more than pretty schema; Usman’s LLM path is what makes format-agnostic ranking work.

---

## What we **kept** from before

1. **One miner = one upstream source** (no clones).
2. **Intent description is law** — weather APIs must answer weather; crypto APIs must answer price. Wrong topic = reject.
3. **YAML must parse** (`validate_miner_yaml.py`) — broken YAML still rejected on-chain.
4. **Hosted YAML byte-match** — public URL == local file we tested.
5. **Fail-closed gas** — no `cast registerMiner` until gates PASS.
6. **Sample APPROVED by auto_review+LLM before gas** — re-run inside `register_gates_v2` every time; manual status override does not unlock gas.
7. **Ahmed: fewer correct > fake pad to 10.**
8. **Do not count Omni ~1400 mass regs** as this method.
9. **Lifecycle docs** (Active / Pre-active / Dead) still apply after Usman ranks.
10. **Golden suite** — if `candidates/*.json` defines the slug, it must PASS (`v2_golden_gate.py`).

---

## What is **new**

1. **Format-agnostic acceptance** — no hard RelTol field/scale gate on this path.
2. **`apiOutputSamples/`** — capture real API response **first**, per intent × slug.
3. **Status workflow:** `pending_review` → **auto-review (heuristics + LLM, mandatory)** → `approved` | `rejected` | `needs_human` (needs_human ≠ register).
4. **Register only if sample is `approved` by auto_review+LLM** (enforced again at gas time).
5. **Live probe** only checks: HTTP OK + non-empty body that still answers (soft). No milli-cent enforcement.
6. Scripts (creation pipeline — all gates stay in the loop):
   - `capture_api_output.py` → sample
   - `auto_review_samples.py --apply --require-llm` → approve/reject (**also runs inside register_gates_v2**)
   - `v2_golden_gate.py` → PASS if suite exists (**inside register_gates_v2**)
   - `generate_yamls_from_approved_samples.py` → YAML + `validate_miner_yaml` (auto_review+LLM approved-only)
   - `register_gates_v2.py` + `register-miner-v2.sh` → gas

---

## How the new mechanism works (steps)

```
1. Pick intent from catalog / INTENT_BUILD_SHEET (read Description).
2. Find API that honestly answers that description (any unit/currency/language OK).
3. Capture:
     python3 scripts/capture_api_output.py \
       --intent WEATHER_CURRENT \
       --slug open-meteo-wx \
       --url 'https://…'
4. (Optional batch) Auto-review with LLM:
     python3 scripts/auto_review_samples.py --apply --require-llm --all
   → needs_human / rejected = fix or drop (do not register)
5. Generate YAMLs only from auto_review+LLM approved samples:
     python3 scripts/generate_yamls_from_approved_samples.py
6. Host YAML, then register — gates re-run auto_review+LLM + golden-if-any automatically:
     ./scripts/register-miner-v2.sh \
       --file intentYamls/…/open-meteo-wx.yaml \
       --url https://omni-chat…/miner-yamls/open-meteo-wx.yaml \
       --sample apiOutputSamples/WEATHER_CURRENT/open-meteo-wx.md
```

**Gas requires auto_review + LLM `approved` every time** (inside `register_gates_v2`).  
`set_sample_status.py` is bookkeeping only — it does **not** unlock registerMiner.  
If `candidates/*.json` defines the slug, golden suite must PASS (`v2_golden_gate.py`).  
Needs: `OMNIROUTE_API_KEY` or `OPENAI_API_KEY` in `.env`.

---

## Examples of “good enough” outputs (V2)

**WEATHER_CURRENT / WEATHER_CHECK** — any of these OK if they answer current weather:

- `{"temperature_c": 22}`
- `"Today's weather is 22 degrees Celsius"`
- `"72°F, clear"`
- French / Spanish prose with the same fact

**CRYPTO_PRICE_LOOKUP / CRYPTO_PRICE** — any of these OK if they answer the token’s price:

- `{"bitcoin":{"usd":64000}}`
- `"BTC is 64000 USDT"`
- Price in USD, USDC, or another quote — LLM normalizes later
- Plain English sentence with the number

**Not OK:** unrelated topic (carbon intensity for weather; TVL list for spot price).

---

## When to still use **old** `register-miner.sh`

Use RelTol path only if Usman explicitly still wants **numeric comparator** scoring for that intent (milli fields, RelTol band).  
Default for new Ahmed/Usman “LLM normalize” work: **`register-miner-v2.sh`**.

---

## File layout

```
MinerCreator/
  SEMANTIC_REGISTER_V2.md          ← this doc (default path)
  README.md                        ← points here first
  apiOutputSamples/
    README.md
    _TEMPLATE.md
    WEATHER_CURRENT/
      <slug>.md
    CRYPTO_PRICE_LOOKUP/
      <slug>.md
  scripts/
    capture_api_output.py
    set_sample_status.py
    register_gates_v2.py
    register-miner-v2.sh
    register-miner.sh              ← legacy RelTol only
  archive/
    README.md
    legacy-batch-register/         ← do not run
    legacy-campaign-docs/          ← dated notes
```
