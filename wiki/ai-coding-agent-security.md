# AI Coding Agent Security

## Decision-useful summary
AI coding agents should be treated as high-capability execution principals, not chat helpers. Docker's 2026 security survey/post argues that the recurring failure pattern is architectural: agents inherit the user's filesystem, secrets, network, and production privileges, then act autonomously on probabilistic judgments. The practical HoneyDrunk decision is to put safety in the execution layer: workspace-scoped sandboxes, blocked credential paths, scoped identities, network egress controls, human approval gates for irreversible actions, and audit logs. [source: raw/2026-05-20-rss-docker-blog-coding-agent-horror-stories-the-security-crisis-threatenin.md]

## Claims
- AI coding agents run an observe-plan-act-repeat loop and may read files, run commands, write/deploy code, query databases, send messages, and call APIs under the permissions available in the launching environment. confidence: 1 source, last-confirmed 2026-05-20. [source: raw/2026-05-20-rss-docker-blog-coding-agent-horror-stories-the-security-crisis-threatenin.md]
- Docker identifies six recurring coding-agent risk categories: unrestricted filesystem access, excessive privilege inheritance, secrets leakage via agent context, prompt injection through ingested content, malicious skills/plugin supply chain, and autonomous action without human-in-the-loop. confidence: 1 source, last-confirmed 2026-05-20. [source: raw/2026-05-20-rss-docker-blog-coding-agent-horror-stories-the-security-crisis-threatenin.md]
- Natural-language directives such as “do not delete” are not security boundaries; irreversible actions need platform-level enforcement that the model cannot reason around. confidence: 1 source, last-confirmed 2026-05-20. [source: raw/2026-05-20-rss-docker-blog-coding-agent-horror-stories-the-security-crisis-threatenin.md]
- The post positions Docker Sandboxes / `sbx` as a microVM-based mitigation layer with workspace scoping, blocked credential-path mounts, network egress policies, git worktree isolation, proxy-injected secrets, resource caps, and audit logs. confidence: 1 vendor source, last-confirmed 2026-05-20. [source: raw/2026-05-20-rss-docker-blog-coding-agent-horror-stories-the-security-crisis-threatenin.md]
- The post cites multiple public incidents and studies, but several incident details are secondary/vendor-collected and should be verified from primary reports before being used as procurement-grade evidence. confidence: 1 vendor roundup source, last-confirmed 2026-05-20. [source: raw/2026-05-20-rss-docker-blog-coding-agent-horror-stories-the-security-crisis-threatenin.md]

## Typed entities
- concept: AI coding agent
- concept: agent execution principal
- concept: workspace-scoped execution
- concept: excessive privilege inheritance
- concept: prompt injection
- concept: agent skill/plugin supply chain
- product: Docker Sandboxes
- CLI/tool: sbx
- isolation type: microVM
- tool/product mentioned: Claude Code
- tool/product mentioned: Claude Cowork
- tool/product mentioned: Cursor
- tool/product mentioned: Replit Agent
- tool/product mentioned: Amazon Kiro
- tool/product mentioned: Google Antigravity
- threat: secrets leakage
- threat: malicious skills
- control: human-in-the-loop approval gate
- control: network egress policy
- control: blocked credential paths

## Explicit relationships
- AI coding agents use the launching user's ambient permissions unless given a separate scoped identity.
- Agent autonomy depends-on execution-layer controls when filesystem, secrets, network, production, or messaging tools are reachable.
- Prompt injection plus private data access plus external communication creates exfiltration risk.
- Malicious skills/plugins exploit the same trust boundary as the agent runtime because they run with agent-level permissions.
- Docker Sandboxes uses microVM isolation to constrain filesystem and network blast radius; this complements, not supersedes, least-privilege identity and human approvals.
- Natural-language safety instructions contradict reliable security enforcement when the underlying tool layer still permits destructive action.

## HoneyDrunk implications
- Default agent work should run in a scoped workspace with recoverable file operations and no ambient access to home-directory credentials.
- Treat agent identity as separate from Oleg/Honeyclaw identity wherever production/cloud access exists; use short-lived scoped tokens and audit logs.
- Require explicit approval gates outside the model for deletion, production database writes, public/external messaging, payments, and deployment.
- If Docker Sandboxes/sbx is evaluated, benchmark it against OpenClaw needs: Windows support, git worktree behavior, network policy ergonomics, secret injection model, and local dev speed.

## Confidence and quality notes
- Quality posture: decision-usable as a threat model and mitigation checklist, but vendor-authored and framed around Docker Sandboxes; validate tooling claims and incident details independently before buying/building around `sbx`.
- Privacy filter: raw contained public incident/person references; wiki retained only decision-relevant public names/tool names and did not copy secrets-like payloads beyond generic control descriptions.

## 2026-05-22 compile additions

### Claims
- Docker Gordon is a local-container workflow agent with broad shell, filesystem, Docker CLI, docs, and web capabilities, but every command/file/Docker operation is shown for explicit approval before running and permissions reset at session close. confidence: 1 vendor source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-docker-blog-meet-gordon-docker-s-ai-agent-for-your-entire-container-wo.md]
- Docker states Gordon does not store code or personal information and says its AI providers do not retain user data, with processing running on SOC 2 Type 2 and ISO 27001 certified infrastructure; this is vendor assurance and should be validated against current terms before sensitive use. confidence: 1 vendor source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-docker-blog-meet-gordon-docker-s-ai-agent-for-your-entire-container-wo.md]
- C#'s planned caller-unsafe model turns memory-unsafety into an explicit compile-time/API-contract surface, which is useful for detecting AI-generated unsafe API calls and dependency surfaces before runtime. confidence: 1 source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-net-blog-improving-c-memory-safety.md; page: [[csharp-memory-safety-and-unsafe-code]]]

### Typed entities
- product: Docker Gordon
- control: explicit approval gate
- control: session-scoped permission
- assurance: SOC 2 Type 2
- assurance: ISO 27001
- language/runtime: C# / .NET
- control: compiler-enforced unsafe blocking

### Explicit relationships
- Docker Gordon's approval model mitigates surprise actions but depends-on user judgment and clear command previews.
- Vendor privacy assurances do not supersede HoneyDrunk's need for data-classification and local secrecy rules.
- Compiler unsafe enforcement complements agent sandboxing by blocking a class of unsafe generated code at build time.

### HoneyDrunk implications
- Do not enable auto-approve for Gordon or similar agents on repos with production credentials, broad filesystem access, or destructive Docker commands until sandbox/network/secret policies are proven.
- Add .NET unsafe policy checks to coding-agent review gates when C# 16/.NET 11 tooling becomes available.

## 2026-05-23 compile additions

### Claims
- Microsoft open-sourced RAMPART and Clarity for AI-agent security during development: RAMPART is a Pytest-native adversarial/benign test framework built on PyRIT with an agent adapter, while Clarity pressure-tests design assumptions before implementation. confidence: 1 source, last-confirmed 2026-05-23. [source: raw/2026-05-22-rss-tldr-infosec-microsoft-open-sources-rampart-and-clarity-to-secure-ai-a.md]
- A Hacker News summary reports GitHub investigated TeamPCP claims that a compromised employee device and poisoned VS Code extension exposed ~3,800 internal repositories, and that the same group trojanized Microsoft's `durabletask` PyPI package to steal cloud/vault/SSH/Kubernetes credentials; treat as security-news evidence requiring primary verification before procurement-grade claims. confidence: 1 secondary source, last-confirmed 2026-05-23. [source: raw/2026-05-22-rss-tldr-infosec-github-breached-employee-device-hack-led-to-exfiltration-.md]
- A GitHub Actions cache-poisoning analysis says recurring open-source supply-chain attacks chain unsafe `pull_request_target`, untrusted input interpolation, cache poisoning, third-party actions pinned to mutable tags, broad publish credentials, and weak package-manager/npm protections. confidence: 1 practitioner source, last-confirmed 2026-05-23. [source: raw/2026-05-23-rss-tldr-infosec-github-actions-cache-poisoning-is-eating-open-source-18-m.md]
- The same cache-poisoning source recommends removing `pull_request_target` workflows that check out PR code, isolating caches in release-capable workflows, pinning third-party actions by commit SHA, treating AI-agent config files as source code, adding `zizmor`/`actionlint`, CODEOWNERS on `.github/`, OIDC trusted publishing, non-SMS 2FA, and package-manager install cooldowns. confidence: 1 practitioner source, last-confirmed 2026-05-23. [source: raw/2026-05-23-rss-tldr-infosec-github-actions-cache-poisoning-is-eating-open-source-18-m.md]
- Kaspersky GReAT disclosed ExifTool CVE-2026-3102 affecting macOS users on ExifTool 13.49 and earlier when `-n`/`-printConv` is used; unsanitized metadata could reach a `system()` sink and execute commands with the invoking user's privileges. confidence: 1 security-research source, last-confirmed 2026-05-23. [source: raw/2026-05-23-rss-tldr-infosec-how-an-image-could-compromise-your-mac-understanding-an-e.md]

### Typed entities
- tool/framework: RAMPART
- tool/framework: Clarity
- framework: PyRIT
- test framework: Pytest
- platform: GitHub Actions
- threat: cache poisoning
- threat: poisoned VS Code extension
- package: durabletask PyPI package
- tool: ExifTool
- vulnerability: CVE-2026-3102
- tool: zizmor
- tool: actionlint
- control: OIDC trusted publishing
- control: CODEOWNERS on `.github/`
- control: commit-SHA action pinning

### Explicit relationships
- RAMPART uses PyRIT and Pytest to move agent red-team testing into development-time CI.
- Clarity complements RAMPART by testing design assumptions before code exists.
- GitHub Actions cache poisoning depends-on writable caches and release-capable credentials crossing trust boundaries.
- Commit-SHA pinning, cache isolation, OIDC trusted publishing, CODEOWNERS, and linting mitigate CI supply-chain compromise.
- ExifTool CVE-2026-3102 is caused by unsanitized metadata reaching a shell-command sink on macOS when machine-readable conversion is used.

### HoneyDrunk implications
- Add RAMPART/Clarity-style agent abuse tests to any agent that can read secrets, call tools, or emit external actions.
- Audit HoneyDrunk GitHub Actions for `pull_request_target`, mutable action tags, release-workflow caches, `.github/` ownership, npm/package publish credentials, and AI-agent config files.
- Treat image/media metadata parsing as an execution risk in asset pipelines; pin/patch ExifTool and sandbox media-processing tools.

### Confidential-container platform controls
- CNCF's CoCo/Kyverno article says Confidential Containers treat the Kubernetes control plane as untrusted and require workload bootstrap data such as runtimeClass, initdata, image policy, attestation server details, and optional sealed secrets/sidecars to be verified by the runtime environment. confidence: 1 CNCF source, last-confirmed 2026-05-23. [source: raw/2026-05-22-rss-tldr-devops-automating-confidential-containers-coco-infrastructure-wit.md]
- Kyverno can mutate and validate Kubernetes resources at admission time to inject/validate CoCo infrastructure requirements, reducing developer friction and catching malformed confidential-workload inputs earlier; this does not remove the trust paradox that Kyverno itself runs in the untrusted control plane. confidence: 1 CNCF source, last-confirmed 2026-05-23. [source: raw/2026-05-22-rss-tldr-devops-automating-confidential-containers-coco-infrastructure-wit.md]

Typed entities added: project: Confidential Containers / CoCo; tool: Kyverno; concept: remote attestation; concept: initdata; control: sealed secrets; control: admission-time mutation/validation.

Relationships added: CoCo workloads depend-on remote attestation and runtime-side verification because the Kubernetes control plane is untrusted; Kyverno policy-as-code complements CoCo by automating required configuration but does not supersede runtime attestation.

## 2026-05-24 compile additions

### Claims
- git-pkgs/proxy is a package-registry caching proxy with a configurable version-cooldown feature that hides newly published versions from package-manager metadata until they age past a global/ecosystem/package threshold, reducing exposure to fast-moving supply-chain attacks. confidence: 1 GitHub repo source, last-confirmed 2026-05-24. [source: raw/2026-05-24-rss-tldr-infosec-git-pkgs-proxy-github-repo.md]
- git-pkgs/proxy currently documents cooldown support for npm, Cargo, RubyGems, Hex, pub.dev, PyPI, NuGet, Composer, and Conda; several other ecosystems are listed as incomplete or without timestamp support. confidence: 1 GitHub repo source, last-confirmed 2026-05-24. [source: raw/2026-05-24-rss-tldr-infosec-git-pkgs-proxy-github-repo.md]
- SafeDep reports the Megalodon campaign pushed 5,718 malicious commits to 5,561 GitHub repositories in roughly six hours on 2026-05-18, injecting GitHub Actions workflows with base64-encoded bash payloads that exfiltrate CI secrets, cloud credentials, SSH keys, OIDC tokens, and source-code secrets to a C2 endpoint. confidence: 1 security-research source, last-confirmed 2026-05-24. [source: raw/2026-05-24-rss-tldr-infosec-megalodon-mass-github-repo-backdooring-via-ci-workflows-1.md]
- SafeDep identifies two Megalodon workflow variants: a mass `SysDiag` workflow triggered on push and pull requests, and a targeted `Optimize-Build` workflow using `workflow_dispatch` to create dormant on-demand backdoors. confidence: 1 security-research source, last-confirmed 2026-05-24. [source: raw/2026-05-24-rss-tldr-infosec-megalodon-mass-github-repo-backdooring-via-ci-workflows-1.md]
- SafeDep reports `@tiledesk/tiledesk-server` npm versions 2.18.6 through 2.18.12 carried the targeted Megalodon variant after a compromised GitHub repository was published by a legitimate maintainer; the npm account itself was not described as directly compromised. confidence: 1 security-research source, last-confirmed 2026-05-24. [source: raw/2026-05-24-rss-tldr-infosec-megalodon-mass-github-repo-backdooring-via-ci-workflows-1.md]

### Typed entities
- project/tool: git-pkgs/proxy
- control: package version cooldown
- package ecosystems: npm, Cargo, RubyGems, Hex, pub.dev, PyPI, NuGet, Composer, Conda
- campaign: Megalodon
- platform: GitHub Actions
- malicious workflow: SysDiag
- malicious workflow: Optimize-Build
- npm package: `@tiledesk/tiledesk-server`
- compromised versions: 2.18.6 through 2.18.12
- threat: CI secret exfiltration
- credential type: GitHub Actions OIDC token
- credential type: cloud credentials
- credential type: SSH private keys

### Explicit relationships
- Package cooldown proxies mitigate fast supply-chain attacks by delaying newly published versions before automated consumers can resolve them.
- Version-cooldown controls depend-on registries exposing trustworthy publish timestamps.
- Megalodon used compromised repository write access to inject CI workflows, which caused downstream npm package compromise when legitimate publishes included poisoned workflow files.
- `pull_request_target`, broad `id-token: write`, workflow write access, and CI secret exposure amplify malicious-workflow blast radius.

### HoneyDrunk implications
- Add package-install cooldown/proxying to the dependency-security option list for high-risk repos, especially npm/NuGet/PyPI automation; validate developer-friction and lockfile behavior before enforcing globally.
- Audit HoneyDrunk repos for unexpected workflow additions/renames, `workflow_dispatch`-only dormant workflows, broad `id-token: write`, and commits that look like generic CI maintenance from bot-like authors.
- Treat package publishing from GitHub source as a trust chain: repository compromise can produce legitimate package releases even when registry credentials remain intact.

### Privacy and quality notes
- Privacy filter: campaign indicators are summarized at control/checklist level; the raw C2 IP and redacted/garbled email addresses were not copied into the wiki.

## 2026-05-26 compile additions

### Claims
- ITPro reports GitHub confirmed roughly 3,800 internal repositories were exfiltrated after a developer installed a malicious VS Code extension; GitHub said customer repositories were not impacted outside internal repositories, while some internal repos may contain customer-support excerpts. confidence: 1 trade-press source quoting GitHub, last-confirmed 2026-05-26. [source: raw/2026-05-26-rss-tldr-devops-github-internal-repositories-exfiltrated-via-malicious-vs-.md]
- GitHub reportedly began rotating critical secrets, prioritizing highest-impact credentials, and continued log analysis/monitoring after the breach. confidence: 1 trade-press source quoting GitHub, last-confirmed 2026-05-26. [source: raw/2026-05-26-rss-tldr-devops-github-internal-repositories-exfiltrated-via-malicious-vs-.md]
- GitHub's npm staged publishing is generally available in npm CLI 11.15.0+: CI can upload a package to a stage queue, but a maintainer must approve with a 2FA challenge before the package version becomes installable. confidence: 1 GitHub changelog source, last-confirmed 2026-05-26. [source: raw/2026-05-26-rss-tldr-infosec-staged-publishing-and-new-install-time-controls-for-npm-2.md]
- npm CLI 11.15.0 adds install source allowlist flags `--allow-file`, `--allow-remote`, and `--allow-directory`, complementing `--allow-git`; each can be set to `all` or `none`, with stricter defaults planned for `--allow-git` in npm v12. confidence: 1 GitHub changelog source, last-confirmed 2026-05-26. [source: raw/2026-05-26-rss-tldr-infosec-staged-publishing-and-new-install-time-controls-for-npm-2.md]

### Typed entities
- platform: GitHub
- threat actor: TeamPCP
- threat: malicious VS Code extension
- platform/tool: VS Code Marketplace
- package manager: npm CLI 11.15.0
- control: npm staged publishing
- control: trusted publishing with OIDC
- control: 2FA maintainer approval
- flag: `--allow-file`
- flag: `--allow-remote`
- flag: `--allow-directory`
- flag: `--allow-git`
- control: install source allowlist

### Explicit relationships
- Malicious developer extensions can cause internal source exfiltration by abusing trusted IDE/dev-tool access.
- Secret rotation, log analysis, and infrastructure monitoring mitigate post-exfiltration credential blast radius.
- npm staged publishing uses human 2FA approval to add proof-of-presence before registry release, including non-interactive CI/OIDC publishing flows.
- npm install source allowlists reduce nonregistry dependency-source risk by rejecting local, remote URL, directory, or Git installs unless explicitly allowed.

### HoneyDrunk implications
- Treat IDE extensions as supply-chain code with repo/credential blast radius; pin/approve extension sets for sensitive development environments.
- For any HoneyDrunk npm package publishing, prefer trusted publishing plus staged publishing from CI, with maintainer approval from a trusted device.
- Add `.npmrc`/policy checks for nonregistry install sources in high-risk repos; default-deny remote URL/Git/local sources where lockfiles do not require them.

### Quality notes
- The GitHub breach report is trade-press and should be backed by GitHub's final incident report before procurement-grade claims. GitHub npm changelog is primary source.

## 2026-05-30 compile additions

### Claims
- GitHub expanded organization-level OIDC support for Dependabot and code scanning private registries to include Cloudsmith and Google Artifact Registry, alongside AWS CodeArtifact, Azure DevOps Artifacts, and JFrog Artifactory; the feature is GA on github.com and planned for GitHub Enterprise Server 3.22. confidence: 1 GitHub changelog source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-github-changelog-expanded-oidc-support-for-dependabot-and-code-scannin.md]
- GitHub secret scanning approval-request lists can now be sorted by newest, oldest, recently updated, and least recently updated at repository, organization, and enterprise levels for push-protection bypass and alert-dismissal requests. confidence: 1 GitHub changelog source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-github-changelog-filter-secret-scanning-approval-requests-by-sort-orde.md]
- The secret scanning alerts REST API now accepts an `is_bypassed` boolean query parameter on repository, organization, and enterprise list endpoints to include or exclude push-protection-bypassed alerts programmatically. confidence: 1 GitHub changelog source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-github-changelog-filter-secret-scanning-approval-requests-by-sort-orde.md]
- GitHub Code Quality coverage uploads require the new fine-grained `code-quality:write` permission, reinforcing least-privilege CI token design for new quality/security telemetry uploads. confidence: 1 GitHub changelog source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-github-changelog-code-coverage-on-pull-requests-is-now-in-public-previ.md; page: [[github-actions-platform-operations]]]

### Typed entities
- platform: Dependabot
- feature: code scanning
- protocol: OpenID Connect / OIDC
- registry: Cloudsmith
- registry: Google Artifact Registry
- registry: AWS CodeArtifact
- registry: Azure DevOps Artifacts
- registry: JFrog Artifactory
- feature: secret scanning push protection
- REST API parameter: `is_bypassed`
- permission: `code-quality:write`

### Explicit relationships
- OIDC private-registry authentication supersedes long-lived registry credentials where supported.
- Secret scanning bypass filters depend-on alert metadata and help security teams prioritize bypassed secrets at scale.
- `code-quality:write` complements least-privilege GitHub Actions permissions for quality telemetry.

### HoneyDrunk implications
- Prefer OIDC-based private-registry access for Dependabot/code scanning rather than static registry secrets wherever supported.
- Add a periodic secret-scanning report for `is_bypassed=true` alerts if HoneyDrunk uses GitHub Advanced Security.
- Keep quality-report upload tokens narrow; do not reuse broad repo/write credentials for Code Quality coverage uploads.

## 2026-05-31 compile additions

### Claims
- Docker's sandboxing comparison says chroot provides filesystem isolation but weak process isolation, systemd-nspawn adds process and network isolation on Linux, containers provide broad portability but Docker-in-Docker often weakens isolation through privileged mode or host-daemon access, and traditional VMs provide strong isolation at higher startup/resource cost. confidence: 1 vendor/community source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-docker-blog-comparing-different-approaches-to-sandboxing.md]
- Docker positions microVM-based Sandboxes as a local agent isolation layer with dedicated guest kernels, isolated networks, and per-sandbox Docker Engines so agent-run Docker commands cannot see the host daemon or other sandbox daemons. confidence: 2 Docker sources, last-confirmed 2026-05-31. [sources: raw/2026-05-31-rss-docker-blog-comparing-different-approaches-to-sandboxing.md; raw/2026-05-31-rss-docker-blog-the-untrusted-autonomous-workload-how-ai-coding-agents-res.md]
- Docker's untrusted-autonomous-workload article says the sandbox's shared workspace remains a deliberate trust boundary: agents can still modify project files that later execute on the host, including Git hooks, package scripts, CI config, IDE tasks, Makefiles, and pre-commit config. confidence: 1 vendor/community source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-docker-blog-the-untrusted-autonomous-workload-how-ai-coding-agents-res.md]
- Docker's network proxy design blocks UDP/ICMP, requires explicit rules for non-HTTP TCP, filters outbound HTTP/HTTPS by policy, and can inject credentials from the host keychain so secrets do not enter the VM; broad allowed domains remain possible exfiltration channels. confidence: 1 vendor/community source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-docker-blog-the-untrusted-autonomous-workload-how-ai-coding-agents-res.md]
- Anthropic frames agent containment around three defense layers: the environment, the model, and external content. It says environmental controls such as sandboxes, VMs, filesystem boundaries, egress controls, and scoped credentials are the deterministic blast-radius limit when model-layer defenses miss. confidence: 1 official vendor source, last-confirmed 2026-05-31. [source: raw/2026-05-31-web-anthropic-engineering-how-we-contain-claude-across-products.md]
- Anthropic reports Claude Code approval fatigue: users approved roughly 93% of prompts, and adding an OS-level sandbox reduced permission prompts by 84%; auto mode is framed as defense-in-depth, not a substitute for sandboxing. confidence: 1 official vendor source, last-confirmed 2026-05-31. [source: raw/2026-05-31-web-anthropic-engineering-how-we-contain-claude-across-products.md]
- Anthropic's Claude Code incidents show that project-local config, hooks, and localhost listeners must not execute before a folder trust prompt; parsing and execution of untrusted project config should be deferred until after trust is established. confidence: 1 official vendor source, last-confirmed 2026-05-31. [source: raw/2026-05-31-web-anthropic-engineering-how-we-contain-claude-across-products.md]
- Anthropic's Claude Cowork allowlist incident shows domain allowlists are capability grants, not just destination filters: allowing a trusted API domain can still permit data exfiltration to an attacker-controlled account unless token provenance, request class, and upload capabilities are constrained. confidence: 1 official vendor source, last-confirmed 2026-05-31. [source: raw/2026-05-31-web-anthropic-engineering-how-we-contain-claude-across-products.md]
- Fowler/Thoughtworks' VibeSec article argues that telling an AI to be secure is not enough; security rules need versioned context files plus deterministic sensors such as SAST, credential scanning, infrastructure validation, dependency checks, and secure-by-default templates. confidence: 1 Thoughtworks/Fowler source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-martin-fowler-the-vibesec-reckoning.md; page: [[ai-assisted-software-practice]]]

### Typed entities
- isolation: chroot
- isolation: systemd-nspawn
- isolation: container
- isolation: virtual machine
- isolation: microVM
- product: Docker Sandboxes / `sbx`
- component: per-sandbox Docker Engine
- control: egress proxy
- control: host-keychain credential injection
- product: Claude Code auto mode
- product: Claude Cowork
- control: folder trust prompt
- threat: pre-trust project config execution
- threat: domain-allowlist exfiltration
- concept: security context file
- control: deterministic security sensor

### Explicit relationships
- MicroVM sandboxes supersede plain containers when an autonomous agent needs its own Docker daemon and broad command execution.
- Sandbox workspace sharing contradicts a belief that VM isolation alone makes agent output safe; host-executed project files still require review.
- Domain allowlists depend-on capability analysis because allowed domains may expose upload, messaging, or arbitrary-content features.
- Security context files guide agent behavior but depend-on computational sensors and deployment gates for enforcement.
- Human approval gates degrade under approval fatigue and should be backed by environment-layer controls.

### HoneyDrunk implications
- Audit OpenClaw/Honeyclaw agent sessions for host-executed workspace artifacts after agent work: `.git/hooks`, package scripts, CI workflows, IDE tasks, Makefiles, pre-commit hooks, and launch profiles.
- Treat MCP/API allowlists as capability grants. For each allowed domain, document whether upload, arbitrary posting, webhooks, or account-switching could become exfiltration paths.
- If adopting Docker Sandboxes or similar, test not only build speed but shared-workspace review, Git worktree use, page-size quirks on Apple Silicon, Windows behavior, EDR visibility, and network-policy ergonomics.
- Add a HoneyDrunk security context file only with matching gates; prompt rules without scanners and policy checks are advisory, not enforcement.

## 2026-06-01 compile additions

### Claims
- Sysdig TRT reports observing an LLM-agent-driven post-compromise intrusion on 2026-05-10: an internet-reachable marimo notebook was compromised via CVE-2026-39987, cloud credentials were harvested, AWS Secrets Manager was queried for an SSH key, and an internal PostgreSQL database was dumped through a bastion. confidence: 1 security-research source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-ai-agent-at-the-wheel-how-an-attacker-used-llms-to-move-from-a-cve-to-.md]
- Sysdig's evidence for agent-driven execution includes real-time improvisation, a leaked planning comment, command shapes optimized for machine parsing, and value handoffs lifted from prior tool output; this is stronger than generic "automation happened" evidence but still a vendor incident analysis. confidence: 1 source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-ai-agent-at-the-wheel-how-an-attacker-used-llms-to-move-from-a-cve-to-.md]
- The Sysdig incident reinforces that per-source-IP detection can fail when attackers fan requests through edge-worker infrastructure; detection must correlate credentials, request timing, API patterns, and downstream session behavior rather than source IP alone. confidence: 1 source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-ai-agent-at-the-wheel-how-an-attacker-used-llms-to-move-from-a-cve-to-.md]
- Datadog's CI/CD threat matrix maps CI/CD-specific attack paths across MITRE-style stages such as reconnaissance, initial access, execution, persistence, privilege escalation, defense evasion, credential access, lateral movement, exfiltration, and impact. confidence: 1 vendor security source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-ci-cd-security-threat-modeling-using-a-mitre-style-threat-matrix.md]
- AWS's pattern-based policy-as-code source recommends organizing OPA/IaC checks around recurring control patterns such as required metadata, allowed configuration, exposure restriction, protection enforcement, and privilege constraint, then running them as preventive CI/CD gates with retained validation artifacts. confidence: 1 AWS security source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-governing-infrastructure-as-code-using-pattern-based-policy-as-code.md]

### Typed entities
- organization: Sysdig Threat Research Team / TRT
- vulnerability: CVE-2026-39987
- project: marimo notebook
- service: AWS Secrets Manager
- service: PostgreSQL
- infrastructure: SSH bastion
- threat technique: edge-worker egress fan-out
- framework: MITRE ATT&CK-style CI/CD threat matrix
- platform: CI/CD pipeline
- policy engine: Open Policy Agent / OPA
- concept: pattern-based policy as code

### Explicit relationships
- LLM-assisted intrusion uses agentic planning and tool-output handoff to accelerate post-compromise pivoting.
- Agent-driven attacker speed depends-on defenders correlating cross-system state, not only individual command strings or source IPs.
- CI/CD threat modeling depends-on mapping pipeline inputs, identities, secrets, artifacts, caches, runners, and deployment permissions as trust boundaries.
- OPA policy-as-code gates complement CI/CD threat modeling by converting known infrastructure risks into preventive delivery checks.

### HoneyDrunk implications
- Treat agent-security controls as dual-use: the same harness capabilities that help defenders can accelerate attackers after initial access.
- Add CI/CD threat modeling to GitHub Actions audits: PR execution permissions, pipeline config writes, secrets, caches, artifact promotion, runner images, and cloud credentials.
- Promote recurring IaC security rules into OPA/checkov-style gates with saved validation artifacts for later audit.

### Privacy and quality notes
- Privacy filter: exploit commands and secret-like values from the incident were summarized at behavior/control level rather than copied as runnable payloads.

## 2026-06-02 compile additions

### Claims
- Hackread/Cyderes report a fake-Anthropic SEO-poisoning campaign targeting first-time Claude Code users with a ClickFix-style lure: users are instructed to run a Windows command that launches a fileless infostealer chain through Windows script tooling and PowerShell. confidence: 1 security-news source citing Cyderes, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-hackread-fake-anthropic-sites-deliver-fileless-infostealer-to-claude-c.md]
- The same campaign is useful as a defensive lesson rather than a payload source: developer onboarding pages, install commands, and search results for AI tools are now credential-theft surfaces; defenders should prefer official install docs, block risky script-host execution where possible, and monitor unusual script-host outbound behavior. confidence: 1 source plus compile judgment, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-hackread-fake-anthropic-sites-deliver-fileless-infostealer-to-claude-c.md]
- LLMReaper demonstrates that browser extensions with page access can read AI conversation DOM content in real time across Claude, ChatGPT, and Gemini, including prompts, responses, titles, and platform user metadata; the attack does not require compromising the AI provider. confidence: 1 researcher PoC source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-lohitya-pushkar-thewhiteh4t-llmreaper-dom-based-ai-conversation-exfilt.md]
- LLMReaper maps the extension risk to masquerading, web portal capture, exfiltration over a command channel, supply-chain compromise, and credentials-from-browser-content techniques; the practical control is treating AI conversations as sensitive browser content and restricting extensions/profiles accordingly. confidence: 1 researcher PoC source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-lohitya-pushkar-thewhiteh4t-llmreaper-dom-based-ai-conversation-exfilt.md]
- Microsoft Tech Community's OpenClaw-on-AKS article argues that standard shared-kernel containers are too thin a boundary for adversarial agent code, and recommends Kata microVM isolation on AKS node pools with `kata-vm-isolation` runtime class, Azure Files persistent storage, and Application Gateway ingress as a stronger defense-in-depth design. confidence: 1 Microsoft community source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-microsoft-tech-community-hardening-openclaw-on-aks-mitigating-containe.md]

### Typed entities
- threat: fake Anthropic / fake Claude Code installer
- technique: SEO poisoning
- technique: ClickFix lure
- threat: fileless infostealer
- tool/runtime: Windows script host / PowerShell
- project/PoC: LLMReaper
- platform: browser extension
- browser API: MutationObserver
- target surfaces: Claude, ChatGPT, Gemini
- isolation: Kata Containers
- isolation: microVM
- platform: Azure Kubernetes Service / AKS
- runtime class: `kata-vm-isolation`
- storage: Azure Files

### Explicit relationships
- Fake installer campaigns exploit AI-tool adoption by turning search/install workflows into credential-theft paths.
- Browser extensions can exfiltrate AI conversation content because LLM chat prompts and responses are rendered in the page DOM.
- Browser profile isolation and extension allowlists mitigate AI-chat exfiltration risk; provider-side privacy controls do not prevent local extension reads.
- Kata microVM isolation supersedes plain container isolation when OpenClaw-style workloads execute untrusted or high-permission agent code.
- MicroVM isolation complements, but does not replace, scoped credentials, egress control, workspace review, and host-executed artifact checks.

### HoneyDrunk implications
- Do not install Claude Code, Codex, or similar agent tools from search-result commands or unofficial mirrors; use official docs and pinned install paths.
- Treat browser extensions as repo/credential access: use a minimal extension profile for AI chat and never paste credentials or private repo excerpts into browsers with unreviewed extensions.
- If OpenClaw moves to AKS, evaluate Kata/runtime-class support, nested-virtualization node SKUs, persistent workspace behavior, and egress/audit policy before relying on agent execution.

### Privacy and quality notes
- Privacy filter: public malware infrastructure, keys, and command strings were not copied into the wiki; the campaign was reduced to defensive behavior and control lessons.
- Quality posture: Hackread is secondary reporting; use Cyderes or other primary technical reporting before treating campaign details as incident-grade evidence. LLMReaper is a PoC and should be used for awareness/control design, not as a production exploit reference.

## 2026-06-03 compile additions

### Claims
- Ammar Askar disclosed a github.dev / VS Code webview bug where untrusted notebook/webview JavaScript could simulate trusted VS Code keybindings, install or activate extension behavior, and expose the broad GitHub OAuth token used by github.dev; the durable control lesson is that browser IDEs and webviews are high-value token-bearing surfaces. confidence: 1 security-research source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-ammar-askar-1-click-github-token-stealing-via-a-vscode-bug.md]
- Askar's source says the github.dev token was not scoped to the opened repository, so compromise could expose private repositories beyond the lure repository; avoid repo-specific trust assumptions for browser-IDE sessions unless token scope is verified. confidence: 1 security-research source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-ammar-askar-1-click-github-token-stealing-via-a-vscode-bug.md]
- Flatt Security's Claude Code GitHub Actions research found an `agent`-mode permission bypass in which GitHub App actors could trigger workflows intended for write/admin users; Anthropic fixed the issue in Claude Code GitHub Actions v1.0.94 by rejecting GitHub App triggers by default. confidence: 1 security-research source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-flatt-security-poisoning-claude-code-one-github-issue-to-break-the-sup.md]
- Flatt also warns that `allowed_non_write_users: "*"` is unsafe when Claude Code workflows expose secrets, write permissions, or exfiltration-capable tools; even seemingly narrow issue-triage workflows can become stepping stones if they can edit issues, post summaries, call GitHub CLI, or reach OIDC token material. confidence: 1 security-research source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-flatt-security-poisoning-claude-code-one-github-issue-to-break-the-sup.md]
- AWS's software-supply-chain security post frames package-consumer defense around temporary credentials, least privilege, defense in depth, artifact signing, centralized dependency management, provenance attestations, continuous scanning, SBOMs, and centralized logging/monitoring. confidence: 1 AWS Security Blog source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-aws-security-blog-well-architected-best-practices-for-software-supply-.md]
- AWS explicitly notes that CVE-only scanners may miss malicious packages before formal identifiers exist; behavioral analysis, community malicious-package feeds, SBOM blast-radius search, and alert routing are needed for fast-moving package-registry attacks. confidence: 1 AWS Security Blog source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-aws-security-blog-well-architected-best-practices-for-software-supply-.md]

### Typed entities
- surface: github.dev
- product: VS Code / VS Code webviews
- threat: browser IDE token theft
- token type: GitHub OAuth token
- product: Claude Code GitHub Actions
- setting: `allowed_non_write_users`
- permission: `id-token: write`
- credential type: GitHub Actions OIDC request credentials
- control: human-actor check
- control: workflow summary suppression
- control: command argument wrapper
- control: temporary credentials
- control: artifact signing
- service: AWS Signer
- service: Amazon CodeArtifact
- service: Amazon ECR
- service: Amazon Inspector
- artifact: SBOM
- standard: npm provenance attestation

### Explicit relationships
- Browser IDEs use OAuth tokens and extension/webview trust boundaries; webview bugs can cause repository-token exfiltration even without desktop RCE.
- Claude Code GitHub Actions depends-on actor validation, least-privilege workflow permissions, scoped secrets, and strict tool allowlists when processing issue or pull-request content.
- `allowed_non_write_users: "*"` contradicts safe handling of untrusted public issue content when secrets or write-capable tools are present.
- OIDC credentials in GitHub Actions can be exchanged for more privileged downstream tokens, so leaking request-token material can supersede ordinary `GITHUB_TOKEN` limits.
- Artifact signing and provenance complement dependency scanning by proving build identity, while malicious-package scanning and SBOMs help detect and scope compromise after publication.

### HoneyDrunk implications
- Treat github.dev, vscode.dev, notebook previews, and browser-based code workspaces as sensitive token surfaces; clear site data and avoid opening untrusted notebook/webview content in authenticated browser IDE sessions until upstream patches and token scoping are verified.
- Audit any Claude Code or similar GitHub Actions workflows for public triggers, `allowed_non_write_users`, `id-token: write`, broad GitHub App permissions, writable issue/PR tools, workflow summaries, and shell/GitHub CLI allowlists.
- For HoneyDrunk package consumers, prefer temporary cloud credentials, OIDC trusted publishing, package provenance checks, centralized dependency proxies, artifact signing, SBOM generation, and alerts that route malicious-package findings as incidents rather than ordinary low-priority CVEs.

### Privacy and quality notes
- Privacy filter: exploit payloads, token-exchange procedure details, and exfiltration examples were reduced to defensive control language. No tokens, malware indicators, or runnable attack sequences were copied into wiki prose.
- Quality posture: Askar and Flatt sources are primary security-research writeups; AWS is vendor-authored but strong for control taxonomy. Validate current VS Code/GitHub/Anthropic mitigation status before treating the historical vulnerabilities as still exploitable.

## 2026-06-04 compile additions

### Claims
- BleepingComputer reports more than 30 npm packages under Red Hat's `@redhat-cloud-services` namespace were compromised in a supply-chain attack distributing a Shai-Hulud-style credential stealer variant called Miasma; Red Hat said the affected packages were internal development tooling and removed them from npm. confidence: 1 security-news source quoting Red Hat/researchers, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-bleepingcomputer-red-hat-npm-packages-compromised-to-steal-developer-c.md]
- The reported Red Hat/Miasma attack path abused a compromised GitHub account, malicious commits, a GitHub Actions workflow, `id-token: write`, npm trusted publishing, and package `preinstall` execution to publish backdoored package versions. confidence: 1 security-news source citing Aikido/OX Security, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-bleepingcomputer-red-hat-npm-packages-compromised-to-steal-developer-c.md]
- Vercel frames inference theft as a high-margin abuse model for internet-facing AI endpoints: attackers wrap custom AI endpoints behind OpenAI/Anthropic-compatible adapters, fan requests through residential proxies, and resell stolen inference. confidence: 1 Vercel source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-vercel-protecting-against-token-theft.md]
- Vercel argues AI endpoint protection needs per-request verification because auth walls and session-level checks are amortized across many stolen inference calls; Vercel reports using BotID deep analysis on every AI request. confidence: 1 Vercel source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-vercel-protecting-against-token-theft.md]
- Thoughtworks' review-gates source reinforces that AI-assisted work should stop at explicit review gates: inner gates after each red-green-refactor test cycle and outer gates at milestone boundaries, with context files updated at stable checkpoints. confidence: 1 Thoughtworks source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-thoughtworks-insights-how-to-implement-effective-review-gates-for-ai-a.md; page: [[ai-assisted-software-practice]]]

### Typed entities
- package namespace: `@redhat-cloud-services`
- malware family/variant: Miasma
- malware family: Shai-Hulud
- permission: `id-token: write`
- control: npm trusted publishing
- package lifecycle hook: `preinstall`
- threat: inference theft
- control: per-request verification
- product/control: Vercel BotID
- pattern: review gate

### Explicit relationships
- Compromised source repositories can cause legitimate package publishes when GitHub Actions and trusted publishing are abused.
- `id-token: write` can amplify package-publishing compromise when workflow permissions and target package lists are not constrained.
- Package install hooks create immediate execution risk for developer workstations and CI runners.
- Inference theft depends-on adapter/proxy infrastructure that turns a victim endpoint into a provider-compatible resale surface.
- Per-request bot verification supersedes session-only checks for high-value AI inference endpoints.
- Review gates complement sandboxing by limiting assumption drift and unreviewed diff size.

### HoneyDrunk implications
- Audit npm/GitHub publishing workflows for `id-token: write`, trusted-publishing package scope, CODEOWNERS on workflow/package files, and install-script risk.
- Treat any package compromise as a credential incident for affected developer/CI environments; rotate reachable tokens rather than only removing the package.
- For public AI endpoints, verify callers at the request that consumes inference, not only at signup or session start.
- Keep AI-code review gates small enough that Oleg/Honeyclaw can actually inspect the diff and tests before the next milestone proceeds.

### Privacy and quality notes
- Privacy filter: payload mechanics, infrastructure indicators, and runnable malware details were summarized at control level and not copied.
- Quality posture: BleepingComputer is secondary reporting; use Red Hat, Aikido, OX Security, and npm/GitHub records for incident-grade follow-up.

## 2026-06-05 compile additions

### Claims
- Docker's practical agent-security overview organizes production AI-agent security into four domains: execution isolation, tool access control, identity/credential management, and runtime monitoring. confidence: 1 Docker source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-how-to-secure-ai-agents-a-practical-overview.md]
- The same source argues permission prompts are not a durable security strategy because approval fatigue scales poorly; infrastructure-level isolation and policy enforcement are stronger controls for autonomous agents. confidence: 1 Docker source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-how-to-secure-ai-agents-a-practical-overview.md]
- Docker recommends task-scoped tool availability, curated/provenance-verified tool registries, review of tool descriptions as well as code, dedicated scoped agent identities, short-lived runtime-injected credentials, and full tool-call decision-chain logging. confidence: 1 Docker source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-how-to-secure-ai-agents-a-practical-overview.md]
- Docker's software supply-chain overview reinforces that build systems, base images, registries, CI/CD pipelines, SBOMs, signing, provenance attestations, vulnerability scans, and deploy-time verification are one continuous trust boundary rather than separate compliance checkboxes. confidence: 1 Docker source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-what-is-software-supply-chain-security.md]
- Calif/Jun Rong reports an HTTP/2 memory-exhaustion attack chain against default HTTP/2 configurations in multiple major servers, combining HPACK header-reference amplification with stalled response flow control; nginx and Apache had public fixes or mitigations, while some affected implementations were still pending fixes at publication time. confidence: 1 primary security-research source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-codex-discovered-a-hidden-http-2-bomb.md]
- The HTTP/2 source's durable defense lesson is that HTTP/2 termination points need both decoded-header-size limits and header-field-count limits, including cookie crumbs, plus bounded stalled-stream lifetime and worker/container memory caps. confidence: 1 primary security-research source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-codex-discovered-a-hidden-http-2-bomb.md]
- GitHub Copilot local/cloud sandboxes add first-party isolated execution options for Copilot shell command execution and cloud tasks, but they do not remove the need for scoped credentials, egress policy, generated-artifact review, and repository workflow safeguards. confidence: 1 GitHub source plus existing page posture, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-cloud-and-local-sandboxes-for-github-copilot-now-in-public-preview.md]

### Typed entities
- control domain: execution isolation
- control domain: tool access control
- control domain: agent identity and credentials
- control domain: runtime monitoring
- threat: tool poisoning
- control: curated tool registry
- control: dedicated scoped agent identity
- artifact: SBOM
- standard: SLSA
- standard: NIST SSDF
- concept: provenance attestation
- vulnerability class: HTTP/2 HPACK memory exhaustion
- protocol: HTTP/2
- compression scheme: HPACK
- server/product: nginx
- server/product: Apache httpd
- server/product: Microsoft IIS
- server/product: Envoy
- server/product: Cloudflare Pingora
- control: header-field-count limit
- control: stalled-stream lifetime bound
- product: GitHub Copilot local/cloud sandboxes

### Explicit relationships
- Agent security depends-on isolation, scoped tools, scoped identity, and monitoring working together; prompts and approvals alone do not enforce the boundary.
- Tool poisoning uses trusted tool metadata as a prompt-injection surface, so tool-description review complements code/provenance review.
- Supply-chain security uses SBOMs, signing, provenance, trusted base images, and registry/deploy policies to verify artifacts at each transition.
- AI coding agents can accelerate vulnerability discovery by composing known attack primitives across codebases.
- HTTP/2 memory exhaustion is caused by HPACK allocation amplification combined with flow-control stalls that keep allocations live.
- Copilot sandboxes complement, but do not supersede, supply-chain and repository-level controls.

### HoneyDrunk implications
- Define a minimum agent-security baseline for OpenClaw/Honeyclaw: disposable isolated workspace, egress allowlist, task-scoped tools, short-lived non-human credentials, and full tool-call audit.
- Add supply-chain controls to agent-generated changes: signed/trusted base images, SBOM generation, dependency provenance, action pinning, and deploy-time image verification where applicable.
- Inventory any HoneyDrunk public HTTP/2 termination points and verify server versions/configuration for header-count, cookie-crumb, stalled-stream, and worker-memory controls.
- Treat first-party Copilot sandboxes as a candidate execution layer, but still inspect generated CI workflows, package scripts, hooks, and dependency changes before host or production execution.

### Privacy and quality notes
- Privacy filter: exploit mechanics were summarized at mitigation/control level; no PoC commands or runnable attack procedure were copied into the wiki.
- Quality posture: Docker sources are vendor-authored but useful control taxonomies. The HTTP/2 source is primary research with active disclosure/patch status that must be checked against current vendor advisories before incident response.

## 2026-06-07 compile additions

### Claims
- Docker's sandbox-security overview frames sandbox security as enforcing isolation boundaries and access controls around sandboxed environments, combining process isolation, system-call filtering, network segmentation, resource limits, runtime monitoring, and audit trails. confidence: 1 Docker source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-what-is-sandbox-security.md]
- Docker contrasts OS-level sandboxing, VM/microVM isolation, and application-level sandboxing: OS-level controls are efficient but share a kernel, VM-based isolation fits multi-tenant or untrusted code at higher cost, and application-level sandboxes should layer on top rather than act as the only boundary. confidence: 1 Docker source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-what-is-sandbox-security.md]
- For AI agents, Docker recommends isolating each tool execution with minimum permissions, exposing only required files/data/environment variables, enforcing egress allowlists, and monitoring file/syscall/network behavior for audit and incident response. confidence: 1 Docker source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-what-is-sandbox-security.md]
- CodeQL 2.25.6 improves sensitive-data heuristics across JavaScript/TypeScript, Python, Swift, and Rust cleartext logging queries, which may surface more credential/private-data handling issues in agent-edited code. confidence: 1 GitHub changelog source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-codeql-2-25-6-adds-swift-6-3-2-support-and-improves-c-coverage.md]

### Typed entities
- concept: sandbox security
- control: process isolation
- control: system call filtering / seccomp
- control: network segmentation
- control: resource limits / cgroups
- control: runtime monitoring
- isolation model: OS-level sandbox
- isolation model: VM/microVM sandbox
- isolation model: application-level sandbox
- tool: CodeQL 2.25.6
- query family: cleartext logging sensitive data

### Explicit relationships
- Sandbox security uses multiple enforcement layers to keep a sandbox from becoming only nominal isolation.
- VM/microVM isolation supersedes shared-kernel containers when code is genuinely untrusted or multi-tenant blast radius matters.
- Application-level sandboxing complements kernel/hypervisor isolation but does not replace it for high-risk agent execution.
- CodeQL sensitive-data detection complements agent review gates by flagging credential/private-data handling that a model may miss.

### HoneyDrunk implications
- Define OpenClaw/Honeyclaw sandbox tiers by trust level: ordinary repo work, untrusted generated code, multi-tenant/cloud execution, and production-adjacent tool use.
- For agent tool execution, enforce egress, visible data, resource limits, and audit outside the model prompt.
- Review new CodeQL sensitive-data alerts after 2.25.6 as possible real findings, not just noise from a query update.

### Privacy and quality notes
- Docker source is vendor-authored and product-positioned, but the control taxonomy is useful. No exploit payloads, secrets, or unsafe indicators were copied.

### Content-safety guardrail note
- NVIDIA's Nemotron 3.5 Content Safety release is a compact 4B multimodal/multilingual safety model with custom policy enforcement, optional concise reasoning traces, and a released safety dataset; it is relevant as a scouting signal for domain-specific guardrails, but benchmark and latency claims are vendor-authored and should not drive production safety policy without local tests. confidence: 1 NVIDIA/Hugging Face source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-nemotron-3-5-content-safety-customizable-multimodal-safety-for-global-.md]

Typed entities added: model: Nemotron 3.5 Content Safety; base model: Gemma 3 4B IT; framework/taxonomy: Aegis 2.0; concept: custom policy enforcement; concept: safety reasoning trace; dataset: Nemotron-3.5-Content-Safety-Dataset.

Relationship added: content-safety guardrails complement execution-layer sandboxing and tool governance by classifying prompts/responses/images against built-in or custom policies, but they do not supersede least-privilege tools, scoped identities, or audit logs.

## 2026-06-08 compile additions

### Claims
- OWASP FinBot CTF is a hands-on Agentic Security Initiative companion to the OWASP GenAI Security Project, simulating a financial-services multi-agent vendor-management platform with real tool access and challenges around prompt injection, tool misuse, policy bypass, data exfiltration, privilege escalation, remote code execution, and MCP tool-server supply-chain attacks. confidence: 1 OWASP GenAI source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-finbot-ctf-is-live-a-hands-on-companion-to-the-owasp-genai-security-pr.md]
- OWASP's Q1 2026 GenAI exploit roundup says major AI-related incidents increasingly target agent identities, orchestration layers, supply chains, prompt-injection paths, and operational trust boundaries rather than only model outputs. confidence: 1 OWASP GenAI roundup source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-owasp-genai-exploit-round-up-report-q1-2026.md]
- The same OWASP roundup notes that many AI security incidents do not map cleanly to CVEs because they arise from misconfiguration, autonomy, trust boundaries, supply-chain compromise, prompt injection, and data-flow manipulation; only classical software flaws such as Flowise CVE-2025-59528 reliably receive CVE tracking. confidence: 1 OWASP GenAI roundup source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-owasp-genai-exploit-round-up-report-q1-2026.md]
- OWASP's MCP Tool Poisoning page describes indirect prompt injection through malicious MCP tool responses: connect-time tool descriptions may look safe, while runtime tool outputs inject instructions into the LLM context and can trigger restricted tools or exfiltration if backend controls are weak. confidence: 1 OWASP security source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-mcp-tool-poisoning.md; page: [[mcp-tool-governance-and-app-surfaces]]]
- Durable MCP tool-poisoning mitigations include approved MCP server allowlists, structured output schemas, output validation/sanitization, least-privilege separation between external and privileged tools, backend tool-access enforcement, and confirmation outside the LLM context for sensitive operations. confidence: 1 OWASP security source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-mcp-tool-poisoning.md]
- OpenAI's TanStack/Mini Shai-Hulud response says two corporate employee devices were impacted, limited credential material was exfiltrated from internal source repositories, signing certificates were rotated as a precaution, macOS OpenAI apps must be updated by 2026-06-12, and OpenAI found no evidence of product, user-data, or IP compromise. confidence: 1 official OpenAI incident-response source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-our-response-to-the-tanstack-npm-supply-chain-attack.md]
- OpenAI's incident controls included system/identity isolation, session revocation, credential rotation, temporary deployment-workflow restrictions, user/credential behavior scrutiny, blocking new notarizations with impacted material, certificate rotation, package-manager controls such as minimum release age, and provenance validation for new packages. confidence: 1 official OpenAI incident-response source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-our-response-to-the-tanstack-npm-supply-chain-attack.md]
- Docker Navigator reinforces that agent execution, hardened images, microVM sandboxes, trusted namespace compromise, VEX-aware scanning, and local-model workflows are converging into one AI-era DevSecOps problem. confidence: 1 Docker newsletter source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-docker-navigator-ai-workflows-container-security-and-build-reliability.md]

### Typed entities
- project: OWASP GenAI Security Project
- project: OWASP Agentic Security Initiative
- platform: OWASP FinBot CTF
- framework: OWASP Top 10 for Agentic Applications 2026
- threat: MCP Tool Poisoning
- protocol: Model Context Protocol
- vulnerability: CVE-2025-59528
- platform/tool: Flowise
- campaign: Mini Shai-Hulud
- library/package family: TanStack npm packages
- organization: OpenAI
- control: minimum release age
- control: package provenance validation
- control: certificate rotation
- product/control: Docker Hardened Images
- control: VEX-aware scanning

### Explicit relationships
- FinBot CTF uses simulated multi-agent financial workflows to make OWASP agentic risks executable and observable.
- MCP Tool Poisoning is caused by a runtime trust gap between reviewed tool metadata and untrusted tool responses.
- Structured MCP outputs and backend tool policies complement prompt-injection detection because free-text injection remains hard to identify reliably.
- Agentic AI incidents often contradict CVE-only vulnerability management; architectural failures need risk registers, controls, and exercises even when no CVE exists.
- Package-manager minimum-age controls and provenance validation mitigate fast-moving dependency compromise before ordinary CVE workflows catch up.
- Certificate rotation supersedes trust in previously exposed signing material even when no malicious signing has been observed.

### HoneyDrunk implications
- Add FinBot or equivalent labs to the candidate training/eval set for anyone building HoneyDrunk agents with tool access.
- Treat MCP server outputs as untrusted data. Approved servers, schema validation, response sanitization, and tool-layer authorization all belong in the baseline.
- Track AI/agent security issues outside CVE feeds: OWASP reports, vendor advisories, package compromise feeds, MCP/tooling disclosures, and incident-response writeups.
- If HoneyDrunk systems run OpenAI macOS apps, update before 2026-06-12 and verify downloads come from official update channels.

### Privacy and quality notes
- Privacy filter: incident details were reduced to control-level posture; no credential material, exploit payloads, malware indicators, or runnable attack examples were copied.
- Quality posture: OWASP/OpenAI sources are high authority for their own materials. OWASP roundup incident details should still be cross-checked against primary reports before incident-grade claims.

## 2026-06-09 compile additions

### Claims
- LangSmith Sandboxes are described as hardware-virtualized microVMs for agent execution, intended to isolate arbitrary model/user/repo/package code while still providing filesystem, shell, package manager, network access, local server preview URLs, snapshots/forks, blueprints, and persistent state. confidence: 1 LangChain source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-give-your-agent-its-own-computer.md]
- LangChain argues containers are insufficient for untrusted agent code because shared-kernel escape risk remains; VM/microVM isolation is the recommended boundary for agents that install arbitrary dependencies or run generated scripts. confidence: 1 vendor security/source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-give-your-agent-its-own-computer.md]
- The LangSmith source's auth-proxy pattern injects credentials at the network layer so secrets do not enter the agent runtime directly, aligning with prior scoped-secret guidance. confidence: 1 source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-give-your-agent-its-own-computer.md]
- Kasra's vulnerable-app experiment shows a common mobile/backend security failure mode: a hardened API can coexist with wide-open Firebase/Firestore or Supabase-style data access, so mobile app security review must inspect embedded service configuration and datastore rules, not only API routes. confidence: 1 practitioner security-eval source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-i-built-a-vulnerable-app-and-spent-1-500-seeing-if-llms-could-hack-it.md]
- The same experiment is weak as a model benchmark because runs were small, costly, harness-dependent, and affected by provider refusal/budget behavior; its stronger signal is that security-agent evaluations need reproducible harnesses, budgets, transcripts, and success criteria. confidence: 1 source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-i-built-a-vulnerable-app-and-spent-1-500-seeing-if-llms-could-hack-it.md; page: [[agent-evaluation-and-benchmarks]]]
- The clearbluejar reproduction of a FreeBSD RPCSEC_GSS CVE reinforces "system over model" for vulnerability research: local open-weight models could find the issue under the right scaffold, but false positives required an added reachability stage to make the output reviewable. confidence: 1 practitioner security-research source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-system-over-model-tested-reproducing-mythos-s-freebsd-find-on-local-op.md; page: [[agent-evaluation-and-benchmarks]]]

### Typed entities
- product: LangSmith Sandboxes
- isolation type: hardware-virtualized microVM
- control: auth proxy
- feature: sandbox snapshot/fork
- service: Firebase / Firestore
- service: Supabase
- vulnerability class: broken access control / missing object-level authorization
- benchmark target: CVE-2026-4747
- project: nano-analyzer
- control: reachability filter
- model family: GPT-OSS-20B
- model family: Gemma 4 31B

### Explicit relationships
- MicroVM execution supersedes shared-kernel containers for untrusted generated code when escape blast radius matters.
- Auth proxies inject credentials outside the model runtime, reducing direct secret exposure.
- Mobile/backend security review depends-on datastore authorization rules as well as API route hardening.
- Vulnerability-research agents depend-on scaffolding, repeated trials, and reachability triage to separate true findings from false positives.

### HoneyDrunk implications
- Keep OpenClaw execution-isolation decisions tied to task risk: dependency installation, generated scripts, cloned repos, or user-submitted code should run in disposable isolated machines.
- Add Firebase/Supabase/datastore-rule checks to mobile app review checklists; API-only review can miss direct client datastore paths.
- When evaluating security agents, count false-positive review burden and require reachability evidence, not just "found a candidate" output.

### Privacy and quality notes
- Privacy filter: exploit details were summarized at vulnerability-class/control level. Practitioner benchmark data is useful for eval design but not procurement-grade model ranking.

## 2026-06-10 compile additions: non-ZDR coding models, agent PR validation, and WASM sandboxing

### Source-backed claims
- Claude Fable 5 introduces a coding-agent privacy exception in Copilot because Anthropic retains prompts and outputs for up to 30 days for safety-classifier and abuse-analysis purposes; GitHub states other Claude Copilot models remain Zero Data Retention. Source: `raw/2026-06-10-web-github-changelog-claude-fable-5-is-generally-available-for-github-copilot-github-changelo.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Anthropic's Fable 5 safeguards can route some sensitive biology, chemistry, cyber, and distillation requests to Opus 4.8, which makes model behavior policy-dependent rather than purely capability-dependent. Source: `raw/2026-06-10-web-anthropic-claude-fable-5-and-claude-mythos-5.md`. confidence: 1 source, last-confirmed 2026-06-10.
- GitHub's third-party coding-agent validation is designed to catch security vulnerabilities, vulnerable newly introduced dependencies, and leaked secrets in agent-authored pull requests before finalization. Source: `raw/2026-06-10-web-github-changelog-security-validation-for-third-party-coding-agents-github-changelog.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Simon Willison's `micropython-wasm` demonstrates an alpha Python-in-WASM sandbox using Wasmtime, memory limits, experimental fuel-based CPU limits, persistent interpreter state through host-function queues, and selected host functions compiled into the WASM blob. Source: `raw/2026-06-10-web-simon-willison-running-python-code-in-a-sandbox-with-micropython-and-wasm.md`. confidence: 1 source, last-confirmed 2026-06-10.
- The `micropython-wasm` author explicitly characterizes the package as alpha and not ready for users unwilling to accept significant security risk. Source: `raw/2026-06-10-web-simon-willison-running-python-code-in-a-sandbox-with-micropython-and-wasm.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Microsoft Foundry gateway guidance frames API gateways as a way to centralize model-level authorization, API-key hiding, routing/failover, throttling, logging, policy, and compliance around model endpoints that otherwise expose resource/project-level access. Source: `raw/2026-06-10-web-microsoft-learn-access-foundry-models-and-other-language-models-through-a-gateway-azure.md`. confidence: 1 source, last-confirmed 2026-06-10.

### Typed entities
- project: Claude Fable 5
- project: GitHub third-party coding-agent validation
- library/tool: CodeQL
- library/tool: Wasmtime
- project: micropython-wasm
- project: Microsoft Foundry
- concept: Zero Data Retention
- concept: WASM sandbox
- decision: sandbox policy for OpenClaw-generated code execution

### Explicit relationships
- Claude Fable 5 contradicts a blanket ZDR assumption for Copilot-hosted Anthropic models.
- GitHub third-party coding-agent validation uses CodeQL, dependency advisory checks, and secret scanning as PR guardrails.
- `micropython-wasm` depends-on Wasmtime and MicroPython compiled to WASI/WASM.
- Foundry gateway patterns mitigate direct client access to broad project/resource model permissions.

### HoneyDrunk implications
- Block non-ZDR coding models from repos containing unreleased game/IP, credentials, customer data, or private partner content unless explicitly approved.
- Treat GitHub agent validation as defense in depth; deterministic tests, branch protection, CODEOWNERS, and secret scanning still remain required.
- Do not adopt `micropython-wasm` for trusted isolation without a dedicated security review, filesystem/network tests, fuel calibration, host-function allowlists, and failure-mode analysis.
- For any Foundry-backed agent app, put model access behind an application/gateway policy surface rather than handing broad project credentials to clients.

### Privacy and quality notes
- Secret examples from sources were summarized generically. No tokens or private prompts were copied. Security controls are date-sensitive and require tenant/repo verification before rollout.

## 2026-06-11 compile additions: MCP threat maturity, tool-chain attacks, Copilot review, and Codex deployment controls

### Source-backed claims
- The Cloud Security Alliance Agentic MCP Security Best Practices draft says MCP security needs defense in depth across authentication, tool integrity, session management, supply-chain validation, execution isolation, behavioral monitoring, and per-invocation verification for high-sensitivity deployments. Source: `raw/2026-06-11-web-cloud-security-alliance-agentic-mcp-security-best-practices-guide.md`. confidence: 1 draft whitepaper source, last-confirmed 2026-06-11.
- The CSA draft maps MCP threats to categories including pre-auth RCE, tool poisoning, rug pulls, session hijacking, supply-chain attacks, cross-tenant information leakage, and insecure tool execution. Source: `raw/2026-06-11-web-cloud-security-alliance-agentic-mcp-security-best-practices-guide.md`. confidence: 1 draft whitepaper source, last-confirmed 2026-06-11.
- CrowdStrike defines agentic tool-chain attacks as reasoning-layer attacks that manipulate tool descriptions, metadata, and context; examples include tool poisoning, tool shadowing, and rugpull attacks. Source: `raw/2026-06-11-web-crowdstrike-how-agentic-tool-chain-attacks-threaten-ai-agent-security.md`. confidence: 1 vendor security source, last-confirmed 2026-06-11.
- CrowdStrike recommends signed manifests, version pinning, metadata audits, mTLS/certificate pinning, pre-execution parameter validation, boundary verification, reasoning telemetry, baseline tracking, and anomaly detection for agentic tool-chain risk. Source: `raw/2026-06-11-web-crowdstrike-how-agentic-tool-chain-attacks-threaten-ai-agent-security.md`. confidence: 1 vendor security source, last-confirmed 2026-06-11.
- GitHub Copilot CLI `/security-review` is an experimental public-preview slash command that analyzes local code changes for high-confidence security findings such as injection, XSS, insecure data handling, path traversal, and weak cryptography; GitHub says it complements but does not rely on code scanning, Dependabot, or secret scanning. Source: `raw/2026-06-11-web-github-changelog-dedicated-security-review-command-now-available-in-copilot-cli-github-c.md`. confidence: 1 GitHub changelog source, last-confirmed 2026-06-11.
- OpenAI's Codex deployment posture combines sandboxing, approvals, managed network allowlists, secure keyring credential storage, enterprise workspace pinning, command allow/block rules, OTel export, and compliance logs. Source: `raw/2026-06-11-web-openai-running-codex-safely-at-openai.md`. confidence: 1 official OpenAI source, last-confirmed 2026-06-11.

### Typed entities
- organization: Cloud Security Alliance
- framework: MCP Security Maturity Model
- threat: tool poisoning
- threat: tool shadowing
- threat: rugpull attack
- threat: session hijacking
- control: signed tool manifest
- control: version pinning
- control: mutual TLS
- control: certificate pinning
- command: GitHub Copilot CLI `/security-review`
- product: OpenAI Codex
- control: OpenTelemetry log export

### Explicit relationships
- Agentic tool-chain attacks exploit natural-language tool metadata and runtime context rather than only executable code.
- Tool shadowing causes one tool's metadata to influence how an agent calls another tool.
- Signed manifests and version pinning mitigate tool-description drift and rugpull risk.
- Copilot CLI `/security-review` complements deterministic scanners but does not supersede CodeQL, Dependabot, secret scanning, or human security review.
- Codex sandboxing and approval policy complement enterprise compliance logs by constraining and explaining agent actions.

### HoneyDrunk implications
- Treat MCP/tool metadata as code: review, hash/sign where possible, pin versions, and alert on drift before exposing tools to broad agents.
- Add `/security-review`-style AI review only as a fast local sensor; keep deterministic SAST, dependency, secret, and path/egress controls mandatory.
- For OpenClaw, record the requested action, policy decision, network decision, and execution result for tool calls; endpoint logs alone will not explain agent intent.

### Privacy and quality notes
- Privacy filter: exploit examples were summarized as threat/control classes; no credential paths, payloads, or runnable exploitation steps were copied.
- Quality posture: CSA source is draft; CrowdStrike is vendor-authored. Use as security architecture signal, not final compliance policy.

## 2026-06-12 compile additions: Agentic email, agentic Top 10, and governed execution

### Source-backed claims
- Fowler's Agentic Email post applies the Lethal Trifecta to email agents: untrusted email content, sensitive account context, and external communication combine into a high-risk exfiltration/control surface, especially because password-reset workflows often route through email. Source: `raw/2026-06-12-web-martin-fowler-bliki-agentic-email.md`. confidence: 1 Fowler source, last-confirmed 2026-06-12.
- Fowler describes a lower-risk email-agent pattern with read-only email access, no internet/external-send capability, and plain-text draft output for human review; this removes one leg of the trifecta but reduces capability. Source: `raw/2026-06-12-web-martin-fowler-bliki-agentic-email.md`. confidence: 1 Fowler source, last-confirmed 2026-06-12.
- OWASP Top 10 for Agentic Applications 2026 is positioned as a peer-reviewed framework for risks facing autonomous AI systems that plan, act, and make decisions across workflows. Source: `raw/2026-06-12-web-owasp-genai-owasp-top-10-for-agentic-applications-for-2026.md`. confidence: 1 OWASP GenAI source, last-confirmed 2026-06-12.
- Microsoft AGT plus Azure Container Apps sandbox guidance frames generated-code execution as two separable controls: where code runs and what it is allowed to do. Source: `raw/2026-06-12-web-microsoft-techcommunity-govern-ai-agents-using-agent-governance-toolkit-and-az.md`. confidence: 1 Microsoft source, last-confirmed 2026-06-12.
- The AGT example enforces shell-out, dependency-install, credential-access, tool-allowlist, egress, CPU/memory, timeout, and audit controls outside the model, using host policy, AST checks, ACA egress proxy, sandbox resource ceilings, and receipts. Source: `raw/2026-06-12-web-microsoft-techcommunity-govern-ai-agents-using-agent-governance-toolkit-and-az.md`. confidence: 1 Microsoft source, last-confirmed 2026-06-12.

### Typed entities
- concept: Lethal Trifecta
- workflow: agentic email
- framework: OWASP Top 10 for Agentic Applications 2026
- framework: Agent Governance Toolkit / AGT
- platform: Azure Container Apps Sandboxes
- control: read-only email access
- control: no external communication
- control: host-side policy evaluation
- control: AST subprocess scan
- control: fail-closed egress proxy
- artifact: execution receipt

### Explicit relationships
- Agentic email creates exfiltration risk when untrusted content, sensitive information, and outbound communication are present together.
- Read-only/no-network email assistance mitigates but does not eliminate agentic email risk.
- OWASP Agentic Top 10 complements MCP-specific threat taxonomies by covering broader autonomous-agent applications.
- Governed execution depends-on sandbox isolation plus explicit policy; sandboxing alone does not define allowed behavior.

### HoneyDrunk implications
- Do not expose email, messaging, calendar, ticketing, or password-reset surfaces to autonomous agents without separating read, draft, send, and approval capabilities.
- For code-running agents, make receipts first-class audit artifacts: allowed, denied-by-policy, blocked-at-egress, timeout, and error should be searchable outcomes.
- Use OWASP Agentic Top 10 as a control checklist for OpenClaw/Honeyclaw agents that plan and act across tools.

### Privacy and quality notes
- Privacy filter: risky prompt examples and secrets from sources were summarized as threat/control classes, not copied as reusable attack payloads.
- Quality posture: Fowler and OWASP are strong practice/taxonomy sources; AGT/ACA details remain vendor implementation guidance.

## 2026-06-14 compile additions: AI-enabled cyber operations, review blind spots, and Miasma supply-chain tooling

### Source-backed claims
- Anthropic Red Team analyzed 832 banned accounts associated with malicious cyber activity from March 2025 through March 2026 and mapped 13,873 observed actions to all 14 MITRE ATT&CK tactics and 482 unique sub-techniques; the highest-risk signal was not technique breadth alone, but whether AI was used for hands-on operational phases such as lateral movement and post-compromise activity. Source: `raw/2026-06-14-rss-anthropic-red-team-llm-att-ck-navigator-red-anthropic-com.md`. confidence: 1 primary vendor threat-intelligence source, last-confirmed 2026-06-14.
- Anthropic's ARiES scoring adds actor threat profile, model contribution to harm, and observed or potential impact to rank AI-enabled misuse cases; the score is designed to identify concerning AI involvement, not to predict whether an attack succeeds. Source: `raw/2026-06-14-rss-anthropic-red-team-llm-att-ck-navigator-red-anthropic-com.md`. confidence: 1 source, last-confirmed 2026-06-14.
- Anthropic reports that medium-or-higher AI enablement scores rose from roughly one-third to more than half of observed actors between the first and second halves of the study period, with more low- and mid-skill actors asking models for operational in-network work. Source: `raw/2026-06-14-rss-anthropic-red-team-llm-att-ck-navigator-red-anthropic-com.md`. confidence: 1 source, last-confirmed 2026-06-14.
- The Brain Overflow Claude Code security-review experiment found that same-session review can suppress findings because the reviewing model inherits the implementation session's assumptions, while cold-session review and diff-scoped plugin review have different blind spots. Source: `raw/2026-06-14-rss-brain-overflow-hidden-gaps-in-claude-code-security-reviews.md`. confidence: 1 practitioner experiment, last-confirmed 2026-06-14.
- The same experiment found diff-scoped security review can miss vulnerability chains split across commits or hidden behind component boundaries, especially when individual tool permissions look benign in isolation. Source: `raw/2026-06-14-rss-brain-overflow-hidden-gaps-in-claude-code-security-reviews.md`. confidence: 1 practitioner experiment, last-confirmed 2026-06-14.
- SafeDep describes Miasma as a broader software supply-chain attack toolkit, not just a worm: it targets public package registries, GitHub repositories and Actions, AI coding tool configuration, SSH/AWS SSM lateral movement, and developer credential stores. Source: `raw/2026-06-14-rss-safedep-inside-the-miasma-software-supply-chain-attack-toolkit-real-ti.md`. confidence: 1 security-research source, last-confirmed 2026-06-14.
- SafeDep reports Miasma uses public GitHub services as command, configuration, and exfiltration infrastructure, shifting detection requirements from simple network anomaly detection toward application-protocol and repository-behavior monitoring. Source: `raw/2026-06-14-rss-safedep-inside-the-miasma-software-supply-chain-attack-toolkit-real-ti.md`. confidence: 1 source, last-confirmed 2026-06-14.
- SafeDep reports Miasma can poison AI coding tool configuration and developer workflow files so payloads run when developers or agents open folders or execute ordinary project commands; this reinforces config files as executable supply-chain surfaces. Source: `raw/2026-06-14-rss-safedep-inside-the-miasma-software-supply-chain-attack-toolkit-real-ti.md`. confidence: 1 source, last-confirmed 2026-06-14.

### Typed entities
- framework: MITRE ATT&CK
- metric/framework: AI Risk Enablement Score / ARiES
- organization: Anthropic Red Team
- organization: Verizon DBIR
- concept: AI-enabled cyber operations
- concept: agentic attack orchestration
- concept: model anchoring bias
- concept: diff-scoped review blind spot
- campaign/toolkit: Miasma
- campaign family: Shai-Hulud / Mini Shai-Hulud
- platform: GitHub Actions
- platform: npm / PyPI / RubyGems
- threat: AI coding tool config poisoning
- threat: public-platform C2
- threat: trusted publishing abuse
- control: cold independent security review
- control: cross-commit chain review
- control: application-protocol anomaly detection

### Explicit relationships
- AI-enabled cyber-risk assessment depends-on orchestration behavior and live-operation use, not only MITRE technique count or actor technical sophistication.
- Lateral movement and post-compromise AI use correlate with higher ARiES risk scores because they indicate AI involvement inside live operations.
- Same-session review can contradict independent security review when implementation context anchors the model to the author's assumptions.
- Diff-scoped review depends-on the full exploit chain being visible in the current diff; it can miss risks split across commits, config files, skills, or subprocess boundaries.
- Supply-chain worms use AI coding tool config poisoning to turn developer and agent startup behavior into an execution path.
- Public GitHub infrastructure can be abused for command and exfiltration channels, so network allowlists alone do not prove safety.

### HoneyDrunk implications
- Run high-stakes security review in a fresh session or independent reviewer path, and add a cross-commit/component-boundary pass for permissions, subprocesses, MCP tools, and agent skills.
- Treat agent tool permissions as a combined capability set: `Write` plus scoped execution can still form write-then-execute risk.
- Add `.claude`, `.gemini`, `.cursor`, `.vscode`, project scripts, package hooks, workflow files, and action tags to supply-chain review surfaces.
- For Grid/OpenClaw review prompts, ask reviewers to reason about agentic orchestration and tool-chain chaining, not just isolated code smells.
- For supply-chain monitoring, inspect GitHub repository events, workflow/tag mutations, bot-like branch changes, config-file additions, and unusual public-repo exfiltration patterns.

### Privacy and quality notes
- Privacy filter: the SafeDep source contained concrete malware strings, payload mechanics, and destructive behaviors. This wiki section records threat and control classes only and intentionally omits reusable indicators, code paths, command strings, and payload snippets.
- Quality posture: Anthropic and SafeDep are strong primary/security-research sources for their own observations. Brain Overflow is a useful practitioner experiment but not a broad benchmark; treat it as review-process design evidence.

## 2026-06-15 compile additions: governed execution, AI-platform exposure, and deterministic security layers

### Source-backed claims
- Microsoft Agent Governance Toolkit (AGT) is a public-preview governance stack for autonomous agents that enforces policy, identity, sandboxing, audit, SRE controls, MCP security gateway checks, and compliance evidence outside the prompt. Source: `raw/2026-06-15-web-microsoft-agent-governance-toolkit.md`. confidence: 1 official GitHub README source, last-confirmed 2026-06-15.
- AGT's README explicitly argues that prompt-level safety is not a security boundary and that every tool call, message send, and delegation should be intercepted in deterministic application code before reaching the wire. Source: `raw/2026-06-15-web-microsoft-agent-governance-toolkit.md`. confidence: 1 official GitHub README source, last-confirmed 2026-06-15.
- AGT currently shares a process boundary between policy engine and agents and recommends separate containers for OS-level isolation in production, so it is middleware governance rather than a complete isolation boundary. Source: `raw/2026-06-15-web-microsoft-agent-governance-toolkit.md`. confidence: 1 official GitHub README source, last-confirmed 2026-06-15.
- OpenTaint positions formal taint analysis as a deterministic layer under AI security agents: one discovered vulnerability pattern can be encoded as a rule and run across the full codebase, with current emphasis on Java/Kotlin/Spring and roadmap support for Python, Go, C#, JavaScript, and TypeScript. Source: `raw/2026-06-15-web-seqra-opentaint.md`. confidence: 1 project README source, last-confirmed 2026-06-15.
- OpenTaint includes agent skills for an appsec workflow covering project build, scans, attack-surface discovery, dependency triage, rule creation, finding triage, and proof generation, making deterministic static analysis part of an agent loop. Source: `raw/2026-06-15-web-seqra-opentaint.md`. confidence: 1 project README source, last-confirmed 2026-06-15.
- Attackers are actively exploiting Langflow CVE-2026-5027, a path traversal issue in file upload handling that can allow arbitrary file writes on exposed servers; public reports cite patches in `langflow-base` 0.8.3 and Langflow 1.9.0, with 1.10.0 recommended in the captured article. Source: `raw/2026-06-15-web-bill-toulas-path-traversal-flaw-in-ai-dev-platform-langflow-exploited-.md`. confidence: 1 security-news source with linked researcher/vendor advisories, last-confirmed 2026-06-15.
- The Langflow report says default unauthenticated auto-login can make exploitation reachable without credentials on exposed instances, reinforcing that AI development platforms are internet-facing application infrastructure, not harmless local tools. Source: `raw/2026-06-15-web-bill-toulas-path-traversal-flaw-in-ai-dev-platform-langflow-exploited-.md`. confidence: 1 security-news source, last-confirmed 2026-06-15.
- Dropbox reports only 12% of implementing PRs linked back to the relevant design review/threat model, while semantic search could link 80% of reviews to implementing code changes; context retrieval found security gaps invisible from code alone. Source: `raw/2026-06-15-web-dropbox-tech-how-dropbox-uses-mcp-and-dash-to-close-the-design-to-code.md`. confidence: 1 Dropbox engineering source, last-confirmed 2026-06-15.
- Anthropic's Project Glasswing expansion reinforces that powerful cyber models can multiply vulnerability-finding capacity, making verification, disclosure, patching, and deployment the limiting security workflow. Source: `raw/2026-06-15-web-anthropic-expanding-project-glasswing.md`. confidence: 1 official Anthropic source, last-confirmed 2026-06-15.

### Typed entities
- framework/toolkit: Microsoft Agent Governance Toolkit / AGT
- component: Agent Control Specification
- component: MCP Security Gateway
- component: Agent SRE
- component: Agent Hypervisor
- project/tool: OpenTaint
- vulnerability: CVE-2026-5027
- platform: Langflow
- company/product: Dropbox Dash
- concept: design-to-code security traceability
- concept: formal taint analysis
- control: deterministic policy interception
- control: tamper-evident audit log

### Explicit relationships
- AGT governance depends-on deterministic middleware policy and audit controls, while production isolation still depends-on separate containers or stronger OS boundaries.
- Prompt-only safety contradicts reliable agent security when tools can perform destructive or external actions.
- OpenTaint complements LLM security review by turning discovered dataflow vulnerabilities into repeatable static rules.
- Langflow CVE-2026-5027 is caused by unsanitized filenames in file upload handling and amplified by exposed unauthenticated access paths.
- Dropbox's MCP/Dash security-review pattern depends-on retrieving design intent and threat models at PR review time.
- AI vulnerability discovery causes triage/patching load unless deterministic scanners, reachability checks, ownership, and deployment workflows absorb the output.

### HoneyDrunk implications
- Treat agent governance libraries as policy middleware, not isolation by themselves. Pair them with containers/microVMs, egress control, secret custody, and receipts.
- For HoneyDrunk appsec agents, prefer an LLM-plus-deterministic-analysis loop: agent finds patterns, deterministic rules prove coverage, humans review reachability and impact.
- Add Langflow and similar AI dev platforms to exposure reviews if ever deployed: public reachability, auth defaults, upload paths, patch level, and file-write permissions are the minimum checks.
- For PR review automation, retrieve applicable design/security requirements and compare implementation to intent, not only to generic secure-coding rules.

### Privacy and quality notes
- Privacy filter: exploit details were summarized at vulnerability/control level. No payloads, traversal strings beyond generic class names, or runnable exploit steps were copied.
- Quality posture: AGT/OpenTaint are project README sources and may be product-positioned; validate package maturity and boundaries before adoption. Dropbox is a strong practice case study but internal metrics need local reproduction.

## 2026-06-16 compile additions: LangGraph checkpointers, bearer-token limits, and package ownership attacks

### Source-backed claims
- Check Point Research reports three LangGraph persistence-layer vulnerabilities: SQLite metadata-filter SQL injection (`CVE-2025-67644`), unsafe msgpack deserialization (`CVE-2026-28277`), and Redis metadata-filter injection (`CVE-2026-27022`). The RCE chain applies where self-hosted LangGraph exposes `get_state_history()` with user-controlled filters and vulnerable checkpointers. Source: `raw/2026-06-16-web-checkpoint-from-sqli-to-rce-exploiting-langgraph-s-checkpointer.md`. confidence: 1 security-research source, last-confirmed 2026-06-16.
- The same source says LangChain patched the issues in `langgraph-checkpoint-sqlite` 3.0.1+, `langgraph` 1.0.10+, and `langgraph-checkpoint-redis` 1.0.2+; LangSmith Deployment was not vulnerable because it runs PostgreSQL rather than the affected SQLite/Redis paths. Source: `raw/2026-06-16-web-checkpoint-from-sqli-to-rce-exploiting-langgraph-s-checkpointer.md`. confidence: 1 security-research source, last-confirmed 2026-06-16.
- Dick Hardt's response to Anthropic's zero-trust agent framework argues that short-lived bearer tokens reduce theft windows but do not make credential replay impossible; non-exportable proof-of-possession credentials and per-call constrained authorization are stronger agent-native patterns. Source: `raw/2026-06-16-web-hello-anthropic-s-zero-trust-for-ai-agents-sets-the-right-test-the-bearer-token-fails-it.md`. confidence: 1 identity-practitioner source, last-confirmed 2026-06-16.
- The same source argues that "agent may use tool" is too coarse for agent authorization; the operation parameters themselves should be part of the authorization decision, and delegation should narrow authority as it travels between agents. Source: `raw/2026-06-16-web-hello-anthropic-s-zero-trust-for-ai-agents-sets-the-right-test-the-bearer-token-fails-it.md`. confidence: 1 identity-practitioner source, last-confirmed 2026-06-16.
- Sonatype reports Atomic Arch, a campaign targeting orphaned Arch User Repository packages by taking over trusted package ownership and modifying PKGBUILDs to install malicious npm dependencies during package installation; preliminary reporting suggested about 1,500 affected packages across waves. Source: `raw/2026-06-16-web-sonatype-atomic-arch-attackers-hijack-trusted-aur-packages-to-deliver-rootkit-like-malware.md`. confidence: 1 security-research source, last-confirmed 2026-06-16.
- Sonatype's analysis found the malicious payload had Linux credential-harvesting, stealth, anti-debugging, and potential exfiltration functionality; affected hosts should be treated as compromised because removing the package alone may not remove second-stage effects. Source: `raw/2026-06-16-web-sonatype-atomic-arch-attackers-hijack-trusted-aur-packages-to-deliver-rootkit-like-malware.md`. confidence: 1 security-research source, last-confirmed 2026-06-16.

### Typed entities
- framework: LangGraph
- component: SQLite checkpointer
- component: Redis checkpointer
- vulnerability: CVE-2025-67644
- vulnerability: CVE-2026-28277
- vulnerability: CVE-2026-27022
- platform: LangSmith Deployment
- concept: proof-of-possession credential
- concept: constrained call authorization
- concept: derived delegation
- ecosystem: Arch User Repository / AUR
- campaign: Atomic Arch
- package: atomic-lockfile
- package: js-digest
- package: lockfile-js

### Explicit relationships
- LangGraph RCE risk depends-on self-hosted affected checkpointers, user-controlled metadata filters, and vulnerable package versions.
- PostgreSQL-backed LangSmith Deployment contradicts exposure assumptions for SQLite/Redis checkpointer findings in that managed service.
- Short-lived bearer tokens mitigate but do not supersede credential replay risk because possession remains sufficient for use.
- Per-call constrained authorization supersedes coarse agent/tool permission grants for sensitive operations.
- AUR ownership takeover uses inherited trust to bypass user expectations; trusted package names can contradict current maintainer trustworthiness.

### HoneyDrunk implications
- If HoneyDrunk uses LangGraph, inventory checkpointer packages and block deployments below the patched versions before exposing state-history filters.
- Treat agent memory/checkpoint stores as attack surfaces with ordinary input-validation, query-parameterization, and deserialization review.
- Prefer sender-constrained or proof-of-possession patterns for high-value agent credentials when platform support exists; document any bearer-token exception with scope and lifetime.
- Review package ecosystems for abandoned-maintainer and install-hook risk, especially where agents install packages on developer or runner machines.

### Privacy and quality notes
- Privacy filter: exploit mechanics were reduced to preconditions, vulnerable components, and patch floors. No payload bytes, command strings, or step-by-step exploit procedure were copied.
- Quality posture: Check Point and Sonatype are security-research sources; validate current advisories/package versions before operational changes. The Hello source is expert opinion on identity architecture, not a standard by itself.

## 2026-06-17 compile additions: indirect prompt injection, skill security, and attested images

### Source-backed claims
- Google Threat Intelligence scanned Common Crawl public-web snapshots with a coarse-to-fine pipeline of signature matching, Gemini classification, and human validation, finding indirect prompt injections in categories such as pranks, benign summary guidance, SEO manipulation, AI-agent deterrence, data-exfiltration attempts, and destructive-command attempts. Source: `raw/2026-06-17-web-blog-google-ai-threats-in-the-wild-the-current-state-of-prompt-injections-on-the-web.md`. confidence: 1 Google security source, last-confirmed 2026-06-17.
- Google found the malicious public-web IPI category was still mostly low-sophistication in the sampled data, but observed a 32% relative increase in malicious detections between November 2025 and February 2026 and expects scale/sophistication to grow as agents become more capable. Source: `raw/2026-06-17-web-blog-google-ai-threats-in-the-wild-the-current-state-of-prompt-injections-on-the-web.md`. confidence: 1 source, last-confirmed 2026-06-17.
- Anthropic's Managed Agents security boundary keeps credentials outside generated-code sandboxes: repository tokens are wired into initialized Git remotes, and custom-tool OAuth tokens are held in a vault behind an MCP proxy rather than exposed to the harness or sandbox environment. Source: `raw/2026-06-17-web-anthropic-com-scaling-managed-agents-decoupling-the-brain-from-the-hands.md`. confidence: 1 Anthropic engineering source, last-confirmed 2026-06-17.
- Docker's DHI/Aikido integration uses signed SPDX SBOMs and OpenVEX attestations for Docker Hardened Images so scanners can suppress findings Docker has marked fixed or not affected, leaving a smaller active queue with attestation evidence for auditors. Source: `raw/2026-06-17-web-docker-com-docker-hardened-images-enhanced-vulnerability-scanning-with-docker-and-aikido-dock.md`. confidence: 1 Docker vendor source, last-confirmed 2026-06-17.
- Docker frames hardened, minimal, attestable base images as more important when AI coding agents can generate services and dependencies faster than humans can triage flat CVE output. Source: `raw/2026-06-17-web-docker-com-docker-hardened-images-enhanced-vulnerability-scanning-with-docker-and-aikido-dock.md`. confidence: 1 Docker vendor source, last-confirmed 2026-06-17.
- OWASP Agentic Skills Top 10 (AST10) positions skills as the behavior layer between models and tools, covering risks such as malicious skills, supply-chain compromise, over-privileged skills, insecure metadata, unsafe deserialization, weak isolation, update drift, poor scanning, no governance, and cross-platform reuse. Source: `raw/2026-06-17-web-owasp-org-owasp-agentic-skills-top-10-owasp-foundation.md`. confidence: 1 OWASP incubator project source, last-confirmed 2026-06-17.
- AST10 recommends skill inventories, verified publishers, code signing, version pinning, permission manifests, sandboxed execution, network restrictions, install-time scanning, audit logging, and incident-response procedures for skill compromises. Source: `raw/2026-06-17-web-owasp-org-owasp-agentic-skills-top-10-owasp-foundation.md`. confidence: 1 OWASP incubator project source, last-confirmed 2026-06-17.

### Typed entities
- threat: indirect prompt injection / IPI
- dataset: Common Crawl
- organization: Google Threat Intelligence Group
- control: LLM-based IPI classification
- product: Claude Managed Agents
- control: credential vault
- control: MCP proxy
- product: Docker Hardened Images / DHI
- company/tool: Aikido
- artifact: signed SPDX SBOM
- artifact: OpenVEX attestation
- framework: OWASP Agentic Skills Top 10 / AST10
- concept: agentic skill behavior layer
- control: skill permission manifest
- control: skill signing

### Explicit relationships
- Public-web prompt injection depends-on agents consuming untrusted HTML, comments, documents, or email-like content as instructions.
- IPI scanning depends-on human validation because educational/security content creates high false-positive rates.
- Credential vaulting and proxy-mediated tool calls mitigate sandbox exfiltration by making raw tokens unreachable to generated code.
- VEX attestations complement CVE scanning by adding exploitability status and justification from the image publisher.
- Agentic skills differ from MCP tools: MCP defines reachable actions, while skills define multi-step behavior over those actions.
- Skill security depends-on provenance, least privilege, isolation, safe parsing, update pinning, behavioral scanning, inventory, and audit logs.

### HoneyDrunk implications
- Treat Lore/browser ingestion as hostile content ingestion. Keep prompt-injection examples out of wiki pages except as summarized risk categories.
- For OpenClaw/Honeyclaw, credentials should be injected as narrow capabilities or held behind proxies/vaults, not mounted into workspaces where generated code can read them.
- Evaluate hardened base images and SBOM/VEX-aware scanners for agent-created container workloads, but verify attestation trust and scanner behavior locally.
- Build a HoneyDrunk skill inventory before broad skill reuse: publisher, source, hash/version, declared permissions, network reach, filesystem reach, and last scan result.

### Privacy and quality notes
- Privacy filter: Google IPI examples and OWASP incident details were summarized by category; no prompt payloads, C2 indicators, commands, or destructive instructions were copied.
- Quality posture: Google security and Docker sources are strong for their own observations/products. OWASP AST10 is useful taxonomy guidance but the project is incubating; source-claimed incident metrics should be corroborated before operational decisions rely on exact numbers.

## 2026-06-18 compile additions: developer plugin theft, AI gateway takeover, and enterprise search exfiltration

### Source-backed claims
- BleepingComputer/Aikido report at least 15 malicious JetBrains Marketplace plugins impersonating AI coding, code-review, Git, and DeepSeek/OpenAI-style tools that exfiltrate AI provider API keys entered into plugin settings; the campaign reportedly reached about 70,000 installs, though download counts can be manipulated. Source: `raw/2026-06-18-web-bleepingcomputer-com-malicious-jetbrains-marketplace-plugins-steal-ai-.md`. confidence: 1 security-news source citing Aikido plus independent confirmation for one plugin, last-confirmed 2026-06-18.
- The JetBrains plugin campaign reinforces that IDE/plugin marketplaces are agent-era credential boundaries: plugins that look like coding assistants can collect API keys at configuration time while still appearing functional. Source: `raw/2026-06-18-web-bleepingcomputer-com-malicious-jetbrains-marketplace-plugins-steal-ai-.md`. confidence: 1 source, last-confirmed 2026-06-18.
- The Hacker News/Obsidian report a LiteLLM proxy vulnerability chain allowing low-privilege users to escalate to proxy admin and reach server-side code execution, exposing model-provider keys, stored credential material, prompts, responses, and potentially MCP/tool credentials. Source: `raw/2026-06-18-web-thehackernews-com-litellm-vulnerability-chain-lets-low-privilege-users.md`. confidence: 1 security-news source citing Obsidian/VulnCheck/X41 details, last-confirmed 2026-06-18.
- The LiteLLM report states the full fix set landed in `v1.83.14-stable`; it also warns that proxy-admin access should be treated as host-level access because LiteLLM can run callbacks and stdio MCP servers. Source: `raw/2026-06-18-web-thehackernews-com-litellm-vulnerability-chain-lets-low-privilege-users.md`. confidence: 1 source, last-confirmed 2026-06-18.
- Varonis reports SearchLeak, remediated by Microsoft as CVE-2026-42824, chained parameter-to-prompt injection in Microsoft 365 Copilot Enterprise Search, an HTML streaming/rendering race, and an allowlisted Bing server-side fetch path to exfiltrate data from content the victim could access after one link click. Source: `raw/2026-06-18-web-varonis-com-searchleak-how-we-turned-m365-copilot-into-a-one-click-dat.md`. confidence: 1 security-research source, last-confirmed 2026-06-18.
- SearchLeak shows AI search surfaces can combine classic web bugs with AI-native instruction interpretation, so render-time sanitization and CSP allowlist review matter for AI-generated streaming output. Source: `raw/2026-06-18-web-varonis-com-searchleak-how-we-turned-m365-copilot-into-a-one-click-dat.md`. confidence: 1 source, last-confirmed 2026-06-18.

### Typed entities
- marketplace: JetBrains Marketplace
- threat: malicious IDE plugin
- credential class: AI provider API key
- project: LiteLLM
- role: `proxy_admin`
- vulnerability: CVE-2026-47101
- vulnerability: CVE-2026-47102
- vulnerability: CVE-2026-40217
- patched version: LiteLLM `v1.83.14-stable`
- vulnerability: SearchLeak / CVE-2026-42824
- product: Microsoft 365 Copilot Enterprise Search
- threat class: parameter-to-prompt injection / P2P
- control: render-time output sanitization
- control: CSP allowlist review

### Explicit relationships
- Malicious IDE plugins use marketplace trust to capture credentials at setup time before source-code or CI controls can see the leak.
- AI gateway compromise has larger blast radius than a single model key because the gateway holds provider credentials, prompts/responses, callbacks, and sometimes MCP/tool credentials.
- Proxy-admin roles in AI gateways can imply code execution when callbacks, custom guardrails, or stdio MCP servers are available.
- SearchLeak combines AI instruction interpretation with web rendering and SSRF-style server-side fetch behavior; each layer is necessary for the chain.
- Streaming AI output contradicts post-processing-only sanitizer assumptions because browsers can act on partial output before final wrapping.

### HoneyDrunk implications
- Maintain an approved plugin list for developer IDEs and agent harnesses; treat AI plugin installation as credential-risk work, not personal preference.
- Audit any LiteLLM or similar model gateway before use: version, admin accounts, callbacks, custom guardrails, MCP servers, provider-key storage, and external exposure.
- Treat AI/search URLs with long natural-language query parameters as potential prompt carriers; monitoring should inspect encoded prompts, not only domains.
- For HoneyDrunk AI UIs, sanitize streamed HTML before render, review CSP allowlists for server-side fetch behavior, and assume model output is untrusted content.

### Privacy and quality notes
- Privacy filter: exploit payloads, attacker infrastructure details, and shell payload mechanics were summarized at control level rather than copied as reusable instructions.
- Quality posture: these are security-research/news sources. Recheck vendor advisories and current patched versions before incident response or implementation work.

## 2026-06-19 compile additions: research-agent query leakage, DCT retirement, and CI trigger hardening

### Source-backed claims
- MosaicLeaks shows that deep-research agents can leak private local-document facts through sequences of ordinary-looking public web queries; the leakage channel is the cumulative query log, not the final answer alone. Source: `raw/2026-06-19-web-huggingface-co-mosaicleaks-can-your-research-agent-keep-a-secret.md`; page: [[agent-evaluation-and-benchmarks]]. confidence: 1 Hugging Face/ServiceNow research source, last-confirmed 2026-06-19.
- The MosaicLeaks source reports that adding a prompt warning against leaky web queries lowered leakage only modestly for some models and could reduce task success, while task-only RL made leakage worse. Source: `raw/2026-06-19-web-huggingface-co-mosaicleaks-can-your-research-agent-keep-a-secret.md`. confidence: 1 source, last-confirmed 2026-06-19.
- Docker is retiring Docker Content Trust / Notary v1 with write brownouts on 2026-07-14 and 2026-07-15, read brownouts on 2026-08-10 and 2026-08-12, and full shutdown on 2026-12-08. Source: `raw/2026-06-19-web-docker-com-docker-content-trust-retirement-and-migration-guidance.md`. confidence: 1 Docker source, last-confirmed 2026-06-19.
- Docker recommends replacing DCT workflows with digest pinning for repeatability and modern OCI-native signing/enforcement paths such as Sigstore/Cosign, Notation, Kyverno, Ratify/Gatekeeper, and Docker Hardened Images. Source: `raw/2026-06-19-web-docker-com-docker-content-trust-retirement-and-migration-guidance.md`. confidence: 1 source, last-confirmed 2026-06-19.
- GitHub `actions/checkout` v7 refuses common `pull_request_target` and fork-PR `workflow_run` pwn-request checkout patterns by default, with enforcement backported to supported major versions on 2026-07-16 unless workflows are pinned to exact SHA/minor/patch versions. Source: `raw/2026-06-19-web-github-blog-safer-pull-request-target-defaults-for-github-actions-checkout.md`; page: [[github-actions-platform-operations]]. confidence: 1 GitHub changelog source, last-confirmed 2026-06-19.
- GitHub workflow execution protections are in public preview, letting admins define actor and event allowlists through rulesets before workflow runs are admitted. Source: `raw/2026-06-19-web-github-blog-control-who-and-what-triggers-github-actions-workflows.md`; page: [[github-actions-platform-operations]]. confidence: 1 GitHub changelog source, last-confirmed 2026-06-19.

### Typed entities
- benchmark: MosaicLeaks
- threat: query-log privacy leakage
- method: Privacy-Aware Deep Research / PA-DR
- product/control: Docker Content Trust / DCT
- service: Notary v1 / `notary.docker.io`
- signing tool: Sigstore / Cosign
- signing tool: Notation
- control: digest pinning
- action: `actions/checkout` v7
- input: `allow-unsafe-pr-checkout`
- feature: GitHub workflow execution protections
- control: actor rule
- control: event rule

### Explicit relationships
- Query-log privacy leakage is caused by private facts being carried into external search terms across a multi-hop task.
- PA-DR mitigates leakage by penalizing the planning decision that makes the cumulative query log more revealing.
- DCT retirement supersedes Notary v1-based trust assumptions for Docker Hub workflows after the 2026 shutdown schedule.
- Digest pinning provides content repeatability but does not prove publisher identity; signatures and admission enforcement complement digest pinning.
- `actions/checkout` v7 blocks a common privileged-event checkout pattern but does not supersede review of other untrusted code execution paths.
- Workflow execution protections complement workflow-file review by moving trigger admission into central rulesets.

### HoneyDrunk implications
- Treat Lore/OpenClaw research queries as an exfiltration surface when private repo notes or internal docs influence web searches.
- Inventory Docker workflows for `DOCKER_CONTENT_TRUST=1`, `docker trust` commands, DCT admission policies, and DCT-signed publisher flows before July 2026 brownouts.
- Audit `pull_request_target`, `workflow_run`, and comment-triggered CI for untrusted checkout or manual `git`/`gh` fetches that bypass checkout safeguards.
- Use workflow execution protections in evaluate mode first when available, then enforce actor/event rules for privileged workflows.

### Privacy and quality notes
- Privacy filter: MosaicLeaks examples were summarized at benchmark/control level. No private synthetic enterprise facts beyond the source's high-level example were promoted as HoneyDrunk facts.
- Quality posture: GitHub and Docker sources are authoritative for product timelines as captured; recheck before enforcement or incident response.

## 2026-06-20 compile additions: AI control, proof-first vulnerability work, and security harnesses

### Source-backed claims
- Google DeepMind's AI Control Roadmap treats powerful internal agents as potentially misaligned insider-like principals and layers monitoring, supervision, prevention, response, and capability-scaled controls on top of alignment, sandboxing, endpoint security, and prompt-injection resistance. Source: `raw/2026-06-20-web-google-deepmind-securing-the-future-of-ai-agents-7-minute-read.md`. confidence: 1 Google DeepMind source, last-confirmed 2026-06-20.
- DeepMind maps controls to two capability axes: detection evasion capability drives detection levels, while attack execution capability drives prevention/response levels; high-risk actions require synchronous blocking rather than delayed review. Source: `raw/2026-06-20-web-google-deepmind-securing-the-future-of-ai-agents-7-minute-read.md`. confidence: 1 source, last-confirmed 2026-06-20.
- Cloudflare's vulnerability harness article argues that enterprise security scanning needs persistent state, model-agnostic stages, adversarial validation, deduplication, cross-repo tracing, proof-of-concept tests against untouched code, and patch/test artifacts before findings reach humans. Source: `raw/2026-06-20-web-cloudflare-build-your-own-vulnerability-harness-20-minute-read.md`; page: [[agent-evaluation-and-benchmarks]]. confidence: 1 Cloudflare security engineering source, last-confirmed 2026-06-20.
- CredRelay's ASUS CVE writeup reinforces a smaller-scale version of the same rule: LLM-assisted reversing is useful only when the human can read the generated C, force a working proof of concept, understand the root cause, and rewrite noisy AI reports before vendor submission. Source: `raw/2026-06-20-web-credrelay-getting-a-cve-without-shipping-slop-4-minute-read.md`. confidence: 1 practitioner source, last-confirmed 2026-06-20.
- Vercel Connect replaces long-lived app-stored provider tokens with runtime credential exchange: a deployment proves identity via OIDC and receives short-lived task-scoped credentials, optionally scoped by user, repository, permission, installation, project, and environment. Source: `raw/2026-06-20-web-vercel-vercel-connect-8-minute-read.md`; page: [[mcp-tool-governance-and-app-surfaces]]. confidence: 1 Vercel product source, last-confirmed 2026-06-20.

### Typed entities
- framework: Google DeepMind AI Control Roadmap
- framework: MITRE ATT&CK
- concept: insider-threat model for agents
- control: supervisor AI
- control: synchronous response
- system: Cloudflare Vulnerability Discovery Harness / VDH
- system: Cloudflare Vulnerability Validation System / VVS
- control: adversarial validator
- control: proof-of-concept test
- control: fail-to-pass patch gate
- tool: Ghidra MCP
- vulnerability: CVE-2026-3508
- vulnerability: CVE-2026-6737
- product: Vercel Connect
- control: OIDC runtime credential exchange
- control: task-scoped token

### Explicit relationships
- AI control treats alignment as necessary but insufficient; system-level monitoring and blocking complement model behavior.
- Vulnerability harnesses depend-on externalized state and independent validators because single-session agents lose context and tend to validate their own theories.
- Working PoCs and tests supersede prose vulnerability claims for vendor-grade reporting.
- Runtime credential exchange mitigates leaked-token blast radius by narrowing duration, subject, environment, repository, and permission scope.
- Short-lived tokens complement but do not supersede policy gates, human approvals, and provider-side revocation behavior.

### HoneyDrunk implications
- For OpenClaw/Honeyclaw security work, require findings to include threat model, affected boundary, source evidence, reproducible test/PoC, proposed patch, and validation status before filing as actionable.
- Treat high-impact agent actions as capability-dependent: delayed audit is acceptable for reversible/low-risk work, but production writes, destructive changes, and external communication need pre-execution gates.
- Prefer runtime-scoped credentials over environment-wide bot tokens for agents; record subject, scope, and expiry in run receipts where possible.

### Privacy and quality notes
- Privacy filter: exploit mechanics were reduced to control and validation requirements. Device names/CVE IDs are public; no reusable exploit code or contact details were copied.
- Quality posture: DeepMind, Cloudflare, and Vercel are vendor/platform-authored; CredRelay is practitioner evidence. Use as architecture/control guidance and verify product APIs before implementation.

## 2026-06-21 compile additions: hardened images, audit hooks, and telemetry denial risk

### Source-backed claims
- Docker's hardened-images explainer defines hardened images as minimal, patched, policy-aligned container bases intended to reduce attack surface, CVE noise, and supply-chain uncertainty; this reinforces the earlier Docker Hardened Images/SBOM/VEX guidance. Source: `raw/2026-06-21-web-docker-hardened-images-explained.md`. confidence: 1 Docker source, last-confirmed 2026-06-21.
- iPurple Team describes a Windows QoS policy abuse path where an elevated actor can throttle outbound traffic for an EDR process, reducing the agent's ability to send telemetry to the cloud console. Source: `raw/2026-06-21-web-ipurple-team-qos-policies.md`. confidence: 1 purple-team source, last-confirmed 2026-06-21.
- Anzenna's Birdclaw signal positions AI audit hooks as a layer that links a prompt to commands, files, MCP destinations, OAuth grants, and named identities; treat as product/watchlist signal until primary documentation is captured. Source: `raw/2026-06-20-birdclaw-x-x-signal-anzennahq-edr-sees-a-python-process-we-see-what-the-agent-was-told-to-d.md`. confidence: 1 low-engagement social source, last-confirmed 2026-06-20.
- ARC Terminal social promotion frames "cryptographically verifiable AI" as a proof layer for model/output/action claims; this is a watchlist idea, not a verified security control without primary specs and threat-model review. Source: `raw/2026-06-20-birdclaw-x-x-signal-bjauhi-arc-terminal-breakdown-what-exactly-is-this-project-to-put-it-si.md`. confidence: 1 social source, last-confirmed 2026-06-20.
- Social posts around AI trading subaccounts and free model-router API keys reinforce a practical agent-security boundary: when agents can trade, spend tokens, or hold API keys, account isolation, withdrawal blocks, quota limits, and provider/key provenance become part of the harness threat model. Source: `wiki/early-social-ai-agent-signals-2026.md`. confidence: low social-source cluster, last-confirmed 2026-06-20.

### Typed entities
- product: Docker Hardened Images
- control: minimal base image
- artifact: SBOM
- artifact: VEX
- Windows feature: QoS policy
- threat: EDR telemetry throttling
- concept: prompt-to-command audit
- concept: cryptographically verifiable AI
- concept: AI trading subaccount
- concept: model-router API key provenance
- page: [[early-social-ai-agent-signals-2026]]

### Explicit relationships
- Hardened images complement agent sandboxing by reducing baseline OS/package attack surface before generated services are deployed.
- Telemetry denial can be caused by endpoint/network policy manipulation, so agent/security monitoring depends-on local health checks as well as cloud-received events.
- Prompt-to-command audit complements process telemetry by linking human/agent intent to filesystem, command, MCP, and OAuth effects.
- Cryptographic AI proof claims depend-on concrete protocols, attestations, verifier access, and threat-model coverage before they can replace ordinary audit.
- AI trading and API-router workflows depend-on scoped accounts, withdrawal/spend limits, and revocation paths.

### HoneyDrunk implications
- Prefer hardened, attestable base images for agent-created services, but verify scanner/VEX behavior in CI before trusting reduced CVE counts.
- Add EDR/runner telemetry health to security thinking: "no alert" can mean no event, or a blocked/throttled reporting path.
- For agent audit work, capture prompt, tool call, command, file diff, MCP destination, credential scope, and actor identity in run receipts where feasible.
- Do not let agents use promotional free API routers or trading accounts without provenance, budget, and account-isolation review.

### Privacy and quality notes
- Privacy filter: attack mechanics are summarized at control level; no reusable bypass commands or payloads were copied.
- Docker is vendor-authored; iPurple is security-practitioner content; Birdclaw items are watchlist-only.

## 2026-06-22 compile additions: hooks, temporary accounts, and post-quantum readiness

### Source-backed claims
- Zarar's agent-hooks source argues that prompt instructions are not reliable enforcement and that agent lifecycle hooks are the appropriate layer for rules such as blocking unsafe edits before tool execution or requiring tests before a session can stop. Source: `raw/2026-06-22-rss-zarar-dev-do-not-rely-on-instructions-use-agent-hooks-to-enforce-guard.md`. confidence: 1 practitioner source, last-confirmed 2026-06-22.
- The same source warns that hooks must be tested as code: JSON-path mistakes, silent nulls, and missing `stop_hook_active` handling can make guards ineffective or create infinite loops. Source: `raw/2026-06-22-rss-zarar-dev-do-not-rely-on-instructions-use-agent-hooks-to-enforce-guard.md`. confidence: 1 source, last-confirmed 2026-06-22.
- Cloudflare Temporary Accounts create disposable deployment authority for agents, which reduces signup friction but creates a new security boundary around temporary account scope, token lifetime, billing/quota behavior, claim links, and cleanup evidence. Source: `raw/2026-06-22-rss-blog-cloudflare-com-temporary-cloudflare-accounts-for-ai-agents.md`. confidence: 1 Cloudflare product source plus compile judgment, last-confirmed 2026-06-22.
- Cloudflare's code-mode MCP source reinforces that keeping credentials out of model context is a security control, but it does not remove the need for scoped runtime credentials, audit logs, and tool-level authorization. Source: `raw/2026-06-22-rss-blog-cloudflare-com-introducing-the-cloudflare-one-stack-agent-powered.md`; page: [[mcp-tool-governance-and-app-surfaces]]. confidence: 1 Cloudflare product source, last-confirmed 2026-06-22.
- Post-quantum migration signals from Brandon Rozek's source indicate SSH, TLS, and VPN stacks are moving at different speeds; see [[post-quantum-security-and-cryptography]] for the dedicated cryptography page. Source: `raw/2026-06-22-rss-brandonrozek-com-on-post-quantum-security-adoption.md`. confidence: 1 practitioner source, last-confirmed 2026-06-22.

### Typed entities
- control: agent lifecycle hook
- control: `PreToolUse` hook
- control: `Stop` hook
- risk: silent JSON-path null
- product: Cloudflare Temporary Accounts
- command: `wrangler deploy --temporary`
- control: scoped runtime credential
- page: [[post-quantum-security-and-cryptography]]

### Explicit relationships
- Agent hooks enforce workflow policy before or after tool calls; they complement but do not supersede sandboxing, identity scoping, and code review.
- Tested hooks can supersede memory-only reminders when the same rule recurs across agent runs.
- Temporary accounts reduce ambient-account reuse but depend-on expiry, quotas, claim controls, and audit logs to avoid becoming disposable untracked infrastructure.
- Runtime credential custody complements MCP governance by preventing raw secrets from entering prompts or wiki pages.

### HoneyDrunk implications
- Promote durable agent safety rules into hooks where available, and validate hooks with positive and negative fixtures before trusting them.
- Treat temporary deployment accounts as infrastructure principals. Run summaries should record account scope, expiry, deployed resource, cleanup/claim status, and any generated URL.
- Add post-quantum readiness to infrastructure/security inventory work, but verify current protocol support before making migration decisions.

### Privacy and quality notes
- No hook payloads, secrets, tokens, or executable bypass details were copied. Sources are practitioner/vendor guidance and require local runtime testing.

## 2026-06-23 compile additions: telemetry injection and AI cyber pipelines

### Source-backed claims
- The New Stack/Tenet report describes "agentjacking" through Sentry-backed MCP workflows: a public write-only Sentry DSN can let an attacker place crafted error data into the queue an AI coding agent later reads as trusted remediation context. Source: `raw/2026-06-23-rss-tldr-infosec-a-public-sentry-key-is-all-it-takes-to-hijack-claude-code.md`. confidence: 1 security-news source citing vendor research, last-confirmed 2026-06-23.
- The same report says the practical risk is not Sentry alone; any MCP integration that returns externally influenced data to an agent can become an instruction/data confusion path unless the runtime gates actions sourced from tool output. Source: `raw/2026-06-23-rss-tldr-infosec-a-public-sentry-key-is-all-it-takes-to-hijack-claude-code.md`. confidence: 1 source, last-confirmed 2026-06-23.
- The Tenet-reported validation claims Claude Code, Cursor, and Codex acted on injected Sentry errors in controlled tests, with the article reporting an 85% success rate and more than 100 confirmed executions; treat those numbers as vendor-reported controlled-test results, not independent measurements. Source: `raw/2026-06-23-rss-tldr-infosec-a-public-sentry-key-is-all-it-takes-to-hijack-claude-code.md`. confidence: 1 vendor-cited report, last-confirmed 2026-06-23.
- GitHub's secret-scanning source says it added context-aware LLM reasoning to reduce false positives for AI-detected generic secrets by analyzing high-signal usage context rather than whole files; the reported false-positive reduction was 75.76% against a 65% target on customer-confirmed false positives. Source: `raw/2026-06-23-rss-tldr-infosec-making-secret-scanning-more-trustworthy-reducing-false-po.md`. confidence: 1 GitHub security source, last-confirmed 2026-06-23.
- The TestingCatalog/TLDR OpenAI cyber source reports a Daybreak/Codex Security direction that moves from vulnerability discovery into scanning, validation, patching, reporting, SARIF/CodeQL export, expert review, and Patch the Planet maintainer support; treat it as secondary reporting until primary OpenAI material is captured. Source: `raw/2026-06-23-rss-tldr-ai-openai-launches-new-security-tools-and-updates-gpt-5-5-cyber-2.md`. confidence: 1 secondary source, last-confirmed 2026-06-23.

### Typed entities
- attack class: agentjacking
- service: Sentry
- credential type: Sentry DSN
- protocol: Model Context Protocol / MCP
- tools: Claude Code, Cursor, Codex
- control: agent runtime action gate
- control: secret-scanning context classifier
- product: GitHub secret scanning
- product: Codex Security
- initiative: Patch the Planet
- product/program: Daybreak

### Explicit relationships
- Public telemetry-write credentials can become agent input channels when agents read monitoring data through MCP.
- Agentjacking is caused by untrusted external data being reinterpreted as tool or shell instructions inside a trusted agent workflow.
- Runtime action gates complement prompt instructions because prompts did not reliably separate untrusted tool output from instructions in the reported tests.
- Secret-scanning LLM verification complements deterministic detectors by adding usage-context judgment after candidate detection.
- AI cyber pipelines depend-on human validation, duplicate removal, severity review, patch tests, and disclosure workflow before fixes are actionable.

### HoneyDrunk implications
- Treat issue trackers, logs, telemetry, crash reports, user tickets, and monitoring dashboards as untrusted input when agents consume them.
- Before wiring agents to Sentry or similar tools, require tool-output sanitization, provenance labels, command-source checks, and approval gates for commands derived from external records.
- For HoneyDrunk secret scanning, prefer systems that keep broad detection coverage but add context-aware false-positive reduction and auditable reasoning.
- Do not treat secondary model/security product reporting as procurement-grade; capture primary docs or run local evals before changing security workflows.

### Privacy and quality notes
- Privacy filter: exploit details were summarized at control level. No payload strings, executable commands, secrets, or target identifiers were copied.
- Quality posture: Tenet sells agent-runtime defenses and the OpenAI cyber source is secondary reporting; both are useful signals but require primary-source or local validation.

## 2026-06-28 compile additions: prompt-injection challenge, MCP threat landscape, and security-solution mapping

### Source-backed claims
- Simon Willison's link post reports that a public challenge saw about 6,000 attempts by roughly 2,000 participants fail to leak secrets from an OpenClaw test instance through email prompt injection, while cautioning that this does not prove production safety for irreversible actions. Source: `raw/2026-06-28-rss-simon-willison-what-happened-after-2-000-people-tried-to-hack-my-ai-as.md`. confidence: 1 practitioner link/source summary, last-confirmed 2026-06-28.
- The same source frames frontier-model prompt-injection resistance as improving, but explicitly keeps the deployment rule conservative: do not put irreversible damage behind prompt-only defenses. Source: `raw/2026-06-28-rss-simon-willison-what-happened-after-2-000-people-tried-to-hack-my-ai-as.md`. confidence: 1 source, last-confirmed 2026-06-28.
- Docker's MCP security source identifies MCP Rug Pull, MCP Shadowing, and Tool Poisoning as emerging tool-metadata and server-response risks, and argues for containerized MCP servers, gateway-style mediation, tool reauthorization on metadata change, and scoped secret injection. Source: `raw/2026-06-28-web-docker-blog-what-s-next-for-mcp-security.md`. confidence: 1 vendor security source, last-confirmed 2026-06-28.
- The OWASP GenAI AI Security Solutions Landscape capture is a quarterly landing page for mapping agentic AI lifecycle security solutions across DevOps and SecOps tasks; the capture does not contain enough product detail to rank individual tools. Source: `raw/2026-06-28-web-owasp-genai-security-project-ai-security-solutions-landscape-for-agent.md`. confidence: 1 low-detail OWASP landing-page capture, last-confirmed 2026-06-28.
- Docker's CRA and SBOM sources reinforce that agent-created container artifacts need supply-chain evidence, not only runtime sandboxing; see [[container-supply-chain-and-compliance]]. Sources: `raw/2026-06-28-rss-docker-blog-eu-cyber-resilience-act-cra-overview.md`; `raw/2026-06-28-rss-docker-blog-sbom-generation-for-container-workflows.md`. confidence: 2 related Docker sources, last-confirmed 2026-06-28.

### Typed entities
- tool/system: OpenClaw test instance
- model: Claude Opus 4.6
- threat: prompt injection
- threat: MCP Rug Pull
- threat: MCP Shadowing
- threat: Tool Poisoning
- control: MCP Gateway
- control: containerized MCP server
- resource: OWASP GenAI Security Solutions Landscape
- page: [[container-supply-chain-and-compliance]]

### Explicit relationships
- Model-side injection resistance complements but does not supersede execution-layer approval, identity, sandbox, and network controls.
- MCP Rug Pull is caused by tool metadata changing after approval; reauthorization and pinned tool definitions mitigate the drift.
- MCP Shadowing and Tool Poisoning are caused by malicious or conflicting tool descriptions influencing agent behavior; gateway scanning and minimal tool profiles reduce exposure.
- Security-solution landscapes complement local threat models, but low-detail landing pages do not provide enough evidence for procurement or approval.
- Container SBOM/provenance controls complement coding-agent sandboxing when generated code becomes deployable images.

### HoneyDrunk implications
- Treat the OpenClaw email challenge as encouraging evidence for model behavior, not a safety boundary for production deletes, credential use, deployment, payments, or external messaging.
- For MCP tools, record tool descriptions, versions, container image digests, network permissions, and secrets scope so later metadata drift can be detected.
- Use OWASP solution maps as discovery input only; approval still requires primary docs, local tests, and fit against HoneyDrunk threat boundaries.

### Privacy and quality notes
- No prompt-injection payloads, command strings, secrets, or reusable bypass details were copied.
- Simon Willison is a strong practitioner source but summarizes another challenge; Docker is vendor-authored; OWASP capture is low-detail.
