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
