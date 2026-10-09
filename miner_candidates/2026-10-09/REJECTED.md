# Rejected candidates — 2026-10-09

One clearest reason each. "Blocked here" = fails from this run's IP/network; may work elsewhere (marked UNVERIFIED).

| Candidate | Intent | Reason |
|-----------|--------|--------|
| OKX (`okx.com/api/v5/market/ticker`) | CRYPTO_PRICE | Connection reset from this IP (geo-blocked). UNVERIFIED — cannot test reliably here. |
| CoinCap (`api.coincap.io`) | CRYPTO_PRICE | DNS does not resolve — API discontinued/moved to a keyed service. Not free/no-key. |
| AscendEX (`ascendex.com/api/pro/v1/ticker`) | CRYPTO_PRICE | HTTP Access Denied from this IP. UNVERIFIED. |
| BitMart (`api-cloud.bitmart.com`) | CRYPTO_PRICE | DNS/host blocked from this network. UNVERIFIED. |
| ProBit (`api.probit.com`) | CRYPTO_PRICE | Cloudflare bot challenge (not a clean API response). ToS/anti-bot. |
| CoinEx (`api.coinex.com/v1/market/ticker`) | CRYPTO_PRICE | v1 endpoint returns "invalid params"; shape not usable as-is. |
| Bitvavo (`api.bitvavo.com/v2/ticker/price`) | CRYPTO_PRICE | Only BTC-EUR markets; wrong quote vs the USD consensus (quote mismatch). |
| CoinMetro (`api.coinmetro.com/exchange/prices`) | CRYPTO_PRICE | Returns one big list of all pairs; the asked pair is not directly addressable (positional-retrieval, not askable). |
| Bit2C (`bit2c.co.il`) | CRYPTO_PRICE | Bot-walled HTML + ILS-only market. |
| **CEX.IO** (`cex.io/api/last_price/BTC/USD`) | CRYPTO_PRICE | **Failed our verifier: disagreed with consensus** — returned $68,991 for BTC and $3,750 for ETH (stale/thin BTC-USD market) while consensus was ~$82,418 / ~$2,494. Correct rejection. |
| Blockchair (`api.blockchair.com/ethereum/...`) | ONCHAIN / TOKEN_SUPPLY | IP blacklisted after light use; requires a paid/registered API key. Not free. |
| Mullvad DoH (`dns.mullvad.net/dns-query`) | DNS_RECORD_LOOKUP | Empty body for the dns-json query (no usable JSON answer). |
| Quad9 DoH (`dns.quad9.net:5053/dns-query`) | DNS_RECORD_LOOKUP | Connection timed out (>8s) from this network. UNVERIFIED. |
