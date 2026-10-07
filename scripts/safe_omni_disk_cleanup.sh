#!/usr/bin/env bash
# Safe disk cleanup on omni-chat host (13.237.89.59).
# KEEP: nginx, miner-yamls, semantic-truth-proxy /truth/*
# FREE: LiteLLM/OmniRoute LLM caches, Docker junk, journal/logs, apt cache
#
# Usage (on the server as ubuntu):
#   bash safe_omni_disk_cleanup.sh
#   bash safe_omni_disk_cleanup.sh --aggressive   # also prune unused docker images
set -euo pipefail

AGGRESSIVE=0
[[ "${1:-}" == "--aggressive" ]] && AGGRESSIVE=1

echo "=== BEFORE ==="
df -h / | tee /tmp/disk-before.txt
echo

# --- protect paths we must never delete ---
KEEP_HINTS=(
  miner-yamls
  response-yamls
  semantic-truth
  truth-proxy
  nginx
)

echo "=== Services (will NOT stop nginx / truth proxy) ==="
systemctl is-active nginx 2>/dev/null || true
docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Size}}' 2>/dev/null || true
echo

echo "=== Largest dirs (top) ==="
sudo du -xh --max-depth=1 / 2>/dev/null | sort -hr | head -15 || true
sudo du -xh --max-depth=2 /var /home /opt /tmp 2>/dev/null | sort -hr | head -25 || true
echo

# --- journal logs ---
echo "=== Truncate systemd journal (keep 3 days / 200M) ==="
sudo journalctl --vacuum-time=3d || true
sudo journalctl --vacuum-size=200M || true

# --- common log files ---
echo "=== Truncate large rotated logs (not delete nginx config) ==="
sudo find /var/log -type f \( -name '*.gz' -o -name '*.1' -o -name '*.old' \) -mtime +7 -print -delete 2>/dev/null || true
sudo find /var/log -type f -name '*.log' -size +50M -exec truncate -s 0 {} \; -print 2>/dev/null || true

# --- apt cache ---
echo "=== apt clean ==="
sudo apt-get clean -y || true
sudo rm -rf /var/cache/apt/archives/*.deb 2>/dev/null || true

# --- tmp ---
echo "=== /tmp old files (>3 days) ==="
sudo find /tmp -xdev -type f -mtime +3 -print -delete 2>/dev/null || true
sudo find /var/tmp -xdev -type f -mtime +7 -print -delete 2>/dev/null || true

# --- LiteLLM / OmniRoute LLM caches (safe: not miner-yamls) ---
echo "=== LiteLLM / HuggingFace / model caches ==="
for d in \
  /home/ubuntu/.cache/huggingface \
  /home/ubuntu/.cache/litellm \
  /home/ubuntu/.cache/pip \
  /root/.cache/huggingface \
  /root/.cache/litellm \
  /root/.cache/pip \
  /var/lib/litellm \
  /opt/litellm \
  /home/ubuntu/litellm \
  /home/ubuntu/OmniRoute \
  /home/ubuntu/omniroute \
  /opt/omniroute
do
  if [[ -d "$d" ]]; then
    echo "found $d ($(sudo du -sh "$d" 2>/dev/null | awk '{print $1}'))"
  fi
done

# Only delete cache dirs — never whole OmniRoute app tree if it also hosts proxy
for d in \
  /home/ubuntu/.cache/huggingface \
  /home/ubuntu/.cache/litellm \
  /home/ubuntu/.cache/pip \
  /root/.cache/huggingface \
  /root/.cache/litellm \
  /root/.cache/pip
do
  if [[ -d "$d" ]]; then
    echo "REMOVING cache $d"
    sudo rm -rf "$d"
  fi
done

# Docker LiteLLM-related stopped containers / unused build cache
if command -v docker >/dev/null 2>&1; then
  echo "=== Docker cleanup (safe) ==="
  docker system df || true
  # prune build cache + dangling images/containers/networks (keeps used images)
  docker builder prune -af || true
  docker container prune -f || true
  docker network prune -f || true
  docker volume prune -f || true
  docker image prune -f || true

  if [[ "$AGGRESSIVE" == "1" ]]; then
    echo "=== Aggressive: remove unused images (running containers' images kept) ==="
    docker image prune -af || true
  fi

  # Stop LiteLLM-only containers if named clearly — DO NOT stop nginx/proxy/yaml hosts
  echo "=== Candidate LLM containers (review; stop only litellm/ollama/vllm) ==="
  docker ps -a --format '{{.Names}} {{.Image}}' | grep -Ei 'litellm|ollama|vllm|open-webui|text-generation' || echo '(none matched)'
  while read -r name; do
    [[ -z "$name" ]] && continue
    echo "Stopping LLM container: $name"
    docker stop "$name" || true
    docker rm "$name" || true
  done < <(docker ps -a --format '{{.Names}}' | grep -Ei '^(litellm|ollama|vllm|open-webui)' || true)
fi

# Snap old revisions
if command -v snap >/dev/null 2>&1; then
  echo "=== snap old revisions ==="
  sudo sh -c 'snap list --all | awk "/disabled/{print \$1, \$3}" | while read n r; do snap remove "$n" --revision="$r"; done' || true
fi

echo
echo "=== AFTER ==="
df -h / | tee /tmp/disk-after.txt
echo
echo "VERIFY miner-yamls / truth still up (from this host):"
curl -sS -m 5 -o /dev/null -w 'miner-yamls=%{http_code}\n' http://127.0.0.1/miner-yamls/ 2>/dev/null || \
  curl -sS -m 5 -o /dev/null -w 'miner-yamls_ssl=%{http_code}\n' https://127.0.0.1/miner-yamls/ -k 2>/dev/null || true
systemctl is-active nginx 2>/dev/null || true
echo "DONE — kept nginx + miner-yamls + truth proxy paths."
