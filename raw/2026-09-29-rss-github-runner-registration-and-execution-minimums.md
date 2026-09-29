---
source: "https://github.blog/changelog/2026-09-28-self-hosted-runner-version-enforcement-date-has-moved/"
title: "Self-hosted runner version enforcement date has moved"
author: "Allison"
date_published: "2026-09-28"
date_clipped: "2026-09-29"
category: "DevOps & CI/CD"
source_type: "rss"
capture_format: "attributed-summary"
---

# Source capture

Capture: attributed summary of the fetched written article; not a full-text reproduction.

GitHub moves full minimum-runner-version enforcement for Enterprise Cloud to September 29, 2026. The announcement distinguishes two thresholds: versions below 2.329.0 cannot register or register again, while executing jobs requires a higher minimum version. An already registered runner can therefore become unable to execute workflows.

GitHub points administrators to its runner-version-deprecation REST API for checking registration and runtime deadlines and automating fleet alerts. Enterprise Server is outside this change; the Data Residency variant had already begun enforcement in July.

For HoneyDrunk, inventory the actual hosting product and runner versions before treating this as an immediate migration requirement. A health check that verifies registration alone cannot establish execution eligibility. The announcement does not state the higher job-execution minimum, so obtain that value from the referenced API or current documentation rather than inferring it from 2.329.0.

Source: [Original article](https://github.blog/changelog/2026-09-28-self-hosted-runner-version-enforcement-date-has-moved/).
