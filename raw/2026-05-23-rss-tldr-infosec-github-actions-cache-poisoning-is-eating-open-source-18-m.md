---
source: "https://neciudan.dev/github-actions-poisoning"
title: "GitHub Actions Cache Poisoning is eating open source (18 minute read)"
author: "TLDR InfoSec"
date_published: "Fri, 22 May 2026 00:00:00 GMT"
date_clipped: "2026-05-23"
category: "Security & Ethical Hacking"
source_type: "rss"
discovered_via: "https://tldr.tech/infosec/2026-05-22"
source_role: "primary-via-tldr"
---

# GitHub Actions Cache Poisoning is eating open source (18 minute read)

Source: https://neciudan.dev/github-actions-poisoning

May 17, 2026 
· security · 18 min read 
GitHub Actions Cache Poisoning is eating open source Angular. tj-actions. Cline. TanStack. The same class of attack has been quietly hijacking publish pipelines for two years. Here's what it is, how it works, and what you need to do today. 
Neciu Dan May 17, 2026 
Hi there, it's Dan, a technical co-founder of an ed-tech startup, host of Señors at Scale - a podcast for Senior Engineers, Organizer of ReactJS Barcelona meetup, international speaker and Staff Software Engineer, I'm here to share insights on combining
technology and education to solve real problems. 
I write about startup challenges, tech innovations, and the Frontend Development. 
Subscribe to join me on this journey of transforming education through technology. Want to discuss
Tech, Frontend or Startup life? Let's connect. 
Website
Company
Subscribe 
Subscribing...
Share: Table of Contents What GitHub Actions cache poisoning actually is Why does it keep working What to audit in your repos today Audit 1: every pull_request_target workflow Audit 2: every workflow that interpolates untrusted input Audit 3: every workflow with id-token: write Audit 4: every third-party action pinned to a tag Audit 5: what your caches are keyed on Audit 6: your npm scope and publish rights What to change, in priority order 1. Remove every pull_request_target workflow that checks out PR code 2. Isolate or remove caches in release-capable workflows 3. Pin every third-party action to a commit SHA 4. Treat untrusted input as untrusted, especially around AI agents 5. Add zizmor or actionlint as a required PR check 6. CODEOWNERS on .github/ 7. Migrate to OIDC trusted publishing if you haven’t already 8. Enforce non-SMS 2FA on GitHub and npm 9. Set an install cooldown on your package manager 10. Treat AI agent config files as source code If you already got hit Closing References WHen I write an article, I try as much as possible to make it timeless. Thats why I avoid writing tips and tricks on AI because the ecosystem changes from month to month and then my article will become obsolete in a flash.
I hope this article becomes obsolete and in the future nobody talks about this subject anymore.
Because if you maintain a public repo with a publish pipeline on GitHub, there’s one class of attack you really need to know about.
It’s called GitHub Actions Cache Poisoning, and it’s been hijacking open-source projects for 2 years now. It usually shows up as part of a chain with one or two other GitHub Actions weaknesses, but the cache is almost always the way in.
Adnan Khan first demonstrated cache poisoning in 2024 against the Angular repo, as a research disclosure.
In March 2025, a related supply-chain attack on tj-actions/changed-files pushed malicious code into 23,000+ downstream workflows using the same runner-memory-dump technique attackers would later reuse.
In February 2026, cache poisoning compromised Cline ( I wrote about that one when it happened ), and 4,000 developers ended up with OpenClaw installed via the Cline CLI.
And last week (or from what time period you are reading this), on May 11 2026, the full chain (untrusted PR → poisoned cache → memory dump) got TanStack: 84 malicious versions across 42 @tanstack/* packages, in six minutes.
This article focuses on the mechanics: What it is, why it keeps working, and the checklist of things to audit and change in your own repo today.
I’m not going to walk through the TanStack incident step by step; their team published a really good postmortem that you should read if you want the full picture.
Let’s get started.
What GitHub Actions cache poisoning actually is 
Most CI workflows spend a lot of their time installing dependencies: npm install , pnpm install , pip install , downloading Rust crates, and building native modules.
On a fresh runner, all of that runs from scratch every time, even though the dependencies haven’t changed since yesterday.
GitHub Actions has a feature that lets you skip that work. After your workflow installs everything, you can tell Actions to save the resulting folder somewhere (typically node_modules or the pnpm store) and name it whatever you like.
The next workflow that runs and asks for the same name gets the folder back, ready to use, in a few seconds instead of a few minutes.
That stored folder is the cache. The name you choose for it is the cache key. Every GitHub repo gets up to 10 GB of cache space to use however it likes.
The key is something you build from the contents of the folder that identifies what’s in it. Most setups use the runner OS plus a hash of the lockfile, like this:
Linux-pnpm-store-${hashFiles('**/pnpm-lock.yaml')} 
If the lockfile changes, the hash changes, so you get a new key and a fresh install. If the lockfile doesn’t change, the key stays the same, and the cache is reused.
But that cache pool is shared across the whole repo. Workflows on different branches, with different triggers and jobs, all read and write to the same pool.
A PR build that ran yesterday can warm the cache for a release that runs today, because they compute the same key from the same lockfile. That’s by design; it’s what makes caching useful across a team.
It’s also exactly what makes it dangerous.
If an attacker can write to that cache pool, they can plant a poisoned dependency directory, a poisoned compiled binary, or a poisoned anything-else under a key that a later, higher-privileged workflow will look up.
When that workflow restores the cache, the attacker’s code lands on the runner before any of the legitimate steps run.
There are two main ways attackers get write access to the cache.
The direct write. The attacker tricks a privileged workflow into running their code. Then they compute the cache key the release workflow will use and write a poisoned entry under that key. This is what hit TanStack (via a pull_request_target workflow that checked out PR code) and what hit Cline (via a Claude issue-triage bot with prompt injection).
The eviction overwrite. Cache entries in GitHub Actions are immutable once written. You can’t overwrite an existing key. So if the legitimate cache entry already exists, the attacker fills the cache with 10 GB of junk to trigger GitHub’s LRU eviction, knocks the legitimate entry out, then writes a poisoned entry under the same key.
Adnan Khan published a proof-of-concept tool called Cacheract that automates this.
Once the cache is poisoned, the attacker just waits. The next time the release workflow runs, it restores the poisoned cache at normal speed.
The attacker’s code is now executing inside a workflow that has access to publish secrets.
Why does it keep working 
A few structural reasons.
The cache is shared across trust boundaries. 
A PR workflow, a scheduled job, an issue-triage bot, and the release workflow all read from the same pool by default. There is no built-in isolation between them, nor is there a built-in way to mark a cache entry as “production-only.”
permissions: contents: read doesn’t block cache writes. 
The cache uses a separate runner-internal token, not the workflow’s GITHUB_TOKEN . Locking down the workflow’s permissions feels like a mitigation, but it doesn’t stop cache poisoning. Adnan Khan documented this in 2024 .
OIDC trusted publishing collapses the trust boundary inside the workflow. 
When you migrate from a long-lived NPM_TOKEN to OIDC trusted publishing, you eliminate one whole class of attack: nobody can steal a static token from your secrets.
But in exchange, every step in the release workflow becomes publish-capable, because any step can request an OIDC token while the workflow has id-token: write .
That token sits in the runner’s worker process memory for a brief time, and any code running on the runner can read it.
pull_request_target is the most common entry point, but not the only one. 
Anything that runs untrusted code in a context that can write to the shared cache is a potential entry point. The Cline attack didn’t use pull_request_target at all; it used an AI issue-triage workflow triggered by issues: opened .
What to audit in your repos today 
Open your highest-trust repo and run through these. The commands work on any repo with a .github/workflows/ directory.
Audit 1: every pull_request_target workflow 
pull_request_target is a workflow trigger that runs with the base repo’s permissions and secrets, even when the PR comes from a fork.
It exists for legitimate reasons (labelers, comment bots, things that need to write back to the PR), but it bypasses GitHub’s “approve workflow runs for first-time contributors” safety gate.
That gate is what normally protects you from a stranger’s malicious PR.
With pull_request_target , there is no gate. So if a pull_request_target workflow also executes code from the PR, you’ve handed a stranger a shell on your CI with your secrets attached.
Start by finding every workflow that uses it:
grep -rn "pull_request_target" .github/workflows/ 
For each match, open the workflow and answer one question: does it check out or run any code from the PR? 
There are three patterns to look for.
First, an explicit checkout of PR code. The dangerous form looks like this:
- uses: actions/checkout@v4 
with: 
ref: refs/pull/${{ github.event.pull_request.number }}/merge 
# also dangerous: 
# ref: ${{ github.event.pull_request.head.sha }} 
# ref: ${{ github.event.pull_request.head.ref }} 
Any of those ref: values points to the PR’s code instead of the base repo’s code. Once checked out, the PR’s files (including scripts, configs, and lockfiles) sit on the runner, ready to be executed by any later step.
Second, a step that installs dependencies from PR-controlled files. npm install , pnpm install , pip install , cargo build , go build , anything that reads package.json , pnpm-lock.yaml , requirements.txt , Cargo.toml , or similar.
If those files came from the PR, the install step runs the lifecycle scripts the attacker added to them.
Third, any step that runs scripts from the checked-out tree directly: pnpm run build , npm test , ./scripts/setup.sh . These execute code straight from the PR.
If any of those three patterns show up in a pull_request_target workflow, you have what GitHub Security Lab calls a Pwn Request.
That’s exactly the pattern that hit TanStack.
Audit 2: every workflow that interpolates untrusted input 
grep -rnE '\$\{\{\s*github\.event\.(issue|pull_request|comment)\.' .github/workflows/ 
This is the Cline-shaped version of the audit. Look for any workflow that puts issue titles, comment bodies, PR titles, or PR bodies into a shell run: block or into a prompt for an AI assistant.
Any of those values is attacker-controlled.
Untrusted input flowing into run: is a form of script injection. Untrusted input flowing into an AI agent prompt is prompt injection.
Both end in arbitrary code execution on the runner.
Audit 3: every workflow with id-token: write 
grep -rn "id-token" .github/workflows/ 
Every match is a publish-capable workflow.
For each one, list every step it runs. Including third-party actions. Including setup actions. Including shell scripts. Each step inherits the workflow’s ability to mint an OIDC token.
For each step, ask: if this step were compromised, could it use the OIDC token to publish? If yes, the step is part of your publish trust boundary.
Audit 4: every third-party action pinned to a tag 
When your workflow says uses: actions/checkout@v4 , you’re telling GitHub Actions to run code from someone else’s repository.
actions/checkout is maintained by GitHub.
pnpm/action-setup is maintained by the pnpm team.
Every uses: line in your workflow is, effectively, a remote-code-execution agreement: their code runs on your CI runner, with your runner’s permissions, on every workflow run.
The question is how you tell GitHub which version of that code to run.
You have two options. You can pin to a version tag like @v4 or a branch like @main , which is what most tutorials show.
Or you can pin to a commit SHA like @39370e3970a6d050c480ffad4ff0ed4d3fdee5af , the full 40-character hash of a specific commit.
The difference matters because tags and branches are mutable.
The owner of the action repo can point v4 to a different commit at any time. If their account gets compromised (phishing, leaked token, stolen laptop), the attacker can re-tag v4 to a malicious commit.
Every workflow consuming @v4 pulls the new code on the next run. That’s exactly how tj-actions/changed-files got 23,000+ downstream workflows in March 2025, and it’s the same mechanism that lets a compromised action steal secrets from every repo using it.
Commit SHAs don’t have that problem.
A SHA points to a specific snapshot of the code that, mathematically, can’t be changed without producing a different SHA. If you pin to a SHA, you get exactly that code, every time, until you choose to update.
Find every action in your repo that’s not pinned to a SHA:
grep -rn "uses:" .github/workflows/ | grep -v "uses: \./" | grep -v "@[0-9a-f]\{40\}" 
That command lists every uses: line, excludes local actions ( uses: ./something ), and excludes anything pinned to a 40-character SHA.
What’s left are your tag-pinned and branch-pinned actions: anything you’ve trusted with mutable references.
Look at each result and ask whether you trust the maintainer enough to rerun their code on every workflow execution, assuming their account might be compromised tomorrow.
For most third-party actions, the honest answer is no. For first-party actions/* from GitHub itself, it’s a closer call, but I’d still pin them.
Run this audit even on actions you maintain yourself. TanStack’s bundle-size.yml used TanStack/config/.github/setup@main , a floating reference on their own internal actions repo.
Audit 5: what your caches are keyed on 
grep -rn "actions/cache" .github/workflows/ 
grep -rn "cache:" .github/workflows/ 
For each cache, find the key. Is it the same key your release workflow uses? If yes, a less-trusted workflow can poison it.
If you use pnpm/action-setup with cache: true (or the equivalent in actions/setup-node ), you almost certainly have shared cache keys between PR runs and release runs.
The default key is the lockfile hash, and it is the same on both.
Audit 6: your npm scope and publish rights 
The identity-side audit. For every package you publish:
npm access list collaborators < package-nam e > 
For every npm org you belong to:
npm team ls < or g > :developers 
npm team ls < or g > :publishers 
Look for accounts that shouldn’t be there: former contributors, inactive accounts, and personal accounts of people who left the team.
Every account with publish rights is a credential-theft target that can republish every package in the scope.
In your npm org settings, check whether 2FA is required for all writes, and whether SMS is still allowed as a method.
SMS is phishable and SIM-swappable; only TOTP or WebAuthn is safe.
npm view < packag e > time --json 
Anything in your publish history you don’t recognize is a problem.
What to change, in priority order 
This list mirrors what TanStack themselves are rolling out after their incident, plus a few additions from the Cline incident and Adnan Khan’s research.
1. Remove every pull_request_target workflow that checks out PR code 
If you don’t actually need write permissions or secrets on PR events, swap pull_request_target for pull_request . The latter runs with read-only permissions and no secret access on fork PRs, which is what you want for builds, tests, and benchmarks.
# before 
on : 
pull_request_target : 
paths : [ 'packages/**' ] 
# after 
on : 
pull_request : 
paths : [ 'packages/**' ] 
If you do need a privileged step on PR events, usually for labeling, commenting, or posting check results, split the work into two workflows. A trusted job triggered by pull_request_target that operates only on PR metadata and never runs PR code, and an untrusted job triggered by pull_request that runs the build with fork-scoped permissions.
GitHub’s docs include a canonical example using workflow_run for when a privileged job needs to react to an untrusted job’s results.
If you must keep a pull_request_target workflow that touches PR code (and you almost certainly don’t), at least gate it on the PR coming from the same repo:
jobs : 
benchmark : 
if : github.event.pull_request.head.repo.full_name == github.repository 
runs-on : ubuntu-latest 
# ... 
That guard means the job runs only on PRs from branches in the base repo, not from forks. Defense in depth, not a fix.
2. Isolate or remove caches in release-capable workflows 
The simplest fix, and the one TanStack chose first, is to turn caching off entirely in any workflow that has id-token: write :
# release.yml 
jobs : 
publish : 
permissions : 
id-token : write 
contents : read 
steps : 
- uses : actions/checkout@<sha> 
- uses : pnpm/action-setup@<sha> 
- uses : actions/setup-node@<sha> 
with : 
node-version : 20 
# no `cache: 'pnpm'`; caching is explicitly disabled 
- run : pnpm install --frozen-lockfile 
- run : pnpm publish 
Release workflows don’t run often. The few seconds you save with caching aren’t worth what we just walked through.
If you really want to keep the cache, use actions/cache/restore and actions/cache/save separately with explicit scopes, and make sure the cache key is scoped to release runs:
- uses : actions/cache/restore@<sha> 
with : 
path : ~/.local/share/pnpm/store 
key : release-pnpm-store-${{ hashFiles('pnpm-lock.yaml') }} 
# different key prefix from PR workflows 
3. Pin every third-party action to a commit SHA 
# before 
- uses : pnpm/action-setup@v3 
- uses : actions/setup-node@v4 
# after 
- uses : pnpm/action-setup@a7487c7e89a18df4991f7f222e4898a00d66ddda # v3.0.0 
- uses : actions/setup-node@39370e3970a6d050c480ffad4ff0ed4d3fdee5af # v4.1.0 
Keep the version comment. Dependabot and Renovate both support SHA pinning natively and will open PRs when a new tag is released, with the new SHA and the new version comment.
If you maintain a shared actions repo for your own org, the same rule applies. TanStack’s bundle-size.yml referenced TanStack/config/.github/setup@main , a floating ref on their own internal actions. Floating refs on internal repos are still mutable; pin them.
4. Treat untrusted input as untrusted, especially around AI agents 
Never interpolate github.event.issue.title , comment.body , pull_request.title , or anything else attacker-controlled directly into a run: block or an AI prompt. For shell, use environment variables instead:
# bad 
- run : echo "Triaging issue : ${{ github.event.issue.title }}" 
# good 
- run : echo "Triaging issue : $TITLE" 
env : 
TITLE : ${{ github.event.issue.title }} 
For AI agents that triage issues or comments, restrict the tools you grant them access to.
The Cline triage bot was given Bash , Read , Write , and Edit permissions on the runner. With that toolset, prompt injection in an issue title could result in arbitrary code execution on a workflow runner that shared a cache with the release pipeline.
Don’t grant Bash to a workflow triggered by issues: opened unless you have a very specific reason.
5. Add zizmor or actionlint as a required PR check 
zizmor is a static analyzer for GitHub Actions workflows. It catches dangerous patterns at PR review time, including pull_request_target with PR checkout, tag-pinned actions, untrusted-input interpolation, and more.
# .github/workflows/lint-workflows.yml 
name : Lint workflows 
on : 
pull_request : 
paths : [ '.github/workflows/**' ] 
jobs : 
zizmor : 
runs-on : ubuntu-latest 
steps : 
- uses : actions/checkout@<sha> 
- uses : woodruffw/zizmor-action@<sha> 
Mark it as a required check in branch protection. New workflow patterns get reviewed by something that doesn’t forget.
6. CODEOWNERS on .github/ 
Anyone who can merge a change to .github/workflows/ can change your entire CI security posture. Lock that folder to a small group:
# .github/CODEOWNERS 
/.github/ @your-org/core-maintainers 
Combined with branch protection that requires CODEOWNERS review, this stops a less-trusted maintainer’s account compromise from turning into a workflow rewrite.
7. Migrate to OIDC trusted publishing if you haven’t already 
The takeaway from TanStack is not to go back to long-lived tokens.
OIDC is still better.
A long-lived NPM_TOKEN in GitHub Secrets is reachable by every workflow with access to secrets, and it persists until you rotate it.
An OIDC token is valid for seconds within a single workflow run. The TanStack chain only worked because they hadn’t audited what else was running inside the OIDC-capable workflow. Items 1 through 3 above are how you keep that audit clean.
npm has the official setup docs. A minimal release workflow looks like this:
name : Release 
on : 
push : 
branches : [ main ] 
jobs : 
publish : 
runs-on : ubuntu-latest 
permissions : 
id-token : write 
contents : read 
steps : 
- uses : actions/checkout@<sha> 
- uses : actions/setup-node@<sha> 
with : 
node-version : 20 
registry-url : 'https://registry.npmjs.org' 
- run : npm ci 
- run : npm publish --provenance --access public 
The --provenance flag publishes a signed statement of which GitHub workflow built the tarball, so downstream consumers can verify it against the trusted-publisher binding. The malicious cline@2.3.0 didn’t have provenance, because it wasn’t published from a workflow.
8. Enforce non-SMS 2FA on GitHub and npm 
For every maintainer with publish access. No exceptions, including the people who keep forgetting their TOTP app. SMS is phishable, SIM-swappable, and not a real second factor in 2026.
In your npm org settings, require 2FA for writes. In your GitHub org settings, require 2FA and disable SMS as a method. These are checkboxes; flip them. TanStack had 2FA enforced on npm but allowed SMS until after the incident.
9. Set an install cooldown on your package manager 
pnpm 11+ ships with minimumReleaseAge on by default at 1440 minutes (24 hours), which refuses to install package versions younger than that. yarn 4+ has npmMinimalAgeGate in .yarnrc.yml . UV supports exclude-newer . bun has the same setting.
# pnpm-workspace.yaml 
minimumReleaseAge : 4320 # minutes; 72 hours 
minimumReleaseAgeExclude : 
- '@my-org/*' # internal packages bypass the gate 
The most effective passive defense against unknown future supply-chain attacks.
If you’d had a 24-hour cooldown enabled on May 11, you wouldn’t have installed the compromised TanStack versions, because they were detected and pulled within hours.
10. Treat AI agent config files as source code 
The TanStack payload writes .claude/settings.json , .claude/setup.mjs , and .vscode/tasks.json into victim repositories using the GitHub GraphQL createCommitOnBranch mutation. These files configure your AI coding agent or editor to execute arbitrary code when the project is opened.
Version-control them. Review changes to them in PRs. Add them to CODEOWNERS. They’re not config; they’re code execution.
If you already got hit 
Everything above is preventative. If you ran npm install against any of the affected versions on May 11, or any future version of a compromised package, you have a different problem to solve first.
⚠️ Stop. Read this before you revoke any credentials.
A researcher noticed the TanStack campaign payload installs a dead-man’s switch. It’s a small background service whose only job is to watch whether the stolen GitHub token still works.
On Linux, it lives at ~/.local/bin/gh-token-monitor.sh , registered as a systemd user service. On macOS, it runs as a LaunchAgent called com.user.gh-token-monitor .
Every 60 seconds, it pings api.github.com/user with the stolen token. The moment GitHub answers with a 40x because you revoked the token, the service runs rm -rf ~/ on your home directory.
Revoking first is the destructive path. Find and remove the watcher service before you touch your credentials.
# Linux 
systemctl --user list-units 
ls -la ~/.config/systemd/user/ 
# macOS 
launchctl list | grep gh-token-monitor 
ls -la ~/Library/LaunchAgents/ 
Other persistence mechanisms probably exist and haven’t been fully analyzed yet, so a clean reinstall of the install host is the safest path.
Once persistence is gone, rotate everything the host had access to: AWS, GCP, Kubernetes, Vault, GitHub, npm, and SSH.
Closing 
GitHub Actions cache poisoning is a structural property of how the cache is shared across trust boundaries inside your workflows.
As long as that property exists, attackers will keep finding new entry points to abuse it: PR checkouts in pull_request_target , prompt injection in AI bots, malicious reusable actions, things nobody has thought of yet.
Audit your own repo today.
References 
TanStack, Postmortem: TanStack npm supply-chain compromise 
SafeDep, Mass Supply Chain Attack Hits TanStack, Mistral AI npm and PyPI Packages 
GitHub Security Lab, Preventing pwn requests 
Adnan Khan, The Monsters in Your Build Cache: GitHub Actions Cache Poisoning 
Adnan Khan, Clinejection: Compromising Cline’s Production Releases just by Prompting an Issue Triager 
My earlier writeup on Cline: How to steal npm publish tokens by opening GitHub issues 
StepSecurity, tj-actions/changed-files action is compromised 
GitHub Security Advisory, GHSA-g7cv-rxg3-hmpx (full list of affected TanStack versions) 
npm docs, Trusted Publishers 
zizmor , workflow static analyzer 
Cacheract , Adnan Khan’s cache-poisoning proof-of-concept tool 
⚡ LIVE · NEXT SESSION THURSDAY MAY 28th · LIMITED SEATS 🏆 SOLD OUT IN SINGAPORE · ATHENS · LONDON
From Lizard to Wizard 
4-hour remote system design intensive. 
Chat apps, microfrontends, BFF, SDUI, event-driven, observability.
€299 4-HOUR INTENSIVE Save your seat → Spots are vanishing. Don't be the one who waited.
security github vulnerability open-source Share: Discover more from The Neciu Dan Newsletter A weekly column on Tech & Education, startup building and occasional hot takes.
Over 1,000 subscribers
Website
Company
Subscribe 
Subscribing...
