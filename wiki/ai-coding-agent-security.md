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
