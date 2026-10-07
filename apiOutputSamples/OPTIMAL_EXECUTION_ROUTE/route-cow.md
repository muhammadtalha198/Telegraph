---
intent: OPTIMAL_EXECUTION_ROUTE
slug: route-cow
status: approved
captured_at: 2026-10-05T09:27:49Z
request_url: https://api.cow.fi/mainnet/api/v1/quote
content_type: application/json
inputs: |
  {"weth": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", "usdc": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", "amount": "1000000000000000000", "addr": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"}
intent_description: |
  Determines optimal multi-venue order execution routing to minimize slippage, exchange fees, and market impact.
answer_requirement: |
  Must return the best swap route / expected output amount for the trade asked.
capture_note: |
  golden-test PASS: CoW Protocol
reviewer_note: "auto_review: [0.80|heuristic+llm] The API response provides the price of the sell token (WETH) in terms of the buy token (USDC). | heuristic: Route quote fields in body"
reviewed_at: 2026-10-05T12:36:16Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 0.800
---

## Raw API output

```json
{
  "quote": {
    "sellToken": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
    "buyToken": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    "receiver": null,
    "sellAmount": "999806318615336778",
    "buyAmount": "2717893685",
    "validTo": 1791194261,
    "appData": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "feeAmount": "193681384663222",
    "gasAmount": "249698",
    "gasPrice": "775662539",
    "sellTokenPrice": "1",
    "kind": "sell",
    "partiallyFillable": false,
    "sellTokenBalance": "erc20",
    "buyTokenBalance": "erc20",
    "signingScheme": "eip712"
  },
  "from": "0xd8da6bf26964af9d7eed9e03e53415d37aa96045",
  "expiration": "2026-10-05T09:29:41.052386088Z",
  "id": 1605402973,
  "verified": true,
  "protocolFeeBps": "2"
}
```

## Why this matches (or not)

_[0.80|heuristic+llm] The API response provides the price of the sell token (WETH) in terms of the buy token (USDC). | heuristic: Route quote fields in body_
