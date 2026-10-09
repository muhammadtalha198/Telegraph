---
intent: CRYPTO_YIELD_RATE
slug: yld-coinbase-cbeth
status: approved
captured_at: 2026-10-08T04:41:55Z
request_url: https://api.exchange.coinbase.com/wrapped-assets/CBETH
content_type: application/json
inputs: |
  {}
intent_description: |
  Tracks annualized percentage yields (APY), staking reward rates, and lending pool yields across DeFi protocols.
answer_requirement: |
  Must return the current annualized yield, as a percent number, for the protocol-specific pool/asset named by the test (ETH liquid-staking rate for cbETH; USDC lending/vault net APY on Ethereum).
capture_note: |
  (none)
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the annualized yield (apy) for the CBETH pool, which matches the intent of the crypto yield rate query."
reviewed_at: 2026-10-08T04:55:07Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "id": "CBETH",
  "circulating_supply": "165957.837052176858084481",
  "total_supply": "373334.0782232124394134",
  "conversion_rate": "1.1411533869922937",
  "apy": "0.0235",
  "redeem_time_estimate_days": "16.2"
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the annualized yield (apy) for the CBETH pool, which matches the intent of the crypto yield rate query._
