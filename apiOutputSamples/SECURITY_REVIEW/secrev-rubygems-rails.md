---
intent: SECURITY_REVIEW
slug: secrev-rubygems-rails
status: pending_review
captured_at: 2026-10-04T18:40:29Z
request_url: https://rubygems.org/api/v2/rubygems/rails/versions/5.0.0.json
content_type: application/json
inputs: |
  rails 5.0.0
intent_description: |
  Scans codebase dependencies, API endpoints, and configuration files for common CVEs, secrets leakage, and misconfigurations.
answer_requirement: |
  Must list known security vulnerabilities for the package/version asked.
capture_note: |
  partial; pair with OSV id for same package
reviewer_note: "re-review after heuristic fix"
reviewed_at: ""
---

## Raw API output

```json
{
  "name": "rails",
  "downloads": 796185143,
  "version": "5.0.0",
  "version_created_at": "2016-06-30T21:32:45.255Z",
  "version_downloads": 1057069,
  "platform": "ruby",
  "ruby_abi": null,
  "authors": "David Heinemeier Hansson",
  "info": "Ruby on Rails is a full-stack web framework optimized for programmer happiness and sustainable productivity. It encourages beautiful code by favoring convention over configuration.",
  "licenses": [
    "MIT"
  ],
  "metadata": {},
  "yanked": false,
  "sha": "2e7be2dd453d6ccd7561cc21c5d60a4042f7b3455325f1d9e8dc3d7f79e2d5ef",
  "spec_sha": "071f74d80df571b41354c393158d9fbcc813af1e3ae9bc14604ab0aa999a23c5",
  "project_uri": "https://rubygems.org/gems/rails",
  "gem_uri": "https://rubygems.org/gems/rails-5.0.0.gem",
  "homepage_uri": "https://rubyonrails.org",
  "wiki_uri": "",
  "documentation_uri": "http://api.rubyonrails.org",
  "mailing_list_uri": "http://groups.google.com/group/rubyonrails-talk",
  "source_code_uri": "http://github.com/rails/rails",
  "bug_tracker_uri": "http://github.com/rails/rails/issues",
  "changelog_uri": null,
  "funding_uri": null,
  "dependencies": {
    "development": [],
    "runtime": [
      {
        "name": "actioncable",
        "requirements": "= 5.0.0"
      },
      {
        "name": "actionmailer",
        "requirements": "= 5.0.0"
      },
      {
        "name": "actionpack",
        "requirements": "= 5.0.0"
      },
      {
        "name": "actionview",
        "requirements": "= 5.0.0"
      },
      {
        "name": "activejob",
        "requirements": "= 5.0.0"
      },
      {
        "name": "activemodel",
        "requirements": "= 5.0.0"
      },
      {
        "name": "activerecord",
        "requirements": "= 5.0.0"
      },
      {
        "name": "activesupport",
        "requirements": "= 5.0.0"
      },
      {
        "name": "bundler",
        "requirements": "< 2.0, >= 1.3.0"
      },
      {
        "name": "railties",
        "requirements": "= 5.0.0"
      },
      {
        "name": "sprockets-rails",
        "requirements": ">= 2.0.0"
      }
    ]
  },
  "built_at": "2016-06-30T00:00:00.000Z",
  "created_at": "2016-06-30T21:32:45.255Z",
  "description": "Ruby on Rails is a full-stack web framework optimized for programmer happiness and sustainable productivity. It encourages beautiful code by favoring convention over configuration.",
  "downloads_count": 1057069,
  "number": "5.0.0",
  "summary": "Full-stack web application framework.",
  "rubygems_version": ">= 1.8.11",
  "ruby_version": ">= 2.2.2",
  "prerelease": false,
  "requirements": []
}
```

## Why this matches (or not)

_Pending your manual review. Approve only if this output clearly answers the intent
description — format does not matter (LLM normalizes on Usman's side)._
