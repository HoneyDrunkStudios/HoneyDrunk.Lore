---
source: "https://github.blog/changelog/2026-05-26-filter-secret-scanning-approval-requests-by-sort-order-and-bypass-status"
title: "Filter secret scanning approval requests by sort order and bypass status"
author: "GitHub Changelog"
date_published: "2026-05-26"
date_clipped: "2026-05-30"
category: "Security & Ethical Hacking"
source_type: "web"
---

# Filter secret scanning approval requests by sort order and bypass status

Source: https://github.blog/changelog/2026-05-26-filter-secret-scanning-approval-requests-by-sort-order-and-bypass-status

Back to changelog 
Improvement 
May 26, 2026 •
2 minute read 
Filter secret scanning approval requests by sort order and bypass status 
Table of Contents 
What's changing 
Sort bypass and dismissal requests 
New is_bypassed REST API filter 
Learn more 
Menu. Currently selected: What's changing 
What's changing 
Sort bypass and dismissal requests 
New is_bypassed REST API filter 
Learn more 
This week, we’re rolling out two improvements to our delegated workflows for secret scanning.
What’s changing 
Sort bypass and dismissal requests in the UI: You can now choose between ascending and descending order for approval request lists in the UI. 
New is_bypassed REST API filter: You can now filter by an is_bypassed query parameter when listing alerts, closing a gap with filtering that was already available in the UI. 
These changes make it easier for organizations to manage requests at scale.
Sort bypass and dismissal requests 
Previously, push protection bypass requests and alert dismissal requests appeared in a fixed order (newest-first). For large organizations, lack of control over sorting made it challenging to manage high volumes of requests. You can now order requests by Newest , Oldest , Recently updated , and Least recently updated directly in the filter UI bar, allowing security analysts and developers to focus on soonest-expiring requests.
Sorting is available at the repository, organization, and enterprise levels for both push protection bypass requests and alert dismissal requests. This improvement makes it substantially easier to manage requests at scale from the UI list view.
New is_bypassed REST API filter 
Previously, the bypassed:true,false qualifier was supported from the UI list view for push protection bypass requests, without an equivalent filter option in the REST API. This improvement makes it easier to programmatically filter alerts by push protection bypasses without additional processing.
The secret scanning alerts API now accepts an is_bypassed boolean query parameter on all three list endpoints:
GET /repos/{owner}/{repo}/secret-scanning/alerts 
GET /orgs/{org}/secret-scanning/alerts 
GET /enterprises/{enterprise}/secret-scanning/alerts 
Pass is_bypassed=true to return only alerts where push protection was bypassed, or is_bypassed=false to exclude them.
Learn more 
Learn more about secret scanning and the secret scanning REST API in our documentation. These improvements were shaped by your feedback. Let us know what you think in the community discussion .
Table of Contents 
What's changing 
Sort bypass and dismissal requests 
New is_bypassed REST API filter 
Learn more 
Menu. Currently selected: What's changing 
What's changing 
Sort bypass and dismissal requests 
New is_bypassed REST API filter 
Learn more 
application security 
Share 
Copied 
Shared 
Back to changelog
