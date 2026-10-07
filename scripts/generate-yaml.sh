#!/usr/bin/env bash
# Generate a single-model CHAT_COMPLETION miner YAML from the template.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMPL="$ROOT/templates/chat-completion.miner.yaml.tmpl"
OUT_DIR="$ROOT/yaml"

ID=""
SLUG=""
NAME=""
MODEL=""
BASE_URL=""
INTENT="CHAT_COMPLETION"
DESCRIPTION=""
MODEL_DESCRIPTION=""

usage() {
  cat <<EOF
Usage: $(basename "$0") --id N --slug SLUG --name NAME --model MODEL --base-url URL [options]

Required:
  --id N              Unique numeric miner id (e.g. 9201)
  --slug SLUG         Unique slug (lowercase-hyphen)
  --name NAME         Display name
  --model MODEL       Exact OmniRoute model id (e.g. auto/cheap)
  --base-url URL      OmniRoute public base (no trailing /v1)

Optional:
  --intent INTENT     Default CHAT_COMPLETION
  --description TEXT  Miner description
  --model-description TEXT
  -h, --help
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
    --model-description) MODEL_DESCRIPTION="$2"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown arg: $1"; usage; exit 1 ;;
  esac
done

[[ -n "$ID" && -n "$SLUG" && -n "$NAME" && -n "$MODEL" && -n "$BASE_URL" ]] || {
  usage; exit 1
}

BASE_URL="${BASE_URL%/}"
BASE_URL="${BASE_URL%/v1}"
DESCRIPTION="${DESCRIPTION:-OpenAI-compatible chat via OmniRoute. Single model: ${MODEL}.}"
MODEL_DESCRIPTION="${MODEL_DESCRIPTION:-Pinned working chat model ${MODEL}}"

mkdir -p "$OUT_DIR"
OUT="$OUT_DIR/${SLUG}.yaml"

# Escape sed specials in replacement values carefully via python
python3 - "$TMPL" "$OUT" <<PY
import sys
from pathlib import Path
tmpl, out = Path(sys.argv[1]), Path(sys.argv[2])
text = tmpl.read_text()
repl = {
    "{{ID}}": """$ID""",
    "{{SLUG}}": """$SLUG""",
    "{{NAME}}": """$NAME""",
    "{{MODEL}}": """$MODEL""",
    "{{BASE_URL}}": """$BASE_URL""",
    "{{INTENT}}": """$INTENT""",
    "{{DESCRIPTION}}": """$DESCRIPTION""",
    "{{MODEL_DESCRIPTION}}": """$MODEL_DESCRIPTION""",
}
for k, v in repl.items():
    text = text.replace(k, v)
out.write_text(text)
print(out)
PY

echo "Wrote $OUT"
# Gate: catch unquoted `: ` / missing label_field / Group D static before anyone hosts this file
python3 "$ROOT/scripts/validate_miner_yaml.py" "$OUT" || {
  echo "FATAL: generated YAML failed validate_miner_yaml.py" >&2
  exit 1
}
python3 "$ROOT/scripts/preflight_miner.py" --file "$OUT" --skip-live || {
  echo "FATAL: generated YAML failed preflight static rules (Groups A–D)" >&2
  exit 1
}
