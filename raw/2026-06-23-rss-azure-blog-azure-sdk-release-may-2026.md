---
source: "https://devblogs.microsoft.com/azure-sdk/azure-sdk-release-may-2026/"
title: "Azure SDK Release (May 2026)"
author: "Azure Blog"
date_published: "Mon, 22 Jun 2026 23:37:37 +0000"
date_clipped: "2026-06-23"
category: "Azure & Cloud"
source_type: "rss"
---

# Azure SDK Release (May 2026)

Source: https://devblogs.microsoft.com/azure-sdk/azure-sdk-release-may-2026/

Thank you for your interest in the new Azure SDKs! We release new features, improvements, and bug fixes every month. Subscribe to our Azure SDK Blog RSS Feed to get notified when a new release is available.
You can find links to packages, code, and docs on our Azure SDK Releases page .
Release highlights 
The Azure SDK for Rust reaches general availability 
The Azure SDK for Rust is now stable. This month’s GA delivers production-ready 1.0.0 crates for Core, Identity, Key Vault (Secrets, Keys, and Certificates), and Storage (Blobs and Queues), built on the same design patterns you already know from the .NET, Java, JavaScript, Python, Go, and C++ SDKs. For the full story, see From beta to stable: Announcing the Azure SDK for Rust .
Azure AI Search adds agentic retrieval with knowledge bases 
The .NET Azure AI Search library (12.0.0) and Python azure-search-documents (12.0.0) introduce knowledge bases and a new KnowledgeBaseRetrievalClient for agentic retrieval. You can now define knowledge sources backed by Azure Blob storage, a search index, OneLake, or the web, then run retrieval requests against a knowledge base, all on the new 2026-04-01 service version. The JavaScript @azure/search-documents (13.0.0) release adds a debug property to inspect non-semantic search queries and an oversampling option for vector search.
New Azure AI Agent Server libraries enter preview 
A new family of preview libraries for hosting agents arrived this month, led by .NET Azure.AI.AgentServer.Core (1.0.0-beta.23) and Python azure-ai-agentserver-core (2.0.0b3) . .NET also ships companion Invocations and Responses packages, while Python ships a companion Responses package this month. They provide an AgentServerHost hosting model with built-in health probes, graceful shutdown, request-ID middleware, and a centralized PlatformHeaders set of HTTP header constants shared across the packages. As preview releases, these libraries are still changing quickly; the latest .NET beta, for example, consolidated six separate setup calls into a single AddAgentServerCore() / UseAgentServerCore() pair.
Azure Batch client library reaches general availability for .NET 
The .NET Azure.Compute.Batch (1.0.0) library is now generally available. The GA release includes breaking changes carried over from beta, including the removal of AuthenticationTokenSettings and BatchAccessScope and a number of property renames (such as BatchJobScheduleConfiguration.DoNotRunUntil to DoNotRunBefore ). Cross-language Batch modernization continued as well with JavaScript @azure/batch (13.0.0) and Python azure-batch (15.1.0) , which ship their own type and option renames.
Initial stable releases 
Client Library for .NET 
Compute Batch 1.0.0 
Management Libraries for .NET 
Resource Management – Compute Limit 1.0.0 
Resource Management – Customer Insights 1.0.0 
Resource Management – Dev Spaces 1.0.0 
Resource Management – DevOps Infrastructure 1.0.0 
Resource Management – File Shares 1.0.0 
Resource Management – Informatica Data Management 1.0.0 
Resource Management – Kubernetes Configuration Extensions 1.0.0 
Resource Management – Network Function 1.0.0 
Resource Management – Planetary Computer 1.0.0 
Resource Management – Power BI Dedicated 1.0.0 
Resource Management – ScVmm 1.0.0 
Resource Management – Trusted Signing 1.0.0 
Resource Management – Weights and Biases 1.0.0 
Resource Management – Workloads SAP Virtual Instance 1.0.0 
Client Library for JavaScript 
OpenTelemetry Instrumentation 1.0.0 
Management Libraries for JavaScript 
Resource Management – Compute Limit 1.0.0 
Resource Management – Kubernetes Configuration Extensions 1.0.0 
Resource Management – Planetary Computer 1.0.0 
Management Libraries for Python 
Resource Management – Compute Limit 1.0.0 
Resource Management – Kubernetes Configuration Extensions 1.0.0 
Resource Management – Planetary Computer 1.0.0 
Management Libraries for Go 
Resource Management – Compute Limit 1.0.0 
Resource Management – Kubernetes Configuration Extensions 1.0.0 
Resource Management – Planetary Computer 1.0.0 
Client Library for Rust 
Azure Core 1.0.0 
Azure Core AMQP 1.0.0 
Azure Core OpenTelemetry 1.0.0 
Azure Identity 1.0.0 
Azure Storage Blob 1.0.0 
Azure Storage Queue 1.0.0 
Azure Key Vault Secrets 1.0.0 
Azure Key Vault Keys 1.0.0 
Azure Key Vault Certificates 1.0.0 
Initial beta releases 
Client Libraries for .NET 
Agent Server – Invocations 1.0.0-beta.1 
Agent Server – Responses 1.0.0-beta.1 
PostgreSQL – Authentication 1.0.0-beta.1 
Provisioning – Container Instance 1.0.0-beta.1 
Provisioning – Logic 1.0.0-beta.1 
Provisioning – Resource Graph 1.0.0-beta.1 
Provisioning – Service Networking 1.0.0-beta.1 
Management Library for .NET 
Resource Management – Relationships 1.0.0-beta.1 
Client Library for JavaScript 
PostgreSQL – Authentication 1.0.0-beta.1 
Management Libraries for JavaScript 
Resource Management – Alert Processing Rules 1.0.0-beta.1 
Resource Management – Alert Rule Recommendations 1.0.0-beta.1 
Resource Management – Alerts Management 1.0.0-beta.1 
Resource Management – File Shares 1.0.0-beta.1 
Resource Management – Monitor SLIs 1.0.0-beta.1 
Resource Management – Preview Alert Rule 1.0.0-beta.1 
Resource Management – Prometheus Rule Groups 1.0.0-beta.1 
Resource Management – Relationships 1.0.0-beta.1 
Resource Management – Service Groups 1.0.0-beta.1 
Resource Management – Tenant Activity Log Alerts 1.0.0-beta.1 
Client Library for Python 
Agent Server – Responses 1.0.0b1 
Management Libraries for Python 
Resource Management – App Network 1.0.0b1 
Resource Management – Certificate Registration 1.0.0b1 
Resource Management – Domain Registration 1.0.0b1 
Resource Management – HorizonDB 1.0.0b1 
Resource Management – Monitor SLIs 1.0.0b1 
Resource Management – Relationships 1.0.0b1 
Resource Management – Service Groups 1.0.0b1 
Management Libraries for Go 
Resource Management – Relationships 0.1.0 
Resource Management – Service Groups 0.1.0 
Resource Management – Monitor SLIs 0.1.0 
Release notes 
All languages 
.NET 
Java 
JavaScript/TypeScript 
Python 
Go 
Rust 
C++ 
Embedded C 
Android 
iOS
