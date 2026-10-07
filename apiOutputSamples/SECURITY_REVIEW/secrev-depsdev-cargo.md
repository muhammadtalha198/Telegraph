---
intent: SECURITY_REVIEW
slug: secrev-depsdev-cargo
status: approved
captured_at: 2026-10-04T18:40:28Z
request_url: https://api.deps.dev/v3/systems/cargo/packages/openssl/versions/0.10.0
content_type: application/json
inputs: |
  cargo openssl 0.10.0
intent_description: |
  Scans codebase dependencies, API endpoints, and configuration files for common CVEs, secrets leakage, and misconfigurations.
answer_requirement: |
  Must list known security vulnerabilities for the package/version asked.
capture_note: |
  (none)
reviewer_note: "auto_review: [0.85|heuristic] Package advisory / security keys present"
reviewed_at: 2026-10-04T18:41:49Z
---

## Raw API output

```json
{
  "versionKey": {
    "system": "CARGO",
    "name": "openssl",
    "version": "0.10.0"
  },
  "publishedAt": "2018-01-11T06:08:30Z",
  "isDefault": false,
  "isDeprecated": false,
  "deprecatedReason": "",
  "licenses": [
    "Apache-2.0"
  ],
  "advisoryKeys": [
    {
      "id": "GHSA-3gxf-9r58-2ghg"
    },
    {
      "id": "GHSA-6hcf-g6gr-hhcr"
    },
    {
      "id": "GHSA-9qwg-crg9-m2vc"
    },
    {
      "id": "GHSA-hppc-g8h3-xhp3"
    },
    {
      "id": "GHSA-pqf5-4pqq-29f5"
    },
    {
      "id": "GHSA-q445-7m23-qrmw"
    },
    {
      "id": "GHSA-rpmj-rpgj-qmpm"
    },
    {
      "id": "GHSA-xcf7-rvmh-g6q4"
    },
    {
      "id": "GHSA-xmgf-hq76-4vx2"
    },
    {
      "id": "GHSA-xp3w-r5p5-63rr"
    },
    {
      "id": "GHSA-xv59-967r-8726"
    },
    {
      "id": "RUSTSEC-2023-0022"
    },
    {
      "id": "RUSTSEC-2023-0023"
    },
    {
      "id": "RUSTSEC-2023-0024"
    },
    {
      "id": "RUSTSEC-2023-0044"
    },
    {
      "id": "RUSTSEC-2023-0072"
    },
    {
      "id": "RUSTSEC-2024-0357"
    },
    {
      "id": "RUSTSEC-2025-0004"
    }
  ],
  "links": [
    {
      "label": "SOURCE_REPO",
      "url": "https://github.com/rust-openssl/rust-openssl"
    }
  ],
  "slsaProvenances": [],
  "attestations": [],
  "registries": [
    "https://crates.io/"
  ],
  "relatedProjects": [
    {
      "projectKey": {
        "id": "github.com/rust-openssl/rust-openssl"
      },
      "relationProvenance": "UNVERIFIED_METADATA",
      "relationType": "SOURCE_REPO"
    }
  ]
}
```

## Why this matches (or not)

_[0.85|heuristic] Package advisory / security keys present_
