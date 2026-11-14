---
source: "https://labs.eye.security/how-attackers-keep-reading-mail-after-m365-session-revocation"
title: "How attackers keep reading mail after M365 session revocation"
author: "Martin Warmer"
date_published: "2026-10-29"
date_clipped: "2026-11-14"
category: "Security & Ethical Hacking"
source_type: "rss"
discovered_via: "https://tldr.tech/infosec/2026-11-12"
---

# How attackers keep reading mail after M365 session revocation

You are a defender and spot an M365 user that was phished. The first thing you want to do is secure the account and deny access to the attacker. So, what do you need to do: revoke sessions, reset the password, or disable the account? This blog post takes a look at what the practical impact is of each option.

## How access to Exchange Online works

All access to Exchange Online is authenticated via Entra. Once the user has been authenticated in Entra, the user receives an access token and a refresh token. The access token is only valid for 60-90 minutes and can be used to directly access the mailbox. After it has expired, the refresh token can be exchanged for a new access token. This is possible for up to 90 days, after which the refresh token also expires. This design reduces the load on Entra since it doesn’t need to be involved in every interaction with Exchange Online. If you’re familiar with traditional Active Directory, the refresh token is roughly equivalent to the TGT and the access token to a service ticket.

## What session revocation actually does

When revoking sessions in Entra, this is implemented as an update of the `StsRefreshTokenValidFrom` timestamp. Any refresh token issued before this timestamp is no longer considered valid. However, the access token was still valid to access a mailbox until it expired. As a countermeasure, Microsoft implemented Continuous Access Evaluation (CAE) which allows Exchange to check e.g. the IP address on each access. The disadvantage is that it breaks a lot of normal use cases like checking your mail on your phone. The phone might be connected to any home, hotel or even in-flight Wi-Fi network, thus changing IP addresses all the time. Therefore, CAE is not often enabled. However, a little-known part of CAE is always active, the critical event evaluation. This is a special mechanism by which Exchange Online, SharePoint Online and Teams can be informed when e.g. sessions are revoked, passwords are changed or accounts are disabled.

> **Critical event evaluation**  
> This process enables the scenario where users lose access to organizational SharePoint Online files, email, calendar, or tasks, and Teams from Microsoft 365 client apps within minutes after a critical event. ([Microsoft documentation](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation#critical-event-evaluation))

## Outlook loses access, the APIs do not

Critical event evaluation is designed to quickly revoke access to email and triggers when sessions are revoked, password are reset and accounts are disabled. Thus, you would assume that after any of these actions the attacker is no longer able to read mail. When using the official Outlook clients, the access is quickly revoked in all scenarios, no matter whether you use Outlook classic, modern Outlook, or Outlook mobile. Even mail clients with an open TCP connection to IMAP get disconnected quickly. However, the access tokens remain valid for API-based access.  No matter if we use the modern Graph API, which Microsoft recommends for new applications. Or we use the already deprecated Exchange Web Services (EWS). Even the old Exchange ActiveSync, intended for syncing to smartphones, remains available.

## Disabling the account is the only full block

The only way to block all access is by disabling the account. While it’s disabled, none of the methods for accessing mail work. When re-enabled, the old access tokens work again, unless their validity is expired. **Thus, to prevent further access, you need to disable the account for 90 minutes after the last access token has been issued.**

One interesting side effect of critical event evaluation only being implemented for a few services is that the Graph API denies access only for some endpoints. After disabling an account, the endpoints which access a mailbox or SharePoint files don’t work. But using the same token to e.g. query users in Entra does work. There is currently no way to block this access.

## Why this matters: phishing kits now use the Graph API

Previously phishers would use the phished tokens to manually access Outlook on the web. But newer phishing kits are automated and use the Graph API to collect email. Thus, while just revoking sessions or resetting the password would work, these days phishers can keep downloading mail. Therefore, disabling the account becomes more important, even if it means temporarily locking users out of their account.

## What needs to change

There is an industrywide consortium working on improving session revocation for OpenID-based sign-ins. Specifically, [OpenID Shared Signals Framework](https://openid.net/specs/openid-sharedsignals-framework-1_0.html) and [OpenID Continuous Access Evaluation Profile](https://openid.net/specs/openid-caep-1_0.html) provide the technical building blocks for an identity provider like Entra to inform services that tokens are no longer valid. Implementing a framework like this for all protocols would help to better secure Exchange Online. The intent is clear no matter whether you revoke sessions, reset passwords, or disable the account. In all cases, mail access should be blocked in real time.

| Protocol/Application | Revoke Sessions | Reset Password | Disable Account |
| --- | --- | --- | --- |
| MAPI (Outlook classic) | Real-time | Real-time | Real-time |
| Outlook on the web | Real-time | Real-time | Real-time |
| Outlook mobile | Real-time | Real-time | Real-time |
| IMAP (generic mail client) | Real-time | Real-time | Real-time |
| Graph API | Up to 90 min. | Up to 90 min. | Real-time |
| Exchange Web Services ([deprecated](https://techcommunity.microsoft.com/blog/exchange/exchange-online-ews-your-time-is-almost-up/4492361)) | Up to 90 min. | Up to 90 min. | Real-time |
| Exchange ActiveSync (iPhone mail, Android mail) | Up to 90 min. | Up to 90 min. | Real-time |
