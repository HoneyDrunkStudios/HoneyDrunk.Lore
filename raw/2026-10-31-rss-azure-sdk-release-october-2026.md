---
source: "https://devblogs.microsoft.com/azure-sdk/azure-sdk-release-october-2026"
title: "Azure SDK Release (October 2026)"
author: "Sandeep Sen"
date_published: "2026-10-28"
date_clipped: "2026-10-31"
category: "Azure & Cloud"
source_type: "rss"
---

# Azure SDK Release (October 2026)

Thank you for your interest in the new Azure SDKs! We release new features, improvements, and bug fixes every month. Subscribe to our [Azure SDK Blog RSS Feed](https://devblogs.microsoft.com/azure-sdk/feed/) to get notified when a new release is available.

You can find links to packages, code, and docs on our [Azure SDK Releases page](https://aka.ms/azsdk/releases).

## Release highlights

### [Azure Core 1.63.0 for .NET](https://www.nuget.org/packages/Azure.Core/1.63.0)

Azure Core adds mTLS proof-of-possession support for client certificate authentication and the managed identity federated identity flow used by configured credentials. It also fixes delays in `DefaultAzureCredential` when the Instance Metadata Service (IMDS) is unavailable and prevents unavailable managed identity sources from prematurely aborting the credential chain. If you use the experimental managed identity proof-of-possession option, replace `DisableMtlsProofOfPossession = true` with `EnableMtlsProofOfPossession = false` to continue forcing bearer authentication.

### [Identity 1.26.0 for Python](https://pypi.org/project/azure-identity/1.26.0/)

`ManagedIdentityCredential` now supports user-assigned managed identities on Azure Arc-enabled servers, selectable by client ID, object ID, or resource ID. Token responses that don’t confirm the requested identity are rejected. This release also fixes synchronous Service Fabric managed identity authentication with MSAL 1.39.0 and later, and a shared-token-cache issue where `AuthorizationCodeCredential` and the asynchronous `OnBehalfOfCredential` could return a cached token for another account. [Identity 1.18.7 for Java](https://central.sonatype.com/artifact/com.azure/azure-identity/1.18.7) adds Azure Arc user-assigned managed identity support to both `ManagedIdentityCredential` and `DefaultAzureCredential`, alongside fixes for native-image compatibility and IMDS discovery timeouts.

### [Cosmos DB 1.0.0 for Rust](https://crates.io/crates/azure_data_cosmos/1.0.0)

The Cosmos DB library for Rust reaches its first stable release alongside the Cosmos DB Client Driver and SDK Macros crates. When upgrading from the preview, rename the `preview_dtx`, `preview_patch`, and `preview_opentelemetry` feature flags to their `unstable_` equivalents, and replace `CosmosCredential::MasterKey` with `CosmosCredential::AccountKey`. The release also changes the `User-Agent` format and maps specific terminal service errors to synthetic 503 errors, retaining the original wire error in `source()`.

### Initial stable releases

- **Management Library for .NET**
  - [Resource Management – Napster Omni Agent API 1.0.0](https://www.nuget.org/packages/Azure.ResourceManager.NapsterOmniagentApi/1.0.0)
- **Management Libraries for Java**
  - [Resource Management – Relationships 1.0.0](https://central.sonatype.com/artifact/com.azure.resourcemanager/azure-resourcemanager-relationships/1.0.0)
  - [Resource Management – Service Groups 1.0.0](https://central.sonatype.com/artifact/com.azure.resourcemanager/azure-resourcemanager-servicegroups/1.0.0)
  - [Resource Management – Template Specs 1.0.0](https://central.sonatype.com/artifact/com.azure.resourcemanager/azure-resourcemanager-resources-templatespecs/1.0.0)
- **Management Libraries for JavaScript**
  - [Resource Management – Relationships 1.0.0](https://www.npmjs.com/package/@azure/arm-relationships/v/1.0.0)
  - [Resource Management – Service Groups 1.0.0](https://www.npmjs.com/package/@azure/arm-servicegroups/v/1.0.0)
  - [Resource Management – Resilience Management 1.0.0](https://www.npmjs.com/package/@azure/arm-resiliencemanagement/v/1.0.0)
- **Management Libraries for Python**
  - [Resource Management – Resource-Policy 1.0.0](https://pypi.org/project/azure-mgmt-resource-policy/1.0.0/)
  - [Resource Management – Relationships 1.0.0](https://pypi.org/project/azure-mgmt-relationships/1.0.0/)
  - [Resource Management – Features 1.0.0](https://pypi.org/project/azure-mgmt-resource-features/1.0.0/)
  - [Resource Management – Locks 1.0.0](https://pypi.org/project/azure-mgmt-resource-locks/1.0.0/)
  - [Resource Management – Template Specs 1.0.0](https://pypi.org/project/azure-mgmt-resource-templatespecs/1.0.0/)
- **Management Libraries for Go**
  - [Resource Management – Relationships 1.0.0](https://pkg.go.dev/github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/relationships/armrelationships@v1.0.0)
  - [Resource Management – Service Groups 1.0.0](https://pkg.go.dev/github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/servicegroups/armservicegroups@v1.0.0)
  - [Resource Management – Resilience Management 1.0.0](https://pkg.go.dev/github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/resiliencemanagement/armresiliencemanagement@v1.0.0)
- **Client Libraries for Rust**
  - [Cosmos DB 1.0.0](https://crates.io/crates/azure_data_cosmos/1.0.0)
  - [Cosmos DB Client Driver 1.0.0](https://crates.io/crates/azure_data_cosmos_driver/1.0.0)
  - [Cosmos DB SDK Macros 1.0.0](https://crates.io/crates/azure_data_cosmos_macros/1.0.0)

### Initial beta releases

- **Client Libraries for .NET**
  - [Web PubSub Chat 1.0.0-beta.1](https://www.nuget.org/packages/Azure.Messaging.WebPubSub.Chat/1.0.0-beta.1)
  - [Provisioning – Databricks 1.0.0-beta.1](https://www.nuget.org/packages/Azure.Provisioning.Databricks/1.0.0-beta.1)
  - [Azure Data AI 1.0.0-beta.1](https://www.nuget.org/packages/Azure.Data.AI/1.0.0-beta.1)
  - [AI Agent Server – Optimization 1.0.0-beta.1](https://www.nuget.org/packages/Azure.AI.AgentServer.Optimization/1.0.0-beta.1)
  - [Provisioning – Fabric 1.0.0-beta.1](https://www.nuget.org/packages/Azure.Provisioning.Fabric/1.0.0-beta.1)
  - [Provisioning – Verified ID 1.0.0-beta.1](https://www.nuget.org/packages/Azure.Provisioning.VerifiedId/1.0.0-beta.1)
- **Management Libraries for Java**
  - [Resource Management – Platform Validation 1.0.0-beta.1](https://central.sonatype.com/artifact/com.azure.resourcemanager/azure-resourcemanager-platformvalidation/1.0.0-beta.1)
  - [Resource Management – Compute Workload Manager 1.0.0-beta.1](https://central.sonatype.com/artifact/com.azure.resourcemanager/azure-resourcemanager-compute-workloadmanager/1.0.0-beta.1)
- **Client Libraries for JavaScript**
  - [Azure AI Content Safety 1.0.0-beta.1](https://www.npmjs.com/package/@azure/ai-content-safety/v/1.0.0-beta.1)
  - [Provisioning 1.0.0-beta.1](https://www.npmjs.com/package/@azure/provisioning-core/v/1.0.0-beta.1)
  - [Provisioning – Key Vault 1.0.0-beta.1](https://www.npmjs.com/package/@azure/provisioning-keyvault/v/1.0.0-beta.1)
- **Management Libraries for JavaScript**
  - [Resource Management – Compute Workload Manager 1.0.0-beta.1](https://www.npmjs.com/package/@azure/arm-computeworkloadmanager/v/1.0.0-beta.1)
  - [Resource Management – Platform Validation 1.0.0-beta.1](https://www.npmjs.com/package/@azure/arm-platformvalidation/v/1.0.0-beta.1)
  - [Resource Management – Secrets Store Extension 1.0.0-beta.1](https://www.npmjs.com/package/@azure/arm-secretsstoreextension/v/1.0.0-beta.1)
- **Client Libraries for Python**
  - [Azure AI Fine-Tuning Sessions 1.0.0b1](https://pypi.org/project/azure-ai-finetuningsessions/1.0.0b1/)
  - [Azure Data AI 1.0.0b1](https://pypi.org/project/azure-data-ai/1.0.0b1/)
  - [Web PubSub Chat 1.0.0b1](https://pypi.org/project/azure-messaging-webpubsubchatservice/1.0.0b1/)
- **Management Libraries for Python**
  - [Resource Management – Platform Validation 1.0.0b1](https://pypi.org/project/azure-mgmt-platformvalidation/1.0.0b1/)
  - [Resource Management – Compute Workload Manager 1.0.0b1](https://pypi.org/project/azure-mgmt-computeworkloadmanager/1.0.0b1/)
- **Client Library for Go**
  - [azure/sdk/storage/internal 0.1.0](https://pkg.go.dev/github.com/Azure/azure-sdk-for-go/sdk/storage/internal@v0.1.0)
- **Management Library for Go**
  - [Resource Management – Platform Validation 0.1.0](https://pkg.go.dev/github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/platformvalidation/armplatformvalidation@v0.1.0)
- **Client Libraries for Rust**
  - [Cosmos DB Client Driver 1.0.0-beta.1](https://crates.io/crates/azure_data_cosmos_driver/1.0.0-beta.1)
  - [Cosmos DB SDK Macros 1.0.0-beta.1](https://crates.io/crates/azure_data_cosmos_macros/1.0.0-beta.1)
  - [Cosmos DB 1.0.0-beta.1](https://crates.io/crates/azure_data_cosmos/1.0.0-beta.1)

## Release notes

- [All languages](https://azure.github.io/azure-sdk/releases/2026-10/index.html)
- [.NET](https://azure.github.io/azure-sdk/releases/2026-10/dotnet.html)
- [Java](https://azure.github.io/azure-sdk/releases/2026-10/java.html)
- [JavaScript/TypeScript](https://azure.github.io/azure-sdk/releases/2026-10/js.html)
- [Python](https://azure.github.io/azure-sdk/releases/2026-10/python.html)
- [Go](https://azure.github.io/azure-sdk/releases/2026-10/go.html)
- [Rust](https://azure.github.io/azure-sdk/releases/2026-10/rust.html)
- [C++](https://azure.github.io/azure-sdk/releases/2026-10/cpp.html)
