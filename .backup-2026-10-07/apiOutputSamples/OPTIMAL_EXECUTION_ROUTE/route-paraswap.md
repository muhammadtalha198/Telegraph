---
intent: OPTIMAL_EXECUTION_ROUTE
slug: route-paraswap
status: approved
captured_at: 2026-10-05T09:27:49Z
request_url: https://api.paraswap.io/prices?srcToken=0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2&destToken=0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48&amount=1000000000000000000&srcDecimals=18&destDecimals=6&side=SELL&network=1
content_type: application/json
inputs: |
  {"weth": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", "usdc": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", "amount": "1000000000000000000", "addr": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"}
intent_description: |
  Determines optimal multi-venue order execution routing to minimize slippage, exchange fees, and market impact.
answer_requirement: |
  Must return the best swap route / expected output amount for the trade asked.
capture_note: |
  golden-test PASS: ParaSwap/Velora
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the expected output amount for the trade asked, which is 2718035823 USDC. | heuristic: Swap route / price route present"
reviewed_at: 2026-10-05T12:33:34Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "priceRoute": {
    "blockNumber": 26125268,
    "network": 1,
    "srcToken": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
    "srcDecimals": 18,
    "srcAmount": "1000000000000000000",
    "destToken": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    "destDecimals": 6,
    "destAmount": "2718035823",
    "bestRoute": [
      {
        "percent": 100,
        "swaps": [
          {
            "srcToken": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
            "srcDecimals": 18,
            "destToken": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "destDecimals": 6,
            "swapExchanges": [
              {
                "exchange": "uniswapv3",
                "srcAmount": "1000000000000000000",
                "destAmount": "2718035823",
                "percent": 100,
                "poolAddresses": [
                  "0xe0554a476a092703abdb3ef35c80e0d76d32939f"
                ],
                "poolIdentifiers": [
                  "uniswapv3_0xe0554a476a092703abdb3ef35c80e0d76d32939f"
                ],
                "targetExchange": "0xe592427a0aece92de3edee1f18e0157c05861564",
                "data": {
                  "apiGo": true,
                  "blockNumber": 26125268,
                  "source": "L1",
                  "path": [
                    {
                      "tokenIn": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
                      "tokenOut": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
                      "fee": "100",
                      "currentFee": "100"
                    }
                  ],
                  "gasUSD": "0.030676"
                }
              }
            ]
          }
        ]
      }
    ],
    "gasCostUSD": "0.062058",
    "gasCost": "202300",
    "side": "SELL",
    "version": "5",
    "contractAddress": "0xDEF171Fe48CF0115B1d80b88dc8eAB59176FEe57",
    "tokenTransferProxy": "0x216b4b4ba9f3e719726886d34a177484278bfcae",
    "contractMethod": "directUniV3Swap",
    "partnerFee": 0.01,
    "srcUSD": "2719.9200000000",
    "destUSD": "2717.7585833461",
    "destAmountAfterFee": "2717764019",
    "partner": "anon",
    "maxImpactReached": false,
    "hmac": "cba33cdb288ed28e7d00f8b8812007a880a8a2f7"
  }
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the expected output amount for the trade asked, which is 2718035823 USDC. | heuristic: Swap route / price route present_
