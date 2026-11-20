---
source: "https://www.harness.io/blog/flaky-test-tooling-landscape-2026"
title: "The 2026 Flaky-Test Tooling Landscape: What Independent Reviews Actually Say"
author: "Shibam Dhar"
date_published: "2026-11-17"
date_clipped: "2026-11-20"
category: "DevOps & CI/CD"
source_type: "rss"
discovered_via: "https://tldr.tech/devops/2026-11-20"
---

# The 2026 Flaky-Test Tooling Landscape: What Independent Reviews Actually Say

A test fails in CI. You rerun the pipeline without touching a single line of code, and this time everything passes. The commit ships. Nobody files a ticket.

Three weeks later, the same test fails on a different branch. Then on main. By the time anyone looks, it has been flaking quietly for a month, and nobody can agree whether it ever caught a real regression or just burned CI minutes.

This is what makes flaky tests expensive. The direct cost of rerunning them is real, but the compounding cost is reader trust. Once a team stops believing a red pipeline, they stop blocking merges on it, and the whole point of CI collapses from the inside.

By 2026, the market has responded. CI platforms ship same-commit flaky detection and quarantine policies. Dedicated reliability vendors sell detection and recovery workflows as a layer on top of your existing CI. Test-observability platforms wire the whole lifecycle into their broader instrumentation. Every vendor page promises better reliability. The useful question is harder: **what does independent evidence actually say about any of this?**

## Independent research says reruns are not enough

The dominant detection approach in the literature and in most vendor products is still dynamic rerun-based: run a test enough times and inconsistent outcomes expose flakiness. Recent independent studies suggest that is a shakier foundation than product pages imply.

A[2026 study in IEEE Transactions on Software Engineering](https://xplorestaging.ieee.org/document/11673059/) analyzed 8.8 billion test executions across four industrial projects and found that **9.8% to 16.3% of failed pipeline runs involved flaky failures that existing detection mechanisms missed.** Failure rates also varied by as much as three times between environments, meaning the test environment itself is a variable the detection logic is usually blind to.

A [2026 evaluation of Shaker for Python projects](https://arxiv.org/abs/2609.25528) pushed on this further. Across 137 paired tests, Shaker's stress-based detection caught 37.2% of known flaky cases, ordinary reruns caught 35.8%, and the difference was not statistically significant.

***Detection methodology matters less than knowing what your tool misses.*** The real differences across vendors are not whether they detect flaky tests; they are what happens next: how a flaky test is quarantined, what evidence survives quarantine, how a team learns the test has been fixed, and what adoption actually costs.

## The seven tools in play

The 2026 landscape sorts into three groups. CI-native capabilities inside the platform you already use (Harness CI, Buildkite Test Engine, CircleCI). A dedicated reliability layer on top of any CI (Trunk, BuildPulse, Mergify). A test-observability model inside a broader platform (Datadog).

| Tool | Detection | What quarantine does | Primary focus |
| --- | --- | --- | --- |
| **Harness CI** | Same-commit inconsistency | Test keeps running, failures excluded from pipeline status | CI-native reliability |
| **Buildkite Test Engine** | Historical monitors | Muted (runs, failures ignored) or Skipped (does not run) | Configurable test state |
| **CircleCI** | Same-commit plus auto reruns | Failed-test retry, test-atom metered | CI-integrated optimisation |
| **Trunk Flaky Tests** | Flakiness monitors | Keeps running without blocking the job | Dedicated reliability layer |
| **BuildPulse** | Git-based plus statistical | Quarantine list exposed via API, CI skips | Impact and prioritization |
| **Mergify Test Engine** | Default-branch plus PR reruns | Quarantine with continued reporting | Prevention before merge |
| **Datadog Test Optimization** | Historical plus Early Flake Detection | Active, Quarantined, Disabled, Fixed lifecycle | Reliability inside observability |

*Capabilities drawn from vendor documentation. No independent benchmark exists comparing detection accuracy across all seven under equivalent conditions, so this is not a scoreboard.*

### The Harness agent: flaky management inside the pipeline

The Harness agent treats flaky-test management as part of normal CI, not a separate product. That matters because every other tool on this list is either an add-on with its own ingestion contract or a workflow that only lights up above a plan tier. The Harness agent ships detection, test-health visibility, and quarantine inside the stage the test already runs in.

Per the [Flaky Test Detection docs](https://developer.harness.io/docs/continuous-integration/use-ci/run-tests/test-management/ci-flaky-tests/), a test is flaky when it has both passed and failed on the same commit inside a 14-day observation window. It clears after five consecutive successful executions or when no inconsistency has occurred for 14 days. The 14-day window is the same window CircleCI uses, which is useful because detection semantics are at least consistent across the CI-native options.

[Test Management](https://developer.harness.io/docs/continuous-integration/use-ci/run-tests/test-management/ci-test-management-overview/) layers test-health visibility and quarantine on top. A quarantined test keeps running, its results still land in the dashboard, and its failures can be configured to stop breaking the pipeline. Three ingestion models exist in Harness CI and they are not interchangeable: conventional JUnit `report.paths` gives test-level results and the standard Tests tab, [Harness Test Intelligence](https://www.harness.io/products/continuous-integration/test-intelligence) adds selective execution on top of that, and Test Management adds test-health, policies, and quarantine. A pipeline configured for one does not automatically light up the others. The broader framing of why test assertions in modern CI need to express intent is covered in the [intent-driven assertions blog](https://www.harness.io/blog/intent-driven-assertions), and the earlier [Test Intelligence deep-dive](https://www.harness.io/blog/test-intelligence) walks through how call-graph selection works on a Java codebase.

### Buildkite Test Engine: Muted vs Skipped is the whole decision

Buildkite builds flaky management around test state. The [test-state docs](https://buildkite.com/docs/pipelines/configure/tests/test-suites/test-state-and-quarantine/) define two behaviors. **Muted tests** keep running, their failures do not block the build, and data keeps flowing. **Skipped tests** do not run at all, which means the system cannot tell you whether they have recovered. Buildkite's own guidance is to prefer muting over skipping unless a test must not run. Skipping is a budget decision, not a reliability one.

Automated state-change workflows (quarantine on detection, recovery on sustained passing) are an Enterprise-plan feature. The Pro plan gives the primitives, with automation running through the REST API or UI. For teams weighing the two platforms side by side on CI reliability, the [Harness CI vs Buildkite comparison](https://www.harness.io/comparison-guide/harness-vs-buildkite) covers the broader fit.

### CircleCI: automatic reruns went GA this October

CircleCI's [Test Insights docs](https://circleci.com/docs/guides/insights/insights-tests/) use the same same-commit, 14-day definition of flakiness Harness does. The 2026 change is Smarter Testing. On [13 October 2026 CircleCI announced general availability](https://circleci.com/changelog/smarter-testing-is-now-generally-available/) of a bundle including automatic reruns, intelligent test selection, dynamic splitting, and analytics. Running tests, static splitting, and manual reruns stay free. The paid parts are metered through "test atoms" with a monthly allowance per plan and overage priced at 3,000 credits per 100,000 atoms evaluated.

Automatic reruns answer one question: is this failure reproducible? They are not a quarantine lifecycle. A test that passes on rerun is marked a potential flake, and the build continues. There is no notion of ownership, no automated reinstatement after N clean runs. The [CircleCI vs Harness CI comparison](https://www.harness.io/comparison-guide/circleci-vs-harness) maps where the two platforms diverge beyond the reruns feature itself.

### Trunk Flaky Tests: separating flaky from broken

Trunk builds flaky-test reliability as a product in its own right. Through [Trunk's quarantine](https://docs.trunk.io/flaky-tests/quarantining), known flaky tests keep running and reporting without blocking the job. The important design choice is one Trunk is explicit about: automated quarantine applies to tests already identified as flaky, not to tests that are consistently broken, because quarantining them hides a real regression.

The integration path matters. Trunk reports on the test results your CI uploads. If a failure happens outside the reported tests (a runner timeout, a stage-script exit code, a container OOM), Trunk cannot see it and cannot quarantine it. A green quarantine dashboard is only as safe as the ingestion feeding it, which is a general property of any dedicated-reliability layer sitting on top of a CI it does not control.

### BuildPulse: measuring the cost of flakiness

BuildPulse puts the operational cost of flaky tests front and centre. Its [Flaky Tests Dashboard](https://docs.buildpulse.io/flaky-tests/guides/Flaky%20Tests%20Dashboard) documents Git-based detection, which compares inconsistent outcomes against equivalent Git tree states, and statistical detection against thresholds. Beyond detection, BuildPulse surfaces metrics most CI platforms do not: disruption frequency per test, failed builds attributable to specific flakes, and engineering time lost.

Its [quarantine approach](https://docs.buildpulse.io/flaky-tests/guides/Test%20Quarantining) exposes a quarantine list through an API. The CI pipeline or test framework reads the list and skips those tests at execution time. Skipped tests do not generate fresh evidence, so the team decides, on a cadence, when to retest and when to restore. Nothing restores them automatically.

### Mergify Test Engine: catch flakes before they merge

Mergify splits the problem into Prevention, Detection, and Quarantine. [Detection](https://docs.mergify.com/test-engine/detection/) looks at test results on the default branch to find existing unreliable tests. That is where every other tool here operates. [Prevention](https://docs.mergify.com/test-engine/prevention/) operates on pull requests: with the right framework integration and a configured rerun budget, it reruns new or modified tests on the PR to expose inconsistent behaviour before merge. Catching flakes in prevention means the author sees the problem before merge and main never absorbs it.

### Datadog Test Optimization: observability for tests

Datadog's [Flaky Tests Management docs](https://docs.datadoghq.com/tests/flaky_management/) model a test's state as Active, Quarantined, Disabled, or Fixed, and track transitions. A quarantined test keeps its history, so when the team eventually investigates, the full timeline is there. [Early Flake Detection](https://docs.datadoghq.com/tests/flaky_tests/early_flake_detection/) proactively reruns previously unseen tests, similar in spirit to Mergify Prevention, wired into the same instrumentation that already watches your services.

Advanced test-management actions depend on native instrumentation and a minimum library version per language. Plain JUnit reporting lights up the dashboard but not the lifecycle actions. Early Flake Detection also adds executions, which have cost and runtime implications.

## The four questions that beat a feature matrix

A side-by-side feature grid misleads because the words mean different things across vendors. Four questions do more work than any grid.

**How does the tool identify a flaky test?** Same-commit inconsistency, PR reruns, and statistical detection against thresholds are three different signals. Each catches a different subset of flakes and misses a different subset. Ask vendors how much history they need, how they decide a test is "the same" across refactors, whether they consider environment variability, and what evidence they have about false positives and missed failures.

**What exactly does quarantine do?** Quarantine is one word doing two very different jobs. In one version, the test keeps running, its failures stop blocking merges, and the signal survives. This is the Harness and Trunk model. In the other, the test does not run at all, which saves time but destroys the only mechanism that would tell you it recovered. This is BuildPulse's default and Buildkite's "skip" state. **The second model is cheaper and more dangerous.**

**How does the team learn a test is fixed?** Detection is where every vendor markets. Recovery is where most of them go quiet. Who owns the quarantined test, how is ownership tracked, what gets reinstated automatically, what demands manual review. The Harness agent clears after five consecutive passes or a 14-day quiet window. CircleCI does not reinstate; it reruns. BuildPulse requires manual action. The differences are not cosmetic.

**What does adoption actually require?** A vendor supporting JUnit reports does not necessarily support quarantine on JUnit reports. Advanced detection often needs a native agent, a minimum library version, or an account feature flag. Add CI-provider compatibility, framework coverage, data retention, plan tier, and the extra test executions the detection logic spends, and the real cost picture gets clearer.

## What user reviews are actually good for

A [verified BuildPulse user review on G2](https://www.g2.com/products/buildpulse/reviews) praises the daily flaky-test alerts and complains about the subscription cancellation flow. That tells you something true for one real customer. It does not tell you whether BuildPulse's detection is better than Trunk's, because the reviewer never ran that comparison. **A good review tells you what the reviewer tested and under what conditions. A generic rating is a vibe.** Treat user reviews as evidence of adoption friction, support quality, and operational feel. Do not treat them as benchmarks.

## Which approach fits which team

There is no independently established universal winner across these seven products. The honest shape of the decision is this.

Teams that want detection, test-health visibility, and quarantine inside the CI stage, without maintaining a second ingestion contract on top, get the most compact answer from the Harness agent. The 14-day same-commit window matches the research-aligned definition of flakiness, quarantine keeps the test running so the signal survives, and the whole lifecycle sits in the same pipeline execution the team already debugs from. [Harness Test Intelligence](https://www.harness.io/products/continuous-integration/test-intelligence) brings selective execution and test-health signals into the same stage, and the [Harness University CI learning path](https://developer.harness.io/university) walks through how Test Intelligence and Test Management integrate.

Teams on another CI who do not want to move it, but do want governance on top, split between Trunk (quarantine with a clear flaky/broken distinction), BuildPulse (impact measurement and API-driven skipping) and Mergify (prevention before merge). Each sits above the CI, which also means each is bounded by the test results that CI emits.

Teams already deep in Datadog for application observability get the test lifecycle in the same instrumentation, with native-agent coverage as the trade-off to verify.

Whichever direction a team picks, the honest evaluation is the one the research recommends: run the candidate against a representative set of flaky tests, with comparable execution budgets, in environments close to production, and look at what the tool misses as closely as what it catches.

## A trustworthy pipeline is more than a green pipeline

Flaky-test management in 2026 has moved past "run it twice." Tools now stitch together detection, proactive reruns, quarantine, test-health dashboards, ownership, and recovery. The scope is bigger. The confidence should be more measured.

The research is clear on one thing: flakiness is hard to detect completely, and every detection technique has conditions under which it falls over. The useful tools are the ones that do more than hide failed builds. They help developers understand what went wrong, keep an audit trail on unreliable tests, and give the team a defensible way to restore confidence once a test is actually fixed.

The objective is not to make every pipeline green. It is to make a green pipeline mean something.

**To see how same-commit detection, quarantine policies, and test-health dashboards look wired into a working CI stage, the** **[Harness Test Management overview](https://developer.harness.io/docs/continuous-integration/use-ci/run-tests/test-management/ci-test-management-overview/)** **is the shortest path to that view, and the** **[Harness Continuous Integration](https://www.harness.io/products/continuous-integration)** **product page shows how it connects to the rest of the delivery pipeline.**
