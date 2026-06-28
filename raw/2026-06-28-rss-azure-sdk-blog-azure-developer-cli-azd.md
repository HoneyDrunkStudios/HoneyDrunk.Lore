---
source: "https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-may-june-2026/"
title: "Azure Developer CLI (azd)"
author: "Kristen Womack"
date_published: "2026-06-26"
date_clipped: "2026-06-28"
category: "Azure & Cloud"
source_type: "rss"
---

# Azure Developer CLI (azd)

Source: https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-may-june-2026/

This is the combined May and June round-up for the Azure Developer CLI ( azd ). Nine releases shipped across the two months: 1.24.3 , 1.25.0 , 1.25.1 , 1.25.2 , 1.25.3 , and 1.25.4 in May, followed by 1.25.5 , 1.25.6 , and 1.26.0 in June. Below is what’s new, what changed, and what we fixed, with links to the pull requests if you want to dig in.
Have feedback or questions? Join the release discussion on GitHub .
Highlights: 
A new azd tool command group discovers, installs, checks, and upgrades Azure development tools. 
azd exec is a new cross-platform command and script runner that inherits the full azd environment, including Key Vault secret resolution. 
Multi-layer provisioning gets safer dependency analysis and an explicit dependsOn field in azure.yaml . 
An interactive prompt on Ctrl+C during azd provision and azd up lets you choose whether to leave the Azure deployment running or cancel it. 
Several concurrency fixes for parallel Container Apps deploys, including cross-service image contamination on Azure Container Registry (ACR) remote builds. 
Go is now a supported language for Azure Functions services in azd up . 
Self-contained extension bundles let you share and install azd extensions without a registry. 
Per-tenant subscription filters persist across runs, so the subscription prompt stays scoped to the subscriptions you actually use. 
These releases include security improvements. Please upgrade to the latest version with azd upgrade . 
New features 
🧰 Tool management 
A new azd tool command group helps you discover, install, check, and upgrade the tools azd and your templates depend on, like language SDKs, the Bicep CLI, Docker, the GitHub CLI, and Visual Studio Code extensions. Instead of hunting down install instructions across multiple sites when a template fails partway through, you can run azd tool list to see what’s needed, azd tool install to get it, and azd tool check to confirm everything is current. New azd users also get a first-run welcome that walks through recommended tooling, so the first azd up is less likely to fail on a missing prerequisite. The command group is on by default. See Manage development tools with azd for the full command reference.
Add azd tool for discovering, installing, checking, and upgrading Azure development tools, including first-run tooling guidance in core workflows. [#7450] 
Improve azd tool check to detect updates by querying package managers, extension registries, and the Visual Studio Code Marketplace instead of relying only on cached values. [#8085] 
Promote the azd tool command group out of alpha. It’s now available by default, along with its first-run welcome and update-check experiences. [#8440] 
Add azd tool install azure-skills and azd tool upgrade azure-skills , with per-host selection for supported agentic CLI hosts. [#8704] 
⚡ Scripting and execution 
Add azd exec , a cross-platform command and script execution engine that runs programs with full azd environment context, including environment variables and Key Vault secret resolution. [#7400] 
🏗️ Provisioning and deployment 
These changes make multi-layer provisioning safer by default, surface deployment IDs to extensions and CI tooling, and improve the prompts during azd provision and azd up .
Add an interactive cancel prompt when Ctrl+C is pressed during azd provision or azd up with Bicep. Choose to leave the Azure deployment running or cancel it through the ARM Cancel API with status feedback. Non-interactive mode defaults to leaving the deployment running. [#7795] 
Add a tenant picker before the subscription prompt for multi-tenant users, scoping the subscription list to the selected tenant. [#8083] 
Add azd config sub-filter set and azd config sub-filter remove to save per-tenant subscription filters and apply them automatically in subscription prompts. [#8424] 
Add Go support for Azure Functions services, enabling azd up for Go Function Apps on Flex Consumption. [#8599] 
Add actionable suggestions and links to preflight warnings, with multi-line formatting for better readability. [#8059] 
Expose ARM deployment IDs through a new AZD_DEPLOYMENT_ID_FILE environment variable during provision, written in NDJSON format for programmatic consumption. [#8047] 
azd show -o json now includes the deployed ingress URL for each service. [#8071] 
🔌 Extensions 
We made improvements across the extension framework SDK, the registry format, and the upgrade workflow itself.
Improve azd extension upgrade --all with continue-on-error batch orchestration: per-extension status display (Upgraded, Skipped, Promoted, Failed) with before→after version, a batch summary line, and --output json for machine-readable continuous integration (CI) output. [#7852] 
Add RegisterFlagOptions to the extension Software Development Kit (SDK) for declaring per-subcommand allowed values, defaults, and validation for inherited persistent flags. The new helper drives help text, shell completion, and parse-time validation automatically. [#7826] 
Add extension registry schema versioning. Extension registries now carry a schemaVersion field, and azd shows a clear upgrade-required message when an incompatible registry schema version is encountered. [#7837] 
Fix extension pack support gaps and improve azd extension upgrade dependency handling. Extension manifests can now declare dependencies without top-level capabilities , semver dependency ranges resolve to the highest compatible published version, and install-time dependency cycles fail with a clear error. The upgrade command reconciles declared dependencies to the latest compatible versions, adds --no-dependency-upgrades to opt out, and reports dependency updates through dependencyUpgrades in --output json . [#8316] 
Add the validation-provider extension capability so extensions can contribute checks to local Bicep preflight validation. [#8656] 
Add self-contained extension bundles with azd x pack --bundle and azd extension install <bundle.zip> for sharing and installing extensions without a registry. [#8697] 
✨ Output and prompts 
Add a Secret prompt option in core azd and extension gRPC prompts so sensitive values are masked during input. [#7982] 
Upgrade seven Command Line Interface (CLI) list commands ( azd ext source list , azd tool list , azd tool check , azd template list , azd template source list , azd copilot consent list , azd config options ) to responsive table output with full, compact, and card layouts based on terminal width. [#8144] 
Improve azd ext list readability with responsive table and card layouts, plus clearer status indicators across terminal widths. [#8091] 
Breaking changes 
Cleaner azd up output. You’ll see one progress view from start to finish instead of three separate stage banners, which consolidates progress into one view. If you have CI that watches for the old messages ( "Packaging services…" , "Provisioning Azure resources…" , "Deploying services…" , or the "Your up workflow…completed in" footer), update those checks. [#7776] 
Faster azd up with parallel steps. Independent work now runs in parallel. One side effect: if a step fails, other in-flight work (like long-running Azure deployments) may keep running for a bit before azd up exits, instead of stopping immediately like it used to. [#7776] 
🪲 Bugs fixed 
Concurrency and parallel execution 
Fix concurrent map writes crashes during azd up and azd deploy on multi-service projects. Environment access, env file save/reload, the bundled kubectl and kustomize clients, and AKS service publish updates are now safe to run in parallel. [#7776] 
Fix cross-service image contamination when publishing multiple Container Apps in parallel with ACR remote build ( docker.remoteBuild: true ), where each app could end up running another service’s image. Each parallel upload now lands in its own blob. [#7776] 
Make x-ms-client-request-id (and the equivalent Microsoft Graph header) unique per HTTP request so Azure services can correctly deduplicate, correlate, and log individual calls during parallel provision and deploy. [#7776] 
Fix a parallel dotnet publish race that could break Aspire deploys by isolating build artifacts per service. [#8195] 
Restore the per-service “Detail” column during azd deploy and azd up so you can see sub-steps like "Pushing image" and "Updating container app" again instead of a blank field between phases. [#7776] 
Deployment lifecycle 
Fix lifecycle hook output ( preprovision , postprovision , and predeploy ) being silently suppressed during azd up . [#8263] 
Fix azd up rendering an empty deploy progress summary when provisioning fails before deploy starts. [#8074] 
Fix azd provision crash when infrastructure layers use Terraform or other non-Bicep providers. [#8136] 
Fix azd deploy polling indefinitely when deploying to a stopped Linux web app. After three consecutive polls with zero running instances, the deployment is treated as complete. [#7773] 
Fix buildArgs and buildEnv in azure.yaml being silently dropped when docker.remoteBuild: true . Build arguments are now forwarded to the ACR remote build task. [#7997] 
Add a safeguard prompt before azd down deletes a resource group that wasn’t created by azd . --no-prompt now fails closed for this scenario unless --force is supplied. [#7998] 
Fix intermittent DeploymentNotFound failures during azd up , azd provision , and azd down by retrying the transient ARM 404 that can be returned immediately after a subscription- or resource-group-scoped deployment is submitted. [#8551] 
Fix azd down failing to purge Azure AI Foundry cognitive accounts due to an SDK type mismatch in the networkInjections response. [#8493] 
Fix Static Web Apps deployment failing with a BadRequest error for the default environment name by passing production to the SWA CLI, and add an optional environment field in azure.yaml for targeting named preview environments. [#8588] 
Fix Aspire .NET deployments not using Podman when Docker is unavailable by lazily detecting the container engine in the deploy path. [#8598] 
Fix dotnet publish failing with “empty dotnet configuration output” when Podman is the container engine by forwarding the detected engine to the .NET SDK. [#8527] 
Authentication and pipelines 
Fix azd pipeline config always using the default OpenID Connect (OIDC) subject format when creating GitHub federated credentials, causing AADSTS700213 mismatches for organizations with customized OIDC subject claims. azd now queries the GitHub OIDC customization API and constructs the correct subject string. [#7705] 
Fix azd pipeline config creating mismatched GitHub OIDC federated credentials for organizations using context or repo claim keys. [#8681] 
Fix azd auth status and provisioning commands reporting “not logged in” when AZD_AUTH_ENDPOINT and AZD_AUTH_KEY external auth is active but azd auth logout was previously run. [#8004] 
Fix azd auth status reporting unauthenticated in Cloud Shell and blocking azd provision and azd ai agent init for sessions relying on the ambient Cloud Shell credential. [#8459] 
Fix stale token errors (for example AADSTS700082 ) persisting after re-running azd auth login ; azd now automatically clears cached authentication data when re-logging in while already signed in. [#8414] 
Fix memory exhaustion and slow model catalog loads when Azure CLI delegated authentication ( auth.useAzCliAuth = true ) fans out concurrent token requests by caching tokens in-process per tenant. [#8458] 
Fix GitHub URL resolution surfacing a misleading “could not find a valid branch” error for Security Assertion Markup Language (SAML) Single Sign-On blocks, rate limiting, private repos, and server errors. azd now identifies the actual failure mode and shows actionable suggestions with relevant documentation links. [#7922] 
CLI parsing and output 
Fix -C and --cwd relative paths being applied twice when invoking extensions, causing “no such file or directory” errors. [#8230] 
Fix -ojson and -otable (short -o flag with attached value) being rejected with a confusing error. Pre-cobra parse errors no longer show nothing on stderr. [#7948] 
Fix the progress widget printing stale, overlapping output on narrow terminals by truncating each rendered line to the terminal width. [#8402] 
Fix first-run tool checks recursively re-invoking azd extension list and leaking ANSI output into JSON command output. [#8084] 
Fix interactive prompts (for example the azd init environment-name prompt) rendering twice on Windows terminals by rendering prompts with azd’s own UX components instead of the archived survey library. [#8649] 
Init and extension installation 
Make azd init idempotent with respect to the environment: re-running init in an initialized project now reuses the existing environment instead of failing with “environment already initialized”. With --no-prompt and no -e , the recorded default environment is reused, and an explicitly requested environment is created and promoted to the default when it does not already exist. [#8561] 
Fix azd init required extension installation failing when an extension is available from multiple sources by prompting users to choose the source interactively. [#8666] 
Fix extension Project().AddService calls overwriting existing top-level azure.yaml properties such as hooks when adding services. [#8679] 
Fix azd update and the macOS update banner failing with “Refusing to load cask from untrusted tap” by running brew trust azure/azd before any Homebrew cask install, upgrade, or uninstall. [#8776] 
Tooling and integration 
Fix the azd tool first-run prompt blocking users who deselect all recommended tools, and clarify its setup wording. [#8487] 
Fix azd init Copilot Preview silently falling back to an older model by upgrading the bundled Copilot SDK to v0.3.0 and CLI to v1.0.36-0. [#8114] 
Fix azd tool Copilot metadata to use the current Visual Studio Code extension and up-to-date Copilot CLI install documentation links. [#8086] 
Fix Artificial Intelligence (AI) agent detection not recognizing Copilot CLI through the COPILOT_CLI environment variable. Thanks @tmeschter for the contribution! [#8249] 
Fix false-positive preflight warning for Azure Chaos Studio target resources ( Microsoft.Chaos/targets ) whose names are service-mandated. [#8240] 
Fix AI model quota preflight blocking all locations on subscriptions where the Azure Cognitive Services /usages API returns an empty list (for example, free-tier subscriptions); empty usage lists are now treated as available quota rather than zero quota. [#8537] 
Fix the AI model quota preflight rejecting all locations on free-tier subscriptions by lowering the required OpenAI.S0.AccountCount capacity from 2 to 1. [#8571] 
Other changes 
Add per-phase timing breakdown to the azd up success output and sanitize deploy progress service names to prevent terminal escape-sequence injection in rendered output. [#8050] 
Improve azd extension upgrade edge case handling: delisted extensions report “no longer available” and continue the batch, network failures show actionable retry guidance, and extension config writes are now atomic to prevent corruption if interrupted. [#7853] 
Improve extension SDK gRPC error transport. Host-returned errors now carry structured suggestion and link data through ActionableErrorDetail , so extensions can surface the full error-suggestion experience to users. [#7919] 
azd up honors AZD_DEPLOY_CONCURRENCY as a fallback when AZD_UP_CONCURRENCY is unset, so existing deploy-tuning configurations carry over to the unified up workflow. [#7776] 
Reduce the size of the generated Fig completion spec ( azd completion fig ) by pruning duplicated help subcommands and redundant extension output options; add --include-help-subcommands to restore the previous expanded output. [#8417] 
Update user-facing references from “.NET Aspire” to “Aspire” to reflect the product rebrand. Thanks @IEvangelist for the contribution! [#8579] 
Improve stacked table readability by labeling grouped headers, dimming structural lines, and highlighting source URLs. [#8725] 
Improve responsive table layouts across azd extension list , azd tool check , azd tool list , and azd template list . [#8785] 
Update bundled Bicep CLI from v0.42.1 to v0.43.8, and then to v0.44.1. [#8148] [#8594] 
Update bundled GitHub CLI to v2.92.0. [#7946] 
New docs 
New and updated azd docs on Microsoft Learn:
Manage Azure development tools with azd tool (June 3) — Full reference for the new azd tool command group: discover, install, check, and upgrade language SDKs, the Bicep CLI, Docker, the GitHub CLI, and VS Code extensions from the command line. Pairs with the May release of the command group. 
Deploy to Azure App Service slots with azd (June 11) — Adds a new “Bypass slot detection” section that documents AZD_DEPLOY_<SERVICE>_IGNORE_SLOTS . Set it to true for a specific service to deploy directly to the main App Service app and ignore any slots, which is useful for CI pipelines that refresh the main app without touching existing slots. 
Customize your azd workflows using command and event hooks (June 12) — shell is now optional in hook definitions. When omitted, azd defaults to pwsh on Windows and sh on Linux and macOS, and prints a warning recommending you set shell explicitly for cross-platform reliability. For run paths, azd infers the shell from the file extension (for example, .sh or .ps1 ). 
Use Terraform with azd (June 22) — Adds an “Authenticate to Azure” section with two sign-in options for Terraform-based azd projects. Recommended: azd config set auth.useAzCliAuth true followed by az login , so both tools share a single credential. Alternative: sign in to azd and Azure CLI separately. A new IMPORTANT callout explains that Terraform’s azurerm provider doesn’t read tokens from azd ‘s credential cache, so azd up fails at the provision step without an az login . 
Deploy to a Microsoft Foundry or Azure Machine Learning online endpoint (June 22) — Documents the kind field in agent.yaml (currently hosted , with either code_configuration for ZIP-based code deploys or image for prebuilt container images from Azure Container Registry) and replaces the previous kind: prompt example with a working kind: hosted definition that azd deploy accepts. 
Supported languages and environments (June 24) — Documents Go as a supported language for Azure Functions services in azd up , including Flex Consumption support and the azure.yaml configuration. 
New templates 
Community templates help you get started faster, cover common scenarios, and show how to deploy real solutions with Azure Developer CLI.
awesome-azd 
In June, 40 AI app templates that previously lived only in the AI App Templates gallery were added to the awesome-azd gallery so they’re discoverable from both places. See awesome-azd #900 for the full list.
Rust MCP Server on Azure Container Apps by zubeyralmaho : A zero-trust, read-only Model Context Protocol (MCP) server written in Rust on top of axum, deployed to Azure Container Apps with Bicep. Designed as a memory-safe, low-latency option for AI agent tool execution as an alternative to Python or Node.js stacks. 
Azure Static Web App with Next.js and Postgres by benleane83 : An Azure Static Web App (SWA) template configured with Next.js, Tailwind, Entra SWA Auth, Node.js Azure Functions, and Postgres. Great as a Vercel or Supabase alternative that’s native to Azure. 
Azure Functions Cosmos DB Trigger quickstarts by Azure Samples , bringing the Cosmos DB Trigger pattern to three more languages alongside the existing .NET, Python, and TypeScript siblings:
Azure Functions Java Cosmos DB Trigger : An Azure Functions quickstart project that demonstrates how to use a Cosmos DB Trigger with azd for quick and easy deployment, using Java. The sample uses managed identity to make deployment secure by default. 
Azure Functions JavaScript Cosmos DB Trigger : An Azure Functions quickstart project that demonstrates how to use a Cosmos DB Trigger with azd for quick and easy deployment, using JavaScript and Node.js. The sample uses managed identity to make deployment secure by default. 
Azure Functions PowerShell Cosmos DB Trigger : An Azure Functions quickstart project that demonstrates how to use a Cosmos DB Trigger with azd for quick and easy deployment, using PowerShell. The sample uses managed identity to make deployment secure by default. 
Azure Functions Flex Consumption with Azure Files OS Mount samples by Azure Samples , showing how to mount an Azure Files share into the Flex Consumption host and reach native binaries and large datasets directly from your function code:
FFmpeg image processing : This scenario demonstrates event-driven image processing using FFmpeg from an Azure Files OS mount. Images uploaded to Blob Storage trigger the function through Event Grid, which processes them using FFmpeg from the mount and saves results to an output container. 
Durable text analysis : This scenario uses Durable Functions fan-out and fan-in orchestration to analyze text files stored on an Azure Files OS mount. An HTTP trigger starts the orchestration, which fans out to analyze each text file in parallel and aggregates results. 
AI gallery 
Sovereign Chat Experience Starter by Microsoft Foundry Team : A reusable Chat UI for AI experiences, built on the Azure OpenAI Responses API standard and Fluent AI components. It connects to a Microsoft Foundry project and is designed to be deployed on Azure Kubernetes Service (AKS) clusters. The application features a chat interface, chat history, streaming responses, and a pluggable provider architecture that supports both live Microsoft Foundry backends and an in-memory mock mode for offline development. 
Video Agents Foundry Solution by Video Indexer : Deploy AI-powered video analysis at the edge using Azure Video Indexer on Arc-enabled AKS clusters with GPU support, combined with AI agents built on Azure OpenAI for automated video analysis workflows. 
The Azure Developer CLI template gallery keeps growing thanks to contributions from the community. Thank you!
🙋‍♀️ New to azd? 
If you’re new to the Azure Developer CLI, azd is an open-source command-line tool that helps you get your application from your local development environment to Azure faster. It provides developer-friendly commands that map to key stages in your workflow, whether you’re working in the terminal, your editor, or CI/CD.
Install azd 
Explore templates: Browse the Awesome azd template gallery and AI App Templates 
Learn more: Visit the official documentation and troubleshooting guide 
Get help: Visit the GitHub repository to file issues or start discussions
