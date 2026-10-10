---
"source": "https://devblogs.microsoft.com/azure-sdk/connect-azure-functions-to-more-services-with-managed-connectors"
"title": "Connect Azure Functions to more services with managed connectors"
"author": "Lily Ma"
"date_published": "2026-10-05"
"date_clipped": "2026-10-08"
"category": "Azure & Cloud"
"source_type": "rss"
---

Azure Functions can already connect to many Azure services through [triggers and bindings](https://learn.microsoft.com/azure/azure-functions/functions-triggers-bindings#supported-bindings). With managed connectors, your functions can access about 1,700 connectors across services such as Microsoft 365, Microsoft Teams, Dataverse, SharePoint, OneDrive, and third-party systems.

Connector triggers deliver events from these services to your function, while typed connector clients let your code take actions against them. You get this broader integration surface without writing the webhook registration code or managing the OAuth tokens required to connect to each service, so you can focus on your function’s business logic and let [Azure Connector Namespace](https://learn.microsoft.com/azure/connector-namespace/connector-namespace-overview) handle the connection.

Azure Functions integration with Connector Namespace is currently in *public preview*. It supports .NET isolated, Python, and Node.js. Review the [managed connectors overview](https://learn.microsoft.com/azure/azure-functions/functions-connectors-overview) for current language, hosting plan, and regional availability.

To demonstrate how connector triggers and actions work together, this article follows a .NET sample that automates RFP intake across SharePoint, Azure Content Understanding, and Teams.

## From an uploaded RFP to Teams notification

Consider an organization that receives requests for proposals (RFPs) in a shared SharePoint document library. Someone must read each document, identify the requested capabilities, determine which subject-matter experts should respond, and notify the right team.

The [automated RFP intake sample](https://github.com/Azure-Samples/functions-connectors-net-rfp-intake-sharepoint-teams) turns that process into an event-driven workflow:

* A customer uploads an RFP to a SharePoint document library.
* A SharePoint connector trigger invokes an Azure Function when the file is created.
* The function uses a typed SharePoint connector client to retrieve the file contents.
* Azure Content Understanding extracts the document’s text and layout.
* The function applies deterministic rules to identify the customer, required capabilities, and recommended subject-matter experts.
* The function uses a typed Teams connector client to post the results as an Adaptive Card in a channel.

Connector Namespace manages the SharePoint and Teams connections. The function controls file processing, document analysis, routing rules, error handling, and notification content.

## How the sample works

The .NET sample demonstrates both parts of the connector programming model: a connector trigger receives an event from SharePoint, and typed connector clients provided by the Connector SDKs perform actions against SharePoint and Teams.

The function starts when the SharePoint **When a file is created** trigger detects a new RFP. It declares the trigger using the `ConnectorTrigger` attribute and receives a typed payload containing the file’s properties:

```
[Function("OnNewFile")]
public async Task OnNewFile(
    [ConnectorTrigger] SharePointOnlineOnNewFileItemsTriggerPayload payload,
    CancellationToken cancellationToken)
{
    // Process the newly uploaded file.
}
```

Because the trigger provides file properties rather than its contents, the function uses a typed SharePoint client to retrieve the document:

```
byte[] response = await _sharePoint.GetFileContentAsync(
    Uri.EscapeDataString(siteAddress),
    fileIdentifier,
    cancellation[redacted-secret-like-value]);

byte[] document = SharePointFileContent.Decode(response);
```

The sample registers the SharePoint and Teams clients through dependency injection. Each client uses the runtime URL of its Connector Namespace connection and authenticates with `DefaultAzureCredential`:

```
services.AddSingleton(
    new SharePointOnlineClient(
        new Uri(sharePointRuntimeUrl),
        credential));

services.AddSingleton(
    new TeamsClient(
        new Uri(teamsRuntimeUrl),
        credential));
```

The function sends the document to Content Understanding’s prebuilt-layout analyzer, which extracts the document’s text and structure. It then applies deterministic C# rules to identify the customer and required capabilities and map those capabilities to predefined subject-matter expert roles.

Finally, the function creates an Adaptive Card containing the results and posts it to the configured Teams channel with the typed Teams client:

```
await _teams.PostCardToConversationAsync(
    postAs,
    postIn,
    request,
    cancellationToken);
```

Connector Namespace handles the SharePoint and Teams connections, while the function controls the document analysis, routing logic, error handling, and notification content.

### Try the sample

The [RFP intake sample](https://github.com/Azure-Samples/functions-connectors-net-rfp-intake-sharepoint-teams) includes the function code, Bicep infrastructure, Azure Developer CLI configuration, and supporting scripts. Its README explains how to test the workflow locally and deploy it to Azure.

## Common connector patterns

Managed connectors are useful when a function must react to events or perform operations in external systems. Common patterns include:

* **Event to action:** React to an event in one service and take an action in another.
* **Event to enrich to action:** Retrieve additional information related to an event before acting.
* **Event to document analysis to action:** Extract text and structure from a document, apply application rules, and send the result through another connector.
* **Event to AI to action:** Analyze event data with an AI service and write the result back through a connector.
* **Extend an existing function app:** Add connector-based integrations alongside HTTP, timer, queue, Service Bus, Event Grid, or Durable Functions workloads.

The RFP sample combines several of these patterns. A SharePoint event starts the workflow, a SharePoint action retrieves the document, Content Understanding extracts its contents, application code enriches the result, and a Teams action sends the notification.

## Closing thoughts

Managed connectors extend the external systems that can trigger your functions and the services your function code can act on. This brings services such as SharePoint, Teams, Microsoft 365, Dataverse, and many third-party systems into the Azure Functions programming model without requiring you to build the underlying webhook and OAuth infrastructure.

Choose Azure Functions with managed connectors when you want this broader integration surface in a code-first application and need custom branching, application libraries and SDKs, other Functions bindings, document or AI processing, or application-specific logic between the trigger and action.

If the workload primarily orchestrates connector operations, involves little custom code, and would benefit from a visual designer, Azure Logic Apps is usually the simpler choice.

## Resources

### Documentation

* [Overview of managed connectors in Azure Functions](https://learn.microsoft.com/azure/azure-functions/functions-connectors-overview?pivots=programming-language-csharp)
* [Azure Functions connector samples](https://github.com/Azure-Samples/functions-connectors)
* [Azure Connector Namespace overview](https://learn.microsoft.com/azure/connector-namespace/connector-namespace-overview)
* [Content Understanding prebuilt-layout analyzer](https://learn.microsoft.com/azure/ai-services/content-understanding/concepts/prebuilt-analyzers#prebuilt-layout)

### Connector SDK GitHub repositories

* [.NET SDK](https://github.com/Azure/Connectors-NET-SDK)
* [Python SDK](https://github.com/Azure/Connectors-python-sdk)
* [Node.js SDK](https://github.com/Azure/connectors-nodejs-sdk)
