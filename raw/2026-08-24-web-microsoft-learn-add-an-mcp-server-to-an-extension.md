---
source: "https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/extensions/develop/extension-mcp-server"
title: "Add an MCP server to an extension"
author: "unknown"
date_published: "2026-07-29"
date_clipped: "2026-08-24"
category: "Azure & Cloud"
source_type: "web"
---

# Add an MCP server to an extension

Source: https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/extensions/develop/extension-mcp-server

Note

An Azure Developer CLI (`azd`

) extension can expose tools to AI agents through a Model Context Protocol (MCP) server. When you add the `mcp-server`

capability, agents such as GitHub Copilot can discover and call your extension's tools. This article shows you how to add an MCP server to the Contoso Resource Tagger sample extension from the Build a sample extension quickstart. You can apply the same pattern to any extension.

Note

`azd`

extensions are currently in beta.

## How MCP servers work

The Model Context Protocol is an open standard that lets AI agents discover and call tools provided by external servers. When your extension declares the `mcp-server`

capability, `azd`

can start your extension as an MCP server and route tool requests from an agent to your extension. Your extension implements tools that the agent calls to perform tasks, such as suggesting standardized tags for a project.

## Declare the capability

Add the `mcp-server`

capability to your `extension.yaml`

manifest:

```
capabilities:
- custom-commands
- mcp-server
```

You can also add an `mcp`

section to the manifest to configure how `azd`

starts the MCP server. The `serve`

property supports `args`

and `env`

; `azd`

already knows the extension executable, so you don't specify a command:

```
mcp:
serve:
args:
- mcp
- start
```

## Add an MCP command

Add a command that starts the MCP server. `azd`

invokes this command to run your extension as an MCP server. Use an MCP server library for Go, such as mcp-go, to handle the protocol.

Create a file named

`mcp.go`

in your`internal/cmd`

directory:`package cmd import ( "context" "fmt" "github.com/mark3labs/mcp-go/mcp" "github.com/mark3labs/mcp-go/server" "github.com/spf13/cobra" ) func newMcpCommand() *cobra.Command { mcpCmd := &cobra.Command{ Use: "mcp", Short: "Model Context Protocol server commands.", Hidden: true, } mcpCmd.AddCommand(newMcpStartCommand()) return mcpCmd } func newMcpStartCommand() *cobra.Command { return &cobra.Command{ Use: "start", Short: "Starts the MCP server.", RunE: func(cmd *cobra.Command, args []string) error { s := server.NewMCPServer( "Contoso Resource Tagger", "0.1.0", ) // Register the suggest_tags tool. s.AddTool(newSuggestTagsTool()) // Serve over stdio so azd and agents can connect. return server.ServeStdio(s) }, } }`

Register the

`mcp`

command on your root command:`rootCmd.AddCommand(newMcpCommand())`

## Implement a tool

Define the tool that the AI agent calls. Add the following `suggest_tags`

tool to the same `internal/cmd/mcp.go`

file you created earlier. The `mcp`

and `server`

identifiers come from the packages already imported in that file (`github.com/mark3labs/mcp-go/mcp`

and `github.com/mark3labs/mcp-go/server`

), and the handler also uses the `context`

and `fmt`

imports. Adding the function to `mcp.go`

reuses those imports so the code compiles:

```
func newSuggestTagsTool() (mcp.Tool, server.ToolHandlerFunc) {
tool := mcp.NewTool(
"suggest_tags",
mcp.WithDescription("Suggests standardized Azure resource tags for a project."),
mcp.WithString("environment",
mcp.Description("The target environment, such as dev or prod."),
mcp.Required(),
),
)
handler := func(ctx context.Context, request mcp.CallToolRequest) (*mcp.CallToolResult, error) {
environment, err := request.RequireString("environment")
if err != nil {
return mcp.NewToolResultError(err.Error()), nil
}
suggestion := fmt.Sprintf(
"Suggested tags: environment=%s, managed-by=azd, cost-center=<required>",
environment,
)
return mcp.NewToolResultText(suggestion), nil
}
return tool, handler
}
```

## Test the MCP server

After you add the MCP server, rebuild your extension and verify the server starts:

Rebuild the extension:

`azd x build`

Start the MCP server directly to verify it runs without errors:

`azd tagger mcp start`

The server starts and listens on standard input and output. An MCP client, such as an AI agent configured to use your extension, connects to this server to call your tools.
