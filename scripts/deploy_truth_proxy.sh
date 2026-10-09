#!/usr/bin/env bash
# Deploy scripts/semantic-truth-proxy.py to the Omni host and keep it supervised.
#
# Why: the proxy behind /truth/* (141 YAMLs) ran as a bare `python3` process — no systemd,
# no @reboot. A crash or reboot silently took those miners down. First run installs a
# systemd unit (Restart=always) and carries over the env vars the live process had.
#
#   ./scripts/deploy_truth_proxy.sh            # deploy + health check, auto-rollback on failure
#   ./scripts/deploy_truth_proxy.sh --dry-run  # show what would happen, change nothing
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
[[ -f "$ROOT/.env" ]] && set -a && source "$ROOT/.env" && set +a
KEY="${OMNI_SSH_KEY:?set OMNI_SSH_KEY in .env}"
TARGET="${OMNI_SSH_TARGET:-ubuntu@13.237.89.59}"
LOCAL="$ROOT/scripts/semantic-truth-proxy.py"
DRY=0; [[ "${1:-}" == "--dry-run" ]] && DRY=1
SSH=(ssh -i "$KEY" -o StrictHostKeyChecking=accept-new -o ConnectTimeout=15 "$TARGET")

python3 -m py_compile "$LOCAL"
LOCAL_MD5=$(python3 -c "import hashlib,sys;print(hashlib.md5(open(sys.argv[1],'rb').read()).hexdigest())" "$LOCAL")
echo "local md5:  $LOCAL_MD5"
echo "server md5: $("${SSH[@]}" "md5sum /home/ubuntu/semantic-truth-proxy.py | cut -d' ' -f1")"
if [[ $DRY == 1 ]]; then
  "${SSH[@]}" "systemctl is-active semantic-truth-proxy 2>/dev/null || echo 'no systemd unit yet (bare process will be migrated)'; pgrep -af semantic-truth-proxy.py || echo 'no running proxy!'"
  echo "DRY RUN — nothing changed."; exit 0
fi

scp -q -i "$KEY" -o StrictHostKeyChecking=accept-new "$LOCAL" "$TARGET:/home/ubuntu/semantic-truth-proxy.py.new"
"${SSH[@]}" "LOCAL_MD5=$LOCAL_MD5 bash -s" <<'REMOTE'
set -euo pipefail
cd /home/ubuntu
P=semantic-truth-proxy.py; UNIT=/etc/systemd/system/semantic-truth-proxy.service; ENVF=/home/ubuntu/semantic-truth-proxy.env
[[ "$(md5sum $P.new | cut -d' ' -f1)" == "$LOCAL_MD5" ]] || { echo "upload corrupted"; exit 1; }
python3 -m py_compile $P.new
TS=$(date -u +%Y%m%dT%H%M%SZ); cp -p $P $P.bak-$TS; echo "backup: $P.bak-$TS"

if [[ ! -f $UNIT ]]; then
  # carry over only the vars the proxy reads, from the live bare process
  PID=$(pgrep -f "python3 /home/ubuntu/$P" | head -1 || true)
  umask 077; : > $ENVF
  if [[ -n "$PID" ]]; then
    sudo cat /proc/$PID/environ | tr '\0' '\n' \
      | grep -E '^(ABUSEIPDB_API_KEY|CINS_CACHE|GREYNOISE_CACHE|HF_TOKEN|HUGGINGFACE_HUB_TOKEN|OFAC_SDN_CACHE|STRIPE_SECRET_KEY|STRIPE_TEST_CHARGE_ID|UN_SDN_CACHE|TRUTH_ALLOW_SUBSTITUTES)=' >> $ENVF || true
  fi
  umask 022
  echo "env carried over: $(cut -d= -f1 $ENVF | tr '\n' ' ')"
  sudo tee $UNIT >/dev/null <<UNITEOF
[Unit]
Description=Telegraph semantic truth proxy (/truth/* on :8765)
After=network-online.target
Wants=network-online.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu
EnvironmentFile=-$ENVF
ExecStart=/usr/bin/python3 -u /home/ubuntu/$P
Restart=always
RestartSec=3
StandardOutput=append:/home/ubuntu/semantic-truth-proxy.log
StandardError=append:/home/ubuntu/semantic-truth-proxy.log

[Install]
WantedBy=multi-user.target
UNITEOF
  sudo systemctl daemon-reload
  sudo systemctl enable semantic-truth-proxy >/dev/null
  mv $P.new $P
  pkill -f "python3 /home/ubuntu/$P" || true   # stop the bare process; port must be free
  sleep 1
  sudo systemctl start semantic-truth-proxy
else
  mv $P.new $P
  sudo systemctl restart semantic-truth-proxy
fi

ok=0
for i in $(seq 1 15); do
  if curl -fsS -m 3 http://127.0.0.1:8765/health >/dev/null 2>&1; then ok=1; break; fi; sleep 1
done
if [[ $ok != 1 ]]; then
  echo "HEALTH FAILED — rolling back to $P.bak-$TS"
  cp -p $P.bak-$TS $P; sudo systemctl restart semantic-truth-proxy; sleep 2
  curl -fsS -m 3 http://127.0.0.1:8765/health && echo " (rolled back, healthy)"
  exit 1
fi
echo "health ok; service: $(systemctl is-active semantic-truth-proxy), enabled: $(systemctl is-enabled semantic-truth-proxy)"
REMOTE

echo "--- public smoke (through nginx)"
for q in "aq-pm25?venue=openmeteo&site=52.52,13.41" "aq-pm25?venue=uba&site=52.52,13.41" "aq-pm25?venue=sensorcommunity&site=52.52,13.41" "aq-pm25?venue=luchtmeetnet&site=52.52,13.41"; do
  printf "  %-55s " "$q"; curl -sS -m 30 "https://omni-chat.13.237.89.59.sslip.io/truth/$q" | head -c 140; echo
done
echo "(luchtmeetnet is expected to refuse the Berlin pin)"
