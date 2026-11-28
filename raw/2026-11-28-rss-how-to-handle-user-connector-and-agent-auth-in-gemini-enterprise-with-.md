---
source: "https://developers.googleblog.com/how-to-handle-user-connector-and-agent-auth-in-gemini-enterprise-with-a-custom-ui"
title: "How to handle user, connector, and agent auth in Gemini Enterprise with a custom UI"
author: "Neeraj Agrawal"
date_published: "2026-11-20"
date_clipped: "2026-11-28"
category: "Security & Ethical Hacking"
source_type: "rss"
---

# How to handle user, connector, and agent auth in Gemini Enterprise with a custom UI

When using the out-of-the-box [**Gemini Enterprise**](https://cloud.google.com/gemini/enterprise/docs/overview) web application, identity and access management happen behind the scenes. Employees sign in through Google Identity or Workforce Identity Federation (such as Microsoft Entra ID or Okta), search results automatically respect per-user access controls (ACLs), and third-party login prompts for **Federated Connectors** or **custom agents** appear automatically in the chat UI.

In practice, however, many enterprises build their own **Customer UI** to embed Gemini Enterprise into an internal portal, intranet, or line-of-business application. To do this, **Customer BE** calls the Gemini Enterprise [**StreamAssist API**](https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants/streamAssist).

The moment an application builds a custom UI and calls the StreamAssist API directly, the three authentication flows that the built-in web app handled automatically become the responsibility of **Customer UI** and **Customer BE**:

1. **Authenticating to StreamAssist (User Identity vs. Workload Identity):** For user-facing applications where document ACLs, isolated chat history, and restricted agent permissions matter, **Customer UI** and **Customer BE** must pass the signed-in employee's identity via Google Identity (**Pattern 1A**) or Workforce Identity Federation (**Pattern 1B**). For non-personalized backend bots or shared service portals, **Customer BE** can authenticate keyless using Workload Identity Federation (**Pattern 1C**).
2. **Authenticating Federated Connectors through Customer UI:** Real-time Federated Connectors use 3-Legged OAuth (3LO) so they only retrieve Google Drive files, SharePoint sites, Jira issues, or ServiceNow incidents that the signed-in employee is allowed to see. Because **Customer UI** does not have Gemini Enterprise's built-in Connect button, **Customer BE** and **Customer UI** must discover the engine's connectors, check the **Keystore** for a valid token, trigger the 3LO consent popup when needed, save the refresh token in the **Keystore**, and include the connector data stores in StreamAssist queries.
3. **Handling per-tool OAuth for custom ADK agents:** When deploying a custom [**ADK agent**](https://google.github.io/adk-docs/) on [**Vertex AI Agent Engine**](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview) that connects to multiple enterprise systems (such as Google Drive and Microsoft SharePoint), attaching static OAuth configs at the root agent registration level blocks the entire agent upfront. Instead, by wrapping protected sub-agent tools with **GcpAuthProvider** (backed by **GCP Auth Manager's Token Vault**) and deploying the agent with **Agent Identity** turned on, StreamAssist triggers an on-demand 3LO popup only when a protected tool is called.

This guide walks through the architecture, component flows, and runnable code for all three layers (**Figure 1**):

Figure 1: End-to-end authentication architecture across StreamAssist login (Google Identity, Workforce STS, or Workload STS), Federated Connectors (Keystore), and custom ADK agents (Vertex AI Agent Engine + GCP Auth Manager Token Vault).

## Part 1: Three patterns to authenticate to StreamAssist (User & Workload)

Depending on whether **Customer UI** is acting on behalf of an individual employee or running as a shared backend bot, customer architectures follow three keyless authentication patterns:

Figure 2: Comparing Pattern 1A (Pure Google Identity), Pattern 1B (Workforce Identity Federation + Google STS), and Pattern 1C (Workload Identity Federation + Google STS) for calling StreamAssist.

**Required IAM Role and License:** Every principal calling the StreamAssist API must be granted the **Discovery Engine User** IAM role on the GCP project. For human user patterns (**Pattern 1A** and **Pattern 1B**), the user (or Workforce Pool group) must also have an active Gemini Enterprise user license assigned in the Admin Console.

### **Pattern 1A: Pure Google Identity (Google Login UI to StreamAssist)**

When employees sign in with Google Workspace or Cloud Identity and the Gemini Enterprise engine is configured for Google Identity, the flow has zero extra hops:

1. **Customer UI** signs the employee in using [**Google Identity Services (OAuth 2.0)**](https://developers.google.com/identity/oauth2/web/guides/overview) with the Google Cloud Platform scope.
2. Google returns a user access token scoped to the signed-in employee.
3. **Customer BE** sends that Bearer token directly to the StreamAssist API.

### **Pattern 1B: Workforce Identity Federation (External IdP UI to Google STS to StreamAssist**)

When employees sign into **Customer UI** with Microsoft Entra ID or Okta and Gemini Enterprise uses [**Workforce Identity Federation (WIF)**](https://cloud.google.com/iam/docs/workforce-identity-federation), you reuse the same Workforce Pool that is already connected to Gemini Enterprise:

1. **Register Customer UI on the existing WIF Provider:** Add the custom web app's Entra ID or Okta Client ID to the Google Cloud Workforce Pool OIDC Provider.
2. **Exchange the IdP token at Google STS:** After the employee signs into **Customer UI** and receives an OIDC token from Entra ID or Okta, **Customer BE** exchanges that token at Google Security Token Service (STS) against the Workforce Pool Provider.
3. **Call StreamAssist with the federated user token:** Google STS returns a short-lived Google access token representing that specific Workforce Pool user, enforcing all of the employee's group permissions and document ACLs.

### **Pattern 1C: Workload Identity Federation (Backend / Shared Bot to Google STS to StreamAssist)**

When a backend service, Slack/Teams webhook, or non-personalized knowledge bot needs to call StreamAssist without any Service Account JSON keys, use a project-scoped [**Workload Identity Pool**](https://cloud.google.com/iam/docs/workload-identity-federation):

1. **Obtain a machine JWT from the external IdP:** **Customer BE** requests an application token from the external IdP (for example, using OAuth 2.0 client credentials in Entra ID).
2. **Exchange at Google STS:** **Customer BE** exchanges that machine JWT at Google STS against the project's Workload Identity Pool Provider with zero keys on disk.
3. **Call StreamAssist:** **Customer BE** sends the returned Google STS token to StreamAssist.

**When to use Pattern 1C vs. Patterns 1A and 1B:** Because Workload Identity Federation authenticates a machine rather than an individual human employee, Gemini Enterprise sees every request as coming from the same workload identity. Use **Pattern 1C** for non-personalized bots over shared knowledge bases, and use **Pattern 1A** or **Pattern 1B** whenever you need per-user document ACLs, user-specific 3LO connectors, or restricted custom agents.

## Part 2: Authenticating Federated Connectors through a custom UI

Once **Customer UI** and **Customer BE** are calling StreamAssist as the signed-in employee, users can query native **Federated Connectors** (such as Google Drive, Microsoft SharePoint Online, Jira, Box, ServiceNow, and Confluence) that search live third-party APIs in real time.

Because Federated Connectors enforce user-level permissions in the third-party system, each employee authorizes the connector once using 3-Legged OAuth (3LO). Gemini Enterprise stores those per-user refresh tokens inside its own managed **Keystore**, so **Customer BE** never has to store third-party credentials in its own database.

Figure 3: Component architecture and 11-step 3LO flow for authenticating a Gemini Enterprise Federated Connector across Customer UI, Customer BE, 3P Auth Server, GE FE Server, GE Server, and Keystore.

- **Phase 1: Discover connectors and check Keystore (Steps 1 to 4):** **Customer UI** requests the available connectors from **Customer BE** (**Step 1**). **Customer BE** calls **GE Server** with the user's Part 1 Bearer token to list the Federated Connectors attached to the engine and check whether the user already has a valid access token for each connector (**Step 2**). **GE Server** checks the **Keystore**: if the user has authorized the connector before, **GE Server** refreshes and returns the token automatically; if not, it returns an authorization URL (**Step 3**). **Customer BE** returns the connector list to **Customer UI**, which renders an **Authorize Button** for any connector that needs consent (**Step 4**).
- **Phase 2: 3LO consent popup and redirect relay (Steps 5 to 7):** When the user clicks the **Authorize Button**, **Customer UI** opens the authorization URL in a popup window at the **3P Auth Server** (**Step 5**). After the user signs in and approves access, the popup redirects to Google's **GE FE Server** OAuth redirect page (**Step 6**), which sends the callback URL (containing the authorization code and state) back to **Customer UI** via browser postMessage and closes the popup (**Step 7**).
- **Phase 3: Exchange code, store refresh token in Keystore, and confirm (Steps 8 to 11):** **Customer UI** forwards the callback URL to **Customer BE** (**Step 8**), which calls **GE Server** to exchange the authorization code with the third-party token endpoint and save the user's refresh token inside the **Keystore** (**Step 9**). **GE Server** confirms to **Customer BE** (**Step 10**) and **Customer UI** (**Step 11**) that the connector is now authorized. Once authorized, **Customer BE** includes the connector's data store ID in its StreamAssist requests so Gemini Enterprise searches the live third-party connector at query time.

**Note for Custom UIs: Enabling Automatic Popup Handoff from GE FE Server:** All Gemini Enterprise Federated Connectors use Google's managed /oauth-redirect endpoint on **GE FE Server** as their fixed callback URL. By default, that page only sends browser postMessage events to the built-in Gemini Enterprise web app origin. When deploying **Customer UI** on a custom domain, work with your Gemini Enterprise team to enable the custom origin flag so **Step 7** automatically posts the callback URL to **Customer UI** and closes the popup.

## **Part 3: Individual tool-level OAuth for custom ADK agents via GCP Auth Manager Vault**

Native Federated Connectors are ideal for federated search and built-in actions. When a workflow requires multi-step reasoning, custom Python logic, or orchestrating across multiple enterprise APIs in a single assistant, teams build a custom [**ADK agent**](https://google.github.io/adk-docs/), deploy it on [**Vertex AI Agent Engine**](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview), and register it in Gemini Enterprise.

### **Why root-level OAuth on the agent registration blocks multi-tool custom UIs**

When registering an ADK agent in Gemini Enterprise, attaching static OAuth configurations directly to the root agent registration creates two issues for a custom UI:

1. **Upfront blocking across all tools:** Root-level OAuth gates the entire agent before the first turn even reaches your agent code. If an assistant connects to both **Google Drive** and **Microsoft SharePoint Online**, a user cannot ask a general policy question or query just SharePoint without being forced through every OAuth login upfront.
2. **Built-in UI coupling:** Root-level agent authorization is designed around the built-in Gemini Enterprise web UI rather than returning tool-specific authorization prompts over the StreamAssist API.

### **The solution: On-demand tool OAuth with Agent Identity and GCP Auth Manager**

To trigger 3-Legged OAuth **on demand per tool** and let Gemini Enterprise and Google Cloud manage the per-user **Token Vault** automatically, follow three simple setup steps:

1. **Create sub-agent tools and wrap protected tools in GcpAuthProvider:** Standard tools that do not need user login run as normal Python functions with zero OAuth prompts. For tools that call protected third-party APIs (such as SharePoint or Google Drive), wrap the tool function in ADK's AuthenticatedFunctionTool and GcpAuthProvider pointing to the Auth Provider resource in GCP Auth Manager.
2. **Deploy the ADK agent to Vertex AI Agent Engine with Agent Identity turned on:** Deploy the Root Router Agent and its sub-agents to Vertex AI Agent Engine with Agent Identity enabled. This provides a built-in SPIFFE identity for the agent. Grant that agent identity the Agent Identity Service Agent IAM role on the GCP project so it can retrieve tokens from the **GCP Auth Manager Token Vault**.
3. **Add a 3LO Auth Provider in Google Cloud Console (Auth Manager):** In the Google Cloud Console, create a 3LO Auth Provider for each third-party OAuth app (such as SharePoint and Google Workspace), set the Default Continue URI to **<website-url>/validateUserId** on Customer UI, and add the GCP Auth Manager callback URL (**/oauthcallback**) as the Redirect URI inside your Microsoft Entra ID or third party app.

Figure 4: Component architecture and 19-step on-demand tool 3LO flow across Customer UI, Customer BE, GE Server, Vertex AI Agent Engine, and GCP Auth Manager.

- **Phase 1: Query routing and Token Vault check (Steps 1 to 7):** The user sends a prompt from **Customer UI** to **Customer BE** (**Step 1**), which calls the StreamAssist API on **GE Server** with the user's Part 1 Bearer token (**Step 2**). **GE Server** invokes the custom ADK agent on **Vertex AI Agent Engine** (**Step 3**). Before running the protected tool, the sub-agent checks the **GCP Auth Manager Token Vault** using its Agent Identity (**Step 4**). On a first-time call (cache miss), **GCP Auth Manager** returns an authorization URL, which flows back from **Vertex AI Agent Engine** to **GE Server** (**Step 5**), **Customer BE** (**Step 6**), and **Customer UI** (**Step 7**).
- **Phase 2: 3LO consent popup and callback redirect (Steps 8 to 10):** **Customer UI** displays an **Authorize Button** that opens the authorization URL in a popup window, where the user signs in and approves access at the **3P Auth Server** (**Step 8**). The **3P Auth Server** redirects the popup to **GCP Auth Manager's** managed OAuth callback endpoint, which exchanges the authorization code for third-party tokens and holds them pending validation (**Step 9**). **GCP Auth Manager** then redirects the popup to the /validateUserId callback page on **Customer UI** with a validation state token (**Step 10**).
- **Phase 3: Validate user authorization and save token in Token Vault (Steps 11 to 14):** **Customer UI** passes the validation state token to **Customer BE** and closes the popup (**Step 11**). **Customer BE** calls the Validate User Authorization API on **GE Server** with the user's Part 1 Bearer token (**Step 12**). **GE Server** verifies the session owner and calls FinalizeCredentials on **GCP Auth Manager**, which permanently saves the user's 3LO token in the **Token Vault** and returns success (**Step 13**). **GE Server** then returns HTTP 200 OK to **Customer BE** (**Step 14**).
- **Phase 4: Automatic query retry and cached execution (Steps 15 to 19):** As soon as **Customer BE** receives HTTP 200 OK in Step 14, **Customer BE** automatically retries the StreamAssist query on the same session (**Step 15**). **GE Server** invokes the ADK agent on **Vertex AI Agent Engine** (**Step 16**), which now gets a **Token Vault** cache hit, calls the third-party API (such as Microsoft Graph or Google Drive) with the 3LO token, and streams the grounded answer back through **GE Server** (**Step 17**), **Customer BE** (**Step 18**), and **Customer UI** (**Step 19**). All subsequent queries run in a single turn with no popups.

## Explore the runnable code blueprint

We have packaged all three authentication layers, along with interactive web test UIs, CLI scripts, and curl commands into the [**gemini-enterprise-custom-ui-auth GitHub repository**](https://github.com/MagnIeeT/gemini-enterprise-custom-ui-auth):

- [**Part 1: User & Workload Auth to StreamAssist (01\_user\_auth\_streamassist/)**](https://github.com/MagnIeeT/gemini-enterprise-custom-ui-auth/tree/main/01_user_auth_streamassist)**:** Standalone Python scripts and curl commands for Google Identity, Workforce Identity Federation, and Workload Identity Federation.
- [**Part 2: Federated Connector 3LO Flow (02\_federated\_connector\_oauth/)**](https://github.com/MagnIeeT/gemini-enterprise-custom-ui-auth/tree/main/02_federated_connector_oauth)**:** CLI helper and interactive web Test UI.
- [**Part 3: Custom ADK Agent On-Demand Tool 3LO (03\_adk\_agent\_oauth/)**](https://github.com/MagnIeeT/gemini-enterprise-custom-ui-auth/tree/main/03_adk_agent_oauth)**:** Multi-agent ADK implementation, Vertex AI Agent Engine deployment script, and interactive web Test UI.
