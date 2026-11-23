---
source: "https://techcommunity.microsoft.com/blog/appsonazureblog/separating-compute-in-azure-functions-building-for-scale-efficiency-and-reliabil/4573977"
title: "Separating Compute in Azure Functions: Building for Scale, efficiency, and reliability."
author: "Fabio Cavalcante"
date_published: "2026-11-17"
date_clipped: "2026-11-22"
category: "Azure & Cloud"
source_type: "rss"
---

# Separating Compute in Azure Functions: Building for Scale, efficiency, and reliability.

As customers bring new workloads to Azure Functions, we continue to evolve the runtime to support them securely and at scale. Compute Separation is part of that work. We're revisiting how the host and language workers are deployed and managed to improve efficiency and reliability, and to enable new capabilities while preserving the Functions programming model.

When a Functions app needs more capacity, the work you want to scale is its language worker and customer code. In the co-located, out-of-process hosting model, adding that capacity also adds another Functions host, even if the existing host capacity could coordinate more workers. The language worker is already a separate process, but the platform's unit of scale is still the instance that contains both host and worker.

Compute Separation changes that unit of scale. The host and the workers run on separately managed compute, allowing the platform to add workers without creating a host for each one. For customers, that opens up more control over the environment running their code, while the platform retains responsibility for the Functions host.

Getting there means revisiting assumptions that were convenient when both components lived in the same instance: access to application files, who starts and replaces a process, and even which side opens the connection. One of the most consequential constraints was networking. Existing workers connect to the host, but the platform's networking model requires the remote connection to run in the other direction.

This post follows the engineering decisions behind that change, the cold-start and reliability requirements that shaped it, and how we're building and proving the architecture in small end-to-end steps.

> *Preview scope: Everything in this article describes a preview implementation that is still in progress. It is not a released product contract or a migration recommendation. We expect the architecture, behavior, and scope to change as we implement features and validate performance and reliability.*

## Why change the host-worker boundary?

The host and the language worker do different jobs. The host connects the app to the platform's control model and implements the runtime-side contract used for worker assignment, readiness, scaling, and reliability actions. It also understands the Functions execution model: it loads trigger and binding extensions, discovers functions, manages listeners, and coordinates invocations. The language worker understands how to load and execute your code in its language runtime.

Process isolation already separates these responsibilities into different processes. Compute Separation also separates their compute and lifecycle.

Keeping those components together made several things straightforward. The host could start a child process, communicate over localhost, and treat process exit as a direct signal that its worker had stopped. Configuration and application files were available in the same deployment environment.

Those conveniences also created dependencies. Scaling the worker repeated the host's resource overhead. A language-specific image carried the host and its dependencies as well as the language runtime. Host maintenance and application image maintenance were coupled.

Consider an application that needs native libraries or a particular operating-system dependency. A customer-provided worker image should let you package that environment without also packaging and maintaining the Functions host. You'd own your application, language runtime, dependencies, and image maintenance. The platform would own the host.

[Custom worker containers](https://techcommunity.microsoft.com/blog/AppsonAzureBlog/run-chromium-and-native-libraries-on-azure-functions-flex-consumption-with-worke/4572085) are the first customer-facing scenario we're using Compute Separation to enable. The architecture has broader value, though. A host fix shouldn't inherently require rebuilding every language-specific application image. Adding customer execution capacity shouldn't require repeating the full host. Independent release and scaling decisions become possible, subject to protocol compatibility and the capacity of each component.

There is a platform-efficiency motivation too. Keeping combined host-and-worker environments warm fragments capacity by language, version, and instance size. A language-independent runtime gives us more options for reusing warm runtime capacity without preparing every combined environment. That is an architectural opportunity, not a measured cold-start improvement or a customer pricing claim.

The goal is to preserve the Functions programming model while changing how its components are operated. Functions still execute in language workers, and trigger and binding behavior still needs to hold across the new boundary.

## Challenge: the worker couldn't initiate the remote connection

In the co-located model, the host listens for a connection and the language worker connects to it. Moving the host to another compute instance might suggest replacing a localhost address with a remote endpoint.

The platform's network security model rules out that approach. Once separated, worker pods run customer code, so they aren't allowed to open outbound connections to runtime pods. Any connection between the two has to be initiated by the runtime.

One option was to change the workers' connection behavior. That would have had a significant compatibility impact across existing worker implementations. It would also have introduced a worker contract tied to the networking needs of this particular hosting model. We wanted to keep those deployment details out of the language workers.

We introduced a platform-owned **WorkerProxy** between the two sides. The runtime opens an authenticated TLS FunctionRpc stream to WorkerProxy. The language worker connects to WorkerProxy over the worker pod's local network, retaining the worker-initiated connection pattern. WorkerProxy bridges the two connections.

*Figure 1. The host initiates the remote connection; the worker connects locally to WorkerProxy. The scope is one application with replicas of one language worker, not a shared host across applications or a fixed worker-to-host ratio.*

Each worker pod contains WorkerProxy and a separate container for the language worker and customer code. WorkerProxy provides the transport bridge and worker-side lifecycle contract. It doesn't become a second Functions host, start the customer process, or take ownership of platform placement and pod deletion.

For workers that negotiate HTTP streaming, there is also a separate data path: the host forwards HTTP through WorkerProxy's assigned HTTPS origin to the worker's local HTTP endpoint. Requests still pass through the host.

On the runtime side, the preview uses a dedicated `Functions.Host` executable with a client-backed worker composition. The ordinary co-located host retains its server-backed path. We can develop the new topology without making every existing app switch to it.

This preserves an important part of worker compatibility, but doesn't eliminate all protocol work. Remote startup also needs configuration, metadata, and extension delivery. Keeping the connection pattern familiar is different from promising that every existing worker version supports the complete new hosting model.

### Preview limitations and why they exist

The networking constraint affects more than the main connection. The FunctionRpc stream isn't the only conversation between a worker and the host. Some extensions add their own communication paths, where code in the worker calls back into components running in the host. In the co-located model, those calls never leave the instance. In the new topology, they become worker-initiated calls to a remote host, which is the direction the networking constraints rule out.

WorkerProxy bridges the main stream, but these additional paths are specific to each extension and carry their own protocols and expectations. Supporting them requires changes in both the host and the extensions. Some of that work was more complex than the initial preview's scope and timeline allowed, so the first preview has extension limitations.

Service Bus and Durable Functions are the most visible examples. Service Bus message settlement relies on one of these paths: when a function explicitly settles a message, for example to complete or dead-letter it, the worker asks the host-side extension to perform that operation. Durable Functions has a similar dependency. Operations such as starting an orchestration or raising an event go from the worker to APIs that the Durable Functions extension exposes in the host. Neither extension is supported in the first preview, and host and extension work to address these limitations is in progress.

## Challenge: protecting cold-start performance

Cold-start performance was the key performance requirement shaping the design. Separating compute adds networking and coordination to activation. Optimizing steady-state invocation forwarding would not be enough if starting an application became slower.

Activation spans networking configuration, specialization of a host instance for the application, initialization of the application container, and linking the worker to the host. Treating all of that as one serial sequence would make each step's latency part of the wait for useful execution.

We designed the activation process to overlap independent work while keeping its dependencies explicit. An assignment can arrive before the language worker starts. Other steps really do need to wait: the host must validate initialization before accepting a link, and invocation dispatch must wait for application setup. The requirement is to parallelize preparation without treating partial progress as readiness.

The host-side startup path illustrates those distinctions:

1. **Assignment configures the worker side.** WorkerProxy accepts application and function-group identity, limits, and the HTTP origin when needed. Assignment acceptance doesn't prove that the customer process has initialized.
2. **The runtime establishes and validates the link.** It connects to WorkerProxy and validates worker initialization, application proof, and delivered host configuration before accepting the link.
3. **Application preparation continues.** Advertised extensions are prepared before the initialized signal is published. Metadata acquisition and ScriptHost construction and setup follow.
4. **The channel becomes eligible for dispatch.** The current application-host setup and channel-readiness checks determine when the worker can receive invocations.

A successful Link response is therefore an intermediate checkpoint, not permission to send traffic. Platform status publication is another checkpoint, not proof that the entire serving path has converged.

*Figure 2. Assignment, link acceptance, initialization, and dispatch readiness mean different things. The lifecycle also separates planned retirement from unexpected connection loss.*

Smaller worker images and more reusable warm runtime capacity give us opportunities to improve startup. Neither establishes the result on its own. Cold-start measurements need to cover the full activation path, including scheduling, image availability, networking, specialization, and linking.

### Application setup without a shared filesystem

Activation also exposed a dependency inside the host: it previously had local access to the customer's deployment. A remote host still needs configuration, function metadata, and binding extensions before it can run the app.

For host configuration, the compute host advertises the `HostConfiguration=1` capability during initialization. A compatible worker returns a typed envelope containing the configuration, and WorkerProxy relays it. The host validates the delivery rather than asking the proxy to interpret the customer's `host.json`. Malformed configuration fails admission instead of silently becoming defaults.

The selected configuration source stays stable across later worker links and child-host restarts. Adding execution capacity must not silently reconfigure an app because another worker connected. Consistency between workers' configuration and function definitions still needs to be validated.

Extensions make the boundary more interesting. Customer function code runs in the worker, but host-side binding extensions still run in the host. The preview implementation can receive an advertised extension archive over the connection, validate and extract it, and prepare those assemblies before extension discovery and listener startup.

The host can therefore start without a shared customer deployment mount, but it still has application-specific dependencies. Moving files across the connection doesn't add the extension-specific communication paths described earlier or qualify every binding. Those behaviors also have to work across the new boundary.

## Challenge: preserving reliability without owning the process

The co-located host could observe and manage its worker as a child process. With independent compute, the platform owns process creation and replacement. Existing host logic has to participate in that lifecycle through explicit contracts while preserving recovery behavior.

A lost connection, for example, is no longer equivalent to a child process exiting. It tells one component that communication stopped; it doesn't prove what the other component is doing. Admission, draining, and replacement need coordinated decisions rather than assumptions based on local process state.

That starts with knowing where work can run. The scheduler selects a ready, non-draining worker in the function's group, using a round-robin preference. For HTTP, a full worker is skipped; if all eligible workers are full, admission waits for capacity. A FIFO gate orders invocation attempts, not execution or completion.

Listeners need to follow that capacity too. The preview gates supported pull-based listeners on workers for their function group, so the runtime doesn't keep acquiring events with no corresponding worker available. Push-based triggers and shared listeners need different handling. Preserving trigger semantics requires more than a generic worker-selection policy.

### When is an invocation actually finished?

Planned scale-in requires a precise answer. The host closes new admission, withdraws the worker from usable capacity, and drains accepted work before terminating or unlinking the channel. The platform then remains responsible for physically removing the pod.

Accepted work includes invocations still buffered or converting input. HTTP adds another case: a worker can send a successful gRPC invocation response while the HTTP response body is still being forwarded to the caller. Removing the worker at that point can truncate a response even though the invocation protocol reported success.

The implementation tracks completion through dispatch and, for proxied HTTP, through response forwarding. Worker retirement waits for that lifecycle. This is a useful example of how a familiar operation, stopping a worker, acquires a more explicit contract once its pieces run independently.

Unexpected runtime loss follows a separate path. In the current implementation, WorkerProxy enters a sticky removal-requested state and rejects new work, leaving removal and replacement to the platform. It doesn't transparently attach another runtime or replay invocations.

Separate compute boundaries also change the failure scenarios we need to test. A worker failure need not require restarting the host, but a runtime failure can affect several workers for the same application. Independent scaling doesn't eliminate shared dependencies.

## Challenge: carrying platform services across the boundary

The host-worker connection now crosses a network and compute boundary. Authenticating the caller, associating a worker with the right application, and handling credentials become explicit parts of the design. The preview implements TLS, runtime caller tokens, and application-key proof during initialization.

Those mechanisms are not a claim that the security contract is finished. The implementation documents limitations in certificate identity validation, shared-key authority, and replay protection. Provisioning, network policy, revocation, and cross-application containment remain part of qualification.

Managed identity illustrates how platform integration also affects startup. Application code can need an identity token before worker initialization completes. If identity access depended on completed initialization, startup could wait on itself.

The preview includes an opt-in Token Service proxy. WorkerProxy carries the worker's local identity request over the existing runtime-initiated stream, and the host forwards it to the host-side Token Service. That path can operate before the customer's worker stream starts. The application gets access to the operation it needs without moving the upstream Token Service credential into the worker-side forwarding contract.

Diagnostics and metering need the same attention to ownership. A failure now involves a runtime, a worker pod, and a connection session; logs need to let us distinguish them while preserving the customer logging path. One runtime can dispatch to several workers, so execution measurements need to identify the worker that actually accepted an invocation.

The preview records that attribution at dispatch and tracks completion against the selected worker. Binding and extension work can happen before admission, though, so the worker's execution window doesn't cover the whole invocation pipeline. Those records are part of the accounting work, not a final billing definition.

## Proving the change one end-to-end outcome at a time

The initial checkpoint deliberately used one worker and one HTTP request. Even that small scenario crossed platform assignment, the host's outbound link, worker metadata, readiness publication, and both the HTTP and FunctionRpc paths. It gave us a bounded way to exercise the new connections and contracts together.

From there, the work expands along several related dimensions: starting an app without a shared deployment mount, executing correctly as worker capacity changes, integrating with platform services, and qualifying the customer experience. These are parallel workstreams with shared contracts, not sequential releases.

*Figure 3. An explanatory grouping of overlapping engineering workstreams, with dependencies and validation feedback. This is not an availability timeline.*

Each step needs an observable outcome. Can another worker join without restarting the application host? Can an early identity request complete during startup? Can a worker drain while its HTTP response is still streaming? Can a non-HTTP trigger preserve its binding and execution behavior?

These questions cross repository and component boundaries. The host provides components and contracts, while placement, networking, frontend routing, image delivery, language-worker support, and rollout involve other parts of the platform. A merged host change isn't evidence that the whole service path is ready.

Small end-to-end scenarios let us test those interactions before broadening coverage. They also let us revise a contract after learning from it, rather than treating a successful connection as proof that startup, execution, and recovery are complete.

## What remains to prove

The next evidence has to cover the full application workload. Cold-start and scale-out measurements need tail latency and image-cache misses, as well as the activation path under normal conditions. Steady-state tests need to quantify network and proxy overhead. Capacity tests need to establish how many workers a runtime can safely coordinate.

Compatibility is another qualification task. We need full fidelity with the existing model to ensure applications continue to run with no modifications.

## What this makes possible

The payoff we're working toward is concrete: customers can own the environment running their code without maintaining the Functions host, and the platform can scale and service those components independently. Custom containers are the first scenario, but the value extends beyond packaging.

Separate compute gives the host and workers their own CPU and memory resources. A worker that misbehaves is less likely to take resources away from the host or affect the rest of the app, though work assigned to that worker can still fail. We can also allocate capacity to each role independently, rather than adding host overhead whenever we add workers. That gives us room to use resources more efficiently.

This separation also gives us a foundation for more advanced deployment options and more flexible scaling. Customer containers can be smaller because they no longer need to include the host and its dependencies. These are opportunities, not capabilities or performance results we can claim for this preview.

We've explored this architecture in internal prototypes. It's exciting to see it making its way into the service and opening up new scenarios for customers, starting with custom worker containers. We also plan to extend this model transparently to existing apps, so current customers can benefit without changing how they build and run their apps. We still have work to do to implement the features and validate the performance, but the direction is clear. Separating the host from the worker gives every Functions app a more reliable and efficient foundation, and opens the door to capabilities we couldn't build with both roles sharing the same compute.
