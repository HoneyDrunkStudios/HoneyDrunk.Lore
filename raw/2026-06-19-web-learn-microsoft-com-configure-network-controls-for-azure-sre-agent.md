---
source: "https://learn.microsoft.com/en-us/azure/sre-agent/configure-network-controls"
title: "Configure Network Controls for Azure SRE Agent"
author: "dchelupati"
date_published: "unknown"
date_clipped: "2026-06-19"
category: "Azure & Cloud"
source_type: "web"
---
# Configure Network Controls for Azure SRE Agent

Note

Access to this page requires authorization. You can try signing in or changing directories.

Access to this page requires authorization. You can try changing directories.

In this article, you set up a VNet-integrated agent with outbound traffic routed through your network, configure managed path toggles for your environment, and verify connectivity to private endpoints. For more information, see Network controls.

## Prerequisites

- An SRE Agent in
**Running**state - An Azure Virtual Network with a subnet that is
**/28 or larger** - The subnet must be
**delegated to**`Microsoft.App/environments`

**Network Contributor**role (or equivalent with`Microsoft.Network/virtualNetworks/subnets/join/action`

) on the target subnet**SRE Agent Administrator**role on the agent resource

## Open workspace configuration

- Open your agent in the Azure portal.
- In the left navigation, select
**Settings**>**Workspace configuration**. - Select the
**Networking**tab.

## Select an egress mode

Choose the mode that matches your security requirements:

**Unrestricted**: Allow all outbound traffic (default).**Limited**: Deny all, allow listed hosts.**Azure VNet**: Private egress via your VNet.

Select **Azure VNet** to route agent traffic through your network.

Note

When you connect a VNet, the Unrestricted and Limited mode cards are disabled. To switch egress modes, you must disconnect the VNet first.

## Connect your VNet

- Select
**Browse subnets...**to open the subnet picker dialog. - In the dialog, select your
**Subscription**,**Resource group**,**Virtual network**, and**Subnet**from the cascading dropdowns. The subnet must be /28 or larger and delegated to`Microsoft.App/environments`

. - Select
**Connect**. The**Use VNet's private DNS**option is enabled automatically. This option lets the agent resolve private endpoint hostnames (for example, Log Analytics workspaces behind AMPLS).

Tip

For private endpoint resolution to work, link the relevant Azure Private DNS zones to your VNet (for example, `privatelink.ods.opinsights.azure.com`

for Log Analytics, `privatelink.vaultcore.azure.net`

for Key Vault). If DNS isn't configured, the agent might fall back to public endpoints or fail to connect.

Note

To change the subnet, disconnect and reconnect the VNet.

## Configure managed path toggles

Under **On the infra network**, decide which public service categories route through the managed path instead of your VNet.

| Toggle | What it controls |
|---|---|
Remote MCP server access |
MCP server traffic |
Package registries |
PyPI, npmjs, NuGet.org, Ubuntu apt (each is an independent toggle) |
Code repositories |
GitHub, GitHub Enterprise, Azure DevOps (each is an independent toggle) |
Additional hosts |
Custom hostnames or wildcard patterns |

Start with the categories your agent needs enabled on the managed path. You can tighten these later as your network adopts FQDN-based egress filtering.

## Save and verify network connectivity

Select

**Save**.The Azure VNet card displays a

**Connected**badge confirming the agent is routed through your VNet.Test by asking the agent to query a resource behind a private endpoint (for example, a Log Analytics workspace with public access disabled). If the query succeeds, VNet routing is working.
