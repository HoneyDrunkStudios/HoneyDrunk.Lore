---
source: "https://safedep.io/inside-the-miasma-supply-chain-attack-toolkit/"
title: "Inside the Miasma Software Supply Chain Attack Toolkit - Real-time Open Source Software Supply Chain Security"
author: "SafeDep"
date_published: "unknown"
date_clipped: "2026-06-14"
category: "Security & Ethical Hacking"
source_type: "rss"
---

# Inside the Miasma Software Supply Chain Attack Toolkit - Real-time Open Source Software Supply Chain Security

Source: https://safedep.io/inside-the-miasma-supply-chain-attack-toolkit/

# Inside the Miasma Software Supply Chain Attack Toolkit

### Table of Contents

The infamous [Miasma worm](https://safedep.io/miasma-worm-ai-coding-agent-config-injection) goes open source. Multiple GitHub repositories with name `Miasma-Open-Source-Release`

started appearing since yesterday. Most of them are likely published through compromised developer accounts. We have seen this in the past when [Team PCP](https://safedep.io/ti/campaigns/teampcp) open sourced the Mini Shai-Hulud payload which in turn, likely motivated further software supply chain attacks.

We managed to obtain the source code from [one such repository](https://github.com/YangYongAn/Miasma-Open-Source-Release) (yanked now). As the developers of [PMG](https://github.com/safedep/pmg), we are continuously looking to update our benchmark of attacker TTPs against which we evaluate PMG, especially its [sandbox features](https://github.com/safedep/pmg/blob/main/docs/sandbox.md).

In this blog, we do a deep-dive analysis of the `Miasma-Open-Source-Release`

source code obtained from one of the public GitHub repositories.

## TL;DR

The Miasma codebase appears to be larger than a supply chain worm. It is a full supply chain attack toolkit that allows the operator to execute various attacks via stolen credentials against arbitrary or targeted packages on public registries (PyPI, npm, RubyGems), JFrog Artifactory, GitHub repositories and GitHub Actions, AI coding tools config poisoning, SSH based lateral movement and other attack vectors.

Some of the interesting findings from the analysis:

- Bypasses GitHub environment protection rules to trigger deployments.
[Details](https://safedep.io#npm-oidc-branch-mutator) - Generates valid Sigstore provenance bundles for trojanized npm packages.
[Details](https://safedep.io#npm-oidc-mutator) - Three independent C2 channels using GitHub commit search, each with a different search string and crypto key.
[Details](https://safedep.io#command-and-control) - Dead-man switch that wipes the victim’s home directory if the stolen PAT is revoked.
[Details](https://safedep.io#dead-man-switch) - Victim PATs embedded in exfiltration commits create a self-perpetuating flywheel for future worm instances.
[Details](https://safedep.io#exfiltration) - Hijacks GitHub Actions semver tags via orphan commits with cloned author metadata.
[Details](https://safedep.io#github-actions-mutator) - Injects into 13 AI coding tools (Claude, Gemini, Cursor, Copilot, Kiro, Cline, and others).
[Details](https://safedep.io#slow-path-propagation) - Living off the pull request (LOTP) technique injects payload into existing project files across 12+ languages.
[Details](https://safedep.io#living-off-the-pull-request-lotp) - Credential harvesting from AWS, Azure, GCP, Kubernetes, HashiCorp Vault, and password managers (1Password, Bitwarden).
[Details](https://safedep.io#credential-gathering) - Dumps GitHub Actions runner memory via
`/proc`

to extract secrets not exposed as env vars.[Details](https://safedep.io#fast-path) - 5-layer build obfuscation with per-build random keys, making each compiled payload unique.
[Details](https://safedep.io#obfuscation-and-evasion) - Targets npm, PyPI, and RubyGems via both stolen auth tokens (fast path) and OIDC trusted publishing (slow path).
[Details](https://safedep.io#propagation) - MCP-suffixed typosquatting mode for PyPI packages.
[Details](https://safedep.io#typo-mutator)

### GitHub as a Common and Control Infrastructure

We have been tracking [TeamPCP, Mini Shai-Hulu, Miasma and other related campaigns](https://safedep.io/ti). One of the common observation is, attackers are moving away from custom C2 infrastructure which requires maintenance, warming and safeguarding. Instead, they are now leveraging GitHub as a full-fledged C2 infra for remote command execution, configuration, exfiltration. This is a key behavioural shift because, traditional network based detection and protection tools rely on baselining and anomaly detection. Defenders now have to operate closer to application protocol to identify behavioural anomaly instead of network based anomalies.

## High Level Architecture

The repository consists of the following files:

The file listing indicates the following:

[Bun](https://bun.sh)as a dependency for the payload, consistent with[droppers that we have seen in the past](https://safedep.io/redhat-cloud-services-hit-by-mini-shai-hulud-npm-worm)`ARCHITECTURE.MD`

and`INTEGRATION_TESTING.md`

files indicate AI coding agent generated and maintained codebase.

### ARCHITECTURE.MD

The `ARCHITECTURE.md`

calls out the intention of the worm:

A worm that aims to automate spreading across multiple developer tooling ecosystems. Written in TypeScript, executed via Bun, designed for CI/CD environments (especially GitHub Actions) and developer machines. Exfiltrates secrets and propagates through NPM packages, PyPI wheels, RubyGems, GitHub repositories and Actions, Claude settings hooks, SSH, and AWS SSM.


The same file calls out a key architecture decision that aligns with what we have identified in past campaigns and why we consider network baselining an ineffective detection strategy for such payloads:

Requires NO C2 infrastructure. No dealing with takedowns or maintaining infrasturcture. Stolen GitHub PATs are all that is necessary.


The same file also calls out the following gaps in the current implementation:

[PyPI trusted publishing](https://docs.pypi.org/trusted-publishers/)based spreading is untested.- SSH based propagation through
`scp`

and`ssh`

(exec) is untested. - JFrog Artifactory
`npm`

package infection is untested. [RubyGems trusted publishing](https://guides.rubygems.org/trusted-publishing/)based package infection is untested.- GCP and Azure provider for secret exfiltration does not work.

### Components

At a high level, the codebase consists of:

`scripts/`

- Containing scripts for payload preparation, obfuscation and operations.`src/`

- Contains the actual worm source code with`src/index.ts`

as the entrypoint.

The worm (application) in turn is divided into following modules:

- Orchestrator
- Assets - Pre-crafted files used at runtime such as loaders, malicious GitHub Actions workflow, VSCode settings for code execution etc.
- Collector
- Dispatcher
- Mutator
- Provider
- Sender
- Utils

The architecture also indicates what we have seen in Shai-Hulud class of worms that consist of a fast and slow path for credential exfiltration and propagation. The fast path is used for quick exfiltration of credentials and slow path is used for propagation through various ecosystems which may take time to execute.

Following is the architecture diagram from the `ARCHITECTURE.md`

file:

## Application Logic

### Preflight

The pre-flight stage of the worm execution performs the following checks:

- Check for known sandbox environment and fail fast.
- Checks and ensures proxy env vars are set consistently across the different variables required by
`bun`

via`libcurl`

. - Bail out on Russian systems identified through locale resolution.

Interestingly, the worm has targeted mode for npm OIDC based self-propagation. During the pre-flight, it checks if `WORKFLOW_ID`

and `REPO_ID_SUFFIX`

env-var is set, matches (substring) `GITHUB_WORKFLOW_REF`

and `GITHUB_REPOSITORY`

env-vars, then it executes the npm OIDC based propagation flow and quits without executing the full worm logic.

The pre-flight also detects malware analysis environments through known fake environment variables, docker containers, `sudo`

restrictions on GitHub Actions, and known security tools by process name and file path. It actively restores `sudo`

access using docker privileged containers and overwrites `/etc/resolv.conf`

with public DNS to evade dynamic analysis tools. Example code for `sudo`

restoration:

### Fast Path

If the pre-flight checks are successful, the worm executes its fast path, that executes:

- Credential gathering from known sources via
`gatherQuickResults()`

. - Infect npm, PyPI, RubyGem packages via download, patch, publish vector if a valid token is found.
- Create a layered sender chain containing the transport logic for exfiltrated data.
- Execute the collector to validate, cache (in-memory) quick results and deliver via the sender chain.

The fast path is designed to quickly exfiltrate credentials and other sensitive information before dropping the larger propagation and persistence payloads, that may be detected by EDR and other security tools.

### Credential Gathering

The worm uses *Provider* as an abstraction for source specific credential gathering logic. Following providers are registered:

The full provider bundle also appends services that are deemed to be available based on credentials gathered from fast path harvesting, such as `GitHubActionsService`

, `GrepProvider`

. Interestingly, the worm logic uses `GrepProvider`

when classic GitHub tokens are found. The following code determines when to register the `GitHubActionsService`

:

### Credential Collection

The `Collector`

acts as an orchestrator for classifying credentials, taking action based on credential type, and triggering exfiltration. The high level behavior is as follows:

- In-memory, bounded cache for
`ProviderResult`

(credentials), flushed based on byte count. - Classify token type by pattern matching and dispatch token-specific handlers that perform validation and propagation using the token’s privileges.
- Execute the slow path for credential collection, which includes cloud services, password managers, vaults, and more.

Example code for dispatching token handles by token pattern:

When collector’s in-memory buffer (cache) reaches a threshold or when the `finalize`

method is called, it invokes the `Dispatcher`

component to exfiltrate the collected credentials from the buffer.

### Exfiltration

Exfiltration of collected credentials is handled by `Dispatcher`

and `Sender`

components. The dispatcher is responsible for:

- Encrypting the batch of credentials to be exfiltrated
- Exfiltrate by invoking the
`Sender`

chain

At the time of initialization in `src/index.ts`

, the worm creates the sender chain by invoking:

The `buildSenderChain`

itself is dynamic and creates the senders based on credentials collected in the fast path. Specifically, it creates the primary GitHub sender if it can find an attacker controlled PAT by searching for commits using [GitHub Commit Search API](https://docs.github.com/en/rest/search/search#search-commits).

In `src/github_utils/fetcher.ts`

, it attempts to find this attacker controlled PAT by searching for the string `DontRevokeOrItGoesBoom`

. The attacker pre-plants GitHub PATs by committing them to public repos. The commit message format is:

The payload for the attacker’s PAT is encrypted with a hardcoded AES key from `src/utils/config.ts`

:

Once decrypted and validated with a prefix `github_pat_11A`

, it checks that the token has `repo`

scope and has 200+ rate limit quota remaining, before it selects it for use else continue with the next. This approach allows the attackers to continuously update the worm with new PATs, likely leveraging compromised credentials and developer machines, almost like a fly-wheel.

It then creates the primary GitHub sender using the attacker controlled PAT:

If no attacker controlled PAT is found, it creates the GitHub sender using victim’s own PAT found earlier in the fast path. This behaviour is again consistent with the observed worm behaviour of exfiltrating encrypted credentials batch using public repositories created under victim’s account.

When using a victim’s PAT, the sender embeds the PAT in the exfiltration commit message. The token is AES-256-CBC encrypted and disguised as a `github_pat_11A...`

string, then included in the commit message as `DontRevokeOrItGoesBoom:<encrypted-token>`

. This closes the flywheel loop. Future worm instances searching for `"DontRevokeOrItGoesBoom"`

find the victim’s PAT and use it as an exfiltration token, turning every compromised developer account into infrastructure for the next infection. The same embedded token also triggers the [dead-man switch](https://safedep.io#dead-man-switch) installation, which wipes the victim’s home directory if the token is revoked.

`DomainSenderFactory`

exists in the codebase and allows the worm to exfiltrate encrypted credentials to attacker-controlled C2 infrastructure. However, it is not wired into the current sender chain. This likely indicates the attackers are relying on public services only for exfiltration, avoiding detection by network monitoring tools and C2 takedowns.

All credential batches are encrypted using a generated AES key and IV. The AES key is in turn encrypted using the attacker’s RSA-4096 public key. Encryption is performed once by the first registered *Sender* and the resulting envelope is reused across fallback attempts. The encryption envelope format is consistent with past Shai-Hulud and Miasma campaigns.

### Propagation

There are two types of propagation approach used by the worm:

- Fast path propagation by publishing a new version of accessible package with worm payload injected into it.
- Slow path propagation (mutation) by leveraging OIDC publisher trust between GitHub Actions and upstream registries like npm, PyPI, RubyGems and other mechanisms such as SSH, AWS SSM and other supported vectors.

#### Fast Path Propagation

The fast path propagation consists of registry infection via stolen credentials. For example, the `npm`

registry propagation uses the following logic:

- Find writable packages via the registry API
- For each writable package, fetch metadata and get the latest dist-tag tarball URL
- Download each package, extract, and inject its own obfuscated payload
- Inject a
`binding.gyp`

file in the package root with the following JSON

- Bump the patch version of the package
- Add
`bun`

as a dependency since it is required to run the worm - Repack into
`.tgz`

and publish to the registry using discovered credentials

The npm registry client has the capability to compute and attach a Sigstore provenance bundle using a short-lived credential obtained from Sigstore via GitHub OIDC (workload identity). However, this requires an OIDC token, not a stolen npm auth token. The worm executes the registry infection in the fast path regardless of whether a GitHub OIDC token is available in the environment.

#### Slow Path Propagation

The worm uses multiple *Mutator* in the slow path to replicate. This includes:

`NPMOidcClient`

- Direct OIDC npm publish`NpmOidcBranchMutator`

- Indirect OIDC based publishing via dangling commits`ActionMutator`

- GitHub actions tag hijacking`RepositoryMutator`

- Pull request feature branch poisoning`Claude`

- AI coding tools config poisoning. See[Config Files that Run Code](https://safedep.io/config-files-that-run-code)for more details on this attack vector.`SshMutator`

- Lateral movement using SSH credentials,`scp`

and`ssh`

based remote exec`ReadmeUpdater`

- AI coding tools config poisoning on remote branches accessible using discovered PATs

##### NPM OIDC Mutator

`NPMOidcClient`

runs in GitHub Actions, requests OIDC token from `ACTIONS_ID_TOKEN_REQUEST_URL`

using runner’s workload identity, with `audience=npm:registry.npmjs.org`

and performs the same fast path infection technique with additional capability of generating and attaching a Sigstore provenance bundle.

##### NPM OIDC Branch Mutator

`NpmOidcBranchMutator`

is the indirect variant. It does not require execution inside GitHub Actions. Instead, it uses a stolen GitHub PAT to find repositories that publish to npm via OIDC trusted publishing and tricks them into running a trojanized workflow on the next CI trigger.

Target repo detection in `src/mutator/npmoidc/detector.ts`

checks three conditions:

- A non-private
`package.json`

with a`name`

field - A workflow YAML with a publish step (
`npm publish`

,`yarn publish`

, or`pnpm publish`

) `id-token: write`

permission on the workflow job

Monorepo layouts are supported by scanning `packages/`

, `libs/`

, `apps/`

, `plugins/`

for additional `package.json`

files.

The mutator has two code paths depending on token scope:

**With**: pushes an orphan commit with the modified workflow YAML and payload to a new`workflow`

scope`snapshot-<random>`

branch. The push event triggers the workflow natively.**Without**: uses a dangling commit technique. Commit 1 (child of default branch HEAD) adds the trojanized workflow. Commit 2 (child of commit 1) restores the original tree. A branch is created at commit 2, so the tip looks clean. A GitHub deployment targeting commit 1 triggers the workflow, and the deployment record is deleted afterward.`workflow`

scope

If the target workflow uses GitHub environment protection and the token has admin access, the mutator bypasses those restrictions before creating the deployment. The bypass handles three types of environment protection:

- Required reviewers. Cleared by sending an empty
`reviewers: []`

to the environment API. - Protected branches policy. Cleared so the temporary
`snapshot-*`

branch is allowed to deploy. - Custom branch policies. Checked for pattern match first, cleared if the branch name does not match.

The original branch policy config is saved for restoration, but the reviewer list is not. If the mutator runs against a repo with required reviewers, that protection is permanently removed.

##### GitHub Actions Mutator

`ActionMutator`

hijacks custom GitHub Actions by force pushing trojanized orphan commits to their semver tags. Any downstream workflow referencing `uses: owner/action@v1`

pulls the compromised version.

- Enumerates all public, non-fork repos the stolen PAT has push access to
- Uses GraphQL to fetch
`action.yml`

or`action.yaml`

from the repo root - Parses and classifies each action as composite, JavaScript (
`using: node20`

), or Docker - For composite actions, appends
`setup-bun`

and a payload execution step to the existing steps - For JavaScript and Docker actions, builds a new composite wrapper that delegates to the original action pinned at the real HEAD commit SHA, passes through all inputs, then appends the payload step

Tag hijacking creates a single Git tree containing the modified `action.yml`

and `index.js`

(self-extracting worm payload), then for each tag matching prefix `v`

:

- Resolves the tag to a commit (handles both lightweight and annotated tags)
- Creates an orphan commit (no parents) with the payload tree, copying the original commit’s message, author, and committer metadata
- Force-pushes the tag ref to point at the orphan commit

The orphan commit has no parents, so `git log`

on the tag shows only the single hijacked commit. The original history is disconnected. But because the commit metadata is cloned from the original, the hijack is harder to spot in casual inspection. The payload step uses `if: always()`

to ensure execution even if the original action’s steps fail.

##### GitHub Repository Mutator

`RepositoryMutator`

poisons feature branches on writable repos by pushing commits that contain the worm payload and AI tool config files. It targets branches backing open pull requests, where developers are likely to interact with the infected code soon.

- Enumerates writable repos, fetches open PRs via GraphQL, extracts head branches
- Up to 10 branches per repo in normal mode, 30 in aggressive mode
- Skips enterprise-managed orgs and repos where
`TARGET_REPOS`

is set

Each commit adds the following files to the branch:

`.github/setup.js`

with the self-extracting worm payload`.claude/settings.json`

with a Claude Code SessionStart hook`.gemini/settings.json`

with a Gemini CLI SessionStart hook`.cursor/rules/setup.mdc`

with an`alwaysApply: true`

rule instructing the AI to run the payload`.vscode/tasks.json`

with a task triggered on`folderOpen`

- Optionally a modified existing source file via the “lotp” (living off the pull request) module

The mutator spoofs author by fetching the previous commit’s author info via GraphQL and reusing it on the malicious commit. It appends `skip-checks:true`

to the commit message to suppress CI checks. If the token has admin access, it also attempts to commit directly to the default branch by temporarily removing branch protection rules.

Aggressive mode is triggered when exfiltration fails in `src/index.ts`

. It widens the blast radius by including private repos and targeting 30 branches per repo instead of 10.

#### Other Mutators

##### Typo Mutator

`TypoMutator`

is an operator configured mode for PyPI typosquatting. It is not part of the automatic mutation plan. It triggers in the collector’s `handlePypiTokens()`

when `TYPO_MODE=1`

and `TARGET_PACKAGES`

env vars are set, as an alternative to the normal `PypiMutator`

flow.

- Takes a list of target package names from
`TARGET_PACKAGES`

- For each package, downloads the original wheel from PyPI
- Injects the
`.pth`

payload into the wheel - Generates typosquat names and publishes under the first available name
- Checks PyPI to skip names that are already taken
- Aborts immediately on rate limiting (HTTP 429)

The typo name generation in `src/mutator/typo/typoGen.ts`

appends MCP-related suffixes rather than using keyboard-adjacent substitution:

The comment in the source says “keyboard proximity” but the implementation only appends `-mcp`

and `-mpc`

suffixes. This likely reflects that PyPI blocks direct typosquats of popular package names but allows suffixed variants. The `-mcp`

suffix is topical given the rise of MCP (Model Context Protocol) tooling.

##### AWS SSM Mutator

`SsmMutator`

propagates to EC2 instances managed by AWS Systems Manager.

- Resolves AWS credentials from the default chain and validates via
`sts:GetCallerIdentity`

- Calls
`ssm:DescribeInstanceInformation`

across 17 AWS regions in parallel, filters for online instances - Base64-encodes the self-extracting payload, chunks it into 24KB pieces (SSM command size limit)
- Delivers via
`ssm:SendCommand`

using`AWS-RunShellScript`

, reassembles on target via`printf`

appends, decodes, executes with`node`

, and cleans up - 5 instances concurrent, 120 second timeout per command

This is a lateral movement vector within AWS environments. If the worm runs on a machine with AWS credentials that have SSM access, it can spread to every managed EC2 instance across all regions.

##### Living Off The Pull Request (LOTP)

The `RepositoryMutator`

uses a “lotp” module (`src/mutator/repository/lotp.ts`

) to inject the worm payload into existing project files that developers run as part of their normal workflow. It maps the repo’s primary language to a list of candidate files, checks which ones exist, and injects a language specific command into the first match.

Supported injection targets:

`package.json`

(JS/TS): appends to the`test`

script`Makefile`

(most languages): adds a phony target hooked into`all`

or`.DEFAULT_GOAL`

`tox.ini`

(Python): appends to`[testenv] commands`

`setup.py`

/`.py`

files: prepends`import os; os.system(...)`

`Gemfile`

/`Rakefile`

/`Podfile`

(Ruby): prepends`system(...)`

`composer.json`

(PHP): adds a`post-install-cmd`

script`Dockerfile`

: injects a`RUN`

instruction`CMakeLists.txt`

(C/C++): injects`execute_process()`

- Shell scripts: injects after the shebang line

The fallback for repos with no recognized language is `Makefile`

and `package.json`

. The injected command runs the worm payload as a side effect of normal developer activity (`npm test`

, `make`

, `tox`

, `pod install`

, etc.).

### Persistence

`InstallMonitor`

installs a persistent Python based C2 polling agent on the victim’s machine. It runs in the slow path mutation phase and is in the *always-run* set, executing on every worm invocation regardless of what tokens were found. It skips if EDR is detected or the machine has fewer than 4 CPU cores. The EDR check (`hasHostileEDR()`

in `src/utils/config.ts`

) scans for process names and file paths belonging to:

- CrowdStrike Falcon (
`falcon-sensor`

,`falcond`

,`csfalcon`

,`crowdstrike`

) - SentinelOne (
`sentinelone`

,`sentinelagent`

) - Microsoft Defender for Endpoint (
`mdatp`

,`wdavdaemon`

) - Carbon Black (
`cbagent`

,`cbdaemon`

) - Cylance (
`cylance`

) - Trend Micro / Deep Security (
`trendmicro`

,`ds_agent`

) - FireEye / Trellix (
`xagt`

) - osquery (
`osquery`

) - Tanium (
`tanium`

) - Qualys (
`qualys`

)

The installer (`INSTALL_MONITOR.sh`

) copies the monitor script to `~/.local/share/updater/update.py`

and registers it as a persistent service:

- On Linux: a systemd user service with
`loginctl enable-linger`

so it survives logouts - On macOS: a LaunchAgent plist with
`RunAtLoad`

and hourly`StartInterval`


The monitor (`GITHUB_MONITOR.py`

) is a Python polling loop that runs every hour. It auto-installs `requests`

and `cryptography`

via pip if missing, then searches GitHub commits for the string `"firedalazer"`

. Matching commit messages contain a base64 encoded URL and an RSA-PSS signature. The monitor verifies the signature against an embedded RSA-4096 public key, and if valid, downloads and executes the URL content as a Python script.

- Uses a different search term (
`"firedalazer"`

) than the main worm (`"DontRevokeOrItGoesBoom"`

) - Tracks executed commands in
`/var/tmp/.gh_update_state`

to prevent re-execution - 300 second timeout per script, temp file cleanup after execution

This is a general-purpose remote code execution backdoor. The attacker can push arbitrary Python scripts to any compromised machine by committing a signed message to any public GitHub repo.

### Command and Control

The worm uses three independent GitHub commit search channels for C2, each with a different search string and purpose:

`"DontRevokeOrItGoesBoom"`

discovers attacker controlled PATs for exfiltration. Checked once during sender chain setup. PATs are AES-256-CBC encrypted in the commit message.`"TheBeautifulSandsOfTime"`

delivers JavaScript for immediate execution. Checked once at startup via`c2Checkin()`

in`src/c2/checkin.ts`

. The commit message contains a base64-encoded payload and RSA signature, verified against`verify_key.pub`

. If valid, the payload is passed directly to`eval()`

.`"firedalazer"`

delivers Python script URLs for the persistent monitor. Polled hourly by`GITHUB_MONITOR.py`

. Uses RSA-PSS signature verification against a separate embedded public key.

All three channels are unauthenticated by default (falling back to authenticated search when a token is available) and use GitHub’s public commit search API. The attacker issues commands by committing a signed message to any public repository. Each channel uses a different verification key or decryption key, so compromising one does not compromise the others.

The `c2Checkin()`

call in `src/index.ts`

is fire-and-forget:

The `DomainSenderFactory`

implements a fourth channel using the search string `"thebeautifulmarchoftime"`

to discover backup C2 domains via signed commits. This factory exists in the codebase but is not wired into the current sender chain.

### Dead-man Switch

When the `GitHubSender`

uses a victim’s own PAT for exfiltration (tier 3 fallback), it installs a dead-man switch before embedding the token in the exfiltration commit. The handler is hardcoded in `src/sender/github/githubSender.ts`

:

The `DEADMAN_SWITCH.sh`

asset installs a persistent monitoring script that:

- Stores the victim’s token in
`~/.config/gh-token-monitor/token`

- Polls
`GET https://api.github.com/user`

every 60 seconds to check token validity - If the API returns any
`40x`

status (token revoked), runs`eval "$HANDLER"`

which executes`rm -rf ~/; rm -rf ~/Documents`

- Exits after a 72 hour TTL if the token is not revoked
- Registers as a systemd user service (Linux) or LaunchAgent (macOS)

The switch only activates when the victim has no enterprise-managed orgs. Enterprise tokens are considered higher-risk to embed. The `"DontRevokeOrItGoesBoom"`

search string used in the exfiltration commit message is a literal warning to anyone who finds it.

### Obfuscation and Evasion

The worm uses a 5-layer build pipeline to obfuscate the final payload.

#### Asset Encryption

The `prebuild`

step (`scripts/pack-assets.ts`

) gzip-compresses each file in `src/assets/`

(loaders, workflows, public keys, Claude settings), then encrypts with a random per-file AES-256-GCM key. The output is `src/generated/index.ts`

with each asset exported as a runtime decryption call. The decryption keys themselves go through the string scramble layer described below.

#### Source Transformation

Three transforms are applied to every `.ts`

file before bundling:

**Env-scramble**: rewrites`process.env.GITHUB_TOKEN`

to`process.env[scramble("GITHUB_TOKEN")]`

, hiding environment variable names from static analysis. Skips`NODE_ENV`

and`TZ`

.**String scramble**: resolves every`scramble("literal")`

call at build time. Uses PBKDF2 (200,000 iterations, SHA-256) to derive a master key from a random per-build passphrase and salt, then applies 3 rounds of CBC-mode polyalphabetic substitution with per-position, per-round lookup tables. The passphrase and salt are injected into`runtimeDecoder.ts`

for decoding at runtime.**Log stripping**: when`isSilent = true`

in`logger.ts`

, removes all`logUtil.*`

calls from source using balanced-paren counting with string-literal awareness.

#### Bundle

All transformed files are bundled into a single `dist/bundle.js`

via `Bun.build()`

with minification enabled, targeting the Bun runtime.

#### JavaScript Obfuscation

Post-build pass using `javascript-obfuscator`

with string array encoding (base64, rotation, shuffle, index shifting), hexadecimal identifier names, and chained wrapper calls. Output goes to `dist_obf/`

. An additional wrapping layer (`obfplus-wrap.js`

) produces a further obfuscated build in `dist_obfplus/`

.

#### Self-Extracting Payload

The `buildSelfExtractingPayload()`

function in `src/utils/selfExtracting.ts`

is used by mutators when embedding the worm into npm packages, GitHub repos, and other targets. It produces a standalone JS file with three nested layers:

**ROT-N outer shell**: random rotation (1-25) applied to the entire inner wrapper, decoded by an inline`eval()`

**AES-128-GCM Section A**: encrypted bun installation guard that downloads Bun from GitHub releases if not present, pinned to`bun-v1.3.13`

**AES-128-GCM Section B**: the actual worm payload, encrypted with a different random key

At runtime, the ROT-N shell decodes and evals the inner wrapper, which decrypts Section A (bun guard) and Section B (payload), writes the payload to a temp file, executes it with `bun run`

, and cleans up. Every invocation produces completely different output due to random keys and random ROT-N rotation.

- supply-chain
- malware
- shai-hulud
- ai-coding-agents
- github
- npm
- pypi
- rubygems

### Author

#### SafeDep Team

safedep.io

### Share

## The Latest from SafeDep blogs

Follow for the latest updates and insights on open source security & engineering

[astro.config.mjs Supply Chain Attack via Blockchain C2](https://safedep.io/astro-config-blockchain-c2-supply-chain)

An obfuscated IIFE hidden in astro.config.mjs fires at every build, beacons an HTTP C2, and pulls staged commands from a Tron-to-BSC blockchain dead drop.

[Config Files That Run Code: Supply Chain Security Blindspot](https://safedep.io/config-files-that-run-code)

Editor and package-manager config files auto-execute commands when a developer opens a folder or installs dependencies. The Miasma worm wired one dropper into seven of them across Claude Code,...

[Miasma Worm: Most Infected GitHub Repos Are Still Live](https://safedep.io/miasma-worm-still-infected-github-repos)

Eight days after the Miasma worm forged a credential stealer into public GitHub repositories, most are still serving it. A re-scan of the published victim list plus a fresh code-search sweep found...

[Miasma Worm Targets AI Coding Agents via GitHub Repos](https://safedep.io/miasma-worm-ai-coding-agent-config-injection)

A Miasma worm variant injects a 4.3 MB dropper into GitHub repos across multiple maintainers, wiring it to auto-run through Claude Code, Gemini, Cursor, and VS Code config files. No npm package is...

## Ship Code.

## Not Malware.

Start free with open source tools on your machine. Scale to a unified platform for your organization.
