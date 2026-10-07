---
intent: CROSS_CHAIN_STATE_VERIFY
slug: xchain-across
status: pending_review
captured_at: 2026-10-05T09:28:52Z
request_url: https://app.across.to/api/deposits?limit=1
content_type: application/json
inputs: |
  {}
intent_description: |
  Proves cryptographic Merkle-Patricia state roots and cross-chain message execution headers between distinct blockchain networks.
answer_requirement: |
  Must return verifiable state roots / cross-chain message status between networks.
capture_note: |
  golden-test PASS: Across
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
[
  {
    "depositAddress": null,
    "sweepTxnRef": null,
    "bridgedInputToken": null,
    "bridgedInputAmount": null,
    "depositRefundAddress": null,
    "actionsTargetRecipient": null,
    "actionsTargetToken": null,
    "actionsTargetAmount": null,
    "actionsTargetTxnRef": null,
    "actionsTargetBlockTimestamp": null,
    "id": 24108935,
    "relayHash": "0x61f791c60b6e46c4f53907c7c9acb709763f07c0362714fe71f1d904b30de742",
    "depositId": "1162035",
    "originChainId": 56,
    "destinationChainId": 1,
    "depositor": "0x144c5fb302dbAa789FC59bbeC301169EaA56c5FC",
    "recipient": "0x9c11115FA30f6d7F31778D00e96607ee3139424F",
    "inputToken": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
    "inputAmount": "156180069500658957",
    "outputToken": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    "swapOutputToken": null,
    "swapOutputTokenAmount": null,
    "outputAmount": "156137166835567125",
    "message": "0x",
    "messageHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "exclusiveRelayer": "0x0000000000000000000000000000000000000000",
    "exclusivityDeadline": null,
    "fillDeadline": "2026-10-05T11:28:50.000Z",
    "quoteTimestamp": "2026-10-05T09:28:50.000Z",
    "depositTxHash": "0x744c5cd1c6aa37d373492cbf074ea47685795541c5b5daa8e50c6d221b1ab00b",
    "depositBlockNumber": 125844200,
    "depositBlockTimestamp": "2026-10-05T09:28:50.000Z",
    "status": "unfilled",
    "depositRefundTxHash": null,
    "swapTokenPriceUsd": null,
    "swapFeeUsd": null,
    "bridgeFeeUsd": null,
    "inputPriceUsd": null,
    "outputPriceUsd": null,
    "fillGasFee": null,
    "fillGasFeeUsd": null,
    "fillGasTokenPriceUsd": null,
    "actionsSucceeded": null,
    "actionsTargetChainId": null,
    "swapTransactionHash": null,
    "swapToken": null,
    "swapTokenAmount": null,
    "relayer": null,
    "fillBlockNumber": null,
    "fillBlockTimestamp": null,
    "fillTx": null,
    "depositTxnRef": "0x744c5cd1c6aa37d373492cbf074ea47685795541c5b5daa8e50c6d221b1ab00b",
    "depositRefundTxnRef": null,
    "fillTxnRef": null,
    "speedups": []
  }
]
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
