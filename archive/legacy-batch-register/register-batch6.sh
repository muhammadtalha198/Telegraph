#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
set -a; source .env; set +a
unset HTTP_PROXY HTTPS_PROXY http_proxy https_proxy ALL_PROXY all_proxy SOCKS_PROXY SOCKS5_PROXY || true

DIAMOND="${DIAMOND:-0x5a2324aA18613FAD4e44bDF0d6c73Ec1f6D87ff8}"
RPC_URL="${RPC_URL:-https://sepolia.base.org}"
MIN_PRICE_USDC="${MIN_PRICE_USDC:-10000}"
HOST_YAML=https://omni-chat.13.237.89.59.sslip.io/miner-yamls
REPORT=out/batch6-register.jsonl
mkdir -p out
: > "$REPORT"

pairs=(
  "intentYamls/dns-lookup/dns-cloudflare.yaml|DNS_RECORD_LOOKUP|dns-cloudflare"
  "intentYamls/dns-lookup/dns-google.yaml|DNS_RECORD_LOOKUP|dns-google"
  "intentYamls/dns-lookup/dns-adguard.yaml|DNS_RECORD_LOOKUP|dns-adguard"
  "intentYamls/dns-lookup/dns-nextdns.yaml|DNS_RECORD_LOOKUP|dns-nextdns"
  "intentYamls/dns-lookup/dns-dnssb.yaml|DNS_RECORD_LOOKUP|dns-dnssb"
  "intentYamls/dns-lookup/dns-rethink.yaml|DNS_RECORD_LOOKUP|dns-rethink"
  "intentYamls/ssl-verification/ssl-certspotter.yaml|SSL_VERIFICATION|ssl-certspotter"
  "intentYamls/ssl-verification/ssl-crtsh.yaml|SSL_VERIFICATION|ssl-crtsh"
  "intentYamls/port-scan-audit/prt-internetdb.yaml|PORT_SCAN_AUDIT|prt-internetdb"
  "intentYamls/port-scan-audit/prt-checkhost.yaml|PORT_SCAN_AUDIT|prt-checkhost"
  "intentYamls/threat-intel/tif-cymru.yaml|THREAT_INTELLIGENCE|tif-cymru"
  "intentYamls/threat-intel/tif-feodo.yaml|THREAT_INTELLIGENCE|tif-feodo"
  "intentYamls/threat-intel/tif-urlhaus.yaml|THREAT_INTELLIGENCE|tif-urlhaus"
  "intentYamls/air-quality/aqi-openmeteo.yaml|AIR_QUALITY_INDEX|aqi-openmeteo"
  "intentYamls/air-quality/aqi-uba.yaml|AIR_QUALITY_INDEX|aqi-uba"
  "intentYamls/air-quality/aqi-luchtmeetnet.yaml|AIR_QUALITY_INDEX|aqi-luchtmeetnet"
  "intentYamls/air-quality/aqi-neasg.yaml|AIR_QUALITY_INDEX|aqi-neasg"
  "intentYamls/air-quality/aqi-sensorcommunity.yaml|AIR_QUALITY_INDEX|aqi-sensorcommunity"
  "intentYamls/weather-forecast-verify/wnd-era5.yaml|WEATHER_FORECAST_VERIFY|wnd-era5"
  "intentYamls/weather-forecast-verify/wnd-brightsky.yaml|WEATHER_FORECAST_VERIFY|wnd-brightsky"
  "intentYamls/weather-forecast-verify/wnd-metar.yaml|WEATHER_FORECAST_VERIFY|wnd-metar"
  "intentYamls/weather-forecast-verify/wnd-envcanada.yaml|WEATHER_FORECAST_VERIFY|wnd-envcanada"
  "intentYamls/weather-forecast-verify/wnd-jma.yaml|WEATHER_FORECAST_VERIFY|wnd-jma"
  "intentYamls/gas-price/gas-metamask.yaml|GAS_PRICE|gas-metamask"
  "intentYamls/gas-price/gas-polygon.yaml|GAS_PRICE|gas-polygon"
  "intentYamls/token-supply/sup-drpc.yaml|TOKEN_TOTAL_SUPPLY_VERIFY|sup-drpc"
  "intentYamls/token-supply/sup-solana.yaml|TOKEN_TOTAL_SUPPLY_VERIFY|sup-solana"
  "intentYamls/validator-performance/vlp-publicnode.yaml|VALIDATOR_PERFORMANCE_VERIFY|vlp-publicnode"
  "intentYamls/validator-performance/vlp-quicknode.yaml|VALIDATOR_PERFORMANCE_VERIFY|vlp-quicknode"
  "intentYamls/loan-rate/lnr-freddie.yaml|LOAN_INTEREST_RATE_QUOTE|lnr-freddie"
  "intentYamls/loan-rate/lnr-fred.yaml|LOAN_INTEREST_RATE_QUOTE|lnr-fred"
  "intentYamls/loan-rate/lnr-boc.yaml|LOAN_INTEREST_RATE_QUOTE|lnr-boc"
  "intentYamls/loan-rate/lnr-ecb.yaml|LOAN_INTEREST_RATE_QUOTE|lnr-ecb"
  "intentYamls/loan-rate/lnr-boe.yaml|LOAN_INTEREST_RATE_QUOTE|lnr-boe"
  "intentYamls/loan-rate/lnr-bcb.yaml|LOAN_INTEREST_RATE_QUOTE|lnr-bcb"
  "intentYamls/api-health/hlt-checkhost.yaml|API_HEALTH_CHECK|hlt-checkhost"
  "intentYamls/server-uptime/upt-checkhost.yaml|SERVER_UPTIME_MONITOR|upt-checkhost"
  "intentYamls/api-health/hlt-hackertarget.yaml|API_HEALTH_CHECK|hlt-hackertarget"
  "intentYamls/server-uptime/upt-hackertarget.yaml|SERVER_UPTIME_MONITOR|upt-hackertarget"
  "intentYamls/cloud-resource/prm-promlabs.yaml|CLOUD_RESOURCE_USAGE|prm-promlabs"
  "intentYamls/cloud-resource/prm-prometheusio.yaml|CLOUD_RESOURCE_USAGE|prm-prometheusio"
  "intentYamls/sensor-telemetry/sen-sensorcommunity.yaml|SENSOR_TELEMETRY_VERIFY|sen-sensorcommunity"
  "intentYamls/sensor-telemetry/sen-usgs.yaml|SENSOR_TELEMETRY_VERIFY|sen-usgs"
  "intentYamls/sensor-telemetry/sen-coops.yaml|SENSOR_TELEMETRY_VERIFY|sen-coops"
  "intentYamls/sensor-telemetry/sen-thingspeak.yaml|SENSOR_TELEMETRY_VERIFY|sen-thingspeak"
  "intentYamls/sensor-telemetry/sen-ndbc.yaml|SENSOR_TELEMETRY_VERIFY|sen-ndbc"
  "intentYamls/vessel-telemetry/ves-digitraffic.yaml|VESSEL_TELEMETRY_VERIFY|ves-digitraffic"
  "intentYamls/carrier-serviceability/car-indiapost.yaml|CARRIER_SERVICEABILITY|car-indiapost"
  "intentYamls/carrier-serviceability/car-auspost.yaml|CARRIER_SERVICEABILITY|car-auspost"
  "intentYamls/vendor-verify/vnd-vies.yaml|VENDOR_VERIFY|vnd-vies"
  "intentYamls/vendor-verify/vnd-brreg.yaml|VENDOR_VERIFY|vnd-brreg"
  "intentYamls/vendor-verify/vnd-openiban.yaml|VENDOR_VERIFY|vnd-openiban"
  "intentYamls/grammar-spell/grm-languagetool.yaml|GRAMMAR_SPELL_CHECK|grm-languagetool"
  "intentYamls/grammar-spell/grm-yandex.yaml|GRAMMAR_SPELL_CHECK|grm-yandex"
  "intentYamls/regression-verify/rgr-paiza.yaml|REGRESSION_VERIFY|rgr-paiza"
  "intentYamls/content-extraction/cex-jina.yaml|CONTENT_EXTRACTION|cex-jina"
  "intentYamls/content-extraction/cex-urltomarkdown.yaml|CONTENT_EXTRACTION|cex-urltomarkdown"
  "intentYamls/sentiment-analysis/snt-textprocessing.yaml|SENTIMENT_ANALYSIS|snt-textprocessing"
  "intentYamls/sentiment-analysis/snt-twinword.yaml|SENTIMENT_ANALYSIS|snt-twinword"
  "intentYamls/web-search/srch-marginalia.yaml|WEB_SEARCH|srch-marginalia"
)

echo "block=$(cast block-number --rpc-url "$RPC_URL")"
echo "count=${#pairs[@]}"
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

python3 <<'PY2'
import json, subprocess, os
from pathlib import Path
RPC=os.environ.get("RPC_URL","https://sepolia.base.org")
rows=[]
for line in Path("out/batch6-register.jsonl").read_text().splitlines():
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
Path("out/batch6-register.json").write_text(json.dumps(rows, indent=2))
PY2
