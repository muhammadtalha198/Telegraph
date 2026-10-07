"""Batch 6 miners (Fable API_SOURCES_BY_INTENT-2026-09-24): one publisher per miner.

Each check is (query_overrides, kind, value):
  kind "pf"    -> PassFail, value = expected int
  kind "fixed" -> RelTol against a fixed expected value
  kind "vs"    -> RelTol against the same route with venue=value
  kind "self"  -> RelTol against its own answer (single publisher / per-pin)
"""

ID_START = 170021

# route -> (param descriptions, label field, label description)
ROUTES = {
    "dns-has": ({"venue": "DoH resolver id", "name": "Domain name", "type": "Record type (A, AAAA, MX, TXT, NS, CNAME)"},
                "has_record", "1 if the resolver returns at least one record of that type, else 0"),
    "ssl-notafter": ({"venue": "Certificate log id", "host": "Hostname"},
                     "not_after_epoch", "notAfter (unix seconds) of the newest unexpired certificate covering host"),
    "port-open": ({"venue": "Scanner id", "host": "IPv4 address", "port": "TCP port"},
                  "port_open", "1 if the TCP port is observed open, else 0"),
    "ti-flag": ({"venue": "Threat feed id", "type": "IOC type (md5/sha1/sha256, ip, domain, url)", "value": "Indicator value"},
                "ioc_flagged", "1 if the feed lists the indicator, else 0"),
    "aq-pm25": ({"venue": "Air-quality network id", "site": "Station / sensor / lat,lon for this network"},
                "pm25_ugm3_x10", "Latest PM2.5 in ug/m3 x10"),
    "wx-wind": ({"venue": "Observation archive id", "site": "Station id or lat,lon for this archive", "when": "Past UTC hour (YYYY-MM-DDTHH:00)"},
                "wind_kmh_milli", "Observed 10 m wind speed at that hour, km/h x1000"),
    "gas-basefee": ({"venue": "Gas oracle id", "chain_id": "EVM chain id"},
                    "base_fee_gwei_micro", "Current base fee in gwei x1e6"),
    "token-supply": ({"venue": "Chain RPC id", "token": "ERC-20 contract or SPL mint", "block": "Block number (EVM) or latest"},
                     "total_supply_raw", "totalSupply in base units"),
    "validator-eb": ({"venue": "Beacon node id", "index": "Validator index", "state": "State id (head, finalized, slot)"},
                     "effective_balance_gwei", "Validator effective balance in gwei"),
    "loan-rate": ({"venue": "Rate publisher id", "series": "Series id at this publisher", "date": "Observation date (YYYY-MM-DD; ECB YYYY-MM)"},
                  "rate_bps", "Published rate in basis points"),
    "http-status": ({"venue": "Probe network id", "url": "URL to fetch"},
                    "http_status", "HTTP status code seen by the probe"),
    "is-up": ({"venue": "Probe network id", "url": "URL to probe"},
              "is_up", "1 if the URL answers with status < 500, else 0"),
    "prom-value": ({"venue": "Prometheus host id", "query": "PromQL instant query"},
                   "metric_value", "Value of the first result series"),
    "sensor-fresh": ({"venue": "Telemetry network id", "sensor": "Sensor / station / channel id", "max_age_s": "Freshness window in seconds"},
                     "heartbeat_fresh", "1 if the newest sample is within max_age_s, else 0"),
    "vessel-sog": ({"mmsi": "Vessel MMSI (Finnish AIS coverage)"},
                   "sog_milliknots", "Latest AIS speed over ground, knots x1000"),
    "deliverable": ({"venue": "Postal operator id", "postcode": "Postcode"},
                    "deliverable", "1 if the postcode has a delivery office/area, else 0"),
    "vendor-id": ({"venue": "Registry id", "id": "VAT number / org number / IBAN for this registry"},
                  "id_valid", "1 if the registry validates the identifier, else 0"),
    "has-error": ({"venue": "Checker id", "text": "Text to check", "lang": "Language code"},
                  "has_error", "1 if the checker reports any issue, else 0"),
    "regress-paiza": ({"source_code": "Program source", "language": "paiza.io language id"},
                      "exit_status", "0 if the program runs and exits 0, else 1"),
    "has-phrase": ({"venue": "Extractor id", "url": "Page URL", "phrase": "Phrase to find (case-insensitive)"},
                   "has_phrase", "1 if the extracted text contains the phrase, else 0"),
    "is-positive": ({"venue": "Classifier id", "text": "Text to classify"},
                    "is_positive", "1 if the classifier labels the text positive, else 0"),
    "top1-match": ({"query": "Search query", "expected_domain": "Domain expected at rank 1"},
                   "top1_domain_match", "1 if the top result is on expected_domain, else 0"),
}

# (folder, slug, intent, route, venue, name, docs, defaults, checks, flag)
M = []


def add(folder, slug, intent, route, venue, name, docs, defaults, checks, flag=""):
    M.append(dict(folder=folder, slug=slug, intent=intent, route=route, venue=venue, name=name,
                  docs=docs, defaults=defaults, checks=checks, flag=flag))


NX = "nxdomain-test-xyz123.example"
for v, nm, doc in (("cloudflare", "Cloudflare 1.1.1.1 DoH", "https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/"),
                   ("google", "Google Public DNS DoH", "https://developers.google.com/speed/public-dns/docs/doh/json"),
                   ("adguard", "AdGuard DNS DoH", "https://adguard-dns.io/kb/general/dns-providers/"),
                   ("nextdns", "NextDNS DoH", "https://nextdns.io"),
                   ("dnssb", "DNS.SB DoH", "https://dns.sb/doh/"),
                   ("rethink", "RethinkDNS DoH", "https://www.rethinkdns.com/configure")):
    add("dns-lookup", f"dns-{v}", "DNS_RECORD_LOOKUP", "dns-has", v, nm, doc,
        {"name": "example.com", "type": "A"},
        [({}, "pf", 1), ({"name": NX}, "pf", 0)], "tie: all resolvers agree")

for v, nm, doc in (("certspotter", "SSLMate Cert Spotter", "https://sslmate.com/help/reference/ct_search_api_v1"),
                   ("crtsh", "crt.sh CT search", "https://crt.sh")):
    add("ssl-verification", f"ssl-{v}", "SSL_VERIFICATION", "ssl-notafter", v, nm, doc,
        {"host": "badssl.com"}, [({}, "fixed", 1793044989)],
        "multi-CA hosts (example.com) differ by which cert is newest; pin single-CA hosts")

for v, nm, doc in (("internetdb", "Shodan InternetDB", "https://internetdb.shodan.io/docs"),
                   ("checkhost", "check-host.net TCP", "https://check-host.net/about/api")):
    add("port-scan-audit", f"prt-{v}", "PORT_SCAN_AUDIT", "port-open", v, nm, doc,
        {"host": "45.33.32.156", "port": "22"},
        [({}, "pf", 1), ({"port": "9999"}, "pf", 0)], "tie")

add("threat-intel", "tif-cymru", "THREAT_INTELLIGENCE", "ti-flag", "cymru", "Team Cymru Malware Hash Registry",
    "https://www.team-cymru.com/mhr", {"type": "md5", "value": "44d88612fea8a8f36de82e1278abb02f"},
    [({}, "pf", 1), ({"value": "5d41402abc4b2a76b9719d911017c592"}, "pf", 0)], "per-pin: hashes only")
add("threat-intel", "tif-feodo", "THREAT_INTELLIGENCE", "ti-flag", "feodo", "abuse.ch Feodo Tracker",
    "https://feodotracker.abuse.ch/blocklist/", {"type": "ip", "value": "162.243.103.246"},
    [({}, "pf", 1), ({"value": "8.8.8.8"}, "pf", 0)], "per-pin: botnet C2 IPs only")
add("threat-intel", "tif-urlhaus", "THREAT_INTELLIGENCE", "ti-flag", "urlhaus", "abuse.ch URLhaus",
    "https://urlhaus.abuse.ch/api/", {"type": "ip", "value": "176.65.134.121"},
    [({}, "pf", 1), ({"type": "domain", "value": "google.com"}, "pf", 0)],
    "per-pin: malware URL hosts; recent-30-day feed so the positive pin may age out")

for v, site, nm, doc in (("openmeteo", "52.52,13.41", "Open-Meteo Air Quality (CAMS)", "https://open-meteo.com/en/docs/air-quality-api"),
                         ("uba", "DEBE034", "Umweltbundesamt Luftdaten", "https://www.umweltbundesamt.de/daten/luft/luftdaten"),
                         ("luchtmeetnet", "NL01485", "Luchtmeetnet (RIVM)", "https://api-docs.luchtmeetnet.nl"),
                         ("neasg", "central", "NEA Singapore PM2.5", "https://data.gov.sg"),
                         ("sensorcommunity", "1412", "Sensor.Community", "https://github.com/opendata-stuttgart/meta/wiki/APIs")):
    add("air-quality", f"aqi-{v}", "AIR_QUALITY_INDEX", "aq-pm25", v, nm, doc, {"site": site},
        [({}, "self", None)], "per-pin: each network has its own sites")

for v, site, nm, doc in (("era5", "52.52,13.41", "Open-Meteo Historical (ERA5)", "https://open-meteo.com/en/docs/historical-weather-api"),
                         ("brightsky", "52.52,13.41", "Bright Sky (DWD observations)", "https://brightsky.dev/docs/"),
                         ("metar", "KJFK", "AviationWeather METAR archive", "https://aviationweather.gov/data/api/"),
                         ("envcanada", "6158731", "ECCC climate-hourly", "https://api.weather.gc.ca/"),
                         ("jma", "44132", "JMA AMeDAS", "https://www.jma.go.jp/bosai/amedas/")):
    add("weather-forecast-verify", f"wnd-{v}", "WEATHER_FORECAST_VERIFY", "wx-wind", v, nm, doc,
        {"site": site, "when": "2026-09-20T06:00"}, [({}, "self", None)],
        "per-pin; at Berlin ERA5 (model) and DWD (station) differ ~10-40%")

for v, chain, nm, doc, vs in (("metamask", "1", "MetaMask Gas API", "https://docs.metamask.io/services/reference/gas-api/", "polygon"),
                              ("owlracle", "1", "Owlracle", "https://owlracle.info/docs", "metamask"),
                              ("polygon", "137", "Polygon Gas Station v2", "https://docs.polygon.technology/tools/gas/polygon-gas-station/", "metamask")):
    add("gas-price", f"gas-{v}", "GAS_PRICE", "gas-basefee", v, nm, doc, {"chain_id": chain},
        [({"chain_id": "137"}, "vs", vs)], "consensus value, near-tie; spread is block timing")

add("token-supply", "sup-drpc", "TOKEN_TOTAL_SUPPLY_VERIFY", "token-supply", "drpc", "dRPC Ethereum eth_call totalSupply",
    "https://drpc.org", {"token": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", "block": "23000000"},
    [({}, "fixed", 41247418952264597)], "per-pin: EVM tokens")
add("token-supply", "sup-solana", "TOKEN_TOTAL_SUPPLY_VERIFY", "token-supply", "solana", "Solana RPC getTokenSupply",
    "https://solana.com/docs/rpc/http/gettokensupply", {"token": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v", "block": "latest"},
    [({}, "self", None)], "per-pin: SPL mints, live only")

for v, nm, doc in (("publicnode", "PublicNode Beacon API", "https://ethereum-beacon-api.publicnode.com"),
                   ("quicknode", "QuickNode public Beacon API", "https://www.quicknode.com/docs/ethereum")):
    add("validator-performance", f"vlp-{v}", "VALIDATOR_PERFORMANCE_VERIFY", "validator-eb", v, nm, doc,
        {"index": "1", "state": "head"}, [({}, "fixed", 32000000000)], "tie: consensus state")

for v, ser, dt, want, nm, doc in (
        ("freddie", "pmms30", "2026-09-17", 695, "Freddie Mac PMMS", "https://www.freddiemac.com/pmms"),
        ("fred", "DPRIME", "2026-09-17", 700, "FRED (St. Louis Fed)", "https://fred.stlouisfed.org"),
        ("boc", "V80691335", "2026-09-09", 609, "Bank of Canada Valet", "https://www.bankofcanada.ca/valet/docs"),
        ("ecb", "M.U2.B.A2C.AM.R.A.2250.EUR.N", "2026-07", 354, "ECB MFI interest rates", "https://data.ecb.europa.eu"),
        ("boe", "IUMBV34", "2026-08-31", 492, "Bank of England IADB", "https://www.bankofengland.co.uk/boeapps/database/"),
        ("bcb", "20779", "2026-07-01", 935, "Banco Central do Brasil SGS", "https://dadosabertos.bcb.gov.br")):
    add("loan-rate", f"lnr-{v}", "LOAN_INTEREST_RATE_QUOTE", "loan-rate", v, nm, doc,
        {"series": ser, "date": dt}, [({}, "fixed", want)], "per-series: each publisher has its own rate")

for v, nm, doc in (("checkhost", "check-host.net HTTP", "https://check-host.net/about/api"),
                   ("hackertarget", "HackerTarget HTTP headers", "https://hackertarget.com/http-header-check/")):
    add("api-health", f"hlt-{v}", "API_HEALTH_CHECK", "http-status", v, nm, doc,
        {"url": "https://example.com/"},
        [({}, "pf", 200), ({"url": "https://httpbin.org/status/404"}, "pf", 404)], "tie")
    add("server-uptime", f"upt-{v}", "SERVER_UPTIME_MONITOR", "is-up", v, nm, doc,
        {"url": "https://example.com/"},
        [({}, "pf", 1), ({"url": f"https://{NX}/"}, "pf", 0)], "tie; same upstreams as API_HEALTH_CHECK")

for v, nm, doc in (("promlabs", "PromLabs demo Prometheus", "https://demo.promlabs.com"),
                   ("prometheusio", "prometheus.io demo Prometheus", "https://prometheus.demo.prometheus.io")):
    add("cloud-resource", f"prm-{v}", "CLOUD_RESOURCE_USAGE", "prom-value", v, nm, doc,
        {"query": "node_memory_MemTotal_bytes"}, [({}, "self", None)],
        "per-host: each demo reports its own machines, cannot rank")

for v, s, nm, doc in (("sensorcommunity", "1412", "Sensor.Community", "https://github.com/opendata-stuttgart/meta/wiki/APIs"),
                      ("usgs", "01646500:00065", "USGS Water Services IV", "https://waterservices.usgs.gov"),
                      ("coops", "8518750", "NOAA CO-OPS", "https://api.tidesandcurrents.noaa.gov/api/prod/"),
                      ("thingspeak", "12397", "ThingSpeak", "https://www.mathworks.com/help/thingspeak/"),
                      ("ndbc", "44025", "NOAA NDBC realtime2", "https://www.ndbc.noaa.gov/faq/rt_data_access.shtml")):
    checks = [({}, "pf", 1)]
    if v == "thingspeak":
        checks.append(({"sensor": "9"}, "pf", 0))
    add("sensor-telemetry", f"sen-{v}", "SENSOR_TELEMETRY_VERIFY", "sensor-fresh", v, nm, doc,
        {"sensor": s, "max_age_s": "7200"}, checks, "per-pin: each network has its own sensors")

add("vessel-telemetry", "ves-digitraffic", "VESSEL_TELEMETRY_VERIFY", "vessel-sog", None, "Fintraffic Digitraffic AIS",
    "https://www.digitraffic.fi/en/marine-traffic/", {"mmsi": "230981000"}, [({}, "self", None)],
    "single publisher; SOG is live — re-pin if idle (was 354540000)")

add("carrier-serviceability", "car-indiapost", "CARRIER_SERVICEABILITY", "deliverable", "indiapost", "India Post PIN directory",
    "https://api.postalpincode.in", {"postcode": "110001"},
    [({}, "pf", 1), ({"postcode": "999999"}, "pf", 0)], "per-pin: Indian PINs")
add("carrier-serviceability", "car-auspost", "CARRIER_SERVICEABILITY", "deliverable", "auspost", "Australia Post postcode search",
    "https://auspost.com.au/postcode", {"postcode": "3000"},
    [({}, "pf", 1), ({"postcode": "3001"}, "pf", 0)], "per-pin: Australian postcodes")

add("vendor-verify", "vnd-vies", "VENDOR_VERIFY", "vendor-id", "vies", "EU VIES VAT check",
    "https://ec.europa.eu/taxation_customs/vies/", {"id": "DE811569869"},
    [({}, "pf", 1), ({"id": "DE123456789"}, "pf", 0)], "per-pin: EU VAT numbers")
add("vendor-verify", "vnd-brreg", "VENDOR_VERIFY", "vendor-id", "brreg", "Bronnoysund Register Centre",
    "https://data.brreg.no/enhetsregisteret/api/docs/", {"id": "923609016"},
    [({}, "pf", 1), ({"id": "999999999"}, "pf", 0)], "per-pin: Norwegian org numbers")
add("vendor-verify", "vnd-openiban", "VENDOR_VERIFY", "vendor-id", "openiban", "OpenIBAN",
    "https://openiban.com", {"id": "DE89370400440532013000"},
    [({}, "pf", 1), ({"id": "DE89370400440532013001"}, "pf", 0)], "per-pin: IBANs (bank account, not company)")

for v, nm, doc in (("languagetool", "LanguageTool public API", "https://languagetool.org/http-api/"),
                   ("yandex", "Yandex Speller", "https://yandex.ru/dev/speller/")):
    add("grammar-spell", f"grm-{v}", "GRAMMAR_SPELL_CHECK", "has-error", v, nm, doc,
        {"text": "This are a test sentense.", "lang": "en"},
        [({}, "pf", 1), ({"text": "This is a test sentence."}, "pf", 0)], "tie")

add("regression-verify", "rgr-paiza", "REGRESSION_VERIFY", "regress-paiza", None, "paiza.io runner",
    "https://paiza.io/help", {"source_code": "print(1+1)", "language": "python3"},
    [({}, "pf", 0), ({"source_code": "import sys;sys.exit(1)"}, "pf", 1)], "single publisher")

for v, nm, doc in (("jina", "Jina Reader", "https://jina.ai/reader/"),
                   ("urltomarkdown", "urltomarkdown", "https://github.com/macsplit/urltomarkdown")):
    add("content-extraction", f"cex-{v}", "CONTENT_EXTRACTION", "has-phrase", v, nm, doc,
        {"url": "https://example.com/", "phrase": "documentation examples"},
        [({}, "pf", 1), ({"phrase": "lorem ipsum"}, "pf", 0)], "tie")

for v, nm, doc in (("textprocessing", "text-processing.com sentiment", "https://text-processing.com/docs/sentiment.html"),
                   ("twinword", "Twinword Sentiment", "https://www.twinword.com/api/sentiment-analysis.php")):
    add("sentiment-analysis", f"snt-{v}", "SENTIMENT_ANALYSIS", "is-positive", v, nm, doc,
        {"text": "I love this wonderful product, it is fantastic"},
        [({}, "pf", 1), ({"text": "This is terrible, I hate it, awful experience"}, "pf", 0)], "tie")

add("web-search", "srch-marginalia", "WEB_SEARCH", "top1-match", None, "Marginalia Search",
    "https://about.marginalia-search.com/article/api/", {"query": "wikipedia", "expected_domain": "wikipedia.org"},
    [({}, "pf", 1)], "single publisher; CC-BY-NC-SA results")

for i, m in enumerate(M):
    m["id"] = ID_START + i

# Dropped after probing; ids stay reserved so published YAML ids do not shift.
DROPPED = {"gas-owlracle": "keyless quota: HTTP 403 after a few calls"}
M[:] = [m for m in M if m["slug"] not in DROPPED]

INTENT_TOL = {
    "DNS_RECORD_LOOKUP": 0, "SSL_VERIFICATION": 1, "PORT_SCAN_AUDIT": 0, "THREAT_INTELLIGENCE": 0,
    "AIR_QUALITY_INDEX": 1000, "WEATHER_FORECAST_VERIFY": 1200, "GAS_PRICE": 1500,
    "TOKEN_TOTAL_SUPPLY_VERIFY": 1, "VALIDATOR_PERFORMANCE_VERIFY": 1, "LOAN_INTEREST_RATE_QUOTE": 1,
    "API_HEALTH_CHECK": 0, "SERVER_UPTIME_MONITOR": 0, "CLOUD_RESOURCE_USAGE": 100,
    "SENSOR_TELEMETRY_VERIFY": 0, "VESSEL_TELEMETRY_VERIFY": 100, "CARRIER_SERVICEABILITY": 0,
    "VENDOR_VERIFY": 0, "GRAMMAR_SPELL_CHECK": 0, "REGRESSION_VERIFY": 0, "CONTENT_EXTRACTION": 0,
    "SENTIMENT_ANALYSIS": 0, "WEB_SEARCH": 0,
}


def query(m: dict, overrides: dict | None = None, venue: str | None = None) -> dict:
    q = {}
    if m["venue"]:
        q["venue"] = venue or m["venue"]
    q.update(m["defaults"])
    q.update(overrides or {})
    return q
