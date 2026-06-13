---
source: "https://github.blog/changelog/2026-06-11-agentic-workflows-no-longer-need-a-personal-access-token/"
title: "Agentic workflows no longer need a personal access token - GitHub Changelog"
author: "unknown"
date_published: "2026-06-11"
date_clipped: "2026-06-12"
category: "DevOps & CI/CD"
source_type: "web"
---

You can now use GitHub Agentic Workflows with GitHub Actions’s built-in `GITHUB_TOKEN`.

This means that you no longer need to create and store a personal access token (PAT), eliminating the operational and security risks of managing long-lived PATs for automations at scale.

When you use the Actions token in an agentic workflow running in an organization-owned repository, AI credits consumed by your agentic workflow are billed directly to the organization.

### [Configuring organization billing for Copilot CLI in GitHub Agentic Workflows](#configuring-organization-billing-for-copilot-cli-in-github-agentic-workflows)

In order to use this feature, you must enable the “Allow use of Copilot CLI billed to the organization” Copilot policy. This is enabled by default if you have the existing “Copilot CLI” policy enabled.

Once enabled, you can configure agentic workflows to bill directly to the organization by adding `copilot-requests: write` to the `permissions` section in the frontmatter of your agentic workflow markdown file, then compiling and pushing your updated lockfile.

> Note: You must be on the latest version of the Agentic Workflows CLI. Use `$ gh extension upgrade aw` to upgrade.

### [Controlling cost while billing to your organization](#controlling-cost-while-billing-to-your-organization)

User-level inference budgets are not considered when billing directly to the organization, because the cost is not attributed to a user. There are multiple ways to manage spend when using this billing method:

- Configure [cost centers](https://docs.github.com/billing/concepts/cost-centers) for the relevant organizations. Cost centers allow cost attribution to groups of organizations, and budgets can be applied to cost centers.
- Use the [cost management tools](https://gh.io/gh-aw-cost) in GitHub Agentic Workflows to monitor, manage, and cap token usage per agentic workflow run.

To learn more, see the [GitHub Agentic Workflows documentation about authentication](https://gh.io/gh-aw-authentication).

This feature is available for all Copilot plans: Copilot Free, Copilot Pro, Copilot Pro+, Copilot Business, and Copilot Enterprise.
