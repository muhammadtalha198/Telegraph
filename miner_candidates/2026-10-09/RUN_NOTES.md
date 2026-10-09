# Run notes — 2026-10-09

## What this round did
Found and **live-verified** 9 new free miners through our own `minercheck` verifier (unchanged),
across the 4 spec-backed intents where the verifier can actually prove correctness. 5 new crypto
exchanges, 2 new DNS resolvers, 1 stock source, 1 weather source. 13 rejected.

## Key constraint discovered
Our verifier only deterministically PASSes an intent that has a spec in `intents/` (19 today).
For the ~52 required intents without a spec, the gate fails closed, so **no candidate can be
"verified by our code" there yet.** Finding miners for those intents is blocked on writing the
specs first (see `docs/CATALOG_COVERAGE.md`), not on finding APIs.

## Search queries / sources that worked
- "free crypto exchange public ticker API no key" → exchange API docs (Phemex, XT, Bitrue, HitBTC, DigiFinex).
- Directly tried each exchange's documented public `ticker`/`ticker/price` endpoint (no key, no account).
- "public DoH JSON resolver" → dns.sb (doh.sb), DNSPod (doh.pub), Mullvad, Quad9.
- "free stock quote API no key" → stockanalysis.com internal quote endpoint.
- "free weather API no key Germany DWD" → Bright Sky (brightsky.dev).

## What worked vs not
- **Worked:** exchange public ticker endpoints are the richest vein of free, no-key, independently
  verifiable miners — each exchange is a distinct order book, so they pass E3 cross-check.
- **Didn't:** many exchanges are geo-blocked or Cloudflare-bot-walled from this IP (OKX, AscendEX,
  BitMart, ProBit) — can't verify here. Blockchair/CoinCap now need keys. DoH JSON needs an Accept header.

## Ideas to reach 1000 (quality-first)
1. **Crypto price has dozens more clean exchanges** — each new one is a verified miner in minutes
   (one spec, many sources). Fastest path to volume that still passes E3.
2. **Write specs for the ~14 "feasible" required intents** in `docs/CATALOG_COVERAGE.md` (CVSS triage,
   crypto-transfer, SSL cert, gas price, route ETA, email security, threat-IP, etc.) — each unlocks
   verification for all its existing registered miners at once.
3. **Weather/time/DNS** have more public no-key providers (regional met services, NTP-backed time
   APIs, national DoH resolvers) — good for provider diversity (one outage ≠ many miners).
4. Directories still to mine: github.com/public-apis, APIs.guru, government open-data (weather, FX,
   holidays, transport), national statistics agencies (macro), block explorers (on-chain/token).
5. **Weak intents right now:** everything without a spec. Volume is cheap on crypto; the binding
   constraint for breadth is spec coverage, not API supply.
