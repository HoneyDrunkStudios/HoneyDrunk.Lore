---
source: "https://github.blog/changelog/2026-05-07-github-actions-concurrency-groups-now-allow-larger-queues"
title: "GitHub Actions concurrency groups now allow larger queues"
author: "GitHub Changelog Actions"
date_published: "Fri, 08 May 2026 00:44:18 +0000"
date_clipped: "2026-05-16"
category: "DevOps & CI/CD"
source_type: "rss"
---

# GitHub Actions concurrency groups now allow larger queues

Source: https://github.blog/changelog/2026-05-07-github-actions-concurrency-groups-now-allow-larger-queues

Back to changelog 
Improvement 
May 7, 2026 •
1 minute read 
GitHub Actions concurrency groups now allow larger queues 
You can now allow multiple jobs or workflow runs to wait in the same GitHub Actions concurrency group instead of being limited to a single pending run.
Previously, a concurrency group could have one run in progress and one pending run. If another run entered the group, the pending run was canceled and replaced. Now, you can configure concurrency groups to queue multiple pending runs and process them sequentially, with support for up to 100 queued jobs or workflow runs per concurrency group.
This makes it easier to manage deployments and other workflows that need to run in order against a shared environment or resource. Increased queuing can be enabled by adding queue: max to the concurrency block in YAML when cancel-in-progress is false or not set.
For more information, see the GitHub Actions documentation on controlling the concurrency of workflows and jobs .
actions 
Share 
Copied 
Shared 
Back to changelog
