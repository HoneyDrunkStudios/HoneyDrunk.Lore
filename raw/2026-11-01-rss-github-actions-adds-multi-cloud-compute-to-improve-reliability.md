---
source: "https://github.blog/changelog/2026-10-28-github-actions-adds-multi-cloud-compute-to-improve-reliability"
title: "GitHub Actions adds multi-cloud compute to improve reliability"
author: "Allison"
date_published: "2026-10-28"
date_clipped: "2026-11-01"
category: "DevOps & CI/CD"
source_type: "rss"
---

# GitHub Actions adds multi-cloud compute to improve reliability

Source: https://github.blog/changelog/2026-10-28-github-actions-adds-multi-cloud-compute-to-improve-reliability

![](https://github.blog/wp-content/themes/github-2021-child/assets/img/featured-v3-improvements.svg)

We’re expanding the infrastructure behind GitHub-hosted runners so your workflows start faster and run more reliably, even during periods of peak demand. GitHub Actions now schedules eligible jobs across a broader, multi-cloud compute pool. This adds capacity, reduces capacity-related queue times, and improves service resilience. As part of this, eligible Linux jobs may run on Amazon Web Services (AWS) in addition to Microsoft Azure.

Multi-cloud compute will be used for standard 2-core and 4-core Linux runners and compatible 2-core and 4-core larger runners without specialized configurations. This change does not apply to Windows runners or runners with private networking or other specialized configurations.

For customers on GitHub Free, GitHub Pro, and GitHub Team, eligible runners will automatically use multi-cloud compute. Customers on GitHub Enterprise Cloud can opt in by going to **Enterprise settings > Actions > Hosted compute cloud providers** and enabling AWS compute.

GitHub Actions automatically schedules eligible jobs across available cloud providers. Your existing runner labels and workflow syntax remain unchanged.

## [Recommended action: Keep your network allowlists up to date](https://github.blog/changelog/2026-10-28-github-actions-adds-multi-cloud-compute-to-improve-reliability#recommended-action-keep-your-network-allowlists-up-to-date)

To get the full benefit of expanded capacity, make sure any IP allowlists or network-based access policies your workflows rely on include all published GitHub Actions IP ranges. Runners in the expanded compute pool use additional outbound IP addresses, so policies that allow only Azure or Microsoft-owned ranges, including Microsoft Entra Conditional Access policies, can block connections or authentication from these runners.

This is a rolling change, so we recommend updating your allowlists now, before your workflows begin running in the expanded compute pool.

All GitHub Actions runner IP ranges, including the new ones, are published in the `actions` array returned by `GET https://api.github.com/meta`. We recommend keeping your allowlists in sync with this endpoint rather than relying on cloud-provider-specific ranges. See [GitHub-hosted runner IP addresses](https://docs.github.com/actions/reference/runners/github-hosted-runners#ip-addresses) for details.
