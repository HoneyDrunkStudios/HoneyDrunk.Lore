---
source: "https://devblogs.microsoft.com/dotnet/mcp-csharp-sdk-2025-06-18-update"
title: "MCP C# SDK Gets Major Update: Support for Protocol Version 2025-06-18"
author: "Mike Kistler"
date_published: "2025-07-22"
date_clipped: "2026-06-18"
category: ".NET Ecosystem"
source_type: "web"
---

# MCP C# SDK Gets Major Update: Support for Protocol Version 2025-06-18

Source: https://devblogs.microsoft.com/dotnet/mcp-csharp-sdk-2025-06-18-update

The Model Context Protocol (MCP) continues to evolve, and we’re excited to announce that the MCP C# SDK now supports the latest specification version 2025-06-18 . This update brings significant new capabilities to .NET developers building AI applications, including an improved authentication protocol, elicitation support, structured tool output, and support for resource links in tool responses.
Whether you’re building AI assistants, automation tools, or integrating AI capabilities into existing .NET applications, these new features will help you create more robust and secure solutions.
Here’s a rundown of the new features and how to access them with the MCP C# SDK.
Improved Authentication Protocol
The 2025-06-18 specification introduces a new authentication protocol that enhances security and flexibility for AI applications. The new protocol separates the roles of authentication server and resource server, allowing easier integration with existing OAuth 2.0 and OpenID Connect providers.
This is a large topic and has already been covered in detail in a separate blog post by Den Delimarsky, OAuth In The MCP C# SDK: Simple, Secure, Standard .
Elicitation: Interactive User Engagement
One of the most significant additions is the elicitation feature, which allows servers to request additional information from users during interactions. This enables more dynamic and interactive AI experiences, making it easier to gather necessary context before executing tasks.
Server Support for Elicitation
Servers request structured data from users with the ElicitAsync extension method on IMcpServer .
The C# SDK registers an instance of IMcpServer with the dependency injection container,
so tools can simply add a parameter of type IMcpServer to their method signature to access it.
The MCP Server must specify the schema of each input value it is requesting from the user.
Only primitive types (string, number, boolean) are supported for elicitation requests.
The schema may include a description to help the user understand what is being requested.
The server can request a single input or multiple inputs at once.
To help distinguish multiple inputs, each input has a unique name.
The following example demonstrates how a server could request a boolean response from the user.
[McpServerTool, Description("A simple game where the user has to guess a number between 1 and 10.")]
public async Task<string> GuessTheNumber(
IMcpServer server, // Get the McpServer from DI container
CancellationToken token
)
{
// First ask the user if they want to play
var playSchema = new RequestSchema
{
Properties =
{
["Answer"] = new BooleanSchema()
}
};
var playResponse = await server.ElicitAsync(new ElicitRequestParams
{
Message = "Do you want to play a game?",
RequestedSchema = playSchema
}, token);
// Check if user wants to play
if (playResponse.Action != "accept" || playResponse.Content?["Answer"].ValueKind != JsonValueKind.True)
{
return "Maybe next time!";
}
// remaining implementation of GuessTheNumber method
Client Support for Elicitation
Elicitation is an optional feature so clients declare their support for it in their capabilities as part of the initialize request. In the MCP C# SDK, this is done by configuring an ElicitationHandler in the McpClientOptions :
McpClientOptions options = new()
{
ClientInfo = new()
{
Name = "ElicitationClient",
Version = "1.0.0"
},
Capabilities = new()
{
Elicitation = new()
{
ElicitationHandler = HandleElicitationAsync
}
}
};
The ElicitationHandler is an asynchronous method that will be called when the server requests additional information.
The ElicitationHandler must request input from the user and return the data in a format that matches the requested schema.
This will be highly dependent on the client application and how it interacts with the user.
If the user provides the requested information, the ElicitationHandler should return an [ElicitResult] with the action set to “accept” and the content containing the user’s input.
If the user does not provide the requested information, the ElicitationHandler should return an [ElicitResult] with the action set to “reject” and no content.
Below is an example of how a console application might handle elicitation requests.
Here’s an example implementation:
async ValueTask<ElicitResult> HandleElicitationAsync(ElicitRequestParams? requestParams, CancellationToken token)
{
// Bail out if the requestParams is null or if the requested schema has no properties
if (requestParams?.RequestedSchema?.Properties == null)
{
return new ElicitResult(); // New ElicitResult with default Action "reject"
}
// Process the elicitation request
if (requestParams?.Message is not null)
{
Console.WriteLine(requestParams.Message);
}
var content = new Dictionary<string, JsonElement>();
// Loop through requestParams.requestSchema.Properties dictionary requesting values for each property
foreach (var property in requestParams.RequestedSchema.Properties)
{
if (property.Value is ElicitRequestParams.BooleanSchema booleanSchema)
{
Console.Write($"{booleanSchema.Description}: ");
var clientInput = Console.ReadLine();
bool parsedBool;
if (bool.TryParse(clientInput, out parsedBool))
{
content[property.Key] = JsonSerializer.Deserialize<JsonElement>(JsonSerializer.Serialize(parsedBool));
}
}
else if (property.Value is ElicitRequestParams.NumberSchema numberSchema)
{
Console.Write($"{numberSchema.Description}: ");
var clientInput = Console.ReadLine();
double parsedNumber;
if (double.TryParse(clientInput, out parsedNumber))
{
content[property.Key] = JsonSerializer.Deserialize<JsonElement>(JsonSerializer.Serialize(parsedNumber));
}
}
else if (property.Value is ElicitRequestParams.StringSchema stringSchema)
{
Console.Write($"{stringSchema.Description}: ");
var clientInput = Console.ReadLine();
content[property.Key] = JsonSerializer.Deserialize<JsonElement>(JsonSerializer.Serialize(clientInput));
}
}
// Return the user's input
return new ElicitResult
{
Action = "accept",
Content = content
};
}
Structured Tool Output
Another important addition in the 2025-06-18 spec is support for structured tool output .
Previously, tool results were allowed to contain structured data but the host/LLM had to perform the parsing and interpretation
without any guidance from the tool itself.
Now, tools can return structured content that is explicitly defined, allowing AI models to better understand and process the output.
The C# SDK supports this by allowing tools to specify that their output is structured, with the UseStructuredContent parameter
of the McpServerTool attribute.
[McpServerTool(UseStructuredContent = true), Description("Gets a list of structured product data with detailed information.")]
public static List<Product> GetProducts(int count = 5)
The C# SDK will generate a JSON schema for the tool’s output based on the return type of the method
and will include this schema in the tool’s metadata. Here is an example of the response to a tools/list call
that shows the output schema for the get_products tool:
{
"result": {
"tools": [
{
"name": "get_products",
"description": "Gets a list of structured product data with detailed information.",
"inputSchema": {
"type": "object",
"properties": {
"count": {
"type": "integer",
"default": 5
}
}
},
"outputSchema": {
"type": "object",
"properties": {
"result": {
"type": "array",
"items": {
"type": "object",
"properties": {
"id": {
"description": "Unique identifier for the product",
"type": "integer"
},
"name": {
"description": "Name of the product",
"type": "string"
},
...
And when the tool is called, the tool response will include the structured output in the result.structuredContent field:
{
"result": {
"content": [
{
"type": "text",
"text": "<text content>"
}
],
"structuredContent": {
"result": [
{
"id": 1,
"name": "Laptop Pro",
"description": "High-quality laptop pro for professional use",
"price": 278,
"category": "Electronics",
"brand": "TechCorp",
"inStock": 24,
"rating": 4.3,
"features": [
"Durable construction",
"Modern design",
"Easy to use"
],
"specifications": {
"Weight": "1 lbs",
"Dimensions": "12x12x2 inches",
"Warranty": "2 years"
}
},
...
]
}
},
"id": 2,
"jsonrpc": "2.0"
}
Resource Links in Tool Results
Tools can now include resource links in their results, enabling better resource discovery and navigation.
This is particularly useful for tools that create or manage resources, allowing clients to easily access and interact with those resources.
In the following example, a tool creates a resource with a random value and returns a link to this resource:
[McpServerTool]
[Description("Creates a resource with a random value and returns a link to this resource.")]
public async Task<CallToolResult> MakeAResource()
{
int id = new Random().Next(1, 101); // 1 to 100 inclusive
var resource = ResourceGenerator.CreateResource(id);
var result = new CallToolResult();
result.Content.Add(new ResourceLinkBlock()
{
Uri = resource.Uri,
Name = resource.Name
});
return result;
}
Schema Improvements
Beyond the major features, several schema improvements enhance the developer experience:
Enhanced Metadata Support
The _meta field is now available on more interface types, providing better extensibility:
public class CustomTool : Tool
{
public ToolMetadata Meta { get; set; } = new()
{
["version"] = "1.0.0",
["author"] = "Your Name",
["category"] = "data-analysis"
};
}
Human-Friendly Titles
Tools, Resources, and Prompts all now support separate name and title fields.
In the MCP C# SDK, you can specify a title for your tool using the Title property of the McpServerTool attribute.
[McpServerToolType]
public class EchoTool
{
[McpServerTool(Name = "echo", Title = "Echo Tool")]
[Description("Echoes the message back to the client.")]
public static string Echo(string message) => $"Echo: {message}";
}
This produces the following tool metadata in the tools/list response:
"tools": [
{
"name": "echo",
"title": "Echo Tool",
"description": "Echoes the message back to the client.",
"inputSchema": {
"type": "object",
"properties": {
"message": {
"type": "string"
}
},
"required": [
"message"
]
},
The name and title parameters of the McpServerTool attribute are optional.
If not specified, the name defaults to the lower snake case form of the method name and the title defaults to an empty string.
Getting Started with the Updated SDK
To start using these new features, update your MCP C# SDK package:
dotnet add package ModelContextProtocol --prerelease
When implementing these new capabilities, consider the following best practices:
Always implement proper OAuth flows for production applications
Use resource indicators to prevent token misuse
Validate all elicited user input
Follow the security best practices outlined in the specification
What’s Next
The MCP ecosystem continues to grow, and we’re committed to keeping the C# SDK up-to-date with the latest specification changes.
The MCP C# SDK is open source and we welcome contributions! Whether you’re reporting bugs, suggesting features, or contributing code, your involvement helps make the SDK better for everyone.
GitHub Repository : modelcontextprotocol/csharp-sdk
Documentation : MCP C# SDK Docs
Samples : MCP C# Samples
Summary
The MCP C# SDK’s support for protocol version 2025-06-18 brings powerful new capabilities to .NET developers building AI applications. With the new authentication protocol, elicitation support, structured tool output, and support for resource links in tool results, you can create more sophisticated and secure AI integrations than ever before.
Start exploring these new features today by updating your SDK and reviewing the updated documentation. The future of AI application development with .NET just got brighter!
Get Started with MCP C# SDK
