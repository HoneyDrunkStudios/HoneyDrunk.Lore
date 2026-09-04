---
source: "https://github.blog/changelog/2026-09-03-github-actions-early-september-2026-updates"
title: "GitHub Actions: Early September 2026 updates"
author: "Allison"
date_published: "2026-09-03"
date_clipped: "2026-09-04"
category: "DevOps & CI/CD"
source_type: "rss"
---

# GitHub Actions: Early September 2026 updates

Source: https://github.blog/changelog/2026-09-03-github-actions-early-september-2026-updates

Back to changelog
Improvement
September 3, 2026 •
1 minute read
GitHub Actions: Early September 2026 updates
Table of Contents
New REST API for runner version deprecations
New vulnerability-alerts permission for GITHUB_TOKEN
New job context properties for reusable workflows
Menu. Currently selected: New REST API for runner version deprecations
New REST API for runner version deprecations
New vulnerability-alerts permission for GITHUB_TOKEN
New job context properties for reusable workflows
GitHub Actions now includes three updates that give you clearer visibility and finer-grained control over your workflows.
New REST API for runner version deprecations
A new REST API returns when registration and runtime support end for a given runner version, so you can plan runner upgrades before a version is deprecated. Call GET /actions/runners/deprecations/{version} at the repository, organization, or enterprise level. The response includes runner_version , runtime_deprecates_at , and registration_deprecates_at .
New vulnerability-alerts permission for GITHUB_TOKEN
You can now grant workflows read-only access to Dependabot alerts with the new vulnerability-alerts permission for GITHUB_TOKEN . This permission supports read and none values, which lets you follow least-privilege practices instead of relying on broader scopes. For more information, check the permissions key in the workflow syntax .
New job context properties for reusable workflows
Reusable workflows can now determine their own source identity at runtime with four new job context properties:
job.workflow_ref : The full ref of the workflow file that defines the current job.
job.workflow_sha : The commit SHA of the workflow file.
job.workflow_repository : The owner/repo of the workflow file.
job.workflow_file_path : The file path relative to the repository root.
Unlike the existing github.workflow_ref and github.workflow_sha properties, these job context values reflect the workflow that defines the current job. For a job defined directly in a workflow, job.workflow_ref matches github.workflow_ref ; they diverge only for reusable workflows. These properties are not available on GitHub Enterprise Server.
To learn more, check the job context documentation .
Table of Contents
New REST API for runner version deprecations
New vulnerability-alerts permission for GITHUB_TOKEN
New job context properties for reusable workflows
Menu. Currently selected: New REST API for runner version deprecations
New REST API for runner version deprecations
New vulnerability-alerts permission for GITHUB_TOKEN
New job context properties for reusable workflows
actions
Share
Copied
Shared
Back to changelog
