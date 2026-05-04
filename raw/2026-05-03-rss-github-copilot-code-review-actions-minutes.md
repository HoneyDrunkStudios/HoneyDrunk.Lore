---
source: "https://github.blog/changelog/2026-04-27-github-copilot-code-review-will-start-consuming-github-actions-minutes-on-june-1-2026"
title: "GitHub Copilot code review will start consuming GitHub Actions minutes on June 1, 2026"
author: "Allison"
date_published: "2026-04-27"
date_clipped: "2026-05-03"
category: "Developer Tooling & AI Coding"
source_type: "rss"
---

Developers and engineering teams worldwide use GitHub Copilot for high-quality, agent-powered code reviews on every pull request. We understand that any change is significant to our customers, especially when it relates to billing, so we are sharing this update early to help you plan and prepare. The sections below outline what is changing, why, and how to plan accordingly.

## What’s changing

Last month, we shared how GitHub Copilot code review runs on agentic tool-calling architecture, allowing the code review agent to pull in broader repository context and produce more relevant feedback on each pull request. That agentic architecture runs on GitHub Actions using GitHub-hosted runners (**Note: GitHub Copilot code review also supports self-hosted runners and GitHub-hosted larger runners which are billed at different rates than standard GitHub-hosted runners.**)

Starting June 1, 2026, each Copilot code review will be billed in two ways:

- All Copilot usage (including code reviews) will be billed as AI Credits under the new usage-based billing model (see the usage-based billing announcement for additional details). 

- GitHub Actions minutes will be consumed from your existing plan entitlement for each review that is run on private repositories, with any usage beyond your included minutes billed at standard GitHub Actions rates. You or your organization administrator (for GitHub Teams and Enterprise) can use budgets to manage spending on GitHub Actions. There are no changes to public repositories, where Actions minutes remain free.

This change applies to the following plans:

- GitHub Copilot Pro 

- GitHub Copilot Pro+ 

- GitHub Copilot Business 

- GitHub Copilot Enterprise

**This includes Copilot code reviews from non-licensed users and billed via [direct org billing](https://docs.github.com/copilot/concepts/agents/code-review#enabling-code-review-for-users-without-a-license).**

## When it takes effect

This change takes effect on **June 1, 2026**. Until that day, Copilot code review usage will continue to draw only from your existing Copilot premium request unit (PRU) allowance and will not consume GitHub Actions minutes.

## What you need to do

To prepare for the billing change, we recommend the following.

### Review billing and usage

- **Review your current GitHub Actions usage.** Billing managers can view minute consumption and entitlements in your account or organization billing settings.

- **Check your budget on spending limits.** [Confirm that your personal or organizational budget](https://docs.github.com/billing/how-tos/set-up-budgets) for Actions aligns with your expected usage. You or your organization administrators (for GitHub Teams and Enterprise) can adjust spending limits for GitHub Actions at any time.

- **Monitor your Copilot and Actions usage over time** via [GitHub Copilot usage metrics](https://docs.github.com/copilot/concepts/copilot-usage-metrics), [GitHub Actions metrics](https://docs.github.com/enterprise-cloud@latest/organizations/collaborating-with-groups-in-organizations/viewing-github-actions-metrics-for-your-organization), and [Billing Usage Report](https://docs.github.com/enterprise-cloud@latest/organizations/collaborating-with-groups-in-organizations/viewing-github-actions-metrics-for-your-organization).

- **Review the usage-based billing announcement** to understand how Copilot usage itself is being measured going forward. 

- **Share this update with your billing administrators and engineering leads** so they are aware of the new usage pattern before June 1, 2026. 

### Review runner settings

- No additional setup is required if you already have [GitHub-hosted Runners enabled on your repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository).

- If you would like to customize your GitHub Hosted Runner environment, see [Upgrade to larger GitHub-hosted Runners](https://docs.github.com/enterprise-cloud@latest/copilot/how-tos/copilot-on-github/set-up-copilot/configure-runners#upgrade-to-larger-github-hosted-github-actions-runners).

- [Self-hosted Runners setup](https://docs.github.com/enterprise-cloud@latest/copilot/how-tos/copilot-on-github/set-up-copilot/configure-runners#upgrade-to-larger-github-hosted-github-actions-runners) is available.

Learn more about these changes in [our documentation](https://docs.github.com/copilot/reference/copilot-billing/models-and-pricing#github-actions-minutes-for-code-review).

And join the discussion within [GitHub Community](https://github.com/orgs/community/discussions/categories/announcements).

The post [GitHub Copilot code review will start consuming GitHub Actions minutes on June 1, 2026](https://github.blog/changelog/2026-04-27-github-copilot-code-review-will-start-consuming-github-actions-minutes-on-june-1-2026) appeared first on [The GitHub Blog](https://github.blog).
