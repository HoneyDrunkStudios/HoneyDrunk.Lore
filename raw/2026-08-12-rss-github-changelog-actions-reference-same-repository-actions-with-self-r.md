---
source: "https://github.blog/changelog/2026-07-30-reference-same-repository-actions-with-self-repository-syntax"
title: "Reference same-repository actions with self-repository syntax"
author: "GitHub Changelog Actions"
date_published: "2026-07-30"
date_clipped: "2026-08-12"
category: "DevOps & CI/CD"
source_type: "rss"
---

# Reference same-repository actions with self-repository syntax

Source: https://github.blog/changelog/2026-07-30-reference-same-repository-actions-with-self-repository-syntax

Back to changelog
Release
July 30, 2026 •
1 minute read
Reference same-repository actions with self-repository syntax
You can now reference an action or reusable workflow that lives in the same repository using the new self-repository syntax. A uses: value that starts with $/ resolves to your workflow’s own repository at the exact commit that is running, with no checkout required. It works everywhere the workspace-relative ./ syntax works, including workflow steps, composite action steps, nested composition, and reusable workflow calls.
Before this, referencing an action defined in your own repository meant either relying on ./ and a checkout, or hardcoding a version. This was a maintenance burden and quietly defeated commit SHA pinning. With self-repository references, sibling actions and workflows automatically match the ref you are already running, so your internal references stay consistent even when callers pin to a full-length commit SHA. This also makes it possible to adopt the enterprise policy that requires actions to be pinned to a full-length commit SHA for workflows that call their own actions.
Self-repository references are now the recommended way to compose actions and reusable workflows within a repository. They are available on github.com. This feature requires the GitHub Actions runner to be on version 2.336.0 or newer.
Learn more by checking out our docs about finding and customizing actions , or join the discussion within GitHub Community .
actions
Share
Copied
Shared
Back to changelog
