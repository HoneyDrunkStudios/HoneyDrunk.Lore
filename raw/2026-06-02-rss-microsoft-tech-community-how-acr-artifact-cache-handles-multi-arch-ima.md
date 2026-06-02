---
source: "https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744"
title: "How ACR Artifact Cache Handles Multi-Arch Images: What Gets Cached and When Webhooks Fire"
author: "Microsoft Tech Community"
date_published: "2026-04-25"
date_clipped: "2026-06-02"
category: "Azure & Cloud"
source_type: "rss"
---

# How ACR Artifact Cache Handles Multi-Arch Images: What Gets Cached and When Webhooks Fire

Source: https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744

# How ACR Artifact Cache Handles Multi-Arch Images: What Gets Cached and When Webhooks Fire

Open Side Menu

[Skip to content](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744#main-content)[![Image 1: Brand Logo](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/themes/customTheme1/favicon-1730836271365.png?time=1730836274203)](https://techcommunity.microsoft.com/)

[Tech Community](https://techcommunity.microsoft.com/)[Community Hubs](https://techcommunity.microsoft.com/Directory)

[Products](https://techcommunity.microsoft.com/)

[Topics](https://techcommunity.microsoft.com/)

[Blogs](https://techcommunity.microsoft.com/Blogs)

[Events](https://techcommunity.microsoft.com/Events)

[Skills Hub](https://techcommunity.microsoft.com/category/skills-hub)

[Community](https://techcommunity.microsoft.com/)

[Register](https://techcommunity.microsoft.com/t5/s/gxcuf89792/auth/oidcss/sso_login_redirect/provider/default?referer=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fappsonazureblog%2Fhow-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho%2F4514744)[Sign In](https://techcommunity.microsoft.com/t5/s/gxcuf89792/auth/oidcss/sso_login_redirect/provider/default?referer=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fappsonazureblog%2Fhow-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho%2F4514744)

1.   [Microsoft Community Hub](https://techcommunity.microsoft.com/)

3.   [Communities](https://techcommunity.microsoft.com/category/communities)[Products](https://techcommunity.microsoft.com/category/products-services)  

5.   [Azure](https://techcommunity.microsoft.com/category/azure)

7.   [Apps on Azure Blog](https://techcommunity.microsoft.com/category/azure/blog/appsonazureblog)

[Report](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744#)

## Apps on Azure Blog

## Blog Post

![Image 2](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTE0NzQ0LW0xSkJ0Mg?revision=1&image-dimensions=2000x2000&constrain-image=true)

Apps on Azure Blog 

9 MIN READ

# How ACR Artifact Cache Handles Multi-Arch Images: What Gets Cached and When Webhooks Fire

[![Image 3: johnsonshi_msft's avatar](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/dS0xMDE0Mjg2LW5uejRibA?image-coordinates=0%2C0%2C463%2C463&image-dimensions=50x50)](https://techcommunity.microsoft.com/users/johnsonshi_msft/1014286)

[johnsonshi_msft](https://techcommunity.microsoft.com/users/johnsonshi_msft/1014286)

![Image 4: Icon for Microsoft rank](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/cmstNC05WEo0blc?image-dimensions=100x16&constrain-image=true)Microsoft

Apr 25, 2026

## Clarifying Azure Container Registry's Artifact Cache behavior for multi-architecture container images, and how to use Webhooks to detect when an image is fully cached locally and no longer being pulled through from upstream.

_By [Johnson Shi](https://www.linkedin.com/in/johnsonshi/) (Senior Product Manager)_, _[Toddy Mladenov](https://www.linkedin.com/in/toddysm/) (Principal PM Manager)_, _[Luis Dieguez](https://www.linkedin.com/in/luis-dieguez-12388b4a/) (Principal SWE Manager),_ _[Akash Singhal](https://www.linkedin.com/in/akash-singhal-941441155/) (Senior Software Engineer_), _Kiran Challa (Senior Software Engineer), [Ren Shao](https://www.linkedin.com/in/renshao/) (Senior Software Engineer)_

## Introduction

Three of the most common questions we hear from teams using Azure Container Registry (ACR) [Artifact Cache](https://learn.microsoft.com/azure/container-registry/artifact-cache-overview) and [Webhooks](https://learn.microsoft.com/azure/container-registry/container-registry-webhook) are:

1.   **"When I pull a multi-architecture (multi-arch) image through Artifact Cache, what exactly gets cached?"**— Does ACR pull all architectures, or just the one I requested?
2.   **"How do I know when an image has been cached using Webhooks?"** — Especially for multi-arch images, how can I tell when the image is fully stored locally in a cache rule's downstream ACR and pulls are no longer being proxied (pulled through) to upstream?
3.   **"When do storage charges begin applying for cached images?"** — How can I determine when an image has been stored locally and when storage charges for the cached image begin incurring?

In this post, we clarify the exact behavior and provide a step-by-step walkthrough so you can verify it in your own environment using ACR artifact cache and webhooks.

## Key Takeaways

*   When you pull a multi-arch image through Artifact Cache, ACR proxies the pull to upstream immediately. In the background, ACR **asynchronously****copies** the**manifest list artifact**(referencing all platforms) and**only the platform manifest artifact that was pulled** into local storage. Other architecture manifests referenced by the manifest list artifact are not copied until someone pulls them.
*   **ACR push webhooks fire when the async copy completes for the artifact cache feature**— signaling that the image is now stored locally in a cache rule's downstream ACR and subsequent pulls will no longer be proxied to upstream. For a single-platform pull of a multi-arch image, ACR fires**3 push webhook events**: two for the manifest list (one tagged, one untagged) and one for the platform-specific manifest.
*   **No ACR push webhooks fire for blob/layer copies** — only a single push webhook event is triggered per digest and tag that is asynchronously copied and locally stored.

## Background

### What Is Artifact Cache?

[ACR Artifact Cache](https://learn.microsoft.com/azure/container-registry/artifact-cache-overview)is a pull-through caching feature in Azure Container Registry. You define a cache rule that maps an upstream repository (such as Docker Hub or Microsoft Artifact Registry) to a local ACR repository.

Here's how it works when an image is not yet cached:

1.   A client pulls from ACR (e.g.,docker pull myacr.azurecr.io/nginx:latest).
2.   ACR does**not**redirect the client to the upstream registry. Instead, ACR**pulls the image through**on the client's behalf — ACR **proxies** the request to upstream and streams the content back to the client. The client only ever talks to the downstream ACR in a cache rule.
3.   At the same time, ACR kicks off an**asynchronous job** to copy the image into the downstream ACR's own storage.
4.   Until that async copy completes, subsequent pulls of the same image are still pulled through to upstream.
5.   Once the async copy finishes, the image is stored locally in the downstream ACR. From that point on, all pulls are served directly from the downstream ACR with no upstream traffic.

This is an important distinction: Artifact Cache is a**pull-through proxy**, not a redirect. Clients always interact with your ACR endpoint, never directly with upstream. The caching happens asynchronously in the background after the first pull.

For more details, see the[Artifact Cache documentation](https://learn.microsoft.com/azure/container-registry/artifact-cache-overview).

### Multi-Arch Images

Multi-architecture images use a**[manifest list](https://docs.docker.com/reference/specifications/image/manifest-list/)**(also called an **OCI image index**) that references multiple platform-specific manifests. In this experiment, we used Docker manifest list media types (application/vnd.docker.distribution.manifest.list.v2+json). OCI image indexes use equivalent but distinct media types — the caching behavior is expected to be the same, but our observations are specific to Docker media types.

For example, the ["mcr.microsoft.com/cbl-mariner/base/core:2.0" multi-arch image](https://mcr.microsoft.com/en-us/artifact/mar/cbl-mariner/base/core/tags) from Microsoft Artifact Registry is a manifest list that references two platform-specific images, each with their own digest:

| Architecture | Digest |
| --- | --- |
| linux/amd64 | sha256:fdf30afe7338... |
| linux/arm64 | sha256:c981b0618917... |

When a Docker client or containerd pulls this image, it resolves the manifest list and downloads only the manifest matching its platform.

### The Behavior in Question

When Artifact Cache handles a multi-arch pull, there are three possible outcomes:

*   **(A)**Cache only the single platform manifest for the client's architecture?
*   **(B)**Cache the manifest list plus the client's architecture only?
*   **(C)**Cache the manifest list plus all architectures?

And how many ACR push webhook events does each produce? The answer is**(B)**, and we demonstrate an experiment to detect when the images are cached using webhooks.

## Walkthrough: Observing Cache Behavior with Webhooks

To illustrate this behavior, we walk through a step-by-step example using ACR webhooks to capture every push event that ACR fires during a cache population. You can follow along in your own environment.

### Prerequisites

*   An ACR registry (any SKU — Basic, Standard, or Premium)
*   Azure CLI (az) installed and logged in
*   Docker Desktop (with Docker CLI) or Podman Desktop (with Podman CLI) installed

### Step 1: Set Up a Webhook Endpoint

You need an HTTP endpoint that can receive and display webhook payloads.[webhook.site](https://webhook.site/)provides a free temporary endpoint — visit the site and copy your unique URL.

### Step 2: Create a Scoped Webhook

Create an ACR push webhook that only fires for push events on the specific repository you'll use for testing. When tags and digests are copied asynchronously into a downstream ACR during artifact cache operations, they are classified as push events on the downstream ACR. As such, the push webhook should fire for these operations, making push webhooks a useful way to observe and validate cache-driven push behavior in the registry. Scoping the webhook to push events also eliminates noise from other registry activity during this experiment.

```bash
az acr webhook create \
  --registry <your-registry> \
  --name cachepushtest \
  --uri <your-webhook-site-url> \
  --actions push \
  --scope "test/cbl-mariner/base/core:*" \
  --status enabled
```

### Step 3: Verify the Webhook

Send a ping to confirm the webhook endpoint is reachable:

```bash
az acr webhook ping \
  --registry <your-registry> \
  --name cachepushtest
```

Check your webhook.site page — you should see a POST request with"action": "ping".

![Image 5](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTE0NzQ0LUpEcVNybw?image-dimensions=999x284&revision=1)
### Step 4: Create a Cache Rule

Map the upstream Microsoft Artifact Registry repository to a local test namespace. Microsoft Artifact Registry doesn't require credentials, which simplifies setup.

```bash
az acr cache create \
  --registry <your-registry> \
  --name cblmariner-cache-test \
  --source-repo mcr.microsoft.com/cbl-mariner/base/core \
  --target-repo test/cbl-mariner/base/core
```

### Step 5: Pull Through Cache

Log in to your registry and pull the multi-arch image. Use--platform to make the test reproducible.

**Note:** When the image already exists in the downstream ACR's cache, pull requests result in cache hits served directly from local storage, bypassing the initial asynchronous copy process and generating no new webhook events. To force webhook events to fire again, delete the cached image tags and digests from the downstream ACR. This clears the cache and triggers the asynchronous copy behavior on the next pull.

```bash
az acr login --name <your-registry>

docker pull --platform linux/amd64 \
  <your-registry>.azurecr.io/test/cbl-mariner/base/core:2.0
```

### Step 6: Observe the Webhook Events

Wait for webhook delivery to complete, then inspect the events:

```bash
az acr webhook list-events \
  --registry <your-registry> \
  --name cachepushtest
```

You can also check [webhook.site](https://webhook.site/) to see the raw payloads.

## Results

Excluding the initial webhook test ping, you will observe**3 ACR webhook events** when running "docker pull --platform linux/amd64 <your-registry>.azurecr.io/test/cbl-mariner/base/core:2.0" that is configured with a cache rule against the upstream ["mcr.microsoft.com/cbl-mariner/base/core:2.0" multi-arch image](https://mcr.microsoft.com/en-us/artifact/mar/cbl-mariner/base/core/tags) from Microsoft Artifact Registry:

### Event 1: Manifest List (Tagged)

```json
{
  "action": "push",
  "target": {
    "mediaType": "application/vnd.docker.distribution.manifest.list.v2+json",
    "digest": "sha256:c833841d2dcfd3081d2ee807050d19368854f70d9b6faef027463e2c6f45ee41",
    "repository": "test/cbl-mariner/base/core",
    "tag": "2.0",
    "size": 860
  }
}
```
![Image 6](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTE0NzQ0LUlzVVZ1RA?image-dimensions=999x396&revision=1)
### Event 2: Manifest List (Untagged)

```bash
{
  "action": "push",
  "target": {
    "mediaType": "application/vnd.docker.distribution.manifest.list.v2+json",
    "digest": "sha256:c833841d2dcfd3081d2ee807050d19368854f70d9b6faef027463e2c6f45ee41",
    "repository": "test/cbl-mariner/base/core",
    "size": 860
  }
}
```
![Image 7](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTE0NzQ0LUhVTHlBZQ?image-dimensions=999x386&revision=1)
Same digest as Event 1, but without a tag. ACR emitted two push webhook events for the same manifest-list digest: one tagged, one untagged.

### Event 3: Platform Manifest (amd64)

```bash
{
  "action": "push",
  "target": {
    "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
    "digest": "sha256:fdf30afe733831d3af0db95aa8e6870fb1094b2c4f531caaaa06e37481b95253",
    "repository": "test/cbl-mariner/base/core",
    "size": 736
  }
}
```
![Image 8](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTE0NzQ0LVN5SGFFbA?image-dimensions=999x385&revision=1)
This is the linux/amd64 platform-specific manifest.

### What Was Not Observed

*   **No webhook for linux/arm64** (sha256:c981b061...). Even though the manifest list references it, the arm64 platform manifest was not cached because the docker pull operation specifically pulled only the linux/amd64 image using the --platform flag.
*   **No ACR push webhooks fire for blob/layer copies** — only a single push webhook event is triggered per digest and tag that is asynchronously copied and locally stored.

### Cross-Referencing with ACR Manifests

We confirmed the webhook results by listing what ACR actually stored:

```bash
az acr manifest list-metadata \
  --registry <your-registry> \
  --name test/cbl-mariner/base/core \
  -o table
```

| Digest | MediaType | Architecture |
| --- | --- | --- |
| sha256:c833841d... | manifest.list.v2+json | _(multi-arch index)_ |
| sha256:fdf30afe... | manifest.v2+json | amd64 |

Only two manifests were stored: the manifest list and the amd64 manifest. The manifest list itself still references both linux/amd64 and linux/arm64, but the arm64 manifest was not downloaded.

## Findings

### Artifact Cache Multi-Arch Behavior: Caches Manifest List + Requested Architecture Only

ACR Artifact Cache performs a**partial closure copy**:

1.   **The full manifest list is cached.**This preserves the multi-arch index so that clients requesting any platform will get a valid manifest list response. The manifest list still references all platforms.
2.   **Only the requested platform manifest is cached.**If you pull linux/amd64, only the amd64 manifest and its layers are copied into ACR storage. The arm64 manifest remains uncached — if someone pulls it, it will be pulled through from upstream and a new async copy job will start.
3.   **Subsequent architecture pulls trigger additional caching.**If a different client later pulls--platform linux/arm64, ACR will pull through from upstream for that architecture and kick off another async copy. Once complete, additional webhook events will fire for the arm64 manifest.

### Webhook Behavior Summary

| Event | MediaType | Tagged | Count |
| --- | --- | --- | --- |
| Manifest list push | manifest.list.v2+json | Yes (2.0) | 1 |
| Manifest list push | manifest.list.v2+json | No | 1 |
| Platform manifest push | manifest.v2+json | No | 1 per architecture pulled |

**Total for a single-platform pull: 3 ACR push webhook events.**

### Using Webhooks to Know When an Image Is Locally Cached

When a client pulls an uncached image, ACR pulls the content through from upstream and serves it immediately — but the image is not yet stored in ACR. An asynchronous copy job runs in the background to store the image locally. Until that job completes, subsequent pulls of the same image continue to be pulled through to upstream.

The webhook push event fires when the async copy completes and the image is actually stored in ACR. After this point, pulls are served directly from ACR with no upstream traffic. This is what the webhook signals — not that a pull happened, but that**the image is now locally cached in your registry**.

**The webhook also signals when the image is stored locally and when storage charges for the cached image begin to apply.**

There are two levels of completion to consider:

*   **Tag locally cached:** A push event with mediaType of application/vnd.docker.distribution.manifest.list.v2+json and a non-null tag field means the manifest list is stored in ACR. The tag now resolves locally. Storage charges are now incurred for the manifest list artifact.
*   **Specific platform locally cached:** A push event with mediaType of application/vnd.docker.distribution.manifest.v2+json means a platform-specific manifest (and its layers) are stored locally. Pulls for that architecture are now served entirely from ACR. Storage charges are now incurred for the platform-specific artifact

To determine which platform a manifest push corresponds to, pre-compute the per-platform digests from the upstream manifest list:

```bash
# Get the upstream manifest list with per-platform digests
docker manifest inspect mcr.microsoft.com/cbl-mariner/base/core:2.0
```

Take note of the architecture-to-digest mapping (e.g., linux/amd64 → sha256:fdf30afe...). In your webhook handler, match incoming digest values against this mapping to identify which architecture was cached.

**Note:** Webhook events may not arrive in strict order, and retries can produce duplicate deliveries. Deduplicate events by id or digest in your handler, and don't assume ordering between the manifest-list and platform-manifest events.

## Cleanup

After running the experiment, clean up the test resources:

```bash
az acr webhook delete --registry <your-registry> --name cachepushtest
az acr cache delete --registry <your-registry> --name cblmariner-cache-test --yes
az acr repository delete --name <your-registry> --repository test/cbl-mariner/base/core --yes
```

## Summary

| Question | Answer |
| --- | --- |
| What gets cached for multi-arch images? | The full manifest list + only the requested platform manifest |
| Are other architectures cached? | No — only on demand when someone pulls them |
| How many webhooks fire? | 3 for a single-platform pull (2 for manifest list, 1 for platform manifest) |
| Do blob/layer uploads fire webhooks? | No — only manifest pushes |
| How do I know when an image is locally cached? | Listen for push webhooks — they fire when the async copy completes and pulls no longer go to upstream |

If you have further questions about Artifact Cache or webhook behavior, reach out to us on the[Azure Container Registry GitHub repository](https://github.com/Azure/acr).

Published Apr 25, 2026

Version 1.0

[azure container registry](https://techcommunity.microsoft.com/tag/azure%20container%20registry?nodeId=board%3AAppsonAzureBlog)

Like 0

Comment

[![Image 9: johnsonshi_msft's avatar](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/dS0xMDE0Mjg2LW5uejRibA?image-coordinates=0%2C0%2C463%2C463&image-dimensions=80x80)](https://techcommunity.microsoft.com/users/johnsonshi_msft/1014286)

[johnsonshi_msft](https://techcommunity.microsoft.com/users/johnsonshi_msft/1014286)

![Image 10: Icon for Microsoft rank](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/cmstNC05WEo0blc?image-dimensions=100x16&constrain-image=true)Microsoft

Joined March 31, 2021

Send Message

[View Profile](https://techcommunity.microsoft.com/users/johnsonshi_msft/1014286)

[](https://techcommunity.microsoft.com/category/azure/blog/appsonazureblog)

[Apps on Azure Blog](https://techcommunity.microsoft.com/category/azure/blog/appsonazureblog)

Follow this blog board to get notified when there's new activity

Enjoying the article? Sign in to share your thoughts.

Sign in

### Share this page

*   [](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fappsonazureblog%2Fhow-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho%2F4514744)
*   [](https://www.facebook.com/share.php?u=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fappsonazureblog%2Fhow-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho%2F4514744&t=How%20ACR%20Artifact%20Cache%20Handles%20Multi-Arch%20Images%3A%20What%20Gets%20Cached%20and%20When%20Webhooks%20Fire)
*   [](https://twitter.com/share?text=How%20ACR%20Artifact%20Cache%20Handles%20Multi-Arch%20Images%3A%20What%20Gets%20Cached%20and%20When%20Webhooks%20Fire&url=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fappsonazureblog%2Fhow-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho%2F4514744)
*   [](https://www.reddit.com/submit?url=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fappsonazureblog%2Fhow-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho%2F4514744&title=How%20ACR%20Artifact%20Cache%20Handles%20Multi-Arch%20Images%3A%20What%20Gets%20Cached%20and%20When%20Webhooks%20Fire)
*   [](https://bsky.app/intent/compose?text=How%20ACR%20Artifact%20Cache%20Handles%20Multi-Arch%20Images%3A%20What%20Gets%20Cached%20and%20When%20Webhooks%20Fire%21%20%F0%9F%A6%8B%0Ahttps%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fappsonazureblog%2Fhow-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho%2F4514744)
*   [](https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/Community)
*   [](mailto:?body=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fappsonazureblog%2Fhow-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho%2F4514744)

What's new

*   [Surface Pro](https://www.microsoft.com/surface/devices/surface-pro)
*   [Surface Laptop](https://www.microsoft.com/surface/devices/surface-laptop)
*   [Surface Laptop Studio 2](https://www.microsoft.com/d/Surface-Laptop-Studio-2/8rqr54krf1dz)
*   [Copilot for organizations](https://www.microsoft.com/microsoft-copilot/organizations?icid=DSM_Footer_CopilotOrganizations)
*   [Copilot for personal use](https://www.microsoft.com/microsoft-copilot/for-individuals?form=MY02PT&OCID=GE_web_Copilot_Free_868g3t5nj)
*   [AI in Windows](https://www.microsoft.com/windows/ai-features?icid=DSM_Footer_WhatsNew_AIinWindows)
*   [Explore Microsoft products](https://www.microsoft.com/microsoft-products-and-apps)
*   [Windows 11 apps](https://www.microsoft.com/windows/apps-for-windows?icid=DSM_Footer_WhatsNew_Windows11apps)

Microsoft Store

*   [Account profile](https://account.microsoft.com/)
*   [Download Center](https://www.microsoft.com/download)
*   [Microsoft Store support](https://go.microsoft.com/fwlink/?linkid=2139749)
*   [Returns](https://go.microsoft.com/fwlink/p/?LinkID=824764&clcid=0x809)
*   [Order tracking](https://www.microsoft.com/store/b/order-tracking)
*   [Certified Refurbished](https://www.microsoft.com/store/b/certified-refurbished-products)
*   [Microsoft Store Promise](https://www.microsoft.com/store/b/why-microsoft-store?icid=footer_why-msft-store_7102020)
*   [Flexible Payments](https://www.microsoft.com/store/b/payment-financing-options?icid=footer_financing_vcc)

Education

*   [Microsoft in education](https://www.microsoft.com/education)
*   [Devices for education](https://www.microsoft.com/education/devices/overview)
*   [Microsoft Teams for Education](https://www.microsoft.com/education/products/teams)
*   [Microsoft 365 Education](https://www.microsoft.com/education/products/microsoft-365)
*   [How to buy for your school](https://www.microsoft.com/education/how-to-buy)
*   [Educator training and development](https://education.microsoft.com/)
*   [Deals for students and parents](https://www.microsoft.com/store/b/education)
*   [AI for education](https://www.microsoft.com/education/ai-in-education)

Business

*   [Microsoft AI](https://www.microsoft.com/ai?icid=DSM_Footer_AI)
*   [Microsoft Security](https://www.microsoft.com/security)
*   [Dynamics 365](https://www.microsoft.com/dynamics-365)
*   [Microsoft 365](https://www.microsoft.com/microsoft-365/business)
*   [Microsoft Power Platform](https://www.microsoft.com/power-platform)
*   [Microsoft Teams](https://www.microsoft.com/microsoft-teams/group-chat-software)
*   [Microsoft 365 Copilot](https://www.microsoft.com/microsoft-365-copilot?icid=DSM_Footer_Microsoft365Copilot)
*   [Small Business](https://www.microsoft.com/store/b/business?icid=CNavBusinessStore)

Developer & IT

*   [Azure](https://azure.microsoft.com/)
*   [Microsoft Developer](https://developer.microsoft.com/)
*   [Microsoft Learn](https://learn.microsoft.com/)
*   [Support for AI marketplace apps](https://www.microsoft.com/software-development-companies/offers-benefits/isv-success?icid=DSM_Footer_SupportAIMarketplace&ocid=cmm3atxvn98)
*   [Microsoft Tech Community](https://techcommunity.microsoft.com/)
*   [Microsoft Marketplace](https://marketplace.microsoft.com/?icid=DSM_Footer_Marketplace&ocid=cmm3atxvn98)
*   [Marketplace Rewards](https://www.microsoft.com/software-development-companies/offers-benefits/marketplace-rewards?icid=DSM_Footer_MarketplaceRewards&ocid=cmm3atxvn98)
*   [Visual Studio](https://visualstudio.microsoft.com/)

Company

*   [Careers](https://careers.microsoft.com/)
*   [About Microsoft](https://www.microsoft.com/about)
*   [Company news](https://news.microsoft.com/source/?icid=DSM_Footer_Company_CompanyNews)
*   [Privacy at Microsoft](https://www.microsoft.com/privacy?icid=DSM_Footer_Company_Privacy)
*   [Investors](https://www.microsoft.com/investor/default.aspx)
*   [Diversity and inclusion](https://www.microsoft.com/diversity/default?icid=DSM_Footer_Company_Diversity)
*   [Accessibility](https://www.microsoft.com/accessibility)
*   [Sustainability](https://www.microsoft.com/sustainability/)

[Your Privacy Choices](https://aka.ms/yourcaliforniaprivacychoices)[Consumer Health Privacy](https://go.microsoft.com/fwlink/?linkid=2259814)

*   [Sitemap](https://www.microsoft.com/en-us/sitemap1.aspx)
*   [Contact Microsoft](https://support.microsoft.com/contactus)
*   [Privacy](https://go.microsoft.com/fwlink/?LinkId=521839)
*   [Manage cookies](javascript:manageConsent();)
*   [Terms of use](https://go.microsoft.com/fwlink/?LinkID=206977)
*   [Trademarks](https://go.microsoft.com/fwlink/?linkid=2196228)
*   [Safety & eco](https://go.microsoft.com/fwlink/?linkid=2196227)
*   [Recycling](https://www.microsoft.com/legal/compliance/recycling)
*   [About our ads](https://choice.microsoft.com/)
*   © Microsoft 2026

*   [![Image 11: Share to LinkedIn](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/social-share-linkedin.svg?time=1743177821000)Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fappsonazureblog%2Fhow-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho%2F4514744)
*   [![Image 12: Share to Facebook](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/social-share-facebook.svg?time=1743177821000)Share on Facebook](https://www.facebook.com/share.php?u=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fappsonazureblog%2Fhow-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho%2F4514744&t=How%20ACR%20Artifact%20Cache%20Handles%20Multi-Arch%20Images%3A%20What%20Gets%20Cached%20and%20When%20Webhooks%20Fire)
*   [![Image 13: Share to X](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/social-share-x.svg?time=1743177821000)Share on X](https://twitter.com/share?text=How%20ACR%20Artifact%20Cache%20Handles%20Multi-Arch%20Images%3A%20What%20Gets%20Cached%20and%20When%20Webhooks%20Fire&url=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fappsonazureblog%2Fhow-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho%2F4514744)
*   [![Image 14: Share to Reddit](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/social-share-reddit.svg?time=1743177821000)Share on Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fappsonazureblog%2Fhow-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho%2F4514744&title=How%20ACR%20Artifact%20Cache%20Handles%20Multi-Arch%20Images%3A%20What%20Gets%20Cached%20and%20When%20Webhooks%20Fire)
*   [![Image 15: Share to Blue Sky](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/bluesky-brands.svg?time=1743697028000)Share on Bluesky](https://bsky.app/intent/compose?text=How%20ACR%20Artifact%20Cache%20Handles%20Multi-Arch%20Images%3A%20What%20Gets%20Cached%20and%20When%20Webhooks%20Fire%21%20%F0%9F%A6%8B%0Ahttps%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fappsonazureblog%2Fhow-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho%2F4514744)
*   [![Image 16: Subscribe to RSS](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/rss.svg?time=1743177821000)Share on RSS](https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/Community)
*   [![Image 17: Share to Email](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/social-share-email.svg?time=1743177821000)Share on Email](mailto:?body=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fappsonazureblog%2Fhow-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho%2F4514744)

"}},"componentScriptGroups({\"componentId\":\"custom.widget.SocialSharing\"})":{"__typename":"ComponentScriptGroups","scriptGroups":{"__typename":"ComponentScriptGroupsDefinition","afterInteractive":{"__typename":"PageScriptGroupDefinition","group":"AFTER_INTERACTIVE","scriptIds":[]},"lazyOnLoad":{"__typename":"PageScriptGroupDefinition","group":"LAZY_ON_LOAD","scriptIds":[]}},"componentScripts":[]},"component({\"componentId\":\"custom.widget.MicrosoftFooter\"})":{"__typename":"Component","render({\"context\":{\"component\":{\"entities\":[],\"props\":{}},\"page\":{\"entities\":[\"message:4514744\"],\"name\":\"BlogMessagePage\",\"props\":{},\"url\":\"https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744\"}}})":{"__typename":"ComponentRenderResult","html":"

*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/surface/devices/surface-pro\" data-m=\"{"cN":"Footer_WhatsNew_SurfacePro_nav","id":"n1c1c1c1m1r1a2","sN":1,"aN":"c1c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/surface/devices/surface-laptop\" data-m=\"{"cN":"Footer_WhatsNew_SurfaceLaptop_nav","id":"n2c1c1c1m1r1a2","sN":2,"aN":"c1c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/d/Surface-Laptop-Studio-2/8rqr54krf1dz\" data-m=\"{"cN":"Footer_WhatsNew_SurfaceLaptopStudio2_nav","id":"n3c1c1c1m1r1a2","sN":3,"aN":"c1c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/microsoft-copilot/organizations?icid=DSM_Footer_CopilotOrganizations\" data-m=\"{"cN":"Footer_WhatsNew_CopilotOrganizations_nav","id":"n4c1c1c1m1r1a2","sN":4,"aN":"c1c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/microsoft-copilot/for-individuals?form=MY02PT&OCID=GE_web_Copilot_Free_868g3t5nj\" data-m=\"{"cN":"Footer_WhatsNew_CopilotPersonal_nav","id":"n5c1c1c1m1r1a2","sN":5,"aN":"c1c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/windows/ai-features?icid=DSM_Footer_WhatsNew_AIinWindows\" data-m=\"{"cN":"Footer_WhatsNew_AIinWindows_nav","id":"n6c1c1c1m1r1a2","sN":6,"aN":"c1c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/microsoft-products-and-apps\" data-m=\"{"cN":"Footer_WhatsNew_ExploreMicrosoftProducts_nav","id":"n7c1c1c1m1r1a2","sN":7,"aN":"c1c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/windows/apps-for-windows?icid=DSM_Footer_WhatsNew_Windows11apps\" data-m=\"{"cN":"Footer_WhatsNew_Windows11Apps_nav","id":"n8c1c1c1m1r1a2","sN":8,"aN":"c1c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)

*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://account.microsoft.com/\" data-m=\"{"cN":"Footer_StoreandSupport_AccountProfile_nav","id":"n1c2c1c1m1r1a2","sN":1,"aN":"c2c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/download\" data-m=\"{"cN":"Footer_StoreandSupport_DownloadCenter_nav","id":"n2c2c1c1m1r1a2","sN":2,"aN":"c2c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://go.microsoft.com/fwlink/?linkid=2139749\" data-m=\"{"cN":"Footer_StoreandSupport_SalesAndSupport_nav","id":"n3c2c1c1m1r1a2","sN":3,"aN":"c2c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" id=\"footer-returns\" href=\"https://go.microsoft.com/fwlink/p/?LinkID=824764&clcid=0x809\" data-m=\"{"cN":"Footer_StoreandSupport_Returns_nav","id":"n4c2c1c1m1r1a2","sN":4,"aN":"c2c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/store/b/order-tracking\" data-m=\"{"cN":"Footer_StoreandSupport_OrderTracking_nav","id":"n5c2c1c1m1r1a2","sN":5,"aN":"c2c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/store/b/certified-refurbished-products\" data-m=\"{"cN":"Footer_StoreandSupport_CertifiedRefurbished_nav","id":"n6c2c1c1m1r1a2","sN":6,"aN":"c2c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/store/b/why-microsoft-store?icid=footer_why-msft-store_7102020\" data-m=\"{"cN":"Footer_StoreandSupport_MicrosoftPromise_nav","id":"n7c2c1c1m1r1a2","sN":7,"aN":"c2c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/store/b/payment-financing-options?icid=footer_financing_vcc\" data-m=\"{"cN":"Footer_StoreandSupport_Financing_nav","id":"n8c2c1c1m1r1a2","sN":8,"aN":"c2c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)

*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/education\" data-m=\"{"cN":"Footer_Education_MicrosoftInEducation_nav","id":"n1c3c1c1m1r1a2","sN":1,"aN":"c3c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/education/devices/overview\" data-m=\"{"cN":"Footer_Education_DevicesforEducation_nav","id":"n2c3c1c1m1r1a2","sN":2,"aN":"c3c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/education/products/teams\" data-m=\"{"cN":"Footer_Education_MicrosoftTeamsforEducation_nav","id":"n3c3c1c1m1r1a2","sN":3,"aN":"c3c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/education/products/microsoft-365\" data-m=\"{"cN":"Footer_Education_Microsoft365Education_nav","id":"n4c3c1c1m1r1a2","sN":4,"aN":"c3c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/education/how-to-buy\" data-m=\"{"cN":"Footer_Education_HowToBuy_nav","id":"n5c3c1c1m1r1a2","sN":5,"aN":"c3c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://education.microsoft.com/\" data-m=\"{"cN":"Footer_Education_EducatorTrainingDevelopment_nav","id":"n6c3c1c1m1r1a2","sN":6,"aN":"c3c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/store/b/education\" data-m=\"{"cN":"Footer_Education_DealsForStudentsandParents_nav","id":"n7c3c1c1m1r1a2","sN":7,"aN":"c3c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/education/ai-in-education\" data-m=\"{"cN":"Footer_Education_AIinEducation_nav","id":"n8c3c1c1m1r1a2","sN":8,"aN":"c3c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)

*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/ai?icid=DSM_Footer_AI\" data-m=\"{"cN":"Footer_Business_MicrosoftAI_nav","id":"n1c4c1c1m1r1a2","sN":1,"aN":"c4c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/security\" data-m=\"{"cN":"Footer_Business_MicrosoftSecurity_nav","id":"n2c4c1c1m1r1a2","sN":2,"aN":"c4c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/dynamics-365\" data-m=\"{"cN":"Footer_Business_MicrosoftDynamics365_nav","id":"n3c4c1c1m1r1a2","sN":3,"aN":"c4c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/microsoft-365/business\" data-m=\"{"cN":"Footer_Business_Microsoft365_nav","id":"n4c4c1c1m1r1a2","sN":4,"aN":"c4c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/power-platform\" data-m=\"{"cN":"Footer_Business_MicrosoftPowerPlatform_nav","id":"n5c4c1c1m1r1a2","sN":5,"aN":"c4c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/microsoft-teams/group-chat-software\" data-m=\"{"cN":"Footer_Business_MicrosoftTeams_nav","id":"n6c4c1c1m1r1a2","sN":6,"aN":"c4c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/microsoft-365-copilot?icid=DSM_Footer_Microsoft365Copilot\" data-m=\"{"cN":"Footer_Business_Microsoft365Copilot_nav","id":"n7c4c1c1m1r1a2","sN":7,"aN":"c4c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/store/b/business?icid=CNavBusinessStore\" data-m=\"{"cN":"Footer_Business_SmallBusiness_nav","id":"n8c4c1c1m1r1a2","sN":8,"aN":"c4c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)

*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://azure.microsoft.com/\" data-m=\"{"cN":"Footer_Enterprise_MicrosoftAzure_nav","id":"n1c5c1c1m1r1a2","sN":1,"aN":"c5c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://developer.microsoft.com/\" data-m=\"{"cN":"Footer_Developer_DeveloperCenter_nav","id":"n2c5c1c1m1r1a2","sN":2,"aN":"c5c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://learn.microsoft.com/\" data-m=\"{"cN":"Footer_DeveloperAndIT_MicrosoftLearn_nav","id":"n3c5c1c1m1r1a2","sN":3,"aN":"c5c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/software-development-companies/offers-benefits/isv-success?icid=DSM_Footer_SupportAIMarketplace&ocid=cmm3atxvn98\" data-m=\"{"cN":"Footer_DeveloperAndIT_SupportAIMarketplace_nav","id":"n4c5c1c1m1r1a2","sN":4,"aN":"c5c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://techcommunity.microsoft.com/\" data-m=\"{"cN":"Footer_DeveloperAndIT_MicrosoftTechCommunity_nav","id":"n5c5c1c1m1r1a2","sN":5,"aN":"c5c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://marketplace.microsoft.com/?icid=DSM_Footer_Marketplace&ocid=cmm3atxvn98\" data-m=\"{"cN":"Footer_DeveloperAndIT_Marketplace_nav","id":"n6c5c1c1m1r1a2","sN":6,"aN":"c5c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/software-development-companies/offers-benefits/marketplace-rewards?icid=DSM_Footer_MarketplaceRewards&ocid=cmm3atxvn98\" data-m=\"{"cN":"Footer_DeveloperAndIT_MarketplaceRewards_nav","id":"n7c5c1c1m1r1a2","sN":7,"aN":"c5c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://visualstudio.microsoft.com/\" data-m=\"{"cN":"Footer_Developer_MicrosoftVisualStudio_nav","id":"n8c5c1c1m1r1a2","sN":8,"aN":"c5c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)

*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://careers.microsoft.com/\" data-m=\"{"cN":"Footer_Company_Careers_nav","id":"n1c6c1c1m1r1a2","sN":1,"aN":"c6c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/about\" data-m=\"{"cN":"Footer_Company_AboutMicrosoft_nav","id":"n2c6c1c1m1r1a2","sN":2,"aN":"c6c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://news.microsoft.com/source/?icid=DSM_Footer_Company_CompanyNews\" data-m=\"{"cN":"Footer_Company_CompanyNews_nav","id":"n3c6c1c1m1r1a2","sN":3,"aN":"c6c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/privacy?icid=DSM_Footer_Company_Privacy\" data-m=\"{"cN":"Footer_Company_PrivacyAtMicrosoft_nav","id":"n4c6c1c1m1r1a2","sN":4,"aN":"c6c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/investor/default.aspx\" data-m=\"{"cN":"Footer_Company_Investors_nav","id":"n5c6c1c1m1r1a2","sN":5,"aN":"c6c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/diversity/default?icid=DSM_Footer_Company_Diversity\" data-m=\"{"cN":"Footer_Company_DiversityAndInclusion_nav","id":"n6c6c1c1m1r1a2","sN":6,"aN":"c6c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/accessibility\" data-m=\"{"cN":"Footer_Company_Accessibility_nav","id":"n7c6c1c1m1r1a2","sN":7,"aN":"c6c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/sustainability/\" data-m=\"{"cN":"Footer_Company_Sustainability_nav","id":"n8c6c1c1m1r1a2","sN":8,"aN":"c6c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)

[](https://techcommunity.microsoft.com/%22https://aka.ms/yourcaliforniaprivacychoices/%22)[](https://techcommunity.microsoft.com/%22https://go.microsoft.com/fwlink/?linkid=2259814\%22)

*   [](https://techcommunity.microsoft.com/%22https://www.microsoft.com/en-us/sitemap1.aspx/%22)
*   [](https://techcommunity.microsoft.com/%22https://support.microsoft.com/contactus/%22)
*   [](https://techcommunity.microsoft.com/%22https://go.microsoft.com/fwlink/?LinkId=521839\%22)
*   [](https://techcommunity.microsoft.com/%22javascript:manageConsent();/%22)
*   [](https://techcommunity.microsoft.com/%22https://go.microsoft.com/fwlink/?LinkID=206977\%22)
*   [](https://techcommunity.microsoft.com/%22https://go.microsoft.com/fwlink/?linkid=2196228\%22)
*   [](https://techcommunity.microsoft.com/%22https://go.microsoft.com/fwlink/?linkid=2196227\%22)
*   [](https://techcommunity.microsoft.com/%22https://www.microsoft.com/legal/compliance/recycling/%22)
*   [](https://techcommunity.microsoft.com/%22https://choice.microsoft.com/%22)
*   © 

*   [![Image 18: \"<li:i18n](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)</li:i18n>\" src=\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/social-share-linkedin.svg?time=1743177821000\">](https://techcommunity.microsoft.com/%22https://www.linkedin.com/sharing/share-offsite/?url=page.url\%22)
*   [![Image 19: \"<li:i18n](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)</li:i18n>\" src=\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/social-share-facebook.svg?time=1743177821000\">](https://techcommunity.microsoft.com/%22https://www.facebook.com/share.php?u=page.url&t=page-name\%22)
*   [![Image 20: \"<li:i18n](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)</li:i18n>\" src=\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/social-share-x.svg?time=1743177821000\">](https://techcommunity.microsoft.com/%22https://twitter.com/share?text=page-name&url=page.url\%22)
*   [![Image 21: \"<li:i18n](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)</li:i18n>\" src=\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/social-share-reddit.svg?time=1743177821000\">](https://techcommunity.microsoft.com/%22https://www.reddit.com/submit?url=page.url&title=page-name\%22)
*   [![Image 22: \"<li:i18n](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)</li:i18n>\" src=\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/bluesky-brands.svg?time=1743697028000\">](https://techcommunity.microsoft.com/%22https://bsky.app/intent/compose?text=page-name%21%20%F0%9F%A6%8B%0Apage.url\%22)
*   [![Image 23: \"<li:i18n](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)</li:i18n>\" src=\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/rss.svg?time=1743177821000\">](https://techcommunity.microsoft.com/%22/t5/s/gxcuf89792/rss/Community/%22)
*   [![Image 24: \"<li:i18n](https://techcommunity.microsoft.com/blog/appsonazureblog/how-acr-artifact-cache-handles-multi-arch-images-what-gets-cached-and-when-webho/4514744)</li:i18n>\" src=\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/social-share-email.svg?time=1743177821000\">](https://techcommunity.microsoft.com/%22mailto:?body=page.url\%22)

"}},"componentScriptGroups({\"componentId\":\"custom.widget.MicrosoftFooter\"})":{"__typename":"ComponentScriptGroups","scriptGroups":{"__typename":"ComponentScriptGroupsDefinition","afterInteractive":{"__typename":"PageScriptGroupDefinition","group":"AFTER_INTERACTIVE","scriptIds":[]},"lazyOnLoad":{"__typename":"PageScriptGroupDefinition","group":"LAZY_ON_LOAD","scriptIds":[]}},"componentScripts":[]},"cachedText({\"lastModified\":\"1780328569503\",\"locale\":\"en-US\",\"namespaces\":[\"components/community/NavbarDropdownToggle\"]})":[{"__ref":"CachedAsset:text:en_US-components/community/NavbarDropdownToggle-1780328569503"}],"cachedText({\"lastModified\":\"1780328569503\",\"locale\":\"en-US\",\"namespaces\":[\"components/messages/MessageCoverImage\"]})":[{"__ref":"CachedAsset:text:en_US-components/messages/MessageCoverImage-1780328569503"}],"cachedText({\"lastModified\":\"1780328569503\",\"locale\":\"en-US\",\"namespaces\":[\"shared/client/components/nodes/NodeTitle\"]})":[{"__ref":"CachedAsset:text:en_US-shared/client/components/nodes/NodeTitle-1780328569503"}],"cachedText({\"lastModified\":\"1780328569503\",\"locale\":\"en-US\",\"namespaces\":[\"components/messages/MessageTimeToRead\"]})":[{"__ref":"CachedAsset:text:en_US-components/messages/MessageTimeToRead-1780328569503"}],"cachedText({\"lastModified\":\"1780328569503\",\"locale\":\"en-US\",\"namespaces\":[\"components/messages/MessageSubject\"]})":[{"__ref":"CachedAsset:text:en_US-components/messages/MessageSubject-1780328569503"}],"cachedText({\"lastModified\":\"1780328569503\",\"locale\":\"en-US\",\"namespaces\":[\"components/users/UserLink\"]})":[{"__ref":"CachedAsset:text:en_US-components/users/UserLink-1780328569503"}],"cachedText({\"lastModified\":\"1780328569503\",\"locale\":\"en-US\",\"namespaces\":[\"shared/client/components/users/UserRank\"]})":[{"__ref":"CachedAsset:text:en_US-shared/client/components/users/UserRank-1780328569503"}],"cachedText({\"lastModified\":\"1780328569503\",\"locale\":\"en-US\",\"namespaces\":[\"components/messages/MessageTime\"]})":[{"__ref":"CachedAsset:text:en_US-components/messages/MessageTime-1780328569503"}],"cachedText({\"lastModified\":\"1780328569503\",\"locale\":\"en-US\",\"namespaces\":[\"components/messages/MessageBody\"]})":[{"__ref":"CachedAsset:text:en_US-components/messages/MessageBody-1780328569503"}],"cachedText({\"lastModified\":\"1780328569503\",\"locale\":\"en-US\",\"namespaces\":[\"components/messages/MessageCustomFields\"]})":[{"__ref":"CachedAsset:text:en_US-components/messages/MessageCustomFields-1780328569503"}],"cachedText({\"lastModified\":\"1780328569503\",\"locale\":\"en-US\",\"namespaces\":[\"components/messages/MessageRevision\"]})":[{"__ref":"CachedAsset:text:en_US-components/messages/MessageRevision-1780328569503"}],"cachedText({\"lastModified\":\"1780328569503\",\"locale\":\"en-US\",\"namespaces\":[\"shared/client/components/common/QueryHandler\"]})":[{"__ref":"CachedAsset:text:en_US-shared/client/components/common/QueryHandler-1780328569503"}],"cachedText({\"lastModified\":\"1780328569503\",\"locale\":\"en-US\",\"namespaces\":[\"components/tags/TagList\"]})":[{"__ref":"CachedAsset:text:en_US-components/tags/TagList-1780328569503"}],"cachedText({\"lastModified\":\"1780328569503\",\"locale\":\"en-US\",\"namespaces\":[\"components/messages/MessageReplyButton\"]})":[{"__ref":"CachedAsset:text:en_US-components/messages/MessageReplyButton-1780328569503"}],"cachedText({\"lastModified\":\"1780328569503\",\"locale\":\"en-US\",\"namespaces\":[\"components/messages/MessageAuthorBio\"]})":[{"__ref":"CachedAsset:text:en_US-components/messages/MessageAuthorBio-1780328569503"}],"coreNode({\"id\":\"community:gxcuf89792\"})":{"__ref":"Community:community:gxcuf89792"},"cachedText({\"lastModified\":\"1780328569503\",\"locale\":\"en-US\",\"namespaces\":[\"shared/client/components/users/UserAvatar\"]})":[{"__ref":"CachedAsset:text:en_US-shared/client/components/users/UserAvatar-1780328569503"}],"cachedText({\"lastModified\":\"1780328569503\",\"locale\":\"en-US\",\"namespaces\":[\"shared/client/components/ranks/UserRankLabel\"]})":[{"__ref":"CachedAsset:text:en_US-shared/client/components/ranks/UserRankLabel-1780328569503"}],"cachedText({\"lastModified\":\"1780328569503\",\"locale\":\"en-US\",\"namespaces\":[\"components/tags/TagView/TagViewChip\"]})":[{"__ref":"CachedAsset:text:en_US-components/tags/TagView/TagViewChip-1780328569503"}],"cachedText({\"lastModified\":\"1780328569503\",\"locale\":\"en-US\",\"namespaces\":[\"components/users/UserRegistrationDate\"]})":[{"__ref":"CachedAsset:text:en_US-components/users/UserRegistrationDate-1780328569503"}],"cachedText({\"lastModified\":\"1780328569503\",\"locale\":\"en-US\",\"namespaces\":[\"shared/client/components/nodes/NodeAvatar\"]})":[{"__ref":"CachedAsset:text:en_US-shared/client/components/nodes/NodeAvatar-1780328569503"}],"cachedText({\"lastModified\":\"1780328569503\",\"locale\":\"en-US\",\"namespaces\":[\"shared/client/components/nodes/NodeDescription\"]})":[{"__ref":"CachedAsset:text:en_US-shared/client/components/nodes/NodeDescription-1780328569503"}],"customFieldDefinitions({\"fieldNames\":[\"blogScoreGradeResponse\"]})":[{"__typename":"CustomFieldDefinitionResource","definition":{"__typename":"CustomFieldDefinition","name":"blogScoreGradeResponse","viewable":false}}],"cachedText({\"lastModified\":\"1780328569503\",\"locale\":\"en-US\",\"namespaces\":[\"shared/client/components/nodes/NodeIcon\"]})":[{"__ref":"CachedAsset:text:en_US-shared/client/components/nodes/NodeIcon-1780328569503"}]},"Theme:customTheme1":{"__typename":"Theme","id":"customTheme1"},"User:user:-1":{"__typename":"User","id":"user:-1","entityType":"USER","eventPath":"community:gxcuf89792/user:-1","uid":-1,"login":"Deleted","email":"","avatar":null,"rank":null,"kudosWeight":1,"registrationData":{"__typename":"RegistrationData","status":"ANONYMOUS","registrationTime":null,"confirmEmailStatus":false,"registrationAccessLevel":"VIEW","ssoRegistrationFields":[]},"ssoId":null,"profileSettings":{"__typename":"ProfileSettings","dateDisplayStyle":{"__typename":"InheritableStringSettingWithPossibleValues","key":"layout.friendly_dates_enabled","value":"false","localValue":"true","possibleValues":["true","false"]},"dateDisplayFormat":{"__typename":"InheritableStringSetting","key":"layout.format_pattern_date","value":"MMM dd yyyy","localValue":"MM-dd-yyyy"},"language":{"__typename":"InheritableStringSettingWithPossibleValues","key":"profile.language","value":"en-US","localValue":null,"possibleValues":["en-US","es-ES"]},"repliesSortOrder":{"__typename":"InheritableStringSettingWithPossibleValues","key":"config.user_replies_sort_order","value":"DEFAULT","localValue":"DEFAULT","possibleValues":["DEFAULT","LIKES","PUBLISH_TIME","REVERSE_PUBLISH_TIME"]}},"deleted":false},"CachedAsset:pages-1780328551759":{"__typename":"CachedAsset","id":"pages-1780328551759","value":[{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"BlogViewAllPostsPage","type":"BLOG","urlPath":"/category/:categoryId/blog/:boardId/all-posts/(/:after|/:before)?","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"CasePortalPage","type":"CASE_PORTAL","urlPath":"/caseportal","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"CreateGroupHubPage","type":"GROUP_HUB","urlPath":"/groups/create","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"CaseViewPage","type":"CASE_DETAILS","urlPath":"/case/:caseId/:caseNumber","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"InboxPage","type":"COMMUNITY","urlPath":"/inbox","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"HelpFAQPage","type":"COMMUNITY","urlPath":"/help","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"IdeaMessagePage","type":"IDEA_POST","urlPath":"/idea/:boardId/:messageSubject/:messageId","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"IdeaViewAllIdeasPage","type":"IDEA","urlPath":"/category/:categoryId/ideas/:boardId/all-ideas/(/:after|/:before)?","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"LoginPage","type":"USER","urlPath":"/signin","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"WorkstreamsPage","type":"COMMUNITY","urlPath":"/workstreams","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"BlogPostPage","type":"BLOG","urlPath":"/category/:categoryId/blogs/:boardId/create","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"UserBlogPermissions.Page","type":"COMMUNITY","urlPath":"/c/user-blog-permissions/page","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"ThemeEditorPage","type":"COMMUNITY","urlPath":"/designer/themes","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"TkbViewAllArticlesPage","type":"TKB","urlPath":"/category/:categoryId/kb/:boardId/all-articles/(/:after|/:before)?","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1730819800000,"localOverride":null,"page":{"id":"AllEvents","type":"CUSTOM","urlPath":"/Events","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"OccasionEditPage","type":"EVENT","urlPath":"/event/:boardId/:messageSubject/:messageId/edit","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"OAuthAuthorizationAllowPage","type":"USER","urlPath":"/auth/authorize/allow","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"PageEditorPage","type":"COMMUNITY","urlPath":"/designer/pages","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"PostPage","type":"COMMUNITY","urlPath":"/category/:categoryId/:boardId/create","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"CreateUserGroup.Page","type":"COMMUNITY","urlPath":"/c/create-user-group/page","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"ForumBoardPage","type":"FORUM","urlPath":"/category/:categoryId/discussions/:boardId","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"TkbBoardPage","type":"TKB","urlPath":"/category/:categoryId/kb/:boardId","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"EventPostPage","type":"EVENT","urlPath":"/category/:categoryId/events/:boardId/create","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"UserBadgesPage","type":"COMMUNITY","urlPath":"/users/:login/:userId/badges","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":1780328551759,"localOverride":null,"page":{"id":"GroupHubMembershipAction","type":"GROUP_HUB","urlPath":"/membership/join/:nodeId/:membershipType","__typename":"PageDescriptor"},"__typename":"PageResource"},{"lastUpdatedTime":178032
