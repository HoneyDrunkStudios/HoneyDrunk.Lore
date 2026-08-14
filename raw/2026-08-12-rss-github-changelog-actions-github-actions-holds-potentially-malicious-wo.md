---
source: "https://github.blog/changelog/2026-07-28-github-actions-holds-potentially-malicious-workflows-for-approval"
title: "GitHub Actions holds potentially malicious workflows for approval"
author: "GitHub Changelog Actions"
date_published: "2026-07-28"
date_clipped: "2026-08-12"
category: "DevOps & CI/CD"
source_type: "rss"
---

# GitHub Actions holds potentially malicious workflows for approval

Source: https://github.blog/changelog/2026-07-28-github-actions-holds-potentially-malicious-workflows-for-approval

Back to changelog
Improvement
July 28, 2026 •
1 minute read
GitHub Actions holds potentially malicious workflows for approval
Recent supply chain attacks use compromised GitHub credentials to push malicious GitHub Actions workflows that steal CI/CD credentials and carry out additional attacks. To help protect public repositories from these attacks, GitHub Actions now holds certain workflow runs for approval before they start.
When a workflow run is identified as potentially malicious and held, the workflow won’t execute until a repository collaborator with write access reviews and approves it. The approval must be submitted through an authenticated web session. Once approved, the workflow continues normally.
You don’t need to configure this protection; GitHub applies it automatically.
This protection currently applies to public repositories on github.com only. GitHub Enterprise Server doesn’t add this protection at this time.
actions
supply chain security
Share
Copied
Shared
Back to changelog
