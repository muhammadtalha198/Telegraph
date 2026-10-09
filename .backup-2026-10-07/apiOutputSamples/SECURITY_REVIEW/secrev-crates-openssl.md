---
intent: SECURITY_REVIEW
slug: secrev-crates-openssl
status: pending_review
captured_at: 2026-10-04T18:40:30Z
request_url: https://crates.io/api/v1/crates/openssl/0.10.0
content_type: application/json
inputs: |
  crates openssl 0.10.0
intent_description: |
  Scans codebase dependencies, API endpoints, and configuration files for common CVEs, secrets leakage, and misconfigurations.
answer_requirement: |
  Must list known security vulnerabilities for the package/version asked.
capture_note: |
  partial metadata
reviewer_note: "re-review after heuristic fix"
reviewed_at: ""
---

## Raw API output

```json
{
  "version": {
    "id": 77081,
    "crate": "openssl",
    "num": "0.10.0",
    "dl_path": "/api/v1/crates/openssl/0.10.0/download",
    "readme_path": "/api/v1/crates/openssl/0.10.0/readme",
    "updated_at": "2018-01-11T06:08:30.148077Z",
    "created_at": "2018-01-11T06:08:30.148077Z",
    "downloads": 17949,
    "features": {
      "v101": [],
      "v102": [],
      "v110": []
    },
    "yanked": false,
    "yank_message": null,
    "lib_links": null,
    "license": "Apache-2.0",
    "links": {
      "dependencies": "/api/v1/crates/openssl/0.10.0/dependencies",
      "version_downloads": "/api/v1/crates/openssl/0.10.0/downloads",
      "authors": "/api/v1/crates/openssl/0.10.0/authors"
    },
    "crate_size": 144157,
    "published_by": null,
    "audit_actions": [],
    "checksum": "deb062a097a6602e60daaca343d9528f7e165e0f316cd4ffed9fe3239cd6aeea",
    "rust_version": null,
    "has_lib": true,
    "bin_names": [],
    "edition": null,
    "description": "OpenSSL bindings",
    "homepage": null,
    "documentation": null,
    "repository": "https://github.com/sfackler/rust-openssl",
    "trustpub_data": null,
    "linecounts": {
      "languages": {
        "Rust": {
          "code_lines": 12342,
          "comment_lines": 124,
          "files": 44
        }
      },
      "total_code_lines": 12342,
      "total_comment_lines": 124
    }
  }
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
