---
intent: VALIDATOR_PERFORMANCE_VERIFY
slug: val-beacon-publicnode
status: approved
captured_at: 2026-10-05T09:41:20Z
request_url: https://ethereum-beacon-api.publicnode.com/eth/v1/beacon/states/head/validators/1
content_type: application/json
inputs: |
  {"vid": "1"}
intent_description: |
  Tracks consensus voting uptime, proposed block rates, slashing penalties, and staking APR for network validators.
answer_requirement: |
  Must return the validator's status/balance/slashing/attestation performance for the validator asked.
capture_note: |
  golden-test PASS: PublicNode beacon
reviewer_note: "auto_review: [1.00|heuristic+llm] The response provides the validator's status, balance, and effective balance which directly answers the intent."
reviewed_at: 2026-10-05T12:00:13Z
review_source: auto_review
review_mode: heuristic+llm
llm_used: true
review_confidence: 1.000
---

## Raw API output

```json
{
  "execution_optimistic": false,
  "finalized": false,
  "data": {
    "index": "1",
    "balance": "32012974157",
    "status": "active_ongoing",
    "validator": {
      "pubkey": "0xa1d1ad0714035353258038e964ae9675dc0252ee22cea896825c01458e1807bfad2f9969338798548d9858a571f7425c",
      "withdrawal_credentials": "0x01000000000000000000000015f4b914a0ccd14333d850ff311d6dafbfbaa32b",
      "effective_balance": "32000000000",
      "slashed": false,
      "activation_eligibility_epoch": "0",
      "activation_epoch": "0",
      "exit_epoch": "18446744073709551615",
      "withdrawable_epoch": "18446744073709551615"
    }
  }
}
```

## Why this matches (or not)

_[1.00|heuristic+llm] The response provides the validator's status, balance, and effective balance which directly answers the intent._
