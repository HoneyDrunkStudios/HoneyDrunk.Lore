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

## 2026-06-03 compile additions

### Claims
- GitHub Copilot app is in technical preview for Copilot Pro, Pro+, Business, and Enterprise users as an agent-native desktop control center with a My Work view spanning active sessions, issues, pull requests, and automations. confidence: 1 GitHub product source, last-confirmed 2026-06-03. [source: raw/2026-06-03-web-github-blog-github-copilot-app-the-agent-native-desktop-experience.md]
- GitHub says each Copilot app session runs in its own git worktree, helping parallel agent sessions isolate branches and changes without manual worktree setup/cleanup. confidence: 1 GitHub product source, last-confirmed 2026-06-03. [source: raw/2026-06-03-web-github-blog-github-copilot-app-the-agent-native-desktop-experience.md]
- GitHub Agent Merge can monitor CI, required reviewers, failing checks, review feedback, and merge conditions while the user decides how much automation is enabled and what ships. confidence: 1 GitHub product source, last-confirmed 2026-06-03. [source: raw/2026-06-03-web-github-blog-github-copilot-app-the-agent-native-desktop-experience.md]
- GitHub announced local and cloud sandboxes for Copilot: local sandboxes run isolated on the developer machine with centrally configurable filesystem/network/system restrictions, while cloud sandboxes are ephemeral isolated Linux environments with organization policy. confidence: 1 GitHub product source, last-confirmed 2026-06-03. [source: raw/2026-06-03-web-github-blog-github-copilot-app-the-agent-native-desktop-experience.md]
- Microsoft announced MAI-Code-1-Flash, a Microsoft-built coding model rolling out to GitHub Copilot individual users in VS Code's model picker and auto picker; Microsoft claims it was trained for Copilot production harnesses and can solve some tasks with fewer solution tokens than Claude Haiku 4.5 in their benchmark setup. confidence: 1 Microsoft AI product source, last-confirmed 2026-06-03. [source: raw/2026-06-03-web-microsoft-ai-introducing-mai-code-1-flash.md]

### Typed entities
- product: GitHub Copilot app
- feature: My Work
- feature: Agent Merge
- feature: canvas
- feature: local sandbox
- feature: cloud sandbox
- feature: Copilot SDK
- feature: Copilot CLI `/every`
- feature: Memory++ / `/chronicle`
- model: MAI-Code-1-Flash
- comparison model: Claude Haiku 4.5
- benchmark: SWE-Bench Verified
- benchmark: SWE-Bench Pro
- benchmark: Terminal Bench 2

### Explicit relationships
- Copilot app uses git worktrees to isolate parallel agent sessions.
- Agent Merge depends-on CI/reviewer/branch-policy state and should remain subordinate to explicit human shipping policy.
- Local/cloud sandboxes complement Copilot code review and agent sessions by reducing direct host or production exposure.
- MAI-Code-1-Flash depends-on Copilot harness training/evaluation; benchmark results are harness-specific and do not supersede HoneyDrunk task evals.

### HoneyDrunk implications
- If adopting Copilot app, set policy for local/cloud sandbox defaults, allowed repositories, network access, merge automation, and when Agent Merge may act versus only report.
- Treat MAI-Code-1-Flash as a candidate for lower-cost routine Copilot tasks, but run HoneyDrunk-specific comparisons before changing model-routing defaults.
- Worktree-based session isolation is useful but not sufficient: still review generated workflows, hooks, package scripts, and CI changes before host or production execution.

### Quality notes
- GitHub and Microsoft claims are product-launch claims. Features are preview/rollout-dependent and should be verified in the actual HoneyDrunk Copilot plan before workflow changes.

## 2026-06-05 compile additions

### Claims
- GitHub Copilot cloud agent tasks can now be started and tracked through the Agent tasks REST API for Copilot Pro, Pro+, and Max users in public preview, with authentication by classic/fine-grained personal access tokens or OAuth tokens. confidence: 1 GitHub changelog source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-agent-tasks-rest-api-now-available-for-copilot-pro-pro-and-max.md]
- The Agent tasks REST API is positioned for custom automation such as repository-wide migrations, internal developer-portal repository setup, and recurring release preparation. confidence: 1 GitHub changelog source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-agent-tasks-rest-api-now-available-for-copilot-pro-pro-and-max.md]
- Copilot cloud agent automations can run on schedules or repository events and can triage issues, attempt nightly failing-test fixes, or prepare weekly release-note pull requests without manual launch. confidence: 1 GitHub changelog source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-schedule-and-automate-tasks-with-copilot-cloud-agent.md]
- Copilot automations are scoped to a single repository and can be configured with a prompt, trigger, tool allowlist, model, and billing attribution to the creating user at standard usage-based rates. confidence: 1 GitHub changelog source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-schedule-and-automate-tasks-with-copilot-cloud-agent.md]
- GitHub's separate sandbox changelog says Copilot can run shell command execution inside local sandboxes with filesystem/network/system restrictions and ephemeral cloud Linux sandboxes that inherit organization Copilot cloud-agent policy. confidence: 1 GitHub changelog source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-cloud-and-local-sandboxes-for-github-copilot-now-in-public-preview.md]

### Typed entities
- API: GitHub Agent tasks REST API
- product: Copilot cloud agent
- feature: Copilot automations
- feature: local sandbox
- feature: cloud sandbox
- control: tool allowlist
- auth: personal access token
- auth: OAuth token
- billing: usage-based Copilot token usage
- technology: Microsoft MXC

### Explicit relationships
- Agent tasks REST API uses Copilot cloud agent as an automation target for background repository work.
- Copilot automations depend-on repository-scoped prompts, triggers, tools, and model selection.
- Copilot automations use usage-based billing attributed to the automation creator.
- Local sandboxes constrain Copilot-initiated shell execution; cloud sandboxes isolate Copilot sessions in GitHub-hosted ephemeral Linux environments.

### HoneyDrunk implications
- Treat Copilot cloud-agent automations as CI-adjacent scheduled actors: define repository scope, tool allowlist, spend owner, branch/PR behavior, and review requirements before enabling.
- Do not fan out agent tasks across many repositories without budget limits, progress tracking, and a rollback plan.
- Prefer sandboxed Copilot execution where available, but keep host-executed artifacts, workflow changes, package scripts, and generated tests under normal PR review.

### Quality notes
- GitHub features are public preview/rollout-dependent. Verify availability, pricing, token scopes, and org policy controls in the actual HoneyDrunk GitHub plan before operational use.

## 2026-06-07 compile additions

### Claims
- GitHub's "Fix with Copilot" button on failing Actions workflow run logs is now available to Copilot Pro, Pro+, and Max subscribers; it starts a Copilot cloud-agent session that investigates the failure, pushes a fix to the branch, and tags the user for review. confidence: 1 GitHub changelog source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-fix-with-copilot-for-failing-actions-now-in-pro-pro-and-max.md]
- Enterprise-managed plugins in VS Code public preview extend prior Copilot CLI enterprise plugin management, allowing enterprise administrators to configure and distribute plugins, hooks, MCP configurations, and auto-installed plugins across VS Code and Copilot CLI clients. confidence: 1 GitHub changelog source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-enterprise-managed-plugins-in-vs-code-in-public-preview.md]

### Typed entities
- feature: Fix with Copilot
- product: Copilot cloud agent
- surface: GitHub Actions workflow run logs
- product: enterprise-managed plugins
- editor: Visual Studio Code
- product: Copilot CLI
- config file: `.github-private/.github/copilot/settings.json`

### Explicit relationships
- Fix with Copilot uses Copilot cloud agent to turn failing CI logs into a branch update for human review.
- Enterprise-managed plugins use centralized Copilot client settings to standardize plugin/hook/MCP configuration across developer clients.
- Fix with Copilot complements, but does not supersede, branch protection, PR review, and test verification.

### HoneyDrunk implications
- Allow Fix with Copilot only for bounded CI failures where branch push behavior, billing owner, review requirement, and allowed tools are understood.
- Treat enterprise-managed plugins as org-level execution policy; auto-installing a plugin should require provenance and hook/MCP review.

### Quality notes
- Both GitHub features are plan/preview dependent. Verify availability, billing, branch permissions, and enterprise policy controls before enabling in HoneyDrunk repos.

## 2026-06-08 compile additions

### Claims
- GitHub Copilot CLI now has generally available rubber duck and voice-input features, while prompt scheduling with `/every` and `/after` and a redesigned terminal interface are available through `/experimental`. confidence: 1 GitHub changelog source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-copilot-cli-improved-ui-rubber-duck-prompt-scheduling-and-voice-input.md]
- Copilot CLI voice input runs local speech-to-text so recorded audio stays on the user's machine; the CLI downloads a runtime/model on first enablement. confidence: 1 GitHub changelog source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-copilot-cli-improved-ui-rubber-duck-prompt-scheduling-and-voice-input.md]
- GitHub Copilot SDK is generally available with stable APIs across Node.js/TypeScript, Python, Go, .NET, Rust, and Java, exposing planning, tool invocation, file edits, streaming, multi-turn sessions, custom tools, MCP, hooks, cloud/remote sessions, and OpenTelemetry tracing. confidence: 1 GitHub changelog source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-copilot-sdk-is-now-generally-available.md]
- The Copilot app technical preview is now available to existing Copilot Pro, Pro+, Business, and Enterprise customers; the release adds canvases, cloud sessions, cloud automations, CLI session visibility in My Work, agentic browsing, voice conversations, rubber duck, and `/chronicle` session querying. confidence: 1 GitHub changelog source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-expanded-technical-preview-availability-for-the-github-copilot-app.md]
- GitHub positions canvases as shared structured work surfaces where users inspect/edit/approve state, agents read and update that state, and the app enforces allowed actions against the underlying artifact or runtime. confidence: 1 GitHub changelog source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-expanded-technical-preview-availability-for-the-github-copilot-app.md]
- VS Code's May 2026 Copilot releases brought the Agents window to Stable preview, added remote agents over SSH or Dev Tunnels, continued Agent Host Protocol work, synced chat sessions to GitHub account history, expanded BYOK to air-gapped environments, and added token/effort/utility-model controls. confidence: 1 GitHub changelog source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-github-copilot-in-visual-studio-code-may-releases.md]
- VS Code terminal-agent updates include expanded terminal output compression, experimental command risk assessments, keeping sensitive prompts in the terminal instead of model context, clearer background-command UX, and the `VSCODE_AGENT` environment variable for agent-aware CLIs. confidence: 1 GitHub changelog source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-github-copilot-in-visual-studio-code-may-releases.md]
- Copilot code review public previews add repository skills/MCP support and a Medium analysis tier that uses a higher-reasoning model for complex/security-sensitive/cross-service pull requests at higher AI Credit cost. confidence: 1 GitHub changelog source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-shape-copilot-code-review-around-your-team.md]

### Typed entities
- product: GitHub Copilot CLI
- feature: rubber duck
- feature: voice input
- feature: `/every`
- feature: `/after`
- feature: experimental terminal interface
- SDK: GitHub Copilot SDK
- language/runtime: Node.js / TypeScript
- language/runtime: Python
- language/runtime: Go
- language/runtime: .NET
- language/runtime: Rust
- language/runtime: Java
- product: GitHub Copilot app
- feature: canvas
- feature: cloud automation
- feature: agentic browsing
- command: `/chronicle`
- product: VS Code Agents window
- protocol: Agent Host Protocol / AHP
- feature: air-gapped BYOK
- environment variable: `VSCODE_AGENT`
- feature: Copilot code review Medium tier
- directory: `.github/skills`
- file: `SKILL.md`

### Explicit relationships
- Copilot CLI scheduling uses `/every` and `/after` to run prompts or skills inside the current session.
- Copilot SDK uses MCP, hooks, custom tools, cloud sessions, and OpenTelemetry to expose Copilot's agent runtime to external applications.
- Copilot app canvases complement chat by making agent state inspectable and editable as a structured artifact.
- VS Code remote agents depend-on SSH or Dev Tunnels so sessions can continue when the client disconnects.
- Sensitive terminal prompts contradict model-context ingestion and should stay in terminal-controlled input paths.
- Copilot code review uses repository skills and MCP servers to bring organization context into review.
- Copilot code review Medium tier depends-on higher AI Credit spend and should be routed to repositories where deeper analysis is worth the cost.

### HoneyDrunk implications
- Treat Copilot surfaces as one ecosystem, not isolated tools: CLI, SDK, app, VS Code Agents window, code review, skills, MCP, cloud sessions, and automations now share configuration and session concepts.
- If HoneyDrunk uses Copilot SDK, define SDK app identities, hook behavior, MCP allowlists, OTel redaction, and BYOK policy before production embedding.
- Keep voice input local-only as a privacy requirement for agent prompts; verify this behavior before using it near sensitive unreleased work.
- For Copilot code review, create repository-specific `code-review` skills only after deciding which standards belong in prompts versus deterministic checks.

### Quality notes
- GitHub sources are authoritative for feature existence, but many capabilities are preview, plan-dependent, or enabled through experimental mode. Verify current plan, billing, and client versions before workflow changes.
