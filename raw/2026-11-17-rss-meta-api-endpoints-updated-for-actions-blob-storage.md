---
"source": "https://github.blog/changelog/2026-10-22-meta-api-endpoints-updated-for-actions-blob-storage"
"title": "Meta API endpoints updated for Actions blob storage"
"author": "Allison"
"date_published": "2026-10-22"
"date_clipped": "2026-11-17"
"category": "DevOps & CI/CD"
"source_type": "rss"
---

# Meta API endpoints updated for Actions blob storage

[Back to changelog](https://github.blog/changelog/)

Improvement

October 22, 2026 •
1 minute read


We’re adding blob storage endpoints for GitHub Actions on github.com as part of our ongoing work to improve capacity and reliability. The [meta API](https://api.github.com/meta) now includes these new endpoints.

If your organization uses a network allowlist to access GitHub Actions blob storage, review your network access settings and ensure you allow the following new hosts (both ranges are inclusive):

- `productionresultssa30.blob.core.windows.net` through `productionresultssa49.blob.core.windows.net`
- `productionresultssa100.blob.core.windows.net` through `productionresultssa199.blob.core.windows.net`

If you already allow `productionresultssa*.blob.core.windows.net`, no changes are needed for these additions. If you allow individual hosts, add the new hosts to avoid interruptions to job summaries and logs.

For guidance on allowlisting GitHub traffic, see [GitHub’s IP addresses](https://docs.github.com/authentication/keeping-your-account-and-data-secure/about-githubs-ip-addresses). You can retrieve the current endpoint list using the [REST API endpoints for meta data](https://docs.github.com/rest/meta/meta).
