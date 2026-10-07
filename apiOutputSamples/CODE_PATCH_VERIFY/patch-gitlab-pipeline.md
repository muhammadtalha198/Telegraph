---
intent: CODE_PATCH_VERIFY
slug: patch-gitlab-pipeline
status: approved
captured_at: 2026-10-04T18:40:45Z
request_url: https://gitlab.com/api/v4/projects/gitlab-org%2Fgitlab-runner/pipelines?per_page=1&status=success
content_type: application/json
inputs: |
  gitlab-runner pipelines
intent_description: |
  Validates that software patch commits compile, resolve targeted defects, and introduce no regression side effects.
answer_requirement: |
  Must convey whether the build/tests for the patch passed or failed.
capture_note: |
  (none)
reviewer_note: "auto_review: [0.80|heuristic] CI pipeline status=success"
reviewed_at: 2026-10-04T18:41:49Z
---

## Raw API output

```json
[
  {
    "id": 2911149449,
    "iid": 52672,
    "project_id": 250833,
    "sha": "42d035cf5e73856424f21742597a33140a18963c",
    "ref": "refs/merge-requests/7480/merge",
    "status": "success",
    "source": "merge_request_event",
    "created_at": "2026-10-04T17:21:28.019Z",
    "updated_at": "2026-10-04T18:05:09.128Z",
    "web_url": "https://gitlab.com/gitlab-org/gitlab-runner/-/pipelines/2911149449",
    "name": null
  }
]
```

## Why this matches (or not)

_[0.80|heuristic] CI pipeline status=success_
