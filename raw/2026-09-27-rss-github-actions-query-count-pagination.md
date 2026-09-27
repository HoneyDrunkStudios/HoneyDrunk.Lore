---
source: "https://github.blog/changelog/2026-09-25-changes-to-query-results-in-the-github-actions-api-and-ui/"
title: "Changes to query results in the GitHub Actions API and UI"
author: "Allison"
date_published: "2026-09-25"
date_clipped: "2026-09-27"
category: "DevOps & CI/CD"
source_type: "rss"
capture_format: "attributed-summary"
---

# Changes to query results in the GitHub Actions API and UI

Source: [Changes to query results in the GitHub Actions API and UI](https://github.blog/changelog/2026-09-25-changes-to-query-results-in-the-github-actions-api-and-ui/)

Capture note: Original summary of the fetched article; full text is not reproduced.

GitHub changed filtered workflow-run counts in its API and interface. When matches exceed 2,500, the displayed count becomes a lower-bound indicator rather than an attempted exact total. The stated reason is that expensive counting queries could time out and produce misleading partial counts.

The announcement separately retains pagination of up to 1,000 returned items. A large count therefore does not mean all matching runs can be enumerated through one query. GitHub recommends narrower filters, such as date ranges, for integrations needing a larger history.

HoneyDrunk relevance: audit activity collectors for assumptions that counts are exact or that one filtered query is exhaustive. Partition retrieval windows and reconcile collected run identifiers before calculating historical completeness.

Evidence posture: official behavior-change notice dated September 25; no live API integration test was performed.
