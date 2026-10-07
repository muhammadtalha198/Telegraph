---
intent: SECURITY_REVIEW
slug: secrev-depsdev
status: approved
captured_at: 2026-10-02T07:46:19Z
request_url: https://api.deps.dev/v3/systems/npm/packages/lodash/versions/4.17.20
content_type: application/json
inputs: |
  npm lodash 4.17.20
intent_description: |
  Scans codebase dependencies, API endpoints, and configuration files for common CVEs, secrets leakage, and misconfigurations.
answer_requirement: |
  Must list known security vulnerabilities for the package/version asked.
capture_note: |
  (none)
reviewer_note: "auto_review: [0.85] Package advisory / security keys present"
reviewed_at: 2026-10-02T12:49:15Z
---

## Raw API output

```json
{
  "versionKey": {
    "system": "NPM",
    "name": "lodash",
    "version": "4.17.20"
  },
  "publishedAt": "2020-08-13T16:53:54Z",
  "isDefault": false,
  "isDeprecated": false,
  "deprecatedReason": "",
  "licenses": [
    "MIT"
  ],
  "advisoryKeys": [
    {
      "id": "GHSA-29mw-wpgm-hmr9"
    },
    {
      "id": "GHSA-35jh-r3h4-6jhm"
    },
    {
      "id": "GHSA-f23m-r3pf-42rh"
    },
    {
      "id": "GHSA-r5fr-rjxr-66jc"
    },
    {
      "id": "GHSA-xxjr-mmjv-4gpg"
    }
  ],
  "links": [
    {
      "label": "HOMEPAGE",
      "url": "https://lodash.com/"
    },
    {
      "label": "ISSUE_TRACKER",
      "url": "https://github.com/lodash/lodash/issues"
    },
    {
      "label": "ORIGIN",
      "url": "https://registry.npmjs.org/lodash/4.17.20"
    },
    {
      "label": "SOURCE_REPO",
      "url": "git+https://github.com/lodash/lodash.git"
    }
  ],
  "slsaProvenances": [],
  "attestations": [],
  "registries": [
    "https://registry.npmjs.org/"
  ],
  "relatedProjects": [
    {
      "projectKey": {
        "id": "github.com/lodash/lodash"
      },
      "relationProvenance": "UNVERIFIED_METADATA",
      "relationType": "ISSUE_TRACKER"
    },
    {
      "projectKey": {
        "id": "github.com/lodash/lodash"
      },
      "relationProvenance": "UNVERIFIED_METADATA",
      "relationType": "SOURCE_REPO"
    }
  ]
}
```

## Why this matches (or not)

_[0.85] Package advisory / security keys present_
