---
source: "https://github.blog/changelog/2026-09-10-control-github-actions-cache-access-with-cache-mode"
title: "Control GitHub Actions cache access with cache-mode"
author: "Allison"
date_published: "2026-09-10"
date_clipped: "2026-09-10"
category: "DevOps & CI/CD"
source_type: "rss"
---

# Control GitHub Actions cache access with cache-mode

Source: https://github.blog/changelog/2026-09-10-control-github-actions-cache-access-with-cache-mode

Back to changelog
Improvement
September 10, 2026 •
1 minute read
Control GitHub Actions cache access with cache-mode
You can now use cache-mode to apply least-privilege access to the GitHub Actions cache at the workflow or job level. By granting each workflow or job only the cache access it needs, you can prevent unnecessary restores or saves and help protect trusted workflows from cache poisoning. This capability is now generally available on all plans.
Choose the access each workflow or job needs:
read allows cache restores but prevents cache saves. This is the default for low-trust events such as pull_request_target .
write allows cache restores and saves. This is the default for trusted events such as push .
write-only allows cache saves but prevents cache restores.
none prevents all cache access.
Job-level settings override workflow-level settings. The selected mode is enforced by the cache service and carries through reusable workflows, where a called workflow cannot receive more cache access than its caller granted.
An explicitly declared cache-mode also overrides the read-only cache default for low-trust events such as pull_request_target . Declaring write or write-only for these events can increase the risk of cache poisoning, so GitHub Actions adds a warning annotation when the declared mode grants write access. Workflows that do not set cache-mode continue to use the existing secure defaults.
Cache mode is generally available on github.com for all GitHub plans. For configuration details, see the cache-mode workflow syntax documentation .
Join the discussion within GitHub Community
actions
application security
supply chain security
Share
Copied
Shared
Back to changelog
