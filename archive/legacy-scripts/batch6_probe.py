"""Probe every Batch 6 venue twice with each pin; prints one line per call."""
import importlib.util
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor

spec = importlib.util.spec_from_file_location("stp", sys.argv[1] if len(sys.argv) > 1 else "/tmp/stp_test.py")
stp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stp)

LABEL = {
    "dns_has": "has_record", "ssl_not_after": "not_after_epoch", "port_open": "port_open",
    "ti_flag": "ioc_flagged", "aq_pm25": "pm25_ugm3_x10", "wx_wind": "wind_kmh_milli",
    "gas_basefee": "base_fee_gwei_micro", "token_supply": "total_supply_raw",
    "validator_eb": "effective_balance_gwei", "loan_rate": "rate_bps", "http_status": "http_status",
    "is_up": "is_up", "prom_value": "metric_value", "sensor_fresh": "heartbeat_fresh",
    "vessel_sog": "sog_milliknots", "deliverable": "deliverable", "vendor_id": "id_valid",
    "has_error": "has_error", "regress_paiza": "exit_status", "has_phrase": "has_phrase",
    "is_positive": "is_positive", "top1_match": "top1_domain_match",
}

P = []


def add(fn, *args):
    P.append((fn, args))


for r in stp.DOH:
    add("dns_has", r, "example.com", "A")
    add("dns_has", r, "nxdomain-test-xyz123.example", "A")
for v in ("certspotter", "crtsh"):
    add("ssl_not_after", v, "badssl.com")
    add("ssl_not_after", v, "example.com")
for v in ("internetdb", "checkhost"):
    add("port_open", v, "45.33.32.156", "22")
    add("port_open", v, "45.33.32.156", "9999")
    add("port_open", v, "1.1.1.1", "53")
EICAR, HELLO = "44d88612fea8a8f36de82e1278abb02f", "5d41402abc4b2a76b9719d911017c592"
add("ti_flag", "cymru", "md5", EICAR)
add("ti_flag", "cymru", "md5", HELLO)
add("ti_flag", "feodo", "ip", "8.8.8.8")
add("ti_flag", "feodo", "ip", "162.243.103.246")
add("ti_flag", "urlhaus", "domain", "google.com")
add("ti_flag", "urlhaus", "ip", "176.65.134.121")
for v, s in (("openmeteo", "52.52,13.41"), ("uba", "DEBE034"), ("luchtmeetnet", "NL01485"),
             ("neasg", "central"), ("sensorcommunity", "1412")):
    add("aq_pm25", v, s)
for v, s in (("era5", "52.52,13.41"), ("brightsky", "52.52,13.41"), ("metar", "KJFK"),
             ("envcanada", "6158731"), ("jma", "44132")):
    add("wx_wind", v, s, "2026-09-20T06:00")
    add("wx_wind", v, s, "2026-09-20T14:00")
for v in ("metamask", "owlracle"):
    add("gas_basefee", v, "1")
    add("gas_basefee", v, "137")
add("gas_basefee", "polygon", "137")
add("token_supply", "drpc", "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", "23000000")
add("token_supply", "drpc", "0xdAC17F958D2ee523a2206206994597C13D831ec7", "23000000")
add("token_supply", "solana", "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v", "latest")
for v in stp.BEACON:
    add("validator_eb", v, "1", "head")
    add("validator_eb", v, "1000000", "head")
for v, s, d in (("freddie", "pmms30", "2026-09-17"), ("fred", "DPRIME", "2026-09-17"),
                ("boc", "V80691335", "2026-09-09"), ("ecb", "M.U2.B.A2C.AM.R.A.2250.EUR.N", "2026-07"),
                ("boe", "IUMBV34", "2026-08-31"), ("bcb", "20779", "2026-07-01")):
    add("loan_rate", v, s, d)
for v in ("checkhost", "hackertarget"):
    add("http_status", v, "https://example.com/")
    add("http_status", v, "https://httpbin.org/status/404")
    add("is_up", v, "https://example.com/")
    add("is_up", v, "https://nxdomain-test-xyz123.example/")
for v in stp.PROM:
    add("prom_value", v, "node_memory_MemTotal_bytes")
    add("prom_value", v, "up")
for v, s in (("sensorcommunity", "1412"), ("usgs", "01646500:00065"), ("coops", "8518750"),
             ("thingspeak", "12397"), ("thingspeak", "9"), ("ndbc", "44025")):
    add("sensor_fresh", v, s, "7200")
add("vessel_sog", "354540000")
add("deliverable", "indiapost", "110001")
add("deliverable", "indiapost", "999999")
add("deliverable", "auspost", "3000")
add("deliverable", "auspost", "3001")
add("vendor_id", "vies", "DE811569869")
add("vendor_id", "vies", "DE123456789")
add("vendor_id", "brreg", "923609016")
add("vendor_id", "brreg", "999999999")
add("vendor_id", "openiban", "DE89370400440532013000")
add("vendor_id", "openiban", "DE89370400440532013001")
for v in ("languagetool", "yandex"):
    add("has_error", v, "This are a test sentense.", "en")
    add("has_error", v, "This is a test sentence.", "en")
add("regress_paiza", "print(1+1)", "python3")
add("regress_paiza", "import sys;sys.exit(1)", "python3")
for v in ("jina", "urltomarkdown"):
    add("has_phrase", v, "https://example.com/", "documentation examples")
    add("has_phrase", v, "https://example.com/", "lorem ipsum")
for v in ("textprocessing", "twinword"):
    add("is_positive", v, "I love this wonderful product, it is fantastic")
    add("is_positive", v, "This is terrible, I hate it, awful experience")
add("top1_match", "wikipedia", "wikipedia.org")
add("top1_match", "python programming language", "python.org")

only = sys.argv[2].split(",") if len(sys.argv) > 2 else None
if only:
    P = [p for p in P if p[0] in only]


def run(p):
    fn, args = p
    out = []
    for _ in range(2):
        t0 = time.time()
        try:
            r = getattr(stp, fn)(*args)
            out.append(f"{r.get(LABEL[fn])}")
        except Exception as e:  # noqa: BLE001
            out.append(f"ERR {type(e).__name__}: {str(e)[:120]}")
        out[-1] += f" ({time.time() - t0:.1f}s)"
    return f"{fn}{args}: " + " | ".join(out)


with ThreadPoolExecutor(12) as ex:
    for line in ex.map(run, P):
        print(line, flush=True)
