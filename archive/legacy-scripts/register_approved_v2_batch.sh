#!/usr/bin/env bash
# Register all APPROVED V2 samples that have local YAMLs.
# Per miner: upload-host.sh → register-miner-v2.sh (fail-closed gates, no bypass).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
# shellcheck disable=SC1091
[[ -f "$ROOT/.env" ]] && set -a && source "$ROOT/.env" && set +a

LOG="$ROOT/out/V2_REGISTER_BATCH-$(date -u +%Y-%m-%d).log"
REPORT="$ROOT/out/V2_REGISTER_BATCH.jsonl"
mkdir -p "$ROOT/out"
: >"$REPORT"
echo "=== V2 batch register $(date -u +%Y-%m-%dT%H:%M:%SZ) ===" | tee "$LOG"

mapfile -t ROWS < <(python3 - <<'PY'
from pathlib import Path
import re
INTENT_DIR = {
    "LIQUIDITY_DEPTH_VERIFY": "liquidity-depth",
    "ONCHAIN_METRIC_VERIFY": "onchain-metric",
    "EVENT_OUTCOME_RESOLUTION": "event-outcome",
    "SECURITY_REVIEW": "security-review",
    "VULNERABILITY_TRIAGE": "vulnerability-triage",
    "CODE_PATCH_VERIFY": "code-patch",
    "OPTIMAL_EXECUTION_ROUTE": "optimal-execution",
    "CROSS_CHAIN_STATE_VERIFY": "cross-chain-state",
}
for p in sorted(Path("apiOutputSamples").rglob("*.md")):
    if p.name in ("_TEMPLATE.md", "README.md"):
        continue
    t = p.read_text(encoding="utf-8", errors="replace")
    if not re.search(r"(?m)^status:\s*approved\s*$", t):
        continue
    intent = re.search(r"(?m)^intent:\s*(\S+)", t)
    slug = re.search(r"(?m)^slug:\s*(\S+)", t)
    if not intent or not slug:
        continue
    intent, slug = intent.group(1), slug.group(1)
    folder = INTENT_DIR.get(intent)
    if not folder:
        continue
    y = Path("intentYamls") / folder / f"{slug}.yaml"
    if not y.is_file():
        print(f"MISSING_YAML\t{intent}\t{slug}", flush=True)
        continue
    print(f"OK\t{intent}\t{slug}\t{y}\t{p}", flush=True)
PY
)

ok=0
fail=0
skip=0
total=0
for row in "${ROWS[@]}"; do
  IFS=$'\t' read -r status intent slug ypath spath <<<"$row"
  if [[ "$status" != "OK" ]]; then
    echo "SKIP  $row" | tee -a "$LOG"
    skip=$((skip + 1))
    continue
  fi
  total=$((total + 1))
  echo "" | tee -a "$LOG"
  echo "[$total] REGISTER $intent/$slug" | tee -a "$LOG"

  if ! HOST_OUT=$(./scripts/upload-host.sh "$ypath" 2>>"$LOG"); then
    echo "FAIL  host $slug" | tee -a "$LOG"
    echo "{\"slug\":\"$slug\",\"intent\":\"$intent\",\"ok\":false,\"stage\":\"host\"}" >>"$REPORT"
    fail=$((fail + 1))
    continue
  fi
  YAML_URL=$(echo "$HOST_OUT" | sed -n 's/^YAML_URL=//p' | tail -1)
  if [[ -z "$YAML_URL" ]]; then
    echo "FAIL  no YAML_URL $slug" | tee -a "$LOG"
    echo "{\"slug\":\"$slug\",\"intent\":\"$intent\",\"ok\":false,\"stage\":\"host_url\"}" >>"$REPORT"
    fail=$((fail + 1))
    continue
  fi
  echo "HOST  $YAML_URL" | tee -a "$LOG"

  if ./scripts/register-miner-v2.sh --file "$ypath" --url "$YAML_URL" --sample "$spath" >>"$LOG" 2>&1; then
    echo "PASS  $slug" | tee -a "$LOG"
    # append last registration snippet
    python3 - <<PY >>"$REPORT"
import json
from pathlib import Path
p = Path("out/last-registration-v2.json")
d = json.loads(p.read_text()) if p.is_file() else {}
d.update({"slug": "$slug", "intent": "$intent", "ok": True, "yaml_url": "$YAML_URL"})
print(json.dumps(d))
PY
    ok=$((ok + 1))
  else
    echo "FAIL  register $slug" | tee -a "$LOG"
    echo "{\"slug\":\"$slug\",\"intent\":\"$intent\",\"ok\":false,\"stage\":\"register\",\"yaml_url\":\"$YAML_URL\"}" >>"$REPORT"
    fail=$((fail + 1))
  fi
  # gentle pacing for paste.rs / RPC
  sleep 2
done

echo "" | tee -a "$LOG"
echo "=== DONE ok=$ok fail=$fail skip=$skip total_attempted=$total ===" | tee -a "$LOG"
python3 - <<PY
from pathlib import Path
import json
rows=[]
for line in Path("$REPORT").read_text().splitlines():
    if line.strip():
        rows.append(json.loads(line))
ok=[r for r in rows if r.get("ok")]
bad=[r for r in rows if not r.get("ok")]
md=["# V2 register batch", "", f"ok **{len(ok)}** · fail **{len(bad)}**", "", "## Registered", ""]
for r in ok:
    md.append(f"- `{r.get('intent')}/{r.get('slug')}` id≈{r.get('new_registration_id')} · [tx]({r.get('tx_url','')})")
md += ["", "## Failed", ""]
for r in bad:
    md.append(f"- `{r.get('intent')}/{r.get('slug')}` stage={r.get('stage')}")
Path("out/V2_REGISTER_BATCH.md").write_text("\n".join(md)+"\n")
print("WROTE out/V2_REGISTER_BATCH.md")
PY
