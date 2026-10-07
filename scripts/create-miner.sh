#!/usr/bin/env bash
# End-to-end: generate YAML → host publicly → hash → registerMiner on Base Sepolia.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# shellcheck disable=SC1091
[[ -f "$ROOT/.env" ]] && set -a && source "$ROOT/.env" && set +a

ID=""
SLUG=""
NAME=""
MODEL=""
BASE_URL="${BASE_URL:-https://omni-chat.13.237.89.59.sslip.io}"
INTENT="CHAT_COMPLETION"
DESCRIPTION=""
UPDATE_ID=""

usage() {
  cat <<EOF
MinerCreator — single-model chat miner automation

Usage:
  $(basename "$0") \\
    --id 9201 \\
    --slug omni-cheap-chat \\
    --name "OmniRoute Cheap Chat" \\
    --model auto/cheap \\
    [--base-url https://omni-chat.13.237.89.59.sslip.io] \\
    [--intent CHAT_COMPLETION] \\
    [--update OLD_REG_ID]

Reads secrets from MinerCreator/.env
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --id) ID="$2"; shift 2 ;;
    --slug) SLUG="$2"; shift 2 ;;
    --name) NAME="$2"; shift 2 ;;
    --model) MODEL="$2"; shift 2 ;;
    --base-url) BASE_URL="$2"; shift 2 ;;
    --intent) INTENT="$2"; shift 2 ;;
    --description) DESCRIPTION="$2"; shift 2 ;;
    --update) UPDATE_ID="$2"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown: $1"; usage; exit 1 ;;
  esac
done

[[ -n "$ID" && -n "$SLUG" && -n "$NAME" && -n "$MODEL" ]] || { usage; exit 1; }

echo "==> 1/3 Generate YAML"
GEN_ARGS=(--id "$ID" --slug "$SLUG" --name "$NAME" --model "$MODEL" --base-url "$BASE_URL" --intent "$INTENT")
[[ -n "$DESCRIPTION" ]] && GEN_ARGS+=(--description "$DESCRIPTION")
"$ROOT/scripts/generate-yaml.sh" "${GEN_ARGS[@]}"
YAML="$ROOT/yaml/${SLUG}.yaml"

echo "==> 2/3 Host YAML (Dropbox or fallback)"
HOST_OUT=$("$ROOT/scripts/upload-host.sh" "$YAML")
echo "$HOST_OUT"
YAML_URL=$(echo "$HOST_OUT" | sed -n 's/^YAML_URL=//p' | tail -1)
[[ -n "$YAML_URL" ]] || { echo "No YAML_URL from hoster" >&2; exit 1; }

echo "==> 3/3 On-chain registration"
REG_ARGS=(--file "$YAML" --url "$YAML_URL" --intents "$INTENT")
if [[ -n "${UPDATE_ID:-}" ]]; then
  REG_ARGS+=(--update "$UPDATE_ID")
fi
"$ROOT/scripts/register-miner.sh" "${REG_ARGS[@]}"

echo ""
echo "Next: wait 1–3 min, then:"
echo "  curl -s https://devnode.telegraphprotocol.com/api/miners/\$(jq -r .new_registration_id $ROOT/out/last-registration.json) | jq '.miner'"
echo "Install API key for slug '$SLUG' after status=active (wallet challenge flow)."
