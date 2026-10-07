---
intent: SSL_CERTIFICATE_VERIFY
slug: ssl-certspotter
status: pending_review
captured_at: 2026-10-05T09:33:22Z
request_url: https://api.certspotter.com/v1/issuances?domain=github.com&expand=issuer&expand=dns_names
content_type: application/json
inputs: |
  {"host": "github.com"}
intent_description: |
  Validates TLS/SSL certificate chains, cipher suites, expiration dates, and revocation statuses.
answer_requirement: |
  Must return TLS certificate details (issuer, validity dates, chain/validity status) for the host.
capture_note: |
  golden-test PASS: SSLMate Cert Spotter
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
[
  {
    "id": "16246130557",
    "tbs_sha256": "a445a23ecad6078069cb942f5c5945ace94be3503b0fbb45e47505c88894cf15",
    "cert_sha256": "71f1077db377fd7b8d68380da66fa68238a303b2911bcb770b3b2a426693cf84",
    "dns_names": [
      "*.github.com",
      "*.github.io",
      "*.githubusercontent.com",
      "github.com",
      "github.io",
      "githubusercontent.com"
    ],
    "pubkey_sha256": "a7831b0537d4dcc4f3a8fc4cd828efd2add638df0be85a92cda9bae4d54491c3",
    "issuer": {
      "friendly_name": "Let's Encrypt",
      "pubkey_sha256": "2e8307068b6db620e4a39d068b5dee5d6ef5788cbb2c0b6d23ead84fcc17178c",
      "name": "C=US, O=Let's Encrypt, CN=YR1"
    },
    "not_before": "2026-08-02T23:38:02Z",
    "not_after": "2026-10-31T23:38:01Z",
    "revoked": false
  },
  {
    "id": "16270160024",
    "tbs_sha256": "d5252811a9ed8ab7f53c7145a7abf83465e5fee81e72d1691981275505c695cc",
    "cert_sha256": "6a6984de4486d95d21770dd9e910bf65dbeadf2d582dec06eaba882b482de7ea",
    "dns_names": [
      "github.com",
      "www.github.com"
    ],
    "pubkey_sha256": "5c00bad1e99b85e1750c9978d9b26b1c24c144dd29015c7844455cc3f9f0bd62",
    "issuer": {
      "friendly_name": "Sectigo",
      "pubkey_sha256": "6bd9212ce649c659c9cabc6cb60fcffac7a20c29be61fdceb2b5f2168701688d",
      "name": "C=GB, O=Sectigo Limited, CN=Sectigo Public Server Authentication CA DV R36"
    },
    "not_before": "2026-08-04T00:00:00Z",
    "not_after": "2026-11-01T23:59:59Z",
    "revoked": false
  },
  {
    "id": "16401858739",
    "tbs_sha256": "c5ee6f6dd1b1d7a7264743a194631eddd1987ab1b8fafd20bfb848f5e72ad1e0",
    "cert_sha256": "1e23ac36939ae9efa41aa41c8c9190451fcff12377153851397af58f19307345",
    "dns_names": [
      "*.github.com",
      "github.com"
    ],
    "pubkey_sha256": "9ffc4eb6babb78f4df0c0aa8d99d89f5d18c60d2397024f75a3c4a993aa2fafa",
    "issuer": {
      "friendly_name": "Sectigo",
      "pubkey_sha256": "6bd9212ce649c659c9cabc6cb60fcffac7a20c29be61fdceb2b5f2168701688d",
      "name": "C=GB, O=Sectigo Limited, CN=Sectigo Public Server Authentication CA DV R36"
    },
    "not_before": "2026-08-10T00:00:00Z",
    "not_after": "2026-11-07T23:59:59Z",
    "revoked": false
  },
  {
    "id": "16533374203",
    "tbs_sha256": "5d499a27cbbfdb7da9b0124f188d6e519c0f3b7109abdd6a887a00f51312dabf",
    "cert_sha256": "5fc67129d4a769cfea6670088fe1ddd6b9558017eeea1053ba344f5947c7f815",
    "dns_names": [
      "garage.github.com",
      "gist.github.com",
      "github.com",
      "www.github.com"
    ],
    "pubkey_sha256": "08af26ffb8e0c5eb488c64501c31197123d1c2b3f46e8f6c4efffdae34883046",
    "issuer": {
      "friendly_name": "Sectigo",
      "pubkey_sha256": "6bd9212ce649c659c9cabc6cb60fcffac7a20c29be61fdceb2b5f2168701688d",
      "name": "C=GB, O=Sectigo Limited, CN=Sectigo Public Server Authentication CA DV R36"
    },
    "not_before": "2026-08-16T00:00:00Z",
    "not_after": "2026-11-13T23:59:59Z",
    "revoked": false
  },
  {
    "id": "16878377385",
    "tbs_sha256": "eb129be547ed517f387c0f04ff41a34ecc23c03a20b3b7ea5f3c324f149c76d3",
    "cert_sha256": "06e6a4a004329905d4a4e7c0d2c6ec7a632c56443f256424a43cc786951b3149",
    "dns_names": [
      "*.github.com",
      "github.com"
    ],
    "pubkey_sha256": "4b62d421bab8c94839c3e3186e3e4b64e580640cda78d189f6b4d37381a3bc14",
    "issuer": {
      "friendly_name": "Sectigo",
      "pubkey_sha256": "6526a0bc3ce396d2e47b05c406e0f1233a56fdda55c3526ebef99dd21864cdd6",
      "name": "C=GB, O=Sectigo Limited, CN=Sectigo Public Server Authentication CA DV E36"
    },
    "not_before": "2026-08-30T00:00:00Z",
    "not_after": "2026-11-27T23:59:59Z",
    "revoked": false
  },
  {
    "id": "16894901843",
    "tbs_sha256": "a7ef4cbcbccfddf4773584c65bb14dc63b75b1773c4ac7fec6bde48bbe06c3e1",
    "cert_sha256": "9c6b98df2063eb48df2afab8ea49b4233ecb5c8537b21813e452fc4e13962ef4",
    "dns_names": [
      "*.github.com",
      "github.com"
    ],
    "pubkey_sha256": "1fdba877a591a2390c2260c11cec1a617379bc8ab921f958a6cf8b58d11c6acc",
    "issuer": {
      "friendly_name": "Sectigo",
      "pubkey_sha256": "6bd9212ce649c659c9cabc6cb60fcffac7a20c29be61fdceb2b5f2168701688d",
      "name": "C=GB, O=Sectigo Limited, CN=Sectigo Public Server Authentication CA DV R36"
    },
    "not_before": "2026-08-31T00:00:00Z",
    "not_after": "2026-11-28T23:59:59Z",
    "revoked": false
  },
  {
    "id": "16913588078",
    "tbs_sha256": "9fc18f8c34c64095e53339d37003f26fad7436d8f19513d232e7b25d7f4b7480",
    "cert_sha256": "46b601ee08b418cf8a3a1ebfe670ba5ce43bb05a917fa8b2dd087a30471cfc63",
    "dns_names": [
      "github.com",
      "www.github.com"
    ],
    "pubkey_sha256": "ff088be6f80e2e0c040f8d564b40cd17c4224c1551fcfe3529dd7aded985c4ad",
    "issuer": {
      "friendly_name": "Sectigo",
      "pubkey_sha256": "6526a0bc3ce396d2e47b05c406e0f1233a56fdda55c3526ebef99dd21864cdd6",
      "name": "C=GB, O=Sectigo Limited, CN=Sectigo Public Server Authentication CA DV E36"
    },
    "not_before": "2026-09-01T00:00:00Z",
    "not_after": "2026-11-29T23:59:59Z",
    "revoked": false
  },
  {
    "id": "17510115980",
    "tbs_sha256": "57bf1350f74a21248e82ce164f4f3540bd9ebeb35516d9bf80fa03702f8024e4",
    "cert_sha256": "f2f9a159ce50a0a168b3eaeaf2fced5addd49ba38e2bf63248f057a139fc7856",
    "dns_names": [
      "*.github.com",
      "*.github.io",
      "*.githubusercontent.com",
      "github.com",
      "github.io",
      "githubusercontent.com"
    ],
    "pubkey_sha256": "94db9ac7d44da25f17c751844eeafd7eb8d7b7e8629ac64708b28e8229ef172c",
    "issuer": {
      "friendly_name": "Let's Encrypt",
      "pubkey_sha256": "2e8307068b6db620e4a39d068b5dee5d6ef5788cbb2c0b6d23ead84fcc17178c",
      "name": "C=US, O=Let's Encrypt, CN=YR1"
    },
    "not_before": "2026-09-30T23:44:46Z",
    "not_after": "2026-12-29T23:44:45Z",
    "revoked": false
  },
  {
    "id": "17531471500",
    "tbs_sha256": "0f3363d22930771a6b4ed3b265c1abf38e1299a077567961b471b3f53a352ab1",
    "cert_sha256": "d98af57e2f20997004dd087e2f0506c2638e9f8d1ff8af6995b317e749670b04",
    "dns_names": [
      "github.com",
      "www.github.com"
    ],
    "pubkey_sha256": "a5f14e015ec0f5a186d493e86a3ee88cbe4fc5e063cc54327aa5e8ff2cd88159",
    "issuer": {
      "friendly_name": "Sectigo",
      "pubkey_sha256": "6bd9212ce649c659c9cabc6cb60fcffac7a20c29be61fdceb2b5f2168701688d",
      "name": "C=GB, O=Sectigo Limited, CN=Sectigo Public Server Authentication CA DV R36"
    },
    "not_before": "2026-10-02T00:00:00Z",
    "not_after": "2026-12-30T23:59:59Z",
    "revoked": false
  }
]
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
