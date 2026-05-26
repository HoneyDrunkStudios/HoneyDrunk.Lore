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
