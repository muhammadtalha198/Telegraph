# Catalog coverage: the remaining required intents

Generated 2026-10-09. Tiers: 71 required, 26 judgment (LLM, no spec), 22 unverifiable (blocked).
**Required with a deterministic spec: 17. Remaining: 54.**

Judgment and unverifiable intents need no spec (the gate SKIPs / BLOCKs them with the catalog reason).
The remaining required intents are bucketed by how verifiable they are with FREE public APIs:


## A. Feasible now — 2+ independent free APIs already exist (write specs next)  (14)

| Intent | Pri | Free hosts | Example sources |
|---|---:|---:|---|
| CODE_PATCH_VERIFY | 10 | 3 | api.github.com, circleci.com, gitlab.com |
| CROSS_CHAIN_STATE_VERIFY | 10 | 9 | across.to, api.axelarscan.io, api.relay.link |
| EVENT_OUTCOME_RESOLUTION | 10 | 8 | api-web.nhle.com, api.jolpi.ca, api.manifold.markets |
| OPTIMAL_EXECUTION_ROUTE | 10 | 8 | aggregator-api.kyberswap.com, api.bebop.xyz, api.cow.fi |
| VULNERABILITY_TRIAGE | 10 | 9 | access.redhat.com, api.first.org, api.osv.dev |
| CRYPTO_TRANSFER_VERIFY | 7 | 6 | api.blockcypher.com, api.haskoin.com, bitcoin-rpc.publicnode.com |
| EMAIL_SECURITY | 7 | 5 | cloudflare-dns.com, dns.adguard-dns.com, dns.alidns.com |
| THREAT_IP_REPUTATION | 7 | 2 | feodotracker.abuse.ch, isc.sans.edu |
| GAS_PRICE_ESTIMATION | 6 | 3 | 1rpc.io, eth.drpc.org, ethereum-rpc.publicnode.com |
| GRAMMAR_SPELL_CHECK | 6 | 3 | api.datamuse.com, api.grammarbot.io, api.languagetool.org |
| ROUTE_ETA | 6 | 2 | router.project-osrm.org, routing.openstreetmap.de |
| SSL_CERTIFICATE_VERIFY | 6 | 2 | api.ssllabs.com, networkcalc.com |
| GRID_POWER_PRICE | 5 | 3 | api.awattar.de, api.spot-hinta.fi, dashboard.elering.ee |
| MINING_HASHPRICE_VERIFY | 5 | 2 | api.blockchain.info, whattomine.com |

## B. Single-source / regional / behind the truth-proxy — need an authority rule or a 2nd free source found  (20)

| Intent | Pri | Free hosts | Example sources |
|---|---:|---:|---|
| TRAVEL_DISRUPTION | 10 | 0 | — |
| ASSET_RESERVE_ATTESTATION | 9 | 0 | — |
| SANCTIONS_SCREENING_MATCH | 9 | 0 | — |
| CURRENCY_EXCHANGE | 7 | 0 | — |
| REGRESSION_VERIFY | 7 | 0 | — |
| SEMANTIC_SIMILARITY | 7 | 0 | — |
| SENTIMENT_ANALYSIS | 7 | 0 | — |
| TEXT_CLASSIFICATION | 7 | 0 | — |
| THREAT_INTELLIGENCE | 7 | 0 | — |
| URL_CONTENT_EXTRACTION | 7 | 1 | api.microlink.io |
| VENDOR_VERIFY | 7 | 1 | api.vatcomply.com |
| AIR_QUALITY_INDEX | 6 | 0 | — |
| API_HEALTH_CHECK | 6 | 0 | — |
| EMBEDDING_GENERATION | 6 | 0 | — |
| PORT_SCAN_AUDIT | 6 | 1 | api.hackertarget.com |
| SERVER_UPTIME_MONITOR | 6 | 0 | — |
| VESSEL_TELEMETRY_VERIFY | 5 | 0 | — |
| WEATHER_FORECAST_VERIFY | 5 | 0 | — |
| PROMPT_INJECTION_DETECT | 0 | 0 | — |
| RAG_GROUNDING_VERIFY | 0 | 0 | — |

## C. Not freely verifiable — need private/paid/issuer data or are satellite/forensic (likely stay blocked)  (20)

| Intent | Pri | Free hosts | Example sources |
|---|---:|---:|---|
| COMMERCE_PURCHASE_VERIFY | 10 | 0 | — |
| LIVE_SHELF_PRICE | 10 | 0 | — |
| SKU_IN_STOCK | 10 | 0 | — |
| CREDIT_SCORE_VERIFY | 7 | 0 | — |
| PURCHASE_ORDER_VERIFY | 7 | 0 | — |
| CLOUD_RESOURCE_USAGE | 5 | 0 | — |
| SENSOR_TELEMETRY_VERIFY | 5 | 0 | — |
| ACCESS_PRIVILEGE_DRIFT_AUDIT | 0 | 0 | — |
| AGENT_TOOL_CALL_AUDIT | 0 | 0 | — |
| CARBON_OFFSET_RETIREMENT | 0 | 0 | — |
| COLD_CHAIN_TEMPERATURE_BREACH | 0 | 0 | — |
| CROSS_BORDER_REMITTANCE_STATUS | 0 | 0 | — |
| DEFORESTATION_SURVEILLANCE | 0 | 0 | — |
| EXPORT_CONTROL_CLASSIFICATION | 0 | 0 | — |
| FLOOD_EXTENT_MAPPING | 0 | 0 | — |
| GDPR_DATA_ERASURE_AUDIT | 0 | 0 | — |
| METHANE_EMISSION_DETECTION | 0 | 0 | — |
| SMART_METER_TAMPER_DETECT | 0 | 0 | — |
| SYNTHETIC_DATA_FIDELITY | 0 | 0 | — |
| WILDFIRE_PERIMETER_MONITOR | 0 | 0 | — |
