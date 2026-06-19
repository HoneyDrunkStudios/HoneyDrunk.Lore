# GitHub Actions Platform Operations

## Decision-useful summary
GitHub Actions has two May 2026 operational changes that matter for CI/CD reliability: concurrency groups can now queue multiple pending runs instead of replacing the single pending run, and hosted runner images are entering migration windows for Arm64 maintenance ownership, Windows 2025/Visual Studio 2026, and `macos-latest` moving to macOS 26. For HoneyDrunk, the concurrency queue is useful for ordered deploys against shared environments, while the runner-image migrations should be pinned/tested before default labels move. [sources: raw/2026-05-16-rss-github-changelog-actions-github-actions-concurrency-groups-now-allow-l.md; raw/2026-05-16-rss-github-changelog-actions-github-actions-upcoming-image-migrations.md]

## Claims
- GitHub Actions concurrency groups can now allow multiple jobs or workflow runs to wait in the same concurrency group, with up to 100 queued jobs or workflow runs per group. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-github-changelog-actions-github-actions-concurrency-groups-now-allow-l.md]
- Larger concurrency queues are enabled with `queue: max` in the workflow `concurrency` block when `cancel-in-progress` is false or unset, making ordered deployment workflows easier to preserve. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-github-changelog-actions-github-actions-concurrency-groups-now-allow-l.md]
- GitHub now owns and maintains Arm64 hosted runner images; `windows-11-arm` has transitioned, and Ubuntu Arm64 images are migrating to GitHub internal pipelines with no expected compatibility/package change. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-github-changelog-actions-github-actions-upcoming-image-migrations.md]
- The `windows-latest` and `windows-2025` hosted-runner labels migrate to Visual Studio 2026 between 2026-06-08 and 2026-06-15; workflows that must stay on Visual Studio 2022 should pin `windows-2022`. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-github-changelog-actions-github-actions-upcoming-image-migrations.md]
- The `macos-latest` label begins a 30-day migration on 2026-06-15 from macOS 15 to macOS 26; workflows requiring macOS 15 should pin `macos-15`. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-github-changelog-actions-github-actions-upcoming-image-migrations.md]

## Typed entities
- platform: GitHub Actions
- feature: concurrency groups
- feature: concurrency `queue: max`
- runner label: `windows-latest`
- runner label: `windows-2025`
- runner label: `windows-2025-vs2026`
- runner label: `windows-2022`
- runner label: `macos-latest`
- runner label: `macos-15`
- runner image: `ubuntu-24.04-arm`
- runner image: `ubuntu-22.04-arm`
- runner image: `windows-11-arm`
- date/decision: 2026-06-08 Windows 2025 Visual Studio 2026 migration begins
- date/decision: 2026-06-15 macos-latest migration begins
- file: raw/2026-05-16-rss-github-changelog-actions-github-actions-concurrency-groups-now-allow-l.md
- file: raw/2026-05-16-rss-github-changelog-actions-github-actions-upcoming-image-migrations.md

## Explicit relationships
- GitHub Actions concurrency groups use `queue: max` to supersede the previous one-pending-run replacement behavior for ordered workflows.
- Ordered deployment workflows depend-on serialized access to shared resources/environments.
- `windows-latest` and `windows-2025` labels will point to Visual Studio 2026 after the migration, superseding implicit Visual Studio 2022 assumptions.
- `macos-latest` will point to macOS 26 after migration, superseding implicit macOS 15 assumptions.
- [[github-copilot-and-app-token-changes]] depends-on GitHub Actions runner capacity/cost for agentic Copilot code review workloads.

## HoneyDrunk implications
- Use `queue: max` for deploy pipelines where canceling pending runs is wrong and sequential delivery matters.
- Pin runner labels for production release workflows before June 2026 migrations; use default labels only after smoke tests pass on the new images.
- Add a CI audit for workflows that assume macOS 15, Visual Studio 2022, or specific Arm64 image package versions.

## Confidence and quality notes
- Quality posture: decision-usable for CI/CD scheduling and runner-image migration planning.
- Weak spots: vendor changelog source; verify exact YAML syntax against GitHub docs before bulk migration.
- Privacy filter: no private repository or runner details copied.

## 2026-05-24 compile additions

### Claims
- GitHub's Issues navigation modernization used a local-first architecture with IndexedDB caching, preheating, in-memory layers, and service workers to reduce perceived latency and make repeated issue views feel instant. confidence: 1 GitHub engineering source, last-confirmed 2026-05-24. [source: raw/2026-05-24-rss-tldr-devops-from-latency-to-instant-modernizing-github-issues-navigati.md]
- The GitHub source reports many React navigation paths loading under 200 ms after the modernization, while remaining hard navigation bottlenecks are tied to JavaScript boot and server rendering. confidence: 1 GitHub engineering source, last-confirmed 2026-05-24. [source: raw/2026-05-24-rss-tldr-devops-from-latency-to-instant-modernizing-github-issues-navigati.md]

### Typed entities
- product: GitHub Issues
- browser storage: IndexedDB
- browser feature: service worker
- architecture pattern: local-first navigation
- concept: preheating
- concept: perceived latency
- framework: React

### Explicit relationships
- Local-first navigation uses IndexedDB, memory caches, preheating, and service workers to reduce repeated-view latency.
- JavaScript boot and server rendering remain bottlenecks even after client-side cache layers improve navigation.

### HoneyDrunk implications
- For issue/task-heavy internal tools, cache issue/task shells and recently visited data locally before optimizing server endpoints.
- Measure perceived navigation latency separately from backend latency; users feel route transitions, boot cost, and hydration, not only API timings.

## 2026-05-30 compile additions

### Claims
- GitHub Code Quality Repository Enablement API is in public preview on github.com, adding `PATCH /repos/{owner}/{repo}/code-quality/setup` to enable/disable default setup, configure languages, and choose runner type, plus `GET /repos/{owner}/{repo}/code-quality/setup` to retrieve state, languages, runner type, and analysis schedule. confidence: 1 GitHub changelog source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-github-changelog-github-code-quality-repository-enablement-api.md]
- The repository enablement API supports `csharp`, `go`, `java-kotlin`, `javascript-typescript`, `python`, and `ruby`, and is not available on GitHub Enterprise Server during this preview. confidence: 1 GitHub changelog source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-github-changelog-github-code-quality-repository-enablement-api.md]
- GitHub code coverage metrics on pull requests are in public preview for GitHub Code Quality users on github.com; teams upload Cobertura reports from CI using `upload-code-coverage`, and GitHub Apps/Actions need the new fine-grained `code-quality:write` permission. confidence: 1 GitHub changelog source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-github-changelog-code-coverage-on-pull-requests-is-now-in-public-previ.md]
- GitHub Code Quality is available for GitHub Enterprise Cloud and Team and free during preview, but not yet available on GitHub Enterprise Server. confidence: 1 GitHub changelog source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-github-changelog-code-coverage-on-pull-requests-is-now-in-public-previ.md]

### Typed entities
- product: GitHub Code Quality
- API: `PATCH /repos/{owner}/{repo}/code-quality/setup`
- API: `GET /repos/{owner}/{repo}/code-quality/setup`
- feature: pull request code coverage
- report format: Cobertura
- action: `upload-code-coverage`
- permission: `code-quality:write`
- languages: C#, Go, Java/Kotlin, JavaScript/TypeScript, Python, Ruby

### Explicit relationships
- GitHub Code Quality Repository Enablement API uses repository-level configuration to automate static analysis rollout.
- Pull request coverage depends-on CI-generated Cobertura reports and `code-quality:write` upload permission.
- Code Quality preview features complement existing CI checks but do not supersede local test and coverage gates until preview behavior is validated.

### HoneyDrunk implications
- Audit which HoneyDrunk repos could enable Code Quality centrally, especially C# and TypeScript repos.
- If coverage is adopted, upload least-privilege Cobertura reports from existing CI and avoid broad permissions where `code-quality:write` is enough.

## 2026-06-01 compile additions

### Claims
- Datadog's CI/CD threat matrix treats pipeline resources, SCM settings, runners, caches, artifacts, secrets, branch protections, and deployment credentials as an attack surface that should be threat-modeled separately from application runtime security. confidence: 1 vendor security source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-ci-cd-security-threat-modeling-using-a-mitre-style-threat-matrix.md]
- The example CI/CD attack path moves from public repo reconnaissance to PR-triggered CI execution, malicious pipeline configuration, credential access, exfiltration, and cryptomining impact. confidence: 1 source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-ci-cd-security-threat-modeling-using-a-mitre-style-threat-matrix.md]
- AWS's OPA policy-as-code article shows preventive IaC checks running in CI/CD before deployment and retaining validation artifacts to support release decisions and audit review. confidence: 1 AWS security source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-governing-infrastructure-as-code-using-pattern-based-policy-as-code.md]

### Typed entities
- framework: CI/CD threat matrix
- concept: pipeline trust boundary
- control: OPA policy gate
- artifact: validation report
- threat: malicious pipeline configuration
- threat: credential exfiltration from CI

### Explicit relationships
- GitHub Actions security depends-on SCM, branch protection, runner, cache, artifact, secret, and cloud-permission configuration together.
- Policy-as-code gates complement GitHub Actions governance by blocking risky infrastructure changes before deployment.

### HoneyDrunk implications
- Extend GitHub Actions audits beyond YAML syntax: model who can change workflows, what credentials a run can reach, where caches/artifacts cross trust boundaries, and whether PRs can execute with write permissions.
- Save policy validation outputs as release evidence for infrastructure changes.

## 2026-06-02 compile additions

### Claims
- CodeQL 2.25.5 improves GitHub Actions query accuracy by extending `poisonable_steps` modeling to additional sinks, including scripts executed through Python modules and `go run` in directories. confidence: 1 GitHub changelog source, last-confirmed 2026-06-02. [source: raw/2026-06-02-web-github-changelog-codeql-2-25-5-improves-query-accuracy-for-github-acti.md]
- CodeQL 2.25.5 updates `actions/unpinned-tag` so it analyzes composite action metadata files (`action.yml` and `action.yaml`) as well as workflow files. confidence: 1 GitHub changelog source, last-confirmed 2026-06-02. [source: raw/2026-06-02-web-github-changelog-codeql-2-25-5-improves-query-accuracy-for-github-acti.md]
- CodeQL 2.25.5 reduces selected false positives in C/C++ cleartext-transmission and Java/Kotlin Zip Slip queries by improving sink modeling, including distinguishing read-only path sinks. confidence: 1 GitHub changelog source, last-confirmed 2026-06-02. [source: raw/2026-06-02-web-github-changelog-codeql-2-25-5-improves-query-accuracy-for-github-acti.md]
- GitHub says CodeQL 2.25.5 is automatically deployed to github.com code scanning users and will be included in GHES 3.22; older GHES users can manually upgrade CodeQL. confidence: 1 GitHub changelog source, last-confirmed 2026-06-02. [source: raw/2026-06-02-web-github-changelog-codeql-2-25-5-improves-query-accuracy-for-github-acti.md]
- GitHub's 2026-06-01 Copilot billing release lets organization admins configure a default Actions runner for Copilot code review across repositories, making Copilot review runner choice an org-level CI operations setting. confidence: 1 GitHub changelog source, last-confirmed 2026-06-02. [source: raw/2026-06-02-web-github-changelog-updates-to-github-copilot-billing-and-plans.md; page: [[github-copilot-and-app-token-changes]]]

### Typed entities
- tool: CodeQL 2.25.5
- query model: `poisonable_steps`
- query: `actions/unpinned-tag`
- file: `action.yml`
- file: `action.yaml`
- product: GitHub Enterprise Server 3.22
- control: default Actions runner for Copilot code review

### Explicit relationships
- Composite action metadata participates in unpinned-tag risk, not only workflow YAML.
- CodeQL query accuracy depends-on sink modeling; improved sinks reduce both missed GitHub Actions risks and irrelevant alerts.
- Copilot code review uses Actions runner infrastructure, so runner defaults belong in CI governance.

### HoneyDrunk implications
- Include composite actions in GitHub Actions pinning audits.
- If HoneyDrunk uses GHES before 3.22, verify CodeQL version manually before expecting these GitHub Actions detections.
- Choose Copilot code-review runners deliberately if review traffic grows; runner class affects cost, isolation, and throughput.

## 2026-06-04 compile additions

### Claims
- GitHub Actions now shows Agentic Workflow markdown configs directly in the Actions run summary for agentic workflows, reducing page switching and preserving the exact config used for the run. confidence: 1 GitHub changelog source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-github-changelog-actions-view-agentic-workflow-configs-in-the-actions-.md]
- The Red Hat/Miasma package compromise report reinforces that GitHub Actions workflow permissions, OIDC trusted publishing, and package release workflows form one supply-chain trust boundary. confidence: 1 security-news source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-bleepingcomputer-red-hat-npm-packages-compromised-to-steal-developer-c.md; page: [[ai-coding-agent-security]]]

### Typed entities
- feature: GitHub Agentic Workflow run-summary config view
- artifact: agentic workflow markdown config
- platform: GitHub Actions
- control: OIDC trusted publishing
- permission: `id-token: write`

### Explicit relationships
- Agentic workflow review depends-on seeing the exact markdown configuration used during a run.
- GitHub Actions OIDC trusted publishing depends-on strict workflow permissions and repository write controls.
- Run-summary visibility complements, but does not replace, CODEOWNERS/review on agentic workflow configs.

### HoneyDrunk implications
- Treat agentic workflow markdown as executable CI configuration: require code review, CODEOWNERS, and run-summary inspection for high-risk workflows.
- Include agentic workflow configs in CI/security audits alongside `.github/workflows`, composite actions, and publish scripts.

## 2026-06-07 compile additions

### Claims
- CodeQL 2.25.6 adds Swift 6.3.2 analysis support, completes C# 14 and .NET 10 extractor/runtime data-flow support, and adds source/sink models for Apache Avro and `scanf_s`-family functions. confidence: 1 GitHub changelog source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-codeql-2-25-6-adds-swift-6-3-2-support-and-improves-c-coverage.md]
- CodeQL 2.25.6 changes GitHub Actions queries: `actions/untrusted-checkout/critical` alerts now appear at checkout points and may reopen previously closed alerts; `actions/unpinned-tag` recognizes 64-character SHA-256 commit hashes as pinned references; Bash regex validation recognition improved for SHA-1/SHA-256 and alphanumeric checks. confidence: 1 GitHub changelog source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-codeql-2-25-6-adds-swift-6-3-2-support-and-improves-c-coverage.md]
- Fix with Copilot for failing Actions makes Copilot cloud-agent CI repair available from workflow logs for Pro, Pro+, and Max users, turning CI failure remediation into an agentic Actions-adjacent workflow. confidence: 1 GitHub changelog source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-fix-with-copilot-for-failing-actions-now-in-pro-pro-and-max.md]

### Typed entities
- tool: CodeQL 2.25.6
- language/runtime: Swift 6.3.2
- language/runtime: C# 14
- platform/runtime: .NET 10
- query: `actions/untrusted-checkout/critical`
- query: `actions/unpinned-tag`
- feature: Fix with Copilot
- product: Copilot cloud agent

### Explicit relationships
- CodeQL language coverage depends-on extractor support and generated runtime models.
- CodeQL query changes can reopen alerts when alert locations or pinning heuristics change.
- Fix with Copilot depends-on Actions logs and Copilot cloud-agent execution, so it belongs in CI operations governance.

### HoneyDrunk implications
- Expect possible CodeQL alert churn after 2.25.6, especially for untrusted checkout and sensitive-data logging queries.
- Include SHA-256-pinned actions in pinning policy and update any internal scanners that only recognize SHA-1 pins.
- Do not let one-click CI repair bypass normal branch protection or human review.

### Quality notes
- GitHub changelog source is authoritative for feature existence. Verify GHES/manual CodeQL upgrade timing if not on github.com code scanning.

## 2026-06-08 compile additions

### Claims
- Copilot code review now supports repository agent skills and MCP server connections in public preview, bringing issue tracking, documentation, service catalogs, incident tooling, and internal standards into review context when configured. confidence: 1 GitHub changelog source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-shape-copilot-code-review-around-your-team.md; page: [[github-copilot-and-app-token-changes]]]
- Copilot code review adds a Medium analysis tier that admins can set per repository, trading higher AI Credit cost for deeper review of complex logic, security-sensitive code, and cross-service changes. confidence: 1 GitHub changelog source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-shape-copilot-code-review-around-your-team.md]
- The same GitHub source says configurable Actions workflows control the compute and environment Copilot uses for review, and shared configuration applies across Copilot code review and Copilot cloud agent. confidence: 1 GitHub changelog source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-shape-copilot-code-review-around-your-team.md]
- VS Code Copilot terminal changes include automatic retry of network-dependent sandbox commands with broader network permissions while keeping filesystem protections, which makes sandbox permission escalation visible as an agent workflow concern. confidence: 1 GitHub changelog source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-github-copilot-in-visual-studio-code-may-releases.md]

### Typed entities
- product: Copilot code review
- feature: review effort level
- tier: Low
- tier: Medium
- directory: `.github/skills`
- file: `SKILL.md`
- protocol: Model Context Protocol
- control: configurable Actions workflow
- control: sandbox network-permission retry

### Explicit relationships
- Copilot code review depends-on Actions runner/workflow configuration when repository context and custom compute are used.
- Medium review tier supersedes Low only when review depth justifies higher AI Credit spend.
- Shared Copilot cloud-agent and code-review configuration means MCP/tool changes can affect both automation and PR review.
- Sandbox network escalation complements filesystem protection but should be auditable because broader network access can change exfiltration risk.

### HoneyDrunk implications
- Treat Copilot review skills/MCP config like CI configuration: CODEOWNERS, review, provenance, secrets handling, and rollback.
- Use Medium review only for repositories or PR classes where subtle bugs/security/cross-service reasoning justify cost; keep docs/simple repos on Low.
- Audit shared Copilot configuration before enabling code review so review agents do not inherit tools meant for separate cloud-agent tasks.

### Quality notes
- GitHub changelog source is authoritative for preview feature existence. Verify repository settings, billing impact, and runner behavior before rollout.

## 2026-06-10 compile additions: inactive scans, agent validation, and HF Jobs CI

### Source-backed claims
- GitHub code scanning can now keep scheduled scans running for repositories with no pushes or pull requests for six months or more, provided those repositories use code scanning default setup. When enabled at the organization level, inactive repositories are scanned every 30 days. Source: `raw/2026-06-10-web-github-changelog-periodic-code-scanning-of-inactive-repositories-github-changelog.md`. confidence: 1 source, last-confirmed 2026-06-10.
- GitHub's generally available third-party coding-agent validation automatically analyzes agent-authored code with CodeQL, dependency advisory checks, and secret scanning when repository settings permit it. Source: `raw/2026-06-10-web-github-changelog-security-validation-for-third-party-coding-agents-github-changelog.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Hugging Face published a GitHub Actions bridge that starts ephemeral Hugging Face Jobs self-hosted runners from signed GitHub `workflow_job.queued` webhooks, allowing workflows to use labels such as `hf-jobs-cpu-upgrade` or `hf-jobs-t4-small` while GitHub Actions remains the control plane. Source: `raw/2026-06-10-web-hugging-face-migrating-your-github-ci-to-hugging-face-jobs.md`. confidence: 1 source, last-confirmed 2026-06-10.
- The Hugging Face Jobs CI pattern relies on a dispatcher GitHub App, short-lived runner registration tokens, a Hugging Face token stored as a Space secret, and one-shot ephemeral runner Jobs that report status back to GitHub before exiting. Source: `raw/2026-06-10-web-hugging-face-migrating-your-github-ci-to-hugging-face-jobs.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Hugging Face reports Trackio CPU CI ran about 30% faster than GitHub-hosted runners and that a GPU `t4-small` suite ran for less than one cent in the cited example; these are project-specific vendor measurements. Source: `raw/2026-06-10-web-hugging-face-migrating-your-github-ci-to-hugging-face-jobs.md`. confidence: 1 source, last-confirmed 2026-06-10.

### Typed entities
- project: GitHub code scanning
- project: GitHub Actions
- project: Hugging Face Jobs
- project: huggingface/jobs-actions
- project: Trackio
- concept: ephemeral self-hosted runner
- decision: whether HoneyDrunk should run GPU or faster CPU CI on Hugging Face Jobs

### Explicit relationships
- Periodic inactive-repository scanning depends-on code scanning default setup.
- Third-party coding-agent validation uses existing Copilot validation-tool settings.
- Hugging Face Jobs CI depends-on GitHub Actions webhooks, a dispatcher Space, short-lived runner tokens, and ephemeral Jobs.
- Hugging Face Jobs can replace GitHub-hosted runner execution while preserving GitHub Actions workflow orchestration.

### HoneyDrunk implications
- Enable periodic scans only after confirming repos use default setup and that scan cadence/noise is acceptable.
- Evaluate HF Jobs for GPU-heavy or slow CPU suites, but review token handling, dispatcher uptime, webhook verification, runner isolation, and cost limits first.
- Keep required GitHub branch checks authoritative even if agent validation or HF Jobs adds earlier feedback.

### Quality notes
- GitHub and Hugging Face are primary/vendor sources. HF Jobs performance numbers are not transferable without local CI measurements.

## 2026-06-12 compile additions: Agentic Workflows public preview and runner images

### Source-backed claims
- GitHub Agentic Workflows is in public preview and compiles natural-language Markdown automation definitions into standard GitHub Actions YAML, reusing existing runner groups and policy constraints. Source: `raw/2026-06-12-web-github-changelog-github-agentic-workflows-is-now-in-public-preview-github-chan.md`. confidence: 1 GitHub changelog source, last-confirmed 2026-06-12.
- GitHub describes Agentic Workflows safeguards including read-only default permissions, integrity filter rules, sandboxed container execution behind the Agent Workflow Firewall, safe outputs validation, and a threat-detection job before proposed changes are applied. Source: `raw/2026-06-12-web-github-changelog-github-agentic-workflows-is-now-in-public-preview-github-chan.md`. confidence: 1 GitHub changelog source, last-confirmed 2026-06-12.
- Agentic Workflows can now use the built-in `GITHUB_TOKEN` instead of a long-lived personal access token, with organization billing enabled through Copilot policy and `copilot-requests: write` workflow permissions. Source: `raw/2026-06-12-web-github-changelog-agentic-workflows-no-longer-need-a-personal-access-token-gith.md`. confidence: 1 GitHub changelog source, last-confirmed 2026-06-12.
- Pull requests created by `github-actions[bot]` can run CI/CD workflows after approval by a user with write access, reducing the risk that bot-created changes merge without CI while still gating sensitive workflow execution. Source: `raw/2026-06-12-web-github-changelog-bot-created-pull-requests-can-run-workflows-if-approved-githu.md`. confidence: 1 GitHub changelog source, last-confirmed 2026-06-12.
- GitHub-hosted runner images `ubuntu-26.04`, `ubuntu-26.04-arm`, and `windows-11-vs2026-arm` are available in public preview; the existing `windows-11-arm` label is planned to migrate to the VS 2026 image after the preview period in early September. Source: `raw/2026-06-12-web-github-changelog-new-runner-images-in-public-preview-github-changelog.md`. confidence: 1 GitHub changelog source, last-confirmed 2026-06-12.

### Typed entities
- product: GitHub Agentic Workflows
- platform: GitHub Actions
- token: `GITHUB_TOKEN`
- permission: `copilot-requests: write`
- actor: `github-actions[bot]`
- runner image: `ubuntu-26.04`
- runner image: `ubuntu-26.04-arm`
- runner image: `windows-11-vs2026-arm`
- runner label: `windows-11-arm`
- control: Agent Workflow Firewall
- control: safe outputs validation

### Explicit relationships
- Agentic Workflows uses GitHub Actions as the execution/control plane for reasoning-based automations.
- `GITHUB_TOKEN` supersedes long-lived PATs for supported Agentic Workflows authentication.
- Bot-created PR CI execution depends-on explicit user approval to avoid automatic sensitive workflow execution.
- Preview runner images complement migration testing and should not silently supersede pinned production release images.

### HoneyDrunk implications
- Treat Agentic Workflow Markdown as executable CI configuration: require review, CODEOWNERS, permission review, lockfile review, and cost policy.
- Prefer `GITHUB_TOKEN` over PATs for GitHub-native automations where feature support is sufficient; long-lived PATs should become exceptions.
- Audit bot-created PR workflows so approval requirements do not leave generated PRs mergeable without required checks.
- Test `ubuntu-26.04` and `windows-11-vs2026-arm` in non-release workflows before any default-label migration affects production CI.

### Quality notes
- GitHub changelog sources are authoritative for preview feature existence. Public-preview behavior, pricing, and lockfile semantics need live verification before policy rollout.

## 2026-06-14 compile additions: CI trigger controls and self-hosted runner enforcement

### Source-backed claims
- CNCF's Cilium CI/CD hardening writeup describes an Ariane bot pattern where only verified organization members can trigger expensive or privileged workflows from PR comments, and the trigger-to-workflow mapping is hand-allowlisted. Source: `raw/2026-06-14-rss-cncf-securing-ci-cd-for-an-open-source-project-controlling-who-runs-wh.md`. confidence: 1 CNCF/project source, last-confirmed 2026-06-14.
- Cilium uses a two-phase checkout pattern for remaining `pull_request_target` workflows: trusted base-branch code loads workflow/composite-action logic first, then untrusted PR code is checked out only as build context, with no scripts or composite actions loaded from the untrusted checkout. Source: `raw/2026-06-14-rss-cncf-securing-ci-cd-for-an-open-source-project-controlling-who-runs-wh.md`. confidence: 1 source, last-confirmed 2026-06-14.
- Cilium protects CI configuration with CODEOWNERS so changes under `.github/`, workflow files, and CI automation config require review from security/CI-owner teams. Source: `raw/2026-06-14-rss-cncf-securing-ci-cd-for-an-open-source-project-controlling-who-runs-wh.md`. confidence: 1 source, last-confirmed 2026-06-14.
- GitHub Actions is resuming minimum-version enforcement for self-hosted runners on github.com and GitHub Enterprise Cloud with Data Residency: runners must be at least `2.329.0` to register with the new platform and must install each new runner release within 30 days to keep executing jobs. Source: `raw/2026-06-14-rss-github-changelog-actions-github-actions-minimum-version-enforcement-ti.md`. confidence: 1 GitHub changelog source, last-confirmed 2026-06-14.
- GitHub says full enforcement begins on 2026-07-31 for GitHub Enterprise Cloud with Data Residency and on 2026-09-25 for GitHub Enterprise Cloud, with temporary brownouts before those dates. Source: `raw/2026-06-14-rss-github-changelog-actions-github-actions-minimum-version-enforcement-ti.md`. confidence: 1 GitHub changelog source, last-confirmed 2026-06-14.
- GitHub added runner version data to REST/audit-log surfaces for runner inventory and upgrade planning, but audit-log registration events are not a complete inventory of all connected runners. Source: `raw/2026-06-14-rss-github-changelog-actions-github-actions-minimum-version-enforcement-ti.md`. confidence: 1 GitHub changelog source, last-confirmed 2026-06-14.
- SafeDep's Miasma analysis reinforces that custom GitHub Actions, semver action tags, OIDC trusted publishing, deployment environments, and workflow permissions can be attacked as one supply-chain surface when credentials or repository write access are compromised. Source: `raw/2026-06-14-rss-safedep-inside-the-miasma-software-supply-chain-attack-toolkit-real-ti.md`. confidence: 1 security-research source, last-confirmed 2026-06-14.

### Typed entities
- project: Cilium
- bot: Ariane
- workflow trigger: PR comment `/test`
- pattern: two-phase checkout
- trigger: `pull_request_target`
- control: CODEOWNERS for `.github/`
- platform: GitHub Actions self-hosted runners
- runner version: `2.329.0`
- enforcement date: 2026-07-31 GitHub Enterprise Cloud with Data Residency
- enforcement date: 2026-09-25 GitHub Enterprise Cloud
- control: runner auto-update
- threat: semver action tag hijacking
- control: OIDC trusted publishing

### Explicit relationships
- Comment-triggered CI depends-on identity checks and a hand-curated workflow allowlist to avoid arbitrary external users triggering expensive or privileged jobs.
- `pull_request_target` workflows depend-on a strict boundary between trusted workflow logic and untrusted PR content.
- CODEOWNERS complements workflow review by ensuring CI/security owners see changes to automation code.
- Self-hosted runner reliability depends-on runner binary freshness, not just successful historical registration.
- Runner brownouts are an early warning mechanism before enforcement blocks registration or job execution.
- Action tag integrity, deployment environments, OIDC tokens, and workflow permissions form one CI supply-chain trust boundary.

### HoneyDrunk implications
- Audit HoneyDrunk comment-triggered workflows for trigger identity, allowed workflow set, dependency workflows, and cost/credential blast radius.
- Keep any `pull_request_target` workflow under a documented trusted/untrusted checkout boundary; scanners are noisy, so the workflow should explain why the pattern is safe if retained.
- Add or verify CODEOWNERS coverage for `.github/`, workflows, composite actions, reusable workflows, agentic workflow configs, and CI trigger bot config.
- Inventory self-hosted runners now and ensure auto-update or a manual upgrade cadence satisfies GitHub's 30-day runner update requirement before the 2026 enforcement windows.
- Treat action version tags as mutable supply-chain assets. Prefer SHA pinning or internal controlled action mirrors for high-impact workflows.

### Privacy and quality notes
- Privacy filter: SafeDep attack mechanics were reduced to CI control classes; no exploit strings or destructive instructions were copied.
- Quality posture: GitHub changelog is authoritative for enforcement timing. CNCF/Cilium is strong practice evidence but should be adapted to HoneyDrunk's smaller repo/fleet scale.

## 2026-06-16 compile additions: deterministic Terraform auto-apply

### Source-backed claims
- Ricard Bejarano argues that Terraform plan review can bottleneck at higher velocity, but AI review cannot fully replace deterministic production infrastructure review because it is nondeterministic, may violate audit requirements, and weakens accountability. Source: `raw/2026-06-16-web-bejarano-safe-terraform-auto-apply-with-conftest.md`. confidence: 1 practitioner source, last-confirmed 2026-06-16.
- The source describes exporting Terraform plans to JSON and using conftest/Open Policy Agent/Rego to deterministically allow or deny auto-apply based on explicit policy such as allowed actions, resource types, changed fields, blast-radius thresholds, and environment tags. Source: `raw/2026-06-16-web-bejarano-safe-terraform-auto-apply-with-conftest.md`. confidence: 1 practitioner source, last-confirmed 2026-06-16.
- The source frames deterministic policy-as-code gates as increasingly important when AI agents can propose or execute infrastructure changes, because an auditable policy boundary can preserve both velocity and confidence. Source: `raw/2026-06-16-web-bejarano-safe-terraform-auto-apply-with-conftest.md`. confidence: 1 practitioner source, last-confirmed 2026-06-16.

### Typed entities
- tool: Terraform
- tool: conftest
- engine: Open Policy Agent / OPA
- language: Rego
- artifact: Terraform plan JSON
- control: policy-as-code auto-apply gate
- concept: infrastructure blast radius

### Explicit relationships
- Terraform auto-apply safety depends-on explicit structured policy, not free-form review impressions.
- Conftest uses OPA/Rego to evaluate Terraform plan JSON before apply.
- AI infrastructure agents increase the value of deterministic plan gates because agent judgment does not satisfy reproducibility or accountability by itself.

### HoneyDrunk implications
- If HoneyDrunk adds Terraform automation, start with deny-by-default plan JSON policies and allow only low-blast-radius changes with versioned tests.
- Keep human approval for production updates/deletes, IAM/security changes, database/network changes, or large blast-radius plans until policy evidence justifies narrower automation.
- Include the policy result, plan summary, and responsible human/agent identity in run receipts.

### Quality notes
- Practitioner source with concrete pattern. Validate against HoneyDrunk providers and Terraform module conventions before enabling auto-apply.

## 2026-06-17 compile additions: Code Quality GA and Copilot metric coverage

### Source-backed claims
- GitHub Code Quality is scheduled to become generally available as a paid product on 2026-07-20, priced at $10 per active committer per month on enabled repositories plus usage-based billing for AI-powered capabilities such as Copilot code review, AI-assisted detection, and Copilot Autofix. Source: `raw/2026-06-17-web-github-blog-github-code-quality-generally-available-july-20-2026-github-changelog.md`. confidence: 1 GitHub changelog source, last-confirmed 2026-06-17.
- Deterministic CodeQL maintainability and reliability scans for Code Quality consume GitHub Actions minutes rather than AI usage charges. Source: `raw/2026-06-17-web-github-blog-github-code-quality-generally-available-july-20-2026-github-changelog.md`. confidence: 1 source, last-confirmed 2026-06-17.
- Code Quality GA adds organization-wide deployment, organization-level dashboards, coverage enforcement through rulesets, quality scoring, and APIs for enablement and finding management; it is available for GitHub Enterprise Cloud and Team, not GitHub Enterprise Server. Source: `raw/2026-06-17-web-github-blog-github-code-quality-generally-available-july-20-2026-github-changelog.md`. confidence: 1 source, last-confirmed 2026-06-17.
- GitHub Copilot usage metrics now include server-side telemetry in addition to client-side IDE/client telemetry, increasing active-user and DAU coverage when client telemetry is missing. Source: `raw/2026-06-17-web-github-blog-copilot-usage-metrics-now-include-more-of-your-active-users-github-changelog.md`. confidence: 1 GitHub changelog source, last-confirmed 2026-06-17.
- Server-side Copilot telemetry currently improves top-level active-user counts but does not yet provide the rich per-interaction breakdowns such as IDE, feature, model, and lines-of-code activity, so more usage can appear unattributed in dimensional reports. Source: `raw/2026-06-17-web-github-blog-copilot-usage-metrics-now-include-more-of-your-active-users-github-changelog.md`. confidence: 1 source, last-confirmed 2026-06-17.

### Typed entities
- product: GitHub Code Quality
- feature: Code Quality quality gates
- feature: Code Quality coverage rulesets
- feature: Code Quality APIs
- tool: CodeQL
- product: GitHub Copilot usage metrics API
- signal: server-side Copilot telemetry
- metric: daily active users / DAU

### Explicit relationships
- Code Quality billing depends-on enabled repositories and active committers, while AI-powered features add usage-based consumption.
- Deterministic CodeQL analysis complements AI-powered code-quality review by consuming Actions minutes rather than model usage.
- Copilot usage metrics now combine client and server telemetry, reducing missing-user gaps but increasing unattributed activity until richer server-side dimensions land.

### HoneyDrunk implications
- Before 2026-07-20, decide which HoneyDrunk repos should keep Code Quality enabled and what active-committer cost envelope is acceptable.
- Treat Copilot usage reports before and after this telemetry change as non-identical time series; DAU may rise because reporting improved, not because behavior changed.
- For code-quality gates, separate deterministic CodeQL/coverage rules from AI review spend so CI costs and model usage are budgeted independently.

### Quality notes
- GitHub changelog sources are authoritative for GitHub product timing and pricing as captured. Billing and availability can change; recheck before procurement or org-wide enablement.

## 2026-06-19 compile additions: trigger admission, Copilot review instructions, and unsafe checkout defaults

### Source-backed claims
- GitHub workflow execution protections are in public preview for enterprises, organizations, and repositories, using rulesets to allow or block workflow triggers by actor and event before a run starts. Source: `raw/2026-06-19-web-github-blog-control-who-and-what-triggers-github-actions-workflows.md`. confidence: 1 GitHub changelog source, last-confirmed 2026-06-19.
- Actor rules can distinguish users, repository roles, GitHub Apps, Copilot, and Dependabot; event rules can permit or block events such as `push`, `pull_request`, `pull_request_target`, and `workflow_dispatch`. Source: `raw/2026-06-19-web-github-blog-control-who-and-what-triggers-github-actions-workflows.md`. confidence: 1 source, last-confirmed 2026-06-19.
- `actions/checkout` v7 refuses fork pull request head or merge commits in `pull_request_target` and selected fork-PR `workflow_run` contexts by default, with an explicit `allow-unsafe-pr-checkout` opt-out for reviewed exceptions. Source: `raw/2026-06-19-web-github-blog-safer-pull-request-target-defaults-for-github-actions-checkout.md`. confidence: 1 GitHub changelog source, last-confirmed 2026-06-19.
- GitHub says same-repository pull requests and ordinary `pull_request` event behavior are not changed by the `actions/checkout` v7 protection, and manual checkout of untrusted code with `git` or `gh` remains outside the protection. Source: `raw/2026-06-19-web-github-blog-safer-pull-request-target-defaults-for-github-actions-checkout.md`. confidence: 1 source, last-confirmed 2026-06-19.
- Copilot code review now reads root-level `AGENTS.md` files automatically and uses relevant instructions when generating review feedback; the change is generally available. Source: `raw/2026-06-19-web-github-blog-copilot-code-review-agents-md-support-and-ui-improvements.md`; page: [[github-copilot-and-app-token-changes]]. confidence: 1 GitHub changelog source, last-confirmed 2026-06-19.

### Typed entities
- feature: GitHub workflow execution protections
- framework: GitHub rulesets
- rule type: actor rule
- rule type: event rule
- event: `pull_request_target`
- event: `workflow_dispatch`
- action: `actions/checkout` v7
- input: `allow-unsafe-pr-checkout`
- file: `AGENTS.md`
- product: Copilot code review

### Explicit relationships
- Workflow execution protections use central rulesets to supersede per-workflow trigger trust for covered actor/event admission.
- `actions/checkout` v7 prevents one common pwn-request pattern but does not block all untrusted code execution inside privileged events.
- `allow-unsafe-pr-checkout` creates an explicit review marker for privileged fork-PR checkout exceptions.
- Copilot code review depends-on repository-level `AGENTS.md` context for convention-aware review feedback.

### HoneyDrunk implications
- Put workflow execution protections into evaluate mode for HoneyDrunk org/repo policies before enforcement so blocked runs are visible without breaking CI.
- Search for `pull_request_target`, `workflow_run`, `github.event.pull_request.head.sha`, `refs/pull/`, and `allow-unsafe-pr-checkout` before July 2026 backport behavior changes affect workflows.
- Treat `AGENTS.md` as review-runtime policy because GitHub Copilot now consumes it directly.

### Quality notes
- GitHub changelog sources are authoritative for feature existence. Public-preview controls and checkout backport behavior should be verified live before org-wide policy changes.
