# Realtime Chat Service Contracts

## Decision-useful summary

Conversation services combine message delivery with identity, membership, storage, and recovery contracts. The captured Azure preview below is one implementation reference; its claims remain publication-specific. Related protocol decisions live in [[realtime-game-network-protocol-design]].


## 2026-09-22: Chat abstractions retain application identity and storage responsibilities

### Typed entities

project: Azure Web PubSub; project: Azure Storage; concept: chat hub; concept: room membership; concept: backend role administration; concept: managed identity.

### Claims and evidence

- Microsoft's August 21 announcement describes a public-preview chat layer with rooms, memberships, ordered messages, history, roles, and reconnection. Persistent messages and authorization records live in the application's Azure Storage account, accessed through the Web PubSub resource's managed identity. confidence: 1 source, last-confirmed 2026-09-22 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-20-rss-azure-web-pubsub-chat-contracts.md)
- Default member permissions include inviting users; role administration belongs in trusted backend code. Production access URLs should be issued through an authenticated backend using application identity, rather than portal-generated experimental URLs. Chat hubs serve conversation workloads; custom telemetry or multiplayer protocols may require standard hubs. confidence: 1 source, last-confirmed 2026-09-22 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-20-rss-azure-web-pubsub-chat-contracts.md)

### Explicit relationships

Chat uses persisted conversation and membership state; authorization depends-on authenticated user identity and trusted role administration. Chat storage depends-on resource identity permissions. See [[realtime-game-network-protocol-design]] and [[azure-agent-automation-and-identity]].

### Decision and quality notes

Historical vendor preview announcement. Evaluate recovery, authorization defaults, and storage behavior locally before selecting this boundary; no present GA status is inferred. Source-specific claims remain provisional single-source evidence; related articles and derived queries add no independent support. Open question: Would a chat hub fit HoneyDrunk conversation requirements, and what tests establish invite permissions, authenticated access URL issuance, reconnect ordering, and retained-storage recovery? See [[indexes/gaps]].
