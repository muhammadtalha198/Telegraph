---
intent: CROSS_CHAIN_STATE_VERIFY
slug: xchain-across-suggested-fees
status: pending_review
captured_at: 2026-10-04T18:41:05Z
request_url: https://across.to/api/suggested-fees?token=0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2&destinationChainId=10&amount=1000000000000000000&originChainId=1
content_type: application/json
inputs: |
  across WETH 1→10
intent_description: |
  Proves cryptographic Merkle-Patricia state roots and cross-chain message execution headers between distinct blockchain networks.
answer_requirement: |
  Must convey whether the cross-chain message/transfer executed and its status.
capture_note: |
  fee/ETA quote — not fill status; partial
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "estimatedFillTimeSec": 3,
  "capitalFeePct": "78750000000001",
  "capitalFeeTotal": "78750000000001",
  "relayGasFeePct": "142229181924",
  "relayGasFeeTotal": "142229181924",
  "relayFeePct": "78892229181925",
  "relayFeeTotal": "78892229181925",
  "lpFeePct": "0",
  "timestamp": "1791139163",
  "isAmountTooLow": false,
  "quoteBlock": "26120840",
  "exclusiveRelayer": "0xFD03AbCAdaF3F930fA4E37Eb2f6ea3A44a41b7F0",
  "exclusivityDeadline": 1791139303,
  "spokePoolAddress": "0x5c7BCd6E7De5423a257D81B442095A1a6ced35C5",
  "destinationSpokePoolAddress": "0x6f26Bf09B1C792e3228e5467807a900A503c0281",
  "totalRelayFee": {
    "pct": "78892229181925",
    "total": "78892229181925"
  },
  "relayerCapitalFee": {
    "pct": "78750000000001",
    "total": "78750000000001"
  },
  "relayerGasFee": {
    "pct": "142229181924",
    "total": "142229181924"
  },
  "lpFee": {
    "pct": "0",
    "total": "0"
  },
  "internalizedSwapFee": {
    "pct": "0",
    "total": "0"
  },
  "limits": {
    "minDeposit": "185096750071262",
    "maxDeposit": "1269146225598913719223",
    "maxDepositInstant": "41068653013723339825",
    "maxDepositShortDelay": "1269146225598913719223",
    "recommendedDepositInstant": "41068653013723339825"
  },
  "fillDeadline": "1791146363",
  "outputAmount": "999921107770818075",
  "inputToken": {
    "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    "symbol": "WETH",
    "decimals": 18,
    "chainId": 1
  },
  "outputToken": {
    "address": "0x4200000000000000000000000000000000000006",
    "symbol": "WETH",
    "decimals": 18,
    "chainId": 10
  },
  "id": "98xmm-1791139265389-3eaf9d5b0b17"
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
