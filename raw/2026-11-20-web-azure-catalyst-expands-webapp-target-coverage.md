---
source: "https://techcommunity.microsoft.com/blog/azuremigrationblog/azure-catalyst-expands-webapp-target-coverage/4574689"
title: "Azure Catalyst expands Webapp target coverage"
author: "Nikita Bajaj"
date_published: "2026-11-19"
date_clipped: "2026-11-20"
category: "Azure & Cloud"
source_type: "web"
---

# Azure Catalyst expands Webapp target coverage

## Assess your webapps for Azure Container Apps and Managed Instance on Azure App Service

### What's new

We are excited to announce **expanded target coverage for webapps** with two new targets: **Azure Container Apps**** **and **Managed Instance on Azure App Service****.** Webapps can now be assessed across multiple Azure targets - Azure App Service Code, Azure App Service Containers, Azure App Service Managed instance, Azure Container Apps (ACA) and Azure Kubernetes Service (AKS). You can determine readiness status for these apps, code changes required to modernize, effort estimate, target SKU size and Azure costs. Comparing these services side by side helps you quickly choose the one that best fits your organization's requirements.

**Azure Container Apps** is a managed, serverless container platform for webapps, APIs and microservices. It provides HTTP and event-driven autoscaling (including scale to zero for supported configurations), managed ingress, revisions with traffic splitting, and connectivity to databases, storage and messaging services, without managing servers or the underlying container orchestration layer.

**Managed Instance on Azure App Service** is a hosting option for Windows webapps that need operating system customization. You can move legacy .NET Framework apps that depend on Windows (COM components, the registry, the Global Assembly Cache, Windows services, mapped drives) to fully managed App Service often with minimal configuration and code changes.

### How it works

- Create an Azure Catalyst project and discover your Servers, Webapps, Databases and auto-discover Applications. Discovery builds an inventory of Webapps, the Servers that host them, Application they are part of and their dependencies.
- Create an Application or Webapp assessment. Select the Applications or Webapps in scope and include Azure Container Apps and Managed Instance on Azure App Service among the targets. Configure the target region, sizing preferences and pricing options, then run the assessment.
- Review readiness, sizing and cost. Each target has its own tab in the assessment report. For every app you see a readiness status, the migration issues and warnings behind it with recommended remediation, the recommended plan and an estimated monthly cost.

- Enhance your configuration assessment by assessing application code through GitHub Copilot Modernization agent to determine code changes required to modernize.
- Generate the target design according to Azure CAF and WAF principles.
- Plan migration waves to group assessed apps into migration batches, review sequencing, dependencies and risks with application owners, and commit the approved plan.
- Migrate and modernize. Apply the recommended code changes, validate builds and deploy to the selected target.

### Learn more

[Create an application assessment](https://learn.microsoft.com/en-us/azure/migrate/create-application-assessment?view=migrate)[Add Code Insights by Using GitHub Copilot Modernization](https://learn.microsoft.com/en-us/azure/migrate/add-copilot-code-insights?view=migrate#run-at-scale-code-assessments-by-using-the-github-copilot-modernize-cli)[Web App Migration and Modernization](https://learn.microsoft.com/en-us/azure/migrate/web-app-migration-modernization?view=migrate)

[Nikita_Bajaj](https://techcommunity.microsoft.com/users/nikita_bajaj/1441355)

[Azure Migration and Modernization Blog](https://techcommunity.microsoft.com/category/azure/blog/azuremigrationblog)
