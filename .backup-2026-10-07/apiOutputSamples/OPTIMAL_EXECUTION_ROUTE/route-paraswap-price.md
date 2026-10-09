---
intent: OPTIMAL_EXECUTION_ROUTE
slug: route-paraswap-price
status: approved
captured_at: 2026-10-04T18:40:52Z
request_url: https://apiv5.paraswap.io/prices?srcToken=0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE&destToken=0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48&amount=1000000000000000000&srcDecimals=18&destDecimals=6&side=SELL&network=1
content_type: application/json
inputs: |
  1 ETH->USDC
intent_description: |
  Determines optimal multi-venue order execution routing to minimize slippage, exchange fees, and market impact.
answer_requirement: |
  Must convey the best swap route / output amount for the trade asked.
capture_note: |
  (none)
reviewer_note: "auto_review: [0.85|heuristic] Swap route / price route present"
reviewed_at: 2026-10-04T18:41:49Z
---

## Raw API output

```json
{
  "priceRoute": {
    "blockNumber": 26120847,
    "network": 1,
    "srcToken": "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
    "srcDecimals": 18,
    "srcAmount": "1000000000000000000",
    "destToken": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    "destDecimals": 6,
    "destAmount": "2700876236",
    "bestRoute": [
      {
        "percent": 100,
        "swaps": [
          {
            "srcToken": "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
            "srcDecimals": 18,
            "destToken": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
            "destDecimals": 6,
            "swapExchanges": [
              {
                "exchange": "uniswapv3",
                "srcAmount": "1000000000000000000",
                "destAmount": "2700876236",
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
                  "blockNumber": 26120847,
                  "source": "L1",
                  "path": [
                    {
                      "tokenIn": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
                      "tokenOut": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
                      "fee": "100",
                      "currentFee": "100"
                    }
                  ],
                  "gasUSD": "0.034010"
                }
              }
            ]
          }
        ]
      }
    ],
    "gasCostUSD": "0.062000",
    "gasCost": "182300",
    "side": "SELL",
    "version": "5",
    "contractAddress": "0xDEF171Fe48CF0115B1d80b88dc8eAB59176FEe57",
    "tokenTransferProxy": "0x216b4b4ba9f3e719726886d34a177484278bfcae",
    "contractMethod": "directUniV3Swap",
    "partnerFee": 0.01,
    "srcUSD": "2700.7900000000",
    "destUSD": "2700.7060807971",
    "destAmountAfterFee": "2700606148",
    "partner": "anon",
    "maxImpactReached": false,
    "hmac": "e6507e2aedc866c175e43a636d0e5795bd0f48b9"
  }
}
```

## Why this matches (or not)

_[0.85|heuristic] Swap route / price route present_
