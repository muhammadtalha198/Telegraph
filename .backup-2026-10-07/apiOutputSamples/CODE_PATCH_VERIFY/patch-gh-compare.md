---
intent: CODE_PATCH_VERIFY
slug: patch-gh-compare
status: pending_review
captured_at: 2026-10-04T18:40:42Z
request_url: https://api.github.com/repos/psf/requests/compare/v2.31.0...v2.32.0
content_type: application/json
inputs: |
  requests v2.31→v2.32
intent_description: |
  Validates that software patch commits compile, resolve targeted defects, and introduce no regression side effects.
answer_requirement: |
  Must convey whether the build/tests for the patch passed or failed.
capture_note: |
  diff only — needs_human unless paired with CI conclusion
reviewer_note: ""
reviewed_at: ""
---

## Raw API output

```json
{
  "url": "https://api.github.com/repos/psf/requests/compare/v2.31.0...v2.32.0",
  "html_url": "https://github.com/psf/requests/compare/v2.31.0...v2.32.0",
  "permalink_url": "https://github.com/psf/requests/compare/psf:147c851...psf:d6ebc4a",
  "diff_url": "https://github.com/psf/requests/compare/v2.31.0...v2.32.0.diff",
  "patch_url": "https://github.com/psf/requests/compare/v2.31.0...v2.32.0.patch",
  "base_commit": {
    "sha": "147c8511ddbfa5e8f71bbf5c18ede0c4ceb3bba4",
    "node_id": "C_kwDOABTKOtoAKDE0N2M4NTExZGRiZmE1ZThmNzFiYmY1YzE4ZWRlMGM0Y2ViM2JiYTQ",
    "commit": {
      "author": {
        "name": "Nate Prewitt",
        "email": "nate.prewitt@gmail.com",
        "date": "2023-05-22T15:10:32Z"
      },
      "committer": {
        "name": "GitHub",
        "email": "noreply@github.com",
        "date": "2023-05-22T15:10:32Z"
      },
      "message": "v2.31.0",
      "tree": {
        "sha": "7be4f5113896a87e2d1ed58a00c237881ae79520",
        "url": "https://api.github.com/repos/psf/requests/git/trees/7be4f5113896a87e2d1ed58a00c237881ae79520"
      },
      "url": "https://api.github.com/repos/psf/requests/git/commits/147c8511ddbfa5e8f71bbf5c18ede0c4ceb3bba4",
      "comment_count": 0,
      "verification": {
        "verified": true,
        "reason": "valid",
        "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJka4XoCRBK7hj4Ov3rIwAAcrgIAI7aPfTLin/XP66DV/hsBBrX\ndD+3KpmoWIFbm5JNHQkKWiUKfrdkuTuRNkdvUiReORlcy7cm9LIJsVW5h3PrWeVR\nj3OPrs2XIW7Egjr9LVh1SU0/M6rtKPVGETZxncgs4omOybyw4dCiuLrMK6zJJ7XJ\ntk2k2+vMXCH39HgFrZENBeYBQrCMz3nNO3LaNFM3b8StFtJXT1sA2mqFANynkPWU\naUEVfrGVxhB5wFnuUH0LqD80+Mb8Vk/NEhsQrhfT7PIxt82Cl2xog7G8MIQyeJR/\nJ6XmbxrxiVsTKTHrqShA10EvmrcBsxhZrT6wZSv4XEJA8FVBee+97bud6BzU6/o=\n=A69M\n-----END PGP SIGNATURE-----\n",
        "payload": "tree 7be4f5113896a87e2d1ed58a00c237881ae79520\nparent 74ea7cf7a6a27a4eeb2ae24e162bcc942a6706d5\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1684768232 -0700\ncommitter GitHub <noreply@github.com> 1684768232 -0600\n\nv2.31.0\n\n",
        "verified_at": "2024-01-16T19:59:59Z"
      }
    },
    "url": "https://api.github.com/repos/psf/requests/commits/147c8511ddbfa5e8f71bbf5c18ede0c4ceb3bba4",
    "html_url": "https://github.com/psf/requests/commit/147c8511ddbfa5e8f71bbf5c18ede0c4ceb3bba4",
    "comments_url": "https://api.github.com/repos/psf/requests/commits/147c8511ddbfa5e8f71bbf5c18ede0c4ceb3bba4/comments",
    "author": {
      "login": "nateprewitt",
      "id": 5271761,
      "node_id": "MDQ6VXNlcjUyNzE3NjE=",
      "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/nateprewitt",
      "html_url": "https://github.com/nateprewitt",
      "followers_url": "https://api.github.com/users/nateprewitt/followers",
      "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
      "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
      "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
      "repos_url": "https://api.github.com/users/nateprewitt/repos",
      "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
      "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "committer": {
      "login": "web-flow",
      "id": 19864447,
      "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
      "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/web-flow",
      "html_url": "https://github.com/web-flow",
      "followers_url": "https://api.github.com/users/web-flow/followers",
      "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
      "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
      "organizations_url": "https://api.github.com/users/web-flow/orgs",
      "repos_url": "https://api.github.com/users/web-flow/repos",
      "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
      "received_events_url": "https://api.github.com/users/web-flow/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "parents": [
      {
        "sha": "74ea7cf7a6a27a4eeb2ae24e162bcc942a6706d5",
        "url": "https://api.github.com/repos/psf/requests/commits/74ea7cf7a6a27a4eeb2ae24e162bcc942a6706d5",
        "html_url": "https://github.com/psf/requests/commit/74ea7cf7a6a27a4eeb2ae24e162bcc942a6706d5"
      }
    ]
  },
  "merge_base_commit": {
    "sha": "147c8511ddbfa5e8f71bbf5c18ede0c4ceb3bba4",
    "node_id": "C_kwDOABTKOtoAKDE0N2M4NTExZGRiZmE1ZThmNzFiYmY1YzE4ZWRlMGM0Y2ViM2JiYTQ",
    "commit": {
      "author": {
        "name": "Nate Prewitt",
        "email": "nate.prewitt@gmail.com",
        "date": "2023-05-22T15:10:32Z"
      },
      "committer": {
        "name": "GitHub",
        "email": "noreply@github.com",
        "date": "2023-05-22T15:10:32Z"
      },
      "message": "v2.31.0",
      "tree": {
        "sha": "7be4f5113896a87e2d1ed58a00c237881ae79520",
        "url": "https://api.github.com/repos/psf/requests/git/trees/7be4f5113896a87e2d1ed58a00c237881ae79520"
      },
      "url": "https://api.github.com/repos/psf/requests/git/commits/147c8511ddbfa5e8f71bbf5c18ede0c4ceb3bba4",
      "comment_count": 0,
      "verification": {
        "verified": true,
        "reason": "valid",
        "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJka4XoCRBK7hj4Ov3rIwAAcrgIAI7aPfTLin/XP66DV/hsBBrX\ndD+3KpmoWIFbm5JNHQkKWiUKfrdkuTuRNkdvUiReORlcy7cm9LIJsVW5h3PrWeVR\nj3OPrs2XIW7Egjr9LVh1SU0/M6rtKPVGETZxncgs4omOybyw4dCiuLrMK6zJJ7XJ\ntk2k2+vMXCH39HgFrZENBeYBQrCMz3nNO3LaNFM3b8StFtJXT1sA2mqFANynkPWU\naUEVfrGVxhB5wFnuUH0LqD80+Mb8Vk/NEhsQrhfT7PIxt82Cl2xog7G8MIQyeJR/\nJ6XmbxrxiVsTKTHrqShA10EvmrcBsxhZrT6wZSv4XEJA8FVBee+97bud6BzU6/o=\n=A69M\n-----END PGP SIGNATURE-----\n",
        "payload": "tree 7be4f5113896a87e2d1ed58a00c237881ae79520\nparent 74ea7cf7a6a27a4eeb2ae24e162bcc942a6706d5\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1684768232 -0700\ncommitter GitHub <noreply@github.com> 1684768232 -0600\n\nv2.31.0\n\n",
        "verified_at": "2024-01-16T19:59:59Z"
      }
    },
    "url": "https://api.github.com/repos/psf/requests/commits/147c8511ddbfa5e8f71bbf5c18ede0c4ceb3bba4",
    "html_url": "https://github.com/psf/requests/commit/147c8511ddbfa5e8f71bbf5c18ede0c4ceb3bba4",
    "comments_url": "https://api.github.com/repos/psf/requests/commits/147c8511ddbfa5e8f71bbf5c18ede0c4ceb3bba4/comments",
    "author": {
      "login": "nateprewitt",
      "id": 5271761,
      "node_id": "MDQ6VXNlcjUyNzE3NjE=",
      "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/nateprewitt",
      "html_url": "https://github.com/nateprewitt",
      "followers_url": "https://api.github.com/users/nateprewitt/followers",
      "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
      "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
      "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
      "repos_url": "https://api.github.com/users/nateprewitt/repos",
      "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
      "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "committer": {
      "login": "web-flow",
      "id": 19864447,
      "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
      "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/web-flow",
      "html_url": "https://github.com/web-flow",
      "followers_url": "https://api.github.com/users/web-flow/followers",
      "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
      "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
      "organizations_url": "https://api.github.com/users/web-flow/orgs",
      "repos_url": "https://api.github.com/users/web-flow/repos",
      "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
      "received_events_url": "https://api.github.com/users/web-flow/received_events",
      "type": "User",
      "user_view_type": "public",
      "site_admin": false
    },
    "parents": [
      {
        "sha": "74ea7cf7a6a27a4eeb2ae24e162bcc942a6706d5",
        "url": "https://api.github.com/repos/psf/requests/commits/74ea7cf7a6a27a4eeb2ae24e162bcc942a6706d5",
        "html_url": "https://github.com/psf/requests/commit/74ea7cf7a6a27a4eeb2ae24e162bcc942a6706d5"
      }
    ]
  },
  "status": "ahead",
  "ahead_by": 128,
  "behind_by": 0,
  "total_commits": 128,
  "commits": [
    {
      "sha": "53a0562331c4a825036a347e77984d68b310fcf3",
      "node_id": "C_kwDOABTKOtoAKDUzYTA1NjIzMzFjNGE4MjUwMzZhMzQ3ZTc3OTg0ZDY4YjMxMGZjZjM",
      "commit": {
        "author": {
          "name": "Volker Schaus",
          "email": "volker.schaus@esa.int",
          "date": "2022-10-23T18:35:43Z"
        },
        "committer": {
          "name": "Volker Schaus",
          "email": "volker.schaus@esa.int",
          "date": "2022-10-23T18:35:43Z"
        },
        "message": "change to SPDX conform license string",
        "tree": {
          "sha": "cd023fa03b6249a60f64c2e5c01a850f80fc9e23",
          "url": "https://api.github.com/repos/psf/requests/git/trees/cd023fa03b6249a60f64c2e5c01a850f80fc9e23"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/53a0562331c4a825036a347e77984d68b310fcf3",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/53a0562331c4a825036a347e77984d68b310fcf3",
      "html_url": "https://github.com/psf/requests/commit/53a0562331c4a825036a347e77984d68b310fcf3",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/53a0562331c4a825036a347e77984d68b310fcf3/comments",
      "author": null,
      "committer": null,
      "parents": [
        {
          "sha": "1e62a3ec18e19f85ddae03b4cbbdf0b4c62834c0",
          "url": "https://api.github.com/repos/psf/requests/commits/1e62a3ec18e19f85ddae03b4cbbdf0b4c62834c0",
          "html_url": "https://github.com/psf/requests/commit/1e62a3ec18e19f85ddae03b4cbbdf0b4c62834c0"
        }
      ]
    },
    {
      "sha": "6e5b15d542a4e85945fd72066bb6cecbc3a82191",
      "node_id": "C_kwDOABTKOtoAKDZlNWIxNWQ1NDJhNGU4NTk0NWZkNzIwNjZiYjZjZWNiYzNhODIxOTE",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2023-05-22T15:36:22Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-05-22T15:36:22Z"
        },
        "message": "Fix linting issues",
        "tree": {
          "sha": "22478d7d9cb29172a7ab056ab7030ef2aded351f",
          "url": "https://api.github.com/repos/psf/requests/git/trees/22478d7d9cb29172a7ab056ab7030ef2aded351f"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/6e5b15d542a4e85945fd72066bb6cecbc3a82191",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJka4v2CRBK7hj4Ov3rIwAA9h8IAFY0TC5TB7oZyCF7s9KTB2RU\ny9//PoVP/Cl7n17W0LnrHI8p9m+mLtuykYz3Pomwb8IHp7vAaXzLn32+PsffdjpS\naJskAeoSPf9yUoMM0CTh8hZovd6lU97Oi/nLJAZ+g+KqqAnndcu8P9InkRUaePB4\nLskm9AbrRSix4WU5M8Fjjo7VYc/FbNbHYEOjR7IHc3qPFsdssCdVEH8kNpBSkGDW\nKMnw7chTxoTd9B1UWg9fvlExGFS9nbuI89+d6Aewp1SKujWjWON8AchhIAkVOcMY\nK/L8zCbhtA63+C3U0q0vCwGfMnHdHScT3BcyXTGbVto8WPAu7vwujJ0nTftpS60=\n=XGuf\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 22478d7d9cb29172a7ab056ab7030ef2aded351f\nparent 147c8511ddbfa5e8f71bbf5c18ede0c4ceb3bba4\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1684769782 -0700\ncommitter GitHub <noreply@github.com> 1684769782 -0600\n\nFix linting issues\n\n",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/6e5b15d542a4e85945fd72066bb6cecbc3a82191",
      "html_url": "https://github.com/psf/requests/commit/6e5b15d542a4e85945fd72066bb6cecbc3a82191",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/6e5b15d542a4e85945fd72066bb6cecbc3a82191/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "147c8511ddbfa5e8f71bbf5c18ede0c4ceb3bba4",
          "url": "https://api.github.com/repos/psf/requests/commits/147c8511ddbfa5e8f71bbf5c18ede0c4ceb3bba4",
          "html_url": "https://github.com/psf/requests/commit/147c8511ddbfa5e8f71bbf5c18ede0c4ceb3bba4"
        }
      ]
    },
    {
      "sha": "22db55a8896b69e53d0a3cc2764c27b832c81478",
      "node_id": "C_kwDOABTKOtoAKDIyZGI1NWE4ODk2YjY5ZTUzZDBhM2NjMjc2NGMyN2I4MzJjODE0Nzg",
      "commit": {
        "author": {
          "name": "Boris Verkhovskiy",
          "email": "boris.verk@gmail.com",
          "date": "2023-06-26T17:09:23Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-06-26T17:09:23Z"
        },
        "message": "Fix doc typo (#6467)",
        "tree": {
          "sha": "d7d70f44a1c7b99d6a9abe78d80cd169d0991dd9",
          "url": "https://api.github.com/repos/psf/requests/git/trees/d7d70f44a1c7b99d6a9abe78d80cd169d0991dd9"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/22db55a8896b69e53d0a3cc2764c27b832c81478",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJkmcZDCRBK7hj4Ov3rIwAAigQIABCKcTFLH0h155VwlfqohQKr\nfoov/IMeYH3huxQNq76ImjGxZcFGOVegOWePbH9BXhPRrP/2qiMyFIr6NnoWxQry\nGr5k4Ho772c1A1H7efKjBnnp1kOWiZaAaImo4eBL6oy5bokTVHxna/F14wXveb0K\n7uU4GzYnr2nTiio3nBDs5ahBz8ppGJ/MlLP1OKglHN5aGkgDr8uR+//iN61lVnKW\nTO2IaFrYFYfIWk+7lPmp9bGpVd4GrlGAd4BVbjm0DZmfNeFcYEl/YfL904un88yu\n7iFdLRXohD7DVprYyAHSD9t/x7unFWlHCQFndu92S4a3yUtut5f/RIYc3z5nFkM=\n=qXSN\n-----END PGP SIGNATURE-----\n",
          "payload": "tree d7d70f44a1c7b99d6a9abe78d80cd169d0991dd9\nparent 6e5b15d542a4e85945fd72066bb6cecbc3a82191\nauthor Boris Verkhovskiy <boris.verk@gmail.com> 1687799363 +0100\ncommitter GitHub <noreply@github.com> 1687799363 -0600\n\nFix doc typo (#6467)\n\n",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/22db55a8896b69e53d0a3cc2764c27b832c81478",
      "html_url": "https://github.com/psf/requests/commit/22db55a8896b69e53d0a3cc2764c27b832c81478",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/22db55a8896b69e53d0a3cc2764c27b832c81478/comments",
      "author": {
        "login": "verhovsky",
        "id": 5687998,
        "node_id": "MDQ6VXNlcjU2ODc5OTg=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5687998?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/verhovsky",
        "html_url": "https://github.com/verhovsky",
        "followers_url": "https://api.github.com/users/verhovsky/followers",
        "following_url": "https://api.github.com/users/verhovsky/following{/other_user}",
        "gists_url": "https://api.github.com/users/verhovsky/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/verhovsky/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/verhovsky/subscriptions",
        "organizations_url": "https://api.github.com/users/verhovsky/orgs",
        "repos_url": "https://api.github.com/users/verhovsky/repos",
        "events_url": "https://api.github.com/users/verhovsky/events{/privacy}",
        "received_events_url": "https://api.github.com/users/verhovsky/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "6e5b15d542a4e85945fd72066bb6cecbc3a82191",
          "url": "https://api.github.com/repos/psf/requests/commits/6e5b15d542a4e85945fd72066bb6cecbc3a82191",
          "html_url": "https://github.com/psf/requests/commit/6e5b15d542a4e85945fd72066bb6cecbc3a82191"
        }
      ]
    },
    {
      "sha": "cdbc2e271529f467b278b2760f12ee0b5d6930d3",
      "node_id": "C_kwDOABTKOtoAKGNkYmMyZTI3MTUyOWY0NjdiMjc4YjI3NjBmMTJlZTBiNWQ2OTMwZDM",
      "commit": {
        "author": {
          "name": "Matthew Armand",
          "email": "marmand68@gmail.com",
          "date": "2023-07-03T20:38:22Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-07-03T20:38:22Z"
        },
        "message": "Add an Example for automatic retries to the Advanced Usage docs (#6258)\n\n- While Requests doesn't automatically retry failures, this ability is a very common advanced use case in real world applications.\r\n- Although there's a mention of this ability on the HTTPAdapter class docs, it's a bit buried and not very specific.\r\n- It makes sense then to have an Example in the HTTPAdapter section of the Advanced Usage docs with a basic template for how this can be accomplished with Requests.",
        "tree": {
          "sha": "1a37c98696e46b474ca8d93a4a8d17036fa95cbe",
          "url": "https://api.github.com/repos/psf/requests/git/trees/1a37c98696e46b474ca8d93a4a8d17036fa95cbe"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/cdbc2e271529f467b278b2760f12ee0b5d6930d3",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJkozG+CRBK7hj4Ov3rIwAA4IcIAErWwRQGLEvY10acccnMmq/E\nlrSt+roWGNTGy7Fn8QHJZ0Ltk4miV1zfSn47XsKdlB/lY29tHTfxkWEW0J/NV+02\n6iwM5Dsm6g14oKFUeHCrTSYeNXD91HR3lZN8vJcPevnMnY+G9BUPhWbxFD2LbBPm\nxLVg68GHrbLEmvmFqmAWu5DuAH4WQJXvpV4sZxJoWFLI0tTwDgAC6c6G7Cpg8p9R\nMuArLBZKr2zSg7dU0v4YI3ZAF6ztII0JWaU9Cwx5It+sU0z78V5A4X361PZq3Ko5\nkIggmMkRhL20ufrZ4LUNq2Kb8HDOct5jm17TLSEYTvLPE95nYSS+QkWjpDFjXCQ=\n=P7vI\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 1a37c98696e46b474ca8d93a4a8d17036fa95cbe\nparent 22db55a8896b69e53d0a3cc2764c27b832c81478\nauthor Matthew Armand <marmand68@gmail.com> 1688416702 -0400\ncommitter GitHub <noreply@github.com> 1688416702 -0700\n\nAdd an Example for automatic retries to the Advanced Usage docs (#6258)\n\n- While Requests doesn't automatically retry failures, this ability is a very common advanced use case in real world applications.\r\n- Although there's a mention of this ability on the HTTPAdapter class docs, it's a bit buried and not very specific.\r\n- It makes sense then to have an Example in the HTTPAdapter section of the Advanced Usage docs with a basic template for how this can be accomplished with Requests.",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/cdbc2e271529f467b278b2760f12ee0b5d6930d3",
      "html_url": "https://github.com/psf/requests/commit/cdbc2e271529f467b278b2760f12ee0b5d6930d3",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/cdbc2e271529f467b278b2760f12ee0b5d6930d3/comments",
      "author": {
        "login": "matthewarmand",
        "id": 4631191,
        "node_id": "MDQ6VXNlcjQ2MzExOTE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/4631191?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/matthewarmand",
        "html_url": "https://github.com/matthewarmand",
        "followers_url": "https://api.github.com/users/matthewarmand/followers",
        "following_url": "https://api.github.com/users/matthewarmand/following{/other_user}",
        "gists_url": "https://api.github.com/users/matthewarmand/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/matthewarmand/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/matthewarmand/subscriptions",
        "organizations_url": "https://api.github.com/users/matthewarmand/orgs",
        "repos_url": "https://api.github.com/users/matthewarmand/repos",
        "events_url": "https://api.github.com/users/matthewarmand/events{/privacy}",
        "received_events_url": "https://api.github.com/users/matthewarmand/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "22db55a8896b69e53d0a3cc2764c27b832c81478",
          "url": "https://api.github.com/repos/psf/requests/commits/22db55a8896b69e53d0a3cc2764c27b832c81478",
          "html_url": "https://github.com/psf/requests/commit/22db55a8896b69e53d0a3cc2764c27b832c81478"
        }
      ]
    },
    {
      "sha": "fecf3dc472ddc78e20e96ea0b18e1589110c1d5e",
      "node_id": "C_kwDOABTKOtoAKGZlY2YzZGM0NzJkZGM3OGUyMGU5NmVhMGIxOGUxNTg5MTEwYzFkNWU",
      "commit": {
        "author": {
          "name": "cpzt",
          "email": "chenpan9012@gmail.com",
          "date": "2023-07-30T01:01:42Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-07-30T01:01:42Z"
        },
        "message": "add docstring parameter `hooks` (#6456)",
        "tree": {
          "sha": "66a6f731175f23fce39b6fb7bcf1e08d049603c7",
          "url": "https://api.github.com/repos/psf/requests/git/trees/66a6f731175f23fce39b6fb7bcf1e08d049603c7"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/fecf3dc472ddc78e20e96ea0b18e1589110c1d5e",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJkxbZ3CRBK7hj4Ov3rIwAA9KsIACDdHqz1P7HI+/CAU7N0fbsm\nHWNd1xcIFgaeJgHMbk5ULwqGW07pGhPEiv9VJxA3nGpuSUTNTy7FCwyr4I6j14K+\n0MZi294EUOcbe4fv2HUNejr9Zq9EefNMi+aKcaX0k4UCr2JbvkeCgebmKc1Fem7I\nJfR+Wo8O25SL3VLx023Q1fdEgpVDFG6ZNFTRuswoWYzhpjF9UQLkW5YNXN5uHxOX\n1GmNkEsJ8D44ia0U+FvLLeomElEbyhoct1n4SA9q+8Y7pm3gYye3oddgp0O3ebM9\nOSX12+FhEyo7PB7MW8ejDbh24UpBZHdEsBizDZpqX7irMAVJpW13xZW5XVp3TyA=\n=iWmV\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 66a6f731175f23fce39b6fb7bcf1e08d049603c7\nparent cdbc2e271529f467b278b2760f12ee0b5d6930d3\nauthor cpzt <chenpan9012@gmail.com> 1690678902 +0800\ncommitter GitHub <noreply@github.com> 1690678902 -0700\n\nadd docstring parameter `hooks` (#6456)\n\n",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/fecf3dc472ddc78e20e96ea0b18e1589110c1d5e",
      "html_url": "https://github.com/psf/requests/commit/fecf3dc472ddc78e20e96ea0b18e1589110c1d5e",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/fecf3dc472ddc78e20e96ea0b18e1589110c1d5e/comments",
      "author": {
        "login": "cpzt",
        "id": 20849658,
        "node_id": "MDQ6VXNlcjIwODQ5NjU4",
        "avatar_url": "https://avatars.githubusercontent.com/u/20849658?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/cpzt",
        "html_url": "https://github.com/cpzt",
        "followers_url": "https://api.github.com/users/cpzt/followers",
        "following_url": "https://api.github.com/users/cpzt/following{/other_user}",
        "gists_url": "https://api.github.com/users/cpzt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/cpzt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/cpzt/subscriptions",
        "organizations_url": "https://api.github.com/users/cpzt/orgs",
        "repos_url": "https://api.github.com/users/cpzt/repos",
        "events_url": "https://api.github.com/users/cpzt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/cpzt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "cdbc2e271529f467b278b2760f12ee0b5d6930d3",
          "url": "https://api.github.com/repos/psf/requests/commits/cdbc2e271529f467b278b2760f12ee0b5d6930d3",
          "html_url": "https://github.com/psf/requests/commit/cdbc2e271529f467b278b2760f12ee0b5d6930d3"
        }
      ]
    },
    {
      "sha": "2ecdb685619340735fa85d253c4779029957246f",
      "node_id": "C_kwDOABTKOtoAKDJlY2RiNjg1NjE5MzQwNzM1ZmE4NWQyNTNjNDc3OTAyOTk1NzI0NmY",
      "commit": {
        "author": {
          "name": "Alexandre Erwin Ittner",
          "email": "alexandre@ittner.com.br",
          "date": "2023-07-30T01:50:43Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-07-30T01:50:43Z"
        },
        "message": "Update reference to \"cookielib\" to \"cookiejar\" in documentation (#6214)",
        "tree": {
          "sha": "1d33eefc1c2ee5dbc13afdfea934fa73887965f9",
          "url": "https://api.github.com/repos/psf/requests/git/trees/1d33eefc1c2ee5dbc13afdfea934fa73887965f9"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/2ecdb685619340735fa85d253c4779029957246f",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJkxcHzCRBK7hj4Ov3rIwAACAUIAFRacHAfNsSl92gvaG7x+Ek6\nrh//aDjnRz+ERvyLcjMPm2T1yzmDKRmKw774sOFoMV0ZACDxE/W0rIyzYaRS4ztu\n0tM1n03VsgDAAnwVa+ig7g15kuyzTfA97Oxe/QO9hjpCTnkLTsS9mLLi3ktg7oAc\nHHbbOv+8tlQDbkKx2wFZJaebNy+FvabSiG2HFzyPliZIlaoPlm1OjhjT+rycmmMk\nIEiSqeEnfzpok8FXlRWcvESLlplQOTc5M02uR96S2+skzWB6PPZgNHChObb+Px3Y\nhkasXvVG8oCkrebEESiwiQOAuqEuFUCwt/zDzLdkQuUSWQScDG/b/dQ6JV0xPkM=\n=EYs5\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 1d33eefc1c2ee5dbc13afdfea934fa73887965f9\nparent fecf3dc472ddc78e20e96ea0b18e1589110c1d5e\nauthor Alexandre Erwin Ittner <alexandre@ittner.com.br> 1690681843 -0300\ncommitter GitHub <noreply@github.com> 1690681843 -0700\n\nUpdate reference to \"cookielib\" to \"cookiejar\" in documentation (#6214)\n\n",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/2ecdb685619340735fa85d253c4779029957246f",
      "html_url": "https://github.com/psf/requests/commit/2ecdb685619340735fa85d253c4779029957246f",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/2ecdb685619340735fa85d253c4779029957246f/comments",
      "author": {
        "login": "ittner",
        "id": 110642,
        "node_id": "MDQ6VXNlcjExMDY0Mg==",
        "avatar_url": "https://avatars.githubusercontent.com/u/110642?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/ittner",
        "html_url": "https://github.com/ittner",
        "followers_url": "https://api.github.com/users/ittner/followers",
        "following_url": "https://api.github.com/users/ittner/following{/other_user}",
        "gists_url": "https://api.github.com/users/ittner/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/ittner/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/ittner/subscriptions",
        "organizations_url": "https://api.github.com/users/ittner/orgs",
        "repos_url": "https://api.github.com/users/ittner/repos",
        "events_url": "https://api.github.com/users/ittner/events{/privacy}",
        "received_events_url": "https://api.github.com/users/ittner/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "fecf3dc472ddc78e20e96ea0b18e1589110c1d5e",
          "url": "https://api.github.com/repos/psf/requests/commits/fecf3dc472ddc78e20e96ea0b18e1589110c1d5e",
          "html_url": "https://github.com/psf/requests/commit/fecf3dc472ddc78e20e96ea0b18e1589110c1d5e"
        }
      ]
    },
    {
      "sha": "dfe46c1b7f55c9377caecba2119be14d3cce74e5",
      "node_id": "C_kwDOABTKOtoAKGRmZTQ2YzFiN2Y1NWM5Mzc3Y2FlY2JhMjExOWJlMTRkM2NjZTc0ZTU",
      "commit": {
        "author": {
          "name": "Kevin Kirsche",
          "email": "kevin.kirsche@one.verizon.com",
          "date": "2023-07-30T01:55:18Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-07-30T01:55:18Z"
        },
        "message": "refactor: prefer dictionary comphrension to loop (#6187)",
        "tree": {
          "sha": "b62a17dcde4c5521b253582517f35d3716f76bfa",
          "url": "https://api.github.com/repos/psf/requests/git/trees/b62a17dcde4c5521b253582517f35d3716f76bfa"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/dfe46c1b7f55c9377caecba2119be14d3cce74e5",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJkxcMGCRBK7hj4Ov3rIwAAxeQIACBA+NQdU/FjmTUDHqz+2nX8\nMXcu2gIxl650cYCCCKGF7ikaR4eBJvrglfVz8gUijAPaK7pZTyc2oZ9WWgdOyqH2\nWuzAL+CMWeKyd2lCzylu71Lag/aJeygBlx1qaDuMTAQbv0OQgGHQqllDbMBWcCnl\nohlkBd1zuhUe/sMTXZwHDER33tuBa+gbqhghArakorNU+8cfz3JuCg/juF7FeJnW\nzq/oZW3HD02PcX+8vqAo8DQGNqSmyl0rfqtqsUsR4K9x6pg/aQNfdBm3Q6AQ9uPl\nEz7OrPBSAuf7CgyX/5hhjvIboDXq4JEojdc1V253KorsD4u3o8SKmEARDlHVzC4=\n=1lnU\n-----END PGP SIGNATURE-----\n",
          "payload": "tree b62a17dcde4c5521b253582517f35d3716f76bfa\nparent 2ecdb685619340735fa85d253c4779029957246f\nauthor Kevin Kirsche <kevin.kirsche@one.verizon.com> 1690682118 -0400\ncommitter GitHub <noreply@github.com> 1690682118 -0700\n\nrefactor: prefer dictionary comphrension to loop (#6187)\n\n",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/dfe46c1b7f55c9377caecba2119be14d3cce74e5",
      "html_url": "https://github.com/psf/requests/commit/dfe46c1b7f55c9377caecba2119be14d3cce74e5",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/dfe46c1b7f55c9377caecba2119be14d3cce74e5/comments",
      "author": null,
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "2ecdb685619340735fa85d253c4779029957246f",
          "url": "https://api.github.com/repos/psf/requests/commits/2ecdb685619340735fa85d253c4779029957246f",
          "html_url": "https://github.com/psf/requests/commit/2ecdb685619340735fa85d253c4779029957246f"
        }
      ]
    },
    {
      "sha": "aa4cc78627bcf8ff87b73422ec06748d833c7a15",
      "node_id": "C_kwDOABTKOtoAKGFhNGNjNzg2MjdiY2Y4ZmY4N2I3MzQyMmVjMDY3NDhkODMzYzdhMTU",
      "commit": {
        "author": {
          "name": "Calle Svensson",
          "email": "calle.svensson@zeta-two.com",
          "date": "2023-07-30T04:05:44Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-07-30T04:05:44Z"
        },
        "message": "Add note about adapter prefix match to docs (#6465)",
        "tree": {
          "sha": "5efdd22b33e133e0ae714b7c7989b362a8550f2e",
          "url": "https://api.github.com/repos/psf/requests/git/trees/5efdd22b33e133e0ae714b7c7989b362a8550f2e"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/aa4cc78627bcf8ff87b73422ec06748d833c7a15",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJkxeGYCRBK7hj4Ov3rIwAAIoEIAEOEJTUJazjlJT7CsRWbB5sY\no2YpJrBFM0YyFGVTleuBfb2wdBRhQz3LJ8Rewa6A89e6EbLdxO85GPPg4uLzK08e\nAUpUxef2O4DRUTXTkxc2Z1f8fqtXTa2bYtSwVIBrOI7tngVu/EwDKtm9ZqZdmm4G\nLs7uW0lR1UZGfoZ0QJH2BOgvx35w7RGD+Qt0rY4K5NmizxLPvHtC68sf+x8QR9KX\njjcOGpvEhfhJcHVjxNbdY/chp4Hd/1QrfhCDlX7tW51S9qyjVrpDMx++bOqd8PrA\nG+1mBsUcY+eFv4BPG2uRLKRQ0DB4y0T+0naksaD/Y3Tyz/7RKI1vcHfLXQHZb9Y=\n=bVyi\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 5efdd22b33e133e0ae714b7c7989b362a8550f2e\nparent dfe46c1b7f55c9377caecba2119be14d3cce74e5\nauthor Calle Svensson <calle.svensson@zeta-two.com> 1690689944 +0200\ncommitter GitHub <noreply@github.com> 1690689944 -0700\n\nAdd note about adapter prefix match to docs (#6465)\n\n",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/aa4cc78627bcf8ff87b73422ec06748d833c7a15",
      "html_url": "https://github.com/psf/requests/commit/aa4cc78627bcf8ff87b73422ec06748d833c7a15",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/aa4cc78627bcf8ff87b73422ec06748d833c7a15/comments",
      "author": {
        "login": "ZetaTwo",
        "id": 870392,
        "node_id": "MDQ6VXNlcjg3MDM5Mg==",
        "avatar_url": "https://avatars.githubusercontent.com/u/870392?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/ZetaTwo",
        "html_url": "https://github.com/ZetaTwo",
        "followers_url": "https://api.github.com/users/ZetaTwo/followers",
        "following_url": "https://api.github.com/users/ZetaTwo/following{/other_user}",
        "gists_url": "https://api.github.com/users/ZetaTwo/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/ZetaTwo/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/ZetaTwo/subscriptions",
        "organizations_url": "https://api.github.com/users/ZetaTwo/orgs",
        "repos_url": "https://api.github.com/users/ZetaTwo/repos",
        "events_url": "https://api.github.com/users/ZetaTwo/events{/privacy}",
        "received_events_url": "https://api.github.com/users/ZetaTwo/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "dfe46c1b7f55c9377caecba2119be14d3cce74e5",
          "url": "https://api.github.com/repos/psf/requests/commits/dfe46c1b7f55c9377caecba2119be14d3cce74e5",
          "html_url": "https://github.com/psf/requests/commit/dfe46c1b7f55c9377caecba2119be14d3cce74e5"
        }
      ]
    },
    {
      "sha": "cb7fcd7ebddb45917fb7a526d3627feb2d7738b9",
      "node_id": "C_kwDOABTKOtoAKGNiN2ZjZDdlYmRkYjQ1OTE3ZmI3YTUyNmQzNjI3ZmViMmQ3NzM4Yjk",
      "commit": {
        "author": {
          "name": "Joren Vrancken",
          "email": "jorenvrancken@gmail.com",
          "date": "2023-08-12T17:53:36Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-08-12T17:53:36Z"
        },
        "message": "Specify that Session.headers needs to be set to a OrderedDict in Header Ordering docs (#6475)",
        "tree": {
          "sha": "daf96f8b1d6ad82486c70191b464bddd20e3d87b",
          "url": "https://api.github.com/repos/psf/requests/git/trees/daf96f8b1d6ad82486c70191b464bddd20e3d87b"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/cb7fcd7ebddb45917fb7a526d3627feb2d7738b9",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk18cgCRBK7hj4Ov3rIwAAKpsIAEHrnOLPyErsqFAG1cZIwJBM\nlUwNmCT0yhnzg9GLUD19Kw0hoc0f5LOBpnLZjg1wMCyWTgCSmrojflE9cw0gL5CQ\nxjLEXPWmGVwPElzAXD+4MZVVlZu6wqra8vC1xGoGpchjYGAqihhZb6e5gBHdVBq2\nKaQsz1bM6lm/aWen+5J0HoC2rQ5TTnTu+L9GZrm4JqfcbFr601FCocw7ioMxoDzv\n4ur77Nl71DjAfdbha/Zqb9UI80N9yRq41pCOWuUxH2fLzdXagYO4hDVNAfdL5zHq\nQN1tmiz0ULKL2DEX5rsSeuUPDUe+OrNM7bDSGdvCKznJsx/Ll/zLkuccDWzUymM=\n=DxhP\n-----END PGP SIGNATURE-----\n",
          "payload": "tree daf96f8b1d6ad82486c70191b464bddd20e3d87b\nparent aa4cc78627bcf8ff87b73422ec06748d833c7a15\nauthor Joren Vrancken <jorenvrancken@gmail.com> 1691862816 +0200\ncommitter GitHub <noreply@github.com> 1691862816 -0700\n\nSpecify that Session.headers needs to be set to a OrderedDict in Header Ordering docs (#6475)\n\n",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/cb7fcd7ebddb45917fb7a526d3627feb2d7738b9",
      "html_url": "https://github.com/psf/requests/commit/cb7fcd7ebddb45917fb7a526d3627feb2d7738b9",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/cb7fcd7ebddb45917fb7a526d3627feb2d7738b9/comments",
      "author": {
        "login": "joren485",
        "id": 7031489,
        "node_id": "MDQ6VXNlcjcwMzE0ODk=",
        "avatar_url": "https://avatars.githubusercontent.com/u/7031489?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/joren485",
        "html_url": "https://github.com/joren485",
        "followers_url": "https://api.github.com/users/joren485/followers",
        "following_url": "https://api.github.com/users/joren485/following{/other_user}",
        "gists_url": "https://api.github.com/users/joren485/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/joren485/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/joren485/subscriptions",
        "organizations_url": "https://api.github.com/users/joren485/orgs",
        "repos_url": "https://api.github.com/users/joren485/repos",
        "events_url": "https://api.github.com/users/joren485/events{/privacy}",
        "received_events_url": "https://api.github.com/users/joren485/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "aa4cc78627bcf8ff87b73422ec06748d833c7a15",
          "url": "https://api.github.com/repos/psf/requests/commits/aa4cc78627bcf8ff87b73422ec06748d833c7a15",
          "html_url": "https://github.com/psf/requests/commit/aa4cc78627bcf8ff87b73422ec06748d833c7a15"
        }
      ]
    },
    {
      "sha": "9b6c62e235429eeaa059544d1516d5e0c58c9a7f",
      "node_id": "C_kwDOABTKOtoAKDliNmM2MmUyMzU0MjllZWFhMDU5NTQ0ZDE1MTZkNWUwYzU4YzlhN2Y",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2023-08-12T18:37:15Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-08-12T18:37:15Z"
        },
        "message": "Merge branch 'main' into spdx-conform-license",
        "tree": {
          "sha": "aa5ed3c21f93fd9172c3ceec03c00043c78775e7",
          "url": "https://api.github.com/repos/psf/requests/git/trees/aa5ed3c21f93fd9172c3ceec03c00043c78775e7"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/9b6c62e235429eeaa059544d1516d5e0c58c9a7f",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk19FbCRBK7hj4Ov3rIwAA4sgIABXe9zF8s1yIm2YjHeiV+Zxy\n8zV2CPTZUem50ZRVVELu0DbX6aNz4WI744W2YTcXRjagKfi4DSP2VWNwiAR0Q/qn\nbu+KlH7kFLogB60w7ZBSsTr7g1kCL9DmPKOks+Gi8FqVxci/2ov7AvGlWiO8qcoN\nx7KPa2PJtvwVym9OLZh3i/ra4AUD9hEG522c1vcv85jQmLBmSXWKsX/0FRJGnloF\nhAgVqaf7PE2ZbdjJrBEJ0Mrgru9pASTviG3StQPhxwQP6ivu5F7di9ciwLrd4Vl0\njUCSRylvxWEfDL+naE+7nSz33zItmIjjuRo5wJCkmDLqBIlvpnVi5/ze1aD+iNw=\n=+1Lh\n-----END PGP SIGNATURE-----\n",
          "payload": "tree aa5ed3c21f93fd9172c3ceec03c00043c78775e7\nparent 53a0562331c4a825036a347e77984d68b310fcf3\nparent cb7fcd7ebddb45917fb7a526d3627feb2d7738b9\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1691865435 -0700\ncommitter GitHub <noreply@github.com> 1691865435 -0700\n\nMerge branch 'main' into spdx-conform-license",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/9b6c62e235429eeaa059544d1516d5e0c58c9a7f",
      "html_url": "https://github.com/psf/requests/commit/9b6c62e235429eeaa059544d1516d5e0c58c9a7f",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/9b6c62e235429eeaa059544d1516d5e0c58c9a7f/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "53a0562331c4a825036a347e77984d68b310fcf3",
          "url": "https://api.github.com/repos/psf/requests/commits/53a0562331c4a825036a347e77984d68b310fcf3",
          "html_url": "https://github.com/psf/requests/commit/53a0562331c4a825036a347e77984d68b310fcf3"
        },
        {
          "sha": "cb7fcd7ebddb45917fb7a526d3627feb2d7738b9",
          "url": "https://api.github.com/repos/psf/requests/commits/cb7fcd7ebddb45917fb7a526d3627feb2d7738b9",
          "html_url": "https://github.com/psf/requests/commit/cb7fcd7ebddb45917fb7a526d3627feb2d7738b9"
        }
      ]
    },
    {
      "sha": "34a64bc65ee12dbe8d6cfd15e33e9ee632942dd2",
      "node_id": "C_kwDOABTKOtoAKDM0YTY0YmM2NWVlMTJkYmU4ZDZjZmQxNWUzM2U5ZWU2MzI5NDJkZDI",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2023-08-12T18:51:42Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-08-12T18:51:42Z"
        },
        "message": "Merge pull request #6266 from elprimato/spdx-conform-license\n\nChange to SPDX conform license string",
        "tree": {
          "sha": "aa5ed3c21f93fd9172c3ceec03c00043c78775e7",
          "url": "https://api.github.com/repos/psf/requests/git/trees/aa5ed3c21f93fd9172c3ceec03c00043c78775e7"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/34a64bc65ee12dbe8d6cfd15e33e9ee632942dd2",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk19S+CRBK7hj4Ov3rIwAAAokIAKxQew6UVRYzu4JB/FUi7hVj\nOEr2x11Y6n7bLzO0X2L9LoaMnnuXctX5YlBSF7kXX72+PvhuLPYlyNyh/yid0Dq2\nvv8xElc0irZ+MHMC3VIEQjfa02T6pCS/+AlC7e0t+IdF7jPbn9Ly75iZCF9poYEP\n1fwVOlxIOQt9mM6MU0o627qyHha59l4XM/IcQAzrItkXRxZv+DfbB13tDJTfqlJP\nc7jbrhjrdH1G41CTJRRPV5Ed8WpttzyR396XshTZ7UIMSx2LRYExd8YKXVhfHA7Z\n09GTLrCp/5JkJ7MD4p8eGWPNCfH6lMq0q7VjgP5D7mbFebkxkvNPtHWhcO7LUaE=\n=QyZE\n-----END PGP SIGNATURE-----\n",
          "payload": "tree aa5ed3c21f93fd9172c3ceec03c00043c78775e7\nparent cb7fcd7ebddb45917fb7a526d3627feb2d7738b9\nparent 9b6c62e235429eeaa059544d1516d5e0c58c9a7f\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1691866302 -0500\ncommitter GitHub <noreply@github.com> 1691866302 -0500\n\nMerge pull request #6266 from elprimato/spdx-conform-license\n\nChange to SPDX conform license string",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/34a64bc65ee12dbe8d6cfd15e33e9ee632942dd2",
      "html_url": "https://github.com/psf/requests/commit/34a64bc65ee12dbe8d6cfd15e33e9ee632942dd2",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/34a64bc65ee12dbe8d6cfd15e33e9ee632942dd2/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "cb7fcd7ebddb45917fb7a526d3627feb2d7738b9",
          "url": "https://api.github.com/repos/psf/requests/commits/cb7fcd7ebddb45917fb7a526d3627feb2d7738b9",
          "html_url": "https://github.com/psf/requests/commit/cb7fcd7ebddb45917fb7a526d3627feb2d7738b9"
        },
        {
          "sha": "9b6c62e235429eeaa059544d1516d5e0c58c9a7f",
          "url": "https://api.github.com/repos/psf/requests/commits/9b6c62e235429eeaa059544d1516d5e0c58c9a7f",
          "html_url": "https://github.com/psf/requests/commit/9b6c62e235429eeaa059544d1516d5e0c58c9a7f"
        }
      ]
    },
    {
      "sha": "2c193bda0c50481d3bff4ef4d90203c578afa294",
      "node_id": "C_kwDOABTKOtoAKDJjMTkzYmRhMGM1MDQ4MWQzYmZmNGVmNGQ5MDIwM2M1NzhhZmEyOTQ",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2023-08-12T19:02:58Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-08-12T19:02:58Z"
        },
        "message": "Pin GHA workflows and add dependabot to keep them up to date (#6497)",
        "tree": {
          "sha": "d95d4d468a3212e2bbdf1acd34705f4d8b79bca0",
          "url": "https://api.github.com/repos/psf/requests/git/trees/d95d4d468a3212e2bbdf1acd34705f4d8b79bca0"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/2c193bda0c50481d3bff4ef4d90203c578afa294",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk19diCRBK7hj4Ov3rIwAAF+QIAADELW+kUW4s4Ew0bh+uH8yp\nRD6pKLSIwhl82A3tRC88MMbLl87rNYX+oDa9+T6tE0ZqnC5dELdruxfn4N0VFKiz\n9FcS+1pwZ/mPXfsvIq1mbRFh7n4bd11WL5WnKQXza8bCQm5jNfDdkg9IwFepGne3\nXd11DGKQBREHYo/gmISee/LW+47mjfPfm8huz07Oyc1VMpyJLdUoZukXRLC6a3GA\njeWxwynfs124NM3JBt2jaGwyDkGlQumju6y7hL47FVnMNtbi6AlxW6PEux4Wo42g\nNBN3V09lyYo5EBXBGmZcAQV0bZo1e9T1lcgH6l6bNkM0oL3wAszu7KKgTItN+wU=\n=wrvS\n-----END PGP SIGNATURE-----\n",
          "payload": "tree d95d4d468a3212e2bbdf1acd34705f4d8b79bca0\nparent 34a64bc65ee12dbe8d6cfd15e33e9ee632942dd2\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1691866978 -0700\ncommitter GitHub <noreply@github.com> 1691866978 -0700\n\nPin GHA workflows and add dependabot to keep them up to date (#6497)\n\n",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/2c193bda0c50481d3bff4ef4d90203c578afa294",
      "html_url": "https://github.com/psf/requests/commit/2c193bda0c50481d3bff4ef4d90203c578afa294",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/2c193bda0c50481d3bff4ef4d90203c578afa294/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "34a64bc65ee12dbe8d6cfd15e33e9ee632942dd2",
          "url": "https://api.github.com/repos/psf/requests/commits/34a64bc65ee12dbe8d6cfd15e33e9ee632942dd2",
          "html_url": "https://github.com/psf/requests/commit/34a64bc65ee12dbe8d6cfd15e33e9ee632942dd2"
        }
      ]
    },
    {
      "sha": "8112fcc7beb15e1cdc66180c10a3290174866828",
      "node_id": "C_kwDOABTKOtoAKDgxMTJmY2M3YmViMTVlMWNkYzY2MTgwYzEwYTMyOTAxNzQ4NjY4Mjg",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2023-08-12T19:03:10Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-08-12T19:03:10Z"
        },
        "message": "Pre commit update (#6498)",
        "tree": {
          "sha": "7f789078010cccf910d46419b80258b7cc2c0019",
          "url": "https://api.github.com/repos/psf/requests/git/trees/7f789078010cccf910d46419b80258b7cc2c0019"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/8112fcc7beb15e1cdc66180c10a3290174866828",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk19duCRBK7hj4Ov3rIwAAR1kIAFYB1fgxZ4arFr+SwXOr+ISP\nbBEHFAumU9eHY3gkFOl6DdHFkBUx249YtPvDdFABfwYU7l2ezHFcD4SZPWEh+W+c\nmpnGum/r4tjsTE48PI8yLxsXf75dNYVlC62+JlgJaFAHA7g6XI7O+XDWgWpv5Q8k\njXOV1lquzIzXa8SfZYWAzAn8SgvaTejh1/F8mU5Kp0QrN+nBuEiswVWvhOvP3RCn\nsZeVCSLzlyngM3/4V+aMQvNHIQRmxrt4gmLHC8Q8amwWf7yaFaYhRFYgBxZzmIo4\nLjcX6/c0I5hMKF1JFU+HpIhSarvFUDFyYFBusXPgYHtpgHgYPUGxdIC6TpoIm9k=\n=tf4m\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 7f789078010cccf910d46419b80258b7cc2c0019\nparent 2c193bda0c50481d3bff4ef4d90203c578afa294\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1691866990 -0700\ncommitter GitHub <noreply@github.com> 1691866990 -0700\n\nPre commit update (#6498)\n\n",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/8112fcc7beb15e1cdc66180c10a3290174866828",
      "html_url": "https://github.com/psf/requests/commit/8112fcc7beb15e1cdc66180c10a3290174866828",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/8112fcc7beb15e1cdc66180c10a3290174866828/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "2c193bda0c50481d3bff4ef4d90203c578afa294",
          "url": "https://api.github.com/repos/psf/requests/commits/2c193bda0c50481d3bff4ef4d90203c578afa294",
          "html_url": "https://github.com/psf/requests/commit/2c193bda0c50481d3bff4ef4d90203c578afa294"
        }
      ]
    },
    {
      "sha": "ea49261a279c9e8216f25410a9e9611b758c2611",
      "node_id": "C_kwDOABTKOtoAKGVhNDkyNjFhMjc5YzllODIxNmYyNTQxMGE5ZTk2MTFiNzU4YzI2MTE",
      "commit": {
        "author": {
          "name": "dependabot[bot]",
          "email": "49699333+dependabot[bot]@users.noreply.github.com",
          "date": "2023-08-12T19:03:17Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-08-12T19:03:17Z"
        },
        "message": "Bump dessant/lock-threads from 3.0.0 to 4.0.1\n\nBumps [dessant/lock-threads](https://github.com/dessant/lock-threads) from 3.0.0 to 4.0.1.\n- [Release notes](https://github.com/dessant/lock-threads/releases)\n- [Changelog](https://github.com/dessant/lock-threads/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/dessant/lock-threads/compare/e460dfeb36e731f3aeb214be6b0c9a9d9a67eda6...be8aa5be94131386884a6da4189effda9b14aa21)\n\n---\nupdated-dependencies:\n- dependency-name: dessant/lock-threads\n  dependency-type: direct:production\n  update-type: version-update:semver-major\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
        "tree": {
          "sha": "17a1e118a56221c848361a8837a9e3a607e2c0b5",
          "url": "https://api.github.com/repos/psf/requests/git/trees/17a1e118a56221c848361a8837a9e3a607e2c0b5"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/ea49261a279c9e8216f25410a9e9611b758c2611",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk19d1CRBK7hj4Ov3rIwAA5vcIAEY++hvNIl+7/i9zw0gKevDo\ns5H77kAMyYhtzALkJUEEd6njMjpfSkNMZcV3XltiVzReYgkS59xa6++sdTItQu9/\nXQMvSd9JdbEW3HGoOcUp+mkFCYg0/fqzdNINx973NWjrZZeTDJ+aHzPyOjmJ7I8l\ngTlq4n4tS667PBxXWTZzS9C62D2F4asUz3zPlKb9tsaDjz0jNNd0kb+LDoimzZmo\n0kMHMgOr+PNkZRycYMs0LXpVwqmbgT7in+A8i4y0dznDRPomNcUxxM1O9u/ILz9Y\nS2ojcII2NX/ssH4ypt0bbecTCNPOAnva/EHlL+3L5OKZv0Z2ZpD8L24sRxW5Ifo=\n=0udb\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 17a1e118a56221c848361a8837a9e3a607e2c0b5\nparent 2c193bda0c50481d3bff4ef4d90203c578afa294\nauthor dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> 1691866997 +0000\ncommitter GitHub <noreply@github.com> 1691866997 +0000\n\nBump dessant/lock-threads from 3.0.0 to 4.0.1\n\nBumps [dessant/lock-threads](https://github.com/dessant/lock-threads) from 3.0.0 to 4.0.1.\n- [Release notes](https://github.com/dessant/lock-threads/releases)\n- [Changelog](https://github.com/dessant/lock-threads/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/dessant/lock-threads/compare/e460dfeb36e731f3aeb214be6b0c9a9d9a67eda6...be8aa5be94131386884a6da4189effda9b14aa21)\n\n---\nupdated-dependencies:\n- dependency-name: dessant/lock-threads\n  dependency-type: direct:production\n  update-type: version-update:semver-major\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/ea49261a279c9e8216f25410a9e9611b758c2611",
      "html_url": "https://github.com/psf/requests/commit/ea49261a279c9e8216f25410a9e9611b758c2611",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/ea49261a279c9e8216f25410a9e9611b758c2611/comments",
      "author": {
        "login": "dependabot[bot]",
        "id": 49699333,
        "node_id": "MDM6Qm90NDk2OTkzMzM=",
        "avatar_url": "https://avatars.githubusercontent.com/in/29110?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/dependabot%5Bbot%5D",
        "html_url": "https://github.com/apps/dependabot",
        "followers_url": "https://api.github.com/users/dependabot%5Bbot%5D/followers",
        "following_url": "https://api.github.com/users/dependabot%5Bbot%5D/following{/other_user}",
        "gists_url": "https://api.github.com/users/dependabot%5Bbot%5D/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/dependabot%5Bbot%5D/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/dependabot%5Bbot%5D/subscriptions",
        "organizations_url": "https://api.github.com/users/dependabot%5Bbot%5D/orgs",
        "repos_url": "https://api.github.com/users/dependabot%5Bbot%5D/repos",
        "events_url": "https://api.github.com/users/dependabot%5Bbot%5D/events{/privacy}",
        "received_events_url": "https://api.github.com/users/dependabot%5Bbot%5D/received_events",
        "type": "Bot",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "2c193bda0c50481d3bff4ef4d90203c578afa294",
          "url": "https://api.github.com/repos/psf/requests/commits/2c193bda0c50481d3bff4ef4d90203c578afa294",
          "html_url": "https://github.com/psf/requests/commit/2c193bda0c50481d3bff4ef4d90203c578afa294"
        }
      ]
    },
    {
      "sha": "c7933453cff05a297d4d1cdacb7fb49480e6924c",
      "node_id": "C_kwDOABTKOtoAKGM3OTMzNDUzY2ZmMDVhMjk3ZDRkMWNkYWNiN2ZiNDk0ODBlNjkyNGM",
      "commit": {
        "author": {
          "name": "dependabot[bot]",
          "email": "49699333+dependabot[bot]@users.noreply.github.com",
          "date": "2023-08-12T19:03:22Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-08-12T19:03:22Z"
        },
        "message": "Bump actions/setup-python from 2.3.4 to 4.7.0\n\nBumps [actions/setup-python](https://github.com/actions/setup-python) from 2.3.4 to 4.7.0.\n- [Release notes](https://github.com/actions/setup-python/releases)\n- [Commits](https://github.com/actions/setup-python/compare/v2.3.4...61a6322f88396a6271a6ee3565807d608ecaddd1)\n\n---\nupdated-dependencies:\n- dependency-name: actions/setup-python\n  dependency-type: direct:production\n  update-type: version-update:semver-major\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
        "tree": {
          "sha": "80bf057bf9a42bed4797ee81e145a5679678f368",
          "url": "https://api.github.com/repos/psf/requests/git/trees/80bf057bf9a42bed4797ee81e145a5679678f368"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/c7933453cff05a297d4d1cdacb7fb49480e6924c",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk19d6CRBK7hj4Ov3rIwAAmicIAJC1gC6OhxzANhiU+XqUN0xF\nfaiBeV/VauHWfBWJm+1XRtCC23jDnRgNROYZIa6C8YNidGxV7dkUs9tBgZtKG5xD\n1DwKgCeHhsn6IuShaPpCRJC/OuyBRJdTi+cvSiLCAt2GRDgvKwsKmpfi+Z4AWeMz\nIEPO/5kZjCDpK40VUxBlGu/OLq13z8f5ohE399JWU9snWCRU0H+ccnTWVTSQjgfz\nHhiisqA7gkHdQJ9OTiNZgTDwHgnxkLfBl8Go0hnWT6An2/aC54jfJ2AK2AV41bO9\nSPRJ7bwlgWgjuZ+B3r4iP311YzJL7Jha+wXHUaC+J9vGXrhIqcEhUS5crr4xsd0=\n=KzSl\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 80bf057bf9a42bed4797ee81e145a5679678f368\nparent 2c193bda0c50481d3bff4ef4d90203c578afa294\nauthor dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> 1691867002 +0000\ncommitter GitHub <noreply@github.com> 1691867002 +0000\n\nBump actions/setup-python from 2.3.4 to 4.7.0\n\nBumps [actions/setup-python](https://github.com/actions/setup-python) from 2.3.4 to 4.7.0.\n- [Release notes](https://github.com/actions/setup-python/releases)\n- [Commits](https://github.com/actions/setup-python/compare/v2.3.4...61a6322f88396a6271a6ee3565807d608ecaddd1)\n\n---\nupdated-dependencies:\n- dependency-name: actions/setup-python\n  dependency-type: direct:production\n  update-type: version-update:semver-major\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/c7933453cff05a297d4d1cdacb7fb49480e6924c",
      "html_url": "https://github.com/psf/requests/commit/c7933453cff05a297d4d1cdacb7fb49480e6924c",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/c7933453cff05a297d4d1cdacb7fb49480e6924c/comments",
      "author": {
        "login": "dependabot[bot]",
        "id": 49699333,
        "node_id": "MDM6Qm90NDk2OTkzMzM=",
        "avatar_url": "https://avatars.githubusercontent.com/in/29110?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/dependabot%5Bbot%5D",
        "html_url": "https://github.com/apps/dependabot",
        "followers_url": "https://api.github.com/users/dependabot%5Bbot%5D/followers",
        "following_url": "https://api.github.com/users/dependabot%5Bbot%5D/following{/other_user}",
        "gists_url": "https://api.github.com/users/dependabot%5Bbot%5D/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/dependabot%5Bbot%5D/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/dependabot%5Bbot%5D/subscriptions",
        "organizations_url": "https://api.github.com/users/dependabot%5Bbot%5D/orgs",
        "repos_url": "https://api.github.com/users/dependabot%5Bbot%5D/repos",
        "events_url": "https://api.github.com/users/dependabot%5Bbot%5D/events{/privacy}",
        "received_events_url": "https://api.github.com/users/dependabot%5Bbot%5D/received_events",
        "type": "Bot",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "2c193bda0c50481d3bff4ef4d90203c578afa294",
          "url": "https://api.github.com/repos/psf/requests/commits/2c193bda0c50481d3bff4ef4d90203c578afa294",
          "html_url": "https://github.com/psf/requests/commit/2c193bda0c50481d3bff4ef4d90203c578afa294"
        }
      ]
    },
    {
      "sha": "9acca90bf6bdb29f80b9c82ff66303bd6fb157fa",
      "node_id": "C_kwDOABTKOtoAKDlhY2NhOTBiZjZiZGIyOWY4MGI5YzgyZmY2NjMwM2JkNmZiMTU3ZmE",
      "commit": {
        "author": {
          "name": "dependabot[bot]",
          "email": "49699333+dependabot[bot]@users.noreply.github.com",
          "date": "2023-08-12T19:03:30Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-08-12T19:03:30Z"
        },
        "message": "Bump github/codeql-action from 1.1.39 to 2.21.3\n\nBumps [github/codeql-action](https://github.com/github/codeql-action) from 1.1.39 to 2.21.3.\n- [Release notes](https://github.com/github/codeql-action/releases)\n- [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/github/codeql-action/compare/231aa2c8a89117b126725a0e11897209b7118144...5b6282e01c62d02e720b81eb8a51204f527c3624)\n\n---\nupdated-dependencies:\n- dependency-name: github/codeql-action\n  dependency-type: direct:production\n  update-type: version-update:semver-major\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
        "tree": {
          "sha": "f308f3a2c83f2847d139566e4096646fa21bfd9c",
          "url": "https://api.github.com/repos/psf/requests/git/trees/f308f3a2c83f2847d139566e4096646fa21bfd9c"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/9acca90bf6bdb29f80b9c82ff66303bd6fb157fa",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk19eCCRBK7hj4Ov3rIwAAZBwIAItciWhulx2/woj/p2OFVa/M\nKoD4bw8TuTyRtqH9nxugkgIG5UiC3Kxf1Hbdaigw1mUpXyCJqp6hDSWlk1eNhDEg\nv63x708QmgacRv/UtzmcGQV7FSDlzbqywW76m9of0IQqFBpzzg7k6jQOd7rebYx/\n8Lg5w8XSsUJVe5LwugePYD+bRAMFCRbVStIR70a0MT0wN+QdASRr3BSh1D4Y56Fh\nehl5ruRSSML5azg3N855v+yDBO2qCY5F5yf1eJCFN3pYLOCHoi+Q3Am4EOH+wQ/f\nU3SVYGmPxLVumDLUg0gBDFUHCcH5qNcKR0vYsC05sVpnlOQy7JwsB/jvMEeXnwo=\n=pW8e\n-----END PGP SIGNATURE-----\n",
          "payload": "tree f308f3a2c83f2847d139566e4096646fa21bfd9c\nparent 2c193bda0c50481d3bff4ef4d90203c578afa294\nauthor dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> 1691867010 +0000\ncommitter GitHub <noreply@github.com> 1691867010 +0000\n\nBump github/codeql-action from 1.1.39 to 2.21.3\n\nBumps [github/codeql-action](https://github.com/github/codeql-action) from 1.1.39 to 2.21.3.\n- [Release notes](https://github.com/github/codeql-action/releases)\n- [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/github/codeql-action/compare/231aa2c8a89117b126725a0e11897209b7118144...5b6282e01c62d02e720b81eb8a51204f527c3624)\n\n---\nupdated-dependencies:\n- dependency-name: github/codeql-action\n  dependency-type: direct:production\n  update-type: version-update:semver-major\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/9acca90bf6bdb29f80b9c82ff66303bd6fb157fa",
      "html_url": "https://github.com/psf/requests/commit/9acca90bf6bdb29f80b9c82ff66303bd6fb157fa",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/9acca90bf6bdb29f80b9c82ff66303bd6fb157fa/comments",
      "author": {
        "login": "dependabot[bot]",
        "id": 49699333,
        "node_id": "MDM6Qm90NDk2OTkzMzM=",
        "avatar_url": "https://avatars.githubusercontent.com/in/29110?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/dependabot%5Bbot%5D",
        "html_url": "https://github.com/apps/dependabot",
        "followers_url": "https://api.github.com/users/dependabot%5Bbot%5D/followers",
        "following_url": "https://api.github.com/users/dependabot%5Bbot%5D/following{/other_user}",
        "gists_url": "https://api.github.com/users/dependabot%5Bbot%5D/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/dependabot%5Bbot%5D/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/dependabot%5Bbot%5D/subscriptions",
        "organizations_url": "https://api.github.com/users/dependabot%5Bbot%5D/orgs",
        "repos_url": "https://api.github.com/users/dependabot%5Bbot%5D/repos",
        "events_url": "https://api.github.com/users/dependabot%5Bbot%5D/events{/privacy}",
        "received_events_url": "https://api.github.com/users/dependabot%5Bbot%5D/received_events",
        "type": "Bot",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "2c193bda0c50481d3bff4ef4d90203c578afa294",
          "url": "https://api.github.com/repos/psf/requests/commits/2c193bda0c50481d3bff4ef4d90203c578afa294",
          "html_url": "https://github.com/psf/requests/commit/2c193bda0c50481d3bff4ef4d90203c578afa294"
        }
      ]
    },
    {
      "sha": "6ad493650c6a4eab659266e300c63f25bc83cf91",
      "node_id": "C_kwDOABTKOtoAKDZhZDQ5MzY1MGM2YTRlYWI2NTkyNjZlMzAwYzYzZjI1YmM4M2NmOTE",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2023-08-12T19:24:59Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-08-12T19:24:59Z"
        },
        "message": "Merge pull request #6499 from psf/dependabot/github_actions/dessant/lock-threads-4.0.1\n\nBump dessant/lock-threads from 3.0.0 to 4.0.1",
        "tree": {
          "sha": "8eb29e56a3da0f1df6050ed9fd5c8019c6c6ba2b",
          "url": "https://api.github.com/repos/psf/requests/git/trees/8eb29e56a3da0f1df6050ed9fd5c8019c6c6ba2b"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/6ad493650c6a4eab659266e300c63f25bc83cf91",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk19yLCRBK7hj4Ov3rIwAA34sIAHpZb4PwJPaoXPkKT99cFNx4\nSwBNJaiYjb5a7G+erW/fJsGVzjkNnQ0dImg7IEhzVTbF8r+sQph3epMvRxtt/bWQ\nnN7P3kkq3E2hc8Ppxck4Vq/IZz2vz1ZsySFWOTx3VWYRR6I9nSDr4bWefqyaIp04\nlgAz1DWAUmRoUbVb+5JYRdbK3aF4DwU2ob56i3BRerr4kJbsvDLYe2KyyXC1hPtx\n50KLx0RyInUOhonWPO5Xbwk0xJZLMZ2jFZRDqSlEW4w5KuU88+i3ntqlZfl6x1NB\nkdnevtxGuXkX7vm/uYdHToV/dmfKbhfBAkiLrFX4Djlfgx+5+v2AnNkIy3aH4G0=\n=uZD3\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 8eb29e56a3da0f1df6050ed9fd5c8019c6c6ba2b\nparent 8112fcc7beb15e1cdc66180c10a3290174866828\nparent ea49261a279c9e8216f25410a9e9611b758c2611\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1691868299 -0700\ncommitter GitHub <noreply@github.com> 1691868299 -0700\n\nMerge pull request #6499 from psf/dependabot/github_actions/dessant/lock-threads-4.0.1\n\nBump dessant/lock-threads from 3.0.0 to 4.0.1",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/6ad493650c6a4eab659266e300c63f25bc83cf91",
      "html_url": "https://github.com/psf/requests/commit/6ad493650c6a4eab659266e300c63f25bc83cf91",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/6ad493650c6a4eab659266e300c63f25bc83cf91/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "8112fcc7beb15e1cdc66180c10a3290174866828",
          "url": "https://api.github.com/repos/psf/requests/commits/8112fcc7beb15e1cdc66180c10a3290174866828",
          "html_url": "https://github.com/psf/requests/commit/8112fcc7beb15e1cdc66180c10a3290174866828"
        },
        {
          "sha": "ea49261a279c9e8216f25410a9e9611b758c2611",
          "url": "https://api.github.com/repos/psf/requests/commits/ea49261a279c9e8216f25410a9e9611b758c2611",
          "html_url": "https://github.com/psf/requests/commit/ea49261a279c9e8216f25410a9e9611b758c2611"
        }
      ]
    },
    {
      "sha": "09a241f59e98c14c085e8f70696610dd1748d0d2",
      "node_id": "C_kwDOABTKOtoAKDA5YTI0MWY1OWU5OGMxNGMwODVlOGY3MDY5NjYxMGRkMTc0OGQwZDI",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2023-08-12T19:36:48Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-08-12T19:36:48Z"
        },
        "message": "Merge pull request #6500 from psf/dependabot/github_actions/actions/setup-python-4.7.0\n\nBump actions/setup-python from 2.3.4 to 4.7.0",
        "tree": {
          "sha": "a1e2fb18af2692a191f863ef8450ae7a85d21293",
          "url": "https://api.github.com/repos/psf/requests/git/trees/a1e2fb18af2692a191f863ef8450ae7a85d21293"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/09a241f59e98c14c085e8f70696610dd1748d0d2",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk199QCRBK7hj4Ov3rIwAAazIIADPW+iOu4MhqcwEfM7zpI2Zz\nn2G7iLfy2LwjVDpqWWOva1G7Zw/FOSULN/fDvHQs/Ph06seLj8QNiax97MBDkwVt\nyPJrWDEQr6nZN5LK3uEUVfxauFjvakFGpZHI/pUQPCVJ3fNLRdLW6llDF/A81HWP\ntAeIR9GkztNsMYqLAOQfN/xd0v1I6GCA5JY9XoIwxxMtpt3ctpwXhARZix+p5LbZ\nGtT3Em1Tg8fYRYWj5QzO4aaLFvsI0Ob2B+QXxs4J9t8cIvBqfSWW7Jkr/5A4i468\nixYd/Bp7LgAWQTfnyQUCJ3rd0Fw8xdNGCSqnhFNlPrPXimRttjfDn9PHSeC87X0=\n=ZRU3\n-----END PGP SIGNATURE-----\n",
          "payload": "tree a1e2fb18af2692a191f863ef8450ae7a85d21293\nparent 6ad493650c6a4eab659266e300c63f25bc83cf91\nparent c7933453cff05a297d4d1cdacb7fb49480e6924c\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1691869008 -0700\ncommitter GitHub <noreply@github.com> 1691869008 -0700\n\nMerge pull request #6500 from psf/dependabot/github_actions/actions/setup-python-4.7.0\n\nBump actions/setup-python from 2.3.4 to 4.7.0",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/09a241f59e98c14c085e8f70696610dd1748d0d2",
      "html_url": "https://github.com/psf/requests/commit/09a241f59e98c14c085e8f70696610dd1748d0d2",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/09a241f59e98c14c085e8f70696610dd1748d0d2/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "6ad493650c6a4eab659266e300c63f25bc83cf91",
          "url": "https://api.github.com/repos/psf/requests/commits/6ad493650c6a4eab659266e300c63f25bc83cf91",
          "html_url": "https://github.com/psf/requests/commit/6ad493650c6a4eab659266e300c63f25bc83cf91"
        },
        {
          "sha": "c7933453cff05a297d4d1cdacb7fb49480e6924c",
          "url": "https://api.github.com/repos/psf/requests/commits/c7933453cff05a297d4d1cdacb7fb49480e6924c",
          "html_url": "https://github.com/psf/requests/commit/c7933453cff05a297d4d1cdacb7fb49480e6924c"
        }
      ]
    },
    {
      "sha": "4bd06cd325f4b7213708ff520f346c177ba218d9",
      "node_id": "C_kwDOABTKOtoAKDRiZDA2Y2QzMjVmNGI3MjEzNzA4ZmY1MjBmMzQ2YzE3N2JhMjE4ZDk",
      "commit": {
        "author": {
          "name": "dependabot[bot]",
          "email": "49699333+dependabot[bot]@users.noreply.github.com",
          "date": "2023-08-12T19:37:22Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-08-12T19:37:22Z"
        },
        "message": "Bump actions/checkout from 2.7.0 to 3.5.3\n\nBumps [actions/checkout](https://github.com/actions/checkout) from 2.7.0 to 3.5.3.\n- [Release notes](https://github.com/actions/checkout/releases)\n- [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/actions/checkout/compare/v2.7.0...c85c95e3d7251135ab7dc9ce3241c5835cc595a9)\n\n---\nupdated-dependencies:\n- dependency-name: actions/checkout\n  dependency-type: direct:production\n  update-type: version-update:semver-major\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
        "tree": {
          "sha": "c024cc83723ddc26097735c0e44f9ff606b00947",
          "url": "https://api.github.com/repos/psf/requests/git/trees/c024cc83723ddc26097735c0e44f9ff606b00947"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/4bd06cd325f4b7213708ff520f346c177ba218d9",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk199yCRBK7hj4Ov3rIwAAOTkIAAdbxVWrucYUftm+JNCGbGjY\nAlvXkQHpjLd4U4cUBR+r7uN1Bp+BC5RvrRerHE3zDqHnCYXKsKjebhscCWUwIP5a\ny2wPADRYAfxiPJHGu0TgTyV4jjEv/fmEwfN3oYNW3M2ubOQ6h3y5j3SrcYUeSLEB\ngAhJoinxCEWC46laX/c2ZWyR2cA2Ley8HFjOE2pzVyYBav2gBhw4Q8mXgLuOVGAS\nw4oXBPfTvdL2uNr0Z4nkFAhqFN5Yk7cUHgxup/6y27q6cC6vAzpqC4D0QvQzD+2/\nyKVz2lKMJ71tyOdfPdcqiU7IELe1JmtgT/QKMtYQhfhB+E1J3hUq/4jeAKhY39c=\n=hFLJ\n-----END PGP SIGNATURE-----\n",
          "payload": "tree c024cc83723ddc26097735c0e44f9ff606b00947\nparent 09a241f59e98c14c085e8f70696610dd1748d0d2\nauthor dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> 1691869042 +0000\ncommitter GitHub <noreply@github.com> 1691869042 +0000\n\nBump actions/checkout from 2.7.0 to 3.5.3\n\nBumps [actions/checkout](https://github.com/actions/checkout) from 2.7.0 to 3.5.3.\n- [Release notes](https://github.com/actions/checkout/releases)\n- [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/actions/checkout/compare/v2.7.0...c85c95e3d7251135ab7dc9ce3241c5835cc595a9)\n\n---\nupdated-dependencies:\n- dependency-name: actions/checkout\n  dependency-type: direct:production\n  update-type: version-update:semver-major\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/4bd06cd325f4b7213708ff520f346c177ba218d9",
      "html_url": "https://github.com/psf/requests/commit/4bd06cd325f4b7213708ff520f346c177ba218d9",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/4bd06cd325f4b7213708ff520f346c177ba218d9/comments",
      "author": {
        "login": "dependabot[bot]",
        "id": 49699333,
        "node_id": "MDM6Qm90NDk2OTkzMzM=",
        "avatar_url": "https://avatars.githubusercontent.com/in/29110?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/dependabot%5Bbot%5D",
        "html_url": "https://github.com/apps/dependabot",
        "followers_url": "https://api.github.com/users/dependabot%5Bbot%5D/followers",
        "following_url": "https://api.github.com/users/dependabot%5Bbot%5D/following{/other_user}",
        "gists_url": "https://api.github.com/users/dependabot%5Bbot%5D/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/dependabot%5Bbot%5D/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/dependabot%5Bbot%5D/subscriptions",
        "organizations_url": "https://api.github.com/users/dependabot%5Bbot%5D/orgs",
        "repos_url": "https://api.github.com/users/dependabot%5Bbot%5D/repos",
        "events_url": "https://api.github.com/users/dependabot%5Bbot%5D/events{/privacy}",
        "received_events_url": "https://api.github.com/users/dependabot%5Bbot%5D/received_events",
        "type": "Bot",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "09a241f59e98c14c085e8f70696610dd1748d0d2",
          "url": "https://api.github.com/repos/psf/requests/commits/09a241f59e98c14c085e8f70696610dd1748d0d2",
          "html_url": "https://github.com/psf/requests/commit/09a241f59e98c14c085e8f70696610dd1748d0d2"
        }
      ]
    },
    {
      "sha": "9ff1a25ef5090a842fef7bb846791217bb2d3e0e",
      "node_id": "C_kwDOABTKOtoAKDlmZjFhMjVlZjUwOTBhODQyZmVmN2JiODQ2NzkxMjE3YmIyZDNlMGU",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2023-08-12T19:50:52Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-08-12T19:50:52Z"
        },
        "message": "Merge pull request #6502 from psf/dependabot/github_actions/github/codeql-action-2.21.3\n\nBump github/codeql-action from 1.1.39 to 2.21.3",
        "tree": {
          "sha": "4e84f51d4f83ea3bef950f26e0abdb2ca25e914b",
          "url": "https://api.github.com/repos/psf/requests/git/trees/4e84f51d4f83ea3bef950f26e0abdb2ca25e914b"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/9ff1a25ef5090a842fef7bb846791217bb2d3e0e",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk1+KcCRBK7hj4Ov3rIwAA284IACG5vvZaY5Vi8WzxQk1clDWK\ngqaQ+pmyUDxH7S2JUMd+9Dn+ckwsSTxqClTasBLWikZpfDfQoUEL7bqlF2D6/kyH\ngBUJfpD8rBaj7xqr0gyWqTdkItIpZnp8QSvq38XhosXeRRH3lDLInP/MuEOefp9c\nquyC8nTvmcEJx46BliKv/WA6UkyzJkLo8xMw0v9w6Q58PMlUlwCvoaePjRH2LKrO\nrL+6/rMkGI7qKBPsL70bIlZJZOQF3Gakn/05AVcCpEGB2roVkqv9WLM+27YAf/iY\nZkOJWjzaLVKkUvSKH/4+ehh1x8Naivbp7eEzVEdBetyRN84aoO1Rz0sj/nMA9n4=\n=UOqp\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 4e84f51d4f83ea3bef950f26e0abdb2ca25e914b\nparent 09a241f59e98c14c085e8f70696610dd1748d0d2\nparent 9acca90bf6bdb29f80b9c82ff66303bd6fb157fa\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1691869852 -0700\ncommitter GitHub <noreply@github.com> 1691869852 -0700\n\nMerge pull request #6502 from psf/dependabot/github_actions/github/codeql-action-2.21.3\n\nBump github/codeql-action from 1.1.39 to 2.21.3",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/9ff1a25ef5090a842fef7bb846791217bb2d3e0e",
      "html_url": "https://github.com/psf/requests/commit/9ff1a25ef5090a842fef7bb846791217bb2d3e0e",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/9ff1a25ef5090a842fef7bb846791217bb2d3e0e/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "09a241f59e98c14c085e8f70696610dd1748d0d2",
          "url": "https://api.github.com/repos/psf/requests/commits/09a241f59e98c14c085e8f70696610dd1748d0d2",
          "html_url": "https://github.com/psf/requests/commit/09a241f59e98c14c085e8f70696610dd1748d0d2"
        },
        {
          "sha": "9acca90bf6bdb29f80b9c82ff66303bd6fb157fa",
          "url": "https://api.github.com/repos/psf/requests/commits/9acca90bf6bdb29f80b9c82ff66303bd6fb157fa",
          "html_url": "https://github.com/psf/requests/commit/9acca90bf6bdb29f80b9c82ff66303bd6fb157fa"
        }
      ]
    },
    {
      "sha": "d8152769ce4792a6bb91cf8794ee75a56824ef17",
      "node_id": "C_kwDOABTKOtoAKGQ4MTUyNzY5Y2U0NzkyYTZiYjkxY2Y4Nzk0ZWU3NWE1NjgyNGVmMTc",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2023-08-12T20:15:39Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-08-12T20:15:39Z"
        },
        "message": "Merge pull request #6501 from psf/dependabot/github_actions/actions/checkout-3.5.3",
        "tree": {
          "sha": "9fff1d932219e7253b154f3dd3883366ddf8ddd8",
          "url": "https://api.github.com/repos/psf/requests/git/trees/9fff1d932219e7253b154f3dd3883366ddf8ddd8"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/d8152769ce4792a6bb91cf8794ee75a56824ef17",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk1+hrCRBK7hj4Ov3rIwAAmKwIAAtK8hvaEC9AFGuwz9uGCyEX\nVr94zmMBj+Lq4yXzGzlMtX0RYg7dfTPniESSX//EN+isa3dzOTgC47WqudjXdqNA\nkuLkY0oFANpx11ihL4FLlTwww/t7DMj4Na9/TowoM5GYFYaWZMyaLTGs6Zn/1NZp\nOcoKcf5/NlsMSJaHZHuLMAwFE42AibFc43kvFx4RAIzz0/qmcCXG39WcEmnjMkUS\neP/0dYcJsPZuect9g5eSHbvw2zuTAPl3q+d587aK9k3smxpF5w9sm8EljJV0/o9a\n0E909iW71KAC/J2tGnJSYEq0Htz9HBpIcvWt/rqqb6wGq6ESfpbZwNMn7UuOywQ=\n=84E7\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 9fff1d932219e7253b154f3dd3883366ddf8ddd8\nparent 9ff1a25ef5090a842fef7bb846791217bb2d3e0e\nparent 4bd06cd325f4b7213708ff520f346c177ba218d9\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1691871339 -0700\ncommitter GitHub <noreply@github.com> 1691871339 -0700\n\nMerge pull request #6501 from psf/dependabot/github_actions/actions/checkout-3.5.3\n\n",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/d8152769ce4792a6bb91cf8794ee75a56824ef17",
      "html_url": "https://github.com/psf/requests/commit/d8152769ce4792a6bb91cf8794ee75a56824ef17",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/d8152769ce4792a6bb91cf8794ee75a56824ef17/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "9ff1a25ef5090a842fef7bb846791217bb2d3e0e",
          "url": "https://api.github.com/repos/psf/requests/commits/9ff1a25ef5090a842fef7bb846791217bb2d3e0e",
          "html_url": "https://github.com/psf/requests/commit/9ff1a25ef5090a842fef7bb846791217bb2d3e0e"
        },
        {
          "sha": "4bd06cd325f4b7213708ff520f346c177ba218d9",
          "url": "https://api.github.com/repos/psf/requests/commits/4bd06cd325f4b7213708ff520f346c177ba218d9",
          "html_url": "https://github.com/psf/requests/commit/4bd06cd325f4b7213708ff520f346c177ba218d9"
        }
      ]
    },
    {
      "sha": "678fca84238e311ffba758d90879d4b870030498",
      "node_id": "C_kwDOABTKOtoAKDY3OGZjYTg0MjM4ZTMxMWZmYmE3NThkOTA4NzlkNGI4NzAwMzA0OTg",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2023-08-13T16:56:53Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-08-13T16:56:53Z"
        },
        "message": "Upgrade to httpbin 0.10.0 (#6496)",
        "tree": {
          "sha": "32ef4b314fc9a158870f23108c2983e730ba43ff",
          "url": "https://api.github.com/repos/psf/requests/git/trees/32ef4b314fc9a158870f23108c2983e730ba43ff"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/678fca84238e311ffba758d90879d4b870030498",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk2QtVCRBK7hj4Ov3rIwAALhwIADVAQFiPD/DBKoWaaFlUxUED\nO4JghJGHgykSQvGj4/rdu4A1zSzkEY8nTHp+AL8TKL+1vvuikV8wzjkkA6K1ifmy\nG1QvNNGZBbvwLa6rmtj0zaIVfiWPFGFmgvCws0bWV+l9AL9x0/669o7MWznq1fsu\nb+52iL1zI0ALsSytm4xq2zIr1Q6eS1D0AZk+ccYdMVgN6bFO9LvfCVLZiASm7Lz+\nNkS5fQ0NCRpFscMdtJojYgOX9bLNfNuDHosMeDEHkYcLC2WbQ7ewpxlIyzjqm+Jk\nQKzz1ouIOhjCM08IgloL1k7rtjvOED6l5rD7OmIMYtrjniwSV5MpsfjVi3iTULg=\n=jyYO\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 32ef4b314fc9a158870f23108c2983e730ba43ff\nparent d8152769ce4792a6bb91cf8794ee75a56824ef17\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1691945813 -0700\ncommitter GitHub <noreply@github.com> 1691945813 -0700\n\nUpgrade to httpbin 0.10.0 (#6496)\n\n",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/678fca84238e311ffba758d90879d4b870030498",
      "html_url": "https://github.com/psf/requests/commit/678fca84238e311ffba758d90879d4b870030498",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/678fca84238e311ffba758d90879d4b870030498/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "d8152769ce4792a6bb91cf8794ee75a56824ef17",
          "url": "https://api.github.com/repos/psf/requests/commits/d8152769ce4792a6bb91cf8794ee75a56824ef17",
          "html_url": "https://github.com/psf/requests/commit/d8152769ce4792a6bb91cf8794ee75a56824ef17"
        }
      ]
    },
    {
      "sha": "e9fa2e2da3076e4f55f18b3f4a169c7b3916b272",
      "node_id": "C_kwDOABTKOtoAKGU5ZmEyZTJkYTMwNzZlNGY1NWYxOGIzZjRhMTY5YzdiMzkxNmIyNzI",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2023-08-13T19:56:18Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-08-13T19:56:18Z"
        },
        "message": "Add 3.12 classifier and tox configuration (#6503)",
        "tree": {
          "sha": "a4394914ebcd5a2c25e3b3eb8b54a05dbfa7b021",
          "url": "https://api.github.com/repos/psf/requests/git/trees/a4394914ebcd5a2c25e3b3eb8b54a05dbfa7b021"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/e9fa2e2da3076e4f55f18b3f4a169c7b3916b272",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk2TViCRBK7hj4Ov3rIwAAZLsIADtR76v/x6y6IcJb4J3zrn9j\nffDG6bt881/4djhDWB+Q0KZpvF3AYYWMHCrwU4/iIeZ7OHiCwf33i6gryOZIj21W\neovLkI13sccTGEldWwEe4AMgH6Io+N/2Fxk+TyDzlMphuSUOV8Uu7HLwd9jr1OgT\nZftqkP5b4N2kcDX2QIveVmptWQo9+c87c6XnvJgJ28N1V93usvgwGoijLMGArK+H\n0Dv1oY9zFSbikh90YQKr+/Cd9Arie6iMBnGHvKuPt05NQZBjZe72iH5oIoZoo+sM\nX51RXh+a+YyWuuOtLRe2v/JZ2HrL+MmeoM87z1yd7T4PPcK9AzawhW3hP1e6oNw=\n=hOU0\n-----END PGP SIGNATURE-----\n",
          "payload": "tree a4394914ebcd5a2c25e3b3eb8b54a05dbfa7b021\nparent 678fca84238e311ffba758d90879d4b870030498\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1691956578 -0700\ncommitter GitHub <noreply@github.com> 1691956578 -0700\n\nAdd 3.12 classifier and tox configuration (#6503)\n\n",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/e9fa2e2da3076e4f55f18b3f4a169c7b3916b272",
      "html_url": "https://github.com/psf/requests/commit/e9fa2e2da3076e4f55f18b3f4a169c7b3916b272",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/e9fa2e2da3076e4f55f18b3f4a169c7b3916b272/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "678fca84238e311ffba758d90879d4b870030498",
          "url": "https://api.github.com/repos/psf/requests/commits/678fca84238e311ffba758d90879d4b870030498",
          "html_url": "https://github.com/psf/requests/commit/678fca84238e311ffba758d90879d4b870030498"
        }
      ]
    },
    {
      "sha": "d63e94f552ebf77ccf45d97e5863ac46500fa2c7",
      "node_id": "C_kwDOABTKOtoAKGQ2M2U5NGY1NTJlYmY3N2NjZjQ1ZDk3ZTU4NjNhYzQ2NTAwZmEyYzc",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2023-08-13T21:46:13Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-08-13T21:46:13Z"
        },
        "message": "Move to src directory (#6506)",
        "tree": {
          "sha": "46586e72c920ad99e6c4f388ccfee630e8047c79",
          "url": "https://api.github.com/repos/psf/requests/git/trees/46586e72c920ad99e6c4f388ccfee630e8047c79"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/d63e94f552ebf77ccf45d97e5863ac46500fa2c7",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk2U8lCRBK7hj4Ov3rIwAAj/oIAAzp6BNrYqwH0CPkV0maoxPJ\nZ7QnUiB65ID/uWwDJmPYgQYtElwsESBkop47FQET2etAlbzcWhwmigiQGOtNi2fD\n0kDMqqwk28YKiWcH43QnAvMXsR5Y9s3fTT+FzQPPrLBEV4AEag/cvF62gYBPIv3r\nG0Dnklqk+Jn9j7msfF/V0OCqbllCp9QUl7x3Nlx0q7ejwHGrD2RtojfAfElq9Eif\nrkA4t9jMPAt0ehv9SRZ8RqWGqn/QzJnL5S80N46L6m3cXnxXmnBZtY3v7vey6B9C\n1QvyfUNjSkrQK6KTbhyg6PcxJsn4c8bWeOgUQwOwnP1vTU7zhmXUO4RQBLuEWOE=\n=Ar7a\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 46586e72c920ad99e6c4f388ccfee630e8047c79\nparent e9fa2e2da3076e4f55f18b3f4a169c7b3916b272\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1691963173 -0700\ncommitter GitHub <noreply@github.com> 1691963173 -0700\n\nMove to src directory (#6506)\n\n",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/d63e94f552ebf77ccf45d97e5863ac46500fa2c7",
      "html_url": "https://github.com/psf/requests/commit/d63e94f552ebf77ccf45d97e5863ac46500fa2c7",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/d63e94f552ebf77ccf45d97e5863ac46500fa2c7/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "e9fa2e2da3076e4f55f18b3f4a169c7b3916b272",
          "url": "https://api.github.com/repos/psf/requests/commits/e9fa2e2da3076e4f55f18b3f4a169c7b3916b272",
          "html_url": "https://github.com/psf/requests/commit/e9fa2e2da3076e4f55f18b3f4a169c7b3916b272"
        }
      ]
    },
    {
      "sha": "005571d1180835eb5266a3fdbdbe8fdae57d90c2",
      "node_id": "C_kwDOABTKOtoAKDAwNTU3MWQxMTgwODM1ZWI1MjY2YTNmZGJkYmU4ZmRhZTU3ZDkwYzI",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2023-08-13T23:08:21Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-08-13T23:08:21Z"
        },
        "message": "Remove pytest-mock requirement (#6505)",
        "tree": {
          "sha": "6b5c3dcaf4e5190eb8f8c2ab3252521e921365ef",
          "url": "https://api.github.com/repos/psf/requests/git/trees/6b5c3dcaf4e5190eb8f8c2ab3252521e921365ef"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/005571d1180835eb5266a3fdbdbe8fdae57d90c2",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk2WJlCRBK7hj4Ov3rIwAAT/8IAAI6X429MijdRCv9pvJN0Yzg\n7qOm3UoSwkkv+2PQsWp/4NbayxWgSWc+GvtdUZp5U9psyVddIjLk3pWTujxmiCf0\nLfInYQsiyLcWGQJiSHYJtBdp4fSVtSC2DbeS5NA1RcZN1VXOsiauM4OlM6RBD1Ui\nZqAE7yfSIF1SSK46rNmcZWxCBxSElFbeArofaclXSJV8KVsERNjg+Pc17PKw/x/k\n+CoBioA9yKQ7jWstcSUw6LJKoGWurd6qbXH0kX99gQH09NjGrMAtAXL614PohNl7\nhf73sE8WqYgVGIXs6wNM90HDyo1WXoU63S7aeFxe70q5yi1A9q2BH9ViwosQCF0=\n=4MCu\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 6b5c3dcaf4e5190eb8f8c2ab3252521e921365ef\nparent d63e94f552ebf77ccf45d97e5863ac46500fa2c7\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1691968101 -0700\ncommitter GitHub <noreply@github.com> 1691968101 -0700\n\nRemove pytest-mock requirement (#6505)\n\n",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/005571d1180835eb5266a3fdbdbe8fdae57d90c2",
      "html_url": "https://github.com/psf/requests/commit/005571d1180835eb5266a3fdbdbe8fdae57d90c2",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/005571d1180835eb5266a3fdbdbe8fdae57d90c2/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "d63e94f552ebf77ccf45d97e5863ac46500fa2c7",
          "url": "https://api.github.com/repos/psf/requests/commits/d63e94f552ebf77ccf45d97e5863ac46500fa2c7",
          "html_url": "https://github.com/psf/requests/commit/d63e94f552ebf77ccf45d97e5863ac46500fa2c7"
        }
      ]
    },
    {
      "sha": "89f0eb91b396619db6695b64e368950e36bdbe7f",
      "node_id": "C_kwDOABTKOtoAKDg5ZjBlYjkxYjM5NjYxOWRiNjY5NWI2NGUzNjg5NTBlMzZiZGJlN2Y",
      "commit": {
        "author": {
          "name": "Jonas Schell",
          "email": "jonas@livekit.io",
          "date": "2023-08-16T15:16:53Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-08-16T15:16:53Z"
        },
        "message": "fix monthly download badge (#6507)",
        "tree": {
          "sha": "90baa6381e1c0bad921b8496d78955435c2ccc1b",
          "url": "https://api.github.com/repos/psf/requests/git/trees/90baa6381e1c0bad921b8496d78955435c2ccc1b"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/89f0eb91b396619db6695b64e368950e36bdbe7f",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk3OhlCRBK7hj4Ov3rIwAAteIIAEXICpLU/X9OBpzEZpxTLnfn\n+4keTH/gprtq7hWdtB7dNpiWBA138JEt6LcH7QGl0gJkz0gHP7swECh3JuEttGMf\nr4ouq0Ttx9DT+wFnEhyXr55YFb/rE4eyVrvhPK41JdfW++LuTBUbjbGqPfcgbCBM\nmx3QVOTvQSZIwMSLaGL2onpjYYE6JXOrtpAZihVa3DBLCA1rDZAcpIXGscDFyPGX\n27x9oCdaHNvvLySSgpZqpzN8acOiIl6FWOsfBz9gCFrhJNo5IFmUfWVKlylY3uRZ\nP9q+ES5q2zAxFMGlcZAp0EHtnhSmFmUK5FeHF0yzXjp4UWuy+EkIsROIiA8qhlA=\n=qO1V\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 90baa6381e1c0bad921b8496d78955435c2ccc1b\nparent 005571d1180835eb5266a3fdbdbe8fdae57d90c2\nauthor Jonas Schell <jonas@livekit.io> 1692199013 +0200\ncommitter GitHub <noreply@github.com> 1692199013 -0700\n\nfix monthly download badge (#6507)\n\n",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/89f0eb91b396619db6695b64e368950e36bdbe7f",
      "html_url": "https://github.com/psf/requests/commit/89f0eb91b396619db6695b64e368950e36bdbe7f",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/89f0eb91b396619db6695b64e368950e36bdbe7f/comments",
      "author": {
        "login": "ocupe",
        "id": 11357413,
        "node_id": "MDQ6VXNlcjExMzU3NDEz",
        "avatar_url": "https://avatars.githubusercontent.com/u/11357413?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/ocupe",
        "html_url": "https://github.com/ocupe",
        "followers_url": "https://api.github.com/users/ocupe/followers",
        "following_url": "https://api.github.com/users/ocupe/following{/other_user}",
        "gists_url": "https://api.github.com/users/ocupe/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/ocupe/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/ocupe/subscriptions",
        "organizations_url": "https://api.github.com/users/ocupe/orgs",
        "repos_url": "https://api.github.com/users/ocupe/repos",
        "events_url": "https://api.github.com/users/ocupe/events{/privacy}",
        "received_events_url": "https://api.github.com/users/ocupe/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "005571d1180835eb5266a3fdbdbe8fdae57d90c2",
          "url": "https://api.github.com/repos/psf/requests/commits/005571d1180835eb5266a3fdbdbe8fdae57d90c2",
          "html_url": "https://github.com/psf/requests/commit/005571d1180835eb5266a3fdbdbe8fdae57d90c2"
        }
      ]
    },
    {
      "sha": "2ee5b0b01c9e7c14217a536886b337d6f08b9aac",
      "node_id": "C_kwDOABTKOtoAKDJlZTViMGIwMWM5ZTdjMTQyMTdhNTM2ODg2YjMzN2Q2ZjA4YjlhYWM",
      "commit": {
        "author": {
          "name": "13steinj",
          "email": "13steinj@users.noreply.github.com",
          "date": "2023-08-18T17:01:26Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-08-18T17:01:26Z"
        },
        "message": "Fix documentation monthly download badge (#6508)",
        "tree": {
          "sha": "0535e227bbcf53c37a4c96c172fe2d01bae75ed3",
          "url": "https://api.github.com/repos/psf/requests/git/trees/0535e227bbcf53c37a4c96c172fe2d01bae75ed3"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/2ee5b0b01c9e7c14217a536886b337d6f08b9aac",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk36PmCRBK7hj4Ov3rIwAAoW0IAJICqunDoF1hY6NDDIvuejTO\n2Zdbp+CiDnV8JxPcPh+3oP4dk2Gpf2oufwGdp3rHYWkrb8A1y7hLBfvcGKZRT79X\nkQShczM/aRtUnrC94+RR5X6AVMXWrOJOz06ccv+tStqiuFhhgIGWczu4JwtrstQv\noJc9o0jZXe/XvIuQeKscWzebL1xtN8lSZ5/b/GoAp9Jza2E9VlORKsUtmGrx0dmS\nUMg3IQnlpy2L4OZhm14K+5rZ9XDeIE/Mbaso3GE5rG/q24jEnr4WzBGrMMLE4HLV\nYYrEEcWIfMLfX2cves8UTSkG+BLPZdOtyHXE7SRDUZrlDHFCaFqUrWhFPYnpd40=\n=43zK\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 0535e227bbcf53c37a4c96c172fe2d01bae75ed3\nparent 89f0eb91b396619db6695b64e368950e36bdbe7f\nauthor 13steinj <13steinj@users.noreply.github.com> 1692378086 -0500\ncommitter GitHub <noreply@github.com> 1692378086 -0600\n\nFix documentation monthly download badge (#6508)\n\n",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/2ee5b0b01c9e7c14217a536886b337d6f08b9aac",
      "html_url": "https://github.com/psf/requests/commit/2ee5b0b01c9e7c14217a536886b337d6f08b9aac",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/2ee5b0b01c9e7c14217a536886b337d6f08b9aac/comments",
      "author": {
        "login": "13steinj",
        "id": 10525230,
        "node_id": "MDQ6VXNlcjEwNTI1MjMw",
        "avatar_url": "https://avatars.githubusercontent.com/u/10525230?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/13steinj",
        "html_url": "https://github.com/13steinj",
        "followers_url": "https://api.github.com/users/13steinj/followers",
        "following_url": "https://api.github.com/users/13steinj/following{/other_user}",
        "gists_url": "https://api.github.com/users/13steinj/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/13steinj/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/13steinj/subscriptions",
        "organizations_url": "https://api.github.com/users/13steinj/orgs",
        "repos_url": "https://api.github.com/users/13steinj/repos",
        "events_url": "https://api.github.com/users/13steinj/events{/privacy}",
        "received_events_url": "https://api.github.com/users/13steinj/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "89f0eb91b396619db6695b64e368950e36bdbe7f",
          "url": "https://api.github.com/repos/psf/requests/commits/89f0eb91b396619db6695b64e368950e36bdbe7f",
          "html_url": "https://github.com/psf/requests/commit/89f0eb91b396619db6695b64e368950e36bdbe7f"
        }
      ]
    },
    {
      "sha": "bea231b033d643a6c4152a5b12c3e0b2524ed48f",
      "node_id": "C_kwDOABTKOtoAKGJlYTIzMWIwMzNkNjQzYTZjNDE1MmE1YjEyYzNlMGIyNTI0ZWQ0OGY",
      "commit": {
        "author": {
          "name": "dependabot[bot]",
          "email": "49699333+dependabot[bot]@users.noreply.github.com",
          "date": "2023-08-28T16:12:37Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-08-28T16:12:37Z"
        },
        "message": "Bump actions/checkout from 3.5.3 to 3.6.0\n\nBumps [actions/checkout](https://github.com/actions/checkout) from 3.5.3 to 3.6.0.\n- [Release notes](https://github.com/actions/checkout/releases)\n- [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/actions/checkout/compare/c85c95e3d7251135ab7dc9ce3241c5835cc595a9...f43a0e5ff2bd294095638e18286ca9a3d1956744)\n\n---\nupdated-dependencies:\n- dependency-name: actions/checkout\n  dependency-type: direct:production\n  update-type: version-update:semver-minor\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
        "tree": {
          "sha": "a1c2a924acabd715c395d2beebc857716a4fe55a",
          "url": "https://api.github.com/repos/psf/requests/git/trees/a1c2a924acabd715c395d2beebc857716a4fe55a"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/bea231b033d643a6c4152a5b12c3e0b2524ed48f",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk7Md1CRBK7hj4Ov3rIwAAvf0IAHBo3MAFko8W+paAGAQBEQkP\nJU/emHHlXRYSd6VzRAnxneccZJCuXzASShHQ1er6+ghs2GD/4vswRIphdg8KiwKF\nV2Xj9xw+Zpvifxoa1wmPMwaHOVlT1FZI3bkuJWtj0d/pCeVzWcUmbL6/obr4RPP/\ngkYd/ZvZI4wvK2MI/ANiy9MmWtYFsxVac+dQVptjgpgEC0vE9vml8wMBtx6WBT5K\npEZ9YFGJLULbae/VWFCkJiLQo+qlkFmyZ5r57sYf30qki+Y4zoa0kyMdU2lxOtLs\npJEOvSg7ALOHcoXW9W4JAlQS1zvpcJ/5Lx7qPbanD+ELapLjZru07Oc8jE11b+I=\n=2OSU\n-----END PGP SIGNATURE-----\n",
          "payload": "tree a1c2a924acabd715c395d2beebc857716a4fe55a\nparent 2ee5b0b01c9e7c14217a536886b337d6f08b9aac\nauthor dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> 1693239157 +0000\ncommitter GitHub <noreply@github.com> 1693239157 +0000\n\nBump actions/checkout from 3.5.3 to 3.6.0\n\nBumps [actions/checkout](https://github.com/actions/checkout) from 3.5.3 to 3.6.0.\n- [Release notes](https://github.com/actions/checkout/releases)\n- [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/actions/checkout/compare/c85c95e3d7251135ab7dc9ce3241c5835cc595a9...f43a0e5ff2bd294095638e18286ca9a3d1956744)\n\n---\nupdated-dependencies:\n- dependency-name: actions/checkout\n  dependency-type: direct:production\n  update-type: version-update:semver-minor\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/bea231b033d643a6c4152a5b12c3e0b2524ed48f",
      "html_url": "https://github.com/psf/requests/commit/bea231b033d643a6c4152a5b12c3e0b2524ed48f",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/bea231b033d643a6c4152a5b12c3e0b2524ed48f/comments",
      "author": {
        "login": "dependabot[bot]",
        "id": 49699333,
        "node_id": "MDM6Qm90NDk2OTkzMzM=",
        "avatar_url": "https://avatars.githubusercontent.com/in/29110?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/dependabot%5Bbot%5D",
        "html_url": "https://github.com/apps/dependabot",
        "followers_url": "https://api.github.com/users/dependabot%5Bbot%5D/followers",
        "following_url": "https://api.github.com/users/dependabot%5Bbot%5D/following{/other_user}",
        "gists_url": "https://api.github.com/users/dependabot%5Bbot%5D/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/dependabot%5Bbot%5D/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/dependabot%5Bbot%5D/subscriptions",
        "organizations_url": "https://api.github.com/users/dependabot%5Bbot%5D/orgs",
        "repos_url": "https://api.github.com/users/dependabot%5Bbot%5D/repos",
        "events_url": "https://api.github.com/users/dependabot%5Bbot%5D/events{/privacy}",
        "received_events_url": "https://api.github.com/users/dependabot%5Bbot%5D/received_events",
        "type": "Bot",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "2ee5b0b01c9e7c14217a536886b337d6f08b9aac",
          "url": "https://api.github.com/repos/psf/requests/commits/2ee5b0b01c9e7c14217a536886b337d6f08b9aac",
          "html_url": "https://github.com/psf/requests/commit/2ee5b0b01c9e7c14217a536886b337d6f08b9aac"
        }
      ]
    },
    {
      "sha": "16dc70df34cef5213f53835cd1f53c48922d6295",
      "node_id": "C_kwDOABTKOtoAKDE2ZGM3MGRmMzRjZWY1MjEzZjUzODM1Y2QxZjUzYzQ4OTIyZDYyOTU",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2023-08-28T19:05:56Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-08-28T19:05:56Z"
        },
        "message": "Merge pull request #6516 from psf/dependabot/github_actions/actions/checkout-3.6.0\n\nBump actions/checkout from 3.5.3 to 3.6.0",
        "tree": {
          "sha": "a1c2a924acabd715c395d2beebc857716a4fe55a",
          "url": "https://api.github.com/repos/psf/requests/git/trees/a1c2a924acabd715c395d2beebc857716a4fe55a"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/16dc70df34cef5213f53835cd1f53c48922d6295",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk7PAUCRBK7hj4Ov3rIwAAXfYIAK9FMqe70JHwUVJ7Xa1NRB0z\nDmYYDjtnPdnjSWaC4K2o/CMYYv8OFzaRUyZIat9HPDjd0b+qvXYfwZeqP7KAtTa1\nWdyN9XY1m4XpEEvIB4YzAmoP5DzbLbPjx6xfQJblYe3FhcHRDfybQr74jRlKD2cy\nk625as5kBkSk9msNyBMv5UwdJQrEg3CSPztXF+hZpTgVUBeoi/qcFKFDZM97vXW0\nbE30R1EAXiwvRqJfwGLoB5TfUE0uKlkz8m9c3Xnpc594GMRHzNGfQU6PCZryV5tu\nQAYLAgkWpOzfk5teZ8W4voG1Z1tDH/DXZHQSWFVnQrfZdUL7zfuWKxHPhgGPEz4=\n=zwyz\n-----END PGP SIGNATURE-----\n",
          "payload": "tree a1c2a924acabd715c395d2beebc857716a4fe55a\nparent 2ee5b0b01c9e7c14217a536886b337d6f08b9aac\nparent bea231b033d643a6c4152a5b12c3e0b2524ed48f\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1693249556 -0500\ncommitter GitHub <noreply@github.com> 1693249556 -0500\n\nMerge pull request #6516 from psf/dependabot/github_actions/actions/checkout-3.6.0\n\nBump actions/checkout from 3.5.3 to 3.6.0",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/16dc70df34cef5213f53835cd1f53c48922d6295",
      "html_url": "https://github.com/psf/requests/commit/16dc70df34cef5213f53835cd1f53c48922d6295",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/16dc70df34cef5213f53835cd1f53c48922d6295/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "2ee5b0b01c9e7c14217a536886b337d6f08b9aac",
          "url": "https://api.github.com/repos/psf/requests/commits/2ee5b0b01c9e7c14217a536886b337d6f08b9aac",
          "html_url": "https://github.com/psf/requests/commit/2ee5b0b01c9e7c14217a536886b337d6f08b9aac"
        },
        {
          "sha": "bea231b033d643a6c4152a5b12c3e0b2524ed48f",
          "url": "https://api.github.com/repos/psf/requests/commits/bea231b033d643a6c4152a5b12c3e0b2524ed48f",
          "html_url": "https://github.com/psf/requests/commit/bea231b033d643a6c4152a5b12c3e0b2524ed48f"
        }
      ]
    },
    {
      "sha": "4585a7fbdaaebf19d213eb16326afae2e9382abe",
      "node_id": "C_kwDOABTKOtoAKDQ1ODVhN2ZiZGFhZWJmMTlkMjEzZWIxNjMyNmFmYWUyZTkzODJhYmU",
      "commit": {
        "author": {
          "name": "Johnny.H",
          "email": "jnhyperion@gmail.com",
          "date": "2023-08-29T05:41:49Z"
        },
        "committer": {
          "name": "Johnny.H",
          "email": "jnhyperion@gmail.com",
          "date": "2023-08-29T05:41:49Z"
        },
        "message": "remove pytest.ini since it does not exist anymore",
        "tree": {
          "sha": "7e844c1b6f06941285a91bd488700a90ce142216",
          "url": "https://api.github.com/repos/psf/requests/git/trees/7e844c1b6f06941285a91bd488700a90ce142216"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/4585a7fbdaaebf19d213eb16326afae2e9382abe",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/4585a7fbdaaebf19d213eb16326afae2e9382abe",
      "html_url": "https://github.com/psf/requests/commit/4585a7fbdaaebf19d213eb16326afae2e9382abe",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/4585a7fbdaaebf19d213eb16326afae2e9382abe/comments",
      "author": {
        "login": "jnhyperion",
        "id": 20297196,
        "node_id": "MDQ6VXNlcjIwMjk3MTk2",
        "avatar_url": "https://avatars.githubusercontent.com/u/20297196?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/jnhyperion",
        "html_url": "https://github.com/jnhyperion",
        "followers_url": "https://api.github.com/users/jnhyperion/followers",
        "following_url": "https://api.github.com/users/jnhyperion/following{/other_user}",
        "gists_url": "https://api.github.com/users/jnhyperion/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/jnhyperion/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/jnhyperion/subscriptions",
        "organizations_url": "https://api.github.com/users/jnhyperion/orgs",
        "repos_url": "https://api.github.com/users/jnhyperion/repos",
        "events_url": "https://api.github.com/users/jnhyperion/events{/privacy}",
        "received_events_url": "https://api.github.com/users/jnhyperion/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "jnhyperion",
        "id": 20297196,
        "node_id": "MDQ6VXNlcjIwMjk3MTk2",
        "avatar_url": "https://avatars.githubusercontent.com/u/20297196?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/jnhyperion",
        "html_url": "https://github.com/jnhyperion",
        "followers_url": "https://api.github.com/users/jnhyperion/followers",
        "following_url": "https://api.github.com/users/jnhyperion/following{/other_user}",
        "gists_url": "https://api.github.com/users/jnhyperion/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/jnhyperion/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/jnhyperion/subscriptions",
        "organizations_url": "https://api.github.com/users/jnhyperion/orgs",
        "repos_url": "https://api.github.com/users/jnhyperion/repos",
        "events_url": "https://api.github.com/users/jnhyperion/events{/privacy}",
        "received_events_url": "https://api.github.com/users/jnhyperion/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "16dc70df34cef5213f53835cd1f53c48922d6295",
          "url": "https://api.github.com/repos/psf/requests/commits/16dc70df34cef5213f53835cd1f53c48922d6295",
          "html_url": "https://github.com/psf/requests/commit/16dc70df34cef5213f53835cd1f53c48922d6295"
        }
      ]
    },
    {
      "sha": "8b560ecb24ee4fa4e839272dcf2653a4fa525a34",
      "node_id": "C_kwDOABTKOtoAKDhiNTYwZWNiMjRlZTRmYTRlODM5MjcyZGNmMjY1M2E0ZmE1MjVhMzQ",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2023-08-29T14:27:10Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-08-29T14:27:10Z"
        },
        "message": "Merge pull request #6517 from jnhyperion/remove-pytest-ini\n\nRemove pytest.ini in MANIFEST.in since it does not exist anymore",
        "tree": {
          "sha": "7e844c1b6f06941285a91bd488700a90ce142216",
          "url": "https://api.github.com/repos/psf/requests/git/trees/7e844c1b6f06941285a91bd488700a90ce142216"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/8b560ecb24ee4fa4e839272dcf2653a4fa525a34",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk7gA+CRBK7hj4Ov3rIwAAMGQIADTS4JmXWqZQ/a1IqR4dDtG1\n5S1gd3ADthaGyMgrobGP1AUeRudC9Ub2yKx932+abPK/UaBK8VqhRPbzfD4IsaX5\nxIEnBbcYdTHM57yQh5KVimITWnFXxQMHt88Avp7rc+k9Zeh3+tem1L0suTykC0iz\nEMbriZqwhfb+Tq4odOEy4ksg7/f4MwhdN23LMihxPNy8/4nAL02hr0JqyYToeYH6\nGKwLaN94rlo0zdTfIj3mzOJz4JGqdc96A3AREvkbwI2BSaNqfP6P5O+6529A6txR\n8IL+lOrbPYGVH4Obz4IepVEKp5mSd8GRarWbM1spGXgElbnkrJ2bGZH4TU48Uwk=\n=pyB/\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 7e844c1b6f06941285a91bd488700a90ce142216\nparent 16dc70df34cef5213f53835cd1f53c48922d6295\nparent 4585a7fbdaaebf19d213eb16326afae2e9382abe\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1693319230 -0500\ncommitter GitHub <noreply@github.com> 1693319230 -0500\n\nMerge pull request #6517 from jnhyperion/remove-pytest-ini\n\nRemove pytest.ini in MANIFEST.in since it does not exist anymore",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/8b560ecb24ee4fa4e839272dcf2653a4fa525a34",
      "html_url": "https://github.com/psf/requests/commit/8b560ecb24ee4fa4e839272dcf2653a4fa525a34",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/8b560ecb24ee4fa4e839272dcf2653a4fa525a34/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "16dc70df34cef5213f53835cd1f53c48922d6295",
          "url": "https://api.github.com/repos/psf/requests/commits/16dc70df34cef5213f53835cd1f53c48922d6295",
          "html_url": "https://github.com/psf/requests/commit/16dc70df34cef5213f53835cd1f53c48922d6295"
        },
        {
          "sha": "4585a7fbdaaebf19d213eb16326afae2e9382abe",
          "url": "https://api.github.com/repos/psf/requests/commits/4585a7fbdaaebf19d213eb16326afae2e9382abe",
          "html_url": "https://github.com/psf/requests/commit/4585a7fbdaaebf19d213eb16326afae2e9382abe"
        }
      ]
    },
    {
      "sha": "29fc8d1e9346a29b91513547d626e23f4c36e557",
      "node_id": "C_kwDOABTKOtoAKDI5ZmM4ZDFlOTM0NmEyOWI5MTUxMzU0N2Q2MjZlMjNmNGMzNmU1NTc",
      "commit": {
        "author": {
          "name": "dependabot[bot]",
          "email": "49699333+dependabot[bot]@users.noreply.github.com",
          "date": "2023-09-04T16:21:27Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-09-04T16:21:27Z"
        },
        "message": "Bump actions/checkout from 3.6.0 to 4.0.0\n\nBumps [actions/checkout](https://github.com/actions/checkout) from 3.6.0 to 4.0.0.\n- [Release notes](https://github.com/actions/checkout/releases)\n- [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/actions/checkout/compare/f43a0e5ff2bd294095638e18286ca9a3d1956744...3df4ab11eba7bda6032a0b82a6bb43b11571feac)\n\n---\nupdated-dependencies:\n- dependency-name: actions/checkout\n  dependency-type: direct:production\n  update-type: version-update:semver-major\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
        "tree": {
          "sha": "75857592e1130f588c7757700167668218958185",
          "url": "https://api.github.com/repos/psf/requests/git/trees/75857592e1130f588c7757700167668218958185"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/29fc8d1e9346a29b91513547d626e23f4c36e557",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk9gQHCRBK7hj4Ov3rIwAADJsIAFEpq7720k75D4i7A/x14roc\nWWc4XwzeYRBWccCyxwl4+gBqnmxNA/miZapBxmJMLvprHC6uI11Muc221KD5fMQf\nTAfR6n38ru0Fe68lHz8Z3eC1azvXBFoZbvE0nOazYfi5rY7C4gMGqUW++c8geAub\n1McFhusL+vwZtuJVrbNqTOuMGAA6+V13gjvD9fxSkrCjhZa8+EoG69SOpkcUHa/L\nR7pTcqxSJj/szpkknvZbFw7So98VSTc3adu5ctAOvL8AnQVhiIT0kIR3Wuyszp81\nRgY8P48FP6VWK1iviRakst12HYFXMIRG+JRMpLXm6/vmH9gZH8XOFMBkt4dfHsI=\n=aP7l\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 75857592e1130f588c7757700167668218958185\nparent 8b560ecb24ee4fa4e839272dcf2653a4fa525a34\nauthor dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> 1693844487 +0000\ncommitter GitHub <noreply@github.com> 1693844487 +0000\n\nBump actions/checkout from 3.6.0 to 4.0.0\n\nBumps [actions/checkout](https://github.com/actions/checkout) from 3.6.0 to 4.0.0.\n- [Release notes](https://github.com/actions/checkout/releases)\n- [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/actions/checkout/compare/f43a0e5ff2bd294095638e18286ca9a3d1956744...3df4ab11eba7bda6032a0b82a6bb43b11571feac)\n\n---\nupdated-dependencies:\n- dependency-name: actions/checkout\n  dependency-type: direct:production\n  update-type: version-update:semver-major\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/29fc8d1e9346a29b91513547d626e23f4c36e557",
      "html_url": "https://github.com/psf/requests/commit/29fc8d1e9346a29b91513547d626e23f4c36e557",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/29fc8d1e9346a29b91513547d626e23f4c36e557/comments",
      "author": {
        "login": "dependabot[bot]",
        "id": 49699333,
        "node_id": "MDM6Qm90NDk2OTkzMzM=",
        "avatar_url": "https://avatars.githubusercontent.com/in/29110?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/dependabot%5Bbot%5D",
        "html_url": "https://github.com/apps/dependabot",
        "followers_url": "https://api.github.com/users/dependabot%5Bbot%5D/followers",
        "following_url": "https://api.github.com/users/dependabot%5Bbot%5D/following{/other_user}",
        "gists_url": "https://api.github.com/users/dependabot%5Bbot%5D/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/dependabot%5Bbot%5D/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/dependabot%5Bbot%5D/subscriptions",
        "organizations_url": "https://api.github.com/users/dependabot%5Bbot%5D/orgs",
        "repos_url": "https://api.github.com/users/dependabot%5Bbot%5D/repos",
        "events_url": "https://api.github.com/users/dependabot%5Bbot%5D/events{/privacy}",
        "received_events_url": "https://api.github.com/users/dependabot%5Bbot%5D/received_events",
        "type": "Bot",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "8b560ecb24ee4fa4e839272dcf2653a4fa525a34",
          "url": "https://api.github.com/repos/psf/requests/commits/8b560ecb24ee4fa4e839272dcf2653a4fa525a34",
          "html_url": "https://github.com/psf/requests/commit/8b560ecb24ee4fa4e839272dcf2653a4fa525a34"
        }
      ]
    },
    {
      "sha": "881281250f74549f560408e5546d95a8cd73ce28",
      "node_id": "C_kwDOABTKOtoAKDg4MTI4MTI1MGY3NDU0OWY1NjA0MDhlNTU0NmQ5NWE4Y2Q3M2NlMjg",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2023-09-05T00:17:08Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-09-05T00:17:08Z"
        },
        "message": "Merge pull request #6519 from psf/dependabot/github_actions/actions/checkout-4.0.0\n\nBump actions/checkout from 3.6.0 to 4.0.0",
        "tree": {
          "sha": "75857592e1130f588c7757700167668218958185",
          "url": "https://api.github.com/repos/psf/requests/git/trees/75857592e1130f588c7757700167668218958185"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/881281250f74549f560408e5546d95a8cd73ce28",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJk9nOECRBK7hj4Ov3rIwAAg9wIAEigMGLSOfPLPrDNAtwIvs8H\nVczFPrM2eaJGI7gWHUYJ1MXoeJsQ1Vta6f0iwX0g342hGF6rNuGaJRMyShZdRTBe\nMGS3hwUCfaFeVkBsenevh9UcQQoEBFxAJ19f2pXXX4VsT4TFarJr6U37gxygurgb\nlNpR3jtXUWN9Jqzoc9nxqrjbtiqcNxIgCMKrArVWNxj2ZDKzR87hjtPQm5dI9mjK\nj2lbKiqprjEhi31XaCpfMVd+UeVAFrIL4P/I7qtkMfbd13JDRZzvEYgr1HVfJ5CL\nukSupJR7HBfOBXG3SkkZytxwICTeCE2dFbCf+fSGoAbLU6tKo9f9W8hsklLnnmE=\n=1oC6\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 75857592e1130f588c7757700167668218958185\nparent 8b560ecb24ee4fa4e839272dcf2653a4fa525a34\nparent 29fc8d1e9346a29b91513547d626e23f4c36e557\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1693873028 -0500\ncommitter GitHub <noreply@github.com> 1693873028 -0500\n\nMerge pull request #6519 from psf/dependabot/github_actions/actions/checkout-4.0.0\n\nBump actions/checkout from 3.6.0 to 4.0.0",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/881281250f74549f560408e5546d95a8cd73ce28",
      "html_url": "https://github.com/psf/requests/commit/881281250f74549f560408e5546d95a8cd73ce28",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/881281250f74549f560408e5546d95a8cd73ce28/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "8b560ecb24ee4fa4e839272dcf2653a4fa525a34",
          "url": "https://api.github.com/repos/psf/requests/commits/8b560ecb24ee4fa4e839272dcf2653a4fa525a34",
          "html_url": "https://github.com/psf/requests/commit/8b560ecb24ee4fa4e839272dcf2653a4fa525a34"
        },
        {
          "sha": "29fc8d1e9346a29b91513547d626e23f4c36e557",
          "url": "https://api.github.com/repos/psf/requests/commits/29fc8d1e9346a29b91513547d626e23f4c36e557",
          "html_url": "https://github.com/psf/requests/commit/29fc8d1e9346a29b91513547d626e23f4c36e557"
        }
      ]
    },
    {
      "sha": "6c8d9b1d0fd6bef2e7b617bcb1574e69c4fc8780",
      "node_id": "C_kwDOABTKOtoAKDZjOGQ5YjFkMGZkNmJlZjJlN2I2MTdiY2IxNTc0ZTY5YzRmYzg3ODA",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2023-09-13T14:33:58Z"
        },
        "committer": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2023-09-13T14:33:58Z"
        },
        "message": "Autoclose specific issue templates\n\nWe spend a fair amount of time closing issues because people don't read\nthe template closely or understand what they're being told. Let's take\nadvantage of being able to auto-label an issue based on the template and\nthen trigger a workflow to auto-magically close the issue with a message\nand lock the issue.",
        "tree": {
          "sha": "5bf183e552fee5cfe68a6b841ae1a1f29a68104b",
          "url": "https://api.github.com/repos/psf/requests/git/trees/5bf183e552fee5cfe68a6b841ae1a1f29a68104b"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/6c8d9b1d0fd6bef2e7b617bcb1574e69c4fc8780",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\niQIzBAABCAAdFiEEgSpQDY8Q9shZFt4GZW0zleSpeRoFAmUByOEACgkQZW0zleSp\neRodLw/7Bou8ACZV4y/jJtMHokSeUq3gp74J5CumGJdJ59b2UU28TIVGLaswBWbX\nkzmpXyz7zcIZdvYBPtRxbchvBVKHyH+iMoPwShFmJrQPbAxp4yRLdDS5vcaigYqB\nDCHBgL02rWjnERCH7ReV/TutlgXqw3HUYaPgy2O7uVvGKCPkHIgJ2O/iygT1qJyd\n5bOGJNo+1BQ+LLNJ6X2bj1HpGjKEsec9Fo1Alb02PmfGAWkAcwNUixizorqi1IZN\nL1mXFLUMLsfujXhetDN3m0btQMrAB+DL/O04Q+82rOjv0GwYMUPcnTZyZxiaw4PV\nw6X50l90VVZUPI5HK+sEhfPwIRB/uk+w7O2KewhXIhfm2hy61IVc74MKCvbBpY5e\nnfByZ2OR6HVB/pjuU9a5VhBJ+LX9eVNBt3gcMSlNkKNqC4BUiX/NJDwTDcWm41Uy\nHR7kHIe74sB/zd+7aLtugk6gXPvJkqyXinN/KWAWP8p1FRNPj3jzRF+l5KLhpz7k\nymVIKvTvut4QpPtEz+X7L6sJyLBIPYDepWitFtNlk+4ERsjeI11f6m9ifG1JtAoC\n7YKACuaCMqtniiZbv73WdzWIsC/2C5J5nSrOA9moalEfyI4p6jihO7xdIiaQ18C2\nZM2uj1Mn++8IqvdCgSJdLyBT3D252Qapkw6/2j8qKHJr/paXLDU=\n=1J9W\n-----END PGP SIGNATURE-----",
          "payload": "tree 5bf183e552fee5cfe68a6b841ae1a1f29a68104b\nparent 881281250f74549f560408e5546d95a8cd73ce28\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1694615638 -0500\ncommitter Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1694615638 -0500\n\nAutoclose specific issue templates\n\nWe spend a fair amount of time closing issues because people don't read\nthe template closely or understand what they're being told. Let's take\nadvantage of being able to auto-label an issue based on the template and\nthen trigger a workflow to auto-magically close the issue with a message\nand lock the issue.\n",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/6c8d9b1d0fd6bef2e7b617bcb1574e69c4fc8780",
      "html_url": "https://github.com/psf/requests/commit/6c8d9b1d0fd6bef2e7b617bcb1574e69c4fc8780",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/6c8d9b1d0fd6bef2e7b617bcb1574e69c4fc8780/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "881281250f74549f560408e5546d95a8cd73ce28",
          "url": "https://api.github.com/repos/psf/requests/commits/881281250f74549f560408e5546d95a8cd73ce28",
          "html_url": "https://github.com/psf/requests/commit/881281250f74549f560408e5546d95a8cd73ce28"
        }
      ]
    },
    {
      "sha": "a775435c4b3ecb9f8f49b91ccb5403a071a0a4ee",
      "node_id": "C_kwDOABTKOtoAKGE3NzU0MzVjNGIzZWNiOWY4ZjQ5YjkxY2NiNTQwM2EwNzFhMGE0ZWU",
      "commit": {
        "author": {
          "name": "dependabot[bot]",
          "email": "49699333+dependabot[bot]@users.noreply.github.com",
          "date": "2023-09-25T16:28:35Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-09-25T16:28:35Z"
        },
        "message": "Bump actions/checkout from 4.0.0 to 4.1.0\n\nBumps [actions/checkout](https://github.com/actions/checkout) from 4.0.0 to 4.1.0.\n- [Release notes](https://github.com/actions/checkout/releases)\n- [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/actions/checkout/compare/3df4ab11eba7bda6032a0b82a6bb43b11571feac...8ade135a41bc03ea155e62e844d188df1ea18608)\n\n---\nupdated-dependencies:\n- dependency-name: actions/checkout\n  dependency-type: direct:production\n  update-type: version-update:semver-minor\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
        "tree": {
          "sha": "19426ba7f7c1042a25de2cc22ddc6a83a3b45d9e",
          "url": "https://api.github.com/repos/psf/requests/git/trees/19426ba7f7c1042a25de2cc22ddc6a83a3b45d9e"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/a775435c4b3ecb9f8f49b91ccb5403a071a0a4ee",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlEbUzCRBK7hj4Ov3rIwAAyqEIALK/tCRxYsGlSKJV+KqJKHW4\npmsii5ZbxBDRHkxgHJohkHUVE194e76lVvhi022ntqlzPC98sWm4R8K5uxIaSOII\nKpV7IP3vHYX6P4ZjY0E2L9gsOf8VkBylBLoLsvi2j3aOx11Zd26o6JNd+b6JjjaY\ncBgVgorOYkGSchmhF6TfD9OU4eGe/Y49FXJrz3sSYgD8a3EA5imNazumjdsVG6vS\naa756X60WzE44MRR1cxe+NiGtdOxbgKO1pQUt62YqxM0rxkVfl3nk8EI0I1sczRJ\n2zt8m1iZg6OftwFcKGms6ecXExeADH37GGw4ZnX/dfo4+xVxWu+/vHwnjkoMzV0=\n=HwP8\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 19426ba7f7c1042a25de2cc22ddc6a83a3b45d9e\nparent 881281250f74549f560408e5546d95a8cd73ce28\nauthor dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> 1695659315 +0000\ncommitter GitHub <noreply@github.com> 1695659315 +0000\n\nBump actions/checkout from 4.0.0 to 4.1.0\n\nBumps [actions/checkout](https://github.com/actions/checkout) from 4.0.0 to 4.1.0.\n- [Release notes](https://github.com/actions/checkout/releases)\n- [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/actions/checkout/compare/3df4ab11eba7bda6032a0b82a6bb43b11571feac...8ade135a41bc03ea155e62e844d188df1ea18608)\n\n---\nupdated-dependencies:\n- dependency-name: actions/checkout\n  dependency-type: direct:production\n  update-type: version-update:semver-minor\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/a775435c4b3ecb9f8f49b91ccb5403a071a0a4ee",
      "html_url": "https://github.com/psf/requests/commit/a775435c4b3ecb9f8f49b91ccb5403a071a0a4ee",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/a775435c4b3ecb9f8f49b91ccb5403a071a0a4ee/comments",
      "author": {
        "login": "dependabot[bot]",
        "id": 49699333,
        "node_id": "MDM6Qm90NDk2OTkzMzM=",
        "avatar_url": "https://avatars.githubusercontent.com/in/29110?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/dependabot%5Bbot%5D",
        "html_url": "https://github.com/apps/dependabot",
        "followers_url": "https://api.github.com/users/dependabot%5Bbot%5D/followers",
        "following_url": "https://api.github.com/users/dependabot%5Bbot%5D/following{/other_user}",
        "gists_url": "https://api.github.com/users/dependabot%5Bbot%5D/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/dependabot%5Bbot%5D/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/dependabot%5Bbot%5D/subscriptions",
        "organizations_url": "https://api.github.com/users/dependabot%5Bbot%5D/orgs",
        "repos_url": "https://api.github.com/users/dependabot%5Bbot%5D/repos",
        "events_url": "https://api.github.com/users/dependabot%5Bbot%5D/events{/privacy}",
        "received_events_url": "https://api.github.com/users/dependabot%5Bbot%5D/received_events",
        "type": "Bot",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "881281250f74549f560408e5546d95a8cd73ce28",
          "url": "https://api.github.com/repos/psf/requests/commits/881281250f74549f560408e5546d95a8cd73ce28",
          "html_url": "https://github.com/psf/requests/commit/881281250f74549f560408e5546d95a8cd73ce28"
        }
      ]
    },
    {
      "sha": "ee93fac6b2f715151f1aa9a1a06ddba9f7dcc59a",
      "node_id": "C_kwDOABTKOtoAKGVlOTNmYWM2YjJmNzE1MTUxZjFhYTlhMWEwNmRkYmE5ZjdkY2M1OWE",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2023-09-25T18:30:05Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-09-25T18:30:05Z"
        },
        "message": "Merge pull request #6538 from psf/dependabot/github_actions/actions/checkout-4.1.0\n\nBump actions/checkout from 4.0.0 to 4.1.0",
        "tree": {
          "sha": "19426ba7f7c1042a25de2cc22ddc6a83a3b45d9e",
          "url": "https://api.github.com/repos/psf/requests/git/trees/19426ba7f7c1042a25de2cc22ddc6a83a3b45d9e"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/ee93fac6b2f715151f1aa9a1a06ddba9f7dcc59a",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlEdGtCRBK7hj4Ov3rIwAAmd8IAHUOHhQYGn0v4eFo5/KiTw1+\nMCMDDt44cGhEu+iNBQXSjHOn0lNj3kXPIaVCB6F1yIjHpny10okLsRiShSFpXqKv\ny5TuDd+hX0WYbZWUSrHpo2dJEnggl9kclOYFhzv4kcdTyVNfXN23TIE4PmxR4/ab\n9C5d6M6cTeFhgcGU2zZ8KzH2tdz9LGV3lQAvjWJsAzyJ93D2UgUNPlChG3x56/6V\nKs8dsMgBFQ74cKF720cNzuS1Ba4tZvpTD/JHaMkMqw4Wxcec4ukKNwnSlrmSWHnT\njaDlIoF5loGumal6qt2mxAEmxEoAWhQRBffW7TOGADAbnzsTw6OEs56Zhk/NPkw=\n=JUR0\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 19426ba7f7c1042a25de2cc22ddc6a83a3b45d9e\nparent 881281250f74549f560408e5546d95a8cd73ce28\nparent a775435c4b3ecb9f8f49b91ccb5403a071a0a4ee\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1695666605 -0700\ncommitter GitHub <noreply@github.com> 1695666605 -0700\n\nMerge pull request #6538 from psf/dependabot/github_actions/actions/checkout-4.1.0\n\nBump actions/checkout from 4.0.0 to 4.1.0",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/ee93fac6b2f715151f1aa9a1a06ddba9f7dcc59a",
      "html_url": "https://github.com/psf/requests/commit/ee93fac6b2f715151f1aa9a1a06ddba9f7dcc59a",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/ee93fac6b2f715151f1aa9a1a06ddba9f7dcc59a/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "881281250f74549f560408e5546d95a8cd73ce28",
          "url": "https://api.github.com/repos/psf/requests/commits/881281250f74549f560408e5546d95a8cd73ce28",
          "html_url": "https://github.com/psf/requests/commit/881281250f74549f560408e5546d95a8cd73ce28"
        },
        {
          "sha": "a775435c4b3ecb9f8f49b91ccb5403a071a0a4ee",
          "url": "https://api.github.com/repos/psf/requests/commits/a775435c4b3ecb9f8f49b91ccb5403a071a0a4ee",
          "html_url": "https://github.com/psf/requests/commit/a775435c4b3ecb9f8f49b91ccb5403a071a0a4ee"
        }
      ]
    },
    {
      "sha": "f5a7aefc2dc123c65ec1c6d3e83949999b03876b",
      "node_id": "C_kwDOABTKOtoAKGY1YTdhZWZjMmRjMTIzYzY1ZWMxYzZkM2U4Mzk0OTk5OWIwMzg3NmI",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2023-10-06T22:34:24Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-10-06T22:34:24Z"
        },
        "message": "Fix urllib3 pin in setup.cfg (#6545)",
        "tree": {
          "sha": "eb0f6fb089a2f775579943deabf8fa94cb34fa72",
          "url": "https://api.github.com/repos/psf/requests/git/trees/eb0f6fb089a2f775579943deabf8fa94cb34fa72"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/f5a7aefc2dc123c65ec1c6d3e83949999b03876b",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlIItwCRBK7hj4Ov3rIwAAvLQIAI78YKCWiJeuKWT/RU2dtJr0\nlM874d/EEp33+sGA18dUbIu823dmIc3riI4t8LCPQF91BTHt6k/2kw6FgG8DjidI\nieC/9zVAwQqTph/yRnL5+HkvQ0OW7xTufvxBvpZAULqvbPUNJH5HwM4hT6H8Rfq9\n+WgohlrYisdSORRynyQW+4wEzDfOib5LQhPkX8yddD7Us6Tkk0JCS6CaXAz8Z5nu\nDmBUbwQ5cQT0X6K16R7rhiCtu2duU9wfHSETELSmu6+71BHR58EMkJqRaWVFQJRi\ns+r55YARPttqtDXno1tMXC4HmntMnfYEhzrknQTJszUsZKP01scghz4efJK74iU=\n=aLJ4\n-----END PGP SIGNATURE-----\n",
          "payload": "tree eb0f6fb089a2f775579943deabf8fa94cb34fa72\nparent ee93fac6b2f715151f1aa9a1a06ddba9f7dcc59a\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1696631664 -0700\ncommitter GitHub <noreply@github.com> 1696631664 -0600\n\nFix urllib3 pin in setup.cfg (#6545)\n\n",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/f5a7aefc2dc123c65ec1c6d3e83949999b03876b",
      "html_url": "https://github.com/psf/requests/commit/f5a7aefc2dc123c65ec1c6d3e83949999b03876b",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/f5a7aefc2dc123c65ec1c6d3e83949999b03876b/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "ee93fac6b2f715151f1aa9a1a06ddba9f7dcc59a",
          "url": "https://api.github.com/repos/psf/requests/commits/ee93fac6b2f715151f1aa9a1a06ddba9f7dcc59a",
          "html_url": "https://github.com/psf/requests/commit/ee93fac6b2f715151f1aa9a1a06ddba9f7dcc59a"
        }
      ]
    },
    {
      "sha": "42a3b5cce8336c52ad7102a3a493576ba40fb4fa",
      "node_id": "C_kwDOABTKOtoAKDQyYTNiNWNjZTgzMzZjNTJhZDcxMDJhM2E0OTM1NzZiYTQwZmI0ZmE",
      "commit": {
        "author": {
          "name": "dependabot[bot]",
          "email": "49699333+dependabot[bot]@users.noreply.github.com",
          "date": "2023-10-09T16:29:55Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-10-09T16:29:55Z"
        },
        "message": "Bump github/codeql-action from 2.21.3 to 2.22.1\n\nBumps [github/codeql-action](https://github.com/github/codeql-action) from 2.21.3 to 2.22.1.\n- [Release notes](https://github.com/github/codeql-action/releases)\n- [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/github/codeql-action/compare/5b6282e01c62d02e720b81eb8a51204f527c3624...fdcae64e1484d349b3366718cdfef3d404390e85)\n\n---\nupdated-dependencies:\n- dependency-name: github/codeql-action\n  dependency-type: direct:production\n  update-type: version-update:semver-minor\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
        "tree": {
          "sha": "52ad54769274db24eb915bd53d25adc4e1ac1488",
          "url": "https://api.github.com/repos/psf/requests/git/trees/52ad54769274db24eb915bd53d25adc4e1ac1488"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/42a3b5cce8336c52ad7102a3a493576ba40fb4fa",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlJCqDCRBK7hj4Ov3rIwAADM0IALHcbUUvG2/nGPZynxt4wjP1\nFnrFCyZPBywLtDs9NehDZGm9gBMb6NkDe0aIMvoLAJMDKXfQJL2KXWPUIzmJ5nL2\njsywbqKshiLN4Ai6j/mj13V2qhrjxLn4767SPeV+n0vlcYTBGvfLYtQWgxaqG8We\nzVZf8ikXyuX+WiRgAk8fzjwdNGCQhOQkWQsnYIcC4u2UhFrZKwVOqAvvVPVdk2ua\nJWtC54vTs0+TEG5NXDFBKAqjlv6DKvETqqYdgU6Or4oNYv3ASaJjE3XVUZeePpjX\nOFaLvL88inV/rgQN+6ZeEF6v3Zro0syndQiUCFVkl5HAs9Qx73hc78O2OZDT9f4=\n=SGUr\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 52ad54769274db24eb915bd53d25adc4e1ac1488\nparent f5a7aefc2dc123c65ec1c6d3e83949999b03876b\nauthor dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> 1696868995 +0000\ncommitter GitHub <noreply@github.com> 1696868995 +0000\n\nBump github/codeql-action from 2.21.3 to 2.22.1\n\nBumps [github/codeql-action](https://github.com/github/codeql-action) from 2.21.3 to 2.22.1.\n- [Release notes](https://github.com/github/codeql-action/releases)\n- [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/github/codeql-action/compare/5b6282e01c62d02e720b81eb8a51204f527c3624...fdcae64e1484d349b3366718cdfef3d404390e85)\n\n---\nupdated-dependencies:\n- dependency-name: github/codeql-action\n  dependency-type: direct:production\n  update-type: version-update:semver-minor\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/42a3b5cce8336c52ad7102a3a493576ba40fb4fa",
      "html_url": "https://github.com/psf/requests/commit/42a3b5cce8336c52ad7102a3a493576ba40fb4fa",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/42a3b5cce8336c52ad7102a3a493576ba40fb4fa/comments",
      "author": {
        "login": "dependabot[bot]",
        "id": 49699333,
        "node_id": "MDM6Qm90NDk2OTkzMzM=",
        "avatar_url": "https://avatars.githubusercontent.com/in/29110?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/dependabot%5Bbot%5D",
        "html_url": "https://github.com/apps/dependabot",
        "followers_url": "https://api.github.com/users/dependabot%5Bbot%5D/followers",
        "following_url": "https://api.github.com/users/dependabot%5Bbot%5D/following{/other_user}",
        "gists_url": "https://api.github.com/users/dependabot%5Bbot%5D/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/dependabot%5Bbot%5D/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/dependabot%5Bbot%5D/subscriptions",
        "organizations_url": "https://api.github.com/users/dependabot%5Bbot%5D/orgs",
        "repos_url": "https://api.github.com/users/dependabot%5Bbot%5D/repos",
        "events_url": "https://api.github.com/users/dependabot%5Bbot%5D/events{/privacy}",
        "received_events_url": "https://api.github.com/users/dependabot%5Bbot%5D/received_events",
        "type": "Bot",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "f5a7aefc2dc123c65ec1c6d3e83949999b03876b",
          "url": "https://api.github.com/repos/psf/requests/commits/f5a7aefc2dc123c65ec1c6d3e83949999b03876b",
          "html_url": "https://github.com/psf/requests/commit/f5a7aefc2dc123c65ec1c6d3e83949999b03876b"
        }
      ]
    },
    {
      "sha": "8199a2b3894536fd3cd587ea8c7946aab6277e3f",
      "node_id": "C_kwDOABTKOtoAKDgxOTlhMmIzODk0NTM2ZmQzY2Q1ODdlYThjNzk0NmFhYjYyNzdlM2Y",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2023-10-09T16:49:28Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-10-09T16:49:28Z"
        },
        "message": "Merge pull request #6548 from psf/dependabot/github_actions/github/codeql-action-2.22.1\n\nBump github/codeql-action from 2.21.3 to 2.22.1",
        "tree": {
          "sha": "52ad54769274db24eb915bd53d25adc4e1ac1488",
          "url": "https://api.github.com/repos/psf/requests/git/trees/52ad54769274db24eb915bd53d25adc4e1ac1488"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/8199a2b3894536fd3cd587ea8c7946aab6277e3f",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlJC8YCRBK7hj4Ov3rIwAA+D4IAHEIDyrif+e8hFJYr5/AwCv2\n30d68ags5VnHFb+IBitYtMk0QqftbImvg1VIwXRbpWu6FkstK0SWwvpLbikQNo/M\n+Yl+QZh1pOpyFLh8B+1wBhL2ClToTB3oe6H6KKiQ4sfQjuo8xO1YQvK7TYmIRDJg\nbgUvQUgLppuW9So83Ec4VMOVPcHXi7zS9P4/gtOBGOdVpUAiYg05Txgn8EAIRD8H\nyMisDRbN6z7WQoWSVyxVUIsvrsDRZxQomjQ1v8QxRSWPVBC/Yvu74kumX3A+lge/\nQ4XrDTc14v3xuYGgYLni0f55sLdDLY7OZelmFVDP2ISYSeHcOI1PkskwFHxNRVA=\n=3dcN\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 52ad54769274db24eb915bd53d25adc4e1ac1488\nparent f5a7aefc2dc123c65ec1c6d3e83949999b03876b\nparent 42a3b5cce8336c52ad7102a3a493576ba40fb4fa\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1696870168 -0700\ncommitter GitHub <noreply@github.com> 1696870168 -0700\n\nMerge pull request #6548 from psf/dependabot/github_actions/github/codeql-action-2.22.1\n\nBump github/codeql-action from 2.21.3 to 2.22.1",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/8199a2b3894536fd3cd587ea8c7946aab6277e3f",
      "html_url": "https://github.com/psf/requests/commit/8199a2b3894536fd3cd587ea8c7946aab6277e3f",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/8199a2b3894536fd3cd587ea8c7946aab6277e3f/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "f5a7aefc2dc123c65ec1c6d3e83949999b03876b",
          "url": "https://api.github.com/repos/psf/requests/commits/f5a7aefc2dc123c65ec1c6d3e83949999b03876b",
          "html_url": "https://github.com/psf/requests/commit/f5a7aefc2dc123c65ec1c6d3e83949999b03876b"
        },
        {
          "sha": "42a3b5cce8336c52ad7102a3a493576ba40fb4fa",
          "url": "https://api.github.com/repos/psf/requests/commits/42a3b5cce8336c52ad7102a3a493576ba40fb4fa",
          "html_url": "https://github.com/psf/requests/commit/42a3b5cce8336c52ad7102a3a493576ba40fb4fa"
        }
      ]
    },
    {
      "sha": "f75b9504fc8427c1617bac2dd1e1aa405c9f1b1b",
      "node_id": "C_kwDOABTKOtoAKGY3NWI5NTA0ZmM4NDI3YzE2MTdiYWMyZGQxZTFhYTQwNWM5ZjFiMWI",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2023-10-11T13:19:14Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-10-11T13:19:14Z"
        },
        "message": "Update close comment\n\nCo-authored-by: Nate Prewitt <nate.prewitt@gmail.com>",
        "tree": {
          "sha": "ebcecec5222d1ff7fbb55f20c7385060c804cca2",
          "url": "https://api.github.com/repos/psf/requests/git/trees/ebcecec5222d1ff7fbb55f20c7385060c804cca2"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/f75b9504fc8427c1617bac2dd1e1aa405c9f1b1b",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlJqDSCRBK7hj4Ov3rIwAABJAIAB6ycb/jUZvtXVdHLpcPZG+k\nekUz8/cU9ochxcu6jqEDwEcCKxh+ueUu3RAl5EQ92Gif4dEx/5ql62jk0K73Mvuq\nEvwTy3c6S7WKhpi6HG/pTJedgiCEi3NJoPVBkMUL1hVm6oB7WfHNq6eZK372H12A\nrHHZRGLNl6RpU/bTu2n+UdCY2nSRufyEZUZY2JaFV3wcoORNYH/VQQ8QR4WIxVTo\nWpLibE4t8HDtnZQAkckf1+eiSPfq0sPk+qGm3AjMxnKVL7YEb7j5uBaQCfk/6DLd\nfy1KTmoBklFiWtoHkaZaJJNFrAxnk9cuDhSQQfCfSDmPSOav/Eh65k5wHyiu9Z0=\n=Ptg/\n-----END PGP SIGNATURE-----\n",
          "payload": "tree ebcecec5222d1ff7fbb55f20c7385060c804cca2\nparent 6c8d9b1d0fd6bef2e7b617bcb1574e69c4fc8780\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1697030354 -0500\ncommitter GitHub <noreply@github.com> 1697030354 -0500\n\nUpdate close comment\n\nCo-authored-by: Nate Prewitt <nate.prewitt@gmail.com>",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/f75b9504fc8427c1617bac2dd1e1aa405c9f1b1b",
      "html_url": "https://github.com/psf/requests/commit/f75b9504fc8427c1617bac2dd1e1aa405c9f1b1b",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/f75b9504fc8427c1617bac2dd1e1aa405c9f1b1b/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "6c8d9b1d0fd6bef2e7b617bcb1574e69c4fc8780",
          "url": "https://api.github.com/repos/psf/requests/commits/6c8d9b1d0fd6bef2e7b617bcb1574e69c4fc8780",
          "html_url": "https://github.com/psf/requests/commit/6c8d9b1d0fd6bef2e7b617bcb1574e69c4fc8780"
        }
      ]
    },
    {
      "sha": "818776862239a7dd97d39157ec3a202c35af122c",
      "node_id": "C_kwDOABTKOtoAKDgxODc3Njg2MjIzOWE3ZGQ5N2QzOTE1N2VjM2EyMDJjMzVhZjEyMmM",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2023-10-11T13:19:57Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-10-11T13:19:57Z"
        },
        "message": "Update close-issues.yml\n\nRemove references to GITHUB_TOKEN/MY_TOKEN",
        "tree": {
          "sha": "ef63e01bfee1c6768edd0410fd3ab6a30682fa0f",
          "url": "https://api.github.com/repos/psf/requests/git/trees/ef63e01bfee1c6768edd0410fd3ab6a30682fa0f"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/818776862239a7dd97d39157ec3a202c35af122c",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlJqD9CRBK7hj4Ov3rIwAAoe8IADi1iaPoRGpJlYdCwL2jK8+0\nDUq4KP0MzYDJus7C9WUN6uj0w5r5gKD91EtnC3Fl/o8vuy9hDB3JwzLzce6XmGyU\n99FztbVC/PVxjeProAcADWW8tRyRg08uTqVSFizkeonNa4hC7gI4bFtHNR5Fn5mL\nhousWtqkmX2c6i8h20KloLhogJ/85YdP7arC2lcOjLhb00K6MvuDKJ+EESdoSOm3\n9IudufmGUCxCaqLYwIc8RjOOGeWBnGjHcaz4K8RdgaH8wF8MWHgIvR7LZx9rcsmX\nsFPtgeR4atkyJz+tEuANA5YI0TbrIBWrv4oNd1vao5xZsGNFX6cPTi1Odx77FL4=\n=jnT4\n-----END PGP SIGNATURE-----\n",
          "payload": "tree ef63e01bfee1c6768edd0410fd3ab6a30682fa0f\nparent f75b9504fc8427c1617bac2dd1e1aa405c9f1b1b\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1697030397 -0500\ncommitter GitHub <noreply@github.com> 1697030397 -0500\n\nUpdate close-issues.yml\n\nRemove references to GITHUB_TOKEN/MY_TOKEN",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/818776862239a7dd97d39157ec3a202c35af122c",
      "html_url": "https://github.com/psf/requests/commit/818776862239a7dd97d39157ec3a202c35af122c",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/818776862239a7dd97d39157ec3a202c35af122c/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "f75b9504fc8427c1617bac2dd1e1aa405c9f1b1b",
          "url": "https://api.github.com/repos/psf/requests/commits/f75b9504fc8427c1617bac2dd1e1aa405c9f1b1b",
          "html_url": "https://github.com/psf/requests/commit/f75b9504fc8427c1617bac2dd1e1aa405c9f1b1b"
        }
      ]
    },
    {
      "sha": "b55bb15c35132f021fc0997c6a72730abe2216f5",
      "node_id": "C_kwDOABTKOtoAKGI1NWJiMTVjMzUxMzJmMDIxZmMwOTk3YzZhNzI3MzBhYmUyMjE2ZjU",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2023-10-11T16:29:20Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-10-11T16:29:20Z"
        },
        "message": "Merge pull request #6527 from sigmavirus24/update-templates\n\nAutoclose specific issue templates",
        "tree": {
          "sha": "dfb102db5a46ba5a5879b8bac522086bfa7a75c8",
          "url": "https://api.github.com/repos/psf/requests/git/trees/dfb102db5a46ba5a5879b8bac522086bfa7a75c8"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/b55bb15c35132f021fc0997c6a72730abe2216f5",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlJs1gCRBK7hj4Ov3rIwAAL5UIADxs6/WtuGA+KKGCdqpL5qXx\nflrSeGcPD/AeXO8f6cYlpZyhvuN0oc7CBM+fF+0x72lBUBOzjID9CX7E9GiFgyxa\njFATq6pYGkQTOL+ukToFIeBc3m+u3B61N0uUutE+QAivyeq6qEfcYa8UI+uOO9fC\nflyi3TeIEA7pHk5R6HVtIxH2jB4wUgz13QrQLTtGc4RxYJ0f4D2l2D/Amp45znev\nu4fc1a6jZaphq8+cG+5Xp41Q8mb1RSbMiSkXu/dlpwiJMFF5n61nIBqEOWHCwmb6\nM+kb3jdribGArGPwSlzACEvR8+jGV3HDjvd7fkIUg5Nzl0Pid169tIpB/Pr3SkQ=\n=GRac\n-----END PGP SIGNATURE-----\n",
          "payload": "tree dfb102db5a46ba5a5879b8bac522086bfa7a75c8\nparent 8199a2b3894536fd3cd587ea8c7946aab6277e3f\nparent 818776862239a7dd97d39157ec3a202c35af122c\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1697041760 -0700\ncommitter GitHub <noreply@github.com> 1697041760 -0700\n\nMerge pull request #6527 from sigmavirus24/update-templates\n\nAutoclose specific issue templates",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/b55bb15c35132f021fc0997c6a72730abe2216f5",
      "html_url": "https://github.com/psf/requests/commit/b55bb15c35132f021fc0997c6a72730abe2216f5",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/b55bb15c35132f021fc0997c6a72730abe2216f5/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "8199a2b3894536fd3cd587ea8c7946aab6277e3f",
          "url": "https://api.github.com/repos/psf/requests/commits/8199a2b3894536fd3cd587ea8c7946aab6277e3f",
          "html_url": "https://github.com/psf/requests/commit/8199a2b3894536fd3cd587ea8c7946aab6277e3f"
        },
        {
          "sha": "818776862239a7dd97d39157ec3a202c35af122c",
          "url": "https://api.github.com/repos/psf/requests/commits/818776862239a7dd97d39157ec3a202c35af122c",
          "html_url": "https://github.com/psf/requests/commit/818776862239a7dd97d39157ec3a202c35af122c"
        }
      ]
    },
    {
      "sha": "a8e9c1b436e9a35c271d8b690eefbc0d3d18df0f",
      "node_id": "C_kwDOABTKOtoAKGE4ZTljMWI0MzZlOWEzNWMyNzFkOGI2OTBlZWZiYzBkM2QxOGRmMGY",
      "commit": {
        "author": {
          "name": "sumedhrao7",
          "email": "sumedhrao7@gmail.com",
          "date": "2023-10-18T02:10:50Z"
        },
        "committer": {
          "name": "sumedhrao7",
          "email": "sumedhrao7@gmail.com",
          "date": "2023-10-18T02:10:50Z"
        },
        "message": "added assert statements into tests/test_requests/test_header_validation in regards to the issue #6551",
        "tree": {
          "sha": "5b2abb9a25646a73a26a3435452079bd88da2856",
          "url": "https://api.github.com/repos/psf/requests/git/trees/5b2abb9a25646a73a26a3435452079bd88da2856"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/a8e9c1b436e9a35c271d8b690eefbc0d3d18df0f",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/a8e9c1b436e9a35c271d8b690eefbc0d3d18df0f",
      "html_url": "https://github.com/psf/requests/commit/a8e9c1b436e9a35c271d8b690eefbc0d3d18df0f",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/a8e9c1b436e9a35c271d8b690eefbc0d3d18df0f/comments",
      "author": {
        "login": "swims-hjkl",
        "id": 49934133,
        "node_id": "MDQ6VXNlcjQ5OTM0MTMz",
        "avatar_url": "https://avatars.githubusercontent.com/u/49934133?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/swims-hjkl",
        "html_url": "https://github.com/swims-hjkl",
        "followers_url": "https://api.github.com/users/swims-hjkl/followers",
        "following_url": "https://api.github.com/users/swims-hjkl/following{/other_user}",
        "gists_url": "https://api.github.com/users/swims-hjkl/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/swims-hjkl/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/swims-hjkl/subscriptions",
        "organizations_url": "https://api.github.com/users/swims-hjkl/orgs",
        "repos_url": "https://api.github.com/users/swims-hjkl/repos",
        "events_url": "https://api.github.com/users/swims-hjkl/events{/privacy}",
        "received_events_url": "https://api.github.com/users/swims-hjkl/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "swims-hjkl",
        "id": 49934133,
        "node_id": "MDQ6VXNlcjQ5OTM0MTMz",
        "avatar_url": "https://avatars.githubusercontent.com/u/49934133?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/swims-hjkl",
        "html_url": "https://github.com/swims-hjkl",
        "followers_url": "https://api.github.com/users/swims-hjkl/followers",
        "following_url": "https://api.github.com/users/swims-hjkl/following{/other_user}",
        "gists_url": "https://api.github.com/users/swims-hjkl/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/swims-hjkl/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/swims-hjkl/subscriptions",
        "organizations_url": "https://api.github.com/users/swims-hjkl/orgs",
        "repos_url": "https://api.github.com/users/swims-hjkl/repos",
        "events_url": "https://api.github.com/users/swims-hjkl/events{/privacy}",
        "received_events_url": "https://api.github.com/users/swims-hjkl/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "b55bb15c35132f021fc0997c6a72730abe2216f5",
          "url": "https://api.github.com/repos/psf/requests/commits/b55bb15c35132f021fc0997c6a72730abe2216f5",
          "html_url": "https://github.com/psf/requests/commit/b55bb15c35132f021fc0997c6a72730abe2216f5"
        }
      ]
    },
    {
      "sha": "839a8edec37c81a18ac8332cfbd44f44e1ae6206",
      "node_id": "C_kwDOABTKOtoAKDgzOWE4ZWRlYzM3YzgxYTE4YWM4MzMyY2ZiZDQ0ZjQ0ZTFhZTYyMDY",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2023-10-18T06:08:52Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-10-18T06:08:52Z"
        },
        "message": "Merge pull request #6552 from swims-hjkl/issue/test_header_validation\n\n#6551  - assert statements for test test_header_validation",
        "tree": {
          "sha": "5b2abb9a25646a73a26a3435452079bd88da2856",
          "url": "https://api.github.com/repos/psf/requests/git/trees/5b2abb9a25646a73a26a3435452079bd88da2856"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/839a8edec37c81a18ac8332cfbd44f44e1ae6206",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlL3Z0CRBK7hj4Ov3rIwAAsNwIAKpjOCed2V4m6bKoEN8VHEkS\nl8zQUbfH9Zjyt8wG+WKlnuvFFJSDdiOGIvydJFcjjklG36loWxy/x8MXD77HOtu6\nnDGjreVb3IdaycS4SKyvsnQTecw57GuPrWqdUsDlV5EJEosUx4zAAD69i1pf8gLE\n9NRJy+dXrYkF+vr5cnrV9qsgdG7E1LDmsiC9feal2iriK7d6mJJjL8Qf379pM4d+\npMlvtVsEG7zR3Zy1nCauhFZXmLNDFp58cNm+/BahiphVKpRztIJJ+sUOP4M0I9Re\npy31y8VF4vLLansacx+hZLNi2fnr4C7mkBOpq5HJ2hea/8QMqnfFaUWqTCJ9gdQ=\n=1d3K\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 5b2abb9a25646a73a26a3435452079bd88da2856\nparent b55bb15c35132f021fc0997c6a72730abe2216f5\nparent a8e9c1b436e9a35c271d8b690eefbc0d3d18df0f\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1697609332 -0700\ncommitter GitHub <noreply@github.com> 1697609332 -0700\n\nMerge pull request #6552 from swims-hjkl/issue/test_header_validation\n\n#6551  - assert statements for test test_header_validation",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/839a8edec37c81a18ac8332cfbd44f44e1ae6206",
      "html_url": "https://github.com/psf/requests/commit/839a8edec37c81a18ac8332cfbd44f44e1ae6206",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/839a8edec37c81a18ac8332cfbd44f44e1ae6206/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "b55bb15c35132f021fc0997c6a72730abe2216f5",
          "url": "https://api.github.com/repos/psf/requests/commits/b55bb15c35132f021fc0997c6a72730abe2216f5",
          "html_url": "https://github.com/psf/requests/commit/b55bb15c35132f021fc0997c6a72730abe2216f5"
        },
        {
          "sha": "a8e9c1b436e9a35c271d8b690eefbc0d3d18df0f",
          "url": "https://api.github.com/repos/psf/requests/commits/a8e9c1b436e9a35c271d8b690eefbc0d3d18df0f",
          "html_url": "https://github.com/psf/requests/commit/a8e9c1b436e9a35c271d8b690eefbc0d3d18df0f"
        }
      ]
    },
    {
      "sha": "ad761abcdd2f1b5e4fcba549676b2ea52bd325cd",
      "node_id": "C_kwDOABTKOtoAKGFkNzYxYWJjZGQyZjFiNWU0ZmNiYTU0OTY3NmIyZWE1MmJkMzI1Y2Q",
      "commit": {
        "author": {
          "name": "mayank",
          "email": "amkarn258@gmail.com",
          "date": "2023-10-30T19:20:10Z"
        },
        "committer": {
          "name": "mayank",
          "email": "amkarn258@gmail.com",
          "date": "2023-10-30T19:20:10Z"
        },
        "message": "every chardet package maps to requests.packages.chardet.* package respectively",
        "tree": {
          "sha": "d61b4fdf83785758db1bca8bfcd05dcdf66281b6",
          "url": "https://api.github.com/repos/psf/requests/git/trees/d61b4fdf83785758db1bca8bfcd05dcdf66281b6"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/ad761abcdd2f1b5e4fcba549676b2ea52bd325cd",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/ad761abcdd2f1b5e4fcba549676b2ea52bd325cd",
      "html_url": "https://github.com/psf/requests/commit/ad761abcdd2f1b5e4fcba549676b2ea52bd325cd",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/ad761abcdd2f1b5e4fcba549676b2ea52bd325cd/comments",
      "author": {
        "login": "amkarn258",
        "id": 55189266,
        "node_id": "MDQ6VXNlcjU1MTg5MjY2",
        "avatar_url": "https://avatars.githubusercontent.com/u/55189266?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/amkarn258",
        "html_url": "https://github.com/amkarn258",
        "followers_url": "https://api.github.com/users/amkarn258/followers",
        "following_url": "https://api.github.com/users/amkarn258/following{/other_user}",
        "gists_url": "https://api.github.com/users/amkarn258/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/amkarn258/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/amkarn258/subscriptions",
        "organizations_url": "https://api.github.com/users/amkarn258/orgs",
        "repos_url": "https://api.github.com/users/amkarn258/repos",
        "events_url": "https://api.github.com/users/amkarn258/events{/privacy}",
        "received_events_url": "https://api.github.com/users/amkarn258/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "amkarn258",
        "id": 55189266,
        "node_id": "MDQ6VXNlcjU1MTg5MjY2",
        "avatar_url": "https://avatars.githubusercontent.com/u/55189266?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/amkarn258",
        "html_url": "https://github.com/amkarn258",
        "followers_url": "https://api.github.com/users/amkarn258/followers",
        "following_url": "https://api.github.com/users/amkarn258/following{/other_user}",
        "gists_url": "https://api.github.com/users/amkarn258/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/amkarn258/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/amkarn258/subscriptions",
        "organizations_url": "https://api.github.com/users/amkarn258/orgs",
        "repos_url": "https://api.github.com/users/amkarn258/repos",
        "events_url": "https://api.github.com/users/amkarn258/events{/privacy}",
        "received_events_url": "https://api.github.com/users/amkarn258/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "839a8edec37c81a18ac8332cfbd44f44e1ae6206",
          "url": "https://api.github.com/repos/psf/requests/commits/839a8edec37c81a18ac8332cfbd44f44e1ae6206",
          "html_url": "https://github.com/psf/requests/commit/839a8edec37c81a18ac8332cfbd44f44e1ae6206"
        }
      ]
    },
    {
      "sha": "e9b1217cff710307e5de9fb8ce2fc21eb79acec3",
      "node_id": "C_kwDOABTKOtoAKGU5YjEyMTdjZmY3MTAzMDdlNWRlOWZiOGNlMmZjMjFlYjc5YWNlYzM",
      "commit": {
        "author": {
          "name": "mayank",
          "email": "amkarn258@gmail.com",
          "date": "2023-10-31T15:07:59Z"
        },
        "committer": {
          "name": "mayank",
          "email": "amkarn258@gmail.com",
          "date": "2023-10-31T15:07:59Z"
        },
        "message": "added handling for chardet and charset_normalizer imports",
        "tree": {
          "sha": "d5047f365323ff27788f6876d3c48b67ee23c3fe",
          "url": "https://api.github.com/repos/psf/requests/git/trees/d5047f365323ff27788f6876d3c48b67ee23c3fe"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/e9b1217cff710307e5de9fb8ce2fc21eb79acec3",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/e9b1217cff710307e5de9fb8ce2fc21eb79acec3",
      "html_url": "https://github.com/psf/requests/commit/e9b1217cff710307e5de9fb8ce2fc21eb79acec3",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/e9b1217cff710307e5de9fb8ce2fc21eb79acec3/comments",
      "author": {
        "login": "amkarn258",
        "id": 55189266,
        "node_id": "MDQ6VXNlcjU1MTg5MjY2",
        "avatar_url": "https://avatars.githubusercontent.com/u/55189266?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/amkarn258",
        "html_url": "https://github.com/amkarn258",
        "followers_url": "https://api.github.com/users/amkarn258/followers",
        "following_url": "https://api.github.com/users/amkarn258/following{/other_user}",
        "gists_url": "https://api.github.com/users/amkarn258/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/amkarn258/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/amkarn258/subscriptions",
        "organizations_url": "https://api.github.com/users/amkarn258/orgs",
        "repos_url": "https://api.github.com/users/amkarn258/repos",
        "events_url": "https://api.github.com/users/amkarn258/events{/privacy}",
        "received_events_url": "https://api.github.com/users/amkarn258/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "amkarn258",
        "id": 55189266,
        "node_id": "MDQ6VXNlcjU1MTg5MjY2",
        "avatar_url": "https://avatars.githubusercontent.com/u/55189266?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/amkarn258",
        "html_url": "https://github.com/amkarn258",
        "followers_url": "https://api.github.com/users/amkarn258/followers",
        "following_url": "https://api.github.com/users/amkarn258/following{/other_user}",
        "gists_url": "https://api.github.com/users/amkarn258/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/amkarn258/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/amkarn258/subscriptions",
        "organizations_url": "https://api.github.com/users/amkarn258/orgs",
        "repos_url": "https://api.github.com/users/amkarn258/repos",
        "events_url": "https://api.github.com/users/amkarn258/events{/privacy}",
        "received_events_url": "https://api.github.com/users/amkarn258/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "ad761abcdd2f1b5e4fcba549676b2ea52bd325cd",
          "url": "https://api.github.com/repos/psf/requests/commits/ad761abcdd2f1b5e4fcba549676b2ea52bd325cd",
          "html_url": "https://github.com/psf/requests/commit/ad761abcdd2f1b5e4fcba549676b2ea52bd325cd"
        }
      ]
    },
    {
      "sha": "d7490c9d2dc967f68c6ca38b73aa099bc888a04e",
      "node_id": "C_kwDOABTKOtoAKGQ3NDkwYzlkMmRjOTY3ZjY4YzZjYTM4YjczYWEwOTliYzg4OGEwNGU",
      "commit": {
        "author": {
          "name": "amkarn258",
          "email": "55189266+amkarn258@users.noreply.github.com",
          "date": "2023-10-31T17:06:39Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-10-31T17:06:39Z"
        },
        "message": "Update src/requests/packages.py\n\nCo-authored-by: Ian Stapleton Cordasco <graffatcolmingov@gmail.com>",
        "tree": {
          "sha": "0a4764922b6c94c8b59ed09ccdd405bfa5519ad7",
          "url": "https://api.github.com/repos/psf/requests/git/trees/0a4764922b6c94c8b59ed09ccdd405bfa5519ad7"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/d7490c9d2dc967f68c6ca38b73aa099bc888a04e",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlQTQfCRBK7hj4Ov3rIwAAEH4IADai8Qmfd/6XMAoQhlFVgo72\nnBC7VgPyqwq/epqNHWH4zilM7Qi+3EVVku55w6rOa416isFb58klZLr4IckAcnPE\nUttSR7CRoN3mzJ+39WpvyDrRrP+4rdhPJRqvVLfHDTBTfwyjCEfgnhXPDyszc70E\n6lr1w/eUbOm9LbDzHbKAN7mgbJ06qPXzbIb3X6cttVOB/JuQzUgiDsr1YylbG8pa\nIe7g+2GMBCJPL1nBJ73cA+WyW1rL8HLosYaDhURU/pd7kiTJGf3/D6g/5O/nkmO5\nnSvvcFTOpsRy41BH4geM9HrWhDk39l82j4qbKpO+lY8Rb0yhpD9siBCNa3Ui3Wg=\n=EuS4\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 0a4764922b6c94c8b59ed09ccdd405bfa5519ad7\nparent e9b1217cff710307e5de9fb8ce2fc21eb79acec3\nauthor amkarn258 <55189266+amkarn258@users.noreply.github.com> 1698771999 +0530\ncommitter GitHub <noreply@github.com> 1698771999 +0530\n\nUpdate src/requests/packages.py\n\nCo-authored-by: Ian Stapleton Cordasco <graffatcolmingov@gmail.com>",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/d7490c9d2dc967f68c6ca38b73aa099bc888a04e",
      "html_url": "https://github.com/psf/requests/commit/d7490c9d2dc967f68c6ca38b73aa099bc888a04e",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/d7490c9d2dc967f68c6ca38b73aa099bc888a04e/comments",
      "author": {
        "login": "amkarn258",
        "id": 55189266,
        "node_id": "MDQ6VXNlcjU1MTg5MjY2",
        "avatar_url": "https://avatars.githubusercontent.com/u/55189266?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/amkarn258",
        "html_url": "https://github.com/amkarn258",
        "followers_url": "https://api.github.com/users/amkarn258/followers",
        "following_url": "https://api.github.com/users/amkarn258/following{/other_user}",
        "gists_url": "https://api.github.com/users/amkarn258/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/amkarn258/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/amkarn258/subscriptions",
        "organizations_url": "https://api.github.com/users/amkarn258/orgs",
        "repos_url": "https://api.github.com/users/amkarn258/repos",
        "events_url": "https://api.github.com/users/amkarn258/events{/privacy}",
        "received_events_url": "https://api.github.com/users/amkarn258/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "e9b1217cff710307e5de9fb8ce2fc21eb79acec3",
          "url": "https://api.github.com/repos/psf/requests/commits/e9b1217cff710307e5de9fb8ce2fc21eb79acec3",
          "html_url": "https://github.com/psf/requests/commit/e9b1217cff710307e5de9fb8ce2fc21eb79acec3"
        }
      ]
    },
    {
      "sha": "89cde235bec9374273281c1b4c9277c409246a6c",
      "node_id": "C_kwDOABTKOtoAKDg5Y2RlMjM1YmVjOTM3NDI3MzI4MWMxYjRjOTI3N2M0MDkyNDZhNmM",
      "commit": {
        "author": {
          "name": "mayank",
          "email": "amkarn258@gmail.com",
          "date": "2023-11-04T17:50:21Z"
        },
        "committer": {
          "name": "mayank",
          "email": "amkarn258@gmail.com",
          "date": "2023-11-04T17:50:21Z"
        },
        "message": "checkstyle",
        "tree": {
          "sha": "6367751d2e86f51f6e6908d05721ade7b5f11744",
          "url": "https://api.github.com/repos/psf/requests/git/trees/6367751d2e86f51f6e6908d05721ade7b5f11744"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/89cde235bec9374273281c1b4c9277c409246a6c",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/89cde235bec9374273281c1b4c9277c409246a6c",
      "html_url": "https://github.com/psf/requests/commit/89cde235bec9374273281c1b4c9277c409246a6c",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/89cde235bec9374273281c1b4c9277c409246a6c/comments",
      "author": {
        "login": "amkarn258",
        "id": 55189266,
        "node_id": "MDQ6VXNlcjU1MTg5MjY2",
        "avatar_url": "https://avatars.githubusercontent.com/u/55189266?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/amkarn258",
        "html_url": "https://github.com/amkarn258",
        "followers_url": "https://api.github.com/users/amkarn258/followers",
        "following_url": "https://api.github.com/users/amkarn258/following{/other_user}",
        "gists_url": "https://api.github.com/users/amkarn258/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/amkarn258/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/amkarn258/subscriptions",
        "organizations_url": "https://api.github.com/users/amkarn258/orgs",
        "repos_url": "https://api.github.com/users/amkarn258/repos",
        "events_url": "https://api.github.com/users/amkarn258/events{/privacy}",
        "received_events_url": "https://api.github.com/users/amkarn258/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "amkarn258",
        "id": 55189266,
        "node_id": "MDQ6VXNlcjU1MTg5MjY2",
        "avatar_url": "https://avatars.githubusercontent.com/u/55189266?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/amkarn258",
        "html_url": "https://github.com/amkarn258",
        "followers_url": "https://api.github.com/users/amkarn258/followers",
        "following_url": "https://api.github.com/users/amkarn258/following{/other_user}",
        "gists_url": "https://api.github.com/users/amkarn258/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/amkarn258/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/amkarn258/subscriptions",
        "organizations_url": "https://api.github.com/users/amkarn258/orgs",
        "repos_url": "https://api.github.com/users/amkarn258/repos",
        "events_url": "https://api.github.com/users/amkarn258/events{/privacy}",
        "received_events_url": "https://api.github.com/users/amkarn258/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "d7490c9d2dc967f68c6ca38b73aa099bc888a04e",
          "url": "https://api.github.com/repos/psf/requests/commits/d7490c9d2dc967f68c6ca38b73aa099bc888a04e",
          "html_url": "https://github.com/psf/requests/commit/d7490c9d2dc967f68c6ca38b73aa099bc888a04e"
        }
      ]
    },
    {
      "sha": "c32b046243dcbf0dceb952da1317261109ac45c4",
      "node_id": "C_kwDOABTKOtoAKGMzMmIwNDYyNDNkY2JmMGRjZWI5NTJkYTEzMTcyNjExMDlhYzQ1YzQ",
      "commit": {
        "author": {
          "name": "Matthew Carruth",
          "email": "carruthm@gmail.com",
          "date": "2023-11-16T01:00:28Z"
        },
        "committer": {
          "name": "Matthew Carruth",
          "email": "carruthm@gmail.com",
          "date": "2023-11-16T01:00:28Z"
        },
        "message": "Fix missing space in error message",
        "tree": {
          "sha": "62895f252cf305dfa0f4e09ef684bc966ab34eea",
          "url": "https://api.github.com/repos/psf/requests/git/trees/62895f252cf305dfa0f4e09ef684bc966ab34eea"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/c32b046243dcbf0dceb952da1317261109ac45c4",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/c32b046243dcbf0dceb952da1317261109ac45c4",
      "html_url": "https://github.com/psf/requests/commit/c32b046243dcbf0dceb952da1317261109ac45c4",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/c32b046243dcbf0dceb952da1317261109ac45c4/comments",
      "author": {
        "login": "msea1",
        "id": 2788918,
        "node_id": "MDQ6VXNlcjI3ODg5MTg=",
        "avatar_url": "https://avatars.githubusercontent.com/u/2788918?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/msea1",
        "html_url": "https://github.com/msea1",
        "followers_url": "https://api.github.com/users/msea1/followers",
        "following_url": "https://api.github.com/users/msea1/following{/other_user}",
        "gists_url": "https://api.github.com/users/msea1/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/msea1/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/msea1/subscriptions",
        "organizations_url": "https://api.github.com/users/msea1/orgs",
        "repos_url": "https://api.github.com/users/msea1/repos",
        "events_url": "https://api.github.com/users/msea1/events{/privacy}",
        "received_events_url": "https://api.github.com/users/msea1/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "msea1",
        "id": 2788918,
        "node_id": "MDQ6VXNlcjI3ODg5MTg=",
        "avatar_url": "https://avatars.githubusercontent.com/u/2788918?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/msea1",
        "html_url": "https://github.com/msea1",
        "followers_url": "https://api.github.com/users/msea1/followers",
        "following_url": "https://api.github.com/users/msea1/following{/other_user}",
        "gists_url": "https://api.github.com/users/msea1/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/msea1/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/msea1/subscriptions",
        "organizations_url": "https://api.github.com/users/msea1/orgs",
        "repos_url": "https://api.github.com/users/msea1/repos",
        "events_url": "https://api.github.com/users/msea1/events{/privacy}",
        "received_events_url": "https://api.github.com/users/msea1/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "839a8edec37c81a18ac8332cfbd44f44e1ae6206",
          "url": "https://api.github.com/repos/psf/requests/commits/839a8edec37c81a18ac8332cfbd44f44e1ae6206",
          "html_url": "https://github.com/psf/requests/commit/839a8edec37c81a18ac8332cfbd44f44e1ae6206"
        }
      ]
    },
    {
      "sha": "9e98a8749a01c12c792833e0e3278763b06c4838",
      "node_id": "C_kwDOABTKOtoAKDllOThhODc0OWEwMWMxMmM3OTI4MzNlMGUzMjc4NzYzYjA2YzQ4Mzg",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2023-11-16T07:44:49Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-11-16T07:44:49Z"
        },
        "message": "Merge pull request #6574 from msea1/matthew/fix_space",
        "tree": {
          "sha": "62895f252cf305dfa0f4e09ef684bc966ab34eea",
          "url": "https://api.github.com/repos/psf/requests/git/trees/62895f252cf305dfa0f4e09ef684bc966ab34eea"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/9e98a8749a01c12c792833e0e3278763b06c4838",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlVchxCRBK7hj4Ov3rIwAAb+EIADWXLHWsPXmTxOpJi27UK8x1\nF2PpET+ldr4OJaGM9SdpPrMngf/5D0i2+y3X4bbGSDTwzMYt5xHjFCGGpr6X5apq\nndSgLc5nHBCeySZCBTUpQkVCBPs2hRD1LzQRZfaZC1Br5Gwqgb22Zvou0oI9jaIP\n2kC6wQzyzIEQ23hj+8DJcRWNrJI6zchd9EfXWSq9jmBWdkafBgSUsVu9YvCYIoeF\n0Zf/fjOS0Kn51A6KKy2hJxH98Wn53PfqlZGkQe4lBA7u55WyPgGQ6tihgA5M+lNx\nR47UhqTuXuwGSHJ8Cl536UqeUqpy2gpnBULu8D3Jd1kjGmOzEW/t/JzgOnHSilo=\n=qqqr\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 62895f252cf305dfa0f4e09ef684bc966ab34eea\nparent 839a8edec37c81a18ac8332cfbd44f44e1ae6206\nparent c32b046243dcbf0dceb952da1317261109ac45c4\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1700120689 -0800\ncommitter GitHub <noreply@github.com> 1700120689 -0800\n\nMerge pull request #6574 from msea1/matthew/fix_space\n\n",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/9e98a8749a01c12c792833e0e3278763b06c4838",
      "html_url": "https://github.com/psf/requests/commit/9e98a8749a01c12c792833e0e3278763b06c4838",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/9e98a8749a01c12c792833e0e3278763b06c4838/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "839a8edec37c81a18ac8332cfbd44f44e1ae6206",
          "url": "https://api.github.com/repos/psf/requests/commits/839a8edec37c81a18ac8332cfbd44f44e1ae6206",
          "html_url": "https://github.com/psf/requests/commit/839a8edec37c81a18ac8332cfbd44f44e1ae6206"
        },
        {
          "sha": "c32b046243dcbf0dceb952da1317261109ac45c4",
          "url": "https://api.github.com/repos/psf/requests/commits/c32b046243dcbf0dceb952da1317261109ac45c4",
          "html_url": "https://github.com/psf/requests/commit/c32b046243dcbf0dceb952da1317261109ac45c4"
        }
      ]
    },
    {
      "sha": "e66a07b28651ddeab4297fbf3a600cb42b21dfe6",
      "node_id": "C_kwDOABTKOtoAKGU2NmEwN2IyODY1MWRkZWFiNDI5N2ZiZjNhNjAwY2I0MmIyMWRmZTY",
      "commit": {
        "author": {
          "name": "dependabot[bot]",
          "email": "49699333+dependabot[bot]@users.noreply.github.com",
          "date": "2023-11-20T16:28:17Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-11-20T16:28:17Z"
        },
        "message": "Bump dessant/lock-threads from 4.0.1 to 5.0.0\n\nBumps [dessant/lock-threads](https://github.com/dessant/lock-threads) from 4.0.1 to 5.0.0.\n- [Release notes](https://github.com/dessant/lock-threads/releases)\n- [Changelog](https://github.com/dessant/lock-threads/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/dessant/lock-threads/compare/be8aa5be94131386884a6da4189effda9b14aa21...d42e5f49803f3c4e14ffee0378e31481265dda22)\n\n---\nupdated-dependencies:\n- dependency-name: dessant/lock-threads\n  dependency-type: direct:production\n  update-type: version-update:semver-major\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
        "tree": {
          "sha": "5b888c6266b54f85b76c4eac839b00bd7aa29efb",
          "url": "https://api.github.com/repos/psf/requests/git/trees/5b888c6266b54f85b76c4eac839b00bd7aa29efb"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/e66a07b28651ddeab4297fbf3a600cb42b21dfe6",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlW4khCRBK7hj4Ov3rIwAAjf4IAKrYjGgBIbs5sEpEewC4Zjf1\n0pIfjJSJOh7BKeuKTChPeTFK47xp25xC7xPTdr6ekuHvfWDEq6giTwTIQ5ORWJUC\nqJ7iVfTqMeIvIBACjKN9u/dv3Kf8swWERXcoaZROjKLCTzYfESXSgAAf4ETCVuyI\nHwEGHnrmP6+SR11D4p0b0smLSYsQMqRqNsB/R3lmB5QIiB9ThYiKbHChx0zjNqHl\nHxvpS0oFm9hVMMrOp3JHVpsB1omPC8NSvttCzPK4X7T31lJdeC3fEI1NbIDlF0vC\nJwfIcWn3uBD0R4cLbptKYBCtopGA078nLDsdpnEWokH2dhmNKMPWBqjBkCTGHtw=\n=utZf\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 5b888c6266b54f85b76c4eac839b00bd7aa29efb\nparent 9e98a8749a01c12c792833e0e3278763b06c4838\nauthor dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> 1700497697 +0000\ncommitter GitHub <noreply@github.com> 1700497697 +0000\n\nBump dessant/lock-threads from 4.0.1 to 5.0.0\n\nBumps [dessant/lock-threads](https://github.com/dessant/lock-threads) from 4.0.1 to 5.0.0.\n- [Release notes](https://github.com/dessant/lock-threads/releases)\n- [Changelog](https://github.com/dessant/lock-threads/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/dessant/lock-threads/compare/be8aa5be94131386884a6da4189effda9b14aa21...d42e5f49803f3c4e14ffee0378e31481265dda22)\n\n---\nupdated-dependencies:\n- dependency-name: dessant/lock-threads\n  dependency-type: direct:production\n  update-type: version-update:semver-major\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/e66a07b28651ddeab4297fbf3a600cb42b21dfe6",
      "html_url": "https://github.com/psf/requests/commit/e66a07b28651ddeab4297fbf3a600cb42b21dfe6",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/e66a07b28651ddeab4297fbf3a600cb42b21dfe6/comments",
      "author": {
        "login": "dependabot[bot]",
        "id": 49699333,
        "node_id": "MDM6Qm90NDk2OTkzMzM=",
        "avatar_url": "https://avatars.githubusercontent.com/in/29110?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/dependabot%5Bbot%5D",
        "html_url": "https://github.com/apps/dependabot",
        "followers_url": "https://api.github.com/users/dependabot%5Bbot%5D/followers",
        "following_url": "https://api.github.com/users/dependabot%5Bbot%5D/following{/other_user}",
        "gists_url": "https://api.github.com/users/dependabot%5Bbot%5D/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/dependabot%5Bbot%5D/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/dependabot%5Bbot%5D/subscriptions",
        "organizations_url": "https://api.github.com/users/dependabot%5Bbot%5D/orgs",
        "repos_url": "https://api.github.com/users/dependabot%5Bbot%5D/repos",
        "events_url": "https://api.github.com/users/dependabot%5Bbot%5D/events{/privacy}",
        "received_events_url": "https://api.github.com/users/dependabot%5Bbot%5D/received_events",
        "type": "Bot",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "9e98a8749a01c12c792833e0e3278763b06c4838",
          "url": "https://api.github.com/repos/psf/requests/commits/9e98a8749a01c12c792833e0e3278763b06c4838",
          "html_url": "https://github.com/psf/requests/commit/9e98a8749a01c12c792833e0e3278763b06c4838"
        }
      ]
    },
    {
      "sha": "c6de5a14e55588d2d3ff5726eaf92824ab1be4dc",
      "node_id": "C_kwDOABTKOtoAKGM2ZGU1YTE0ZTU1NTg4ZDJkM2ZmNTcyNmVhZjkyODI0YWIxYmU0ZGM",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2023-11-20T16:37:07Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-11-20T16:37:07Z"
        },
        "message": "Merge pull request #6580 from psf/dependabot/github_actions/dessant/lock-threads-5.0.0\n\nBump dessant/lock-threads from 4.0.1 to 5.0.0",
        "tree": {
          "sha": "5b888c6266b54f85b76c4eac839b00bd7aa29efb",
          "url": "https://api.github.com/repos/psf/requests/git/trees/5b888c6266b54f85b76c4eac839b00bd7aa29efb"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/c6de5a14e55588d2d3ff5726eaf92824ab1be4dc",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlW4szCRBK7hj4Ov3rIwAAXqYIAIrM+YgVc61sgdLsE9HgQqqq\nDlfj3TBlWhvmlGcqxoEjdT58tcmyY3pSeyFRfiFkBaP7xhRVggGR8VFgTI0nj/zf\nXGQXiznxkGlcBmqOQGOZaT5qa1xjGLrIiD+g1WaApWNUYRwfvYPrrrGo2Fzed5iF\nzOxjJ22wfX8FCgpa870QXugbgmDUmhI+jJ/SxvgqWiq/lT9eaoGrUo/ARvwJa68s\nbnE9opmLrgnm3kAA5+gs7lMv/FLLl6H/nxfNcvomObbLG+dKoaG44Mejc+p4NDKY\nSo2AZKdNXClVw2uk+3+o8pT/PHapTjnsQ1bQ6bvNKnTCsFnj3tvoPGf3bF8N7yw=\n=WUcO\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 5b888c6266b54f85b76c4eac839b00bd7aa29efb\nparent 9e98a8749a01c12c792833e0e3278763b06c4838\nparent e66a07b28651ddeab4297fbf3a600cb42b21dfe6\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1700498227 -0600\ncommitter GitHub <noreply@github.com> 1700498227 -0600\n\nMerge pull request #6580 from psf/dependabot/github_actions/dessant/lock-threads-5.0.0\n\nBump dessant/lock-threads from 4.0.1 to 5.0.0",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/c6de5a14e55588d2d3ff5726eaf92824ab1be4dc",
      "html_url": "https://github.com/psf/requests/commit/c6de5a14e55588d2d3ff5726eaf92824ab1be4dc",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/c6de5a14e55588d2d3ff5726eaf92824ab1be4dc/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "9e98a8749a01c12c792833e0e3278763b06c4838",
          "url": "https://api.github.com/repos/psf/requests/commits/9e98a8749a01c12c792833e0e3278763b06c4838",
          "html_url": "https://github.com/psf/requests/commit/9e98a8749a01c12c792833e0e3278763b06c4838"
        },
        {
          "sha": "e66a07b28651ddeab4297fbf3a600cb42b21dfe6",
          "url": "https://api.github.com/repos/psf/requests/commits/e66a07b28651ddeab4297fbf3a600cb42b21dfe6",
          "html_url": "https://github.com/psf/requests/commit/e66a07b28651ddeab4297fbf3a600cb42b21dfe6"
        }
      ]
    },
    {
      "sha": "15849947ec4b8b7c3c136a47e950499edfd36921",
      "node_id": "C_kwDOABTKOtoAKDE1ODQ5OTQ3ZWM0YjhiN2MzYzEzNmE0N2U5NTA0OTllZGZkMzY5MjE",
      "commit": {
        "author": {
          "name": "Elliot Ford",
          "email": "elliot.ford@astrazeneca.com",
          "date": "2023-11-22T11:31:53Z"
        },
        "committer": {
          "name": "Elliot Ford",
          "email": "elliot.ford@astrazeneca.com",
          "date": "2023-11-22T11:34:04Z"
        },
        "message": "fix docstring typo: a -> as",
        "tree": {
          "sha": "3477f30d0f9ebcaf5abfcfb0ceb3dd73765cfc59",
          "url": "https://api.github.com/repos/psf/requests/git/trees/3477f30d0f9ebcaf5abfcfb0ceb3dd73765cfc59"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/15849947ec4b8b7c3c136a47e950499edfd36921",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/15849947ec4b8b7c3c136a47e950499edfd36921",
      "html_url": "https://github.com/psf/requests/commit/15849947ec4b8b7c3c136a47e950499edfd36921",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/15849947ec4b8b7c3c136a47e950499edfd36921/comments",
      "author": {
        "login": "EFord36",
        "id": 20516159,
        "node_id": "MDQ6VXNlcjIwNTE2MTU5",
        "avatar_url": "https://avatars.githubusercontent.com/u/20516159?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/EFord36",
        "html_url": "https://github.com/EFord36",
        "followers_url": "https://api.github.com/users/EFord36/followers",
        "following_url": "https://api.github.com/users/EFord36/following{/other_user}",
        "gists_url": "https://api.github.com/users/EFord36/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/EFord36/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/EFord36/subscriptions",
        "organizations_url": "https://api.github.com/users/EFord36/orgs",
        "repos_url": "https://api.github.com/users/EFord36/repos",
        "events_url": "https://api.github.com/users/EFord36/events{/privacy}",
        "received_events_url": "https://api.github.com/users/EFord36/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "EFord36",
        "id": 20516159,
        "node_id": "MDQ6VXNlcjIwNTE2MTU5",
        "avatar_url": "https://avatars.githubusercontent.com/u/20516159?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/EFord36",
        "html_url": "https://github.com/EFord36",
        "followers_url": "https://api.github.com/users/EFord36/followers",
        "following_url": "https://api.github.com/users/EFord36/following{/other_user}",
        "gists_url": "https://api.github.com/users/EFord36/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/EFord36/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/EFord36/subscriptions",
        "organizations_url": "https://api.github.com/users/EFord36/orgs",
        "repos_url": "https://api.github.com/users/EFord36/repos",
        "events_url": "https://api.github.com/users/EFord36/events{/privacy}",
        "received_events_url": "https://api.github.com/users/EFord36/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "c6de5a14e55588d2d3ff5726eaf92824ab1be4dc",
          "url": "https://api.github.com/repos/psf/requests/commits/c6de5a14e55588d2d3ff5726eaf92824ab1be4dc",
          "html_url": "https://github.com/psf/requests/commit/c6de5a14e55588d2d3ff5726eaf92824ab1be4dc"
        }
      ]
    },
    {
      "sha": "0b4d494192de489701d3a2e32acef8fb5d3f042e",
      "node_id": "C_kwDOABTKOtoAKDBiNGQ0OTQxOTJkZTQ4OTcwMWQzYTJlMzJhY2VmOGZiNWQzZjA0MmU",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2023-11-22T15:10:47Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-11-22T15:10:47Z"
        },
        "message": "Merge pull request #6581 from EFord36/typo-fix\n\nfix docstring typo: a -> as",
        "tree": {
          "sha": "3477f30d0f9ebcaf5abfcfb0ceb3dd73765cfc59",
          "url": "https://api.github.com/repos/psf/requests/git/trees/3477f30d0f9ebcaf5abfcfb0ceb3dd73765cfc59"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/0b4d494192de489701d3a2e32acef8fb5d3f042e",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlXhn3CRBK7hj4Ov3rIwAAoIwIACvgNY/jDpm9MCsWJWY3Upwn\nGX78xtAnkmMidv2ZmEG/hIMPGHrhdXGSkxjo8c9zOn9bBwxKX51zuCcmgvA1h2AI\nG4a34v2xNC9ImR3LQkdftiNfsCYHYIlOPK7BC6graG5NgHu23/lUxLnKn7okKPVi\n4ZRNpXqO9ExcdHeg5Y7chlb+H/r/ZqWMz7ZK3uaVLC9sjeWdjd/OhofPGrAStM9r\nrFwS5wyQeTTokFg2pnRVMSOaFB8rbHYpnk2UcX55DdUaKLsmcMsHVGhr4fttXJbx\nprE7w9CHr9hckd1ll40tmvbCtnDKjBLiYXHMfH3buKNRUqmJbpnqGS+u1NO7CzE=\n=o1ie\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 3477f30d0f9ebcaf5abfcfb0ceb3dd73765cfc59\nparent c6de5a14e55588d2d3ff5726eaf92824ab1be4dc\nparent 15849947ec4b8b7c3c136a47e950499edfd36921\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1700665847 -0600\ncommitter GitHub <noreply@github.com> 1700665847 -0600\n\nMerge pull request #6581 from EFord36/typo-fix\n\nfix docstring typo: a -> as",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/0b4d494192de489701d3a2e32acef8fb5d3f042e",
      "html_url": "https://github.com/psf/requests/commit/0b4d494192de489701d3a2e32acef8fb5d3f042e",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/0b4d494192de489701d3a2e32acef8fb5d3f042e/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "c6de5a14e55588d2d3ff5726eaf92824ab1be4dc",
          "url": "https://api.github.com/repos/psf/requests/commits/c6de5a14e55588d2d3ff5726eaf92824ab1be4dc",
          "html_url": "https://github.com/psf/requests/commit/c6de5a14e55588d2d3ff5726eaf92824ab1be4dc"
        },
        {
          "sha": "15849947ec4b8b7c3c136a47e950499edfd36921",
          "url": "https://api.github.com/repos/psf/requests/commits/15849947ec4b8b7c3c136a47e950499edfd36921",
          "html_url": "https://github.com/psf/requests/commit/15849947ec4b8b7c3c136a47e950499edfd36921"
        }
      ]
    },
    {
      "sha": "f6707042d8b18d2a3737380bf58ff020872fb07b",
      "node_id": "C_kwDOABTKOtoAKGY2NzA3MDQyZDhiMThkMmEzNzM3MzgwYmY1OGZmMDIwODcyZmIwN2I",
      "commit": {
        "author": {
          "name": "Bruce Adams",
          "email": "bruce.adams@acm.org",
          "date": "2023-11-27T22:27:43Z"
        },
        "committer": {
          "name": "Bruce Adams",
          "email": "bruce.adams@acm.org",
          "date": "2023-11-27T22:27:43Z"
        },
        "message": "Unit test for string containing multi-byte UTF-8\n\nThere are two tests here. One demonstrating existing, correct\nbehavior for `data=bytes`, and another, failing, test for the case\nwhere `data=string` and the string contains multi-byte UTF-8.",
        "tree": {
          "sha": "7d908350e04173389174428fac0f09ec3558e0ce",
          "url": "https://api.github.com/repos/psf/requests/git/trees/7d908350e04173389174428fac0f09ec3558e0ce"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/f6707042d8b18d2a3737380bf58ff020872fb07b",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/f6707042d8b18d2a3737380bf58ff020872fb07b",
      "html_url": "https://github.com/psf/requests/commit/f6707042d8b18d2a3737380bf58ff020872fb07b",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/f6707042d8b18d2a3737380bf58ff020872fb07b/comments",
      "author": {
        "login": "bruceadams",
        "id": 225823,
        "node_id": "MDQ6VXNlcjIyNTgyMw==",
        "avatar_url": "https://avatars.githubusercontent.com/u/225823?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/bruceadams",
        "html_url": "https://github.com/bruceadams",
        "followers_url": "https://api.github.com/users/bruceadams/followers",
        "following_url": "https://api.github.com/users/bruceadams/following{/other_user}",
        "gists_url": "https://api.github.com/users/bruceadams/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/bruceadams/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/bruceadams/subscriptions",
        "organizations_url": "https://api.github.com/users/bruceadams/orgs",
        "repos_url": "https://api.github.com/users/bruceadams/repos",
        "events_url": "https://api.github.com/users/bruceadams/events{/privacy}",
        "received_events_url": "https://api.github.com/users/bruceadams/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "bruceadams",
        "id": 225823,
        "node_id": "MDQ6VXNlcjIyNTgyMw==",
        "avatar_url": "https://avatars.githubusercontent.com/u/225823?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/bruceadams",
        "html_url": "https://github.com/bruceadams",
        "followers_url": "https://api.github.com/users/bruceadams/followers",
        "following_url": "https://api.github.com/users/bruceadams/following{/other_user}",
        "gists_url": "https://api.github.com/users/bruceadams/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/bruceadams/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/bruceadams/subscriptions",
        "organizations_url": "https://api.github.com/users/bruceadams/orgs",
        "repos_url": "https://api.github.com/users/bruceadams/repos",
        "events_url": "https://api.github.com/users/bruceadams/events{/privacy}",
        "received_events_url": "https://api.github.com/users/bruceadams/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "0b4d494192de489701d3a2e32acef8fb5d3f042e",
          "url": "https://api.github.com/repos/psf/requests/commits/0b4d494192de489701d3a2e32acef8fb5d3f042e",
          "html_url": "https://github.com/psf/requests/commit/0b4d494192de489701d3a2e32acef8fb5d3f042e"
        }
      ]
    },
    {
      "sha": "b37878d3407995e41fd3c160fd04d5d0afda1130",
      "node_id": "C_kwDOABTKOtoAKGIzNzg3OGQzNDA3OTk1ZTQxZmQzYzE2MGZkMDRkNWQwYWZkYTExMzA",
      "commit": {
        "author": {
          "name": "Ata Tuzuner",
          "email": "atatuzuner61@gmail.com",
          "date": "2023-11-28T23:12:22Z"
        },
        "committer": {
          "name": "Ata Tuzuner",
          "email": "atatuzuner61@gmail.com",
          "date": "2023-11-28T23:12:22Z"
        },
        "message": "Too early definition added to 425 status code type",
        "tree": {
          "sha": "858e5cdc13ef9a028652597a033586df6ba2d06a",
          "url": "https://api.github.com/repos/psf/requests/git/trees/858e5cdc13ef9a028652597a033586df6ba2d06a"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/b37878d3407995e41fd3c160fd04d5d0afda1130",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/b37878d3407995e41fd3c160fd04d5d0afda1130",
      "html_url": "https://github.com/psf/requests/commit/b37878d3407995e41fd3c160fd04d5d0afda1130",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/b37878d3407995e41fd3c160fd04d5d0afda1130/comments",
      "author": {
        "login": "atatuzuner61",
        "id": 85669350,
        "node_id": "MDQ6VXNlcjg1NjY5MzUw",
        "avatar_url": "https://avatars.githubusercontent.com/u/85669350?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/atatuzuner61",
        "html_url": "https://github.com/atatuzuner61",
        "followers_url": "https://api.github.com/users/atatuzuner61/followers",
        "following_url": "https://api.github.com/users/atatuzuner61/following{/other_user}",
        "gists_url": "https://api.github.com/users/atatuzuner61/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/atatuzuner61/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/atatuzuner61/subscriptions",
        "organizations_url": "https://api.github.com/users/atatuzuner61/orgs",
        "repos_url": "https://api.github.com/users/atatuzuner61/repos",
        "events_url": "https://api.github.com/users/atatuzuner61/events{/privacy}",
        "received_events_url": "https://api.github.com/users/atatuzuner61/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "atatuzuner61",
        "id": 85669350,
        "node_id": "MDQ6VXNlcjg1NjY5MzUw",
        "avatar_url": "https://avatars.githubusercontent.com/u/85669350?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/atatuzuner61",
        "html_url": "https://github.com/atatuzuner61",
        "followers_url": "https://api.github.com/users/atatuzuner61/followers",
        "following_url": "https://api.github.com/users/atatuzuner61/following{/other_user}",
        "gists_url": "https://api.github.com/users/atatuzuner61/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/atatuzuner61/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/atatuzuner61/subscriptions",
        "organizations_url": "https://api.github.com/users/atatuzuner61/orgs",
        "repos_url": "https://api.github.com/users/atatuzuner61/repos",
        "events_url": "https://api.github.com/users/atatuzuner61/events{/privacy}",
        "received_events_url": "https://api.github.com/users/atatuzuner61/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "0b4d494192de489701d3a2e32acef8fb5d3f042e",
          "url": "https://api.github.com/repos/psf/requests/commits/0b4d494192de489701d3a2e32acef8fb5d3f042e",
          "html_url": "https://github.com/psf/requests/commit/0b4d494192de489701d3a2e32acef8fb5d3f042e"
        }
      ]
    },
    {
      "sha": "889910c77a9618dc59dd800c17913e2b1644cee3",
      "node_id": "C_kwDOABTKOtoAKDg4OTkxMGM3N2E5NjE4ZGM1OWRkODAwYzE3OTEzZTJiMTY0NGNlZTM",
      "commit": {
        "author": {
          "name": "Ata Tuzuner",
          "email": "atatuzuner61@gmail.com",
          "date": "2023-11-29T17:24:15Z"
        },
        "committer": {
          "name": "Ata Tuzuner",
          "email": "atatuzuner61@gmail.com",
          "date": "2023-11-29T17:24:15Z"
        },
        "message": "Added tests for status code 425 definitions.",
        "tree": {
          "sha": "666268d0f0ac304b5c2834feff63dac2c8b49f3c",
          "url": "https://api.github.com/repos/psf/requests/git/trees/666268d0f0ac304b5c2834feff63dac2c8b49f3c"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/889910c77a9618dc59dd800c17913e2b1644cee3",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/889910c77a9618dc59dd800c17913e2b1644cee3",
      "html_url": "https://github.com/psf/requests/commit/889910c77a9618dc59dd800c17913e2b1644cee3",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/889910c77a9618dc59dd800c17913e2b1644cee3/comments",
      "author": {
        "login": "atatuzuner61",
        "id": 85669350,
        "node_id": "MDQ6VXNlcjg1NjY5MzUw",
        "avatar_url": "https://avatars.githubusercontent.com/u/85669350?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/atatuzuner61",
        "html_url": "https://github.com/atatuzuner61",
        "followers_url": "https://api.github.com/users/atatuzuner61/followers",
        "following_url": "https://api.github.com/users/atatuzuner61/following{/other_user}",
        "gists_url": "https://api.github.com/users/atatuzuner61/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/atatuzuner61/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/atatuzuner61/subscriptions",
        "organizations_url": "https://api.github.com/users/atatuzuner61/orgs",
        "repos_url": "https://api.github.com/users/atatuzuner61/repos",
        "events_url": "https://api.github.com/users/atatuzuner61/events{/privacy}",
        "received_events_url": "https://api.github.com/users/atatuzuner61/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "atatuzuner61",
        "id": 85669350,
        "node_id": "MDQ6VXNlcjg1NjY5MzUw",
        "avatar_url": "https://avatars.githubusercontent.com/u/85669350?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/atatuzuner61",
        "html_url": "https://github.com/atatuzuner61",
        "followers_url": "https://api.github.com/users/atatuzuner61/followers",
        "following_url": "https://api.github.com/users/atatuzuner61/following{/other_user}",
        "gists_url": "https://api.github.com/users/atatuzuner61/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/atatuzuner61/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/atatuzuner61/subscriptions",
        "organizations_url": "https://api.github.com/users/atatuzuner61/orgs",
        "repos_url": "https://api.github.com/users/atatuzuner61/repos",
        "events_url": "https://api.github.com/users/atatuzuner61/events{/privacy}",
        "received_events_url": "https://api.github.com/users/atatuzuner61/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "b37878d3407995e41fd3c160fd04d5d0afda1130",
          "url": "https://api.github.com/repos/psf/requests/commits/b37878d3407995e41fd3c160fd04d5d0afda1130",
          "html_url": "https://github.com/psf/requests/commit/b37878d3407995e41fd3c160fd04d5d0afda1130"
        }
      ]
    },
    {
      "sha": "ec84f2c539d952499e0207849dfd3f73e2c11324",
      "node_id": "C_kwDOABTKOtoAKGVjODRmMmM1MzlkOTUyNDk5ZTAyMDc4NDlkZmQzZjczZTJjMTEzMjQ",
      "commit": {
        "author": {
          "name": "Ata Tuzuner",
          "email": "atatuzuner61@gmail.com",
          "date": "2023-11-29T17:27:18Z"
        },
        "committer": {
          "name": "Ata Tuzuner",
          "email": "atatuzuner61@gmail.com",
          "date": "2023-11-29T17:27:18Z"
        },
        "message": "Fixes to test",
        "tree": {
          "sha": "f3afc12a612e73dd39541888b14778c747da309b",
          "url": "https://api.github.com/repos/psf/requests/git/trees/f3afc12a612e73dd39541888b14778c747da309b"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/ec84f2c539d952499e0207849dfd3f73e2c11324",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/ec84f2c539d952499e0207849dfd3f73e2c11324",
      "html_url": "https://github.com/psf/requests/commit/ec84f2c539d952499e0207849dfd3f73e2c11324",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/ec84f2c539d952499e0207849dfd3f73e2c11324/comments",
      "author": {
        "login": "atatuzuner61",
        "id": 85669350,
        "node_id": "MDQ6VXNlcjg1NjY5MzUw",
        "avatar_url": "https://avatars.githubusercontent.com/u/85669350?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/atatuzuner61",
        "html_url": "https://github.com/atatuzuner61",
        "followers_url": "https://api.github.com/users/atatuzuner61/followers",
        "following_url": "https://api.github.com/users/atatuzuner61/following{/other_user}",
        "gists_url": "https://api.github.com/users/atatuzuner61/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/atatuzuner61/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/atatuzuner61/subscriptions",
        "organizations_url": "https://api.github.com/users/atatuzuner61/orgs",
        "repos_url": "https://api.github.com/users/atatuzuner61/repos",
        "events_url": "https://api.github.com/users/atatuzuner61/events{/privacy}",
        "received_events_url": "https://api.github.com/users/atatuzuner61/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "atatuzuner61",
        "id": 85669350,
        "node_id": "MDQ6VXNlcjg1NjY5MzUw",
        "avatar_url": "https://avatars.githubusercontent.com/u/85669350?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/atatuzuner61",
        "html_url": "https://github.com/atatuzuner61",
        "followers_url": "https://api.github.com/users/atatuzuner61/followers",
        "following_url": "https://api.github.com/users/atatuzuner61/following{/other_user}",
        "gists_url": "https://api.github.com/users/atatuzuner61/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/atatuzuner61/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/atatuzuner61/subscriptions",
        "organizations_url": "https://api.github.com/users/atatuzuner61/orgs",
        "repos_url": "https://api.github.com/users/atatuzuner61/repos",
        "events_url": "https://api.github.com/users/atatuzuner61/events{/privacy}",
        "received_events_url": "https://api.github.com/users/atatuzuner61/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "889910c77a9618dc59dd800c17913e2b1644cee3",
          "url": "https://api.github.com/repos/psf/requests/commits/889910c77a9618dc59dd800c17913e2b1644cee3",
          "html_url": "https://github.com/psf/requests/commit/889910c77a9618dc59dd800c17913e2b1644cee3"
        }
      ]
    },
    {
      "sha": "3fd309a5c14e4cfbd96bea6c8e71b4958fe090bb",
      "node_id": "C_kwDOABTKOtoAKDNmZDMwOWE1YzE0ZTRjZmJkOTZiZWE2YzhlNzFiNDk1OGZlMDkwYmI",
      "commit": {
        "author": {
          "name": "Bruce Adams",
          "email": "bruce.adams@acm.org",
          "date": "2023-11-28T18:17:49Z"
        },
        "committer": {
          "name": "Bruce Adams",
          "email": "bruce.adams@acm.org",
          "date": "2023-11-29T20:42:57Z"
        },
        "message": "Enhance `super_len` to count encoded bytes for str\n\nThis fixes issue #6586",
        "tree": {
          "sha": "3c8a8cce7c1f573e12ad8c601fa1ecf5590c11a1",
          "url": "https://api.github.com/repos/psf/requests/git/trees/3c8a8cce7c1f573e12ad8c601fa1ecf5590c11a1"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/3fd309a5c14e4cfbd96bea6c8e71b4958fe090bb",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/3fd309a5c14e4cfbd96bea6c8e71b4958fe090bb",
      "html_url": "https://github.com/psf/requests/commit/3fd309a5c14e4cfbd96bea6c8e71b4958fe090bb",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/3fd309a5c14e4cfbd96bea6c8e71b4958fe090bb/comments",
      "author": {
        "login": "bruceadams",
        "id": 225823,
        "node_id": "MDQ6VXNlcjIyNTgyMw==",
        "avatar_url": "https://avatars.githubusercontent.com/u/225823?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/bruceadams",
        "html_url": "https://github.com/bruceadams",
        "followers_url": "https://api.github.com/users/bruceadams/followers",
        "following_url": "https://api.github.com/users/bruceadams/following{/other_user}",
        "gists_url": "https://api.github.com/users/bruceadams/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/bruceadams/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/bruceadams/subscriptions",
        "organizations_url": "https://api.github.com/users/bruceadams/orgs",
        "repos_url": "https://api.github.com/users/bruceadams/repos",
        "events_url": "https://api.github.com/users/bruceadams/events{/privacy}",
        "received_events_url": "https://api.github.com/users/bruceadams/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "bruceadams",
        "id": 225823,
        "node_id": "MDQ6VXNlcjIyNTgyMw==",
        "avatar_url": "https://avatars.githubusercontent.com/u/225823?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/bruceadams",
        "html_url": "https://github.com/bruceadams",
        "followers_url": "https://api.github.com/users/bruceadams/followers",
        "following_url": "https://api.github.com/users/bruceadams/following{/other_user}",
        "gists_url": "https://api.github.com/users/bruceadams/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/bruceadams/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/bruceadams/subscriptions",
        "organizations_url": "https://api.github.com/users/bruceadams/orgs",
        "repos_url": "https://api.github.com/users/bruceadams/repos",
        "events_url": "https://api.github.com/users/bruceadams/events{/privacy}",
        "received_events_url": "https://api.github.com/users/bruceadams/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "f6707042d8b18d2a3737380bf58ff020872fb07b",
          "url": "https://api.github.com/repos/psf/requests/commits/f6707042d8b18d2a3737380bf58ff020872fb07b",
          "html_url": "https://github.com/psf/requests/commit/f6707042d8b18d2a3737380bf58ff020872fb07b"
        }
      ]
    },
    {
      "sha": "d6ffd868ee3730f4e5c7d1595da37e2027a93eb8",
      "node_id": "C_kwDOABTKOtoAKGQ2ZmZkODY4ZWUzNzMwZjRlNWM3ZDE1OTVkYTM3ZTIwMjdhOTNlYjg",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2023-12-01T14:05:59Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-12-01T14:05:59Z"
        },
        "message": "Update close-issues.yml\n\nI noticed the auto-labeling was working but not the auto-closing. Looking at recent actions runs I see that we need to specify the token even if we're not giving our own special token. See https://github.com/psf/requests/actions/runs/7057701782/job/19211845073#step:2:13 for additional context, namely\r\n\r\n```\r\n gh: To use GitHub CLI in a GitHub Actions workflow, set the GH_TOKEN environment variable. Example:\r\n  env:\r\n    GH_TOKEN: ${{ github.token }}\r\n```",
        "tree": {
          "sha": "d274e51a0956d2093f16fb479b98940625f590f9",
          "url": "https://api.github.com/repos/psf/requests/git/trees/d274e51a0956d2093f16fb479b98940625f590f9"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/d6ffd868ee3730f4e5c7d1595da37e2027a93eb8",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlaehHCRBK7hj4Ov3rIwAAOtMIAAvPG3IeYBM0qJkm2jEJvkQU\nYgLNaDK/d5/sT8VWkpSWq51BFmPj06MYpXedM+yK4tp7+RghZ0pbQGnMnTeVXKiq\n3hEEk8y1Z0RyMO0SP37P8p4oLlFSbV1Yj73bfSb8ubgv79t7MI2KK3Z+21nkmpN9\nI3Jm0Q+mxzQ5btRJyM49CIj8aa+1L4ZDKMvqArId4JfKBDCYPuhXrownxDKH685A\nPVCzioMaV0jD3RVi2eJOVBsoXRAry5caGHvUBV3hrGX6rC6pQU1s/lDbI8DtBOF7\nwMf2PxiG512zzinc7OP/kqFBxRs9/s719gpm7u++iOa4pW/DkmxdzIouOsr73RY=\n=a5k8\n-----END PGP SIGNATURE-----\n",
          "payload": "tree d274e51a0956d2093f16fb479b98940625f590f9\nparent 0b4d494192de489701d3a2e32acef8fb5d3f042e\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1701439559 -0600\ncommitter GitHub <noreply@github.com> 1701439559 -0600\n\nUpdate close-issues.yml\n\nI noticed the auto-labeling was working but not the auto-closing. Looking at recent actions runs I see that we need to specify the token even if we're not giving our own special token. See https://github.com/psf/requests/actions/runs/7057701782/job/19211845073#step:2:13 for additional context, namely\r\n\r\n```\r\n gh: To use GitHub CLI in a GitHub Actions workflow, set the GH_TOKEN environment variable. Example:\r\n  env:\r\n    GH_TOKEN: ${{ github.token }}\r\n```",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/d6ffd868ee3730f4e5c7d1595da37e2027a93eb8",
      "html_url": "https://github.com/psf/requests/commit/d6ffd868ee3730f4e5c7d1595da37e2027a93eb8",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/d6ffd868ee3730f4e5c7d1595da37e2027a93eb8/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "0b4d494192de489701d3a2e32acef8fb5d3f042e",
          "url": "https://api.github.com/repos/psf/requests/commits/0b4d494192de489701d3a2e32acef8fb5d3f042e",
          "html_url": "https://github.com/psf/requests/commit/0b4d494192de489701d3a2e32acef8fb5d3f042e"
        }
      ]
    },
    {
      "sha": "769bc3ae5cc8cb42242e4505b310dd10889cb54c",
      "node_id": "C_kwDOABTKOtoAKDc2OWJjM2FlNWNjOGNiNDIyNDJlNDUwNWIzMTBkZDEwODg5Y2I1NGM",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2023-12-01T17:18:02Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-12-01T17:18:02Z"
        },
        "message": "Merge pull request #6596 from psf/fix-autoclose-automtaion\n\nUpdate close-issues.yml",
        "tree": {
          "sha": "d274e51a0956d2093f16fb479b98940625f590f9",
          "url": "https://api.github.com/repos/psf/requests/git/trees/d274e51a0956d2093f16fb479b98940625f590f9"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/769bc3ae5cc8cb42242e4505b310dd10889cb54c",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlahVKCRBK7hj4Ov3rIwAARR0IAGumWwdz/YWQ+CiqPY2brMVJ\nXT5va1igRzeP56fzHMr/+hq8G82ddxoir4w+4Pb7Eu4XLIH5lWR5BMaNDFWnU7Po\nzJ8SQCQJMqEJ/FvylvhMnzVuKR+g0hPNeVZfdKbulRIf64qWc2Qi7aLZvYn6Eno5\nDUdjaRlxiJUkNmuIaJ8YP80q6QJ5Or4CNrRlKEAaaYsnwElZpasM9AjGffFOJlgK\njah9eNhBykZYcV8P3xsy74+IAgUoZjlt5+LEFXksxdM2KjPCVO5G/TtBbsXbdXGp\nmYj7smoLoJGaGvVnDcVpI8CecnMxei8L8cM4bvyrWAif6ZpW7YcVK8VInf3u1CI=\n=KhM+\n-----END PGP SIGNATURE-----\n",
          "payload": "tree d274e51a0956d2093f16fb479b98940625f590f9\nparent 0b4d494192de489701d3a2e32acef8fb5d3f042e\nparent d6ffd868ee3730f4e5c7d1595da37e2027a93eb8\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1701451082 -0800\ncommitter GitHub <noreply@github.com> 1701451082 -0800\n\nMerge pull request #6596 from psf/fix-autoclose-automtaion\n\nUpdate close-issues.yml",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/769bc3ae5cc8cb42242e4505b310dd10889cb54c",
      "html_url": "https://github.com/psf/requests/commit/769bc3ae5cc8cb42242e4505b310dd10889cb54c",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/769bc3ae5cc8cb42242e4505b310dd10889cb54c/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "0b4d494192de489701d3a2e32acef8fb5d3f042e",
          "url": "https://api.github.com/repos/psf/requests/commits/0b4d494192de489701d3a2e32acef8fb5d3f042e",
          "html_url": "https://github.com/psf/requests/commit/0b4d494192de489701d3a2e32acef8fb5d3f042e"
        },
        {
          "sha": "d6ffd868ee3730f4e5c7d1595da37e2027a93eb8",
          "url": "https://api.github.com/repos/psf/requests/commits/d6ffd868ee3730f4e5c7d1595da37e2027a93eb8",
          "html_url": "https://github.com/psf/requests/commit/d6ffd868ee3730f4e5c7d1595da37e2027a93eb8"
        }
      ]
    },
    {
      "sha": "ba67dc8dccd114faf8347e66c56baaa9d72f6429",
      "node_id": "C_kwDOABTKOtoAKGJhNjdkYzhkY2NkMTE0ZmFmODM0N2U2NmM1NmJhYWE5ZDcyZjY0Mjk",
      "commit": {
        "author": {
          "name": "dependabot[bot]",
          "email": "49699333+dependabot[bot]@users.noreply.github.com",
          "date": "2023-12-11T16:07:15Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-12-11T16:07:15Z"
        },
        "message": "Bump actions/setup-python from 4.7.0 to 5.0.0\n\nBumps [actions/setup-python](https://github.com/actions/setup-python) from 4.7.0 to 5.0.0.\n- [Release notes](https://github.com/actions/setup-python/releases)\n- [Commits](https://github.com/actions/setup-python/compare/61a6322f88396a6271a6ee3565807d608ecaddd1...0a5c61591373683505ea898e09a3ea4f39ef2b9c)\n\n---\nupdated-dependencies:\n- dependency-name: actions/setup-python\n  dependency-type: direct:production\n  update-type: version-update:semver-major\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
        "tree": {
          "sha": "7b544912d62fa2d94d60a463e9abaa60fb3910b7",
          "url": "https://api.github.com/repos/psf/requests/git/trees/7b544912d62fa2d94d60a463e9abaa60fb3910b7"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/ba67dc8dccd114faf8347e66c56baaa9d72f6429",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJldzOzCRBK7hj4Ov3rIwAATuEIAIftZnJYEXYO2rp2WyxhxUkJ\n5Pjai8EhyBGkFNDFd/pOZ60fi3bKTRl9BzCIm4qKaf+GC4gPmQIYp4kXrJbUBnEI\n2sTRN1gu++85HKxjCt3LcXwagSwsDZXKe4PBHCoEdVqOqPxivdoWLbF3J8Wxj+wy\nJ8rejE/k4cV8laOIVf+1liYOnA9u+yxUPYMOAO0cMdZrG/+6WztgmTiLyrlbrZTs\nCDpWceTHecbn9KsZbPqtj/oFbQzw1QQ7pXo9jLNDQgnVABxmAiK6IlGW2qFqcQ03\nh8CyUcFXLfP2ABmUyRbmVjGwFJIj8vo4t9WrSYtFyXiulhRUeoHYQut5Vr7hVp8=\n=Jxc3\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 7b544912d62fa2d94d60a463e9abaa60fb3910b7\nparent 769bc3ae5cc8cb42242e4505b310dd10889cb54c\nauthor dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> 1702310835 +0000\ncommitter GitHub <noreply@github.com> 1702310835 +0000\n\nBump actions/setup-python from 4.7.0 to 5.0.0\n\nBumps [actions/setup-python](https://github.com/actions/setup-python) from 4.7.0 to 5.0.0.\n- [Release notes](https://github.com/actions/setup-python/releases)\n- [Commits](https://github.com/actions/setup-python/compare/61a6322f88396a6271a6ee3565807d608ecaddd1...0a5c61591373683505ea898e09a3ea4f39ef2b9c)\n\n---\nupdated-dependencies:\n- dependency-name: actions/setup-python\n  dependency-type: direct:production\n  update-type: version-update:semver-major\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/ba67dc8dccd114faf8347e66c56baaa9d72f6429",
      "html_url": "https://github.com/psf/requests/commit/ba67dc8dccd114faf8347e66c56baaa9d72f6429",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/ba67dc8dccd114faf8347e66c56baaa9d72f6429/comments",
      "author": {
        "login": "dependabot[bot]",
        "id": 49699333,
        "node_id": "MDM6Qm90NDk2OTkzMzM=",
        "avatar_url": "https://avatars.githubusercontent.com/in/29110?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/dependabot%5Bbot%5D",
        "html_url": "https://github.com/apps/dependabot",
        "followers_url": "https://api.github.com/users/dependabot%5Bbot%5D/followers",
        "following_url": "https://api.github.com/users/dependabot%5Bbot%5D/following{/other_user}",
        "gists_url": "https://api.github.com/users/dependabot%5Bbot%5D/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/dependabot%5Bbot%5D/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/dependabot%5Bbot%5D/subscriptions",
        "organizations_url": "https://api.github.com/users/dependabot%5Bbot%5D/orgs",
        "repos_url": "https://api.github.com/users/dependabot%5Bbot%5D/repos",
        "events_url": "https://api.github.com/users/dependabot%5Bbot%5D/events{/privacy}",
        "received_events_url": "https://api.github.com/users/dependabot%5Bbot%5D/received_events",
        "type": "Bot",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "769bc3ae5cc8cb42242e4505b310dd10889cb54c",
          "url": "https://api.github.com/repos/psf/requests/commits/769bc3ae5cc8cb42242e4505b310dd10889cb54c",
          "html_url": "https://github.com/psf/requests/commit/769bc3ae5cc8cb42242e4505b310dd10889cb54c"
        }
      ]
    },
    {
      "sha": "a25fde6989f8df5c3d823bc9f2e2fc24aa71f375",
      "node_id": "C_kwDOABTKOtoAKGEyNWZkZTY5ODlmOGRmNWMzZDgyM2JjOWYyZTJmYzI0YWE3MWYzNzU",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2023-12-11T16:11:07Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-12-11T16:11:07Z"
        },
        "message": "Merge pull request #6599 from psf/dependabot/github_actions/actions/setup-python-5.0.0",
        "tree": {
          "sha": "7b544912d62fa2d94d60a463e9abaa60fb3910b7",
          "url": "https://api.github.com/repos/psf/requests/git/trees/7b544912d62fa2d94d60a463e9abaa60fb3910b7"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/a25fde6989f8df5c3d823bc9f2e2fc24aa71f375",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJldzSbCRBK7hj4Ov3rIwAAYv4IAAMfsNi/nieGmZEEZX6BuI0O\nEzjwBPv597u+QfGckLXQ6XbyKiajovOgsxbF8niMndvRE6a1rptZf07qoeWYydvS\n4cTADKktbXDy9FzX+jWAsmw2sRjWZfwT4W6yM1u/FCAk/eagJGpjwq7p3A9rs82Y\nZz0JuS8N70WKgG9D75/JhtMAfK8a/BctSLXuT2doaw+0xD8PHfigpinhUi51vod2\nukpvJuz/8ldVphPRwHA6/j8Z3sXuk+2Wop5EGgdvsntFQ3SreU71zJh0qo+AU/vu\nTMLOT0Ae91i7qXkIC2y7pRpevvO2PIgDXTxf534/BMN1zqoG8zoZnl9/HLDAT+I=\n=fXvf\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 7b544912d62fa2d94d60a463e9abaa60fb3910b7\nparent 769bc3ae5cc8cb42242e4505b310dd10889cb54c\nparent ba67dc8dccd114faf8347e66c56baaa9d72f6429\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1702311067 -0800\ncommitter GitHub <noreply@github.com> 1702311067 -0800\n\nMerge pull request #6599 from psf/dependabot/github_actions/actions/setup-python-5.0.0\n\n",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/a25fde6989f8df5c3d823bc9f2e2fc24aa71f375",
      "html_url": "https://github.com/psf/requests/commit/a25fde6989f8df5c3d823bc9f2e2fc24aa71f375",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/a25fde6989f8df5c3d823bc9f2e2fc24aa71f375/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "769bc3ae5cc8cb42242e4505b310dd10889cb54c",
          "url": "https://api.github.com/repos/psf/requests/commits/769bc3ae5cc8cb42242e4505b310dd10889cb54c",
          "html_url": "https://github.com/psf/requests/commit/769bc3ae5cc8cb42242e4505b310dd10889cb54c"
        },
        {
          "sha": "ba67dc8dccd114faf8347e66c56baaa9d72f6429",
          "url": "https://api.github.com/repos/psf/requests/commits/ba67dc8dccd114faf8347e66c56baaa9d72f6429",
          "html_url": "https://github.com/psf/requests/commit/ba67dc8dccd114faf8347e66c56baaa9d72f6429"
        }
      ]
    },
    {
      "sha": "a64f32ba453bc19aa679018838bee8ef8cc9a68b",
      "node_id": "C_kwDOABTKOtoAKGE2NGYzMmJhNDUzYmMxOWFhNjc5MDE4ODM4YmVlOGVmOGNjOWE2OGI",
      "commit": {
        "author": {
          "name": "Rodrigo Silva",
          "email": "github@rodrigosilva.com",
          "date": "2023-12-13T13:05:12Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-12-13T13:05:12Z"
        },
        "message": "Add note on connection timeout being larger than specified. Fix #5773\n\nOn servers with multiple IPs, such as IPv4 and IPv6, `urllib3` tries each address sequentially until one successfully connects, using the specified timeout for _each_ attempt, leading to a total connection timeout that is a _multiple_ of the requested time.",
        "tree": {
          "sha": "75685bf51d44b790a4ed7dc8cb3420163b70b958",
          "url": "https://api.github.com/repos/psf/requests/git/trees/75685bf51d44b790a4ed7dc8cb3420163b70b958"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/a64f32ba453bc19aa679018838bee8ef8cc9a68b",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJleawJCRBK7hj4Ov3rIwAA7MwIACVfZ/w/xIZl+BBuuInltO2Y\nw3eL69BYqBWoJ5iH83k1+AbAvf9y+iCr+w3yQJ+irS0oHLp4YdMI7k9ef8sglxfE\njHfM/QGeCf4pVaYpQsugjDsdE/96oEEzRGWuuOB5x/QjbD/i3w++o+osfolcyk2H\nsd2KQBi1am4Sd4ZsMQu3Wmqw90knKjBT1XyxNyBG/KBvHD/LMVqWNivZ1vjGS08U\n8kV2QCVbK9F1vhbqwf7QsHUg7mz59uZaWzPIlDwhbiUsk22I4K1F7dPrDBzX8QyM\nUcchHnZsYyrT0OWoG4OKMMyHEirnOgjPMAEtnPTDQYrqvWszRgQ5B20XpwzZIAM=\n=Zy7h\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 75685bf51d44b790a4ed7dc8cb3420163b70b958\nparent a25fde6989f8df5c3d823bc9f2e2fc24aa71f375\nauthor Rodrigo Silva <github@rodrigosilva.com> 1702472712 -0300\ncommitter GitHub <noreply@github.com> 1702472712 -0300\n\nAdd note on connection timeout being larger than specified. Fix #5773\n\nOn servers with multiple IPs, such as IPv4 and IPv6, `urllib3` tries each address sequentially until one successfully connects, using the specified timeout for _each_ attempt, leading to a total connection timeout that is a _multiple_ of the requested time.",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/a64f32ba453bc19aa679018838bee8ef8cc9a68b",
      "html_url": "https://github.com/psf/requests/commit/a64f32ba453bc19aa679018838bee8ef8cc9a68b",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/a64f32ba453bc19aa679018838bee8ef8cc9a68b/comments",
      "author": {
        "login": "MestreLion",
        "id": 992317,
        "node_id": "MDQ6VXNlcjk5MjMxNw==",
        "avatar_url": "https://avatars.githubusercontent.com/u/992317?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/MestreLion",
        "html_url": "https://github.com/MestreLion",
        "followers_url": "https://api.github.com/users/MestreLion/followers",
        "following_url": "https://api.github.com/users/MestreLion/following{/other_user}",
        "gists_url": "https://api.github.com/users/MestreLion/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/MestreLion/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/MestreLion/subscriptions",
        "organizations_url": "https://api.github.com/users/MestreLion/orgs",
        "repos_url": "https://api.github.com/users/MestreLion/repos",
        "events_url": "https://api.github.com/users/MestreLion/events{/privacy}",
        "received_events_url": "https://api.github.com/users/MestreLion/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "a25fde6989f8df5c3d823bc9f2e2fc24aa71f375",
          "url": "https://api.github.com/repos/psf/requests/commits/a25fde6989f8df5c3d823bc9f2e2fc24aa71f375",
          "html_url": "https://github.com/psf/requests/commit/a25fde6989f8df5c3d823bc9f2e2fc24aa71f375"
        }
      ]
    },
    {
      "sha": "c7c2ebf1a7b4b0f4149b3935b781e1392015e2d6",
      "node_id": "C_kwDOABTKOtoAKGM3YzJlYmYxYTdiNGIwZjQxNDliMzkzNWI3ODFlMTM5MjAxNWUyZDY",
      "commit": {
        "author": {
          "name": "Nicola Soranzo",
          "email": "nicola.soranzo@earlham.ac.uk",
          "date": "2023-12-15T20:59:51Z"
        },
        "committer": {
          "name": "Nicola Soranzo",
          "email": "nicola.soranzo@earlham.ac.uk",
          "date": "2023-12-15T20:59:56Z"
        },
        "message": "Add now mandatory readthedocs config file\n\nDocs builds currently fail with:\n\n```\nProblem in your project's configuration. No default configuration file found at repository's root. See https://docs.readthedocs.io/en/stable/config-file/\n```\n\nSee e.g. https://readthedocs.org/projects/requests/builds/22842479/",
        "tree": {
          "sha": "1a33c3e8591382435ecaa7c11d41f3bcd4a34157",
          "url": "https://api.github.com/repos/psf/requests/git/trees/1a33c3e8591382435ecaa7c11d41f3bcd4a34157"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/c7c2ebf1a7b4b0f4149b3935b781e1392015e2d6",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/c7c2ebf1a7b4b0f4149b3935b781e1392015e2d6",
      "html_url": "https://github.com/psf/requests/commit/c7c2ebf1a7b4b0f4149b3935b781e1392015e2d6",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/c7c2ebf1a7b4b0f4149b3935b781e1392015e2d6/comments",
      "author": {
        "login": "nsoranzo",
        "id": 4924623,
        "node_id": "MDQ6VXNlcjQ5MjQ2MjM=",
        "avatar_url": "https://avatars.githubusercontent.com/u/4924623?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nsoranzo",
        "html_url": "https://github.com/nsoranzo",
        "followers_url": "https://api.github.com/users/nsoranzo/followers",
        "following_url": "https://api.github.com/users/nsoranzo/following{/other_user}",
        "gists_url": "https://api.github.com/users/nsoranzo/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nsoranzo/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nsoranzo/subscriptions",
        "organizations_url": "https://api.github.com/users/nsoranzo/orgs",
        "repos_url": "https://api.github.com/users/nsoranzo/repos",
        "events_url": "https://api.github.com/users/nsoranzo/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nsoranzo/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "nsoranzo",
        "id": 4924623,
        "node_id": "MDQ6VXNlcjQ5MjQ2MjM=",
        "avatar_url": "https://avatars.githubusercontent.com/u/4924623?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nsoranzo",
        "html_url": "https://github.com/nsoranzo",
        "followers_url": "https://api.github.com/users/nsoranzo/followers",
        "following_url": "https://api.github.com/users/nsoranzo/following{/other_user}",
        "gists_url": "https://api.github.com/users/nsoranzo/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nsoranzo/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nsoranzo/subscriptions",
        "organizations_url": "https://api.github.com/users/nsoranzo/orgs",
        "repos_url": "https://api.github.com/users/nsoranzo/repos",
        "events_url": "https://api.github.com/users/nsoranzo/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nsoranzo/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "a25fde6989f8df5c3d823bc9f2e2fc24aa71f375",
          "url": "https://api.github.com/repos/psf/requests/commits/a25fde6989f8df5c3d823bc9f2e2fc24aa71f375",
          "html_url": "https://github.com/psf/requests/commit/a25fde6989f8df5c3d823bc9f2e2fc24aa71f375"
        }
      ]
    },
    {
      "sha": "51d0d83eaf7cd82526443424f61f7b5cfad82cde",
      "node_id": "C_kwDOABTKOtoAKDUxZDBkODNlYWY3Y2Q4MjUyNjQ0MzQyNGY2MWY3YjVjZmFkODJjZGU",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2023-12-16T13:24:37Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-12-16T13:24:37Z"
        },
        "message": "Merge pull request #6603 from nsoranzo/rtd_config\n\nAdd now mandatory readthedocs config file",
        "tree": {
          "sha": "1a33c3e8591382435ecaa7c11d41f3bcd4a34157",
          "url": "https://api.github.com/repos/psf/requests/git/trees/1a33c3e8591382435ecaa7c11d41f3bcd4a34157"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/51d0d83eaf7cd82526443424f61f7b5cfad82cde",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlfaUVCRBK7hj4Ov3rIwAAjkoIABCmd+i55+aVc58wkavnywk7\nBGpvFlrF81elyJIFi1CRy2uZ2EQDbCVmDdUy5Wvr5FFX+FlS7+rvN5P+Nf6+ahot\nXRgfDDuORJE199rUIiY7j+Sg00mkD6px3CNQmuY8aPVqUkpaLoRnEB1Vz4doEBCF\nQ7hvtyXo0B4to0q0iCkT0ipRVAu0rdgDLeBGQRHmA9lgsLjV6L2pGUrIyQ1TWs1X\nRQtmWArLI9PZ8zT368CS9V33KDtzTPb2yYgNYvUN4x1m+lQrLjcJ0ZHMKHv61sA7\n4NQYHDUXNn+rlT8CARiMpa4EXzwKGUmGjts6AOXoAqGeQL6EhXg3MXLgVEGoN9A=\n=yVQb\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 1a33c3e8591382435ecaa7c11d41f3bcd4a34157\nparent a25fde6989f8df5c3d823bc9f2e2fc24aa71f375\nparent c7c2ebf1a7b4b0f4149b3935b781e1392015e2d6\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1702733077 -0600\ncommitter GitHub <noreply@github.com> 1702733077 -0600\n\nMerge pull request #6603 from nsoranzo/rtd_config\n\nAdd now mandatory readthedocs config file",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/51d0d83eaf7cd82526443424f61f7b5cfad82cde",
      "html_url": "https://github.com/psf/requests/commit/51d0d83eaf7cd82526443424f61f7b5cfad82cde",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/51d0d83eaf7cd82526443424f61f7b5cfad82cde/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "a25fde6989f8df5c3d823bc9f2e2fc24aa71f375",
          "url": "https://api.github.com/repos/psf/requests/commits/a25fde6989f8df5c3d823bc9f2e2fc24aa71f375",
          "html_url": "https://github.com/psf/requests/commit/a25fde6989f8df5c3d823bc9f2e2fc24aa71f375"
        },
        {
          "sha": "c7c2ebf1a7b4b0f4149b3935b781e1392015e2d6",
          "url": "https://api.github.com/repos/psf/requests/commits/c7c2ebf1a7b4b0f4149b3935b781e1392015e2d6",
          "html_url": "https://github.com/psf/requests/commit/c7c2ebf1a7b4b0f4149b3935b781e1392015e2d6"
        }
      ]
    },
    {
      "sha": "951dd15fa619b23aba6b72532f1aac30b69389b7",
      "node_id": "C_kwDOABTKOtoAKDk1MWRkMTVmYTYxOWIyM2FiYTZiNzI1MzJmMWFhYzMwYjY5Mzg5Yjc",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2023-12-16T13:26:23Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-12-16T13:26:23Z"
        },
        "message": "Update docs/user/advanced.rst\r\n\r\nfix indentation for note so it renders properly",
        "tree": {
          "sha": "3b52c412d402071088a9215fd242877958e211af",
          "url": "https://api.github.com/repos/psf/requests/git/trees/3b52c412d402071088a9215fd242877958e211af"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/951dd15fa619b23aba6b72532f1aac30b69389b7",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlfaV/CRBK7hj4Ov3rIwAADq0IAJx9jV/CCiQDoiXjxqxBMWGK\nnJmxhY0yJzKdltPTlFJkhElDhQv7pOqkCsTITFxSIVhyqEkyZ4dfrkLtbNiz2hjB\n+y3sl/RPq9eWUbFw/H8qhjqDVEe8q2WBtFERKsbHPOT8H9FYNRcGnMKzMKdle/Lg\nAyLPG8v/YT/Bh7xwlHlAyWkmfMR0dVbNAfe52RTgffMDPOmUPiFvuUxjWffFcfrC\nAVKF/+0bcStS2dmmjVC8s4eDK1xHS4bT52tuCKaachC0anYY19sGA+wrkAX+svd2\n6jzgHTMQSGvsabswhN7qfPdiqQgAndJv4YHEZwMvrL1bdbDIOYyfAqzspZWIqmI=\n=N3p0\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 3b52c412d402071088a9215fd242877958e211af\nparent a64f32ba453bc19aa679018838bee8ef8cc9a68b\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1702733183 -0600\ncommitter GitHub <noreply@github.com> 1702733183 -0600\n\nUpdate docs/user/advanced.rst\r\n\r\nfix indentation for note so it renders properly",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/951dd15fa619b23aba6b72532f1aac30b69389b7",
      "html_url": "https://github.com/psf/requests/commit/951dd15fa619b23aba6b72532f1aac30b69389b7",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/951dd15fa619b23aba6b72532f1aac30b69389b7/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "a64f32ba453bc19aa679018838bee8ef8cc9a68b",
          "url": "https://api.github.com/repos/psf/requests/commits/a64f32ba453bc19aa679018838bee8ef8cc9a68b",
          "html_url": "https://github.com/psf/requests/commit/a64f32ba453bc19aa679018838bee8ef8cc9a68b"
        }
      ]
    },
    {
      "sha": "92f9e431c99d5e0776a00c10a90dfdf11cd45ba0",
      "node_id": "C_kwDOABTKOtoAKDkyZjllNDMxYzk5ZDVlMDc3NmEwMGMxMGE5MGRmZGYxMWNkNDViYTA",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2023-12-16T13:29:50Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-12-16T13:29:50Z"
        },
        "message": "Update docs/user/advanced.rst\r\n\r\nAdd note about wall clock too",
        "tree": {
          "sha": "c459cd3a6adf183ce7a3885681276a5daf3d267e",
          "url": "https://api.github.com/repos/psf/requests/git/trees/c459cd3a6adf183ce7a3885681276a5daf3d267e"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/92f9e431c99d5e0776a00c10a90dfdf11cd45ba0",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlfaZOCRBK7hj4Ov3rIwAAxicIALB1HkwqNZZi56oKiDR5jiF/\nTq/QYx8+zyVBI4KBh0NgVigPSjWT6hHniMXPMAfI7rAiCqTw+Km3G42SMsile0W9\nWavZaPt0cy76tdSsnNGaBGLzTg8AQuj29eHaPDPqHzf8kaSKtVJzSXNOTDLsyKz4\nr60LjTnessCY1K3ualJRe48bEnM0lYWImUe+xHX62fFe03Sx7mMT11DKo6O3SS68\naqEdY7uUULiinuTlZyC0yrXfGKRVB18ca6qQsYnfu3HZGSNyZ81yfXQx4Fc40CyH\ni3PieWKRtlaFPotdjYtdWqNh4PQwKjhCf5I/jK89y3j6hbbkSPNn9XeAqyyQs4w=\n=2qfn\n-----END PGP SIGNATURE-----\n",
          "payload": "tree c459cd3a6adf183ce7a3885681276a5daf3d267e\nparent 951dd15fa619b23aba6b72532f1aac30b69389b7\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1702733390 -0600\ncommitter GitHub <noreply@github.com> 1702733390 -0600\n\nUpdate docs/user/advanced.rst\r\n\r\nAdd note about wall clock too",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/92f9e431c99d5e0776a00c10a90dfdf11cd45ba0",
      "html_url": "https://github.com/psf/requests/commit/92f9e431c99d5e0776a00c10a90dfdf11cd45ba0",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/92f9e431c99d5e0776a00c10a90dfdf11cd45ba0/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "951dd15fa619b23aba6b72532f1aac30b69389b7",
          "url": "https://api.github.com/repos/psf/requests/commits/951dd15fa619b23aba6b72532f1aac30b69389b7",
          "html_url": "https://github.com/psf/requests/commit/951dd15fa619b23aba6b72532f1aac30b69389b7"
        }
      ]
    },
    {
      "sha": "1ddf014f477c322197400c365aef9fab56e25e40",
      "node_id": "C_kwDOABTKOtoAKDFkZGYwMTRmNDc3YzMyMjE5NzQwMGMzNjVhZWY5ZmFiNTZlMjVlNDA",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2023-12-16T13:30:18Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-12-16T13:30:18Z"
        },
        "message": "Merge pull request #6600 from MestreLion/MestreLion-connection-timeout-note\n\nAdd note on connection timeout being larger than specified. Fix #5773",
        "tree": {
          "sha": "97b576aa001a59f5ae04b373dfc5050214ed1014",
          "url": "https://api.github.com/repos/psf/requests/git/trees/97b576aa001a59f5ae04b373dfc5050214ed1014"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/1ddf014f477c322197400c365aef9fab56e25e40",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlfaZqCRBK7hj4Ov3rIwAA8QsIAIS7oQl+nwZYQHtMdiNYuqic\nwXwp2zkHf6egtrkk0hInjtTZjkEyyy6OFSNZahKJHEuIFHfmaak3BWI8TfOFbHkf\n8Ls9kIEDhGw85oekqN1qTxef5LKeh104X/HTEkQnfJ93Ca0me9xaY1HODPrdZ7Wm\nDIwZDWY1WTx5M8GPFNPYRMxDcXhHDrFvW8A7XMQ/3pB1Mgfsyb0i6nS/fK+YA5dv\nJId+R49bP6mASFohP4odJ4oiTNXJoYF2FPFfYFCCpu08+AkanKMdJCP1Pua2Yo14\nheegIbjFuZkawCQik+HzAzL+mLW2TMCEdBA5KMQzGoSuRir4RKfr3k/jyFuHRtI=\n=soLw\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 97b576aa001a59f5ae04b373dfc5050214ed1014\nparent 51d0d83eaf7cd82526443424f61f7b5cfad82cde\nparent 92f9e431c99d5e0776a00c10a90dfdf11cd45ba0\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1702733418 -0600\ncommitter GitHub <noreply@github.com> 1702733418 -0600\n\nMerge pull request #6600 from MestreLion/MestreLion-connection-timeout-note\n\nAdd note on connection timeout being larger than specified. Fix #5773",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/1ddf014f477c322197400c365aef9fab56e25e40",
      "html_url": "https://github.com/psf/requests/commit/1ddf014f477c322197400c365aef9fab56e25e40",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/1ddf014f477c322197400c365aef9fab56e25e40/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "51d0d83eaf7cd82526443424f61f7b5cfad82cde",
          "url": "https://api.github.com/repos/psf/requests/commits/51d0d83eaf7cd82526443424f61f7b5cfad82cde",
          "html_url": "https://github.com/psf/requests/commit/51d0d83eaf7cd82526443424f61f7b5cfad82cde"
        },
        {
          "sha": "92f9e431c99d5e0776a00c10a90dfdf11cd45ba0",
          "url": "https://api.github.com/repos/psf/requests/commits/92f9e431c99d5e0776a00c10a90dfdf11cd45ba0",
          "html_url": "https://github.com/psf/requests/commit/92f9e431c99d5e0776a00c10a90dfdf11cd45ba0"
        }
      ]
    },
    {
      "sha": "3b5978fc5d1c121d70e83ddf59379cf36418b4ce",
      "node_id": "C_kwDOABTKOtoAKDNiNTk3OGZjNWQxYzEyMWQ3MGU4M2RkZjU5Mzc5Y2YzNjQxOGI0Y2U",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2023-12-16T20:24:02Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-12-16T20:24:02Z"
        },
        "message": "Merge pull request #6592 from atatuzuner61/bug/6584\n\n\"TOO_EARLY\" type definition for status code 425",
        "tree": {
          "sha": "7500aafdb15cda1c553c3b104db6ace7ad8f24d5",
          "url": "https://api.github.com/repos/psf/requests/git/trees/7500aafdb15cda1c553c3b104db6ace7ad8f24d5"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/3b5978fc5d1c121d70e83ddf59379cf36418b4ce",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlfgdiCRBK7hj4Ov3rIwAAqLwIAJS4xHusyO+VzjaVmX0DM0M7\nftnSl6xEymLDaiOJtWOVflwkDO+5ZatgMJFI6LUiNP+NiQjOH/ZZ41YHdpVwlq33\nSkZm5MG6xjJE6hM5Zl1P6xC2KaaSdz6AmW7jUkKi6W4AgOoUD9AFtFyxvBw0bHAV\nqpPX7jbOMH7ISHNg+vDFqjDAsASZEB1F3xj+TfWmJJbXccOGxVRxqHeqKophRy/v\nRuJ7iXJwaZl9pUv/YRR7uuoYUIUhZaqNSjuC4xPRb6p+S9mP2wPqbsSWeR6y216Z\nOdHAsLfX5eOSCprKDIlSsG6rWvH/PMOrDfdTBo2NhjxpRWu7aZotjM1XECKIcbA=\n=A2+p\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 7500aafdb15cda1c553c3b104db6ace7ad8f24d5\nparent 1ddf014f477c322197400c365aef9fab56e25e40\nparent ec84f2c539d952499e0207849dfd3f73e2c11324\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1702758242 -0600\ncommitter GitHub <noreply@github.com> 1702758242 -0600\n\nMerge pull request #6592 from atatuzuner61/bug/6584\n\n\"TOO_EARLY\" type definition for status code 425",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/3b5978fc5d1c121d70e83ddf59379cf36418b4ce",
      "html_url": "https://github.com/psf/requests/commit/3b5978fc5d1c121d70e83ddf59379cf36418b4ce",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/3b5978fc5d1c121d70e83ddf59379cf36418b4ce/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "1ddf014f477c322197400c365aef9fab56e25e40",
          "url": "https://api.github.com/repos/psf/requests/commits/1ddf014f477c322197400c365aef9fab56e25e40",
          "html_url": "https://github.com/psf/requests/commit/1ddf014f477c322197400c365aef9fab56e25e40"
        },
        {
          "sha": "ec84f2c539d952499e0207849dfd3f73e2c11324",
          "url": "https://api.github.com/repos/psf/requests/commits/ec84f2c539d952499e0207849dfd3f73e2c11324",
          "html_url": "https://github.com/psf/requests/commit/ec84f2c539d952499e0207849dfd3f73e2c11324"
        }
      ]
    },
    {
      "sha": "1447bccc057e7fbffdfecd75cd4922702489a14b",
      "node_id": "C_kwDOABTKOtoAKDE0NDdiY2NjMDU3ZTdmYmZmZGZlY2Q3NWNkNDkyMjcwMjQ4OWExNGI",
      "commit": {
        "author": {
          "name": "Jaikish Pai",
          "email": "jkshpai@gmail.com",
          "date": "2023-12-17T21:34:30Z"
        },
        "committer": {
          "name": "Jaikish Pai",
          "email": "jkshpai@gmail.com",
          "date": "2023-12-17T21:34:30Z"
        },
        "message": "fix for ##6604",
        "tree": {
          "sha": "5d1456217b43a7303b173e97b5b43537736b0c3b",
          "url": "https://api.github.com/repos/psf/requests/git/trees/5d1456217b43a7303b173e97b5b43537736b0c3b"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/1447bccc057e7fbffdfecd75cd4922702489a14b",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/1447bccc057e7fbffdfecd75cd4922702489a14b",
      "html_url": "https://github.com/psf/requests/commit/1447bccc057e7fbffdfecd75cd4922702489a14b",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/1447bccc057e7fbffdfecd75cd4922702489a14b/comments",
      "author": {
        "login": "jaikishpai",
        "id": 35526514,
        "node_id": "MDQ6VXNlcjM1NTI2NTE0",
        "avatar_url": "https://avatars.githubusercontent.com/u/35526514?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/jaikishpai",
        "html_url": "https://github.com/jaikishpai",
        "followers_url": "https://api.github.com/users/jaikishpai/followers",
        "following_url": "https://api.github.com/users/jaikishpai/following{/other_user}",
        "gists_url": "https://api.github.com/users/jaikishpai/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/jaikishpai/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/jaikishpai/subscriptions",
        "organizations_url": "https://api.github.com/users/jaikishpai/orgs",
        "repos_url": "https://api.github.com/users/jaikishpai/repos",
        "events_url": "https://api.github.com/users/jaikishpai/events{/privacy}",
        "received_events_url": "https://api.github.com/users/jaikishpai/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "jaikishpai",
        "id": 35526514,
        "node_id": "MDQ6VXNlcjM1NTI2NTE0",
        "avatar_url": "https://avatars.githubusercontent.com/u/35526514?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/jaikishpai",
        "html_url": "https://github.com/jaikishpai",
        "followers_url": "https://api.github.com/users/jaikishpai/followers",
        "following_url": "https://api.github.com/users/jaikishpai/following{/other_user}",
        "gists_url": "https://api.github.com/users/jaikishpai/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/jaikishpai/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/jaikishpai/subscriptions",
        "organizations_url": "https://api.github.com/users/jaikishpai/orgs",
        "repos_url": "https://api.github.com/users/jaikishpai/repos",
        "events_url": "https://api.github.com/users/jaikishpai/events{/privacy}",
        "received_events_url": "https://api.github.com/users/jaikishpai/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "3b5978fc5d1c121d70e83ddf59379cf36418b4ce",
          "url": "https://api.github.com/repos/psf/requests/commits/3b5978fc5d1c121d70e83ddf59379cf36418b4ce",
          "html_url": "https://github.com/psf/requests/commit/3b5978fc5d1c121d70e83ddf59379cf36418b4ce"
        }
      ]
    },
    {
      "sha": "421b1f175766065e2feb569990c528df16c2874f",
      "node_id": "C_kwDOABTKOtoAKDQyMWIxZjE3NTc2NjA2NWUyZmViNTY5OTkwYzUyOGRmMTZjMjg3NGY",
      "commit": {
        "author": {
          "name": "dependabot[bot]",
          "email": "49699333+dependabot[bot]@users.noreply.github.com",
          "date": "2023-12-18T16:39:47Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-12-18T16:39:47Z"
        },
        "message": "Bump github/codeql-action from 2.22.1 to 3.22.11\n\nBumps [github/codeql-action](https://github.com/github/codeql-action) from 2.22.1 to 3.22.11.\n- [Release notes](https://github.com/github/codeql-action/releases)\n- [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/github/codeql-action/compare/fdcae64e1484d349b3366718cdfef3d404390e85...b374143c1149a9115d881581d29b8390bbcbb59c)\n\n---\nupdated-dependencies:\n- dependency-name: github/codeql-action\n  dependency-type: direct:production\n  update-type: version-update:semver-major\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
        "tree": {
          "sha": "69bea012f1680b3a08ade7d3a6b6c67ea601e6ad",
          "url": "https://api.github.com/repos/psf/requests/git/trees/69bea012f1680b3a08ade7d3a6b6c67ea601e6ad"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/421b1f175766065e2feb569990c528df16c2874f",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlgHXTCRBK7hj4Ov3rIwAAJ/QIAIuRKCTKtw0tiD+ycAfSl7bA\nCR1sihOupXFTVgtC3X0/m/yvljCDMP1FMSLYWZ6GSKmFQ2uQy8SGw33wQYivOLsU\nuFYgirP3wH76gec8i2IOA28P7/+aRX2qmrLnGPExSPsL/GVDCDnjO899qszmfbLn\nV3RfNQllWW675zalHVZ7Auc9S7YxubYLsFBRrvedR0aKH7r7Z6v7cFzr231AcIlo\np6pchMf4pNTLJLpKa1LKOdkrSgSk+xurxC6DvCb2SzrzZV+0kIMRYwkEF9lhAaoy\nVa9SCqmLmeGd9Wu0UHlvZWDyx5xoNxNyTji3xFSUfYrdOT+jGzDONb6WWMUXkMk=\n=Dx8X\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 69bea012f1680b3a08ade7d3a6b6c67ea601e6ad\nparent 3b5978fc5d1c121d70e83ddf59379cf36418b4ce\nauthor dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> 1702917587 +0000\ncommitter GitHub <noreply@github.com> 1702917587 +0000\n\nBump github/codeql-action from 2.22.1 to 3.22.11\n\nBumps [github/codeql-action](https://github.com/github/codeql-action) from 2.22.1 to 3.22.11.\n- [Release notes](https://github.com/github/codeql-action/releases)\n- [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/github/codeql-action/compare/fdcae64e1484d349b3366718cdfef3d404390e85...b374143c1149a9115d881581d29b8390bbcbb59c)\n\n---\nupdated-dependencies:\n- dependency-name: github/codeql-action\n  dependency-type: direct:production\n  update-type: version-update:semver-major\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/421b1f175766065e2feb569990c528df16c2874f",
      "html_url": "https://github.com/psf/requests/commit/421b1f175766065e2feb569990c528df16c2874f",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/421b1f175766065e2feb569990c528df16c2874f/comments",
      "author": {
        "login": "dependabot[bot]",
        "id": 49699333,
        "node_id": "MDM6Qm90NDk2OTkzMzM=",
        "avatar_url": "https://avatars.githubusercontent.com/in/29110?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/dependabot%5Bbot%5D",
        "html_url": "https://github.com/apps/dependabot",
        "followers_url": "https://api.github.com/users/dependabot%5Bbot%5D/followers",
        "following_url": "https://api.github.com/users/dependabot%5Bbot%5D/following{/other_user}",
        "gists_url": "https://api.github.com/users/dependabot%5Bbot%5D/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/dependabot%5Bbot%5D/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/dependabot%5Bbot%5D/subscriptions",
        "organizations_url": "https://api.github.com/users/dependabot%5Bbot%5D/orgs",
        "repos_url": "https://api.github.com/users/dependabot%5Bbot%5D/repos",
        "events_url": "https://api.github.com/users/dependabot%5Bbot%5D/events{/privacy}",
        "received_events_url": "https://api.github.com/users/dependabot%5Bbot%5D/received_events",
        "type": "Bot",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "3b5978fc5d1c121d70e83ddf59379cf36418b4ce",
          "url": "https://api.github.com/repos/psf/requests/commits/3b5978fc5d1c121d70e83ddf59379cf36418b4ce",
          "html_url": "https://github.com/psf/requests/commit/3b5978fc5d1c121d70e83ddf59379cf36418b4ce"
        }
      ]
    },
    {
      "sha": "e4c821a24778c3a33beec2aa86f3d58e3d94b58c",
      "node_id": "C_kwDOABTKOtoAKGU0YzgyMWEyNDc3OGMzYTMzYmVlYzJhYTg2ZjNkNThlM2Q5NGI1OGM",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2023-12-18T17:30:42Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-12-18T17:30:42Z"
        },
        "message": "Merge pull request #6607 from psf/dependabot/github_actions/github/codeql-action-3.22.11\n\nBump github/codeql-action from 2.22.1 to 3.22.11",
        "tree": {
          "sha": "69bea012f1680b3a08ade7d3a6b6c67ea601e6ad",
          "url": "https://api.github.com/repos/psf/requests/git/trees/69bea012f1680b3a08ade7d3a6b6c67ea601e6ad"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/e4c821a24778c3a33beec2aa86f3d58e3d94b58c",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlgIHCCRBK7hj4Ov3rIwAAa9QIAECgoSdlofq+qAK7skNk5otI\nH4qV3SdF83hmaipwL3HLEYQ7Bww1gpaoxnlMWbuXWKRLvf+dE+QhQM0KxYTqLox2\nFdUyc6ysFAbgrt60bxZM9Fshgux3+J8Rt0y/BCxzmWRXs1T/or+rnntZbmMLc5UZ\nrCHDhem7aro9HZ4pqAEbOyxSpCAY5zgslxdlo2BiNEZ/kx3CBhuS4leJQSJfFDsC\nBtOtZCoKxwtQ8MUhG6hheAeD51GqiemD4H6L/gXlBpzX1s4pL0Z3Y5JKKVtx1jzE\nRJxj1EU+evqvcs7DXlL7qcU3pXwEivHD/VZ2dZ5omF5R0pOlFYsmBpX3pNXZ8UY=\n=IUF3\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 69bea012f1680b3a08ade7d3a6b6c67ea601e6ad\nparent 3b5978fc5d1c121d70e83ddf59379cf36418b4ce\nparent 421b1f175766065e2feb569990c528df16c2874f\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1702920642 -0800\ncommitter GitHub <noreply@github.com> 1702920642 -0800\n\nMerge pull request #6607 from psf/dependabot/github_actions/github/codeql-action-3.22.11\n\nBump github/codeql-action from 2.22.1 to 3.22.11",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/e4c821a24778c3a33beec2aa86f3d58e3d94b58c",
      "html_url": "https://github.com/psf/requests/commit/e4c821a24778c3a33beec2aa86f3d58e3d94b58c",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/e4c821a24778c3a33beec2aa86f3d58e3d94b58c/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "3b5978fc5d1c121d70e83ddf59379cf36418b4ce",
          "url": "https://api.github.com/repos/psf/requests/commits/3b5978fc5d1c121d70e83ddf59379cf36418b4ce",
          "html_url": "https://github.com/psf/requests/commit/3b5978fc5d1c121d70e83ddf59379cf36418b4ce"
        },
        {
          "sha": "421b1f175766065e2feb569990c528df16c2874f",
          "url": "https://api.github.com/repos/psf/requests/commits/421b1f175766065e2feb569990c528df16c2874f",
          "html_url": "https://github.com/psf/requests/commit/421b1f175766065e2feb569990c528df16c2874f"
        }
      ]
    },
    {
      "sha": "1396eb6f7a1116d49f1f0df0ddf895343f84af64",
      "node_id": "C_kwDOABTKOtoAKDEzOTZlYjZmN2ExMTE2ZDQ5ZjFmMGRmMGRkZjg5NTM0M2Y4NGFmNjQ",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2023-12-20T06:17:55Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-12-20T06:17:55Z"
        },
        "message": "Merge pull request #6605 from jaikishpai/fix-#6604\n\nfix for ##6604",
        "tree": {
          "sha": "fb5883a3e959510412b986d4e4c422f12a2f7ab0",
          "url": "https://api.github.com/repos/psf/requests/git/trees/fb5883a3e959510412b986d4e4c422f12a2f7ab0"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/1396eb6f7a1116d49f1f0df0ddf895343f84af64",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlgocTCRBK7hj4Ov3rIwAAnGIIAAebOl4LgoEtdCxDWXIgR7sa\ncYsBTbM+PPoy0Ms/UbMAF9TT5BJNgAy/91LfxbSCab07VIb6YuMcVNA+C6N0E4fG\n/LWb3ylm8HzR7+NQgxUW9P1JurhUtwdyg9kNi17kl+zXV3eTh7jfjLRW1Ycr9G5q\npx8/kbZz1+MZm2LX76cifcUYZ/5x+pEhNW3MvvWBfbD828pfCiYtoFyWhLPGBJbs\nHfrpKosBfnVkEVRM+JFkhud9ZPCCiuTOFrVJ5UDGAVa+ZmGRkbHTmLTBWNFocl7p\noP2zz3hibbzl67zM2vfaIUrLuHRZRDOyDOJ/4YTRrIUUH5zp60KfsGcM2iI8Gbg=\n=BIVG\n-----END PGP SIGNATURE-----\n",
          "payload": "tree fb5883a3e959510412b986d4e4c422f12a2f7ab0\nparent e4c821a24778c3a33beec2aa86f3d58e3d94b58c\nparent 1447bccc057e7fbffdfecd75cd4922702489a14b\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1703053075 -0800\ncommitter GitHub <noreply@github.com> 1703053075 -0800\n\nMerge pull request #6605 from jaikishpai/fix-#6604\n\nfix for ##6604",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/1396eb6f7a1116d49f1f0df0ddf895343f84af64",
      "html_url": "https://github.com/psf/requests/commit/1396eb6f7a1116d49f1f0df0ddf895343f84af64",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/1396eb6f7a1116d49f1f0df0ddf895343f84af64/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "e4c821a24778c3a33beec2aa86f3d58e3d94b58c",
          "url": "https://api.github.com/repos/psf/requests/commits/e4c821a24778c3a33beec2aa86f3d58e3d94b58c",
          "html_url": "https://github.com/psf/requests/commit/e4c821a24778c3a33beec2aa86f3d58e3d94b58c"
        },
        {
          "sha": "1447bccc057e7fbffdfecd75cd4922702489a14b",
          "url": "https://api.github.com/repos/psf/requests/commits/1447bccc057e7fbffdfecd75cd4922702489a14b",
          "html_url": "https://github.com/psf/requests/commit/1447bccc057e7fbffdfecd75cd4922702489a14b"
        }
      ]
    },
    {
      "sha": "242d3113c09d10ba9a11dbcc05e0310a1e7568af",
      "node_id": "C_kwDOABTKOtoAKDI0MmQzMTEzYzA5ZDEwYmE5YTExZGJjYzA1ZTAzMTBhMWU3NTY4YWY",
      "commit": {
        "author": {
          "name": "Mike Fiedler",
          "email": "miketheman@gmail.com",
          "date": "2023-12-23T16:16:50Z"
        },
        "committer": {
          "name": "Mike Fiedler",
          "email": "miketheman@gmail.com",
          "date": "2023-12-23T16:16:50Z"
        },
        "message": "docs: specify sphinx dirhtml builder\n\nWith the requirement of a configuration file, the default builder\nof `dirhtml` that RTD used to use is no longer specified.\nThis leads to URLs ending in `.html` now, which\nbreaks other exisitng references.\n\nRefs: #6603\nRefs: https://docs.readthedocs.io/en/stable/config-file/v2.html#sphinx-builder\nRefs: https://www.sphinx-doc.org/en/master/usage/builders/index.html#sphinx.builders.dirhtml.DirectoryHTMLBuilder\n\nSigned-off-by: Mike Fiedler <miketheman@gmail.com>",
        "tree": {
          "sha": "553b5d091400048b8622ff977cf9a17fd8478b6d",
          "url": "https://api.github.com/repos/psf/requests/git/trees/553b5d091400048b8622ff977cf9a17fd8478b6d"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/242d3113c09d10ba9a11dbcc05e0310a1e7568af",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/242d3113c09d10ba9a11dbcc05e0310a1e7568af",
      "html_url": "https://github.com/psf/requests/commit/242d3113c09d10ba9a11dbcc05e0310a1e7568af",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/242d3113c09d10ba9a11dbcc05e0310a1e7568af/comments",
      "author": {
        "login": "miketheman",
        "id": 529516,
        "node_id": "MDQ6VXNlcjUyOTUxNg==",
        "avatar_url": "https://avatars.githubusercontent.com/u/529516?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/miketheman",
        "html_url": "https://github.com/miketheman",
        "followers_url": "https://api.github.com/users/miketheman/followers",
        "following_url": "https://api.github.com/users/miketheman/following{/other_user}",
        "gists_url": "https://api.github.com/users/miketheman/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/miketheman/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/miketheman/subscriptions",
        "organizations_url": "https://api.github.com/users/miketheman/orgs",
        "repos_url": "https://api.github.com/users/miketheman/repos",
        "events_url": "https://api.github.com/users/miketheman/events{/privacy}",
        "received_events_url": "https://api.github.com/users/miketheman/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "miketheman",
        "id": 529516,
        "node_id": "MDQ6VXNlcjUyOTUxNg==",
        "avatar_url": "https://avatars.githubusercontent.com/u/529516?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/miketheman",
        "html_url": "https://github.com/miketheman",
        "followers_url": "https://api.github.com/users/miketheman/followers",
        "following_url": "https://api.github.com/users/miketheman/following{/other_user}",
        "gists_url": "https://api.github.com/users/miketheman/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/miketheman/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/miketheman/subscriptions",
        "organizations_url": "https://api.github.com/users/miketheman/orgs",
        "repos_url": "https://api.github.com/users/miketheman/repos",
        "events_url": "https://api.github.com/users/miketheman/events{/privacy}",
        "received_events_url": "https://api.github.com/users/miketheman/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "1396eb6f7a1116d49f1f0df0ddf895343f84af64",
          "url": "https://api.github.com/repos/psf/requests/commits/1396eb6f7a1116d49f1f0df0ddf895343f84af64",
          "html_url": "https://github.com/psf/requests/commit/1396eb6f7a1116d49f1f0df0ddf895343f84af64"
        }
      ]
    },
    {
      "sha": "b5bd0f14cc6fe12a712d21d7881aab59d0dd9951",
      "node_id": "C_kwDOABTKOtoAKGI1YmQwZjE0Y2M2ZmUxMmE3MTJkMjFkNzg4MWFhYjU5ZDBkZDk5NTE",
      "commit": {
        "author": {
          "name": "Mike Fiedler",
          "email": "miketheman@gmail.com",
          "date": "2023-12-23T17:17:34Z"
        },
        "committer": {
          "name": "Mike Fiedler",
          "email": "miketheman@gmail.com",
          "date": "2023-12-23T17:17:34Z"
        },
        "message": "docs: add label to socks heading\n\nWhen trying to link via intersphinx, a label must be used.\nOtherwise a full URL is required, which is less desirable.\n\nSigned-off-by: Mike Fiedler <miketheman@gmail.com>",
        "tree": {
          "sha": "3b8260a06489962531b8e9594ea03422e55fd101",
          "url": "https://api.github.com/repos/psf/requests/git/trees/3b8260a06489962531b8e9594ea03422e55fd101"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/b5bd0f14cc6fe12a712d21d7881aab59d0dd9951",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/b5bd0f14cc6fe12a712d21d7881aab59d0dd9951",
      "html_url": "https://github.com/psf/requests/commit/b5bd0f14cc6fe12a712d21d7881aab59d0dd9951",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/b5bd0f14cc6fe12a712d21d7881aab59d0dd9951/comments",
      "author": {
        "login": "miketheman",
        "id": 529516,
        "node_id": "MDQ6VXNlcjUyOTUxNg==",
        "avatar_url": "https://avatars.githubusercontent.com/u/529516?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/miketheman",
        "html_url": "https://github.com/miketheman",
        "followers_url": "https://api.github.com/users/miketheman/followers",
        "following_url": "https://api.github.com/users/miketheman/following{/other_user}",
        "gists_url": "https://api.github.com/users/miketheman/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/miketheman/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/miketheman/subscriptions",
        "organizations_url": "https://api.github.com/users/miketheman/orgs",
        "repos_url": "https://api.github.com/users/miketheman/repos",
        "events_url": "https://api.github.com/users/miketheman/events{/privacy}",
        "received_events_url": "https://api.github.com/users/miketheman/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "miketheman",
        "id": 529516,
        "node_id": "MDQ6VXNlcjUyOTUxNg==",
        "avatar_url": "https://avatars.githubusercontent.com/u/529516?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/miketheman",
        "html_url": "https://github.com/miketheman",
        "followers_url": "https://api.github.com/users/miketheman/followers",
        "following_url": "https://api.github.com/users/miketheman/following{/other_user}",
        "gists_url": "https://api.github.com/users/miketheman/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/miketheman/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/miketheman/subscriptions",
        "organizations_url": "https://api.github.com/users/miketheman/orgs",
        "repos_url": "https://api.github.com/users/miketheman/repos",
        "events_url": "https://api.github.com/users/miketheman/events{/privacy}",
        "received_events_url": "https://api.github.com/users/miketheman/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "1396eb6f7a1116d49f1f0df0ddf895343f84af64",
          "url": "https://api.github.com/repos/psf/requests/commits/1396eb6f7a1116d49f1f0df0ddf895343f84af64",
          "html_url": "https://github.com/psf/requests/commit/1396eb6f7a1116d49f1f0df0ddf895343f84af64"
        }
      ]
    },
    {
      "sha": "f3f978441916389abcb2f2a72522955d551326e9",
      "node_id": "C_kwDOABTKOtoAKGYzZjk3ODQ0MTkxNjM4OWFiY2IyZjJhNzI1MjI5NTVkNTUxMzI2ZTk",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2023-12-23T17:24:56Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-12-23T17:24:56Z"
        },
        "message": "Merge pull request #6613 from miketheman/add-socks-label\n\ndocs: add label to socks heading",
        "tree": {
          "sha": "3b8260a06489962531b8e9594ea03422e55fd101",
          "url": "https://api.github.com/repos/psf/requests/git/trees/3b8260a06489962531b8e9594ea03422e55fd101"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/f3f978441916389abcb2f2a72522955d551326e9",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlhxfoCRBK7hj4Ov3rIwAARbkIAH1KKPEVodGbAKkNwLZkxgph\nfBqyBN9YGBJoOcH2CZoX3PZSnVv/41RRoMZVL1OXUeDnt7Ovpi7pDSrb6NRak7F1\nlMdkF35gOFf0kUdaCaZVgHH94v1JZn/hiqXaAnHg7XH2ifZheJW8FD9KVXzzE1ED\nhDoKwxQp4+krH+6IjHybhkJZp1qx5gNbacXklNKBDwCxnFnRrwI085eAx7TWBmzF\nAAx5yXPAfItzVdunY1uAf9aZz+bFaz9rDpnCv1CCBvYU3BWCuM54uxlxwuoly7/8\nij5dDJLmIIJSSqcs2PJciChls1M66n8UtcLJIlwsTBKy3BcnRf8SbtmCo5IE0j8=\n=xYP2\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 3b8260a06489962531b8e9594ea03422e55fd101\nparent 1396eb6f7a1116d49f1f0df0ddf895343f84af64\nparent b5bd0f14cc6fe12a712d21d7881aab59d0dd9951\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1703352296 -0600\ncommitter GitHub <noreply@github.com> 1703352296 -0600\n\nMerge pull request #6613 from miketheman/add-socks-label\n\ndocs: add label to socks heading",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/f3f978441916389abcb2f2a72522955d551326e9",
      "html_url": "https://github.com/psf/requests/commit/f3f978441916389abcb2f2a72522955d551326e9",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/f3f978441916389abcb2f2a72522955d551326e9/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "1396eb6f7a1116d49f1f0df0ddf895343f84af64",
          "url": "https://api.github.com/repos/psf/requests/commits/1396eb6f7a1116d49f1f0df0ddf895343f84af64",
          "html_url": "https://github.com/psf/requests/commit/1396eb6f7a1116d49f1f0df0ddf895343f84af64"
        },
        {
          "sha": "b5bd0f14cc6fe12a712d21d7881aab59d0dd9951",
          "url": "https://api.github.com/repos/psf/requests/commits/b5bd0f14cc6fe12a712d21d7881aab59d0dd9951",
          "html_url": "https://github.com/psf/requests/commit/b5bd0f14cc6fe12a712d21d7881aab59d0dd9951"
        }
      ]
    },
    {
      "sha": "f23346a9b8e74de01220cce96c037bbd2404a1c6",
      "node_id": "C_kwDOABTKOtoAKGYyMzM0NmE5YjhlNzRkZTAxMjIwY2NlOTZjMDM3YmJkMjQwNGExYzY",
      "commit": {
        "author": {
          "name": "Mike Fiedler",
          "email": "miketheman@gmail.com",
          "date": "2023-12-23T17:36:34Z"
        },
        "committer": {
          "name": "Mike Fiedler",
          "email": "miketheman@gmail.com",
          "date": "2023-12-23T17:36:34Z"
        },
        "message": "Revert \"Merge pull request #6605 from jaikishpai/fix-#6604\"\n\nThis reverts commit 1396eb6f7a1116d49f1f0df0ddf895343f84af64, reversing\nchanges made to e4c821a24778c3a33beec2aa86f3d58e3d94b58c.",
        "tree": {
          "sha": "c9205d2816bd22c8043157de5f181bac3932f46b",
          "url": "https://api.github.com/repos/psf/requests/git/trees/c9205d2816bd22c8043157de5f181bac3932f46b"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/f23346a9b8e74de01220cce96c037bbd2404a1c6",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/f23346a9b8e74de01220cce96c037bbd2404a1c6",
      "html_url": "https://github.com/psf/requests/commit/f23346a9b8e74de01220cce96c037bbd2404a1c6",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/f23346a9b8e74de01220cce96c037bbd2404a1c6/comments",
      "author": {
        "login": "miketheman",
        "id": 529516,
        "node_id": "MDQ6VXNlcjUyOTUxNg==",
        "avatar_url": "https://avatars.githubusercontent.com/u/529516?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/miketheman",
        "html_url": "https://github.com/miketheman",
        "followers_url": "https://api.github.com/users/miketheman/followers",
        "following_url": "https://api.github.com/users/miketheman/following{/other_user}",
        "gists_url": "https://api.github.com/users/miketheman/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/miketheman/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/miketheman/subscriptions",
        "organizations_url": "https://api.github.com/users/miketheman/orgs",
        "repos_url": "https://api.github.com/users/miketheman/repos",
        "events_url": "https://api.github.com/users/miketheman/events{/privacy}",
        "received_events_url": "https://api.github.com/users/miketheman/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "miketheman",
        "id": 529516,
        "node_id": "MDQ6VXNlcjUyOTUxNg==",
        "avatar_url": "https://avatars.githubusercontent.com/u/529516?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/miketheman",
        "html_url": "https://github.com/miketheman",
        "followers_url": "https://api.github.com/users/miketheman/followers",
        "following_url": "https://api.github.com/users/miketheman/following{/other_user}",
        "gists_url": "https://api.github.com/users/miketheman/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/miketheman/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/miketheman/subscriptions",
        "organizations_url": "https://api.github.com/users/miketheman/orgs",
        "repos_url": "https://api.github.com/users/miketheman/repos",
        "events_url": "https://api.github.com/users/miketheman/events{/privacy}",
        "received_events_url": "https://api.github.com/users/miketheman/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "242d3113c09d10ba9a11dbcc05e0310a1e7568af",
          "url": "https://api.github.com/repos/psf/requests/commits/242d3113c09d10ba9a11dbcc05e0310a1e7568af",
          "html_url": "https://github.com/psf/requests/commit/242d3113c09d10ba9a11dbcc05e0310a1e7568af"
        }
      ]
    },
    {
      "sha": "bfba9dc68c841b78ca51e6302d3283d33167f773",
      "node_id": "C_kwDOABTKOtoAKGJmYmE5ZGM2OGM4NDFiNzhjYTUxZTYzMDJkMzI4M2QzMzE2N2Y3NzM",
      "commit": {
        "author": {
          "name": "Mike Fiedler",
          "email": "miketheman@gmail.com",
          "date": "2023-12-23T18:09:08Z"
        },
        "committer": {
          "name": "Mike Fiedler",
          "email": "miketheman@gmail.com",
          "date": "2023-12-23T18:09:55Z"
        },
        "message": "docs: replace concrete URLs with references\n\nAny development links will now refer back to the generated docs.\n\nSigned-off-by: Mike Fiedler <miketheman@gmail.com>",
        "tree": {
          "sha": "888c9ec73468535bdf652a67c27d6314d6e88201",
          "url": "https://api.github.com/repos/psf/requests/git/trees/888c9ec73468535bdf652a67c27d6314d6e88201"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/bfba9dc68c841b78ca51e6302d3283d33167f773",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/bfba9dc68c841b78ca51e6302d3283d33167f773",
      "html_url": "https://github.com/psf/requests/commit/bfba9dc68c841b78ca51e6302d3283d33167f773",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/bfba9dc68c841b78ca51e6302d3283d33167f773/comments",
      "author": {
        "login": "miketheman",
        "id": 529516,
        "node_id": "MDQ6VXNlcjUyOTUxNg==",
        "avatar_url": "https://avatars.githubusercontent.com/u/529516?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/miketheman",
        "html_url": "https://github.com/miketheman",
        "followers_url": "https://api.github.com/users/miketheman/followers",
        "following_url": "https://api.github.com/users/miketheman/following{/other_user}",
        "gists_url": "https://api.github.com/users/miketheman/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/miketheman/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/miketheman/subscriptions",
        "organizations_url": "https://api.github.com/users/miketheman/orgs",
        "repos_url": "https://api.github.com/users/miketheman/repos",
        "events_url": "https://api.github.com/users/miketheman/events{/privacy}",
        "received_events_url": "https://api.github.com/users/miketheman/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "miketheman",
        "id": 529516,
        "node_id": "MDQ6VXNlcjUyOTUxNg==",
        "avatar_url": "https://avatars.githubusercontent.com/u/529516?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/miketheman",
        "html_url": "https://github.com/miketheman",
        "followers_url": "https://api.github.com/users/miketheman/followers",
        "following_url": "https://api.github.com/users/miketheman/following{/other_user}",
        "gists_url": "https://api.github.com/users/miketheman/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/miketheman/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/miketheman/subscriptions",
        "organizations_url": "https://api.github.com/users/miketheman/orgs",
        "repos_url": "https://api.github.com/users/miketheman/repos",
        "events_url": "https://api.github.com/users/miketheman/events{/privacy}",
        "received_events_url": "https://api.github.com/users/miketheman/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "f23346a9b8e74de01220cce96c037bbd2404a1c6",
          "url": "https://api.github.com/repos/psf/requests/commits/f23346a9b8e74de01220cce96c037bbd2404a1c6",
          "html_url": "https://github.com/psf/requests/commit/f23346a9b8e74de01220cce96c037bbd2404a1c6"
        }
      ]
    },
    {
      "sha": "25939d8784dc8bec784b8129152efa4443daa82f",
      "node_id": "C_kwDOABTKOtoAKDI1OTM5ZDg3ODRkYzhiZWM3ODRiODEyOTE1MmVmYTQ0NDNkYWE4MmY",
      "commit": {
        "author": {
          "name": "Mike Fiedler",
          "email": "miketheman@gmail.com",
          "date": "2023-12-23T18:15:33Z"
        },
        "committer": {
          "name": "Mike Fiedler",
          "email": "miketheman@gmail.com",
          "date": "2023-12-23T18:15:33Z"
        },
        "message": "add myself\n\nSigned-off-by: Mike Fiedler <miketheman@gmail.com>",
        "tree": {
          "sha": "4c9189cb54245ab5d5707b53bc3825cfb82f28e6",
          "url": "https://api.github.com/repos/psf/requests/git/trees/4c9189cb54245ab5d5707b53bc3825cfb82f28e6"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/25939d8784dc8bec784b8129152efa4443daa82f",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/25939d8784dc8bec784b8129152efa4443daa82f",
      "html_url": "https://github.com/psf/requests/commit/25939d8784dc8bec784b8129152efa4443daa82f",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/25939d8784dc8bec784b8129152efa4443daa82f/comments",
      "author": {
        "login": "miketheman",
        "id": 529516,
        "node_id": "MDQ6VXNlcjUyOTUxNg==",
        "avatar_url": "https://avatars.githubusercontent.com/u/529516?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/miketheman",
        "html_url": "https://github.com/miketheman",
        "followers_url": "https://api.github.com/users/miketheman/followers",
        "following_url": "https://api.github.com/users/miketheman/following{/other_user}",
        "gists_url": "https://api.github.com/users/miketheman/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/miketheman/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/miketheman/subscriptions",
        "organizations_url": "https://api.github.com/users/miketheman/orgs",
        "repos_url": "https://api.github.com/users/miketheman/repos",
        "events_url": "https://api.github.com/users/miketheman/events{/privacy}",
        "received_events_url": "https://api.github.com/users/miketheman/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "miketheman",
        "id": 529516,
        "node_id": "MDQ6VXNlcjUyOTUxNg==",
        "avatar_url": "https://avatars.githubusercontent.com/u/529516?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/miketheman",
        "html_url": "https://github.com/miketheman",
        "followers_url": "https://api.github.com/users/miketheman/followers",
        "following_url": "https://api.github.com/users/miketheman/following{/other_user}",
        "gists_url": "https://api.github.com/users/miketheman/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/miketheman/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/miketheman/subscriptions",
        "organizations_url": "https://api.github.com/users/miketheman/orgs",
        "repos_url": "https://api.github.com/users/miketheman/repos",
        "events_url": "https://api.github.com/users/miketheman/events{/privacy}",
        "received_events_url": "https://api.github.com/users/miketheman/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "bfba9dc68c841b78ca51e6302d3283d33167f773",
          "url": "https://api.github.com/repos/psf/requests/commits/bfba9dc68c841b78ca51e6302d3283d33167f773",
          "html_url": "https://github.com/psf/requests/commit/bfba9dc68c841b78ca51e6302d3283d33167f773"
        }
      ]
    },
    {
      "sha": "72eccc8dd8b7c272e520f22b0256386c80864e94",
      "node_id": "C_kwDOABTKOtoAKDcyZWNjYzhkZDhiN2MyNzJlNTIwZjIyYjAyNTYzODZjODA4NjRlOTQ",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2023-12-23T18:33:48Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2023-12-23T18:33:48Z"
        },
        "message": "Merge pull request #6612 from miketheman/fix-docs-urls\n\ndocs: specify sphinx dirhtml builder, use references instead of absolutes",
        "tree": {
          "sha": "dd534cb151819f38f78a78de598f13d28b2f6ef9",
          "url": "https://api.github.com/repos/psf/requests/git/trees/dd534cb151819f38f78a78de598f13d28b2f6ef9"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/72eccc8dd8b7c272e520f22b0256386c80864e94",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlhygMCRBK7hj4Ov3rIwAAJ04IACbfABf14xflczh6lxpXfY1Y\nxIZuzxdE9hJFkE2px/PZuqYA0I4i3rsT+mVPz8S2aYAEPyumKiJ3YTIocgmifkwC\nijqsXXvfbwNGverLRa8rk9MDEON+bGmf+aNBQo/6DyFkcNluS/MwPHgi6VfAVeFU\neRIg+VSlNh5npB0mIKR8dpf9tJpYagJqiPqqnhql/H80ztf0rNKVSKOT6AOfJ8Ud\nWROyM7XCxqfjKGo/2zCfoEoV5tfJTEcqCEqHzgVx/SD0UuLHB9rVsJsWSbO9dobU\n/7SujNe08nTue2HLdgaX1JUoE4IWGxZ1meMORLNCjnpxueYk4eXcFckKMKFlFNY=\n=RHag\n-----END PGP SIGNATURE-----\n",
          "payload": "tree dd534cb151819f38f78a78de598f13d28b2f6ef9\nparent f3f978441916389abcb2f2a72522955d551326e9\nparent 25939d8784dc8bec784b8129152efa4443daa82f\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1703356428 -0600\ncommitter GitHub <noreply@github.com> 1703356428 -0600\n\nMerge pull request #6612 from miketheman/fix-docs-urls\n\ndocs: specify sphinx dirhtml builder, use references instead of absolutes",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/72eccc8dd8b7c272e520f22b0256386c80864e94",
      "html_url": "https://github.com/psf/requests/commit/72eccc8dd8b7c272e520f22b0256386c80864e94",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/72eccc8dd8b7c272e520f22b0256386c80864e94/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "f3f978441916389abcb2f2a72522955d551326e9",
          "url": "https://api.github.com/repos/psf/requests/commits/f3f978441916389abcb2f2a72522955d551326e9",
          "html_url": "https://github.com/psf/requests/commit/f3f978441916389abcb2f2a72522955d551326e9"
        },
        {
          "sha": "25939d8784dc8bec784b8129152efa4443daa82f",
          "url": "https://api.github.com/repos/psf/requests/commits/25939d8784dc8bec784b8129152efa4443daa82f",
          "html_url": "https://github.com/psf/requests/commit/25939d8784dc8bec784b8129152efa4443daa82f"
        }
      ]
    },
    {
      "sha": "b0e6c9bf85378acd079ca84a4481f361b47a2147",
      "node_id": "C_kwDOABTKOtoAKGIwZTZjOWJmODUzNzhhY2QwNzljYTg0YTQ0ODFmMzYxYjQ3YTIxNDc",
      "commit": {
        "author": {
          "name": "dependabot[bot]",
          "email": "49699333+dependabot[bot]@users.noreply.github.com",
          "date": "2024-01-08T17:01:37Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-01-08T17:01:37Z"
        },
        "message": "Bump github/codeql-action from 3.22.11 to 3.23.0\n\nBumps [github/codeql-action](https://github.com/github/codeql-action) from 3.22.11 to 3.23.0.\n- [Release notes](https://github.com/github/codeql-action/releases)\n- [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/github/codeql-action/compare/b374143c1149a9115d881581d29b8390bbcbb59c...e5f05b81d5b6ff8cfa111c80c22c5fd02a384118)\n\n---\nupdated-dependencies:\n- dependency-name: github/codeql-action\n  dependency-type: direct:production\n  update-type: version-update:semver-minor\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
        "tree": {
          "sha": "57998a9c9d376b98cbdca00ceb85dfab1f996504",
          "url": "https://api.github.com/repos/psf/requests/git/trees/57998a9c9d376b98cbdca00ceb85dfab1f996504"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/b0e6c9bf85378acd079ca84a4481f361b47a2147",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlnCpxCRBK7hj4Ov3rIwAAcD4IACYyKCC3Y8LfF07AfYLceUCv\nS/BNmZeU0VFQhl0nzyD9ZdnQPzkRUEVjPCawdvoIVsn1rfDQcU6R9oQGK22F6FuU\nQbNHi640+xLyi8OZgpGyK+ORR7XpZLQFVcCDzLw/voL0alY8wybTYalMKg8U1vGd\nguB7yFkBZRkVM92DsX9c54iWUUZOIKyVQRXjZNhsIkVA6+e/2Mc3kZ5NQJ2/dSBH\nB3InSHyqSHQugjTTCT2bGHFIubvfKfGeHg5pOiEXWJAErmh8wPax00n6ljl73aGZ\nEZS9WNDcw0sB7cZ8avfvbbnE0HHqCsZ9Q04KV6pLgQFlFIDxqGatghbtv+uZGMw=\n=aWw7\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 57998a9c9d376b98cbdca00ceb85dfab1f996504\nparent 72eccc8dd8b7c272e520f22b0256386c80864e94\nauthor dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> 1704733297 +0000\ncommitter GitHub <noreply@github.com> 1704733297 +0000\n\nBump github/codeql-action from 3.22.11 to 3.23.0\n\nBumps [github/codeql-action](https://github.com/github/codeql-action) from 3.22.11 to 3.23.0.\n- [Release notes](https://github.com/github/codeql-action/releases)\n- [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/github/codeql-action/compare/b374143c1149a9115d881581d29b8390bbcbb59c...e5f05b81d5b6ff8cfa111c80c22c5fd02a384118)\n\n---\nupdated-dependencies:\n- dependency-name: github/codeql-action\n  dependency-type: direct:production\n  update-type: version-update:semver-minor\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/b0e6c9bf85378acd079ca84a4481f361b47a2147",
      "html_url": "https://github.com/psf/requests/commit/b0e6c9bf85378acd079ca84a4481f361b47a2147",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/b0e6c9bf85378acd079ca84a4481f361b47a2147/comments",
      "author": {
        "login": "dependabot[bot]",
        "id": 49699333,
        "node_id": "MDM6Qm90NDk2OTkzMzM=",
        "avatar_url": "https://avatars.githubusercontent.com/in/29110?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/dependabot%5Bbot%5D",
        "html_url": "https://github.com/apps/dependabot",
        "followers_url": "https://api.github.com/users/dependabot%5Bbot%5D/followers",
        "following_url": "https://api.github.com/users/dependabot%5Bbot%5D/following{/other_user}",
        "gists_url": "https://api.github.com/users/dependabot%5Bbot%5D/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/dependabot%5Bbot%5D/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/dependabot%5Bbot%5D/subscriptions",
        "organizations_url": "https://api.github.com/users/dependabot%5Bbot%5D/orgs",
        "repos_url": "https://api.github.com/users/dependabot%5Bbot%5D/repos",
        "events_url": "https://api.github.com/users/dependabot%5Bbot%5D/events{/privacy}",
        "received_events_url": "https://api.github.com/users/dependabot%5Bbot%5D/received_events",
        "type": "Bot",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "72eccc8dd8b7c272e520f22b0256386c80864e94",
          "url": "https://api.github.com/repos/psf/requests/commits/72eccc8dd8b7c272e520f22b0256386c80864e94",
          "html_url": "https://github.com/psf/requests/commit/72eccc8dd8b7c272e520f22b0256386c80864e94"
        }
      ]
    },
    {
      "sha": "96b22fa18c00831656ee4b286bf1c9062459b00a",
      "node_id": "C_kwDOABTKOtoAKDk2YjIyZmExOGMwMDgzMTY1NmVlNGIyODZiZjFjOTA2MjQ1OWIwMGE",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2024-01-08T17:56:01Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-01-08T17:56:01Z"
        },
        "message": "Merge pull request #6619 from psf/dependabot/github_actions/github/codeql-action-3.23.0\n\nBump github/codeql-action from 3.22.11 to 3.23.0",
        "tree": {
          "sha": "57998a9c9d376b98cbdca00ceb85dfab1f996504",
          "url": "https://api.github.com/repos/psf/requests/git/trees/57998a9c9d376b98cbdca00ceb85dfab1f996504"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/96b22fa18c00831656ee4b286bf1c9062459b00a",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJlnDcxCRBK7hj4Ov3rIwAArbcIAGR8mpq3p17PxwdDprysZQi6\n9XIels97cUaNhwBJXJsCTtdMVns5H1cKpsVwmzFGmKrjkrP3k6BQPOFqIJ8h7/g/\nYcU+AMPEORUS0PjS2S/9EkWM99RB9+6BFMmfkSaVTrGRYor3k9vz3vR9EpDyuiLf\neeSaMthBXEWSVqz964MWVN9D7+f57Oc80tVwzh2uWeQIH5dN0PAtEgJLaK13H0EY\nx1ceKGUjarW+IYblYyZVL86TAZ4HlYcbwP/MXamIRHH2xIvqJf3tEI5deEl/xscq\ncBSk7tN1hC/ef7FXv1V7RzoSSnJa1escH0BCmJYCeosWo89xmJ3dG8nS4mVBCZI=\n=mXEz\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 57998a9c9d376b98cbdca00ceb85dfab1f996504\nparent 72eccc8dd8b7c272e520f22b0256386c80864e94\nparent b0e6c9bf85378acd079ca84a4481f361b47a2147\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1704736561 -0600\ncommitter GitHub <noreply@github.com> 1704736561 -0600\n\nMerge pull request #6619 from psf/dependabot/github_actions/github/codeql-action-3.23.0\n\nBump github/codeql-action from 3.22.11 to 3.23.0",
          "verified_at": "2024-01-16T19:59:59Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/96b22fa18c00831656ee4b286bf1c9062459b00a",
      "html_url": "https://github.com/psf/requests/commit/96b22fa18c00831656ee4b286bf1c9062459b00a",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/96b22fa18c00831656ee4b286bf1c9062459b00a/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "72eccc8dd8b7c272e520f22b0256386c80864e94",
          "url": "https://api.github.com/repos/psf/requests/commits/72eccc8dd8b7c272e520f22b0256386c80864e94",
          "html_url": "https://github.com/psf/requests/commit/72eccc8dd8b7c272e520f22b0256386c80864e94"
        },
        {
          "sha": "b0e6c9bf85378acd079ca84a4481f361b47a2147",
          "url": "https://api.github.com/repos/psf/requests/commits/b0e6c9bf85378acd079ca84a4481f361b47a2147",
          "html_url": "https://github.com/psf/requests/commit/b0e6c9bf85378acd079ca84a4481f361b47a2147"
        }
      ]
    },
    {
      "sha": "3ff3ff21dd45957c9e143cd500291959bb15f690",
      "node_id": "C_kwDOABTKOtoAKDNmZjNmZjIxZGQ0NTk1N2M5ZTE0M2NkNTAwMjkxOTU5YmIxNWY2OTA",
      "commit": {
        "author": {
          "name": "Thomas Dehghani",
          "email": "thomas.dehghani@gmail.com",
          "date": "2024-01-31T16:07:35Z"
        },
        "committer": {
          "name": "Thomas Dehghani",
          "email": "thomas.dehghani@gmail.com",
          "date": "2024-01-31T16:13:53Z"
        },
        "message": "Fix #6628 - JSONDecodeError are not deserializable\n\nrequests.exceptions.JSONDecodeError are not deserializable: calling\n`pickle.dumps` followed by `pickle.loads` will trigger an error.\n\nThis is particularly a problem in a process pool, as an attempt to\ndecode json on an invalid json document will result in the entire\nprocess pool crashing.\n\nThis is due to the MRO of the `requests.exceptions.JSONDecodeError`\nclass: the `__reduce__` method called when pickling an instance is not\nthe one from the JSON library parent: two out of three args expected\nfor instantiation will be dropped, and the instance can't be\ndeserialised.\n\nBy specifying in the class which parent `__reduce__` method should be\ncalled, the bug is fixed as all args are carried over in the resulting\npickled bytes.",
        "tree": {
          "sha": "df91092f6d019cecb7265075fef228745e3fda6e",
          "url": "https://api.github.com/repos/psf/requests/git/trees/df91092f6d019cecb7265075fef228745e3fda6e"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/3ff3ff21dd45957c9e143cd500291959bb15f690",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/3ff3ff21dd45957c9e143cd500291959bb15f690",
      "html_url": "https://github.com/psf/requests/commit/3ff3ff21dd45957c9e143cd500291959bb15f690",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/3ff3ff21dd45957c9e143cd500291959bb15f690/comments",
      "author": {
        "login": "Tarty",
        "id": 8852408,
        "node_id": "MDQ6VXNlcjg4NTI0MDg=",
        "avatar_url": "https://avatars.githubusercontent.com/u/8852408?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/Tarty",
        "html_url": "https://github.com/Tarty",
        "followers_url": "https://api.github.com/users/Tarty/followers",
        "following_url": "https://api.github.com/users/Tarty/following{/other_user}",
        "gists_url": "https://api.github.com/users/Tarty/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/Tarty/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/Tarty/subscriptions",
        "organizations_url": "https://api.github.com/users/Tarty/orgs",
        "repos_url": "https://api.github.com/users/Tarty/repos",
        "events_url": "https://api.github.com/users/Tarty/events{/privacy}",
        "received_events_url": "https://api.github.com/users/Tarty/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "Tarty",
        "id": 8852408,
        "node_id": "MDQ6VXNlcjg4NTI0MDg=",
        "avatar_url": "https://avatars.githubusercontent.com/u/8852408?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/Tarty",
        "html_url": "https://github.com/Tarty",
        "followers_url": "https://api.github.com/users/Tarty/followers",
        "following_url": "https://api.github.com/users/Tarty/following{/other_user}",
        "gists_url": "https://api.github.com/users/Tarty/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/Tarty/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/Tarty/subscriptions",
        "organizations_url": "https://api.github.com/users/Tarty/orgs",
        "repos_url": "https://api.github.com/users/Tarty/repos",
        "events_url": "https://api.github.com/users/Tarty/events{/privacy}",
        "received_events_url": "https://api.github.com/users/Tarty/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "96b22fa18c00831656ee4b286bf1c9062459b00a",
          "url": "https://api.github.com/repos/psf/requests/commits/96b22fa18c00831656ee4b286bf1c9062459b00a",
          "html_url": "https://github.com/psf/requests/commit/96b22fa18c00831656ee4b286bf1c9062459b00a"
        }
      ]
    },
    {
      "sha": "a5a0e4b587c7f2de4250ec965caf21b8fca172e0",
      "node_id": "C_kwDOABTKOtoAKGE1YTBlNGI1ODdjN2YyZGU0MjUwZWM5NjVjYWYyMWI4ZmNhMTcyZTA",
      "commit": {
        "author": {
          "name": "dependabot[bot]",
          "email": "49699333+dependabot[bot]@users.noreply.github.com",
          "date": "2024-02-05T16:38:01Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-02-05T16:38:01Z"
        },
        "message": "Bump github/codeql-action from 3.23.0 to 3.24.0\n\nBumps [github/codeql-action](https://github.com/github/codeql-action) from 3.23.0 to 3.24.0.\n- [Release notes](https://github.com/github/codeql-action/releases)\n- [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/github/codeql-action/compare/e5f05b81d5b6ff8cfa111c80c22c5fd02a384118...e8893c57a1f3a2b659b6b55564fdfdbbd2982911)\n\n---\nupdated-dependencies:\n- dependency-name: github/codeql-action\n  dependency-type: direct:production\n  update-type: version-update:semver-minor\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
        "tree": {
          "sha": "30eeeaa4a18a5cc779edc60c6cee861debef297e",
          "url": "https://api.github.com/repos/psf/requests/git/trees/30eeeaa4a18a5cc779edc60c6cee861debef297e"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/a5a0e4b587c7f2de4250ec965caf21b8fca172e0",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJlwQ7pCRC1aQ7uu5UhlAAAN78QAEt+AXHSB7GDjUp+BBPklQQA\nwG3M8pLThnBy56xS/9KCUcuYkHDg74/SiMVoy0U7LND/5QN19LsseemY/7+M3+s+\nFMx1ecmFMJvXhBZgTuBzU2M6jqWLt7+Tb9RJiaoNHnm/joKqGSPfLeS60scA+Ht6\nVPJ2cpANfnEe6LkqjV+0ySAuCoDRyStb4/pvjzDh/mlSQoStu1KK+DzMLdOXarJ7\nr9/DrjNlyFSSf44x59gSxF6hWULAnyUqFQ6ms+NqyxBSOgelPUOY31MJHWpGW8Mp\nvCBP3ymXBDd6iLo2vpS4jU0X8B6ry+nswwrZgVZABGUkv6nBVkqtGXcjqO/byEr7\nqCZBv7wQL1mSlTsbl4DUUVPNXM7xzLco9CO2+FFrPEHdDmEVNq27Xk/VuhMiz1t7\nzJCERXjhmVdKQhwOBUxeKZ51pHvAb7v+P0DwRJQvYdlezbAGdgqna7DVvk/XhQqc\nc2a56sXiOGeQZxSjUk4zRDLMqt5SF4rxMJDNcOUZIXlAV+wX6dt3LywH4A1gQ/Yh\nUKcDZkNqm681QmC+EsUvAU3t+cXhwTVMM6P/F0eFU/0+U2ZwJHr5vaTWsMguKbmB\nqb2qkrp/RThvMBwAL0XeH/fJYypJaeBwmHg7VMeMEktE+kHcfiE3pq5AUUlA45Gh\n3o8c2nEyVV9GeG4QAGpY\n=+rug\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 30eeeaa4a18a5cc779edc60c6cee861debef297e\nparent 96b22fa18c00831656ee4b286bf1c9062459b00a\nauthor dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> 1707151081 +0000\ncommitter GitHub <noreply@github.com> 1707151081 +0000\n\nBump github/codeql-action from 3.23.0 to 3.24.0\n\nBumps [github/codeql-action](https://github.com/github/codeql-action) from 3.23.0 to 3.24.0.\n- [Release notes](https://github.com/github/codeql-action/releases)\n- [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/github/codeql-action/compare/e5f05b81d5b6ff8cfa111c80c22c5fd02a384118...e8893c57a1f3a2b659b6b55564fdfdbbd2982911)\n\n---\nupdated-dependencies:\n- dependency-name: github/codeql-action\n  dependency-type: direct:production\n  update-type: version-update:semver-minor\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/a5a0e4b587c7f2de4250ec965caf21b8fca172e0",
      "html_url": "https://github.com/psf/requests/commit/a5a0e4b587c7f2de4250ec965caf21b8fca172e0",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/a5a0e4b587c7f2de4250ec965caf21b8fca172e0/comments",
      "author": {
        "login": "dependabot[bot]",
        "id": 49699333,
        "node_id": "MDM6Qm90NDk2OTkzMzM=",
        "avatar_url": "https://avatars.githubusercontent.com/in/29110?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/dependabot%5Bbot%5D",
        "html_url": "https://github.com/apps/dependabot",
        "followers_url": "https://api.github.com/users/dependabot%5Bbot%5D/followers",
        "following_url": "https://api.github.com/users/dependabot%5Bbot%5D/following{/other_user}",
        "gists_url": "https://api.github.com/users/dependabot%5Bbot%5D/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/dependabot%5Bbot%5D/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/dependabot%5Bbot%5D/subscriptions",
        "organizations_url": "https://api.github.com/users/dependabot%5Bbot%5D/orgs",
        "repos_url": "https://api.github.com/users/dependabot%5Bbot%5D/repos",
        "events_url": "https://api.github.com/users/dependabot%5Bbot%5D/events{/privacy}",
        "received_events_url": "https://api.github.com/users/dependabot%5Bbot%5D/received_events",
        "type": "Bot",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "96b22fa18c00831656ee4b286bf1c9062459b00a",
          "url": "https://api.github.com/repos/psf/requests/commits/96b22fa18c00831656ee4b286bf1c9062459b00a",
          "html_url": "https://github.com/psf/requests/commit/96b22fa18c00831656ee4b286bf1c9062459b00a"
        }
      ]
    },
    {
      "sha": "4f3f189d6b7d2a19ff73dfb4a3e39713d4abe01a",
      "node_id": "C_kwDOABTKOtoAKDRmM2YxODlkNmI3ZDJhMTlmZjczZGZiNGEzZTM5NzEzZDRhYmUwMWE",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2024-02-06T02:54:26Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-02-06T02:54:26Z"
        },
        "message": "Merge pull request #6632 from psf/dependabot/github_actions/github/codeql-action-3.24.0\n\nBump github/codeql-action from 3.23.0 to 3.24.0",
        "tree": {
          "sha": "30eeeaa4a18a5cc779edc60c6cee861debef297e",
          "url": "https://api.github.com/repos/psf/requests/git/trees/30eeeaa4a18a5cc779edc60c6cee861debef297e"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/4f3f189d6b7d2a19ff73dfb4a3e39713d4abe01a",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJlwZ9iCRC1aQ7uu5UhlAAA+LoQAGbr7SZK0YLAXEjxRDgr0AbE\nM+jTKePy797R1rI48ezv/+tI3GZW/Sej0jHYmPSjjmwI5whH5xE9Whv7HUKAmEio\nql+9Nn8Fn6WK/W/eiXLY0+vXI2rHq+3mTgQDSXrO/b0v2HXU7WMLsFw24aZmZQY1\nL7XlCj9Lg27sZrTjDhYah1thC+Clz/EtZDDQ6j9TV55BReQkmym8c+pkAaN2fGsz\nx2pgf3mOUdKSy4Eepb8pMnxBi7qP4wBoNdZ7wZtYHcRhozdEUwQPvbH5tiXbIrts\nIS2Zyp1QCbl3HBuL6GbJz8222dIYvUPmUrrwW9d+KkRK2WmbfBo9IM8XGPrERznH\nOBEoyoqFR/NtgGPnHjBX1tDS3R2SrgMtim0Of8RmsgSDZ3TcJhe1p0G81Jk5ZDdj\n7LY1xgH2uPxELS14v3rlUn8D/hKVq8ChrZtNxEpOrPHcmSUY6LStfrmvvm1ptyL/\nA4JHxJxM9jDooCD6eKpMhPF5lQPWl5R3yuJldqqGHQoeMXzSLQ03njUlPFN2OMqB\n5RgOsWY9g5U9CHNUJMfzwVrnxkD5bnBVgrTVnFyjD0Q5w4n2fn4FIi1pyjugdnLY\n9pYWTDaED5Fly8ePlFkImI9tzYkb8wL78vY31Csk6Sz1t40VbNJoEuoqyQst8fOQ\nW7iOwRjz0u9BRPU2NBDt\n=52Gw\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 30eeeaa4a18a5cc779edc60c6cee861debef297e\nparent 96b22fa18c00831656ee4b286bf1c9062459b00a\nparent a5a0e4b587c7f2de4250ec965caf21b8fca172e0\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1707188066 -0600\ncommitter GitHub <noreply@github.com> 1707188066 -0600\n\nMerge pull request #6632 from psf/dependabot/github_actions/github/codeql-action-3.24.0\n\nBump github/codeql-action from 3.23.0 to 3.24.0",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/4f3f189d6b7d2a19ff73dfb4a3e39713d4abe01a",
      "html_url": "https://github.com/psf/requests/commit/4f3f189d6b7d2a19ff73dfb4a3e39713d4abe01a",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/4f3f189d6b7d2a19ff73dfb4a3e39713d4abe01a/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "96b22fa18c00831656ee4b286bf1c9062459b00a",
          "url": "https://api.github.com/repos/psf/requests/commits/96b22fa18c00831656ee4b286bf1c9062459b00a",
          "html_url": "https://github.com/psf/requests/commit/96b22fa18c00831656ee4b286bf1c9062459b00a"
        },
        {
          "sha": "a5a0e4b587c7f2de4250ec965caf21b8fca172e0",
          "url": "https://api.github.com/repos/psf/requests/commits/a5a0e4b587c7f2de4250ec965caf21b8fca172e0",
          "html_url": "https://github.com/psf/requests/commit/a5a0e4b587c7f2de4250ec965caf21b8fca172e0"
        }
      ]
    },
    {
      "sha": "6106a63eb6c0fa490efa73d44388ac25b1b08af4",
      "node_id": "C_kwDOABTKOtoAKDYxMDZhNjNlYjZjMGZhNDkwZWZhNzNkNDQzODhhYzI1YjFiMDhhZjQ",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2024-02-20T19:58:35Z"
        },
        "committer": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2024-02-20T19:58:35Z"
        },
        "message": "Cleanup defunct links from community docs page",
        "tree": {
          "sha": "b3dea3db6e66ec7eff971792816d74499a17c56a",
          "url": "https://api.github.com/repos/psf/requests/git/trees/b3dea3db6e66ec7eff971792816d74499a17c56a"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/6106a63eb6c0fa490efa73d44388ac25b1b08af4",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/6106a63eb6c0fa490efa73d44388ac25b1b08af4",
      "html_url": "https://github.com/psf/requests/commit/6106a63eb6c0fa490efa73d44388ac25b1b08af4",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/6106a63eb6c0fa490efa73d44388ac25b1b08af4/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "4f3f189d6b7d2a19ff73dfb4a3e39713d4abe01a",
          "url": "https://api.github.com/repos/psf/requests/commits/4f3f189d6b7d2a19ff73dfb4a3e39713d4abe01a",
          "html_url": "https://github.com/psf/requests/commit/4f3f189d6b7d2a19ff73dfb4a3e39713d4abe01a"
        }
      ]
    },
    {
      "sha": "46c1a3d8c83754167280e3479bc3ac43b4900ba6",
      "node_id": "C_kwDOABTKOtoAKDQ2YzFhM2Q4YzgzNzU0MTY3MjgwZTM0NzliYzNhYzQzYjQ5MDBiYTY",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2024-02-20T20:04:33Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-02-20T20:04:33Z"
        },
        "message": "Merge pull request #6640 from nateprewitt/community_docs_cleanup\n\nCleanup defunct links from community docs page",
        "tree": {
          "sha": "b3dea3db6e66ec7eff971792816d74499a17c56a",
          "url": "https://api.github.com/repos/psf/requests/git/trees/b3dea3db6e66ec7eff971792816d74499a17c56a"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/46c1a3d8c83754167280e3479bc3ac43b4900ba6",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJl1QXRCRC1aQ7uu5UhlAAAShIQAE5sH5KB4n//52BvY2JfoPQw\nMKS0GgwIruJ0jnRPdrNqdxUKnWfhuEzDB49cVObBhxxTLEBHym3/Mmsr2SWUxx/3\nUDUzUGzE2OevV1FSqPK4ndEsWZ/ZECqYmQB4fo30BAgX27n524yD6pLSK7YukM+T\njlD80Zo8EQlNQwjQTwZG0bkXIyXWjbEuUHAmKhFIRbHjFKA1uvAiVcKRg8Hk6jTs\n2btFFbneff7IyTgRYUqiO+8U3g2FpjM+MLD/w7Yro8AW5TQIOmRwfLD7wgbI/ZaP\nGxZXgsSQN+0YNUr1gYe0EEhSHLP42IAdFIp85CZJWSEA9FK79E/iiuYa4SQnFi7r\nc1qt40Dyz4nul+wXKAdRxTxNBlzK5oUY64WLY0XM9O+phnSrc3PB6dEggyEzDCFJ\nF6dtSwPy9XuO4lKQrbLC4fZACoMlXm5w1nHQ4YsfIJyTyv1mYOZzmWhrcAc9OuoO\nlgOklBDCV/K4NOfun0rlDGHVlYqcPb5feyC00HXwWIVj5gLRJXbTPVfRMGBvD2QE\nJyhbi9BgxGYaNt/Kr/4GIJwNBQ3SZcTe51Yt4I6GeV0LvrPH77GRGJ2aiYzpH53U\nprUwWXlRpADtqVdjmdVFFjzI/nR3h7z1Dv2Py22aeKrOQhpehP5mOMUQ/JWdmDrH\nZrpUF56PskR1trfrUgT2\n=C34S\n-----END PGP SIGNATURE-----\n",
          "payload": "tree b3dea3db6e66ec7eff971792816d74499a17c56a\nparent 4f3f189d6b7d2a19ff73dfb4a3e39713d4abe01a\nparent 6106a63eb6c0fa490efa73d44388ac25b1b08af4\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1708459473 -0600\ncommitter GitHub <noreply@github.com> 1708459473 -0600\n\nMerge pull request #6640 from nateprewitt/community_docs_cleanup\n\nCleanup defunct links from community docs page",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/46c1a3d8c83754167280e3479bc3ac43b4900ba6",
      "html_url": "https://github.com/psf/requests/commit/46c1a3d8c83754167280e3479bc3ac43b4900ba6",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/46c1a3d8c83754167280e3479bc3ac43b4900ba6/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "4f3f189d6b7d2a19ff73dfb4a3e39713d4abe01a",
          "url": "https://api.github.com/repos/psf/requests/commits/4f3f189d6b7d2a19ff73dfb4a3e39713d4abe01a",
          "html_url": "https://github.com/psf/requests/commit/4f3f189d6b7d2a19ff73dfb4a3e39713d4abe01a"
        },
        {
          "sha": "6106a63eb6c0fa490efa73d44388ac25b1b08af4",
          "url": "https://api.github.com/repos/psf/requests/commits/6106a63eb6c0fa490efa73d44388ac25b1b08af4",
          "html_url": "https://github.com/psf/requests/commit/6106a63eb6c0fa490efa73d44388ac25b1b08af4"
        }
      ]
    },
    {
      "sha": "5fc10bf1f5185f330f8471c738ce753b3e231008",
      "node_id": "C_kwDOABTKOtoAKDVmYzEwYmYxZjUxODVmMzMwZjg0NzFjNzM4Y2U3NTNiM2UyMzEwMDg",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2024-02-20T21:37:25Z"
        },
        "committer": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2024-02-20T21:37:25Z"
        },
        "message": "Fix httpbin pin for test suite",
        "tree": {
          "sha": "2ee69dc82bfc147ec7fac4049e6fb1d64a280096",
          "url": "https://api.github.com/repos/psf/requests/git/trees/2ee69dc82bfc147ec7fac4049e6fb1d64a280096"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/5fc10bf1f5185f330f8471c738ce753b3e231008",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/5fc10bf1f5185f330f8471c738ce753b3e231008",
      "html_url": "https://github.com/psf/requests/commit/5fc10bf1f5185f330f8471c738ce753b3e231008",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/5fc10bf1f5185f330f8471c738ce753b3e231008/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "46c1a3d8c83754167280e3479bc3ac43b4900ba6",
          "url": "https://api.github.com/repos/psf/requests/commits/46c1a3d8c83754167280e3479bc3ac43b4900ba6",
          "html_url": "https://github.com/psf/requests/commit/46c1a3d8c83754167280e3479bc3ac43b4900ba6"
        }
      ]
    },
    {
      "sha": "28855fd43a68bf26fec23aa9b548239e13255edf",
      "node_id": "C_kwDOABTKOtoAKDI4ODU1ZmQ0M2E2OGJmMjZmZWMyM2FhOWI1NDgyMzllMTMyNTVlZGY",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2024-02-20T21:58:26Z"
        },
        "committer": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2024-02-20T21:58:26Z"
        },
        "message": "Update supported copies of PyPy\n\nDropped support for pypy-3.7 and pypy-3.8 which are no longer maintained by upstream.\nAdded support for pypy-3.10.",
        "tree": {
          "sha": "f629cf651a76cec903fbe2a52c4ff8f0b89297d7",
          "url": "https://api.github.com/repos/psf/requests/git/trees/f629cf651a76cec903fbe2a52c4ff8f0b89297d7"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/28855fd43a68bf26fec23aa9b548239e13255edf",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/28855fd43a68bf26fec23aa9b548239e13255edf",
      "html_url": "https://github.com/psf/requests/commit/28855fd43a68bf26fec23aa9b548239e13255edf",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/28855fd43a68bf26fec23aa9b548239e13255edf/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "5fc10bf1f5185f330f8471c738ce753b3e231008",
          "url": "https://api.github.com/repos/psf/requests/commits/5fc10bf1f5185f330f8471c738ce753b3e231008",
          "html_url": "https://github.com/psf/requests/commit/5fc10bf1f5185f330f8471c738ce753b3e231008"
        }
      ]
    },
    {
      "sha": "8fa4302322f1a34053683b7f4c0d2ee5ef0ebd64",
      "node_id": "C_kwDOABTKOtoAKDhmYTQzMDIzMjJmMWEzNDA1MzY4M2I3ZjRjMGQyZWU1ZWYwZWJkNjQ",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2024-02-20T23:04:04Z"
        },
        "committer": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2024-02-20T23:04:38Z"
        },
        "message": "Update Sphinx to work with latest readthedocs requirements",
        "tree": {
          "sha": "04b3a53dbbda777a7364682eed57e824dcc68d48",
          "url": "https://api.github.com/repos/psf/requests/git/trees/04b3a53dbbda777a7364682eed57e824dcc68d48"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/8fa4302322f1a34053683b7f4c0d2ee5ef0ebd64",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/8fa4302322f1a34053683b7f4c0d2ee5ef0ebd64",
      "html_url": "https://github.com/psf/requests/commit/8fa4302322f1a34053683b7f4c0d2ee5ef0ebd64",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/8fa4302322f1a34053683b7f4c0d2ee5ef0ebd64/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "28855fd43a68bf26fec23aa9b548239e13255edf",
          "url": "https://api.github.com/repos/psf/requests/commits/28855fd43a68bf26fec23aa9b548239e13255edf",
          "html_url": "https://github.com/psf/requests/commit/28855fd43a68bf26fec23aa9b548239e13255edf"
        }
      ]
    },
    {
      "sha": "9439fad03848d882f68710fdb3d69eaf02ef21ca",
      "node_id": "C_kwDOABTKOtoAKDk0MzlmYWQwMzg0OGQ4ODJmNjg3MTBmZGIzZDY5ZWFmMDJlZjIxY2E",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2024-02-20T23:32:57Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-02-20T23:32:57Z"
        },
        "message": "Merge pull request #6641 from nateprewitt/fix_ci\n\nFix CI",
        "tree": {
          "sha": "04b3a53dbbda777a7364682eed57e824dcc68d48",
          "url": "https://api.github.com/repos/psf/requests/git/trees/04b3a53dbbda777a7364682eed57e824dcc68d48"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/9439fad03848d882f68710fdb3d69eaf02ef21ca",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJl1TapCRC1aQ7uu5UhlAAALl4QAKNwXRyzvLvra9AMW4gA2lqS\nXeQwuk5s3WLIAsw6NmcKXaN5UKms8sfKZB2Ycm2uiE1a+p5H5nxAKNQa3JAf8X5a\n37EoNZdJSIjVDVDOfUI0jcs8nOloYyIAVu9C261Nlh4g/2P5uxasRMEGDeBKLmyF\ndhh4uAcAxs6Y9jxH7bjRiO4T23Dje2Wec8VF7gMdCrPOiS9bqNP6043/8urfjx6P\nfGb2Q9pRIngwbqHu/gwvGYVqyIcL5oCAt811jrH+ymMNzgFNzeuX19U1wLgd4DZP\nocQ0qELu3cRSD71pbBJsZO93pIxMccC0+yr0X78Xk5+0Z+8X40FmPcwGbWVLecwp\navzM2EQCOO9O9BQ8+5UjGsuEEAP35RM10cgXByBwscohj93oO09DPcmXEqks61hX\nBSiLfvHpNLDpJNJQziVXBjW6sgj9XiwIAfNi5X8HanEh1aRrFANswMVY6awMC2Uk\nP0DdgCAR7cSZ7i6b5BmBW7fr3i2c9g55g7EA3zp0FpqRLbiRzQi17qU7IcxGzpKz\nvCSoBmHmJiSwmI9kHmuL6aE943xZxM5da6nQn5LvwPE2HWXsLWg3yWaJT0HC09V2\nAfFTlNn27YA5aNqxf2pDVdRlSCPr7zN4Fk8xWCulSXBuTLOWp2w9zkhSsco1cgF/\nsIq0yCdLSVgwqTFQSAJW\n=5B68\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 04b3a53dbbda777a7364682eed57e824dcc68d48\nparent 46c1a3d8c83754167280e3479bc3ac43b4900ba6\nparent 8fa4302322f1a34053683b7f4c0d2ee5ef0ebd64\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1708471977 -0600\ncommitter GitHub <noreply@github.com> 1708471977 -0600\n\nMerge pull request #6641 from nateprewitt/fix_ci\n\nFix CI",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/9439fad03848d882f68710fdb3d69eaf02ef21ca",
      "html_url": "https://github.com/psf/requests/commit/9439fad03848d882f68710fdb3d69eaf02ef21ca",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/9439fad03848d882f68710fdb3d69eaf02ef21ca/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "46c1a3d8c83754167280e3479bc3ac43b4900ba6",
          "url": "https://api.github.com/repos/psf/requests/commits/46c1a3d8c83754167280e3479bc3ac43b4900ba6",
          "html_url": "https://github.com/psf/requests/commit/46c1a3d8c83754167280e3479bc3ac43b4900ba6"
        },
        {
          "sha": "8fa4302322f1a34053683b7f4c0d2ee5ef0ebd64",
          "url": "https://api.github.com/repos/psf/requests/commits/8fa4302322f1a34053683b7f4c0d2ee5ef0ebd64",
          "html_url": "https://github.com/psf/requests/commit/8fa4302322f1a34053683b7f4c0d2ee5ef0ebd64"
        }
      ]
    },
    {
      "sha": "58cea7a7282999adafdc19a4e82e2d09207ab568",
      "node_id": "C_kwDOABTKOtoAKDU4Y2VhN2E3MjgyOTk5YWRhZmRjMTlhNGU4MmUyZDA5MjA3YWI1Njg",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2024-02-20T23:22:20Z"
        },
        "committer": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2024-02-20T23:37:46Z"
        },
        "message": "Drop support for CPython 3.7",
        "tree": {
          "sha": "4a14378b74ac3d965f13e05d27670223b5739190",
          "url": "https://api.github.com/repos/psf/requests/git/trees/4a14378b74ac3d965f13e05d27670223b5739190"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/58cea7a7282999adafdc19a4e82e2d09207ab568",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/58cea7a7282999adafdc19a4e82e2d09207ab568",
      "html_url": "https://github.com/psf/requests/commit/58cea7a7282999adafdc19a4e82e2d09207ab568",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/58cea7a7282999adafdc19a4e82e2d09207ab568/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "9439fad03848d882f68710fdb3d69eaf02ef21ca",
          "url": "https://api.github.com/repos/psf/requests/commits/9439fad03848d882f68710fdb3d69eaf02ef21ca",
          "html_url": "https://github.com/psf/requests/commit/9439fad03848d882f68710fdb3d69eaf02ef21ca"
        }
      ]
    },
    {
      "sha": "7a13c041dbef42f9f3feb14110f02626f6892e9a",
      "node_id": "C_kwDOABTKOtoAKDdhMTNjMDQxZGJlZjQyZjlmM2ZlYjE0MTEwZjAyNjI2ZjY4OTJlOWE",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2024-02-20T23:44:43Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-02-20T23:44:43Z"
        },
        "message": "Merge pull request #6642 from nateprewitt/drop_python_37\n\nDrop support for CPython 3.7",
        "tree": {
          "sha": "4a14378b74ac3d965f13e05d27670223b5739190",
          "url": "https://api.github.com/repos/psf/requests/git/trees/4a14378b74ac3d965f13e05d27670223b5739190"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/7a13c041dbef42f9f3feb14110f02626f6892e9a",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJl1TlrCRC1aQ7uu5UhlAAAQqwQAGqTBYa0VNmvJN754T7ddaAE\nE3AGDPl6kYYH+Vt1tYelnRcm2sBS1+yTDDCgk0YWN12245i5txo/Po4jZp2tiqXW\nMJhK6/D/Pv5H/DMF9La5PwmN7j9n2ICIt3wZLPovmEDwqfBOi4vWwiP9ejqIKl8Z\nVvE1CwBuPfZcOoqBl4PzpHntJ5RnSJKT1aCsolSF1W0JqXoAbjoipTZXLRrukY7x\nTcUxEmnEiI5tHmbBVkzzwZTJlL5TH8rCftTBEPv8uL+ztdRHLlk6AcAlAM/tKF5w\nMEEThIsTYG7pNqrEtTBgcyoQpqg+rJVrUzCpnqPec0AeVx0QS49GbdNz6L0Jwuyz\nGhTuP3IXmx7CrSEFkkiAhyiqX33B3vqaQTx0GDfL9CSwU6rncaRii4ak3z/66+GE\n/vB5i44qYho5rU74Y4MUzQHuGcG+8WYsAM7N5m794JWGw5cTjhcsF8Dp7HFNUGLU\njhkRxjkX7Ac+qBoF5teIPg/8ZKOXfDrVhrJX2kFxiFPKDMIqnEh33+FH0OQi7RME\nZeJvUVy8JAowh6HOUMTnZiQ/nFGcPDH61a06GOlDuA447tuD45DtaaJHk33Sm4fD\nnuX3Pm00cImReo56R0n/3OvgJcjZQ1Bsi/THZNdyavgOAg4nPl9VXDgXDns4PNjz\nJUhcMMXroLYgAzERMCnx\n=n9vd\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 4a14378b74ac3d965f13e05d27670223b5739190\nparent 9439fad03848d882f68710fdb3d69eaf02ef21ca\nparent 58cea7a7282999adafdc19a4e82e2d09207ab568\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1708472683 -0800\ncommitter GitHub <noreply@github.com> 1708472683 -0800\n\nMerge pull request #6642 from nateprewitt/drop_python_37\n\nDrop support for CPython 3.7",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/7a13c041dbef42f9f3feb14110f02626f6892e9a",
      "html_url": "https://github.com/psf/requests/commit/7a13c041dbef42f9f3feb14110f02626f6892e9a",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/7a13c041dbef42f9f3feb14110f02626f6892e9a/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "9439fad03848d882f68710fdb3d69eaf02ef21ca",
          "url": "https://api.github.com/repos/psf/requests/commits/9439fad03848d882f68710fdb3d69eaf02ef21ca",
          "html_url": "https://github.com/psf/requests/commit/9439fad03848d882f68710fdb3d69eaf02ef21ca"
        },
        {
          "sha": "58cea7a7282999adafdc19a4e82e2d09207ab568",
          "url": "https://api.github.com/repos/psf/requests/commits/58cea7a7282999adafdc19a4e82e2d09207ab568",
          "html_url": "https://github.com/psf/requests/commit/58cea7a7282999adafdc19a4e82e2d09207ab568"
        }
      ]
    },
    {
      "sha": "382fc2c0c6c0ef0874bc65bc1175f97c073e5086",
      "node_id": "C_kwDOABTKOtoAKDM4MmZjMmMwYzZjMGVmMDg3NGJjNjViYzExNzVmOTdjMDczZTUwODY",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2024-02-22T20:27:37Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-02-22T20:27:37Z"
        },
        "message": "Merge pull request #6629 from Tarty/fix-6628-jsondecode-error-not-deserializable\n\nFix #6628 - JSONDecodeError are not deserializable",
        "tree": {
          "sha": "6e77739021025919bcae78f397c4768806b35116",
          "url": "https://api.github.com/repos/psf/requests/git/trees/6e77739021025919bcae78f397c4768806b35116"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/382fc2c0c6c0ef0874bc65bc1175f97c073e5086",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJl1645CRC1aQ7uu5UhlAAAbr0QALBxtF6CbObJyJkYp7Hr27iP\nCSqP+SLz15bTOhyUrO3+x69amAiMCo18ztNt/30aYCUbx9HMIRaNyJrWhJ39lslD\nfk8RB+32JF9GqzN5AbJYabJpvD7PXmi72oGHjTw2hTp4O+GhCfWAvrNDCxohyYV1\nBDC0+csJunMOtycVeU1EXzDje+VGWk4FsKwZQGWNCqxRQDU1BpT/3t8PK1UfJxGG\ndg0bxqQfTzHl2fclvqgGxVscjf1kTHQ0H7JIOEephjg/XlCLLXd/5HqvkgqnYIsZ\nhThz/jwQ/NddV3oy+69s15jjR0OFUxjqdrogxhCaunfDlFD7jwEGRpGyrNZgJMFE\nyOgJM9G8xYujF/SNKx76GvqZVBbO/I1iqv1Xnf3JWwuOqV2qlvpAJuM/qcDB6Kgt\n7/Y4hlscFRb0EEILtBgV/ggmnk7XtE7VpjQcThoXr3JmR1NDedeRJeb48R11mb3S\nz9WFYzXKz12GzmA1IRhP5bAD7QLvsbmbH9FrtHzqLkHm0M7FV1ya1ep/uYDoYuDz\ngmLsPueZOyaXCHT1PZ5Usz3rN1jLOIXTnDAnaWs9BEexSIpu+WKv9Wr+YrA91ck4\nWXuuZH9G3IrSZIp3h1dh8959vlP/RBeqoJotoNxsSfPlsQVksUMUIXNz53F+7XB+\naP5rXKBRh54Ww0/0rMGr\n=p5FF\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 6e77739021025919bcae78f397c4768806b35116\nparent 7a13c041dbef42f9f3feb14110f02626f6892e9a\nparent 3ff3ff21dd45957c9e143cd500291959bb15f690\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1708633657 -0800\ncommitter GitHub <noreply@github.com> 1708633657 -0800\n\nMerge pull request #6629 from Tarty/fix-6628-jsondecode-error-not-deserializable\n\nFix #6628 - JSONDecodeError are not deserializable",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/382fc2c0c6c0ef0874bc65bc1175f97c073e5086",
      "html_url": "https://github.com/psf/requests/commit/382fc2c0c6c0ef0874bc65bc1175f97c073e5086",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/382fc2c0c6c0ef0874bc65bc1175f97c073e5086/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "7a13c041dbef42f9f3feb14110f02626f6892e9a",
          "url": "https://api.github.com/repos/psf/requests/commits/7a13c041dbef42f9f3feb14110f02626f6892e9a",
          "html_url": "https://github.com/psf/requests/commit/7a13c041dbef42f9f3feb14110f02626f6892e9a"
        },
        {
          "sha": "3ff3ff21dd45957c9e143cd500291959bb15f690",
          "url": "https://api.github.com/repos/psf/requests/commits/3ff3ff21dd45957c9e143cd500291959bb15f690",
          "html_url": "https://github.com/psf/requests/commit/3ff3ff21dd45957c9e143cd500291959bb15f690"
        }
      ]
    },
    {
      "sha": "60389df6d69ce833164696dcf36cbb43336d3426",
      "node_id": "C_kwDOABTKOtoAKDYwMzg5ZGY2ZDY5Y2U4MzMxNjQ2OTZkY2YzNmNiYjQzMzM2ZDM0MjY",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2024-02-22T01:09:48Z"
        },
        "committer": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2024-02-23T00:36:44Z"
        },
        "message": "Trim excess leading path separators\n\nA URL with excess leading / (path-separator)s would cause urllib3 to\nattempt to reparse the request-uri as a full URI with a host and port.\nThis bypasses that logic in ConnectionPool.urlopen by replacing these\nleading /s with just a single /.\n\nCloses #6643",
        "tree": {
          "sha": "8a63f9d4c3c4d580bfa3b4a93711f7f2b556683e",
          "url": "https://api.github.com/repos/psf/requests/git/trees/8a63f9d4c3c4d580bfa3b4a93711f7f2b556683e"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/60389df6d69ce833164696dcf36cbb43336d3426",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\niQIzBAABCAAdFiEEgSpQDY8Q9shZFt4GZW0zleSpeRoFAmXX6J0ACgkQZW0zleSp\neRom+Q//S/lQjOiWLTFksqI6rpBwEpYoPD21BHccDOGRG5ihWyOA8FvfBCtbRith\nEA4VQS8rjFecw3oL5XJ5jjPJ8fdX7e3EbxtQ3W0OjIouF7JmEL6Wb54HK6k4QXue\nBco8BzHKPI4UwHeyQmXmYDj+jEnuA+CP9khZUNUu+HYECSiuNPvpBnrNOY5FEoQ5\ntOL2J+EgzwhDAE/aOjroYOnee2NVfWeL+j2JADD5cln5vGB64vdaqSYWvjCLXqv1\nAkRn46xQmZeompXv+uvHcsfozlVh+ASFqgE8jUBF7pCa+4z11W0TmLO7s72Cm8+5\nMuhZ2znUjTIRvrysnCxkhY7Ydg2BhPJueMEXeJ900Pbmh+Pk9iH8uUW0HnIFF77N\nIn+8O5mqTlxQ7IOm/JTH7UxMIIiJcl1aL7eoaqsU7dym6Y68tWoIvOB8xFw9oSLy\n2zkBV1MMjYxmm6ubkT97UvZYFZFP5eVnMyzkW2fwhf3MS00Y7qPsTAr55w3hR9/e\nSShVemuk1suTBPr/3PpCpsoG0uaUbmKs/6B+b7qSh3etbkVQ9cf8ryNQXYGJeTWh\nstOJbOHGzVu66LMLaByQXgQ1jnblxkNxQaNO5hXXuJxVXEfsawJuqi76Dn358wG/\nDPDQEuCSJq01nc+Fa2jVluF6U+xib2K4BbuHdlgSORfy2vP+25o=\n=Umdn\n-----END PGP SIGNATURE-----",
          "payload": "tree 8a63f9d4c3c4d580bfa3b4a93711f7f2b556683e\nparent 7a13c041dbef42f9f3feb14110f02626f6892e9a\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1708564188 -0600\ncommitter Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1708648604 -0600\n\nTrim excess leading path separators\n\nA URL with excess leading / (path-separator)s would cause urllib3 to\nattempt to reparse the request-uri as a full URI with a host and port.\nThis bypasses that logic in ConnectionPool.urlopen by replacing these\nleading /s with just a single /.\n\nCloses #6643\n",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/60389df6d69ce833164696dcf36cbb43336d3426",
      "html_url": "https://github.com/psf/requests/commit/60389df6d69ce833164696dcf36cbb43336d3426",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/60389df6d69ce833164696dcf36cbb43336d3426/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "7a13c041dbef42f9f3feb14110f02626f6892e9a",
          "url": "https://api.github.com/repos/psf/requests/commits/7a13c041dbef42f9f3feb14110f02626f6892e9a",
          "html_url": "https://github.com/psf/requests/commit/7a13c041dbef42f9f3feb14110f02626f6892e9a"
        }
      ]
    },
    {
      "sha": "3587a5f869ea7ae2ba6b20d281d810b65aa2418e",
      "node_id": "C_kwDOABTKOtoAKDM1ODdhNWY4NjllYTdhZTJiYTZiMjBkMjgxZDgxMGI2NWFhMjQxOGU",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2024-02-23T00:49:42Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-02-23T00:49:42Z"
        },
        "message": "Merge pull request #6644 from sigmavirus24/bug/6643\n\nTrim excess leading path separators",
        "tree": {
          "sha": "ec9bd84f7cfdf7cae41fa97f0cef4d62833bccc2",
          "url": "https://api.github.com/repos/psf/requests/git/trees/ec9bd84f7cfdf7cae41fa97f0cef4d62833bccc2"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/3587a5f869ea7ae2ba6b20d281d810b65aa2418e",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJl1+umCRC1aQ7uu5UhlAAAtkEQAD6vfz65D9J755Ld6rpTHNft\nBXHmpJZs0x8EkdktliVJqkQ/sGpH9DkS4gatl8wY0BZ+lj9TvsbtxV0KRFtwCZ0p\nX/7FV2T/CDKWc4dkYUatMPGduDxuHSilJAvU3BV2hpHE9X6i2lcp3WM8+bIZeUjY\nC3RssJN6gxe5Vwb4SEWzVncXqgHZQQe+CJcBBflOFJWbI5+1+QxYjgvs5Copjm1U\nMX8+tH5YiCl3yzOUis2bsA6px5+Y+S7FNnxGqb8uLAUGAXTztrwFLOfxxT0vR+e/\nMMzlqqvEP1GBOMlxt6DgBpHp4gnt2eMexHJdVd/67b/P1JTG3dpr9Ik9P6SCGhzU\nZ6tWvWl+o/YYk5RXTn8W5LI4D4pTPjsQK6akDpSHvmj/g4x209iZ2Amt3123Fk0m\nFz7X1z5PSDoCzKJNP+bgCbpWYZpbO5Tpbh7q5fIw7k6htgb36QtNnOE5geiIsEkU\nNdSgRn9phJfl42yufH5uTrkccGefPOZc67XmFTQQbjQxPnMRJDDiJTQdlZHkcG6R\n1Ri67Uo6HSO5jFbelG3qIxP6uvAyAp+IIsNVPvRMNrIamQ3JnwZl2kn92TWKW3wW\nCVZxJQdElOOzC6jt/4+L6k5NvK8q2DnDaWZmApL5m3RvJ8lxEpNCQIyv3G3dMrg+\nHgL3iTqJE0MH0+H7xCqX\n=ufO+\n-----END PGP SIGNATURE-----\n",
          "payload": "tree ec9bd84f7cfdf7cae41fa97f0cef4d62833bccc2\nparent 382fc2c0c6c0ef0874bc65bc1175f97c073e5086\nparent 60389df6d69ce833164696dcf36cbb43336d3426\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1708649382 -0600\ncommitter GitHub <noreply@github.com> 1708649382 -0600\n\nMerge pull request #6644 from sigmavirus24/bug/6643\n\nTrim excess leading path separators",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/3587a5f869ea7ae2ba6b20d281d810b65aa2418e",
      "html_url": "https://github.com/psf/requests/commit/3587a5f869ea7ae2ba6b20d281d810b65aa2418e",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/3587a5f869ea7ae2ba6b20d281d810b65aa2418e/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "382fc2c0c6c0ef0874bc65bc1175f97c073e5086",
          "url": "https://api.github.com/repos/psf/requests/commits/382fc2c0c6c0ef0874bc65bc1175f97c073e5086",
          "html_url": "https://github.com/psf/requests/commit/382fc2c0c6c0ef0874bc65bc1175f97c073e5086"
        },
        {
          "sha": "60389df6d69ce833164696dcf36cbb43336d3426",
          "url": "https://api.github.com/repos/psf/requests/commits/60389df6d69ce833164696dcf36cbb43336d3426",
          "html_url": "https://github.com/psf/requests/commit/60389df6d69ce833164696dcf36cbb43336d3426"
        }
      ]
    },
    {
      "sha": "b8be93a721792deeadd2f498b8f77cf610e7765f",
      "node_id": "C_kwDOABTKOtoAKGI4YmU5M2E3MjE3OTJkZWVhZGQyZjQ5OGI4Zjc3Y2Y2MTBlNzc2NWY",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2024-02-23T00:53:25Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-02-23T00:53:25Z"
        },
        "message": "Merge pull request #6589 from bruceadams/super_len_str_utf-8\n\nEnhance `super_len` to count encoded bytes for str",
        "tree": {
          "sha": "809f4a2afcfd5bb41393b70aee5d09dc66ef3d8b",
          "url": "https://api.github.com/repos/psf/requests/git/trees/809f4a2afcfd5bb41393b70aee5d09dc66ef3d8b"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/b8be93a721792deeadd2f498b8f77cf610e7765f",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJl1+yFCRC1aQ7uu5UhlAAAqeYQAJLwW/UEc0PSZpA3ZxyTGpFu\nCg6pKrFQiBL1zF7pQlsqY3/7lsz8/L7fgkYKP3QGyR2ve8KExRqxJtnegiCXyLtI\nXbzDHWEv/fx0UAKoevVNueAbGfP2WFzPLQbsOAZQEaJWWky05uLEA5jNH4mFv/kF\nGRGvRHrXBnXnPd3T3T4kIHKGPkXJ7LakcSRZVnLlAyerTZ4OgiVyhSWAcgYDI5US\ns/AbXlxJVzLJ2TchmoLd3GcOxPO753nHDEGhCCRfqpycHUk6R2j887a5U7ibsmf9\nVgIsvdzebFWUL/8ooRYNRESxd89y9BkWCbL733q5kwpmWfplhhlDjA+1P70mhv9o\naSDJKcNthoK5sPXIxMT8D0E61WzYA8UXnUgQfYB4ZL/WoKV1rXMaGYmnmEKovcBc\nbbh/DhQvEMK6wJu1aPcXMDc1zyn6Byiv5jLsPLJ/0nRTPcyvYp0xhRGgBNN2j3/e\nXap3e9hC6jbnkS0vpH0v644IVwQTUM3S3eVlapEN7I/7HOV2W5js9yaltsCDsIbZ\nTq16Gg2QHRENaAKaHrZYcQpBiCESh8N4VORk50yfldQIQs7oFiGp7KPdB3T/bu1j\nH3kf+MGZY4IoVAjkRytvbL+Jq3EVy8MvTU0ayBqG5bvf7f79P/XWJir6gzaUe0mI\npC0WpTmFLLno+LXWVHcY\n=V/+E\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 809f4a2afcfd5bb41393b70aee5d09dc66ef3d8b\nparent 3587a5f869ea7ae2ba6b20d281d810b65aa2418e\nparent 3fd309a5c14e4cfbd96bea6c8e71b4958fe090bb\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1708649605 -0600\ncommitter GitHub <noreply@github.com> 1708649605 -0600\n\nMerge pull request #6589 from bruceadams/super_len_str_utf-8\n\nEnhance `super_len` to count encoded bytes for str",
          "verified_at": "2024-11-05T16:16:04Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/b8be93a721792deeadd2f498b8f77cf610e7765f",
      "html_url": "https://github.com/psf/requests/commit/b8be93a721792deeadd2f498b8f77cf610e7765f",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/b8be93a721792deeadd2f498b8f77cf610e7765f/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "3587a5f869ea7ae2ba6b20d281d810b65aa2418e",
          "url": "https://api.github.com/repos/psf/requests/commits/3587a5f869ea7ae2ba6b20d281d810b65aa2418e",
          "html_url": "https://github.com/psf/requests/commit/3587a5f869ea7ae2ba6b20d281d810b65aa2418e"
        },
        {
          "sha": "3fd309a5c14e4cfbd96bea6c8e71b4958fe090bb",
          "url": "https://api.github.com/repos/psf/requests/commits/3fd309a5c14e4cfbd96bea6c8e71b4958fe090bb",
          "html_url": "https://github.com/psf/requests/commit/3fd309a5c14e4cfbd96bea6c8e71b4958fe090bb"
        }
      ]
    },
    {
      "sha": "0ec2780c291107b6686996e4b38f3d63e076eda7",
      "node_id": "C_kwDOABTKOtoAKDBlYzI3ODBjMjkxMTA3YjY2ODY5OTZlNGIzOGYzZDYzZTA3NmVkYTc",
      "commit": {
        "author": {
          "name": "Elliot Ford",
          "email": "elliot.ford@astrazeneca.com",
          "date": "2023-11-24T10:37:33Z"
        },
        "committer": {
          "name": "Elliot Ford",
          "email": "elliot.ford@astrazeneca.com",
          "date": "2024-02-23T10:25:50Z"
        },
        "message": "update broken github pagination link",
        "tree": {
          "sha": "dc59cd6245c190a18b8bff50b053f659d690e6eb",
          "url": "https://api.github.com/repos/psf/requests/git/trees/dc59cd6245c190a18b8bff50b053f659d690e6eb"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/0ec2780c291107b6686996e4b38f3d63e076eda7",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/0ec2780c291107b6686996e4b38f3d63e076eda7",
      "html_url": "https://github.com/psf/requests/commit/0ec2780c291107b6686996e4b38f3d63e076eda7",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/0ec2780c291107b6686996e4b38f3d63e076eda7/comments",
      "author": {
        "login": "EFord36",
        "id": 20516159,
        "node_id": "MDQ6VXNlcjIwNTE2MTU5",
        "avatar_url": "https://avatars.githubusercontent.com/u/20516159?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/EFord36",
        "html_url": "https://github.com/EFord36",
        "followers_url": "https://api.github.com/users/EFord36/followers",
        "following_url": "https://api.github.com/users/EFord36/following{/other_user}",
        "gists_url": "https://api.github.com/users/EFord36/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/EFord36/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/EFord36/subscriptions",
        "organizations_url": "https://api.github.com/users/EFord36/orgs",
        "repos_url": "https://api.github.com/users/EFord36/repos",
        "events_url": "https://api.github.com/users/EFord36/events{/privacy}",
        "received_events_url": "https://api.github.com/users/EFord36/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "EFord36",
        "id": 20516159,
        "node_id": "MDQ6VXNlcjIwNTE2MTU5",
        "avatar_url": "https://avatars.githubusercontent.com/u/20516159?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/EFord36",
        "html_url": "https://github.com/EFord36",
        "followers_url": "https://api.github.com/users/EFord36/followers",
        "following_url": "https://api.github.com/users/EFord36/following{/other_user}",
        "gists_url": "https://api.github.com/users/EFord36/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/EFord36/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/EFord36/subscriptions",
        "organizations_url": "https://api.github.com/users/EFord36/orgs",
        "repos_url": "https://api.github.com/users/EFord36/repos",
        "events_url": "https://api.github.com/users/EFord36/events{/privacy}",
        "received_events_url": "https://api.github.com/users/EFord36/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "b8be93a721792deeadd2f498b8f77cf610e7765f",
          "url": "https://api.github.com/repos/psf/requests/commits/b8be93a721792deeadd2f498b8f77cf610e7765f",
          "html_url": "https://github.com/psf/requests/commit/b8be93a721792deeadd2f498b8f77cf610e7765f"
        }
      ]
    },
    {
      "sha": "d3b3399ece1f76387d323983638e0838c06e88ea",
      "node_id": "C_kwDOABTKOtoAKGQzYjMzOTllY2UxZjc2Mzg3ZDMyMzk4MzYzOGUwODM4YzA2ZTg4ZWE",
      "commit": {
        "author": {
          "name": "Elliot Ford",
          "email": "elliot.ford@astrazeneca.com",
          "date": "2023-11-24T10:44:09Z"
        },
        "committer": {
          "name": "Elliot Ford",
          "email": "elliot.ford@astrazeneca.com",
          "date": "2024-02-23T10:25:50Z"
        },
        "message": "update authors github link\n\nUpdate account link for original author which has changed.",
        "tree": {
          "sha": "10d4deecbbeb29465730385065ce9f317bc2ef83",
          "url": "https://api.github.com/repos/psf/requests/git/trees/10d4deecbbeb29465730385065ce9f317bc2ef83"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/d3b3399ece1f76387d323983638e0838c06e88ea",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/d3b3399ece1f76387d323983638e0838c06e88ea",
      "html_url": "https://github.com/psf/requests/commit/d3b3399ece1f76387d323983638e0838c06e88ea",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/d3b3399ece1f76387d323983638e0838c06e88ea/comments",
      "author": {
        "login": "EFord36",
        "id": 20516159,
        "node_id": "MDQ6VXNlcjIwNTE2MTU5",
        "avatar_url": "https://avatars.githubusercontent.com/u/20516159?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/EFord36",
        "html_url": "https://github.com/EFord36",
        "followers_url": "https://api.github.com/users/EFord36/followers",
        "following_url": "https://api.github.com/users/EFord36/following{/other_user}",
        "gists_url": "https://api.github.com/users/EFord36/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/EFord36/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/EFord36/subscriptions",
        "organizations_url": "https://api.github.com/users/EFord36/orgs",
        "repos_url": "https://api.github.com/users/EFord36/repos",
        "events_url": "https://api.github.com/users/EFord36/events{/privacy}",
        "received_events_url": "https://api.github.com/users/EFord36/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "EFord36",
        "id": 20516159,
        "node_id": "MDQ6VXNlcjIwNTE2MTU5",
        "avatar_url": "https://avatars.githubusercontent.com/u/20516159?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/EFord36",
        "html_url": "https://github.com/EFord36",
        "followers_url": "https://api.github.com/users/EFord36/followers",
        "following_url": "https://api.github.com/users/EFord36/following{/other_user}",
        "gists_url": "https://api.github.com/users/EFord36/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/EFord36/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/EFord36/subscriptions",
        "organizations_url": "https://api.github.com/users/EFord36/orgs",
        "repos_url": "https://api.github.com/users/EFord36/repos",
        "events_url": "https://api.github.com/users/EFord36/events{/privacy}",
        "received_events_url": "https://api.github.com/users/EFord36/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "0ec2780c291107b6686996e4b38f3d63e076eda7",
          "url": "https://api.github.com/repos/psf/requests/commits/0ec2780c291107b6686996e4b38f3d63e076eda7",
          "html_url": "https://github.com/psf/requests/commit/0ec2780c291107b6686996e4b38f3d63e076eda7"
        }
      ]
    },
    {
      "sha": "541aa80ca3d0ee771611bd155a5172efaa26d9da",
      "node_id": "C_kwDOABTKOtoAKDU0MWFhODBjYTNkMGVlNzcxNjExYmQxNTVhNTE3MmVmYWEyNmQ5ZGE",
      "commit": {
        "author": {
          "name": "Elliot Ford",
          "email": "elliot.ford@astrazeneca.com",
          "date": "2023-11-24T11:04:16Z"
        },
        "committer": {
          "name": "Elliot Ford",
          "email": "elliot.ford@astrazeneca.com",
          "date": "2024-02-23T10:26:21Z"
        },
        "message": "update urllib3 docs link",
        "tree": {
          "sha": "da0e52efee467307cb5a46a33df90045394498ea",
          "url": "https://api.github.com/repos/psf/requests/git/trees/da0e52efee467307cb5a46a33df90045394498ea"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/541aa80ca3d0ee771611bd155a5172efaa26d9da",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/541aa80ca3d0ee771611bd155a5172efaa26d9da",
      "html_url": "https://github.com/psf/requests/commit/541aa80ca3d0ee771611bd155a5172efaa26d9da",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/541aa80ca3d0ee771611bd155a5172efaa26d9da/comments",
      "author": {
        "login": "EFord36",
        "id": 20516159,
        "node_id": "MDQ6VXNlcjIwNTE2MTU5",
        "avatar_url": "https://avatars.githubusercontent.com/u/20516159?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/EFord36",
        "html_url": "https://github.com/EFord36",
        "followers_url": "https://api.github.com/users/EFord36/followers",
        "following_url": "https://api.github.com/users/EFord36/following{/other_user}",
        "gists_url": "https://api.github.com/users/EFord36/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/EFord36/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/EFord36/subscriptions",
        "organizations_url": "https://api.github.com/users/EFord36/orgs",
        "repos_url": "https://api.github.com/users/EFord36/repos",
        "events_url": "https://api.github.com/users/EFord36/events{/privacy}",
        "received_events_url": "https://api.github.com/users/EFord36/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "EFord36",
        "id": 20516159,
        "node_id": "MDQ6VXNlcjIwNTE2MTU5",
        "avatar_url": "https://avatars.githubusercontent.com/u/20516159?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/EFord36",
        "html_url": "https://github.com/EFord36",
        "followers_url": "https://api.github.com/users/EFord36/followers",
        "following_url": "https://api.github.com/users/EFord36/following{/other_user}",
        "gists_url": "https://api.github.com/users/EFord36/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/EFord36/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/EFord36/subscriptions",
        "organizations_url": "https://api.github.com/users/EFord36/orgs",
        "repos_url": "https://api.github.com/users/EFord36/repos",
        "events_url": "https://api.github.com/users/EFord36/events{/privacy}",
        "received_events_url": "https://api.github.com/users/EFord36/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "d3b3399ece1f76387d323983638e0838c06e88ea",
          "url": "https://api.github.com/repos/psf/requests/commits/d3b3399ece1f76387d323983638e0838c06e88ea",
          "html_url": "https://github.com/psf/requests/commit/d3b3399ece1f76387d323983638e0838c06e88ea"
        }
      ]
    },
    {
      "sha": "5f1c3c22ff7c7bb89a4e017e3f336cbc88e189c3",
      "node_id": "C_kwDOABTKOtoAKDVmMWMzYzIyZmY3YzdiYjg5YTRlMDE3ZTNmMzM2Y2JjODhlMTg5YzM",
      "commit": {
        "author": {
          "name": "Elliot Ford",
          "email": "elliot.ford@astrazeneca.com",
          "date": "2023-11-24T11:04:32Z"
        },
        "committer": {
          "name": "Elliot Ford",
          "email": "elliot.ford@astrazeneca.com",
          "date": "2024-02-23T10:26:21Z"
        },
        "message": "remove section with broken link to survey",
        "tree": {
          "sha": "9a7324671a4145fc00232040412605fa7303dd08",
          "url": "https://api.github.com/repos/psf/requests/git/trees/9a7324671a4145fc00232040412605fa7303dd08"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/5f1c3c22ff7c7bb89a4e017e3f336cbc88e189c3",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/5f1c3c22ff7c7bb89a4e017e3f336cbc88e189c3",
      "html_url": "https://github.com/psf/requests/commit/5f1c3c22ff7c7bb89a4e017e3f336cbc88e189c3",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/5f1c3c22ff7c7bb89a4e017e3f336cbc88e189c3/comments",
      "author": {
        "login": "EFord36",
        "id": 20516159,
        "node_id": "MDQ6VXNlcjIwNTE2MTU5",
        "avatar_url": "https://avatars.githubusercontent.com/u/20516159?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/EFord36",
        "html_url": "https://github.com/EFord36",
        "followers_url": "https://api.github.com/users/EFord36/followers",
        "following_url": "https://api.github.com/users/EFord36/following{/other_user}",
        "gists_url": "https://api.github.com/users/EFord36/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/EFord36/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/EFord36/subscriptions",
        "organizations_url": "https://api.github.com/users/EFord36/orgs",
        "repos_url": "https://api.github.com/users/EFord36/repos",
        "events_url": "https://api.github.com/users/EFord36/events{/privacy}",
        "received_events_url": "https://api.github.com/users/EFord36/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "EFord36",
        "id": 20516159,
        "node_id": "MDQ6VXNlcjIwNTE2MTU5",
        "avatar_url": "https://avatars.githubusercontent.com/u/20516159?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/EFord36",
        "html_url": "https://github.com/EFord36",
        "followers_url": "https://api.github.com/users/EFord36/followers",
        "following_url": "https://api.github.com/users/EFord36/following{/other_user}",
        "gists_url": "https://api.github.com/users/EFord36/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/EFord36/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/EFord36/subscriptions",
        "organizations_url": "https://api.github.com/users/EFord36/orgs",
        "repos_url": "https://api.github.com/users/EFord36/repos",
        "events_url": "https://api.github.com/users/EFord36/events{/privacy}",
        "received_events_url": "https://api.github.com/users/EFord36/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "541aa80ca3d0ee771611bd155a5172efaa26d9da",
          "url": "https://api.github.com/repos/psf/requests/commits/541aa80ca3d0ee771611bd155a5172efaa26d9da",
          "html_url": "https://github.com/psf/requests/commit/541aa80ca3d0ee771611bd155a5172efaa26d9da"
        }
      ]
    },
    {
      "sha": "0a7f662aa70d39b6c3b5c804be00af5731292550",
      "node_id": "C_kwDOABTKOtoAKDBhN2Y2NjJhYTcwZDM5YjZjM2I1YzgwNGJlMDBhZjU3MzEyOTI1NTA",
      "commit": {
        "author": {
          "name": "Elliot Ford",
          "email": "elliot.ford@astrazeneca.com",
          "date": "2023-11-24T11:04:54Z"
        },
        "committer": {
          "name": "Elliot Ford",
          "email": "elliot.ford@astrazeneca.com",
          "date": "2024-02-23T10:26:21Z"
        },
        "message": "Make example URL format a literal rather than an actual link\n\nThe rendered docs 'auto-link' this, which might encourage users to click\nthe link, even though it doesn't go anywhere.",
        "tree": {
          "sha": "d8430eb75e022bc95ecd38ca10169dc95797c4e6",
          "url": "https://api.github.com/repos/psf/requests/git/trees/d8430eb75e022bc95ecd38ca10169dc95797c4e6"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/0a7f662aa70d39b6c3b5c804be00af5731292550",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/0a7f662aa70d39b6c3b5c804be00af5731292550",
      "html_url": "https://github.com/psf/requests/commit/0a7f662aa70d39b6c3b5c804be00af5731292550",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/0a7f662aa70d39b6c3b5c804be00af5731292550/comments",
      "author": {
        "login": "EFord36",
        "id": 20516159,
        "node_id": "MDQ6VXNlcjIwNTE2MTU5",
        "avatar_url": "https://avatars.githubusercontent.com/u/20516159?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/EFord36",
        "html_url": "https://github.com/EFord36",
        "followers_url": "https://api.github.com/users/EFord36/followers",
        "following_url": "https://api.github.com/users/EFord36/following{/other_user}",
        "gists_url": "https://api.github.com/users/EFord36/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/EFord36/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/EFord36/subscriptions",
        "organizations_url": "https://api.github.com/users/EFord36/orgs",
        "repos_url": "https://api.github.com/users/EFord36/repos",
        "events_url": "https://api.github.com/users/EFord36/events{/privacy}",
        "received_events_url": "https://api.github.com/users/EFord36/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "EFord36",
        "id": 20516159,
        "node_id": "MDQ6VXNlcjIwNTE2MTU5",
        "avatar_url": "https://avatars.githubusercontent.com/u/20516159?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/EFord36",
        "html_url": "https://github.com/EFord36",
        "followers_url": "https://api.github.com/users/EFord36/followers",
        "following_url": "https://api.github.com/users/EFord36/following{/other_user}",
        "gists_url": "https://api.github.com/users/EFord36/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/EFord36/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/EFord36/subscriptions",
        "organizations_url": "https://api.github.com/users/EFord36/orgs",
        "repos_url": "https://api.github.com/users/EFord36/repos",
        "events_url": "https://api.github.com/users/EFord36/events{/privacy}",
        "received_events_url": "https://api.github.com/users/EFord36/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "5f1c3c22ff7c7bb89a4e017e3f336cbc88e189c3",
          "url": "https://api.github.com/repos/psf/requests/commits/5f1c3c22ff7c7bb89a4e017e3f336cbc88e189c3",
          "html_url": "https://github.com/psf/requests/commit/5f1c3c22ff7c7bb89a4e017e3f336cbc88e189c3"
        }
      ]
    },
    {
      "sha": "a0e79bad059f2d0e6d3c00a2a7311acb2bef4d67",
      "node_id": "C_kwDOABTKOtoAKGEwZTc5YmFkMDU5ZjJkMGU2ZDNjMDBhMmE3MzExYWNiMmJlZjRkNjc",
      "commit": {
        "author": {
          "name": "Elliot Ford",
          "email": "elliot.ford@astrazeneca.com",
          "date": "2023-11-24T11:05:45Z"
        },
        "committer": {
          "name": "Elliot Ford",
          "email": "elliot.ford@astrazeneca.com",
          "date": "2024-02-23T10:26:21Z"
        },
        "message": "update broken rfc link\n\nietf seems appropriate here - it's used elsewhere in the requets docs in\nseveral places.",
        "tree": {
          "sha": "1d5bf5c3a436d4d97145bf8d328cfca055aae728",
          "url": "https://api.github.com/repos/psf/requests/git/trees/1d5bf5c3a436d4d97145bf8d328cfca055aae728"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/a0e79bad059f2d0e6d3c00a2a7311acb2bef4d67",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/a0e79bad059f2d0e6d3c00a2a7311acb2bef4d67",
      "html_url": "https://github.com/psf/requests/commit/a0e79bad059f2d0e6d3c00a2a7311acb2bef4d67",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/a0e79bad059f2d0e6d3c00a2a7311acb2bef4d67/comments",
      "author": {
        "login": "EFord36",
        "id": 20516159,
        "node_id": "MDQ6VXNlcjIwNTE2MTU5",
        "avatar_url": "https://avatars.githubusercontent.com/u/20516159?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/EFord36",
        "html_url": "https://github.com/EFord36",
        "followers_url": "https://api.github.com/users/EFord36/followers",
        "following_url": "https://api.github.com/users/EFord36/following{/other_user}",
        "gists_url": "https://api.github.com/users/EFord36/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/EFord36/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/EFord36/subscriptions",
        "organizations_url": "https://api.github.com/users/EFord36/orgs",
        "repos_url": "https://api.github.com/users/EFord36/repos",
        "events_url": "https://api.github.com/users/EFord36/events{/privacy}",
        "received_events_url": "https://api.github.com/users/EFord36/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "EFord36",
        "id": 20516159,
        "node_id": "MDQ6VXNlcjIwNTE2MTU5",
        "avatar_url": "https://avatars.githubusercontent.com/u/20516159?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/EFord36",
        "html_url": "https://github.com/EFord36",
        "followers_url": "https://api.github.com/users/EFord36/followers",
        "following_url": "https://api.github.com/users/EFord36/following{/other_user}",
        "gists_url": "https://api.github.com/users/EFord36/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/EFord36/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/EFord36/subscriptions",
        "organizations_url": "https://api.github.com/users/EFord36/orgs",
        "repos_url": "https://api.github.com/users/EFord36/repos",
        "events_url": "https://api.github.com/users/EFord36/events{/privacy}",
        "received_events_url": "https://api.github.com/users/EFord36/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "0a7f662aa70d39b6c3b5c804be00af5731292550",
          "url": "https://api.github.com/repos/psf/requests/commits/0a7f662aa70d39b6c3b5c804be00af5731292550",
          "html_url": "https://github.com/psf/requests/commit/0a7f662aa70d39b6c3b5c804be00af5731292550"
        }
      ]
    },
    {
      "sha": "f3f2611d832e762423f55e08899c64224902dad1",
      "node_id": "C_kwDOABTKOtoAKGYzZjI2MTFkODMyZTc2MjQyM2Y1NWUwODg5OWM2NDIyNDkwMmRhZDE",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2024-02-23T11:30:46Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-02-23T11:30:46Z"
        },
        "message": "Merge pull request #6583 from EFord36/fix-broken-links\n\nFix broken links in docs",
        "tree": {
          "sha": "1d5bf5c3a436d4d97145bf8d328cfca055aae728",
          "url": "https://api.github.com/repos/psf/requests/git/trees/1d5bf5c3a436d4d97145bf8d328cfca055aae728"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/f3f2611d832e762423f55e08899c64224902dad1",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJl2IHmCRC1aQ7uu5UhlAAAQiMQAH6NkDbrUAgxWrdrL+C+vijM\n4seU4mVP005zxd8/xxT4oXWWqOJm/Llq79rk8+dpv5AKHnZuzl9VpICMKOk6UDSJ\nCkXpQXTJ/9aKUU6okuG/2Fd6SQebLfHbNW3VZvPONbhq+w+wZGurXWm7XV/bpYty\nb6EcejVXaQX26AzYfNoWa6Fmqv2jAwoQyZQlK+OiFsEw8NgGG6pC9z2WP23oac33\nZKcPvkZ6NP9AI84cbwAKA/XImQ8IF+Zm4NIg0op7qcirq74WmQwauR3IfBH1As+U\nWDMCCt9s52NuV17eXJh7AqWHt0xLJfVmGtuqHEr/pOgdD5bLmGkmUvBMr7zpFe/R\nISdqllBAPyaWcJrrI/GmjgNAJIrGKNdVB2Eyxzye8hGblEnTRbVof5QLnxSkZKAF\nuVlw+wrURkRM1Tfscy3VGabIzEAFO3qqzAVINjzhTjoWtAB7+RTwzvOmVz02VovU\nPAH0Ev/F+joHEcNAQn0+DU2UiOcY1maB7gKCEVRvZaAWIsUd3wVGhAKZjGY5o0vh\n+7MinBa3lcW1APWWKrehRF7GOghq8K+a6nQESb1unfdlLlqMA7Q7AsPeAbjaqwEV\n9SwjmQlaJoP8b3t1O5ZayC7TrAB4+xU0rYypZXcGJ+PHuHvI+tQ0KEq5FX/oUJ/c\nS6c/fvgNCk71H0heCSot\n=kRwP\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 1d5bf5c3a436d4d97145bf8d328cfca055aae728\nparent b8be93a721792deeadd2f498b8f77cf610e7765f\nparent a0e79bad059f2d0e6d3c00a2a7311acb2bef4d67\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1708687846 -0600\ncommitter GitHub <noreply@github.com> 1708687846 -0600\n\nMerge pull request #6583 from EFord36/fix-broken-links\n\nFix broken links in docs",
          "verified_at": "2024-11-05T15:56:01Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/f3f2611d832e762423f55e08899c64224902dad1",
      "html_url": "https://github.com/psf/requests/commit/f3f2611d832e762423f55e08899c64224902dad1",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/f3f2611d832e762423f55e08899c64224902dad1/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "b8be93a721792deeadd2f498b8f77cf610e7765f",
          "url": "https://api.github.com/repos/psf/requests/commits/b8be93a721792deeadd2f498b8f77cf610e7765f",
          "html_url": "https://github.com/psf/requests/commit/b8be93a721792deeadd2f498b8f77cf610e7765f"
        },
        {
          "sha": "a0e79bad059f2d0e6d3c00a2a7311acb2bef4d67",
          "url": "https://api.github.com/repos/psf/requests/commits/a0e79bad059f2d0e6d3c00a2a7311acb2bef4d67",
          "html_url": "https://github.com/psf/requests/commit/a0e79bad059f2d0e6d3c00a2a7311acb2bef4d67"
        }
      ]
    },
    {
      "sha": "eea3bbf9ac635f465ee6c9903dc57c677952dafd",
      "node_id": "C_kwDOABTKOtoAKGVlYTNiYmY5YWM2MzVmNDY1ZWU2Yzk5MDNkYzU3YzY3Nzk1MmRhZmQ",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2024-02-23T12:26:38Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-02-23T12:26:38Z"
        },
        "message": "Merge pull request #6562 from amkarn258/issue-6223\n\nevery chardet package maps to requests.packages.chardet.* package respectively",
        "tree": {
          "sha": "7c9bce606aa86a59bf2ec5f0f070d1cf781a4900",
          "url": "https://api.github.com/repos/psf/requests/git/trees/7c9bce606aa86a59bf2ec5f0f070d1cf781a4900"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/eea3bbf9ac635f465ee6c9903dc57c677952dafd",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJl2I7+CRC1aQ7uu5UhlAAAQFUQABvmOufz6DQB5/nmImz+OUlf\nmjUCXfVykxVx1mMFnWccCFQiODGxPNjhaV0SQzcmAC9AonJqnPNXgFYG38vlD0hN\nhZV2Y0depyGy2xcH1txMONVgbqq7Ci09yp7isJPa1SGEhPiTY2Dd1slPmaKY8i6y\nB8qQo9FmxXM8h0i1pxzIVx+Pklclbh+W5C60k6YPSXcdsDveTwK60UmUEwj5FWXk\noXUBN8fd8/ZAp9LrkCQqiax8RYRaTibHpfoMixZIdMUQvmEPOCFKhqCu3XT3XGOh\nYs8/8GnDbVdRVBrybsY9KCiBgmp3SWEB1H5wOlKB6xOCOv//4kykV7n9Sq6c/V+h\nsDY51AQB7GwasdQXT8luSnQ8JFE67kL6+8ywCjF11uWmMEZ3n/dasaV3cBQvyaFy\naq1y4xKk8eY/sfHAOIK59TGUXC0sOIuYcqBOT7I/vigX2umbzlyjeuhOsoMMJR6Q\n141dVJ9ARthYoNcLh3pBne/lJ/44z/LCevkJ1aJyKjdN8Qxc1rhIFI7bHSM5FYSf\nbBrS0r1PU3F+8ruQ9p5Lbht4/+vKYCBaJjOB7XeuShFuTnKYhuaBph+SDmn4WkKZ\nTMAEA6eb6DBP0oh/bJFvqFgo8tdNsUl3rLjyMj314tAhD9J08bAR+q4a/QzsDtmL\nReQJ6defGqgjHj/h1V/p\n=7H76\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 7c9bce606aa86a59bf2ec5f0f070d1cf781a4900\nparent f3f2611d832e762423f55e08899c64224902dad1\nparent 89cde235bec9374273281c1b4c9277c409246a6c\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1708691198 -0600\ncommitter GitHub <noreply@github.com> 1708691198 -0600\n\nMerge pull request #6562 from amkarn258/issue-6223\n\nevery chardet package maps to requests.packages.chardet.* package respectively",
          "verified_at": "2024-11-05T15:56:01Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/eea3bbf9ac635f465ee6c9903dc57c677952dafd",
      "html_url": "https://github.com/psf/requests/commit/eea3bbf9ac635f465ee6c9903dc57c677952dafd",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/eea3bbf9ac635f465ee6c9903dc57c677952dafd/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "f3f2611d832e762423f55e08899c64224902dad1",
          "url": "https://api.github.com/repos/psf/requests/commits/f3f2611d832e762423f55e08899c64224902dad1",
          "html_url": "https://github.com/psf/requests/commit/f3f2611d832e762423f55e08899c64224902dad1"
        },
        {
          "sha": "89cde235bec9374273281c1b4c9277c409246a6c",
          "url": "https://api.github.com/repos/psf/requests/commits/89cde235bec9374273281c1b4c9277c409246a6c",
          "html_url": "https://github.com/psf/requests/commit/89cde235bec9374273281c1b4c9277c409246a6c"
        }
      ]
    },
    {
      "sha": "c0813a2d910ea6b4f8438b91d315b8d181302356",
      "node_id": "C_kwDOABTKOtoAKGMwODEzYTJkOTEwZWE2YjRmODQzOGI5MWQzMTViOGQxODEzMDIzNTY",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2024-03-03T13:00:49Z"
        },
        "committer": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2024-03-06T17:28:13Z"
        },
        "message": "Use TLS settings in selecting connection pool\n\nPreviously, if someone made a request with `verify=False` then made a\nrequest where they expected verification to be enabled to the same host,\nthey would potentially reuse a connection where TLS had not been\nverified.\n\nThis fixes that issue.",
        "tree": {
          "sha": "80f84bc66adcd957192e8ac52976546989edfd74",
          "url": "https://api.github.com/repos/psf/requests/git/trees/80f84bc66adcd957192e8ac52976546989edfd74"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/c0813a2d910ea6b4f8438b91d315b8d181302356",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\niQIzBAABCAAdFiEEgSpQDY8Q9shZFt4GZW0zleSpeRoFAmXop60ACgkQZW0zleSp\neRplkQ/+LEeYtVZdRepioYacDcAdkbQn0yP2mfwAfW9ftDvjKavPnObJfCUzFAsf\nOGp2/dnUimaDQp2ktHzxybwIN0VrqronPi/UIFVVfeP2ljpudTJ95IMrlmlG6JlG\nqmmjlZ0Ki0lZfJGbKxuRTNSepRjNgxcwz7pDgyYpidfDKlTvSC6h+YuQUrOfA+RR\nVN9QOPISwarh9iTAXxAtljBkff1v2EosnaT6OLcr+5WLo7mBRA41FOer+zB5Q6cF\nYLjcXMxnkZYOr2dpL0weMoFz/UfIucoy+n14esODhIbMcEvc7w5gFnK6DHmcCZ5E\nK41REBwbmfBI1iCDCLA8ALwq91UyKBlvJe4/v3B5pJy3OO84oE11UHbIkxlIhN8i\nrkOY6KGMoJ5I8/K6ahRNF7bBkaBR0Zaa+d5Pg4lR3qorSVXuVLtnDKr5frcLQvUb\nsKWzlD/Ac1oa+IawQPXb/QJ6TwQ+DqDTcfzNOhG1Y14UVuEjEBiN5IjlWPWAMSPV\nUAd65w6NqQK+6KZD6K9FneHfbO7ueNbrix3kcqMIfEncctbUl40GsrOfPIDNsujZ\n0lRAYBFWehpA0oAzS82gaGzFhmsMUZagMaWrJqd3lQmSChCfaz3yUXVPzCuuBx9V\n4YaJ/bDnEDA3MOJOWvN7mwfaQawk7PR5Z0xfx5ELau5g0/FS0GY=\n=jxX3\n-----END PGP SIGNATURE-----",
          "payload": "tree 80f84bc66adcd957192e8ac52976546989edfd74\nparent eea3bbf9ac635f465ee6c9903dc57c677952dafd\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1709470849 -0600\ncommitter Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1709746093 -0600\n\nUse TLS settings in selecting connection pool\n\nPreviously, if someone made a request with `verify=False` then made a\nrequest where they expected verification to be enabled to the same host,\nthey would potentially reuse a connection where TLS had not been\nverified.\n\nThis fixes that issue.\n",
          "verified_at": "2024-11-05T15:56:01Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/c0813a2d910ea6b4f8438b91d315b8d181302356",
      "html_url": "https://github.com/psf/requests/commit/c0813a2d910ea6b4f8438b91d315b8d181302356",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/c0813a2d910ea6b4f8438b91d315b8d181302356/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "eea3bbf9ac635f465ee6c9903dc57c677952dafd",
          "url": "https://api.github.com/repos/psf/requests/commits/eea3bbf9ac635f465ee6c9903dc57c677952dafd",
          "html_url": "https://github.com/psf/requests/commit/eea3bbf9ac635f465ee6c9903dc57c677952dafd"
        }
      ]
    },
    {
      "sha": "a58d7f2ffb4d00b46dca2d70a3932a0b37e22fac",
      "node_id": "C_kwDOABTKOtoAKGE1OGQ3ZjJmZmI0ZDAwYjQ2ZGNhMmQ3MGEzOTMyYTBiMzdlMjJmYWM",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2024-03-11T11:21:59Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-03-11T11:21:59Z"
        },
        "message": "Merge pull request #6655 from sigmavirus24/fix-tls-floppy\n\nUse TLS settings in selecting connection pool",
        "tree": {
          "sha": "80f84bc66adcd957192e8ac52976546989edfd74",
          "url": "https://api.github.com/repos/psf/requests/git/trees/80f84bc66adcd957192e8ac52976546989edfd74"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/a58d7f2ffb4d00b46dca2d70a3932a0b37e22fac",
        "comment_count": 2,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJl7ulXCRC1aQ7uu5UhlAAA/QAQACAaNzhk7f036Sg7LQAnVFaC\nWb3oZEQ3bArFOo1toY03VEHl37zDev+Tel7TgETc3cKzOANl9My0mulh0K0TB+fM\nV1dF+0FhxIlcywxBRxmPC8zSccYuZioAGVYYZYptSKHbccjh8ff6QXR5Hy40Zigi\ngyRrhqdHPsswt3Mm3iBD8HwehXz1NBiMSrKxi2Iz6VeUQDHOjecAdpfmi5XdXvrA\nPxkAowMuIbZx90JzaXTSDl/IAXqZ2YYfP0rCzbu26rWcowVhstiI+DnNEldEGcKj\ng5PXf1CJRIbUG9dSwPV5urltj8CLTWHigGYo877qIDfXF7CdHQi7pTibEQP3P/Z6\npL+0JAxotz8i29J3CfuyKfimK+RynrIdJEdfS8S1CoBlR0+tkBl20BzUl8TjEauu\nnazuVts3fVXocp8ZWIZOSDrRENk7teMzMh5Bt0TeI7eNMc7yV0ezVBtq3461TObo\nlbZVW8+NbPXqm+jirDUl5gIXSUG/x5zlNAtGTi3RHHhCN6BZjIsRXknDgubMVCnL\n5EJId0ahPt1Nad5atwjbgEUzAPMbvQ88JBYcAIlIrOkoTXEIjuYKEob5LlAe+cvM\nKjRy+T9cwHaGs23e3A1y59Yrpt4ss/NHY+doNPm03WS/IDaXJocQyGfuLdtVoflV\n2ds0O0wU62EkzcnlZZ3J\n=yCtK\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 80f84bc66adcd957192e8ac52976546989edfd74\nparent eea3bbf9ac635f465ee6c9903dc57c677952dafd\nparent c0813a2d910ea6b4f8438b91d315b8d181302356\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1710156119 -0500\ncommitter GitHub <noreply@github.com> 1710156119 -0500\n\nMerge pull request #6655 from sigmavirus24/fix-tls-floppy\n\nUse TLS settings in selecting connection pool",
          "verified_at": "2024-11-05T15:56:01Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/a58d7f2ffb4d00b46dca2d70a3932a0b37e22fac",
      "html_url": "https://github.com/psf/requests/commit/a58d7f2ffb4d00b46dca2d70a3932a0b37e22fac",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/a58d7f2ffb4d00b46dca2d70a3932a0b37e22fac/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "eea3bbf9ac635f465ee6c9903dc57c677952dafd",
          "url": "https://api.github.com/repos/psf/requests/commits/eea3bbf9ac635f465ee6c9903dc57c677952dafd",
          "html_url": "https://github.com/psf/requests/commit/eea3bbf9ac635f465ee6c9903dc57c677952dafd"
        },
        {
          "sha": "c0813a2d910ea6b4f8438b91d315b8d181302356",
          "url": "https://api.github.com/repos/psf/requests/commits/c0813a2d910ea6b4f8438b91d315b8d181302356",
          "html_url": "https://github.com/psf/requests/commit/c0813a2d910ea6b4f8438b91d315b8d181302356"
        }
      ]
    },
    {
      "sha": "a94e9b5308ffcc3d2913ab873e9810a6601a67da",
      "node_id": "C_kwDOABTKOtoAKGE5NGU5YjUzMDhmZmNjM2QyOTEzYWI4NzNlOTgxMGE2NjAxYTY3ZGE",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2024-03-13T20:58:45Z"
        },
        "committer": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2024-03-14T11:06:22Z"
        },
        "message": "Add local TLS server\n\nThis also adds certificates for testing purposes and files to make it\neasy to generate/regenerate them.\n\nThis also replaces an existing test of how we utilize our pool manager\nsuch that we don't connect to badssl.com\n\nFinally, this adds additional context parameters for our pool manager to\naccount for mTLS certificates used by clients to authenticate to a\nserver.",
        "tree": {
          "sha": "8c83219bb1b267d1e5bafe0e906cdd1594fdeb33",
          "url": "https://api.github.com/repos/psf/requests/git/trees/8c83219bb1b267d1e5bafe0e906cdd1594fdeb33"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/a94e9b5308ffcc3d2913ab873e9810a6601a67da",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\niQIzBAABCAAdFiEEgSpQDY8Q9shZFt4GZW0zleSpeRoFAmXy2i4ACgkQZW0zleSp\neRrAyg//UKMmhfcIonSpOqivIufTUkTH0s+DeQnOw7/zr9Q3yzO6NAmqaj0wd+I8\nvIeoijRfvOTv9j9q7f4YUKBaXAFSJKR9Ou4UTMx5avPHVb+xjTIZHx+6Kyo3VHNj\nK1Uxq4T02OMnLEl1eLPrnAtVSW06VU1Izj67EOu7w+MLybFRmIKZFAKvUPUMupMV\nzOak7jKVt3gb6UqBOaeQUvQcxryDSbYbW1S73FsYaFS6gUrSXc85D6/uu/tzcy8d\nuVcRkIW/AnOxYZ4wHjQKDYIAqc40aO5IpWmYC0a+oIjadwbFrg8lSwHy7mAYA2aC\nD3xp1gohJu+ndWzPROsm1UDNUtdZSYDHr1zKiH4H0ReFpwiALehUCA+Sa/OYiS5n\nlCbh+hPQmKFPraZnkJnqZ+eGbK0kfLGi1y2Uir322Dfpzox/a5pMjGtC10jYbjqs\naHB+2pBP/7H0ZrAZEiFf3/ZT2IoqrRlpc3CM86cpyZO+G9lJ7J88XJ5sJV0OJw4Z\nTTN6PAOpFxHuW4w5DOoLp99ccv9ZvHeU/5wiCAXGcjbrOuBci86WkRMnJ4ALv07m\nc7a8aEqXGGIiHAO0xsKJVHQ0aOfTcCgyIEr28a6lzfT8gvMAJFhdHbdKltbTr51B\nIIAtYmVysWoMk0SUqkyjBWE+jF161pvw+hE4gN+SXeI0+NqbTz0=\n=Jq9D\n-----END PGP SIGNATURE-----",
          "payload": "tree 8c83219bb1b267d1e5bafe0e906cdd1594fdeb33\nparent a58d7f2ffb4d00b46dca2d70a3932a0b37e22fac\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1710363525 -0500\ncommitter Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1710414382 -0500\n\nAdd local TLS server\n\nThis also adds certificates for testing purposes and files to make it\neasy to generate/regenerate them.\n\nThis also replaces an existing test of how we utilize our pool manager\nsuch that we don't connect to badssl.com\n\nFinally, this adds additional context parameters for our pool manager to\naccount for mTLS certificates used by clients to authenticate to a\nserver.\n",
          "verified_at": "2024-11-05T15:56:01Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/a94e9b5308ffcc3d2913ab873e9810a6601a67da",
      "html_url": "https://github.com/psf/requests/commit/a94e9b5308ffcc3d2913ab873e9810a6601a67da",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/a94e9b5308ffcc3d2913ab873e9810a6601a67da/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "a58d7f2ffb4d00b46dca2d70a3932a0b37e22fac",
          "url": "https://api.github.com/repos/psf/requests/commits/a58d7f2ffb4d00b46dca2d70a3932a0b37e22fac",
          "html_url": "https://github.com/psf/requests/commit/a58d7f2ffb4d00b46dca2d70a3932a0b37e22fac"
        }
      ]
    },
    {
      "sha": "eeafb6ab3a54ab01cbf864d452ea30f5fdb67ce8",
      "node_id": "C_kwDOABTKOtoAKGVlYWZiNmFiM2E1NGFiMDFjYmY4NjRkNDUyZWEzMGY1ZmRiNjdjZTg",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2024-03-14T11:25:24Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-03-14T11:25:24Z"
        },
        "message": "Merge pull request #6662 from sigmavirus24/fix-tls-floppy\n\nAdd local TLS server",
        "tree": {
          "sha": "8c83219bb1b267d1e5bafe0e906cdd1594fdeb33",
          "url": "https://api.github.com/repos/psf/requests/git/trees/8c83219bb1b267d1e5bafe0e906cdd1594fdeb33"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/eeafb6ab3a54ab01cbf864d452ea30f5fdb67ce8",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJl8t6kCRC1aQ7uu5UhlAAATXwQABx27p+wpC3vzbbTlzL0b5w4\nBsHmJ2zXbF0E5RBsWyY1a5h8qK10XO/4NiSUlXnqrOBlj2pv64BV/26sAV3AuhM4\nFHu4WCHTuL0AO2EmfImX0kQdlowV8d3EBxU0bdrHxG0SwUYAL80OXjtB9VY2xLdj\nW/h0ygkq347J8IidyL08t2UkUnl6+bC4K1ujzbLXNEfj9+dQ38KUDUX8nRpEJp1l\nl2VG15cydQYvmyxAxq0xhMukalKZsvqFd8HO4JSc5c6+yq27/Y2puaoaVJKzRWZc\nGpIPE2y1kWyUZ73Snw5Vt/emoRyGzox0SUteULsvmLcDQI6rdeRZQAXUL4K5Xcfh\nDePOVZ2cnm/RfgRhFaWhMgMX5+LiuVcVRq1It1QtSBVh/n8gthgxnI7zh5BnXAXC\nyNy8rmyMWm4dENTNuyscj9oy3S/qqc1ysiu5IItKkSDRDZSP0gKO+IJ/G3sNF8gn\nwdW5WNT4gX6GG0ha/XdlcLyLX3e614JwYToT8t+TATZfc7+Zm85/QGpwLP6jSfwx\nB5hdCmD1Jm7tbL8ix/UeCiYFlIeXvRsqUFwLF6KHrqXsfo7QE8+3qe4zB7FiTgY7\nNOxELVgg94OL7wwauKczEehTUieeE0PO/6Y7unVd3shE5ZWp5VmX/ZM/3qkt0oin\nZpJCUxL30MO495kBO0Sy\n=DvAJ\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 8c83219bb1b267d1e5bafe0e906cdd1594fdeb33\nparent a58d7f2ffb4d00b46dca2d70a3932a0b37e22fac\nparent a94e9b5308ffcc3d2913ab873e9810a6601a67da\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1710415524 -0500\ncommitter GitHub <noreply@github.com> 1710415524 -0500\n\nMerge pull request #6662 from sigmavirus24/fix-tls-floppy\n\nAdd local TLS server",
          "verified_at": "2024-11-05T15:48:14Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/eeafb6ab3a54ab01cbf864d452ea30f5fdb67ce8",
      "html_url": "https://github.com/psf/requests/commit/eeafb6ab3a54ab01cbf864d452ea30f5fdb67ce8",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/eeafb6ab3a54ab01cbf864d452ea30f5fdb67ce8/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "a58d7f2ffb4d00b46dca2d70a3932a0b37e22fac",
          "url": "https://api.github.com/repos/psf/requests/commits/a58d7f2ffb4d00b46dca2d70a3932a0b37e22fac",
          "html_url": "https://github.com/psf/requests/commit/a58d7f2ffb4d00b46dca2d70a3932a0b37e22fac"
        },
        {
          "sha": "a94e9b5308ffcc3d2913ab873e9810a6601a67da",
          "url": "https://api.github.com/repos/psf/requests/commits/a94e9b5308ffcc3d2913ab873e9810a6601a67da",
          "html_url": "https://github.com/psf/requests/commit/a94e9b5308ffcc3d2913ab873e9810a6601a67da"
        }
      ]
    },
    {
      "sha": "1604e20fc87ce212cf3a02474a6d7509b640cbbb",
      "node_id": "C_kwDOABTKOtoAKDE2MDRlMjBmYzg3Y2UyMTJjZjNhMDI0NzRhNmQ3NTA5YjY0MGNiYmI",
      "commit": {
        "author": {
          "name": "flysee",
          "email": "birdsee@qq.com",
          "date": "2022-12-07T11:24:22Z"
        },
        "committer": {
          "name": "flysee",
          "email": "birdsee@qq.com",
          "date": "2024-03-18T07:36:36Z"
        },
        "message": "Fix the proxy_bypass_registry function all returning true in some cases.",
        "tree": {
          "sha": "5cad6aeef56fedcb9073a8557b85ba0acc099961",
          "url": "https://api.github.com/repos/psf/requests/git/trees/5cad6aeef56fedcb9073a8557b85ba0acc099961"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/1604e20fc87ce212cf3a02474a6d7509b640cbbb",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/1604e20fc87ce212cf3a02474a6d7509b640cbbb",
      "html_url": "https://github.com/psf/requests/commit/1604e20fc87ce212cf3a02474a6d7509b640cbbb",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/1604e20fc87ce212cf3a02474a6d7509b640cbbb/comments",
      "author": {
        "login": "flysee",
        "id": 8475072,
        "node_id": "MDQ6VXNlcjg0NzUwNzI=",
        "avatar_url": "https://avatars.githubusercontent.com/u/8475072?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/flysee",
        "html_url": "https://github.com/flysee",
        "followers_url": "https://api.github.com/users/flysee/followers",
        "following_url": "https://api.github.com/users/flysee/following{/other_user}",
        "gists_url": "https://api.github.com/users/flysee/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/flysee/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/flysee/subscriptions",
        "organizations_url": "https://api.github.com/users/flysee/orgs",
        "repos_url": "https://api.github.com/users/flysee/repos",
        "events_url": "https://api.github.com/users/flysee/events{/privacy}",
        "received_events_url": "https://api.github.com/users/flysee/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "flysee",
        "id": 8475072,
        "node_id": "MDQ6VXNlcjg0NzUwNzI=",
        "avatar_url": "https://avatars.githubusercontent.com/u/8475072?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/flysee",
        "html_url": "https://github.com/flysee",
        "followers_url": "https://api.github.com/users/flysee/followers",
        "following_url": "https://api.github.com/users/flysee/following{/other_user}",
        "gists_url": "https://api.github.com/users/flysee/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/flysee/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/flysee/subscriptions",
        "organizations_url": "https://api.github.com/users/flysee/orgs",
        "repos_url": "https://api.github.com/users/flysee/repos",
        "events_url": "https://api.github.com/users/flysee/events{/privacy}",
        "received_events_url": "https://api.github.com/users/flysee/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "eeafb6ab3a54ab01cbf864d452ea30f5fdb67ce8",
          "url": "https://api.github.com/repos/psf/requests/commits/eeafb6ab3a54ab01cbf864d452ea30f5fdb67ce8",
          "html_url": "https://github.com/psf/requests/commit/eeafb6ab3a54ab01cbf864d452ea30f5fdb67ce8"
        }
      ]
    },
    {
      "sha": "13d892bdbe9a2aa374959a166e8067c35253705d",
      "node_id": "C_kwDOABTKOtoAKDEzZDg5MmJkYmU5YTJhYTM3NDk1OWExNjZlODA2N2MzNTI1MzcwNWQ",
      "commit": {
        "author": {
          "name": "flysee",
          "email": "birdsee@qq.com",
          "date": "2024-03-18T14:33:17Z"
        },
        "committer": {
          "name": "flysee",
          "email": "birdsee@qq.com",
          "date": "2024-03-18T14:33:17Z"
        },
        "message": "Additional should_bypass_proxies function test cases",
        "tree": {
          "sha": "b19e29fe875daa8dedaa2bd64c2124355ae31663",
          "url": "https://api.github.com/repos/psf/requests/git/trees/b19e29fe875daa8dedaa2bd64c2124355ae31663"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/13d892bdbe9a2aa374959a166e8067c35253705d",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/13d892bdbe9a2aa374959a166e8067c35253705d",
      "html_url": "https://github.com/psf/requests/commit/13d892bdbe9a2aa374959a166e8067c35253705d",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/13d892bdbe9a2aa374959a166e8067c35253705d/comments",
      "author": {
        "login": "flysee",
        "id": 8475072,
        "node_id": "MDQ6VXNlcjg0NzUwNzI=",
        "avatar_url": "https://avatars.githubusercontent.com/u/8475072?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/flysee",
        "html_url": "https://github.com/flysee",
        "followers_url": "https://api.github.com/users/flysee/followers",
        "following_url": "https://api.github.com/users/flysee/following{/other_user}",
        "gists_url": "https://api.github.com/users/flysee/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/flysee/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/flysee/subscriptions",
        "organizations_url": "https://api.github.com/users/flysee/orgs",
        "repos_url": "https://api.github.com/users/flysee/repos",
        "events_url": "https://api.github.com/users/flysee/events{/privacy}",
        "received_events_url": "https://api.github.com/users/flysee/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "flysee",
        "id": 8475072,
        "node_id": "MDQ6VXNlcjg0NzUwNzI=",
        "avatar_url": "https://avatars.githubusercontent.com/u/8475072?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/flysee",
        "html_url": "https://github.com/flysee",
        "followers_url": "https://api.github.com/users/flysee/followers",
        "following_url": "https://api.github.com/users/flysee/following{/other_user}",
        "gists_url": "https://api.github.com/users/flysee/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/flysee/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/flysee/subscriptions",
        "organizations_url": "https://api.github.com/users/flysee/orgs",
        "repos_url": "https://api.github.com/users/flysee/repos",
        "events_url": "https://api.github.com/users/flysee/events{/privacy}",
        "received_events_url": "https://api.github.com/users/flysee/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "1604e20fc87ce212cf3a02474a6d7509b640cbbb",
          "url": "https://api.github.com/repos/psf/requests/commits/1604e20fc87ce212cf3a02474a6d7509b640cbbb",
          "html_url": "https://github.com/psf/requests/commit/1604e20fc87ce212cf3a02474a6d7509b640cbbb"
        }
      ]
    },
    {
      "sha": "8dd3b26bf59808de24fd654699f592abf6de581e",
      "node_id": "C_kwDOABTKOtoAKDhkZDNiMjZiZjU5ODA4ZGUyNGZkNjU0Njk5ZjU5MmFiZjZkZTU4MWU",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2024-03-18T21:38:16Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-03-18T21:38:16Z"
        },
        "message": "Merge pull request #6302 from flysee/main\n\nFix the proxy_bypass_registry function all returning true in some cases.",
        "tree": {
          "sha": "b19e29fe875daa8dedaa2bd64c2124355ae31663",
          "url": "https://api.github.com/repos/psf/requests/git/trees/b19e29fe875daa8dedaa2bd64c2124355ae31663"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/8dd3b26bf59808de24fd654699f592abf6de581e",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJl+LRICRC1aQ7uu5UhlAAAXkkQACR7aqKlG2XOr5ZfHdRssLnG\neUnvSyg5TMvYhpH5NYAyixjJAENnFUdyay0AvdT8mGLVEuWyHce1W1bLRlm0H3DG\nL1vihYZcJ78+XtnzeiPVcetp9RdQ3NvuPrac99O1oeHuaweB6k248ECj9i1gtvV7\njgjKn3KOdkEqfXKh4lho2UX65uTkEqaAlnmV4KjyRi5Gzgrs3r6dJmxKI/vox4ii\np84nvyiHoZhcRnogXMiN88cnixRjPp2psa3ezMBrsIn+dMr1i/3jeGPCVzOrJqYL\njc+6EMgXp1AO8ScEhS1FGPBErsNf+YfnJj/OBWGHbaiKZB3J6xmP7EUzPAQfrAci\nsuxvnEMzD+wKZ5z19kO3dV561JBhvN/YCFp/olfTbqRX91nvDjAE/1Ef9Pq+vU9Y\nAZEW6OdMBFYnOmzdRJC+0t5PT/j6PRv+kSWq0ywb9vd0kbRBSQ8tbDKyAkFgz7/o\nETshq4KT0xLWrfJNcRyjl91gjg180PoavoVuvugnU58O0SP8F/IF8iemAuoVhxrc\niEA0Qp1YWEZSCO8iA03MtQ+fz+/34MdPLnu1OH6LdPYP1+4XPZP9jjTKoPXxxJ6L\nxX8QCinNtTKrrYr08hqJ4YcCISr6CUXoKReOrSzYQAirT95G57Tj7GOHHxrN3Ymo\nRCuucWCCbqnO9u4eG5k+\n=T0cW\n-----END PGP SIGNATURE-----\n",
          "payload": "tree b19e29fe875daa8dedaa2bd64c2124355ae31663\nparent eeafb6ab3a54ab01cbf864d452ea30f5fdb67ce8\nparent 13d892bdbe9a2aa374959a166e8067c35253705d\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1710797896 -0500\ncommitter GitHub <noreply@github.com> 1710797896 -0500\n\nMerge pull request #6302 from flysee/main\n\nFix the proxy_bypass_registry function all returning true in some cases.",
          "verified_at": "2024-11-05T15:48:14Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/8dd3b26bf59808de24fd654699f592abf6de581e",
      "html_url": "https://github.com/psf/requests/commit/8dd3b26bf59808de24fd654699f592abf6de581e",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/8dd3b26bf59808de24fd654699f592abf6de581e/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "eeafb6ab3a54ab01cbf864d452ea30f5fdb67ce8",
          "url": "https://api.github.com/repos/psf/requests/commits/eeafb6ab3a54ab01cbf864d452ea30f5fdb67ce8",
          "html_url": "https://github.com/psf/requests/commit/eeafb6ab3a54ab01cbf864d452ea30f5fdb67ce8"
        },
        {
          "sha": "13d892bdbe9a2aa374959a166e8067c35253705d",
          "url": "https://api.github.com/repos/psf/requests/commits/13d892bdbe9a2aa374959a166e8067c35253705d",
          "html_url": "https://github.com/psf/requests/commit/13d892bdbe9a2aa374959a166e8067c35253705d"
        }
      ]
    },
    {
      "sha": "2daa7b52a78984ab5e66358052fc8dfe93e251bd",
      "node_id": "C_kwDOABTKOtoAKDJkYWE3YjUyYTc4OTg0YWI1ZTY2MzU4MDUyZmM4ZGZlOTNlMjUxYmQ",
      "commit": {
        "author": {
          "name": "dependabot[bot]",
          "email": "49699333+dependabot[bot]@users.noreply.github.com",
          "date": "2024-04-01T17:00:20Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-04-01T17:00:20Z"
        },
        "message": "Bump actions/setup-python from 5.0.0 to 5.1.0\n\nBumps [actions/setup-python](https://github.com/actions/setup-python) from 5.0.0 to 5.1.0.\n- [Release notes](https://github.com/actions/setup-python/releases)\n- [Commits](https://github.com/actions/setup-python/compare/0a5c61591373683505ea898e09a3ea4f39ef2b9c...82c7e631bb3cdc910f68e0081d67478d79c6982d)\n\n---\nupdated-dependencies:\n- dependency-name: actions/setup-python\n  dependency-type: direct:production\n  update-type: version-update:semver-minor\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
        "tree": {
          "sha": "477e646a462e6203801788cd824c7aca643de3bc",
          "url": "https://api.github.com/repos/psf/requests/git/trees/477e646a462e6203801788cd824c7aca643de3bc"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/2daa7b52a78984ab5e66358052fc8dfe93e251bd",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJmCugkCRC1aQ7uu5UhlAAA0L8QAEuwL/fkB/t0qB0M27hmyYs1\nMV91KV2DYFOAjF+8o8x6kwBPlL/VtMmW1HG4FAsUwiNIgZGS6vqVLRyCawVtizgm\nwDsQhVIUUPY9xjyXB7NZ8H7NSg+KUaiyfo2hSMrAZKqdYspr7ZUvkWVCwXi5rHJA\nzwZS67fOhwT8xRc/gSzZxz64MfaYgVYR+7IABDq1Q/VQrNMCioK+u0EdqVquazWn\nQSlhgcX4Ca1U7irrFyI9BE0i8Av3JJWdQ6hrNMNe5V/tDDI8pq2On0mq9i2BgVv7\nLx/BuGxwTeeHvycpNZbO6J+SL78uzztLBHva+iJaD709YeSanv21UOjY7vMS7yEP\ntl9j4YUM+ISjdx1Vycs6MoMH/kvZy1ZVwhUYHWlUVDgd04KfH/qO2sA1O3UC2cU5\nuuVQJnzsYNmjrvPhqYCv04g1txVEHDff1Va7sflql4zvkFOXsjETEVFF1ONccery\n2NEsLttkki9+FwUnWJNsBdhj0ty6UMxye8TKKWqMhXvFqptGV3d9uy9QXKHu3Ch1\niaS13/ECCOsVH9Iq5wGusIt0ch+SyVM75m+QHe1G6qJP2o/NlU7AEi7H03Mgrbpe\n0uxKv7ijMjoCtX86wc5SIqNDGLbJpimAB01GfoSVwr9IWpxRWLnaL3mUWrTPRLs6\ng4SJk9shfxWFhJKeR8f5\n=4YZY\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 477e646a462e6203801788cd824c7aca643de3bc\nparent 8dd3b26bf59808de24fd654699f592abf6de581e\nauthor dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> 1711990820 +0000\ncommitter GitHub <noreply@github.com> 1711990820 +0000\n\nBump actions/setup-python from 5.0.0 to 5.1.0\n\nBumps [actions/setup-python](https://github.com/actions/setup-python) from 5.0.0 to 5.1.0.\n- [Release notes](https://github.com/actions/setup-python/releases)\n- [Commits](https://github.com/actions/setup-python/compare/0a5c61591373683505ea898e09a3ea4f39ef2b9c...82c7e631bb3cdc910f68e0081d67478d79c6982d)\n\n---\nupdated-dependencies:\n- dependency-name: actions/setup-python\n  dependency-type: direct:production\n  update-type: version-update:semver-minor\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
          "verified_at": "2024-11-05T15:48:14Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/2daa7b52a78984ab5e66358052fc8dfe93e251bd",
      "html_url": "https://github.com/psf/requests/commit/2daa7b52a78984ab5e66358052fc8dfe93e251bd",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/2daa7b52a78984ab5e66358052fc8dfe93e251bd/comments",
      "author": {
        "login": "dependabot[bot]",
        "id": 49699333,
        "node_id": "MDM6Qm90NDk2OTkzMzM=",
        "avatar_url": "https://avatars.githubusercontent.com/in/29110?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/dependabot%5Bbot%5D",
        "html_url": "https://github.com/apps/dependabot",
        "followers_url": "https://api.github.com/users/dependabot%5Bbot%5D/followers",
        "following_url": "https://api.github.com/users/dependabot%5Bbot%5D/following{/other_user}",
        "gists_url": "https://api.github.com/users/dependabot%5Bbot%5D/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/dependabot%5Bbot%5D/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/dependabot%5Bbot%5D/subscriptions",
        "organizations_url": "https://api.github.com/users/dependabot%5Bbot%5D/orgs",
        "repos_url": "https://api.github.com/users/dependabot%5Bbot%5D/repos",
        "events_url": "https://api.github.com/users/dependabot%5Bbot%5D/events{/privacy}",
        "received_events_url": "https://api.github.com/users/dependabot%5Bbot%5D/received_events",
        "type": "Bot",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "8dd3b26bf59808de24fd654699f592abf6de581e",
          "url": "https://api.github.com/repos/psf/requests/commits/8dd3b26bf59808de24fd654699f592abf6de581e",
          "html_url": "https://github.com/psf/requests/commit/8dd3b26bf59808de24fd654699f592abf6de581e"
        }
      ]
    },
    {
      "sha": "2a438c27b5a5828c8ea0dc958112eecffca70b12",
      "node_id": "C_kwDOABTKOtoAKDJhNDM4YzI3YjVhNTgyOGM4ZWEwZGM5NTgxMTJlZWNmZmNhNzBiMTI",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2024-04-01T17:36:47Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-04-01T17:36:47Z"
        },
        "message": "Merge pull request #6677 from psf/dependabot/github_actions/actions/setup-python-5.1.0\n\nBump actions/setup-python from 5.0.0 to 5.1.0",
        "tree": {
          "sha": "477e646a462e6203801788cd824c7aca643de3bc",
          "url": "https://api.github.com/repos/psf/requests/git/trees/477e646a462e6203801788cd824c7aca643de3bc"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/2a438c27b5a5828c8ea0dc958112eecffca70b12",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJmCvCvCRC1aQ7uu5UhlAAA+YgQAKHwuqFKDNGnaf6LEAIvroed\n3K1JEXj2hmnmsBP2BiRdvrPme9r01dIsia0ISoOoWt+5ahTcx7wigPoKDNP7X/3w\nBMNAobnkCd1269oVws113vf50ZasqRRA4BzS5TaLk7vvOYnNM+cCdKEfMCBdNrse\nWN5ct830WlyqiVKeVHJ9WCKcBSm3QbwhCABFMAFab4t+P7lPwHu1eAermWiaFpkl\nSaSn4gyD5Pf8HL9cg3qY/pkQjt0egCDzE3trjpEhIKbs4tdD41qqrwH+JWHYZ3mG\n7Uv6hFxyvxp8IlTdKvrbhtoXlNwSbh3XAcC7MnwqLIXntfpZM3nz6dPhRnKAo9WL\nlRp8XQDP1zsEgx3sF0a0zYEPIT3uW3IbfSKw/NhTPTE4JhNjb5aQILuLRtLI0BYL\nPbY4sHsO2IUAYf/Z9xAIp9N9NUB7M3T1gHGyU58H9TW8Dhhlji6e3rBI58AyLbm0\n0dzdlzsyRnEG5XlPWmMYA4fOAORperC8IrcQVQtRt/cokU3g4qqA3+lHbnQiyjoj\nP2ZsCq5O2M8oZThA3nJ2emSMQR+Qt0OG3WShVK2AoyAAqZVo+H8C5yfNpeAiz8uw\nWYPWm2VJnVdYc3BT0vSMMPXo87jE2TxXAhd9VZIjLd+TVc874q5/iFBSgIMwHRuC\npmZdbY3Fo3OZBJpou1yV\n=j7HI\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 477e646a462e6203801788cd824c7aca643de3bc\nparent 8dd3b26bf59808de24fd654699f592abf6de581e\nparent 2daa7b52a78984ab5e66358052fc8dfe93e251bd\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1711993007 -0700\ncommitter GitHub <noreply@github.com> 1711993007 -0700\n\nMerge pull request #6677 from psf/dependabot/github_actions/actions/setup-python-5.1.0\n\nBump actions/setup-python from 5.0.0 to 5.1.0",
          "verified_at": "2024-11-05T15:48:14Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/2a438c27b5a5828c8ea0dc958112eecffca70b12",
      "html_url": "https://github.com/psf/requests/commit/2a438c27b5a5828c8ea0dc958112eecffca70b12",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/2a438c27b5a5828c8ea0dc958112eecffca70b12/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "8dd3b26bf59808de24fd654699f592abf6de581e",
          "url": "https://api.github.com/repos/psf/requests/commits/8dd3b26bf59808de24fd654699f592abf6de581e",
          "html_url": "https://github.com/psf/requests/commit/8dd3b26bf59808de24fd654699f592abf6de581e"
        },
        {
          "sha": "2daa7b52a78984ab5e66358052fc8dfe93e251bd",
          "url": "https://api.github.com/repos/psf/requests/commits/2daa7b52a78984ab5e66358052fc8dfe93e251bd",
          "html_url": "https://github.com/psf/requests/commit/2daa7b52a78984ab5e66358052fc8dfe93e251bd"
        }
      ]
    },
    {
      "sha": "e45b428960ff3927812fc9b555e2ac627ba95769",
      "node_id": "C_kwDOABTKOtoAKGU0NWI0Mjg5NjBmZjM5Mjc4MTJmYzliNTU1ZTJhYzYyN2JhOTU3Njk",
      "commit": {
        "author": {
          "name": "Michiel W. Beijen",
          "email": "mb@x14.nl",
          "date": "2024-04-08T19:47:12Z"
        },
        "committer": {
          "name": "Michiel W. Beijen",
          "email": "mb@x14.nl",
          "date": "2024-04-08T19:48:24Z"
        },
        "message": "Add rfc9110 HTTP status code names\n\nRFC 9110 _HTTP Semantics_ obsoletes some earlier RFCs which defined HTTP\n1.1. It adds some status codes that were previously only used for\nWebDAV to HTTP _proper_ after making the names somewhat more generic.\n\nSee https://www.rfc-editor.org/rfc/rfc9110.html#name-changes-from-rfc-7231\n\nThis commit adds the http status code names from that RFC.",
        "tree": {
          "sha": "6d72690327378214a8e8c724d682f216619d42c2",
          "url": "https://api.github.com/repos/psf/requests/git/trees/6d72690327378214a8e8c724d682f216619d42c2"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/e45b428960ff3927812fc9b555e2ac627ba95769",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/e45b428960ff3927812fc9b555e2ac627ba95769",
      "html_url": "https://github.com/psf/requests/commit/e45b428960ff3927812fc9b555e2ac627ba95769",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/e45b428960ff3927812fc9b555e2ac627ba95769/comments",
      "author": {
        "login": "mbeijen",
        "id": 659504,
        "node_id": "MDQ6VXNlcjY1OTUwNA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/659504?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/mbeijen",
        "html_url": "https://github.com/mbeijen",
        "followers_url": "https://api.github.com/users/mbeijen/followers",
        "following_url": "https://api.github.com/users/mbeijen/following{/other_user}",
        "gists_url": "https://api.github.com/users/mbeijen/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/mbeijen/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/mbeijen/subscriptions",
        "organizations_url": "https://api.github.com/users/mbeijen/orgs",
        "repos_url": "https://api.github.com/users/mbeijen/repos",
        "events_url": "https://api.github.com/users/mbeijen/events{/privacy}",
        "received_events_url": "https://api.github.com/users/mbeijen/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "mbeijen",
        "id": 659504,
        "node_id": "MDQ6VXNlcjY1OTUwNA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/659504?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/mbeijen",
        "html_url": "https://github.com/mbeijen",
        "followers_url": "https://api.github.com/users/mbeijen/followers",
        "following_url": "https://api.github.com/users/mbeijen/following{/other_user}",
        "gists_url": "https://api.github.com/users/mbeijen/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/mbeijen/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/mbeijen/subscriptions",
        "organizations_url": "https://api.github.com/users/mbeijen/orgs",
        "repos_url": "https://api.github.com/users/mbeijen/repos",
        "events_url": "https://api.github.com/users/mbeijen/events{/privacy}",
        "received_events_url": "https://api.github.com/users/mbeijen/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "2a438c27b5a5828c8ea0dc958112eecffca70b12",
          "url": "https://api.github.com/repos/psf/requests/commits/2a438c27b5a5828c8ea0dc958112eecffca70b12",
          "html_url": "https://github.com/psf/requests/commit/2a438c27b5a5828c8ea0dc958112eecffca70b12"
        }
      ]
    },
    {
      "sha": "0790ea4250bce844734f625a1a8b37d5581fd8cd",
      "node_id": "C_kwDOABTKOtoAKDA3OTBlYTQyNTBiY2U4NDQ3MzRmNjI1YTFhOGIzN2Q1NTgxZmQ4Y2Q",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2024-04-11T14:10:57Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-04-11T14:10:57Z"
        },
        "message": "Merge pull request #6680 from mbeijen/rfc9110\n\nAdd rfc9110 HTTP status code names",
        "tree": {
          "sha": "6d72690327378214a8e8c724d682f216619d42c2",
          "url": "https://api.github.com/repos/psf/requests/git/trees/6d72690327378214a8e8c724d682f216619d42c2"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/0790ea4250bce844734f625a1a8b37d5581fd8cd",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJmF+9xCRC1aQ7uu5UhlAAAhJYQAFwPqn3pV3y4eNKuikhIJ1dc\n5Apszn2i36Qi2WRkM2ZAVd9WkTiMLdzo7/sSe7eC1YSky9EhgRaQ5d3V4YvvWBuG\nkkbV2+9mWmo4rlYtLE1rCGv2A2himt/ZnEZxT7H4Fz+zHHAqIpe7D2hwnx7RTzWi\nTBcKmRWLX6ELTPdCEhV6ZpMTnOUh/TNn1UUctMnuj74piO3BgZI9+s9EDZFXr2j4\nl+6SFzv35dIv2CdaBIPPeZmZRBlF4tVD9/j8ucJ2RXXb4ltJd8zJ6fGOphSLcMKr\n1kPkgOmY05i39xQkUC/snX2SM76xX2TDACxud8+VM5dy1vhonwBcpBa9QGfnrGuu\nXhorbSCTr16V2O7UsJT+FZhkW3pxD5pAr8Rt89PI1OdZrWBkD6QAqqFFsLUa2Jtj\nXmMzTCA1+9eXVTDyyRZkcJ4xHPkMZGfsdLkEcti4wptOs2IMvFIrzqCruIdNVJiP\nsPNlPSdNPbzTtNYL/jr63N3qZQA9WWJtM9h1/eLksl+RRDBlHMJMMmQc9jajErc5\nQyWkBCzKdGr8ss+wZ3H+uZhdbCsNImpKfBM1zkP5R4pEzsjeu1wmufhIoibpBnJ8\nBJKyqeMKJhx0GjEqGUDo//w7KzQSjOfQIWZ+fgN6AEa3zoDTNXraMVtag2ICx5RL\n3FtBxSI7X0mu1H2Uq5ds\n=rXVf\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 6d72690327378214a8e8c724d682f216619d42c2\nparent 2a438c27b5a5828c8ea0dc958112eecffca70b12\nparent e45b428960ff3927812fc9b555e2ac627ba95769\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1712844657 -0700\ncommitter GitHub <noreply@github.com> 1712844657 -0700\n\nMerge pull request #6680 from mbeijen/rfc9110\n\nAdd rfc9110 HTTP status code names",
          "verified_at": "2024-11-05T15:48:14Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/0790ea4250bce844734f625a1a8b37d5581fd8cd",
      "html_url": "https://github.com/psf/requests/commit/0790ea4250bce844734f625a1a8b37d5581fd8cd",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/0790ea4250bce844734f625a1a8b37d5581fd8cd/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "2a438c27b5a5828c8ea0dc958112eecffca70b12",
          "url": "https://api.github.com/repos/psf/requests/commits/2a438c27b5a5828c8ea0dc958112eecffca70b12",
          "html_url": "https://github.com/psf/requests/commit/2a438c27b5a5828c8ea0dc958112eecffca70b12"
        },
        {
          "sha": "e45b428960ff3927812fc9b555e2ac627ba95769",
          "url": "https://api.github.com/repos/psf/requests/commits/e45b428960ff3927812fc9b555e2ac627ba95769",
          "html_url": "https://github.com/psf/requests/commit/e45b428960ff3927812fc9b555e2ac627ba95769"
        }
      ]
    },
    {
      "sha": "cc23d1c6445d61c1e6905cae4861d6e3c3244274",
      "node_id": "C_kwDOABTKOtoAKGNjMjNkMWM2NDQ1ZDYxYzFlNjkwNWNhZTQ4NjFkNmUzYzMyNDQyNzQ",
      "commit": {
        "author": {
          "name": "Lumir Balhar",
          "email": "lbalhar@redhat.com",
          "date": "2024-04-11T19:10:36Z"
        },
        "committer": {
          "name": "Lumir Balhar",
          "email": "lbalhar@redhat.com",
          "date": "2024-04-11T19:10:36Z"
        },
        "message": "Fix compatibility with pytest 8\n\n`pytest.warns(None)` has been deprecated in pytest 7.0.0\nand it's no longer working in pytest 8.\n\nResolves: https://github.com/psf/requests/issues/6679",
        "tree": {
          "sha": "084f6a70c22c8da484871ca2078d6586134b2996",
          "url": "https://api.github.com/repos/psf/requests/git/trees/084f6a70c22c8da484871ca2078d6586134b2996"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/cc23d1c6445d61c1e6905cae4861d6e3c3244274",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/cc23d1c6445d61c1e6905cae4861d6e3c3244274",
      "html_url": "https://github.com/psf/requests/commit/cc23d1c6445d61c1e6905cae4861d6e3c3244274",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/cc23d1c6445d61c1e6905cae4861d6e3c3244274/comments",
      "author": {
        "login": "frenzymadness",
        "id": 5688939,
        "node_id": "MDQ6VXNlcjU2ODg5Mzk=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5688939?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/frenzymadness",
        "html_url": "https://github.com/frenzymadness",
        "followers_url": "https://api.github.com/users/frenzymadness/followers",
        "following_url": "https://api.github.com/users/frenzymadness/following{/other_user}",
        "gists_url": "https://api.github.com/users/frenzymadness/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/frenzymadness/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/frenzymadness/subscriptions",
        "organizations_url": "https://api.github.com/users/frenzymadness/orgs",
        "repos_url": "https://api.github.com/users/frenzymadness/repos",
        "events_url": "https://api.github.com/users/frenzymadness/events{/privacy}",
        "received_events_url": "https://api.github.com/users/frenzymadness/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "frenzymadness",
        "id": 5688939,
        "node_id": "MDQ6VXNlcjU2ODg5Mzk=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5688939?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/frenzymadness",
        "html_url": "https://github.com/frenzymadness",
        "followers_url": "https://api.github.com/users/frenzymadness/followers",
        "following_url": "https://api.github.com/users/frenzymadness/following{/other_user}",
        "gists_url": "https://api.github.com/users/frenzymadness/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/frenzymadness/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/frenzymadness/subscriptions",
        "organizations_url": "https://api.github.com/users/frenzymadness/orgs",
        "repos_url": "https://api.github.com/users/frenzymadness/repos",
        "events_url": "https://api.github.com/users/frenzymadness/events{/privacy}",
        "received_events_url": "https://api.github.com/users/frenzymadness/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "2a438c27b5a5828c8ea0dc958112eecffca70b12",
          "url": "https://api.github.com/repos/psf/requests/commits/2a438c27b5a5828c8ea0dc958112eecffca70b12",
          "html_url": "https://github.com/psf/requests/commit/2a438c27b5a5828c8ea0dc958112eecffca70b12"
        }
      ]
    },
    {
      "sha": "31ebb8102c00f8cf8b396a6356743cca4362e07b",
      "node_id": "C_kwDOABTKOtoAKDMxZWJiODEwMmMwMGY4Y2Y4YjM5NmE2MzU2NzQzY2NhNDM2MmUwN2I",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2024-04-11T19:49:35Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-04-11T19:49:35Z"
        },
        "message": "Merge pull request #6682 from frenzymadness/pytest8\n\nFix compatibility with pytest 8",
        "tree": {
          "sha": "2385e51eee2d2d4b19047668c8d2bede9a8825d7",
          "url": "https://api.github.com/repos/psf/requests/git/trees/2385e51eee2d2d4b19047668c8d2bede9a8825d7"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/31ebb8102c00f8cf8b396a6356743cca4362e07b",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJmGD7PCRC1aQ7uu5UhlAAA4q4QAFkmAyG81sxHqGEDMepTkbVm\nuz8IOiHBhR72qdIt38i9s0uhTo1aJtwAAWNJNFjt5A20M+4QAGULm+s506la7Hgt\nLiS6ISkJ3gm/i3LNWTzADXLU95tXm+iSbH2yKfn9aeu/5ELDj/I8id15HT9bOg9V\niq2cSqg2mP00OkVXYDsoq+cOrv6TnA62ELkhI0BQZo6jukT5+93rHfHZiJpDZq6F\n7UA9i0ze9+KVlalqYdsElp8ciP/u0GZdbPO4MNygj+7o3GZ6ySgTvxLkaYXccckd\nhVw4WTmYEyA9BP72JmaXhzBPniw0a2OUD/6vnb2fQesLsx9oZbY7+LOy+W17fozn\nUDxVmsol90AncjC+1IBCrUCj9A1UDiB3Tnm0NFMFQlufyOASIx2YMoNGvSiBgsjp\nNXhDVqFQP92d9WybdNkMg8TdxJor8Wo5IEgD34Mcojc6yDsLD5lVRK7YTOAp+Qf9\nejTs/5r84Kc8gewiI8Vu2oWL6JgNhOWc/PhHopRtyb29jj8axpXc9aRd8v1lDI8T\nOwyXTdBBBkKTp/HW8WIGaXlZvXoCiVNjUMajQM4WYAmBN8YuJMzdwC0cULlim6h9\n8ZGURzhCTNY3BRBmxfzxBpBlRFydYOF2L21GIy3MjqoZCv38YV2i6PmsNm+FcZsS\n7Igct1NjiSQbtNkFccpn\n=LWiw\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 2385e51eee2d2d4b19047668c8d2bede9a8825d7\nparent 0790ea4250bce844734f625a1a8b37d5581fd8cd\nparent cc23d1c6445d61c1e6905cae4861d6e3c3244274\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1712864975 -0500\ncommitter GitHub <noreply@github.com> 1712864975 -0500\n\nMerge pull request #6682 from frenzymadness/pytest8\n\nFix compatibility with pytest 8",
          "verified_at": "2024-11-05T15:48:14Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/31ebb8102c00f8cf8b396a6356743cca4362e07b",
      "html_url": "https://github.com/psf/requests/commit/31ebb8102c00f8cf8b396a6356743cca4362e07b",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/31ebb8102c00f8cf8b396a6356743cca4362e07b/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "0790ea4250bce844734f625a1a8b37d5581fd8cd",
          "url": "https://api.github.com/repos/psf/requests/commits/0790ea4250bce844734f625a1a8b37d5581fd8cd",
          "html_url": "https://github.com/psf/requests/commit/0790ea4250bce844734f625a1a8b37d5581fd8cd"
        },
        {
          "sha": "cc23d1c6445d61c1e6905cae4861d6e3c3244274",
          "url": "https://api.github.com/repos/psf/requests/commits/cc23d1c6445d61c1e6905cae4861d6e3c3244274",
          "html_url": "https://github.com/psf/requests/commit/cc23d1c6445d61c1e6905cae4861d6e3c3244274"
        }
      ]
    },
    {
      "sha": "60047ade64b0b882cbc94e047198818ab580911e",
      "node_id": "C_kwDOABTKOtoAKDYwMDQ3YWRlNjRiMGI4ODJjYmM5NGUwNDcxOTg4MThhYjU4MDkxMWU",
      "commit": {
        "author": {
          "name": "dependabot[bot]",
          "email": "49699333+dependabot[bot]@users.noreply.github.com",
          "date": "2024-04-15T16:40:35Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-04-15T16:40:35Z"
        },
        "message": "Bump github/codeql-action from 3.24.0 to 3.25.0\n\nBumps [github/codeql-action](https://github.com/github/codeql-action) from 3.24.0 to 3.25.0.\n- [Release notes](https://github.com/github/codeql-action/releases)\n- [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/github/codeql-action/compare/e8893c57a1f3a2b659b6b55564fdfdbbd2982911...df5a14dc28094dc936e103b37d749c6628682b60)\n\n---\nupdated-dependencies:\n- dependency-name: github/codeql-action\n  dependency-type: direct:production\n  update-type: version-update:semver-minor\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
        "tree": {
          "sha": "db5dbdaf342093e34afc6a377a2c3d035be22ac6",
          "url": "https://api.github.com/repos/psf/requests/git/trees/db5dbdaf342093e34afc6a377a2c3d035be22ac6"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/60047ade64b0b882cbc94e047198818ab580911e",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJmHViDCRC1aQ7uu5UhlAAASxgQACUM2zAX+Pbxtdj04px0iX7n\nv6/Al9SuYXLeJp2ZRVI3PgwDFrBtDHVzab+5uIEzlyh0Guw2Xa+sA5QafiM60gvR\nMthDFmhTVRzhwfzAIfT5fHETPKcjv9g4RArw1KkOKAlN0kbgxmJ8oRHChugQkP2o\nGOn0Yfa3sf+Y9cwLeQX5o5HxHm3jWs5VvfGgwHEG48SE3eOM2O59Ypwj5Pofy6KK\nYciaIjFOBZKPbQ93WCw59B6Ja9n9Jn4AHEe/FqaV4xIW+PUFMeKuV23nfzhfQt2O\nm4bB3fzUDR3MukOrX/a0zxJFKqC0qK3rRhpqTn0u3DkcxesbYaNDlEzMl/z4j/Ov\n5R5iDgdAibLB27GS1HZUoAvLW3iMAauN/xX+uItfoymo5eY/UDHl22u55+o50lia\nVq8hI+FlBdYBGpFQGiHi6sFxmBFokj0MhU4c6Z6HkFzXzlmTKW7Af9CVTQljcm2p\n2VfMWOPlG6E0+C23835wPJAeIuUE2jyvsJJNqOOEXXBCvCvHxqSwGl15225Fvbrz\neAOxYZhVCdIwoJR5otJa8xJmdBXtLhTht4Kr9c0zbLa74FWH6qxB5SkzcBIIIwgM\n14Lo+o5CWFFsvkdjY7OqqreHnx3V/CrRGGIIcisiihg+NSdf8ZLu7cKu45TbZZdQ\nItBzi0unyo+/IqVg5joH\n=SgQp\n-----END PGP SIGNATURE-----\n",
          "payload": "tree db5dbdaf342093e34afc6a377a2c3d035be22ac6\nparent 31ebb8102c00f8cf8b396a6356743cca4362e07b\nauthor dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> 1713199235 +0000\ncommitter GitHub <noreply@github.com> 1713199235 +0000\n\nBump github/codeql-action from 3.24.0 to 3.25.0\n\nBumps [github/codeql-action](https://github.com/github/codeql-action) from 3.24.0 to 3.25.0.\n- [Release notes](https://github.com/github/codeql-action/releases)\n- [Changelog](https://github.com/github/codeql-action/blob/main/CHANGELOG.md)\n- [Commits](https://github.com/github/codeql-action/compare/e8893c57a1f3a2b659b6b55564fdfdbbd2982911...df5a14dc28094dc936e103b37d749c6628682b60)\n\n---\nupdated-dependencies:\n- dependency-name: github/codeql-action\n  dependency-type: direct:production\n  update-type: version-update:semver-minor\n...\n\nSigned-off-by: dependabot[bot] <support@github.com>",
          "verified_at": "2024-11-05T15:48:14Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/60047ade64b0b882cbc94e047198818ab580911e",
      "html_url": "https://github.com/psf/requests/commit/60047ade64b0b882cbc94e047198818ab580911e",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/60047ade64b0b882cbc94e047198818ab580911e/comments",
      "author": {
        "login": "dependabot[bot]",
        "id": 49699333,
        "node_id": "MDM6Qm90NDk2OTkzMzM=",
        "avatar_url": "https://avatars.githubusercontent.com/in/29110?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/dependabot%5Bbot%5D",
        "html_url": "https://github.com/apps/dependabot",
        "followers_url": "https://api.github.com/users/dependabot%5Bbot%5D/followers",
        "following_url": "https://api.github.com/users/dependabot%5Bbot%5D/following{/other_user}",
        "gists_url": "https://api.github.com/users/dependabot%5Bbot%5D/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/dependabot%5Bbot%5D/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/dependabot%5Bbot%5D/subscriptions",
        "organizations_url": "https://api.github.com/users/dependabot%5Bbot%5D/orgs",
        "repos_url": "https://api.github.com/users/dependabot%5Bbot%5D/repos",
        "events_url": "https://api.github.com/users/dependabot%5Bbot%5D/events{/privacy}",
        "received_events_url": "https://api.github.com/users/dependabot%5Bbot%5D/received_events",
        "type": "Bot",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "31ebb8102c00f8cf8b396a6356743cca4362e07b",
          "url": "https://api.github.com/repos/psf/requests/commits/31ebb8102c00f8cf8b396a6356743cca4362e07b",
          "html_url": "https://github.com/psf/requests/commit/31ebb8102c00f8cf8b396a6356743cca4362e07b"
        }
      ]
    },
    {
      "sha": "f1bb07d39b74d6444e333879f8b8a3d9dd4d2311",
      "node_id": "C_kwDOABTKOtoAKGYxYmIwN2QzOWI3NGQ2NDQ0ZTMzMzg3OWY4YjhhM2Q5ZGQ0ZDIzMTE",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2024-04-15T17:01:39Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-04-15T17:01:39Z"
        },
        "message": "Merge pull request #6687 from psf/dependabot/github_actions/github/codeql-action-3.25.0\n\nBump github/codeql-action from 3.24.0 to 3.25.0",
        "tree": {
          "sha": "db5dbdaf342093e34afc6a377a2c3d035be22ac6",
          "url": "https://api.github.com/repos/psf/requests/git/trees/db5dbdaf342093e34afc6a377a2c3d035be22ac6"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/f1bb07d39b74d6444e333879f8b8a3d9dd4d2311",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJmHV1zCRC1aQ7uu5UhlAAAu70QAFhpu0PigQ3bf+roHsTvLfCJ\n8Ww/UMnNjjKMyPaYmsHwvXtjLVLgnULEHCk2khIl0iFbhn4LycTt4CenO/wXHxYu\nLDO638Uov7XLyjSNl8QorenMKfc1X3K+x9Y0sjKTEwSkfXGHuvRoMabV8lxPnQzf\n9ooO6cwRSOqE5DBH969PwTUNw3c8IBXyE9joEjLejA6fk5ATHQ5y0worBdn8Xg0h\nw1yBy1K8jIOZm9rZpIt33IipZ7q98oJoHQXP3Iq/+fY6zru2+ktr/td5rZl+2qMT\n2yNrnsyvqQh6+f5wB1szDlQ2gapeNItLFwbrBFJ7f6HjVoRum90kXwoAUimFRRu4\nWQPAEbfKAeLR3a61kRg8xZKJ5KZFJctLX2jDUWzZRHc0tWFK2Ow5QQGUzmBcE7zi\nnDTTzWPF+Q29eEHNWQn4PxmdEB6GPDQHVvLjaZ/Rs3g9NPgv6n5FRQ3iDE7umdmq\n+yZC4bJ4v9zMMnY/2OlPdSfl9KyyNpH2GRpUeQNpwxeA3m34kgKiV5qRdtJNljLV\ntvTEBY/do607tuhQTtf7CkCEYdMhDYA3VS8WkAWD8Ka8zxz525KlN9q87lPcFBHs\nVDjjRtkg7IA7jAYfCfYjFSJYyhrwdg7QBU4jqVp18RWg0W0l22MdxMnWF58oPa2s\ndOhNJIxmDg4IqsQVOw2a\n=AJ0k\n-----END PGP SIGNATURE-----\n",
          "payload": "tree db5dbdaf342093e34afc6a377a2c3d035be22ac6\nparent 31ebb8102c00f8cf8b396a6356743cca4362e07b\nparent 60047ade64b0b882cbc94e047198818ab580911e\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1713200499 -0600\ncommitter GitHub <noreply@github.com> 1713200499 -0600\n\nMerge pull request #6687 from psf/dependabot/github_actions/github/codeql-action-3.25.0\n\nBump github/codeql-action from 3.24.0 to 3.25.0",
          "verified_at": "2024-11-05T15:48:14Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/f1bb07d39b74d6444e333879f8b8a3d9dd4d2311",
      "html_url": "https://github.com/psf/requests/commit/f1bb07d39b74d6444e333879f8b8a3d9dd4d2311",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/f1bb07d39b74d6444e333879f8b8a3d9dd4d2311/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "31ebb8102c00f8cf8b396a6356743cca4362e07b",
          "url": "https://api.github.com/repos/psf/requests/commits/31ebb8102c00f8cf8b396a6356743cca4362e07b",
          "html_url": "https://github.com/psf/requests/commit/31ebb8102c00f8cf8b396a6356743cca4362e07b"
        },
        {
          "sha": "60047ade64b0b882cbc94e047198818ab580911e",
          "url": "https://api.github.com/repos/psf/requests/commits/60047ade64b0b882cbc94e047198818ab580911e",
          "html_url": "https://github.com/psf/requests/commit/60047ade64b0b882cbc94e047198818ab580911e"
        }
      ]
    },
    {
      "sha": "2d5f54779ad174035c5437b3b3c1146b0eaf60fe",
      "node_id": "C_kwDOABTKOtoAKDJkNWY1NDc3OWFkMTc0MDM1YzU0MzdiM2IzYzExNDZiMGVhZjYwZmU",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2024-04-23T17:50:19Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-04-23T17:50:19Z"
        },
        "message": "Pin 3.8 and 3.9 runners back to macos-13 (#6688)",
        "tree": {
          "sha": "564450f07178316e24637d80f910fd7248c3fa88",
          "url": "https://api.github.com/repos/psf/requests/git/trees/564450f07178316e24637d80f910fd7248c3fa88"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/2d5f54779ad174035c5437b3b3c1146b0eaf60fe",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJmJ/TbCRC1aQ7uu5UhlAAAf/IQAKZ5cPcjjHkFZmY5ZziUng9Z\nKenUlyyCc8cca4fz8i8gEn6Mfl+MqVDqKUg3/iZGCmJ0NskkX75LS7LxXInOj+e+\nAVCms949EGWAngPIqE+fFuy2TSvkjfIh8/rvYYzMYUyx/Bvh5yQTgDJBFolJAKay\nKnbH4P4TewJsyNDJk0aUfcht/+vGp+uBNWVVndRhu4cYF4lijmt4SyAEd+Wwb04Z\nRpgHyG0CIPG1Gow3sW9jJpXvFYNerdUGUNAjiQsTFLF91VK8lHEjL99LlDAhjeUJ\nFSD6QUn6Zk1/5BZ2QnJoeWyHhtRpzHHe2nPTYA18iCbhR/2RWn9wyC8sHT1ss10v\nHzo3rVx69z7Lgbnah57uUohlC0nV9IWAq24+mjdS+nFYG1kFFcmP2yt4twXIxcEI\nfp7TGkiI+hbvmk4OLBtqlqbth2RQRO6OlzlGtoot501FHnXSCtYCpJXrKZTQnVkb\nSLcd7ho+FWG1JfAKEJb7FgITwTTctI47FQ84VXz/MoU0jvdZPQgeIjSeF7bVyVeW\nhTJKAumOLLQcdiKy+tkoLoj8FP9pHLpl4QKrVvv8rRIln9ARQ1v7Sgnb/KdfE+jW\nbqokz+KPJdEyZgWlNc94Z3czDQDaRlvMivOXzFn7gGD2piYgN5wAG7NoUq/Jot77\nxxueLqYUfS88daPg4Saz\n=ySZh\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 564450f07178316e24637d80f910fd7248c3fa88\nparent f1bb07d39b74d6444e333879f8b8a3d9dd4d2311\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1713894619 -0600\ncommitter GitHub <noreply@github.com> 1713894619 -0700\n\nPin 3.8 and 3.9 runners back to macos-13 (#6688)\n\n",
          "verified_at": "2024-11-05T15:48:14Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/2d5f54779ad174035c5437b3b3c1146b0eaf60fe",
      "html_url": "https://github.com/psf/requests/commit/2d5f54779ad174035c5437b3b3c1146b0eaf60fe",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/2d5f54779ad174035c5437b3b3c1146b0eaf60fe/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "f1bb07d39b74d6444e333879f8b8a3d9dd4d2311",
          "url": "https://api.github.com/repos/psf/requests/commits/f1bb07d39b74d6444e333879f8b8a3d9dd4d2311",
          "html_url": "https://github.com/psf/requests/commit/f1bb07d39b74d6444e333879f8b8a3d9dd4d2311"
        }
      ]
    },
    {
      "sha": "bf24b7d8d17da34be720c19e5978b2d3bf94a53b",
      "node_id": "C_kwDOABTKOtoAKGJmMjRiN2Q4ZDE3ZGEzNGJlNzIwYzE5ZTU5NzhiMmQzYmY5NGE1M2I",
      "commit": {
        "author": {
          "name": "franekmagiera",
          "email": "framagie@gmail.com",
          "date": "2024-05-12T20:08:24Z"
        },
        "committer": {
          "name": "franekmagiera",
          "email": "framagie@gmail.com",
          "date": "2024-05-12T20:08:24Z"
        },
        "message": "Use an invalid URI that will not cause httpbin to throw 500",
        "tree": {
          "sha": "0d4fa085cbaab1b3ca322022ae1c63e0e3062995",
          "url": "https://api.github.com/repos/psf/requests/git/trees/0d4fa085cbaab1b3ca322022ae1c63e0e3062995"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/bf24b7d8d17da34be720c19e5978b2d3bf94a53b",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/bf24b7d8d17da34be720c19e5978b2d3bf94a53b",
      "html_url": "https://github.com/psf/requests/commit/bf24b7d8d17da34be720c19e5978b2d3bf94a53b",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/bf24b7d8d17da34be720c19e5978b2d3bf94a53b/comments",
      "author": {
        "login": "franekmagiera",
        "id": 36968154,
        "node_id": "MDQ6VXNlcjM2OTY4MTU0",
        "avatar_url": "https://avatars.githubusercontent.com/u/36968154?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/franekmagiera",
        "html_url": "https://github.com/franekmagiera",
        "followers_url": "https://api.github.com/users/franekmagiera/followers",
        "following_url": "https://api.github.com/users/franekmagiera/following{/other_user}",
        "gists_url": "https://api.github.com/users/franekmagiera/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/franekmagiera/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/franekmagiera/subscriptions",
        "organizations_url": "https://api.github.com/users/franekmagiera/orgs",
        "repos_url": "https://api.github.com/users/franekmagiera/repos",
        "events_url": "https://api.github.com/users/franekmagiera/events{/privacy}",
        "received_events_url": "https://api.github.com/users/franekmagiera/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "franekmagiera",
        "id": 36968154,
        "node_id": "MDQ6VXNlcjM2OTY4MTU0",
        "avatar_url": "https://avatars.githubusercontent.com/u/36968154?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/franekmagiera",
        "html_url": "https://github.com/franekmagiera",
        "followers_url": "https://api.github.com/users/franekmagiera/followers",
        "following_url": "https://api.github.com/users/franekmagiera/following{/other_user}",
        "gists_url": "https://api.github.com/users/franekmagiera/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/franekmagiera/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/franekmagiera/subscriptions",
        "organizations_url": "https://api.github.com/users/franekmagiera/orgs",
        "repos_url": "https://api.github.com/users/franekmagiera/repos",
        "events_url": "https://api.github.com/users/franekmagiera/events{/privacy}",
        "received_events_url": "https://api.github.com/users/franekmagiera/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "2d5f54779ad174035c5437b3b3c1146b0eaf60fe",
          "url": "https://api.github.com/repos/psf/requests/commits/2d5f54779ad174035c5437b3b3c1146b0eaf60fe",
          "html_url": "https://github.com/psf/requests/commit/2d5f54779ad174035c5437b3b3c1146b0eaf60fe"
        }
      ]
    },
    {
      "sha": "d6dded3f00afcf56a7e866cb0732799045301eb0",
      "node_id": "C_kwDOABTKOtoAKGQ2ZGRlZDNmMDBhZmNmNTZhN2U4NjZjYjA3MzI3OTkwNDUzMDFlYjA",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2024-05-12T21:33:47Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-05-12T21:33:47Z"
        },
        "message": "Merge pull request #6700 from franekmagiera/update-redirect-to-invalid-uri-test\n\nUse an invalid URI that will not cause httpbin to throw 500",
        "tree": {
          "sha": "0d4fa085cbaab1b3ca322022ae1c63e0e3062995",
          "url": "https://api.github.com/repos/psf/requests/git/trees/0d4fa085cbaab1b3ca322022ae1c63e0e3062995"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/d6dded3f00afcf56a7e866cb0732799045301eb0",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJmQTW7CRC1aQ7uu5UhlAAAN7kQAGTvj8QxdMmLTQegZeLOxAWc\nObGMr4lcpJlf1nls2GJ5ir11ppGLzHmIdIEzUVqW5sqFwkYyihhyIMKWZUBBOCWZ\nP3/AeiC/1zaIT4/V1/tBgf4VKLO8Lc4BlQjt66UKE0G0vjXiC4zlKLceE31PX2eQ\njAMC/vQbImb5NMmxGDMADkz7IKHGf/QFNpsYkKNe9jiicebaBuB99K+TsyioFJ+9\nz6b4dffZhBQKcn4dIDmQC6W/3vuDeo08lIDzX6pNFoQEX2aetdhYRd6RdxxWLL1R\n+R21bS4AL2qFKrLBoZ8/vqroA/DRpbALYuJWq7rezUenEByfLIRYPufiqFLOgxqg\nDaUM34Sh4zB6KOupan8yns/k8PnWkSFa39v+NmbrpUoqcYLOv86tKgc807v9E25x\nw4mTBYL9fkRvZa1M1LOgXghMUO8DyayqEPUi3WEsvLLSyvc+nvpYUZIRTkIZE5Y6\nP6HB+XAzCp4zKIv4gT7eJG6mtZe/W/6tqKEQsOX0iIP4Ww7k53sY1h+ysCTGKBxs\nnXreesfJ50CTt/p5ZM0Kae9/nEurC2vriAqPkVUK20MBc1BsopoadkLMPrtIOcxu\n3TzEpqOLFZR9WIoZGpSMhHyHtYNb5oK24RaxeGGtiaLwWJYfFMeVhwuLJHBOq1x7\nI3xfhAicX94NEs4OYkoW\n=oNFn\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 0d4fa085cbaab1b3ca322022ae1c63e0e3062995\nparent 2d5f54779ad174035c5437b3b3c1146b0eaf60fe\nparent bf24b7d8d17da34be720c19e5978b2d3bf94a53b\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1715549627 -0500\ncommitter GitHub <noreply@github.com> 1715549627 -0500\n\nMerge pull request #6700 from franekmagiera/update-redirect-to-invalid-uri-test\n\nUse an invalid URI that will not cause httpbin to throw 500",
          "verified_at": "2024-11-05T15:48:14Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/d6dded3f00afcf56a7e866cb0732799045301eb0",
      "html_url": "https://github.com/psf/requests/commit/d6dded3f00afcf56a7e866cb0732799045301eb0",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/d6dded3f00afcf56a7e866cb0732799045301eb0/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "2d5f54779ad174035c5437b3b3c1146b0eaf60fe",
          "url": "https://api.github.com/repos/psf/requests/commits/2d5f54779ad174035c5437b3b3c1146b0eaf60fe",
          "html_url": "https://github.com/psf/requests/commit/2d5f54779ad174035c5437b3b3c1146b0eaf60fe"
        },
        {
          "sha": "bf24b7d8d17da34be720c19e5978b2d3bf94a53b",
          "url": "https://api.github.com/repos/psf/requests/commits/bf24b7d8d17da34be720c19e5978b2d3bf94a53b",
          "html_url": "https://github.com/psf/requests/commit/bf24b7d8d17da34be720c19e5978b2d3bf94a53b"
        }
      ]
    },
    {
      "sha": "555b870eb19d497ddb67042645420083ec8efb02",
      "node_id": "C_kwDOABTKOtoAKDU1NWI4NzBlYjE5ZDQ5N2RkYjY3MDQyNjQ1NDIwMDgzZWM4ZWZiMDI",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2024-05-14T21:59:26Z"
        },
        "committer": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2024-05-14T22:26:04Z"
        },
        "message": "Allow character detection dependencies to be optional in post-packaging steps",
        "tree": {
          "sha": "bcab4af2ae4ffd043bb11c1fe40967fa3a24d404",
          "url": "https://api.github.com/repos/psf/requests/git/trees/bcab4af2ae4ffd043bb11c1fe40967fa3a24d404"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/555b870eb19d497ddb67042645420083ec8efb02",
        "comment_count": 0,
        "verification": {
          "verified": false,
          "reason": "unsigned",
          "signature": null,
          "payload": null,
          "verified_at": null
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/555b870eb19d497ddb67042645420083ec8efb02",
      "html_url": "https://github.com/psf/requests/commit/555b870eb19d497ddb67042645420083ec8efb02",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/555b870eb19d497ddb67042645420083ec8efb02/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "d6dded3f00afcf56a7e866cb0732799045301eb0",
          "url": "https://api.github.com/repos/psf/requests/commits/d6dded3f00afcf56a7e866cb0732799045301eb0",
          "html_url": "https://github.com/psf/requests/commit/d6dded3f00afcf56a7e866cb0732799045301eb0"
        }
      ]
    },
    {
      "sha": "0c030f78d24f29a459dbf39b28b4cc765e2153d7",
      "node_id": "C_kwDOABTKOtoAKDBjMDMwZjc4ZDI0ZjI5YTQ1OWRiZjM5YjI4YjRjYzc2NWUyMTUzZDc",
      "commit": {
        "author": {
          "name": "Ian Stapleton Cordasco",
          "email": "graffatcolmingov@gmail.com",
          "date": "2024-05-15T00:15:19Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-05-15T00:15:19Z"
        },
        "message": "Merge pull request #6702 from nateprewitt/no_char_detection\n\nAllow optional char detection dependencies in post-packaging",
        "tree": {
          "sha": "bcab4af2ae4ffd043bb11c1fe40967fa3a24d404",
          "url": "https://api.github.com/repos/psf/requests/git/trees/bcab4af2ae4ffd043bb11c1fe40967fa3a24d404"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/0c030f78d24f29a459dbf39b28b4cc765e2153d7",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJmQ/6XCRC1aQ7uu5UhlAAAUhcQAIkvQUrlM7zGkx/GcHapreDf\nF0d/7QLb0JgXEu1z9W3xg5Bw6NtL/XNAPrsQWU0D7vdyEAeA0rhtKJncsnVJuHmt\nDq3xPzHMlWtuUfrZj2rVQUtb0Y8YwpgkM2xHMpRsjRMUatZgE2IiyHdUIzlcPtJi\nwjsU9KFCrimdoZGoNsZLqB/9ayLVJgYQENNZh9lzqAVJFPCKnQNjqL4KPuZ2F30X\nNCjmFIK8Yg/wf7CI+6+OQheoOFEc8RqrIjm7nKgtl5U7qthXqacWaWVGfpTBlDSQ\nULBZrTe3zp8wudlNeYvctRV4XX70kHKUD+qfOFd5M6LiEEbkU3diBwKPWuQDlRLt\nTI31BsVjED0Yay2s5hfp4iLFf5XTefCGkBnUnktz74ZzwPnZLAavyBAdNFJZhXVF\nf+BwY7bpyuw8nyJk/Sncx8xCszPJL36kUztIPIALPGa/4ehQjjuWj43yfZ7vAMrR\n+dbqcEHbwhUNdo7ORptddFjItQADAZa1hv57bbbb8/LtbW0afHo6XA1ccTnL0oGZ\nlMvXYlOH+apB74i06DiyoqMpg+hJHbYsTDRETIc/y85dO03YMUPRKpGnRtBTQvos\nu7gJZtK8JL0jRIRRqQVD4CG4dlUXxQ2vc6vmgkVVyGlSUVHbH+74cpTaYq0sPmWZ\nu7p8mdGVShtY9X/pOHrm\n=T7bM\n-----END PGP SIGNATURE-----\n",
          "payload": "tree bcab4af2ae4ffd043bb11c1fe40967fa3a24d404\nparent d6dded3f00afcf56a7e866cb0732799045301eb0\nparent 555b870eb19d497ddb67042645420083ec8efb02\nauthor Ian Stapleton Cordasco <graffatcolmingov@gmail.com> 1715732119 -0500\ncommitter GitHub <noreply@github.com> 1715732119 -0500\n\nMerge pull request #6702 from nateprewitt/no_char_detection\n\nAllow optional char detection dependencies in post-packaging",
          "verified_at": "2024-11-05T15:48:14Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/0c030f78d24f29a459dbf39b28b4cc765e2153d7",
      "html_url": "https://github.com/psf/requests/commit/0c030f78d24f29a459dbf39b28b4cc765e2153d7",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/0c030f78d24f29a459dbf39b28b4cc765e2153d7/comments",
      "author": {
        "login": "sigmavirus24",
        "id": 240830,
        "node_id": "MDQ6VXNlcjI0MDgzMA==",
        "avatar_url": "https://avatars.githubusercontent.com/u/240830?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/sigmavirus24",
        "html_url": "https://github.com/sigmavirus24",
        "followers_url": "https://api.github.com/users/sigmavirus24/followers",
        "following_url": "https://api.github.com/users/sigmavirus24/following{/other_user}",
        "gists_url": "https://api.github.com/users/sigmavirus24/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/sigmavirus24/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/sigmavirus24/subscriptions",
        "organizations_url": "https://api.github.com/users/sigmavirus24/orgs",
        "repos_url": "https://api.github.com/users/sigmavirus24/repos",
        "events_url": "https://api.github.com/users/sigmavirus24/events{/privacy}",
        "received_events_url": "https://api.github.com/users/sigmavirus24/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "d6dded3f00afcf56a7e866cb0732799045301eb0",
          "url": "https://api.github.com/repos/psf/requests/commits/d6dded3f00afcf56a7e866cb0732799045301eb0",
          "html_url": "https://github.com/psf/requests/commit/d6dded3f00afcf56a7e866cb0732799045301eb0"
        },
        {
          "sha": "555b870eb19d497ddb67042645420083ec8efb02",
          "url": "https://api.github.com/repos/psf/requests/commits/555b870eb19d497ddb67042645420083ec8efb02",
          "html_url": "https://github.com/psf/requests/commit/555b870eb19d497ddb67042645420083ec8efb02"
        }
      ]
    },
    {
      "sha": "9a40d1277807f0a4f26c9a37eea8ec90faa8aadc",
      "node_id": "C_kwDOABTKOtoAKDlhNDBkMTI3NzgwN2YwYTRmMjZjOWEzN2VlYThlYzkwZmFhOGFhZGM",
      "commit": {
        "author": {
          "name": "agubelu",
          "email": "agubelu@users.noreply.github.com",
          "date": "2024-05-15T20:07:26Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-05-15T20:07:26Z"
        },
        "message": "Avoid reloading root certificates to improve concurrent performance (#6667)",
        "tree": {
          "sha": "c9efab2276aebd6467ba9d17ddea153e1c3424f9",
          "url": "https://api.github.com/repos/psf/requests/git/trees/c9efab2276aebd6467ba9d17ddea153e1c3424f9"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/9a40d1277807f0a4f26c9a37eea8ec90faa8aadc",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJmRRX+CRC1aQ7uu5UhlAAASpgQAFSf7bkmKiIHLvsGpaHzF9f5\nifKoX6HxAWA53WvgXNlGNoqh/hzIvRioZ6DKPybm7VXX1X8OQ2afqOLx9gEtQTel\nBrISY8HzFcquHuIMYdUwtrbc4M3pS8VlWAPknp8fXD6wTvDGORwvzdECzMm86Vsj\nDDWfeHISV/Z0r5TStyQ43hzZuIGZgPv+YVKAS8Zu7fMqThuBDNujENfIEBb/T9VN\nBIYBDKn1ePOSB9w5kf9lHH04VH0ch9xoloTTyKqRpODeObi8XsBq/3ntjaQcHDPZ\nq6yzspLkoKI+lmCUSzvj/F3B2E7W0lV5QC6JDCFm2zaQb252WWZ+j+0trJw36Tik\nzKyD3QOeNuLBqg0BkRzX0Z9HHUUaS0EGhbgWxYaESJL8RMKqLjHZyH6kyR8l1yA/\ngsq2WNPfYD7kvzQiXSUKn/glaxjjXElsFMP4S6+qgYrUSqrFM90sJ2REOv2nzapX\n+YJ2+00KL8kaKIsG8r36yq+EghrRw9ccdHDG+j6S6bZ+rOZOhFypIPxAN93llieu\npJs12K8wkM0ImSFWNPYk3DfO9j1KV/zqczbteeY8JkgcNw29Oi6PhmF+ZnUmvAC4\nPtQ+FIadE95Jf6+G7W+FfnT+vST7SP7860ffDPyLFdRk3JCbn9P7PmE3N4Hm1E5t\nfvCEMuqp5dMILFMtU09g\n=Bplz\n-----END PGP SIGNATURE-----\n",
          "payload": "tree c9efab2276aebd6467ba9d17ddea153e1c3424f9\nparent 0c030f78d24f29a459dbf39b28b4cc765e2153d7\nauthor agubelu <agubelu@users.noreply.github.com> 1715803646 +0200\ncommitter GitHub <noreply@github.com> 1715803646 -0600\n\nAvoid reloading root certificates to improve concurrent performance (#6667)\n\n",
          "verified_at": "2024-11-05T15:48:14Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/9a40d1277807f0a4f26c9a37eea8ec90faa8aadc",
      "html_url": "https://github.com/psf/requests/commit/9a40d1277807f0a4f26c9a37eea8ec90faa8aadc",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/9a40d1277807f0a4f26c9a37eea8ec90faa8aadc/comments",
      "author": {
        "login": "agubelu",
        "id": 1207202,
        "node_id": "MDQ6VXNlcjEyMDcyMDI=",
        "avatar_url": "https://avatars.githubusercontent.com/u/1207202?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/agubelu",
        "html_url": "https://github.com/agubelu",
        "followers_url": "https://api.github.com/users/agubelu/followers",
        "following_url": "https://api.github.com/users/agubelu/following{/other_user}",
        "gists_url": "https://api.github.com/users/agubelu/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/agubelu/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/agubelu/subscriptions",
        "organizations_url": "https://api.github.com/users/agubelu/orgs",
        "repos_url": "https://api.github.com/users/agubelu/repos",
        "events_url": "https://api.github.com/users/agubelu/events{/privacy}",
        "received_events_url": "https://api.github.com/users/agubelu/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "0c030f78d24f29a459dbf39b28b4cc765e2153d7",
          "url": "https://api.github.com/repos/psf/requests/commits/0c030f78d24f29a459dbf39b28b4cc765e2153d7",
          "html_url": "https://github.com/psf/requests/commit/0c030f78d24f29a459dbf39b28b4cc765e2153d7"
        }
      ]
    },
    {
      "sha": "d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "node_id": "C_kwDOABTKOtoAKGQ2ZWJjNGEyZjFmNjhiN2UzNTVmYjdlNGRkNWZmYzA4NDU1NDdmOWY",
      "commit": {
        "author": {
          "name": "Nate Prewitt",
          "email": "nate.prewitt@gmail.com",
          "date": "2024-05-20T15:46:49Z"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com",
          "date": "2024-05-20T15:46:49Z"
        },
        "message": "v2.32.0",
        "tree": {
          "sha": "3fa7dfe759e3f9a3e9174ba409746708fd399bf6",
          "url": "https://api.github.com/repos/psf/requests/git/trees/3fa7dfe759e3f9a3e9174ba409746708fd399bf6"
        },
        "url": "https://api.github.com/repos/psf/requests/git/commits/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
        "comment_count": 0,
        "verification": {
          "verified": true,
          "reason": "valid",
          "signature": "-----BEGIN PGP SIGNATURE-----\n\nwsFcBAABCAAQBQJmS3BpCRC1aQ7uu5UhlAAA+UgQACSYv+mjY87EqEZkkrhzBLpQ\nRoL8C8dZD7Gd5yAC8mY0uYWylWFAQEwk70lKxJuhdWXJJ1ujBoiF3+Fl2TxaFSJw\neBCL+aO82Z85EnnVbF5aA/PxQoIEM+jQbLiEunlI0RWsgNkEYiB6X5miHL0KkQbj\n3t7jiXAo1li8TVbXwqZmbn+7WQsiuxZI7Vrcke9l5qmRVsdjN/cJ4Wk4FoZ/FWb4\n0YdN4v2eGbriI1tEnlx+gbccrwS8PK7iCzibU9y8qSylEGKVFo6/tGO9ZA94h2zg\n9EA70Q6E8Ay7008KULJ3aLvN5OqWopeLNXK8Gm15KRLBjleM5kltZsorcu32dHuR\n6LJppZNvhWdq0w+YDt8T/R8EaWOZLTr9WTEO/Ll6YchLLz0lLRKRPd8yJn9nukX9\np4HC1wUI93KX9HvM6PwdYENgLQL5MTPrHxjMX5CXu6fT7uzBp9s7U0JSSnF+2HSc\n6HziGNHrUzQxYBL5QXia7nvX0Kx12QSNoUtoeEGFRS/rbUIHX5XLBdR0UL3MEedp\n4Jj5CotW8yMIs0WPRSzJhxiTfHTQpeZgVZ6uyGGR0T2RGj+8hz1AaQnFbaFz1VOD\nrg+JM8hrME/vNQNfVTmrLrvLfBpP5QL7SgSkb9y0BzZrt0dxLxAXI9wiMFzjIPvc\nrdpZrHmvOYUgo8SZUWjJ\n=tYIJ\n-----END PGP SIGNATURE-----\n",
          "payload": "tree 3fa7dfe759e3f9a3e9174ba409746708fd399bf6\nparent 9a40d1277807f0a4f26c9a37eea8ec90faa8aadc\nauthor Nate Prewitt <nate.prewitt@gmail.com> 1716220009 -0700\ncommitter GitHub <noreply@github.com> 1716220009 -0700\n\nv2.32.0\n\n",
          "verified_at": "2024-11-05T15:46:02Z"
        }
      },
      "url": "https://api.github.com/repos/psf/requests/commits/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "html_url": "https://github.com/psf/requests/commit/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "comments_url": "https://api.github.com/repos/psf/requests/commits/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/comments",
      "author": {
        "login": "nateprewitt",
        "id": 5271761,
        "node_id": "MDQ6VXNlcjUyNzE3NjE=",
        "avatar_url": "https://avatars.githubusercontent.com/u/5271761?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/nateprewitt",
        "html_url": "https://github.com/nateprewitt",
        "followers_url": "https://api.github.com/users/nateprewitt/followers",
        "following_url": "https://api.github.com/users/nateprewitt/following{/other_user}",
        "gists_url": "https://api.github.com/users/nateprewitt/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/nateprewitt/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/nateprewitt/subscriptions",
        "organizations_url": "https://api.github.com/users/nateprewitt/orgs",
        "repos_url": "https://api.github.com/users/nateprewitt/repos",
        "events_url": "https://api.github.com/users/nateprewitt/events{/privacy}",
        "received_events_url": "https://api.github.com/users/nateprewitt/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "committer": {
        "login": "web-flow",
        "id": 19864447,
        "node_id": "MDQ6VXNlcjE5ODY0NDQ3",
        "avatar_url": "https://avatars.githubusercontent.com/u/19864447?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/web-flow",
        "html_url": "https://github.com/web-flow",
        "followers_url": "https://api.github.com/users/web-flow/followers",
        "following_url": "https://api.github.com/users/web-flow/following{/other_user}",
        "gists_url": "https://api.github.com/users/web-flow/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/web-flow/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/web-flow/subscriptions",
        "organizations_url": "https://api.github.com/users/web-flow/orgs",
        "repos_url": "https://api.github.com/users/web-flow/repos",
        "events_url": "https://api.github.com/users/web-flow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/web-flow/received_events",
        "type": "User",
        "user_view_type": "public",
        "site_admin": false
      },
      "parents": [
        {
          "sha": "9a40d1277807f0a4f26c9a37eea8ec90faa8aadc",
          "url": "https://api.github.com/repos/psf/requests/commits/9a40d1277807f0a4f26c9a37eea8ec90faa8aadc",
          "html_url": "https://github.com/psf/requests/commit/9a40d1277807f0a4f26c9a37eea8ec90faa8aadc"
        }
      ]
    }
  ],
  "files": [
    {
      "sha": "332c3aea9764662b5efdb9a325d5359f6be4bf86",
      "filename": ".github/ISSUE_TEMPLATE/Custom.md",
      "status": "modified",
      "additions": 3,
      "deletions": 0,
      "changes": 3,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/.github%2FISSUE_TEMPLATE%2FCustom.md",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/.github%2FISSUE_TEMPLATE%2FCustom.md",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/.github%2FISSUE_TEMPLATE%2FCustom.md?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -1,6 +1,9 @@\n ---\r\n name: Request for Help\r\n about: Guidance on using Requests.\r\n+labels:\r\n+- \"Question/Not a bug\"\r\n+- \"actions/autoclose-qa\"\r\n \r\n ---\r\n \r"
    },
    {
      "sha": "544113ae1c5c2a67d27cbfbbe9b405ff47e6ebba",
      "filename": ".github/ISSUE_TEMPLATE/Feature_request.md",
      "status": "modified",
      "additions": 3,
      "deletions": 0,
      "changes": 3,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/.github%2FISSUE_TEMPLATE%2FFeature_request.md",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/.github%2FISSUE_TEMPLATE%2FFeature_request.md",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/.github%2FISSUE_TEMPLATE%2FFeature_request.md?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -1,6 +1,9 @@\n ---\r\n name: Feature request\r\n about: Suggest an idea for this project\r\n+labels:\r\n+- \"Feature Request\"\r\n+- \"actions/autoclose-feat\"\r\n \r\n ---\r\n \r"
    },
    {
      "sha": "2be85338e3a7033ae53dbe11ea8897bc120b9652",
      "filename": ".github/dependabot.yml",
      "status": "added",
      "additions": 11,
      "deletions": 0,
      "changes": 11,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/.github%2Fdependabot.yml",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/.github%2Fdependabot.yml",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/.github%2Fdependabot.yml?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,11 @@\n+version: 2\n+updates:\n+  - package-ecosystem: github-actions\n+    directory: /\n+    schedule:\n+      interval: weekly\n+    ignore:\n+      # Ignore all patch releases as we can manually\n+      # upgrade if we run into a bug and need a fix.\n+      - dependency-name: \"*\"\n+        update-types: [\"version-update:semver-patch\"]"
    },
    {
      "sha": "bedc75ea5b9c53f1c8760ae69ac54ab487166dc1",
      "filename": ".github/workflows/close-issues.yml",
      "status": "added",
      "additions": 35,
      "deletions": 0,
      "changes": 35,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/.github%2Fworkflows%2Fclose-issues.yml",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/.github%2Fworkflows%2Fclose-issues.yml",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/.github%2Fworkflows%2Fclose-issues.yml?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,35 @@\n+name: 'Autoclose Issues'\n+\n+on:\n+  issues:\n+    types:\n+      - labeled\n+\n+permissions:\n+  issues: write\n+\n+jobs:\n+  close_qa:\n+    if: github.event.label.name == 'actions/autoclose-qa'\n+    runs-on: ubuntu-latest\n+    steps:\n+      - env:\n+          ISSUE_URL: ${{ github.event.issue.html_url }}\n+          GH_TOKEN: ${{ github.token }}\n+        run: |\n+          gh issue close $ISSUE_URL \\\n+            --comment \"As described in the template, we won't be able to answer questions on this issue tracker. Please use [Stack Overflow](https://stackoverflow.com/)\" \\\n+            --reason completed\n+          gh issue lock $ISSUE_URL --reason off_topic\n+  close_feature_request:\n+    if: github.event.label.name == 'actions/autoclose-feat'\n+    runs-on: ubuntu-latest\n+    steps:\n+      - env:\n+          ISSUE_URL: ${{ github.event.issue.html_url }}\n+          GH_TOKEN: ${{ github.token }}\n+        run: |\n+          gh issue close $ISSUE_URL \\\n+            --comment \"As described in the template, Requests is not accepting feature requests\" \\\n+            --reason \"not planned\"\n+          gh issue lock $ISSUE_URL --reason off_topic"
    },
    {
      "sha": "b6d544640be9c9175f04a89fd40f93df073c5157",
      "filename": ".github/workflows/codeql-analysis.yml",
      "status": "modified",
      "additions": 4,
      "deletions": 4,
      "changes": 8,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/.github%2Fworkflows%2Fcodeql-analysis.yml",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/.github%2Fworkflows%2Fcodeql-analysis.yml",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/.github%2Fworkflows%2Fcodeql-analysis.yml?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -32,7 +32,7 @@ jobs:\n \n     steps:\n     - name: Checkout repository\n-      uses: actions/checkout@v2\n+      uses: actions/checkout@8ade135a41bc03ea155e62e844d188df1ea18608 # v4.1.0\n       with:\n         # We must fetch at least the immediate parents so that if this is\n         # a pull request then we can checkout the head.\n@@ -45,7 +45,7 @@ jobs:\n \n     # Initializes the CodeQL tools for scanning.\n     - name: Initialize CodeQL\n-      uses: github/codeql-action/init@v1\n+      uses: github/codeql-action/init@df5a14dc28094dc936e103b37d749c6628682b60 # v3.25.0\n       with:\n         languages: \"python\"\n         # If you wish to specify custom queries, you can do so here or in a config file.\n@@ -56,7 +56,7 @@ jobs:\n     # Autobuild attempts to build any compiled languages  (C/C++, C#, or Java).\n     # If this step fails, then you should remove it and run the build manually (see below)\n     - name: Autobuild\n-      uses: github/codeql-action/autobuild@v1\n+      uses: github/codeql-action/autobuild@df5a14dc28094dc936e103b37d749c6628682b60 # v3.25.0\n \n     # ℹ️ Command-line programs to run using the OS shell.\n     # 📚 https://git.io/JvXDl\n@@ -70,4 +70,4 @@ jobs:\n     #   make release\n \n     - name: Perform CodeQL Analysis\n-      uses: github/codeql-action/analyze@v1\n+      uses: github/codeql-action/analyze@df5a14dc28094dc936e103b37d749c6628682b60 # v3.25.0"
    },
    {
      "sha": "46a7862eacb4b8f2dee5ebc16eac23f5f904da3a",
      "filename": ".github/workflows/lint.yml",
      "status": "modified",
      "additions": 3,
      "deletions": 3,
      "changes": 6,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/.github%2Fworkflows%2Flint.yml",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/.github%2Fworkflows%2Flint.yml",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/.github%2Fworkflows%2Flint.yml?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -11,10 +11,10 @@ jobs:\n     timeout-minutes: 10\n \n     steps:\n-    - uses: actions/checkout@v3\n+    - uses: actions/checkout@8ade135a41bc03ea155e62e844d188df1ea18608 # v4.1.0\n     - name: Set up Python\n-      uses: actions/setup-python@v4\n+      uses: actions/setup-python@82c7e631bb3cdc910f68e0081d67478d79c6982d # v5.1.0\n       with:\n         python-version: \"3.x\"\n     - name: Run pre-commit\n-      uses: pre-commit/action@v3.0.0\n+      uses: pre-commit/action@646c83fcd040023954eafda54b4db0192ce70507 # v3.0.0"
    },
    {
      "sha": "7d5a3c6525646fd421c4a284f3dd76486fbbfce3",
      "filename": ".github/workflows/lock-issues.yml",
      "status": "modified",
      "additions": 1,
      "deletions": 1,
      "changes": 2,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/.github%2Fworkflows%2Flock-issues.yml",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/.github%2Fworkflows%2Flock-issues.yml",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/.github%2Fworkflows%2Flock-issues.yml?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -13,7 +13,7 @@ jobs:\n     if: github.repository_owner == 'psf'\n     runs-on: ubuntu-latest\n     steps:\n-      - uses: dessant/lock-threads@v3\n+      - uses: dessant/lock-threads@d42e5f49803f3c4e14ffee0378e31481265dda22 # v5.0.0\n         with:\n             issue-lock-inactive-days: 90\n             pr-lock-inactive-days: 90"
    },
    {
      "sha": "c35af968c47cae08ce08b424d430b69e189de248",
      "filename": ".github/workflows/run-tests.yml",
      "status": "modified",
      "additions": 32,
      "deletions": 7,
      "changes": 39,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/.github%2Fworkflows%2Frun-tests.yml",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/.github%2Fworkflows%2Frun-tests.yml",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/.github%2Fworkflows%2Frun-tests.yml?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -12,23 +12,48 @@ jobs:\n     strategy:\n       fail-fast: false\n       matrix:\n-        python-version: [\"3.7\", \"3.8\", \"3.9\", \"3.10\", \"3.11\", \"3.12-dev\", \"pypy-3.8\", \"pypy-3.9\"]\n+        python-version: [\"3.8\", \"3.9\", \"3.10\", \"3.11\", \"3.12\", \"pypy-3.9\", \"pypy-3.10\"]\n         os: [ubuntu-22.04, macOS-latest, windows-latest]\n+        # Python 3.8 and 3.9 do not run on macOS-latest which\n+        # is now using arm64 hardware.\n+        # https://github.com/actions/setup-python/issues/696#issuecomment-1637587760\n+        exclude:\n+        - { python-version: \"3.8\", os: \"macos-latest\" }\n+        - { python-version: \"3.9\", os: \"macos-latest\" }\n         include:\n-          # pypy-3.7 on Windows and Mac OS currently fails trying to compile\n-          # cryptography. Moving pypy-3.7 to only test linux.\n-          - python-version: pypy-3.7\n-            os: ubuntu-latest\n+        - { python-version: \"3.8\", os: \"macos-13\" }\n+        - { python-version: \"3.9\", os: \"macos-13\" }\n \n     steps:\n-    - uses: actions/checkout@v2\n+    - uses: actions/checkout@8ade135a41bc03ea155e62e844d188df1ea18608 # v4.1.0\n     - name: Set up Python ${{ matrix.python-version }}\n-      uses: actions/setup-python@v2\n+      uses: actions/setup-python@82c7e631bb3cdc910f68e0081d67478d79c6982d # v5.1.0\n       with:\n         python-version: ${{ matrix.python-version }}\n+        cache: 'pip'\n     - name: Install dependencies\n       run: |\n         make\n     - name: Run tests\n       run: |\n         make ci\n+\n+  no_chardet:\n+    name: \"No Character Detection\"\n+    runs-on: ubuntu-latest\n+    strategy:\n+      fail-fast: true\n+\n+    steps:\n+      - uses: actions/checkout@8ade135a41bc03ea155e62e844d188df1ea18608\n+      - name: 'Set up Python 3.8'\n+        uses: actions/setup-python@82c7e631bb3cdc910f68e0081d67478d79c6982d\n+        with:\n+          python-version: '3.8'\n+      - name: Install dependencies\n+        run: |\n+          make\n+          python -m pip uninstall -y \"charset_normalizer\" \"chardet\"\n+      - name: Run tests\n+        run: |\n+          make ci"
    },
    {
      "sha": "0a0515cf87a37464c11056127db6cc617b2f31ec",
      "filename": ".pre-commit-config.yaml",
      "status": "modified",
      "additions": 4,
      "deletions": 4,
      "changes": 8,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/.pre-commit-config.yaml",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/.pre-commit-config.yaml",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/.pre-commit-config.yaml?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -2,7 +2,7 @@ exclude: 'docs/|ext/'\n \n repos:\n - repo: https://github.com/pre-commit/pre-commit-hooks\n-  rev: v4.0.1\n+  rev: v4.4.0\n   hooks:\n   - id: check-yaml\n   - id: debug-statements\n@@ -13,16 +13,16 @@ repos:\n   hooks:\n     - id: isort\n - repo: https://github.com/psf/black\n-  rev: 22.3.0\n+  rev: 23.7.0\n   hooks:\n     - id: black\n       exclude: tests/test_lowlevel.py\n - repo: https://github.com/asottile/pyupgrade\n-  rev: v2.31.1\n+  rev: v3.10.1\n   hooks:\n     - id: pyupgrade\n       args: [--py37-plus]\n - repo: https://github.com/PyCQA/flake8\n-  rev: 6.0.0\n+  rev: 6.1.0\n   hooks:\n     - id: flake8"
    },
    {
      "sha": "0e2c719e08549d4bd8123abc65686e57780ccc5f",
      "filename": ".readthedocs.yaml",
      "status": "added",
      "additions": 29,
      "deletions": 0,
      "changes": 29,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/.readthedocs.yaml",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/.readthedocs.yaml",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/.readthedocs.yaml?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,29 @@\n+# Read the Docs configuration file for Sphinx projects\n+# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details\n+\n+# Required\n+version: 2\n+\n+# Set the OS, Python version and other tools you might need\n+build:\n+  os: ubuntu-22.04\n+  tools:\n+    python: \"3.12\"\n+\n+# Build documentation in the \"docs/\" directory with Sphinx\n+sphinx:\n+  configuration: docs/conf.py\n+  builder: \"dirhtml\"\n+\n+# Optionally build your docs in additional formats such as PDF and ePub\n+formats:\n+  - pdf\n+  - epub\n+\n+# Optional but recommended, declare the Python requirements required\n+# to build your documentation\n+# See https://docs.readthedocs.io/en/stable/guides/reproducible-builds.html\n+python:\n+  install:\n+    - path: .\n+    - requirements: docs/requirements.txt"
    },
    {
      "sha": "6e017c9a915b56273db2f63107a676336f4764b5",
      "filename": "AUTHORS.rst",
      "status": "modified",
      "additions": 2,
      "deletions": 1,
      "changes": 3,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/AUTHORS.rst",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/AUTHORS.rst",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/AUTHORS.rst?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -8,7 +8,7 @@ Keepers of the Crystals\n \n Previous Keepers of Crystals\n ````````````````````````````\n-- Kenneth Reitz <me@kennethreitz.org> `@ken-reitz <https://github.com/ken-reitz>`_, reluctant Keeper of the Master Crystal.\n+- Kenneth Reitz <me@kennethreitz.org> `@kennethreitz <https://github.com/kennethreitz>`_, reluctant Keeper of the Master Crystal.\n - Cory Benfield <cory@lukasa.co.uk> `@lukasa <https://github.com/lukasa>`_\n - Ian Cordasco <graffatcolmingov@gmail.com> `@sigmavirus24 <https://github.com/sigmavirus24>`_.\n \n@@ -192,3 +192,4 @@ Patches and Suggestions\n - Alessio Izzo (`@aless10 <https://github.com/aless10>`_)\n - Sylvain Marié (`@smarie <https://github.com/smarie>`_)\n - Hod Bin Noon (`@hodbn <https://github.com/hodbn>`_)\n+- Mike Fiedler (`@miketheman <https://github.com/miketheman>`_)"
    },
    {
      "sha": "7c2cd71c109605242a1524dfe946ed2f92c96119",
      "filename": "HISTORY.md",
      "status": "modified",
      "additions": 47,
      "deletions": 1,
      "changes": 48,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/HISTORY.md",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/HISTORY.md",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/HISTORY.md?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -6,6 +6,52 @@ dev\n \n - \\[Short description of non-trivial change.\\]\n \n+2.32.0 (2024-05-20)\n+-------------------\n+\n+**Security**\n+- Fixed an issue where setting `verify=False` on the first request from a\n+  Session will cause subsequent requests to the _same origin_ to also ignore\n+  cert verification, regardless of the value of `verify`.\n+  (https://github.com/psf/requests/security/advisories/GHSA-9wx4-h78v-vm56)\n+\n+**Improvements**\n+- `verify=True` now reuses a global SSLContext which should improve\n+  request time variance between first and subsequent requests. It should\n+  also minimize certificate load time on Windows systems when using a Python\n+  version built with OpenSSL 3.x. (#6667)\n+- Requests now supports optional use of character detection\n+  (`chardet` or `charset_normalizer`) when repackaged or vendored.\n+  This enables `pip` and other projects to minimize their vendoring\n+  surface area. The `Response.text()` and `apparent_encoding` APIs\n+  will default to `utf-8` if neither library is present. (#6702)\n+\n+**Bugfixes**\n+- Fixed bug in length detection where emoji length was incorrectly\n+  calculated in the request content-length. (#6589)\n+- Fixed deserialization bug in JSONDecodeError. (#6629)\n+- Fixed bug where an extra leading `/` (path separator) could lead\n+  urllib3 to unnecessarily reparse the request URI. (#6644)\n+\n+**Deprecations**\n+\n+- Requests has officially added support for CPython 3.12 (#6503)\n+- Requests has officially added support for PyPy 3.9 and 3.10 (#6641)\n+- Requests has officially dropped support for CPython 3.7 (#6642)\n+- Requests has officially dropped support for PyPy 3.7 and 3.8 (#6641)\n+\n+**Documentation**\n+- Various typo fixes and doc improvements.\n+\n+**Packaging**\n+- Requests has started adopting some modern packaging practices.\n+  The source files for the projects (formerly `requests`) is now located\n+  in `src/requests` in the Requests sdist. (#6506)\n+- Starting in Requests 2.33.0, Requests will migrate to a PEP 517 build system\n+  using `hatchling`. This should not impact the average user, but extremely old\n+  versions of packaging utilities may have issues with the new packaging format.\n+\n+\n 2.31.0 (2023-05-22)\n -------------------\n \n@@ -14,7 +60,7 @@ dev\n   forwarding of `Proxy-Authorization` headers to destination servers when\n   following HTTPS redirects.\n \n-  When proxies are defined with user info (https://user:pass@proxy:8080), Requests\n+  When proxies are defined with user info (`https://user:pass@proxy:8080`), Requests\n   will construct a `Proxy-Authorization` header that is attached to the request to\n   authenticate with the proxy.\n "
    },
    {
      "sha": "87a23ab937aa80eb85f586ae1aabbb0a47244197",
      "filename": "MANIFEST.in",
      "status": "modified",
      "additions": 1,
      "deletions": 1,
      "changes": 2,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/MANIFEST.in",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/MANIFEST.in",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/MANIFEST.in?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -1,2 +1,2 @@\n-include README.md LICENSE NOTICE HISTORY.md pytest.ini requirements-dev.txt\n+include README.md LICENSE NOTICE HISTORY.md requirements-dev.txt\n recursive-include tests *.py"
    },
    {
      "sha": "192b926853138bfde739920fa4d147fcd419a2ec",
      "filename": "Makefile",
      "status": "modified",
      "additions": 5,
      "deletions": 5,
      "changes": 10,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/Makefile",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/Makefile",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/Makefile?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -1,23 +1,23 @@\n .PHONY: docs\n init:\n-\tpip install -r requirements-dev.txt\n+\tpython -m pip install -r requirements-dev.txt\n test:\n \t# This runs all of the tests on all supported Python versions.\n \ttox -p\n ci:\n-\tpytest tests --junitxml=report.xml\n+\tpython -m pytest tests --junitxml=report.xml\n \n test-readme:\n \tpython setup.py check --restructuredtext --strict && ([ $$? -eq 0 ] && echo \"README.rst and HISTORY.rst ok\") || echo \"Invalid markup in README.rst or HISTORY.rst!\"\n \n flake8:\n-\tflake8 --ignore=E501,F401,E128,E402,E731,F821 requests\n+\tpython -m flake8 src/requests\n \n coverage:\n-\tpytest --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=requests tests\n+\tpython -m pytest --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=src/requests tests\n \n publish:\n-\tpip install 'twine>=1.5.0'\n+\tpython -m pip install 'twine>=1.5.0'\n \tpython setup.py sdist bdist_wheel\n \ttwine upload dist/*\n \trm -fr build dist .egg requests.egg-info"
    },
    {
      "sha": "79cf54d1e158db157703d67e7670400621c521f4",
      "filename": "README.md",
      "status": "modified",
      "additions": 2,
      "deletions": 2,
      "changes": 4,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/README.md",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/README.md",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/README.md?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -21,7 +21,7 @@ Requests allows you to send HTTP/1.1 requests extremely easily. There’s no nee\n \n Requests is one of the most downloaded Python packages today, pulling in around `30M downloads / week`— according to GitHub, Requests is currently [depended upon](https://github.com/psf/requests/network/dependents?package_id=UGFja2FnZS01NzA4OTExNg%3D%3D) by `1,000,000+` repositories. You may certainly put your trust in this code.\n \n-[![Downloads](https://pepy.tech/badge/requests/month)](https://pepy.tech/project/requests)\n+[![Downloads](https://static.pepy.tech/badge/requests/month)](https://pepy.tech/project/requests)\n [![Supported Versions](https://img.shields.io/pypi/pyversions/requests.svg)](https://pypi.org/project/requests)\n [![Contributors](https://img.shields.io/github/contributors/psf/requests.svg)](https://github.com/psf/requests/graphs/contributors)\n \n@@ -33,7 +33,7 @@ Requests is available on PyPI:\n $ python -m pip install requests\n ```\n \n-Requests officially supports Python 3.7+.\n+Requests officially supports Python 3.8+.\n \n ## Supported Features & Best–Practices\n "
    },
    {
      "sha": "607bf92c4e31951864788278661a02f8962e1aab",
      "filename": "docs/_templates/sidebarintro.html",
      "status": "modified",
      "additions": 6,
      "deletions": 6,
      "changes": 12,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/docs%2F_templates%2Fsidebarintro.html",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/docs%2F_templates%2Fsidebarintro.html",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/docs%2F_templates%2Fsidebarintro.html?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -16,15 +16,15 @@\n \n <h3>Useful Links</h3>\n <ul>\n-  <li><a href=\"https://requests.readthedocs.io/en/latest/user/quickstart/\">Quickstart</a></li>\n-  <li><a href=\"https://requests.readthedocs.io/en/latest/user/advanced/\">Advanced Usage</a></li>\n-  <li><a href=\"https://requests.readthedocs.io/en/latest/api/\">API Reference</a></li>\n-  <li><a href=\"https://requests.readthedocs.io/en/latest/community/updates/#release-history\">Release History</a></li>\n-  <li><a href=\"https://requests.readthedocs.io/en/latest/dev/contributing/\">Contributors Guide</a></li>\n+  <li><a href=\"{{ pathto('user/quickstart') }}\">Quickstart</a></li>\n+  <li><a href=\"{{ pathto('user/advanced') }}\">Advanced Usage</a></li>\n+  <li><a href=\"{{ pathto('api') }}\">API Reference</a></li>\n+  <li><a href=\"{{ pathto('community/updates') + '#release-history' }}\">Release History</a></li>\n+  <li><a href=\"{{ pathto('dev/contributing') }}\">Contributors Guide</a></li>\n \n   <p></p>\n \n-  <li><a href=\"https://requests.readthedocs.io/en/latest/community/recommended/\">Recommended Packages and Extensions</a></li>\n+  <li><a href=\"{{ pathto('community/recommended') }}\">Recommended Packages and Extensions</a></li>\n \n   <p></p>\n "
    },
    {
      "sha": "71eb82e726475ac4ebaac0b87067325da6200b80",
      "filename": "docs/_templates/sidebarlogo.html",
      "status": "modified",
      "additions": 6,
      "deletions": 6,
      "changes": 12,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/docs%2F_templates%2Fsidebarlogo.html",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/docs%2F_templates%2Fsidebarlogo.html",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/docs%2F_templates%2Fsidebarlogo.html?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -11,15 +11,15 @@\n \n <h3>Useful Links</h3>\n <ul>\n-  <li><a href=\"https://requests.readthedocs.io/en/latest/user/quickstart/\">Quickstart</a></li>\n-  <li><a href=\"https://requests.readthedocs.io/en/latest/user/advanced/\">Advanced Usage</a></li>\n-  <li><a href=\"https://requests.readthedocs.io/en/latest/api/\">API Reference</a></li>\n-  <li><a href=\"https://requests.readthedocs.io/en/latest/community/updates/#release-history\">Release History</a></li>\n-  <li><a href=\"https://requests.readthedocs.io/en/latest/dev/contributing/\">Contributors Guide</a></li>\n+  <li><a href=\"{{ pathto('user/quickstart') }}\">Quickstart</a></li>\n+  <li><a href=\"{{ pathto('user/advanced') }}\">Advanced Usage</a></li>\n+  <li><a href=\"{{ pathto('api') }}\">API Reference</a></li>\n+  <li><a href=\"{{ pathto('community/updates') + '#release-history' }}\">Release History</a></li>\n+  <li><a href=\"{{ pathto('dev/contributing') }}\">Contributors Guide</a></li>\n \n   <p></p>\n \n-  <li><a href=\"https://requests.readthedocs.io/en/latest/community/recommended/\">Recommended Packages and Extensions</a></li>\n+  <li><a href=\"{{ pathto('community/recommended') }}\">Recommended Packages and Extensions</a></li>\n \n   <p></p>\n "
    },
    {
      "sha": "b6ea654e60b83ce0f54ac0c25c7c09788b6be8fc",
      "filename": "docs/community/faq.rst",
      "status": "modified",
      "additions": 2,
      "deletions": 2,
      "changes": 4,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/docs%2Fcommunity%2Ffaq.rst",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/docs%2Fcommunity%2Ffaq.rst",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/docs%2Fcommunity%2Ffaq.rst?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -22,7 +22,7 @@ Custom User-Agents?\n -------------------\n \n Requests allows you to easily override User-Agent strings, along with\n-any other HTTP Header. See `documentation about headers <https://requests.readthedocs.io/en/latest/user/quickstart/#custom-headers>`_.\n+any other HTTP Header. See :ref:`documentation about headers <custom-headers>`.\n \n \n \n@@ -55,7 +55,7 @@ Chris Adams gave an excellent summary on\n Python 3 Support?\n -----------------\n \n-Yes! Requests officially supports Python 3.7+ and PyPy.\n+Yes! Requests officially supports Python 3.8+ and PyPy.\n \n Python 2 Support?\n -----------------"
    },
    {
      "sha": "c75c71f6a2dcb1c1c30fde955ce42e883e174508",
      "filename": "docs/community/out-there.rst",
      "status": "modified",
      "additions": 1,
      "deletions": 13,
      "changes": 14,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/docs%2Fcommunity%2Fout-there.rst",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/docs%2Fcommunity%2Fout-there.rst",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/docs%2Fcommunity%2Fout-there.rst?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -1,22 +1,10 @@\n Integrations\n ============\n \n-Python for iOS\n---------------\n-\n-Requests is built into the wonderful `Python for iOS <https://itunes.apple.com/us/app/python-2.7-for-ios/id485729872?mt=Python8>`_ runtime!\n-\n-To give it a try, simply::\n-\n-    import requests\n-\n-\n Articles & Talks\n ================\n-- `Python for the Web <https://www.gun.io/blog/python-for-the-web>`_ teaches how to use Python to interact with the web, using Requests.\n - `Daniel Greenfeld's Review of Requests <https://pydanny.blogspot.com/2011/05/python-http-requests-for-humans.html>`_\n-- `My 'Python for Humans' talk <http://python-for-humans.heroku.com>`_ ( `audio <https://codeconf.s3.amazonaws.com/2011/pycodeconf/talks/PyCodeConf2011%20-%20Kenneth%20Reitz.m4a>`_ )\n-- `Issac Kelly's 'Consuming Web APIs' talk <https://issackelly.github.com/Consuming-Web-APIs-with-Python-Talk/slides/slides.html>`_\n+- `Issac Kelly's 'Consuming Web APIs' talk <https://issackelly.github.io/Consuming-Web-APIs-with-Python-Talk/slides/slides.html>`_\n - `Blog post about Requests via Yum <https://arunsag.wordpress.com/2011/08/17/new-package-python-requests-http-for-humans/>`_\n - `Russian blog post introducing Requests <https://habr.com/post/126262/>`_\n - `Sending JSON in Requests <http://www.coglib.com/~icordasc/blog/2014/11/sending-json-in-requests.html>`_"
    },
    {
      "sha": "289250c2a4e0aa1b7450c8a0888b4efb00e66cbd",
      "filename": "docs/index.rst",
      "status": "modified",
      "additions": 2,
      "deletions": 2,
      "changes": 4,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/docs%2Findex.rst",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/docs%2Findex.rst",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/docs%2Findex.rst?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -9,7 +9,7 @@ Requests: HTTP for Humans™\n Release v\\ |version|. (:ref:`Installation <install>`)\n \n \n-.. image:: https://pepy.tech/badge/requests/month\n+.. image:: https://static.pepy.tech/badge/requests/month\n     :target: https://pepy.tech/project/requests\n     :alt: Requests Downloads Per Month Badge\n     \n@@ -72,7 +72,7 @@ Requests is ready for today's web.\n - Chunked Requests\n - ``.netrc`` Support\n \n-Requests officially supports Python 3.7+, and runs great on PyPy.\n+Requests officially supports Python 3.8+, and runs great on PyPy.\n \n \n The User Guide"
    },
    {
      "sha": "2af334d57b7103158612d79e5d786fc29e2f380e",
      "filename": "docs/requirements.txt",
      "status": "modified",
      "additions": 1,
      "deletions": 1,
      "changes": 2,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/docs%2Frequirements.txt",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/docs%2Frequirements.txt",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/docs%2Frequirements.txt?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -1,3 +1,3 @@\n # Pinning to avoid unexpected breakages.\n # Used by RTD to generate docs.\n-Sphinx==4.2.0\n+Sphinx==7.2.6"
    },
    {
      "sha": "ff3a3d0f268c4356f095ffd11570eba7af054a80",
      "filename": "docs/user/advanced.rst",
      "status": "modified",
      "additions": 46,
      "deletions": 4,
      "changes": 50,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/docs%2Fuser%2Fadvanced.rst",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/docs%2Fuser%2Fadvanced.rst",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/docs%2Fuser%2Fadvanced.rst?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -291,7 +291,7 @@ versions of Requests.\n For the sake of security we recommend upgrading certifi frequently!\n \n .. _HTTP persistent connection: https://en.wikipedia.org/wiki/HTTP_persistent_connection\n-.. _connection pooling: https://urllib3.readthedocs.io/en/latest/reference/index.html#module-urllib3.connectionpool\n+.. _connection pooling: https://urllib3.readthedocs.io/en/latest/reference/urllib3.connectionpool.html\n .. _certifi: https://certifiio.readthedocs.io/\n .. _Mozilla trust store: https://hg.mozilla.org/mozilla-central/raw-file/tip/security/nss/lib/ckfw/builtins/certdata.txt\n \n@@ -666,6 +666,8 @@ You override this default certificate bundle by setting the ``REQUESTS_CA_BUNDLE\n     >>> import requests\n     >>> requests.get('https://example.org')\n \n+.. _socks:\n+\n SOCKS\n ^^^^^\n \n@@ -946,7 +948,7 @@ Link Headers\n Many HTTP APIs feature Link headers. They make APIs more self describing and\n discoverable.\n \n-GitHub uses these for `pagination <https://developer.github.com/v3/#pagination>`_\n+GitHub uses these for `pagination <https://docs.github.com/en/rest/guides/using-pagination-in-the-rest-api>`_\n in their API, for example::\n \n     >>> url = 'https://api.github.com/users/kennethreitz/repos?page=1&per_page=10'\n@@ -994,6 +996,10 @@ The mount call registers a specific instance of a Transport Adapter to a\n prefix. Once mounted, any HTTP request made using that session whose URL starts\n with the given prefix will use the given Transport Adapter.\n \n+.. note:: The adapter will be chosen based on a longest prefix match. Be mindful\n+   prefixes such as ``http://localhost`` will also match ``http://localhost.other.com``\n+   or ``http://localhost@other.com``. It's recommended to terminate full hostnames with a ``/``.\n+\n Many of the details of implementing a Transport Adapter are beyond the scope of\n this documentation, but take a look at the next example for a simple SSL use-\n case. For more than that, you might look at subclassing the\n@@ -1026,8 +1032,30 @@ library to use SSLv3::\n                 num_pools=connections, maxsize=maxsize,\n                 block=block, ssl_version=ssl.PROTOCOL_SSLv3)\n \n+Example: Automatic Retries\n+^^^^^^^^^^^^^^^^^^^^^^^^^^\n+\n+By default, Requests does not retry failed connections. However, it is possible\n+to implement automatic retries with a powerful array of features, including\n+backoff, within a Requests :class:`Session <requests.Session>` using the\n+`urllib3.util.Retry`_ class::\n+\n+    from urllib3.util import Retry\n+    from requests import Session\n+    from requests.adapters import HTTPAdapter\n+\n+    s = Session()\n+    retries = Retry(\n+        total=3,\n+        backoff_factor=0.1,\n+        status_forcelist=[502, 503, 504],\n+        allowed_methods={'POST'},\n+    )\n+    s.mount('https://', HTTPAdapter(max_retries=retries))\n+\n .. _`described here`: https://kenreitz.org/essays/2012/06/14/the-future-of-python-http\n .. _`urllib3`: https://github.com/urllib3/urllib3\n+.. _`urllib3.util.Retry`: https://urllib3.readthedocs.io/en/stable/reference/urllib3.util.html#urllib3.util.Retry\n \n .. _blocking-or-nonblocking:\n \n@@ -1055,7 +1083,7 @@ Header Ordering\n \n In unusual circumstances you may want to provide headers in an ordered manner. If you pass an ``OrderedDict`` to the ``headers`` keyword argument, that will provide the headers with an ordering. *However*, the ordering of the default headers used by Requests will be preferred, which means that if you override default headers in the ``headers`` keyword argument, they may appear out of order compared to other headers in that keyword argument.\n \n-If this is problematic, users should consider setting the default headers on a :class:`Session <requests.Session>` object, by setting :attr:`Session <requests.Session.headers>` to a custom ``OrderedDict``. That ordering will always be preferred.\n+If this is problematic, users should consider setting the default headers on a :class:`Session <requests.Session>` object, by setting :attr:`Session.headers <requests.Session.headers>` to a custom ``OrderedDict``. That ordering will always be preferred.\n \n .. _timeouts:\n \n@@ -1071,7 +1099,7 @@ The **connect** timeout is the number of seconds Requests will wait for your\n client to establish a connection to a remote machine (corresponding to the\n `connect()`_) call on the socket. It's a good practice to set connect timeouts\n to slightly larger than a multiple of 3, which is the default `TCP packet\n-retransmission window <https://www.hjp.at/doc/rfc/rfc2988.txt>`_.\n+retransmission window <https://datatracker.ietf.org/doc/html/rfc2988>`_.\n \n Once your client has connected to the server and sent the HTTP request, the\n **read** timeout is the number of seconds the client will wait for the server\n@@ -1096,4 +1124,18 @@ coffee.\n \n     r = requests.get('https://github.com', timeout=None)\n \n+.. note:: The connect timeout applies to each connection attempt to an IP address.\n+          If multiple addresses exist for a domain name, the underlying ``urllib3`` will\n+          try each address sequentially until one successfully connects.\n+          This may lead to an effective total connection timeout *multiple* times longer\n+          than the specified time, e.g. an unresponsive server having both IPv4 and IPv6\n+          addresses will have its perceived timeout *doubled*, so take that into account\n+          when setting the connection timeout.\n+.. note:: Neither the connect nor read timeouts are `wall clock`_. This means\n+          that if you start a request, and look at the time, and then look at\n+          the time when the request finishes or times out, the real-world time\n+          may be greater than what you specified.\n+\n+\n+.. _`wall clock`: https://wiki.php.net/rfc/max_execution_wall_time\n .. _`connect()`: https://linux.die.net/man/2/connect"
    },
    {
      "sha": "33c2732c7f2b6c61b0bdf1ce1e75508ccecfae9a",
      "filename": "docs/user/quickstart.rst",
      "status": "modified",
      "additions": 2,
      "deletions": 3,
      "changes": 5,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/docs%2Fuser%2Fquickstart.rst",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/docs%2Fuser%2Fquickstart.rst",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/docs%2Fuser%2Fquickstart.rst?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -201,6 +201,8 @@ may better fit your use cases.\n    were returned, use ``Response.raw``.\n \n \n+.. _custom-headers:\n+\n Custom Headers\n --------------\n \n@@ -566,6 +568,3 @@ All exceptions that Requests explicitly raises inherit from\n -----------------------\n \n Ready for more? Check out the :ref:`advanced <advanced>` section.\n-\n-\n-If you're on the job market, consider taking `this programming quiz <https://triplebyte.com/a/b1i2FB8/requests-docs-1>`_. A substantial donation will be made to this project, if you find a job through this platform."
    },
    {
      "sha": "1b7901e1559544ac387713b7c45e9ebe165cce83",
      "filename": "pyproject.toml",
      "status": "modified",
      "additions": 2,
      "deletions": 5,
      "changes": 7,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/pyproject.toml",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/pyproject.toml",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/pyproject.toml?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -1,13 +1,10 @@\n [tool.isort]\n profile = \"black\"\n-src_paths = [\"requests\", \"test\"]\n+src_paths = [\"src/requests\", \"test\"]\n honor_noqa = true\n \n [tool.pytest.ini_options]\n addopts = \"--doctest-modules\"\n doctest_optionflags = \"NORMALIZE_WHITESPACE ELLIPSIS\"\n minversion = \"6.2\"\n-testpaths = [\n-    \"requests\",\n-    \"tests\",\n-]\n+testpaths = [\"tests\"]"
    },
    {
      "sha": "e80b18581e22ba92f743ba336eb423c3b412ce87",
      "filename": "requirements-dev.txt",
      "status": "modified",
      "additions": 2,
      "deletions": 8,
      "changes": 10,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/requirements-dev.txt",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/requirements-dev.txt",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/requirements-dev.txt?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -1,13 +1,7 @@\n -e .[socks]\n-pytest>=2.8.0,<=6.2.5\n+pytest>=2.8.0,<9\n pytest-cov\n pytest-httpbin==2.0.0\n-pytest-mock==2.0.0\n-httpbin==0.7.0\n+httpbin~=0.10.0\n trustme\n wheel\n-cryptography<40.0.0; python_version <= '3.7' and platform_python_implementation == 'PyPy'\n-\n-# Flask Stack\n-Flask>1.0,<2.0\n-markupsafe<2.1"
    },
    {
      "sha": "8d44e0e14b1901923d71a3c1cb02d4e1e55f77a6",
      "filename": "setup.cfg",
      "status": "modified",
      "additions": 3,
      "deletions": 3,
      "changes": 6,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/setup.cfg",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/setup.cfg",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/setup.cfg?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -7,11 +7,11 @@ requires-dist =\n     certifi>=2017.4.17\n     charset_normalizer>=2,<4\n     idna>=2.5,<4\n-    urllib3>=1.21.1,<1.27\n+    urllib3>=1.21.1,<3\n \n [flake8]\n ignore = E203, E501, W503\n per-file-ignores =\n-    requests/__init__.py:E402, F401\n-    requests/compat.py:E402, F401\n+    src/requests/__init__.py:E402, F401\n+    src/requests/compat.py:E402, F401\n     tests/compat.py:F401"
    },
    {
      "sha": "1b0eb377b4c84736b2c77ef0a5bd343815eec409",
      "filename": "setup.py",
      "status": "modified",
      "additions": 6,
      "deletions": 6,
      "changes": 12,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/setup.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/setup.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/setup.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -7,7 +7,7 @@\n from setuptools.command.test import test as TestCommand\n \n CURRENT_PYTHON = sys.version_info[:2]\n-REQUIRED_PYTHON = (3, 7)\n+REQUIRED_PYTHON = (3, 8)\n \n if CURRENT_PYTHON < REQUIRED_PYTHON:\n     sys.stderr.write(\n@@ -20,7 +20,7 @@\n consider upgrading to a supported Python version.\n \n If you can't upgrade your Python version, you'll need to\n-pin to an older version of Requests (<2.28).\n+pin to an older version of Requests (<2.32.0).\n \"\"\".format(\n             *(REQUIRED_PYTHON + CURRENT_PYTHON)\n         )\n@@ -75,7 +75,7 @@ def run_tests(self):\n \n about = {}\n here = os.path.abspath(os.path.dirname(__file__))\n-with open(os.path.join(here, \"requests\", \"__version__.py\"), \"r\", \"utf-8\") as f:\n+with open(os.path.join(here, \"src\", \"requests\", \"__version__.py\"), \"r\", \"utf-8\") as f:\n     exec(f.read(), about)\n \n with open(\"README.md\", \"r\", \"utf-8\") as f:\n@@ -92,9 +92,9 @@ def run_tests(self):\n     url=about[\"__url__\"],\n     packages=[\"requests\"],\n     package_data={\"\": [\"LICENSE\", \"NOTICE\"]},\n-    package_dir={\"requests\": \"requests\"},\n+    package_dir={\"\": \"src\"},\n     include_package_data=True,\n-    python_requires=\">=3.7\",\n+    python_requires=\">=3.8\",\n     install_requires=requires,\n     license=about[\"__license__\"],\n     zip_safe=False,\n@@ -107,11 +107,11 @@ def run_tests(self):\n         \"Operating System :: OS Independent\",\n         \"Programming Language :: Python\",\n         \"Programming Language :: Python :: 3\",\n-        \"Programming Language :: Python :: 3.7\",\n         \"Programming Language :: Python :: 3.8\",\n         \"Programming Language :: Python :: 3.9\",\n         \"Programming Language :: Python :: 3.10\",\n         \"Programming Language :: Python :: 3.11\",\n+        \"Programming Language :: Python :: 3.12\",\n         \"Programming Language :: Python :: 3 :: Only\",\n         \"Programming Language :: Python :: Implementation :: CPython\",\n         \"Programming Language :: Python :: Implementation :: PyPy\","
    },
    {
      "sha": "051cda1340effaa0706b46dd68ac002ceda3d45c",
      "filename": "src/requests/__init__.py",
      "status": "renamed",
      "additions": 5,
      "deletions": 1,
      "changes": 6,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2F__init__.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2F__init__.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/src%2Frequests%2F__init__.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -83,7 +83,11 @@ def check_compatibility(urllib3_version, chardet_version, charset_normalizer_ver\n         # charset_normalizer >= 2.0.0 < 4.0.0\n         assert (2, 0, 0) <= (major, minor, patch) < (4, 0, 0)\n     else:\n-        raise Exception(\"You need either charset_normalizer or chardet installed\")\n+        warnings.warn(\n+            \"Unable to find acceptable character detection dependency \"\n+            \"(chardet or charset_normalizer).\",\n+            RequestsDependencyWarning,\n+        )\n \n \n def _check_cryptography(cryptography_version):",
      "previous_filename": "requests/__init__.py"
    },
    {
      "sha": "1ac168734eec45a065ee65b41d4c906729d16cd4",
      "filename": "src/requests/__version__.py",
      "status": "renamed",
      "additions": 3,
      "deletions": 3,
      "changes": 6,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2F__version__.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2F__version__.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/src%2Frequests%2F__version__.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -5,10 +5,10 @@\n __title__ = \"requests\"\n __description__ = \"Python HTTP for Humans.\"\n __url__ = \"https://requests.readthedocs.io\"\n-__version__ = \"2.31.0\"\n-__build__ = 0x023100\n+__version__ = \"2.32.0\"\n+__build__ = 0x023200\n __author__ = \"Kenneth Reitz\"\n __author_email__ = \"me@kennethreitz.org\"\n-__license__ = \"Apache 2.0\"\n+__license__ = \"Apache-2.0\"\n __copyright__ = \"Copyright Kenneth Reitz\"\n __cake__ = \"\\u2728 \\U0001f370 \\u2728\"",
      "previous_filename": "requests/__version__.py"
    },
    {
      "sha": "f2cf635e2937ee9b123a1498c5c5f723a6e20084",
      "filename": "src/requests/_internal_utils.py",
      "status": "renamed",
      "additions": 0,
      "deletions": 0,
      "changes": 0,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2F_internal_utils.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2F_internal_utils.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/src%2Frequests%2F_internal_utils.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "previous_filename": "requests/_internal_utils.py"
    },
    {
      "sha": "f544f9d5457160255c2d99a857f5e9b09eace493",
      "filename": "src/requests/adapters.py",
      "status": "renamed",
      "additions": 96,
      "deletions": 18,
      "changes": 114,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fadapters.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fadapters.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/src%2Frequests%2Fadapters.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -8,6 +8,7 @@\n \n import os.path\n import socket  # noqa: F401\n+import typing\n \n from urllib3.exceptions import ClosedPoolError, ConnectTimeoutError\n from urllib3.exceptions import HTTPError as _HTTPError\n@@ -25,6 +26,7 @@\n from urllib3.util import Timeout as TimeoutSauce\n from urllib3.util import parse_url\n from urllib3.util.retry import Retry\n+from urllib3.util.ssl_ import create_urllib3_context\n \n from .auth import _basic_auth_str\n from .compat import basestring, urlparse\n@@ -61,11 +63,57 @@ def SOCKSProxyManager(*args, **kwargs):\n         raise InvalidSchema(\"Missing dependencies for SOCKS support.\")\n \n \n+if typing.TYPE_CHECKING:\n+    from .models import PreparedRequest\n+\n+\n DEFAULT_POOLBLOCK = False\n DEFAULT_POOLSIZE = 10\n DEFAULT_RETRIES = 0\n DEFAULT_POOL_TIMEOUT = None\n \n+_preloaded_ssl_context = create_urllib3_context()\n+_preloaded_ssl_context.load_verify_locations(\n+    extract_zipped_paths(DEFAULT_CA_BUNDLE_PATH)\n+)\n+\n+\n+def _urllib3_request_context(\n+    request: \"PreparedRequest\",\n+    verify: \"bool | str | None\",\n+    client_cert: \"typing.Tuple[str, str] | str | None\",\n+) -> \"(typing.Dict[str, typing.Any], typing.Dict[str, typing.Any])\":\n+    host_params = {}\n+    pool_kwargs = {}\n+    parsed_request_url = urlparse(request.url)\n+    scheme = parsed_request_url.scheme.lower()\n+    port = parsed_request_url.port\n+    cert_reqs = \"CERT_REQUIRED\"\n+    if verify is False:\n+        cert_reqs = \"CERT_NONE\"\n+    elif verify is True:\n+        pool_kwargs[\"ssl_context\"] = _preloaded_ssl_context\n+    elif isinstance(verify, str):\n+        if not os.path.isdir(verify):\n+            pool_kwargs[\"ca_certs\"] = verify\n+        else:\n+            pool_kwargs[\"ca_cert_dir\"] = verify\n+    pool_kwargs[\"cert_reqs\"] = cert_reqs\n+    if client_cert is not None:\n+        if isinstance(client_cert, tuple) and len(client_cert) == 2:\n+            pool_kwargs[\"cert_file\"] = client_cert[0]\n+            pool_kwargs[\"key_file\"] = client_cert[1]\n+        else:\n+            # According to our docs, we allow users to specify just the client\n+            # cert path\n+            pool_kwargs[\"cert_file\"] = client_cert\n+    host_params = {\n+        \"scheme\": scheme,\n+        \"host\": parsed_request_url.hostname,\n+        \"port\": port,\n+    }\n+    return host_params, pool_kwargs\n+\n \n class BaseAdapter:\n     \"\"\"The Base Transport Adapter\"\"\"\n@@ -247,28 +295,26 @@ def cert_verify(self, conn, url, verify, cert):\n         :param cert: The SSL certificate to verify.\n         \"\"\"\n         if url.lower().startswith(\"https\") and verify:\n+            conn.cert_reqs = \"CERT_REQUIRED\"\n \n-            cert_loc = None\n-\n-            # Allow self-specified cert location.\n+            # Only load the CA certificates if 'verify' is a string indicating the CA bundle to use.\n+            # Otherwise, if verify is a boolean, we don't load anything since\n+            # the connection will be using a context with the default certificates already loaded,\n+            # and this avoids a call to the slow load_verify_locations()\n             if verify is not True:\n+                # `verify` must be a str with a path then\n                 cert_loc = verify\n \n-            if not cert_loc:\n-                cert_loc = extract_zipped_paths(DEFAULT_CA_BUNDLE_PATH)\n+                if not os.path.exists(cert_loc):\n+                    raise OSError(\n+                        f\"Could not find a suitable TLS CA certificate bundle, \"\n+                        f\"invalid path: {cert_loc}\"\n+                    )\n \n-            if not cert_loc or not os.path.exists(cert_loc):\n-                raise OSError(\n-                    f\"Could not find a suitable TLS CA certificate bundle, \"\n-                    f\"invalid path: {cert_loc}\"\n-                )\n-\n-            conn.cert_reqs = \"CERT_REQUIRED\"\n-\n-            if not os.path.isdir(cert_loc):\n-                conn.ca_certs = cert_loc\n-            else:\n-                conn.ca_cert_dir = cert_loc\n+                if not os.path.isdir(cert_loc):\n+                    conn.ca_certs = cert_loc\n+                else:\n+                    conn.ca_cert_dir = cert_loc\n         else:\n             conn.cert_reqs = \"CERT_NONE\"\n             conn.ca_certs = None\n@@ -328,6 +374,35 @@ def build_response(self, req, resp):\n \n         return response\n \n+    def _get_connection(self, request, verify, proxies=None, cert=None):\n+        # Replace the existing get_connection without breaking things and\n+        # ensure that TLS settings are considered when we interact with\n+        # urllib3 HTTP Pools\n+        proxy = select_proxy(request.url, proxies)\n+        try:\n+            host_params, pool_kwargs = _urllib3_request_context(request, verify, cert)\n+        except ValueError as e:\n+            raise InvalidURL(e, request=request)\n+        if proxy:\n+            proxy = prepend_scheme_if_needed(proxy, \"http\")\n+            proxy_url = parse_url(proxy)\n+            if not proxy_url.host:\n+                raise InvalidProxyURL(\n+                    \"Please check proxy URL. It is malformed \"\n+                    \"and could be missing the host.\"\n+                )\n+            proxy_manager = self.proxy_manager_for(proxy)\n+            conn = proxy_manager.connection_from_host(\n+                **host_params, pool_kwargs=pool_kwargs\n+            )\n+        else:\n+            # Only scheme should be lower case\n+            conn = self.poolmanager.connection_from_host(\n+                **host_params, pool_kwargs=pool_kwargs\n+            )\n+\n+        return conn\n+\n     def get_connection(self, url, proxies=None):\n         \"\"\"Returns a urllib3 connection for the given URL. This should not be\n         called from user code, and is only exposed for use when subclassing the\n@@ -391,6 +466,9 @@ def request_url(self, request, proxies):\n             using_socks_proxy = proxy_scheme.startswith(\"socks\")\n \n         url = request.path_url\n+        if url.startswith(\"//\"):  # Don't confuse urllib3\n+            url = f\"/{url.lstrip('/')}\"\n+\n         if is_proxied_http_request and not using_socks_proxy:\n             url = urldefragauth(request.url)\n \n@@ -451,7 +529,7 @@ def send(\n         \"\"\"\n \n         try:\n-            conn = self.get_connection(request.url, proxies)\n+            conn = self._get_connection(request, verify, proxies=proxies, cert=cert)\n         except LocationValueError as e:\n             raise InvalidURL(e, request=request)\n ",
      "previous_filename": "requests/adapters.py"
    },
    {
      "sha": "5960744552e7f8eea815429e7bdad38b0cc2741d",
      "filename": "src/requests/api.py",
      "status": "renamed",
      "additions": 1,
      "deletions": 1,
      "changes": 2,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fapi.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fapi.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/src%2Frequests%2Fapi.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -25,7 +25,7 @@ def request(method, url, **kwargs):\n     :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.\n     :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.\n         ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``\n-        or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content-type'`` is a string\n+        or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content_type'`` is a string\n         defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers\n         to add for the file.\n     :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.",
      "previous_filename": "requests/api.py"
    },
    {
      "sha": "4a7ce6dc1460e0de8aa0c38ea9123faa69bd5110",
      "filename": "src/requests/auth.py",
      "status": "renamed",
      "additions": 0,
      "deletions": 1,
      "changes": 1,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fauth.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fauth.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/src%2Frequests%2Fauth.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -258,7 +258,6 @@ def handle_401(self, r, **kwargs):\n         s_auth = r.headers.get(\"www-authenticate\", \"\")\n \n         if \"digest\" in s_auth.lower() and self._thread_local.num_401_calls < 2:\n-\n             self._thread_local.num_401_calls += 1\n             pat = re.compile(r\"digest \", flags=re.IGNORECASE)\n             self._thread_local.chal = parse_dict_header(pat.sub(\"\", s_auth, count=1))",
      "previous_filename": "requests/auth.py"
    },
    {
      "sha": "be422c3e91e43bacf60ff3302688df0b28742333",
      "filename": "src/requests/certs.py",
      "status": "renamed",
      "additions": 0,
      "deletions": 0,
      "changes": 0,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fcerts.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fcerts.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/src%2Frequests%2Fcerts.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "previous_filename": "requests/certs.py"
    },
    {
      "sha": "095de1b6cae2f460174af54efa975411645f40c6",
      "filename": "src/requests/compat.py",
      "status": "renamed",
      "additions": 20,
      "deletions": 5,
      "changes": 25,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fcompat.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fcompat.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/src%2Frequests%2Fcompat.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -7,13 +7,28 @@\n compatibility until the next major version.\n \"\"\"\n \n-try:\n-    import chardet\n-except ImportError:\n-    import charset_normalizer as chardet\n-\n+import importlib\n import sys\n \n+# -------------------\n+# Character Detection\n+# -------------------\n+\n+\n+def _resolve_char_detection():\n+    \"\"\"Find supported character detection libraries.\"\"\"\n+    chardet = None\n+    for lib in (\"chardet\", \"charset_normalizer\"):\n+        if chardet is None:\n+            try:\n+                chardet = importlib.import_module(lib)\n+            except ImportError:\n+                pass\n+    return chardet\n+\n+\n+chardet = _resolve_char_detection()\n+\n # -------\n # Pythons\n # -------",
      "previous_filename": "requests/compat.py"
    },
    {
      "sha": "f69d0cda9e1c893401015a09f2db2de5a5960fd2",
      "filename": "src/requests/cookies.py",
      "status": "renamed",
      "additions": 8,
      "deletions": 8,
      "changes": 16,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fcookies.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fcookies.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/src%2Frequests%2Fcookies.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -2,7 +2,7 @@\n requests.cookies\n ~~~~~~~~~~~~~~~~\n \n-Compatibility code to be able to use `cookielib.CookieJar` with requests.\n+Compatibility code to be able to use `http.cookiejar.CookieJar` with requests.\n \n requests.utils imports from here, so be careful with imports.\n \"\"\"\n@@ -23,7 +23,7 @@\n class MockRequest:\n     \"\"\"Wraps a `requests.Request` to mimic a `urllib2.Request`.\n \n-    The code in `cookielib.CookieJar` expects this interface in order to correctly\n+    The code in `http.cookiejar.CookieJar` expects this interface in order to correctly\n     manage cookie policies, i.e., determine whether a cookie can be set, given the\n     domains of the request and the cookie.\n \n@@ -76,7 +76,7 @@ def get_header(self, name, default=None):\n         return self._r.headers.get(name, self._new_headers.get(name, default))\n \n     def add_header(self, key, val):\n-        \"\"\"cookielib has no legitimate use for this method; add it back if you find one.\"\"\"\n+        \"\"\"cookiejar has no legitimate use for this method; add it back if you find one.\"\"\"\n         raise NotImplementedError(\n             \"Cookie headers should be added with add_unredirected_header()\"\n         )\n@@ -104,11 +104,11 @@ class MockResponse:\n     \"\"\"Wraps a `httplib.HTTPMessage` to mimic a `urllib.addinfourl`.\n \n     ...what? Basically, expose the parsed HTTP headers from the server response\n-    the way `cookielib` expects to see them.\n+    the way `http.cookiejar` expects to see them.\n     \"\"\"\n \n     def __init__(self, headers):\n-        \"\"\"Make a MockResponse for `cookielib` to read.\n+        \"\"\"Make a MockResponse for `cookiejar` to read.\n \n         :param headers: a httplib.HTTPMessage or analogous carrying the headers\n         \"\"\"\n@@ -124,7 +124,7 @@ def getheaders(self, name):\n def extract_cookies_to_jar(jar, request, response):\n     \"\"\"Extract the cookies from the response into a CookieJar.\n \n-    :param jar: cookielib.CookieJar (not necessarily a RequestsCookieJar)\n+    :param jar: http.cookiejar.CookieJar (not necessarily a RequestsCookieJar)\n     :param request: our own requests.Request object\n     :param response: urllib3.HTTPResponse object\n     \"\"\"\n@@ -174,7 +174,7 @@ class CookieConflictError(RuntimeError):\n \n \n class RequestsCookieJar(cookielib.CookieJar, MutableMapping):\n-    \"\"\"Compatibility class; is a cookielib.CookieJar, but exposes a dict\n+    \"\"\"Compatibility class; is a http.cookiejar.CookieJar, but exposes a dict\n     interface.\n \n     This is the CookieJar we create by default for requests and sessions that\n@@ -341,7 +341,7 @@ def __setitem__(self, name, value):\n         self.set(name, value)\n \n     def __delitem__(self, name):\n-        \"\"\"Deletes a cookie given a name. Wraps ``cookielib.CookieJar``'s\n+        \"\"\"Deletes a cookie given a name. Wraps ``http.cookiejar.CookieJar``'s\n         ``remove_cookie_by_name()``.\n         \"\"\"\n         remove_cookie_by_name(self, name)",
      "previous_filename": "requests/cookies.py"
    },
    {
      "sha": "83986b489849131efeb7f286b328961205256fd8",
      "filename": "src/requests/exceptions.py",
      "status": "renamed",
      "additions": 10,
      "deletions": 0,
      "changes": 10,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fexceptions.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fexceptions.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/src%2Frequests%2Fexceptions.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -41,6 +41,16 @@ def __init__(self, *args, **kwargs):\n         CompatJSONDecodeError.__init__(self, *args)\n         InvalidJSONError.__init__(self, *self.args, **kwargs)\n \n+    def __reduce__(self):\n+        \"\"\"\n+        The __reduce__ method called when pickling the object must\n+        be the one from the JSONDecodeError (be it json/simplejson)\n+        as it expects all the arguments for instantiation, not just\n+        one like the IOError, and the MRO would by default call the\n+        __reduce__ method from the IOError due to the inheritance order.\n+        \"\"\"\n+        return CompatJSONDecodeError.__reduce__(self)\n+\n \n class HTTPError(RequestException):\n     \"\"\"An HTTP error occurred.\"\"\"",
      "previous_filename": "requests/exceptions.py"
    },
    {
      "sha": "8fbcd6560a8fe2c8a07e3bd1441a81e0db9cb689",
      "filename": "src/requests/help.py",
      "status": "renamed",
      "additions": 0,
      "deletions": 0,
      "changes": 0,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fhelp.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fhelp.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/src%2Frequests%2Fhelp.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "previous_filename": "requests/help.py"
    },
    {
      "sha": "d181ba2ec2e55d274897315887b78fbdca757da8",
      "filename": "src/requests/hooks.py",
      "status": "renamed",
      "additions": 0,
      "deletions": 0,
      "changes": 0,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fhooks.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fhooks.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/src%2Frequests%2Fhooks.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "previous_filename": "requests/hooks.py"
    },
    {
      "sha": "8f56ca7d23a9a12084df80cb649e019572308cfe",
      "filename": "src/requests/models.py",
      "status": "renamed",
      "additions": 8,
      "deletions": 5,
      "changes": 13,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fmodels.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fmodels.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/src%2Frequests%2Fmodels.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -170,7 +170,7 @@ def _encode_files(files, data):\n                         )\n                     )\n \n-        for (k, v) in files:\n+        for k, v in files:\n             # support for explicit filename\n             ft = None\n             fh = None\n@@ -268,7 +268,6 @@ def __init__(\n         hooks=None,\n         json=None,\n     ):\n-\n         # Default empty dicts for dict params.\n         data = [] if data is None else data\n         files = [] if files is None else files\n@@ -277,7 +276,7 @@ def __init__(\n         hooks = {} if hooks is None else hooks\n \n         self.hooks = default_hooks()\n-        for (k, v) in list(hooks.items()):\n+        for k, v in list(hooks.items()):\n             self.register_hook(event=k, hook=v)\n \n         self.method = method\n@@ -790,7 +789,12 @@ def next(self):\n     @property\n     def apparent_encoding(self):\n         \"\"\"The apparent encoding, provided by the charset_normalizer or chardet libraries.\"\"\"\n-        return chardet.detect(self.content)[\"encoding\"]\n+        if chardet is not None:\n+            return chardet.detect(self.content)[\"encoding\"]\n+        else:\n+            # If no character detection library is available, we'll fall back\n+            # to a standard Python utf-8 str.\n+            return \"utf-8\"\n \n     def iter_content(self, chunk_size=1, decode_unicode=False):\n         \"\"\"Iterates over the response data.  When stream=True is set on the\n@@ -865,7 +869,6 @@ def iter_lines(\n         for chunk in self.iter_content(\n             chunk_size=chunk_size, decode_unicode=decode_unicode\n         ):\n-\n             if pending is not None:\n                 chunk = pending + chunk\n ",
      "previous_filename": "requests/models.py"
    },
    {
      "sha": "5ab3d8e250de8475cb22553f564e5444e02c7460",
      "filename": "src/requests/packages.py",
      "status": "renamed",
      "additions": 9,
      "deletions": 14,
      "changes": 23,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fpackages.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fpackages.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/src%2Frequests%2Fpackages.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -1,13 +1,6 @@\n import sys\n \n-try:\n-    import chardet\n-except ImportError:\n-    import warnings\n-\n-    import charset_normalizer as chardet\n-\n-    warnings.filterwarnings(\"ignore\", \"Trying to detect\", module=\"charset_normalizer\")\n+from .compat import chardet\n \n # This code exists for backwards compatibility reasons.\n # I don't like it either. Just look the other way. :)\n@@ -20,9 +13,11 @@\n         if mod == package or mod.startswith(f\"{package}.\"):\n             sys.modules[f\"requests.packages.{mod}\"] = sys.modules[mod]\n \n-target = chardet.__name__\n-for mod in list(sys.modules):\n-    if mod == target or mod.startswith(f\"{target}.\"):\n-        target = target.replace(target, \"chardet\")\n-        sys.modules[f\"requests.packages.{target}\"] = sys.modules[mod]\n-# Kinda cool, though, right?\n+if chardet is not None:\n+    target = chardet.__name__\n+    for mod in list(sys.modules):\n+        if mod == target or mod.startswith(f\"{target}.\"):\n+            imported_mod = sys.modules[mod]\n+            sys.modules[f\"requests.packages.{mod}\"] = imported_mod\n+            mod = mod.replace(target, \"chardet\")\n+            sys.modules[f\"requests.packages.{mod}\"] = imported_mod",
      "previous_filename": "requests/packages.py"
    },
    {
      "sha": "b387bc36df7bc064b502adcb3c1a4527dd401fda",
      "filename": "src/requests/sessions.py",
      "status": "renamed",
      "additions": 5,
      "deletions": 7,
      "changes": 12,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fsessions.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fsessions.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/src%2Frequests%2Fsessions.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -262,7 +262,6 @@ def resolve_redirects(\n             if yield_requests:\n                 yield req\n             else:\n-\n                 resp = self.send(\n                     req,\n                     stream=stream,\n@@ -326,7 +325,7 @@ def rebuild_proxies(self, prepared_request, proxies):\n \n         # urllib3 handles proxy authorization for us in the standard adapter.\n         # Avoid appending this to TLS tunneled requests where it may be leaked.\n-        if not scheme.startswith('https') and username and password:\n+        if not scheme.startswith(\"https\") and username and password:\n             headers[\"Proxy-Authorization\"] = _basic_auth_str(username, password)\n \n         return new_proxies\n@@ -389,7 +388,6 @@ class Session(SessionRedirectMixin):\n     ]\n \n     def __init__(self):\n-\n         #: A case-insensitive dictionary of headers to be sent on each\n         #: :class:`Request <Request>` sent from this\n         #: :class:`Session <Session>`.\n@@ -545,6 +543,8 @@ def request(\n         :type allow_redirects: bool\n         :param proxies: (optional) Dictionary mapping protocol or protocol and\n             hostname to the URL of the proxy.\n+        :param hooks: (optional) Dictionary mapping hook name to one event or\n+            list of events, event must be callable.\n         :param stream: (optional) whether to immediately download the response\n             content. Defaults to ``False``.\n         :param verify: (optional) Either a boolean, in which case it controls whether we verify\n@@ -711,7 +711,6 @@ def send(self, request, **kwargs):\n \n         # Persist cookies\n         if r.history:\n-\n             # If the hooks create history then we want those cookies too\n             for resp in r.history:\n                 extract_cookies_to_jar(self.cookies, resp.request, resp.raw)\n@@ -759,7 +758,7 @@ def merge_environment_settings(self, url, proxies, stream, verify, cert):\n             # Set environment's proxies.\n             no_proxy = proxies.get(\"no_proxy\") if proxies is not None else None\n             env_proxies = get_environ_proxies(url, no_proxy=no_proxy)\n-            for (k, v) in env_proxies.items():\n+            for k, v in env_proxies.items():\n                 proxies.setdefault(k, v)\n \n             # Look for requests environment configuration\n@@ -785,8 +784,7 @@ def get_adapter(self, url):\n \n         :rtype: requests.adapters.BaseAdapter\n         \"\"\"\n-        for (prefix, adapter) in self.adapters.items():\n-\n+        for prefix, adapter in self.adapters.items():\n             if url.lower().startswith(prefix.lower()):\n                 return adapter\n ",
      "previous_filename": "requests/sessions.py"
    },
    {
      "sha": "c7945a2f06897ed980cc575df2f48d9e6c1a9f7e",
      "filename": "src/requests/status_codes.py",
      "status": "renamed",
      "additions": 5,
      "deletions": 5,
      "changes": 10,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fstatus_codes.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fstatus_codes.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/src%2Frequests%2Fstatus_codes.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -24,7 +24,7 @@\n     # Informational.\n     100: (\"continue\",),\n     101: (\"switching_protocols\",),\n-    102: (\"processing\",),\n+    102: (\"processing\", \"early-hints\"),\n     103: (\"checkpoint\",),\n     122: (\"uri_too_long\", \"request_uri_too_long\"),\n     200: (\"ok\", \"okay\", \"all_ok\", \"all_okay\", \"all_good\", \"\\\\o/\", \"✓\"),\n@@ -65,8 +65,8 @@\n     410: (\"gone\",),\n     411: (\"length_required\",),\n     412: (\"precondition_failed\", \"precondition\"),\n-    413: (\"request_entity_too_large\",),\n-    414: (\"request_uri_too_large\",),\n+    413: (\"request_entity_too_large\", \"content_too_large\"),\n+    414: (\"request_uri_too_large\", \"uri_too_long\"),\n     415: (\"unsupported_media_type\", \"unsupported_media\", \"media_type\"),\n     416: (\n         \"requested_range_not_satisfiable\",\n@@ -76,10 +76,10 @@\n     417: (\"expectation_failed\",),\n     418: (\"im_a_teapot\", \"teapot\", \"i_am_a_teapot\"),\n     421: (\"misdirected_request\",),\n-    422: (\"unprocessable_entity\", \"unprocessable\"),\n+    422: (\"unprocessable_entity\", \"unprocessable\", \"unprocessable_content\"),\n     423: (\"locked\",),\n     424: (\"failed_dependency\", \"dependency\"),\n-    425: (\"unordered_collection\", \"unordered\"),\n+    425: (\"unordered_collection\", \"unordered\", \"too_early\"),\n     426: (\"upgrade_required\", \"upgrade\"),\n     428: (\"precondition_required\", \"precondition\"),\n     429: (\"too_many_requests\", \"too_many\"),",
      "previous_filename": "requests/status_codes.py"
    },
    {
      "sha": "188e13e4829591facb23ae0e2eda84b9807cb818",
      "filename": "src/requests/structures.py",
      "status": "renamed",
      "additions": 0,
      "deletions": 0,
      "changes": 0,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fstructures.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Fstructures.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/src%2Frequests%2Fstructures.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "previous_filename": "requests/structures.py"
    },
    {
      "sha": "ae6c42f6cb48d2beaa3b7352bc1d130db3e4e3be",
      "filename": "src/requests/utils.py",
      "status": "renamed",
      "additions": 9,
      "deletions": 7,
      "changes": 16,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Futils.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/src%2Frequests%2Futils.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/src%2Frequests%2Futils.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -97,6 +97,8 @@ def proxy_bypass_registry(host):\n         # '<local>' string by the localhost entry and the corresponding\n         # canonical entry.\n         proxyOverride = proxyOverride.split(\";\")\n+        # filter out empty strings to avoid re.match return true in the following code.\n+        proxyOverride = filter(None, proxyOverride)\n         # now check if we match one of the registry values.\n         for test in proxyOverride:\n             if test == \"<local>\":\n@@ -134,6 +136,9 @@ def super_len(o):\n     total_length = None\n     current_position = 0\n \n+    if isinstance(o, str):\n+        o = o.encode(\"utf-8\")\n+\n     if hasattr(o, \"__len__\"):\n         total_length = len(o)\n \n@@ -466,11 +471,7 @@ def dict_from_cookiejar(cj):\n     :rtype: dict\n     \"\"\"\n \n-    cookie_dict = {}\n-\n-    for cookie in cj:\n-        cookie_dict[cookie.name] = cookie.value\n-\n+    cookie_dict = {cookie.name: cookie.value for cookie in cj}\n     return cookie_dict\n \n \n@@ -767,6 +768,7 @@ def should_bypass_proxies(url, no_proxy):\n \n     :rtype: bool\n     \"\"\"\n+\n     # Prioritize lowercase environment variables over uppercase\n     # to keep a consistent behaviour with other http projects (curl, wget).\n     def get_proxy(key):\n@@ -862,7 +864,7 @@ def select_proxy(url, proxies):\n def resolve_proxies(request, proxies, trust_env=True):\n     \"\"\"This method takes proxy information from a request and configuration\n     input to resolve a mapping of target proxies. This will consider settings\n-    such a NO_PROXY to strip proxy configurations.\n+    such as NO_PROXY to strip proxy configurations.\n \n     :param request: Request or PreparedRequest\n     :param proxies: A dictionary of schemes or schemes and hosts to proxy URLs\n@@ -1054,7 +1056,7 @@ def _validate_header_part(header, header_part, header_validator_index):\n     if not validator.match(header_part):\n         header_kind = \"name\" if header_validator_index == 0 else \"value\"\n         raise InvalidHeader(\n-            f\"Invalid leading whitespace, reserved character(s), or return\"\n+            f\"Invalid leading whitespace, reserved character(s), or return \"\n             f\"character(s) in header {header_kind}: {header_part!r}\"\n         )\n ",
      "previous_filename": "requests/utils.py"
    },
    {
      "sha": "4bf7002e0b17e14449cd116daf2406760022eebb",
      "filename": "tests/certs/README.md",
      "status": "added",
      "additions": 10,
      "deletions": 0,
      "changes": 10,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2FREADME.md",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2FREADME.md",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2FREADME.md?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,10 @@\n+# Testing Certificates\n+\n+This is a collection of certificates useful for testing aspects of Requests'\n+behaviour.\n+\n+The certificates include:\n+\n+* [expired](./expired) server certificate with a valid certificate authority\n+* [mtls](./mtls) provides a valid client certificate with a 2 year validity\n+* [valid](./valid) has a valid server certificate"
    },
    {
      "sha": "d5a51da5419a81188fb92f6c28868c622baee829",
      "filename": "tests/certs/expired/Makefile",
      "status": "added",
      "additions": 13,
      "deletions": 0,
      "changes": 13,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2FMakefile",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2FMakefile",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fexpired%2FMakefile?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,13 @@\n+.PHONY: all clean ca server\n+\n+ca:\n+\tmake -C $@ all\n+\n+server:\n+\tmake -C $@ all\n+\n+all: ca server\n+\n+clean:\n+\tmake -C ca clean\n+\tmake -C server clean"
    },
    {
      "sha": "f7234f8820f7ffc749eb45ba12529647704ab297",
      "filename": "tests/certs/expired/README.md",
      "status": "added",
      "additions": 11,
      "deletions": 0,
      "changes": 11,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2FREADME.md",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2FREADME.md",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fexpired%2FREADME.md?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,11 @@\n+# Expired Certificates and Configuration for Testing\n+\n+This has a valid certificate authority in [ca](./ca) and an invalid server\n+certificate in [server](./server).\n+\n+This can all be regenerated with:\n+\n+```\n+make clean\n+make all\n+```"
    },
    {
      "sha": "098193f88d9bacd97a91aecaf874ac584977ac94",
      "filename": "tests/certs/expired/ca/Makefile",
      "status": "added",
      "additions": 13,
      "deletions": 0,
      "changes": 13,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2Fca%2FMakefile",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2Fca%2FMakefile",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fexpired%2Fca%2FMakefile?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,13 @@\n+.PHONY: all clean\n+\n+root_files = ca-private.key ca.crt\n+\n+ca-private.key:\n+\topenssl genrsa -out ca-private.key 2048\n+\n+all: ca-private.key\n+\topenssl req -x509 -sha256 -days 7300 -key ca-private.key -out ca.crt -config ca.cnf\n+\tln -s ca.crt cacert.pem\n+\n+clean:\n+\trm -f cacert.pem ca.crt ca-private.key *.csr"
    },
    {
      "sha": "507b1f5623f8d8f04c772281a0fea8af261ab644",
      "filename": "tests/certs/expired/ca/ca-private.key",
      "status": "added",
      "additions": 28,
      "deletions": 0,
      "changes": 28,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2Fca%2Fca-private.key",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2Fca%2Fca-private.key",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fexpired%2Fca%2Fca-private.key?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,28 @@\n+-----BEGIN PRIVATE KEY-----\n+MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDHlIhe7GLCeSk8\n+RZOKdtmyKns6KdZgGw/LcxPkYvQlu1g0zV8X0DqVr2LdMumWUTNCc9sPdSlAG+He\n+mQp2TMoWUMumMuwDtit9RT0Sb6Eh9svWgjY9ferovPJRfCWUTsA2Ug8uoh0wyEXK\n+na7X6fHt5E3B9vj0+b9a4vDibdBXV11FheLT02/uEmAEJDdP/zeBgvVbhcVyumO6\n+fAGMIWzR2ukhe8z/ma5H9zoi4gZA8nsK6reZUD8+6affnPe+jIt/AdzggtV9jkWm\n+zSpr+RHeZ0y+q4eik2ZNUGg4XcF6JsJ9yu/AqLBXxd38uLdFfgyhP2y6K628yzgy\n+e6lzFyWnAgMBAAECggEAFwzHhzcD3PQDWCus85PwZoxTeQ817BmUBGpBBOKM0gLG\n+GCsT7XsmGP2NjICBy9OK+QTKawmb/wR5XK0OMUWDHXqtWn+NFIyojyo8+HEeCf8n\n+4ZleTFHLnJ+d2N1etbc2qc9mY3tjpaurq8/0Tol9YH06ock1TY2+lO+a5HvMURnY\n+hcWs70CamL+5B/6n67DhjzMtIW3dIXuEEceM1BW/jW8SKq0JHpQ3t+OJwID7zFaJ\n+bLyOwAVheMzVGvN3yphf8tll3tMA65bNjdOzgOfZSjAy7EGjW3DyAolDw9jKLRyu\n+E0gw/exNGe618oMIeUDv0KParlL4RjdiUP8l0xYOwQKBgQD3eYj9rWeqZquI9vKP\n+gaSv6urb2UJLngShZUpEZRNJgBO+Ewiof0w8tpQdsnuMvWudxMLbzgiUNA+NyC/K\n+CpzIXFkWnWx+A/pxs8ZO8moOfajVRayJgeOLsQZb7c4fXGsVGApbN4+cPNhTNG6d\n+ucErv6tae/SzAzcLc5Vkw/ELxwKBgQDOdJ5Wl5JeKAvU/3kF6+MYWCrXxZqMjoHS\n+y1BtyMX5RbdaWTCfDUu1aV3qJOJjjWQ9DJdJQcEsrTjOpD4bVdZx4w/XEG0JXAa3\n+jRypVHGdeG/TjhUGJA8U+KX3a1DkcdqM9pqFYRw5Ie95Wz9YRroI+YkixqpK8d7W\n+C+5BodxXIQKBgCk8Lv9V7XgPM3XW8APJbk+BrTCEuu8unUbnQcCztssAdEmvkjnB\n+PErBgVyRaNTCmzPmnTFS20sWgaD2QkBAFG+uM4n5ISK+NvTLJ7fv3IwdlAw1V9Jx\n+uiCElrKqpTXEiHMzVkZss5ks6j6y9duCIBXSEhM5pERPvNRDphjsLTXxAoGARSNC\n+nyb1Kjjo9XR0V+pNy6pC9q1C+00B5tCVZ55zxe114Hi70pfGQcM+YxnlAoeoCNW9\n+mBfAFDESNAlGjyrovIzYkiH7EcZSrYdBEOepgJ2DfWo4Wi0bK9+03K2AknAaS1iO\n+GJqTtAJMSuymwu40gKroJNA42Q40nKO0LyCARGECgYEAiFRHkblBtStv22SpZxNC\n+jim9yuM0ikh7Ij1lEHysc/GWb2RQNxQVk54BU2kQ0d9xwMZQTKvpF3VE9t7uGdwt\n+AasWPr/tWYt35Ud0D4bNlagJJ4Xdslf8n1nkq3qqqDQbd7kkQRgwGzVr0uVg7ZfS\n+26qSPQ0/aF9nagb5eHX3AuU=\n+-----END PRIVATE KEY-----"
    },
    {
      "sha": "8c4b823053e13b174538075b623899639f5a367e",
      "filename": "tests/certs/expired/ca/ca.cnf",
      "status": "added",
      "additions": 12,
      "deletions": 0,
      "changes": 12,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2Fca%2Fca.cnf",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2Fca%2Fca.cnf",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fexpired%2Fca%2Fca.cnf?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,12 @@\n+[req]\n+default_bits = 2048\n+prompt = no\n+default_md = sha256\n+encrypt_key = no\n+distinguished_name = dn\n+\n+[dn]\n+C = US                            # country code\n+O = Python Software Foundation    # organization\n+OU = python-requests              # organization unit/department\n+CN = Self-Signed Root CA          # common name / your cert name"
    },
    {
      "sha": "c332b7cb7b321e617966cf3c0a3939852c72e514",
      "filename": "tests/certs/expired/ca/ca.crt",
      "status": "added",
      "additions": 20,
      "deletions": 0,
      "changes": 20,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2Fca%2Fca.crt",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2Fca%2Fca.crt",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fexpired%2Fca%2Fca.crt?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,20 @@\n+-----BEGIN CERTIFICATE-----\n+MIIDWzCCAkMCFA9wdtNh/V99DRwYp8vXjPxSjJnWMA0GCSqGSIb3DQEBCwUAMGox\n+CzAJBgNVBAYTAlVTMSMwIQYDVQQKDBpQeXRob24gU29mdHdhcmUgRm91bmRhdGlv\n+bjEYMBYGA1UECwwPcHl0aG9uLXJlcXVlc3RzMRwwGgYDVQQDDBNTZWxmLVNpZ25l\n+ZCBSb290IENBMB4XDTI0MDMxMjIxMDQwM1oXDTQ0MDMwNzIxMDQwM1owajELMAkG\n+A1UEBhMCVVMxIzAhBgNVBAoMGlB5dGhvbiBTb2Z0d2FyZSBGb3VuZGF0aW9uMRgw\n+FgYDVQQLDA9weXRob24tcmVxdWVzdHMxHDAaBgNVBAMME1NlbGYtU2lnbmVkIFJv\n+b3QgQ0EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDHlIhe7GLCeSk8\n+RZOKdtmyKns6KdZgGw/LcxPkYvQlu1g0zV8X0DqVr2LdMumWUTNCc9sPdSlAG+He\n+mQp2TMoWUMumMuwDtit9RT0Sb6Eh9svWgjY9ferovPJRfCWUTsA2Ug8uoh0wyEXK\n+na7X6fHt5E3B9vj0+b9a4vDibdBXV11FheLT02/uEmAEJDdP/zeBgvVbhcVyumO6\n+fAGMIWzR2ukhe8z/ma5H9zoi4gZA8nsK6reZUD8+6affnPe+jIt/AdzggtV9jkWm\n+zSpr+RHeZ0y+q4eik2ZNUGg4XcF6JsJ9yu/AqLBXxd38uLdFfgyhP2y6K628yzgy\n+e6lzFyWnAgMBAAEwDQYJKoZIhvcNAQELBQADggEBAGymNVTsKSAq8Ju6zV+AWAyV\n+GcUNBmLpgzDA0e7pkVYhHTdWKlGH4GnrRcp0nvnSbr6iq1Ob/8yEUUoRzK55Flws\n+Kt1OLwnZyhfRoSUesoEqpP68vzWEgiYv0QuIWvzNt0YfAAvEgGoc3iri44MelKLn\n+9ZMT8m91nVamA35R8ZjfeAkNp2xcz0a67V0ww6o4wSXrG7o5ZRXyjqZ/9K7SfwUJ\n+rV9RciccsjH/MzKbfrx73QwsbPWiFmjzHopdasIO0lDlmgm/r9gKfkbzfKoGCgLZ\n+6an6FlmLftLSXijf/QwtqeSP9fODeE3dzBmnTM3jdoVS53ZegUDWNl14o25v2Kg=\n+-----END CERTIFICATE-----"
    },
    {
      "sha": "fab68405ed30093291a848dc095edfe75fab707c",
      "filename": "tests/certs/expired/ca/ca.srl",
      "status": "added",
      "additions": 1,
      "deletions": 0,
      "changes": 1,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2Fca%2Fca.srl",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2Fca%2Fca.srl",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fexpired%2Fca%2Fca.srl?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1 @@\n+4F36C3A7E075BA6452D10EEB81E7F189FF489B74"
    },
    {
      "sha": "79914ee1dbf2eca48ba265e03899cc555cdc925a",
      "filename": "tests/certs/expired/server/Makefile",
      "status": "added",
      "additions": 16,
      "deletions": 0,
      "changes": 16,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2Fserver%2FMakefile",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2Fserver%2FMakefile",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fexpired%2Fserver%2FMakefile?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,16 @@\n+.PHONY: all clean\n+\n+server.key:\n+\topenssl genrsa -out $@ 2048\n+\n+server.csr: server.key\n+\topenssl req -key $< -new -out $@ -config cert.cnf\n+\n+server.pem: server.csr\n+\topenssl x509 -req -CA ../ca/ca.crt -CAkey ../ca/ca-private.key -in server.csr -outform PEM -out server.pem -days 0 -CAcreateserial\n+\topenssl x509 -in ../ca/ca.crt -outform PEM >> $@\n+\n+all: server.pem\n+\n+clean:\n+\trm -f server.*"
    },
    {
      "sha": "a773fc679f22e1a538f171535463e1fd116b61ac",
      "filename": "tests/certs/expired/server/cert.cnf",
      "status": "added",
      "additions": 24,
      "deletions": 0,
      "changes": 24,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2Fserver%2Fcert.cnf",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2Fserver%2Fcert.cnf",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fexpired%2Fserver%2Fcert.cnf?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,24 @@\n+[req]\n+req_extensions = v3_req\n+distinguished_name = req_distinguished_name\n+prompt=no\n+\n+[req_distinguished_name]\n+C = US\n+ST = DE\n+O = Python Software Foundation\n+OU = python-requests\n+CN = localhost\n+\n+[v3_req]\n+# Extensions to add to a certificate request\n+basicConstraints = CA:FALSE\n+keyUsage = digitalSignature, keyEncipherment\n+extendedKeyUsage = serverAuth\n+subjectAltName = @alt_names\n+\n+[alt_names]\n+DNS.1 = *.localhost\n+DNS.1 = localhost\n+IP.1 = 127.0.0.1\n+IP.2 = ::1"
    },
    {
      "sha": "5e3c1776472cb6ad7caebe011ca0608943ba567b",
      "filename": "tests/certs/expired/server/server.csr",
      "status": "added",
      "additions": 19,
      "deletions": 0,
      "changes": 19,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2Fserver%2Fserver.csr",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2Fserver%2Fserver.csr",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fexpired%2Fserver%2Fserver.csr?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,19 @@\n+-----BEGIN CERTIFICATE REQUEST-----\n+MIIDHjCCAgYCAQAwbTELMAkGA1UEBhMCVVMxCzAJBgNVBAgMAkRFMSMwIQYDVQQK\n+DBpQeXRob24gU29mdHdhcmUgRm91bmRhdGlvbjEYMBYGA1UECwwPcHl0aG9uLXJl\n+cXVlc3RzMRIwEAYDVQQDDAlsb2NhbGhvc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IB\n+DwAwggEKAoIBAQCKulIMpo633iCgbkKv1UoiLC4sQt5xWpgguujywu3hLYwmPFp9\n+kvPt//imqtl8FhuhKqJ8FCGrVl2YIGj1RJIB3GW7MSPNCuIBFL/gwNi35LxDPtoA\n+IPyXytIR7VH9+ch9DFInJaoA/BekMuKvbXk54VW9whpHbwkXSG2lBS2vKL0XemYh\n+9VjvtuRDji2iOZpznlVE2PEN80bojArp6oYKakv2kYzgzgxAJiI/NZGvC7mbSI4e\n+ja7ad3R9G0kB1FzNj36jrNO5WtxHO/mrRiXSpDeyUbitYvt0HKoM0vhTnOR+BspP\n+IltfwOQh8qq2Q2AaMHNcVjMH3gHCZADfhk/zAgMBAAGgbDBqBgkqhkiG9w0BCQ4x\n+XTBbMAkGA1UdEwQCMAAwCwYDVR0PBAQDAgWgMBMGA1UdJQQMMAoGCCsGAQUFBwMB\n+MCwGA1UdEQQlMCOCCWxvY2FsaG9zdIcEfwAAAYcQAAAAAAAAAAAAAAAAAAAAATAN\n+BgkqhkiG9w0BAQsFAAOCAQEAfAhEhrulsZae71YFqgvzwJHm/hzXh47hErtgDXVJ\n+mFqAxgF6XrnzYujlt3XQXUx/8vdrU7jH+Pe8WO1rDvFwRPMDGoBF3RX29SzyX/2F\n+e102egnoRR+Hlf0Ixqu0CuTjEVnD+g4mRgXhV7LPKP4W6qGwzcVbaJ3c/zRcfqNR\n+g9gN6Q6Qt4fXDc7wlx2T3nOszBLQ2XCsIyzVtOJ2sSuadqKH9Aj+mrkrLBdzVFHD\n+FHnTMJ0t0+anZwd+AWDNsCr5lIwBGL634zw7/yJepMHuPFd2X24S3u8EaWPkfVQn\n+lV6rLQMGjXYTe2xuYzlUCUYnKvkyPTMjSXDkxWa+WSNwyQ==\n+-----END CERTIFICATE REQUEST-----"
    },
    {
      "sha": "27ddafd1ca44327f85e6db4d25d84411a7549339",
      "filename": "tests/certs/expired/server/server.key",
      "status": "added",
      "additions": 28,
      "deletions": 0,
      "changes": 28,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2Fserver%2Fserver.key",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2Fserver%2Fserver.key",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fexpired%2Fserver%2Fserver.key?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,28 @@\n+-----BEGIN PRIVATE KEY-----\n+MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCKulIMpo633iCg\n+bkKv1UoiLC4sQt5xWpgguujywu3hLYwmPFp9kvPt//imqtl8FhuhKqJ8FCGrVl2Y\n+IGj1RJIB3GW7MSPNCuIBFL/gwNi35LxDPtoAIPyXytIR7VH9+ch9DFInJaoA/Bek\n+MuKvbXk54VW9whpHbwkXSG2lBS2vKL0XemYh9VjvtuRDji2iOZpznlVE2PEN80bo\n+jArp6oYKakv2kYzgzgxAJiI/NZGvC7mbSI4eja7ad3R9G0kB1FzNj36jrNO5WtxH\n+O/mrRiXSpDeyUbitYvt0HKoM0vhTnOR+BspPIltfwOQh8qq2Q2AaMHNcVjMH3gHC\n+ZADfhk/zAgMBAAECggEAFSF9RvUFzyb0BEvXN44+/QaKv+4tkMmSW4Xs3rFnZ4G3\n+E8nkpLUCF9ICD2z9tKNvcPScDFdKq5z7o6ToJ9faf5MRIdrBz8UlGLIO6g6l1Bjw\n+vjNwJE3h+8MGjXl/IDbwXW/HgbQAeabsePPRSJRdvz2+ACn1M8VLdrLvFJA93ayW\n++n3Bk0bXdsrzqBGdoDiNzmIHI3WqdONiR9TymuJe41NJtMKxQDF+c6Y1n/X1OtBk\n+s9L+u9Xr+R3H72xSYrf1KH1mFZJfTnIPoOmdEU2tVZnZj03rZhT7p8R1fVNX6OHu\n+NX1Dy9VA6J7dbcqdPvTI743ByQeb+hNnqI/3hmV5eQKBgQC++1Wn3v/dxtczjA+I\n+tN4a7zyjhazpB25lde55HVfCQPxmYxIYct+j6S0JkMaoLrjiEDb4pnu4Gt4MDqZa\n+r0Xm8t3wD1YKUUbhpBEGvsMhAEZEIsBOcwkTiEwsoF0mKFa2mTyqAImgIQa8uFt8\n+Y/oTj55XFe1x6pZKEJRg+K+QSwKBgQC59ONVkMSBirLGS+G+b2kqiBdwZB/3s3wr\n+feS1xTa+deL3AChnKT9+MsVqOkxdE2TRj/mAeF+5Woa5bPMvgr9Kl7u8bulTH80l\n+YA/N6FneO11/ncnkgK9wN54kd5TiOtGsGB5S5t/nEAIMUIwWrM/cRau72xNEWOhT\n+Tvw7TOSF+QKBgQCa/texeiYmE24sA4vH4yIuseKAw8hlBwbtiRyVZt8GZD9zyQuy\n+k+g02tUWYk0XyXN65LX4bwURkZyMJIeWKZGNsaW1YnzturDQB5tZ4g/zBIoCWkHA\n+aVQAaimIPk3a3foiD5NQVUdckfEp0GVPOsSGg5R6EO23+i8mxPXnDW1OqQKBgGvf\n+lelTO8tyLFdAOcqBUt6rZ/1499p3snaAZ6bSqvk95dYnr0h48y5AQaln/FiaIYg4\n+HyLZsZ4S18jFXSWYkWOyNeQP6yafciBWY5StT0TN52VaoX3+8McGXKUHAcVjHbLZ\n+ou2wpP6jmKyQJVQaF9LOT9uAMOMbOFrrnQLBjmfxAoGAQAnUhMFG5mwi9Otxt6Mz\n+g+Gr+3JTlzwC3L7UwGdlFc3G2vSdGx/yOrfzpxPImfIBS95mibDfdvEBMer26pvw\n+a/ycqybyX9d/5nPDIaJ1lc4M4cbHC/cB52JI6avr/1g8OMK7lR7b/FsPVHS1w8kl\n+n6uwEjVt2+gP2o9DFTGs158=\n+-----END PRIVATE KEY-----"
    },
    {
      "sha": "05a2a4dac809bb6863e628e53b5d0d5f389c145e",
      "filename": "tests/certs/expired/server/server.pem",
      "status": "added",
      "additions": 41,
      "deletions": 0,
      "changes": 41,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2Fserver%2Fserver.pem",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fexpired%2Fserver%2Fserver.pem",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fexpired%2Fserver%2Fserver.pem?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,41 @@\n+-----BEGIN CERTIFICATE-----\n+MIIDXjCCAkYCFE82w6fgdbpkUtEO64Hn8Yn/SJt0MA0GCSqGSIb3DQEBCwUAMGox\n+CzAJBgNVBAYTAlVTMSMwIQYDVQQKDBpQeXRob24gU29mdHdhcmUgRm91bmRhdGlv\n+bjEYMBYGA1UECwwPcHl0aG9uLXJlcXVlc3RzMRwwGgYDVQQDDBNTZWxmLVNpZ25l\n+ZCBSb290IENBMB4XDTI0MDMxMzIxMTQ0NVoXDTI0MDMxMzIxMTQ0NVowbTELMAkG\n+A1UEBhMCVVMxCzAJBgNVBAgMAkRFMSMwIQYDVQQKDBpQeXRob24gU29mdHdhcmUg\n+Rm91bmRhdGlvbjEYMBYGA1UECwwPcHl0aG9uLXJlcXVlc3RzMRIwEAYDVQQDDAls\n+b2NhbGhvc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCKulIMpo63\n+3iCgbkKv1UoiLC4sQt5xWpgguujywu3hLYwmPFp9kvPt//imqtl8FhuhKqJ8FCGr\n+Vl2YIGj1RJIB3GW7MSPNCuIBFL/gwNi35LxDPtoAIPyXytIR7VH9+ch9DFInJaoA\n+/BekMuKvbXk54VW9whpHbwkXSG2lBS2vKL0XemYh9VjvtuRDji2iOZpznlVE2PEN\n+80bojArp6oYKakv2kYzgzgxAJiI/NZGvC7mbSI4eja7ad3R9G0kB1FzNj36jrNO5\n+WtxHO/mrRiXSpDeyUbitYvt0HKoM0vhTnOR+BspPIltfwOQh8qq2Q2AaMHNcVjMH\n+3gHCZADfhk/zAgMBAAEwDQYJKoZIhvcNAQELBQADggEBAGeQdB4+iDbJ78eKhCMV\n+49Cm8nyYi9215rRRJ24Bw6BtVw1ECwymxLVOEB0gHCu8kKdsFnniFBtChts/ilFg\n+blIyPKTsb3+kQW9YV9QwVdFdC4mTIljujCSQ4HNUC/Vjfnz85SDKf9/3PMKRr36+\n+GtSLIozudPvkNmCv68jy3RRXyCwWHc43BLMSZKPD/W+DEuXShI9OIpIlSLBx16Hz\n+4ce3/1pGuITWcsw6UcRqW31oPR31QmNs5fsq5ZCojDNFzEFCA1t9LiR6UOftFUKy\n+yOZWfZeAGGdK75U+XDqS9Xkr5/ic5jE0I5rT7e7r3lpvQdgIj8lSx493fczLOGHr\n+YA0=\n+-----END CERTIFICATE-----\n+-----BEGIN CERTIFICATE-----\n+MIIDWzCCAkMCFA9wdtNh/V99DRwYp8vXjPxSjJnWMA0GCSqGSIb3DQEBCwUAMGox\n+CzAJBgNVBAYTAlVTMSMwIQYDVQQKDBpQeXRob24gU29mdHdhcmUgRm91bmRhdGlv\n+bjEYMBYGA1UECwwPcHl0aG9uLXJlcXVlc3RzMRwwGgYDVQQDDBNTZWxmLVNpZ25l\n+ZCBSb290IENBMB4XDTI0MDMxMjIxMDQwM1oXDTQ0MDMwNzIxMDQwM1owajELMAkG\n+A1UEBhMCVVMxIzAhBgNVBAoMGlB5dGhvbiBTb2Z0d2FyZSBGb3VuZGF0aW9uMRgw\n+FgYDVQQLDA9weXRob24tcmVxdWVzdHMxHDAaBgNVBAMME1NlbGYtU2lnbmVkIFJv\n+b3QgQ0EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDHlIhe7GLCeSk8\n+RZOKdtmyKns6KdZgGw/LcxPkYvQlu1g0zV8X0DqVr2LdMumWUTNCc9sPdSlAG+He\n+mQp2TMoWUMumMuwDtit9RT0Sb6Eh9svWgjY9ferovPJRfCWUTsA2Ug8uoh0wyEXK\n+na7X6fHt5E3B9vj0+b9a4vDibdBXV11FheLT02/uEmAEJDdP/zeBgvVbhcVyumO6\n+fAGMIWzR2ukhe8z/ma5H9zoi4gZA8nsK6reZUD8+6affnPe+jIt/AdzggtV9jkWm\n+zSpr+RHeZ0y+q4eik2ZNUGg4XcF6JsJ9yu/AqLBXxd38uLdFfgyhP2y6K628yzgy\n+e6lzFyWnAgMBAAEwDQYJKoZIhvcNAQELBQADggEBAGymNVTsKSAq8Ju6zV+AWAyV\n+GcUNBmLpgzDA0e7pkVYhHTdWKlGH4GnrRcp0nvnSbr6iq1Ob/8yEUUoRzK55Flws\n+Kt1OLwnZyhfRoSUesoEqpP68vzWEgiYv0QuIWvzNt0YfAAvEgGoc3iri44MelKLn\n+9ZMT8m91nVamA35R8ZjfeAkNp2xcz0a67V0ww6o4wSXrG7o5ZRXyjqZ/9K7SfwUJ\n+rV9RciccsjH/MzKbfrx73QwsbPWiFmjzHopdasIO0lDlmgm/r9gKfkbzfKoGCgLZ\n+6an6FlmLftLSXijf/QwtqeSP9fODeE3dzBmnTM3jdoVS53ZegUDWNl14o25v2Kg=\n+-----END CERTIFICATE-----"
    },
    {
      "sha": "399a906da795e1deef237cf6e10035e503b8cf04",
      "filename": "tests/certs/mtls/Makefile",
      "status": "added",
      "additions": 7,
      "deletions": 0,
      "changes": 7,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fmtls%2FMakefile",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fmtls%2FMakefile",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fmtls%2FMakefile?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,7 @@\n+.PHONY: all clean\n+\n+all:\n+\tmake -C client all\n+\n+clean:\n+\tmake -C client clean"
    },
    {
      "sha": "9a3df4623eedff71c276ecfa7f0c46f485f649a0",
      "filename": "tests/certs/mtls/README.md",
      "status": "added",
      "additions": 4,
      "deletions": 0,
      "changes": 4,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fmtls%2FREADME.md",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fmtls%2FREADME.md",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fmtls%2FREADME.md?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,4 @@\n+# Certificate Examples for mTLS\n+\n+This has some generated certificates for mTLS utilization. The idea is to be\n+able to have testing around how Requests handles client certificates."
    },
    {
      "sha": "9c6c388be1111d062ee21566c6c4188ec7fe1f9e",
      "filename": "tests/certs/mtls/client/Makefile",
      "status": "added",
      "additions": 16,
      "deletions": 0,
      "changes": 16,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fmtls%2Fclient%2FMakefile",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fmtls%2Fclient%2FMakefile",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fmtls%2Fclient%2FMakefile?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,16 @@\n+.PHONY: all clean\n+\n+client.key:\n+\topenssl genrsa -out $@ 2048\n+\n+client.csr: client.key\n+\topenssl req -key $< -new -out $@ -config cert.cnf\n+\n+client.pem: client.csr\n+\topenssl x509 -req -CA ./ca/ca.crt -CAkey ./ca/ca-private.key -in client.csr -outform PEM -out client.pem -days 730 -CAcreateserial\n+\topenssl x509 -in ./ca/ca.crt -outform PEM >> $@\n+\n+all: client.pem\n+\n+clean:\n+\trm -f client.*"
    },
    {
      "sha": "85c8e8f2c2ce668cc9fb0d32a01b7ad341874c37",
      "filename": "tests/certs/mtls/client/ca",
      "status": "added",
      "additions": 1,
      "deletions": 0,
      "changes": 1,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fmtls%2Fclient%2Fca",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fmtls%2Fclient%2Fca",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fmtls%2Fclient%2Fca?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1 @@\n+../../expired/ca/\n\\ No newline at end of file"
    },
    {
      "sha": "338e2527bac76d691937e63af86462992579853e",
      "filename": "tests/certs/mtls/client/cert.cnf",
      "status": "added",
      "additions": 26,
      "deletions": 0,
      "changes": 26,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fmtls%2Fclient%2Fcert.cnf",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fmtls%2Fclient%2Fcert.cnf",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fmtls%2Fclient%2Fcert.cnf?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,26 @@\n+[req]\n+req_extensions = v3_req\n+distinguished_name = req_distinguished_name\n+prompt=no\n+\n+[req_distinguished_name]\n+C = US\n+ST = DE\n+O = Python Software Foundation\n+OU = python-requests\n+CN = requests\n+\n+[v3_req]\n+# Extensions to add to a certificate request\n+basicConstraints = CA:FALSE\n+keyUsage = digitalSignature, keyEncipherment\n+extendedKeyUsage = clientAuth\n+subjectAltName = @alt_names\n+\n+[alt_names]\n+DNS.1 = *.localhost\n+IP.1 = 127.0.0.1\n+IP.2 = ::1\n+URI.1 = spiffe://trust.python.org/v0/maintainer/sigmavirus24/project/requests/org/psf\n+URI.2 = spiffe://trust.python.org/v1/maintainer:sigmavirus24/project:requests/org:psf\n+URI.3 = spiffe://trust.python.org/v1/maintainer=sigmavirus24/project=requests/org=psf"
    },
    {
      "sha": "9a5713d5c797a72399ee4217f7c5bb359f491728",
      "filename": "tests/certs/mtls/client/client.csr",
      "status": "added",
      "additions": 24,
      "deletions": 0,
      "changes": 24,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fmtls%2Fclient%2Fclient.csr",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fmtls%2Fclient%2Fclient.csr",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fmtls%2Fclient%2Fclient.csr?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,24 @@\n+-----BEGIN CERTIFICATE REQUEST-----\n+MIIEGjCCAwICAQAwbDELMAkGA1UEBhMCVVMxCzAJBgNVBAgMAkRFMSMwIQYDVQQK\n+DBpQeXRob24gU29mdHdhcmUgRm91bmRhdGlvbjEYMBYGA1UECwwPcHl0aG9uLXJl\n+cXVlc3RzMREwDwYDVQQDDAhyZXF1ZXN0czCCASIwDQYJKoZIhvcNAQEBBQADggEP\n+ADCCAQoCggEBAMn3iQycTjUzpKJChRNkcm33UB282cUwpxeqKN4ahHxBpS09HRhk\n+cQYO7yErEUQwzQnBQEcIpzzeIMZIqHuCkgnySjeEJd95AIzNzGyoLLkS51TcJwgR\n+v83AvT8ljA88s9h38qGTy4/TCxJgf76pfHIuC1qoKVQh3AuHj9nOxIZLUsrdDbWF\n+WoLqKSVyTby+RXvSAppAR+cuBCaWStQ6xFORn48RHfc6t30ggD4rDAjyU6Vz6oR8\n+ot3XmGdK0h42UdqidUWkRJajEbpkCnQSXS21IvfXKxF5sFqAXJrj9iVbUfpNPpaa\n+W8IrHByngyV8amazGZrASstUVRFtWrnrcWECAwEAAaCCAWcwggFjBgkqhkiG9w0B\n+CQ4xggFUMIIBUDAJBgNVHRMEAjAAMAsGA1UdDwQEAwIFoDATBgNVHSUEDDAKBggr\n+BgEFBQcDAjCCAR8GA1UdEQSCARYwggESggsqLmxvY2FsaG9zdIcEfwAAAYcQAAAA\n+AAAAAAAAAAAAAAAAAYZNc3BpZmZlOi8vdHJ1c3QucHl0aG9uLm9yZy92MC9tYWlu\n+dGFpbmVyL3NpZ21hdmlydXMyNC9wcm9qZWN0L3JlcXVlc3RzL29yZy9wc2aGTXNw\n+aWZmZTovL3RydXN0LnB5dGhvbi5vcmcvdjEvbWFpbnRhaW5lcjpzaWdtYXZpcnVz\n+MjQvcHJvamVjdDpyZXF1ZXN0cy9vcmc6cHNmhk1zcGlmZmU6Ly90cnVzdC5weXRo\n+b24ub3JnL3YxL21haW50YWluZXI9c2lnbWF2aXJ1czI0L3Byb2plY3Q9cmVxdWVz\n+dHMvb3JnPXBzZjANBgkqhkiG9w0BAQsFAAOCAQEAwP1KJ+Evddn2RV1FM6BFkoDK\n+MPDO9qwb8ea3j57SIJXZlpw168DljmuGzxJw9oys2O6FYcspbHIocAkfFwiYgVAr\n+NEog6xlCdPxNBJgC3YFIKwnmBjMPG6ZCWiJn940qTbaJ/j6ZviN17uW4K7Sl+THp\n+IkMv29uQTWkfg+GbZ9q1hm2m2GHhYLGLAUdJdtv7JI+yq5uxdsWaCANpH6kc8SnK\n+2rik6D3iItDhHCmToHBpdEnP8J+KDzf5pJrv/g3WH8XVrl4ZzBsOhmciWF4C3Hbf\n+9eu8eAsp1AsIrZOEGTfClBd7vFCES5DmI0/iRs4czQooqZPnHjOw3Azp/LujrA==\n+-----END CERTIFICATE REQUEST-----"
    },
    {
      "sha": "81071253997bad4d929cecabaab58cd9c44d1b05",
      "filename": "tests/certs/mtls/client/client.key",
      "status": "added",
      "additions": 28,
      "deletions": 0,
      "changes": 28,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fmtls%2Fclient%2Fclient.key",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fmtls%2Fclient%2Fclient.key",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fmtls%2Fclient%2Fclient.key?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,28 @@\n+-----BEGIN PRIVATE KEY-----\n+MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDJ94kMnE41M6Si\n+QoUTZHJt91AdvNnFMKcXqijeGoR8QaUtPR0YZHEGDu8hKxFEMM0JwUBHCKc83iDG\n+SKh7gpIJ8ko3hCXfeQCMzcxsqCy5EudU3CcIEb/NwL0/JYwPPLPYd/Khk8uP0wsS\n+YH++qXxyLgtaqClUIdwLh4/ZzsSGS1LK3Q21hVqC6iklck28vkV70gKaQEfnLgQm\n+lkrUOsRTkZ+PER33Ord9IIA+KwwI8lOlc+qEfKLd15hnStIeNlHaonVFpESWoxG6\n+ZAp0El0ttSL31ysRebBagFya4/YlW1H6TT6WmlvCKxwcp4MlfGpmsxmawErLVFUR\n+bVq563FhAgMBAAECggEABhWX97JJxN6JFNOjhgGzqiPA3R8lrFlv3zhNbODS9u9U\n+q404xYBZIKaYhkucLzgNJUBrevhZbsL+V8WJQIH0JlU57nw5ATIjAHA+uqiXraen\n+zRhTcLHK28b1AeRUA4LU+YN7jWnnawN075kf9WgjtfOJ0gcDimOkE7uCFjyyvPJA\n+LG9bG+8enGjvUleKXNgmwP4Sq/GlEdGz9Qy+8ga3mtfAULUWe8haFNZXK8CN3xPp\n+wmVqy7QzgH2TGN1p6Dyxib9ksSN/lOg0dShL8zgu+QXDNx2VwmVrI8Vr02vmB//0\n+bYxCo5pfICPIFLjLl5yo30dvrUfYqF29PperStHGlQKBgQD/TdemlLjJNP0fvSs7\n+KEVJj/22YuHK+wurNr2ZFbSdcF3v9sfiwysllmEyGr5cNYA56uUbfG+8VSw7kDll\n+G+6BKK2UdlPH++6RahqWLqo4k6rsNrkq7elj8xG4gIjR5qzu2uLpjNwp2BGmIoUI\n+eb1NcLfTlMcNCooV8RHjm1Z5WwKBgQDKhHkUPDcJm2/9Ltq2NZQMrCS7o4LV2uAI\n+GhGpISfY+SfHkQQNZ9Fvbe6hrFeZs31nAvlTDpPEg/LGSVKA5I2EZT9gwzAQU1TD\n+Cyol4xqqWFWlwze7w+RLYqX5LtXf7NJg2m5p+ZOoOzzqvTVpodDxqTlCNp2/6ICP\n+vAIvWhbA8wKBgAYlr62ZIyHlHrsm6OWRwKlWyDseAmXKyasjtEj9Vs37qKdgf8ub\n++2v6RPjZ3/+EYkQCveV9h4s3WctNW7Rtib6eZh+PAdFs5X+m2GEJWpvmIlVxs9+u\n+vtHjRmf04FZ9gWh26MPK2no/c51Wc3GSzNYSgrqbeHd963k/xrh+QwTFAoGAZZjb\n+3UjwG4O9RPjyhCKQ6WKa8v9urbamWaoqXfziLrmgOUAJFmiU6x/tbXI2aEdhjAIz\n+7nULsLS5YLx8BWmjjV3106dYP3hut4KsXGF4iSjTnts25J27tA4DUeUrKrF2QVyT\n+s9qfNvCw+Np/J0Uku3e33/3iWdpcVL9vIS5C5/0CgYBEuxb3dffNRqEiNkpOUrCD\n+mQTqbO3X+hin9zT3GrxQE+7KpfCfdDIqdK6c5UWHirR3HUjUPZmIFLSx8msfLl3k\n+hgQw37NMV+asg0Wy3P908qbtnEA2P6aDOMQeHJoC7qEHIDOcOQ1KP3FMvOrdscwS\n+f0IIDygTH6fYr329s0iXjg==\n+-----END PRIVATE KEY-----"
    },
    {
      "sha": "0a11d4d472c4e7a33c52cb0b5190293b07c7f885",
      "filename": "tests/certs/mtls/client/client.pem",
      "status": "added",
      "additions": 41,
      "deletions": 0,
      "changes": 41,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fmtls%2Fclient%2Fclient.pem",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fmtls%2Fclient%2Fclient.pem",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fmtls%2Fclient%2Fclient.pem?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,41 @@\n+-----BEGIN CERTIFICATE-----\n+MIIDXTCCAkUCFE82w6fgdbpkUtEO64Hn8Yn/SJtzMA0GCSqGSIb3DQEBCwUAMGox\n+CzAJBgNVBAYTAlVTMSMwIQYDVQQKDBpQeXRob24gU29mdHdhcmUgRm91bmRhdGlv\n+bjEYMBYGA1UECwwPcHl0aG9uLXJlcXVlc3RzMRwwGgYDVQQDDBNTZWxmLVNpZ25l\n+ZCBSb290IENBMB4XDTI0MDMxMzE4MzUwNFoXDTI2MDMxMzE4MzUwNFowbDELMAkG\n+A1UEBhMCVVMxCzAJBgNVBAgMAkRFMSMwIQYDVQQKDBpQeXRob24gU29mdHdhcmUg\n+Rm91bmRhdGlvbjEYMBYGA1UECwwPcHl0aG9uLXJlcXVlc3RzMREwDwYDVQQDDAhy\n+ZXF1ZXN0czCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMn3iQycTjUz\n+pKJChRNkcm33UB282cUwpxeqKN4ahHxBpS09HRhkcQYO7yErEUQwzQnBQEcIpzze\n+IMZIqHuCkgnySjeEJd95AIzNzGyoLLkS51TcJwgRv83AvT8ljA88s9h38qGTy4/T\n+CxJgf76pfHIuC1qoKVQh3AuHj9nOxIZLUsrdDbWFWoLqKSVyTby+RXvSAppAR+cu\n+BCaWStQ6xFORn48RHfc6t30ggD4rDAjyU6Vz6oR8ot3XmGdK0h42UdqidUWkRJaj\n+EbpkCnQSXS21IvfXKxF5sFqAXJrj9iVbUfpNPpaaW8IrHByngyV8amazGZrASstU\n+VRFtWrnrcWECAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAHHgMckLDRV72p1FEVmCh\n+AAPZjCswiPZFrwGPN57JqSWjoRB9ilKvo87aPosEO7vfa05OD/qkM/T9Qykuhati\n+I1T1T7qX4Ymb5kTJIBouuflAO3uKVaq+ga2Q/HLlU5w/VoMU4RuK7+RaiRUEE3xL\n+iPSMBvZpoMj695LnzcGrT5oLkFI0bTIlpQt1SFjDpHFtOj/ZdwgSbZYLoTCBXQK3\n+7Y29qAj/XwEiCH63n8tJKvZcD8/ssMIMIdWhNmu+0jOWica/3WSih9Geoy6Ydtxi\n+I5t9vRjC4LIipMUAF86AJIfvHJyI6aCNT420LaR6NRW0FQn5CPTHPAsKg3JkAywn\n+Ew==\n+-----END CERTIFICATE-----\n+-----BEGIN CERTIFICATE-----\n+MIIDWzCCAkMCFA9wdtNh/V99DRwYp8vXjPxSjJnWMA0GCSqGSIb3DQEBCwUAMGox\n+CzAJBgNVBAYTAlVTMSMwIQYDVQQKDBpQeXRob24gU29mdHdhcmUgRm91bmRhdGlv\n+bjEYMBYGA1UECwwPcHl0aG9uLXJlcXVlc3RzMRwwGgYDVQQDDBNTZWxmLVNpZ25l\n+ZCBSb290IENBMB4XDTI0MDMxMjIxMDQwM1oXDTQ0MDMwNzIxMDQwM1owajELMAkG\n+A1UEBhMCVVMxIzAhBgNVBAoMGlB5dGhvbiBTb2Z0d2FyZSBGb3VuZGF0aW9uMRgw\n+FgYDVQQLDA9weXRob24tcmVxdWVzdHMxHDAaBgNVBAMME1NlbGYtU2lnbmVkIFJv\n+b3QgQ0EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDHlIhe7GLCeSk8\n+RZOKdtmyKns6KdZgGw/LcxPkYvQlu1g0zV8X0DqVr2LdMumWUTNCc9sPdSlAG+He\n+mQp2TMoWUMumMuwDtit9RT0Sb6Eh9svWgjY9ferovPJRfCWUTsA2Ug8uoh0wyEXK\n+na7X6fHt5E3B9vj0+b9a4vDibdBXV11FheLT02/uEmAEJDdP/zeBgvVbhcVyumO6\n+fAGMIWzR2ukhe8z/ma5H9zoi4gZA8nsK6reZUD8+6affnPe+jIt/AdzggtV9jkWm\n+zSpr+RHeZ0y+q4eik2ZNUGg4XcF6JsJ9yu/AqLBXxd38uLdFfgyhP2y6K628yzgy\n+e6lzFyWnAgMBAAEwDQYJKoZIhvcNAQELBQADggEBAGymNVTsKSAq8Ju6zV+AWAyV\n+GcUNBmLpgzDA0e7pkVYhHTdWKlGH4GnrRcp0nvnSbr6iq1Ob/8yEUUoRzK55Flws\n+Kt1OLwnZyhfRoSUesoEqpP68vzWEgiYv0QuIWvzNt0YfAAvEgGoc3iri44MelKLn\n+9ZMT8m91nVamA35R8ZjfeAkNp2xcz0a67V0ww6o4wSXrG7o5ZRXyjqZ/9K7SfwUJ\n+rV9RciccsjH/MzKbfrx73QwsbPWiFmjzHopdasIO0lDlmgm/r9gKfkbzfKoGCgLZ\n+6an6FlmLftLSXijf/QwtqeSP9fODeE3dzBmnTM3jdoVS53ZegUDWNl14o25v2Kg=\n+-----END CERTIFICATE-----"
    },
    {
      "sha": "46f26c398207fffebbc6c25a355891773d81560c",
      "filename": "tests/certs/valid/ca",
      "status": "added",
      "additions": 1,
      "deletions": 0,
      "changes": 1,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fvalid%2Fca",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fvalid%2Fca",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fvalid%2Fca?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1 @@\n+../expired/ca\n\\ No newline at end of file"
    },
    {
      "sha": "9ce6778c0f229d16d4682333923e7566dc2c8607",
      "filename": "tests/certs/valid/server/Makefile",
      "status": "added",
      "additions": 16,
      "deletions": 0,
      "changes": 16,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fvalid%2Fserver%2FMakefile",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fvalid%2Fserver%2FMakefile",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fvalid%2Fserver%2FMakefile?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,16 @@\n+.PHONY: all clean\n+\n+server.key:\n+\topenssl genrsa -out $@ 2048\n+\n+server.csr: server.key\n+\topenssl req -key $< -config cert.cnf -new -out $@\n+\n+server.pem: server.csr\n+\topenssl x509 -req -CA ../ca/ca.crt -CAkey ../ca/ca-private.key -in server.csr -outform PEM -out server.pem -extfile cert.cnf -extensions v3_ca -days 7200 -CAcreateserial\n+\topenssl x509 -in ../ca/ca.crt -outform PEM >> $@\n+\n+all: server.pem\n+\n+clean:\n+\trm -f server.*"
    },
    {
      "sha": "f9a01cd8b4ba0e745f7ee866e4651bba009ab8c6",
      "filename": "tests/certs/valid/server/cert.cnf",
      "status": "added",
      "additions": 31,
      "deletions": 0,
      "changes": 31,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fvalid%2Fserver%2Fcert.cnf",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fvalid%2Fserver%2Fcert.cnf",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fvalid%2Fserver%2Fcert.cnf?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,31 @@\n+[req]\n+req_extensions = v3_req\n+distinguished_name = req_distinguished_name\n+prompt=no\n+\n+[req_distinguished_name]\n+C = US\n+ST = DE\n+O = Python Software Foundation\n+OU = python-requests\n+CN = localhost\n+\n+[v3_req]\n+# Extensions to add to a certificate request\n+basicConstraints = critical, CA:FALSE\n+keyUsage = critical, digitalSignature, keyEncipherment\n+extendedKeyUsage = critical, serverAuth\n+subjectAltName = critical, @alt_names\n+\n+[v3_ca]\n+# Extensions to add to a certificate request\n+basicConstraints = critical, CA:FALSE\n+keyUsage = critical, digitalSignature, keyEncipherment\n+extendedKeyUsage = critical, serverAuth\n+subjectAltName = critical, @alt_names\n+\n+[alt_names]\n+DNS.1 = *.localhost\n+DNS.1 = localhost\n+IP.1 = 127.0.0.1\n+IP.2 = ::1"
    },
    {
      "sha": "000d1facb29024b81b602114e2fd154848a914b6",
      "filename": "tests/certs/valid/server/server.csr",
      "status": "added",
      "additions": 19,
      "deletions": 0,
      "changes": 19,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fvalid%2Fserver%2Fserver.csr",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fvalid%2Fserver%2Fserver.csr",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fvalid%2Fserver%2Fserver.csr?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,19 @@\n+-----BEGIN CERTIFICATE REQUEST-----\n+MIIDKjCCAhICAQAwbTELMAkGA1UEBhMCVVMxCzAJBgNVBAgMAkRFMSMwIQYDVQQK\n+DBpQeXRob24gU29mdHdhcmUgRm91bmRhdGlvbjEYMBYGA1UECwwPcHl0aG9uLXJl\n+cXVlc3RzMRIwEAYDVQQDDAlsb2NhbGhvc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IB\n+DwAwggEKAoIBAQChEKOx377ymuDg23By5Re1DHi2RiBKSHr85/ZTZuwP/69lHN7q\n+TQEO//EMEFZ9+ZwezeJJsejjP2HO5lQZbcsWok3hbM0wVT+vApkogPvJ8WNFFWFe\n+ZBnGLi/1WM9cSZpUsDJ0XCsG0RTtO27wfgZQlKQMZxTkfi971oPYxNVSjTm2JcLT\n+kvwYIwxjJXPDTOgRo9TEAY3cWkCrBJN4w74GWBTM5KDDA230T7WwLuv81XD2LvYj\n+YYdMBGcxPr5tYTIlp3LncbcrDRNk3pbYQk0bRJgkw2vUkteiRGjkt+dgVnLc6+MI\n+W+VLXEpj+zsOZ5/R4d1pofqj9sDyDPhtNr1JAgMBAAGgeDB2BgkqhkiG9w0BCQ4x\n+aTBnMAwGA1UdEwEB/wQCMAAwDgYDVR0PAQH/BAQDAgWgMBYGA1UdJQEB/wQMMAoG\n+CCsGAQUFBwMBMC8GA1UdEQEB/wQlMCOCCWxvY2FsaG9zdIcEfwAAAYcQAAAAAAAA\n+AAAAAAAAAAAAATANBgkqhkiG9w0BAQsFAAOCAQEAFTlFTn5Mn8JXtqB5bGjuiChe\n+ClA6Y32Co4l7N0CtAlf+bExwLdpLOleTX3WnryIPALl9uBUI/67dy/STn/J1Yn86\n+jWPEFwpmYNSKgQljYWcwtBdYLWfIsJO11kKdaAkOUHBEN5DKrXJ46Vs4918bD1/Q\n+6ztqdrThiKc646u9xB58Hg7F0IyMWbHfs0x16ZpcN9otrIkbqOE2wzTmc65O1t1i\n+HDljcSk7OnNy3a9wtLEnyPiyMqHf2k/bTlmiDRVe3cSy9xieoqmzHTnOCSASe1y9\n+7lcEBQild18Jo4nACV4vCYOUwrMi/58LWW+lD6OmMnPiWUqOvMbgMffMNDpWPA==\n+-----END CERTIFICATE REQUEST-----"
    },
    {
      "sha": "d6afaf59fe445a2d66049498681d27a06c0ec800",
      "filename": "tests/certs/valid/server/server.key",
      "status": "added",
      "additions": 28,
      "deletions": 0,
      "changes": 28,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fvalid%2Fserver%2Fserver.key",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fvalid%2Fserver%2Fserver.key",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fvalid%2Fserver%2Fserver.key?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,28 @@\n+-----BEGIN PRIVATE KEY-----\n+MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQChEKOx377ymuDg\n+23By5Re1DHi2RiBKSHr85/ZTZuwP/69lHN7qTQEO//EMEFZ9+ZwezeJJsejjP2HO\n+5lQZbcsWok3hbM0wVT+vApkogPvJ8WNFFWFeZBnGLi/1WM9cSZpUsDJ0XCsG0RTt\n+O27wfgZQlKQMZxTkfi971oPYxNVSjTm2JcLTkvwYIwxjJXPDTOgRo9TEAY3cWkCr\n+BJN4w74GWBTM5KDDA230T7WwLuv81XD2LvYjYYdMBGcxPr5tYTIlp3LncbcrDRNk\n+3pbYQk0bRJgkw2vUkteiRGjkt+dgVnLc6+MIW+VLXEpj+zsOZ5/R4d1pofqj9sDy\n+DPhtNr1JAgMBAAECggEAIuLzBfXgCvXzlBjL2kMXd7p4EgkN+PEKnKmUr/t40b1Q\n+zR6sBQWBX3GeET4fseElSQHQzCQaPNCve4xltm1S4jftFREHP7sTVHHEYWLQxuy/\n+Uwkewj5927CI6ERgg82YfVP91bjaA/u5I+pt7O7rKLyNbPdN7fEMEW+FNuhpiVvg\n+JMrcK1BCFL6pmIT21LyTwkacMKZSPko58pWE24MA9aSCHk6cXdwQWQK0AfQT3XGT\n+C4I0hRed7LgqMH+gMuhpakiO13t8yTwxt2iQC9+aa4oSHD3BOi/CwIWfe1mHwmlr\n+cj4Kof1JSnK4SVTD16T++PlnWZkF6oaLUNg+/c2C9QKBgQDOFSYIY7+HzinT2hbI\n+yTIJCHpp+Iee+WVvvxjdZIPMDINrlIiHcMfXb0itUdcUO6tz0KYDMDLRC9CSP0ar\n+6mBWUTHfAKF2S4JpI9JYI4PNtIpOP1NiYuyJlnh5+ytU1yIeIvl39hmLcRwI9mgz\n+njy/D7yEoDCrG1dhcltubKpNXQKBgQDIFAVg0A7MNcxBZDLlk1NAME2JKOSszX8E\n+VNucvZD+9l+L9V9BmwwPQdzYifv/dNp3nYn+lxRPPgze3ZWu4+PeDuGudxu0I6ll\n+beFdbIcp1wbeQguzHYLjBYJqsMb4Pao5HPInjPu/HWfZlg9oZpJbKVucQwbonJLX\n+lgca9KaE3QKBgA+OUx+g/+0tZ8ThGoUvgsJhzHPBWeNrKfgEcckMdFJrw2PUg3XN\n+0pf1g4PpwJV7Z5bHcjCda8iR3r2bXydM+tapLF2L+6QlUQPEu3UBwUo+zY3Yg9/S\n+Xc6I+DEk/4FY9+9UboZaolT/RcF7cCQtVqKJeo58VRAlcTQe4L32H+jVAoGALXX3\n+Ht9HbXkP1w/YTLej4+LVy0OCag0rPiW13LBqALSkUx3GrhZ3sAPMFVuM6ad4eFNQ\n+ZouXbsXvkLgSabGYNf11o/mmTtEHjWdhHKQrNgOIqPmixOkAs2quDmXqX79LLTz5\n+fKkZDny0+wiQqa0cth/4k9HbAQGKj/ej16kdKPUCgYAz08Y39NnJYxRNz3tu/7C6\n+jKyXKxhuZCZCt3cSWto5Tg0mVVB+2Jk2GhG1hCfZoRCP25R3FFBR1HOJgOc59T7C\n+LL67FdO0+7mj/WNzHj3+9gyOYQyQgPVDaTmsJLbuzT2S+GpR94ZNliwL2NEa5baG\n+B/Nb2ruRNj0GgZVw48N4XQ==\n+-----END PRIVATE KEY-----"
    },
    {
      "sha": "0168cd3e3fbb04b5e69f1f86483077416370563c",
      "filename": "tests/certs/valid/server/server.pem",
      "status": "added",
      "additions": 47,
      "deletions": 0,
      "changes": 47,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fvalid%2Fserver%2Fserver.pem",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Fcerts%2Fvalid%2Fserver%2Fserver.pem",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Fcerts%2Fvalid%2Fserver%2Fserver.pem?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,47 @@\n+-----BEGIN CERTIFICATE-----\n+MIIEhTCCA22gAwIBAgIUTzbDp+B1umRS0Q7rgefxif9Im3wwDQYJKoZIhvcNAQEL\n+BQAwajELMAkGA1UEBhMCVVMxIzAhBgNVBAoMGlB5dGhvbiBTb2Z0d2FyZSBGb3Vu\n+ZGF0aW9uMRgwFgYDVQQLDA9weXRob24tcmVxdWVzdHMxHDAaBgNVBAMME1NlbGYt\n+U2lnbmVkIFJvb3QgQ0EwHhcNMjQwMzE0MDAxMDAzWhcNNDMxMTMwMDAxMDAzWjBt\n+MQswCQYDVQQGEwJVUzELMAkGA1UECAwCREUxIzAhBgNVBAoMGlB5dGhvbiBTb2Z0\n+d2FyZSBGb3VuZGF0aW9uMRgwFgYDVQQLDA9weXRob24tcmVxdWVzdHMxEjAQBgNV\n+BAMMCWxvY2FsaG9zdDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAKEQ\n+o7HfvvKa4ODbcHLlF7UMeLZGIEpIevzn9lNm7A//r2Uc3upNAQ7/8QwQVn35nB7N\n+4kmx6OM/Yc7mVBltyxaiTeFszTBVP68CmSiA+8nxY0UVYV5kGcYuL/VYz1xJmlSw\n+MnRcKwbRFO07bvB+BlCUpAxnFOR+L3vWg9jE1VKNObYlwtOS/BgjDGMlc8NM6BGj\n+1MQBjdxaQKsEk3jDvgZYFMzkoMMDbfRPtbAu6/zVcPYu9iNhh0wEZzE+vm1hMiWn\n+cudxtysNE2TelthCTRtEmCTDa9SS16JEaOS352BWctzr4whb5UtcSmP7Ow5nn9Hh\n+3Wmh+qP2wPIM+G02vUkCAwEAAaOCAR4wggEaMAwGA1UdEwEB/wQCMAAwDgYDVR0P\n+AQH/BAQDAgWgMBYGA1UdJQEB/wQMMAoGCCsGAQUFBwMBMC8GA1UdEQEB/wQlMCOC\n+CWxvY2FsaG9zdIcEfwAAAYcQAAAAAAAAAAAAAAAAAAAAATAdBgNVHQ4EFgQUJ90a\n+UnXKPP13yDprLhG39fUrnu8wgZEGA1UdIwSBiTCBhqFupGwwajELMAkGA1UEBhMC\n+VVMxIzAhBgNVBAoMGlB5dGhvbiBTb2Z0d2FyZSBGb3VuZGF0aW9uMRgwFgYDVQQL\n+DA9weXRob24tcmVxdWVzdHMxHDAaBgNVBAMME1NlbGYtU2lnbmVkIFJvb3QgQ0GC\n+FA9wdtNh/V99DRwYp8vXjPxSjJnWMA0GCSqGSIb3DQEBCwUAA4IBAQCVh4hiraRv\n+JzYbS/TombP//xfVEWHXDBEYsT5GgWf7GPJ/QtSvv6uJFsK7heqLzf9f+r4Z5xMh\n+YAkb0oe/Ge0T30Mo1YaBEqkKuQL9lOMcP69S9uFz2VT6I/76I8qqAu2AFhu74p8f\n+qudwmQyRYo1Ryg4R/SgRhSJKF/ST/2wOusNWSsBe1s8S2PmtOb4dr3cMBGihrUzS\n+DmCQpWjuiuE23HXnnYDc/EUAnEEPkLDgCsE9iLq37FPUHcHjqdYIAhmImPBpv2EL\n+ftXeRWfxN2hRHpS5Fn3QuAOwfJw5tUcVXojJCJfSpL+Ac97iSjxNaDIPlyomauKw\n+1rgbUkSw+9JQ\n+-----END CERTIFICATE-----\n+-----BEGIN CERTIFICATE-----\n+MIIDWzCCAkMCFA9wdtNh/V99DRwYp8vXjPxSjJnWMA0GCSqGSIb3DQEBCwUAMGox\n+CzAJBgNVBAYTAlVTMSMwIQYDVQQKDBpQeXRob24gU29mdHdhcmUgRm91bmRhdGlv\n+bjEYMBYGA1UECwwPcHl0aG9uLXJlcXVlc3RzMRwwGgYDVQQDDBNTZWxmLVNpZ25l\n+ZCBSb290IENBMB4XDTI0MDMxMjIxMDQwM1oXDTQ0MDMwNzIxMDQwM1owajELMAkG\n+A1UEBhMCVVMxIzAhBgNVBAoMGlB5dGhvbiBTb2Z0d2FyZSBGb3VuZGF0aW9uMRgw\n+FgYDVQQLDA9weXRob24tcmVxdWVzdHMxHDAaBgNVBAMME1NlbGYtU2lnbmVkIFJv\n+b3QgQ0EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDHlIhe7GLCeSk8\n+RZOKdtmyKns6KdZgGw/LcxPkYvQlu1g0zV8X0DqVr2LdMumWUTNCc9sPdSlAG+He\n+mQp2TMoWUMumMuwDtit9RT0Sb6Eh9svWgjY9ferovPJRfCWUTsA2Ug8uoh0wyEXK\n+na7X6fHt5E3B9vj0+b9a4vDibdBXV11FheLT02/uEmAEJDdP/zeBgvVbhcVyumO6\n+fAGMIWzR2ukhe8z/ma5H9zoi4gZA8nsK6reZUD8+6affnPe+jIt/AdzggtV9jkWm\n+zSpr+RHeZ0y+q4eik2ZNUGg4XcF6JsJ9yu/AqLBXxd38uLdFfgyhP2y6K628yzgy\n+e6lzFyWnAgMBAAEwDQYJKoZIhvcNAQELBQADggEBAGymNVTsKSAq8Ju6zV+AWAyV\n+GcUNBmLpgzDA0e7pkVYhHTdWKlGH4GnrRcp0nvnSbr6iq1Ob/8yEUUoRzK55Flws\n+Kt1OLwnZyhfRoSUesoEqpP68vzWEgiYv0QuIWvzNt0YfAAvEgGoc3iri44MelKLn\n+9ZMT8m91nVamA35R8ZjfeAkNp2xcz0a67V0ww6o4wSXrG7o5ZRXyjqZ/9K7SfwUJ\n+rV9RciccsjH/MzKbfrx73QwsbPWiFmjzHopdasIO0lDlmgm/r9gKfkbzfKoGCgLZ\n+6an6FlmLftLSXijf/QwtqeSP9fODeE3dzBmnTM3jdoVS53ZegUDWNl14o25v2Kg=\n+-----END CERTIFICATE-----"
    },
    {
      "sha": "6c55d5a130bcbef6aa8765e45679ec6a2fd47449",
      "filename": "tests/test_adapters.py",
      "status": "added",
      "additions": 8,
      "deletions": 0,
      "changes": 8,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Ftest_adapters.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Ftest_adapters.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Ftest_adapters.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -0,0 +1,8 @@\n+import requests.adapters\n+\n+\n+def test_request_url_trims_leading_path_separators():\n+    \"\"\"See also https://github.com/psf/requests/issues/6643.\"\"\"\n+    a = requests.adapters.HTTPAdapter()\n+    p = requests.Request(method=\"GET\", url=\"http://127.0.0.1:10000//v:h\").prepare()\n+    assert \"/v:h\" == a.request_url(p, {})"
    },
    {
      "sha": "5fca6207efa3fbcb2d15485334830502fe636ccf",
      "filename": "tests/test_help.py",
      "status": "modified",
      "additions": 8,
      "deletions": 6,
      "changes": 14,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Ftest_help.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Ftest_help.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Ftest_help.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -1,3 +1,5 @@\n+from unittest import mock\n+\n from requests.help import info\n \n \n@@ -11,15 +13,15 @@ def __init__(self, version):\n         self.__version__ = version\n \n \n-def test_idna_without_version_attribute(mocker):\n+def test_idna_without_version_attribute():\n     \"\"\"Older versions of IDNA don't provide a __version__ attribute, verify\n     that if we have such a package, we don't blow up.\n     \"\"\"\n-    mocker.patch(\"requests.help.idna\", new=None)\n-    assert info()[\"idna\"] == {\"version\": \"\"}\n+    with mock.patch(\"requests.help.idna\", new=None):\n+        assert info()[\"idna\"] == {\"version\": \"\"}\n \n \n-def test_idna_with_version_attribute(mocker):\n+def test_idna_with_version_attribute():\n     \"\"\"Verify we're actually setting idna version when it should be available.\"\"\"\n-    mocker.patch(\"requests.help.idna\", new=VersionedPackage(\"2.6\"))\n-    assert info()[\"idna\"] == {\"version\": \"2.6\"}\n+    with mock.patch(\"requests.help.idna\", new=VersionedPackage(\"2.6\")):\n+        assert info()[\"idna\"] == {\"version\": \"2.6\"}"
    },
    {
      "sha": "b4e9fe92ae46281475d8391581ceebb2ae0c564d",
      "filename": "tests/test_requests.py",
      "status": "modified",
      "additions": 206,
      "deletions": 40,
      "changes": 246,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Ftest_requests.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Ftest_requests.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Ftest_requests.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -7,7 +7,9 @@\n import os\n import pickle\n import re\n+import threading\n import warnings\n+from unittest import mock\n \n import pytest\n import urllib3\n@@ -50,6 +52,7 @@\n \n from . import SNIMissingWarning\n from .compat import StringIO\n+from .testserver.server import TLSServer, consume_socket_content\n from .utils import override_environ\n \n # Requests to this URL should always fail with a connection timeout (nothing\n@@ -75,11 +78,9 @@\n \n \n class TestRequests:\n-\n     digest_auth_algo = (\"MD5\", \"SHA-256\", \"SHA-512\")\n \n     def test_entry_points(self):\n-\n         requests.session\n         requests.session().get\n         requests.session().head\n@@ -510,7 +511,6 @@ def test_headers_preserve_order(self, httpbin):\n \n     @pytest.mark.parametrize(\"key\", (\"User-agent\", \"user-agent\"))\n     def test_user_agent_transfers(self, httpbin, key):\n-\n         heads = {key: \"Mozilla/5.0 (github.com/psf/requests)\"}\n \n         r = requests.get(httpbin(\"user-agent\"), headers=heads)\n@@ -647,25 +647,26 @@ def test_proxy_authorization_preserved_on_request(self, httpbin):\n \n         assert sent_headers.get(\"Proxy-Authorization\") == proxy_auth_value\n \n-\n     @pytest.mark.parametrize(\n         \"url,has_proxy_auth\",\n         (\n-            ('http://example.com', True),\n-            ('https://example.com', False),\n+            (\"http://example.com\", True),\n+            (\"https://example.com\", False),\n         ),\n     )\n-    def test_proxy_authorization_not_appended_to_https_request(self, url, has_proxy_auth):\n+    def test_proxy_authorization_not_appended_to_https_request(\n+        self, url, has_proxy_auth\n+    ):\n         session = requests.Session()\n         proxies = {\n-            'http': 'http://test:pass@localhost:8080',\n-            'https': 'http://test:pass@localhost:8090',\n+            \"http\": \"http://test:pass@localhost:8080\",\n+            \"https\": \"http://test:pass@localhost:8090\",\n         }\n-        req = requests.Request('GET', url)\n+        req = requests.Request(\"GET\", url)\n         prep = req.prepare()\n         session.rebuild_proxies(prep, proxies)\n \n-        assert ('Proxy-Authorization' in prep.headers) is has_proxy_auth\n+        assert (\"Proxy-Authorization\" in prep.headers) is has_proxy_auth\n \n     def test_basicauth_with_netrc(self, httpbin):\n         auth = (\"user\", \"pass\")\n@@ -703,7 +704,6 @@ def get_netrc_auth_mock(url):\n             requests.sessions.get_netrc_auth = old_auth\n \n     def test_DIGEST_HTTP_200_OK_GET(self, httpbin):\n-\n         for authtype in self.digest_auth_algo:\n             auth = HTTPDigestAuth(\"user\", \"pass\")\n             url = httpbin(\"digest-auth\", \"auth\", \"user\", \"pass\", authtype, \"never\")\n@@ -721,7 +721,6 @@ def test_DIGEST_HTTP_200_OK_GET(self, httpbin):\n             assert r.status_code == 200\n \n     def test_DIGEST_AUTH_RETURNS_COOKIE(self, httpbin):\n-\n         for authtype in self.digest_auth_algo:\n             url = httpbin(\"digest-auth\", \"auth\", \"user\", \"pass\", authtype)\n             auth = HTTPDigestAuth(\"user\", \"pass\")\n@@ -732,7 +731,6 @@ def test_DIGEST_AUTH_RETURNS_COOKIE(self, httpbin):\n             assert r.status_code == 200\n \n     def test_DIGEST_AUTH_SETS_SESSION_COOKIES(self, httpbin):\n-\n         for authtype in self.digest_auth_algo:\n             url = httpbin(\"digest-auth\", \"auth\", \"user\", \"pass\", authtype)\n             auth = HTTPDigestAuth(\"user\", \"pass\")\n@@ -741,7 +739,6 @@ def test_DIGEST_AUTH_SETS_SESSION_COOKIES(self, httpbin):\n             assert s.cookies[\"fake\"] == \"fake_value\"\n \n     def test_DIGEST_STREAM(self, httpbin):\n-\n         for authtype in self.digest_auth_algo:\n             auth = HTTPDigestAuth(\"user\", \"pass\")\n             url = httpbin(\"digest-auth\", \"auth\", \"user\", \"pass\", authtype)\n@@ -753,7 +750,6 @@ def test_DIGEST_STREAM(self, httpbin):\n             assert r.raw.read() == b\"\"\n \n     def test_DIGESTAUTH_WRONG_HTTP_401_GET(self, httpbin):\n-\n         for authtype in self.digest_auth_algo:\n             auth = HTTPDigestAuth(\"user\", \"wrongpass\")\n             url = httpbin(\"digest-auth\", \"auth\", \"user\", \"pass\", authtype)\n@@ -770,7 +766,6 @@ def test_DIGESTAUTH_WRONG_HTTP_401_GET(self, httpbin):\n             assert r.status_code == 401\n \n     def test_DIGESTAUTH_QUOTES_QOP_VALUE(self, httpbin):\n-\n         for authtype in self.digest_auth_algo:\n             auth = HTTPDigestAuth(\"user\", \"pass\")\n             url = httpbin(\"digest-auth\", \"auth\", \"user\", \"pass\", authtype)\n@@ -779,7 +774,6 @@ def test_DIGESTAUTH_QUOTES_QOP_VALUE(self, httpbin):\n             assert '\"auth\"' in r.request.headers[\"Authorization\"]\n \n     def test_POSTBIN_GET_POST_FILES(self, httpbin):\n-\n         url = httpbin(\"post\")\n         requests.post(url).raise_for_status()\n \n@@ -797,7 +791,6 @@ def test_POSTBIN_GET_POST_FILES(self, httpbin):\n             requests.post(url, files=[\"bad file data\"])\n \n     def test_invalid_files_input(self, httpbin):\n-\n         url = httpbin(\"post\")\n         post = requests.post(url, files={\"random-file-1\": None, \"random-file-2\": 1})\n         assert b'name=\"random-file-1\"' not in post.request.body\n@@ -845,7 +838,6 @@ def seek(self, offset, where=0):\n         assert post2.json()[\"data\"] == \"st\"\n \n     def test_POSTBIN_GET_POST_FILES_WITH_DATA(self, httpbin):\n-\n         url = httpbin(\"post\")\n         requests.post(url).raise_for_status()\n \n@@ -983,12 +975,12 @@ def test_invalid_ssl_certificate_files(self, httpbin_secure):\n             ),\n         ),\n     )\n-    def test_env_cert_bundles(self, httpbin, mocker, env, expected):\n+    def test_env_cert_bundles(self, httpbin, env, expected):\n         s = requests.Session()\n-        mocker.patch(\"os.environ\", env)\n-        settings = s.merge_environment_settings(\n-            url=httpbin(\"get\"), proxies={}, stream=False, verify=True, cert=None\n-        )\n+        with mock.patch(\"os.environ\", env):\n+            settings = s.merge_environment_settings(\n+                url=httpbin(\"get\"), proxies={}, stream=False, verify=True, cert=None\n+            )\n         assert settings[\"verify\"] == expected\n \n     def test_http_with_certificate(self, httpbin):\n@@ -1011,7 +1003,7 @@ def test_https_warnings(self, nosan_server):\n                 \"SubjectAltNameWarning\",\n             )\n \n-        with pytest.warns(None) as warning_records:\n+        with pytest.warns() as warning_records:\n             warnings.simplefilter(\"always\")\n             requests.get(f\"https://localhost:{port}/\", verify=ca_bundle)\n \n@@ -1034,7 +1026,6 @@ def test_certificate_failure(self, httpbin_secure):\n             requests.get(httpbin_secure(\"status\", \"200\"))\n \n     def test_urlencoded_get_query_multivalued_param(self, httpbin):\n-\n         r = requests.get(httpbin(\"get\"), params={\"test\": [\"foo\", \"baz\"]})\n         assert r.status_code == 200\n         assert r.url == httpbin(\"get?test=foo&test=baz\")\n@@ -1476,11 +1467,9 @@ def test_response_chunk_size_type(self):\n             (urllib3.exceptions.SSLError, tuple(), RequestsSSLError),\n         ),\n     )\n-    def test_iter_content_wraps_exceptions(\n-        self, httpbin, mocker, exception, args, expected\n-    ):\n+    def test_iter_content_wraps_exceptions(self, httpbin, exception, args, expected):\n         r = requests.Response()\n-        r.raw = mocker.Mock()\n+        r.raw = mock.Mock()\n         # ReadTimeoutError can't be initialized by mock\n         # so we'll manually create the instance with args\n         r.raw.stream.side_effect = exception(*args)\n@@ -1715,7 +1704,7 @@ def test_header_validation(self, httpbin):\n         }\n         r = requests.get(httpbin(\"get\"), headers=valid_headers)\n         for key in valid_headers.keys():\n-            valid_headers[key] == r.request.headers[key]\n+            assert valid_headers[key] == r.request.headers[key]\n \n     @pytest.mark.parametrize(\n         \"invalid_header, key\",\n@@ -1821,6 +1810,23 @@ def test_autoset_header_values_are_native(self, httpbin):\n \n         assert p.headers[\"Content-Length\"] == length\n \n+    def test_content_length_for_bytes_data(self, httpbin):\n+        data = \"This is a string containing multi-byte UTF-8 ☃️\"\n+        encoded_data = data.encode(\"utf-8\")\n+        length = str(len(encoded_data))\n+        req = requests.Request(\"POST\", httpbin(\"post\"), data=encoded_data)\n+        p = req.prepare()\n+\n+        assert p.headers[\"Content-Length\"] == length\n+\n+    def test_content_length_for_string_data_counts_bytes(self, httpbin):\n+        data = \"This is a string containing multi-byte UTF-8 ☃️\"\n+        length = str(len(data.encode(\"utf-8\")))\n+        req = requests.Request(\"POST\", httpbin(\"post\"), data=data)\n+        p = req.prepare()\n+\n+        assert p.headers[\"Content-Length\"] == length\n+\n     def test_nonhttp_schemes_dont_check_URLs(self):\n         test_urls = (\n             \"data:image/gif;base64,R0lGODlhAQABAHAAACH5BAUAAAAALAAAAAABAAEAAAICRAEAOw==\",\n@@ -2105,16 +2111,16 @@ def test_response_iter_lines_reentrant(self, httpbin):\n         next(r.iter_lines())\n         assert len(list(r.iter_lines())) == 3\n \n-    def test_session_close_proxy_clear(self, mocker):\n+    def test_session_close_proxy_clear(self):\n         proxies = {\n-            \"one\": mocker.Mock(),\n-            \"two\": mocker.Mock(),\n+            \"one\": mock.Mock(),\n+            \"two\": mock.Mock(),\n         }\n         session = requests.Session()\n-        mocker.patch.dict(session.adapters[\"http://\"].proxy_manager, proxies)\n-        session.close()\n-        proxies[\"one\"].clear.assert_called_once_with()\n-        proxies[\"two\"].clear.assert_called_once_with()\n+        with mock.patch.dict(session.adapters[\"http://\"].proxy_manager, proxies):\n+            session.close()\n+            proxies[\"one\"].clear.assert_called_once_with()\n+            proxies[\"two\"].clear.assert_called_once_with()\n \n     def test_proxy_auth(self):\n         adapter = HTTPAdapter()\n@@ -2715,7 +2721,7 @@ def test_preparing_bad_url(self, url):\n         with pytest.raises(requests.exceptions.InvalidURL):\n             r.prepare()\n \n-    @pytest.mark.parametrize(\"url, exception\", ((\"http://localhost:-1\", InvalidURL),))\n+    @pytest.mark.parametrize(\"url, exception\", ((\"http://:1\", InvalidURL),))\n     def test_redirecting_to_bad_url(self, httpbin, url, exception):\n         with pytest.raises(exception):\n             requests.get(httpbin(\"redirect-to\"), params={\"url\": url})\n@@ -2808,3 +2814,163 @@ def test_json_decode_persists_doc_attr(self, httpbin):\n         with pytest.raises(requests.exceptions.JSONDecodeError) as excinfo:\n             r.json()\n         assert excinfo.value.doc == r.text\n+\n+    def test_status_code_425(self):\n+        r1 = requests.codes.get(\"TOO_EARLY\")\n+        r2 = requests.codes.get(\"too_early\")\n+        r3 = requests.codes.get(\"UNORDERED\")\n+        r4 = requests.codes.get(\"unordered\")\n+        r5 = requests.codes.get(\"UNORDERED_COLLECTION\")\n+        r6 = requests.codes.get(\"unordered_collection\")\n+\n+        assert r1 == 425\n+        assert r2 == 425\n+        assert r3 == 425\n+        assert r4 == 425\n+        assert r5 == 425\n+        assert r6 == 425\n+\n+    def test_different_connection_pool_for_tls_settings_verify_True(self):\n+        def response_handler(sock):\n+            consume_socket_content(sock, timeout=0.5)\n+            sock.send(\n+                b\"HTTP/1.1 200 OK\\r\\n\"\n+                b\"Content-Length: 18\\r\\n\\r\\n\"\n+                b'\\xff\\xfe{\\x00\"\\x00K0\"\\x00=\\x00\"\\x00\\xab0\"\\x00\\r\\n'\n+            )\n+\n+        s = requests.Session()\n+        close_server = threading.Event()\n+        server = TLSServer(\n+            handler=response_handler,\n+            wait_to_close_event=close_server,\n+            requests_to_handle=3,\n+            cert_chain=\"tests/certs/expired/server/server.pem\",\n+            keyfile=\"tests/certs/expired/server/server.key\",\n+        )\n+\n+        with server as (host, port):\n+            url = f\"https://{host}:{port}\"\n+            r1 = s.get(url, verify=False)\n+            assert r1.status_code == 200\n+\n+            # Cannot verify self-signed certificate\n+            with pytest.raises(requests.exceptions.SSLError):\n+                s.get(url)\n+\n+            close_server.set()\n+        assert 2 == len(s.adapters[\"https://\"].poolmanager.pools)\n+\n+    def test_different_connection_pool_for_tls_settings_verify_bundle_expired_cert(\n+        self,\n+    ):\n+        def response_handler(sock):\n+            consume_socket_content(sock, timeout=0.5)\n+            sock.send(\n+                b\"HTTP/1.1 200 OK\\r\\n\"\n+                b\"Content-Length: 18\\r\\n\\r\\n\"\n+                b'\\xff\\xfe{\\x00\"\\x00K0\"\\x00=\\x00\"\\x00\\xab0\"\\x00\\r\\n'\n+            )\n+\n+        s = requests.Session()\n+        close_server = threading.Event()\n+        server = TLSServer(\n+            handler=response_handler,\n+            wait_to_close_event=close_server,\n+            requests_to_handle=3,\n+            cert_chain=\"tests/certs/expired/server/server.pem\",\n+            keyfile=\"tests/certs/expired/server/server.key\",\n+        )\n+\n+        with server as (host, port):\n+            url = f\"https://{host}:{port}\"\n+            r1 = s.get(url, verify=False)\n+            assert r1.status_code == 200\n+\n+            # Has right trust bundle, but certificate expired\n+            with pytest.raises(requests.exceptions.SSLError):\n+                s.get(url, verify=\"tests/certs/expired/ca/ca.crt\")\n+\n+            close_server.set()\n+        assert 2 == len(s.adapters[\"https://\"].poolmanager.pools)\n+\n+    def test_different_connection_pool_for_tls_settings_verify_bundle_unexpired_cert(\n+        self,\n+    ):\n+        def response_handler(sock):\n+            consume_socket_content(sock, timeout=0.5)\n+            sock.send(\n+                b\"HTTP/1.1 200 OK\\r\\n\"\n+                b\"Content-Length: 18\\r\\n\\r\\n\"\n+                b'\\xff\\xfe{\\x00\"\\x00K0\"\\x00=\\x00\"\\x00\\xab0\"\\x00\\r\\n'\n+            )\n+\n+        s = requests.Session()\n+        close_server = threading.Event()\n+        server = TLSServer(\n+            handler=response_handler,\n+            wait_to_close_event=close_server,\n+            requests_to_handle=3,\n+            cert_chain=\"tests/certs/valid/server/server.pem\",\n+            keyfile=\"tests/certs/valid/server/server.key\",\n+        )\n+\n+        with server as (host, port):\n+            url = f\"https://{host}:{port}\"\n+            r1 = s.get(url, verify=False)\n+            assert r1.status_code == 200\n+\n+            r2 = s.get(url, verify=\"tests/certs/valid/ca/ca.crt\")\n+            assert r2.status_code == 200\n+\n+            close_server.set()\n+        assert 2 == len(s.adapters[\"https://\"].poolmanager.pools)\n+\n+    def test_different_connection_pool_for_mtls_settings(self):\n+        client_cert = None\n+\n+        def response_handler(sock):\n+            nonlocal client_cert\n+            client_cert = sock.getpeercert()\n+            consume_socket_content(sock, timeout=0.5)\n+            sock.send(\n+                b\"HTTP/1.1 200 OK\\r\\n\"\n+                b\"Content-Length: 18\\r\\n\\r\\n\"\n+                b'\\xff\\xfe{\\x00\"\\x00K0\"\\x00=\\x00\"\\x00\\xab0\"\\x00\\r\\n'\n+            )\n+\n+        s = requests.Session()\n+        close_server = threading.Event()\n+        server = TLSServer(\n+            handler=response_handler,\n+            wait_to_close_event=close_server,\n+            requests_to_handle=2,\n+            cert_chain=\"tests/certs/expired/server/server.pem\",\n+            keyfile=\"tests/certs/expired/server/server.key\",\n+            mutual_tls=True,\n+            cacert=\"tests/certs/expired/ca/ca.crt\",\n+        )\n+\n+        cert = (\n+            \"tests/certs/mtls/client/client.pem\",\n+            \"tests/certs/mtls/client/client.key\",\n+        )\n+        with server as (host, port):\n+            url = f\"https://{host}:{port}\"\n+            r1 = s.get(url, verify=False, cert=cert)\n+            assert r1.status_code == 200\n+            with pytest.raises(requests.exceptions.SSLError):\n+                s.get(url, cert=cert)\n+            close_server.set()\n+\n+        assert client_cert is not None\n+\n+\n+def test_json_decode_errors_are_serializable_deserializable():\n+    json_decode_error = requests.exceptions.JSONDecodeError(\n+        \"Extra data\",\n+        '{\"responseCode\":[\"706\"],\"data\":null}{\"responseCode\":[\"706\"],\"data\":null}',\n+        36,\n+    )\n+    deserialized_error = pickle.loads(pickle.dumps(json_decode_error))\n+    assert repr(json_decode_error) == repr(deserialized_error)"
    },
    {
      "sha": "5e9b56ea644e7855cc1bf7eea4acc0575b8a5d76",
      "filename": "tests/test_utils.py",
      "status": "modified",
      "additions": 37,
      "deletions": 4,
      "changes": 41,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Ftest_utils.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Ftest_utils.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Ftest_utils.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -5,6 +5,7 @@\n import zipfile\n from collections import deque\n from io import BytesIO\n+from unittest import mock\n \n import pytest\n \n@@ -751,13 +752,13 @@ def test_should_bypass_proxies(url, expected, monkeypatch):\n         (\"http://user:pass@hostname:5000\", \"hostname\"),\n     ),\n )\n-def test_should_bypass_proxies_pass_only_hostname(url, expected, mocker):\n+def test_should_bypass_proxies_pass_only_hostname(url, expected):\n     \"\"\"The proxy_bypass function should be called with a hostname or IP without\n     a port number or auth credentials.\n     \"\"\"\n-    proxy_bypass = mocker.patch(\"requests.utils.proxy_bypass\")\n-    should_bypass_proxies(url, no_proxy=None)\n-    proxy_bypass.assert_called_once_with(expected)\n+    with mock.patch(\"requests.utils.proxy_bypass\") as proxy_bypass:\n+        should_bypass_proxies(url, no_proxy=None)\n+        proxy_bypass.assert_called_once_with(expected)\n \n \n @pytest.mark.parametrize(\n@@ -923,3 +924,35 @@ def test_set_environ_raises_exception():\n             raise Exception(\"Expected exception\")\n \n     assert \"Expected exception\" in str(exception.value)\n+\n+\n+@pytest.mark.skipif(os.name != \"nt\", reason=\"Test only on Windows\")\n+def test_should_bypass_proxies_win_registry_ProxyOverride_value(monkeypatch):\n+    \"\"\"Tests for function should_bypass_proxies to check if proxy\n+    can be bypassed or not with Windows ProxyOverride registry value ending with a semicolon.\n+    \"\"\"\n+    import winreg\n+\n+    class RegHandle:\n+        def Close(self):\n+            pass\n+\n+    ie_settings = RegHandle()\n+\n+    def OpenKey(key, subkey):\n+        return ie_settings\n+\n+    def QueryValueEx(key, value_name):\n+        if key is ie_settings:\n+            if value_name == \"ProxyEnable\":\n+                return [1]\n+            elif value_name == \"ProxyOverride\":\n+                return [\n+                    \"192.168.*;127.0.0.1;localhost.localdomain;172.16.1.1;<-loopback>;\"\n+                ]\n+\n+    monkeypatch.setenv(\"NO_PROXY\", \"\")\n+    monkeypatch.setenv(\"no_proxy\", \"\")\n+    monkeypatch.setattr(winreg, \"OpenKey\", OpenKey)\n+    monkeypatch.setattr(winreg, \"QueryValueEx\", QueryValueEx)\n+    assert should_bypass_proxies(\"http://example.com/\", None) is False"
    },
    {
      "sha": "da1b65608e34cbb3b4dcdf45a865a8e3b305abc7",
      "filename": "tests/testserver/server.py",
      "status": "modified",
      "additions": 42,
      "deletions": 0,
      "changes": 42,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Ftestserver%2Fserver.py",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tests%2Ftestserver%2Fserver.py",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tests%2Ftestserver%2Fserver.py?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -1,5 +1,6 @@\n import select\n import socket\n+import ssl\n import threading\n \n \n@@ -132,3 +133,44 @@ def __exit__(self, exc_type, exc_value, traceback):\n         self._close_server_sock_ignore_errors()\n         self.join()\n         return False  # allow exceptions to propagate\n+\n+\n+class TLSServer(Server):\n+    def __init__(\n+        self,\n+        *,\n+        handler=None,\n+        host=\"localhost\",\n+        port=0,\n+        requests_to_handle=1,\n+        wait_to_close_event=None,\n+        cert_chain=None,\n+        keyfile=None,\n+        mutual_tls=False,\n+        cacert=None,\n+    ):\n+        super().__init__(\n+            handler=handler,\n+            host=host,\n+            port=port,\n+            requests_to_handle=requests_to_handle,\n+            wait_to_close_event=wait_to_close_event,\n+        )\n+        self.cert_chain = cert_chain\n+        self.keyfile = keyfile\n+        self.ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)\n+        self.ssl_context.load_cert_chain(self.cert_chain, keyfile=self.keyfile)\n+        self.mutual_tls = mutual_tls\n+        self.cacert = cacert\n+        if mutual_tls:\n+            # For simplicity, we're going to assume that the client cert is\n+            # issued by the same CA as our Server certificate\n+            self.ssl_context.verify_mode = ssl.CERT_OPTIONAL\n+            self.ssl_context.load_verify_locations(self.cacert)\n+\n+    def _create_socket_and_bind(self):\n+        sock = socket.socket()\n+        sock = self.ssl_context.wrap_socket(sock, server_side=True)\n+        sock.bind((self.host, self.port))\n+        sock.listen()\n+        return sock"
    },
    {
      "sha": "c438ef316a860794bb8df4d374f943ce577ef5f4",
      "filename": "tox.ini",
      "status": "modified",
      "additions": 2,
      "deletions": 2,
      "changes": 4,
      "blob_url": "https://github.com/psf/requests/blob/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tox.ini",
      "raw_url": "https://github.com/psf/requests/raw/d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f/tox.ini",
      "contents_url": "https://api.github.com/repos/psf/requests/contents/tox.ini?ref=d6ebc4a2f1f68b7e355fb7e4dd5ffc0845547f9f",
      "patch": "@@ -1,13 +1,13 @@\n [tox]\n-envlist = py{37,38,39,310,311}-{default, use_chardet_on_py3}\n+envlist = py{38,39,310,311,312}-{default, use_chardet_on_py3}\n \n [testenv]\n deps = -rrequirements-dev.txt\n extras =\n     security\n     socks\n commands =\n-    pytest tests\n+    pytest {posargs:tests}\n \n [testenv:default]\n "
    }
  ]
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
