# Gap report vs existing MinerCreator (from MinerCreator_2.zip)

| Intent | Existing miners (intentYamls) | Status | New candidates here |
|---|---|---|---|
| FX_NOW | 11 | Covered | - |
| WEATHER_CURRENT (WEATHER_CHECK) | 5 | Covered | - |
| CRYPTO_PRICE_LOOKUP (CRYPTO_PRICE) | 10 | Covered | - |
| VULNERABILITY_TRIAGE | many (nvd, circl, osv, ghsa, redhat, cve.org) | Covered | shodan-cvedb, epss, ubuntu, cisa-kev |
| EVENT_OUTCOME_RESOLUTION | 3 | Add | thesportsdb, espn |
| ONCHAIN_METRIC_VERIFY | 1 (ocm-eth-balance, proxy) | Add | 5x Blockscout, Blockchair (balance only) |
| LIQUIDITY_DEPTH_VERIFY | 2 | Add | 7 CEX order books |
| CROSS_CHAIN_STATE_VERIFY | 1 (across) | Add | layerzero, wormholescan, lifi (need real tx hashes) |
| OPTIMAL_EXECUTION_ROUTE | cow, kyber, lifi, paraswap | Add | openocean, sushi |
| CODE_PATCH_VERIFY | godbolt, judge0, wandbox | Add | github-actions |
| SECURITY_REVIEW | 0 | Add | deps.dev, pypi |
| CODE_REVIEW | 0 | Blocked | needs POST+key LLM calls; capture_api_output.py is GET-only |
| WASH_TRADING_DETECTION | 0 | Blocked | no free API returns a verdict, only raw trades |

Notes
- capture_api_output.py only does GET, so POST APIs (public RPCs, LLM chat, Judge0-style runners) need your /truth proxy pattern or a POST option.
- All candidates are unverified until captured and you approve the .md sample.
