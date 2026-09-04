---
source: "https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-august-2026/"
title: "Azure Developer CLI (azd) – August 2026"
author: "Kristen Womack, Jeffrey C."
date_published: "2026-08-27"
date_clipped: "2026-09-04"
category: "Azure & Cloud"
source_type: "rss"
---

# Azure Developer CLI (azd) – August 2026

Source: https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-august-2026/

Welcome to the August 2026 edition of the Azure Developer CLI ( azd ) release blog. This post covers releases 1.30.0 , 1.31.0 , 1.31.1 , 1.31.2 , and 1.32.0 . To share your feedback and questions, join the August release discussion on GitHub .
Highlights:
The azd extension framework is generally available .
Azure Functions services can deploy from a Dockerfile, a prebuilt image, or an Azure Container Registry remote build.
docker.imagePassthrough deploys an already-published container image by reference, with no local or remote image operations.
Extension bundles install directly from HTTPS URLs without first registering a source.
Layered provisioning infers dependencies from Bicep parameter references, so dependent layers run in the right order.
New features
🔌 Extensions
The azd extension framework reached general availability this month. Read more in The Azure Developer CLI extension framework is generally available .
Install a self-contained extension bundle directly from an HTTPS URL with azd extension install . The command uses the existing extraction, registry, and checksum validation flow. [#9417]
Official-source extensions can report named usage events with bounded attributes through the new TelemetryService.ReportUsage extension gRPC API. [#9174]
📦 Container deployment
Deploy container-based Azure Functions services from a Dockerfile, a prebuilt image, or an Azure Container Registry (ACR) remote build by configuring host: function in azure.yaml . [#9284]
Pass an already-published container image to the destination by setting docker.imagePassthrough: true with a service-level image . azd doesn’t require Docker or Podman, and it doesn’t build, pull, tag, or publish the image. [#9588]
services:
api:
host: containerapp
image: registry.example.com/apps/api:1.0
docker:
imagePassthrough: true
Breaking changes
Extension and tool update terminology. The canonical commands are now azd extension update and azd tool update . The former upgrade commands remain as aliases, but JSON output reports "action": "update" and telemetry identifiers use update terminology. Update scripts that inspect the action field and custom telemetry queries that use the former identifiers. The --no-dependency-upgrades flag is now --no-dependency-updates . Contributed by Hiyo Shin (@hyoshis) . [#9370]
Extension source name validation. Source names must contain 1-64 lowercase letters, digits, hyphens, or underscores. Remove and re-add existing sources with names that contain spaces, periods, uppercase letters, or other unsupported characters. [#9451]
🪲 Bugs fixed
Provisioning and deployment
Expand ${VAR} references in deployment stack settings such as denySettings.excludedActions and denySettings.excludedPrincipals . [#9238]
Show nested Azure Resource Manager (ARM) failures and recovery guidance when azd provision --preview encounters issues such as quota limits. [#9324]
Infer custom provisioning layer dependencies from Bicep parameter references, preventing dependent layers from receiving empty or stale outputs. [#9535]
Complete App Service deployments with a warning when their status doesn’t change for five minutes instead of waiting indefinitely. [#9489]
Prefer project-tagged Bicep deployments during refresh, down, and provision-state lookup so azd doesn’t use another project’s deployment history. [#9490]
Set Azure Kubernetes Service kubeconfig directories and files to owner-only permissions. [#9675]
Pipelines and updates
Install the exact stable version reported by azd update instead of a newer release that appears while the command is running. [#9325]
Accept federated authentication for azd pipeline config --provider azdo --auth-type federated and correct the flag’s help text for Azure DevOps. [#9329]
Support GitHub Actions repositories that use immutable OpenID Connect (OIDC) subject claims. [#9430]
Aspire and initialization
Prevent azd init --from-code and azd infra generate --force from waiting indefinitely when persistent Microsoft Build Engine worker nodes keep output pipes open for Aspire solutions. [#9347]
Detect unsupported non-C# Aspire AppHosts early in azd init and azd up , then show actionable guidance instead of Docker or source-build errors. [#9353]
Complete Aspire AppHost manifest generation when the Aspire CLI run hook rewrites the azd publish invocation. [#9473]
Exclude extension-specific templates from azd init and azd template list when they can’t be initialized as standard templates. [#9495]
Extensions and interactive experiences
Improve extension install and update errors to distinguish missing dependencies from incompatible versions. Errors now identify the requested version and searched sources while preserving values in retry commands. [#9361]
Fall back to the official azd registry when an extension’s source doesn’t contain a compatible dependency version. [#9537]
Preserve HTTP status codes and provider error details when Azure service errors cross the extension gRPC boundary. [#9613]
Keep GitHub Copilot desktop terminals interactive instead of incorrectly detecting them as Copilot CLI agent sessions and enabling no-prompt behavior. Contributed by Alberto Gimeno (@gimenete) . [#9504]
Remove duplicated punctuation from interactive prompts. [#9476]
Preserve optional values for extension flags in generated shell completions and telemetry parsing, so flags that accept a bare form or an explicit value complete correctly. [#9714]
Reject empty extension multi-select submissions consistently in interactive and no-prompt modes unless the extension allows an empty selection. [#9715]
Preserve structured extension error details when they pass through nested gRPC calls. [#9636]
Select the GitHub Copilot model before offering reasoning levels, and only show levels that the model supports. [#9645]
Other changes
Update the bundled GitHub CLI to v2.97.0, then to v2.98.0. [#9380] [#9673]
Replace raw extension source telemetry with privacy-safe source categories such as azd , dev , nightly , local , and bundle . [#9452]
Report generic GitHub Copilot agent sessions in Visual Studio Code as GitHub Copilot VSCode in the execution.environment telemetry field. Contributed by @qinezh . [#9420]
Add provider and config fields to infra.layers[] in the azure.yaml schema so editors can validate per-layer provisioning providers and configuration. [#9457]
Show the complete set of required extensions and why each one is needed before prompting for automatic installation. azd now resolves the full install plan before making changes. [#9474]
Recognize Codex and Cursor as AI-agent execution environments for non-interactive behavior and telemetry. [#9698]
Update the bundled GitHub Copilot CLI to v1.0.80 and the Copilot SDK to v1.0.11. [#9644]
New docs
New and updated azd documentation on Microsoft Learn:
Manage Azure development tools with azd tool (August 5)—Added azd tool uninstall guidance, including dry runs, bulk removal, and per-agent skill output.
Explore Azure Developer CLI support for CI/CD pipelines (August 7)—Documented federated authentication support for Azure DevOps and corrected the authentication guidance.
Azure Developer CLI’s azure.yaml schema (August 7 and 14)—Added agent environment-variable validation and clarified when layered provisioning infers dependencies or requires explicit dependsOn .
Extension development concepts (August 13)—Updated for the generally available extension framework, project-level extension requirements, extension bundles, and source types.
Layered provisioning with the Azure Developer CLI (August 14)—Explained dependency-based layer ordering and when non-Bicep providers need explicit dependencies.
New templates
Community-authored templates help you get started faster, solve real-world scenarios, and showcase best practices for deploying solutions with Azure Developer CLI.
Daily Repo Digest with AI Gateway by Microsoft : A Python Foundry Hosted Agent sample that runs a Microsoft Agent Framework repo-digest agent. Model requests and read-only GitHub MCP calls are routed through Azure AI Gateway, and the template deploys end to end with azd up using Bicep infrastructure. This is the sample used by the AI Gateway quickstart.
Serverless Repo Digest Agent by paulyuk : A daily GitHub repository digest agent running on the Azure Functions serverless agents runtime with Azure AI Gateway and GitHub MCP tools.
M365 Inbox Agent for Azure Functions (Python) by Azure Functions Team : An AI agent that triages a Microsoft 365 inbox, escalating urgent mail to Teams, drafting replies, and sending daily briefings based on rules written in Markdown.
Serverless Expense Processor Agent by Microsoft : A markdown-first Azure Functions serverless agent for queue-driven expense processing. It reads expense requests from Azure Queue Storage in any format, selects and applies the matching policy document from Blob Storage, and routes the decision to an approved, review, or flagged output queue.
Document Reviewer by Azure Samples : A markdown-first Azure Functions serverless agent that reviews new SharePoint PDF and DOCX files and posts an evidence-backed brief to one Microsoft Teams channel.
Flexible Azure Landing Zone (Bicep-Based) by Durga Prasad Katrapally : A modular Azure landing zone with hub-spoke networking, optional security controls, monitoring, and a scalable architecture.
The Azure Developer CLI template gallery continues to grow with contributions from the community. Thank you!
🙋‍♀️ New to azd?
If you’re new to the Azure Developer CLI, azd is an open-source command-line tool that helps you get your application from your local development environment to Azure faster. It provides developer-friendly commands that map to key stages in your workflow, whether you’re working in the terminal, your editor, or continuous integration and delivery.
Install azd
Explore templates: Browse the Awesome azd template gallery and AI App Templates
Learn more: Visit the official documentation and troubleshooting guide
Get help: Visit the GitHub repository to file issues or start discussions.
