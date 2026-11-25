---
source: "https://techcommunity.microsoft.com/t5/apps-on-azure-blog/enable-and-manage-gateway-api-on-azure-portal/ba-p/4574567"
title: "Enable and manage Gateway API on Azure Portal"
author: "mjranda"
date_published: "2026-11-18"
date_clipped: "2026-11-25"
category: "Azure & Cloud"
source_type: "rss"
canonical_url: "https://techcommunity.microsoft.com/blog/appsonazureblog/enable-and-manage-gateway-api-on-azure-portal/4574567"
---

# Enable and manage Gateway API on Azure Portal

Gateway API is the long-term Kubernetes standard for ingress and L7 traffic management. Compared with the traditional Ingress resource, Gateway API separates infrastructure entry points from routing configuration, giving platform and application teams clearer ownership boundaries and a more extensible model for managing application traffic.

 Customers can now discover and configure Gateway API-based ingress solutions, view Gateway and HTTPRoute resources and better understand the ingress configuration of an AKS cluster without leaving the Portal.

## A new Ingress profile for AKS

AKS offers two options for Gateway API implementations:

- [**Application Routing with Gateway API**](https://learn.microsoft.com/en-us/azure/aks/app-routing-gateway-api?pivots=azure-portal), an AKS-native path for cluster-hosted routing.
- [**Application Gateway for Containers**](https://learn.microsoft.com/en-us/azure/application-gateway/for-containers/overview?toc=/azure/aks/toc.json&bc=/azure/aks/breadcrumb/toc.json), an Azure application-layer load balancing and traffic-management solution managed through the ALB Controller.

To enable either Gateway controller, you can:

1. Navigate to an AKS cluster in the Azure portal.
2. Select **Networking**.
3. Select **Ingress profile**.
4. Select **Manage** under **Application Routing with Gateway API** or **Application Gateway for Containers**
5. Select **Enable.**

The portal will install the Managed Gateway API add-on as a prerequisite to using either Gateway API implementation, if not already installed. Once enablement is complete, you can return to the **Ingress profile** on any cluster to easily understand which controller(s) are currently enabled and disable if desired.

## Gateways and HTTPRoutes are now visible under Kubernetes resources

The AKS Kubernetes resources experience also now surfaces **Gateways** and **HTTPRoutes**, allowing customers to inspect the Gateway API resources running on their cluster directly from the Portal.

You can view and manage Gateway and HTTPRoute resources directly from Portal and easily grasp additional details per-resource such as listeners and backends, respectively.

The following shows an overview of a sample Gateway resource in Portal.

This makes the Portal useful not just for enabling Gateway API, but for understanding interactions between the resulting Gateway and Route resources.

## Get started

To try Application Routing with Gateway API, see Azure Kubernetes Service (AKS) Application Routing Add-On with the Kubernetes Gateway API. [[Azure Kube...soft Learn | Learn.Microsoft.com]](https://learn.microsoft.com/en-us/azure/aks/app-routing-gateway-api)

To use Application Gateway for Containers, see Quickstart: Deploy Application Gateway for Containers ALB Controller - AKS Add-on. [[Quickstart...soft Learn | Learn.Microsoft.com]](https://learn.microsoft.com/en-us/azure/application-gateway/for-containers/quickstart-deploy-application-gateway-for-containers-alb-controller-addon)

Published Nov 18, 2026

Version 1.0

[azure kubernetes service](https://techcommunity.microsoft.com/tag/azure%20kubernetes%20service?nodeId=board%3AAppsonAzureBlog)

[![mjranda's avatar](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/avatars/default/avatar-5.svg?image-dimensions=50x50)](https://techcommunity.microsoft.com/users/mjranda/2112868)

[mjranda](https://techcommunity.microsoft.com/users/mjranda/2112868)

![Icon for Microsoft rank](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/cmstNC05WEo0blc?image-dimensions=100x16&constrain-image=true)Microsoft

Joined October 30, 2023

[View Profile](https://techcommunity.microsoft.com/users/mjranda/2112868)

[Apps on Azure Blog](https://techcommunity.microsoft.com/category/azure/blog/appsonazureblog) 

Follow this blog board to get notified when there's new activity
