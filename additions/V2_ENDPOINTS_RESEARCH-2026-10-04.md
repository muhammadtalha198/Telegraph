# V2 Endpoints Research — Semantic Register pattern

**Date:** 2026-10-04  
**Pattern:** GET capture → `auto_review_samples.py` → approved sample → YAML → `register-miner-v2.sh`  
**Machine file:** [`v2_endpoints_research.json`](./v2_endpoints_research.json) (includes `smoke` field)  
**Smoke tool:** `python3 scripts/smoke_v2_endpoints.py`

## Scope

Focused on **gap / under-filled intents** from `GAP_REPORT.md` + low Active counts — not all 97 catalog intents.
Goal: **≥10 distinct upstream GET endpoints per intent** that can answer the intent description (format-agnostic).

## Smoke summary (live HTTP from this machine)

| Intent | Listed | Smoke OK | Notes |
|--------|------:|---------:|-------|
| `CODE_PATCH_VERIFY` | 11 | **8** |  |
| `CROSS_CHAIN_STATE_VERIFY` | 13 | **6** | Some need FILL tx hash; list endpoints OK for hunting pins |
| `EVENT_OUTCOME_RESOLUTION` | 12 | **11** |  |
| `LIQUIDITY_DEPTH_VERIFY` | 13 | **12** | Prefer `dex_pool` over `cex_book` for catalog |
| `ONCHAIN_METRIC_VERIFY` | 12 | **11** |  |
| `OPTIMAL_EXECUTION_ROUTE` | 15 | **8** | 1inch/0x need keys; Jupiter DNS failed here |
| `SECURITY_REVIEW` | 11 | **11** | Prefer deps.dev/OSV/PyPI vulns over bare registry meta |
| `VULNERABILITY_TRIAGE` | 12 | **10** |  |

## Capture-ready (smoke=ok) — use these next

### `CODE_PATCH_VERIFY` (8 OK)

| Slug | Fit | URL |
|------|-----|-----|
| `patch-gh-actions-pytest` | `ci_real_tests` | `https://api.github.com/repos/pallets/flask/actions/runs?per_page=1&status=completed` |
| `patch-gh-compare` | `diff_partial` | `https://api.github.com/repos/psf/requests/compare/v2.31.0...v2.32.0` |
| `patch-gh-commit-check` | `ci_checks` | `https://api.github.com/repos/psf/requests/commits/main/check-runs` |
| `patch-gitlab-pipeline` | `ci_real_tests` | `https://gitlab.com/api/v4/projects/gitlab-org%2Fgitlab-runner/pipelines?per_page=1&status=success` |
| `patch-piston-runtimes` | `sandbox_meta` | `https://emkc.org/api/v2/piston/runtimes` |
| `patch-circleci-recent` | `ci_real_tests` | `https://circleci.com/api/v1.1/project/github/CircleCI-Public/circleci-cli?limit=1&filter=completed` |
| `patch-gh-workflow-django` | `ci_real_tests` | `https://api.github.com/repos/django/django/actions/runs?per_page=1&status=completed` |
| `patch-gh-actions-requests-tests` | `ci_real_tests` | `https://api.github.com/repos/psf/requests/actions/workflows/run-tests.yml/runs?per_page=1&status=completed` |

### `CROSS_CHAIN_STATE_VERIFY` (6 OK)

| Slug | Fit | URL |
|------|-----|-----|
| `xchain-wormholescan` | `bridge_status` | `https://api.wormholescan.io/api/v1/operations?page=0&pageSize=5` |
| `xchain-across-deposits` | `bridge_status` | `https://across.to/api/deposits?limit=5` |
| `xchain-axelarscan-search` | `bridge_status` | `https://api.axelarscan.io/gmp/searchGMP?size=5` |
| `xchain-axelar-transfers` | `bridge_status` | `https://api.axelarscan.io/token/searchTransfers?size=5` |
| `xchain-across-suggested-fees` | `bridge_quote_partial` | `https://across.to/api/suggested-fees?token=0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2&destinationChainId=10&am…` |
| `xchain-relay-requests` | `bridge_status` | `https://api.relay.link/requests/v2?limit=5` |

### `EVENT_OUTCOME_RESOLUTION` (11 OK)

| Slug | Fit | URL |
|------|-----|-----|
| `event-thesportsdb-last` | `settled_sports` | `https://www.thesportsdb.com/api/v1/json/3/eventslast.php?id=133602` |
| `event-thesportsdb-lookup` | `settled_sports` | `https://www.thesportsdb.com/api/v1/json/3/lookupevent.php?id=1036723` |
| `event-poly-closed` | `prediction_resolved` | `https://gamma-api.polymarket.com/events?closed=true&limit=5` |
| `event-poly-markets-closed` | `prediction_resolved` | `https://gamma-api.polymarket.com/markets?closed=true&limit=5` |
| `event-espn-nba-scoreboard` | `settled_sports` | `https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20240617` |
| `event-espn-nfl-scoreboard` | `settled_sports` | `https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?dates=20240211` |
| `event-espn-mlb-scoreboard` | `settled_sports` | `https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard?dates=20241030` |
| `event-mlb-statsapi` | `settled_sports` | `https://statsapi.mlb.com/api/v1/schedule?sportId=1&date=2024-10-30&hydrate=decisions` |
| `event-nhl-schedule` | `settled_sports` | `https://api-web.nhle.com/v1/score/2024-06-24` |
| `event-openligadb-bl1` | `settled_sports` | `https://api.openligadb.de/getmatchdata/bl1/2023` |
| `event-jolpica-f1` | `settled_sports` | `https://api.jolpi.ca/ergast/f1/2024/1/results.json` |

### `LIQUIDITY_DEPTH_VERIFY` (12 OK)

| Slug | Fit | URL |
|------|-----|-----|
| `liq-gecko-eth-usdc-pool` | `dex_pool` | `https://api.geckoterminal.com/api/v2/networks/eth/pools/0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640` |
| `liq-gecko-base-trending` | `dex_pool` | `https://api.geckoterminal.com/api/v2/networks/base/trending_pools` |
| `liq-gecko-search-eth` | `dex_pool` | `https://api.geckoterminal.com/api/v2/search/pools?query=WETH%20USDC&network=eth` |
| `liq-dexscreener-pair` | `dex_pool` | `https://api.dexscreener.com/latest/dex/pairs/ethereum/0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640` |
| `liq-dexscreener-token-weth` | `dex_pool` | `https://api.dexscreener.com/latest/dex/tokens/0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2` |
| `liq-dexscreener-search-btc` | `dex_pool` | `https://api.dexscreener.com/latest/dex/search?q=WBTC%20USDC` |
| `liq-bybit-orderbook` | `cex_book` | `https://api.bybit.com/v5/market/orderbook?category=spot&symbol=BTCUSDT&limit=50` |
| `liq-kucoin-orderbook` | `cex_book` | `https://api.kucoin.com/api/v1/market/orderbook/level2_20?symbol=BTC-USDT` |
| `liq-gate-orderbook` | `cex_book` | `https://api.gateio.ws/api/v4/spot/order_book?currency_pair=BTC_USDT&limit=50` |
| `liq-mexc-depth` | `cex_book` | `https://api.mexc.com/api/v3/depth?symbol=BTCUSDT&limit=50` |
| `liq-bitget-orderbook` | `cex_book` | `https://api.bitget.com/api/v2/spot/market/orderbook?symbol=BTCUSDT&limit=50` |
| `liq-binance-depth` | `cex_book` | `https://api.binance.com/api/v3/depth?symbol=BTCUSDT&limit=50` |

### `ONCHAIN_METRIC_VERIFY` (11 OK)

| Slug | Fit | URL |
|------|-----|-----|
| `ocm-blockscout-eth` | `balance` | `https://eth.blockscout.com/api/v2/addresses/0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045` |
| `ocm-blockscout-base` | `balance` | `https://base.blockscout.com/api/v2/addresses/0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045` |
| `ocm-blockscout-optimism` | `balance` | `https://optimism.blockscout.com/api/v2/addresses/0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045` |
| `ocm-blockscout-polygon` | `balance` | `https://polygon.blockscout.com/api/v2/addresses/0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045` |
| `ocm-blockscout-gnosis` | `balance` | `https://gnosis.blockscout.com/api/v2/addresses/0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045` |
| `ocm-blockscout-arbitrum` | `balance` | `https://arbitrum.blockscout.com/api/v2/addresses/0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045` |
| `ocm-blockscout-scroll` | `balance` | `https://scroll.blockscout.com/api/v2/addresses/0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045` |
| `ocm-ethplorer-addr` | `balance_tokens` | `https://api.ethplorer.io/getAddressInfo/0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045?apiKey=freekey` |
| `ocm-blockcypher-eth` | `balance` | `https://api.blockcypher.com/v1/eth/main/addrs/0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045/balance` |
| `ocm-blockstream-btc` | `balance_utxo` | `https://blockstream.info/api/address/bc1qgdjqv0av3q56jvd82tkdjpy7gdp9ut8tlqmgrpmv24sq90ecnvqqjwvw97` |
| `ocm-etherscan-balance` | `balance` | `https://api.etherscan.io/api?module=account&action=balance&address=0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045&…` |

### `OPTIMAL_EXECUTION_ROUTE` (8 OK)

| Slug | Fit | URL |
|------|-----|-----|
| `route-lifi-quote` | `swap_quote` | `https://li.quest/v1/quote?fromChain=1&toChain=1&fromToken=ETH&toToken=USDC&fromAmount=1000000000000000000&from…` |
| `route-paraswap-price` | `swap_quote` | `https://apiv5.paraswap.io/prices?srcToken=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE&destToken=0xA0b86991c6218…` |
| `route-kyber-route` | `swap_quote` | `https://aggregator-api.kyberswap.com/ethereum/api/v1/routes?tokenIn=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE…` |
| `route-sushi-quote` | `swap_quote` | `https://api.sushi.com/swap/v7/1?tokenIn=0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2&tokenOut=0xA0b86991c6218b36…` |
| `route-bebop-quote` | `swap_quote` | `https://api.bebop.xyz/pmm/ethereum/v3/quote?buy_tokens=0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48&sell_tokens=…` |
| `route-kyber-bsc` | `swap_quote` | `https://aggregator-api.kyberswap.com/bsc/api/v1/routes?tokenIn=0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c&toke…` |
| `route-paraswap-usdt` | `swap_quote` | `https://apiv5.paraswap.io/prices?srcToken=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE&destToken=0xdAC17F958D2ee…` |
| `route-lifi-arb-usdc` | `swap_quote` | `https://li.quest/v1/quote?fromChain=1&toChain=42161&fromToken=ETH&toToken=USDC&fromAmount=1000000000000000000&…` |

### `SECURITY_REVIEW` (11 OK)

| Slug | Fit | URL |
|------|-----|-----|
| `secrev-depsdev` | `pkg_advisories` | `https://api.deps.dev/v3/systems/npm/packages/lodash/versions/4.17.20` |
| `secrev-pypi-django` | `pkg_advisories` | `https://pypi.org/pypi/django/3.0/json` |
| `secrev-pypi-requests` | `pkg_advisories` | `https://pypi.org/pypi/requests/2.19.0/json` |
| `secrev-osv-ghsa` | `advisory` | `https://api.osv.dev/v1/vulns/GHSA-jfh8-c2jp-5v3q` |
| `secrev-osv-cve` | `advisory` | `https://api.osv.dev/v1/vulns/CVE-2021-44228` |
| `secrev-depsdev-pypi` | `pkg_advisories` | `https://api.deps.dev/v3/systems/pypi/packages/django/versions/3.0` |
| `secrev-depsdev-maven` | `pkg_advisories` | `https://api.deps.dev/v3/systems/maven/packages/org.apache.logging.log4j%3Alog4j-core/versions/2.14.1` |
| `secrev-depsdev-cargo` | `pkg_advisories` | `https://api.deps.dev/v3/systems/cargo/packages/openssl/versions/0.10.0` |
| `secrev-npm-lodash-pkg` | `pkg_meta_partial` | `https://registry.npmjs.org/lodash/4.17.20` |
| `secrev-rubygems-rails` | `pkg_meta_partial` | `https://rubygems.org/api/v2/rubygems/rails/versions/5.0.0.json` |
| `secrev-crates-openssl` | `pkg_meta_partial` | `https://crates.io/api/v1/crates/openssl/0.10.0` |

### `VULNERABILITY_TRIAGE` (10 OK)

| Slug | Fit | URL |
|------|-----|-----|
| `vuln-shodan-cvedb` | `cvss` | `https://cvedb.shodan.io/cve/CVE-2021-44228` |
| `vuln-epss` | `epss` | `https://api.first.org/data/v1/epss?cve=CVE-2021-44228` |
| `vuln-cisa-kev` | `exploit_in_wild` | `https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json` |
| `vuln-nvd-cve` | `cvss` | `https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2021-44228` |
| `vuln-circl-cve` | `cvss` | `https://cve.circl.lu/api/cve/CVE-2021-44228` |
| `vuln-osv-cve` | `advisory_severity` | `https://api.osv.dev/v1/vulns/CVE-2021-44228` |
| `vuln-redhat-cve` | `cvss` | `https://access.redhat.com/hydra/rest/securitydata/cve/CVE-2021-44228.json` |
| `vuln-mitre-cveorg` | `cve_record` | `https://cveawg.mitre.org/api/cve/CVE-2021-44228` |
| `vuln-ghsa-advisory` | `advisory_severity` | `https://api.osv.dev/v1/vulns/GHSA-jfh8-c2jp-5v3q` |
| `vuln-alpine-secdb` | `distro_advisories` | `https://secdb.alpinelinux.org/v3.19/main.json` |

## How to use

1. Capture (example):
```bash
python3 scripts/capture_api_output.py \
  --intent LIQUIDITY_DEPTH_VERIFY \
  --slug liq-gecko-eth-usdc-pool \
  --url 'https://api.geckoterminal.com/api/v2/networks/eth/pools/0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640' \
  --inputs 'Uniswap V3 WETH/USDC'
```
2. Auto-review: `python3 scripts/auto_review_samples.py` then `--apply` if report looks good.
3. Build YAML + host + `./scripts/register-miner-v2.sh … --sample …`

## Already approved samples (from prior batch)

- ONCHAIN: 5× blockscout
- SECURITY: secrev-depsdev, secrev-pypi
- VULN: epss, shodan, ubuntu, cisa-kev
- EVENT: event-thesportsdb-last

## Not 10 yet / blocked

| Intent | Smoke OK | Why short |
|--------|---------:|-----------|
| `OPTIMAL_EXECUTION_ROUTE` | ~7 | Keyed aggregators (1inch/0x); some CF/DNS fails |
| `CROSS_CHAIN_STATE_VERIFY` | ~6 | Many explorers need a **real filled tx hash**; meta-only APIs rejected |
| `CODE_REVIEW` / `WASH_TRADING` | 0 | Still blocked (POST+LLM / no free verdict API) |

## Distinct-source rule

Usman: **one miner = one upstream**. Multiple Blockscout chains count as distinct chains/sources;
multiple CEX books are distinct publishers; do not register two miners that hit the same host+API as clones.

