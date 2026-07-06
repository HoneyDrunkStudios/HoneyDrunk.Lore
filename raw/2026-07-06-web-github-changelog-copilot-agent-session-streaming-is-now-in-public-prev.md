---
source: "https://github.blog/changelog/2026-07-02-copilot-agent-session-streaming-is-now-in-public-preview"
title: "Copilot agent session streaming is now in public preview"
author: "GitHub Changelog"
date_published: "2026-07-02"
date_clipped: "2026-07-06"
category: "Developer Tooling & AI Coding"
source_type: "web"
---

# Copilot agent session streaming is now in public preview

Source: https://github.blog/changelog/2026-07-02-copilot-agent-session-streaming-is-now-in-public-preview

Back to changelog 
Improvement 
July 2, 2026 •
1 minute read 
Copilot agent session streaming is now in public preview 
Table of Contents 
Streaming endpoint 
REST API 
Menu. Currently selected: Streaming endpoint 
Streaming endpoint 
REST API 
GitHub Enterprise Cloud customers with enterprise managed users can now access GitHub Copilot agent session data across all Copilot clients, including:
Cloud agents operating on github.com and data resident deployments on ghe.com 
GitHub Copilot CLI 
Visual Studio Code 
Visual Studio 
Partner IDEs, such as those provided by JetBrains and Eclipse 
This gives you direct visibility into agent session activity (e.g., prompts, responses, and tool calls) so you can manage AI usage across your enterprise. You can choose to access this data via a streaming endpoint or the REST API. To enable this, go to the Copilot subpage in AI Controls and select Enable everywhere for both “Copilot Usage Records Streaming” and “Copilot Usage Records API”.
Streaming endpoint 
You can initiate a streaming connection to an event collector or SIEM tool of your choice from your audit log settings. Once configured, GitHub automatically streams all session data for your enterprise to that endpoint. Microsoft Purview is also available as a supported streaming endpoint in public preview, giving customers in the Microsoft ecosystem a direct pathway to send auditability data from all GitHub Copilot clients. For more information, see our documentation on setting up audit log streaming .
REST API 
The REST API lets enterprise owners pull the last 48 hours of session data on demand using this endpoint:
GET /enterprises/{enterprise}/copilot/usage-records : Retrieve Copilot usage records for an enterprise. 
To learn more, read the Copilot Usage Records REST API documentation .
Table of Contents 
Streaming endpoint 
REST API 
Menu. Currently selected: Streaming endpoint 
Streaming endpoint 
REST API 
copilot 
enterprise management tools 
Share 
Copied 
Shared 
Back to changelog
