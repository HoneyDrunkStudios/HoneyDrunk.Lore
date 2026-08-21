---
source: "https://github.blog/changelog/2026-08-20-separate-github-actions-path-for-github-code-quality"
title: "Separate GitHub Actions path for GitHub Code Quality"
author: "unknown"
date_published: "2026-08-20"
date_clipped: "2026-08-21"
category: "DevOps & CI/CD"
source_type: "rss"
---

# Separate GitHub Actions path for GitHub Code Quality

Source: https://github.blog/changelog/2026-08-20-separate-github-actions-path-for-github-code-quality

Back to changelog
Improvement
August 20, 2026 •
1 minute read
Separate GitHub Actions path for GitHub Code Quality
A dedicated workflow path for code quality CodeQL actions workflows is now generally available. Your workflow run history and your Actions usage reports now tell GitHub Code Quality runs apart from GitHub code scanning runs. Code Quality analysis runs on dynamic/github-code-quality/codeql and shows github-code-quality as the actor, instead of sharing the dynamic/github-code-scanning/codeql path and the github-advanced-security actor with code scanning.
What you need to do
Code Quality itself doesn’t need reconfiguration, and your enabled repositories keep scanning as they are. If you’ve built anything on the old path or actor, you need to update it:
Change Actions usage and billing reports that filter on dynamic/github-code-scanning/codeql so they also account for dynamic/github-code-quality/codeql .
Update scripts, dashboards, or workflow run filters that identify Code Quality runs by the github-advanced-security actor.
GitHub Code Quality is available on GitHub Enterprise Cloud and GitHub Team, as well as on GitHub Enterprise Cloud with data residency. To learn more, see GitHub Code Quality billing .
Join the discussion within GitHub Community .
actions
application security
Share
Copied
Shared
Back to changelog
