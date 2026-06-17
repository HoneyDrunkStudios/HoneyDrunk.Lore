---
source: "https://github.blog/changelog/2026-06-15-copilot-usage-metrics-now-include-more-of-your-active-users/"
title: "Copilot usage metrics now include more of your active users - GitHub Changelog"
author: "unknown"
date_published: "2026-06-15"
date_clipped: "2026-06-17"
category: "Developer Tooling & AI Coding"
source_type: "web"
---
[Back to changelog](https://github.blog/changelog/)

Copilot usage metrics reports now draw on server-side telemetry in addition to client signals, so more of your active Copilot users show up in reports. Enterprise usage reports returned by the [Copilot usage metrics API](https://docs.github.com/enterprise-cloud@latest/rest/copilot/copilot-usage-metrics?apiVersion=2026-03-10) now surface active users that client-side telemetry alone would have missed, giving you a more complete and consistent picture of who is using Copilot.

### [What’s new](#whats-new)

Copilot usage reports have historically been built from client-side telemetry emitted by IDEs and other clients. That telemetry is the richest source we have, but it does not always reach us. Network conditions, proxy configurations, client settings, and other factors outside of your control or ours can prevent a client from reporting activity. When that happened, an active, billed user could be absent from your reports.

This update incorporates additional server-side telemetry to identify active users. Any active user we can confirm from the server side who was not already captured from client telemetry is now included in your enterprise single-day and 28-day reports, increasing your daily active user (DAU) coverage.

These newly surfaced users are fully identified and counted toward your active user totals. What server-side telemetry does not yet carry is the rich, per-interaction detail that client telemetry provides (i.e., the specific IDE, feature, model, and lines-of-code activity). So for these users, the high-level counts go up while the detailed breakdowns stay empty until richer telemetry is available for them.

### [What you’ll see in a typical report](#what-youll-see-in-a-typical-report)

Suppose an enterprise single-day report previously showed 1,000 daily active users, all sourced from client telemetry. With this change, that same report might now show 1,050. The extra 50 are users we confirmed were active from server-side telemetry but never received client telemetry for.

In practice, your active user and DAU counts immediately become more complete, while the dimensional breakdowns (such as `totals_by_ide` and `totals_by_feature`) won’t yet reflect these users, so a larger share of activity may appear unattributed. Top-level totals and breakdowns for your existing users are unchanged.

This is the first step in a broader effort to bring server-side signals into Copilot metrics. Users surfaced from server-side telemetry are now included, and upcoming releases will progressively attribute richer per-feature and per-surface detail to them, filling in those empty breakdowns over time.

### [Why this matters](#why-this-matters)

- **More consistency across your data:** Usage reports line up more closely with what you see in the activity log and billing, reducing the gaps that drive support escalations about “missing” users.
- **Resilient by design:** Combining server-side and client-side signals means a single client-side hiccup no longer erases a user from your reports.

Visit [our API documentation](https://docs.github.com/enterprise-cloud@latest/rest/copilot/copilot-usage-metrics?apiVersion=2026-03-10) to learn more.

Join the discussion within [GitHub Community](https://github.com/orgs/community/discussions/categories/announcements).

## Related Posts

### Jun.16 Release

[Organization-level enablement for GitHub Code Quality](https://github.blog/changelog/2026-06-16-organization-level-enablement-for-github-code-quality)

[application security](https://github.blog/changelog/2026/?label=application-security)
[enterprise management tools](https://github.blog/changelog/2026/?label=enterprise-management-tools)

...
+1

### Jun.12 Improvement

[Copilot code review: New configurations and controls](https://github.blog/changelog/2026-06-12-copilot-code-review-new-configurations-and-controls)

[copilot](https://github.blog/changelog/2026/?label=copilot)

### Jun.11 Improvement

[AI usage report updates](https://github.blog/changelog/2026-06-11-ai-usage-report-updates)

[enterprise management tools](https://github.blog/changelog/2026/?label=enterprise-management-tools)

### Jun.11 Release

[Copilot CLI: Configure everything from one place with /settings](https://github.blog/changelog/2026-06-11-copilot-cli-configure-everything-from-one-place-with-settings)

[client apps](https://github.blog/changelog/2026/?label=client-apps)
[copilot](https://github.blog/changelog/2026/?label=copilot)

...
+1

### Jun.11 Release

[GitHub Agentic Workflows is now in public preview](https://github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview)

[actions](https://github.blog/changelog/2026/?label=actions)
[copilot](https://github.blog/changelog/2026/?label=copilot)

...
+1

### Jun.11 Release

[Agentic workflows no longer need a personal access token](https://github.blog/changelog/2026-06-11-agentic-workflows-no-longer-need-a-personal-access-token)

[copilot](https://github.blog/changelog/2026/?label=copilot)

### Jun.10 Release

[Copilot Chat now sees your agent sessions](https://github.blog/changelog/2026-06-10-copilot-chat-now-sees-your-agent-sessions)

[copilot](https://github.blog/changelog/2026/?label=copilot)

### Jun.10 Improvement

[Enterprises can now create up to 500 cost centers](https://github.blog/changelog/2026-06-10-enterprises-can-now-create-up-to-500-cost-centers)

[account management](https://github.blog/changelog/2026/?label=account-management)
[enterprise management tools](https://github.blog/changelog/2026/?label=enterprise-management-tools)

...
+1

### Jun.10 Improvement

[Dedicated security review command now available in Copilot CLI](https://github.blog/changelog/2026-06-10-dedicated-security-review-command-now-available-in-copilot-cli)

[application security](https://github.blog/changelog/2026/?label=application-security)
[client apps](https://github.blog/changelog/2026/?label=client-apps)
[copilot](https://github.blog/changelog/2026/?label=copilot)

...
+2

## Subscribe to our developer newsletter

Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.

[Back to top](#start-of-content)
