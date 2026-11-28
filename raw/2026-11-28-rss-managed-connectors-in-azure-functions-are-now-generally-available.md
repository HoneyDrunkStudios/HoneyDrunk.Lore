---
source: "https://techcommunity.microsoft.com/t5/apps-on-azure-blog/managed-connectors-in-azure-functions-are-now-generally/ba-p/4574143"
title: "Managed connectors in Azure Functions are now generally available"
author: "Lily-Ma"
date_published: "2026-11-17"
date_clipped: "2026-11-28"
category: "Azure & Cloud"
source_type: "rss"
---

# Managed connectors in Azure Functions are now generally available

Today, we're announcing the **general availability of managed connectors in Azure Functions**, bringing managed connectivity to business systems directly into Azure Function apps and [hosted skills.](https://learn.microsoft.com/en-us/azure/azure-functions/functions-hosted-skills)

Modern applications rarely operate within a single system. Whether you're processing documents from SharePoint, responding to customer updates in Salesforce, orreacting to changes in Microsoft Dataverse, building these integrations often means writing service-specific API code, building and managing authentication, handling event delivery and retry before you can focus on your application's business logic.

With managed connectors, developers can:

- **Connect to 1,600+ services** through the managed connector ecosystem, including Microsoft 365, Salesforce, Dataverse, Jira, Slack, Dropbox, and many more.
- **React to events** from connected services using Connector triggers.
- **Take actions** against connected services using language-native Connector SDKs.
- **Build in familiar languages**, including C#, Python, and TypeScript.
- **Scale automatically with polling triggers**, newly supported for GA

Built through close collaboration between the Azure Functions and [Azure Connector Namespace](https://techcommunity.microsoft.com/blog/integrationsonazureblog/connector-namespace-is-generally-available/4573019) teams, this integration brings managed connectors directly into the Azure Functions programming model. Connector Namespace handles connections, authentication, and service-specific integration logic, while Azure Functions provides the familiar development experience, event-driven execution, and automatic scaling. Together, they enable developers to build integrations with enterprise services using the same programming model and tools they already use for Azure Functions.

## See managed connectors in action

Suppose you're building an application that processes documents uploaded to SharePoint. When a new file arrives, you want to extract information, run custom validation, and update another business system.

Traditionally, implementing this workflow requires managing SharePoint authentication, detecting new files, and delivering those events to your application.

With managed connectors, you can use a **Connector Trigger** to invoke your function when a new event is detected. For example, here's what a connector-triggered function looks like in C#, using a SharePoint event to illustrate the programming model:

```
[Function("OnNewFile")]
    public void OnNewFile(
        [ConnectorTrigger(
            DeliveryMode = ConnectorTriggerDeliveryMode.Poll,
            Connection = "ConnectorNamespace",
            TriggerConfigName = "%OnNewFileTriggerConfigName%")]
        SharePointOnlineOnNewFileItemsTriggerPayload payload)
    {
        _logger.LogInformation("Received OnNewFile trigger ({Count} items)", payload.Body?.Value?.Count ?? 0);
    }
```

The function receives the events and runs your application logic. Connector Namespace handles the integration with the external service.

The same approach works for other supported connector events, including Outlook changes, Dataverse updates, and more.

The following is a connector-trigger function in Python showing a Outlook new calendar event:

```
@app.function_name(name="OnNewCalendarEvent")
@app.connector_trigger(
    arg_name="events",
    connection="ConnectorNamespace",
    delivery_mode=func.DeliveryMode.POLL,
    trigger_config_name="%OnNewCalendarEventTriggerConfigName%",
)
def on_new_calendar_event(events: List[office365.GraphCalendarEventClientReceive]) -> None:
    """Triggered when a new calendar event is created in Office 365."""
    logging.info("Received OnNewCalendarEvent trigger (%d items)", len(events))
```

Connector-trigger function in TypeScript showing a Dataverse row modified event:

```
import { app, DeliveryMode, InvocationContext } from '@azure/functions';

app.connectorTrigger('OnDataverseRowModified', {
    deliveryMode: DeliveryMode.Poll,
    connection: 'ConnectorNamespace',
    triggerConfigName: '%OnDataverseRowModifiedTriggerConfigName%',
    handler: async (payload: unknown, invocationContext: InvocationContext) => {
        invocationContext.log('Received OnDataverseRowModified trigger.');
        return payload;
    },
});
```

## Take actions with strongly typed Connector SDKs

While Connector triggers let your functions **react to events**, Connector SDKs let your code **call operations in connected services**. This makes it easy to combine integrations with external services, custom business logic, and Azure AI capabilities within the same application.

For example, in [this RFP intake sample](https://github.com/Azure-Samples/functions-connectors-net-rfp-intake-sharepoint-teams), an Azure Function is triggered when a new document arrives in SharePoint. It uses the SharePoint Connector SDK to retrieve the document, Azure Content Understanding to extract its contents, and the Teams Connector SDK to post a summary card to a Teams channel.

The following is simplified code from the RFP sample showing how the Teams client from the .NET Connector SDK is used to post an Adaptive Card to a channel:

*1. Register the TeamsClient in `Program.cs`*

```
services.AddSingleton(new TeamsClient(
    new Uri(teamsRuntimeUrl), new DefaultAzureCredential()));
```

*2. Inject and use it in the function:*

```
public class RfpFunctions(TeamsClient teams)
{
    [Function("OnNewFile")]
    public async Task OnNewFile(
        [ConnectorTrigger] SharePointOnlineOnNewFileItemsTriggerPayload payload,
        CancellationToken cancellationToken)
    {
        var request = new DynamicPostCardRequest
        {
            AdditionalProperties =
            {
                ["recipient"] = JsonSerializer.SerializeToElement(
                    new { groupId = "<team-id>", channelId = "<channel-id>" }),
                ["messageBody"] = JsonSerializer.SerializeToElement(new
                {
                    type = "AdaptiveCard",
                    version = "1.4",
                    body = new[] {
                        new { type = "TextBlock", text = "New RFP received!" }
                    }
                })
            }
        };

        await teams.PostCardToConversationAsync(
            "Flow bot", "Channel", request, cancellationToken);
    }
}
```

## The connector catalog

For popular connectors such as Outlook, SharePoint, and Teams, the Azure Functions Connector extension provides strongly typed event payloads, while the Connector SDKs offer strongly typed clients and models for interacting with these services. This lets developers work with familiar language-native objects when responding to events or calling connector operations, with less manual JSON parsing and API integration code.

Below are examples of popular connectors in each enterprise integration category:

- **Microsoft 365 and productivity:** Outlook, SharePoint, Teams, OneDrive for Business, Planner, and OneNote
- **CRM and business applications:** Salesforce, Pipedrive, Microsoft Dataverse, and Zendesk
- **Developer tools and collaboration:** Azure DevOps, GitHub, Jira, and Slack.
- **File storage and data services:** Dropbox, Box, FTP, Azure Blob Storage, and SQL Server.
- **Messaging and event streaming:** Azure Event Hubs, Azure Service Bus, and RSS.

For other connectors supported by Connector Namespace, developers can still use the generic Connector Trigger to receive events as JSON payloads and parse them in their function code. Together, the breadth of the managed connector ecosystem and a code-first, strongly typed developer experience make it easier to integrate business systems while retaining the flexibility of Azure Functions.

To explore the strongly typed APIs available for each connector, refer to the following resources. These references help you identify supported trigger payloads, SDK clients, operations, and models:

|  |  |
| --- | --- |
| **Capability** | **Where to find supported types** |
| Strongly typed trigger payloads | [Connector trigger payloads for Azure Functions](https://github.com/Azure/azure-functions-connector-extension/blob/main/docs/operations-functions-match.md) |
| Python Connector SDK clients | [Python API reference](https://azure.github.io/connectors-python-sdk/) |
| TypeScript Connector SDK clients | [TypeScript API reference](https://azure.github.io/Connectors-NodeJS-SDK/) |
| .NET Connector SDK clients | [.NET API reference](https://learn.microsoft.com/dotnet/api/azure.connectors.sdk?view=azure-dotnet) |

*Note: generic trigger support doesn't automatically imply Connector SDK action support. Developers can receive events from connectors across the broader catalog, but strongly typed SDK clients for taking actions are available only for supported connectors and operations.*

## New for GA: Polling triggers with automatic scaling

One of the biggest additions in this release issupport for[polling-based connector triggers](https://techcommunity.microsoft.com/blog/integrationsonazureblog/polling-triggers-in-connector-namespace-let-your-code-pull-connector-events/4573529).

Previously, managed connector triggers in Azure Functions relied on webhook delivery. With GA, developers can choose between webhook and polling mode, depending on their application's requirements. Both models use the same Connector Trigger programming model, but they differ in how events reach your function.

#### Webhook delivery

With webhook delivery, Connector Namespace sends events directly to your Function App's webhook endpoint. This is useful when you want events pushed to your application as they become available, minimizing latency.

#### Polling delivery

With polling delivery, Connector Namespace makes events available through a polling endpoint, and Azure Functions retrieves those events. Polling triggers integrate with the Azure Functions scaling infrastructure to monitor pending connector events, allowing applications to handle changing event volumes without manually managing the number of function instances.

The polling model also supports batching, so a function invocation can process multiple events.

Developers can configure settings such as:

- *MaxBatchSize*: Controls how many events can be retrieved in a batch.
- *TargetPendingEventThreshold*: Influences scaling based on the number of pending events.
- *maxPollingInterval*: Controls the maximum interval between polling attempts.

These settings provide flexibility to balance processing throughput, responsiveness, and resource consumption.

### Local development experience

For GA, we're also introducing a new**Connector Triggers experience in the** [Azure Functions extension for VS Code (v1.23.0 or higher)](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions)**,** making it easier to build and test *polling-based* connector triggers.

From *Azure Functions: Create New Project -> Connectors* tab, you can:

1. **Choose a connector and event.** Browse available connectors and select one or more events you want your function to respond to.
2. **Generate your project and code.** VS Code scaffolds an Azure Functions project with the corresponding connector trigger code, so you can start building without writing the integration boilerplate yourself.
3. **Configure resources for local testing.** When you're ready to debug with F5, VS Code guides you through creating or reusing the required Connector Namespace, connection, and trigger resources, including connection authentication and configuration.

This streamlined experience lets you go from selecting an event to running and debugging your function locally, without manually provisioning and configuring each integration resource.

For developers who prefer the command line, **Azure Functions Core Tools (v4.16.1 or higher)** **also includes a selection of connector trigger templates****,** providing another way to get started with connector-triggered functions.

## Pricing

Managed connectors in Azure Functions follow existing Azure pricing models, with **no** **additional charge for the integration itself****.** Two pricing components apply:

- **Azure Functions:** Standard [Azure Functions pricing](https://azure.microsoft.com/en-us/pricing/details/functions/) applies based on your hosting plan.
- **Managed connectors:** Connector usage is billed based on connector calls, with rates depending on whether the connector is classified as Standard or Enterprise. For details, see the [Connector Namespace pricing.](https://learn.microsoft.com/en-us/azure/connector-namespace/connector-namespace-overview#pricing)

## Get started with managed connectors

There are several ways to get started with managed connectors in Azure Functions, depending on your preferred development tools.

***Azure Developer CLI (azd)***

If you're familiar with the Azure Developer CLI, the easiest way to get started is with our sample repositories. They include examples of different connectors and triggers, along with Bicep templates that provision the required Azure resources, connector connections, and trigger configurations.

Clone a sample, follow its prerequisites, and run azd up to provision and deploy the application.

- [C# samples](https://github.com/Azure-Samples/functions-connectors-net)
- [Python samples](https://github.com/Azure-Samples/functions-connectors-python)
- [TypeScript samples](https://github.com/Azure-Samples/functions-connectors-typescript)

***Visual Studio Code***

Use the Azure Functions extension for VS Code to browse connectors and events in the Template Gallery, scaffold your project, and get guided setup for the connector resources and trigger configurations needed for local testing.

***Azure Functions Core Tools***

If you prefer working from the command line, Azure Functions Core Tools also offers a selection of connector trigger templates to help you scaffold your project. Follow the instructions at [aka.ms/connectortrigger](https://aka.ms/connectortrigger) to set up the required resources and configurations to test the scaffolded project.

## More references

To learn more about managed connectors in Azure Functions, explore the following resources:

- [Use managed connectors in Azure Functions](https://learn.microsoft.com/azure/azure-functions/functions-connectors-overview?pivots=programming-language-csharp)
- [Azure Functions Connectors Samples](https://github.com/azure-samples/functions-connectors)
- [Azure Connector Namespace Overview](https://learn.microsoft.com/azure/connector-namespace/connector-namespace-overview)
- [Browse available managed connectors](https://learn.microsoft.com/connectors/connector-reference/)

Connector SDKs:

- [.NET SDK](https://github.com/Azure/Connectors-NET-SDK)
- [Python SDK](https://github.com/Azure/Connectors-python-sdk)
- [Node.js SDK](https://github.com/Azure/Connectors-nodejs-sdk)
