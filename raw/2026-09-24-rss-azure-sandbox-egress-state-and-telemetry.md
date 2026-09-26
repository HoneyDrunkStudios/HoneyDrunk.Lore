---
source: "https://techcommunity.microsoft.com/blog/appsonazureblog/azure-container-apps-sandboxes-now-generally-available/4559125"
title: "Azure Container Apps Sandboxes, Now Generally Available"
author: "Jan-Kalis"
date_published: "2026-09-23"
date_clipped: "2026-09-24"
category: "Azure & Cloud"
source_type: "rss"
capture_method: "attributed-summary"
source_alias: "https://techcommunity.microsoft.com/t5/apps-on-azure-blog/azure-container-apps-sandboxes-now-generally-available/ba-p/4559125"
---

# Azure Container Apps Sandboxes, Now Generally Available

Attributed summary of the fetched article.

Microsoft describes generally available Container Apps Sandboxes as per-task microVMs with separate Linux kernels. External egress enforcement can filter destinations, inject credentials outside the guest, and delegate decisions to a webhook. Network isolation and access grants remain explicit configuration choices.

Disk snapshots and combined memory/disk snapshots serve different restart needs. Lifecycle policies can stop, resume, and delete instances; persistent volumes can outlive them. Data disks attach to one sandbox, while Blob-backed mounts target shared, read-heavy datasets. Telemetry is opt-in per sandbox and includes application signals and egress decisions.

HoneyDrunk application: prototype isolated agent execution with narrow outbound access, explicit retention, and audit collection. The article lists Python and TypeScript SDKs, with .NET still forthcoming. Terraform support and connector integrations retain preview qualifications. Performance and isolation descriptions are vendor claims requiring workload validation.

Source: [Original article](https://techcommunity.microsoft.com/blog/appsonazureblog/azure-container-apps-sandboxes-now-generally-available/4559125).
