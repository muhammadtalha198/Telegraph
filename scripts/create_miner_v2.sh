#!/usr/bin/env bash
# Semantic V2 miner creation — one entrypoint that keeps all gates in the loop.
#
# Pipeline (fail-closed):
#   1) capture_api_output.py          → apiOutputSamples/... (pending_review)
#   2) auto_review_samples.py --apply → approved|rejected|needs_human
#   3) generate_yamls_from_approved_samples.py → intentYamls/... + validate_miner_yaml
#   4) (you) host YAML
#   5) register-miner-v2.sh           → sample approved + yaml + live probe + byte-match + gas
#
# Usage:
#   ./scripts/create_miner_v2.sh --capture --intent LIQUIDITY_DEPTH_VERIFY --slug liq-x --url 'https://…'
#   ./scripts/create_miner_v2.sh --review-apply
#   ./scripts/create_miner_v2.sh --gen-yamls
#   ./scripts/create_miner_v2.sh --all-from-research   # review pending + gen yamls for approved
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

MODE=""
INTENT=""
SLUG=""
URL=""
INPUTS=""
FORCE=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --capture) MODE="capture"; shift ;;
    --review-apply) MODE="review"; shift ;;
    --gen-yamls) MODE="yamls"; shift ;;
    --all-from-research) MODE="all"; shift ;;
    --intent) INTENT="$2"; shift 2 ;;
    --slug) SLUG="$2"; shift 2 ;;
    --url) URL="$2"; shift 2 ;;
    --inputs) INPUTS="$2"; shift 2 ;;
    --force) FORCE="--force"; shift ;;
    -h|--help)
      sed -n '2,20p' "$0"; exit 0 ;;
    *) echo "Unknown: $1" >&2; exit 1 ;;
  esac
done

case "${MODE:-}" in
  capture)
    [[ -n "$INTENT" && -n "$SLUG" && -n "$URL" ]] || {
      echo "Need --intent --slug --url" >&2; exit 1
    }
    python3 scripts/capture_api_output.py \
      --intent "$INTENT" --slug "$SLUG" --url "$URL" --inputs "${INPUTS:-}"
    echo "Next: ./scripts/create_miner_v2.sh --review-apply"
    ;;
  review)
    python3 scripts/auto_review_samples.py --apply
    echo "Next: ./scripts/create_miner_v2.sh --gen-yamls"
    ;;
  yamls)
    python3 scripts/generate_yamls_from_approved_samples.py $FORCE ${INTENT:+--intent "$INTENT"} ${SLUG:+--slug "$SLUG"}
    echo "Next: host YAMLs, then ./scripts/register-miner-v2.sh --file … --url … --sample …"
    ;;
  all)
    python3 scripts/auto_review_samples.py --apply || true
    python3 scripts/generate_yamls_from_approved_samples.py $FORCE
    echo "Done review+yamls. Host + register-miner-v2 for each approved slug."
    ;;
  *)
    echo "Pick: --capture | --review-apply | --gen-yamls | --all-from-research" >&2
    exit 1
    ;;
esac
