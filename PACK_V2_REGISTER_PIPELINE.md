# Pack → Semantic V2 register pipeline

Updated: **2026-10-05 07:15 UTC**

Source: `files/Intent_Coverage_and_Candidates.xlsx` (372 candidates)

## Pipeline used (same as V2)

1. Classify + dedup (slug / host / publisher per intent)
2. Live smoke GET
3. `capture_api_output.py` → `apiOutputSamples/`
4. Sample approve (distinct publisher; skip Open-Meteo model variants)
5. `generate_yamls_from_approved_samples.py`
6. `register-miner-v2.sh` via `register_approved_v2_batch.py` (gates: approved sample + validate YAML + live probe + hosted byte-match)

## Classification summary (372)

| Status | Count | Action |
|--------|------:|--------|
| `ALREADY_REGISTERED` | 214 | Marked — **not** re-registered |
| `SAME_HOST_AS_REGISTERED` | 1 | Same source — skip |
| `NEEDS_API_KEY` | 70 | Deferred (see `files/KEYS_NEEDED.md`) |
| `SKIP_POST` | 4 | Capture is GET-only |
| `ELIGIBLE` → smoke | 83 | Live tested |
| Smoke PASS → capture | 44 | Samples written |
| Approved (distinct source) | 41 | YAMLs + V2 register |
| **REGISTERED (this run)** | **41** | On-chain via Semantic V2 |

## Already registered (not re-registered)

These pack candidates matched an existing `intentYamls/` slug or `possible_existing` slug. Full list in queue file.

Count: **214** — see `out/pack_v2_queue.jsonl` where `status=ALREADY_REGISTERED`.

## Newly registered (pack V2)

| Intent | Slug | Reg ID | YAML | TX |
|--------|------|-------:|------|----|
| `CRYPTO_PRICE` | `cp-binance` | 4560 | [yaml](https://paste.rs/N44h7) | [tx](https://sepolia.basescan.org/tx/0xa92373be8e1611e8) |
| `CRYPTO_PRICE` | `cp-bitfinex` | 4593 | [yaml](https://paste.rs/ks096) | [tx](https://sepolia.basescan.org/tx/0xacf896ad1d09e487cf2530271fc3e7e1f4789224c059e42c814cc17d9a751532) |
| `CRYPTO_PRICE` | `cp-bitget` | 4564 | [yaml](https://paste.rs/OzzeW) | [tx](https://sepolia.basescan.org/tx/0x1c75316024fa50e50cc147d7e3a9a373521b17c7091577fde01f2e4236ead9fc) |
| `CRYPTO_PRICE` | `cp-bitstamp` | 4562 | [yaml](https://paste.rs/feCXg) | [tx](https://sepolia.basescan.org/tx/0xe78e0f8b1f5c7c3cc173270762d92477f65ccaee337a6d66c76c3aec81a4d444) |
| `CRYPTO_PRICE` | `cp-bybit` | 4564 | [yaml](https://paste.rs/Bx9LD) | [tx](https://sepolia.basescan.org/tx/0x636c8f68e55b4f1976cc89398a97294cca7b3741f819005a480761e501b15141) |
| `CRYPTO_PRICE` | `cp-coinbase` | 4566 | [yaml](https://paste.rs/8UYTA) | [tx](https://sepolia.basescan.org/tx/0xa3f4f0d908068ebce237274fbdc5a18f7a376c34a6c73e6175d61b93c15eeee6) |
| `CRYPTO_PRICE` | `cp-coingecko` | 4566 | [yaml](https://paste.rs/U7QbZ) | [tx](https://sepolia.basescan.org/tx/0x279b46f3d15ad44b724a90be599a23c3c146977a404c35ce7763542e2ef00ac1) |
| `CRYPTO_PRICE` | `cp-cryptocom` | 4567 | [yaml](https://paste.rs/1Hy5P) | [tx](https://sepolia.basescan.org/tx/0xab2541865c8c521176440af94642ee2dea2747f7819126f8caf5eb7e78abf0f6) |
| `CRYPTO_PRICE` | `cp-defillama` | 4568 | [yaml](https://paste.rs/dcORc) | [tx](https://sepolia.basescan.org/tx/0x449e33f1085a8d6b274c61b177e316336b2f394d7dd4746424b7377c700e8c52) |
| `CRYPTO_PRICE` | `cp-gate` | 4570 | [yaml](https://paste.rs/Tddeh) | [tx](https://sepolia.basescan.org/tx/0x06212f2a39496dd5366625eeb12ae86d07ac9452ba6ed4bccea8b9aac2d39dca) |
| `CRYPTO_PRICE` | `cp-gemini` | 4582 | [yaml](https://paste.rs/MPQ4u) | [tx](https://sepolia.basescan.org/tx/0x881d7056558cf8039784539ac2b0d1a7ac32f774d63b2b5e56acb67eca6c961a) |
| `CRYPTO_PRICE` | `cp-htx` | 4583 | [yaml](https://paste.rs/4aPNE) | [tx](https://sepolia.basescan.org/tx/0xab6b373b263a8fce1dfd24770a2378c92817d11e83ef5beb2b70190a5eafc8a3) |
| `CRYPTO_PRICE` | `cp-kraken` | 4584 | [yaml](https://paste.rs/ObxHP) | [tx](https://sepolia.basescan.org/tx/0x2c161996e8b349e55c56a319a3e05ff154343c1304eb63be451bc4af7786b47a) |
| `CRYPTO_PRICE` | `cp-kucoin` | 4585 | [yaml](https://paste.rs/XKzw1) | [tx](https://sepolia.basescan.org/tx/0x944e972223993fa8a8f4d0f139a850f20c55392c2bb9b49a73a240700ed8e48c) |
| `CRYPTO_PRICE` | `cp-mexc` | 4570 | [yaml](https://paste.rs/SZcu7) | [tx](https://sepolia.basescan.org/tx/0x1abfa47736187c94c48ceed453d7e84f141a075c331e845dd986d7e6cb8881ef) |
| `CRYPTO_PRICE` | `cp-redstone` | 4571 | [yaml](https://paste.rs/qDE18) | [tx](https://sepolia.basescan.org/tx/0x029707878fdf3a39930f1c10247dc1b39259eedab205204befae9b9fcec69d19) |
| `DNS_RECORD_LOOKUP` | `dns-dnspod` | 4572 | [yaml](https://paste.rs/H5RHZ) | [tx](https://sepolia.basescan.org/tx/0xb8bc490bb5dacac6dd4b076521f6509109a835a0fbfe84ed155ac1f7190f3ac8) |
| `DNS_RECORD_LOOKUP` | `dns-hackertarget` | 4587 | [yaml](https://paste.rs/HsaLy) | [tx](https://sepolia.basescan.org/tx/0xd16eec54d230e0ff6a99514dd614db65a93692dcf88f5ae162e8c3d739ee00d8) |
| `CONTENT_EXTRACTION` | `extract-microlink` | 4560 | [yaml](https://paste.rs/XS2l6) | [tx](https://sepolia.basescan.org/tx/0x90709fab81cedda90ae9491869cf6e06c7bf4fb2e44c5e606279a023c8ab7f7f) |
| `REGULATORY_FILING_MONITOR` | `filing-esma-esef` | 4588 | [yaml](https://paste.rs/2rJSX) | [tx](https://sepolia.basescan.org/tx/0x6ad0d27d8a07ec15e2f19688fece7f8ea8a233ae97046147b7d401d9431ec888) |
| `GRAMMAR_SPELL_CHECK` | `grammar-datamuse` | 4587 | [yaml](https://paste.rs/zCtBn) | [tx](https://sepolia.basescan.org/tx/0xd1c1e9ffe02b775314479fa1f4c63a78c6563b0379f1024a42b3bd00656a5f33) |
| `GRAMMAR_SPELL_CHECK` | `grammar-grammarbot` | 4595 | [yaml](https://paste.rs/ubuZ8) | [tx](https://sepolia.basescan.org/tx/0x2c02df091a5e52c109a6112f24efd784da0a6ce0eee758000859b5818a3174e7) |
| `MINING_HASHPRICE_VERIFY` | `hash-blockchain-stats` | 4575 | [yaml](https://paste.rs/eePf7) | [tx](https://sepolia.basescan.org/tx/0x74e8893a31449611832a2449ab6af95dc0a9eb7fdebd6c8833582350a1d5f465) |
| `MINING_HASHPRICE_VERIFY` | `hash-whattomine` | 4575 | [yaml](https://paste.rs/SpbGh) | [tx](https://sepolia.basescan.org/tx/0x1378b0862d3b16d659aac2a261bec91e16d52f54deb10b6e7e667c793f3b433e) |
| `LOAN_INTEREST_RATE_QUOTE` | `loan-nyfed-sofr` | 4599 | [yaml](https://paste.rs/IQ8Rs) | [tx](https://sepolia.basescan.org/tx/0x3101c2a0723d8e56a7b70785273fc2562ebb42b520ab3d400936f4c36483ac15) |
| `LOAN_INTEREST_RATE_QUOTE` | `loan-riksbank` | 4562 | [yaml](https://paste.rs/dzcDm) | [tx](https://sepolia.basescan.org/tx/0x7b5a0db45cf244c29971d95caaade22d2f0992b299fa0599935a903965d1ecad) |
| `LOAN_INTEREST_RATE_QUOTE` | `loan-treasury-yields` | 4573 | [yaml](https://paste.rs/KWpaX) | [tx](https://sepolia.basescan.org/tx/0x7f60a1cfbdf356d6128cc37f66fb40ab4059cc93b3895fd387a56a0f8d042ea1) |
| `PORT_SCAN_AUDIT` | `port-hackertarget-nmap` | 4597 | [yaml](https://paste.rs/bfw9i) | [tx](https://sepolia.basescan.org/tx/0x5d0fa89ba72512ed402b3a6f83d8319c75e6a292b8d225e9cde1e2585d5fefb1) |
| `WEB_SEARCH` | `search-duckduckgo-ia` | 4580 | [yaml](https://paste.rs/OTpIz) | [tx](https://sepolia.basescan.org/tx/0x2e4442a9cf2ef4fe5ee69db7a311d34d75055719bb5103c2eea202200335948e) |
| `WEB_SEARCH` | `search-wikipedia` | 4582 | [yaml](https://paste.rs/MH93M) | [tx](https://sepolia.basescan.org/tx/0x1f475aede7eb115f13926e41a79da5fa64c1019140a3a9693e734e5e0b266486) |
| `SSL_VERIFICATION` | `ssl-networkcalc` | 4589 | [yaml](https://paste.rs/qK8H8) | [tx](https://sepolia.basescan.org/tx/0x9b9b8c0ccb614300c6004b3f97b8b5fce76b6917122e7cbd911c5a6872bc772d) |
| `SSL_VERIFICATION` | `ssl-ssllabs` | 4591 | [yaml](https://paste.rs/nmEWw) | [tx](https://sepolia.basescan.org/tx/0x23ed7cd67139e31cdab4a7af8bea2b9fa8bc089edfa9d8f12e2818908daf5868) |
| `STOCK_PRICE` | `stock-cnbc` | 4577 | [yaml](https://paste.rs/brUt6) | [tx](https://sepolia.basescan.org/tx/0xe988b35ab7f319b06b9ad305324a918f576bb42e9cd6586b9433ff8f34937b1b) |
| `STOCK_PRICE` | `stock-nasdaq` | 4592 | [yaml](https://paste.rs/ntHfH) | [tx](https://sepolia.basescan.org/tx/0x0d99626a32a00dd8a92a1d1ee06762690dba5643d61a3040f9496ec0997ae0eb) |
| `STOCK_PRICE` | `stock-yahoo` | 4577 | [yaml](https://paste.rs/ISSj5) | [tx](https://sepolia.basescan.org/tx/0x8d31fbe56138b68d2d4d67d768dc72bf8770b4cdaa7b20db32fe9557c60bedd0) |
| `TOKEN_TOTAL_SUPPLY_VERIFY` | `supply-coingecko` | 4593 | [yaml](https://paste.rs/JENlv) | [tx](https://sepolia.basescan.org/tx/0x248b91b7414e3495300562a60842e9c1edbc645a7d095d22078c884d6bda4c42) |
| `LANGUAGE_TRANSLATION` | `tr-popcat` | 4595 | [yaml](https://paste.rs/tiOK7) | [tx](https://sepolia.basescan.org/tx/0xc76ed12c82d241ea4c98e1da2324b7815803ef9ccd0f8654bf614be9a56edd97) |
| `WEATHER_CHECK` | `wx-7timer` | 4597 | [yaml](https://paste.rs/8CUel) | [tx](https://sepolia.basescan.org/tx/0x0fedd89c7c9cdbf5399b4b98dab137226bf2c54b2ecf05385fca23a92fed6a50) |
| `WEATHER_CHECK` | `wx-metno` | 4598 | [yaml](https://paste.rs/RIvnV) | [tx](https://sepolia.basescan.org/tx/0x9f214edf9f6794e9bec7391cac8d4da3b1c0fdb3bf65bd8812fc826b194bcb3e) |
| `WEATHER_CHECK` | `wx-openmeteo` | 4578 | [yaml](https://paste.rs/wAHqA) | [tx](https://sepolia.basescan.org/tx/0x9de975be2812c2e8ff098c489e3c2e7c10d130ae407ba391594e24c9ed23544c) |
| `WEATHER_CHECK` | `wx-wttr` | 4580 | [yaml](https://paste.rs/UwAKo) | [tx](https://sepolia.basescan.org/tx/0xf64df250b05c78368d5da6f8134ad82edcaae50ad99f704825af944d42cb9ac5) |

## Skipped same-source / variants

- Open-Meteo weather model variants (`wx-openmeteo-gfs/icon/ecmwf`) — one Open-Meteo miner only (`wx-openmeteo`)
- Host/publisher collisions with existing Active/Pre-active YAMLs
- Needs API key / POST (no silent register)

## Artifacts

| File | Role |
|------|------|
| `PACK_V2_REGISTER_PIPELINE.md` | This tracker |
| `out/pack_v2_queue.jsonl` | Per-candidate status |
| `out/PACK_V2_REGISTER.jsonl` | Register results |
| `out/PACK_V2_REGISTER.md` | Batch register notes |
| `scripts/pack_v2_pipeline.py` | Classify / smoke / capture |
| `scripts/v2_intent_folders.py` | Intent → YAML folder map |

