---
intent: CODE_PATCH_VERIFY
slug: patch-ci-azuredevops
status: rejected
captured_at: 2026-10-08T04:42:25Z
request_url: https://dev.azure.com/dnceng-public/public/_apis/build/builds?%24top=1&statusFilter=completed&api-version=7.1
content_type: application/json
inputs: |
  {}
intent_description: |
  Validates that software patch commits compile, resolve targeted defects, and introduce no regression side effects.
answer_requirement: |
  Must report whether the code compiles/runs and what it outputs (pass/fail of the patch).
capture_note: |
  (none)
reviewer_note: "auto_review: [0.70|heuristic] no clear build/test pass-fail for a patch"
reviewed_at: 2026-10-08T04:49:51Z
review_source: auto_review
review_mode: heuristic
llm_used: false
review_confidence: 0.700
---

## Raw API output

```json
{
  "count": 1,
  "value": [
    {
      "_links": {
        "self": {
          "href": "https://dev.azure.com/dnceng-public/cbb18261-c48f-4abb-8651-8cdcb5474649/_apis/build/Builds/1627560"
        },
        "web": {
          "href": "https://dev.azure.com/dnceng-public/cbb18261-c48f-4abb-8651-8cdcb5474649/_build/results?buildId=1627560"
        },
        "sourceVersionDisplayUri": {
          "href": "https://dev.azure.com/dnceng-public/cbb18261-c48f-4abb-8651-8cdcb5474649/_apis/build/builds/1627560/sources"
        },
        "timeline": {
          "href": "https://dev.azure.com/dnceng-public/cbb18261-c48f-4abb-8651-8cdcb5474649/_apis/build/builds/1627560/Timeline"
        },
        "badge": {
          "href": "https://dev.azure.com/dnceng-public/cbb18261-c48f-4abb-8651-8cdcb5474649/_apis/build/status/139"
        }
      },
      "properties": {},
      "tags": [],
      "validationResults": [],
      "plans": [
        {
          "planId": "90533c89-ff63-432a-91be-e9e2ca124ac7"
        }
      ],
      "triggerInfo": {
        "pr.sourceBranch": "gdv-debuginfo-to-ret-expression",
        "pr.sourceSha": "2e08d5d9852dbf41b219d6091a0bdb569f674cc5",
        "pr.id": "4745208282",
        "pr.title": "JIT: Add DebugInfo to ret expr statement when doing GDV",
        "pr.number": "135209",
        "pr.isFork": "True",
        "pr.draft": "False",
        "pr.sender.name": "anderspedersen",
        "pr.sender.avatarUrl": "https://avatars.githubusercontent.com/u/5472407?v=4",
        "pr.sender.isExternal": "True",
        "pr.providerId": "github",
        "pr.autoCancel": "true"
      },
      "id": 1627560,
      "buildNumber": "20261007.96",
      "status": "completed",
      "result": "succeeded",
      "queueTime": "2026-10-08T03:37:08.1587704Z",
      "startTime": "2026-10-08T03:40:20.5222247Z",
      "finishTime": "2026-10-08T04:41:27.3816273Z",
      "url": "https://dev.azure.com/dnceng-public/cbb18261-c48f-4abb-8651-8cdcb5474649/_apis/build/Builds/1627560",
      "definition": {
        "drafts": [],
        "id": 139,
        "name": "dotnet-linker-tests",
        "url": "https://dev.azure.com/dnceng-public/cbb18261-c48f-4abb-8651-8cdcb5474649/_apis/build/Definitions/139?revision=1",
        "uri": "vstfs:///Build/Definition/139",
        "path": "\\dotnet\\runtime",
        "type": "build",
        "queueStatus": "enabled",
        "revision": 1,
        "project": {
          "id": "cbb18261-c48f-4abb-8651-8cdcb5474649",
          "name": "public",
          "description": "Project exists exclusively for .NET Core projects which build publicly",
          "url": "https://dev.azure.com/dnceng-public/_apis/projects/cbb18261-c48f-4abb-8651-8cdcb5474649",
          "state": "wellFormed",
          "revision": 20,
          "visibility": "public",
          "lastUpdateTime": "2023-05-16T15:27:53.67Z"
        }
      },
      "buildNumberRevision": 96,
      "project": {
        "id": "cbb18261-c48f-4abb-8651-8cdcb5474649",
        "name": "public",
        "description": "Project exists exclusively for .NET Core projects which build publicly",
        "url": "https://dev.azure.com/dnceng-public/_apis/projects/cbb18261-c48f-4abb-8651-8cdcb5474649",
        "state": "wellFormed",
        "revision": 20,
        "visibility": "public",
        "lastUpdateTime": "2023-05-16T15:27:53.67Z"
      },
      "uri": "vstfs:///Build/Build/1627560",
      "sourceBranch": "refs/pull/135209/merge",
      "sourceVersion": "9e9d2102f3b5d808024e9d40f0b3048bbe652ad3",
      "priority": "normal",
      "reason": "pullRequest",
      "requestedFor": {
        "displayName": "GitHub",
        "url": "https://spsprodcus4.vssps.visualstudio.com/A10a5dd58-16e3-41e8-b079-e25cb8111111/_apis/Identities/2cda4d09-cbed-4967-be9d-61a0df5130b4",
        "_links": {
          "avatar": {
            "href": "https://dev.azure.com/dnceng-public/_apis/GraphProfile/MemberAvatars/svc.MTBhNWRkNTgtMTZlMy00MWU4LWIwNzktZTI1Y2I4MTExMTExOkdpdEh1YiBBcHA6Y2JiMTgyNjEtYzQ4Zi00YWJiLTg2NTEtOGNkY2I1NDc0NjQ5"
          }
        },
        "id": "2cda4d09-cbed-4967-be9d-61a0df5130b4",
        "uniqueName": null,
        "imageUrl": null,
        "descriptor": "svc.MTBhNWRkNTgtMTZlMy00MWU4LWIwNzktZTI1Y2I4MTExMTExOkdpdEh1YiBBcHA6Y2JiMTgyNjEtYzQ4Zi00YWJiLTg2NTEtOGNkY2I1NDc0NjQ5"
      },
      "requestedBy": {
        "displayName": "GitHub",
        "url": "https://spsprodcus4.vssps.visualstudio.com/A10a5dd58-16e3-41e8-b079-e25cb8111111/_apis/Identities/2cda4d09-cbed-4967-be9d-61a0df5130b4",
        "_links": {
          "avatar": {
            "href": "https://dev.azure.com/dnceng-public/_apis/GraphProfile/MemberAvatars/svc.MTBhNWRkNTgtMTZlMy00MWU4LWIwNzktZTI1Y2I4MTExMTExOkdpdEh1YiBBcHA6Y2JiMTgyNjEtYzQ4Zi00YWJiLTg2NTEtOGNkY2I1NDc0NjQ5"
          }
        },
        "id": "2cda4d09-cbed-4967-be9d-61a0df5130b4",
        "uniqueName": null,
        "imageUrl": null,
        "descriptor": "svc.MTBhNWRkNTgtMTZlMy00MWU4LWIwNzktZTI1Y2I4MTExMTExOkdpdEh1YiBBcHA6Y2JiMTgyNjEtYzQ4Zi00YWJiLTg2NTEtOGNkY2I1NDc0NjQ5"
      },
      "lastChangedDate": "2026-10-08T04:41:27.497Z",
      "lastChangedBy": {
        "displayName": "Microsoft.VisualStudio.Services.TFS",
        "url": "https://spsprodcus4.vssps.visualstudio.com/A10a5dd58-16e3-41e8-b079-e25cb8111111/_apis/Identities/00000002-0000-8888-8000-000000000000",
        "_links": {
          "avatar": {
            "href": "https://dev.azure.com/dnceng-public/_apis/GraphProfile/MemberAvatars/s2s.MDAwMDAwMDItMDAwMC04ODg4LTgwMDAtMDAwMDAwMDAwMDAwQDJjODk1OTA4LTA0ZTAtNDk1Mi04OWZkLTU0YjAwNDZkNjI4OA"
          }
        },
        "id": "00000002-0000-8888-8000-000000000000",
        "uniqueName": null,
        "imageUrl": null,
        "descriptor": "s2s.MDAwMDAwMDItMDAwMC04ODg4LTgwMDAtMDAwMDAwMDAwMDAwQDJjODk1OTA4LTA0ZTAtNDk1Mi04OWZkLTU0YjAwNDZkNjI4OA"
      },
      "parameters": "{\"system.pullRequest.pullRequestId\":\"4745208282\",\"system.pullRequest.pullRequestNumber\":\"135209\",\"system.pullRequest.mergedAt\":\"\",\"system.pullRequest.sourceBranch\":\"gdv-debuginfo-to-ret-expression\",\"system.pullRequest.targetBranch\":\"main\",\"system.pullRequest.targetBranchName\":\"main\",\"system.pullRequest.sourceRepositoryUri\":\"https://github.com/dotnet/runtime\",\"system.pullRequest.sourceCommitId\":\"2e08d5d9852dbf41b219d6091a0bdb569f674cc5\",\"system.pullRequest.isFork\":\"True\"}",
      "orchestrationPlan": {
        "planId": "90533c89-ff63-432a-91be-e9e2ca124ac7"
      },
      "logs": {
        "id": 0,
        "type": "Container",
        "url": "https://dev.azure.com/dnceng-public/cbb18261-c48f-4abb-8651-8cdcb5474649/_apis/build/builds/1627560/logs"
      },
      "repository": {
        "id": "dotnet/runtime",
        "type": "GitHub",
        "url": "https://github.com:443/dotnet/runtime",
        "clean": null,
        "checkoutSubmodules": false
      },
      "retainedByRelease": false,
      "triggeredByBuild": null,
      "appendCommitMessageToRunName": true
    }
  ]
}
```

## Why this matches (or not)

_[0.70|heuristic] no clear build/test pass-fail for a patch_
