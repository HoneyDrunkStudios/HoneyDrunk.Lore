---
source: "https://devblogs.microsoft.com/aspire/hermetic-aspire-tests-chaos-studio"
title: "How Azure Chaos Studio ships with hermetic Aspire end-to-end tests"
author: "Brent Rusinow"
date_published: "2026-05-28"
date_clipped: "2026-10-18"
category: "DevOps & CI/CD"
source_type: "rss"
---

# How Azure Chaos Studio ships with hermetic Aspire end-to-end tests

End-to-end tests have a reputation problem.

They’re slow, they’re flaky, and the moment you wire in a real cloud dependency, your CI builds become an exercise in waiting and retrying.
Most teams I’ve talked to handle this one of two ways: they push everything down into integration tests and call it good (and lose confidence that the full system actually composes),
or they spin up shared “dev” environments and run E2E against those (and accept the cross-talk, the flake, and the “who broke staging” group chat messages as the cost of doing business).

We took a third path, and it’s paid off in a way I didn’t fully expect.

## A quick word on what we’re building

[Azure Chaos Studio](https://learn.microsoft.com/azure/chaos-studio/) lets customers proactively break their own systems in safe, controlled ways — to validate that their resilience strategies actually hold up under real failure.
Under the hood we have four independently-shipped services: a control plane, an execution plane, a fault-execution plugin host, and a data plane.
Each one is its own deployable, with its own dependencies, its own long-running-operation (LRO) semantics, and its own surface to test.

We’re heading toward GA of our V2 platform later this year, and the velocity bar has gone up — particularly as the team has leaned heavily into agent-assisted development. We needed test coverage we could actually trust before we let agents make non-trivial changes.

## The problem with our previous setup

For a long time, our end-to-end tests ran against shared environments. That’s a familiar story for anyone working on real cloud services:

* Even with stage-level serialization inside a single pipeline, separate release pipelines for each service all pointed at the same shared environment — and they ran in parallel
* Flake from real network conditions creeps in everywhere
* A regression in one service can block unrelated work
* Local repro is “spin up your own resource group and pray”

We had a solid integration test layer too. Each service has its own `WebApplicationFactory`-style suite that spins the API up in-process, runs real HTTP through it, and stubs out the data and event collaborators with mocks. Those tests are fast, deterministic, and great at catching regressions inside a single service.

But that’s exactly the limit. Integration tests of that shape can’t tell you whether the four services compose correctly — whether the LRO state machine in the control plane actually agrees with what the execution plane is polling for,
whether the auth flow holds across hops, whether a retry on one service surfaces sensibly two services downstream.
That’s the layer where most of our real bugs live, and that’s the layer we didn’t have a trustworthy story for.

## Hermetic, ephemeral, per-test environments

About a year ago I read [this writeup on hermetic, ephemeral test environments](https://carloarg02.medium.com/how-we-use-hermetic-ephemeral-test-environments-at-google-to-reduce-test-flakiness-a87be42b37aa),
and it stuck with me. The core idea: every test gets its own clean, isolated environment, brought up just for that test, with all dependencies running locally.
No shared state. No flake from neighbors. Failures are reproducible by construction.

It’s a great vision. The hard part is getting there in a real system with deep cloud dependencies.

Then a conversation with one of the .NET teams connected the dots for me: [`Aspire.Hosting.Testing`](https://aspire.dev/testing/overview/) was already most of the way there. Aspire already knows how to bring up your full service graph as a process tree. With the testing package, you can do it programmatically — from inside an xUnit fixture, on every PR, in your CI pipeline.

## What the setup looks like

The hermetic model has three pieces:

1. **The real service code**, running as the real binaries, wired up the way it is in production.
2. **Emulators or local stand-ins for external dependencies** — Cosmos and Storage both have first-class emulator support in Aspire. Key Vault doesn’t have one out of the box, but James Gould’s excellent [Azure Key Vault Emulator](https://github.com/james-gould/azure-keyvault-emulator) plugs straight into Aspire’s `AddAzureKeyVault(...).RunAsEmulator()` flow.
3. **A stub for anything that can’t be emulated.** We use [WireMock](https://wiremock.org/) for the one external dependency without a usable emulator.

In Aspire, that’s all expressed as resources on the AppHost. The same model that drives our local dev loop drives our tests:

```
var builder = DistributedApplication.CreateBuilder(args);

// Emulated dependencies
var cosmos = builder.AddAzureCosmosDB("cosmos").RunAsEmulator();
var storage = builder.AddAzureStorage("storage").RunAsEmulator();

// Key Vault emulator comes from the community package
// AzureKeyVaultEmulator.Aspire.Hosting (james-gould/azure-keyvault-emulator)
var keyVault = builder.AddAzureKeyVault("kv").RunAsEmulator();

// Stub for the one dependency we can't emulate
var authStub = builder.AddContainer("auth-stub", "wiremock/wiremock")
    .WithHttpEndpoint(targetPort: 8080, name: "http");

// Our actual services
var controlPlane = builder.AddProject<Projects.ControlPlane>("control-plane")
    .WithReference(cosmos)
    .WithReference(storage)
    .WithReference(keyVault)
    .WithReference(authStub.GetEndpoint("http"));

var executionPlane = builder.AddProject<Projects.ExecutionPlane>("execution-plane")
    .WithReference(controlPlane);
```

The test fixture brings the whole graph up, hands the test a typed `HttpClient` for each service, and tears it all down when the test finishes:

```
public class HermeticFixture : IAsyncLifetime
{
    private DistributedApplication _app = null!;

    public HttpClient ControlPlaneClient { get; private set; } = null!;

    public async Task InitializeAsync()
    {
        var appHost = await DistributedApplicationTestingBuilder
            .CreateAsync<Projects.ChaosStudio_AppHost>();

        _app = await appHost.BuildAsync();
        await _app.StartAsync();

        ControlPlaneClient = _app.CreateHttpClient("control-plane");
        await _app.ResourceNotifications
            .WaitForResourceHealthyAsync("control-plane");
    }

    public async Task DisposeAsync() => await _app.DisposeAsync();
}
```

That last `WaitForResourceHealthyAsync` call is one of those quietly important details. Tests don’t run until the service graph is actually ready, and “ready” means real health checks — not arbitrary sleeps that drift and flake.

## What we’re actually testing

We’re up to roughly **90 hermetic tests**, and they cover meaningfully more than the original “do the services start up” check. The interesting ones are the scenario tests — end-to-end fault-injection flows driven through the real service graph:

* A **zone-outage** scenario, exercising the full LRO lifecycle from request through orchestration
* An **identity-outage** scenario, validating how the data plane behaves when an identity provider goes sideways
* A **DNS-failure** scenario, covering one of the trickiest classes of resilience bugs to catch in any other way
* A **geo-replication-failure** scenario, walking the cross-region paths end to end

Each of those used to be a careful manual exercise in a shared environment. Now they run on every PR, in parallel, with no cross-talk.

## The agent payoff

Here’s the part I genuinely didn’t see coming.

When the team started leaning into agent-assisted development in earnest, this test suite quietly became our trust anchor. An agent can propose a meaningful refactor or a non-trivial feature, and we have a real signal — not just “the unit tests still pass” — that the change actually composes across services.

> Agents don’t have to be perfect. They have to be **checkable**.

That distinction is the whole game. Perfection isn’t a realistic bar for any contributor, human or otherwise — and chasing it tends to slow the team down more than it helps. Checkability is. If the system can tell you, quickly and unambiguously, whether a proposed change holds up end to end, you can move fast and stay honest about it.

Hermetic end-to-end tests turn out to be one of the highest-leverage checks you can give an agent, because:

* The feedback is **structured** — you can read the test output and see exactly what broke and where in the service graph
* The failure is **reproducible** — no “works on my machine” mystery, because there is no “my machine” state involved
* The signal is **strong** — these are real services exercising real flows, not mock-against-mock theater

This isn’t a hypothetical. The last few months of our V2 push would have been a much scarier ride without it.

## A few practical notes

If you’re considering something similar, a couple of things saved us time:

* **Start with one happy-path scenario, end to end.** Don’t try to build a full test grid on day one. One working hermetic test is a much better foundation than a long list of half-wired ones.
* **Treat your AppHost as production code.** Same resources, same wiring, same configuration shape. If your test AppHost drifts from your real one, your tests will quietly start lying to you.
* **Be honest about what you stub.** A WireMock stub for a service you can’t emulate is fine — but write down what behavior you’re assuming, and revisit it when that service evolves.
* **Run them on every PR.** Hermetic tests are only valuable as a feedback loop if they actually feed back. Ours run in Azure Pipelines on every change, and that’s where the velocity unlock really shows up.

## Closing

Aspire didn’t just make hermetic testing possible for us — it made it the path of least resistance.

If you’re building a distributed system and your end-to-end test story isn’t where you want it to be, give [`Aspire.Hosting.Testing`](https://aspire.dev/testing/overview/) a serious look. It’s quietly one of the most valuable things in the package.
