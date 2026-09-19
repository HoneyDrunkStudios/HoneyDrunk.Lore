---
source: "https://techcommunity.microsoft.com/blog/appsonazureblog/azure-sre-agent-vnet-integration-is-now-generally-available/4549774"
title: "Azure SRE Agent VNet integration is now generally available"
author: "Cary_Chai"
date_published: "2026-08-25"
date_clipped: "2026-09-19"
category: "Azure & Cloud"
source_type: "rss"
capture_format: "attributed-summary"
---

# Azure SRE Agent VNet integration is now generally available

Source: [Azure SRE Agent VNet integration is now generally available](https://techcommunity.microsoft.com/blog/appsonazureblog/azure-sre-agent-vnet-integration-is-now-generally-available/4549774)

*Attributed summary of the fetched written article; not a verbatim reproduction.*

Microsoft announces general availability of VNet integration for Azure SRE Agent. Selected outbound traffic can reach private resources through existing routing, firewall, network security group, and private DNS configuration.

The article distinguishes three controls: network routing limits destinations; identity and permissions govern resource access; tool policies and approvals govern operations. VNet integration covers outbound traffic only, and not all agent traffic uses the VNet.

Setup requires an empty dedicated subnet of /27 or larger, in the agent's region, delegated to Microsoft.App/environments. After connecting it in workspace settings, operators should check repository access and test the intended private network path.

Workspace inspection includes connectivity tests and an audit of agent egress-policy decisions. That audit is not a complete network record and must be supplemented by infrastructure logs.

HoneyDrunk implication: treat private connectivity as one layer of agent isolation, alongside authorization and tool policy. Validate actual routes and logging coverage before depending on the deployment boundary.
