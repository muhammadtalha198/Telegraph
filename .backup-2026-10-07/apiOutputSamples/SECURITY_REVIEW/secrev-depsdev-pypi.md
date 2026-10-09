---
intent: SECURITY_REVIEW
slug: secrev-depsdev-pypi
status: approved
captured_at: 2026-10-04T18:40:27Z
request_url: https://api.deps.dev/v3/systems/pypi/packages/django/versions/3.0
content_type: application/json
inputs: |
  pypi django 3.0
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
    "system": "PYPI",
    "name": "django",
    "version": "3.0.0"
  },
  "publishedAt": "2019-12-02T11:13:11Z",
  "isDefault": false,
  "isDeprecated": false,
  "deprecatedReason": "",
  "licenses": [
    "non-standard"
  ],
  "advisoryKeys": [
    {
      "id": "GHSA-2m34-jcjv-45xf"
    },
    {
      "id": "GHSA-3gh2-xw74-jmcw"
    },
    {
      "id": "GHSA-3h9f-r86x-qvjx"
    },
    {
      "id": "GHSA-68w8-qjq3-2gfm"
    },
    {
      "id": "GHSA-6w2r-r2m5-xq5w"
    },
    {
      "id": "GHSA-7xr5-9hcq-chf9"
    },
    {
      "id": "GHSA-8cjm-8mp7-r2xf"
    },
    {
      "id": "GHSA-8qcx-xf44-272x"
    },
    {
      "id": "GHSA-8x94-hmjh-97hq"
    },
    {
      "id": "GHSA-923m-gv2p-w5qp"
    },
    {
      "id": "GHSA-crhf-3pfg-w68w"
    },
    {
      "id": "GHSA-fr28-569j-53c4"
    },
    {
      "id": "GHSA-frmv-pr5f-9mcr"
    },
    {
      "id": "GHSA-fvgf-6h6h-3322"
    },
    {
      "id": "GHSA-h7pc-vwp9-298g"
    },
    {
      "id": "GHSA-hmr4-m2h5-33qx"
    },
    {
      "id": "GHSA-m6gj-h9gm-gw44"
    },
    {
      "id": "GHSA-p99v-5w3c-jqq9"
    },
    {
      "id": "GHSA-q238-5cxm-5c9h"
    },
    {
      "id": "GHSA-qw25-v68c-qjf3"
    },
    {
      "id": "GHSA-rrqc-c2jx-6jgv"
    },
    {
      "id": "GHSA-rxjp-mfm9-w4wr"
    },
    {
      "id": "GHSA-v6rh-hp5x-86rv"
    },
    {
      "id": "GHSA-vfq6-hq5r-27r6"
    },
    {
      "id": "GHSA-wpjr-j57x-wxfw"
    },
    {
      "id": "GHSA-wvqv-fj8w-qmhm"
    },
    {
      "id": "GHSA-xgxc-v2qg-chmh"
    },
    {
      "id": "GHSA-xpfp-f569-q3p2"
    },
    {
      "id": "PYSEC-2020-31"
    },
    {
      "id": "PYSEC-2020-32"
    },
    {
      "id": "PYSEC-2020-33"
    },
    {
      "id": "PYSEC-2020-34"
    },
    {
      "id": "PYSEC-2020-35"
    },
    {
      "id": "PYSEC-2020-36"
    },
    {
      "id": "PYSEC-2021-6"
    },
    {
      "id": "PYSEC-2021-9"
    },
    {
      "id": "PYSEC-2021-98"
    },
    {
      "id": "PYSEC-2021-99"
    },
    {
      "id": "PYSEC-2026-1297"
    },
    {
      "id": "PYSEC-2026-3717"
    },
    {
      "id": "PYSEC-2026-4035"
    }
  ],
  "links": [
    {
      "label": "DOCUMENTATION",
      "url": "https://docs.djangoproject.com/"
    },
    {
      "label": "SOURCE_REPO",
      "url": "https://github.com/django/django"
    }
  ],
  "slsaProvenances": [],
  "attestations": [],
  "registries": [
    "https://pypi.org/simple"
  ],
  "relatedProjects": [
    {
      "projectKey": {
        "id": "github.com/django/django"
      },
      "relationProvenance": "UNVERIFIED_METADATA",
      "relationType": "SOURCE_REPO"
    }
  ],
  "projectStatus": {
    "status": "active",
    "reason": ""
  }
}
```

## Why this matches (or not)

_[0.85|heuristic] Package advisory / security keys present_
