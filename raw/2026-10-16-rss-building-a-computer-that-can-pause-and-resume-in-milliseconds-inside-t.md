---
source: "https://www.digitalocean.com/blog/microvm-architecture"
title: "Building a computer that can pause and resume in milliseconds: Inside the MicroVM architecture behind Managed Agents"
author: "Braden Bassingthwaite"
date_published: "2026-10-15"
date_clipped: "2026-10-16"
category: "Software Architecture"
source_type: "rss"
date_modified: "2026-10-15"
discovered_via: "https://tldr.tech/dev/2026-10-16"
---

# Building a computer that can pause and resume in milliseconds: Inside the MicroVM architecture behind Managed Agents

An agent starts a test suite, edits a file, calls a model, and waits. Later, it resumes work with the same processes, files, and context. Sometimes it needs to fork that environment and try two approaches at once.

These workloads force a tradeoff on conventional infrastructure. Keep a machine running, and idle sessions continue to occupy resources. Destroy it, and the next interaction must rebuild the environment. Saving the filesystem helps, but it does not preserve a running interpreter, an in-memory index, or a process halfway through a task.

[DigitalOcean Managed Agents](https://www.digitalocean.com/blog/managed-agents-public-preview_), now in public preview, require a different foundation, so Harness Runtime gives each session a Firecracker microVM. The MicroVM platform underneath manages isolation, networking, storage, and checkpoint restore. Action Gateway complements that runtime with governed access to tools.

Firecracker uses KVM hardware [virtualization](https://www.digitalocean.com/resources/articles/benefits-of-virtualization), giving each guest its own kernel rather than sharing the host kernel as a container does. Network namespaces complement that VM boundary (not replace it).

The central design decision is to separate a session from the host that runs it:

* A guest keeps a stable network configuration.
* Immutable storage holds its checkpointed disk and memory.
* Host-side proxies apply network policy and can attach credentials without putting those credentials in the guest environment.

Let’s examine the MicroVM architecture design behind Managed Agents: from the cell control plane to a single memory page fault. Along the way, we will explain why our guests share an IP address, why a disk write usually stays local, and why near instant restore comes from loading less, not loading faster.

## Start with a cell instead of a global scheduler

A cell is a single self-contained, region-scoped instance of the MicroVM platform. It brings its own VPC and DigitalOcean Kubernetes cluster, managed PostgreSQL database and Spaces bucket, and pool of hypervisor hosts. Because each cell is complete on its own, a region can run many of them side by side.

Cells give us a repeatable unit of capacity and operation. We can add host capacity within a cell or add another cell. A cell-local database or routing failure does not require every other cell to share that failure. Cells still depend on shared regional and platform services. A cell limits the blast radius of a failure but does not eliminate shared dependencies. High availability was a foundational design principle rather than an afterthought. By serving as a distinct unit for capacity, lifecycle coordination, and failure isolation, each cell prevents localized disruptions from impacting the broader infrastructure. This design sustains our current operational footprint while maintaining fault boundaries as the fleet expands into additional regions.

We split each cell into two parts:

* ********The control plane********, which owns lifecycle decisions, placement, and durable metadata. It runs on [Kubernetes](https://www.digitalocean.com/products/kubernetes).
* ********The host plane********, which runs Firecracker and the services that provide guest networking, disks, and memory. It runs on hypervisor Droplets.

![Inside-a-MicroVM-cell](https://www.digitalocean.com/api/static-content/v1/images?src=https%3A%2F%2Fdoimages.nyc3.cdn.digitaloceanspaces.com%2F008ArticleImages%2FMicroVM-architecture%2FInside-a-MicroVM-cell.png&[redacted-secret-like-value])

**A cell separates request routing, lifecycle coordination, and durable state. This diagram shows selected paths, not every dependency.**

The stores have different jobs:

* PostgreSQL holds MicroVM definitions, execution state, routing and lease information, request activity, and checkpoint metadata.
* Spaces holds the large disk and memory artifacts. The activator resolves execution placement from a compact routing view without reading checkpoint payloads or running the placement scheduler for every request.

The controller coordinates creation, pause, resume, and placement. Temporal workers handle longer operations, such as template preparation and host-fleet management. On each host, microvm-d turns those decisions into Firecracker processes and local resources.

The activator bridges lifecycle management and HTTP traffic. DigitalOcean deploys its three roles separately: dataplane replicas scale with requests, lifecycle replicas handle host heartbeats and reconciliation, and the execution role runs beside the controller. We deploy them separately to independently manage each component’s scale as a traffic spike and burst of host heartbeats need different capacity. Certain services are deployed more frequently and a controller rollout should not require restarting the HTTP dataplane which would impact in-flight HTTP requests such as WebSocket or SSE.

### The database underneath the control plane

Our production cells use [DigitalOcean Managed PostgreSQL Advanced Edition](https://www.digitalocean.com/blog/introducing-mysql-postgresql-advanced). It holds the execution state the platform uses to place, route, pause, and restore MicroVMs.

That workload combines frequent small state updates with transactions that must commit related changes together, for example:

* Publishing a checkpoint records its completed state and artifact references in one transaction.
* PostgreSQL stores those decisions.
* Spaces stores the much larger disk and memory payloads.

Keeping these responsibilities separate prevents snapshot size from becoming database transaction size.

Each cell’s control plane connects to its database over a private VPC endpoint. Controller and orchestrator application traffic uses a transaction-mode [PgBouncer](https://docs.digitalocean.com/products/databases/postgresql/how-to/manage-connection-pools/) pool. Many application connections share a bounded set of database backends, so an idle client does not reserve a backend connection. Session-dependent operations, such as schema migrations, use a separate direct connection.

Advanced Edition also addresses database operations that would otherwise complicate the control plane. Its connection pooler routes reconnecting clients to the new primary after a failover, without waiting on DNS changes. These operations do not remove the need to handle interrupted transactions. Query and connection-pool observability provides visibility into slow queries and connection pressure as execution concurrency grows.

DigitalOcean uses a managed database for these responsibilities, rather than building database failover and capacity management into the MicroVM scheduler. The database remains cell-local, while the managed service handles the database infrastructure underneath.

## Follow a request: from Edge to the guest

Inbound and outbound traffic solve different problems: inbound traffic must find a particular execution (possibly waking it first), while outbound traffic must respect that execution’s network policy.

For HTTP ingress, the path is:

![From-the-edge-to-the-guest](https://www.digitalocean.com/api/static-content/v1/images?src=https%3A%2F%2Fdoimages.nyc3.cdn.digitaloceanspaces.com%2F008ArticleImages%2FMicroVM-architecture%2FFrom-the-edge-to-the-guest.png&[redacted-secret-like-value])

**Running executions use the hot path. The wake path coordinates lifecycle changes only when policy permits.**

The DigitalOcean Edge provides the platform’s edge routing layer. The MicroVM controller publishes routes that select a cell’s activator. For execution ingress URLs, those routes configure authentication and ownership checks. They also set the internal routing headers that carry the execution identity and destination port, replacing any values the client sent. A client cannot steer a request to another execution by forging those headers.

The activator then chooses between two paths:

* ********On the hot path********, the execution is running, its readiness flag is set, and its lease remains valid. The activator resolves the host from a PostgreSQL-backed execution state and forwards the request without asking the controller to make a new placement decision.
* ********On the wake path********, the activator asks the controller to create or resume execution when the execution policy permits. The request waits for the routing state to become eligible, subject to a deadline. Note that a control-plane readiness flag is not, by itself, proof that every application endpoint is healthy.

Host heartbeats keep this routing view up to date, and execution leases put a time limit on it. When a host stops reporting, its addresses stop being eligible instead of lingering as stale routes. Lifecycle workers coordinate their reconciliation shards through Kubernetes Leases.

The last proxy hop is local to the host. `microvm-proxyd` runs Envoy with platform bootstrap and certificate support. `microvm-d` supplies listeners, routes, and upstreams through Envoy’s dynamic configuration API, xDS, over a local Unix socket.

The activator connects to host Envoy over mutual TLS. Envoy selects the execution and port, removes internal routing headers, and forwards HTTP to the guest. This is not one unbroken TLS connection from the client to the application: each proxy hop has an explicit role and trust boundary.

No single component needs to own all three concerns:

* DigitalOcean’s Edge handles edge routing and access.
* The activator handles execution availability.
* Local Envoy handles the final host-specific route.

## Every guest has the same IP address

A checkpoint preserves the guest kernel’s view of the network along with application memory, including interface configuration and cached neighbor entries.

Giving every restored guest a new interface address would require changing that preserved state. And forking a checkpoint would make the problem worse, because every fork starts with the same configuration in memory.

So instead, we make the guest network deliberately repeatable:

| Guest-visible property | Value |
| --- | --- |
| Guest IPv4 address | 192.168.240.2 |
| Default gateway | 192.168.240.1 |
| Guest MAC address | 02:00:00:00:00:02 |
| Gateway MAC address | 02:00:00:00:00:01 |

These addresses do not collide, because each execution has a separate host-side Linux network namespace. Each namespace contains a TAP interface for the guest and a veth connection to the host network. The guest-facing interfaces do not share one Layer 2 network.

Outside that boundary, the platform allocates a host-facing execution address. Namespace NAT translates between that address and the fixed guest address.

![Network-Anatomy-of-a-MicroVM](https://www.digitalocean.com/api/static-content/v1/images?src=https%3A%2F%2Fdoimages.nyc3.cdn.digitaloceanspaces.com%2F008ArticleImages%2FMicroVM-architecture%2FNetwork-Anatomy-of-a-MicroVM.png&[redacted-secret-like-value])

**Different host-facing identities, identical guest networks. Namespace isolation makes repeated IP and MAC addresses safe.**

Only the host-facing side changes between guests; inside the VM, all guests see the same addresses.

The fixed gateway MAC is a small detail with a large effect. From inside the VM, the default gateway is the host-side TAP interface in the guest’s namespace, and the gateway MAC is that interface’s hardware address. Suppose a guest checkpoints after resolving its gateway through ARP. If restore creates a TAP device with a random MAC, the guest’s cached ARP entry points to an address that no longer exists. Even replies to incoming connections can stall until neighbor discovery repairs the entry.

Keeping the gateway MAC fixed ensures that the saved entry remains valid in the new namespace. We recreate the network the guest expects, instead of waiting for the guest to discover that it changed.

This design does not preserve arbitrary connections to the outside world. A remote TCP peer does not roll back when we restore a checkpoint, and applications may need to reconnect after restore (especially after a fork or host change).

Stable addresses solve local network reconstruction, not connectivity to the outside world.

## We put network policy outside the code it governs

Agents need network access to fetch packages, call model APIs, and connect to tools. However, those same agents execute code that no developer has reviewed line by line, so that access has to be governed.

A proxy environment variable is a useful configuration, but it is not a security boundary. Code can ignore `HTTP_PROXY`, open its own socket, or bring another HTTP client.

When a MicroVM’s forward-proxy policy and the host forward path are enabled, the platform installs namespace-level nftables rules. These rules block new guest-forwarded connections that would bypass the proxy. Replies to inbound connections remain possible, and local DNS, metadata, and proxy services remain reachable.

Envoy then applies the configured destination allowlist. Rules can name exact domains, wildcard domains, or exact IP addresses. Unmatched explicit-proxy requests receive a denial. These rules answer one question: can this execution reach this destination? They do not inspect what the application does once it gets there.

There are two ways for traffic to reach the forward proxy:

* ********Explicit proxying********: Compatible clients send HTTP requests or HTTPS `CONNECT` requests to the local proxy.
* ********Transparent proxying********: When enabled on the host, namespace rules redirect guest TCP traffic on ports 80 and 443 to Envoy. This covers clients that ignore proxy environment variables.

Ordinary allowed HTTPS connections can remain opaque tunnels. Transparent TLS routing uses the requested server name for domain rules. We do not need to decrypt every allowed connection to enforce a hostname policy.

Credential injection is a narrower, opt-in case where decryption is necessary.

### Let an agent use a credential without handing it the credential

An environment variable containing a production API key is easy to use. It is also easy for a process to print, copy into a file, or capture in a memory snapshot.

For supported HTTP integrations, we move credential use to the host proxy. A credential binding identifies an exact destination hostname, a header, an authorization handle, and (optionally) a permitted path prefix.

The host redeems the authorization handle with our internal secrets manager over mTLS. It supplies platform context, including the team and region that owns it. The resulting value goes to Envoy through its secret-discovery mechanism, SDS. The proxy-injection path does not intentionally deliver that value to guest metadata or the workload environment.

For an active HTTPS credential binding, the flow is:

![Two-TLS-sessions-One-binding](https://www.digitalocean.com/api/static-content/v1/images?src=https%3A%2F%2Fdoimages.nyc3.cdn.digitaloceanspaces.com%2F008ArticleImages%2FMicroVM-architecture%2FTwo-TLS-sessions-One-binding.png&[redacted-secret-like-value])

**Two TLS sessions, with one controlled credential-injection point. The guest receives a public trust root—not the redeemed API key or a CA signing key.**

Envoy replaces the configured credential header rather than trusting a value supplied by guest code. It checks the HTTP authority and any configured path restriction. Its new upstream TLS connection validates the origin certificate against the expected hostname.

The distinction is important: the guest gets permission to make an authenticated request through the proxy. It does not need a copy of the underlying API key.

This reduces one source of credential exposure, but does not make every operation on an allowed API safe. Tool permissions and approval workflows remain separate concerns, including the controls provided by Action Gateway. Proxy injection is also distinct from explicit secret-environment delivery, which deliberately makes a secret available inside the guest.

### Why the MicroVM CA is part of checkpoint design

To inject a header into HTTPS, Envoy must terminate the guest’s TLS connection. That only works if the guest trusts a certificate authority the platform controls.

The MicroVM interception CA uses a stable fleet root and per-cell issuing intermediates. It is separate from the PKI used for service-to-service mTLS. The guest receives a public trust anchor, not a CA signing key.

Guest init installs the supplied trust material before workload processes start, including for guests without credential bindings. The platform preserves the image’s existing roots and configures supported runtimes to use the combined trust bundle.

Why install trust before startup rather than after restore? TLS libraries can cache trust roots in process memory. Rewriting a certificate file cannot prove that an already-running process will reload it. Checkpoints therefore record the interception root fingerprint. Creating a credential-enabled MicroVM from a checkpoint checks compatibility with the active root.

This interception is a deliberate tradeoff, with these consequences:

* The host proxy sees plaintext for intercepted requests.
* Clients that pin certificates or ship their own trust configuration may need adjustment.
* Per-cell intermediates keep issuance separate, but their certificates all validate under one fleet root, so cells are not cryptographic trust boundaries from each other.
* End-to-end TLS is replaced, not preserved. The interception CA is an explicit part of the runtime’s trust model.

### Private connectivity without changing the guest

The same network boundary supports customer-VPC egress. The controller validates the requested VPC’s ownership, region, and optional subnet. A private NAT Gateway provides the path from the cell VPC into the selected customer network.

The guest still sees its fixed gateway. For domain-based forward-proxy traffic, Envoy opens upstream sockets inside the execution namespace. Those connections follow the execution’s selected egress path, including VPC mode.

This gives a sandbox a route to private services without putting a customer-VPC address on its virtual NIC. The guest can open connections into the VPC; the VPC cannot open connections to the guest.

Connecting to a private API should not require granting every process unrestricted access to that network or copying an API key into the filesystem. Network reachability, destination policy, and credentials remain separate controls.

## A remote disk with local writes

Networking works across hosts because the guest never owns its host-facing identity. Storage has to solve the same problem: a checkpoint has to be usable on a host that has never seen the guest’s disk.

Downloading a complete disk image before every execution would put image size directly on the startup path. Sharing one writable disk could cause executions to interfere with each other.

Our disk has two parts:

1. An immutable base in content-addressed storage(********CAS********).
2. A private, host-local writable overlay for each execution.

`microvm-ublk` exposes this combination as a Linux block device through ublk, the kernel’s userspace block-device interface. Firecracker attaches that device as a guest drive. Inside the guest, applications see an ordinary filesystem. Spaces objects and chunk indexes exist only on the host side.

![Shared-base-Private-writes](https://www.digitalocean.com/api/static-content/v1/images?src=https%3A%2F%2Fdoimages.nyc3.cdn.digitaloceanspaces.com%2F008ArticleImages%2FMicroVM-architecture%2FShared-base-Private-writes.png&[redacted-secret-like-value])

**Writes stay in a private local overlay. Reads select the newest owning layer, with cached content-addressed chunks beneath it.**

The overlay is a sparse delta file with one bitmap bit per 4 KiB block. A set bit means the delta owns that block. Reads use the newest overlay that owns the block, then fall back to the immutable base.

Writes update the local delta and bitmap. They do not require an object-store write for every guest write. A partial-block write may first read the parent block to preserve bytes the write does not replace.

Even writing zeros requires care. A hole in a sparse file reads as zero, but an unset bitmap bit means “read the parent.” Zeroing a block must therefore set its bit, even when the implementation stores those zeros as a hole. Otherwise, old parent data would reappear.

### The index is the disk’s recipe

We use casync-style `.caibx` index files and the Go `desync` implementation. An index describes the ordered chunks that reconstruct a byte stream. Each chunk has a content-derived identifier. The index maps a disk offset to the chunk containing those bytes.

Chunk boundaries are content-defined, not one object per 4 KiB block. The default chunking target is 512 KiB, with 256 KiB and 768 KiB bounds. Remote chunks use compression. The larger unit amortizes object-store requests and allows identical content to be reused within the shared store.

A cache miss fetches and decompresses a chunk. Later reads can use the host-local uncompressed cache. Multiple executions from the same template can reuse cached immutable content while retaining separate writable overlays.

This moves the startup requirement from “download the disk” to “make the disk addressable.” The guest fetches data as it needs it.

It also creates explicit durability boundaries. Local write acknowledgement can precede host-disk durability because overlays synchronize periodically. Sealing explicitly synchronizes the delta and bitmap. Recent local writes are not automatically remote checkpoints. Remote checkpoint completion means the captured artifacts and their references have been published.

## A checkpoint is more than a disk snapshot

A disk snapshot can preserve files, but not the process that was using them.

For a resumable VM checkpoint, we capture three types of state:

| State | What it preserves | How the platform represents it |
| --- | --- | --- |
| Disk | Filesystem contents at capture | CAS chunks and a disk index |
| Memory | Guest RAM, including kernel and process state | CAS chunks and a memory index |
| Device and vCPU state | Virtual hardware state and execution position | Firecracker snapshot data in the checkpoint layer metadata |

The checkpoint record is a small index that points to these artifacts rather than containing them.

Capture and publication run on different clocks: capture needs a consistent instant in the VM’s lifecycle, while publication needs time to move large artifacts to remote storage.

For a checkpoint of an active execution, the sequence is:

1. Run an optional pre-checkpoint hook while the guest can still respond.
2. Pause the VM for capture.
3. Flush and seal the disk overlay, and capture memory and virtual-device state.
4. Switch future disk writes to a fresh overlay and resume the active execution.
5. Publish the captured disk, memory, and device artifacts.
6. Mark the checkpoint complete (a PostgreSQL commit) after all required publication stages succeed.

An execution that was already paused stays paused. A per-execution capture lock prevents a concurrent resume from changing state halfway through capture.

Sealing makes captured bytes independent of later writes. For disk, the sealed overlay becomes a read-only parent beneath a fresh writable overlay. Memory capture produces an independent local artifact for publication. Uploads can then continue without holding an active guest paused for the entire remote transfer.

Disk publication combines the sealed overlays into a self-contained index. It reuses unchanged base chunks and reconstructs dirty regions. Because chunk boundaries are content-defined, a small change in a block can shift boundaries and force rechunking over a larger range. The upload is a set of new chunks, not a list of changed blocks.

Lifecycle capture currently snapshots the full memory image. Content addressing deduplicates chunks that match previous checkpoints, but capture itself does not track which pages changed.

Finally, the controller commits the completed checkpoint references in PostgreSQL. Restore and checkpoint-derived creation require a complete checkpoint. Completion is the metadata publication barrier, not a distributed transaction spanning PostgreSQL and object storage.

Forking then becomes a matter of referring to immutable checkpoint content and giving the new execution its own writable state. A full remote disk copy for each branch is not necessary.

There are limits to what this preserves. The platform pauses the VM wherever it happens to be. An application that needs to reach a clean stopping point first has to do so in the pre-checkpoint hook. External databases, remote sockets, and completed API side effects remain outside the snapshot.

## Restore memory without reading all of it

Lazy disk access is only half the problem. A VM with several GiB of memory could still spend its startup budget downloading RAM.

Linux `userfaultfd` (********UFFD********), lets us defer that work. It allows a userspace process to handle missing pages in another process’s registered memory ranges.

![Saved-state-Memory-on-demand](https://www.digitalocean.com/api/static-content/v1/images?src=https%3A%2F%2Fdoimages.nyc3.cdn.digitaloceanspaces.com%2F008ArticleImages%2FMicroVM-architecture%2FSaved-state-Memory-on-demand.png&[redacted-secret-like-value])

**Restore makes saved state addressable without loading all of it. The fault loop brings missing memory pages into the running guest, on demand.**

On restore, `microvm-uffd` prepares a memory source and a Unix socket. Firecracker loads its device snapshot with the VM still paused and hands the userfaultfd and memory-region mappings to the memory service. Only then does the host resume the vCPUs, so the first page fault always finds a handler waiting.

When execution touches a missing page:

1. The kernel reports a fault through userfaultfd and blocks the faulting thread.
2. `microvm-uffd` translates the faulting address into an offset in the memory snapshot.
3. `microvm-uffd` reads the bytes from its memory source. For CAS-backed memory, that means resolving the checkpoint layer and chunk index, checking local caches, and fetching from Spaces on a miss. For a local-file source, it reads the mapped range directly.
4. `microvm-uffd` installs the bytes with `UFFDIO_COPY`, allowing the blocked thread to continue.

Known-zero ranges can use `UFFDIO_ZEROPAGE` rather than fetching and copying stored zeros.

A restored VM can execute without first populating its entire memory image. A checkpoint taken after application initialization can also avoid repeating kernel boot, package initialization, and application startup.

A cold page can still stall execution. We manage that cost with shared decompressed-chunk caches, host-local storage caches, coalesced chunk fetches, and read-ahead. Fault-around copying installs nearby pages together, reducing repeated trips through the fault handler.

These optimizations trade extra work now for fewer faults later. Fetching too little creates repeated stalls, while fetching too much consumes bandwidth and memory for pages the guest may never touch. Cache state, workload locality, and concurrent restores all affect the result.

We defer loading rather than eliminate it. Demand paging loads memory as execution needs it. Caching and read-ahead reduce stalls without making the entire snapshot a prerequisite for progress.

### How the warm path fits inside 200 milliseconds

On the warm-template path, we bring a MicroVM from an execution request to serving traffic in under 200 ms at p50 in our internal testing. There is no single operation that makes this possible on its own. Each stage stays small because we prepare reusable resources early and defer bulk data loading.

The path starts with an existing template checkpoint, available host capacity, a prepared network endpoint, and warm storage caches. Image import, initial application boot, and a complete snapshot download are not on this path.

| Stage | Warm-path threshold | Work on the request path |
| --- | --- | --- |
| Request resolution and wake admission | ≤10 ms | Resolve execution policy and state, admit the wake, and dispatch to the controller. |
| Placement and host dispatch | ≤10 ms | Select an eligible host from its capacity and health reports, then contact microvm-d. |
| Host resource setup | ≤20 ms combined | Claim and bind a prepared network endpoint, create the sparse overlay and ublk device, and set up the Firecracker process and jail. |
| Firecracker snapshot restore | ≤40 ms | Load device and vCPU state, connect the prepared UFFD memory backend, and resume guest execution. |
| Route activation and first byte | ≤20 ms | Make the execution route eligible, install the local Envoy route, and forward traffic to the guest. |

The five stages account for roughly 100 ms of the 200 ms envelope; the rest covers memory-backend preparation, coordination, and the working-set page and block reads a first request needs. The per-stage numbers are budgets we hold each stage to, not measured percentiles, so they are not meant to be summed into the p50. Only the end-to-end figure is measured.

#### Place the execution, not a new host

The controller chooses from hosts that already report their available execution capacity, CPU, memory, and disk resources. It filters out stale or incompatible hosts and dispatches to an eligible `microvm-d`. Provisioning a Droplet or waiting for a fleet-scale operation is not part of the 10 ms placement step.

The activator handles request resolution separately. It does not repeat image preparation or ask a global scheduler to reconstruct the session. Placement hands a compact execution specification and checkpoint references to an already available host.

#### Build the network before the request arrives

Creating a namespace is only the start of network setup. A usable endpoint also needs a veth pair, TAP device, addresses, routes, neighbor entries, and NAT rules. Each of those is a separate kernel call, and building the whole set on every request would put many of them directly in the latency path.

Instead, each host maintains a pool of prepared, unused network endpoints. Background workers reserve addresses and create namespaces, veth pairs, TAP devices, fixed gateway configuration, and baseline routing. They publish an endpoint to the pool only after preparation succeeds.

Creating an execution claims one of those endpoints through a host-local SQLite transaction. The host then applies execution-specific differences, such as forward-proxy lockdown or a customer-VPC egress route. For the default network shape without lockdown, binding adds no further kernel operations.

A claim also wakes the refill workers. They replace consumed capacity in the background rather than making the requesting execution wait for it.

Endpoints are built fresh and used once. When an execution releases one, the host destroys it, and the address stays reserved until teardown succeeds. No execution inherits another tenant’s conntrack or neighbor state.

#### Create a disk handle, not a disk copy

Disk setup has two distinct steps. First, `microvm-ublk` creates the execution’s sparse delta file and block-ownership bitmap over an immutable base. Second, it creates and starts a Linux ublk device backed by that overlay.

The kernel device is new; not a reused writable disk from a previous execution. Likewise, it is not a preattached device waiting in the network pool. What we reuse is the immutable image backend and cached content—there is no full disk copy or filesystem reconstruction.

The host exposes the new block device inside the Firecracker jail under the stable drive name rootfs. The restored device model can therefore use the same path even when Linux assigns a different ublk device number.

Network claim and binding, overlay and device creation, and process setup share the 20 ms host-setup threshold. We keep them small by removing bulk provisioning.

#### Restore the machine instead of booting it

The Firecracker snapshot contains the saved device model and vCPU state. These bytes are distinct from both the disk contents and the Linux ublk device. The host stages that snapshot and prepares the UFFD handler before loading the VM.

Firecracker starts as a new process, loads the saved state while paused, and connects to the memory backend. A separate resume operation then releases the vCPUs. Within the 40 ms restore threshold, the guest continues from its saved execution state rather than repeating kernel and application initialization.

The host preserves the dependency order: network, disk, memory backend, then Firecracker. We do not need to run those setup steps simultaneously to remove full-disk and full-memory transfers from startup.

#### Make the first request useful

Configured execution-init and post-restore hooks complete before the execution becomes eligible for traffic. Their execution contributes to the same end-to-end window.

The final 20 ms stage connects execution readiness to the local Envoy route and the first forwarded byte. UFFD serves missing memory pages as the guest runs. ublk serves disk blocks as the guest reads them. Caches, coalesced fetches, and read-ahead reduce repeated waits for the same content.

Those page and block reads still add to first-request latency, and any prefetch configured ahead of them adds more. This path avoids waiting on the full snapshot.

The 200 ms figure assumes the warm state is in place. An empty endpoint pool or cold caches adds work outside that envelope, and a first-time image import or a model-generated agent response is a separate operation with its own cost. The path we measure is a ready template becoming a traffic-serving MicroVM.

That is the whole warm path: a network built in advance, a new writable disk over shared content, and a restored machine that loads only the pages it touches.

## A foundation for sandboxes and agents

The architecture works because the pieces reinforce each other:

* A cell gives us a bounded unit of capacity and lifecycle management. DigitalOcean Edge and the activator route requests without making the client track host placement. Network namespaces let a guest keep the configuration captured in its memory.
* Content-addressed storage makes checkpointed disk and memory independent of the original host. Local overlays keep ordinary disk writes off the object-store path. UFFD and ublk let a restored guest use that state without downloading all of it first.
* Host-local Envoy keeps destination policy and supported credential injection outside guest code. VPC egress connects the same execution model to private services. These controls make networking a platform capability rather than a collection of secrets and firewall rules inside each sandbox.

Together, they expose useful primitives: isolated execution, checkpoint, restore, fork, governed egress, and private connectivity. Managed Agents builds session and tool workflows on top of those primitives.

The result is not just a smaller VM: it is a computer whose useful lifetime can exceed the lifetime of the host process running it. An agent can work, wait, and branch without requiring developers to reconstruct its environment at every transition.
