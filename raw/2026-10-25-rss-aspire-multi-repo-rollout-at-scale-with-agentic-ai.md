---
source: "https://devblogs.microsoft.com/aspire/aspire-windows-365-part2/"
title: "Aspire Multi-repo Rollout at Scale with Agentic AI"
author: "Jeff Liu"
date_published: "2026-06-04"
date_clipped: "2026-10-25"
category: ".NET Ecosystem"
source_type: "rss"
---

# Aspire Multi-repo Rollout at Scale with Agentic AI

In our previous post, *[Aspire Multi-Repo Microservices – Windows 365 Integration Journey](https://devblogs.microsoft.com/aspire/aspire-windows-365/)*, we explored how we extended Aspire to unlock multi-repo microservice development, enabling teams to independently build, test, and debug microservices across repositories with a consistent developer experience. Building on that foundation, two follow-on challenges shaped the next chapter of the journey. First, the patterns had to become *reliable* – every service behaving deterministically and producing the same pass/fail result locally, in CI, and on every build agent. Second, the patterns had to *scale* – easily apply across dozens of repositories with fewer effort.

This Windows 365 Integration Journey part 2 blog post covers both halves of that work: the **Phase 2 reliability foundation** that turned intermittent failures into deterministic, testable behavior, and the **Phase 3 agentic-AI rollout** that put that reliability to work across the fleet – with Aspire as the control plane underneath both. We then look at the resulting adoption growth and what comes next.

## Windows 365 adoption journey

Windows 365’s Aspire adoption follows an evolving, multi-phase journey. This post focuses on the most recent phases that enabled scale, while additional phases will continue as the platform evolves:

* **Phase 1 – Functional Foundation.** Microservice F5 *just works*. Teams can clone a microservice repo, press F5, and run end-to-end microservices locally thanks to the multi-repo support we built on top of Aspire’s extensibility model – Aspire itself does not ship multi-repo as a built-in concept; we extended its resource and orchestration primitives to add it (detail covered in Part 1 blog).
* **Phase 2 – Reliability at Scale.** With the foundation in place, the next challenge was making it reliable. Early adoption exposed recurring failure patterns – Azure Functions startup issues, cold start and host isolation problems in cloud test, and inconsistent Cosmos DB emulator readiness. We addressed these systematically by standardizing runtime and SDK configurations, introducing explicit hosting patterns, and enforcing readiness-based health checks. These improvements turned intermittent failures into deterministic, testable behaviors, establishing a reliable baseline for every microservice.
* **Phase 3 – AI-Accelerated Rollout.** Once reliability was established, we could scale. Using agentic AI tools (GitHub Copilot SDK and the Microsoft Agent Framework) on top of Aspire, we automated rollout across the full set of Windows 365 microservice repos. Instead of manual onboarding, agents apply proven patterns end-to-end – checking health, fixing issues, and generating pull requests. **AI acts as an accelerator – but only because a solid, reliable foundation is already in place.**

## Phase 2 – Building a reliable baseline

Before anything reliable could be built on top, every service had to behave predictably in isolation. The Phase 2 work was unglamorous but load-bearing: turning a handful of intermittent, hard-to-reproduce failures into deterministic, testable behavior. We did this for plain human reasons – flaky tests slow down feature work, and *“works on my machine”* is not a debugging strategy. AI tooling was not on our radar yet at this point; the fact that these same patterns would later enable a fleet-scale automated rollout was a happy accident we only saw afterward.

### Standardized Azure Functions SDK and tooling configuration

Most of the early cloud test failures we saw were not in our service logic; they were related to Azure Functions worker/runtime versioning, the .NET SDK pinning that those projects depend on, or the Aspire workload version drifting between developer machines and the build agent. It took us longer than expected to isolate this. We spent multiple cycles chasing what looked like intermittent app bugs, with a fair amount of frustration across local runs, CI, and build agents that disagreed in subtle ways.

The turning point came when we partnered with the Aspire team and traced the issue end-to-end to SDK/tooling alignment. The root cause and requirement are explicitly documented in the Azure Functions host guidance: <https://aspire.dev/integrations/cloud/azure/azure-functions/azure-functions-host/>, including the key requirement: “You must use a .NET 9 SDK or later.” We also used Visual Studio tooling to check for workload and tooling updates, which closed the remaining environment drift across developer machines.

After that, we collapsed those degrees of freedom: a single `global.json` SDK pin per repo, a single Azure Functions worker version, and a shared set of analyzer and code-style packages declared via Central Package Management. The result is that the build a developer sees on their laptop is the build the pipeline sees, and the pipeline build is the build the agent sees.

### A shared `AppHostFixture` – a reusable reliability primitive

Parallel cloud test runs were the second source of flakiness. Tests would race each other for ports, container handles, and emulator state. We replaced ad-hoc test setup with a shared `AppHostFixture<TAppHost>` – a single, reusable component that became the standard way test in project obtains an AppHost. Beyond owning the in-process spin-up and deterministic teardown, the fixture does several things that turned out to matter for reliability:

* **Readiness-gated startup, not time-based waits.** Each test class declares the resources it needs healthy via `ResourcesToWaitForHealthy`, and the fixture blocks until each one transitions to running through `ResourceNotificationService`. No `Thread.Sleep`, no “give it 30 seconds and hope” – the test starts the moment the system actually reports ready.
* **A typed handle to the live `DistributedApplication` and `ResourceNotificationService`.** Tests get a real Aspire object graph, not a mock – they can resolve endpoints, query resource state, and listen for snapshot updates the same way any production observer would.
* **Per-resource console-log capture across the whole run.** The fixture subscribes to Aspire resource’s stdout/stderr stream and accumulates error- and warning-level lines. When a test fails, the captured per-resource snapshot is right there for triage – instead of re-running with extra logging.
* **Built-in assertions for silent misbehavior.** `AssertNoErrorLogsAsync` fails the test if any resource emitted an error during the run, and `AssertNoWarningFloodingAsync(maxOccurrences: 10)` fails if a single warning category repeats above the threshold. This catches the class of regression where the test “passes” but a service was logging exceptions throughout.

Above are some example of reliability fix in shared fixture. The investment paid to stabilize tests and enforce consistent practices.

### Readiness-based Cosmos health checks

The Cosmos DB emulator is fast on a warm machine and very slow on a cold one. Our original startup checks were time-based – wait N seconds, hope for the best – and were the largest single contributor to failing tests. We rewrote them as *readiness checks*: poll the emulator’s catalog endpoint until partitions are reported, then return healthy. The same check runs on the developer’s laptop, in CI, and on every build agent in the pipeline, and produces the same answer. Tests that used to fail one run in twenty stopped failing.

This work was done against the **GA (generally available) version of the Cosmos DB emulator**. We were aware that a newer vNext preview emulator was in development that addressed some of these startup and readiness issues. Once the preview stabilized and demonstrated consistent improvements, we started adopting it alongside the GA version – expanding test scenarios with both emulator versions to validate that the migration path was safe. We also got great help and support from the Cosmos DB emulator team along the process. While we were preparing this blog, the Cosmos DB emulator team just announced their GA, see [Announcing General availability of the Azure Cosmos DB vNext emulator](https://devblogs.microsoft.com/cosmosdb/announcing-general-availability-of-the-azure-cosmos-db-vnext-emulator/). We will soon fully switch to that, and expect that will further reduce the variance in startup behavior across development environments.

### Standardized health-check wiring on top of Aspire’s built-ins

Aspire ships `WithHttpHealthCheck` and `WaitFor` as built-in extension methods on `IResourceBuilder<T>` – Aspire is doing the HTTP polling, the dashboard reporting, and the lifecycle gating. What Aspire does not do out of the box is decide what “healthy” means for a specific service; that is a per-service implementation detail that must be defined by the application.

Our work in this layer was twofold. First, **standardize a consistent calling convention**: every service registers health check endpoints at `/health/ready` for readiness and `/health/live` for liveness. We created a small ServiceDefaults extension that wires up these endpoints, connects them to Aspire’s dashboard, and binds them to the `WaitFor` lifecycle gates in one place—so individual services only had to apply the pattern, not remember the recipe. This convention applied uniformly across every repo. Second, **implement service-specific readiness logic** – custom health checks that each endpoint exposes, such as Cosmos seed-data validation, data-explorer reachability, and domain-specific readiness criteria – all registered through the standard .NET `AddHealthChecks()` API. The payoff: when the Aspire dashboard reports a service as healthy, that report reflects a real, service-specific readiness contract—not just “the process is running”—and the same contract is validated on the developer’s laptop, in CI, and on every build agent.

### A required cloud test gate on every PR

Reliability that is not enforced regresses. Every pull request now blocks on a cloud test run that exercises the AppHost end-to-end against the emulator stack. The gate is fast enough to live with (under 20 to 30 minutes for the typical service, depending on emulator warm-up) and the failure messages are specific (which check, which container, which assertion). When the gate runs in that range and the failure messages are useful, expecting every PR to pass stops being an unreasonable ask.

### From reliable baseline to scalable rollout

By the end of Phase 2, every Aspire service shared the same load-bearing patterns just described. What we only noticed after Phase 2 completed was that every one of these patterns was concrete, scriptable, and deterministic. We had not designed them that way on purpose – we just wanted reliable services. But once we stepped back, the pattern was unmistakable: every case had a check, a fix, and a binary pass/fail result.

Two things converged at that point. First, applying these patterns by hand across the full set of microservice repos was clearly the bottleneck – onboarding each new service was weeks of repetitive, copy-paste-this-pattern work, and the infra team had become the rate-limiter. Second, the GitHub Copilot SDK reached preview around the same time, and the Microsoft Agent Framework began offering a clean way to compose agent workflows on top of it. For the first time, the question *“What if a workflow ran the checks, proposed the fixes, validated against cloud test, and opened the PRs at fleet scale?”* had a viable answer.

## Phase 3 – Multi-repo rollout at scale with agentic AI

Phase 3 is what came out of that convergence. With Aspire as the control plane and the Phase 2 patterns as the playbook, we could automate the rollout work. **AI acts as the accelerator – but only because the reliability foundation that makes acceleration safe was already in place.**

Here is a short demo of the Phase 3 rollout loop in action:

Aspire Multi-repo Rollout at Scale with Agentic AI[Watch on YouTube](https://www.youtube.com/watch?v=b9L2DfLH-_8)

What came out of that convergence is **MARS** (Multi-repo Agentic Rollout System) – a small fleet of specialized agents built on top of Aspire, the **[Microsoft Agent Framework](https://github.com/microsoft/agent-framework)**, and the **[GitHub Copilot SDK](https://github.com/github/copilot-sdk)**. MARS takes a rollout target – every repo must adopt pattern X – and drives it to completion across the fleet, repo by repo.

![MARS layered architecture](https://devblogs.microsoft.com/aspire/wp-content/uploads/sites/90/2026/06/mars-architecture.webp)

This shows a quick comparison of the manual vs. agentic flow: ![MARS advantage - manual per-repo onboarding vs AI-driven fleet rollout](https://devblogs.microsoft.com/aspire/wp-content/uploads/sites/90/2026/06/mars-advantage.webp)

### The agent loop: check -> plan -> fix -> validate -> learn

The thing that makes agentic rollout tractable is not the LLM – it is the loop the LLM runs inside. Every repo passes through the same five stages:

![The five-stage agent loop](https://devblogs.microsoft.com/aspire/wp-content/uploads/sites/90/2026/06/agent-loop.webp)

* **Check.** A grounded health evaluation against the target pattern, using the same metric checks that gate the pattern in CI. No model guessing – the check is a structured query that returns a boolean per metric, with the failing evidence attached.
* **Plan.** If the repo is non-compliant, the LLM writes a fix plan *before* touching any files. The plan is a short markdown document that names the failing metrics, the proposed change for each, and the order. Writing it out is the cheapest way to catch a misread of the failing evidence – the plan is reviewed (by a deterministic structure check, not another LLM) before the fix stage starts. Fixes without plans do not run.
* **Fix.** With a plan in hand, an agent session is spawned with scoped permissions to that one repo. It uses a small set of MCP tools – `check`, `check_metric`, `fix`, `fix_metric`, `list_metrics`, `run_command`, `status` – to apply the plan, propose a change, and verify the change locally before committing.
* **Validate.** The agent opens a pull request and hands it off to the cloud – the same pre-existing cloud test gate the human PR flow uses. If cloud test goes red, a separate agent picks the PR back up and works the failure.
* **Learn.** Per-repo outcomes flow into a learning agent that aggregates patterns across the fleet. When a fix recipe shows up in three or more repos, it is promoted into the skill docs the next session reads – the system gets faster at the same kind of fix the second time it sees it.

The loop terminates only when the fleet is green or progress stalls – not on a fixed iteration count. That is deliberate: we want the system’s work to match the shape of the problem, not a hard-coded limit.

### Grounded by the Metric Engine

The single most important design decision in MARS is that the agent does not own the definition of repo health. The Metric Engine does – and it is plain C# code that any human reviewer can read, test, and ship without an LLM in the loop.

A metric is a composite check decorated with a `[Metric("id", MetricType.Local | MetricType.Cloud)]` attribute. Each evaluator implements two paired methods:

```
Task<MetricResult> EvaluateAsync(RepoContext ctx, CancellationToken ct);
Task<FixResult>    FixAsync(RepoContext ctx, MetricResult prior, CancellationToken ct);
```

`EvaluateAsync` produces a structured MetricResult – a list of pass/fail sub-checks with the actual file path, line number, and observed value attached as evidence. `FixAsync` consumes that same structure and emits a deterministic remediation proposal.

A few of the metrics in production today:

* `app-host` (Local) – the AppHost project exists, references each service, and emits the expected launch profile.
* `cosmos` (Local) – Cosmos resource is configured, partitions are non-zero, health checks are wired, EmuHub is referenced for tests.
* `e2e-tests` (Local) – an end-to-end aspire scenario test project exists, has at least one test class, and is included in the cloud test pipeline.
* `seed-data` (Local) – the Cosmos seed-data folder exists and is non-empty with the expected layout.
* `pr-validation` (Cloud) – the open pull request has a compliant description, passes branch-protection rules, and has a green build snapshot from Azure DevOps.

The Local/Cloud distinction is meaningful: **Local metrics ground themselves in file globs and AST scans of the cloned repo**, so they run offline and produce identical results across multiple runs. **Cloud metrics ground themselves in Azure DevOps snapshots** – PR state, build results, test results – so they are observations of an external system, not predictions of one. In both cases, the source of truth is something the agent reads, not something it argues about. This ensure the PR is ready-to-merge once it reaches repo-green state, passing both local metric and cloud metric checks.

This is what makes the loop safe to leave running. An LLM that hallucinates a fix still has to satisfy a deterministic gate before its commit is accepted, and the gate is the same one a reviewer would use by hand.

### Built on the Microsoft Agent Framework

Each agent is a Microsoft.Agents.AI agent, configured against a GitHubCopilotAgent backed by the GitHub Copilot SDK. The [Agent Framework](https://github.com/microsoft/agent-framework) gives us two things that turned out to matter:

* **A swappable model surface.** GitHubCopilotAgent wraps GitHub.Copilot.SDK behind the same AIAgent interface that every other backend implements. Copilot is a building block, not a hardwired dependency – when we want to switch AI Agent later, we could do that.
* **Workflows as graphs.** The remediation logic is expressed as multi-step workflows with explicit edges, not as a single mega-prompt. The four primary workflows are:

  + **`LocalFixWorkflow`** – health check -> plan -> fix -> recheck -> PR handoff, with explicit edge conditions for `green`, `regressed`, and `max_iterations`.
  + **`PrHandoffWorkflow`** – a seven-step graph: commit -> push -> risk assessment (LLM) -> PR description (LLM) -> create -> verify -> queue.
  + **`CloudFixWorkflow`** – status check -> fix -> recheck, with an early-exit edge for cloud-pending so we do not burn iterations waiting on a build.
  + **`RepoRemediationWorkflow`** – sequences LocalFix then either yields to a CI gate or runs an inline CI-wait + CloudFix.

Treating remediation as a graph means each LLM call has a tiny, well-bounded prompt; the control flow between calls lives in code, not in a sprawling system message. It is also what lets the workflow short-circuit cleanly when a metric flips green mid-loop.

### Agent roles

Inside that loop, MARS dispatches work to a small set of specialized agents, each with one job and a bounded scope:

* **Rollout Orchestrator.** The write side. Reads the target repo list, dispatches work to the agent pools, owns gating between batches, and decides when to advance, retry, or stop.
* **Local Fix Agent (3 parallel sessions).** Per-repo health evaluation, code/config fixes, and pull-request handoff.
* **Cloud Fix Agent (2 parallel sessions).** Picks up after the PR is open. Reads cloud test failures from ADO, diagnoses, and applies follow-up fixes – without re-running the local stage.
* **Learning Agent.** Watches outcomes across all repos and evolves the skill docs that future agent sessions inherit. Improvements are tagged AUTO-LEARNED and surface as proposals for human review before adoption.
* **Guardrail Agent.** Enforces scope boundaries – a session for Repo A cannot touch Repo B’s files; .NET version changes and test-count deltas are checked against safety policies before commit.
* **Evolution Agent.** Sits one level above the loop. Watches fleet health continuously, detects stalls or regressions between rollouts, and dispatches targeted fix sessions without waiting for the next scheduled pass.

The pool sizes are deliberately small – three Local Fix sessions, two Cloud Fix sessions, one Learning, one Guardrail. Steady fleet-wide convergence matters more than peak throughput on any single batch, and small pools are easier to reason about when something goes wrong. Concurrency can grow as confidence in the loop grows.

### Aspire as the control plane

What made this buildable in weeks instead of quarters is that we did not build a new orchestration platform. We used Aspire as the control plane and added what was missing. The list below is what we got for free versus what we extended.

* **Custom resource types** – `OrchestratorResource`, `CopilotAgentResource`, `CopilotSessionResource` – let agent sessions live in the AppHost graph alongside services. The parent `CopilotAgentResource` is a grouping node; child `CopilotSessionResource` instances are real `ProjectResource`s, one per pool slot. That single trick – **a parent resource that exposes its pool of children to the dashboard** – gave us per-session logs, per-session traces, and per-session start/stop without writing any custom UI.
* **Service discovery as the emulator swap.** The Playground Emulator is wired in via `WithReference` + `WithEnvironment` so the rest of the system never branches on dev-vs-prod. (Detailed below.)
* **`WithCommand()` for operator actions.** Resume Rollout, Stop Rollout, Restart Session are all declared in the AppHost as resource commands; the dashboard renders them as buttons that POST to orchestrator HTTP endpoints. No separate admin UI to build or maintain.
* **`WaitFor` and health-gated startup.** `orch.WaitFor(mcpServer)` ensures the orchestrator does not begin dispatching until the MCP server’s health endpoint reports ready. This is the same primitive we use for `WaitFor(database)` in any normal Aspire app.
* **`IDistributedApplicationEventing` as the agent bus.** Aspire’s built-in event hub support custom eventing, and we leverage that to publish `RepoProcessedEvent`, `RolloutStartedEvent`, and `RolloutFinishedEvent` between resources. Local Fix agent publishes, Cloud Fix, and Learning agents subscribe. We did not stand up a message broker.
* **`ResourceNotificationService` for live agent state.** Each agent publishes a snapshot of `CurrentRepo`, `Processed`, `Succeeded`, `Failed` after every loop tick. The dashboard reflects it without us writing any wiring beyond the snapshot call.
* **`ServiceDefaults` for one telemetry baseline.** Every project – orchestrator, agents, MCP server, API, dashboard – references the same ServiceDefaults library, so OTEL, resilience policies, and health-check shape are configured exactly once. When we tune retries or sampling, we tune them in one place.
* **Parameters for secrets.** `ADO_PAT` and `ADO_ORG` are declared as Aspire Parameter references and propagated to every agent that needs them through the same dependency-graph wiring. No .env files copied around; secrets are first-class resources.
* **Dashboard log retention raised for long rollouts.** A fleet-wide pass can run for an hour; we set `DASHBOARD__TELEMETRYLIMITS__MAXLOGCOUNT=100000` so the trace history covers a full rollout, not just the last few minutes.

The pattern that emerged was a fundamental architectural truth: **when you already have a reliable distributed-runtime story, agentic AI fits inside it as a class of resource, not as an external system you bolt on.**

### Conversations as traces – GenAI visualization in the dashboard

The dashboard view that surprised us most is the GenAI one. With `OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT=true` set on each agent process, every Copilot SDK call shows up on the trace timeline as a chat span with structured `gen_ai.system.message`, `gen_ai.user.message`, `gen_ai.tool.message`, and `gen_ai.assistant.message` events attached. We emit those events explicitly from a small TelemetryMiddleware so the conversation is captured the same way regardless of which AIAgent backend produced it.

What that means in practice: when a fix does not land on the first try, you click into the failed repo’s trace, expand the chat span, and read the entire system -> user -> tool -> assistant transcript inline next to the build logs and the metric results. There is no separate prompt-replay tool to wire up – the LLM conversation, the MCP tool calls it triggered, and the file-system effects are all on one timeline.

![GenAI dashboard trace example](https://devblogs.microsoft.com/aspire/wp-content/uploads/sites/90/2026/06/genai-dashboard-trace-example.webp)

### A playground for safe iteration

Running an agent that opens pull requests against every production repository in the fleet is not where you want to discover a bug. So we built a playground that is a peer of the real thing, and made it an Aspire resource.

The Playground Emulator replays scripted Azure DevOps API responses for a fixture set of repos: builds, PRs, test results, branch policies. The Multi-repo Sandbox is a folder of seeded clones the agents check out and modify. Both compose into the same AppHost graph as production, and the swap between real ADO and emulator ADO is done entirely through Aspire’s service-discovery mechanism:

```
if (emulator is not null)
{
  orch
    .WithReference(emulator)
    .WithEnvironment(
      "Rollout__RepoDiscovery__ServiceBaseUrl",
      emulator.GetEndpoint("http"));
}
```

The orchestrator and the agents see a single configuration key, `Rollout__RepoDiscovery__ServiceBaseUrl`, and resolve the endpoint through the standard `HttpClient` factory. There is **no if-emulator branch in production code**: the same `IDevOpsClient`, the same workflows, the same metric checks all run unchanged. We swap the resource, not the code path.

This is what lets us iterate fast and ship safely. A new fix recipe can be exercised end-to-end against the sandbox in minutes – including the cloud test leg – before it is ever pointed at a live repository. The orchestration code under test is the same code that will ship.

### Tested as a distributed application

The Playground also unlocks something we did not initially expect: **MARS guards itself.** Because the entire system – orchestrator, agent pools, MCP server, dashboard, emulator – composes into a single AppHost, we can spin the whole thing up inside an xUnit fixture using `Aspire.Hosting.Testing` and exercise it like any other distributed app.

The E2E suite is around 30 scenario classes today, each with multiple parameterized cases – over 700 individual end-to-end tests in total. They cover rollout orchestration (`RolloutScenarioE2ETests`, `RemediationDispatchE2ETests`), emulator behavior (`EmulatorAvailabilityE2ETests`, `EmulatorIsolationE2ETests`), branch and pipeline isolation, and dashboard contracts (`AspireDashboardE2ETests`). A typical test starts the AppHost in-process, posts to /rollout/new with a scenario and a repo set, lets the orchestrator dispatch through real agents talking to the emulator, then asserts on the resulting metric flips, PR creations, and event sequence. Every PR against the rollout system itself runs the suite.

The point worth highlighting for an Aspire audience: **`Aspire.Hosting.Testing` makes it cheap to test the orchestration itself, not just the individual services.** When we change the dispatch policy, the gate logic, or the agent-to-agent eventing, an aspire scenario test spec catches the regression before it ever reaches a real repo. The same primitive that makes Aspire pleasant for F5 debugging is what makes it tractable to test a system whose whole job is to coordinate other systems.

### How the system gets better over time

MARS improves through two distinct loops, and we keep them separate on purpose.

The production loop is conservative. The Learning Agent observes per-repo outcomes, aggregates fix recipes that succeed in three or more repos, and emits them as AUTO-LEARNED proposals into a `proposals/` folder. A human reviews and merges them into the skill docs the next agent session will read. We do not let the system silently rewrite its own checks – every promotion is a reviewed pull request, the same as any other change to the platform.

The harness loop is where most of the structural improvements have come from so far. When something goes wrong – a recurring agent mistake, a class of PR-comment-resolution bug, an ambiguous gate – we write a short retrospective, distill it into a falsifiable spec, and ship the fix as a structural prevention (a hook, a test, a contract change). Recent examples include the PR-comment-resolver gate that closed a four-time-recurring class of silent thread resolution bugs and the phase-coverage gap detector that prevents partial-scope deferrals. Each one started as a one-page retrospective and ended as an enforced rule the agent cannot bypass.

The takeaway: learn by shipping. Patterns become specs become code, and the code is what the next agent inherits.

## Results and developer impact

Eight months after the Phase 2 reliability work shipped, the picture is clear. Adoption nearly tripled in the final quarter, the harness ran enough validations to gate every PR, and the infra team was no longer the rate-limiting step for new onboardings.

![Aspire adoption and automation case growth, Sep 2025 - May 2026](https://devblogs.microsoft.com/aspire/wp-content/uploads/sites/90/2026/06/aspire-adoption-chart-v3.webp)

### Adoption growth

By May 2026, **50+ microservice repositories** had Aspire wired up – up from the ~15 we reported in the previous part 1 post. Growth was non-linear: most of the gain came in the last few months, once the agentic rollout pipeline began running against the live fleet. Over the same window, the count of automated test cases (aspire scenario test) grew to **700+** – each one sourced from the per-service aspire scenario test suites that AppHost composes. The two curves moved together on purpose. Each new repo MARS onboarded brought its own `Aspire.Hosting.Testing` scenarios with it; each new Aspire scenario test became a cloud test gate; each new gate raised the floor that the next rollout PR had to meet. Reliability and adoption fed each other.

### Developer time saved

For the team owning a newly-onboarded repo, the experience changed from “spend a day reading the playbook and copying boilerplate” to “review a ready-to-merge PR”. The agentic rollout produces an end-to-end pull request that compiles, builds, runs the local Aspire scenario test suite, and passes the cloud test gate before a human looks at it. We estimate **4-8 hours of manual setup eliminated per repo**, multiplied across more than three dozen newly-onboarded services. More importantly, the resulting code is consistent – the same `AppHostFixture` shape, the same health-check wiring, the same Cosmos readiness pattern, every time. Lower variance means lower long-tail maintenance.

### Aspire onboarding as the AI-readiness foundation for microservice repos

One distinction matters here: there is a **MARS system repo** (infra repo) and there are **microservice repos** (target repos being onboarded). MARS orchestrates rollout, but the long-term value lands in the microservice repos. The hardest part of AI-native transformation in those repos is usually not writing an agent prompt – it is building a reliable feedback loop the agent can trust.

Aspire onboarding gave those microservice repos that loop early. Once a repo had AppHost composition, end-to-end testing, dashboard visibility, and OTEL telemetry wired in, it already had the core harness engineering needed for agentic workflows:

* **`Aspire.Hosting.Testing` as verification in microservice repos.** Each repo can validate changes end-to-end against its own composed runtime before merging, so AI-proposed fixes are checked against real behavior rather than static guesswork.
* **The Aspire dashboard as a shared debugging surface.** When a change fails, teams can inspect service state, traces, logs, and health transitions in one place, which makes agent iterations and human review faster and more grounded.
* **OTEL as the result-validation channel.** Because the repo emits standard telemetry, both humans and automation can verify whether a fix actually moved the intended signal (for example, readiness or test outcomes), not just whether code compiled.

The practical outcome is that feature teams did not have to build harness plumbing from scratch when they began AI-native work. Aspire adoption for microservices – originally pursued for reliability and developer productivity – also created the technical foundation that made agentic rollout and ongoing AI-assisted engineering far more manageable.

## Conclusion: looking ahead

Three threads will shape the work that comes next:

* **Drive Aspire scenario test coverage up.** Partner with feature teams to make Aspire scenario test coverage a first-class, per-service signal – surface gaps from telemetry and help teams close them with the agent-assisted workflow.
* **From engaged to dedicated Aspire usage.** Move Aspire from local-dev convenience to the production-supported backbone – one AppHost graph behind local debugging, cloud test gating, and on-call diagnostics.
* **Help feature teams boost AI maturity on top of Aspire.** Help teams close the autonomy gap in their existing agent-assisted workflows, and close gaps in the underlying infra as they hit them.

We will share what we learn in follow-up posts as this work runs against the live fleet. Stay tuned.
