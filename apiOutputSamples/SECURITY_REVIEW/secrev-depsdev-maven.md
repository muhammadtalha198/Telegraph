---
intent: SECURITY_REVIEW
slug: secrev-depsdev-maven
status: approved
captured_at: 2026-10-04T18:40:28Z
request_url: https://api.deps.dev/v3/systems/maven/packages/org.apache.logging.log4j%3Alog4j-core/versions/2.14.1
content_type: application/json
inputs: |
  log4j-core 2.14.1
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
    "system": "MAVEN",
    "name": "org.apache.logging.log4j:log4j-core",
    "version": "2.14.1"
  },
  "publishedAt": "2021-03-07T05:12:31Z",
  "isDefault": false,
  "isDeprecated": false,
  "deprecatedReason": "",
  "licenses": [
    "Apache-2.0"
  ],
  "advisoryKeys": [
    {
      "id": "GHSA-3pxv-7cmr-fjr4"
    },
    {
      "id": "GHSA-6hg6-v5c8-fphq"
    },
    {
      "id": "GHSA-7rjr-3q55-vv33"
    },
    {
      "id": "GHSA-8489-44mv-ggj8"
    },
    {
      "id": "GHSA-jfh8-c2jp-5v3q"
    },
    {
      "id": "GHSA-p6xc-xr62-6r2g"
    },
    {
      "id": "GHSA-vc5p-v9hr-52mj"
    }
  ],
  "links": [
    {
      "label": "SOURCE_REPO",
      "url": "https://gitbox.apache.org/repos/asf?p=logging-log4j2.git"
    },
    {
      "label": "ISSUE_TRACKER",
      "url": "https://issues.apache.org/jira/browse/LOG4J2"
    },
    {
      "label": "HOMEPAGE",
      "url": "https://logging.apache.org/log4j/2.x/"
    }
  ],
  "slsaProvenances": [],
  "attestations": [],
  "registries": [
    "https://repo.maven.apache.org/maven2/"
  ],
  "relatedProjects": [
    {
      "projectKey": {
        "id": ""
      },
      "relationProvenance": "UNVERIFIED_METADATA",
      "relationType": "ISSUE_TRACKER"
    }
  ]
}
```

## Why this matches (or not)

_[0.85|heuristic] Package advisory / security keys present_
