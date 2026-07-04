---
source: "https://developers.googleblog.com/build-agentic-full-stack-apps-with-genkit"
title: "Build agentic full-stack apps with Genkit"
author: "Chris Gill"
date_published: "2026-07-01"
date_clipped: "2026-07-04"
category: "AI / LLM Research & Tooling"
source_type: "web"
---

# Build agentic full-stack apps with Genkit

Source: https://developers.googleblog.com/build-agentic-full-stack-apps-with-genkit

[Genkit](https://genkit.dev/) is an open-source framework for **building full-stack, AI-powered and agentic applications for any platform** with support for TypeScript, Go, Dart, and Python. Some of the most compelling AI features are conversational, like a support assistant that remembers the ticket or a copilot that works across several turns. Each needs more than a single `generate()`

call, and building one today means wiring up message history, the tool loop, streaming, persistence, and a frontend protocol by hand. That plumbing repeats on every project and has little to do with what makes your app distinct.

Genkit solves this with the [ Agents API](https://genkit.dev/docs/agents/overview/), which packages all of that behind one interface. You define an agent on the server, then drive it with the same

`chat()`

API whether it runs in process or behind an HTTP endpoint.**>** The Agents API is in **preview** today in TypeScript and Go. It can introduce breaking changes in minor version releases.

An agent needs a name and a system prompt to start. From there you add tools, state, and a session store as the feature grows.

```
import genkitx "github.com/firebase/genkit/go/genkit/exp"
g := genkit.Init(ctx,
genkit.WithPlugins(&googlegenai.GoogleAI{}),
genkit.WithExperimental(), // Enables preview features like Agents API.
)
assistant := genkitx.DefineAgent(g, "assistant",
aix.InlinePrompt{
ai.WithModelName("googleai/gemini-flash-latest"),
ai.WithSystem("You are a helpful assistant."),
},
)
out, err := assistant.RunText(ctx, "Hello. What can you do?")
if err != nil {
log.Fatal(err)
}
fmt.Println(out.Message.Text())
```

The same agent object is flexible and can handle a one-shot reply, a streamed turn, a paused tool call, and a multi-turn conversation. You do not reach for a different abstraction as the feature grows.

Every conversation needs continuity between turns, and you decide who owns it.

Add a `store`

and the agent becomes **server-managed**. The server persists messages, custom state, and artifacts as snapshots, and clients continue by sending back a session ID. Choose this for persistent chat apps, shared devices, and any workflow where the client should not carry the whole conversation.

```
import firebasex "github.com/firebase/genkit/go/plugins/firebase/exp"
import genkitx "github.com/firebase/genkit/go/genkit/exp"
store, err := firebasex.NewFirestoreSessionStore[WeatherState](ctx, g,
firebasex.WithCollection("snapshots"),
firebasex.WithCheckpointInterval(10),
)
if err != nil {
log.Fatal(err)
}
weatherAgent := genkitx.DefineAgent(g, "weatherAgent",
aix.InlinePrompt{
ai.WithSystem("Answer weather questions. Ask for a location when one is missing."),
ai.WithTools(getWeather),
},
aix.WithSessionStore(store),
)
```

The store you configure decides where snapshots live. For production, Firestore gives you a managed, multi-instance database that several server instances can share. Genkit also ships lighter stores for local work and lets you implement your own, which the section below covers.

Leave the store off and the agent is client-managed: the server returns the full state and the client sends it back on the next turn. Use this when your app already owns persistence or you need stateless server deployments.

Every successful server-managed turn writes a snapshot, so you can resume the latest state by `sessionId`

or branch from an exact point in history by `snapshotId`

. Branching lets a user explore an alternative from any saved moment without disturbing the original thread.

```
// Continue the latest state in a conversation.
out, err := weatherAgent.RunText(ctx, "Continue where we left off.",
aix.WithSessionID[WeatherState]("user-session-123"),
)
// Or branch from a specific saved point.
branch, err := weatherAgent.RunText(ctx, "Revise this plan for a smaller budget.",
aix.WithSnapshotID[WeatherState](approvedPlanSnapshotID),
)
```

Alongside message history, an agent carries two more kinds of state. **Custom state** is your typed application data, the compact control and UI values that drive the next turn, such as workflow status, a task list, or selected entities. **Artifacts** are generated outputs the user may inspect, download, or version on their own, such as a report, a patch, or an itinerary. A tool updates either one through the active session, and Genkit streams the changes to the client as they happen.

Every agent is already a servable action, so putting one behind an HTTP endpoint is a few lines. The route helpers return descriptors you mount on a standard http.ServeMux, and they wire up the turn endpoint plus the snapshot and abort companions for you.

```
import genkitx "github.com/firebase/genkit/go/genkit/exp"
mux := http.NewServeMux()
for _, route := range genkitx.AllAgentRoutes(g) {
mux.HandleFunc(route.Pattern(), route.Handler())
}
log.Fatal(http.ListenAndServe(":8080", mux))
```

That same wire protocol is what the client below speaks, so a JavaScript or Go backend serves any client identically.

The piece that ties your server and client together is the remote agent. `remoteAgent()`

returns a handle with the **same** `chat()`

** interface** as a local agent, so the code that drives an agent in your backend tests is the code that drives it from the browser. There is no separate request and response protocol to design, and no streaming format to invent.

We are launching a JavaScript client, so a web frontend can talk to the same agent endpoint. The following is an example of how to connect to a remote agent from a TypeScript frontend.

```
import { remoteAgent } from 'genkit/beta/client';
const agent = remoteAgent<WeatherState>({
url: 'http://localhost:8080/api/weatherAgent',
});
const chat = agent.chat();
const res = await chat.send('Weather in Tokyo?');
console.log(res.text);
```

The client speaks one wire protocol over the agent route, so it works the same against a JavaScript or a Go backend. It resolves dynamic auth headers per request, applies streamed state patches, and continues the next turn with a session ID, a snapshot ID, or client-managed state, whichever your agent uses.

Streaming is built into the same interface. `sendStream()`

gives you a chunk stream and a final response, and each chunk can carry text, custom state, or an artifact as it is produced.

```
const turn = agent.chat().sendStream('Write a long report.');
for await (const chunk of turn.stream) {
if (chunk.text) process.stdout.write(chunk.text);
if (chunk.custom) updateStatus(chunk.custom);
if (chunk.artifact) renderArtifact(chunk.artifact);
}
const res = await turn.response;
```

If you already have apps that use the [Vercel AI SDK UI](https://ai-sdk.dev/docs/ai-sdk-ui) library, the `@genkit-ai/vercel-ai`

package provides an adapter for its `useChat`

hook. The `GenkitChatTransport`

adapter connects `useChat`

to your Genkit agent, so you can assemble the interface from Vercel's [AI Elements](https://elements.ai-sdk.dev/) components while getting all the benefits of Genkit on the backend.

A tool can pause an agent and hand control back to the user. The model decides outside input is needed, the tool interrupts, and the client approves, rejects, or supplies the missing value before the turn continues. This is how you put a human in the loop before a payment, a deployment, or any action you do not want to run automatically.

```
import genkitx "github.com/firebase/genkit/go/genkit/exp"
import "github.com/firebase/genkit/go/ai/exp/tool"
runShell := genkitx.DefineInterruptibleTool(g, "run_shell",
"Run a shell command after a safety check.",
func(ctx context.Context, input ShellInput, confirm *Confirmation) (ShellOutput, error) {
if isRisky(input.Command) {
if confirm == nil {
return ShellOutput{}, tool.Interrupt(ShellInterrupt{
Command: input.Command,
Reason: "The command can modify files.",
})
} else if !confirm.Approved {
return ShellOutput{}, errors.New("user rejected shell command execution")
}
}
return execute(input.Command)
},
)
```

The turn finishes with an `interrupted`

reason and the paused request on the response. The client resumes once the user answers, and the runtime validates the resume payload against session history so a tool cannot be tricked into running with forged input.

Some turns take longer than a user wants to wait. With server-managed state, a client can detach a turn, close the tab, and reconnect later by snapshot ID. The agent keeps working on the server, writing progress to a pending snapshot that another session can poll, wait on, or abort.

```
const chat = reportAgent.chat({ sessionId: 'report-123' });
const task = await chat.detach('Write the quarterly market report.');
// Persist this so any client can reconnect to the work later.
savePendingSnapshot(task.snapshotId);
for await (const snapshot of task.poll({ intervalMs: 1000 })) {
renderStatus(snapshot.status);
if (snapshot.status === 'completed') renderMessages(snapshot.state.messages);
}
```

This makes long research jobs, multi-step planning, and tool-heavy workflows practical without holding a connection open or building a separate job queue.

When one prompt cannot do everything well, you can split work across specialized agents and let an orchestrator combine their results. The `Agents`

middleware injects a delegation tool for each sub-agent, so the orchestrator model can route parts of a request to the right specialist. Subagents with Genkit give you full control and the ability to implement your own orchestration.

```
import middlewarex "github.com/firebase/genkit/go/plugins/middleware/exp"
coordinator := genkit.DefineAgent(g, "coordinator",
aix.InlinePrompt{
ai.WithSystem("Delegate to specialists, inspect their results, then answer the user."),
ai.WithUse(
&middlewarex.Agents{
Agents: []aix.AgentRef{researcher.Ref(), coder.Ref()},
MaxDelegations: 5,
ArtifactStrategy: middlewarex.ArtifactStrategySession,
},
&middlewarex.Artifacts{Readonly: true},
),
},
)
```

Delegation shows up as ordinary tool activity in the orchestrator's stream, and specialist artifacts can merge into the parent session so the final answer can build on what each specialist produced.

Genkit agents are an application primitive, built to live inside a full-stack, user-facing app. Consider the [Agent Development Kit (ADK)](https://google.github.io/adk-docs/) instead when:

Server-managed agents store snapshots through a session store, and Genkit ships several so you can match the store to where you are running:

Agents are first-class in the Genkit [Developer UI](https://genkit.dev/docs/devtools/). The new **Agent Runner** lets you start a conversation, send turns, watch streamed output and state updates, drive tool interrupts, and inspect snapshots, all without writing a client. It is the fastest way to exercise an agent while you are building it and to reproduce a conversation when you are debugging one.

The Agents API turns the repeated plumbing of conversational, full-stack AI into something you configure rather than rebuild. Define an agent on the server, give it a store when you want persistence, and drive it from your frontend with the same chat() interface through remoteAgent().

Head to the [Full-stack agents documentation](https://genkit.dev/docs/agents/overview/) to dive in, or [get started with Genkit](https://genkit.dev/docs/get-started/) if you are new to the framework. The API is in Beta, so we want your feedback: [file an issue](https://github.com/genkit-ai/genkit/issues) with what you build and what you would change.

Happy coding! 🚀
