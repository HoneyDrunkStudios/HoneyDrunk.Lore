---
source: "https://techcommunity.microsoft.com/t5/apps-on-azure-blog/introducing-geo-redundancy-in-azure-app-service-simplify-multi/ba-p/4573896"
title: "Introducing Geo-redundancy in Azure App Service: Simplify multi-region application resilience"
author: "apwestgarth"
date_published: "2026-11-17"
date_clipped: "2026-11-24"
category: "Azure & Cloud"
source_type: "rss"
---

# Introducing Geo-redundancy in Azure App Service: Simplify multi-region application resilience

Source: https://techcommunity.microsoft.com/t5/apps-on-azure-blog/introducing-geo-redundancy-in-azure-app-service-simplify-multi/ba-p/4573896

Building resilient applications across Azure regions has traditionally required teams to deploy and maintain separate applications, coordinate application updates and configuration, and manage traffic routing and failover. While these capabilities are essential for business-critical applications, implementing them can introduce significant operational complexity.

Today, at Microsoft Ignite 2026, we're excited to announce the **public preview of Geo-redundancy in Azure App Service**, a new capability that simplifies how customers build and operate regionally resilient web applications.

With Geo-redundancy, you can extend an eligible Azure App Service web app across multiple Azure regions, synchronize supported application content and configuration, and configure health-based traffic routing and regional failover, all through a unified App Service experience.

**The result: less time managing multi-region application infrastructure and more time delivering application value.**

## Multi-region resilience, simplified

Geo-redundancy introduces a more integrated approach to building multi-region applications on Azure App Service.

Instead of independently provisioning, deploying, and maintaining web applications in multiple regions, you can start with an existing eligible web app and add managed regional replicas in supported Azure regions.

Azure App Service provisions and manages the corresponding regional application and App Service plan resources, synchronizes supported application revisions, and maintains the underlying Azure Traffic Manager configuration.

This gives you a simpler way to establish and operate a multi-region application topology while retaining control over where your application runs, how traffic is distributed, and how application revisions are synchronized.

### What's new in the public preview?

Geo-redundancy brings together several capabilities designed to simplify regional application resilience:

- **Managed regional replicas:** Extend your application into additional Azure regions without independently provisioning and maintaining each regional deployment.
- **Application content and configuration synchronization:** Keep supported application revisions aligned across regions, reducing the effort required to coordinate multi-region deployments.
- **Flexible traffic routing:** Choose between Active and Passive traffic modes to align regional traffic distribution with your application's resilience strategy.
- **Integrated health-based routing and failover:** Use Azure Traffic Manager to direct new connections to eligible, healthy regional endpoints according to your configured routing policy.
- **Application revision control:** Inspect synchronization status, validate application revisions, and use supported last-known-good revision capabilities to maintain greater control over regional deployments.

Together, these capabilities reduce the operational overhead of managing multi-region web applications while giving teams more control over how applications are deployed and served across regions.

Geo-redundancy in Azure App Service in Azure Portal

## Choose how your application serves traffic across regions

Different applications have different resilience requirements. Geo-redundancy supports two traffic modes, giving you flexibility in how regional application replicas participate in serving requests.

### Active mode: Serve traffic across multiple regions

With **Active mode**, multiple healthy regional replicas can serve application traffic simultaneously.

You can configure traffic weights to influence how new connections are distributed across eligible regional endpoints.

This approach is useful for applications designed to operate across multiple regions, allowing you to distribute application traffic while maintaining regional deployment flexibility.

### Passive mode: Prioritize a primary region with regional failover

With **Passive mode**, your application primarily serves traffic from a designated region, with additional regional replicas available as failover destinations.

You configure regional routing priorities to determine which endpoints should receive traffic when the preferred region becomes unavailable.

This approach is particularly useful for applications that normally operate from a primary region but need an alternative regional hosting destination when disruptions occur.

Both modes use Azure Traffic Manager's DNS-based routing capabilities. Routing decisions depend on endpoint health and the configured policy, with failover timing influenced by DNS caching and client behavior.

**Whether your application needs multiple active regions or a primary region with standby capacity, Geo-redundancy provides an integrated way to configure and manage regional traffic routing.**

## Simplify application deployments across regions

Maintaining consistent application versions across regions is an important part of operating resilient applications.

Geo-redundancy helps simplify this process by enabling supported application content and configuration to be synchronized from your primary web app to regional replicas.

Rather than coordinating every regional application deployment independently, you can deploy supported updates to your primary application and manage their synchronization across regional replicas.

The preview also introduces revision-management capabilities that help you:

- Inspect application revision and synchronization status across regions.
- Control when supported application revisions are synchronized.
- Validate application revisions in regional replicas.
- Retain a validated last-known-good revision for a replica where supported.

These capabilities give application teams greater visibility and control over regional application versions, helping reduce the complexity of coordinating deployments across multiple Azure regions.

Applications should still be validated in each region, including their dependencies and regional configuration. Changes made outside supported deployment workflows may require an explicit snapshot or synchronization action.

## Build resilience across your application architecture

Geo-redundancy simplifies **multi-region application hosting on Azure App Service**, but resilient applications also depend on the availability of their underlying services.

Databases, storage accounts, secrets, networking, external APIs, and other application dependencies must be designed and configured with appropriate regional resilience.

For example, an application replica may be healthy and available in another region, but it still needs access to the data and downstream services required to process requests.

Geo-redundancy does not automatically replicate databases, Azure Storage, Azure Key Vault, live runtime state, or external dependencies.

Customers remain responsible for designing and testing the resilience of these services, including data consistency, regional connectivity, and recovery behavior.

**Geo-redundancy simplifies the application hosting layer of your resilience architecture, allowing your team to focus on the broader application and data resilience strategy.**

## Get started with Geo-redundancy in public preview

The public preview of Geo-redundancy is initially available for eligible **Windows web apps running on Premium v3 and Premium v4 App Service plans** in supported multitenant Azure regions.

Getting started involves five steps:

1. **Choose your application and regions.** Review preview eligibility, supported configurations, and regional availability.
2. **Add a regional replica.** Configure Geo-redundancy for an eligible web app and select a supported Azure region.
3. **Configure traffic routing.** Choose Active or Passive mode and configure the appropriate regional weights or priorities.
4. **Synchronize and validate your application.** Verify supported application content, configuration, and revision status across regions.
5. **Test your resilience strategy.** Validate endpoint health, regional failover, recovery behavior, and the availability of application dependencies.

Before enabling the preview, review the [published support matrix for supported regions, application configurations, custom-domain requirements, and known limitations.](https://learn.microsoft.com/azure/app-service/overview-geo-redundancy)

### Pricing

Geo-redundancy introduces a per-enabled-application monthly charge in addition to the App Service compute charges associated with the primary application and regional replicas.

For current pricing and billing details, see [Azure App Service pricing](https://azure.microsoft.com/pricing/details/app-service/windows).

## Take the next step toward multi-region application resilience

Building regionally resilient applications shouldn't mean building and operating your own multi-region application deployment and traffic-management solution.

With Geo-redundancy in Azure App Service, we're making it simpler to extend applications across Azure regions, coordinate application revisions, and configure regional traffic routing and failover.

**The public preview is an opportunity to explore a simpler approach to multi-region application hosting, with more integrated management and greater control over regional application behavior.**

Ready to explore what's possible?

**[Explore Geo-redundancy in Azure App Service and get started with the public preview](https://aka.ms/georedundancyonappservice).**
