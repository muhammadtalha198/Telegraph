---
intent: CODE_PATCH_VERIFY
slug: patch-circleci-recent
status: approved
captured_at: 2026-10-04T18:40:46Z
request_url: https://circleci.com/api/v1.1/project/github/CircleCI-Public/circleci-cli?limit=1&filter=completed
content_type: text/plain
inputs: |
  circleci-cli builds
intent_description: |
  Validates that software patch commits compile, resolve targeted defects, and introduce no regression side effects.
answer_requirement: |
  Must convey whether the build/tests for the patch passed or failed.
capture_note: |
  public project API
reviewer_note: "auto_review: [0.80|heuristic] CI pipeline status=success"
reviewed_at: 2026-10-04T18:41:49Z
---

## Raw API output

```json
[
  {
    "compare": null,
    "previous_successful_build": null,
    "build_parameters": {},
    "oss": true,
    "all_commit_details_truncated": false,
    "committer_date": "2026-10-02T15:55:56.000Z",
    "body": "Compare two runs, typically the same pipeline before and after a config\nchange, by total running time and total credits. Credits come from\nPOST /api/v3/analysis/charges, filtered by pipeline.id and summed across\nworkflows; running time spans the earliest workflow creation to the\nlatest workflow end.\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>",
    "usage_queued_at": "2026-10-02T15:55:59.164Z",
    "context_ids": [],
    "fail_reason": null,
    "retry_of": null,
    "reponame": "circleci-cli",
    "ssh_users": [],
    "build_url": "https://circleci.com/gh/CircleCI-Public/circleci-cli/51953",
    "parallel": 1,
    "failed": false,
    "branch": "proposal/compare-config",
    "username": "CircleCI-Public",
    "author_date": "2026-10-02T15:55:56.000Z",
    "why": "github",
    "user": {
      "is_user": true,
      "login": "cloverfern",
      "avatar_url": "https://avatars.githubusercontent.com/u/10763929?v=4",
      "name": "Fernando",
      "vcs_type": "github",
      "id": 10763929
    },
    "vcs_revision": "015931442ef425507ddaaec5d5b0cf3d15db87a6",
    "workflows": {
      "workflow_id": "554add22-7ae2-44b9-a64b-db4335b0f291",
      "workflow_name": "ci",
      "workspace_id": "554add22-7ae2-44b9-a64b-db4335b0f291",
      "job_name": "dry-run",
      "job_id": "7124cb89-1b64-44a5-b67e-9e91e6e861bb",
      "upstream_job_ids": [],
      "upstream_concurrency_map": {}
    },
    "vcs_tag": null,
    "build_num": 51953,
    "infrastructure_fail": false,
    "committer_email": "10763929+cloverfern@users.noreply.github.com",
    "previous": {
      "build_num": 51947,
      "status": "success",
      "build_time_millis": 123703
    },
    "status": "success",
    "committer_name": "Fernando",
    "retries": null,
    "subject": "Add circleci run compare",
    "vcs_type": "github",
    "timedout": false,
    "dont_build": null,
    "lifecycle": "finished",
    "stop_time": "2026-10-02T15:58:36.384Z",
    "ssh_disabled": false,
    "build_time_millis": 127941,
    "picard": null,
    "circle_yml": null,
    "messages": [],
    "is_first_green_build": false,
    "job_name": null,
    "start_time": "2026-10-02T15:56:28.443Z",
    "canceler": null,
    "all_commit_details": [
      {
        "committer_date": "2026-10-02T15:55:56.000Z",
        "body": "Compare two runs, typically the same pipeline before and after a config\nchange, by total running time and total credits. Credits come from\nPOST /api/v3/analysis/charges, filtered by pipeline.id and summed across\nworkflows; running time spans the earliest workflow creation to the\nlatest workflow end.\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>",
        "branch": "proposal/compare-config",
        "author_date": "2026-10-02T15:55:56.000Z",
        "committer_email": "10763929+cloverfern@users.noreply.github.com",
        "commit": "015931442ef425507ddaaec5d5b0cf3d15db87a6",
        "committer_login": "cloverfern",
        "committer_name": "Fernando",
        "subject": "Add circleci run compare",
        "commit_url": "https://github.com/CircleCI-Public/circleci-cli/commit/015931442ef425507ddaaec5d5b0cf3d15db87a6",
        "author_login": "cloverfern",
        "author_name": "Fernando",
        "author_email": "fernando.lima@circleci.com"
      }
    ],
    "platform": "2.0",
    "outcome": "success",
    "vcs_url": "https://github.com/CircleCI-Public/circleci-cli",
    "author_name": "Fernando",
    "node": null,
    "queued_at": "2026-10-02T15:55:59.243Z",
    "canceled": false,
    "author_email": "fernando.lima@circleci.com"
  }
]
```

## Why this matches (or not)

_[0.80|heuristic] CI pipeline status=success_
