---
intent: MINING_HASHPRICE_VERIFY
slug: hash-mempool-difficulty
status: pending_review
captured_at: 2026-10-05T09:41:44Z
request_url: https://mempool.space/api/v1/difficulty-adjustment
content_type: application/json
inputs: |
  {}
intent_description: |
  Calculates instantaneous proof-of-work mining revenue per unit of hashing power based on block rewards and network difficulty.
answer_requirement: |
  Must return mining revenue per unit of hashrate (hashprice) or the inputs to compute it.
capture_note: |
  golden-test PASS: mempool.space
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "progressPercent": 14.682539682539684,
  "difficultyChange": -1.909509687533617,
  "estimatedRetargetDate": 1792247483120,
  "remainingBlocks": 1720,
  "remainingTime": 1054181120,
  "previousRetarget": -0.03093703234718248,
  "previousTime": 1791011796,
  "nextRetargetHeight": 971712,
  "timeAvg": 613195,
  "adjustedTimeAvg": 612896,
  "timeOffset": 0,
  "expectedBlocks": 302.51
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
