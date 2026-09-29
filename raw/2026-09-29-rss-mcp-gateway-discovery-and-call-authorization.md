---
source: "https://developers.googleblog.com/turn-your-rest-apis-into-mcp-tools-with-google-cloud-api-gateway/"
title: "Turn your REST APIs into MCP tools with Google Cloud API Gateway"
author: "Sanjay Pujare; Paul Howell; Geir Sjurseth"
date_published: "2026-09-24"
date_clipped: "2026-09-29"
category: "AI / LLM Research & Tooling"
source_type: "rss"
capture_format: "attributed-summary"
---

# Source capture

Capture: attributed summary of the fetched written article; not a full-text reproduction.

Google's API Gateway preview exposes selected REST operations as MCP tools from annotated OpenAPI definitions. Calls pass through the existing operation's authentication, quota, and logging path; the gateway translates between MCP arguments and REST requests.

Discovery has a separate security boundary. Tool listing is public by default, potentially exposing operation names and schemas. The article describes JWT protection for discovery and notes that API keys cannot secure that method. Tool calls retain the underlying operation's authentication requirements.

For HoneyDrunk, the portable design lesson is to evaluate discovery exposure separately from execution authority, and to provide descriptions that explain appropriate tool use. Preview limitations include omitted empty-response operations, incomplete rendering of deeply nested schemas, and absence of response streaming. This is an MCP integration pattern, not a recommendation to migrate Azure workloads to Google Cloud.

Source: [Original article](https://developers.googleblog.com/turn-your-rest-apis-into-mcp-tools-with-google-cloud-api-gateway/).
