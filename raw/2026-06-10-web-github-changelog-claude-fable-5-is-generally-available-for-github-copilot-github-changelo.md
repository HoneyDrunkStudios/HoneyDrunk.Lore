---
source: "https://github.blog/changelog/2026-06-09-claude-fable-5-is-generally-available-for-github-copilot/"
title: "Claude Fable 5 is generally available for GitHub Copilot - GitHub Changelog"
author: "unknown"
date_published: "2026-06-09"
date_clipped: "2026-06-10"
category: "Developer Tooling & AI Coding"
source_type: "web"
---

# Claude Fable 5 is generally available for GitHub Copilot - GitHub Changelog

Source: https://github.blog/changelog/2026-06-09-claude-fable-5-is-generally-available-for-github-copilot/

[Back to changelog](https://github.blog/changelog/)

Claude Fable 5 from Anthropic is now available in GitHub Copilot, the first model in Anthropic’s Mythos class, designed for long-horizon, autonomous coding and knowledge-work tasks. Unlike other Claude models in GitHub Copilot, Claude Fable 5 requires data retention to operate Anthropic’s safety classifiers. Continue reading for more details. In our internal benchmarks on autonomous coding workflows, Fable 5 completed equivalent work with fewer tool calls and lower token consumption than previous Opus-tier models.

This model is billed at provider list pricing under Usage Based Billing. See [GitHub Copilot’s pricing for models and requests](https://docs.github.com/copilot/reference/copilot-billing/models-and-pricing) for details.

[
](https://github.com/user-attachments/assets/40cea358-b3eb-4ebd-8cd9-20e10d42bcdb)

### [Availability in GitHub Copilot](#availability-in-github-copilot)

Claude Fable 5 will be available to Copilot Pro+, Max, Business, and Enterprise users. You’ll be able to select the model in the model picker in:

- Visual Studio Code in all modes (i.e., chat, ask, edit, and agent)
- Visual Studio
- Copilot CLI
- GitHub Copilot cloud agent
- GitHub Copilot app
- github.com
- GitHub Mobile iOS and Android
- JetBrains
- Xcode
- Eclipse

Rollout will be gradual. Check back soon if you don’t see it yet.

### [Enabling access](#enabling-access)

Copilot Enterprise and Copilot Business plan administrators must enable the Claude Fable 5 policy in Copilot settings. The policy is off by default.

**Important: Claude Fable 5 requires data retention.** As part of Anthropic’s safety architecture for this model, Anthropic retains prompts and outputs for up to 30 days to operate safety classifiers that detect harmful or abusive use. After 30 days, it deletes the prompts and outputs. Retained data is **not used** to train Anthropic’s models.

This data retention applies **only to Claude Fable 5**. All other Claude models in GitHub Copilot, including Claude Opus 4.8, Sonnet 4.5, and Haiku 4.5, continue to operate under Zero Data Retention (ZDR).

For more on how Anthropic handles this data, see [Anthropic’s commercial terms and data retention policy](https://www.anthropic.com/legal/commercial-terms). Enabling the Claude Fable 5 policy constitutes acknowledgement of this requirement. Leaving it off keeps Claude Fable 5 unavailable to your organization.

### [Learn more](#learn-more)

To explore all models available in GitHub Copilot, see our [documentation on models](https://docs.github.com/copilot/reference/ai-models/supported-models) and get started with Copilot.

### [Share your feedback](#share-your-feedback)

Join the [GitHub Community](https://github.com/orgs/community/discussions/categories/copilot-conversations) to share your feedback.

## Related Posts

### Jun.10 Improvement

[Dedicated security review command now available in Copilot CLI](https://github.blog/changelog/2026-06-10-dedicated-security-review-command-now-available-in-copilot-cli)

[application security](https://github.blog/changelog/2026/?label=application-security)
[client apps](https://github.blog/changelog/2026/?label=client-apps)
[copilot](https://github.blog/changelog/2026/?label=copilot)

...
+2

### Jun.09 Improvement

[Security validation for third-party coding agents](https://github.blog/changelog/2026-06-09-security-validation-for-third-party-coding-agents)

[application security](https://github.blog/changelog/2026/?label=application-security)
[copilot](https://github.blog/changelog/2026/?label=copilot)

...
+1

### Jun.05 Retired

[GPT-5.2 and GPT-5.2-Codex deprecated](https://github.blog/changelog/2026-06-05-gpt-5-2-and-gpt-5-2-codex-deprecated)

[copilot](https://github.blog/changelog/2026/?label=copilot)

### Jun.05 Improvement

[Enterprise-managed plugins in VS Code in public preview](https://github.blog/changelog/2026-06-05-enterprise-managed-plugins-in-vs-code-in-public-preview)

[client apps](https://github.blog/changelog/2026/?label=client-apps)
[copilot](https://github.blog/changelog/2026/?label=copilot)
[enterprise management tools](https://github.blog/changelog/2026/?label=enterprise-management-tools)

...
+2

### Jun.04 Improvement

[Fix with Copilot for failing Actions now in Pro, Pro+, and Max](https://github.blog/changelog/2026-06-04-fix-with-copilot-for-failing-actions-now-in-pro-pro-and-max)

[copilot](https://github.blog/changelog/2026/?label=copilot)

### Jun.04 Release

[Agent tasks REST API now available for Copilot Pro, Pro+, and Max](https://github.blog/changelog/2026-06-04-agent-tasks-rest-api-now-available-for-copilot-pro-pro-and-max)

[copilot](https://github.blog/changelog/2026/?label=copilot)

### Jun.04 Release

[Larger context windows and configurable reasoning levels for GitHub Copilot](https://github.blog/changelog/2026-06-04-larger-context-windows-and-configurable-reasoning-levels-for-github-copilot)

[copilot](https://github.blog/changelog/2026/?label=copilot)

### Jun.04 Release

[GitHub Copilot in Visual Studio — May update](https://github.blog/changelog/2026-06-04-github-copilot-in-visual-studio-may-update)

[copilot](https://github.blog/changelog/2026/?label=copilot)

### Jun.04 Release

[Copilot Chat brings richer context to pull requests](https://github.blog/changelog/2026-06-04-copilot-chat-brings-richer-context-to-pull-requests)

[copilot](https://github.blog/changelog/2026/?label=copilot)

## Subscribe to our developer newsletter

Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.

[Back to top](#start-of-content)
