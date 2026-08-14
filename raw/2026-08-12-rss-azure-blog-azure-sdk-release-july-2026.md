---
source: "https://devblogs.microsoft.com/azure-sdk/azure-sdk-release-july-2026/"
title: "Azure SDK Release (July 2026)"
author: "Azure Blog"
date_published: "2026-07-29"
date_clipped: "2026-08-12"
category: "Azure & Cloud"
source_type: "rss"
---

# Azure SDK Release (July 2026)

Source: https://devblogs.microsoft.com/azure-sdk/azure-sdk-release-july-2026/

Thank you for your interest in the new Azure SDKs! We release new features, improvements, and bug fixes every month. Subscribe to our Azure SDK Blog RSS Feed to get notified when a new release is available.
You can find links to packages, code, and docs on our Azure SDK Releases page .
Release highlights
The Azure SDK for Rust adds Storage Shared Access Signature support
Following the Azure SDK for Rust reaching general availability in May and completing its 1.0.0 foundation in June, this month brings the first client capability built on top of that stack: azure_storage_sas (0.1.0) . The new crate is a user-delegation Shared Access Signature (SAS) builder for Azure Storage, letting Rust developers grant scoped, time-limited access to Blob, Queue, and other Storage resources without sharing account keys.
App Service domain and certificate management reach general availability for Python
Two paired management libraries hit their first stable release this month: Domain Registration 1.0.0 and Certificate Registration 1.0.0 . Together they give Python developers a supported, stable client for purchasing and managing App Service domains and provisioning and managing App Service certificates, so custom-domain and TLS setup for web apps can be fully automated in code.
Azure Resource Health management reaches general availability for Python
The Resource Health 1.0.0 management library is now generally available. It gives Python developers a stable client for querying the availability and health status of Azure resources programmatically, which makes it straightforward to build automated health monitoring, alerting, and reporting on top of Azure Resource Health.
Azure Data Boundaries management reaches general availability for Python
The Data Boundaries 1.0.0 management library reaches its first stable release. It lets Python developers configure and manage tenant-level data boundary settings programmatically, supporting data-residency and compliance requirements such as the EU Data Boundary.
Initial stable releases
Management Libraries for Python
Resource Management – Certificate Registration 1.0.0
Resource Management – Data Boundaries 1.0.0
Resource Management – Domain Registration 1.0.0
Resource Management – Kubernetes Configuration Flux Configurations 1.0.0
Resource Management – Monitor Workspaces 1.0.0
Resource Management – Network Function 1.0.0
Resource Management – Resource Health 1.0.0
Initial beta releases
Management Library for Java
Resource Management – Resilience Management 1.0.0-beta.1
Management Libraries for Python
Resource Management – Alert Processing Rules 1.0.0b1
Resource Management – Billing Trust 1.0.0b1
Resource Management – Commvault Content Store 1.0.0b1
Resource Management – Domain Services 1.0.0b1
Resource Management – Marketplace 1.0.0b1
Resource Management – Power Platform 1.0.0b1
Resource Management – Program Enrollment 1.0.0b1
Resource Management – Prometheus Rule Groups 1.0.0b1
Resource Management – Provider Hub 1.0.0b1
Resource Management – Resilience Management 1.0.0b1
Client Library for Rust
Azure Storage SAS 0.1.0
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
