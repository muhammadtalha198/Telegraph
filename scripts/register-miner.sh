#!/usr/bin/env bash
# Safe registerMiner / updateMiner — MANDATORY validation pipeline, then gas.
#
# THIS IS THE ONLY supported way to register a miner.
# Do NOT call `cast send … registerMiner` or legacy batch scripts directly.
#
# Automatic gates (fail-closed — gas is NEVER spent if any gate fails):
#   1) validate_miner_yaml.py
#   2) preflight_miner.py          (Groups A–D live quantity / NON-DET text)
#   3) miner_selftest.py           (RelTol or NON-DET text askability)
#   4) local_validate_keepers.py   (--slug or --from-yaml; always runs)
#   5) hosted YAML bytes == local
#   6) cast registerMiner / updateMiner
#
# Usage:
#   ./scripts/register-miner.sh --file intentYamls/.../slug.yaml --url https://…/slug.yaml
#   ./scripts/register-miner.sh --file ... --url ... --update OLD_ID
#
# Unsafe bypass (emergencies ONLY):
#   ALLOW_UNSAFE_REGISTER=1 ./scripts/register-miner.sh ... --skip-gates
#
# Env (.env): DIAMOND, RPC_URL, MINER_PRIVATE_KEY, FEE_ADDRESS, MIN_PRICE_USDC
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# shellcheck disable=SC1091
[[ -f "$ROOT/.env" ]] && set -a && source "$ROOT/.env" && set +a

FILE=""
YAML_URL=""
INTENTS=""          # empty → auto from YAML via register_gates
MODE="register"     # register | update
OLD_ID=""
SKIP_KEEPERS=0
SKIP_GATES=0

usage() {
  cat <<EOF
Usage: $(basename "$0") --file YAML --url PUBLIC_URL [--intents CSV] [--update OLD_ID]

Always runs validate_miner_yaml + preflight + miner_selftest + keepers
BEFORE spending gas. Intent defaults are taken from the YAML when --intents omitted.

Unsafe (requires ALLOW_UNSAFE_REGISTER=1):
  --skip-gates    skip all validation (never for normal work)
  --skip-keepers  skip keepers only

Env (.env): DIAMOND, RPC_URL, MINER_PRIVATE_KEY, FEE_ADDRESS, MIN_PRICE_USDC
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --file) FILE="$2"; shift 2 ;;
    --url) YAML_URL="$2"; shift 2 ;;
    --intents) INTENTS="$2"; shift 2 ;;
    --update) MODE="update"; OLD_ID="$2"; shift 2 ;;
    --skip-keepers) SKIP_KEEPERS=1; shift ;;
    --skip-gates) SKIP_GATES=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown: $1"; usage; exit 1 ;;
  esac
done

[[ -f "${FILE:-}" && -n "${YAML_URL:-}" ]] || { usage; exit 1; }
[[ -n "${MINER_PRIVATE_KEY:-}" && -n "${FEE_ADDRESS:-}" ]] || {
  echo "Set MINER_PRIVATE_KEY and FEE_ADDRESS in $ROOT/.env" >&2; exit 1
}

if [[ "$SKIP_GATES" -eq 1 || "$SKIP_KEEPERS" -eq 1 ]]; then
  if [[ "${ALLOW_UNSAFE_REGISTER:-}" != "1" ]]; then
    echo "FATAL: --skip-gates/--skip-keepers blocked." >&2
    echo "  Validation is mandatory. For a true emergency only:" >&2
    echo "  ALLOW_UNSAFE_REGISTER=1 $0 ..." >&2
    exit 1
  fi
  echo "WARN  ALLOW_UNSAFE_REGISTER=1 — skipping validation (unsafe)"
fi

DIAMOND="${DIAMOND:-0x5a2324aA18613FAD4e44bDF0d6c73Ec1f6D87ff8}"
RPC_URL="${RPC_URL:-https://sepolia.base.org}"
MIN_PRICE_USDC="${MIN_PRICE_USDC:-10000}"

# --- automatic gates (no hand-running validate / preflight / selftest / keepers) ---
if [[ "$SKIP_GATES" -eq 0 ]]; then
  META_FILE=$(mktemp /tmp/reg-gates-meta.XXXXXX)
  GATE_ARGS=(--file "$FILE" --meta-out "$META_FILE")
  [[ "$SKIP_KEEPERS" -eq 1 ]] && GATE_ARGS+=(--skip-keepers)
  echo "=== automatic register gates (fail-closed) ==="
  python3 "$ROOT/scripts/register_gates.py" "${GATE_ARGS[@]}" || {
    rm -f "$META_FILE"
    echo "FATAL: register_gates.py failed — NOT sending registerMiner." >&2
    exit 1
  }
  # Auto-fill intents from YAML when caller omitted --intents
  if [[ -z "$INTENTS" ]]; then
    INTENTS=$(sed -n 's/^INTENT=//p' "$META_FILE" | head -1)
  fi
  rm -f "$META_FILE"
  if [[ -z "$INTENTS" ]]; then
    echo "FATAL: could not determine intent (pass --intents CSV)" >&2
    exit 1
  fi
  echo "INTENTS(auto)=$INTENTS"
else
  echo "WARN  --skip-gates: spending gas WITHOUT validation"
  [[ -n "$INTENTS" ]] || {
    echo "FATAL: --skip-gates requires --intents CSV" >&2
    exit 1
  }
fi

# Verify remote bytes == local before spending gas
curl -sSL -m 30 -A "Go-http-client/1.1" "$YAML_URL" -o /tmp/reg-remote.yaml
cmp -s "$FILE" /tmp/reg-remote.yaml || {
  echo "FATAL: hosted YAML bytes != local file — aborting to avoid hash mismatch." >&2
  echo "  Host first, then re-run register-miner.sh" >&2
  exit 1
}

YAML_HASH="0x$(shasum -a 256 "$FILE" | awk '{print $1}')"
echo "YAML_HASH=$YAML_HASH"

INTENTS_JSON=$(python3 -c "import json,sys; print(json.dumps([x.strip() for x in sys.argv[1].split(',') if x.strip()]))" "$INTENTS")

ADDR=$(cast wallet address --private-key "$MINER_PRIVATE_KEY")
echo "SIGNER=$ADDR"
echo "FEE_ADDRESS=$FEE_ADDRESS"
echo "YAML_URL=$YAML_URL"

if [[ "$MODE" == "update" ]]; then
  [[ -n "$OLD_ID" ]] || { echo "--update needs old registration id" >&2; exit 1; }
  echo "Sending updateMiner($OLD_ID)..."
  OUT=$(cast send "$DIAMOND" \
    "updateMiner(uint256,string,bytes32,address,uint256,string[])" \
    "$OLD_ID" \
    "$YAML_URL" \
    "$YAML_HASH" \
    "$FEE_ADDRESS" \
    "$MIN_PRICE_USDC" \
    "$INTENTS_JSON" \
    --rpc-url "$RPC_URL" \
    --private-key "$MINER_PRIVATE_KEY" \
    --json)
else
  echo "Sending registerMiner..."
  OUT=$(cast send "$DIAMOND" \
    "registerMiner(string,bytes32,address,uint256,string[])" \
    "$YAML_URL" \
    "$YAML_HASH" \
    "$FEE_ADDRESS" \
    "$MIN_PRICE_USDC" \
    "$INTENTS_JSON" \
    --rpc-url "$RPC_URL" \
    --private-key "$MINER_PRIVATE_KEY" \
    --json)
fi

TX=$(echo "$OUT" | python3 -c "import json,sys; print(json.load(sys.stdin).get('transactionHash',''))")
STATUS=$(echo "$OUT" | python3 -c "import json,sys; print(json.load(sys.stdin).get('status',''))")
NEW_ID=$(cast call "$DIAMOND" "minerCount()(uint256)" --rpc-url "$RPC_URL")

mkdir -p "$ROOT/out"
REPORT="$ROOT/out/last-registration.json"
python3 - "$REPORT" <<PY
import json, sys
from pathlib import Path
Path(sys.argv[1]).write_text(json.dumps({
  "mode": "$MODE",
  "old_registration_id": "$OLD_ID" or None,
  "new_registration_id": int("$NEW_ID"),
  "tx_hash": "$TX",
  "tx_status": "$STATUS",
  "tx_url": f"https://sepolia.basescan.org/tx/$TX",
  "yaml_file": "$FILE",
  "yaml_url": "$YAML_URL",
  "yaml_hash": "$YAML_HASH",
  "fee_address": "$FEE_ADDRESS",
  "signer": "$ADDR",
  "intents": $INTENTS_JSON,
  "min_price_usdc": int("$MIN_PRICE_USDC"),
  "diamond": "$DIAMOND",
  "rpc": "$RPC_URL",
  "gates": "register_gates.py (yaml+preflight+selftest+keepers; fail-closed)",
}, indent=2))
print(Path(sys.argv[1]).read_text())
PY

echo ""
echo "=== DONE ==="
echo "Registration ID (latest counter): $NEW_ID"
echo "TX: https://sepolia.basescan.org/tx/$TX"
echo "Poll: curl -s https://devnode.telegraphprotocol.com/api/miners/$NEW_ID | jq '.miner|{slug,activation_status,rejection_reason}'"
