---
source: "https://github.blog/changelog/2026-06-26-read-only-actions-cache-for-untrusted-triggers"
title: "Read-only Actions cache for untrusted triggers - GitHub Changelog"
author: "GitHub Changelog"
date_published: "2026-06-26"
date_clipped: "2026-07-03"
category: "DevOps & CI/CD"
source_type: "web"
---

# Read-only Actions cache for untrusted triggers - GitHub Changelog

Source: https://github.blog/changelog/2026-06-26-read-only-actions-cache-for-untrusted-triggers

Back to changelog
GitHub Actions now issues
read-only
cache tokens to the default branch for workflow events that can be triggered without write permissions to the repository. This applies least privilege to the cache and prevents common privilege-escalation paths through cache poisoning.
Previously, the Actions service issued read-write cache tokens for every workflow event, including triggers like
pull_request_target
,
issue_comment
, and fork-pull-request
workflow_run
cascades. Workflow code that an external actor can influence (e.g., through script injection or “pwn requests”) could write to the default-branch cache, and a trusted workflow such as
push
or
schedule
would later restore those poisoned entries. This opened up a path to run arbitrary code and exfiltrate production secrets in these more trusted workflows.
To close that path, GitHub now issues a read-only cache token when both of these are true:
The triggering event is untrusted, meaning someone other than a repository collaborator can trigger the event.
The workflow execution context and cache scope come from the shared default-branch SHA.
The most common workflow triggers that write to the default-branch cache keep full read-write caching. These triggers are
push
,
schedule
,
workflow_dispatch
,
repository_dispatch
,
delete
,
registry_package
, and
page_build
. Additionally, any trigger that uses a non-default-branch scope, such as
pull_request
and
release
, keeps read-write caching permission.
Who’s affected
This change regresses caching for a small set of untrusted workflows that write to the cache from a default-branch-SHA context. When a write is restricted,
actions/cache
logs a warning in the run and the job continues without saving. Restores are unaffected.
To keep the benefit of caching in these workflows, you will need to have a separate workflow triggered by an event with read-write cache access such as
push
which does cache saves. This will enable following workflows with read-only cache access to restore and use the cache.
This change ships to both github.com and GitHub with Data Residency. Check the
GitHub Actions cache documentation
to learn more, and join the discussion in
GitHub Community
.
Related Posts
Jun.30
Release
Open source license compliance is in public preview
supply chain security
Jun.30
Improvement
Dependabot no longer infers .npmrc
supply chain security
Jun.30
Improvement
Upcoming cloud data retention policy for closed security alerts
application security
supply chain security
Jun.25
Release
More control over your GitHub-hosted runners
actions
Jun.25
Improvement
Actions steps can now be run in parallel
actions
Jun.25
Improvement
npm adds preventive account protection for high-impact accounts
supply chain security
Jun.25
Release
Red Hat Enterprise Linux runner images are now in public preview
actions
Jun.23
Retired
Deprecation of Python 3.9 for Dependabot
supply chain security
Jun.18
Improvement
Actions: Build custom images from custom images
actions
Subscribe to our developer newsletter
Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.
Back to top
