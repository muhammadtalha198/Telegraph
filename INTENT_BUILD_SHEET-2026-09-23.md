# Intent build sheet — verifiable catalog intents

**Source:** `Intent Catalog v2 25-Sept (1).xlsx` (sheet Intent Catalog)
**Filter:** drop rows where `Verifiable` = `No` (obsolete / not independently reproducible).
**Doctrine:** `MinerCreator/MINER_BUILD_PLAN-2026-09-23.md` — quantity sentence, askable pins, distinct source, description check necessary but not sufficient.
**Hard rule (Usman):** **one miner = one source.** Ranking needs distinct upstreams. Same-source clones were removed 2026-09-23 (**71 deregistered → 28 keepers**). Do **not** follow catalog “How to Scale to 10+ Miners Instantly” as a clone recipe.

- Active (buildable pool): **97**
- Obsolete (`Verifiable=No`): **22** — listed at bottom, do not build
- Live keepers: **`workingMiners.md`** (39 wired keepers; Active pool larger — see below)
- Lifecycle Index: **Active → Not registered → Dead** (Pre-active removed 2026-10-06)
## Miner tables (YAML links)

1. **[Active — 289 miners](#active-miner-tables-usman-verified)** (all registered)

# Active miner tables (Usman verified)

**289 miners · 56 intents** — YAML host: [omni-chat miner-yamls](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/) + paste.rs for later V2 batches. Wired keepers: [`workingMiners.md`](./workingMiners.md).

**2026-10-06:** All former Pre-active miners promoted to Active (NON-DET + Semantic V2 + Pack V2). Lifecycle no longer uses a Pre-active bucket.

### `AIR_QUALITY_INDEX` — 7 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `aqi-cerns` | DETERMINISTIC | 2960 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/aqi-cerns.yaml) | [tx](https://sepolia.basescan.org/tx/0x6114213b100a24ee70910786ddb7972db57da8e64b2e7915591b9db2bdadeaba) |
| `aqi-infranode` | DETERMINISTIC | 2961 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/aqi-infranode.yaml) | [tx](https://sepolia.basescan.org/tx/0x284a7f652119d1a3ffdd584e551abd27e8c08feff5c3859c06ca827138c49dee) |
| `aqi-luchtmeetnet` | DETERMINISTIC | 2905 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/aqi-luchtmeetnet.yaml) | [tx](https://sepolia.basescan.org/tx/0x8ff5186d488b383de58f6d1e9e6771db342a0aa72e63489d862d96c235646f99) |
| `aqi-neasg` | DETERMINISTIC | 2906 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/aqi-neasg.yaml) | [tx](https://sepolia.basescan.org/tx/0x0afd2e0b0a6aa6ea35cceab56911a9742b4066e9b2fe245b245119b7d0fff82c) |
| `aqi-openmeteo` | DETERMINISTIC | 2903 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/aqi-openmeteo.yaml) | [tx](https://sepolia.basescan.org/tx/0x2209d89094faa67ae9547cf68b46fc31480297bb04f6d8153cfa085ad5b939ed) |
| `aqi-sensorcommunity` | DETERMINISTIC | 2907 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/aqi-sensorcommunity.yaml) | [tx](https://sepolia.basescan.org/tx/0x2ea83219599d9a3c71c361d2696c9143ad14aec4cf99df1fabee301224784dcd) |
| `aqi-uba` | DETERMINISTIC | 2904 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/aqi-uba.yaml) | [tx](https://sepolia.basescan.org/tx/0x5b05fedde3806d2d73fb98f2ae94669980526d949771d2aa309ad3999fbbba95) |

### `API_HEALTH_CHECK` — 2 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `hlt-checkhost` | DETERMINISTIC | 2925 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/hlt-checkhost.yaml) | [tx](https://sepolia.basescan.org/tx/0xdace9dcc6048421a7ad4cfd4dd722c8af85728c1e9dce590b1bdcea051722b3e) |
| `hlt-hackertarget` | DETERMINISTIC | 2927 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/hlt-hackertarget.yaml) | [tx](https://sepolia.basescan.org/tx/0x15bafb0af3746945dacbbebc5055166dd1c1ae1cf4ef9760fe2b4513e074d8bb) |

### `ASSET_RESERVE_ATTESTATION` — 1 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `res-wbtc-por` | DETERMINISTIC | 2763 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/res-wbtc-por.yaml) | [tx](https://sepolia.basescan.org/tx/0x55ba052ac4f5d81b8aacb3128c604917d5d1fa05b6275b27d1cf41dad785f35a) |

### `CARRIER_SERVICEABILITY` — 2 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `car-auspost` | DETERMINISTIC | 2938 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/car-auspost.yaml) | [tx](https://sepolia.basescan.org/tx/0x00fd456053b26c91b5e2c440d25311b9b366c6e7d839a15a5930fbda9e936719) |
| `car-indiapost` | DETERMINISTIC | 2937 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/car-indiapost.yaml) | [tx](https://sepolia.basescan.org/tx/0x9b8e82df4598f630344f56ce620001d0c2f6e3c41873a781cd820b27aaa333c4) |

### `CHATBOT_CONVERSATION` — 3 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `chat-aihorde` | NON-DETERMINISTIC | 4399 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/chat-aihorde.yaml) | [tx](https://sepolia.basescan.org/tx/0x14a824c58d7565b7e187e016e412bef8adaef707a8e26ea98e308979c4267aff) |
| `chat-nova` | NON-DETERMINISTIC | 4401 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/chat-nova.yaml) | [tx](https://sepolia.basescan.org/tx/0xfdc74775d5d61e099d239fbdf42cfc4f27595c3400594f9e349f989de455177d) |
| `chat-pollinations` | NON-DETERMINISTIC | 4395 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/chat-pollinations.yaml) | [tx](https://sepolia.basescan.org/tx/0xcb2b32dadf70d4daa0de04ba3c9c234e7aec33089ebc3972279d191dfe950a79) |

### `CLOUD_RESOURCE_USAGE` — 2 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `prm-prometheusio` | DETERMINISTIC | 2930 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/prm-prometheusio.yaml) | [tx](https://sepolia.basescan.org/tx/0xadf45044003bc78d60ac3eda02f34c0e86f06a3b49b41cbf1cc5fb188689c81e) |
| `prm-promlabs` | DETERMINISTIC | 2929 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/prm-promlabs.yaml) | [tx](https://sepolia.basescan.org/tx/0x943b9f4546ffcfc70d6878dfd067803c00123308d192841d40449f6316cedcaf) |

### `CODE_PATCH_VERIFY` — 7 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `patch-circleci-recent` | DETERMINISTIC | 4519 | [yaml](https://paste.rs/84PcO) | [tx](https://sepolia.basescan.org/tx/0x85e2bc841e1bed73d99f2d7ef71fcb82e1545353ffd9885ee5ed83a2398202df) |
| `patch-gh-actions-requests-tests` | DETERMINISTIC | 4497 | [yaml](https://paste.rs/VDAwS) | `0x41e282dbca1451a2…` |
| `patch-gh-commit-check` | DETERMINISTIC | 4497 | [yaml](https://paste.rs/EhQ9Y) | `0x7a33546974fec012…` |
| `patch-gitlab-pipeline` | DETERMINISTIC | 4498 | [yaml](https://paste.rs/0lC0F) | `0x0d54f868429bbeab…` |
| `patch-godbolt` | DETERMINISTIC | 2845 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/patch-godbolt.yaml) | [tx](https://sepolia.basescan.org/tx/0x2a717dee6b7f8b607eed9b7a1444e065a0f3d1feb6be56f35616ff7b8f68607f) |
| `patch-judge0-ce` | DETERMINISTIC | 2843 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/patch-judge0-ce.yaml) | [tx](https://sepolia.basescan.org/tx/0x781b532a2feabe862749fb15a0f2a7a5a2c72a061948e626c5b787003f245960) |
| `patch-wandbox` | DETERMINISTIC | 2844 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/patch-wandbox.yaml) | [tx](https://sepolia.basescan.org/tx/0x323ba4097ec69649330238a2ca8489db45c75719d422eacc1af3b973593fd7d9) |

### `CONTENT_EXTRACTION` — 2 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `cex-jina` | DETERMINISTIC | 2945 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/cex-jina.yaml) | [tx](https://sepolia.basescan.org/tx/0x6d22fdc64e90bed3aaf7acc1f2a31a76d5b1f865cffbea480164d5163f9255e2) |
| `cex-urltomarkdown` | DETERMINISTIC | 2946 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/cex-urltomarkdown.yaml) | [tx](https://sepolia.basescan.org/tx/0x374c97eaa464b2916146dbd44e325ff7406e019eeaaec5139dd52bb8507f72f9) |

### `CORPORATE_REGISTRY_LOOKUP` — 6 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `corp-brreg` | DETERMINISTIC | 2966 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/corp-brreg.yaml) | [tx](https://sepolia.basescan.org/tx/0x86a84e99db5da87e768867ae6a438acdd18c873cf05041e836a40e5cfcf9b8f7) |
| `corp-brreg-no` | DETERMINISTIC | 4627 | [yaml](https://paste.rs/KToEC) | [tx](https://sepolia.basescan.org/tx/0x94efe91ce9d921ab31dddb9b6844c425ae6ff4212a9dc05526ecd2c93b09750b) |
| `corp-fr-recherche` | DETERMINISTIC | 2862 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/corp-fr-recherche.yaml) | [tx](https://sepolia.basescan.org/tx/0x2b2898691725d1e9e15d2336d0628856c0bbd03b19b2a4dfe654b77262207e9a) |
| `corp-gleif-status` | DETERMINISTIC | 2861 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/corp-gleif-status.yaml) | [tx](https://sepolia.basescan.org/tx/0xc78b57d74468bb5de7707e05b749d0b28e5129488afb069c28e34c44de01262f) |
| `corp-krs-pl` | DETERMINISTIC | 4629 | [yaml](https://paste.rs/20Nz7) | [tx](https://sepolia.basescan.org/tx/0x12b5f28b939222c3d0779ba9229cfb0e68546fa11d35ac0936bfcfbca224f74f) |
| `corp-prh-fi` | DETERMINISTIC | 4629 | [yaml](https://paste.rs/lYxfZ) | [tx](https://sepolia.basescan.org/tx/0xd790bf2ebdff8ffdcbbd127278398105712c925489c681ad76120edca2c36d1c) |

### `CROSS_CHAIN_STATE_VERIFY` — 12 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `xchain-across-deposit` | DETERMINISTIC | 2848 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/xchain-across-deposit.yaml) | [tx](https://sepolia.basescan.org/tx/0x8cbe232c071401f3cf2aed9a12f6b075c96ffa102d9d9b17df44cb3ea947b6df) |
| `xchain-across-deposits` | DETERMINISTIC | 4499 | [yaml](https://paste.rs/yFgSV) | `0xc738ef184de8d2e2…` |
| `xchain-arbitrum-root` | DETERMINISTIC | 4631 | [yaml](https://paste.rs/L9HBw) | [tx](https://sepolia.basescan.org/tx/0xa051a41a7c845507ef6f2e9b508b57c5435f9f405a625ac5d81964635e63c88e) |
| `xchain-axelar-gmp` | DETERMINISTIC | 2846 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/xchain-axelar-gmp.yaml) | [tx](https://sepolia.basescan.org/tx/0x288e6ae1902c7ebf79346096274feb8a23d2b1a6905008a8846e8e459316b926) |
| `xchain-axelar-transfers` | DETERMINISTIC | 4500 | [yaml](https://paste.rs/pTeWl) | `0x6ce5e924b0718d2f…` |
| `xchain-axelarscan-search` | DETERMINISTIC | 4501 | [yaml](https://paste.rs/HJFoZ) | `0xeb537b042a41b4f2…` |
| `xchain-base-root` | DETERMINISTIC | 4632 | [yaml](https://paste.rs/lGZJH) | [tx](https://sepolia.basescan.org/tx/0x4e58f70a534a3b12c21f5c1d3567839a5d48f3a09d38eff7630415359e066f20) |
| `xchain-beacon-publicnode` | DETERMINISTIC | 4601 | [yaml](https://paste.rs/TWxxo) | [tx](https://sepolia.basescan.org/tx/0xe4e775214663b9fff52bd80aefb054d8d098a318c5acff42c6391c52e6ed5c80) |
| `xchain-optimism-root` | DETERMINISTIC | 4632 | [yaml](https://paste.rs/5Shbl) | [tx](https://sepolia.basescan.org/tx/0xe50cc5c71fcaea5db29020b4a26246f35df86d5e316bc8bef321fee3e79a1f9e) |
| `xchain-relay-requests` | DETERMINISTIC | 4503 | [yaml](https://paste.rs/DvzgF) | `0x610d0999ccfe6296…` |
| `xchain-wormhole-vaa` | DETERMINISTIC | 2847 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/xchain-wormhole-vaa.yaml) | [tx](https://sepolia.basescan.org/tx/0x09a1670435d0a35c5e8bf06b5a71ab1b892f4aab294e563c90a9fd2945627118) |
| `xchain-wormholescan` | DETERMINISTIC | 4503 | [yaml](https://paste.rs/IzaXC) | `0x2dfb8b074eaf1667…` |

### `CRYPTO_PRICE` — 12 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `cp-coinlore` | DETERMINISTIC | 4653 | [yaml](https://paste.rs/wfS5j) | [tx](https://sepolia.basescan.org/tx/0xe3b4af309bac22f9b5dbd3c01b3e9ed3475e28b174a8e584c6d0f7d1cbbd8f97) |
| `cp-coinpaprika` | DETERMINISTIC | 4654 | [yaml](https://paste.rs/XUnUF) | [tx](https://sepolia.basescan.org/tx/0x962261f64a8328878984b60eb8cb07e32fdad4fae315da39e1d28d54ccc10ea9) |
| `crypto-binance` | DETERMINISTIC | 2866 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/crypto-binance.yaml) | [tx](https://sepolia.basescan.org/tx/0x3f3aa64ccbba7409771162be3669afb298c38a402c91c6e2fba02c8d0c25af39) |
| `crypto-bitfinex` | DETERMINISTIC | 2956 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/crypto-bitfinex.yaml) | [tx](https://sepolia.basescan.org/tx/0x15649870fbfd38abf70cfc0a9de37ad31ac137b855466219b55c7292323d519e) |
| `crypto-bitstamp` | DETERMINISTIC | 2867 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/crypto-bitstamp.yaml) | [tx](https://sepolia.basescan.org/tx/0x73f228cb68b486460b03527044806ae8161e2732df8b22e0327c7bb73226bd88) |
| `crypto-bybit` | DETERMINISTIC | 2957 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/crypto-bybit.yaml) | [tx](https://sepolia.basescan.org/tx/0x1a4cde6faa3b0c2a57bbba4bd4df7f76436d1a04b08c83bb87bce5b5c8a53e8e) |
| `crypto-coinbase` | DETERMINISTIC | 2864 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/crypto-coinbase.yaml) | [tx](https://sepolia.basescan.org/tx/0x5f6dc267d015627e41bf94f3464ba594a5db743fec97cd03a084c3d8abd3a7e3) |
| `crypto-gate` | DETERMINISTIC | 2955 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/crypto-gate.yaml) | [tx](https://sepolia.basescan.org/tx/0x09a2d3ed8a94965b9aee6bafa1cb9fb68b7f0640251c3acda5ccd1cc4826db28) |
| `crypto-gemini` | DETERMINISTIC | 2868 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/crypto-gemini.yaml) | [tx](https://sepolia.basescan.org/tx/0x60fa9fb0b4e10f4ff73669c8e82613342fbf42ecc53433ac368503956f8514c7) |
| `crypto-htx` | DETERMINISTIC | 2953 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/crypto-htx.yaml) | [tx](https://sepolia.basescan.org/tx/0xbc9ac3d896fba5fefa71ac6fcca64af4459f5da6f09d317d1db5e7ddbe6df6a9) |
| `crypto-kraken` | DETERMINISTIC | 2865 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/crypto-kraken.yaml) | [tx](https://sepolia.basescan.org/tx/0x764e35fc969b195221286ff6504a4f870ec7840d09cc63441b5f3759a05a1a15) |
| `crypto-mexc` | DETERMINISTIC | 2954 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/crypto-mexc.yaml) | [tx](https://sepolia.basescan.org/tx/0x9863d8e82043df529f2b03cc1c6a2a3fa26e53ead825cbe5476c230466de62aa) |

### `CRYPTO_TRANSFER_VERIFY` — 7 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `ctx-tx-receipt` | DETERMINISTIC | 2869 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/ctx-tx-receipt.yaml) | [tx](https://sepolia.basescan.org/tx/0x8ebe03adee90e0492152347a05211c5cdbb084bf02a9f645f810bdbf9a0193f8) |
| `xfer-blockchain-info` | DETERMINISTIC | 4655 | [yaml](https://paste.rs/SGRiH) | [tx](https://sepolia.basescan.org/tx/0x3727a17c07a8d31ae90b53ed23c754e6dd6ab280929cd5ebbf1745a87a8a975a) |
| `xfer-blockcypher` | DETERMINISTIC | 4633 | [yaml](https://paste.rs/5b3aq) | [tx](https://sepolia.basescan.org/tx/0xb0bb71457201b5b8e18d112ea18afb87fb3da64b315b789db38082546f6bcf41) |
| `xfer-blockstream` | DETERMINISTIC | 4634 | [yaml](https://paste.rs/SPaCO) | [tx](https://sepolia.basescan.org/tx/0x0044ff284862e608dd3c8c9ef19df54e88b36effc456eb41f327d53cea92e218) |
| `xfer-haskoin` | DETERMINISTIC | 4601 | [yaml](https://paste.rs/vLHVK) | [tx](https://sepolia.basescan.org/tx/0x1bf6ebc1ca5e9ec6715fa0ceab4befc0eee8f07ccb6e79a138454f36009a8cd8) |
| `xfer-publicnode-rpc` | DETERMINISTIC | 4603 | [yaml](https://paste.rs/vq8jX) | [tx](https://sepolia.basescan.org/tx/0xba629fd8e366de2c2341a2655c992f0df1e873aec6cba3402b7aced4a2028b09) |
| `xfer-trezor-blockbook` | DETERMINISTIC | 4603 | [yaml](https://paste.rs/XOild) | [tx](https://sepolia.basescan.org/tx/0xe92b09e5b151fa2115e84ddd2a2c343d6c1969f849965897595931f8e72bae40) |

### `CRYPTO_YIELD_RATE` — 7 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `yld-aave` | DETERMINISTIC | 4361 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/yld-aave.yaml) | [tx](https://sepolia.basescan.org/tx/0xc6975f53f7d72b76adfac6f2ced157abedb47c82495a12b316e01f31b4a0d1a4) |
| `yld-compound` | DETERMINISTIC | 4375 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/yld-compound.yaml) | [tx](https://sepolia.basescan.org/tx/0x8176a256e739460abcae0eb591a24205d4a1d83d41898f5f9784a233df6df260) |
| `yld-defillama` | DETERMINISTIC | 4357 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/yld-defillama.yaml) | [tx](https://sepolia.basescan.org/tx/0xc6ae1e17b3fd2665686c55eb2341667a6ee9d99fa3abc15aa9d21cf6e881311f) |
| `yld-frax` | DETERMINISTIC | 4359 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/yld-frax.yaml) | [tx](https://sepolia.basescan.org/tx/0xa9b4a313b9dc8b24fdbd84885e45046393fe185958db8bffe90b1000be44ee97) |
| `yld-lido` | DETERMINISTIC | 4356 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/yld-lido.yaml) | [tx](https://sepolia.basescan.org/tx/0xf8e1a2591d97bbc9b5e9ff7bf91e996c03094fbbae9b155d43a4e2c16d0275f1) |
| `yld-rocketpool` | DETERMINISTIC | 4358 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/yld-rocketpool.yaml) | [tx](https://sepolia.basescan.org/tx/0xa5b8348960685d04d1578ee8c941ebd148cb2ed109af908ca05d25eb9955926a) |
| `yld-stader` | DETERMINISTIC | 4360 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/yld-stader.yaml) | [tx](https://sepolia.basescan.org/tx/0x972679e9c9d698472edc181ccc8a627dd0080b6e598471b3b0789509fb8450f6) |

### `DNS_RECORD_LOOKUP` — 7 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `dns-adguard` | DETERMINISTIC | 2892 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/dns-adguard.yaml) | [tx](https://sepolia.basescan.org/tx/0x07c316a7dbec667f4ee67a70737759f6f7c6698867f2a7fc5668cbd4a07328bf) |
| `dns-alidns` | DETERMINISTIC | 2962 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/dns-alidns.yaml) | [tx](https://sepolia.basescan.org/tx/0xed070440da22fd34f7c20dcc6e2f77ec11fbfbe1fc036375de546236874857d0) |
| `dns-cloudflare` | DETERMINISTIC | 2890 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/dns-cloudflare.yaml) | [tx](https://sepolia.basescan.org/tx/0xd72698a7e74130c07186b58e28c156d4470e49b4942af24a62a935bb1ac0d6da) |
| `dns-dnssb` | DETERMINISTIC | 2894 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/dns-dnssb.yaml) | [tx](https://sepolia.basescan.org/tx/0xe4b7235ad25150e2837e2a34d6d318032701b506fc608eea3958eed2460e57d4) |
| `dns-google` | DETERMINISTIC | 2891 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/dns-google.yaml) | [tx](https://sepolia.basescan.org/tx/0x882c0a95c7ad936fd49e26baf7d20f43aaea767bcc3797fd62e22c4c452c4152) |
| `dns-nextdns` | DETERMINISTIC | 2893 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/dns-nextdns.yaml) | [tx](https://sepolia.basescan.org/tx/0xe9241007a51b5bb75a9734d758a4bd0def4a957d7a372109a4f128bb7962cd81) |
| `dns-rethink` | DETERMINISTIC | 2895 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/dns-rethink.yaml) | [tx](https://sepolia.basescan.org/tx/0xc90c43778b1955cb2c587b3aef5287ed97d6785739857a896e42c529ca4cb736) |

### `EMAIL_SECURITY` — 5 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `email-cf-gmail-mx` | HYBRID | 1653 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/email-cf-gmail-mx.yaml) | [tx](https://sepolia.basescan.org/tx/0x1870cf3810aa207033462fc13884892ef3e864e59a40dfa4f7fec21756023411) |
| `email-dns-dmarc-gmail` | HYBRID | 1655 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/email-dns-dmarc-gmail.yaml) | [tx](https://sepolia.basescan.org/tx/0x15bdd5d7eadcc1531407a3cbfa7f4edcec8e0aad732e624238611a6be1d9aabe) |
| `email-doh-adguard` | HYBRID | 4604 | [yaml](https://paste.rs/iubQr) | [tx](https://sepolia.basescan.org/tx/0x0bf67d18715a65f00b5b5d583b5b9f48afcda438b046aa8648b16c5179579080) |
| `email-doh-alidns` | HYBRID | 4605 | [yaml](https://paste.rs/4lNZ5) | [tx](https://sepolia.basescan.org/tx/0x0b5f6e336ab25ee1728f6ddb01aba299b23ec2eb672e5b51ecbfe23bb3443db2) |
| `email-doh-dnspod` | HYBRID | 4635 | [yaml](https://paste.rs/vgxu3) | [tx](https://sepolia.basescan.org/tx/0xe1a4be094153f22d503e02ccbb034616a93dc19d4ce106ecc3d5cc3decc204b8) |

### `EVENT_OUTCOME_RESOLUTION` — 15 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `event-espn-mlb-scoreboard` | HYBRID | 4504 | [yaml](https://paste.rs/Y8Er8) | `0xe8a32b92318d421b…` |
| `event-espn-nba-scoreboard` | HYBRID | 4506 | [yaml](https://paste.rs/wm2tn) | `0xb4e972d9cd1a60e3…` |
| `event-espn-nfl-scoreboard` | HYBRID | 4507 | [yaml](https://paste.rs/q29Om) | `0xcc54e12c3ece4bb4…` |
| `event-jolpica-f1` | HYBRID | 4507 | [yaml](https://paste.rs/4Ta4s) | `0xacee923db16a3be9…` |
| `event-kalshi-result` | HYBRID | 4364 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/event-kalshi-result.yaml) | [tx](https://sepolia.basescan.org/tx/0xee49b83fb0c4a5ac717adaa99457e8c9934c9ca30ce42c02538b65038a32b8e5) |
| `event-manifold` | HYBRID | 4636 | [yaml](https://paste.rs/zwtJA) | [tx](https://sepolia.basescan.org/tx/0xc4ec6e714a5265e0968e1999ee111ffd6573ebad79c3fa2d8531b7bbbb2c74db) |
| `event-manifold-resolution` | HYBRID | 2851 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/event-manifold-resolution.yaml) | [tx](https://sepolia.basescan.org/tx/0xb8dc4c7695b14cf457cab961a5f4d020876f5240ff9c2420f40f98f7bc8f35d5) |
| `event-mlb-statsapi` | HYBRID | 4508 | [yaml](https://paste.rs/TccvF) | `0x7206a5d881704525…` |
| `event-nhl-schedule` | HYBRID | 4510 | [yaml](https://paste.rs/6LHKE) | `0x62ec43f762112e19…` |
| `event-openligadb-bl1` | HYBRID | 4511 | [yaml](https://paste.rs/hqhLc) | `0x23474bbc4b3f0caf…` |
| `event-poly-clob-winner` | HYBRID | 2849 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/event-poly-clob-winner.yaml) | [tx](https://sepolia.basescan.org/tx/0x6d98ba12ee445967656c4c9cfd794d1543d57e572c9cb1f592d44ce0efdb3ec6) |
| `event-poly-closed` | HYBRID | 4512 | [yaml](https://paste.rs/SlWwD) | `0x59476f773b96ac55…` |
| `event-poly-markets-closed` | HYBRID | 4512 | [yaml](https://paste.rs/ath7A) | `0x0b5d40b996a846f5…` |
| `event-thesportsdb-last` | HYBRID | 4514 | [yaml](https://paste.rs/BvKvP) | `0x070ce1015e95069d…` |
| `event-thesportsdb-lookup` | HYBRID | 4514 | [yaml](https://paste.rs/WAyQW) | `0x974647a7f10af4dc…` |

### `FX_NOW` — 13 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `fx-awesomeapi` | DETERMINISTIC | 1396 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/fx-awesomeapi.yaml) | [tx](https://sepolia.basescan.org/tx/0x6033732006a80bcec8cbb85b363a16f13d419337ee153cce51675d4d0ae8868d) |
| `fx-boc` | DETERMINISTIC | 1397 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/fx-boc.yaml) | [tx](https://sepolia.basescan.org/tx/0x47d06efca48bbf649175f697ecf518219aa22394d09f98f2b8ef5c21595e0dd3) |
| `fx-cbr` | DETERMINISTIC | 1398 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/fx-cbr.yaml) | [tx](https://sepolia.basescan.org/tx/0x4aabc2910135b4b83864c08f92f0051182779739ffbb1658ac184ededb04b6a2) |
| `fx-coinbase` | DETERMINISTIC | 1399 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/fx-coinbase.yaml) | [tx](https://sepolia.basescan.org/tx/0x07313a00da1d8207f17896d01068b21a9e421bccfa2ebeca5105c1daac11ddc5) |
| `fx-er-api` | DETERMINISTIC | 1400 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/fx-er-api.yaml) | [tx](https://sepolia.basescan.org/tx/0x5b16c009f55d60eef3f4a8b5e80cd96b3a00775ddc504934d993e4d236ce898c) |
| `fx-erapi-v4` | DETERMINISTIC | 1401 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/fx-erapi-v4.yaml) | [tx](https://sepolia.basescan.org/tx/0x0a288eec7119c47fc04e1cd9dd11862523279ae7de42d6f22cd7dac136fdc875) |
| `fx-fawaz` | DETERMINISTIC | 1402 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/fx-fawaz.yaml) | [tx](https://sepolia.basescan.org/tx/0xf016c54c47f0bfe7c8f75b884582fd736d25ea8513f3a6a9116626b2c567b9d0) |
| `fx-frankfurter` | DETERMINISTIC | 1403 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/fx-frankfurter.yaml) | [tx](https://sepolia.basescan.org/tx/0x8641a23c1648e7851787758227d5896947f750d94de9e53a6bb4e409615086bd) |
| `fx-hexarate` | DETERMINISTIC | 4638 | [yaml](https://paste.rs/imVjp) | [tx](https://sepolia.basescan.org/tx/0x89bf92f15da5d3ce5924b700999fe031e91734fbca69e0b41a9f5f17c1e57111) |
| `fx-hnb` | DETERMINISTIC | 1406 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/fx-hnb.yaml) | — |
| `fx-riksbank` | DETERMINISTIC | 1404 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/fx-riksbank.yaml) | [tx](https://sepolia.basescan.org/tx/0x6b52a584ff317ddddf1a5519defbdfd834e86432b21cf71bc2d5ebb834351fd8) |
| `fx-vatcomply` | DETERMINISTIC | 1405 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/fx-vatcomply.yaml) | [tx](https://sepolia.basescan.org/tx/0x5ef901640d2e8a6734ff9f791b8e54f588736af0637b63e3ba2e69498f6b6cad) |
| `fx-yahoo` | DETERMINISTIC | 4638 | [yaml](https://paste.rs/SplQn) | [tx](https://sepolia.basescan.org/tx/0xa64560d49a447fc2f2a8e9932167a3be3d040e88c57bf27116c0a65369cfb9d4) |

### `GAS_PRICE` — 5 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `gas-1rpc` | DETERMINISTIC | 4639 | [yaml](https://paste.rs/RAPwu) | [tx](https://sepolia.basescan.org/tx/0xd719753cc5312c50d83dd30f7f6eb3dc48d8f44744fe28e61170725f86c94aa7) |
| `gas-drpc-rpc` | DETERMINISTIC | 4657 | [yaml](https://paste.rs/M8OTk) | [tx](https://sepolia.basescan.org/tx/0x2c8bfb17d5356a2145f8847935933f9dc4c1f2a27d77f55d9715f459e21e05cc) |
| `gas-metamask` | DETERMINISTIC | 2913 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/gas-metamask.yaml) | [tx](https://sepolia.basescan.org/tx/0x51329ddb8208e7df47693d182bf9f2d403fa5e3b40dbaceb8ab0172c70419a50) |
| `gas-polygon` | DETERMINISTIC | 2914 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/gas-polygon.yaml) | [tx](https://sepolia.basescan.org/tx/0xcea7206e801c4738c20b12e6440d697aff7273a921c1d6cc3b728bbb34d7beda) |
| `gas-publicnode-rpc` | DETERMINISTIC | 4658 | [yaml](https://paste.rs/YXsXR) | [tx](https://sepolia.basescan.org/tx/0x2e3328e2bafff4ac72503601e24fd312765fcea7a35932d6536eb71be4fe36e2) |

### `GRAMMAR_SPELL_CHECK` — 3 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `grammar-languagetool` | DETERMINISTIC | 4606 | [yaml](https://paste.rs/lZ1Th) | [tx](https://sepolia.basescan.org/tx/0x2192a64b934901342fea572a796e2c06a62957bd3f36d54ea1ddb6ffaa5085f8) |
| `grm-languagetool` | DETERMINISTIC | 2942 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/grm-languagetool.yaml) | [tx](https://sepolia.basescan.org/tx/0x51278d5333849fb27b042d731eb422285500033e7e11635acf48b68ca15ce6d2) |
| `grm-yandex` | DETERMINISTIC | 2943 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/grm-yandex.yaml) | [tx](https://sepolia.basescan.org/tx/0x77707e176452121eff34c0e252711609dc1e0a6bac4ad86b95f84852d22b815f) |

### `GRID_POWER_PRICE` — 4 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `grid-awattar-de` | DETERMINISTIC | 4607 | [yaml](https://paste.rs/FnIKS) | [tx](https://sepolia.basescan.org/tx/0xe44603661dd7ab45207eae396a1e8fa87f429cee234edcda9b5a0d1851e2b4c6) |
| `grid-caiso-np15-dam` | DETERMINISTIC | 2758 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/grid-caiso-np15-dam.yaml) | [tx](https://sepolia.basescan.org/tx/0xcc739dc2237db369028563c9b126c70690f729444027e7b81cef307046424aca) |
| `grid-elering` | DETERMINISTIC | 4608 | [yaml](https://paste.rs/OnBDU) | [tx](https://sepolia.basescan.org/tx/0x61411fb1b6cb6c23e4af605137144212d2f2681b5ac06ddd894a32acbe201dc5) |
| `grid-spot-hinta` | DETERMINISTIC | 4609 | [yaml](https://paste.rs/Mz4a3) | [tx](https://sepolia.basescan.org/tx/0xfc8ffc2ad712a59901b6764a8f21c6229cda879c1de7fdd94b9af92b3e6b5a40) |

### `LANGUAGE_TRANSLATION` — 5 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `tr-apertium` | NON-DETERMINISTIC | 4640 | [yaml](https://paste.rs/yPmRF) | [tx](https://sepolia.basescan.org/tx/0x1c487c111cd24d6ec1c841169e6c90fdbbfb581f92a552d0456527f9b23cb63c) |
| `tr-google` | NON-DETERMINISTIC | 4384 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/tr-google.yaml) | [tx](https://sepolia.basescan.org/tx/0x0651497d2c88379555dfff2deec7362ce2bc4172b170a08f0a525d6a8737f58e) |
| `tr-hf-opus` | NON-DETERMINISTIC | 4388 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/tr-hf-opus.yaml) | [tx](https://sepolia.basescan.org/tx/0xc1497a8d06ecb70a311ea05ab2ef9d00a26e52787ed8cfa34c5b2a2b42f4161b) |
| `tr-mymemory` | NON-DETERMINISTIC | 4383 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/tr-mymemory.yaml) | [tx](https://sepolia.basescan.org/tx/0xac6881986e39f80993b077b56e608b8a8dd093f6550990a8a82dc8a3a4f9a09d) |
| `tr-pollinations` | NON-DETERMINISTIC | 4389 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/tr-pollinations.yaml) | [tx](https://sepolia.basescan.org/tx/0xfd08779de90e8b9527f6ae7c232af6375c0566947cdbdb0e4cff0de8f81b149f) |

### `LIQUIDITY_DEPTH_VERIFY` — 21 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `liq-binance-depth` | DETERMINISTIC | 4641 | [yaml](https://paste.rs/NGF8B) | [tx](https://sepolia.basescan.org/tx/0x0d8c5e7d72ce43fcf23f15f2482b0e3c0faf1d01c5804a95606c414f1cfd5b6a) |
| `liq-bitfinex-book` | DETERMINISTIC | 4643 | [yaml](https://paste.rs/kBZwt) | [tx](https://sepolia.basescan.org/tx/0x8da92ab2fa9ceb8671f3c81fd79ca0dcffe5010281eab223aaac9ec6de8a5fcd) |
| `liq-bitget-book` | DETERMINISTIC | 4610 | [yaml](https://paste.rs/JxCN2) | [tx](https://sepolia.basescan.org/tx/0x125f7d836e4a689a5068e6a85867a4c23b86a70c1dcc94bf0ec9a060d101c234) |
| `liq-bitstamp-book` | DETERMINISTIC | 4612 | [yaml](https://paste.rs/vh1zm) | [tx](https://sepolia.basescan.org/tx/0x484367688178775a49dbbf350bdef85e6a86fdc344884cc4c0c04ba0137590cc) |
| `liq-bybit-book` | DETERMINISTIC | 4612 | [yaml](https://paste.rs/AJZsq) | [tx](https://sepolia.basescan.org/tx/0x0b61492728d6971b1547b32ef07142f887d39968756468994dd37257564214b7) |
| `liq-coinbase-book` | DETERMINISTIC | 4658 | [yaml](https://paste.rs/H6XnN) | [tx](https://sepolia.basescan.org/tx/0xd57c74b8e9e913c013b28ade5456d2afd262d15fee9a96fc29a6ab7841c7d1fa) |
| `liq-cryptocom-book` | DETERMINISTIC | 4643 | [yaml](https://paste.rs/lqVzE) | [tx](https://sepolia.basescan.org/tx/0x61271ca8c2c84a048b9a6451a6aa439b9b0cac592885c901bcc71345a51f8619) |
| `liq-dex-pair-cents` | DETERMINISTIC | 2766 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/liq-dex-pair-cents.yaml) | [tx](https://sepolia.basescan.org/tx/0x5f9c6b472e5c7757d6e1bd5e0f68aac12b59fcdd2e94ca3c5d64a08ad45fa741) |
| `liq-dexscreener-pair` | DETERMINISTIC | 4515 | [yaml](https://paste.rs/Z7DXC) | `0xd38940f495286e9e…` |
| `liq-dexscreener-search-btc` | DETERMINISTIC | 4516 | [yaml](https://paste.rs/knzd2) | `0xbfa3f94c72fe8da6…` |
| `liq-dexscreener-token-weth` | DETERMINISTIC | 4518 | [yaml](https://paste.rs/sp5eV) | `0x4ef34266aca3d3f2…` |
| `liq-gate-book` | DETERMINISTIC | 4659 | [yaml](https://paste.rs/2YyaC) | [tx](https://sepolia.basescan.org/tx/0xe41083cee4e46b0f0e6493f07818b25e672befdb1de38f0b48d1ebfd77a7cbcb) |
| `liq-gecko-base-trending` | DETERMINISTIC | 4519 | [yaml](https://paste.rs/ie5EZ) | `0x6c14e5149fab90f7…` |
| `liq-gecko-eth-usdc-pool` | DETERMINISTIC | 4521 | [yaml](https://paste.rs/ylYrP) | [tx](https://sepolia.basescan.org/tx/0xf6d5a0bc1e33e46ec6ff572914d12c9c52c6f70da1ec81015ec5b93f190560bf) |
| `liq-gecko-pool-cents` | DETERMINISTIC | 2765 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/liq-gecko-pool-cents.yaml) | [tx](https://sepolia.basescan.org/tx/0x50a42892b02d970b1abf8da5f03d43bb7cdde9b10c0211b7a9a90845e79dc848) |
| `liq-gecko-search-eth` | DETERMINISTIC | 4521 | [yaml](https://paste.rs/tHC8g) | [tx](https://sepolia.basescan.org/tx/0x889330615bc75dc2c0974ad50879832c64f9a2036c140438caca1ff494d9ab82) |
| `liq-gemini-book` | DETERMINISTIC | 4661 | [yaml](https://paste.rs/YsPaz) | [tx](https://sepolia.basescan.org/tx/0xc688cfd6b1605525796d2d0cfe82de3e42039ceb59279c0cf20b9b07e155b383) |
| `liq-htx-depth` | DETERMINISTIC | 4614 | [yaml](https://paste.rs/IVjQT) | [tx](https://sepolia.basescan.org/tx/0xd1bbaca33a39acb4ebd12f3f209f456fe0e58f155e4123ebaa6ca87636d66c9d) |
| `liq-kraken-depth` | DETERMINISTIC | 4615 | [yaml](https://paste.rs/cZ86W) | [tx](https://sepolia.basescan.org/tx/0x561e1b95ee9cf24485a607898d98c6250dc8aa913d74fa6bfd56654184cc2a34) |
| `liq-kucoin-book` | DETERMINISTIC | 4616 | [yaml](https://paste.rs/x7Xgo) | [tx](https://sepolia.basescan.org/tx/0x69d07155f4ccf431048187685a7361c6bf4a5c38cfe7068e2c63fe4c2bf6837b) |
| `liq-mexc-depth` | DETERMINISTIC | 4645 | [yaml](https://paste.rs/fK7tr) | [tx](https://sepolia.basescan.org/tx/0xbb2a19a21605138144f6d05b74653ffdcef487dd4719876e61228c0289d0ace5) |

### `LIVE_SHELF_PRICE` — 1 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `shelf-open-prices` | DETERMINISTIC | 2759 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/shelf-open-prices.yaml) | [tx](https://sepolia.basescan.org/tx/0xfb8fb91014ae7c354c54b51c31541205a6b1f1ad180dbd99de2b11320e70f478) |

### `LOAN_INTEREST_RATE_QUOTE` — 6 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `lnr-bcb` | DETERMINISTIC | 2924 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/lnr-bcb.yaml) | [tx](https://sepolia.basescan.org/tx/0x79314d71df166519dbf254b51046124c4ef5d04625429d86488085051710ead7) |
| `lnr-boc` | DETERMINISTIC | 2921 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/lnr-boc.yaml) | [tx](https://sepolia.basescan.org/tx/0x0cfdf19b8c343a431a73b7c4377b322a3ff4eac3828850b57c86cb118fbb5034) |
| `lnr-boe` | DETERMINISTIC | 2923 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/lnr-boe.yaml) | [tx](https://sepolia.basescan.org/tx/0xd58ece1197911db8e0972fca088c1869cd026cf873f47d06d04d34d84bc7f8e5) |
| `lnr-ecb` | DETERMINISTIC | 2922 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/lnr-ecb.yaml) | [tx](https://sepolia.basescan.org/tx/0x15207abdff74edf58e859334a49f407c963d24bbb877aefa2a780d1e6f2c3623) |
| `lnr-fred` | DETERMINISTIC | 2920 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/lnr-fred.yaml) | [tx](https://sepolia.basescan.org/tx/0x9fa119b2d0a9582f5f76960d0a5e07b62d97a65ebc423281d67d9b3359734acd) |
| `lnr-freddie` | DETERMINISTIC | 2919 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/lnr-freddie.yaml) | [tx](https://sepolia.basescan.org/tx/0xa1bab7b48408fdfc3c2c0f640dcb1af3008fedfdd414a1a57858dc99e867ddc6) |

### `MACRO_ECONOMIC_INDICATOR` — 3 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `macro-eurostat` | DETERMINISTIC | 4645 | [yaml](https://paste.rs/xBQ5g) | [tx](https://sepolia.basescan.org/tx/0xcedca5e716496f15204b37d5af3535270c633d96d1107f861db27356530d02af) |
| `macro-wb-unemp-proxy` | DETERMINISTIC | 2784 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/macro-wb-unemp-proxy.yaml) | [tx](https://sepolia.basescan.org/tx/0x4b3039e1ee929f04bf6c96a604ea6d0b1c228273ac8fb7235dbf214ff667840f) |
| `macro-wb-unemp-us` | DETERMINISTIC | 2753 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/macro-wb-unemp-us.yaml) | [tx](https://sepolia.basescan.org/tx/0xefee12bf5878f7e2bfdb47fbbb9ccf8d4646fea0a9b6bdc29b9bd0f96a59c77f) |

### `MINING_HASHPRICE_VERIFY` — 1 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `mine-mempool-hashprice` | DETERMINISTIC | 2764 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/mine-mempool-hashprice.yaml) | [tx](https://sepolia.basescan.org/tx/0x89ea155bd4a281b24e7b46b6ec914b25c973ee4633d54e1bfadf7f571e48672c) |

### `ONCHAIN_METRIC_VERIFY` — 14 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `ocm-blockcypher-eth` | DETERMINISTIC | 4523 | [yaml](https://paste.rs/CCJd9) | [tx](https://sepolia.basescan.org/tx/0xd28ec1e70ba65a91213638c9c835f9288956f16d534ac5b998cd92a3943fbe01) |
| `ocm-blockscout-arbitrum` | DETERMINISTIC | 4523 | [yaml](https://paste.rs/frHIp) | [tx](https://sepolia.basescan.org/tx/0x8d11f09b3dd06dd1247704400e9a45c83f68f9f18ffa962e9c4b1fae88a2c074) |
| `ocm-blockscout-base` | DETERMINISTIC | 4524 | [yaml](https://paste.rs/KGWp0) | [tx](https://sepolia.basescan.org/tx/0x7ee631fde8bbd519ce38fa5c4bfb739d31b7ec7e582c7aa80a7e04106059c413) |
| `ocm-blockscout-eth` | DETERMINISTIC | 4525 | [yaml](https://paste.rs/U0cuC) | [tx](https://sepolia.basescan.org/tx/0x1da5a701fbff030e11970814709b0cd404c0f92c13c1a6f4e9c367323a774253) |
| `ocm-blockscout-gnosis` | DETERMINISTIC | 4527 | [yaml](https://paste.rs/SCxOA) | [tx](https://sepolia.basescan.org/tx/0xb8540172e299dd2ea66865bb8d7a56af01488f039da8f02b1406449f1f6bee4c) |
| `ocm-blockscout-optimism` | DETERMINISTIC | 4527 | [yaml](https://paste.rs/ydwKi) | [tx](https://sepolia.basescan.org/tx/0x90a10eab9b643ca5a44b574220ed7e9b79ed734f16f8ce4db7bf3ae07e291a1e) |
| `ocm-blockscout-polygon` | DETERMINISTIC | 4528 | [yaml](https://paste.rs/fBnf3) | [tx](https://sepolia.basescan.org/tx/0xa63738762c73ce869dcb673c311fff436abc5e2259481aca4b33b9047e17a979) |
| `ocm-blockscout-scroll` | DETERMINISTIC | 4529 | [yaml](https://paste.rs/Me0xD) | [tx](https://sepolia.basescan.org/tx/0x8e8966474349ccef3d11e55b58e32fac4f45ed61adcab1c0bd54387215398bbd) |
| `ocm-blockstream-btc` | DETERMINISTIC | 4531 | [yaml](https://paste.rs/AKV8V) | [tx](https://sepolia.basescan.org/tx/0x3a44c6434437b5d2399c11df3a7f43dbed417fdd6875874dedea766ef348e17a) |
| `ocm-drpc-rpc` | DETERMINISTIC | 4647 | [yaml](https://paste.rs/PiJVl) | [tx](https://sepolia.basescan.org/tx/0x6ecd410def8b0b3173824801669167cceb4aa916178c27563940f3955f5b0596) |
| `ocm-eth-balance` | DETERMINISTIC | 2761 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/ocm-eth-balance.yaml) | [tx](https://sepolia.basescan.org/tx/0x687979e506d80f6a12a9b5fb90ef80623e3fa1ffa74f862f2523928cecbfae52) |
| `ocm-ethplorer-addr` | DETERMINISTIC | 4531 | [yaml](https://paste.rs/coGsD) | [tx](https://sepolia.basescan.org/tx/0x6260231b6d7ad6a36a003ec9095e12e82e13fadb706e4bb2b6137746616abad5) |
| `ocm-publicnode-rpc` | DETERMINISTIC | 4616 | [yaml](https://paste.rs/RyeX6) | [tx](https://sepolia.basescan.org/tx/0x45e06991967e9c8653fd657b09ccf9a7dd07f4c0d6aa1e1cf23ef00b8000c9fa) |
| `ocm-trezor-blockbook` | DETERMINISTIC | 4617 | [yaml](https://paste.rs/wVDcZ) | [tx](https://sepolia.basescan.org/tx/0x7686d42a62864c0569a9eacb57d88ec4592ace4d67d3024c6f0158ea2ca9c5be) |

### `OPTIMAL_EXECUTION_ROUTE` — 14 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `route-bebop-quote` | HYBRID | 4533 | [yaml](https://paste.rs/lHAkY) | [tx](https://sepolia.basescan.org/tx/0x748acd99292e232598e40bc8f1cff0a1e9ea90071d0ebc808b996b2582bc0690) |
| `route-cowswap-buyamount` | HYBRID | 2854 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/route-cowswap-buyamount.yaml) | [tx](https://sepolia.basescan.org/tx/0x9dc7347d624f6e265db8f22e535e1387275679d073432be320003b4b232c81b4) |
| `route-jupiter` | HYBRID | 4647 | [yaml](https://paste.rs/QuRmy) | [tx](https://sepolia.basescan.org/tx/0x50dc151e039174205cbd4b7387eb7b3090e06baddc4de7edd527d5d6e68c85ec) |
| `route-kyber-amountout` | HYBRID | 2853 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/route-kyber-amountout.yaml) | [tx](https://sepolia.basescan.org/tx/0xc4afce20380412815cc7d193e7c68d5929a77bc78e3167441952b15ab2273aed) |
| `route-kyber-bsc` | HYBRID | 4533 | [yaml](https://paste.rs/EraXU) | [tx](https://sepolia.basescan.org/tx/0x170df057626acfa3ced88a9f77018b1276c58b6b6d7573314b4a59ec34e493f1) |
| `route-kyber-route` | HYBRID | 4534 | [yaml](https://paste.rs/QhhBW) | [tx](https://sepolia.basescan.org/tx/0x07217b39e3c01a0c119865c4de052bc4071b74b4ccfc09becd80ee28c8a0b228) |
| `route-lifi-arb-usdc` | HYBRID | 4535 | [yaml](https://paste.rs/5WOqO) | [tx](https://sepolia.basescan.org/tx/0x64e28f71209dd5670b02dba0f0be52dd10cd7216cc900be36f73cf16688765fd) |
| `route-lifi-effprice` | HYBRID | 2855 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/route-lifi-effprice.yaml) | [tx](https://sepolia.basescan.org/tx/0x3afe3d65fb77ee3e0c3201c2d735965ed0c460ad7b3133ece55855e9bb230c69) |
| `route-lifi-quote` | HYBRID | 4536 | [yaml](https://paste.rs/mV8B5) | [tx](https://sepolia.basescan.org/tx/0x30f489591d8ff44918569635713a68c83d05e2e95a5c5498caadd0d7876e33c7) |
| `route-paraswap` | HYBRID | 4648 | [yaml](https://paste.rs/mpnm8) | [tx](https://sepolia.basescan.org/tx/0x00b7880d7c4513bd9584de87e55723bb8db965e23e75fc11eff2cb45d6e79f23) |
| `route-paraswap-destamount` | HYBRID | 2852 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/route-paraswap-destamount.yaml) | [tx](https://sepolia.basescan.org/tx/0x2e653ddfb98fa405f7a896889329e345ed20b3e6976b6bca80869d30f8e17377) |
| `route-paraswap-price` | HYBRID | 4538 | [yaml](https://paste.rs/hZSPb) | [tx](https://sepolia.basescan.org/tx/0x930930c7a37502a50a853495073ecf277076b3d34b1fc08839d4076b3a19e803) |
| `route-paraswap-usdt` | HYBRID | 4539 | [yaml](https://paste.rs/QaZG6) | [tx](https://sepolia.basescan.org/tx/0xb92ef588789a5f3437a93bea6e58c8b42670078944064684cf701811549061ee) |
| `route-sushi-quote` | HYBRID | 4539 | [yaml](https://paste.rs/bYrz0) | [tx](https://sepolia.basescan.org/tx/0x65e2b7030b0e8db4ce079b644541160fc879b23192395f471cb813ff0ca1ce60) |

### `PAYMENT_METHOD_VERIFY` — 6 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `pay-bin-scheme` | DETERMINISTIC | 2857 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/pay-bin-scheme.yaml) | [tx](https://sepolia.basescan.org/tx/0x769af23856ef471b6a559f6c9f29db110a582e7b8303c217fc0a508f69600b7d) |
| `pay-binlist` | DETERMINISTIC | 4651 | [yaml](https://paste.rs/illVy) | [tx](https://sepolia.basescan.org/tx/0x32e3bfc03a0e6c1e5c1e5b6fe2e5f311257fbcf426b8f63fad195f8954e5fccb) |
| `pay-binlist-io` | DETERMINISTIC | 4649 | [yaml](https://paste.rs/TS0SL) | [tx](https://sepolia.basescan.org/tx/0xdc49f2979f65142a79004f02a1fa71bf54ff72d08c5c55c5ec4c765e27308ce4) |
| `pay-handyapi-bin` | DETERMINISTIC | 4618 | [yaml](https://paste.rs/pZimG) | [tx](https://sepolia.basescan.org/tx/0x97edb851390a0e9dc5a361c8ab4d72b0156c74c2aab89d49acb281dabcdd2bfb) |
| `pay-handyapi-scheme` | DETERMINISTIC | 2858 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/pay-handyapi-scheme.yaml) | [tx](https://sepolia.basescan.org/tx/0x715884570ce051531868f99ffd490040ad495aaf22eb0148547fd02345d47356) |
| `pay-openiban` | DETERMINISTIC | 4619 | [yaml](https://paste.rs/1N4hW) | [tx](https://sepolia.basescan.org/tx/0xbeaececcef412e2504e0db5d71f50246877b4bb7df4614c8f4a95e7de774149c) |

### `PORT_SCAN_AUDIT` — 2 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `prt-checkhost` | DETERMINISTIC | 2899 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/prt-checkhost.yaml) | [tx](https://sepolia.basescan.org/tx/0x38ccdc0d22bb26f0beb4401c445b39b7b908c0207bf5feb7758c1ae5142b9f6f) |
| `prt-internetdb` | DETERMINISTIC | 2898 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/prt-internetdb.yaml) | [tx](https://sepolia.basescan.org/tx/0x0ce871775bde6b77fbdba86140187ffe865f659241070ceb9f378259c3c64ddf) |

### `REGRESSION_VERIFY` — 1 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `rgr-paiza` | DETERMINISTIC | 2944 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/rgr-paiza.yaml) | [tx](https://sepolia.basescan.org/tx/0xa78a2faeb8931db33225266a3639cc35cd3fdbb40799ab629b02bcbac0cb1e8e) |

### `REGULATORY_FILING_MONITOR` — 2 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `filing-sec-submissions` | DETERMINISTIC | 4621 | [yaml](https://paste.rs/3nyab) | [tx](https://sepolia.basescan.org/tx/0xd90ab349d4d5cc29cc1659e0c1e01e713f47de517dc756813abf171ac7ad4ef4) |
| `reg-sec-edgar` | DETERMINISTIC | 2863 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/reg-sec-edgar.yaml) | [tx](https://sepolia.basescan.org/tx/0x828d2bae404506b7a14eea218c38ccc3724cc52a1faeb6851bfa3ee60bff73af) |

### `ROUTE_ETA` — 4 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `eta-osrm-fossgis` | DETERMINISTIC | 4622 | [yaml](https://paste.rs/QVaFr) | [tx](https://sepolia.basescan.org/tx/0xbca45fd061780193fe2764cbf3171eaf72a04b80e8e5c2ff3ea5fe2dcf236015) |
| `route-osrm-berlin` | DETERMINISTIC | 1663 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/route-osrm-berlin.yaml) | [tx](https://sepolia.basescan.org/tx/0xf18aca7a53143b0e48689429fc2895e262aac86aa47ac3b1ff246782fe458675) |
| `route-osrm-table` | DETERMINISTIC | 1668 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/route-osrm-table.yaml) | [tx](https://sepolia.basescan.org/tx/0xf8d571e8b29b26afa73bae04a60b23dd39f9d026abd49617216eb2a8f243b59c) |
| `route-valhalla` | DETERMINISTIC | 2965 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/route-valhalla.yaml) | [tx](https://sepolia.basescan.org/tx/0x06d029ec48ef4ef461c4bce0c4bae8a1d26edc7b7ae2be2a923820016eacbc1e) |

### `SANCTIONS_SCREENING_MATCH` — 2 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `san-ofac-entity` | HYBRID | 2859 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/san-ofac-entity.yaml) | [tx](https://sepolia.basescan.org/tx/0x53e34791109a284f453d7d98769095229820a02358aa5893ab54cdb2ed2b88ce) |
| `san-un-list` | HYBRID | 2860 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/san-un-list.yaml) | [tx](https://sepolia.basescan.org/tx/0x3994be53f8e6a44ea92c8b8f5506115eb18324eafb07f3d6b3b9b77b54b8bdbd) |

### `SECURITY_REVIEW` — 8 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `secrev-depsdev` | HYBRID | 4544 | [yaml](https://paste.rs/gZeot) | [tx](https://sepolia.basescan.org/tx/0x7254917e520eeeac1a592ef3fc06ccd907078686fa9789e291e778b71a0e3a4c) |
| `secrev-depsdev-cargo` | HYBRID | 4540 | [yaml](https://paste.rs/uFtxl) | [tx](https://sepolia.basescan.org/tx/0x84b35f273a5dcff58a680a99e046688763e3fbca9aec75e9395d3b8f44e2b59a) |
| `secrev-depsdev-maven` | HYBRID | 4542 | [yaml](https://paste.rs/06O2H) | [tx](https://sepolia.basescan.org/tx/0x311817e8ec7507dddf07f52579096d7622d83955ef3a27deeaee436c24872cd1) |
| `secrev-depsdev-pypi` | HYBRID | 4542 | [yaml](https://paste.rs/aI6k2) | [tx](https://sepolia.basescan.org/tx/0xd2e1ac8dac8768655b1f6a5cde4154f1fdd2fc076a4e2f4ba110a8958eef9d7c) |
| `secrev-osv-cve` | HYBRID | 4544 | [yaml](https://paste.rs/2GKmd) | [tx](https://sepolia.basescan.org/tx/0x64e457c13e6391520398efdeafbdd8998c55e5fdc65acf7d775a222e76ee4de0) |
| `secrev-osv-ghsa` | HYBRID | 4545 | [yaml](https://paste.rs/dHPiI) | [tx](https://sepolia.basescan.org/tx/0xe08be66bfbc106d53815e2492efb157c3cfaf261451aec339531a24a6a908e2a) |
| `secrev-pypi` | HYBRID | 4548 | [yaml](https://paste.rs/h87an) | [tx](https://sepolia.basescan.org/tx/0xadb0e6561ceb2397d10495a24034ad22215a6584816cf1884cf4245ae085f771) |
| `secrev-pypi-django` | HYBRID | 4546 | [yaml](https://paste.rs/mpVQy) | [tx](https://sepolia.basescan.org/tx/0xfbbbf7eb7eda47a8b77c1886bd896672dd5fe216396ab5325c8dbfab03d091e6) |

### `SEMANTIC_SIMILARITY` — 1 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `sem-hf-minilm` | DETERMINISTIC | 2968 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/sem-hf-minilm.yaml) | [tx](https://sepolia.basescan.org/tx/0xae2a77702e07f3f3d05b6157bcb1a22612f44a0d59dc7d5af16d4a6bb9d5dd7b) |

### `SENSOR_TELEMETRY_VERIFY` — 5 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `sen-coops` | DETERMINISTIC | 2933 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/sen-coops.yaml) | [tx](https://sepolia.basescan.org/tx/0x2f6f354422eb11163dc9302e2b16e82851f1958b633ca1c82e53e220b12521ce) |
| `sen-ndbc` | DETERMINISTIC | 2935 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/sen-ndbc.yaml) | [tx](https://sepolia.basescan.org/tx/0x7457861671a456301ef410f513691844c4fa23437875dc9ebc780fecf3f1fd09) |
| `sen-sensorcommunity` | DETERMINISTIC | 2931 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/sen-sensorcommunity.yaml) | [tx](https://sepolia.basescan.org/tx/0x291d3a8b267faa06741e38bc6b02f66b1395d10105fa749dc635d459de3279e8) |
| `sen-thingspeak` | DETERMINISTIC | 2934 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/sen-thingspeak.yaml) | [tx](https://sepolia.basescan.org/tx/0xb9aef3ee059210ff7799d16457877bb893337052f06d7806fcef297b1ff51aef) |
| `sen-usgs` | DETERMINISTIC | 2932 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/sen-usgs.yaml) | [tx](https://sepolia.basescan.org/tx/0xb589f36ae1d648de2dec86f79b35d3197e92caac6ccf9a1a5cad74ab682bfb27) |

### `SENTIMENT_ANALYSIS` — 2 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `snt-textprocessing` | HYBRID | 2947 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/snt-textprocessing.yaml) | [tx](https://sepolia.basescan.org/tx/0x96f930d4409344939244fdf38343b028bd4bd2d1c173220fbc29ef06738796a4) |
| `snt-twinword` | HYBRID | 2948 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/snt-twinword.yaml) | [tx](https://sepolia.basescan.org/tx/0xac52115394b0f6f61748e666712aef015b7543eeb7df5f7e7fe6e1c3d4843277) |

### `SERVER_UPTIME_MONITOR` — 2 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `upt-checkhost` | DETERMINISTIC | 2926 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/upt-checkhost.yaml) | [tx](https://sepolia.basescan.org/tx/0x8d723a54c26c4c2a9f940e2733798306f44bc89ec26939c53ffb7575d4a98e82) |
| `upt-hackertarget` | DETERMINISTIC | 2928 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/upt-hackertarget.yaml) | [tx](https://sepolia.basescan.org/tx/0xbf723e59818c60aaf888f4dddccec3fecc660199de7387c6659f748fd22abf87) |

### `SKU_IN_STOCK` — 1 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `sku-shopify-available` | DETERMINISTIC | 2856 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/sku-shopify-available.yaml) | [tx](https://sepolia.basescan.org/tx/0x545cdeeb046984a49eacd819bb292be3c12ebdef2ced28bebabf40b7de5c6b1e) |

### `SSL_VERIFICATION` — 2 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `ssl-certspotter` | DETERMINISTIC | 2896 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/ssl-certspotter.yaml) | [tx](https://sepolia.basescan.org/tx/0x3d20d1f1cddd93b72c2c514e31471004793a69e680cd95e413e2b6cb669e60aa) |
| `ssl-crtsh` | DETERMINISTIC | 2897 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/ssl-crtsh.yaml) | [tx](https://sepolia.basescan.org/tx/0x91902724619415eff726492df648ca1767b905c7a39b5faf6365488f8337d98e) |

### `STOCK_PRICE` — 3 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `stk-nasdaq` | DETERMINISTIC | 2886 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/stk-nasdaq.yaml) | [tx](https://sepolia.basescan.org/tx/0x8c79a9b751d38cedd33e7bba3e370b56160c8056eb2aa887e42009bcc6d46b83) |
| `stk-robinhood` | DETERMINISTIC | 2888 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/stk-robinhood.yaml) | [tx](https://sepolia.basescan.org/tx/0x6f141a8885b9d59f1db92c5a7db3dd2253dfc5f62bfea7320653123a7337e0ba) |
| `stk-tradingview` | DETERMINISTIC | 2887 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/stk-tradingview.yaml) | [tx](https://sepolia.basescan.org/tx/0x090fae7a049cdd5ab809a5a8f4223c4a3003bbed6abf5f098a6601b2b97d2fd8) |

### `TEXT_CLASSIFICATION` — 2 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `cls-hf-bart-mnli` | HYBRID | 2969 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/cls-hf-bart-mnli.yaml) | [tx](https://sepolia.basescan.org/tx/0xf53e2d374f84a2b0d1ef9eb2b3170d33f0044d99d53a9e42033ef49978506d46) |
| `cls-hf-twitter-roberta` | HYBRID | 2970 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/cls-hf-twitter-roberta.yaml) | [tx](https://sepolia.basescan.org/tx/0x3b59dcbc1a1e8b59af9a719b733d6a0f97a9bdd50a242382e5dc715c48c764de) |

### `TEXT_SUMMARIZATION` — 4 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `sum-hf-bart` | NON-DETERMINISTIC | 4391 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/sum-hf-bart.yaml) | [tx](https://sepolia.basescan.org/tx/0x269454a21a7221fe8531af2bbb5a93b575aa3902a6fb2ab900207c0689a348ed) |
| `sum-hf-distilbart` | NON-DETERMINISTIC | 4393 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/sum-hf-distilbart.yaml) | [tx](https://sepolia.basescan.org/tx/0x5165cf9457d33bcb6e5879189ba1cedbdba66c9c827a21344bf7837bc9ceade4) |
| `sum-hf-pegasus` | NON-DETERMINISTIC | 4392 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/sum-hf-pegasus.yaml) | [tx](https://sepolia.basescan.org/tx/0x0d4109363db1ca0d5536a25b5100ec0aaa9c5a8a493df11751969e8b86b8dc43) |
| `sum-pollinations` | NON-DETERMINISTIC | 4404 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/sum-pollinations.yaml) | [tx](https://sepolia.basescan.org/tx/0xe0c031af5762a3ddcb1465ff09a1cf969044f0e8a4d89daf99e0d00ae4271d1a) |

### `TEXT_TO_SPEECH` — 2 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `tts-espeak` | NON-DETERMINISTIC | 4403 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/tts-espeak.yaml) | [tx](https://sepolia.basescan.org/tx/0x9a156d943016f7cda9439e7ae59aadfad6f9d424fdf763fbc91f4b0e9daaeace) |
| `tts-google` | NON-DETERMINISTIC | 4402 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/tts-google.yaml) | [tx](https://sepolia.basescan.org/tx/0xf26742aee35c349231ea026b1ca450dd1ea541877781122439b758ac96c3887c) |

### `THREAT_INTELLIGENCE` — 3 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `tif-cymru` | HYBRID | 2900 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/tif-cymru.yaml) | [tx](https://sepolia.basescan.org/tx/0x1f2ab27c339be623adec45f51b722d94d9dd85617850c10830ba519e7005605d) |
| `tif-feodo` | HYBRID | 2901 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/tif-feodo.yaml) | [tx](https://sepolia.basescan.org/tx/0xdfb10897b169aa8e4aa5548b9b54c702ae5960f22a61caeee2548fe248db3907) |
| `tif-urlhaus` | HYBRID | 2902 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/tif-urlhaus.yaml) | [tx](https://sepolia.basescan.org/tx/0xacae04be35faf7aa1ca94e31fb39a9e24a62886ebc0565ec7422c60e7f09002b) |

### `THREAT_IP_REPUTATION` — 8 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `ipr-cins` | HYBRID | 2881 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/ipr-cins.yaml) | [tx](https://sepolia.basescan.org/tx/0xb6bc0f49c618ae791fa15248939e8468032e4b68966102d0a7b2051494b47dc1) |
| `ipr-dronebl` | HYBRID | 2880 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/ipr-dronebl.yaml) | [tx](https://sepolia.basescan.org/tx/0x04898aca2bfb6be44a582cb40928cbee636ddc44f3cf53c0252c0a4f61b45c54) |
| `ipr-greynoise` | HYBRID | 2877 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/ipr-greynoise.yaml) | [tx](https://sepolia.basescan.org/tx/0x1d6211dc46106e377d5c7e2cda50f639f55dc2a19e25fdff6c045409cc29ab1b) |
| `ipr-otx` | HYBRID | 2878 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/ipr-otx.yaml) | [tx](https://sepolia.basescan.org/tx/0x6bf24123b9819d1795aa4e2e5de3a1c33de8a9bf06c12b062e9509052bcace92) |
| `ipr-pulsedive` | HYBRID | 2879 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/ipr-pulsedive.yaml) | [tx](https://sepolia.basescan.org/tx/0x40d1a3f71a911ef1f715e9de9042bae41ed29a48be8a65de2bc566651d0150e5) |
| `tip-abuseipdb` | HYBRID | 2958 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/tip-abuseipdb.yaml) | [tx](https://sepolia.basescan.org/tx/0xaf850ca2103414212f385c707f7f41b215ee642d162f669fdb68f3e9eb5671f5) |
| `tip-dshield` | HYBRID | 4623 | [yaml](https://paste.rs/uWpCG) | [tx](https://sepolia.basescan.org/tx/0xbdb989727ff5c5b434b145f0d065b5eaaaaaac704c8db3cd8110a3094676faf4) |
| `tip-feodo` | HYBRID | 4623 | [yaml](https://paste.rs/Pezao) | [tx](https://sepolia.basescan.org/tx/0x49f8fab368c465bc2885341aed138a5570c03626c514abcae78d1f611c0cb88b) |

### `TOKEN_TOTAL_SUPPLY_VERIFY` — 5 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `sup-drpc` | DETERMINISTIC | 2915 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/sup-drpc.yaml) | [tx](https://sepolia.basescan.org/tx/0x8532209c42bdeb38fd26556ed89bba1a7be28f46bb3f6f69c846f76f606b6d4d) |
| `sup-solana` | DETERMINISTIC | 2916 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/sup-solana.yaml) | [tx](https://sepolia.basescan.org/tx/0x5d40e1ec9edcf0280c1d6df4364483ddc0686806b7a3ff41cdedfaa96b0f7e0d) |
| `supply-blockscout` | DETERMINISTIC | 4624 | [yaml](https://paste.rs/Fv02b) | [tx](https://sepolia.basescan.org/tx/0x8e52f9c3c1800b51ccef1176157457f657b1c2065c4d2c57e6410d6f439c9ad7) |
| `supply-coinpaprika` | DETERMINISTIC | 4651 | [yaml](https://paste.rs/sNEZN) | [tx](https://sepolia.basescan.org/tx/0x8c18928bc09ec580315d8bd02082f6fd4a419b4bbd0873e8c69bab26724c7f5e) |
| `supply-ethplorer` | DETERMINISTIC | 4653 | [yaml](https://paste.rs/c4b3V) | [tx](https://sepolia.basescan.org/tx/0xe51c2228de3957021538dd206fea85efeb19aeeb6436b9cb56d7b4fdfeb694a3) |

### `TRAVEL_DISRUPTION` — 1 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `trd-faa-nas` | DETERMINISTIC | 2889 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/trd-faa-nas.yaml) | [tx](https://sepolia.basescan.org/tx/0x0c110fae25850d0b439e2eacb270143f5cbada17704928f75ea1889c44ae5568) |

### `VALIDATOR_PERFORMANCE_VERIFY` — 3 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `val-beacon-publicnode` | DETERMINISTIC | 4625 | [yaml](https://paste.rs/HILFr) | [tx](https://sepolia.basescan.org/tx/0x81f9096f89bd80976c9a940990574279a7cc0d80ffa10d86900095fe9ab3e162) |
| `vlp-publicnode` | DETERMINISTIC | 2917 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/vlp-publicnode.yaml) | [tx](https://sepolia.basescan.org/tx/0x7a5ca9d57a72528a4d20b6d1b060305fe50c64fc0be14caaf60ae76a2310574c) |
| `vlp-quicknode` | DETERMINISTIC | 2918 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/vlp-quicknode.yaml) | [tx](https://sepolia.basescan.org/tx/0x82617473b95305b32386b2ad84b307b11d1f35e996576ce830faa297e9cc0195) |

### `VENDOR_VERIFY` — 5 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `vendor-vatcomply` | HYBRID | 4626 | [yaml](https://paste.rs/qd5qd) | [tx](https://sepolia.basescan.org/tx/0x3048f87d823a67c99daf42eb8939f77e399f3f0d2b7cc6b09cc44c12b8dd8109) |
| `vnd-brreg` | HYBRID | 2940 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/vnd-brreg.yaml) | [tx](https://sepolia.basescan.org/tx/0xb180ecaacd41de1af16c9032bad23761fe4175d92284d7ab4ae8ae76ac8b47c9) |
| `vnd-openiban` | HYBRID | 2941 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/vnd-openiban.yaml) | [tx](https://sepolia.basescan.org/tx/0x0fb88021407b57097bef041b0c008eceaf678f4ba99b4379c8e39a4c3c714208) |
| `vnd-vatcomply` | HYBRID | 2967 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/vnd-vatcomply.yaml) | [tx](https://sepolia.basescan.org/tx/0x657ce4e32c005b258e8a70e46f5120cbd1f4272cbf7a84fd8e23d61982304c27) |
| `vnd-vies` | HYBRID | 2939 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/vnd-vies.yaml) | [tx](https://sepolia.basescan.org/tx/0x32bdb9687c18a28a27cb4fc7cf57d8aee000d42386c67f5df4343e953210016c) |

### `VESSEL_TELEMETRY_VERIFY` — 1 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `ves-digitraffic` | DETERMINISTIC | 4365 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/ves-digitraffic.yaml) | [tx](https://sepolia.basescan.org/tx/0xe904ca271d47bc438a445ed8074a3d8b903a0cb28c45049a8d6c5e5466f01799) |

### `VULNERABILITY_TRIAGE` — 16 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `vuln-alpine-secdb` | HYBRID | 4548 | [yaml](https://paste.rs/csLqJ) | [tx](https://sepolia.basescan.org/tx/0x2492c5719ae1408615b046d6ccd5ba6dbf4bcb45f093914322566f7bb4db5299) |
| `vuln-circl-cve` | HYBRID | 4549 | [yaml](https://paste.rs/70kBV) | [tx](https://sepolia.basescan.org/tx/0xbe177367abf9f2655677a7ce6b34d9338c890da4e849284446175e98900fc96f) |
| `vuln-circl-cvss` | HYBRID | 2811 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/vuln-circl-cvss.yaml) | [tx](https://sepolia.basescan.org/tx/0xa5cfc46bb12da2d934ceeb3e8c4a4db823c1d885af8c96b05e9e39c5927c94a9) |
| `vuln-cisa-kev` | HYBRID | 4550 | [yaml](https://paste.rs/Uh0mw) | [tx](https://sepolia.basescan.org/tx/0x1184f2d2c584dbcce8b62128226ef88b2eca160d1c30327828bcb5df1d83fc64) |
| `vuln-cveorg-cvss` | HYBRID | 2785 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/vuln-cveorg-cvss.yaml) | [tx](https://sepolia.basescan.org/tx/0x24fd3dd46cc3cbe830790dfaab88390407391876ae307386d61f581d2456ec08) |
| `vuln-epss` | HYBRID | 4552 | [yaml](https://paste.rs/hpr4J) | [tx](https://sepolia.basescan.org/tx/0xf739d96018c42b1733dd6914bf73c239276958bdb675fa820c23c493c3e0d388) |
| `vuln-ghsa` | HYBRID | 2963 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/vuln-ghsa.yaml) | [tx](https://sepolia.basescan.org/tx/0xf8f9b350ec353e8c584d47d4b6793f01605f6460254d739ba64fa7cc47f56d2a) |
| `vuln-ghsa-advisory` | HYBRID | 4552 | [yaml](https://paste.rs/ydAfo) | [tx](https://sepolia.basescan.org/tx/0x0dd69920cd112d6a73bcdb2ad3656261ba2cc5efa914f22871ceef7e4c8f4fb7) |
| `vuln-mitre-cveorg` | HYBRID | 4553 | [yaml](https://paste.rs/xOGGR) | [tx](https://sepolia.basescan.org/tx/0x49c79262eb8cc3e5b9f8d63012c4bfb8e6df05b03ab48a85fcbc3761ad7c2947) |
| `vuln-nvd-cve` | HYBRID | 2768 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/vuln-nvd-cve.yaml) | [tx](https://sepolia.basescan.org/tx/0x9afc5adbd0796d403cd34825e2f6af4e83f57e57f262c7cf6d7f3c3764fb320c) |
| `vuln-osv-cve` | HYBRID | 4556 | [yaml](https://paste.rs/OCaTn) | [tx](https://sepolia.basescan.org/tx/0x502e645f25ae117e9a2d81640864a07e2b6c7297ff2a4c464c4196dca858dc6d) |
| `vuln-osv-cvss` | HYBRID | 2812 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/vuln-osv-cvss.yaml) | [tx](https://sepolia.basescan.org/tx/0x135893c4449878c461bde924022d0181c3109c9a268d81aea6232d1fc802dff6) |
| `vuln-redhat` | HYBRID | 2964 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/vuln-redhat.yaml) | [tx](https://sepolia.basescan.org/tx/0xa671dd500009fba153598e2a2eff3fca7d97d7084f85ff96addf34b0030b09ae) |
| `vuln-redhat-cve` | HYBRID | 4557 | [yaml](https://paste.rs/PogtP) | [tx](https://sepolia.basescan.org/tx/0x90c005d7db0d9cea40b6ddeb905842f2f1e20f3442489e825d4a5b8789ce7243) |
| `vuln-shodan-cvedb` | HYBRID | 4557 | [yaml](https://paste.rs/P83eJ) | [tx](https://sepolia.basescan.org/tx/0x857d470f7926c91673e55e3579a959b06529b8dc89e81e606cb65fa4981afb8a) |
| `vuln-ubuntu` | HYBRID | 4559 | [yaml](https://paste.rs/n2wtx) | [tx](https://sepolia.basescan.org/tx/0xf929ba9d510bdf9faefec3806028c79338bf6ea330d282bbb49a9cb362339ad4) |

### `WEATHER_CHECK` — 5 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `wxk-7timer` | DETERMINISTIC | 2959 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/wxk-7timer.yaml) | [tx](https://sepolia.basescan.org/tx/0xe21f5333f7f4992fda59b0ed8b6231aaaf957cb44ce3d70e5b70f156a27dcb13) |
| `wxk-brightsky` | DETERMINISTIC | 2884 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/wxk-brightsky.yaml) | [tx](https://sepolia.basescan.org/tx/0x123f751731df9acd17f31083fc1fef83d40eb7d76cf84ab72bae2156ea0bc42b) |
| `wxk-metar` | DETERMINISTIC | 2885 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/wxk-metar.yaml) | [tx](https://sepolia.basescan.org/tx/0xbb1ae9e8d7918c8c827e91db28061704ac5b5ba17913234aa1888e0d113beee3) |
| `wxk-metno` | DETERMINISTIC | 2883 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/wxk-metno.yaml) | [tx](https://sepolia.basescan.org/tx/0xd94dc5b203e40f6952aae29f8ed091c81a0cf8e9ad3fc26a2a8bc755ccb8014e) |
| `wxk-openmeteo` | DETERMINISTIC | 2882 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/wxk-openmeteo.yaml) | [tx](https://sepolia.basescan.org/tx/0xe62ff4d29795374f74e0751802dffc2487847d5e38cca2fd76f47faa3ae7c28d) |

### `WEATHER_FORECAST_VERIFY` — 5 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `wnd-brightsky` | DETERMINISTIC | 2909 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/wnd-brightsky.yaml) | [tx](https://sepolia.basescan.org/tx/0x957e5c57c25f7d73006c190be620845e1847a073d9aeeb45698efb5846f85ff4) |
| `wnd-envcanada` | DETERMINISTIC | 2911 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/wnd-envcanada.yaml) | [tx](https://sepolia.basescan.org/tx/0xe8064f429ed348bbd99bcf915af141e93136fefe9d4e8fc8781e289fe699268b) |
| `wnd-era5` | DETERMINISTIC | 2908 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/wnd-era5.yaml) | [tx](https://sepolia.basescan.org/tx/0xc64ec164da138b7591d43fb0e1a4aabf1b6fee17fe638a1188154abebe343502) |
| `wnd-jma` | DETERMINISTIC | 2912 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/wnd-jma.yaml) | [tx](https://sepolia.basescan.org/tx/0xe4e95fc3c72572d8e627857537cb9fb5cc026fe65a77359ebea02334ad55b7b6) |
| `wnd-metar` | DETERMINISTIC | 2910 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/wnd-metar.yaml) | [tx](https://sepolia.basescan.org/tx/0xc1f1396315ca88493940f8e2673cc58c38d97befa94e4af5ed852127829da1f2) |

### `WEB_SEARCH` — 1 miner(s)

| Slug | Class | Reg | YAML | Tx |
|------|-------|----:|------|-----|
| `srch-marginalia` | DETERMINISTIC | 2949 | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/srch-marginalia.yaml) | [tx](https://sepolia.basescan.org/tx/0x58ab2158e7217fd844d67c6f08049709d39f6fc1e2cb3affe355f0e7a1cf091f) |

---

<div style="background:#e8f5e9;border:2px solid #2e7d32;border-radius:8px;padding:12px 16px;margin:12px 0">

### 1. Active — registered & approved

Per-miner **YAML + tx** tables: **top of file** (`# Active miner tables`) — **289 miners · 56 intents**. Intent rollup only in [Appendix](#appendix--lifecycle-rollups-reference).

</div>


<div style="background:#e8f5e9;border:2px solid #2e7d32;border-radius:8px;padding:12px 16px;margin:12px 0">

### 2. Pre-active — none

Removed **2026-10-06**. Former Pre-active (**137**) promoted into Active (**289** total).

</div>

### 3. Not registered yet — waiting on a free key

None left open after Batch 7 (HF + AbuseIPDB keys unlocked `SEMANTIC_SIMILARITY` and `TEXT_CLASSIFICATION`).

**Subtotal:** **0 intents** still open.

---

<div style="background:#fce4ec;border:2px solid #c62828;border-radius:8px;padding:12px 16px;margin:12px 0">

### 4. Dead — rejected or no source found

Usman rejected a pre-active pack, **or** a hunt found **zero** description-correct sources. Do not keep hunting without new evidence.

**2026-09-29/30:** `LANGUAGE_TRANSLATION`, `TEXT_SUMMARIZATION`, `CHATBOT_CONVERSATION`, `TEXT_TO_SPEECH` removed from Dead → **Pre-active** (NON-DET campaign, 13 miners).

| Intent | Class | Scoring path | Category | Priority | Miners | Reason |
|--------|-------|--------------|----------|----------:|-------:|--------|
| `CODE_REVIEW` | NON-DETERMINISTIC | adapter only | Software / Engineering | 10.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — NO_JUDGMENT (lookups ≠ review); no honest source |
| `COMMERCE_PURCHASE_VERIFY` | DETERMINISTIC | comparator only | Commerce & Procurement | 10.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — needs Stripe/PayPal key; no keyless purchase-auth API |
| `WASH_TRADING_DETECTION` | HYBRID | comparator + adapter | Blockchain & Web3 | 10.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — no circular-flow API; volume = WRONG_QUANTITY |
| `FRAUD_RISK` | NON-DETERMINISTIC | adapter only | Financial / Transactional | 9.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — adapter only; keyed risk engines |
| `LLM_OUTPUT_EVALUATION` | NON-DETERMINISTIC | adapter only | AI & Machine Learning | 9.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — adapter only / NO_JUDGMENT lookups |
| `TRANSACTION_RISK` | NON-DETERMINISTIC | adapter only | Financial / Transactional | 9.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Gate 0 adapter-only |
| `CODE_GENERATION` | HYBRID | comparator + adapter | Software / Engineering | 8.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — generate ≠ compile; sandboxes = CODE_PATCH |
| `CONTRACT_OBLIGATION_AUDIT` | NON-DETERMINISTIC | adapter only | Enterprise Operations | 8.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Gate 0 adapter-only |
| `FACT_CHECKING` | HYBRID | comparator + adapter | Trust & Safety | 8.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — keyed ClaimReview / NO_JUDGMENT |
| `QUESTION_ANSWERING` | HYBRID | comparator + adapter | AI & Machine Learning | 8.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — LLM/RAG adapter path |
| `TOXICITY_MODERATION` | HYBRID | comparator + adapter | Trust & Safety | 8.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Perspective/OpenAI keyed |
| `CREDIT_SCORE_VERIFY` | HYBRID | comparator + adapter | Financial / Transactional | 7.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — bureau sandboxes keyed |
| `CURRENCY_EXCHANGE` | DETERMINISTIC | comparator only | Financial / Transactional | 7.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — DUPLICATE of FX_NOW |
| `ENTITY_EXTRACTION` | HYBRID | comparator + adapter | AI & Machine Learning | 7.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — keyed NER + gold spans |
| `INTENT_CLASSIFICATION` | HYBRID | comparator + adapter | AI & Machine Learning | 7.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — labeled NLU adapter |

| `PLAGIARISM_DETECTION` | HYBRID | comparator + adapter | Trust & Safety | 7.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: paid/keyed only |
| `PURCHASE_ORDER_VERIFY` | DETERMINISTIC | comparator only | Commerce & Procurement | 7.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: demo ERPs closed; award registries are a different quantity |
| `SMART_CONTRACT_AUDIT` | HYBRID | comparator + adapter | Blockchain & Web3 | 7.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: no analyzer API; Sourcify is_verified is a different quantity |
| `SOCIAL_BOT_DETECTION` | NON-DETERMINISTIC | adapter only | Trust & Safety | 7.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: Gate 0 adapter-only |
| `SPEECH_TO_TEXT` | HYBRID | comparator + adapter | AI & Machine Learning | 7.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: keyed ASR; WER needs a gold transcript |
| `TASK_EXECUTION_QUALITY` | NON-DETERMINISTIC | adapter only | Software / Engineering | 7.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: Gate 0 adapter-only |
| `CUSTOMER_TICKET_RESOLUTION` | NON-DETERMINISTIC | adapter only | Enterprise Operations | 6.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: Gate 0 adapter-only |
| `EMBEDDING_GENERATION` | DETERMINISTIC | comparator only | AI & Machine Learning | 6.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: output is a vector, not a scalar, and APIs are keyed |
| `IMAGE_CAPTIONING` | NON-DETERMINISTIC | adapter only | AI & Machine Learning | 6.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: Gate 0 adapter-only |
| `KEYWORD_EXTRACTION` | HYBRID | comparator + adapter | AI & Machine Learning | 6.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: keyed; output is a set, not a scalar |
| `SHIPMENT_DELAY_RISK` | NON-DETERMINISTIC | adapter only | Logistics | 5.0 | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: Gate 0 adapter-only |
| `ACCESS_PRIVILEGE_DRIFT_AUDIT` | HYBRID | comparator + adapter | Enterprise Operations |  | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: not on chain; private IAM data |
| `AGENT_TOOL_CALL_AUDIT` | HYBRID | comparator + adapter | AI & Machine Learning |  | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: not on chain; no public source |
| `CARBON_OFFSET_RETIREMENT` | DETERMINISTIC | comparator only | Climate & Weather |  | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: not on chain |
| `COLD_CHAIN_TEMPERATURE_BREACH` | DETERMINISTIC | comparator only | IoT & Telemetry |  | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: not on chain; private logger data |
| `COLLATERAL_HAIRCUT_VALUATION` | HYBRID | comparator + adapter | Financial / Transactional |  | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: not on chain; judgment model |
| `CROSS_BORDER_REMITTANCE_STATUS` | DETERMINISTIC | comparator only | Financial / Transactional |  | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: not on chain; SWIFT gpi is authenticated |
| `DEFORESTATION_SURVEILLANCE` | HYBRID | comparator + adapter | Geospatial & Remote Sensing |  | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: not on chain; Global Forest Watch is keyed |
| `EXPORT_CONTROL_CLASSIFICATION` | HYBRID | comparator + adapter | Legal & Compliance |  | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: not on chain; interpretive |
| `FLOOD_EXTENT_MAPPING` | HYBRID | comparator + adapter | Climate & Weather |  | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: not on chain; no scalar |
| `GDPR_DATA_ERASURE_AUDIT` | HYBRID | comparator + adapter | Legal & Compliance |  | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: not on chain; private ledgers |
| `METHANE_EMISSION_DETECTION` | HYBRID | comparator + adapter | Geospatial & Remote Sensing |  | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: not on chain; inference over imagery |
| `PROMPT_INJECTION_DETECT` | HYBRID | comparator + adapter | AI & Machine Learning |  | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: not on chain; classifier judgment |
| `RAG_GROUNDING_VERIFY` | HYBRID | comparator + adapter | AI & Machine Learning |  | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: not on chain; judgment |
| `SMART_METER_TAMPER_DETECT` | HYBRID | comparator + adapter | IoT & Telemetry |  | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: not on chain; private utility data |
| `SYNTHETIC_DATA_FIDELITY` | HYBRID | comparator + adapter | AI & Machine Learning |  | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: not on chain; judgment over statistics |
| `WILDFIRE_PERIMETER_MONITOR` | HYBRID | comparator + adapter | Geospatial & Remote Sensing |  | 0 | <span style="background:#ffcdd2;color:#b71c1c;padding:2px 8px;border-radius:4px;font-weight:700">DEAD</span> — Fable 2026-09-24: not on chain; NASA FIRMS needs a key; perimeter is modelled |
**Subtotal:** **46 intents** dead.

</div>

---

# Active intents — detail

<div style="background:#e8f5e9;border:2px solid #2e7d32;border-radius:8px;padding:4px 16px 16px 16px;margin:16px 0">

## Registered intents (live miners)

Highlighted in green. Number = live keepers after same-source cleanup (one miner = one source).

<div style="background:#e8f5e9;border-left:6px solid #2e7d32;padding:10px 14px;margin:16px 0 8px 0;border-radius:4px">

### <span style="color:#0b6e4f">`FX_NOW`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">REGISTERED · 11 miners</span>

</div>

- **Class:** DETERMINISTIC
- **Why:** Mid-market rate, numeric tolerance, short TTL.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 8.0 · **Verification complexity:** Low
- **Data source type:** FX Liquidity Feeds
- **Primary aggregators / hubs:** Frankfurter / ExchangeRate-API
- **Target latency:** < 200ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Provides real-time institutional foreign exchange mid-market rates, spreads, and currency conversion quotes.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

RapidAPI hosts 40+ FX APIs. Miners query different liquidity feeds to calculate mid-market consensus.

</details>

**Comparator contract (scored — from build plan Part III):**

| Field | Value |
|-------|-------|
| `label_field` | `rate` |
| Scale | ×10000 |
| Tolerance | 50 bps |
| Required params | `base, quote` |
| Pins / known truths | USD→EUR, USD→CAD, USD→SEK |

**Quantity sentence template:** This miner returns **`rate`** for pinned params `base, quote`.

**Live:** 11 keepers — one per distinct FX provider. Do not add mirrors of an existing provider.

---

---

<div style="background:#e8f5e9;border-left:6px solid #2e7d32;padding:10px 14px;margin:16px 0 8px 0;border-radius:4px">

### <span style="color:#0b6e4f">`VULNERABILITY_TRIAGE`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">REGISTERED · 4 miners</span>

</div>

- **Class:** HYBRID
- **Why:** CVE lookup is a fact; priority ordering is judgment.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 10.0 · **Verification complexity:** High
- **Data source type:** Vulnerability DB / Scanner
- **Primary aggregators / hubs:** NIST NVD / CVE Details / RapidAPI
- **Target latency:** < 2s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Ranks and categorizes detected vulnerabilities by CVSS score, active exploit availability, and asset criticality.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners cross-reference CVSS severity scores from different global vulnerability databases.

</details>

**Doctrine pitfall:** Hybrid pass_fail in contract; Usman Discord listed as working/rankable with 4 sources (CIRCL/OSV/NVD/CVE.org). Prefer description CVSS.

**Live:** 4 keepers (`vuln-nvd-cve`, `vuln-cveorg-cvss`, `vuln-circl-cvss`, `vuln-osv-cvss`). NVD/CVE.org letter clones removed.

---

---

<div style="background:#e8f5e9;border-left:6px solid #2e7d32;padding:10px 14px;margin:16px 0 8px 0;border-radius:4px">

### <span style="color:#0b6e4f">`EMAIL_SECURITY`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">REGISTERED · 2 miners</span>

</div>

- **Class:** HYBRID
- **Why:** SPF/DKIM/DMARC are mechanical; phishing intent is judgment.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 7.0 · **Verification complexity:** Medium
- **Data source type:** Mail Gateway / DNS Feed
- **Primary aggregators / hubs:** Mailcheck / DMARC Analyzer
- **Target latency:** < 500ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Verifies SPF, DKIM, and DMARC records, inspects header anomalies, and detects spoofing or malicious attachments.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners independently query and parse DNS MX, SPF, and DMARC TXT records.

</details>

**Doctrine pitfall:** Hybrid pass_fail in contract; Usman Discord listed working. SPF/DKIM/DMARC via DoH.

**Live:** 2 keepers (`email-cf-gmail-mx`, `email-dns-dmarc-gmail`) — Cloudflare + Google DoH. Extra DoH variants deregistered.

---

---

<div style="background:#e8f5e9;border-left:6px solid #2e7d32;padding:10px 14px;margin:16px 0 8px 0;border-radius:4px">

### <span style="color:#0b6e4f">`LIQUIDITY_DEPTH_VERIFY`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">REGISTERED · 2 miners</span>

</div>

- **Class:** DETERMINISTIC
- **Why:** Orderbook depth at a timestamp is an observable number.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 10.0 · **Verification complexity:** Medium
- **Data source type:** DEX Orderbook / Node Feed
- **Primary aggregators / hubs:** GeckoTerminal / DexScreener
- **Target latency:** < 500ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Measures bid-ask order book depth, cumulative slippage bands, and market maker liquidity across decentralized pools.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners query different decentralized exchange liquidity subgraphs and order books.

</details>

**Comparator contract (scored — from build plan Part III):**

| Field | Value |
|-------|-------|
| `label_field` | `liquidity_usd_cents` |
| Scale | ×100 |
| Tolerance | 300 bps |
| Required params | `network, pool_address` |
| Pins / known truths | network eth, pool 0x88e6a0c2…5640 |

**Quantity sentence template:** This miner returns **`liquidity_usd_cents`** for pinned params `network, pool_address`.

**Doctrine pitfall:** Description says order-book depth/slippage; code scores pool TVL (liquidity_usd_cents). Match the CODE field until Usman changes wiring.

**Live:** 2 keepers (`liq-gecko-pool-cents`, `liq-dex-pair-cents`) — one per source. No clones. New miners must be a third distinct publisher.

---

---

<div style="background:#e8f5e9;border-left:6px solid #2e7d32;padding:10px 14px;margin:16px 0 8px 0;border-radius:4px">

### <span style="color:#0b6e4f">`MACRO_ECONOMIC_INDICATOR`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">REGISTERED · 2 miners</span>

</div>

- **Class:** DETERMINISTIC
- **Why:** Published statistic from a central bank or stat agency.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 8.0 · **Verification complexity:** Low
- **Data source type:** Central Bank / Stat Agency
- **Primary aggregators / hubs:** FRED / World Bank API
- **Target latency:** < 2s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Aggregates released central bank interest rates, consumer price index (CPI) updates, and unemployment figures.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners query different federal reserve nodes, statistical agencies, and open finance endpoints.

</details>

**Comparator contract (scored — from build plan Part III):**

| Field | Value |
|-------|-------|
| `label_field` | `rate_pct` |
| Scale | ×1000 |
| Tolerance | 150 bps |
| Required params | `country, indicator, year` |
| Pins / known truths | USA / SL.UEM.TOTL.ZS / 2019 → 3.669 |

**Quantity sentence template:** This miner returns **`rate_pct`** for pinned params `country, indicator, year`.

**Doctrine pitfall:** Description covers CPI/rates broadly; pin is unemployment SL.UEM.TOTL.ZS by country+year.

**Live:** 2 keepers (`macro-wb-unemp-us`, `macro-wb-unemp-proxy`). Proxy letter clones removed. Prefer a truly independent compiler next.

---

---

<div style="background:#e8f5e9;border-left:6px solid #2e7d32;padding:10px 14px;margin:16px 0 8px 0;border-radius:4px">

### <span style="color:#0b6e4f">`ROUTE_ETA`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">REGISTERED · 2 miners</span>

</div>

- **Class:** DETERMINISTIC
- **Why:** Scored as numeric agreement with routing-engine consensus.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 6.0 · **Verification complexity:** Low
- **Data source type:** Geospatial Telematics
- **Primary aggregators / hubs:** OpenRouteService / OSRM / Google
- **Target latency:** < 500ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Computes multimodal routing itineraries, live traffic transit times, and turn-by-turn arrival estimations.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners query different routing engines (TomTom, Mapbox, OSRM) to output median transit time.

</details>

**Comparator contract (scored — from build plan Part III):**

| Field | Value |
|-------|-------|
| `label_field` | `eta_seconds` |
| Scale | ×1 |
| Tolerance | 800 bps |
| Required params | `origin_lat, origin_lon, dest_lat, dest_lon` |
| Pins / known truths | three origin/destination coordinate pairs |

**Quantity sentence template:** This miner returns **`eta_seconds`** for pinned params `origin_lat, origin_lon, dest_lat, dest_lon`.

**Doctrine pitfall:** Description says live traffic; truth is free-flow OSRM. Second source must be free-flow (GraphHopper/Valhalla/ORS), NOT traffic-aware.

**Live:** 2 keepers (`route-osrm-berlin`, `route-osrm-table`) — OSRM route + table. Other OSRM default peers removed. Next source must be free-flow (GraphHopper/Valhalla/ORS), not more OSRM.

---

---

<div style="background:#e8f5e9;border-left:6px solid #2e7d32;padding:10px 14px;margin:16px 0 8px 0;border-radius:4px">

### <span style="color:#0b6e4f">`ASSET_RESERVE_ATTESTATION`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">REGISTERED · 1 miner</span>

</div>

- **Class:** DETERMINISTIC
- **Why:** Attested balance compared against a custody feed.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 9.0 · **Verification complexity:** High
- **Data source type:** Oracle / Custody API
- **Primary aggregators / hubs:** Chainlink PoR / Etherscan API
- **Target latency:** < 5s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Verifies cryptographic proof-of-reserves and custodial bank confirmations backing stablecoins and tokenized assets.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners cross-reference on-chain reserve wallet balances with custodian public API endpoints.

</details>

**Comparator contract (scored — from build plan Part III):**

| Field | Value |
|-------|-------|
| `label_field` | `attested_reserve` |
| Scale | ×1 pre-scaled |
| Tolerance | 150 bps |
| Required params | `feed_address, block` |
| Pins / known truths | feed 0xa81FE040…, block 0x18d20a9 → 116144649223 |

**Quantity sentence template:** This miner returns **`attested_reserve`** for pinned params `feed_address, block`.

**Doctrine pitfall:** Description covers stablecoin backing generally; pin is one WBTC feed at one block. Latest-only APIs = NOT_ASKABLE.

**Live:** 1 keeper (`res-wbtc-por`). Same-source clones removed. Need a second independent publisher — not another RPC.

---

---

<div style="background:#e8f5e9;border-left:6px solid #2e7d32;padding:10px 14px;margin:16px 0 8px 0;border-radius:4px">

### <span style="color:#0b6e4f">`GRID_POWER_PRICE`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">REGISTERED · 1 miner</span>

</div>

- **Class:** DETERMINISTIC
- **Why:** Published ISO/RTO settlement price.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 5.0 · **Verification complexity:** Low
- **Data source type:** ISO / RTO Telemetry Feed
- **Primary aggregators / hubs:** U.S. EIA API / ENTSO-E / ERCOT
- **Target latency:** < 1s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Ingests real-time nodal marginal locational prices (LMP) and day-ahead electricity spot rates from regional grid operators.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners query independent regional ISOs and grid telemetry dashboards directly.

</details>

**Comparator contract (scored — from build plan Part III):**

| Field | Value |
|-------|-------|
| `label_field` | `lmp_usd_per_mwh_milli` |
| Scale | ×1000 |
| Tolerance | 30 bps |
| Required params | `node, market, interval_start_utc` |
| Pins / known truths | TH_NP15_GEN-APND, DAM, 2026-09-13T14:00:00Z → 38095 |

**Quantity sentence template:** This miner returns **`lmp_usd_per_mwh_milli`** for pinned params `node, market, interval_start_utc`.

**Doctrine pitfall:** Must be nodal LMP in USD/MWh milli — carbon intensity / EU zones = WRONG_QUANTITY/MARKET.

**Live:** 1 keeper (`grid-caiso-np15-dam`). Letter peers removed. Need a distinct LMP publisher for ranking.

---

---

<div style="background:#e8f5e9;border-left:6px solid #2e7d32;padding:10px 14px;margin:16px 0 8px 0;border-radius:4px">

### <span style="color:#0b6e4f">`LIVE_SHELF_PRICE`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">REGISTERED · 1 miner</span>

</div>

- **Class:** DETERMINISTIC
- **Why:** A quoted price at a moment, numeric tolerance.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 10.0 · **Verification complexity:** Low
- **Data source type:** Web Scraping / API
- **Primary aggregators / hubs:** RapidAPI (Amazon/Walmart Scrapers)
- **Target latency:** < 2s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Fetches and verifies current live shelf or retail listing prices across online merchant catalogs and marketplaces.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

RapidAPI has 50+ e-commerce scrapers. Miners use different scraping endpoints to find the median price.

</details>

**Comparator contract (scored — from build plan Part III):**

| Field | Value |
|-------|-------|
| `label_field` | `price_cents` |
| Scale | ×100 |
| Tolerance | 300 bps |
| Required params | `price_id` |
| Pins / known truths | price_id 1→2770, 100→373, 331088→523, 331090→99 (EUR) |

**Quantity sentence template:** This miner returns **`price_cents`** for pinned params `price_id`.

**Doctrine pitfall:** Description says merchant catalogs; pin is Open Prices price_id (EUR).

**Live:** 1 keeper (`shelf-open-prices`). Same-source clones removed. Need a second independent publisher of the same quantity.

---

---

<div style="background:#e8f5e9;border-left:6px solid #2e7d32;padding:10px 14px;margin:16px 0 8px 0;border-radius:4px">

### <span style="color:#0b6e4f">`MINING_HASHPRICE_VERIFY`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">REGISTERED · 1 miner</span>

</div>

- **Class:** DETERMINISTIC
- **Why:** Derived from observable pool and block-explorer data.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 5.0 · **Verification complexity:** Medium
- **Data source type:** Mining Pool / Block Explorer
- **Primary aggregators / hubs:** Mempool.space / Hashrate Index
- **Target latency:** < 1s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Calculates instantaneous proof-of-work mining revenue per unit of hashing power based on block rewards and network difficulty.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners query different Bitcoin/PoW mempool explorers and difficulty calculators.

</details>

**Comparator contract (scored — from build plan Part III):**

| Field | Value |
|-------|-------|
| `label_field` | `hashprice_sats_per_ph_s_day` |
| Scale | ×1 |
| Tolerance | 400 bps |
| Required params | `height` |
| Pins / known truths | heights 800000, 840000, 900000; 800000 → 233214 |

**Quantity sentence template:** This miner returns **`hashprice_sats_per_ph_s_day`** for pinned params `height`.

**Doctrine pitfall:** Must be height-pinnable hashprice sats/PH/s/day — raw hashrate/fees = WRONG_QUANTITY. Mempool mirrors = one source.

**Live:** 1 keeper (`mine-mempool-hashprice`). Mempool/blockstream mirrors removed (same formula).

---

---

<div style="background:#e8f5e9;border-left:6px solid #2e7d32;padding:10px 14px;margin:16px 0 8px 0;border-radius:4px">

### <span style="color:#0b6e4f">`ONCHAIN_METRIC_VERIFY`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">REGISTERED · 1 miner</span>

</div>

- **Class:** DETERMINISTIC
- **Why:** Read a value from an RPC node at a block height.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 10.0 · **Verification complexity:** Medium
- **Data source type:** Blockchain RPC Node
- **Primary aggregators / hubs:** Alchemy / Infura / QuickNode
- **Target latency:** < 2s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Validates smart contract event logs, gas consumption, token balances, and wallet transaction states directly on-chain.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners query independent RPC providers and archive nodes to prevent single-provider spoofing.

</details>

**Comparator contract (scored — from build plan Part III):**

| Field | Value |
|-------|-------|
| `label_field` | `value_gwei` |
| Scale | ×1 pre-scaled |
| Tolerance | 5 bps |
| Required params | `address, block` |
| Pins / known truths | block 23000000; VITALIK / BEACON / EXCHANGE |

**Quantity sentence template:** This miner returns **`value_gwei`** for pinned params `address, block`.

**Doctrine pitfall:** Description covers gas/logs/tx; pin is native ETH balance at block. Multi-RPC = one source.

**Live:** 1 keeper (`ocm-eth-balance`). Same-source RPC clones removed. Multi-RPC ≠ new source.

---

---

</div>

## Other active intents (0 miners)

## AI & Machine Learning

### <span style="color:#b71c1c">`AGENT_TOOL_CALL_AUDIT`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. not on chain; no public source.

- **Class:** HYBRID
- **Why:** Schema and policy compliance are mechanical; appropriateness of the call is judgment.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** — · **Verification complexity:** Medium
- **Data source type:** API Gateway Telemetry
- **Primary aggregators / hubs:** —
- **Target latency:** < 400ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Validates deterministic schema arguments and authorization scopes for AI agent function invocations.

---

---

### <span style="color:#0b6e4f">`CHATBOT_CONVERSATION`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 3 miners</span>

- **Lifecycle:** Active — promoted 2026-10-06 (was Pre-active) — NON-DET campaign 2026-09-29; flipped from Dead. See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md).


- **Class:** NON-DETERMINISTIC
- **Why:** Conversational flow, persona adherence, and helpfulness are subjective qualitative traits.
- **Scoring path:** adapter only
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 7.0 · **Verification complexity:** High
- **Data source type:** Conversational LLM
- **Primary aggregators / hubs:** OpenRouter / Anthropic / OpenAI
- **Target latency:** < 1.5s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Multi-Turn CSAT & Safety Rubric

**Description (what the miner must answer):**

> Maintains multi-turn conversational context, tone alignment, and empathetic response delivery.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners generate interactive dialogue turns evaluated against persona rubrics and safety constraints.

</details>

---

---

### <span style="color:#b71c1c">`EMBEDDING_GENERATION`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. output is a vector, not a scalar, and APIs are keyed.

- **Class:** DETERMINISTIC
- **Why:** Inference through a fixed neural model with greedy deterministic forward pass returns invariant float vectors.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 6.0 · **Verification complexity:** Low
- **Data source type:** Vector Embedding Service
- **Primary aggregators / hubs:** OpenAI text-embedding-3 / Voyage AI / BGE-large
- **Target latency:** < 200ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Vector Epsilon Comparator

**Description (what the miner must answer):**

> Transforms input text strings into standardized high-dimensional float vector embeddings for retrieval systems.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners run the exact model weights to confirm output vector components within floating-point epsilon.

</details>

---

---

### `ENTITY_EXTRACTION`

- **Class:** HYBRID
- **Why:** Standard entity spans are verifiable; disambiguation and novel entity types require judgment.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 7.0 · **Verification complexity:** Medium
- **Data source type:** NER Engine / NLP Model
- **Primary aggregators / hubs:** spaCy / Hugging Face (GLiNER) / OpenAI
- **Target latency:** < 600ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Span-Level F1 Score

**Description (what the miner must answer):**

> Extracts named entities (people, organizations, locations, dates) with character offsets from unstructured text.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners run distinct open-source NER models to cross-verify entity span annotations.

</details>

---

---

### <span style="color:#b71c1c">`IMAGE_CAPTIONING`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. Gate 0 adapter-only.

- **Class:** NON-DETERMINISTIC
- **Why:** Salient objects and visual descriptions have multiple valid verbal formulations.
- **Scoring path:** adapter only
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 6.0 · **Verification complexity:** High
- **Data source type:** Vision-Language Model (VLM)
- **Primary aggregators / hubs:** OpenRouter (GPT-4o / Qwen-VL) / BLIP-2
- **Target latency:** < 2.5s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** CLIPScore & CIDEr Metric

**Description (what the miner must answer):**

> Generates descriptive, contextual alt-text captions describing the primary subjects and scenes in image files.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners run distinct open-source vision-language models evaluated with CIDEr and CLIP score.

</details>

---

---

### `INTENT_CLASSIFICATION`

- **Class:** HYBRID
- **Why:** Deterministic match on exact triggers; semantic embedding intent matching requires probability scoring.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 7.0 · **Verification complexity:** Medium
- **Data source type:** NLU Intent Engine
- **Primary aggregators / hubs:** Rasa NLU / Hugging Face / Cohere Classify
- **Target latency:** < 300ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Top-1 Intent Match & Slot F1

**Description (what the miner must answer):**

> Classifies user natural language input into downstream system action intents and extracts slot arguments.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners map conversational inputs to canonical intent schemas using independent transformer classifiers.

</details>

---

---

### <span style="color:#b71c1c">`KEYWORD_EXTRACTION`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. keyed; output is a set, not a scalar.

- **Class:** HYBRID
- **Why:** TF-IDF / statistical term frequency is mechanical; conceptual relevance ranking is judgment.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 6.0 · **Verification complexity:** Low
- **Data source type:** NLP Keyphrase Extractor
- **Primary aggregators / hubs:** KeyBERT / YAKE / RapidAPI (NLP)
- **Target latency:** < 400ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Jaccard Index & Rank Overlap

**Description (what the miner must answer):**

> Extracts representative topical keywords, keyphrases, and n-grams from body text.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners run distinct keyphrase algorithms (KeyBERT, YAKE, RAKE) and compute rank intersection.

</details>

---

---

### <span style="color:#0b6e4f">`LANGUAGE_TRANSLATION`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 4 miners</span>

- **Lifecycle:** Active — promoted 2026-10-06 (was Pre-active) — NON-DET campaign 2026-09-29; flipped from Dead. See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md).


- **Class:** NON-DETERMINISTIC
- **Why:** Fluency and phrasing vary across linguists; no single authoritative translation exists.
- **Scoring path:** adapter only
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 8.0 · **Verification complexity:** High
- **Data source type:** NMT / Translation LLM
- **Primary aggregators / hubs:** DeepL API / Google Translate / NLLB-200
- **Target latency:** < 1.5s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** COMET / BLEU Metric Comparator

**Description (what the miner must answer):**

> Translates multilingual text between source and target language pairs preserving semantic intent and idiom.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners execute translation across different neural machine translation models scored by BLEU and COMET.

</details>

---

---

### `LLM_OUTPUT_EVALUATION`

- **Class:** NON-DETERMINISTIC
- **Why:** Judging generative output against fidelity and safety is the definition of judgment.
- **Scoring path:** adapter only
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 9.0 · **Verification complexity:** High
- **Data source type:** LLM Benchmark Evaluator
- **Primary aggregators / hubs:** OpenRouter.ai / Hugging Face
- **Target latency:** < 3s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Evaluates generative model responses against factual ground truth, citation fidelity, hallucination markers, and safety guardrails.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

OpenRouter has 200+ models. 10 miners run 10 different "Judge" LLMs (Llama 3, DeepSeek, etc.).

</details>

---

---

### <span style="color:#b71c1c">`PROMPT_INJECTION_DETECT`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. not on chain; classifier judgment.

- **Class:** HYBRID
- **Why:** Labelled corpora exist for known attacks; novel phrasings need inference.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** — · **Verification complexity:** High
- **Data source type:** Guardrail Classifier
- **Primary aggregators / hubs:** —
- **Target latency:** < 250ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Detects direct and indirect adversarial prompt injection attempts and jailbreak patterns in user inputs.

---

---

### `QUESTION_ANSWERING`

- **Class:** HYBRID
- **Why:** Factual premise is checkable against reference knowledge; completeness and phrasing require judgment.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 8.0 · **Verification complexity:** High
- **Data source type:** Generative LLM / RAG
- **Primary aggregators / hubs:** OpenRouter / Perplexity API
- **Target latency:** < 2s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Factuality Rubric & LLM-as-Judge

**Description (what the miner must answer):**

> Answers open-domain and context-bounded user queries with cited factual assertions and logical deductions.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners generate reasoning paths evaluated against authoritative ground truth documents via LLM judge.

</details>

---

---

### <span style="color:#b71c1c">`RAG_GROUNDING_VERIFY`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. not on chain; judgment.

- **Class:** HYBRID
- **Why:** Citation presence is checkable; whether it actually supports the claim is not.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** — · **Verification complexity:** High
- **Data source type:** Vector DB / LLM Evaluator
- **Primary aggregators / hubs:** —
- **Target latency:** < 1.5s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Evaluates retrieval-augmented generation output faithfulness against retrieved document context snippets.

---

---

### `SEMANTIC_SIMILARITY`

- **Class:** DETERMINISTIC
- **Why:** Cosine similarity between specified normalized embedding vectors is an exact calculation.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 7.0 · **Verification complexity:** Low
- **Data source type:** Sentence Transformer Engine
- **Primary aggregators / hubs:** Hugging Face (all-MiniLM-L6-v2) / OpenAI Embeddings
- **Target latency:** < 250ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Numeric Tolerance Comparator

**Description (what the miner must answer):**

> Calculates mathematical cosine similarity and semantic relatedness distance between pairs of sentences.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners generate dense vectors using standard reference models and compute cosine dot-products.

</details>

---

---

### <span style="color:#0b6e4f">`SENTIMENT_ANALYSIS`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 2 miners</span>

- **Lifecycle:** Active — Usman verified 2026-09-30 (promoted from Pre-active). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) archive.

- **Class:** HYBRID
- **Why:** Binary polarity on clear text is objective; nuanced tone and sarcasm require subjective interpretation.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 7.0 · **Verification complexity:** Medium
- **Data source type:** NLP Classifier / Transformer
- **Primary aggregators / hubs:** RoBERTa / Hugging Face Sentiment Pipeline
- **Target latency:** < 300ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Probability Distribution Alignment

**Description (what the miner must answer):**

> Scores emotional valence, polarity (positive/negative/neutral), and subjective tone in textual messages.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners classify input text across diverse pre-trained sentiment models and aggregate probability distributions.

</details>

---

---

### <span style="color:#b71c1c">`SPEECH_TO_TEXT`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. keyed ASR; WER needs a gold transcript.

- **Class:** HYBRID
- **Why:** Acoustic signal has objective phonetic ground truth, but accents and noise introduce ambiguity.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 7.0 · **Verification complexity:** Medium
- **Data source type:** ASR Speech Model
- **Primary aggregators / hubs:** Whisper / AssemblyAI / Deepgram
- **Target latency:** < 4s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Word Error Rate (WER) Comparator

**Description (what the miner must answer):**

> Transcribes spoken audio streams into punctuated, timestamped text transcriptions with speaker diarization.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners execute inference across varied open Whisper checkpoints and compute Word Error Rate (WER).

</details>

---

---

### <span style="color:#b71c1c">`SYNTHETIC_DATA_FIDELITY`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. not on chain; judgment over statistics.

- **Class:** HYBRID
- **Why:** Statistical tests are deterministic; overall fidelity is a judgment over them.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** — · **Verification complexity:** High
- **Data source type:** Statistical Test Engine
- **Primary aggregators / hubs:** —
- **Target latency:** < 10s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Measures statistical distribution alignment and privacy preservation metrics for synthetically generated datasets.

---

---

### `TEXT_CLASSIFICATION`

- **Class:** HYBRID
- **Why:** Clear category matches are mechanical; boundary cases require probabilistic inference.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 7.0 · **Verification complexity:** Medium
- **Data source type:** Text Classification Pipeline
- **Primary aggregators / hubs:** Hugging Face (BART-large-MNLI) / Cohere
- **Target latency:** < 400ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Multi-Engine Voting Consensus

**Description (what the miner must answer):**

> Assigns predefined taxonomic category tags and topic hierarchies to incoming text documents.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners run zero-shot classification pipelines and vote on primary taxonomy label distributions.

</details>

---

---

### <span style="color:#0b6e4f">`TEXT_SUMMARIZATION`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 4 miners</span>

- **Lifecycle:** Active — promoted 2026-10-06 (was Pre-active) — NON-DET campaign 2026-09-29; flipped from Dead. See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md).


- **Class:** NON-DETERMINISTIC
- **Why:** Multiple valid summaries exist; evaluation is inherently comparative and subjective.
- **Scoring path:** adapter only
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 8.0 · **Verification complexity:** High
- **Data source type:** LLM Generative Model
- **Primary aggregators / hubs:** OpenRouter (Claude 3.5 / Llama 3) / Hugging Face
- **Target latency:** < 3s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** LLM-as-Judge & BERTScore

**Description (what the miner must answer):**

> Generates concise, factual executive summaries capturing primary themes of long-form source documents.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners generate summaries using varied foundation LLMs evaluated via ROUGE, BERTScore, and LLM-as-judge.

</details>

---

---

### <span style="color:#0b6e4f">`TEXT_TO_SPEECH`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 2 miners</span>

- **Lifecycle:** Active — promoted 2026-10-06 (was Pre-active) — NON-DET campaign 2026-09-29; flipped from Dead (Google TTS + eSpeak). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md).

- **Class:** NON-DETERMINISTIC
- **Why:** Acoustic realism, prosody, and naturalness are qualitative perceptual judgments.
- **Scoring path:** adapter only
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 6.0 · **Verification complexity:** High
- **Data source type:** Neural TTS Model
- **Primary aggregators / hubs:** ElevenLabs / Kokoro / Coqui TTS
- **Target latency:** < 3s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** MOS / NISQA Perceptual Score

**Description (what the miner must answer):**

> Synthesizes natural-sounding spoken voice waveforms from text input with adjustable emotion and cadence.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners synthesize audio and evaluate perceptual quality using NISQA and MOS neural estimators.

</details>

---

---

### <span style="color:#0b6e4f">`URL_CONTENT_EXTRACTION`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 2 miners</span>

- **Lifecycle:** Active — Usman verified 2026-09-30 (promoted from Pre-active). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) archive.

- **Class:** DETERMINISTIC
- **Why:** HTML DOM parsing and markdown content extraction follow deterministic rules.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 7.0 · **Verification complexity:** Low
- **Data source type:** Headless Browser / Web Scraper
- **Primary aggregators / hubs:** Firecrawl / Jina Reader / Diffbot
- **Target latency:** < 2s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Text Diff & Token Overlap

**Description (what the miner must answer):**

> Scrapes target web pages, cleans boilerplate DOM nodes, and extracts clean markdown article content.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners scrape the destination URL using headless chromium instances and extract core article text.

</details>

---

---

### <span style="color:#0b6e4f">`WEB_SEARCH_QUERY`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 1 miner</span>

- **Lifecycle:** Active — Usman verified 2026-09-30 (promoted from Pre-active). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) archive.

- **Class:** HYBRID
- **Why:** SERP ranking hits are retrievable facts; relevance ordering is algorithmic judgment.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 8.0 · **Verification complexity:** Medium
- **Data source type:** Search Engine Index / SERP API
- **Primary aggregators / hubs:** Brave Search / Serper / Google Custom Search
- **Target latency:** < 800ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Rank Correlation (NDCG / Spearman)

**Description (what the miner must answer):**

> Executes programmatic web search queries and returns top ranked organic URLs, snippets, and knowledge graphs.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners query different search index providers to compute consensus ranking of top results.

</details>

---

---

## Blockchain & Web3

### <span style="color:#0b6e4f">`CROSS_CHAIN_STATE_VERIFY`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 3 miners</span>

- **Lifecycle:** Active — Usman verified 2026-09-30 (promoted from Pre-active). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) archive.
- **Class:** DETERMINISTIC
- **Why:** Light-client proof either verifies or does not.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 10.0 · **Verification complexity:** High
- **Data source type:** Light Client / Relayer Bridge
- **Primary aggregators / hubs:** LayerZero / Wormhole RPCs
- **Target latency:** < 3s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** PassFail on `execution_ok` (1=ok, 0=fail) — **not wired** in Usman comparator yet
- **Pre-active miners:** `xchain-axelar-gmp` (2846), `xchain-wormhole-vaa` (2847), `xchain-across-deposit` (2848)

**Description (what the miner must answer):**

> Proves cryptographic Merkle-Patricia state roots and cross-chain message execution headers between distinct blockchain networks.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners independently verify state roots by querying different cross-chain relayer nodes.

</details>

---

---

### `CRYPTO_PRICE_LOOKUP`

- **Class:** DETERMINISTIC
- **Why:** Aggregated volume-weighted average price across major exchange spot pairs.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 7.0 · **Verification complexity:** Low
- **Data source type:** CEX/DEX Spot Aggregator
- **Primary aggregators / hubs:** CoinGecko / CoinMarketCap / Binance
- **Target latency:** < 400ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Numeric Tolerance Comparator

**Description (what the miner must answer):**

> Fetches real-time spot and volume-weighted average prices for crypto assets across major exchanges.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners fetch spot trades across independent centralized and decentralized exchange orderbooks.

</details>

---

---

### `CRYPTO_TRANSFER_VERIFY`

- **Class:** DETERMINISTIC
- **Why:** Transaction inclusion and confirmation count are verified directly on-chain.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 7.0 · **Verification complexity:** Medium
- **Data source type:** Blockchain RPC Node
- **Primary aggregators / hubs:** Etherscan / Alchemy / QuickNode
- **Target latency:** < 1.5s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Exact Match Comparator

**Description (what the miner must answer):**

> Verifies on-chain transaction status, gas fee burn, sender/recipient addresses, and block confirmations.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners query diverse archive RPC nodes to cross-verify transaction receipt status and events.

</details>

---

---

### <span style="color:#0b6e4f">`CRYPTO_YIELD_RATE`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 7 miners</span>

- **Lifecycle:** Active 2026-09-29 — YAML quote + compound on-chain · regs **4356–4361** + **4375** · shared `pool` pin · not wired yet. See [`workingMiners.md`](./workingMiners.md).
- **Class:** DETERMINISTIC
- **Why:** Calculated from smart contract liquidity pools and staking emission contracts.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 6.0 · **Verification complexity:** Medium
- **Data source type:** DeFi Yield Aggregator
- **Primary aggregators / hubs:** DefiLlama / Yearn Finance / Compound
- **Target latency:** < 1.2s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Numeric Tolerance Comparator

**Description (what the miner must answer):**

> Tracks annualized percentage yields (APY), staking reward rates, and lending pool yields across DeFi protocols.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners query smart contract liquidity pools directly to calculate instantaneous lending APY.

</details>

---

---

### <span style="color:#0b6e4f">`EVENT_OUTCOME_RESOLUTION`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 3 miners</span>

- **Lifecycle:** Active 2026-09-29 — Kalshi re-pinned **4364** · 3/3 working · not wired yet. See [`workingMiners.md`](./workingMiners.md).
- **Class:** HYBRID
- **Why:** Settled outcome is checkable; pre-settlement resolution of ambiguous/disputed events is judgment.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 10.0 · **Verification complexity:** High
- **Data source type:** Multi-Oracle Consensus Feed
- **Primary aggregators / hubs:** Polymarket API / NewsAPI
- **Target latency:** < 5s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Resolves objective real-world event outcomes for prediction markets and conditional contracts using quorum oracles.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners scrape consensus from 10+ independent news outlets, sports APIs, or flight statuses.

</details>

---

---

### <span style="color:#0b6e4f">`GAS_PRICE_ESTIMATION`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 2 miners</span>

- **Lifecycle:** Active — Usman verified 2026-09-30 (promoted from Pre-active). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) archive.

- **Class:** DETERMINISTIC
- **Why:** Pending mempool base fee and priority fee percentiles are observable metrics.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 6.0 · **Verification complexity:** Low
- **Data source type:** Mempool / Gas Oracle
- **Primary aggregators / hubs:** Blocknative / Etherscan Gas Tracker
- **Target latency:** < 500ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Numeric Tolerance Comparator

**Description (what the miner must answer):**

> Estimates dynamic base fee, tip priority, and gas limits across standard transaction speed tiers.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners sample local node mempools to compute standard 25th/50th/75th percentile gas prices.

</details>

---

---

### <span style="color:#b71c1c">`SMART_CONTRACT_AUDIT`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. no analyzer API; Sourcify is_verified is a different quantity.

- **Class:** HYBRID
- **Why:** Automated vulnerability patterns are mechanical; business logic flaws require semantic analysis.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 7.0 · **Verification complexity:** High
- **Data source type:** Static Analysis / Symbolic Execution
- **Primary aggregators / hubs:** Slither / Mythril / OpenZeppelin Defender
- **Target latency:** < 8s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Multi-Engine Heuristic Scoring

**Description (what the miner must answer):**

> Inspects bytecode and smart contract source code for reentrancy, access control, and integer overflows.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners run distinct open-source static analyzers and automated formal verification suites.

</details>

---

---

### <span style="color:#0b6e4f">`TOKEN_TOTAL_SUPPLY_VERIFY`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 2 miners</span>

- **Lifecycle:** Active — Usman verified 2026-09-30 (promoted from Pre-active). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) archive.

- **Class:** DETERMINISTIC
- **Why:** Calling totalSupply() on an ERC-20/SPL contract returns an exact integer.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 6.0 · **Verification complexity:** Low
- **Data source type:** Blockchain RPC Node
- **Primary aggregators / hubs:** Etherscan / Solscan / Alchemy
- **Target latency:** < 500ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Exact Match Comparator

**Description (what the miner must answer):**

> Verifies token circulating supply, burnt token balances, and total minted token counts on-chain.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners execute eth_call view functions against token contracts via independent archive nodes.

</details>

---

---

### <span style="color:#0b6e4f">`VALIDATOR_PERFORMANCE_VERIFY`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 2 miners</span>

- **Lifecycle:** Active — Usman verified 2026-09-30 (promoted from Pre-active). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) archive.

- **Class:** DETERMINISTIC
- **Why:** Uptime and attestation rates from consensus telemetry.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 6.0 · **Verification complexity:** Medium
- **Data source type:** Consensus Node Telemetry
- **Primary aggregators / hubs:** Beaconcha.in / Rated.network
- **Target latency:** < 1.5s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Tracks consensus voting uptime, proposed block rates, slashing penalties, and staking APR for network validators.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners query independent consensus layer block explorers to calculate uptime.

</details>

---

---

### `WASH_TRADING_DETECTION`

- **Class:** HYBRID
- **Why:** Circular-flow and address-identity checks are mechanical; intent to wash is inferred.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 10.0 · **Verification complexity:** High
- **Data source type:** On-Chain Graph Analytics
- **Primary aggregators / hubs:** DexScreener / Bitquery / Dune
- **Target latency:** < 4s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Analyzes DEX transaction graphs and circular transfer loops between affiliated wallets to identify artificial trade volume.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners run distinct graph-analysis heuristics across different indexed subgraphs.

</details>

---

---

## Climate & Weather

### <span style="color:#0b6e4f">`AIR_QUALITY_INDEX`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 7 miners</span>

- **Lifecycle:** Active — Usman verified 2026-09-30 (promoted from Pre-active). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) archive.

- **Class:** DETERMINISTIC
- **Why:** Sensor measurements of PM2.5, PM10, and ozone concentrations.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 6.0 · **Verification complexity:** Low
- **Data source type:** Environmental Sensor Network
- **Primary aggregators / hubs:** OpenAQ / WAQI / EPA AirNow
- **Target latency:** < 800ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Numeric Tolerance Comparator

**Description (what the miner must answer):**

> Aggregates particulate matter (PM2.5/PM10), ground ozone, and composite AQI metrics from monitoring stations.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners cross-reference municipal air monitoring station telemetry and calibrated sensor APIs.

</details>

---

---

### <span style="color:#b71c1c">`CARBON_OFFSET_RETIREMENT`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. not on chain.

- **Class:** DETERMINISTIC
- **Why:** Retirement record exists in the registry.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** — · **Verification complexity:** Medium
- **Data source type:** Environmental Registry
- **Primary aggregators / hubs:** —
- **Target latency:** < 2.5s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Verifies the serial number retirement and non-double-spending of voluntary carbon credits on registries.

---

---

### <span style="color:#b71c1c">`FLOOD_EXTENT_MAPPING`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. not on chain; no scalar.

- **Class:** HYBRID
- **Why:** SAR inundation signal is measured; extent boundary is modelled.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** — · **Verification complexity:** High
- **Data source type:** SAR Satellite Inundation
- **Primary aggregators / hubs:** —
- **Target latency:** < 8s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Maps hydro-dynamic surface water accumulation and flood inundation zones from synthetic aperture radar data.

---

---

### <span style="color:#0b6e4f">`WEATHER_CURRENT`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 4 miners</span>

- **Class:** DETERMINISTIC
- **Why:** Physical weather station observations at time and geo-coordinates.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 6.0 · **Verification complexity:** Low
- **Data source type:** Surface Weather Observation
- **Primary aggregators / hubs:** Open-Meteo / NOAA / Tomorrow.io
- **Target latency:** < 600ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Numeric Tolerance Comparator

**Description (what the miner must answer):**

> Provides real-time ambient temperature, humidity, precipitation rate, and wind vectors by coordinates.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners fetch readings from nearby certified METAR airport stations and national weather networks.

</details>

---

---

### <span style="color:#0b6e4f">`WEATHER_FORECAST_VERIFY`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 5 miners</span>

- **Lifecycle:** Active — Usman verified 2026-09-30 (promoted from Pre-active). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) archive.

- **Class:** DETERMINISTIC
- **Why:** Forecast compared against subsequent observation.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 5.0 · **Verification complexity:** Low
- **Data source type:** Meteorological Bureau API
- **Primary aggregators / hubs:** Open-Meteo / NOAA / Tomorrow.io
- **Target latency:** < 1s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Reconciles localized Doppler radar feeds, barometric pressure, wind gusts, and severe weather alert bulletins.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Open-Meteo aggregates 15+ weather models (GFS, ECMWF, HRRR); miners query different underlying models.

</details>

---

---

## Commerce & Procurement

### `COMMERCE_PURCHASE_VERIFY`

- **Class:** DETERMINISTIC
- **Why:** Order exists in the merchant API or it does not.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 10.0 · **Verification complexity:** Medium
- **Data source type:** Merchant API
- **Primary aggregators / hubs:** Stripe Sandbox / RapidAPI
- **Target latency:** < 1s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Verifies the authenticity, item line totals, and payment authorization for a completed e-commerce purchase transaction.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners verify simulated or standard cryptographic receipt hashes against payment webhook schemas.

</details>

---

---

### <span style="color:#b71c1c">`PURCHASE_ORDER_VERIFY`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. demo ERPs closed; award registries are a different quantity.

- **Class:** DETERMINISTIC
- **Why:** PO fields match the ERP record.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 7.0 · **Verification complexity:** Medium
- **Data source type:** ERP System
- **Primary aggregators / hubs:** Odoo / ERPNext REST APIs
- **Target latency:** < 2s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Reconciles enterprise purchase orders with procurement approval workflows, vendor quotas, and budget allocations.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners use open-source ERP mock endpoints to execute deterministic 3-way matching.

</details>

---

---

### `SKU_IN_STOCK`

- **Class:** DETERMINISTIC
- **Why:** Boolean from an inventory system.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 10.0 · **Verification complexity:** Low
- **Data source type:** Inventory DB / API
- **Primary aggregators / hubs:** RapidAPI (Retail) / Rainforest API
- **Target latency:** < 500ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Confirms real-time stock availability, quantities, and warehouse fulfillment readiness for a given SKU.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners use different proxy networks and inventory APIs to confirm stock booleans.

</details>

---

---

### <span style="color:#0b6e4f">`VENDOR_VERIFY`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 4 miners</span>

- **Lifecycle:** Active — Usman verified 2026-09-30 (promoted from Pre-active). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) archive.

- **Class:** HYBRID
- **Why:** Registration status is a lookup; vendor risk is an assessment.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 7.0 · **Verification complexity:** High
- **Data source type:** Compliance Registry
- **Primary aggregators / hubs:** OpenSanctions / RapidAPI
- **Target latency:** < 3s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Audits vendor tax identifiers, compliance credentials, banking details, and sanctions list clearance.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners check tax identifiers and sanctions lists using distinct firmographic API endpoints.

</details>

---

---

## Cybersecurity

### <span style="color:#0b6e4f">`DNS_RECORD_LOOKUP`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 7 miners</span>

- **Lifecycle:** Active — Usman verified 2026-09-30 (promoted from Pre-active). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) archive.

- **Class:** DETERMINISTIC
- **Why:** Authoritative nameserver response for requested record type.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 6.0 · **Verification complexity:** Low
- **Data source type:** Authoritative DNS Resolver
- **Primary aggregators / hubs:** Cloudflare 1.1.1.1 / Google DNS / Quad9
- **Target latency:** < 200ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Exact Match Comparator

**Description (what the miner must answer):**

> Resolves and validates authoritative DNS records (A, AAAA, CNAME, MX, TXT) across global resolvers.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners query authoritative and anycast DNS resolvers to verify propagation and record parity.

</details>

---

---

### <span style="color:#0b6e4f">`PORT_SCAN_AUDIT`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 2 miners</span>

- **Lifecycle:** Active — Usman verified 2026-09-30 (promoted from Pre-active). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) archive.

- **Class:** DETERMINISTIC
- **Why:** TCP SYN/ACK handshake state or open UDP response is observable network truth.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 6.0 · **Verification complexity:** Medium
- **Data source type:** Network Port Scanner / Telemetry
- **Primary aggregators / hubs:** Shodan / Censys / Nmap API
- **Target latency:** < 2s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Exact Match Comparator

**Description (what the miner must answer):**

> Identifies open network service ports, banner disclosures, and listening daemon protocols on specified hosts.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners scan target endpoints using controlled SYN probes to confirm listening service ports.

</details>

---

---

### <span style="color:#0b6e4f">`SSL_CERTIFICATE_VERIFY`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 2 miners</span>

- **Lifecycle:** Active — Usman verified 2026-09-30 (promoted from Pre-active). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) archive.

- **Class:** DETERMINISTIC
- **Why:** X.509 certificate chain, expiration, and CRL/OCSP status are cryptographically verified.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 6.0 · **Verification complexity:** Low
- **Data source type:** PKI / Certificate Transparency
- **Primary aggregators / hubs:** Crt.sh / SSL Labs API / Let's Encrypt
- **Target latency:** < 500ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Deterministic Rule Validator

**Description (what the miner must answer):**

> Validates TLS/SSL certificate chains, cipher suites, expiration dates, and revocation statuses.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners initiate TLS handshakes directly and query public Certificate Transparency logs.

</details>

---

---

### <span style="color:#0b6e4f">`THREAT_INTELLIGENCE`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 3 miners</span>

- **Lifecycle:** Active — Usman verified 2026-09-30 (promoted from Pre-active). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) archive.

- **Class:** HYBRID
- **Why:** Feed aggregation is mechanical; relevance and severity are assessed.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 7.0 · **Verification complexity:** Medium
- **Data source type:** SIEM / Threat Intel Feed
- **Primary aggregators / hubs:** AbuseIPDB / AlienVault OTX
- **Target latency:** < 1s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Aggregates indicators of compromise (IOCs), malicious IP ranges, and adversary tactics from global security feeds.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners query different open-source threat intelligence platforms (OSINT) for IOC scores.

</details>

---

---

### <span style="color:#0b6e4f">`THREAT_IP_REPUTATION`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 6 miners</span>

- **Class:** HYBRID
- **Why:** Blocklist presence is a deterministic lookup; composite confidence score is an inference.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 7.0 · **Verification complexity:** Medium
- **Data source type:** Threat Intelligence Engine
- **Primary aggregators / hubs:** AbuseIPDB / AlienVault OTX / GreyNoise
- **Target latency:** < 400ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Consensus Scoring Comparator

**Description (what the miner must answer):**

> Assesses malicious IP address risk scores, botnet associations, and brute-force history across threat registries.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners query diverse global IP threat feeds and aggregate historical abuse report counts.

</details>

---

---

## Energy & Infrastructure

### <span style="color:#0b6e4f">`CLOUD_RESOURCE_USAGE`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 2 miners</span>

- **Lifecycle:** Active — Usman verified 2026-09-30 (promoted from Pre-active). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) archive.

- **Class:** DETERMINISTIC
- **Why:** CPU, memory, and network telemetry counters exported by hypervisor metrics.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 5.0 · **Verification complexity:** Medium
- **Data source type:** Cloud Telemetry Gateway
- **Primary aggregators / hubs:** Prometheus / AWS CloudWatch / Datadog
- **Target latency:** < 1s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Numeric Tolerance Comparator

**Description (what the miner must answer):**

> Audits virtual machine and container compute utilization, memory pressure, and network throughput metrics.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners query open Prometheus exporter metrics to verify real-time hardware telemetry.

</details>

---

---

## Enterprise Operations

### <span style="color:#b71c1c">`ACCESS_PRIVILEGE_DRIFT_AUDIT`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. not on chain; private IAM data.

- **Class:** HYBRID
- **Why:** Diff against policy is mechanical; which drift matters is judgment.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** — · **Verification complexity:** High
- **Data source type:** IAM Directory / SIEM
- **Primary aggregators / hubs:** —
- **Target latency:** < 4s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Discovers unapproved privilege escalations, dormant service accounts, and entitlement drift across cloud IAM.

---

---

### <span style="color:#0b6e4f">`API_HEALTH_CHECK`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 2 miners</span>

- **Lifecycle:** Active — Usman verified 2026-09-30 (promoted from Pre-active). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) archive.

- **Class:** DETERMINISTIC
- **Why:** Service payload validation and response code comparison against OpenAPI specification.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 6.0 · **Verification complexity:** Low
- **Data source type:** API Monitoring Suite
- **Primary aggregators / hubs:** Postman / Datadog / Runscope
- **Target latency:** < 400ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** JSON Schema Validator

**Description (what the miner must answer):**

> Verifies REST/GraphQL API responsiveness, JSON schema payload structure, and HTTP status codes.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners execute automated schema conformance checks against public health endpoints.

</details>

---

---

### `CONTRACT_OBLIGATION_AUDIT`

- **Class:** NON-DETERMINISTIC
- **Why:** Extracting obligations from prose; competent lawyers disagree on scope.
- **Scoring path:** adapter only
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 8.0 · **Verification complexity:** High
- **Data source type:** CLM / NLP Parser
- **Primary aggregators / hubs:** OpenRouter (Claude / DeepSeek)
- **Target latency:** < 4s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Parses and verifies legal contract milestone deliverables, payment terms, and vendor performance commitments.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

10 miners use 10 different LLMs to extract milestone JSON schemas from legal text.

</details>

---

---

### <span style="color:#b71c1c">`CUSTOMER_TICKET_RESOLUTION`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. Gate 0 adapter-only.

- **Class:** NON-DETERMINISTIC
- **Why:** Resolution accuracy and CSAT reasoning are comparative.
- **Scoring path:** adapter only
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 6.0 · **Verification complexity:** Medium
- **Data source type:** CRM / Ticketing API
- **Primary aggregators / hubs:** Zendesk / Freshdesk Sandboxes
- **Target latency:** < 1.5s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Analyzes helpdesk support interactions, resolution accuracy, agent action compliance, and customer satisfaction outcomes.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners use different semantic evaluation LLMs to score ticket resolution accuracy.

</details>

---

---

### <span style="color:#0b6e4f">`SERVER_UPTIME_MONITOR`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 2 miners</span>

- **Lifecycle:** Active — Usman verified 2026-09-30 (promoted from Pre-active). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) archive.

- **Class:** DETERMINISTIC
- **Why:** HTTP response code and TCP latency from synthetic edge probes.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 6.0 · **Verification complexity:** Low
- **Data source type:** Synthetic APM Probe
- **Primary aggregators / hubs:** BetterStack / UptimeRobot / Pingdom
- **Target latency:** < 600ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Exact Match Comparator

**Description (what the miner must answer):**

> Monitors synthetic HTTP/HTTPS endpoint availability, handshake latency, and uptime status from multiple edge regions.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners execute concurrent HTTP GET requests from geo-distributed locations to confirm availability.

</details>

---

---

## Financial / Transactional

### <span style="color:#b71c1c">`COLLATERAL_HAIRCUT_VALUATION`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. not on chain; judgment model.

- **Class:** HYBRID
- **Why:** Market inputs are observable; the haircut model is a judgment call.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** — · **Verification complexity:** Medium
- **Data source type:** Margin Engine / Market Feeds
- **Primary aggregators / hubs:** —
- **Target latency:** < 350ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Calculates mark-to-market valuations and risk haircuts for pledged securities and digital collateral.

---

---

### `CREDIT_SCORE_VERIFY`

- **Class:** HYBRID
- **Why:** Bureau numerical score is a lookup; credit risk tiering involves underwriting criteria.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 7.0 · **Verification complexity:** Medium
- **Data source type:** Credit Bureau Gateway
- **Primary aggregators / hubs:** Experian / Equifax API Sandboxes
- **Target latency:** < 800ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Scored Range Comparator

**Description (what the miner must answer):**

> Validates consumer credit bureau score ranges, adverse factors, and debt-to-income benchmarks.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners cross-reference simulated credit bureau score bands across test scoring engines.

</details>

---

---

### <span style="color:#b71c1c">`CROSS_BORDER_REMITTANCE_STATUS`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. not on chain; SWIFT gpi is authenticated.

- **Class:** DETERMINISTIC
- **Why:** SWIFT GPI returns a status code.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** — · **Verification complexity:** Medium
- **Data source type:** SWIFT GPI / Banking Gateway
- **Primary aggregators / hubs:** —
- **Target latency:** < 1s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Tracks real-time settlement rails, intermediary SWIFT messaging, and local payout statuses for cross-border wires.

---

---

### `CURRENCY_EXCHANGE`

- **Class:** DETERMINISTIC
- **Why:** Spot exchange rate at timestamp within numeric tolerance band.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 7.0 · **Verification complexity:** Low
- **Data source type:** FX Liquidity Feed
- **Primary aggregators / hubs:** OANDA / XE.com / Frankfurter
- **Target latency:** < 250ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Numeric Tolerance Comparator

**Description (what the miner must answer):**

> Calculates fiat currency conversion rates and mid-market spot pricing across global currency pairs.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners query distinct institutional FX liquidity providers and calculate median mid-market rate.

</details>

---

---

### `FRAUD_RISK`

- **Class:** NON-DETERMINISTIC
- **Why:** A risk score with no ground truth at query time; the label only arrives later.
- **Scoring path:** adapter only
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 9.0 · **Verification complexity:** High
- **Data source type:** Risk Engine / ML Model
- **Primary aggregators / hubs:** IPQualityScore / MaxMind MinFraud
- **Target latency:** < 350ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Computes real-time behavioral fraud probability scores using device fingerprinting, IP geolocation, and transaction context.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners use different risk-engine APIs to evaluate IP geolocation and device fingerprinting.

</details>

---

---

### <span style="color:#0b6e4f">`LOAN_INTEREST_RATE_QUOTE`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 6 miners</span>

- **Lifecycle:** Active — Usman verified 2026-09-30 (promoted from Pre-active). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) archive.

- **Class:** DETERMINISTIC
- **Why:** Published benchmark APRs from institutional lending matrices.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 6.0 · **Verification complexity:** Low
- **Data source type:** Lending Rate Aggregator
- **Primary aggregators / hubs:** Bankrate / FRED / LendingTree
- **Target latency:** < 1s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Numeric Tolerance Comparator

**Description (what the miner must answer):**

> Aggregates residential mortgage APRs, prime lending rates, and personal loan interest quotes.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners scrape and parse published APR tables across licensed retail and commercial lenders.

</details>

---

---

### `OPTIMAL_EXECUTION_ROUTE`

- **Class:** HYBRID
- **Why:** Executed price is checkable; 'optimal' depends on an objective the request may not fix.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 10.0 · **Verification complexity:** High
- **Data source type:** Smart Order Router
- **Primary aggregators / hubs:** 1inch / 0x / ParaSwap
- **Target latency:** < 150ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Determines optimal multi-venue order execution routing to minimize slippage, exchange fees, and market impact.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners query different DEX aggregators and private RPCs for the best routing path.

</details>

---

---

### `PAYMENT_METHOD_VERIFY`

- **Class:** DETERMINISTIC
- **Why:** Bank switch returns a definitive validity response.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 9.0 · **Verification complexity:** Medium
- **Data source type:** Banking Switch / ACH API
- **Primary aggregators / hubs:** BinCodes / Plaid / RapidAPI
- **Target latency:** < 600ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Verifies card BIN validity, tokenization credentials, bank account routing, and active account standing.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners query distinct global BIN/IIN databases to check card token validity and bank routing.

</details>

---

---

### <span style="color:#0b6e4f">`STOCK_PRICE_QUOTE`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 3 miners</span>

- **Class:** DETERMINISTIC
- **Why:** NBBO consolidated tape quote at specific execution timestamp.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 7.0 · **Verification complexity:** Low
- **Data source type:** Equity Market Data Feed
- **Primary aggregators / hubs:** Polygon.io / Alpha Vantage / IEX Cloud
- **Target latency:** < 350ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Numeric Tolerance Comparator

**Description (what the miner must answer):**

> Retrieves live and official market-close equity quotes, bid-ask spreads, and trading volume.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners query distinct market data feeds and verify against consolidated equity exchange tapes.

</details>

---

---

### `TRANSACTION_RISK`

- **Class:** NON-DETERMINISTIC
- **Why:** Same shape as FRAUD_RISK: a forward-looking score.
- **Scoring path:** adapter only
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 9.0 · **Verification complexity:** High
- **Data source type:** Payment Gateway Telemetry
- **Primary aggregators / hubs:** Stripe Radar Sandbox / Sift Science
- **Target latency:** < 250ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Evaluates cardholder spending velocity, merchant categorization codes, and chargeback history to score transaction risk.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners query different payment risk evaluation endpoints for chargeback probability scores.

</details>

---

---

## Geospatial & Remote Sensing

### <span style="color:#b71c1c">`DEFORESTATION_SURVEILLANCE`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. not on chain; Global Forest Watch is keyed.

- **Class:** HYBRID
- **Why:** Radar change detection is measurable; attribution to deforestation is inferred.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** — · **Verification complexity:** High
- **Data source type:** SAR / Multispectral Radar
- **Primary aggregators / hubs:** —
- **Target latency:** < 15s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Evaluates canopy loss anomalies and unauthorized road clearings within protected forest conservation zones.

---

---

### <span style="color:#b71c1c">`METHANE_EMISSION_DETECTION`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. not on chain; inference over imagery.

- **Class:** HYBRID
- **Why:** Spectral signature is measured; plume attribution and rate are inferred.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** — · **Verification complexity:** High
- **Data source type:** Hyperspectral Satellite Feed
- **Primary aggregators / hubs:** —
- **Target latency:** < 20s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Quantifies point-source industrial methane plumes and flaring leakage using high-resolution spectral imagery.

---

---

### <span style="color:#b71c1c">`WILDFIRE_PERIMETER_MONITOR`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. not on chain; NASA FIRMS needs a key; perimeter is modelled.

- **Class:** HYBRID
- **Why:** Thermal anomalies are measured; perimeter delineation is a modelled boundary.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** — · **Verification complexity:** High
- **Data source type:** Thermal Satellite Sensor
- **Primary aggregators / hubs:** —
- **Target latency:** < 5s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Tracks infrared thermal anomalies and active fire perimeter expansion boundaries from geostationary orbit.

---

---

## IoT & Telemetry

### <span style="color:#b71c1c">`COLD_CHAIN_TEMPERATURE_BREACH`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. not on chain; private logger data.

- **Class:** DETERMINISTIC
- **Why:** Logged temperature against a threshold.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** — · **Verification complexity:** Low
- **Data source type:** IoT Temperature Logger
- **Primary aggregators / hubs:** —
- **Target latency:** < 300ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Detects excursions above critical pharmaceutical or perishables refrigeration thresholds in transit.

---

---

### <span style="color:#0b6e4f">`SENSOR_TELEMETRY_VERIFY`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 5 miners</span>

- **Lifecycle:** Active — Usman verified 2026-09-30 (promoted from Pre-active). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) archive.

- **Class:** DETERMINISTIC
- **Why:** MQTT broker readings.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 5.0 · **Verification complexity:** Medium
- **Data source type:** MQTT / IoT Telemetry Broker
- **Primary aggregators / hubs:** ThingsBoard / Public MQTT
- **Target latency:** < 400ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Validates edge sensor heartbeat signals, cryptographic payload integrity, and calibration threshold bounds.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners subscribe to distinct IoT broker endpoints and evaluate payload HMAC signatures.

</details>

---

---

### <span style="color:#b71c1c">`SMART_METER_TAMPER_DETECT`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. not on chain; private utility data.

- **Class:** HYBRID
- **Why:** Threshold breaches are mechanical; tamper vs fault is judgment.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** — · **Verification complexity:** Medium
- **Data source type:** AMI Smart Grid Headend
- **Primary aggregators / hubs:** —
- **Target latency:** < 800ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Identifies power bypass, magnetic interference, or meter enclosure breaches across utility distribution grids.

---

---

## Legal & Compliance

### `CORPORATE_REGISTRY_LOOKUP`

- **Class:** DETERMINISTIC
- **Why:** Registry record fields.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 8.0 · **Verification complexity:** Medium
- **Data source type:** Government Chamber API
- **Primary aggregators / hubs:** OpenCorporates / RapidAPI
- **Target latency:** < 2.5s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Queries national business registers for incorporation status, registered agent details, and beneficial ownership filings.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

OpenCorporates aggregates 140+ global registries; miners query different jurisdictions.

</details>

---

---

### <span style="color:#b71c1c">`EXPORT_CONTROL_CLASSIFICATION`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. not on chain; interpretive.

- **Class:** HYBRID
- **Why:** The ECCN matrix is rule-based; applying it to a novel product is interpretive.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** — · **Verification complexity:** High
- **Data source type:** Trade Compliance Matrix
- **Primary aggregators / hubs:** —
- **Target latency:** < 1.5s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Reconciles harmonized tariff codes and dual-use technological specifications against export regulations.

---

---

### <span style="color:#b71c1c">`GDPR_DATA_ERASURE_AUDIT`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. not on chain; private ledgers.

- **Class:** HYBRID
- **Why:** Ledger entries are checkable; sufficiency of erasure is judgment.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** — · **Verification complexity:** Medium
- **Data source type:** Storage Ledger Audit Log
- **Primary aggregators / hubs:** —
- **Target latency:** < 3s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Audits and confirms cryptographic deletion proofs for user data removal requests across distributed storage.

---

---

### `REGULATORY_FILING_MONITOR`

- **Class:** DETERMINISTIC
- **Why:** A filing appeared on EDGAR or it did not.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 8.0 · **Verification complexity:** Medium
- **Data source type:** Regulatory EDGAR / RSS Feed
- **Primary aggregators / hubs:** SEC EDGAR / HKEX News
- **Target latency:** < 3s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Parses statutory regulatory filings, 10-K/10-Q disclosures, and disclosure updates from financial oversight portals.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners scrape different official financial oversight RSS feeds and registry APIs.

</details>

---

---

### `SANCTIONS_SCREENING_MATCH`

- **Class:** HYBRID
- **Why:** Exact list hits are mechanical; fuzzy name matching is judgment.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 9.0 · **Verification complexity:** Medium
- **Data source type:** Watchlist Engine
- **Primary aggregators / hubs:** OpenSanctions / OFAC SDN API
- **Target latency:** < 500ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Screens counterparties and beneficial owners against OFAC, EU, and UN consolidated financial sanctions lists.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners use different matching algorithms (Levenshtein, Jaro-Winkler) against the OpenSanctions DB.

</details>

---

---

## Logistics

### <span style="color:#0b6e4f">`CARRIER_SERVICEABILITY`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 2 miners</span>

- **Lifecycle:** Active — Usman verified 2026-09-30 (promoted from Pre-active). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) archive.

- **Class:** DETERMINISTIC
- **Why:** Lane serviceable or not, from the routing matrix.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 5.0 · **Verification complexity:** Low
- **Data source type:** Carrier Routing Matrix
- **Primary aggregators / hubs:** EasyPost / Shippo / Route4Me
- **Target latency:** < 600ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Evaluates freight and courier delivery coverage, weight limits, and hazardous material restrictions for target routes.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners query distinct courier rating matrices to confirm hazardous material and weight limits.

</details>

---

---

### <span style="color:#b71c1c">`SHIPMENT_DELAY_RISK`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. Gate 0 adapter-only.

- **Class:** NON-DETERMINISTIC
- **Why:** Forward-looking risk over weather, congestion and customs; truth arrives later.
- **Scoring path:** adapter only
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 5.0 · **Verification complexity:** High
- **Data source type:** Predictive Logistics Engine
- **Primary aggregators / hubs:** Project44 / FourKites / RapidAPI
- **Target latency:** < 2s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Assesses predictive delay risk based on customs processing times, port congestion, weather conditions, and transport nodes.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners use distinct risk models to weigh port congestion against weather delay factors.

</details>

---

---

## Logistics & Maritime

### <span style="color:#0b6e4f">`VESSEL_TELEMETRY_VERIFY`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 1 miner</span>

- **Lifecycle:** Active 2026-09-29 — re-pinned `230981000` + AIS fallbacks · reg **4365** · single-source · not wired yet. See [`workingMiners.md`](./workingMiners.md).

- **Class:** DETERMINISTIC
- **Why:** AIS position and heading.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 5.0 · **Verification complexity:** Medium
- **Data source type:** Satellite AIS Feed
- **Primary aggregators / hubs:** Spire / OpenSky / AISHub
- **Target latency:** < 1.5s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Ingests maritime AIS positioning transponder data to track vessel speed, draft, bunker fuel burn, and nautical headings.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners query diverse crowdsourced AIS aggregator hubs for ship coordinates and draft.

</details>

---

---

## Software / Engineering

### `CODE_GENERATION`

- **Class:** HYBRID
- **Why:** Syntax compilation and unit tests are deterministic; stylistic elegance and architecture are judgment.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 8.0 · **Verification complexity:** High
- **Data source type:** Code LLM / Sandboxed Runner
- **Primary aggregators / hubs:** Judge0 / OpenRouter (Claude 3.5 Sonnet / Qwen Coder)
- **Target latency:** < 4s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Unit Test Pass Rate + LLM Review

**Description (what the miner must answer):**

> Generates executable, type-safe code snippets and algorithms meeting specified functional specifications.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners generate candidate code implementations that are executed in sandboxes against automated unit test suites.

</details>

---

---

### <span style="color:#0b6e4f">`CODE_PATCH_VERIFY`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 3 miners</span>

- **Lifecycle:** Active — Usman verified 2026-09-30 (promoted from Pre-active). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) archive.
- **Class:** DETERMINISTIC
- **Why:** Build and test suite pass or fail.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 10.0 · **Verification complexity:** High
- **Data source type:** CI/CD Pipeline API
- **Primary aggregators / hubs:** Judge0 API / GitHub Actions
- **Target latency:** < 10s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** PassFail on `exit_status` (0=pass, 1=fail) — **not wired** in Usman comparator yet
- **Pre-active miners:** `patch-judge0-ce` (2843), `patch-wandbox` (2844), `patch-godbolt` (2845)

**Description (what the miner must answer):**

> Validates that software patch commits compile, resolve targeted defects, and introduce no regression side effects.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners run the patch in isolated sandbox environments (Judge0, JDoodle) to verify zero exit status.

</details>

---

---

### <span style="color:#b71c1c">`CODE_REVIEW`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — hunt found **no** description-correct source (NO_JUDGMENT: lookups ≠ review). Do not re-hunt without new evidence.
- **Class:** NON-DETERMINISTIC
- **Why:** No correct review exists; quality is comparative.
- **Scoring path:** adapter only
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 10.0 · **Verification complexity:** High
- **Data source type:** Git VCS / Static Analyzer
- **Primary aggregators / hubs:** OpenRouter (Llama 3 / Qwen)
- **Target latency:** < 5s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Evaluates source code pull requests against internal architectural patterns, maintainability standards, and syntax rules.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

10 miners use 10 different coding models to execute static analysis on the same GitHub PR.

</details>

---

---

### <span style="color:#0b6e4f">`GRAMMAR_SPELL_CHECK`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 2 miners</span>

- **Lifecycle:** Active — Usman verified 2026-09-30 (promoted from Pre-active). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) archive.

- **Class:** DETERMINISTIC
- **Why:** Lexicon lookup and formal syntactic grammatical rules are deterministically verifiable.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 6.0 · **Verification complexity:** Low
- **Data source type:** Linguistic Rule Engine
- **Primary aggregators / hubs:** LanguageTool API / Grammarly Sandbox
- **Target latency:** < 350ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Rule Match Comparator

**Description (what the miner must answer):**

> Detects typographical, orthographic, punctuation, and grammatical syntax errors with correction offsets.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners evaluate text against open-source linguistic rule sets (LanguageTool) to confirm error rule triggers.

</details>

---

---

### <span style="color:#0b6e4f">`REGRESSION_VERIFY`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 1 miner</span>

- **Lifecycle:** Active — Usman verified 2026-09-30 (promoted from Pre-active). See [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md) archive.

- **Class:** DETERMINISTIC
- **Why:** Test runner produces a pass/fail set.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 7.0 · **Verification complexity:** High
- **Data source type:** Automated Test Runner
- **Primary aggregators / hubs:** Playwright / Cypress / RapidAPI
- **Target latency:** < 15s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Runs automated test suite executions to confirm backward compatibility across modified service APIs and libraries.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners execute headless test suites across different cloud CI runners to confirm 100% pass rates.

</details>

---

---

### <span style="color:#b71c1c">`TASK_EXECUTION_QUALITY`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. Gate 0 adapter-only.

- **Class:** NON-DETERMINISTIC
- **Why:** Scored against rubrics; no single correct execution.
- **Scoring path:** adapter only
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 7.0 · **Verification complexity:** Medium
- **Data source type:** Execution Log Telemetry
- **Primary aggregators / hubs:** DeepEval / Promptfoo (Open Source)
- **Target latency:** < 2s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Benchmarks automated job or agent execution outputs against gold-standard rubrics and expected schema constraints.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners use different evaluation models to score agent output against standard rubrics.

</details>

---

---

## Travel & Mobility

### <span style="color:#0b6e4f">`TRAVEL_DISRUPTION`</span> <span style="background:#2e7d32;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">ACTIVE · 1 miner</span>

- **Class:** DETERMINISTIC
- **Why:** Flight status from an FAA/telemetry feed.
- **Scoring path:** comparator only
- **Needs dataset?** No · **Needs adapter?** No
- **Priority:** 10.0 · **Verification complexity:** Medium
- **Data source type:** Flight Telemetry / FAA Feed
- **Primary aggregators / hubs:** FAA NAS Status / FlightRadar24
- **Target latency:** < 1s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Detects and monitors flight delays, cancellations, gate shifts, and weather-driven travel disruptions in real time.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners query independent aviation telemetry endpoints to verify ground stops and delays.

</details>

---

---

## Trust & Safety

### `FACT_CHECKING`

- **Class:** HYBRID
- **Why:** Authoritative database entries provide ground truth; assessing truthfulness of complex claims is judgment.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 8.0 · **Verification complexity:** High
- **Data source type:** Fact Check Knowledge Base
- **Primary aggregators / hubs:** Google Fact Check Tools / Snopes / PolitiFact API
- **Target latency:** < 2.5s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Claim Verification Consensus

**Description (what the miner must answer):**

> Verifies factual claims against authoritative knowledge bases, peer-reviewed registries, and primary sources.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners cross-reference claim claims against structured claim-review schemas and credible web archives.

</details>

---

---

### <span style="color:#b71c1c">`PLAGIARISM_DETECTION`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. paid/keyed only.

- **Class:** HYBRID
- **Why:** N-gram fingerprint matching is mechanical; paraphrasing and attribution legitimacy require judgment.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 7.0 · **Verification complexity:** High
- **Data source type:** Plagiarism Search Engine
- **Primary aggregators / hubs:** Copyleaks / Unicheck / Turnitin Sandboxes
- **Target latency:** < 3s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Shingle Overlap & Similarity Threshold

**Description (what the miner must answer):**

> Detects verbatim text duplication, disguised paraphrasing, and uncredited citations across corpus databases.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners generate shingled min-hash fingerprints and query web index corpora to calculate overlap percentages.

</details>

---

---

### <span style="color:#b71c1c">`SOCIAL_BOT_DETECTION`</span> <span style="background:#c62828;color:#fff;padding:2px 10px;border-radius:4px;font-size:0.85em;font-weight:700">DEAD · 0 miners</span>

- **Lifecycle:** Dead — Fable 2026-09-24 found no keyless source. Gate 0 adapter-only.

- **Class:** NON-DETERMINISTIC
- **Why:** No authoritative bot label exists; it is an inference over behaviour.
- **Scoring path:** adapter only
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 7.0 · **Verification complexity:** High
- **Data source type:** Social Graph API
- **Primary aggregators / hubs:** RapidAPI (Social) / Botometer
- **Target latency:** < 2s · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** —

**Description (what the miner must answer):**

> Classifies social media user accounts by post frequency anomalies, follower graph clusters, and coordinated inauthentic behavior.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners pass target profiles through different heuristic models (follower ratio, burst timing).

</details>

---

---

### `TOXICITY_MODERATION`

- **Class:** HYBRID
- **Why:** Explicit profanity blocklists are mechanical; contextual harassment and hate speech require judgment.
- **Scoring path:** comparator + adapter
- **Needs dataset?** Yes · **Needs adapter?** Yes
- **Priority:** 8.0 · **Verification complexity:** Medium
- **Data source type:** Content Moderation Model
- **Primary aggregators / hubs:** OpenAI Moderation API / Perspective API / Llama Guard
- **Target latency:** < 350ms · **Miners integrated (catalog):** 0.0 · **Ranking supported (catalog):** False
- **Evaluation mechanism:** Multi-Model Safety Consensus

**Description (what the miner must answer):**

> Evaluates user submitted text for hate speech, harassment, sexual content, self-harm incitement, and toxicity.

<details><summary>Catalog “Scale to 10+” (DO NOT use as clone recipe)</summary>

Miners classify text across diverse safety classifiers (Perspective, Llama Guard) and aggregate hazard scores.

</details>

---

---

# Obsolete — `Verifiable = No` (do not build)

| Intent | Class | Why not verifiable |
|--------|-------|--------------------|
| `B2B_IDENTITY_ENRICHMENT` | HYBRID | Firmographic DBs (Apollo/Clearbit/ZoomInfo) are proprietary and disagree for the same company; no canonical public truth to converge on. |
| `DATACENTER_TELEMETRY_VERIFY` | DETERMINISTIC | PUE/thermal readings come from a private building BMS (catalog itself specifies “simulated” endpoints); not publicly reproducible. |
| `DELIVERY_WINDOW_VERIFY` | DETERMINISTIC | Committed delivery windows live only in a private dispatch system; not independently reproducible by a validator/other miners. |
| `DOCUMENT_AUTHENTICITY` | HYBRID | Signature validity is a locally-computed cryptographic verification (doc+signature+public key), not a fetchable HTTP value; verifiable in principle but the fetch-based host mechanism cannot express it. |
| `FARE_RULE_VERIFY` | HYBRID | Fares/fare-rules are GDS-session-specific and change per query; two validators never obtain the same answer for the same ticket. |
| `FLIGHT_AVAILABILITY` | DETERMINISTIC | GDS fare-class seat inventory is private/keyed; the only keyless signal (OpenSky “airborne”) is a proxy, not the fact. |
| `HOTEL_AVAILABILITY` | DETERMINISTIC | Private OTA/PMS inventory and no keyless public source exists at all; cannot be independently reproduced. |
| `INVOICE_LEDGER_RECONCILE` | HYBRID | The 3-way match is against a private company ERP ledger (Xero/QuickBooks); no public replica for a validator to reproduce. |
| `KYC_BIOMETRIC_LIVENESS` | HYBRID | Ground truth is private user data (selfie/ID) plus an engine-specific, non-reproducible liveness score; cannot be made public or replicated. |
| `LIVE_PORT_CONGESTION` | HYBRID | Port 'congestion' is a time-sensitive derived metric; two AIS queries seconds apart differ, so there is no stable snapshot to converge on. |
| `MALWARE_DETECTION` | HYBRID | Multi-engine AV detection counts drift over time and differ per engine set; the same hash yields different verdicts across validators and dates. |
| `MEDIA_FORENSIC_VERIFY` | NON-DETERMINISTIC | Deepfake/manipulation has no authoritative public label to converge on (adapter-only by design); additionally out of scope for the pipeline, which is text-only (ModernBERT) with no vision/audio backbone and no way to pass pixels or audio into the wasm. |
| `PACKAGE_STATUS` | DETERMINISTIC | Courier tracking lives in a private carrier DB behind keyed aggregators; not independently reproducible. |
| `PRODUCT_AUTHENTICITY` | HYBRID | Free registries cannot return a trustworthy "not registered"; GS1 is membership-gated. |
| `RETURN_POLICY_VERIFY` | HYBRID | Merchant return policies change without versioning and require LLM extraction; no stable deterministic fact two validators reproduce identically. |
| `SATELLITE_IMAGERY_ANALYSIS` | NON-DETERMINISTIC | Open-ended imagery interpretation has no authoritative public label to converge on (adapter-only by design); additionally out of scope for the pipeline, which is text-only (ModernBERT) with no vision backbone and no way to pass image data into the wasm. |
| `SECURITY_REVIEW` | HYBRID | Different SAST/SCA scanners (Snyk/Trivy/Semgrep) return different findings on identical code; no single convergent finding set to check against. |
| `SHIP_RATE_ETA` | HYBRID | Quoted shipping rate is carrier-account/contract-specific; each validator's account returns a different negotiated price, so there is no single public rate. |
| `SLA_COMPLIANCE` | DETERMINISTIC | Measured against a private internal APM ledger; no public source, so the network would have to trust one party’s private data. |
| `TRAVEL_TRANSIT_LOCK` | DETERMINISTIC | A fare-hold/PNR lock exists inside one private GDS session; no public replica for independent verification. |
| `URL_SAFE` | HYBRID | Ruled out for the build set; threat-feed verdicts also drift/differ across engines and time (non-convergent). |
| `WAREHOUSE_INVENTORY` | DETERMINISTIC | Ground truth (bin/pallet counts) lives only in a private WMS; no public source to reproduce and an API key exposes only the owner’s own data. |




---

## Appendix — lifecycle rollups (reference)

## How to use this file when hunting miners

For each intent, before registering:
1. Write Gate 1 quantity sentence from Description + (if scored) `label_field`.
2. Confirm candidate returns that physical quantity in convertible units (Gate 3).
3. Confirm every required / pinned param is a real request input (Gate 4).
4. Confirm a second miner would use a **different upstream publisher**, not a mirror/RPC/letter peer (Gate 5). **Never register a second miner on the same source.**
5. Prefer `Scoring path = comparator only` for deterministic ranking work; hybrid needs judgment path.

### Live inventory (updated 2026-09-29 — Groups A–D closed)

| Intent | Keepers | Sources | Bucket | Notes |
|--------|--------:|--------:|--------|-------|
| `FX_NOW` | 11 | 11 | rankable · wired | scoreboard ranks ✅ (6 scored this epoch) |
| `VULNERABILITY_TRIAGE` | 4 | 4 | rankable · wired | scoreboard ranks ✅ · Group D twins re-specced (not counted) |
| `EMAIL_SECURITY` | 2 | 2 | rankable · wired | scoreboard tie (all 1.0) |
| `ROUTE_ETA` | 2 | 2 | rankable · wired | scoreboard tie (all OSRM) |
| `MACRO_ECONOMIC_INDICATOR` | 2 | 2 | rankable · wired | scoreboard single this epoch |
| `LIQUIDITY_DEPTH_VERIFY` | 2 | 2 | rankable · wired | scoreboard ranks ✅ |
| `ASSET_RESERVE_ATTESTATION` | 1 | 1 | single-source · wired | scoreboard tie |
| `GRID_POWER_PRICE` | 1 | 1 | single-source · wired | |
| `LIVE_SHELF_PRICE` | 1 | 1 | single-source · wired | |
| `MINING_HASHPRICE_VERIFY` | 1 | 1 | single-source · wired | scoreboard single |
| `ONCHAIN_METRIC_VERIFY` | 1 | 1 | single-source · wired | |
| `CRYPTO_PRICE` | 10 | 10 | **rankable · not wired** | promoted 2026-09-28 (BAG20×5 + Batch7×5) |
| `WEATHER_CHECK` | 5 | 5 | **rankable · not wired** | promoted 2026-09-28 (Batch5×4 + 7Timer) |
| `STOCK_PRICE` | 3 | 3 | **rankable · not wired** | promoted 2026-09-28 |
| `CRYPTO_YIELD_RATE` | 7 | 7 | **rankable · not wired** | promoted 2026-09-29 · YAML + compound on-chain · shared `pool` pin |
| `EVENT_OUTCOME_RESOLUTION` | 3 | 3 | **rankable · not wired** | promoted 2026-09-29 · Kalshi re-pinned **4364** |
| `VESSEL_TELEMETRY_VERIFY` | 1 | 1 | **single-source · not wired** | promoted 2026-09-29 · pin `230981000` · reg **4365** |

**Total Active: 289 miners · 56 intents** (2026-10-06; Pre-active bucket removed).

**Pre-active:** none (removed 2026-10-06; all promoted to Active).

Comparator-wired (9): FX_NOW, ROUTE_ETA, MACRO_ECONOMIC_INDICATOR, LIQUIDITY_DEPTH_VERIFY, MINING_HASHPRICE_VERIFY, GRID_POWER_PRICE, LIVE_SHELF_PRICE, ONCHAIN_METRIC_VERIFY, ASSET_RESERVE_ATTESTATION. Rankable-not-wired (5): CRYPTO_PRICE, WEATHER_CHECK, STOCK_PRICE, CRYPTO_YIELD_RATE, EVENT_OUTCOME_RESOLUTION.

Full YAML/tx tables: `MinerCreator/workingMiners.md`. Cleanup log: `out/same-source-cleanup-plan.md`.

## Active summary

| Class | Count |
|-------|------:|
| DETERMINISTIC | 47 |
| HYBRID | 36 |
| NON-DETERMINISTIC | 14 |

| Scoring path | Count |
|--------------|------:|
| adapter only | 14 |
| comparator + adapter | 36 |
| comparator only | 47 |

## Index (lifecycle)

Four buckets. Flow: hunt → register → **pre-active** (await Usman) → **active** if approved, else **dead**. Intents with **zero** honest sources after a hunt also go to **dead**.

| Bucket | Meaning |
|--------|---------|
| **1. Active (registered)** | Usman-side keepers in `workingMiners.md` |
| **2. Pre-active** | On-chain in `newlyRegisteredMiners.md` — NON-DET awaiting adapter wire |
| **3. Not registered** | Still open to hunt |
| **4. Dead** | Usman rejected **or** hunt found **no** usable source/API |

---

<div style="background:#e8f5e9;border:2px solid #2e7d32;border-radius:8px;padding:12px 16px;margin:12px 0">

### 1. Active — registered & approved

| Intent | Class | Scoring path | Category | Priority | **Miners** | Status |
|--------|-------|--------------|----------|----------:|----------:|--------|
| <span style="color:#0b6e4f;font-weight:700">`FX_NOW`</span> | DETERMINISTIC | comparator only | Financial / Transactional | 8.0 | <span style="color:#0b6e4f;font-weight:700">11</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`VULNERABILITY_TRIAGE`</span> | HYBRID | comparator + adapter | Cybersecurity | 10.0 | <span style="color:#0b6e4f;font-weight:700">4</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`EMAIL_SECURITY`</span> | HYBRID | comparator + adapter | Cybersecurity | 7.0 | <span style="color:#0b6e4f;font-weight:700">2</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`LIQUIDITY_DEPTH_VERIFY`</span> | DETERMINISTIC | comparator only | Blockchain & Web3 | 10.0 | <span style="color:#0b6e4f;font-weight:700">2</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`MACRO_ECONOMIC_INDICATOR`</span> | DETERMINISTIC | comparator only | Macroeconomics & Finance | 8.0 | <span style="color:#0b6e4f;font-weight:700">2</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`ROUTE_ETA`</span> | DETERMINISTIC | comparator only | Travel & Mobility | 6.0 | <span style="color:#0b6e4f;font-weight:700">2</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`ASSET_RESERVE_ATTESTATION`</span> | DETERMINISTIC | comparator only | Blockchain & Web3 | 9.0 | <span style="color:#0b6e4f;font-weight:700">1</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`GRID_POWER_PRICE`</span> | DETERMINISTIC | comparator only | Energy & Infrastructure | 5.0 | <span style="color:#0b6e4f;font-weight:700">1</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`LIVE_SHELF_PRICE`</span> | DETERMINISTIC | comparator only | Commerce & Procurement | 10.0 | <span style="color:#0b6e4f;font-weight:700">1</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`MINING_HASHPRICE_VERIFY`</span> | DETERMINISTIC | comparator only | Energy & Infrastructure | 5.0 | <span style="color:#0b6e4f;font-weight:700">1</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`ONCHAIN_METRIC_VERIFY`</span> | DETERMINISTIC | comparator only | Blockchain & Web3 | 10.0 | <span style="color:#0b6e4f;font-weight:700">1</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| | | | | | | |
| **—— 2026-09-28 ——** | | | | | | **promoted from Pre-active (Usman RANKABLE)** |
| <span style="color:#0b6e4f;font-weight:700">`CRYPTO_PRICE`</span> / catalog `CRYPTO_PRICE_LOOKUP` | DETERMINISTIC | comparator only | Blockchain & Web3 | 7.0 | <span style="color:#0b6e4f;font-weight:700">10</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> — **not wired** yet · `price_usd_cents` · BAG20+Batch7 |
| <span style="color:#0b6e4f;font-weight:700">`WEATHER_CHECK`</span> / catalog `WEATHER_CURRENT` | DETERMINISTIC | comparator only | Climate & Weather | 6.0 | <span style="color:#0b6e4f;font-weight:700">5</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> — **not wired** yet · `temp_k_x100` · +7Timer |
| <span style="color:#0b6e4f;font-weight:700">`STOCK_PRICE`</span> / catalog `STOCK_PRICE_QUOTE` | DETERMINISTIC | comparator only | Financial / Transactional | 7.0 | <span style="color:#0b6e4f;font-weight:700">3</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> — **not wired** yet · `last_cents` |
| | | | | | | |
| **—— 2026-09-29 ——** | | | | | | **promoted (Groups A–D closed)** |
| <span style="color:#0b6e4f;font-weight:700">`CRYPTO_YIELD_RATE`</span> | DETERMINISTIC | comparator only | Blockchain & Web3 | 6.0 | <span style="color:#0b6e4f;font-weight:700">7</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> — **not wired** yet · `apy_bps` · regs **4356–4361** + **4375** |
| <span style="color:#0b6e4f;font-weight:700">`EVENT_OUTCOME_RESOLUTION`</span> | HYBRID | comparator + adapter | Blockchain & Web3 | 10.0 | <span style="color:#0b6e4f;font-weight:700">3</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> — **not wired** yet · `resolved_yes` · Kalshi **4364** |
| <span style="color:#0b6e4f;font-weight:700">`VESSEL_TELEMETRY_VERIFY`</span> | DETERMINISTIC | comparator only | Logistics & Maritime | 5.0 | <span style="color:#0b6e4f;font-weight:700">1</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> — **not wired** yet · `sog_milliknots` · reg **4365** · single-source |


| | | | | | | |
| **—— 2026-09-30 ——** | | | | | | **promoted from Pre-active (Usman verified)** |
| <span style="color:#0b6e4f;font-weight:700">`CODE_PATCH_VERIFY`</span> | DETERMINISTIC | comparator only | Software / Engineering | 10.0 | <span style="color:#0b6e4f;font-weight:700">3</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`CROSS_CHAIN_STATE_VERIFY`</span> | DETERMINISTIC | comparator only | Blockchain & Web3 | 10.0 | <span style="color:#0b6e4f;font-weight:700">3</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`OPTIMAL_EXECUTION_ROUTE`</span> | HYBRID | comparator + adapter | Financial / Transactional | 10.0 | <span style="color:#0b6e4f;font-weight:700">4</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`SKU_IN_STOCK`</span> | DETERMINISTIC | comparator only | Commerce & Procurement | 10.0 | <span style="color:#0b6e4f;font-weight:700">1</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`PAYMENT_METHOD_VERIFY`</span> | DETERMINISTIC | comparator only | Financial / Transactional | 9.0 | <span style="color:#0b6e4f;font-weight:700">2</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`SANCTIONS_SCREENING_MATCH`</span> | HYBRID | comparator + adapter | Legal & Compliance | 9.0 | <span style="color:#0b6e4f;font-weight:700">2</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`CORPORATE_REGISTRY_LOOKUP`</span> | DETERMINISTIC | comparator only | Legal & Compliance | 8.0 | <span style="color:#0b6e4f;font-weight:700">3</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`REGULATORY_FILING_MONITOR`</span> | DETERMINISTIC | comparator only | Legal & Compliance | 8.0 | <span style="color:#0b6e4f;font-weight:700">1</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`CRYPTO_TRANSFER_VERIFY`</span> | DETERMINISTIC | comparator only | Blockchain & Web3 | 7.0 | <span style="color:#0b6e4f;font-weight:700">1</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`THREAT_IP_REPUTATION`</span> | HYBRID | comparator + adapter | Cybersecurity | 7.0 | <span style="color:#0b6e4f;font-weight:700">6</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`TRAVEL_DISRUPTION`</span> | DETERMINISTIC | comparator only | Travel & Mobility | 10.0 | <span style="color:#0b6e4f;font-weight:700">1</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`DNS_RECORD_LOOKUP`</span> | DETERMINISTIC | comparator only | Cybersecurity | 6.0 | <span style="color:#0b6e4f;font-weight:700">7</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`SSL_VERIFICATION`</span> / catalog `SSL_CERTIFICATE_VERIFY` | DETERMINISTIC | comparator only | Cybersecurity | 6.0 | <span style="color:#0b6e4f;font-weight:700">2</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`PORT_SCAN_AUDIT`</span> | DETERMINISTIC | comparator only | Cybersecurity | 6.0 | <span style="color:#0b6e4f;font-weight:700">2</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`THREAT_INTELLIGENCE`</span> | HYBRID | comparator + adapter | Cybersecurity | 7.0 | <span style="color:#0b6e4f;font-weight:700">3</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`AIR_QUALITY_INDEX`</span> | DETERMINISTIC | comparator only | Climate & Weather | 6.0 | <span style="color:#0b6e4f;font-weight:700">7</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`WEATHER_FORECAST_VERIFY`</span> | DETERMINISTIC | comparator only | Climate & Weather | 5.0 | <span style="color:#0b6e4f;font-weight:700">5</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`GAS_PRICE`</span> / catalog `GAS_PRICE_ESTIMATION` | DETERMINISTIC | comparator only | Blockchain & Web3 | 6.0 | <span style="color:#0b6e4f;font-weight:700">2</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`TOKEN_TOTAL_SUPPLY_VERIFY`</span> | DETERMINISTIC | comparator only | Blockchain & Web3 | 6.0 | <span style="color:#0b6e4f;font-weight:700">2</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`VALIDATOR_PERFORMANCE_VERIFY`</span> | DETERMINISTIC | comparator only | Blockchain & Web3 | 6.0 | <span style="color:#0b6e4f;font-weight:700">2</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`LOAN_INTEREST_RATE_QUOTE`</span> | DETERMINISTIC | comparator only | Financial / Transactional | 6.0 | <span style="color:#0b6e4f;font-weight:700">6</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`API_HEALTH_CHECK`</span> | DETERMINISTIC | comparator only | Enterprise Operations | 6.0 | <span style="color:#0b6e4f;font-weight:700">2</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`SERVER_UPTIME_MONITOR`</span> | DETERMINISTIC | comparator only | Enterprise Operations | 6.0 | <span style="color:#0b6e4f;font-weight:700">2</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`CLOUD_RESOURCE_USAGE`</span> | DETERMINISTIC | comparator only | Energy & Infrastructure | 5.0 | <span style="color:#0b6e4f;font-weight:700">2</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`SENSOR_TELEMETRY_VERIFY`</span> | DETERMINISTIC | comparator only | IoT & Telemetry | 5.0 | <span style="color:#0b6e4f;font-weight:700">5</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`CARRIER_SERVICEABILITY`</span> | DETERMINISTIC | comparator only | Logistics | 5.0 | <span style="color:#0b6e4f;font-weight:700">2</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`VENDOR_VERIFY`</span> | HYBRID | comparator + adapter | Commerce & Procurement | 7.0 | <span style="color:#0b6e4f;font-weight:700">4</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`GRAMMAR_SPELL_CHECK`</span> | DETERMINISTIC | comparator only | Software / Engineering | 6.0 | <span style="color:#0b6e4f;font-weight:700">2</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`REGRESSION_VERIFY`</span> | DETERMINISTIC | comparator only | Software / Engineering | 7.0 | <span style="color:#0b6e4f;font-weight:700">1</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`CONTENT_EXTRACTION`</span> / catalog `URL_CONTENT_EXTRACTION` | DETERMINISTIC | comparator only | AI & Machine Learning | 7.0 | <span style="color:#0b6e4f;font-weight:700">2</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`SENTIMENT_ANALYSIS`</span> | HYBRID | comparator + adapter | AI & Machine Learning | 7.0 | <span style="color:#0b6e4f;font-weight:700">2</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`WEB_SEARCH`</span> / catalog `WEB_SEARCH_QUERY` | HYBRID | comparator + adapter | AI & Machine Learning | 8.0 | <span style="color:#0b6e4f;font-weight:700">1</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`SEMANTIC_SIMILARITY`</span> | DETERMINISTIC | comparator only | AI & Machine Learning | 7.0 | <span style="color:#0b6e4f;font-weight:700">1</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |
| <span style="color:#0b6e4f;font-weight:700">`TEXT_CLASSIFICATION`</span> | HYBRID | comparator + adapter | AI & Machine Learning | 7.0 | <span style="color:#0b6e4f;font-weight:700">2</span> | <span style="background:#c8e6c9;color:#1b5e20;padding:2px 8px;border-radius:4px;font-weight:700">ACTIVE</span> |

**Subtotal:** **153 miners** · **49 intents** · wired keepers → [`workingMiners.md`](./workingMiners.md) · promoted bag detail archived in [`newlyRegisteredMiners.md`](./newlyRegisteredMiners.md)

<!-- Day separator convention: blank row + `—— YYYY-MM-DD ——` before each day's new Active adds. -->

</div>

