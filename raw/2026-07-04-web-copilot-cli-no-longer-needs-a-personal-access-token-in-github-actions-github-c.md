---
source: "https://github.blog/changelog/2026-07-02-copilot-cli-no-longer-needs-a-personal-access-token-in-github-actions"
title: "Copilot CLI no longer needs a personal access token in GitHub Actions - GitHub Changelog"
author: "Allison"
date_published: "2026-07-02"
date_clipped: "2026-07-04"
category: "DevOps & CI/CD"
source_type: "web"
---

# Copilot CLI no longer needs a personal access token in GitHub Actions - GitHub Changelog

Source: https://github.blog/changelog/2026-07-02-copilot-cli-no-longer-needs-a-personal-access-token-in-github-actions

# Copilot CLI no longer needs a personal access token in GitHub Actions

You can now run [GitHub Copilot CLI](https://docs.github.com/copilot/concepts/agents/copilot-cli/about-copilot-cli) in GitHub Actions using the built-in `GITHUB_TOKEN`

.

This means that you no longer need to create and store a personal access token (PAT), eliminating the operational and security risks of managing long-lived PATs for automations at scale.

When you run Copilot CLI with the Actions token in an organization-owned repository, AI credits consumed by the CLI are billed directly to the organization.

[Configuring organization billing for Copilot CLI in GitHub Actions](https://github.blog#configuring-organization-billing-for-copilot-cli-in-github-actions)

In order to use this feature, you must enable the “Allow use of Copilot CLI billed to the organization” Copilot policy. This is enabled by default if you have the existing “Copilot CLI” policy enabled.

Once enabled, workflows just need the `copilot-requests: write`

permission and can authenticate with the workflow’s built-in `GITHUB_TOKEN`

. No additional secrets are required.

To learn more, see [“Using Copilot CLI in GitHub Actions with GITHUB_TOKEN”](https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli-in-actions) in the GitHub Docs.

Note: You must be on a recent version of Copilot CLI. Update with

`copilot update`

, or reinstall the latest version with`npm install -g @github/copilot`

.

[Controlling cost while billing to your organization](https://github.blog#controlling-cost-while-billing-to-your-organization)

User-level budgets are not considered when billing directly to the organization because the cost is not attributed to a user. There are multiple ways to manage spend when using this billing method:

- Configure
[cost centers](https://docs.github.com/billing/concepts/cost-centers)for the relevant organizations. Cost centers allow cost attribution to groups of organizations, and budgets can be applied to cost centers. - Monitor Copilot usage from your organization’s billing and usage dashboards to track consumption over time.
- Set a
[session limit](https://docs.github.com/copilot/how-tos/copilot-cli/use-copilot-cli/set-session-limit)to configure a maximum amount of AI credits that will be used by a workflow.
