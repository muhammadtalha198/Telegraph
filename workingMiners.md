# workingMiners

> **Scope:** wired keepers only (~39), not the full Active list. Count of record = `INTENT_BUILD_SHEET-2026-09-23.md` / `out/ACTIVE_PREACTIVE_MINERS.xlsx`. Live truth = `out/RECONCILED_REG_IDS.md`.

**Rule (Usman):** one miner = one source. Ranking needs distinct upstreams; clones only alphabetise ties.

- YAML host: https://omni-chat.13.237.89.59.sslip.io/miner-yamls/
- Diamond: `0x5a2324aA18613FAD4e44bDF0d6c73Ec1f6D87ff8`
- Catalog build sheet: [INTENT_BUILD_SHEET-2026-09-23.md](./INTENT_BUILD_SHEET-2026-09-23.md)
- Doctrine: [MINER_BUILD_PLAN-2026-09-23.md](./MINER_BUILD_PLAN-2026-09-23.md)
- Updated: **2026-09-29** — **39** keepers (prior 28 + CRYPTO_YIELD 7 + EVENT_OUTCOME 3 + VESSEL 1). Groups A–D closed.

This file lists only miners that are **Usman-side keepers**: multi-source **rankable**, or **single-source** (not ranked yet — need a second distinct publisher). New registrations awaiting Usman go in [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) only.

---

## Inventory

| Intent | Bucket | Keepers | Sources |
|--------|--------|--------:|--------:|
| **FX_NOW** | rankable | 11 | 11 |
| **VULNERABILITY_TRIAGE** | rankable | 4 | 4 |
| **EMAIL_SECURITY** | rankable | 2 | 2 |
| **ROUTE_ETA** | rankable | 2 | 2 |
| **MACRO_ECONOMIC_INDICATOR** | rankable | 2 | 2 |
| **LIQUIDITY_DEPTH_VERIFY** | rankable | 2 | 2 |
| **CRYPTO_YIELD_RATE** | rankable · not wired | 7 | 7 |
| **EVENT_OUTCOME_RESOLUTION** | rankable · not wired | 3 | 3 |
| **ASSET_RESERVE_ATTESTATION** | single-source | 1 | 1 |
| **GRID_POWER_PRICE** | single-source | 1 | 1 |
| **LIVE_SHELF_PRICE** | single-source | 1 | 1 |
| **MINING_HASHPRICE_VERIFY** | single-source | 1 | 1 |
| **ONCHAIN_METRIC_VERIFY** | single-source | 1 | 1 |
| **VESSEL_TELEMETRY_VERIFY** | single-source · not wired | 1 | 1 |

**Total: 39 keepers.**

---

## Rankable (multi-source)

### FX_NOW

| Name | Reg ID | Slug | YAML | Tx |
|------|--------|------|------|-----|
| fx-awesomeapi | 1396 | `fx-awesomeapi` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/fx-awesomeapi.yaml) | [tx](https://sepolia.basescan.org/tx/0x6033732006a80bcec8cbb85b363a16f13d419337ee153cce51675d4d0ae8868d) |
| fx-boc | 1397 | `fx-boc` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/fx-boc.yaml) | [tx](https://sepolia.basescan.org/tx/0x47d06efca48bbf649175f697ecf518219aa22394d09f98f2b8ef5c21595e0dd3) |
| fx-cbr | 1398 | `fx-cbr` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/fx-cbr.yaml) | [tx](https://sepolia.basescan.org/tx/0x4aabc2910135b4b83864c08f92f0051182779739ffbb1658ac184ededb04b6a2) |
| fx-coinbase | 1399 | `fx-coinbase` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/fx-coinbase.yaml) | [tx](https://sepolia.basescan.org/tx/0x07313a00da1d8207f17896d01068b21a9e421bccfa2ebeca5105c1daac11ddc5) |
| fx-er-api | 1400 | `fx-er-api` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/fx-er-api.yaml) | [tx](https://sepolia.basescan.org/tx/0x5b16c009f55d60eef3f4a8b5e80cd96b3a00775ddc504934d993e4d236ce898c) |
| fx-erapi-v4 | 1401 | `fx-erapi-v4` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/fx-erapi-v4.yaml) | [tx](https://sepolia.basescan.org/tx/0x0a288eec7119c47fc04e1cd9dd11862523279ae7de42d6f22cd7dac136fdc875) |
| fx-fawaz | 1402 | `fx-fawaz` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/fx-fawaz.yaml) | [tx](https://sepolia.basescan.org/tx/0xf016c54c47f0bfe7c8f75b884582fd736d25ea8513f3a6a9116626b2c567b9d0) |
| fx-frankfurter | 1403 | `fx-frankfurter` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/fx-frankfurter.yaml) | [tx](https://sepolia.basescan.org/tx/0x8641a23c1648e7851787758227d5896947f750d94de9e53a6bb4e409615086bd) |
| fx-riksbank | 1404 | `fx-riksbank` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/fx-riksbank.yaml) | [tx](https://sepolia.basescan.org/tx/0x6b52a584ff317ddddf1a5519defbdfd834e86432b21cf71bc2d5ebb834351fd8) |
| fx-vatcomply | 1405 | `fx-vatcomply` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/fx-vatcomply.yaml) | [tx](https://sepolia.basescan.org/tx/0x5ef901640d2e8a6734ff9f791b8e54f588736af0637b63e3ba2e69498f6b6cad) |
| HNB FX Now | 1406 | `fx-hnb` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/fx-hnb.yaml) |  |

### VULNERABILITY_TRIAGE

| Name | Reg ID | Slug | YAML | Tx |
|------|--------|------|------|-----|
| NVD CVE By Id | 2768 | `vuln-nvd-cve` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/vuln-nvd-cve.yaml) | [tx](https://sepolia.basescan.org/tx/0x9afc5adbd0796d403cd34825e2f6af4e83f57e57f262c7cf6d7f3c3764fb320c) |
| vuln-cveorg-cvss | 2785 | `vuln-cveorg-cvss` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/vuln-cveorg-cvss.yaml) | [tx](https://sepolia.basescan.org/tx/0x24fd3dd46cc3cbe830790dfaab88390407391876ae307386d61f581d2456ec08) |
| vuln-circl-cvss | 2811 | `vuln-circl-cvss` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/vuln-circl-cvss.yaml) | [tx](https://sepolia.basescan.org/tx/0xa5cfc46bb12da2d934ceeb3e8c4a4db823c1d885af8c96b05e9e39c5927c94a9) |
| vuln-osv-cvss | 2812 | `vuln-osv-cvss` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/vuln-osv-cvss.yaml) | [tx](https://sepolia.basescan.org/tx/0x135893c4449878c461bde924022d0181c3109c9a268d81aea6232d1fc802dff6) |

### EMAIL_SECURITY

| Name | Reg ID | Slug | YAML | Tx |
|------|--------|------|------|-----|
| Cloudflare DoH Gmail MX | 1653 | `email-cf-gmail-mx` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/email-cf-gmail-mx.yaml) | [tx](https://sepolia.basescan.org/tx/0x1870cf3810aa207033462fc13884892ef3e864e59a40dfa4f7fec21756023411) |
| Google DoH Gmail DMARC | 1655 | `email-dns-dmarc-gmail` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/email-dns-dmarc-gmail.yaml) | [tx](https://sepolia.basescan.org/tx/0x15bdd5d7eadcc1531407a3cbfa7f4edcec8e0aad732e624238611a6be1d9aabe) |

### ROUTE_ETA

| Name | Reg ID | Slug | YAML | Tx |
|------|--------|------|------|-----|
| OSRM Berlin Local | 1663 | `route-osrm-berlin` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/route-osrm-berlin.yaml) | [tx](https://sepolia.basescan.org/tx/0xf18aca7a53143b0e48689429fc2895e262aac86aa47ac3b1ff246782fe458675) |
| OSRM Duration Table | 1668 | `route-osrm-table` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/route-osrm-table.yaml) | [tx](https://sepolia.basescan.org/tx/0xf8d571e8b29b26afa73bae04a60b23dd39f9d026abd49617216eb2a8f243b59c) |

### MACRO_ECONOMIC_INDICATOR

| Name | Reg ID | Slug | YAML | Tx |
|------|--------|------|------|-----|
| World Bank US Unemployment | 2753 | `macro-wb-unemp-us` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/macro-wb-unemp-us.yaml) | [tx](https://sepolia.basescan.org/tx/0xefee12bf5878f7e2bfdb47fbbb9ccf8d4646fea0a9b6bdc29b9bd0f96a59c77f) |
| macro-wb-unemp-proxy | 2784 | `macro-wb-unemp-proxy` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/macro-wb-unemp-proxy.yaml) | [tx](https://sepolia.basescan.org/tx/0x4b3039e1ee929f04bf6c96a604ea6d0b1c228273ac8fb7235dbf214ff667840f) |

### LIQUIDITY_DEPTH_VERIFY

| Name | Reg ID | Slug | YAML | Tx |
|------|--------|------|------|-----|
| GeckoTerminal Pool Cents | 2765 | `liq-gecko-pool-cents` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/liq-gecko-pool-cents.yaml) | [tx](https://sepolia.basescan.org/tx/0x50a42892b02d970b1abf8da5f03d43bb7cdde9b10c0211b7a9a90845e79dc848) |
| DexScreener Pair Cents | 2766 | `liq-dex-pair-cents` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/liq-dex-pair-cents.yaml) | [tx](https://sepolia.basescan.org/tx/0x5f9c6b472e5c7757d6e1bd5e0f68aac12b59fcdd2e94ca3c5d64a08ad45fa741) |

### CRYPTO_YIELD_RATE

Shared askable `pool`. Field `apy_bps`. RelTol 500. Regs **4356–4361** + compound **4375** (ignore old 2870–2876 / 4362–4363).

| Name | Reg ID | Slug | YAML | Tx |
|------|--------|------|------|-----|
| DefiLlama Yields | 4357 | `yld-defillama` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/yld-defillama.yaml) | [tx](https://sepolia.basescan.org/tx/0xc6ae1e17b3fd2665686c55eb2341667a6ee9d99fa3abc15aa9d21cf6e881311f) |
| Lido | 4356 | `yld-lido` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/yld-lido.yaml) | [tx](https://sepolia.basescan.org/tx/0xf8e1a2591d97bbc9b5e9ff7bf91e996c03094fbbae9b155d43a4e2c16d0275f1) |
| Rocket Pool | 4358 | `yld-rocketpool` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/yld-rocketpool.yaml) | [tx](https://sepolia.basescan.org/tx/0xa5b8348960685d04d1578ee8c941ebd148cb2ed109af908ca05d25eb9955926a) |
| Frax | 4359 | `yld-frax` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/yld-frax.yaml) | [tx](https://sepolia.basescan.org/tx/0xa9b4a313b9dc8b24fdbd84885e45046393fe185958db8bffe90b1000be44ee97) |
| Stader | 4360 | `yld-stader` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/yld-stader.yaml) | [tx](https://sepolia.basescan.org/tx/0x972679e9c9d698472edc181ccc8a627dd0080b6e598471b3b0789509fb8450f6) |
| Aave | 4361 | `yld-aave` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/yld-aave.yaml) | [tx](https://sepolia.basescan.org/tx/0xc6975f53f7d72b76adfac6f2ced157abedb47c82495a12b316e01f31b4a0d1a4) |
| Compound | 4375 | `yld-compound` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/yld-compound.yaml) | [tx](https://sepolia.basescan.org/tx/0x8176a256e739460abcae0eb591a24205d4a1d83d41898f5f9784a233df6df260) |

### EVENT_OUTCOME_RESOLUTION

Field `resolved_yes`. PassFail. Kalshi re-pinned **4364** (ignore old 2850).

| Name | Reg ID | Slug | YAML | Tx |
|------|--------|------|------|-----|
| Polymarket | 2849 | `event-poly-clob-winner` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/event-poly-clob-winner.yaml) | [tx](https://sepolia.basescan.org/tx/0x6d98ba12ee445967656c4c9cfd794d1543d57e572c9cb1f592d44ce0efdb3ec6) |
| Kalshi | 4364 | `event-kalshi-result` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/event-kalshi-result.yaml) | [tx](https://sepolia.basescan.org/tx/0xee49b83fb0c4a5ac717adaa99457e8c9934c9ca30ce42c02538b65038a32b8e5) |
| Manifold | 2851 | `event-manifold-resolution` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/event-manifold-resolution.yaml) | [tx](https://sepolia.basescan.org/tx/0xb8dc4c7695b14cf457cab961a5f4d020876f5240ff9c2420f40f98f7bc8f35d5) |

---

## Single-source (not ranked yet — need a 2nd distinct publisher)

### ASSET_RESERVE_ATTESTATION

| Name | Reg ID | Slug | YAML | Tx |
|------|--------|------|------|-----|
| Chainlink WBTC PoR | 2763 | `res-wbtc-por` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/res-wbtc-por.yaml) | [tx](https://sepolia.basescan.org/tx/0x55ba052ac4f5d81b8aacb3128c604917d5d1fa05b6275b27d1cf41dad785f35a) |

### GRID_POWER_PRICE

| Name | Reg ID | Slug | YAML | Tx |
|------|--------|------|------|-----|
| CAISO NP15 DAM LMP | 2758 | `grid-caiso-np15-dam` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/grid-caiso-np15-dam.yaml) | [tx](https://sepolia.basescan.org/tx/0xcc739dc2237db369028563c9b126c70690f729444027e7b81cef307046424aca) |

### LIVE_SHELF_PRICE

| Name | Reg ID | Slug | YAML | Tx |
|------|--------|------|------|-----|
| Open Prices By Id | 2759 | `shelf-open-prices` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/shelf-open-prices.yaml) | [tx](https://sepolia.basescan.org/tx/0xfb8fb91014ae7c354c54b51c31541205a6b1f1ad180dbd99de2b11320e70f478) |

### MINING_HASHPRICE_VERIFY

| Name | Reg ID | Slug | YAML | Tx |
|------|--------|------|------|-----|
| Mempool Hashprice By Height | 2764 | `mine-mempool-hashprice` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/mine-mempool-hashprice.yaml) | [tx](https://sepolia.basescan.org/tx/0x89ea155bd4a281b24e7b46b6ec914b25c973ee4633d54e1bfadf7f571e48672c) |

### ONCHAIN_METRIC_VERIFY

| Name | Reg ID | Slug | YAML | Tx |
|------|--------|------|------|-----|
| ETH Balance At Block | 2761 | `ocm-eth-balance` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/ocm-eth-balance.yaml) | [tx](https://sepolia.basescan.org/tx/0x687979e506d80f6a12a9b5fb90ef80623e3fa1ffa74f862f2523928cecbfae52) |

### VESSEL_TELEMETRY_VERIFY

Field `sog_milliknots`. Pin `230981000` (+ AIS fallbacks). Reg **4365** (ignore old 2936).

| Name | Reg ID | Slug | YAML | Tx |
|------|--------|------|------|-----|
| Fintraffic Digitraffic AIS | 4365 | `ves-digitraffic` | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/ves-digitraffic.yaml) | [tx](https://sepolia.basescan.org/tx/0xe904ca271d47bc438a445ed8074a3d8b903a0cb28c45049a8d6c5e5466f01799) |
