---
source: "https://devblogs.microsoft.com/dotnet/routing-and-failover-for-microsoft-extensions-ai/"
title: "Routing and Failover for Microsoft.Extensions.AI"
author: ".NET Blog"
date_published: "2026-08-13"
date_clipped: "2026-08-14"
category: ".NET Ecosystem"
source_type: "rss"
---

# Routing and Failover for Microsoft.Extensions.AI

Source: https://devblogs.microsoft.com/dotnet/routing-and-failover-for-microsoft-extensions-ai/

As AI adoption scales, cost, uptime, and latency become first-class constraints on application architecture. Routing between models or providers is a lever on all three at once.
These new Microsoft.Extensions.AI primitives handle it directly: route by message content, fail over when a provider goes down, or build your own policy on the same abstractions, all as IChatClient implementations.
Four new experimental types cover the main scenarios:
RoutingChatClient : the base class, an IChatClient that selects and forwards to another client per request.
SemanticRoutingChatClient : a RoutingChatClient that routes by content, using embedding similarity against app-provided example utterances.
FailoverChatClient : an abstract RoutingChatClient that adds a retry loop, reselecting when an attempt fails before committing any output, serving as a base class for different failover strategies.
OrderedFailoverChatClient : a concrete FailoverChatClient that walks a list of clients in order.
RoutingChatClient
RoutingChatClient is an abstract IChatClient that calls SelectClientAsync on each request, forwards the call to the returned client, and propagates the response.
The simplest way to use it is RoutingChatClient.Create , which takes a callback:
var router = RoutingChatClient.Create((context, ct) =>
new(isComplexRequest(context) ? powerfulClient : cheapClient));
For stateful or more advanced routing policies, derive from RoutingChatClient and override the SelectClientAsync method:
class MyRouter : RoutingChatClient
{
protected override ValueTask<IChatClient> SelectClientAsync(
RoutingContext context, CancellationToken ct)
{
// ...
}
}
Each call to GetResponseAsync or GetStreamingResponseAsync creates a RoutingContext containing the request messages and a clone of ChatOptions . The caller’s own options object is never handed to a client, and changes they make after the call starts aren’t observed.
This splits option shaping into two levels:
Request-level options live on context.ChatOptions . Changes persist across the request, including any later attempt if a client fails.
Route-level options belong on the client, typically a ConfigureOptionsChatClient wrapper, which clones the request options and applies its own values on top.
SemanticRoutingChatClient
SemanticRoutingChatClient , inspired by Aurelio Labs’ semantic router , routes by message meaning. You provide a set of example utterances per client, and at runtime the last user message is embedded and matched against them. The client with the highest similarity score above the threshold wins; if nothing clears it, the configured defaultClient is used.
var router = new SemanticRoutingChatClient(
embeddingGenerator,
clientProfiles: new Dictionary<IChatClient, IReadOnlyList<string>>
{
[codingClient] = ["write code", "fix this bug", "refactor this function"],
[creativeClient] = ["write a story", "brainstorm names", "generate a poem"],
},
defaultClient: generalClient,
scoreThreshold: 0.3f);
Profile embeddings are generated lazily and cached. The first routed request embeds every profile utterance in one batched call and keeps the vectors, so later requests only embed the incoming message and compare against them.
Key options:
scoreThreshold : minimum score to select a profiled client. Requests that don’t clear it go to defaultClient .
topK : how many top-matching utterances per request to consider when aggregating scores. Default is 1 .
scoreAggregation : Mean or Sum across the top-K matches. Affects what threshold values are valid.
leaveOpen : by default SemanticRoutingChatClient owns the clients and embedding generator and disposes them. Set this to true to opt out.
Another reasonable starting point is topK: 5 with Mean aggregation, which is what Aurelio Labs’ semantic router uses as its default. Averaging several matches is steadier than betting on the single closest one, which can swing on a lucky phrasing match, and Mean keeps scores on the same -1 to 1 scale, so a threshold like 0.3 means the same thing whatever topK is. Give each client enough utterances that five matches are actually available.
Before routing every turn independently
Reasoning models often return their reasoning as an opaque, provider-specific artifact. Encrypted content the provider needs back to continue, or a continuation token tied to its own session. Switching providers mid-conversation strands it.
A new provider or model within the same provider means a fresh prompt with no warm cache to reuse; you eat the full compute cost of the prefix again on every switch.
If a conversation is going to stay on one classification, decide that once and keep it there rather than re-routing on every turn (see “Sticky selection” below).
FailoverChatClient
FailoverChatClient extends RoutingChatClient with a retry loop. When a selected client fails before any streaming output is exposed to the caller, it calls SelectClientAsync again and retries. After output starts flowing to the caller, failure becomes terminal: there’s no mid-stream recovery. With non-streaming responses, this is simpler: there’s no output to commit partway through, so an attempt either returns a response or fails outright.
Derived classes implement SelectClientAsync to supply the next client and override OnRoutingUpdateAsync to observe each attempt. The update fires after every client invocation (success, failure, or abandonment) with a FailoverChatClientAttempt that contains:
Client ( IChatClient ): the client that was invoked
Duration ( TimeSpan ): time spent actively invoking the client (caller processing time excluded for streaming)
Exception ( Exception? ): the exception observed, if any
ResponseCompleted ( bool ): whether the response finished successfully
OutputCommitted ( bool ): whether any streaming update reached the caller
TimeToFirstUpdate ( TimeSpan? ): time to first streaming update, if applicable
Duration and TimeToFirstUpdate let you track provider performance over time: circuit-break a slow provider, score candidates by historical latency, or feed into an observability pipeline. The hook fires on every attempt, not just failures, so the data reflects successes too.
The isTerminal flag passed alongside tells you whether the base class will select again after this update returns. A nonterminal update means a failed attempt with more retries to come, and state changes made in the override are visible to the next SelectClientAsync call.
Exceptions from your own code end the request without a report. If SelectClientAsync throws, no update is raised for it. If OnRoutingUpdateAsync throws during a nonterminal update, no retry follows and no further update is raised. Either way you get no callback to clean up in, so release any per-request state before throwing.
MaximumAttemptsPerRequest caps the total number of invocations per request, and once the request’s cancellation token is canceled, no reselection occurs.
OrderedFailoverChatClient
OrderedFailoverChatClient is the ready-to-use FailoverChatClient implementation. Pass it a ranked list of clients and it walks them in order: first client fails, try the second, and so on. When every client has failed, the last exception is rethrown.
var failover = new OrderedFailoverChatClient([primaryClient, backupClient, lastResortClient]);
The same client can appear more than once; it will be invoked once per position. MaximumAttemptsPerRequest can cap the list short if you don’t want to exhaust every option on every failure. By default OrderedFailoverChatClient owns the clients and disposes them; pass leaveOpen: true to opt out.
A fresh RoutingContext is created per request, so it works as a request-scoped key: share state between SelectClientAsync and OnRoutingUpdateAsync without inventing your own request ID, whether that’s a client index, a running attempt count, or a route name as in the sticky selection example below.
Building on the primitives
The four built-in types cover common cases, but custom routers can also manage application state or treat different configurations of one model as separate routes.
Sticky selection
You might be tempted to key sticky routing on ChatOptions.ConversationId , but that ID belongs to a provider’s stateful conversation and may not transfer to another client. Use an application-owned session ID instead.
For multi-turn conversations, the application can keep the selected route in its existing session state. The router itself can be reused across sessions. Name the routes, pass the application’s session ID through ChatOptions.AdditionalProperties , and store the chosen name in IDistributedCache (for example, Redis):
var routes = new Dictionary<string, IChatClient>
{
["fast"] = fastClient,
["deep"] = deepClient,
};
var options = new ChatOptions
{
AdditionalProperties = new() { ["routing-session-id"] = sessionId },
};
class StickyRouter : FailoverChatClient
{
private readonly IReadOnlyDictionary<string, IChatClient> _routes;
private readonly ConcurrentDictionary<RoutingContext, string> _pending = new();
private readonly IDistributedCache _cache;
public StickyRouter(IReadOnlyDictionary<string, IChatClient> routes, IDistributedCache cache)
{
_routes = routes.ToDictionary(r => r.Key, r => r.Value);
_cache = cache;
MaximumAttemptsPerRequest = 1;
}
protected override async ValueTask<IChatClient> SelectClientAsync(
RoutingContext context, CancellationToken ct)
{
string route = await _cache.GetStringAsync(CacheKey(context), ct) ?? Classify(context);
_pending[context] = route;
return _routes[route];
}
protected override async ValueTask OnRoutingUpdateAsync(
RoutingContext context, FailoverChatClientAttempt attempt, bool isTerminal, CancellationToken ct)
{
if (_pending.TryRemove(context, out string? route) && attempt.ResponseCompleted)
{
await _cache.SetStringAsync(CacheKey(context), route, ct);
}
}
private static string CacheKey(RoutingContext context) =>
context.ChatOptions?.AdditionalProperties?.TryGetValue("routing-session-id", out string? id) == true
? $"chat-route:{id}"
: throw new InvalidOperationException("A routing session ID is required.");
}
Classify returns a route name rather than a client, so the cache, the classifier, and the pin all deal in the same string; _routes converts it once on the way out. It only runs on the first request of a session, which is what makes an embedding call affordable there.
The pin happens only after the response completes, so a client that fails on the first turn never gets stuck to the session. A caller that breaks out of the enumeration early counts the same way: ResponseCompleted stays false, so nothing is pinned.
Getting that behavior right is the reason this router derives from FailoverChatClient , with MaximumAttemptsPerRequest = 1 to switch off the retry loop it doesn’t want. Completion tracking lives on the failover type, so observing attempts means inheriting retry machinery, only to disable it. Splitting the two apart would let them compose independently and would be a useful future improvement.
One model, multiple reasoning levels
Staying on a single model while varying reasoning effort is an effective way to route while maintaining prompt-caching behavior. If one model supports multiple reasoning levels, wrap it once per effort level and route between those wrappers:
IChatClient lowEffort = baseClient.AsBuilder()
.ConfigureOptions(options =>
options.Reasoning = new ReasoningOptions { Effort = ReasoningEffort.Low })
.Build();
IChatClient highEffort = baseClient.AsBuilder()
.ConfigureOptions(options =>
options.Reasoning = new ReasoningOptions { Effort = ReasoningEffort.High })
.Build();
var router = RoutingChatClient.Create((context, ct) =>
new(isComplexRequest(context) ? highEffort : lowEffort));
Each wrapper is a distinct IChatClient , so routing policies can track low and high effort separately.
Other patterns worth exploring
Latency- and health-aware routing. Use Duration , TimeToFirstUpdate , and failures from OnRoutingUpdateAsync to rank clients by observed performance. New clients need seeded estimates or independent probes before enough live data exists.
Circuit breaking and cooldowns. Remove unhealthy clients from selection after repeated failures, then test recovery after a delay. The recovery window can depend on the failure: a timeout may need seconds, while an authentication failure may require manual intervention.
Cost-aware routing. Prefer cheaper candidates for routine requests, reserve expensive models for harder work, or enforce a budget across a session or tenant.
Capability-aware routing. Filter clients before selection based on requirements such as vision, tool calling, structured output, or context length.
Region-based routing. Prefer a nearby deployment to reduce network latency, or select a region that satisfies data-residency requirements.
Router composition. Every router is an IChatClient , so a cost- or capability-aware router can sit inside a failover chain while OnRoutingUpdateAsync records each attempt.
Limitations
RoutingChatClient always makes its selection before invoking anything: one client, chosen up front, per request. That puts a few routing paradigms outside its scope. None of them are impossible in Microsoft.Extensions.AI , they’re just not what RoutingChatClient is for:
Model cascading. FailoverChatClient reselects on failure, not when a successful response misses a quality threshold.
Ensemble routing. Fanning out to several clients and merging or voting on the responses needs a client that invokes more than one.
Hedging. Racing several clients and taking the first to respond trades extra cost for lower tail latency; that also needs fan-out.
Where the router sits in the pipeline matters too. Selection happens once per request, so a router wrapped around FunctionInvokingChatClient keeps the same client for every iteration of a tool-calling loop. Sending the initial reasoning to a strong model and the tool-result turns to a cheap one means putting the router inside FunctionInvokingChatClient rather than around it.
Getting Started
RoutingChatClient , RoutingContext , FailoverChatClient , FailoverChatClientAttempt , OrderedFailoverChatClient , and SemanticRoutingChatClient shipped in the Microsoft.Extensions.AI version 10.9.0. All of these types are marked [Experimental] with diagnostic ID MEAI001 .
dotnet add package Microsoft.Extensions.AI
We look forward to your feedback on these new features, the API shapes, and particularly the behaviors around:
Failover’s retry and attempt-limit
What OnRoutingUpdateAsync reports on each attempt
How much state the framework tracks versus leaves to you
SemanticRoutingChatClient ‘s scoring defaults and aggregation options
Whether per-attempt option shaping should be expressible without also selecting a different client
This list isn’t exhaustive. If you build something with these, file issues or start a discussion on dotnet/extensions . Tell us what worked and what you had to work around.
Learn more:
dotnet/extensions#7662 : the PR that introduces these types
Microsoft.Extensions.AI documentation
dotnet/extensions on GitHub
Routing CLI Sample
