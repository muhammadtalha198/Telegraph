# newlyRegisteredMiners

**Lifecycle (updated 2026-10-05):**  
Diamond: `0x5a2324aA18613FAD4e44bDF0d6c73Ec1f6D87ff8` (Base Sepolia)  
YAML host at register time: **paste.rs** (omni-chat disk full / Dropbox token empty).

Prior Pre-active / archived bags that are already listed in [`INTENT_BUILD_SHEET-2026-09-23.md`](./INTENT_BUILD_SHEET-2026-09-23.md) (Active + Pre-active) were **removed from this file** on 2026-10-05.

**Current Active (promoted 2026-10-06 — was Pre-active pack):**

- **Pack Semantic V2** (2026-10-05) — **61 miners / 22 intents** — golden PASS + auto_review+Ollama LLM + `register-miner-v2.sh` gates.
- Report: [`out/PACK_V2_REGISTER_COMBINED.md`](./out/PACK_V2_REGISTER_COMBINED.md) · pipeline: [`PACK_V2_REGISTER_PIPELINE.md`](./PACK_V2_REGISTER_PIPELINE.md).

**Active total (this file): 61 miners · 22 intents.** Path: [`SEMANTIC_REGISTER_V2.md`](./SEMANTIC_REGISTER_V2.md).

Not registered from the same 66 LLM-approved set (gates failed): `filing-sec-atom` (SEC 403), `macro-bls` (golden FAIL), `route-cow` (405 POST), `val-beacon-chainsafe` / `xchain-beacon-lodestar` (429).

---

## New miner hunt — 2026-10-09 (6 registered)

**6 miners / 3 intents.** New free, no-key providers found via a dedicated miner-hunt round (`miner_candidates/2026-10-09/`), each run through the full `minercheck` catalog-bound verifier (E1 extract → E5 type → E2 sanity → E4 freshness → E5 entity → E3 cross-check against the existing registered consensus) **and** the full fail-closed `register-miner-v2.sh` gate chain (auto_review+Ollama LLM → golden-if-any → validate_miner_yaml → pin_consistency_check → sample-question==node-request → `minercheck gate` → live probe → hosted byte-match) before any gas was spent. YAML host: **Omni SSH** (`omni-chat.13.237.89.59.sslip.io`).

| Slug | Intent | Reg ID | Publisher | YAML | Tx |
|------|--------|-------:|-----------|------|-----|
| `cp-phemex` | `CRYPTO_PRICE` | 4804 | phemex.com | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/cp-phemex.yaml) | [tx](https://sepolia.basescan.org/tx/0xad76ba8f1ccd4fed87d893a5b3db018cd7415f83896ffd485ce01de5641944f2) |
| `cp-xt` | `CRYPTO_PRICE` | 4805 | xt.com | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/cp-xt.yaml) | [tx](https://sepolia.basescan.org/tx/0xeaa1ab82e80196e03d9223502a9ca781a9a0236f311f7a44a72cee88582cacc8) |
| `cp-bitrue` | `CRYPTO_PRICE` | 4806 | bitrue.com | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/cp-bitrue.yaml) | [tx](https://sepolia.basescan.org/tx/0xa50deb2a6dae50ba832c00380d6b9d7f882bc053fde31d2b9372c42d738386ac) |
| `cp-hitbtc` | `CRYPTO_PRICE` | 4807 | hitbtc.com | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/cp-hitbtc.yaml) | [tx](https://sepolia.basescan.org/tx/0xb85341fd3518811c7450389fe4e1d0fdf1c729465450b9238f5c0c864bed8470) |
| `cp-digifinex` | `CRYPTO_PRICE` | 4808 | digifinex.com | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/cp-digifinex.yaml) | [tx](https://sepolia.basescan.org/tx/0x6eeb4c5d1b669f34ef42e99ef62cb66740bc53284f6547962fef18a78fd00400) |
| `stock-stockanalysis` | `STOCK_PRICE` | 4809 | stockanalysis.com | [yaml](https://omni-chat.13.237.89.59.sslip.io/miner-yamls/stock-stockanalysis.yaml) | [tx](https://sepolia.basescan.org/tx/0xf591afe98b872e69aafb14fd555277dd7f3cbe75555e78323390e8b8a2fcb670) |

All 6 confirmed `activation_status: active` via `GET /api/miners/<id>` after registration. All are new publishers (none duplicate an existing registered endpoint).

**From the same 2026-10-09 hunt, NOT registered:**
- `dns-dnssb` (dns.sb DoH) and `dns-dnspod` (DNSPod doh.pub) — **dropped as duplicates**: `dns-dnssb` slug is already taken (reg 2894, different truth-proxy signal) and `dns-dnspod` (reg 4671, Active) is the literal same `doh.pub/dns-query` endpoint already registered. Caught during the dedupe pass before any capture/gas.
- `wx-brightsky-de` (Bright Sky / DWD current-weather, Germany-only) — sample **rejected by the Ollama LLM judge** (`qwen2.5:3b` wrongly said the response has no temperature field; it does — `weather.temperature` is present in the captured body). Per CLAUDE.md, manual override does not unlock gas and was not attempted. Candidate YAML + sample kept in `miner_candidates/2026-10-09/` for a future re-run of auto_review.

---

## Active summary — Pack Semantic V2 (2026-10-05)

| Intent | Miners | ≈reg notes |
|--------|-------:|------------|
| `CORPORATE_REGISTRY_LOOKUP` | 3 | 4627–4629 |
| `CROSS_CHAIN_STATE_VERIFY` | 4 | 4601–4632 |
| `CRYPTO_PRICE` | 2 | 4653–4654 |
| `CRYPTO_TRANSFER_VERIFY` | 6 | 4601–4655 |
| `EMAIL_SECURITY` | 3 | 4604–4635 |
| `EVENT_OUTCOME_RESOLUTION` | 1 | 4636–4636 |
| `FX_NOW` | 2 | 4638–4638 |
| `GAS_PRICE` | 3 | 4639–4658 |
| `GRAMMAR_SPELL_CHECK` | 1 | 4606–4606 |
| `GRID_POWER_PRICE` | 3 | 4607–4609 |
| `LANGUAGE_TRANSLATION` | 1 | 4640–4640 |
| `LIQUIDITY_DEPTH_VERIFY` | 13 | 4610–4661 |
| `MACRO_ECONOMIC_INDICATOR` | 1 | 4645–4645 |
| `ONCHAIN_METRIC_VERIFY` | 3 | 4616–4647 |
| `OPTIMAL_EXECUTION_ROUTE` | 2 | 4647–4648 |
| `PAYMENT_METHOD_VERIFY` | 4 | 4618–4651 |
| `REGULATORY_FILING_MONITOR` | 1 | 4621–4621 |
| `ROUTE_ETA` | 1 | 4622–4622 |
| `THREAT_IP_REPUTATION` | 2 | 4623–4623 |
| `TOKEN_TOTAL_SUPPLY_VERIFY` | 3 | 4624–4653 |
| `VALIDATOR_PERFORMANCE_VERIFY` | 1 | 4625–4625 |
| `VENDOR_VERIFY` | 1 | 4626–4626 |
| **Total** | **61** | |

---

## Active detail — Pack Semantic V2 (2026-10-05)

**61 miners · 22 intents.** On-chain YAML host is **paste.rs** (click [yaml]). Local: `intentYamls/`.

### `CORPORATE_REGISTRY_LOOKUP`

| Slug | Class | ≈Reg | YAML | Tx |
|------|-------|-----:|------|-----|
| `corp-brreg-no` | DETERMINISTIC | 4627 | [yaml](https://paste.rs/KToEC) | [tx](https://sepolia.basescan.org/tx/0x94efe91ce9d921ab31dddb9b6844c425ae6ff4212a9dc05526ecd2c93b09750b) |
| `corp-krs-pl` | DETERMINISTIC | 4629 | [yaml](https://paste.rs/20Nz7) | [tx](https://sepolia.basescan.org/tx/0x12b5f28b939222c3d0779ba9229cfb0e68546fa11d35ac0936bfcfbca224f74f) |
| `corp-prh-fi` | DETERMINISTIC | 4629 | [yaml](https://paste.rs/lYxfZ) | [tx](https://sepolia.basescan.org/tx/0xd790bf2ebdff8ffdcbbd127278398105712c925489c681ad76120edca2c36d1c) |

### `CROSS_CHAIN_STATE_VERIFY`

| Slug | Class | ≈Reg | YAML | Tx |
|------|-------|-----:|------|-----|
| `xchain-arbitrum-root` | DETERMINISTIC | 4631 | [yaml](https://paste.rs/L9HBw) | [tx](https://sepolia.basescan.org/tx/0xa051a41a7c845507ef6f2e9b508b57c5435f9f405a625ac5d81964635e63c88e) |
| `xchain-base-root` | DETERMINISTIC | 4632 | [yaml](https://paste.rs/lGZJH) | [tx](https://sepolia.basescan.org/tx/0x4e58f70a534a3b12c21f5c1d3567839a5d48f3a09d38eff7630415359e066f20) |
| `xchain-beacon-publicnode` | DETERMINISTIC | 4601 | [yaml](https://paste.rs/TWxxo) | [tx](https://sepolia.basescan.org/tx/0xe4e775214663b9fff52bd80aefb054d8d098a318c5acff42c6391c52e6ed5c80) |
| `xchain-optimism-root` | DETERMINISTIC | 4632 | [yaml](https://paste.rs/5Shbl) | [tx](https://sepolia.basescan.org/tx/0xe50cc5c71fcaea5db29020b4a26246f35df86d5e316bc8bef321fee3e79a1f9e) |

### `CRYPTO_PRICE`

| Slug | Class | ≈Reg | YAML | Tx |
|------|-------|-----:|------|-----|
| `cp-coinlore` | DETERMINISTIC | 4653 | [yaml](https://paste.rs/wfS5j) | [tx](https://sepolia.basescan.org/tx/0xe3b4af309bac22f9b5dbd3c01b3e9ed3475e28b174a8e584c6d0f7d1cbbd8f97) |
| `cp-coinpaprika` | DETERMINISTIC | 4654 | [yaml](https://paste.rs/XUnUF) | [tx](https://sepolia.basescan.org/tx/0x962261f64a8328878984b60eb8cb07e32fdad4fae315da39e1d28d54ccc10ea9) |

### `CRYPTO_TRANSFER_VERIFY`

| Slug | Class | ≈Reg | YAML | Tx |
|------|-------|-----:|------|-----|
| `xfer-blockchain-info` | DETERMINISTIC | 4655 | [yaml](https://paste.rs/SGRiH) | [tx](https://sepolia.basescan.org/tx/0x3727a17c07a8d31ae90b53ed23c754e6dd6ab280929cd5ebbf1745a87a8a975a) |
| `xfer-blockcypher` | DETERMINISTIC | 4633 | [yaml](https://paste.rs/5b3aq) | [tx](https://sepolia.basescan.org/tx/0xb0bb71457201b5b8e18d112ea18afb87fb3da64b315b789db38082546f6bcf41) |
| `xfer-blockstream` | DETERMINISTIC | 4634 | [yaml](https://paste.rs/SPaCO) | [tx](https://sepolia.basescan.org/tx/0x0044ff284862e608dd3c8c9ef19df54e88b36effc456eb41f327d53cea92e218) |
| `xfer-haskoin` | DETERMINISTIC | 4601 | [yaml](https://paste.rs/vLHVK) | [tx](https://sepolia.basescan.org/tx/0x1bf6ebc1ca5e9ec6715fa0ceab4befc0eee8f07ccb6e79a138454f36009a8cd8) |
| `xfer-publicnode-rpc` | DETERMINISTIC | 4603 | [yaml](https://paste.rs/vq8jX) | [tx](https://sepolia.basescan.org/tx/0xba629fd8e366de2c2341a2655c992f0df1e873aec6cba3402b7aced4a2028b09) |
| `xfer-trezor-blockbook` | DETERMINISTIC | 4603 | [yaml](https://paste.rs/XOild) | [tx](https://sepolia.basescan.org/tx/0xe92b09e5b151fa2115e84ddd2a2c343d6c1969f849965897595931f8e72bae40) |

### `EMAIL_SECURITY`

| Slug | Class | ≈Reg | YAML | Tx |
|------|-------|-----:|------|-----|
| `email-doh-adguard` | HYBRID | 4604 | [yaml](https://paste.rs/iubQr) | [tx](https://sepolia.basescan.org/tx/0x0bf67d18715a65f00b5b5d583b5b9f48afcda438b046aa8648b16c5179579080) |
| `email-doh-alidns` | HYBRID | 4605 | [yaml](https://paste.rs/4lNZ5) | [tx](https://sepolia.basescan.org/tx/0x0b5f6e336ab25ee1728f6ddb01aba299b23ec2eb672e5b51ecbfe23bb3443db2) |
| `email-doh-dnspod` | HYBRID | 4635 | [yaml](https://paste.rs/vgxu3) | [tx](https://sepolia.basescan.org/tx/0xe1a4be094153f22d503e02ccbb034616a93dc19d4ce106ecc3d5cc3decc204b8) |

### `EVENT_OUTCOME_RESOLUTION`

| Slug | Class | ≈Reg | YAML | Tx |
|------|-------|-----:|------|-----|
| `event-manifold` | HYBRID | 4636 | [yaml](https://paste.rs/zwtJA) | [tx](https://sepolia.basescan.org/tx/0xc4ec6e714a5265e0968e1999ee111ffd6573ebad79c3fa2d8531b7bbbb2c74db) |

### `FX_NOW`

| Slug | Class | ≈Reg | YAML | Tx |
|------|-------|-----:|------|-----|
| `fx-hexarate` | DETERMINISTIC | 4638 | [yaml](https://paste.rs/imVjp) | [tx](https://sepolia.basescan.org/tx/0x89bf92f15da5d3ce5924b700999fe031e91734fbca69e0b41a9f5f17c1e57111) |
| `fx-yahoo` | DETERMINISTIC | 4638 | [yaml](https://paste.rs/SplQn) | [tx](https://sepolia.basescan.org/tx/0xa64560d49a447fc2f2a8e9932167a3be3d040e88c57bf27116c0a65369cfb9d4) |

### `GAS_PRICE`

| Slug | Class | ≈Reg | YAML | Tx |
|------|-------|-----:|------|-----|
| `gas-1rpc` | DETERMINISTIC | 4639 | [yaml](https://paste.rs/RAPwu) | [tx](https://sepolia.basescan.org/tx/0xd719753cc5312c50d83dd30f7f6eb3dc48d8f44744fe28e61170725f86c94aa7) |
| `gas-drpc-rpc` | DETERMINISTIC | 4657 | [yaml](https://paste.rs/M8OTk) | [tx](https://sepolia.basescan.org/tx/0x2c8bfb17d5356a2145f8847935933f9dc4c1f2a27d77f55d9715f459e21e05cc) |
| `gas-publicnode-rpc` | DETERMINISTIC | 4658 | [yaml](https://paste.rs/YXsXR) | [tx](https://sepolia.basescan.org/tx/0x2e3328e2bafff4ac72503601e24fd312765fcea7a35932d6536eb71be4fe36e2) |

### `GRAMMAR_SPELL_CHECK`

| Slug | Class | ≈Reg | YAML | Tx |
|------|-------|-----:|------|-----|
| `grammar-languagetool` | DETERMINISTIC | 4606 | [yaml](https://paste.rs/lZ1Th) | [tx](https://sepolia.basescan.org/tx/0x2192a64b934901342fea572a796e2c06a62957bd3f36d54ea1ddb6ffaa5085f8) |

### `GRID_POWER_PRICE`

| Slug | Class | ≈Reg | YAML | Tx |
|------|-------|-----:|------|-----|
| `grid-awattar-de` | DETERMINISTIC | 4607 | [yaml](https://paste.rs/FnIKS) | [tx](https://sepolia.basescan.org/tx/0xe44603661dd7ab45207eae396a1e8fa87f429cee234edcda9b5a0d1851e2b4c6) |
| `grid-elering` | DETERMINISTIC | 4608 | [yaml](https://paste.rs/OnBDU) | [tx](https://sepolia.basescan.org/tx/0x61411fb1b6cb6c23e4af605137144212d2f2681b5ac06ddd894a32acbe201dc5) |
| `grid-spot-hinta` | DETERMINISTIC | 4609 | [yaml](https://paste.rs/Mz4a3) | [tx](https://sepolia.basescan.org/tx/0xfc8ffc2ad712a59901b6764a8f21c6229cda879c1de7fdd94b9af92b3e6b5a40) |

### `LANGUAGE_TRANSLATION`

| Slug | Class | ≈Reg | YAML | Tx |
|------|-------|-----:|------|-----|
| `tr-apertium` | NON-DETERMINISTIC | 4640 | [yaml](https://paste.rs/yPmRF) | [tx](https://sepolia.basescan.org/tx/0x1c487c111cd24d6ec1c841169e6c90fdbbfb581f92a552d0456527f9b23cb63c) |

### `LIQUIDITY_DEPTH_VERIFY`

| Slug | Class | ≈Reg | YAML | Tx |
|------|-------|-----:|------|-----|
| `liq-binance-depth` | DETERMINISTIC | 4641 | [yaml](https://paste.rs/NGF8B) | [tx](https://sepolia.basescan.org/tx/0x0d8c5e7d72ce43fcf23f15f2482b0e3c0faf1d01c5804a95606c414f1cfd5b6a) |
| `liq-bitfinex-book` | DETERMINISTIC | 4643 | [yaml](https://paste.rs/kBZwt) | [tx](https://sepolia.basescan.org/tx/0x8da92ab2fa9ceb8671f3c81fd79ca0dcffe5010281eab223aaac9ec6de8a5fcd) |
| `liq-bitget-book` | DETERMINISTIC | 4610 | [yaml](https://paste.rs/JxCN2) | [tx](https://sepolia.basescan.org/tx/0x125f7d836e4a689a5068e6a85867a4c23b86a70c1dcc94bf0ec9a060d101c234) |
| `liq-bitstamp-book` | DETERMINISTIC | 4612 | [yaml](https://paste.rs/vh1zm) | [tx](https://sepolia.basescan.org/tx/0x484367688178775a49dbbf350bdef85e6a86fdc344884cc4c0c04ba0137590cc) |
| `liq-bybit-book` | DETERMINISTIC | 4612 | [yaml](https://paste.rs/AJZsq) | [tx](https://sepolia.basescan.org/tx/0x0b61492728d6971b1547b32ef07142f887d39968756468994dd37257564214b7) |
| `liq-coinbase-book` | DETERMINISTIC | 4658 | [yaml](https://paste.rs/H6XnN) | [tx](https://sepolia.basescan.org/tx/0xd57c74b8e9e913c013b28ade5456d2afd262d15fee9a96fc29a6ab7841c7d1fa) |
| `liq-cryptocom-book` | DETERMINISTIC | 4643 | [yaml](https://paste.rs/lqVzE) | [tx](https://sepolia.basescan.org/tx/0x61271ca8c2c84a048b9a6451a6aa439b9b0cac592885c901bcc71345a51f8619) |
| `liq-gate-book` | DETERMINISTIC | 4659 | [yaml](https://paste.rs/2YyaC) | [tx](https://sepolia.basescan.org/tx/0xe41083cee4e46b0f0e6493f07818b25e672befdb1de38f0b48d1ebfd77a7cbcb) |
| `liq-gemini-book` | DETERMINISTIC | 4661 | [yaml](https://paste.rs/YsPaz) | [tx](https://sepolia.basescan.org/tx/0xc688cfd6b1605525796d2d0cfe82de3e42039ceb59279c0cf20b9b07e155b383) |
| `liq-htx-depth` | DETERMINISTIC | 4614 | [yaml](https://paste.rs/IVjQT) | [tx](https://sepolia.basescan.org/tx/0xd1bbaca33a39acb4ebd12f3f209f456fe0e58f155e4123ebaa6ca87636d66c9d) |
| `liq-kraken-depth` | DETERMINISTIC | 4615 | [yaml](https://paste.rs/cZ86W) | [tx](https://sepolia.basescan.org/tx/0x561e1b95ee9cf24485a607898d98c6250dc8aa913d74fa6bfd56654184cc2a34) |
| `liq-kucoin-book` | DETERMINISTIC | 4616 | [yaml](https://paste.rs/x7Xgo) | [tx](https://sepolia.basescan.org/tx/0x69d07155f4ccf431048187685a7361c6bf4a5c38cfe7068e2c63fe4c2bf6837b) |
| `liq-mexc-depth` | DETERMINISTIC | 4645 | [yaml](https://paste.rs/fK7tr) | [tx](https://sepolia.basescan.org/tx/0xbb2a19a21605138144f6d05b74653ffdcef487dd4719876e61228c0289d0ace5) |

### `MACRO_ECONOMIC_INDICATOR`

| Slug | Class | ≈Reg | YAML | Tx |
|------|-------|-----:|------|-----|
| `macro-eurostat` | DETERMINISTIC | 4645 | [yaml](https://paste.rs/xBQ5g) | [tx](https://sepolia.basescan.org/tx/0xcedca5e716496f15204b37d5af3535270c633d96d1107f861db27356530d02af) |

### `ONCHAIN_METRIC_VERIFY`

| Slug | Class | ≈Reg | YAML | Tx |
|------|-------|-----:|------|-----|
| `ocm-drpc-rpc` | DETERMINISTIC | 4647 | [yaml](https://paste.rs/PiJVl) | [tx](https://sepolia.basescan.org/tx/0x6ecd410def8b0b3173824801669167cceb4aa916178c27563940f3955f5b0596) |
| `ocm-publicnode-rpc` | DETERMINISTIC | 4616 | [yaml](https://paste.rs/RyeX6) | [tx](https://sepolia.basescan.org/tx/0x45e06991967e9c8653fd657b09ccf9a7dd07f4c0d6aa1e1cf23ef00b8000c9fa) |
| `ocm-trezor-blockbook` | DETERMINISTIC | 4617 | [yaml](https://paste.rs/wVDcZ) | [tx](https://sepolia.basescan.org/tx/0x7686d42a62864c0569a9eacb57d88ec4592ace4d67d3024c6f0158ea2ca9c5be) |

### `OPTIMAL_EXECUTION_ROUTE`

| Slug | Class | ≈Reg | YAML | Tx |
|------|-------|-----:|------|-----|
| `route-jupiter` | HYBRID | 4647 | [yaml](https://paste.rs/QuRmy) | [tx](https://sepolia.basescan.org/tx/0x50dc151e039174205cbd4b7387eb7b3090e06baddc4de7edd527d5d6e68c85ec) |
| `route-paraswap` | HYBRID | 4648 | [yaml](https://paste.rs/mpnm8) | [tx](https://sepolia.basescan.org/tx/0x00b7880d7c4513bd9584de87e55723bb8db965e23e75fc11eff2cb45d6e79f23) |

### `PAYMENT_METHOD_VERIFY`

| Slug | Class | ≈Reg | YAML | Tx |
|------|-------|-----:|------|-----|
| `pay-binlist` | DETERMINISTIC | 4651 | [yaml](https://paste.rs/illVy) | [tx](https://sepolia.basescan.org/tx/0x32e3bfc03a0e6c1e5c1e5b6fe2e5f311257fbcf426b8f63fad195f8954e5fccb) |
| `pay-binlist-io` | DETERMINISTIC | 4649 | [yaml](https://paste.rs/TS0SL) | [tx](https://sepolia.basescan.org/tx/0xdc49f2979f65142a79004f02a1fa71bf54ff72d08c5c55c5ec4c765e27308ce4) |
| `pay-handyapi-bin` | DETERMINISTIC | 4618 | [yaml](https://paste.rs/pZimG) | [tx](https://sepolia.basescan.org/tx/0x97edb851390a0e9dc5a361c8ab4d72b0156c74c2aab89d49acb281dabcdd2bfb) |
| `pay-openiban` | DETERMINISTIC | 4619 | [yaml](https://paste.rs/1N4hW) | [tx](https://sepolia.basescan.org/tx/0xbeaececcef412e2504e0db5d71f50246877b4bb7df4614c8f4a95e7de774149c) |

### `REGULATORY_FILING_MONITOR`

| Slug | Class | ≈Reg | YAML | Tx |
|------|-------|-----:|------|-----|
| `filing-sec-submissions` | DETERMINISTIC | 4621 | [yaml](https://paste.rs/3nyab) | [tx](https://sepolia.basescan.org/tx/0xd90ab349d4d5cc29cc1659e0c1e01e713f47de517dc756813abf171ac7ad4ef4) |

### `ROUTE_ETA`

| Slug | Class | ≈Reg | YAML | Tx |
|------|-------|-----:|------|-----|
| `eta-osrm-fossgis` | DETERMINISTIC | 4622 | [yaml](https://paste.rs/QVaFr) | [tx](https://sepolia.basescan.org/tx/0xbca45fd061780193fe2764cbf3171eaf72a04b80e8e5c2ff3ea5fe2dcf236015) |

### `THREAT_IP_REPUTATION`

| Slug | Class | ≈Reg | YAML | Tx |
|------|-------|-----:|------|-----|
| `tip-dshield` | HYBRID | 4623 | [yaml](https://paste.rs/uWpCG) | [tx](https://sepolia.basescan.org/tx/0xbdb989727ff5c5b434b145f0d065b5eaaaaaac704c8db3cd8110a3094676faf4) |
| `tip-feodo` | HYBRID | 4623 | [yaml](https://paste.rs/Pezao) | [tx](https://sepolia.basescan.org/tx/0x49f8fab368c465bc2885341aed138a5570c03626c514abcae78d1f611c0cb88b) |

### `TOKEN_TOTAL_SUPPLY_VERIFY`

| Slug | Class | ≈Reg | YAML | Tx |
|------|-------|-----:|------|-----|
| `supply-blockscout` | DETERMINISTIC | 4624 | [yaml](https://paste.rs/Fv02b) | [tx](https://sepolia.basescan.org/tx/0x8e52f9c3c1800b51ccef1176157457f657b1c2065c4d2c57e6410d6f439c9ad7) |
| `supply-coinpaprika` | DETERMINISTIC | 4651 | [yaml](https://paste.rs/sNEZN) | [tx](https://sepolia.basescan.org/tx/0x8c18928bc09ec580315d8bd02082f6fd4a419b4bbd0873e8c69bab26724c7f5e) |
| `supply-ethplorer` | DETERMINISTIC | 4653 | [yaml](https://paste.rs/c4b3V) | [tx](https://sepolia.basescan.org/tx/0xe51c2228de3957021538dd206fea85efeb19aeeb6436b9cb56d7b4fdfeb694a3) |

### `VALIDATOR_PERFORMANCE_VERIFY`

| Slug | Class | ≈Reg | YAML | Tx |
|------|-------|-----:|------|-----|
| `val-beacon-publicnode` | DETERMINISTIC | 4625 | [yaml](https://paste.rs/HILFr) | [tx](https://sepolia.basescan.org/tx/0x81f9096f89bd80976c9a940990574279a7cc0d80ffa10d86900095fe9ab3e162) |

### `VENDOR_VERIFY`

| Slug | Class | ≈Reg | YAML | Tx |
|------|-------|-----:|------|-----|
| `vendor-vatcomply` | HYBRID | 4626 | [yaml](https://paste.rs/qd5qd) | [tx](https://sepolia.basescan.org/tx/0x3048f87d823a67c99daf42eb8939f77e399f3f0d2b7cc6b09cc44c12b8dd8109) |
