---
source: "https://aos.owasp.org/spec/instrument/extend_mcp/"
title: "Instrument MCP - Agent Observability Standard"
author: "OWASP Agent Observability Standard"
date_published: "unknown"
date_clipped: "2026-06-08"
category: "Security & Ethical Hacking"
source_type: "web"
---

# Instrument MCP - Agent Observability Standard

Source: https://aos.owasp.org/spec/instrument/extend_mcp/

# Extending MCP

## MCP protocol

The Model Context Protocol ([MCP](https://modelcontextprotocol.io/introduction)) is an open standard that simplifies how AI models, particularly Large Language Models (LLMs) and agents, interact with external data sources, tools, and APIs. It's designed to provide a standardized way for AI agents to connect with the real world, making it easier to build AI applications that can access and use external information.

MCP is gaining popularity world-wide and is being adopted and integrated almost everywhere, security and observability must be implemented to prevent unwanted bad consequences.

In the same manner as AOS standardize security for non-standardize access and use of tools and data, it also extends MCP protocol to allow secure usage and implement security controls.

## MCP support

AOS extension for MCP is used as a **transport** for MCP communications between the agent and the guardian agent. Meaning AOS understands and delivers MCP message as is.

Securing MCP means securing outbound and inbound communications/messages from the agent (using MCP client) to the MCP server and vice versa.


#### To extend MCP protocol:

- Agents using MCP
use AOS as a transport protocol to deliver MCP messages to the guardian agent using*must*[MCP protocol hooks](https://aos.owasp.org/hooks/#mcp-protocol-hooks). - Agents using MCP
understand and enforce AOS responses.*must*

#### The following flow explains how this should be done:

- Agent
**A**prepares (using MCP client) MCP-compliant message. - Agent
**A**uses AOS as a transport to send the message to the guardian agent. - The guardian agent understands and processes the MCP transported message and send the result back to agent
**A**. - Agent
**A**interprets and enforces the response from guardian agent. - In case response is
`allow`

, agent**A**sends the MCP message to MCP server. - MCP server processes the message and sends back to agent
**A**the response. - Agent
**A**uses AOS as a transport to send the MCP response to the guardian agent. - The guardian agent understands and processes the MCP transported response and send the result back to agent
**A**. - Agent
**A**interprets and enforces the response from guardian agent.

## Examples

### Scenario: Agent **A** asks MCP server for the weather and guardian agent respond with allow

#### 1. Agent **A** prepares MCP `tools/call`

message

{
"jsonrpc": "2.0",
"id": 1,
"method": "tools/call",
"params": {
"arguments": {
"city": "Barcelona"
},
"name": "get_weather"
}
}


#### 2. Agent **A** uses ASOP as a transport and sends MCP `protocols/MCP`

message

{
"jsonrpc": "2.0",
"id": 70,
"method": "protocols/MCP",
"params": {
"jsonrpc": "2.0",
"id": 1,
"method": "tools/call",
"params": {
"arguments": {
"city": "Barcelona"
},
"name": "get_weather"
}
}
}


#### 3. Guardian agent sends `allow`

response to agent **A**

{
"jsonrpc": "2.0",
"id": 70,
"result": {
"decision": "allow",
"message": "Allow tools/call.",
"reasoning": "I understand that this is an MCP message. An agent is asking the weather. Nothing suspicious here."
}
}


### Scenario: Agent **A** asks MCP server for to send email with sensitive data and guardian agent respond with modify

#### 1. Agent **A** prepares MCP `tools/call`

message

{
"jsonrpc": "2.0",
"id": 1,
"method": "tools/call",
"params": {
"arguments": {
"to": "[[email protected]](https://aos.owasp.org/cdn-cgi/l/email-protection)",
"subject": "",
"body": ""
},
"name": "send_email"
}
}


#### 2. Agent **A** uses ASOP as a transport and sends MCP `protocols/MCP`

message

{
"jsonrpc": "2.0",
"id": 80,
"method": "protocols/MCP",
"params": {
"jsonrpc": "2.0",
"id": 1,
"method": "tools/call",
"params": {
"arguments": {
"to": "[[email protected]](https://aos.owasp.org/cdn-cgi/l/email-protection)",
"from": "[[email protected]](https://aos.owasp.org/cdn-cgi/l/email-protection)",
"subject": "Employee Salary Raise Request",
"body": "Hi, I would like to ask for a salary raise for emplyee #12222. The current salary is 200000$, the requested salary is 300000$. Let's have a meeting discuss this."
},
"name": "send_email"
}
}
}


#### 3. Guardian agent sends `modify`

response to agent **A**

{
"jsonrpc": "2.0",
"id": 80,
"result": {
"decision": "modify",
"message": "Modified data for tools/call.",
"reasoning": "I understand that this is an MCP message. An agent is asking to send an email with sensitive info, I need to mask it first.",
"modifiedRequest": {
"jsonrpc": "2.0",
"id": 80,
"method": "protocols/MCP",
"params": {
"jsonrpc": "2.0",
"id": 1,
"method": "tools/call",
"params": {
"arguments": {
"to": "[[email protected]](https://aos.owasp.org/cdn-cgi/l/email-protection)",
"from": "[[email protected]](https://aos.owasp.org/cdn-cgi/l/email-protection)",
"subject": "Employee Salary Raise Request",
"body": "Hi, I would like to ask for a salary raise for emplyee #12222. The current salary is **********$, the requested salary is **********$. Let's have a meeting discuss this."
},
"name": "send_email"
}
}
}
}
}


### Scenario: Agent **A** asks MCP server for to send email with sensitive data to an outsider and guardian agent respond with deny

#### 1. Agent **A** prepares MCP `tools/call`

message

{
"jsonrpc": "2.0",
"id": 1,
"method": "tools/call",
"params": {
"arguments": {
"to": "[[email protected]](https://aos.owasp.org/cdn-cgi/l/email-protection)",
"subject": "Financial info",
"body": "The ARR for the company for year 2024 was 100000000000$ "
},
"name": "send_email"
}
}


#### 2. Agent **A** uses ASOP as a transport and sends MCP `protocols/MCP`

message

{
"jsonrpc": "2.0",
"id": 100,
"method": "protocols/MCP",
"params": {
"jsonrpc": "2.0",
"id": 1,
"method": "tools/call",
"params": {
"arguments": {
"to": "[[email protected]](https://aos.owasp.org/cdn-cgi/l/email-protection)",
"subject": "Financial info",
"body": "The ARR for the company for year 2024 was 100000000000$ "
},
"name": "send_email"
}
}
}
