---
source: "https://azure.microsoft.com/en-us/blog/enhancing-microsoft-azure-virtual-machine-lifecycle/"
title: "Enhancing Microsoft Azure Virtual Machine lifecycle"
author: "The Microsoft Azure Team"
date_published: "2026-09-28"
date_clipped: "2026-09-29"
category: "Azure & Cloud"
source_type: "rss"
capture_format: "attributed-summary"
---

# Source capture

Capture: attributed summary of the fetched written article; not a full-text reproduction.

Microsoft defines four VM lifecycle stages for general-purpose, memory-, compute-, and storage-optimized families. Current instances are recommended for new deployments. Extended instances remain supported, but migration planning and quota restrictions become relevant. End-of-life instances retain support while customers transition; capacity, new deployment, reservation, and pricing options may change.

Retirement has stronger consequences: provisioning ends, existing instances are deallocated, and support and SLA coverage cease. The policy also allows product-, region-, and operational exceptions. Advisor and Service Health are identified as tools for discovering affected resources and tracking transitions.

For HoneyDrunk, include lifecycle stage in infrastructure inventory and capacity planning. A VM that runs today is not evidence that replacement capacity or an equivalent purchasing option will remain available. Check the specific family and region before selecting migration timing; this general policy does not itself announce a retirement date for every VM series.

Source: [Original article](https://azure.microsoft.com/en-us/blog/enhancing-microsoft-azure-virtual-machine-lifecycle/).
