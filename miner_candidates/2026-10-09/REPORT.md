# New miner candidates — 2026-10-09

**Method:** each candidate was called live on ≥2–3 real inputs and run through our verifier
(`minercheck`) **unchanged** — added as a source in the matching `intents/<INTENT>.yaml` and
checked that it extracts (E1), is the right answer type (E5), passes sanity/freshness (E2/E4),
and **agrees with the existing independent consensus** (E3). "Verified" below means the candidate
showed `agreed` against the already-registered sources. No verification code was modified.

**Scope note:** our verifier only produces a real PASS for the 19 intents that already have a spec.
So all accepted candidates are for spec-backed intents (crypto price, DNS, stock, weather). Intents
without a spec cannot be verified by our code yet (the gate fails closed) — not covered this round.

**Accepted: 9** across 4 intents · **Rejected: 13** (see REJECTED.md).

| # | Intent | Provider | Endpoint | Key? | Rate limit (published) | Latency | Verification (E1/E5/E2/E4/E3) | Dup check | Licence/ToS | Confidence |
|---|--------|----------|----------|------|------------------------|---------|-------------------------------|-----------|-------------|------------|
| 1 | CRYPTO_PRICE | Phemex | `api.phemex.com/md/spot/ticker/24hr?symbol=sBTCUSDT` | N | not published; light public use | <1s | PASS all; agreed BTC/ETH/SOL | new publisher (not in 26 registered) | public market data; automated use OK | high |
| 2 | CRYPTO_PRICE | XT.com | `sapi.xt.com/v4/public/ticker/price?symbol=btc_usdt` | N | public | <1s | PASS all; agreed BTC/ETH/SOL | new publisher | public market data | high |
| 3 | CRYPTO_PRICE | Bitrue | `openapi.bitrue.com/api/v1/ticker/price?symbol=BTCUSDT` | N | public | <1s | PASS all; agreed BTC/ETH/SOL | new publisher | public market data | high |
| 4 | CRYPTO_PRICE | HitBTC | `api.hitbtc.com/api/3/public/ticker/BTCUSDT` | N | public | <1s | PASS all; agreed BTC/ETH/SOL | new publisher | public market data | high |
| 5 | CRYPTO_PRICE | DigiFinex | `openapi.digifinex.com/v3/ticker?symbol=btc_usdt` | N | public | <1s | PASS all; agreed BTC/ETH | new publisher | public market data | high |
| 6 | DNS_RECORD_LOOKUP | dns.sb | `doh.sb/dns-query?name=&type=` (Accept: application/dns-json) | N | public resolver | <1s | PASS; agreed on stable hostnames (geo-rotating e.g. github.com legitimately differs) | new resolver (not cloudflare/google/alidns) | public DoH | **med** (needs Accept header — see caveat) |
| 7 | DNS_RECORD_LOOKUP | DNSPod (doh.pub) | `doh.pub/dns-query?name=&type=` (Accept: application/dns-json) | N | public resolver | <1s | PASS; agreed dns.google/example.com/github.com | new resolver | public DoH | **med** (needs Accept header) |
| 8 | STOCK_PRICE | stockanalysis.com | `stockanalysis.com/api/quotes/s/{symbol}` | N | public | <1s | PASS all; agreed AAPL/MSFT/KO | new publisher (not yahoo/nasdaq/cnbc) | site API; confirm ToS for sustained automated use | med |
| 9 | WEATHER_CHECK | Bright Sky (DWD) | `api.brightsky.dev/current_weather?lat=&lon=` | N | public, generous | <1s | PASS; agreed Berlin/Munich/Hamburg | new publisher (DWD, not open-meteo/met.no/metar) | CC-licensed DWD data, free | high **(Germany + borders only)** |

## To let our register gate verify each one (add as a spec source)
A node-format YAML (in this folder) is what gets registered, but the **gate** also needs the miner
mapped as a source in its spec. Add these `sources:` entries (then `minercheck gate --file <yaml> --intent <X>` passes):

- `intents/CRYPTO_PRICE.yaml` — add, each with `kind: cex` and `miner: {slug: <slug>, question: {asset: BTC}}`:
  - phemex `value: [{json: result.lastEp, scale: "0.00000001", unit: USDT}]` url `.../ticker/24hr?symbol=s{symbol}USDT`
  - xt `value: [{json: "result.0.p", unit: USDT}]` url `.../ticker/price?symbol={symbol_lower}_usdt`
  - bitrue `value: [{json: price, unit: USDT}]` url `.../ticker/price?symbol={symbol}USDT`
  - hitbtc `value: [{json: last, unit: USDT}]` url `.../public/ticker/{symbol}USDT`
  - digifinex `value: [{json: "ticker.0.last", unit: USDT}]` url `.../v3/ticker?symbol={symbol_lower}_usdt`
- `intents/DNS_RECORD_LOOKUP.yaml` — `kind: dns_resolver`, header `accept: application/dns-json`,
  `value: [{json: Answer, each: data, where: {type: "{rtype_num}"}}]`, slugs dns-dnssb / dns-dnspod.
- `intents/STOCK_PRICE_QUOTE.yaml` — `kind: price_aggregator`, `miner: {slug: stock-stockanalysis, question: {symbol: AAPL}}`, `value: [{json: data.p, unit: USD}]`.
- `intents/WEATHER_CHECK.yaml` — `kind: weather_station`, `miner: {slug: wx-brightsky-de, question: {location: "52.52,13.41"}}`, `value: [{json: weather.temperature, unit: C}]`, `timestamp: [{json: weather.timestamp}]`.

## Caveats (be direct)
- **DNS (6,7):** these DoH endpoints require an `Accept: application/dns-json` request header. Our
  verifier sends it; confirm the **node** can send a static Accept header from a miner YAML before
  registering, or route via the truth proxy. Until confirmed, treat as medium confidence.
- **Bright Sky (9):** only covers Germany + border areas. It verifies for German coordinates and
  errors elsewhere (the node falls back to other weather miners). Register as a regional source.
- **stockanalysis.com (8):** a site API, not a documented public API — confirm ToS allows sustained
  automated use before relying on it.
- **IDs 190201–190209** are placeholders; confirm uniqueness against live `minerCount`/registry before register.
