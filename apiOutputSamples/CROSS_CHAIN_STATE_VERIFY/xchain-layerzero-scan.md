---
intent: CROSS_CHAIN_STATE_VERIFY
slug: xchain-layerzero-scan
status: pending_review
captured_at: 2026-10-05T09:28:52Z
request_url: https://scan.layerzero-api.com/v1/messages/latest?limit=1
content_type: application/json
inputs: |
  {}
intent_description: |
  Proves cryptographic Merkle-Patricia state roots and cross-chain message execution headers between distinct blockchain networks.
answer_requirement: |
  Must return verifiable state roots / cross-chain message status between networks.
capture_note: |
  golden-test PASS: LayerZero Scan
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "data": [
    {
      "pathway": {
        "srcEid": 30110,
        "dstEid": 30184,
        "sender": {
          "address": "0xc08cd26474722ce93f4d0c34d16201461c10aa8c",
          "id": "carv",
          "name": "CARV",
          "chain": "arbitrum"
        },
        "receiver": {
          "address": "0xc08cd26474722ce93f4d0c34d16201461c10aa8c",
          "id": "carv",
          "name": "CARV",
          "chain": "base"
        },
        "id": "30110-30184-0xc08cd26474722ce93f4d0c34d16201461c10aa8c-0xc08cd26474722ce93f4d0c34d16201461c10aa8c",
        "nonce": 54128
      },
      "source": {
        "status": "VALIDATING_TX",
        "tx": {
          "txHash": "0x90ed9ead5e854c53f1c6a1e750c5e308fafb8e783e77e648b62284fd172590e9",
          "blockHash": "0x57cbcfdb99b20b94b7b5251e535fb5c84e1ca0e2044bd99c05018736e0c34a5d",
          "blockNumber": "511882433",
          "blockTimestamp": 1791192514,
          "from": "0x655ccf2e4687c1a77e2dcf25a82cc0055efe2b05",
          "payload": "0x000000000000000000000000655ccf2e4687c1a77e2dcf25a82cc0055efe2b05000000005669de52",
          "options": {
            "lzReceive": {
              "gas": "200000",
              "value": "2500000"
            },
            "ordered": false
          }
        }
      },
      "destination": {
        "status": "WAITING"
      },
      "verification": {
        "dvn": {
          "dvns": {
            "0x9e059a54699a285714207b43b055483e78faac25": {
              "status": "WAITING"
            },
            "0xcd37ca043f8479064e10635020c65ffc005d36f6": {
              "status": "WAITING"
            }
          },
          "status": "WAITING"
        },
        "sealer": {
          "status": "WAITING"
        }
      },
      "guid": "0xcef6236e0df54b833c14120af7a1a10b717f6b3428d5237b6cf3d8060d0056c8",
      "config": {
        "error": false,
        "dvnConfigError": false,
        "receiveLibrary": "0xc70AB6f32772f59fBfc23889Caf4Ba3376C84bAf",
        "sendLibrary": "0x975bcD720be66659e3EB3C0e4F1866a3020E493A",
        "inboundConfig": {
          "confirmations": 10,
          "requiredDVNCount": 2,
          "optionalDVNCount": 0,
          "optionalDVNThreshold": 0,
          "requiredDVNs": [
            "0x9e059a54699a285714207b43b055483e78faac25",
            "0xcd37ca043f8479064e10635020c65ffc005d36f6"
          ],
          "requiredDVNNames": [
            "LayerZero Labs",
            "Nethermind"
          ],
          "optionalDVNs": [],
          "optionalDVNNames": []
        },
        "outboundConfig": {
          "confirmations": 10,
          "requiredDVNCount": 2,
          "optionalDVNCount": 0,
          "optionalDVNThreshold": 0,
          "requiredDVNs": [
            "0x2f55c492897526677c5b68fb199ea31e2c126416",
            "0xa7b5189bca84cd304d8553977c7c614329750d99"
          ],
          "requiredDVNNames": [
            "LayerZero Labs",
            "Nethermind"
          ],
          "optionalDVNs": [],
          "optionalDVNNames": []
        },
        "ulnSendVersion": "V302",
        "ulnReceiveVersion": "V302"
      },
      "status": {
        "name": "INFLIGHT",
        "message": "Source transaction sent"
      },
      "created": "2026-10-05T09:28:38.000Z",
      "updated": "2026-10-05T09:28:38.000Z"
    }
  ],
  "nextToken": "eyJtZXNzYWdlSWQiOiIzMDExMC0zMDE4NC0weGMwOGNkMjY0NzQ3MjJjZTkzZjRkMGMzNGQxNjIwMTQ2MWMxMGFhOGMtMHhjMDhjZDI2NDc0NzIyY2U5M2Y0ZDBjMzRkMTYyMDE0NjFjMTBhYThjLTU0MTI4IiwiZW5kIjoiMTc5MTE5MjUxOCJ9"
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
