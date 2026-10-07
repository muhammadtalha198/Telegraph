---
intent: CODE_PATCH_VERIFY
slug: patch-gh-workflow-django
status: pending_review
captured_at: 2026-10-04T18:40:48Z
request_url: https://api.github.com/repos/django/django/actions/runs?per_page=1&status=completed
content_type: application/json
inputs: |
  django/django
intent_description: |
  Validates that software patch commits compile, resolve targeted defects, and introduce no regression side effects.
answer_requirement: |
  Must convey whether the build/tests for the patch passed or failed.
capture_note: |
  (none)
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "total_count": 2500,
  "workflow_runs": [
    {
      "id": 36002741110,
      "name": "Coverage Comment",
      "node_id": "WFR_kwLOAD-Lgs8AAAAIYe47dg",
      "head_branch": "main",
      "head_sha": "a013c821ea7838a953869615b0bdcfdb298cc09f",
      "path": ".github/workflows/coverage_comment.yml",
      "display_title": "Coverage Comment",
      "run_number": 5002,
      "event": "workflow_run",
      "status": "completed",
      "conclusion": "skipped",
      "workflow_id": 212990903,
      "check_suite_id": 97489968804,
      "check_suite_node_id": "CS_kwDOAD-Lgs8AAAAWstrepA",
      "url": "https://api.github.com/repos/django/django/actions/runs/36002741110",
      "html_url": "https://github.com/django/django/actions/runs/36002741110",
      "pull_requests": [
        {
          "url": "https://api.github.com/repos/ananyas2006/django/pulls/1",
          "id": 3339013944,
          "number": 1,
          "head": {
            "ref": "main",
            "sha": "a461af8ce48762d7ec602260aaff81014ddccbcb",
            "repo": {
              "id": 4164482,
              "url": "https://api.github.com/repos/django/django",
              "name": "django"
            }
          },
          "base": {
            "ref": "main",
            "sha": "33fbab6ce46067f09ab4f856fe3b6522afa169fc",
            "repo": {
              "id": 1167785127,
              "url": "https://api.github.com/repos/ananyas2006/django",
              "name": "django"
            }
          }
        },
        {
          "url": "https://api.github.com/repos/yashvanzara/django/pulls/1",
          "id": 3166350706,
          "number": 1,
          "head": {
            "ref": "main",
            "sha": "a461af8ce48762d7ec602260aaff81014ddccbcb",
            "repo": {
              "id": 4164482,
              "url": "https://api.github.com/repos/django/django",
              "name": "django"
            }
          },
          "base": {
            "ref": "main",
            "sha": "d61838761f17d7c934c7be288fadfa14f471b598",
            "repo": {
              "id": 1131674434,
              "url": "https://api.github.com/repos/yashvanzara/django",
              "name": "django"
            }
          }
        },
        {
          "url": "https://api.github.com/repos/mergify-ci-insights/django/pulls/13",
          "id": 2719505598,
          "number": 13,
          "head": {
            "ref": "main",
            "sha": "a461af8ce48762d7ec602260aaff81014ddccbcb",
            "repo": {
              "id": 4164482,
              "url": "https://api.github.com/repos/django/django",
              "name": "django"
            }
          },
          "base": {
            "ref": "main",
            "sha": "212f473e93cbde92a5db1a0404d17853728a3821",
            "repo": {
              "id": 1018854768,
              "url": "https://api.github.com/repos/mergify-ci-insights/django",
              "name": "django"
            }
          }
        },
        {
          "url": "https://api.github.com/repos/Karinza38/django/pulls/4",
          "id": 2244467543,
          "number": 4,
          "head": {
            "ref": "main",
            "sha": "a461af8ce48762d7ec602260aaff81014ddccbcb",
            "repo": {
              "id": 4164482,
              "url": "https://api.github.com/repos/django/django",
              "name": "django"
            }
          },
          "base": {
            "ref": "main",
            "sha": "3ee4c6a27ad520d4ecc3cded260d47cbccafb144",
            "repo": {
              "id": 903334094,
              "url": "https://api.github.com/repos/Karinza38/django",
              "name": "django"
            }
          }
        },
        {
          "url": "https://api.github.com/repos/Mesh-12/django/pulls/1",
          "id": 1856826315,
          "number": 1,
          "head": {
            "ref": "main",
            "sha": "a461af8ce48762d7ec602260aaff81014ddccbcb",
            "repo": {
              "id": 4164482,
              "url": "https://api.github.com/repos/django/django",
              "name": "django"
            }
          },
          "base": {
            "ref": "main",
            "sha": "6345a6ff63a8b8af86ee9a025e29984a410c9764",
            "repo": {
              "id": 796623427,
              "url": "https://api.github.com/repos/Mesh-12/django",
              "name": "django"
            }
          }
        },
        {
          "url": "https://api.github.com/repos/Thesohan/django/pulls/161",
          "id": 832337673,
          "number": 161,
          "head": {
            "ref": "main",
            "sha": "a461af8ce48762d7ec602260aaff81014ddccbcb",
            "repo": {
              "id": 4164482,
              "url": "https://api.github.com/repos/django/django",
              "name": "django"
            }
          },
          "base": {
            "ref": "main",
            "sha": "a93a1ba347be9744e8492dd8288f18b3831caa02",
            "repo": {
              "id": 415982811,
              "url": "https://api.github.com/repos/Thesohan/django",
              "name": "django"
            }
          }
        }
      ],
      "created_at": "2026-09-24T13:00:29Z",
      "updated_at": "2026-09-24T13:00:38Z",
      "actor": {
        "login": "cliffordgama",
        "id": 53076065,
        "node_id": "MDQ6VXNlcjUzMDc2MDY1",
        "avatar_url": "https://avatars.githubusercontent.com/u/53076065?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/cliffordgama",
        "html_url": "https://github.com/cliffordgama",
        "followers_url": "https://api.github.com/users/cliffordgama/followers",
        "following_url": "https://api.github.com/users/cliffordgama/following{/other_user}",
        "gists_url": "https://api.github.com/users/cliffordgama/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/cliffordgama/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/cliffordgama/subscriptions",
        "organizations_url": "https://api.github.com/users/cliffordgama/orgs",
        "repos_url": "https://api.github.com/users/cliffordgama/repos",
        "events_url": "https://api.github.com/users/cliffordgama/events{/privacy}",
        "received_events_url": "https://api.github.com/users/cliffordgama/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "run_attempt": 1,
      "referenced_workflows": [],
      "run_started_at": "2026-09-24T13:00:29Z",
      "triggering_actor": {
        "login": "cliffordgama",
        "id": 53076065,
        "node_id": "MDQ6VXNlcjUzMDc2MDY1",
        "avatar_url": "https://avatars.githubusercontent.com/u/53076065?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/cliffordgama",
        "html_url": "https://github.com/cliffordgama",
        "followers_url": "https://api.github.com/users/cliffordgama/followers",
        "following_url": "https://api.github.com/users/cliffordgama/following{/other_user}",
        "gists_url": "https://api.github.com/users/cliffordgama/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/cliffordgama/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/cliffordgama/subscriptions",
        "organizations_url": "https://api.github.com/users/cliffordgama/orgs",
        "repos_url": "https://api.github.com/users/cliffordgama/repos",
        "events_url": "https://api.github.com/users/cliffordgama/events{/privacy}",
        "received_events_url": "https://api.github.com/users/cliffordgama/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "jobs_url": "https://api.github.com/repos/django/django/actions/runs/36002741110/jobs",
      "logs_url": "https://api.github.com/repos/django/django/actions/runs/36002741110/logs",
      "check_suite_url": "https://api.github.com/repos/django/django/check-suites/97489968804",
      "artifacts_url": "https://api.github.com/repos/django/django/actions/runs/36002741110/artifacts",
      "cancel_url": "https://api.github.com/repos/django/django/actions/runs/36002741110/cancel",
      "rerun_url": "https://api.github.com/repos/django/django/actions/runs/36002741110/rerun",
      "previous_attempt_url": null,
      "workflow_url": "https://api.github.com/repos/django/django/actions/workflows/212990903",
      "head_commit": {
        "id": "a013c821ea7838a953869615b0bdcfdb298cc09f",
        "tree_id": "09a2e3fcbc66c3b104c732384845e27e2b5c0cb2",
        "message": "Fixed #37177 -- Reduced per-middleware context switching under ASGI.\n\nRelying on MiddlewareMixin.__acall__() to handle async requests imposed\nper-middleware context switching, defeating BaseHandler's intent\nto transition only once per middleware chain.\n\nTo minimize breaking changes, MiddlewareMixin's default value did not\nchange: only the values on Django's own subclasses. Use cases where the\nprior behavior is preferable (in order to avoid pinning a thread per\nrequest) are fleshed out in docs.\n\nThanks Mykhailo Havelia for the report.",
        "timestamp": "2026-09-24T08:59:37Z",
        "author": {
          "name": "Jacob Walls",
          "email": "jacobtylerwalls@gmail.com"
        },
        "committer": {
          "name": "Jacob Walls",
          "email": "jacobtylerwalls@gmail.com"
        }
      },
      "repository": {
        "id": 4164482,
        "node_id": "MDEwOlJlcG9zaXRvcnk0MTY0NDgy",
        "name": "django",
        "full_name": "django/django",
        "private": false,
        "owner": {
          "login": "django",
          "id": 27804,
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjI3ODA0",
          "avatar_url": "https://avatars.githubusercontent.com/u/27804?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/django",
          "html_url": "https://github.com/django",
          "followers_url": "https://api.github.com/users/django/followers",
          "following_url": "https://api.github.com/users/django/following{/other_user}",
          "gists_url": "https://api.github.com/users/django/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/django/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/django/subscriptions",
          "organizations_url": "https://api.github.com/users/django/orgs",
          "repos_url": "https://api.github.com/users/django/repos",
          "events_url": "https://api.github.com/users/django/events{/privacy}",
          "received_events_url": "https://api.github.com/users/django/received_events",
          "type": "Organization",
          "user_view_type": "public",
          "site_admin": false
        },
        "html_url": "https://github.com/django/django",
        "description": "The Web framework for perfectionists with deadlines.",
        "fork": false,
        "url": "https://api.github.com/repos/django/django",
        "forks_url": "https://api.github.com/repos/django/django/forks",
        "keys_url": "https://api.github.com/repos/django/django/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/django/django/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/django/django/teams",
        "hooks_url": "https://api.github.com/repos/django/django/hooks",
        "issue_events_url": "https://api.github.com/repos/django/django/issues/events{/number}",
        "events_url": "https://api.github.com/repos/django/django/events",
        "assignees_url": "https://api.github.com/repos/django/django/assignees{/user}",
        "branches_url": "https://api.github.com/repos/django/django/branches{/branch}",
        "tags_url": "https://api.github.com/repos/django/django/tags",
        "blobs_url": "https://api.github.com/repos/django/django/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/django/django/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/django/django/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/django/django/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/django/django/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/django/django/languages",
        "stargazers_url": "https://api.github.com/repos/django/django/stargazers",
        "contributors_url": "https://api.github.com/repos/django/django/contributors",
        "subscribers_url": "https://api.github.com/repos/django/django/subscribers",
        "subscription_url": "https://api.github.com/repos/django/django/subscription",
        "commits_url": "https://api.github.com/repos/django/django/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/django/django/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/django/django/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/django/django/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/django/django/contents/{+path}",
        "compare_url": "https://api.github.com/repos/django/django/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/django/django/merges",
        "archive_url": "https://api.github.com/repos/django/django/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/django/django/downloads",
        "issues_url": "https://api.github.com/repos/django/django/issues{/number}",
        "pulls_url": "https://api.github.com/repos/django/django/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/django/django/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/django/django/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/django/django/labels{/name}",
        "releases_url": "https://api.github.com/repos/django/django/releases{/id}",
        "deployments_url": "https://api.github.com/repos/django/django/deployments"
      },
      "head_repository": {
        "id": 4164482,
        "node_id": "MDEwOlJlcG9zaXRvcnk0MTY0NDgy",
        "name": "django",
        "full_name": "django/django",
        "private": false,
        "owner": {
          "login": "django",
          "id": 27804,
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjI3ODA0",
          "avatar_url": "https://avatars.githubusercontent.com/u/27804?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/django",
          "html_url": "https://github.com/django",
          "followers_url": "https://api.github.com/users/django/followers",
          "following_url": "https://api.github.com/users/django/following{/other_user}",
          "gists_url": "https://api.github.com/users/django/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/django/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/django/subscriptions",
          "organizations_url": "https://api.github.com/users/django/orgs",
          "repos_url": "https://api.github.com/users/django/repos",
          "events_url": "https://api.github.com/users/django/events{/privacy}",
          "received_events_url": "https://api.github.com/users/django/received_events",
          "type": "Organization",
          "user_view_type": "public",
          "site_admin": false
        },
        "html_url": "https://github.com/django/django",
        "description": "The Web framework for perfectionists with deadlines.",
        "fork": false,
        "url": "https://api.github.com/repos/django/django",
        "forks_url": "https://api.github.com/repos/django/django/forks",
        "keys_url": "https://api.github.com/repos/django/django/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/django/django/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/django/django/teams",
        "hooks_url": "https://api.github.com/repos/django/django/hooks",
        "issue_events_url": "https://api.github.com/repos/django/django/issues/events{/number}",
        "events_url": "https://api.github.com/repos/django/django/events",
        "assignees_url": "https://api.github.com/repos/django/django/assignees{/user}",
        "branches_url": "https://api.github.com/repos/django/django/branches{/branch}",
        "tags_url": "https://api.github.com/repos/django/django/tags",
        "blobs_url": "https://api.github.com/repos/django/django/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/django/django/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/django/django/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/django/django/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/django/django/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/django/django/languages",
        "stargazers_url": "https://api.github.com/repos/django/django/stargazers",
        "contributors_url": "https://api.github.com/repos/django/django/contributors",
        "subscribers_url": "https://api.github.com/repos/django/django/subscribers",
        "subscription_url": "https://api.github.com/repos/django/django/subscription",
        "commits_url": "https://api.github.com/repos/django/django/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/django/django/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/django/django/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/django/django/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/django/django/contents/{+path}",
        "compare_url": "https://api.github.com/repos/django/django/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/django/django/merges",
        "archive_url": "https://api.github.com/repos/django/django/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/django/django/downloads",
        "issues_url": "https://api.github.com/repos/django/django/issues{/number}",
        "pulls_url": "https://api.github.com/repos/django/django/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/django/django/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/django/django/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/django/django/labels{/name}",
        "releases_url": "https://api.github.com/repos/django/django/releases{/id}",
        "deployments_url": "https://api.github.com/repos/django/django/deployments"
      }
    }
  ]
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
