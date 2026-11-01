---
source: "https://github.blog/changelog/2026-10-20-github-package-firewall-in-public-preview"
title: "GitHub package firewall in public preview"
author: "Allison"
date_published: "2026-10-20"
date_clipped: "2026-10-31"
category: "Security & Ethical Hacking"
source_type: "rss"
discovered_via: "https://tldr.tech/infosec/2026-10-30"
---

# GitHub package firewall in public preview

[Back to changelog](https://github.blog/changelog/)

Release

October 20, 2026 •
2 minute read

# GitHub package firewall in public preview

*Editor’s note (October 21, 2026): Rewrote the changelog for clarity and added imagery.*

There’s been a recent flood of malware attacks that exploit systems at package installation time. Agents and CI runners are particularly vulnerable to these attacks because they install dependencies to accomplish a task or complete a build without a human in the loop. To stem this tide, GitHub is introducing a new package firewall, which sits between endpoints or internal registries and the upstream package repositories. The firewall inspects both metadata requests and package downloads for signs of malicious activity, acting as an install-time policy gate. The package firewall is available today in public preview for all GitHub Enterprise Cloud customers, including data-resident GitHub Enterprise Cloud.

## [How it works](https://github.blog/changelog/2026-10-20-github-package-firewall-in-public-preview#how-it-works)

First, administrators set policy controls for their enterprise. The controls available today include a configurable cooldown period, checking the GitHub Advisory Database for malware or vulnerability advisories, and supply-chain checks like attestation downgrades.

Then, endpoints like coding agents and CI/CD hosts use the firewall for their requests instead of pointing directly at the upstream package registries. Metadata requests for package lists as well as the actual package downloads flow through the firewall, which evaluates them against the policy. If a package is blocked erroneously, the user can request an exception with a workflow similar to other GitHub Advanced Security features.

## [Availability and limitations](https://github.blog/changelog/2026-10-20-github-package-firewall-in-public-preview#availability-and-limitations)

The package firewall is available in public preview as we scale up the infrastructure behind it and continue to add features based on customer demand. It is available to GitHub Enterprise Cloud customers, including GitHub Enterprise Cloud with data residency. The service is free while in the preview period. When it reaches general availability, it will be charged based on metered usage, similar to Actions billing.

Currently the package firewall only supports npm packages.

## [How to use it](https://github.blog/changelog/2026-10-20-github-package-firewall-in-public-preview#how-to-use-it)

For detailed setup instructions, see [Protecting endpoints with package firewall](https://docs.github.com/enterprise-cloud@latest/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/protecting-endpoints-with-package-firewall). Join the discussion in [GitHub Community](https://github.com/orgs/community/discussions/210809).
