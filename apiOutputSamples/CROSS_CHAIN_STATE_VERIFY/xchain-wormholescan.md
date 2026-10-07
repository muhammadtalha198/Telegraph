---
intent: CROSS_CHAIN_STATE_VERIFY
slug: xchain-wormholescan
status: pending_review
captured_at: 2026-10-05T09:28:52Z
request_url: https://api.wormholescan.io/api/v1/operations?pageSize=1
content_type: application/json
inputs: |
  {}
intent_description: |
  Proves cryptographic Merkle-Patricia state roots and cross-chain message execution headers between distinct blockchain networks.
answer_requirement: |
  Must return verifiable state roots / cross-chain message status between networks.
capture_note: |
  golden-test PASS: Wormholescan
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "operations": [
    {
      "id": "2/000000000000000000000000d78d199f8c402e7b5cc2abe278df0412400a3bae/259605",
      "emitterChain": 2,
      "emitterAddress": {
        "hex": "000000000000000000000000d78d199f8c402e7b5cc2abe278df0412400a3bae",
        "native": "0xd78d199f8c402e7b5cc2abe278df0412400a3bae"
      },
      "sequence": "259605",
      "content": {
        "standarizedProperties": {
          "appIds": null,
          "fromChain": 0,
          "fromAddress": "",
          "toChain": 0,
          "toAddress": "",
          "tokenChain": 0,
          "tokenAddress": "",
          "amount": "",
          "feeAddress": "",
          "feeChain": 0,
          "fee": "",
          "normalizedDecimals": null
        },
        "executorRequest": null
      },
      "sourceChain": {
        "chainId": 2,
        "timestamp": "2026-10-05T09:28:35Z",
        "transaction": {
          "txHash": "0x4cafd2890b0ee9574f811ea28d5b187fda8294b9d71f05e723a0f6ef466f95c4"
        },
        "from": "0x754dcfb2861547015b221e963b4133a71dbdc024",
        "status": "confirmed",
        "fee": "0.000166612850436595",
        "gasTokenNotional": "2717.64",
        "feeUSD": "0.4527937468605080358",
        "balanceChanges": [
          {
            "amount": "-240029200",
            "recipient": "0x754dcfb2861547015b221e963b4133a71dbdc024",
            "tokenAddress": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"
          }
        ],
        "isSolanaShim": false
      }
    }
  ]
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
