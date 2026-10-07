#!/usr/bin/env bash
# Host a YAML file publicly. Prefers Dropbox; optional paste.rs fallback.
# Prints: YAML_URL=<public raw url>
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# shellcheck disable=SC1091
[[ -f "$ROOT/.env" ]] && set -a && source "$ROOT/.env" && set +a

FILE="${1:-}"
[[ -f "$FILE" ]] || { echo "Usage: $(basename "$0") path/to/miner.yaml" >&2; exit 1; }

ABS="$(cd "$(dirname "$FILE")" && pwd)/$(basename "$FILE")"
NAME="$(basename "$ABS")"

upload_dropbox() {
  local token="$DROPBOX_ACCESS_TOKEN"
  [[ -n "${token:-}" ]] || return 1

  local dest="/MinerCreator/${NAME}"
  echo "Uploading to Dropbox: $dest" >&2

  curl -sS -X POST https://content.dropboxapi.com/2/files/upload \
    -H "Authorization: Bearer $token" \
    -H "Content-Type: application/octet-stream" \
    -H "Dropbox-API-Arg: {\"path\":\"${dest}\",\"mode\":\"overwrite\",\"autorename\":false,\"mute\":false}" \
    --data-binary @"$ABS" >/tmp/dbx-upload.json

  if grep -q '"error"' /tmp/dbx-upload.json 2>/dev/null; then
    echo "Dropbox upload failed:" >&2
    cat /tmp/dbx-upload.json >&2
    return 1
  fi

  # Create or reuse shared link
  local link_json link
  link_json=$(curl -sS -X POST https://api.dropboxapi.com/2/sharing/create_shared_link_with_settings \
    -H "Authorization: Bearer $token" \
    -H "Content-Type: application/json" \
    -d "{\"path\":\"${dest}\",\"settings\":{\"requested_visibility\":\"public\",\"audience\":\"public\",\"access\":\"viewer\"}}" || true)

  if echo "$link_json" | grep -q '"shared_link_already_exists"'; then
    link_json=$(curl -sS -X POST https://api.dropboxapi.com/2/sharing/list_shared_links \
      -H "Authorization: Bearer $token" \
      -H "Content-Type: application/json" \
      -d "{\"path\":\"${dest}\",\"direct_only\":true}")
    link=$(python3 -c "import json,sys; d=json.load(sys.stdin); print(d['links'][0]['url'])" <<<"$link_json")
  else
    link=$(python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('url',''))" <<<"$link_json")
  fi

  [[ -n "$link" ]] || { echo "No Dropbox shared link" >&2; cat <<<"$link_json" >&2; return 1; }

  # Force raw download so node hash matches file bytes
  if [[ "$link" == *\?* ]]; then
    link="${link%%\?*}?dl=1"
  else
    link="${link}?dl=1"
  fi
  # Also normalize www.dropbox.com → dl.dropboxusercontent is handled by ?dl=1 redirect

  echo "Verifying Dropbox raw fetch..." >&2
  curl -sSL -m 30 -A "Go-http-client/1.1" "$link" -o /tmp/dbx-fetched.yaml
  if ! cmp -s "$ABS" /tmp/dbx-fetched.yaml; then
    # try raw=1
    link="${link/dl=1/raw=1}"
    curl -sSL -m 30 -A "Go-http-client/1.1" "$link" -o /tmp/dbx-fetched.yaml
  fi
  if ! cmp -s "$ABS" /tmp/dbx-fetched.yaml; then
    echo "ERROR: Dropbox fetched bytes != local YAML (hash would mismatch)." >&2
    echo "Local:  $(shasum -a 256 "$ABS")" >&2
    echo "Remote: $(shasum -a 256 /tmp/dbx-fetched.yaml)" >&2
    head -c 120 /tmp/dbx-fetched.yaml >&2; echo >&2
    return 1
  fi

  echo "YAML_URL=$link"
}

upload_omni() {
  local prefix="${HOST_PREFIX_CHAT:-}"
  [[ -n "$prefix" ]] || return 1
  prefix="${prefix%/}"
  local url="${prefix}/${NAME}"
  echo "Checking omni-chat hosted YAML: $url" >&2
  if curl -sSL -m 30 -A "Go-http-client/1.1" "$url" -o /tmp/omni-fetched.yaml 2>/dev/null \
    && cmp -s "$ABS" /tmp/omni-fetched.yaml; then
    echo "YAML_URL=$url"
    return 0
  fi
  if [[ -n "${OMNI_YAML_SYNC_CMD:-}" ]]; then
    echo "Running OMNI_YAML_SYNC_CMD for $NAME" >&2
    # shellcheck disable=SC2086
    OMNI_YAML_LOCAL="$ABS" OMNI_YAML_NAME="$NAME" bash -lc "$OMNI_YAML_SYNC_CMD" || return 1
    curl -sSL -m 30 -A "Go-http-client/1.1" "$url" -o /tmp/omni-fetched.yaml
    cmp -s "$ABS" /tmp/omni-fetched.yaml || { echo "omni byte mismatch after sync" >&2; return 1; }
    echo "YAML_URL=$url"
    return 0
  fi
  return 1
}

upload_paste() {
  echo "Dropbox token missing — using paste.rs fallback (set DROPBOX_ACCESS_TOKEN for Dropbox)." >&2
  local url attempt
  for attempt in 1 2 3 4 5; do
    url=$(curl -sS -m 45 --data-binary @"$ABS" https://paste.rs)
    [[ "$url" == https://* ]] || {
      echo "paste.rs attempt $attempt failed: ${url:0:120}" >&2
      sleep $((attempt * 3))
      continue
    }
    curl -sS -m 20 -A "Go-http-client/1.1" "$url" -o /tmp/paste-fetched.yaml
    if cmp -s "$ABS" /tmp/paste-fetched.yaml; then
      echo "YAML_URL=$url"
      return 0
    fi
    echo "paste.rs byte mismatch attempt $attempt" >&2
    sleep $((attempt * 3))
  done
  # secondary public paste host
  echo "Trying 0x0.st fallback…" >&2
  url=$(curl -sS -m 45 -F "file=@${ABS}" https://0x0.st)
  [[ "$url" == https://* ]] || { echo "0x0.st failed: $url" >&2; return 1; }
  curl -sS -m 20 -A "Go-http-client/1.1" "$url" -o /tmp/paste-fetched.yaml
  cmp -s "$ABS" /tmp/paste-fetched.yaml || { echo "0x0.st byte mismatch" >&2; return 1; }
  echo "YAML_URL=$url"
}

if [[ -n "${DROPBOX_ACCESS_TOKEN:-}" ]]; then
  upload_dropbox
elif upload_omni; then
  :
elif [[ "${ALLOW_PASTE_FALLBACK:-true}" == "true" ]]; then
  upload_paste
else
  echo "ERROR: no host path (Dropbox / omni / paste)" >&2
  exit 1
fi
