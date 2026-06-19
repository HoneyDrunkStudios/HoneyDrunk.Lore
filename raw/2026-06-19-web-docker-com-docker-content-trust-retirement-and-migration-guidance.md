---
source: "https://www.docker.com/blog/docker-content-trust-retirement-and-migration-guidance/"
title: "Docker Content Trust: Retirement and Migration Guidance"
author: "unknown"
date_published: "2026-06-18"
date_clipped: "2026-06-19"
category: "Security & Ethical Hacking"
source_type: "web"
---
# Docker Content Trust: Retirement and Migration Guidance

*TLDR: Docker Content Trust (DCT) and the Notary v1 service at notary.docker.io are being fully retired (first announced in **July of 2025**). This blog explains what is changing, who is affected, and how to move to modern alternatives. *

Ten years ago, Docker Content Trust (DCT) gave the container ecosystem one of its first ways to verify the integrity and publisher of an image, built on The Update Framework and the Notary v1 project. The upstream Notary v1 codebase is no longer maintained, more modern signing tools have become the standard, and today a very small number (fewer than 0.05%) of Docker Hub pulls rely on DCT.

Last year we began retiring DCT for Docker Official Images, and now we’re completing that work by fully retiring DCT and the Notary v1 service at notary.docker.io. This post covers what’s changing, who’s affected (for most people, nothing), and the modern alternatives that are available to users.

**Why are we retiring Docker Content Trust (DCT)?**

DCT relies on the upstream Notary v1 server, the original TUF-based implementation that was first released in 2015, and the project is no longer maintained. In the years since, the ecosystem has standardized on OCI-native signing tools such as Sigstore/Cosign and the Notary Project’s Notation, that store signatures alongside the image in any compliant registry, with no separate trust infrastructure to run. The broader ecosystem has been retiring this approach–Microsoft deprecated DCT support in Azure Container Registry some time ago, and Harbor deprecated Notary v1 support too.

Retiring Notary v1 lets us put our investment behind other modern, standards-based tools (described below) that developers are already adopting, and behind making secure defaults first-class citizens on Docker Hub.

**Who is affected by this change?**

**Who is affected by this change?**

DCT was opt-in, and normal image pulls (`docker pull`

) would not touch the Notary service, so if you’ve never deliberately turned it on, nothing about your workflow changes. You can stop reading here.

The change matters if you configured DCT for use, which usually shows up in one of a few ways:

- You have
`DOCKER_CONTENT_TRUST=1`

set in your environment, shell profile, CI pipeline, or Dockerfile. - Your scripts or automation use
`docker trust sign`

,`docker trust inspect`

, or`docker trust revoke`

. - Your Kubernetes admission controllers or deployment policies check for DCT signatures.
- You publish images to Docker Hub with DCT signing enabled.

If you have never set `DOCKER_CONTENT_TRUST`

and do not use `docker trust`

commands, this change does not affect you.

**Pathway to retirement: timeline**

We’re winding DCT down in stages rather than all at once. The brownouts are brief, scheduled outages, these are dry runs that flush out any pipeline still leaning on the service while there’s time to fix it. Writes go dark before reads, so signing breaks before verification and publishers can get the earliest heads-up.

|
Date |
What happens |
|
Jul 14, 2026 |
4-hour write brownout |
|
Jul 15, 2026 |
4-hour write brownout |
|
Aug 10, 2026 |
4-hour read brownout |
|
Aug 12, 2026 |
4-hour read brownout |
|
Dec 8, 2026 |
Full shutdown |

Windows run ~4 hours and begin at 8AM Pacific Time.

Note this only touches DCT trust operations; ordinary docker pull and docker push operations will keep working through these windows.

**What to do if you are affected: migration guide and alternatives**

If any of the cases above describe your setup, here’s how to move off DCT cleanly. The ecosystem has settled on a handful of strong, widely-adopted tools, so this is as much a menu as a manual. The steps run from the quickest unblock to the most complete setup; pick the leading technology that fits your workflow, and go as far down the list as your situation calls for.

**Ensuring image pulls succeed**

If your only goal is to ensure that image pulls keep working past the shutdown date, disable DCT. This is the fastest path to unblocking your workflows, but it removes tag-level verification.

```
# Remove from your current shell session
unset DOCKER_CONTENT_TRUST
# Or explicitly disable it
export DOCKER_CONTENT_TRUST=0
```

Search your environment for anywhere this variable might be set, including shell profiles, CI/CD configuration, Compose files, and K8s manifests. Once DCT is disabled, all pulls continue to work normally.

**Ensuring pulls are repeatable**

Tags on image registries can change when an image is updated. Pulling by digest guarantees that you get the exact image content you expect, regardless of whether a tag has been moved or overwritten. Digests are immutable.

```
# Find the digest of an image you have pulled
docker pull busybox:latest
docker images --digests busybox
# REPOSITORY TAG DIGEST IMAGE ID
# busybox latest sha256:f85340bf... abc123def456
# Pull by digest
docker pull busybox@sha256:f85340bf...
```

Use digests in dockerfiles for reproducible builds, and in Kubernetes manifests or Compose files to ensure predictable deployments.

Digest pinning verifies content integrity (you get exactly what you asked for), but it does not by itself prove publisher identity. For that, you need cryptographic signatures, which is where Sigstore/Cosign and Notation come in.

**Proving publisher identity**

Two mature, actively maintained signing projects have replaced DCT’s signing capabilities in Hub. Both store signatures alongside the image in OCI-compliant registries.

**Option A: Sigstore / Cosign**

Cosign is part of the Sigstore project and supports identity-based signing using short-lived certificates tied to an OIDC identity. It stores signatures as OCI artifacts in the same registry, alongside the image.

- Sigstore quickstart: https://docs.sigstore.dev/quickstart/quickstart-cosign/
- Cosign on GitHub: https://github.com/sigstore/cosign

**Option B: Notation**

Notation is the CLI for the Notary Project. It uses a certificate-based PKI model and stores signatures as OCI reference artifacts.

- Notation quickstart: https://notaryproject.dev/docs/quickstart/
- Notation on GitHub: https://github.com/notaryproject/notation

**Enforcing verification in production**

Signing images is only half the story. To get full security benefits, you need to enforce that only signed images can be deployed.

**Kyverno (works with Cosign)**

Kyverno can verify Cosign signatures before pulling into a cluster. See the documentation for details.** **

**Ratify + Gatekeeper (works with Notation)**

Ratify can verify Notation signatures before admitting pods. See the Ratify quickstart for setup instructions.

**Use Docker Hardened Images as a built-in replacement**

If you currently rely on DCT to verify base images from Docker Hub, switching to Docker Hardened Images (DHI) is a free and secure path forward. Every DHI comes with cryptographic signatures, provenance attestations, and SBOMs already built in.

This means the integrity checks you relied on with DCT are guaranteed, and then some. DHI images are minimal by design and continuously rebuilt when new CVEs appear. You are not just replacing a verification mechanism, you are getting a more secure base image to begin with.

- Read more here: https://docs.docker.com/dhi/
- Or view the free catalog at dhi.io

**Need help?**

A couple of things worth knowing as you plan your move.

If you are a Docker Hub *publisher* currently signing images with DCT, Docker cannot provide replacement signatures on your behalf. You will need to adopt Cosign or Notation to sign your own images.

If you are a *consumer* of third-party images that were signed with DCT, contact those publishers directly to determine whether they plan to adopt modern signing.

For questions or issues related to the shutdown, or if you want to work more directly with us on a migration plan, contact Docker support.
