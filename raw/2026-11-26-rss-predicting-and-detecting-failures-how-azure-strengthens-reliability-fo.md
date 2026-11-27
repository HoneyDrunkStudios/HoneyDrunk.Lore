---
source: "https://azure.microsoft.com/en-us/blog/predicting-and-detecting-failures-how-azure-strengthens-reliability-for-mission-critical-workloads/"
title: "Predicting and detecting failures: How Azure strengthens reliability for mission-critical workloads"
author: "Mark Russinovich"
date_published: "2026-11-04"
date_clipped: "2026-11-26"
category: "Azure & Cloud"
source_type: "rss"
---

# Predicting and detecting failures: How Azure strengthens reliability for mission-critical workloads

**Takeaway**: [Azure Failure Prediction and Detection](https://techcommunity.microsoft.com/blog/azurecompute/revolutionizing-reliability-introducing-the-azure-failure-prediction-and-detecti/4464883) (AFPD) is Microsoft Azure’s end-to-end system aiming to catch hardware failures before they interrupt a workload, not after. Across the Azure fleet, AFPD has improved the [prevention of hardware-related VM interruptions by 36%](https://ieeexplore.ieee.org/abstract/document/11108193). SAP workloads offer a compelling example of AFPD’s value, illustrating why preventing interruptions matters for mission-critical services. But AFPD isn’t specific to SAP: it operates across General Purpose, Specialized Compute, HPC/AI, and select Storage workloads, making SAP’s experience a window into Azure’s broader approach to reliability for mission-critical third-party services. To learn more, watch our [companion video](https://techcommunity.microsoft.com/blog/reliability-and-resiliency-in-azure/from-proactive-detection-to-action-how-azure-protects-mission-critical-workloads/4569949) to learn how AFPD helps reduce the risk of failures disrupting your critical workloads.

## Reliability engineered into the platform

Most conversations about cloud reliability focus on what you build: zone-redundant architectures, failover patterns, and backup strategies. Less visible, but just as consequential, is what the platform does on your behalf; before a failure ever becomes an incident you need to respond to.

That’s the premise behind AFPD, which became fully operational in 2024. AFPD is an end-to-end system that uses machine learning and telemetry to predict, mitigate, and remediate hardware failures in the Azure fleet before they interrupt your workloads. For a deep dive discussion into this capability, see the companion post [here](https://techcommunity.microsoft.com/blog/reliability-and-resiliency-in-azure/from-proactive-detection-to-action-how-azure-protects-mission-critical-workloads/4569949).

## How does AFPD predict and prevent hardware failures?

Historically, hardware failures on any cloud platform follow a familiar pattern: a component degrades, your workload is interrupted, an engineer investigates, and a reboot or hardware replacement follows. This is the old model Azure has spent years moving away from, one built around mission-critical escalations, supply chain constraints, and manual recovery.

AFPD replaces that pattern with three coordinated phases:

1. **Predict and detect**: Machine learning models and detection rules continuously monitor telemetry across the Azure fleet, node behavior, component signals, and hardware-specific indicators like Solid State Drive (SSD) health, to catch patterns that indicate an active or likely future failure.
2. **Mitigate**: Once a node is flagged, the mitigation service marks it not allocatable for new workloads and, where eligible, live-migrates existing customer workloads to a healthy node with no reboot, typically just a pause of a few seconds. Live migration is available on many, but not all M-series sized virtual machines (VMs); check the [feature support table](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/memory-optimized/m-family?tabs=mbsv3%2Cmsv3mm%2Cmsv3hm%2Cmsv2mm) for more information. Where live migration isn’t possible, a notification with a redeploy deadline and recommended action is posted to the VMs Resource Health and Scheduled Events.
3. **Remediate**: The affected node is pulled from production, tagged with diagnostic detail so technicians can skip redundant troubleshooting, repaired using proactively staged spare parts, and returned to the fleet. In practice, this coordinated approach has delivered measurable gains: [AFPD has increased the monthly node repair rate by 80%](https://ieeexplore.ieee.org/abstract/document/11108193).

The result is a system that doesn’t just react faster; in many cases, it prevents the interruption from reaching you. This approach has [reduced the overall number of hardware reboots by more than 36%](https://ieeexplore.ieee.org/abstract/document/11108193), and the underlying system won the Best Paper Award at the 2025 IEEE Cloud Summit for its approach to predicting, mitigating, and remediating node interruptions at scale.

## What SAP’s result means for other workloads

Every customer benefits from fewer interruptions, but SAP workloads make the case for AFPD unusually clear. SAP systems are highly sensitive to downtime; they are often the system of record for finance, supply chain, and operations, and even brief interruptions carry outsized business impact. A platform that has the ability to predict or detect hardware issues and reduce their impact before you experience an interruption isn’t a convenience for SAP customers; it’s foundational to running SAP on Azure with confidence.

That sensitivity also exposed a real gap the team was candid about: many SAP customers aren’t yet aware of the notification and automation options available to them. [AFPD surfaces its findings](https://techcommunity.microsoft.com/blog/azurecompute/revolutionizing-reliability-introducing-the-azure-failure-prediction-and-detecti/4464883) through four consistent, customer-facing channels:

- [Resource Health](https://learn.microsoft.com/en-us/azure/virtual-machines/flash-azure-resource-health), for viewing detailed health events and recommended actions on individual VMs, including live migration eligibility and redeployment deadlines.
- [Resource Graph Explorer](https://learn.microsoft.com/en-us/azure/virtual-machines/flash-azure-resource-graph), for querying health status across your fleet, including large SAP landscapes that require programmatic visibility.
- [Event Grid](https://learn.microsoft.com/en-us/azure/virtual-machines/flash-event-grid-system-topic), for wiring AFPD events directly into your own monitoring and automation, with [Azure Functions](https://azure.microsoft.com/en-us/products/functions), webhooks, or REST APIs.
- [Scheduled Events](https://learn.microsoft.com/en-us/azure/virtual-machines/scheduled-events-overview), for receiving advance VM event notifications through IMDS, enabling configured SAP HA clusters to move resources off affected nodes.

The notification content is identical across Resource Health, Resource Graph, and Event Grid, so the channel you choose is a matter of scale and integration preference, not information quality. For SAP customers running at scale, that consistency is what makes automated, hands-off resiliency actually practical.

It’s tempting to read AFPD as an SAP-specific feature. It isn’t. SAP is simply where the stakes are high enough that the system’s value becomes obvious fastest. AFPD operates across [Azure Compute’s](https://azure.microsoft.com/en-us/products/category/compute) General Purpose and Specialized Compute offerings, HPC/AI workloads, and select Storage scenarios, meaning the same predictive, self-healing infrastructure protecting SAP landscapes today is the same infrastructure underpinning every mission-critical third-party service hosted on Azure.

That’s the broader narrative worth taking away: AFPD isn’t a tier you pay up for or something you have to configure at the infrastructure layer; it runs automatically across the fleet. It’s an active, continuously improving discipline, one where machine learning models get better at predicting failure over time, where remediation gets faster because spares are already staged, and where your first signal of a problem is often a notification that it’s already been handled. For any ISV or enterprise running a downtime intolerant workload on Azure, SAP’s experience with AFPD is a preview, not an exception.

## What to do next

- **Check your own notification setup**. If you’re running SAP or another mission-critical workload on Azure, confirm you’re consuming AFPD events through one of these:
  - **[Resource Health (RHC)](https://learn.microsoft.com/en-us/azure/service-health/resource-health-overview)**: Best for looking at the health of one VM, including what happened and why.
  - **[Resource Graph (ARG)](https://learn.microsoft.com/en-us/azure/governance/resource-graph/overview)**: Best for finding affected VMs at scale across many subscriptions in a single query.
  - **[Event Grid](https://learn.microsoft.com/en-us/azure/event-grid/event-schema-health-resources?tabs=event-grid-event-schema)**: Best for automation, since it pushes notifications as health changes so you can react without polling. Events can be sent to a REST webhook endpoint or an [Azure Functions](https://azure.microsoft.com/en-us/products/functions), and onward to other services such as Logic Apps, Event Hubs, or Azure Monitor alerts.
  - **[Prepare your automation for Scheduled Events](https://learn.microsoft.com/en-us/azure/virtual-machines/scheduled-events-overview)**: Make sure your automation can process [Scheduled Events](https://learn.microsoft.com/en-us/azure/virtual-machines/scheduled-events-overview) for [Azure Virtual Machines](https://azure.microsoft.com/en-us/products/virtual-machines), including events with a NotBefore time up to seven days in the future.
  - **Configure Pacemaker for Azure Scheduled Events**: For SAP high-availability clusters, follow the guidance for configuring the Pacemaker `azure-events-az` resource agent leveraging the relevant guides for [SUSE Linux Enterprise Server (SLES) in Azure](https://learn.microsoft.com/en-us/azure/sap/workloads/high-availability-guide-suse-pacemaker?tabs=msi&pivots=sbd-shared-disk) or [RHEL in Azure](https://learn.microsoft.com/en-us/azure/sap/workloads/high-availability-guide-rhel-pacemaker?tabs=msi%2Crhel10&pivots=sbd-shared-disk).
- **Watch the full conversation**. The [SAP on Azure podcast episode](https://www.saponazurepodcast.de/episode301) goes deeper into the live demo of Resource Health, Resource Graph, and Event Grid notifications than this post can cover.
- **Go deeper technically**. The IEEE paper, [AFPD: System for Prediction, Mitigation and Remediation of Node Interruptions in Cloud Infrastructure (IEEE)](https://ieeexplore.ieee.org/abstract/document/11108193) (2025 IEEE Cloud Summit Best Paper), covers the ML models and system architecture in full detail.

---

**Related resources**

- [From Proactive Detection to Action: How Azure Protects Mission-Critical Workloads](https://techcommunity.microsoft.com/blog/reliability-and-resiliency-in-azure/from-proactive-detection-to-action-how-azure-protects-mission-critical-workloads/4569949)
- [Revolutionizing Reliability: Introducing the Azure Failure Prediction and Detection (AFPD) system](https://techcommunity.microsoft.com/blog/azurecompute/revolutionizing-reliability-introducing-the-azure-failure-prediction-and-detecti/4464883)
- [AFPD: System for Prediction, Mitigation and Remediation of Node Interruptions in Cloud Infrastructure (IEEE)](https://ieeexplore.ieee.org/abstract/document/11108193)
- [Resource Health virtual machine Health Annotations](https://learn.microsoft.com/en-us/azure/service-health/resource-health-vm-annotation)
- [Project Flash – Use Azure Resource Health to monitor Azure Virtual Machine availability](https://learn.microsoft.com/en-us/azure/virtual-machines/flash-azure-resource-health)
- [Project Flash – Use Azure Resource Graph to monitor Azure Virtual Machine availability](https://learn.microsoft.com/en-us/azure/virtual-machines/flash-azure-resource-graph)
- [List of sample Azure Resource Graph queries by table](https://learn.microsoft.com/en-us/previous-versions/azure/governance/resource-graph/samples/samples-by-table?tabs=azure-cli#healthresourcechanges)
- [Advancing failure prediction and mitigation—introducing Narya](https://azure.microsoft.com/en-us/blog/advancing-failure-prediction-and-mitigation-introducing-narya/?msockid=0b9480c9a32a63ae2204955da23e6290)
- [SAP on Azure](https://learn.microsoft.com/en-us/azure/sap/)
- [Set up Pacemaker on SUSE Linux Enterprise Server (SLES) in Azure](https://learn.microsoft.com/en-us/azure/sap/workloads/high-availability-guide-suse-pacemaker?tabs=msi&pivots=sbd-shared-disk)
- [Set up Pacemaker on RHEL in Azure](https://learn.microsoft.com/en-us/azure/sap/workloads/high-availability-guide-rhel-pacemaker?tabs=msi%2Crhel10&pivots=sbd-shared-disk)
- [M family VM size series](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/memory-optimized/m-family?tabs=mbsv3%2Cmsv3mm%2Cmsv3hm%2Cmsv2mm)
