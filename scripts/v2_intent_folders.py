"""Canonical intent names → intentYamls/ subfolder (Semantic V2)."""
from __future__ import annotations

# Catalog / sheet aliases → on-chain intent string used in YAML
CATALOG_TO_CANONICAL: dict[str, str] = {
    "CRYPTO_PRICE_LOOKUP": "CRYPTO_PRICE",
    "GAS_PRICE_ESTIMATION": "GAS_PRICE",
    "SSL_CERTIFICATE_VERIFY": "SSL_VERIFICATION",
    "URL_CONTENT_EXTRACTION": "CONTENT_EXTRACTION",
    "WEB_SEARCH_QUERY": "WEB_SEARCH",
    "WEATHER_CURRENT": "WEATHER_CHECK",
    "STOCK_PRICE_QUOTE": "STOCK_PRICE",
}

INTENT_TO_FOLDER: dict[str, str] = {
    "AIR_QUALITY_INDEX": "air-quality",
    "API_HEALTH_CHECK": "api-health",
    "ASSET_RESERVE_ATTESTATION": "asset-reserve",
    "CARRIER_SERVICEABILITY": "carrier-serviceability",
    "CHATBOT_CONVERSATION": "chatbot-conversation",
    "CLOUD_RESOURCE_USAGE": "cloud-resource",
    "CODE_PATCH_VERIFY": "code-patch",
    "CONTENT_EXTRACTION": "content-extraction",
    "CORPORATE_REGISTRY_LOOKUP": "corporate-registry",
    "CROSS_CHAIN_STATE_VERIFY": "cross-chain-state",
    "CRYPTO_PRICE": "crypto-price",
    "CRYPTO_TRANSFER_VERIFY": "crypto-transfer",
    "CRYPTO_YIELD_RATE": "crypto-yield",
    "DNS_RECORD_LOOKUP": "dns-lookup",
    "EMAIL_SECURITY": "email-security",
    "EVENT_OUTCOME_RESOLUTION": "event-outcome",
    "FX_NOW": "fx-now",
    "GAS_PRICE": "gas-price",
    "GRAMMAR_SPELL_CHECK": "grammar-spell",
    "GRID_POWER_PRICE": "grid-power-price",
    "LANGUAGE_TRANSLATION": "language-translation",
    "LIQUIDITY_DEPTH_VERIFY": "liquidity-depth",
    "LIVE_SHELF_PRICE": "live-shelf-price",
    "LOAN_INTEREST_RATE_QUOTE": "loan-rate",
    "MACRO_ECONOMIC_INDICATOR": "macro-indicator",
    "MINING_HASHPRICE_VERIFY": "mining-hashprice",
    "ONCHAIN_METRIC_VERIFY": "onchain-metric",
    "OPTIMAL_EXECUTION_ROUTE": "optimal-execution",
    "PAYMENT_METHOD_VERIFY": "payment-method",
    "PORT_SCAN_AUDIT": "port-scan-audit",
    "REGRESSION_VERIFY": "regression-verify",
    "REGULATORY_FILING_MONITOR": "regulatory-filing",
    "ROUTE_ETA": "route-eta",
    "SANCTIONS_SCREENING_MATCH": "sanctions-screening",
    "SECURITY_REVIEW": "security-review",
    "SEMANTIC_SIMILARITY": "semantic-similarity",
    "SENSOR_TELEMETRY_VERIFY": "sensor-telemetry",
    "SENTIMENT_ANALYSIS": "sentiment-analysis",
    "SERVER_UPTIME_MONITOR": "server-uptime",
    "SKU_IN_STOCK": "sku-in-stock",
    "SSL_VERIFICATION": "ssl-verification",
    "STOCK_PRICE": "stock-price",
    "TEXT_CLASSIFICATION": "text-classification",
    "TEXT_SUMMARIZATION": "text-summarization",
    "TEXT_TO_SPEECH": "text-to-speech",
    "THREAT_INTELLIGENCE": "threat-intel",
    "THREAT_IP_REPUTATION": "threat-ip",
    "TOKEN_TOTAL_SUPPLY_VERIFY": "token-supply",
    "TRAVEL_DISRUPTION": "travel-disruption",
    "VALIDATOR_PERFORMANCE_VERIFY": "validator-performance",
    "VENDOR_VERIFY": "vendor-verify",
    "VESSEL_TELEMETRY_VERIFY": "vessel-telemetry",
    "VULNERABILITY_TRIAGE": "vulnerability-triage",
    "WEATHER_CHECK": "weather-forecast-verify",
    "WEATHER_FORECAST_VERIFY": "weather-forecast-verify",
    "WEB_SEARCH": "web-search",
}


def canonical_intent(name: str) -> str:
    u = (name or "").strip().upper()
    return CATALOG_TO_CANONICAL.get(u, u)


def intent_folder(intent: str) -> str | None:
    return INTENT_TO_FOLDER.get(canonical_intent(intent))
