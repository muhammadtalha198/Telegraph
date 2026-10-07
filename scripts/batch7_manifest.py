"""Batch 7 (Round Two ACCEPT): new publishers for under-10 intents.

Skips already-registered Round-2 hits (MET Norway, Polymarket) and Gate-1-risky PoR.
"""

ID_START = 170100

# route_key used in YAML external_path /truth/<route>
# For venue-based existing routes, route is the shared path and venue is in defaults.

M = []


def add(**kw):
    M.append(kw)


# --- CRYPTO_PRICE (extend crypto-spot) ---
for v, name, docs in (
    ("htx", "HTX Spot", "https://www.htx.com/"),
    ("mexc", "MEXC Spot", "https://www.mexc.com/"),
    ("gate", "Gate.io Spot", "https://www.gate.io/"),
    ("bitfinex", "Bitfinex Spot", "https://docs.bitfinex.com/"),
    ("bybit", "Bybit Spot", "https://bybit-exchange.github.io/docs/"),
):
    add(
        folder="crypto-price",
        slug=f"crypto-{v}",
        intent="CRYPTO_PRICE",
        route="crypto-spot",
        name=name,
        docs=docs,
        defaults={"venue": v, "pair": "BTC-USD"},
        label="price_usd_cents",
        checks=[({}, "vs", "coinbase")],
        flag="round2: new CEX",
    )

# --- THREAT_IP ---
add(
    folder="threat-ip",
    slug="tip-abuseipdb",
    intent="THREAT_IP_REPUTATION",
    route="ip-rep",
    name="AbuseIPDB",
    docs="https://docs.abuseipdb.com/",
    defaults={"venue": "abuseipdb", "ip": "8.8.8.8"},
    label="listed",
    checks=[({}, "pf", 0), ({"ip": "185.220.101.1"}, "pf", 1)],
    flag="round2: keyed ABUSEIPDB_API_KEY",
)

# --- WEATHER ---
add(
    folder="weather-check",
    slug="wxk-7timer",
    intent="WEATHER_CHECK",
    route="wx-temp",
    name="7Timer Civil",
    docs="http://www.7timer.info/doc.php",
    defaults={"venue": "7timer", "lat": "52.52", "lon": "13.41"},
    label="temp_k_x100",
    checks=[({}, "self", None)],
    flag="round2: coarse model; self-truth",
)

# --- AQI ---
add(
    folder="air-quality",
    slug="aqi-cerns",
    intent="AIR_QUALITY_INDEX",
    route="aq-pm25",
    name="CERNS Berlin AQI",
    docs="https://cerns.io/developers",
    defaults={"venue": "cerns", "site": "berlin"},
    label="pm25_ugm3_x10",
    checks=[({}, "self", None)],
    flag="round2: per-pin city",
)
add(
    folder="air-quality",
    slug="aqi-infranode",
    intent="AIR_QUALITY_INDEX",
    route="aq-pm25",
    name="InfraNode UBA Berlin",
    docs="https://infranode.dev/daten/luftqualitaet-api/",
    defaults={"venue": "infranode", "site": "berlin"},
    label="pm25_ugm3_x10",
    checks=[({}, "self", None)],
    flag="round2: per-pin city",
)

# --- DNS ---
add(
    folder="dns-lookup",
    slug="dns-alidns",
    intent="DNS_RECORD_LOOKUP",
    route="dns-has",
    name="Alibaba Public DNS",
    docs="https://www.alibabacloud.com/help/en/dns",
    defaults={"venue": "alidns", "name": "example.com", "type": "A"},
    label="has_record",
    checks=[({}, "pf", 1), ({"name": "nxdomain-test-xyz123.example"}, "pf", 0)],
    flag="round2: tie with other DoH",
)

# --- STOCK (dropped from register: Yahoo Finance 429/502 under probe load) ---
# add(... stk-yahoo ...) — keep YAML for later; do not register until stable.

# --- VULN ---
add(
    folder="vulnerability",
    slug="vuln-ghsa",
    intent="VULNERABILITY_TRIAGE",
    route="ghsa-cvss",
    name="GitHub Advisory CVSS",
    docs="https://docs.github.com/en/rest/security-advisories",
    defaults={"cve_id": "CVE-2024-3094"},
    label="cvss_base_score_milli",
    checks=[({}, "vs_route", ("nvd-cvss", {"cve_id": "CVE-2024-3094"}))],
    flag="round2: vs NVD",
)
add(
    folder="vulnerability",
    slug="vuln-redhat",
    intent="VULNERABILITY_TRIAGE",
    route="redhat-cvss",
    name="Red Hat CVE CVSS",
    docs="https://access.redhat.com/documentation/en-us/red_hat_security_data_api",
    defaults={"cve_id": "CVE-2024-3094"},
    label="cvss_base_score_milli",
    checks=[({}, "vs_route", ("nvd-cvss", {"cve_id": "CVE-2024-3094"}))],
    flag="round2: vs NVD",
)

# --- ROUTE ---
add(
    folder="route-eta",
    slug="route-valhalla",
    intent="ROUTE_ETA",
    route="route-valhalla",
    name="Valhalla OSM.de",
    docs="https://valhalla.github.io/valhalla/",
    defaults={
        "origin_lat": "52.5200",
        "origin_lon": "13.4050",
        "dest_lat": "52.5163",
        "dest_lon": "13.3777",
    },
    label="eta_seconds",
    checks=[({}, "self", None)],
    flag="round2: free-flow peer to OSRM; self until RelTol band confirmed",
)

# --- CORP ---
add(
    folder="corporate-registry",
    slug="corp-brreg",
    intent="CORPORATE_REGISTRY_LOOKUP",
    route="corp-brreg",
    name="Bronnoysund Enhetsregisteret",
    docs="https://data.brreg.no/enhetsregisteret/api/docs/",
    defaults={"name": "Equinor"},
    label="status_active",
    checks=[({}, "pf", 1), ({"name": "ZzNoSuchCorpXYZ999"}, "pf", 0)],
    flag="round2: name search (vendor brreg is orgnr id_valid)",
)

# --- VENDOR ---
add(
    folder="vendor-verify",
    slug="vnd-vatcomply",
    intent="VENDOR_VERIFY",
    route="vendor-id",
    name="VATComply VAT",
    docs="https://www.vatcomply.com/",
    defaults={"venue": "vatcomply", "id": "DE811569869"},
    label="id_valid",
    checks=[({}, "pf", 1), ({"id": "DE000000000"}, "pf", 0)],
    flag="round2",
)

# --- SEMANTIC / CLASSIFY (keys) ---
add(
    folder="semantic-similarity",
    slug="sem-hf-minilm",
    intent="SEMANTIC_SIMILARITY",
    route="semantic-sim",
    name="HF MiniLM Sentence Similarity",
    docs="https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2",
    defaults={
        "source": "a sunny day in berlin",
        "candidate": "a bright day in berlin",
        "model": "sentence-transformers/all-MiniLM-L6-v2",
    },
    label="similarity_x10000",
    checks=[({}, "self", None)],
    flag="round2: HF_TOKEN; RelTol self",
)
add(
    folder="text-classification",
    slug="cls-hf-bart-mnli",
    intent="TEXT_CLASSIFICATION",
    route="text-classify",
    name="HF BART-MNLI Zero-Shot",
    docs="https://huggingface.co/facebook/bart-large-mnli",
    defaults={
        "venue": "bart-mnli",
        "text": "I love this product",
        "labels": "positive,negative",
        "expected": "positive",
    },
    label="top_label_match",
    checks=[
        ({}, "pf", 1),
        ({"text": "I hate this terrible product", "expected": "negative"}, "pf", 1),
    ],
    flag="round2: HF_TOKEN",
)
add(
    folder="text-classification",
    slug="cls-hf-twitter-roberta",
    intent="TEXT_CLASSIFICATION",
    route="text-classify",
    name="HF Twitter-RoBERTa Sentiment",
    docs="https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest",
    defaults={
        "venue": "twitter-roberta",
        "text": "I love this product",
        "labels": "positive,negative,neutral",
        "expected": "positive",
    },
    label="top_label_match",
    checks=[
        ({}, "pf", 1),
        ({"text": "I hate this terrible product", "expected": "negative"}, "pf", 1),
    ],
    flag="round2: HF_TOKEN",
)

# Assign ids
for i, m in enumerate(M):
    m["id"] = ID_START + i

INTENT_TOL = {
    "CRYPTO_PRICE": 100,
    "THREAT_IP_REPUTATION": 0,
    "WEATHER_CHECK": 50,
    "AIR_QUALITY_INDEX": 1000,
    "DNS_RECORD_LOOKUP": 0,
    "STOCK_PRICE": 50,
    "VULNERABILITY_TRIAGE": 150,
    "ROUTE_ETA": 800,
    "CORPORATE_REGISTRY_LOOKUP": 0,
    "VENDOR_VERIFY": 0,
    "SEMANTIC_SIMILARITY": 500,
    "TEXT_CLASSIFICATION": 0,
}


def query(m: dict) -> dict:
    return dict(m["defaults"])
