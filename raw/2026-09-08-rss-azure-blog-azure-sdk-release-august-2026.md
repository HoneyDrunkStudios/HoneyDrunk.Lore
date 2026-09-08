---
source: "https://devblogs.microsoft.com/azure-sdk/azure-sdk-release-august-2026/"
title: "Azure SDK Release (August 2026)"
author: "Justin Bettencourt"
date_published: "2026-09-04"
date_clipped: "2026-09-08"
category: "Azure & Cloud"
source_type: "rss"
---

# Azure SDK Release (August 2026)

Source: https://devblogs.microsoft.com/azure-sdk/azure-sdk-release-august-2026/

Thank you for your interest in the new Azure SDKs! We release new features, improvements, and bug fixes every month. Subscribe to our Azure SDK Blog RSS Feed to get notified when a new release is available.
You can find links to packages, code, and docs on our Azure SDK Releases page .
To restore a complete release record, this roundup also includes 49 initial stable and beta releases that were publicly available from package registries in July but weren’t listed in the July post because several release-data updates hadn’t merged. Public package availability, rather than release-data pull request status, determines inclusion.
Release highlights
Document Translation 2.0.0
Document Translation added support for the 2026-03-01 service API, including translation of text embedded in images for batch and single-document requests, custom translation model deployments, and expanded image scan reporting. The Java and Python 2.0.0 releases include breaking changes, while the new JavaScript package replaces the REST-level client with modeled DocumentTranslationClient and SingleDocumentTranslationClient APIs.
Storage – Blobs 12.30.0-beta.1
Azure Storage preview releases across .NET, Java, JavaScript, Python, Go, and C++ added support for service version 2026-10-06 . Blob libraries introduced Apache Arrow response support for listing operations, additional access-tier metadata, and responses that can include both MD5 and CRC64 hashes. File Share libraries added paged range-list APIs, and .NET Blob uploads now generate random block IDs to prevent collisions during concurrent uploads.
Azure AI Discovery 1.0.0
Azure AI Discovery reached its first stable release for Python and JavaScript. The libraries expose Workspace capabilities for conversations, investigations, tasks, and tools, plus Bookshelf knowledge-base lifecycle, indexing, and citation-aware search operations. The stable Python release also adds paged responses, storage mount protocol controls, and long-running cancellation while establishing a new compatibility baseline from the preview.
Initial stable releases
Client Library for .NET
Planetary Computer 1.0.0
Client Library for Java
Planetary Computer 1.0.0
Client Libraries for JavaScript
Azure AI Discovery 1.0.0
Document Translation 1.0.0
Core Process 1.0.0
Planetary Computer 1.0.0
Client Library for Python
Azure AI Discovery 1.0.0
Management Libraries for Go
Resource Management – Automation 1.0.0
Resource Management – Certificate Registration 1.0.0
Resource Management – Connected Cache 1.0.0
Resource Management – Data Boundaries 1.0.0
Resource Management – Domain Registration 1.0.0
Resource Management – Monitor Workspaces 1.0.0
Resource Management – SQL Virtual Machine 1.0.0
Management Library for Java
Resource Management – Connected Cache 1.0.0
Management Libraries for JavaScript
Resource Management – Alert Processing Rules 1.0.0
Resource Management – Connected Cache 1.0.0
Resource Management – Cost Management 1.0.0
Resource Management – Data Boundaries 1.0.0
Resource Management – Discovery 1.0.0
Resource Management – Edge Order 1.0.0
Resource Management – Guest Configuration 1.0.0
Resource Management – Kubernetes Configuration – Flux Configurations 1.0.0
Resource Management – Marketplace 1.0.0
Resource Management – Monitor Workspaces 1.0.0
Resource Management – Prometheus Rule Groups 1.0.0
Resource Management – ProviderHub 1.0.0
Resource Management – Red Hat OpenShift 1.0.0
Resource Management – Resources Deployments 1.0.0
Management Libraries for Python
Resource Management – Connected Cache 1.0.0
Resource Management – Discovery 1.0.0
Resource Management – Guest Configuration 1.0.0
Resource Management – Resource Deployments 1.0.0
Resource Management – Resource Subscriptions 1.0.0
Resource Management – SQL Virtual Machine 1.0.0
Initial beta releases
Management Libraries for .NET
Provisioning – Attestation 1.0.0-beta.1
Provisioning – Bot Service 1.0.0-beta.1
Provisioning – Domain Registration 1.0.0-beta.1
Provisioning – Durable Task 1.0.0-beta.1
Provisioning – IoT Hub 1.0.0-beta.1
Provisioning – Recovery Services 1.0.0-beta.1
Provisioning – Recovery Services Backup 1.0.0-beta.1
Provisioning – Service Fabric 1.0.0-beta.1
Provisioning – Service Fabric Managed Clusters 1.0.0-beta.1
Provisioning – Standby Pool 1.0.0-beta.1
Provisioning – Traffic Manager 1.0.0-beta.1
Resource Management – Billing Trust 1.0.0-beta.1
Resource Management – Container Service Prepared Image Spec 1.0.0-beta.1
Resource Management – Discovery 1.0.0-beta.1
Resource Management – Enclave 1.0.0-beta.1
Resource Management – Resources Bicep 1.0.0-beta.1
Resource Management – Resources Deployments 1.0.0-beta.1
Management Libraries for Go
Resource Management – Billing Trust 0.1.0
Resource Management – Commvault ContentStore 0.1.0
Resource Management – Container Service AI Manager 0.1.0
Resource Management – Container Service Prepared Image Spec 0.1.0
Resource Management – Discovery 0.1.0
Resource Management – Enclave 0.1.0
Management Libraries for Java
Resource Management – Billing Trust 1.0.0-beta.1
Resource Management – Compute Bulk Actions 1.0.0-beta.1
Resource Management – Container Service AI Manager 1.0.0-beta.1
Resource Management – Container Service Prepared Image Spec 1.0.0-beta.1
Resource Management – Discovery 1.0.0-beta.1
Resource Management – Enclave 1.0.0-beta.1
Management Libraries for JavaScript
Resource Management – Billing Trust 1.0.0-beta.1
Resource Management – Commvault ContentStore 1.0.0-beta.1
Resource Management – Compute Bulk Actions 1.0.0-beta.1
Resource Management – Container Service AI Manager 1.0.0-beta.1
Resource Management – Container Service Prepared Image Spec 1.0.0-beta.1
Resource Management – Enclave 1.0.0-beta.1
Management Libraries for Python
Resource Management – Compute Bulk Actions 1.0.0b1
Resource Management – Container Service AI Manager 1.0.0b1
Resource Management – Container Service Prepared Image Spec 1.0.0b1
Resource Management – Enclave 1.0.0b1
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
