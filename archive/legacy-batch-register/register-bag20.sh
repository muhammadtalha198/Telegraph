#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
set -a; source .env; set +a
# Drop Cursor sandbox proxies that break cast/curl (after .env)
unset HTTP_PROXY HTTPS_PROXY http_proxy https_proxy ALL_PROXY all_proxy SOCKS_PROXY SOCKS5_PROXY || true

DIAMOND="${DIAMOND:-0x5a2324aA18613FAD4e44bDF0d6c73Ec1f6D87ff8}"
RPC_URL="${RPC_URL:-https://sepolia.base.org}"
MIN_PRICE_USDC="${MIN_PRICE_USDC:-10000}"
HOST_YAML=https://omni-chat.13.237.89.59.sslip.io/miner-yamls
REPORT=out/bag20-register.jsonl
: > "$REPORT"

pairs=(
  "intentYamls/payment-method/pay-bin-scheme.yaml|PAYMENT_METHOD_VERIFY|pay-bin-scheme"
  "intentYamls/payment-method/pay-handyapi-scheme.yaml|PAYMENT_METHOD_VERIFY|pay-handyapi-scheme"
  "intentYamls/sanctions-screening/san-ofac-entity.yaml|SANCTIONS_SCREENING_MATCH|san-ofac-entity"
  "intentYamls/sanctions-screening/san-un-list.yaml|SANCTIONS_SCREENING_MATCH|san-un-list"
  "intentYamls/corporate-registry/corp-gleif-status.yaml|CORPORATE_REGISTRY_LOOKUP|corp-gleif-status"
  "intentYamls/corporate-registry/corp-fr-recherche.yaml|CORPORATE_REGISTRY_LOOKUP|corp-fr-recherche"
  "intentYamls/regulatory-filing/reg-sec-edgar.yaml|REGULATORY_FILING_MONITOR|reg-sec-edgar"
  "intentYamls/crypto-price/crypto-coinbase.yaml|CRYPTO_PRICE_LOOKUP|crypto-coinbase"
  "intentYamls/crypto-price/crypto-kraken.yaml|CRYPTO_PRICE_LOOKUP|crypto-kraken"
  "intentYamls/crypto-price/crypto-binance.yaml|CRYPTO_PRICE_LOOKUP|crypto-binance"
  "intentYamls/crypto-price/crypto-bitstamp.yaml|CRYPTO_PRICE_LOOKUP|crypto-bitstamp"
  "intentYamls/crypto-price/crypto-gemini.yaml|CRYPTO_PRICE_LOOKUP|crypto-gemini"
  "intentYamls/crypto-transfer/ctx-tx-receipt.yaml|CRYPTO_TRANSFER_VERIFY|ctx-tx-receipt"
)

echo "block=$(cast block-number --rpc-url "$RPC_URL")"
for row in "${pairs[@]}"; do
  IFS='|' read -r file intent slug <<<"$row"
  echo "=== $slug ==="
  url="$HOST_YAML/${slug}.yaml"
  curl -sSL -m 30 -A "Go-http-client/1.1" "$url" -o "/tmp/reg-$slug.yaml"
  cmp -s "$file" "/tmp/reg-$slug.yaml" || { echo "YAML mismatch $slug"; exit 1; }
  YAML_HASH="0x$(shasum -a 256 "$file" | awk '{print $1}')"
  INTENTS_JSON=$(python3 -c "import json,sys; print(json.dumps([sys.argv[1]]))" "$intent")
  OUT=$(cast send "$DIAMOND" \
    "registerMiner(string,bytes32,address,uint256,string[])" \
    "$url" "$YAML_HASH" "$FEE_ADDRESS" "$MIN_PRICE_USDC" "$INTENTS_JSON" \
    --rpc-url "$RPC_URL" --private-key "$MINER_PRIVATE_KEY" --json)
  echo "$OUT" > "/tmp/cast-$slug.json"
  python3 -c "import json; from pathlib import Path; out=json.loads(Path('/tmp/cast-$slug.json').read_text()); rec={'slug':'$slug','intent':'$intent','tx_hash':out.get('transactionHash'),'tx_status':out.get('status'),'yaml_url':'$url','yaml_hash':'$YAML_HASH'}; Path('$REPORT').open('a').write(json.dumps(rec)+chr(10)); print(rec['slug'], rec['tx_hash'], rec['tx_status'])"
  sleep 2
done

python3 <<'PY'
import json, subprocess, os
from pathlib import Path
RPC=os.environ.get("RPC_URL","https://sepolia.base.org")
rows=[]
for line in Path("out/bag20-register.jsonl").read_text().splitlines():
    r=json.loads(line)
    tx=r["tx_hash"]
    out=subprocess.check_output(["cast","receipt",tx,"--rpc-url",RPC,"--json"], text=True)
    rec=json.loads(out)
    reg_id=None
    for log in rec.get("logs") or []:
        topics=log.get("topics") or []
        if len(topics)>=2:
            try:
                rid=int(topics[1],16)
                if 2000 < rid < 100000:
                    reg_id=rid
            except Exception:
                pass
    r["reg_id"]=reg_id
    r["receipt_status"]=rec.get("status")
    rows.append(r)
    print(r["slug"], "reg_id", reg_id, "status", rec.get("status"))
Path("out/bag20-register.json").write_text(json.dumps(rows, indent=2))
PY
