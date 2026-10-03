---
source: "https://github.blog/changelog/2026-10-01-actions-retention-now-covers-checks-runs-and-statuses"
title: "Actions retention now covers checks, runs, and statuses"
author: "Allison"
date_published: "2026-10-01"
date_clipped: "2026-10-02"
category: "DevOps & CI/CD"
source_type: "rss"
---

# Actions retention now covers checks, runs, and statuses

# Actions retention now covers checks, runs, and statuses

As [previously announced](https://github.blog/changelog/2026-08-27-actions-retention-will-cover-checks-workflow-runs-and-statuses/), checks, workflow runs, and statuses are now governed by the same GitHub Actions retention setting that controls how long artifacts and logs are kept.

These records are automatically cleaned up when they exceed the retention period configured for your enterprise, organization, or repository. This applies to checks and statuses created by GitHub Actions and third-party applications.

The setting is labeled “Check, workflow run, status, artifact and log retention” in the UI. Repository retention remains subject to organization and enterprise caps, and the maximum retention for public repositories is 90 days. Changing the setting won’t restore data that was previously removed.

Review or update the [artifact and log retention period for your repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#setting-the-artifact-and-log-retention-period-for-a-repository). The expanded retention policy applies to GitHub Actions on github.com.
