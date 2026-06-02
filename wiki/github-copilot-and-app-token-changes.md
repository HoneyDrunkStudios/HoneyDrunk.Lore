# GitHub Copilot and App Token Changes

## Decision-useful summary
Two GitHub platform changes affect automation cost and compatibility: GitHub App installation tokens are moving to a longer `ghs_APPID_JWT` format, and Copilot code review starts consuming GitHub Actions minutes on June 1, 2026 in addition to AI Credits. Copilot cloud agent startup also improved through Actions custom images. [sources: raw/2026-05-03-rss-github-app-installation-token-format.md; raw/2026-05-03-rss-github-copilot-code-review-actions-minutes.md; raw/2026-05-03-rss-github-copilot-cloud-agent-custom-images.md]

## Claims
- Starting April 27, 2026, GitHub began staged rollout of a new stateless GitHub App installation-token format; new `ghs_` tokens become `ghs_APPID_JWT`, grow to roughly 520 characters, and vary in length. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-rss-github-app-installation-token-format.md]
- GitHub warns that apps relying on installation tokens being exactly 40 characters long may break under the new format. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-rss-github-app-installation-token-format.md]
- Starting June 1, 2026, GitHub Copilot code review will be billed as AI Credits and will also consume GitHub Actions minutes from the user's existing plan. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-rss-github-copilot-code-review-actions-minutes.md]
- Copilot code review uses an agentic tool-calling architecture that runs on GitHub Actions runners, including GitHub-hosted, self-hosted, and larger runners. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-rss-github-copilot-code-review-actions-minutes.md]
- Copilot cloud agent startup became over 20% faster by using optimized runner environments built with GitHub Actions custom images; this builds on a prior reported 50% startup improvement in March 2026. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-rss-github-copilot-cloud-agent-custom-images.md]

## Typed entities
- platform: GitHub
- product: GitHub Copilot code review
- product: Copilot cloud agent
- token type: GitHub App installation token
- token prefix: `ghs_`
- billing unit: GitHub Actions minutes
- billing unit: AI Credits
- date/decision: 2026-06-01 Copilot code review Actions-minute billing begins
- file: raw/2026-05-03-rss-github-app-installation-token-format.md
- file: raw/2026-05-03-rss-github-copilot-code-review-actions-minutes.md
- file: raw/2026-05-03-rss-github-copilot-cloud-agent-custom-images.md

## Explicit relationships
- GitHub App installation-token format supersedes prior fixed-length-token assumptions.
- GitHub Copilot code review depends-on GitHub Actions runners for agentic repository-context work.
- Copilot code review uses AI Credits and GitHub Actions minutes for billing after 2026-06-01.
- Copilot cloud agent uses GitHub Actions custom images to reduce startup latency.

## HoneyDrunk implications
- Audit any token validators, DB column sizes, regexes, log redactors, or secret scanners that assume `ghs_` tokens are 40 characters.
- Treat Copilot code review as a CI cost center after 2026-06-01; cap usage or route reviews onto appropriate runners if cost matters.

## Confidence and quality notes
- Quality posture: decision-usable; all operational dates are cited.
- Supersession: older fixed-length `ghs_` token assumptions are superseded by the 2026 format rollout.
- Privacy filter: no real tokens or secrets copied.

## 2026-05-30 compile additions

### Claims
- Microsoft/.NET Blog guidance frames GitHub Copilot for .NET as a set of surfaces with different fit: inline completions for repetitive C# work, chat for reasoning/planning/explanation, Visual Studio Test Agent for solution-local testing, Copilot CLI for terminal build/test loops, and cloud coding agent for bounded background changes. confidence: 1 Microsoft/.NET Blog source, last-confirmed 2026-05-30. [source: raw/2026-05-30-rss-net-blog-doing-more-with-github-copilot-as-a-net-developer.md]
- The source says agentic Copilot tasks should be multi-step, bounded, reviewable, and paired with constraints such as preserving public APIs, following existing test style, limiting scope, and rerunning relevant tests. confidence: 1 Microsoft/.NET Blog source, last-confirmed 2026-05-30. [source: raw/2026-05-30-rss-net-blog-doing-more-with-github-copilot-as-a-net-developer.md]

### Typed entities
- product: GitHub Copilot
- feature: inline completions
- feature: Copilot Chat
- feature: Visual Studio Test Agent
- feature: Copilot CLI
- feature: cloud coding agent
- language/runtime: .NET / C#

### Explicit relationships
- Copilot cloud coding agent depends-on GitHub Actions runner capacity and cost, as tracked in this page's billing claims.
- Agentic Copilot use complements, not replaces, PR-style diff review and test verification.

### HoneyDrunk implications
- Treat Copilot agent tasks as CI-costing work units after 2026-06-01 when code review Actions-minute billing begins; scope and verify them like other runner-consuming automation.

## 2026-06-01 compile additions

### Claims
- dotnet/runtime's CCA experience reinforces that Copilot cloud coding agent PRs are human-initiated and should be treated as reviewed drafts, not autonomous commits: every CCA PR in the report was explicitly requested by a maintainer. confidence: 1 Microsoft/.NET source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-ten-months-with-copilot-coding-agent-in-dotnet-runtime.md]
- The report notes CCA PRs may overproduce tests and require review pruning, especially when "comprehensive" is underspecified or when tests could encode existing incorrect behavior. confidence: 1 source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-ten-months-with-copilot-coding-agent-in-dotnet-runtime.md]

### Typed entities
- product: GitHub Copilot Coding Agent
- repository: dotnet/runtime
- concept: human-requested PR
- concept: AI-generated test review

### Explicit relationships
- Copilot cloud agent output depends-on human PR review before merge.
- Test-generation assistance complements coverage work but does not supersede human judgment about behavior under test.

### HoneyDrunk implications
- Keep Copilot agent usage under PR-review discipline, especially after code review and agent runs consume Actions minutes.
- Prompt generated-test tasks with expected behavior and bug hypotheses, not only "add comprehensive tests."

## 2026-06-02 compile additions

### Claims
- GitHub Copilot usage metrics API now assigns engaged users to AI adoption phases over a rolling 28-day window using a new user-level `ai_adoption_phase` field and enterprise/organization `totals_by_ai_adoption_phase` grouping. confidence: 1 GitHub changelog source, last-confirmed 2026-06-02. [source: raw/2026-06-02-web-github-changelog-copilot-usage-metrics-api-adds-cohorts-for-ai-adoptio.md]
- GitHub's v1 adoption phases are Phase 0 no cohort, Phase 1 code first, Phase 2 agent first, and Phase 3 multi-agent; phase assignment requires use of matching Copilot surfaces on at least two days in the last 28 days. confidence: 1 GitHub changelog source, last-confirmed 2026-06-02. [source: raw/2026-06-02-web-github-changelog-copilot-usage-metrics-api-adds-cohorts-for-ai-adoptio.md]
- As of 2026-06-01, usage-based billing is active for all Copilot plans, Copilot code review consumes GitHub Actions minutes in addition to AI Credits, organization admins can configure a default runner for Copilot code review, and user-level budgets are generally available for organizations and enterprises. confidence: 1 GitHub changelog source, last-confirmed 2026-06-02. [source: raw/2026-06-02-web-github-changelog-updates-to-github-copilot-billing-and-plans.md]
- Copilot Max is available as an upgrade for existing Student, Pro, and Pro+ subscribers, while new user sign-ups for Student, Pro, Pro+, and Max remained paused at publication time. confidence: 1 GitHub changelog source, last-confirmed 2026-06-02. [source: raw/2026-06-02-web-github-changelog-updates-to-github-copilot-billing-and-plans.md]

### Typed entities
- API field: `ai_adoption_phase`
- API field: `totals_by_ai_adoption_phase`
- cohort: Phase 0 no cohort
- cohort: Phase 1 code first
- cohort: Phase 2 agent first
- cohort: Phase 3 multi-agent
- billing unit: GitHub AI Credits
- billing unit: GitHub Actions minutes
- control: default Actions runner for Copilot code review
- control: user-level budget
- plan: Copilot Max

### Explicit relationships
- Copilot usage metrics use adoption cohorts to relate product-surface usage to AI rollout maturity.
- User-level budgets constrain Copilot AI Credit consumption at the organization/enterprise level.
- Default Copilot code-review runners route code-review work onto an organization-chosen Actions runner instead of requiring per-repository configuration.
- Copilot code review now depends-on both AI Credit and Actions-minute governance.

### HoneyDrunk implications
- If HoneyDrunk uses GitHub Copilot broadly, report adoption by cohort rather than active-user count alone; multi-agent use should trigger stronger cost and review policy.
- Configure a default runner and user budgets before turning on Copilot code review widely, because billing is active as of 2026-06-01.
