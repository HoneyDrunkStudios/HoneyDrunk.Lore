---
source: "https://devblogs.microsoft.com/azure-sdk/from-beta-to-stable-announcing-the-azure-sdk-for-rust-ga/"
title: "From beta to stable: Announcing the Azure SDK for Rust 🎉🦀"
author: "Azure Blog"
date_published: "Thu, 14 May 2026 15:46:19 +0000"
date_clipped: "2026-05-16"
category: "Azure & Cloud"
source_type: "rss"
---

# From beta to stable: Announcing the Azure SDK for Rust 🎉🦀

Source: https://devblogs.microsoft.com/azure-sdk/from-beta-to-stable-announcing-the-azure-sdk-for-rust-ga/

Picture a Rust service that signs in with Microsoft Entra ID, pulls a signing key from Key Vault, picks up work items off a Storage Queue, and lands the results in Blob Storage. Every piece of that stack is now stable. 🚀
The Azure SDK for Rust 🦀 is stable . What we shipped as a beta is now a production-ready SDK with stable APIs, semver guarantees, and a surface area you can build on today.
Why Rust on Azure? 
A few reasons teams keep telling us they picked Rust:
⚡ Small binaries, low memory, fast cold starts. Great fit for containers and the edge, where every millisecond and megabyte matters. 
🛡️ Whole categories of bugs (null derefs, data races, use-after-free) caught at compile time instead of at 3:00 AM. 
🔌 Native async on top of Tokio , with predictable performance for high-throughput workloads like event processing and streaming. 
🌐 The same design patterns you know from the .NET, Java, JavaScript, Python, Go, and C++ SDKs . Different language, familiar shape. 
What’s stable today 
Six service libraries and the core infrastructure that powers them: Core , Identity 🔐, Key Vault (Secrets, Keys, Certificates), and Storage (Blobs, Queues). All of them are crates you’ve already been using throughout beta. Now they’re stable.
Service 
Crate 📦 
Docs 
Source Code 
Core 
azure_core 
Reference 
GitHub 
Identity 
azure_identity 
Reference 
GitHub 
Key Vault Secrets 
azure_security_keyvault_secrets 
Reference 
GitHub 
Key Vault Keys 
azure_security_keyvault_keys 
Reference 
GitHub 
Key Vault Certificates 
azure_security_keyvault_certificates 
Reference 
GitHub 
Storage Blobs 
azure_storage_blob 
Reference 
GitHub 
Storage Queues 
azure_storage_queue 
Reference 
GitHub 
What’s new since beta 
Service coverage is the headline. But a lot changed under the hood. We spent the past year hardening the SDK on real-world usage and community feedback:
Stabilized API surface. Every public type, trait, and function got a pass against the Azure SDK guidelines . Breaking changes now follow semver . 
Unified core primitives. A redesigned Pager that yields items by default. A Poller you can just .await for long-running operations. One ManagedIdentityCredential that works across every Azure hosting environment. A new DeveloperToolsCredential that streamlines local development by falling through your installed dev tools (Azure CLI, Azure Developer CLI) until one returns a token. 
Production-grade resilience. Automatic retries on transient failures. Challenge-based authentication so sovereign and private clouds just work. 
First-class observability. ⚡ Distributed tracing through azure_core_opentelemetry using #[tracing::*] macros, plus an HTTP logging policy that sanitizes secrets by default. 
Pluggable async runtime. Tokio out of the box. Bring your own with set_async_runtime() . 
Get started 🚀 
A few lines in your terminal and you’re off:
1. Add dependencies 
cargo add azure_identity azure_storage_blob futures tokio --features tokio/full 
2. Authenticate and list some blobs 
DeveloperToolsCredential is the credential you reach for during local development. It falls through your installed dev tools (Azure CLI, Azure Developer CLI) until one returns a token. For workloads running in Azure, swap it for ManagedIdentityCredential . The rest of the code stays the same.
use azure_identity::DeveloperToolsCredential;
use azure_storage_blob::BlobContainerClient;
use futures::TryStreamExt;
#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
// Locally, DeveloperToolsCredential falls through your dev tools (Azure CLI, Azure Developer CLI).
// In Azure, swap this for ManagedIdentityCredential.
let credential = DeveloperToolsCredential::new(None)?;
let container = BlobContainerClient::new(
"https://<your-storage-account>.blob.core.windows.net/",
"my-container",
Some(credential),
None,
)?;
let mut pager = container.list_blobs(None)?;
while let Some(blob) = pager.try_next().await? {
println!("📦 {}", blob.name.unwrap_or_default());
}
Ok(())
} 
A few things worth noticing:
Pager yields blob items directly. try_next().await? walks the whole result set without any manual page bookkeeping. Need the raw pages instead? Call .into_pages() on the pager. 
Errors propagate with ? . No surprise panics in your hot path. 
Same credential type plugs into every other stable crate. No per-service auth boilerplate. 
Want more? Each library has an examples directory in its project folder on GitHub , with more cross-library samples in the root /samples folder.
Documentation 📚 
Get productive fast:
Documentation . Learn about the SDK architecture, design patterns, and best practices. 
Azure SDK for Rust on GitHub . Source code, examples, and contributing guide. 
What’s coming next 
Going stable is a milestone, not a finish line. A few things we’re working on:
📨 Event Hubs. azure_messaging_eventhubs and azure_messaging_eventhubs_checkpointstore_blob are close. They won’t ship in this stable wave, but they’re a top priority for the next one. 
🗄️ Azure Cosmos DB. azure_data_cosmos is in active development and is another planned stable release, expected in 2026. 
📡 More service crates. Coverage keeps growing. The fastest way to nudge the roadmap is to upvote 👍 the services you actually need. 
🔭 Continued investments in observability, runtime flexibility, and ergonomics across the existing stable crates. 
Don’t see your favorite service? Open an issue . We read every one.
Join the conversation 🤝 
Community feedback shaped a huge amount of this SDK. Keep it coming:
⭐ Star the repo: Azure/azure-sdk-for-rust 
🐛 File a bug: GitHub Issues 
💡 Vote on open feature requests 
🗣️ Weigh in on design discussions 
🆕 Tell us which Azure service should be next by opening an issue 
Now go build something. We can’t wait to see it. 🚀
