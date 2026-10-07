---
intent: ONCHAIN_METRIC_VERIFY
slug: ocm-blockscout-scroll
status: approved
captured_at: 2026-10-04T18:40:07Z
request_url: https://scroll.blockscout.com/api/v2/addresses/0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
content_type: application/json
inputs: |
  vitalik addr scroll
intent_description: |
  Validates smart contract event logs, gas consumption, token balances, and wallet transaction states directly on-chain.
answer_requirement: |
  Must convey the on-chain value asked (wallet/token balance or tx state) for the address given.
capture_note: |
  NEW
reviewer_note: "auto_review: [0.80|heuristic] Returns wallet/token balance (partial vs full logs/gas description)"
reviewed_at: 2026-10-04T18:41:49Z
---

## Raw API output

```json
{
  "block_number_balance_updated_at": 35275164,
  "coin_balance": "70942521591221114",
  "creation_status": null,
  "creation_transaction_hash": null,
  "creator_address_hash": null,
  "ens_domain_name": null,
  "exchange_rate": "2700.79",
  "has_beacon_chain_withdrawals": false,
  "has_logs": false,
  "has_token_transfers": true,
  "has_tokens": true,
  "has_validated_blocks": false,
  "hash": "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
  "implementations": [],
  "is_contract": false,
  "is_scam": false,
  "is_verified": false,
  "metadata": null,
  "name": null,
  "private_tags": [],
  "proxy_type": null,
  "public_tags": [],
  "reputation": "ok",
  "token": null,
  "watchlist_address_id": null,
  "watchlist_names": []
}
```

## Why this matches (or not)

_[0.80|heuristic] Returns wallet/token balance (partial vs full logs/gas description)_
