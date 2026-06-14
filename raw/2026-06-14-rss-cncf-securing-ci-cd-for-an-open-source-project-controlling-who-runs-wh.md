---
source: "https://www.cncf.io/blog/2026/06/04/securing-ci-cd-for-an-open-source-project-controlling-who-runs-what/"
title: "Securing CI/CD for an open source project: Controlling who runs what"
author: "CNCF"
date_published: "2026-06-04"
date_clipped: "2026-06-14"
category: "DevOps & CI/CD"
source_type: "rss"
---

# Securing CI/CD for an open source project: Controlling who runs what

Source: https://www.cncf.io/blog/2026/06/04/securing-ci-cd-for-an-open-source-project-controlling-who-runs-what/

## Part one

The last twelve months have been rough on the open source supply chain. [Axios was compromised on npm](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan) and shipped a remote access trojan inside otherwise normal-looking releases. [LiteLLM’s PyPI package was hijacked](https://futuresearch.ai/blog/litellm-pypi-supply-chain-attack/) to exfiltrate environment variables. [Typosquatted forks of Trivy](https://rosesecurity.dev/2026/03/20/typosquatting-trivy.html) were published to catch people who fat-finger go install. And the canonical example, the [2020 SolarWinds breach](https://en.wikipedia.org/wiki/2020_United_States_federal_government_data_breach), is still the cautionary tale we keep coming back to: attackers got into the build system and pushed malware through normal Orion updates to roughly 18,000 organizations, including U.S. federal agencies, NATO, and Microsoft. The malware sat dormant for months. The breach went undetected for the better part of a year.

Cilium runs in the kernel-level networking path of millions of Kubernetes pods. If our supply chain were compromised, the blast radius would not be small. Hardening the project against that scenario is something we work on continuously, and we wanted to write down what we actually do, in detail. Most of what follows isn’t Cilium-specific: any open source project running CI/CD on GitHub Actions can apply these patterns. We’ve also called out where we still fall short, in case any of it makes a useful starting point for someone else.

This is the first post in a three-part series. This post covers access control: who can trigger builds and what code CI is allowed to execute. Part 2 will cover dependency hardening, and Part 3 credential isolation, release verification, and the gaps we’re still closing.

**TL;DR**

If you don’t have time to read the whole series, here’s what Cilium does to harden its supply chain today, organized by which layer of the pipeline each control lives at:

| Layer | Control | What it does |
| Who triggers builds |
|

[Two-phase checkouts for pull_request_target](https://cilium.io/blog/2026/05/06/securing-cicd-open-source-lessons-from-cilium/#separating-trusted-and-untrusted-code-in-ci)[CODEOWNERS gates](https://cilium.io/blog/2026/05/06/securing-cicd-open-source-lessons-from-cilium/#codeowners-as-a-review-gate)[SHA-pinned actions and images](https://cilium.io/blog/2026/05/06/securing-cicd-open-source-lessons-from-cilium/#pinning-github-actions-by-sha-digest)[Renovate](https://cilium.io/blog/2026/05/06/securing-cicd-open-source-lessons-from-cilium/#automated-updates-with-a-trust-boundary)keeps the pins fresh and waits 5 days before picking up new releases.[Vendored Go dependencies](https://cilium.io/blog/2026/05/06/securing-cicd-open-source-lessons-from-cilium/#go-module-vendoring)[Static analysis on workflows](https://cilium.io/blog/2026/05/06/securing-cicd-open-source-lessons-from-cilium/#catching-mistakes-with-static-analysis)[CI vs. production credential isolation](https://cilium.io/blog/2026/05/06/securing-cicd-open-source-lessons-from-cilium/#ci-vs-production-credential-isolation)[Signed releases](https://cilium.io/blog/2026/05/06/securing-cicd-open-source-lessons-from-cilium/#signing-and-attesting-what-we-ship)[Sigstore Cosign](https://github.com/sigstore/cosign)using keyless OIDC, with SBOM attestations attached.[Gaps we’re still closing](https://cilium.io/blog/2026/05/06/securing-cicd-open-source-lessons-from-cilium/#what-were-still-working-on)## Controlling who runs what

The first question in any CI supply chain story is: who can trigger a build, and what code does it execute? Plenty of CI compromises start right here, by tricking the system into running attacker-controlled code with elevated privileges.

### Workflow trigger restrictions with Ariane

[Ariane](https://github.com/cilium/ariane) is a GitHub bot we wrote in-house to dispatch CI workflows from PR comments. When a maintainer types /test or /ci-eks on a pull request, Ariane checks that the commenter belongs to the organization-members team, figures out which workflows to fire (including dependencies, like tests that need a fresh image build first), and dispatches them via workflow_dispatch.

The interesting bit is the allow-list. Only verified org members can trigger workflows, and the set of workflows that can be triggered is enumerated by hand in the config:

`.github/ariane-config.yaml`


```
allowed-teams:
- organization-members
triggers:
/test\s*:
workflows:
- conformance-aws-cni.yaml
- conformance-clustermesh.yaml
- conformance-eks.yaml
# ...and so on
depends-on:
- /build-images-dependency
/ci-aks:
workflows:
- conformance-aks.yaml
depends-on:
- /build-images-dependency
```


A random external commenter typing /test in a PR is ignored. They can’t kick off our expensive cloud-provider conformance suites or burn through our CI minutes.

### Separating trusted and untrusted code in CI

When somebody opens a PR we need to build their code, but we obviously can’t trust it. This is the classic [pull_request_target problem](https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/). We avoid pull_request_target where we can, but a handful of workflows still need it, and we wrap those in mitigating controls.

The image build workflow is the canonical example. It splits the checkout in two:

```
.github/workflows/build-images-ci.yaml
```


```
- name: Checkout base or default branch (trusted)
uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
with:
ref: ${{ github.base_ref || github.event.repository.default_branch }}
persist-credentials: false
# ...trusted setup steps run here, including loading composite actions...
# Warning: since this is a privileged workflow, subsequent workflow job
# steps must take care not to execute untrusted code.
- name: Checkout pull request branch (NOT TRUSTED)
uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
with:
persist-credentials: false
ref: ${{ steps.tag.outputs.sha }}
```


The first checkout grabs the *base branch* (code that’s already been reviewed and merged) so we can load our composite actions, scripts, and the Cosign signing logic from a known-good source. Only after that does the workflow check out the PR head, and that checkout is used purely as build context for docker build. Nothing from the PR branch is ever executed as a script.

We get security reports about this pattern fairly regularly. Automated scanners and well-meaning researchers see “pull_request_target plus a second checkout” and flag it as a vulnerability. In the general case they’re right too. In ours, the workflow is intentionally designed so the pattern is safe:

- No run: steps execute scripts from the untrusted checkout. Every shell block after the second checkout is written inline in the workflow YAML (disk usage checks, file copies, digest output). Nothing is sourced from the PR branch.
- No composite actions are loaded from the untrusted checkout either. All composite actions (set-runtime-image, cosign, set-env-variables) come from the trusted base-branch checkout or from the saved ../cilium-base-branch/ directory. We’re also working on moving these composite actions into a dedicated repository so we don’t have to check out source to run them at all.
- Docker BuildKit does execute the untrusted Dockerfile, and that’s the whole point of building a CI image from a PR. BuildKit runs in isolation: no GitHub Actions environment variables, no repo secrets, no access to the runner’s Docker credential store. The build args we pass contain no secrets, just the runtime image reference and the operator variant name.
- Untrusted data flows into exactly one trusted action. The runtime-image*.txt file from the PR is fed into the trusted set-runtime-image action, which checks the image reference starts with quay.io/cilium/ and strips newlines so an attacker can’t smuggle in a GITHUB_ENV injection. There’s no way to repoint the build to anything outside the Cilium namespace.
- Only CI credentials are in scope. The Docker login uses QUAY_USERNAME_CI / QUAY_PASSWORD_CI, which can only push to the -ci development registry. Production credentials aren’t on the runner at all.

The worst-case outcome of a compromised PR build is a malicious CI image landing in the development registry, which is the same blast radius any CI system that builds contributor code carries. We do appreciate every report and read each one carefully, but this pattern is intentional.

### CODEOWNERS as a review gate

We lean on [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) pretty heavily so that changes always land in front of the people with the most context. For CI configuration that means anything under .github/ is owned by @cilium/github-sec (our security-focused CI team) plus @cilium/ci-structure, and the auto-approve.yaml workflow is owned by @cilium/cilium-maintainers:

```
/.github/ @cilium/github-sec @cilium/ci-structure
/.github/ariane-config.yaml @cilium/github-sec @cilium/ci-structure
/.github/renovate.json5 @cilium/github-sec @cilium/ci-structure
/.github/workflows/ @cilium/github-sec @cilium/ci-structure
/.github/workflows/auto-approve.yaml @cilium/cilium-maintainers
```


Nobody can change the CI pipeline without an explicit review from the team responsible for keeping it safe.

Next up, Part 2 we will cover how we lock down what code builds actually pull in: SHA-pinned actions, automated dependency updates, and Go module vendoring.

*André Martins is a Cilium maintainer and Software Engineer, Isovalent at Cisco. Feroz Salam is a member of the Cilium Security Team and a Security Engineer, Isovalent at Cisco. Find Cilium on *[GitHub](https://github.com/cilium/cilium) *and join the community on **Slack**.*
