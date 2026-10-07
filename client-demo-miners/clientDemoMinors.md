# Client Demo Minors

Temporary re-registration of the old (~1400) intent YAMLs for client demo.
Not counted as production keepers. Do not merge into INTENT_BUILD_SHEET / newlyRegisteredMiners.

| Field | Value |
|-------|-------|
| Updated | 2026-09-26 00:03 UTC |
| Total candidates | 1386 |
| Registered | **1367** |
| Not registered | 19 |
| Reg ID range | 2972 – 4347 |
| Status | **COMPLETE** |
| Host | paste.rs (SSH:22 blocked) |
| Diamond | `0x5a2324aA18613FAD4e44bDF0d6c73Ec1f6D87ff8` |

## Progress

| Batch | Attempted | Validate OK | Registered | Failed/Skip |
|------:|----------:|------------:|-----------:|------------:|
| 1 | 200 | 199 | 199 | 1 |
| 2 | 200 | 197 | 197 | 3 |
| 3 | 200 | 200 | 200 | 0 |
| 4 | 200 | 190 | 190 | 10 |
| 5 | 200 | 198 | 197 | 3 |
| 6 | 200 | 198 | 198 | 2 |
| 7 | 186 | 186 | 186 | 0 |
| **Total** | **1386** | | **1367** | **19** |

## Not registered (19)

| Slug | Status | Intent |
|------|--------|--------|
| `commerce-stripe-charge` | validate_failed | COMMERCE_PURCHASE_VERIFY |
| `crypto-coinpaprika` | validate_failed | CRYPTO_PRICE |
| `crypto-defillama` | validate_failed | CRYPTO_PRICE |
| `dc-sensor` | validate_failed | DATACENTER_TELEMETRY_VERIFY |
| `ocm-blockchair` | validate_failed | ONCHAIN_METRIC_VERIFY |
| `patch-gh-linux` | validate_failed | CODE_PATCH_VERIFY |
| `patch-gh-pr-commits` | validate_failed | CODE_PATCH_VERIFY |
| `plag-crossref` | validate_failed | PLAGIARISM_DETECTION |
| `plag-crossref2` | validate_failed | PLAGIARISM_DETECTION |
| `plag-hn` | validate_failed | PLAGIARISM_DETECTION |
| `prod-off-search` | validate_failed | PRODUCT_AUTHENTICITY |
| `prod-upc` | validate_failed | PRODUCT_AUTHENTICITY |
| `psa-dns-a` | validate_failed | PORT_SCAN_AUDIT |
| `qa-zenodo` | validate_failed | QUESTION_ANSWERING |
| `shipd-rail` | validate_failed | SHIPMENT_DELAY_RISK |
| `sla-httpbin-ip` | register_failed | SLA_COMPLIANCE |
| `sre-rail` | validate_failed | SHIP_RATE_ETA |
| `stk-yahoo` | validate_failed | STOCK_PRICE |
| `ttl-rail` | validate_failed | TRAVEL_TRANSIT_LOCK |

## Notes

- May be deregistered later after the demo.
- Logs: `client-demo-miners/out/run.log`, `batchN-register.jsonl`
