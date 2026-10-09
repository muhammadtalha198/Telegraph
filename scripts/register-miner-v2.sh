#!/usr/bin/env bash
# Semantic Register V2 — answer-correct / format-agnostic path.
#
# Fail-closed gates (automatic — do not skip):
#   1) auto_review_samples.py --gate  (hard + minercheck sample check + heuristic + LLM; must approve)
#   2) v2_golden_gate.py              (must PASS if candidates/*.json has slug)
#   3) validate_miner_yaml.py + pin_consistency_check.py
#   4) sample request == the request the node will send (same question)
#   5) minercheck gate: live answer verified vs independent sources (SKIP if no intents/<INTENT>.yaml)
#   6) live probe of the YAML request (content family)
#   7) hosted YAML bytes == local
#   8) registerMiner / updateMiner
#
# Manual set_sample_status approved alone does NOT unlock gas.
#
# Usage:
#   ./scripts/register-miner-v2.sh \
#     --file intentYamls/.../slug.yaml \
#     --url  https://omni-chat…/miner-yamls/slug.yaml \
#     --sample apiOutputSamples/WEATHER_CURRENT/slug.md
#
# Env (.env): DIAMOND, RPC_URL, MINER_PRIVATE_KEY, FEE_ADDRESS, MIN_PRICE_USDC
#             Ollama (local) and/or OMNIROUTE_API_KEY / OPENAI_API_KEY for auto_review LLM
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# shellcheck disable=SC1091
[[ -f "$ROOT/.env" ]] && set -a && source "$ROOT/.env" && set +a

FILE=""
YAML_URL=""
SAMPLE=""
INTENTS=""
MODE="register"
OLD_ID=""

usage() {
  cat <<EOF
Usage: $(basename "$0") --file YAML --url PUBLIC_URL --sample apiOutputSamples/INTENT/slug.md

V2 gates (fail-closed, automatic):
  1) auto_review + LLM must APPROVE the sample (rejects / needs_human = no gas)
  2) golden suite PASS if candidates/*.json defines the slug
  3) validate_miner_yaml.py + shared pin / distinct publisher
  4) sample asked the same question the node will ask
  5) minercheck: live answer verified against independent sources (intents/<INTENT>.yaml)
  6) live probe of the YAML request
  7) hosted YAML bytes == local
  8) registerMiner / updateMiner

Capture first, then register (review is inside the gate — do not hand-approve to skip):
  python3 scripts/capture_api_output.py --intent … --slug … --url …
  ./scripts/register-miner-v2.sh --file … --url … --sample …
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --file) FILE="$2"; shift 2 ;;
    --url) YAML_URL="$2"; shift 2 ;;
    --sample) SAMPLE="$2"; shift 2 ;;
    --intents) INTENTS="$2"; shift 2 ;;
    --update) MODE="update"; OLD_ID="$2"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown: $1"; usage; exit 1 ;;
  esac
done

[[ -f "${FILE:-}" && -n "${YAML_URL:-}" && -n "${SAMPLE:-}" ]] || { usage; exit 1; }
[[ -n "${MINER_PRIVATE_KEY:-}" && -n "${FEE_ADDRESS:-}" ]] || {
  echo "Set MINER_PRIVATE_KEY and FEE_ADDRESS in $ROOT/.env" >&2; exit 1
}
# Local Ollama counts as LLM (default http://127.0.0.1:11434). Cloud keys optional fallback.
_ollama_ok=0
if curl -fsS --max-time 2 "${OLLAMA_BASE_URL:-http://127.0.0.1:11434}/api/tags" >/dev/null 2>&1; then
  _ollama_ok=1
fi
if [[ -z "${OMNIROUTE_API_KEY:-}${OPENAI_API_KEY:-}" && "${_ollama_ok}" != "1" && "${ALLOW_UNSAFE_REGISTER:-}" != "1" ]]; then
  echo "FATAL: start Ollama (qwen2.5:3b) or set OMNIROUTE_API_KEY / OPENAI_API_KEY for auto_review LLM gate." >&2
  exit 1
fi

DIAMOND="${DIAMOND:-0x5a2324aA18613FAD4e44bDF0d6c73Ec1f6D87ff8}"
RPC_URL="${RPC_URL:-https://sepolia.base.org}"
MIN_PRICE_USDC="${MIN_PRICE_USDC:-10000}"

# Gates need PyYAML (validate_miner_yaml, pin check, minercheck): prefer the project venv.
PY="${PYTHON:-$ROOT/.venv/bin/python}"
[[ -x "$PY" ]] || PY=python3

echo "=== Semantic Register V2 gates (fail-closed) ==="
"$PY" "$ROOT/scripts/register_gates_v2.py" --file "$FILE" --sample "$SAMPLE" || {
  echo "FATAL: register_gates_v2.py failed — NOT sending registerMiner." >&2
  exit 1
}

# Intent from sample front matter if not passed (catalog aliases → on-chain canonical)
if [[ -z "$INTENTS" ]]; then
  SAMPLE_PATH="$SAMPLE"
  [[ -f "$SAMPLE_PATH" ]] || SAMPLE_PATH="$ROOT/$SAMPLE"
  INTENTS=$(python3 -c "
import re, sys
from pathlib import Path
sys.path.insert(0, r'''$ROOT/scripts''')
from v2_intent_folders import canonical_intent
t = Path(r'''$SAMPLE_PATH''').read_text(encoding='utf-8')
m = re.search(r'(?m)^intent:\s*(\S+)', t)
print(canonical_intent(m.group(1)) if m else '')
")
else
  INTENTS=$(python3 -c "
import sys
sys.path.insert(0, r'''$ROOT/scripts''')
from v2_intent_folders import canonical_intent
print(','.join(canonical_intent(x) for x in sys.argv[1].split(',') if x.strip()))
" "$INTENTS")
fi
[[ -n "$INTENTS" ]] || {
  echo "FATAL: could not read intent from sample (pass --intents)" >&2
  exit 1
}
echo "INTENTS=$INTENTS"

curl -sSL -m 30 -A "Go-http-client/1.1" "$YAML_URL" -o /tmp/reg-remote-v2.yaml
cmp -s "$FILE" /tmp/reg-remote-v2.yaml || {
  echo "FATAL: hosted YAML bytes != local file — host first, then re-run." >&2
  exit 1
}

YAML_HASH="0x$(shasum -a 256 "$FILE" | awk '{print $1}')"
echo "YAML_HASH=$YAML_HASH"

INTENTS_JSON=$(python3 -c "import json,sys; print(json.dumps([x.strip() for x in sys.argv[1].split(',') if x.strip()]))" "$INTENTS")
ADDR=$(cast wallet address --private-key "$MINER_PRIVATE_KEY")
echo "SIGNER=$ADDR"

if [[ "$MODE" == "update" ]]; then
  [[ -n "$OLD_ID" ]] || { echo "--update needs old registration id" >&2; exit 1; }
  echo "Sending updateMiner($OLD_ID)..."
  OUT=$(cast send "$DIAMOND" \
    "updateMiner(uint256,string,bytes32,address,uint256,string[])" \
    "$OLD_ID" "$YAML_URL" "$YAML_HASH" "$FEE_ADDRESS" "$MIN_PRICE_USDC" "$INTENTS_JSON" \
    --rpc-url "$RPC_URL" --private-key "$MINER_PRIVATE_KEY" --json)
else
  echo "Sending registerMiner..."
  OUT=$(cast send "$DIAMOND" \
    "registerMiner(string,bytes32,address,uint256,string[])" \
    "$YAML_URL" "$YAML_HASH" "$FEE_ADDRESS" "$MIN_PRICE_USDC" "$INTENTS_JSON" \
    --rpc-url "$RPC_URL" --private-key "$MINER_PRIVATE_KEY" --json)
fi

TX=$(echo "$OUT" | python3 -c "import json,sys; print(json.load(sys.stdin).get('transactionHash',''))")
STATUS=$(echo "$OUT" | python3 -c "import json,sys; print(json.load(sys.stdin).get('status',''))")
# Registration ID comes from the receipt's MinerRegistered / MinerUpdated event —
# NOT minerCount() (stale RPC / concurrent registrants gave duplicate IDs 2026-10-05).
# Also fails closed if the tx reverted (status != 0x1).
NEW_ID=$(echo "$OUT" | python3 "$ROOT/scripts/reg_id_from_receipt.py" --diamond "$DIAMOND" --mode "$MODE") || {
  echo "FAIL: tx $TX did not produce a registration (status=$STATUS). Nothing recorded." >&2
  exit 1
}

mkdir -p "$ROOT/out"
REPORT="$ROOT/out/last-registration-v2.json"
python3 - "$REPORT" <<PY
import json
from pathlib import Path
Path("$REPORT").write_text(json.dumps({
  "mode": "$MODE",
  "path": "semantic-v2",
  "old_registration_id": "$OLD_ID" or None,
  "new_registration_id": int("$NEW_ID"),
  "tx_hash": "$TX",
  "tx_status": "$STATUS",
  "tx_url": f"https://sepolia.basescan.org/tx/$TX",
  "yaml_file": "$FILE",
  "yaml_url": "$YAML_URL",
  "sample": "$SAMPLE",
  "yaml_hash": "$YAML_HASH",
  "intents": $INTENTS_JSON,
  "gates": "register_gates_v2.py (auto_review+LLM + golden-if-any + yaml + pin + question + minercheck + live + byte-match)",
}, indent=2) + "\n")
print(Path("$REPORT").read_text())
PY

echo ""
echo "=== DONE (V2) ==="
echo "Registration ID (from receipt event): $NEW_ID"
echo "TX: https://sepolia.basescan.org/tx/$TX"
echo "Poll: curl -s https://devnode.telegraphprotocol.com/api/miners/$NEW_ID | jq '.miner|{slug,activation_status,rejection_reason}'"
