---
source: "https://techcommunity.microsoft.com/blog/appsonazureblog/introducing-brewlet-manage-golden-images-at-platform-speed/4576767"
title: "Introducing Brewlet: Manage Golden Images at Platform Speed"
author: "Bruno Borges"
date_published: "2026-11-25"
date_clipped: "2026-11-26"
category: "Azure & Cloud"
source_type: "rss"
---

# Introducing Brewlet: Manage Golden Images at Platform Speed

In October 2026, the PHP project released security updates for critical vulnerabilities that could allow unauthenticated remote code execution. For teams running PHP in Kubernetes, applying a runtime fix can mean more than updating PHP: it can mean rebuilding application images, waiting for application pipelines and approvals, and coordinating deployments across services, even when the application code itself has not changed. That delivery gap matters.

AI is accelerating software development, but also vulnerability discovery and exploitation, increasing pressure on organizations to respond quickly. But asking every application team to rebuild and redeploy at once is not always practical. How can platform teams deliver a runtime update without making unrelated application releases a prerequisite?

Today, we’re introducing [Brewlet](https://brewlet.sh), an experimental open-source project that treats approved runtimes as Kubernetes infrastructure. Application teams publish their application code and launch instructions as an OCI image. Platform teams approve golden runtime images and offer them to selected Kubernetes node pools. Compatible workloads can then use an updated runtime, with a security patch, without rebuilding their application image.

## Golden images and independent runtime updates solve different problems

A golden image can help remove unnecessary components, attack surface and the amount of software teams need to assess. But it still bundles a language interpreter, system library or certificate bundle. When these components live in the final artifact of an application image, their security patches are still tied to the application’s build and release process.

Brewlet explores a different boundary: separate the application workload from its execution environment so they can be managed on distinct lifecycles. Of course, not every runtime should be moved out of every application image. The right boundary depends on compatibility, operations and who should own the update. But the goal here is to make the separation available when it helps.

## The application runtime shifts back to infrastructure.

With Brewlet, an application image contains the application and its dependencies under /app, along with an explicit launch.json describing how to start it. It does not bundle the selected runtime. A platform team approves a digest-pinned golden runtime image, including its non-root identity, and decides which node pools offer it.

At container creation, Brewlet composes the application with the approved runtime available on the node. Applications remain ordinary Kubernetes workloads using OCI artifacts, containerd and runc. Sharing runtime files does not mean sharing a process, heap, writable filesystem or resource limits between applications.

Ultimately, the platform team can curate the runtime environment for its workloads, optionally with a set of common platform-owned dependencies, while application teams keep ownership of application code and application-specific dependencies.

## How Brewlet fits into Kubernetes

1. **Approve a runtime.** The platform team defines a RuntimeImage that points to an approved runtime image by digest and declares its non-root identity.
2. **Offer it on a pool.** A NodeProfile determines which nodes provide the runtime and how it is provisioned.
3. **Package the application.** Developers use their existing build tools, then package the application files and launch metadata into an OCI image with the Brewlet CLI.
4. **Select the runtime.** The Kubernetes workload uses runtimeClassName: brewlet and selects a runtime ID for each managed container. Admission validates the selection and placement; the node provisioner installs the approved runtime, and the Brewlet shim prepares the container for runc.

The following illustrative Deployment selects a platform-approved php-8.4 runtime for a separately packaged application:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: orders
  annotations:
    brewlet.sh/restart-on-rotation: "true"
spec:
  replicas: 2
  selector:
    matchLabels:
      app: orders
  template:
    metadata:
      labels:
        app: orders
      annotations:
        runtime-image.brewlet.sh/app: php-8.4
    spec:
      runtimeClassName: brewlet
      containers:
        - name: app
          image: registry.example.com/apps/orders:v1
```

This example assumes the platform has approved and offered php-8.4, and the application has been packaged for that runtime. The restart annotation is on the Deployment metadata. For Brewlet to restart opted-in workloads during rotation, the operator’s rotation-restart feature must also be enabled.

## Change the runtime, not the application artifact

The [Brewlet PHP guide](https://brewlet.sh/docs/php/) demonstrates moving a PHP workload from PHP 8.4.26 to 8.4.27 by changing the approved runtime image while keeping the application digest the same. This example shows that a PHP security release can be qualified and distributed as a platform runtime update rather than requiring an application rebuild for every service.

It is important to note that a runtime rotation is not an in-place patch to a running process. Existing containers continue using the generation they started with, while new containers use the new generation, and workloads that have opted-in to restart-on-rotation be rolled by their Kubernetes controller when the operator feature is enabled. Workload rollout strategies still apply; paused, partitioned or otherwise constrained workloads can remain on the older generation.

The [Java demonstration](https://brewlet.sh/docs/demo/) illustrates another kind of runtime change: rotating a JDK also changes the certificate roots in that JDK’s bundled trust store, while preserving the application artifact. It makes visible that a runtime can contain security-relevant material beyond the language executable.

## What runtime separation does, and does not, solve

Brewlet can help platform teams govern and roll out common components supplied by the approved runtime image. It does not update vulnerable libraries packaged under /app, such as application-specific dependencies; those still need an application update. Nor does it eliminate shared risk: if many workloads use the same vulnerable runtime, they are still exposed until they are running a fixed generation. Brewlet changes how that runtime can be distributed and governed, not the need to qualify it, replace workloads and verify the outcome.

Kubernetes [image volumes](https://kubernetes.io/docs/concepts/storage/volumes/#image) can also separate an application from runtime files and may be the simpler choice for teams whose existing policies and tooling already cover their needs. Brewlet’s additional value is an integrated model for runtime approval, node-pool provisioning, start-time authorization, generation visibility and opt-in rotation.

## Try Brewlet

Brewlet is an MIT-licensed open-source project. The current releases are experimental and intended for evaluation. Start with the [local Kubernetes tutorial](https://brewlet.sh/docs/local-kubernetes/), which deploys a Python application and demonstrates a runtime rotation in kind. Explore the [Java demonstration](https://brewlet.sh/docs/demo/), the [language guides](https://brewlet.sh/docs/language-recipes/), and [when to consider Brewlet](https://brewlet.sh/docs/choosing-brewlet/) for a fuller description of the operational tradeoffs.

Find Brewlet on [GitHub](https://github.com/microsoft/brewlet), and use the [issue tracker](https://github.com/microsoft/brewlet/issues) to report problems or share feedback. We’d like to hear how runtime updates flow through your organization today, and whether separating runtime delivery from application releases would make those updates easier to govern.
