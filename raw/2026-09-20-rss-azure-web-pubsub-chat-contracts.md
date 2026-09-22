---
source: "https://techcommunity.microsoft.com/blog/appsonazureblog/announcing-azure-web-pubsub-chat-in-public-preview/4548907"
title: "Announcing Azure Web PubSub chat in public preview"
author: "kevinguo"
date_published: "2026-08-21"
date_clipped: "2026-09-20"
category: "Azure & Cloud"
source_type: "rss"
capture_format: "attributed-summary"
---

# Announcing Azure Web PubSub chat in public preview

Source: [Announcing Azure Web PubSub chat in public preview](https://techcommunity.microsoft.com/blog/appsonazureblog/announcing-azure-web-pubsub-chat-in-public-preview/4548907)

Attributed summary of the fetched full written article; not a verbatim reproduction. Claims remain source-specific and have not been independently reproduced.

Microsoft announces a public-preview chat layer over Azure Web PubSub. It adds rooms, membership, ordered messages, retained history, roles, and reconnection behavior. A JavaScript client supports interactive operations; server REST APIs retain administrative control.

Persistent messages, memberships, users, and permissions live in the application's chosen Azure Storage account. The service accesses it using the Web PubSub resource's managed identity. The article distinguishes chat hubs from standard hubs: conversation workloads benefit from chat abstractions, while telemetry or multiplayer state may need a custom protocol.

Default member permissions include inviting other users, so application teams must evaluate role semantics instead of assuming restrictive defaults. Role administration belongs in trusted backend code.

Portal-generated client access URLs are for experiments. Production should issue access URLs through an authenticated backend and derive user identity from the authenticated application user.

HoneyDrunk relevance: evaluate this as a conversation service boundary, preserving its preview status and independently testing recovery, authorization, and storage behavior.
