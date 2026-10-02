---
source: "https://www.uber.com/us/en/blog/protecting-against-retry-storms"
title: "How Uber Protects Against Retry Storms"
author: "unknown"
date_published: "2026-09-30"
date_clipped: "2026-09-30"
category: "Software Architecture"
source_type: "rss"
capture_format: "attributed-summary"
---

# Source capture

Capture: attributed summary of the fetched written article; not a full-text reproduction.

Uber describes propagating error ownership through its service mesh to stop upstream retries from multiplying load on a failing dependency. Retry budgets still amplify across deep call chains; locating the originating error constrains retries to the useful edge. The design addresses coincidental failures, missing context, and paths without configured retries through dependency analysis and an at-least-once-retry flag. Uber reports avoiding millions of spurious requests during an incident. For HoneyDrunk, evaluate retry behavior across the entire call graph, including correlated overload and lost metadata. The reported availability calculations assume independent failures, an assumption the article explicitly limits.

Source: [Original article](https://www.uber.com/us/en/blog/protecting-against-retry-storms).
