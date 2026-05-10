---
source: "https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/"
title: "The problem: All-or-nothing batch processing in Azure Service Bus"
author: "Azure Blog"
date_published: "Tue, 28 Apr 2026 18:47:37 +0000"
date_clipped: "2026-05-10"
category: "Azure & Cloud"
source_type: "rss"
---

# The problem: All-or-nothing batch processing in Azure Service Bus

Source: https://devblogs.microsoft.com/azure-sdk/per-message-settlement-azure-service-bus/

Azure Service Bus is one of the most widely used messaging services for building event-driven applications on Azure. When you use Azure Functions with a Service Bus trigger in batch mode, your function receives multiple messages at once for efficient, high-throughput processing.
But what happens when one message in the batch fails? Assume your function receives a batch of 50 Service Bus messages. Forty-nine process perfectly, and one fails.
In the default model, the entire batch fails. All 50 messages go back on the queue and get reprocessed, including the 49 that already succeeded. This leads to:
Duplicate processing —messages that were already handled successfully get processed again 
Wasted compute —you pay for re-executing work that already completed 
Infinite retry loops —if that one “poison” message keeps failing, it blocks the entire batch indefinitely 
Idempotency burden —your downstream systems must handle duplicates gracefully, adding complexity to every consumer 
This pattern is the classic all-or-nothing batch failure problem. Azure Functions solves it with per-message settlement.
The solution: Per-message settlement for Azure Service Bus 
Azure Functions gives you direct control over how each individual message is settled in real time, as you process it. Instead of treating the batch as all-or-nothing, you settle each message independently based on its processing outcome.
With Service Bus message settlement actions in Azure Functions, you can:
Action 
What It Does 
Complete 
Remove the message from the queue (successfully processed) 
Abandon 
Release the lock so the message returns to the queue for retry, optionally modifying application properties 
Dead-letter 
Move the message to the dead-letter queue (poison message handling) 
Defer 
Keep the message in the queue but make it only retrievable by sequence number 
This capability means in a batch of 50 messages, you can:
Complete 47 that processed successfully 
Abandon 2 that hit a transient error (with updated retry metadata) 
Dead-letter 1 that’s malformed and never succeeds 
All in a single function invocation. No reprocessing of successful messages. No building failure response objects. No all-or-nothing.
Why this matters 
1. Eliminates duplicate processing 
When you complete messages individually, successfully processed messages are immediately removed from the queue. There’s no chance of them being redelivered, even if other messages in the same batch fail.
2. Enables granular error handling 
Different failures deserve different treatments. A malformed message should be dead-lettered immediately. A message that failed due to a transient database timeout should be abandoned for retry. A message that requires manual intervention should be deferred. Per-message settlement gives you this granularity.
3. Implements exponential backoff without external infrastructure 
By combining abandon with modified application properties, you can track retry counts per message, and implement exponential backoff patterns directly in your function code. No extra queues or Durable Functions are required.
4. Reduces cost 
You stop paying for redundant re-execution of already-successful work. In high-throughput systems processing millions of messages, this approach can be a material cost reduction.
5. Simplifies idempotency requirements 
When successful messages are never redelivered, your downstream systems don’t need to guard against duplicates as aggressively. This change reduces architectural complexity and potential for bugs.
Before: One message = one function invocation 
Before batch support, there was no cardinality option, Azure Functions processed each Service Bus message as a separate function invocation. If your queue had 50 messages, the runtime spun up 50 individual executions.
Single-message processing (the old way) 
import { app, InvocationContext } from '@azure/functions';
async function processOrder(
message: unknown, // ← One message at a time, no batch
context: InvocationContext
): Promise<void> {
try {
const order = message as Order;
await processOrder(order);
} catch (error) {
context.error('Failed to process message:', error);
// Message auto-complete by default.
throw error;
}
}
app.serviceBusQueue('processOrder', {
connection: 'ServiceBusConnection',
queueName: 'orders-queue',
handler: processOrder,
}); 
What this cost you:
50 messages on the queue 
Old (single-message) 
New (batch + settlement) 
Function invocations 
50 separate invocations 
One invocation 
Connection overhead 
50 separate DB/API connections 
One connection, reused across batch 
Compute cost 
50× invocation overhead 
1× invocation overhead 
Settlement control 
Binary: throw or don’t 
Four actions per message 
Every message paid the full price of a function invocation, startup, connection setup, teardown. At scale (millions of messages/day), this overhead was a significant cost and latency penalty. And when a message failed, your only option was to throw (retry the whole message) or swallow the error (lose it silently).
Code examples 
Let’s see how this looks across all three major Azure Functions language stacks.
Node.js (TypeScript with @azure/functions-extensions-servicebus) 
import '@azure/functions-extensions-servicebus';
import { app, InvocationContext } from '@azure/functions';
import { ServiceBusMessageContext, messageBodyAsJson } from '@azure/functions-extensions-servicebus';
interface Order { id: string; product: string; amount: number; }
export async function processOrderBatch(
sbContext: ServiceBusMessageContext,
context: InvocationContext
): Promise<void> {
const { messages, actions } = sbContext;
for (const message of messages) {
try {
const order = messageBodyAsJson<Order>(message);
await processOrder(order);
await actions.complete(message); // ✅ Done
} catch (error) {
context.error(`Failed ${message.messageId}:`, error);
await actions.deadletter(message); // ☠️ Poison
}
}
}
app.serviceBusQueue('processOrderBatch', {
connection: 'ServiceBusConnection',
queueName: 'orders-queue',
sdkBinding: true,
autoCompleteMessages: false,
cardinality: 'many',
handler: processOrderBatch,
}); 
Key points: 
Enable sdkBinding: true and autoCompleteMessages: false to gain manual settlement control 
ServiceBusMessageContext provides both the messages array and actions object 
Settlement actions: complete() , abandon() , deadletter() , defer() 
Application properties can be passed to abandon() for retry tracking 
Built-in helpers like messageBodyAsJson<T>() handle Buffer-to-object parsing 
Full sample: serviceBusSampleWithComplete 
Python (V2 programming model) 
import json
import logging
from typing import List
import azure.functions as func
import azurefunctions.extensions.bindings.servicebus as servicebus
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
@app.service_bus_queue_trigger(arg_name="messages",
queue_name="orders-queue",
connection="SERVICEBUS_CONNECTION",
auto_complete_messages=False,
cardinality="many")
def process_order_batch(messages: List[servicebus.ServiceBusReceivedMessage],
message_actions: servicebus.ServiceBusMessageActions):
for message in messages:
try:
order = json.loads(message.body)
process_order(order)
message_actions.complete(message) # ✅ Done
except Exception as e:
logging.error(f"Failed {message.message_id}: {e}")
message_actions.dead_letter(message) # ☠️ Poison
def process_order(order):
logging.info(f"Processing order: {order['id']}") 
Key points: 
Uses azurefunctions.extensions.bindings.servicebus for SDK-type bindings with ServiceBusReceivedMessage 
The extension supports both queue and topic triggers with cardinality="many" for batch processing 
Each message exposes SDK properties like body , enqueued_time_utc , lock_token , message_id , and sequence_number 
Full sample: servicebus_samples_settlement 
.NET (C# Isolated Worker) 
using Azure.Messaging.ServiceBus;
using Microsoft.Azure.Functions.Worker;
public class ServiceBusBatchProcessor(ILogger<ServiceBusBatchProcessor> logger)
{
[Function(nameof(ProcessOrderBatch))]
public async Task ProcessOrderBatch(
[ServiceBusTrigger("orders-queue", Connection = "ServiceBusConnection")]
ServiceBusReceivedMessage[] messages,
ServiceBusMessageActions messageActions)
{
foreach (var message in messages)
{
try
{
var order = message.Body.ToObjectFromJson<Order>();
await ProcessOrder(order);
await messageActions.CompleteMessageAsync(message); // ✅ Done
}
catch (Exception ex)
{
logger.LogError(ex, "Failed {MessageId}", message.MessageId);
await messageActions.DeadLetterMessageAsync(message); // ☠️ Poison
}
}
}
private Task ProcessOrder(Order order) => Task.CompletedTask;
}
public record Order(string Id, string Product, decimal Amount); 
Key points: 
Inject ServiceBusMessageActions directly alongside the message array 
Each message is individually settled with CompleteMessageAsync , DeadLetterMessageAsync , or AbandonMessageAsync 
Application properties can be modified on abandon to track retry metadata 
Full sample: ServiceBusReceivedMessageFunctions.cs
