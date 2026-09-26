---
source: "https://platformengineering.org/blog/cutting-ci-pipeline-time-by-64-what-actually-works-in-production"
title: "Cutting CI pipeline time by 64%: What actually works in production"
author: "Serhii Yakovenko"
date_published: "2026-09-22"
date_clipped: "2026-09-24"
category: "DevOps & CI/CD"
source_type: "rss"
capture_method: "attributed-summary"
discovered_via: "https://tldr.tech/devops/2026-09-23"
---

# Cutting CI pipeline time by 64%: What actually works in production

Attributed summary of the fetched article.

Serhii Yakovenko reports reducing a merge-train pipeline from about an hour to twenty-two minutes while improving reliability. Infrastructure experiments used ten sequential runs per configuration and considered variance alongside average duration. Browser-dependent tests and service tests were separated to avoid unnecessary Chrome containers.

Other changes batched telemetry queries, cached lint results, and skipped work for selected documentation changes. Repeated failures and an LLM-assisted review identified potentially flaky tests; quarantine included evidence but initially misclassified some cases.

HoneyDrunk application: measure queue delay, runtime distribution, retry frequency, and runner costs separately, then change one major variable at a time. Quarantine needs ownership and follow-up so an apparent reliability gain does not conceal regressions. Reported savings come from one organization's 2025–2026 workload and are not transferable estimates for HoneyDrunk.

Source: [Original article](https://platformengineering.org/blog/cutting-ci-pipeline-time-by-64-what-actually-works-in-production).
