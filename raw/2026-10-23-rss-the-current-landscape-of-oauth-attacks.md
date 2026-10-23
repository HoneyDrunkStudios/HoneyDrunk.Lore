---
source: "https://unit42.paloaltonetworks.com/current-landscape-oauth-attacks"
title: "The Current Landscape of OAuth Attacks"
author: "Shawn He Shuang; Beliz Kaleli; Diva-Oriane Marty; Oleksii Alex Starov"
date_published: "2026-10-22"
date_clipped: "2026-10-23"
category: "Security & Ethical Hacking"
source_type: "rss"
discovered_via: "https://tldr.tech/infosec/2026-10-23"
---

# The Current Landscape of OAuth Attacks

Source: https://unit42.paloaltonetworks.com/current-landscape-oauth-attacks

As enterprises continue to roll out multi-factor authentication (MFA), attackers have adapted. Rather than only stealing credentials, attackers have shifted to stealing Open Authorization (OAuth) tokens, the keys that govern what applications can do on your behalf. Adversaries are already accelerating these attacks by using dynamic evasion code, phishing-as-a-service (PhaaS) templates and LLM-generated brand impersonations.

Because OAuth attacks occur at the authorization layer after user authentication, stolen access and refresh tokens bypass MFA, survive password resets and grant durable access.

While OAuth misuse occurs at a lower volume than traditional phishing attacks, these attacks may carry severe consequences such as:

- Account takeover
- Persistent access to sensitive data that survives password resets and MFA re-enrollment
- Lateral movement across every service connected to the compromised identity
- Data exfiltration without triggering credential-based alerts
- A foothold in enterprise environments for broader supply chain or insider attacks

Defending against these threats can be accomplished using several strategies:

- Disabling end-user app consent for vague or impersonating app names
- Enforcing admin-only approval workflows
- Monitoring authorization code clipboard events
- Continuously auditing registered redirect\_uri values

To understand why OAuth has become such a prime target for modern adversaries, it helps to examine the authentication challenges the protocol was originally designed to solve. Looking back at how applications handled identity before OAuth reveals how the threat landscape has evolved from simple password theft to complex token hijacking.

## The Past: Phishing for Passwords

Websites and applications often tie together functionality from other sites. For example, some popular ecommerce and social media platforms allow users to log in through their email accounts.

In 2006, before OAuth, combining functionality between applications involved sharing one application’s credentials, which are supposed to be secret, with another. This type of sharing is a significant security issue because it increases the consequences of a successful credential phishing attack.

In credential phishing, attackers trick users into sharing their login credentials, allowing attackers to gain full access to their accounts. This could be access to an email account, business system, social media account or bank account. The attacker gains access to all of the information in that account and the authority to make changes, including altering the password and locking out the user.

During the pre-OAuth era, applications or sites sharing credentials meant that attackers could pivot to different platforms or services through compromising a single account.

To address these issues, the OAuth working group released the first draft of [OAuth Core 1.0](https://oauth.net/core/1.0/) in 2007. The Internet Engineering Task Force (IETF) released Request for Comments (RFC) 6749 for [OAuth 2.0](https://www.rfc-editor.org/info/rfc6749/) in 2012 and is working on [OAuth 2.1](https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/) as of 2026.

## The Present: Why OAuth Became the New Attack Surface

### The OAuth Framework

[OAuth](https://www.microsoft.com/en-us/security/business/security-101/what-is-oauth) allows users to grant third-party applications passwordless authorization to their data on another service. Figure 1 displays a sample sign-in screen presenting OAuth authentication options with three different Identity Providers (IdPs): Google, Apple and Microsoft.

Figure 1. Example sign-in page presenting OAuth options.

In a typical OAuth flow:

1. The user authenticates with the identity provider
2. The user approves the permissions (i.e., scopes) requested by the third-party application
3. The identity provider issues an access token to the third-party application
4. The third-party application then uses the access token to retrieve user data within the authorized scopes

This token is temporary, revocable and has scoped permissions. This gives the third-party application access to permitted resources on the user’s behalf.

### OAuth Becomes the New Attack Surface

Standard phishing attacks are designed to steal login credentials like user account names and passwords. OAuth-based phishing bypasses login credential authentication entirely.

Victims authenticate through legitimate IdPs and complete MFA. They are then redirected with tokens that can grant attackers persistent, durable access.

Attackers don’t need to defeat MFA directly, because they are able to bypass it by acquiring the authorization tokens after a victim authenticates. This presents a weak spot between authentication and authorization where OAuth-based phishing can happen. If someone is the victim of a phishing campaign, their stolen tokens may give unintended permissions to an attacker’s app.

A [large-scale analysis of OAuth websites](https://petsymposium.org/popets/2023/popets-2023-0119.pdf) found that 18.53% of these sites request permissions beyond the minimum required (typically just a user's profile and email). While not directly malicious, this statistic illustrates the likelihood of privacy and privilege leaks when excessive permissions are granted.

### The Core Vulnerability: Tokens Outlive Passwords

One of the primary advantages of OAuth is that tokens, unlike passwords, are designed to be short-lived and easily revoked. However, in practice, OAuth tokens:

- Are frequently configured to be long-lived
- Survive a password reset since the token is not a password
- Bypass MFA since the victim already completed MFA during the flow
- Provide persistent access (until explicitly revoked) since refresh tokens silently mint new access tokens for days or months after the initial compromise

This persistence directly amplifies the following authorization vulnerabilities:

- Cross-User OAuth Session Fixation (COSF)
- Cross-Tenant Client ID Confusion
- Cross-Connector OAuth Account Takeover

COSF allows an attacker to use a long-lived token as a permanent backdoor. This type of vulnerability arises when an OAuth session is used to complete an authentication flow without verifying its strict binding to the initiating user’s identity.

1. The attacker initiates an OAuth process (e.g., “Connect your Slack”) inside a target app
2. Before completing the OAuth process, the attacker freezes the session and sends the victim a phishing link
3. The victim logs into their real Slack account, but through the attacker's [fixated session](https://owasp.org/www-community/attacks/Session_fixation)
4. The resulting access token lands in the attacker's account

The next two vulnerabilities rely on OAuth-as-a-service (OaaS). OaaS lets organizations outsource token management to a centralized cloud provider where the provider creates a single token vault and manages tokens for hundreds of different apps (tenants). These are commonly used by organizations with many applications. OaaS architecture is inherently susceptible to Cross-Tenant Client ID Confusion and Cross-Connector OAuth Account Takeover.

#### Cross-Tenant Client ID Confusion

In Cross-Tenant Client ID Confusion, a malicious app (Tenant A) swaps its app identifier (Client ID) to impersonate a trusted app (Tenant B) sharing the same vault. The vault trusts both tenants, processes the request under the trusted app's context and accidentally exposes access to the malicious tenant.

#### Cross-Connector OAuth Account Takeover

In Cross-Connector OAuth Account Takeover, a malicious tenant manipulates how the vault maps OAuth sessions to connectors. A victim's authorization flow, meant for a different app entirely, gets rerouted into the attacker's control. As a result, attackers take over the full account without stealing credentials

Both attacks get easier the longer a token stays valid. A short-lived token limits the damage window.

### Existing Mitigations

OAuth security is decentralized and dictated by the IdP. While major IdPs have robust defenses against flow misuse, many smaller platforms offer weak protections.

The root challenge is the lack of a global registry for Client IDs. Without a universal ground truth of identity, attackers can easily impersonate legitimate app names on lax platforms. To counter this, leading IdPs enforce strict guardrails. Google, for example, [mitigates misuse](https://developers.google.com/identity/protocols/oauth2/policies) through:

- Domain ownership verification for redirect URIs
- Unverified app warnings to deter users from unauthorized integrations
- Strict security audits for apps requesting sensitive scopes

Because you cannot rely on every IdP to protect your data equally, a third-party consent security policy is essential. A centralized, automated policy enables organizations to standardize their defenses by:

- Enforcing least-privilege
- Blocking unverified apps
- Revoking risky grants uniformly, regardless of the individual provider's security gaps

## OAuth-Based Phishing Campaigns

Currently, OAuth-based phishing campaigns fall into three categories, each defined by what the attacker is trying to achieve:

- **Account hijacking:** The attacker obtains a durable token granting them the same access as the victim (full identity assumption)
- **Permission hijacking:** The victim is tricked into consenting to a malicious app, giving the attacker scoped access to specific resources
- **Malicious redirect:** The attacker uses the OAuth flow's redirect mechanism to deliver malware or phishing, exploiting the trust users place in flows that originate from real identity provider domains

### Account Hijacking: Stealing the Identity Itself

Account hijacking is the most complete form of identity compromise. The attacker ends up with an OAuth access or refresh token that authenticates them as the victim on every downstream service that trusts that identity provider. Attackers misuse two distinct OAuth flows to achieve account hijacking: the device authorization flow and the authorization code flow.

#### Device Authorization (DeviceAuth) Misuse

##### How the Legitimate Flow Works

The [device authorization grant](https://datatracker.ietf.org/doc/html/rfc8628) was designed for devices that cannot open a browser such as smart TVs, gaming consoles and command-line tools. The device displays a short code and a URL (like microsoft[.]com/devicelogin). The user opens that URL on a separate device, enters the code, signs in and the original device receives an access token.

##### How Attackers Exploit It

Instead of a legitimate device requesting the code, the attacker's server requests it. The attacker then shows that code to the victim and instructs them to paste it into, for example, Microsoft's real device login page. When the victim signs in and submits the code, they are unknowingly authenticating the attacker's session.

#### Authorization Code Theft via Benign Apps

##### How the Legitimate Flow Works

In the standard authorization code flow, a user authenticates with an identity provider, which issues a short-lived authorization code and redirects the browser to a registered redirect\_uri. The application then exchanges that code for an access token in a server-to-server call the user never sees.

##### How Attackers Exploit It

Attackers use a legitimate application's redirect\_uri to expose the authorization code in the browser, then use social engineering to extract it. No malicious app registration is needed; the attack rides on apps that already pass every security check.

### Permission Hijacking: Tricking Users into Granting Access

Permission hijacking is more of a surgical attack than a full account takeover. Rather than stealing a code or device token, the attacker's goal is to have the victim click Allow on an OAuth consent screen that grants an attacker-registered application persistent, scoped access to specific resources. The victim authenticates legitimately and completes MFA. They simply consent to the wrong application.

The consent screen is the attack surface. Victims reach it through two attack strategies: vague app names or brand impersonation.

#### Vague App Names

In this strategy, the attacker registers an application with an innocuous-sounding name (e.g., Privacy Policy Extension or Security App) that provides no meaningful signal about its intent. It then requests permissions far beyond what the name implies.

#### Brand Impersonation

In this strategy, the attacker registers an application that displays as a trusted brand while the underlying client\_id belongs to an attacker-controlled application. The consent screen shows the name provided at registration rather than any verified identity. As such, the victim sees a familiar brand name from a legitimate identity provider, with no visible signal that the application is fraudulent.

### Malicious Redirect: Weaponizing the OAuth Flow for Delivery

In malicious redirect attacks, the attacker's goal is not account access or a scoped token. Instead, they weaponize the OAuth authorization flow itself as a delivery mechanism, exploiting the trust users place in pages and redirects that originate from real identity provider domains.

Attackers have used different tactics to weaponize the OAuth flow, such as:

- Impersonating trusted services
- Triggering OAuth errors
- Leveraging less safe IdPs

#### Impersonating Trusted Services

Attackers register OAuth applications that impersonate trusted services and configure attacker-owned domains as the redirect\_uri. When the victim completes the OAuth flow on the real identity provider, the browser is redirected to the attacker's domain as part of the normal protocol. Because the user just interacted with a legitimate identity provider and expects to land somewhere, the redirect is implicitly trusted.

#### Triggering OAuth Errors

Documented by Microsoft in March 2026, [a more covert campaign](https://www.microsoft.com/en-us/security/blog/2026/03/02/oauth-redirection-abuse-enables-phishing-malware-delivery/) exploits how identity providers handle errors to redirect users to attacker-controlled malicious landing pages. Attackers crafted authorization URLs designed to deliberately trigger an authentication error. For example, they combined prompt=none with parameters that required user interaction, creating an irresolvable conflict.

When the identity provider cannot complete the authorization, it does not show an error page. Instead, it appends error parameters to the redirect\_uri and sends the browser there automatically. An example of a redirect URL format after triggering an error is as follows:

<attacker-domain>/security/?state=<encoded-victim-email>&error=interaction\_required&error\_subtype=access\_denied

Since the crafted link points to a trusted OAuth provider, the user is more likely to click it and be exposed to the malicious content with just that one click.

#### Leveraging Less Safe IdPs

Attackers weaponize lax validation on less secure IdPs to execute redirection attacks. For example:

- If an IdP fails to validate the presence of a client\_id, attackers can weaponize the authorization server as a generic open redirector without even creating a malicious OAuth app
- If an IdP has a permissive redirect\_uri validation, attackers may leverage path traversal or URL parameters to redirect to their own malicious domains

## The Escalation: Shift From Basic to Sophisticated Methods

Credential phishing generally relies on mass-delivered, low-fidelity landing pages designed to capture plaintext passwords. Today, attackers have evolved from only harvesting static secrets to hijacking active, authenticated sessions. By positioning themselves inside legitimate OAuth protocols, campaigns can bypass perimeter controls, turning the trust mechanisms of single sign-on (SSO) and federation into vectors for compromise.

### From Static Pages to Dynamic Evasion

Security architectures have in the past heavily relied on static analysis and domain reputation to block malicious links. In response, threat groups shifted from static HTML templates to dynamic, highly evasive client-side execution environments.

Key characteristics of this shift include:

- **Runtime decryption:** As observed in recent campaigns, threat actors deliver payloads as obfuscated blobs (using encryption algorithms such as AES-GCM) via edge infrastructure like Cloudflare Workers. The payloads assemble the interface only after execution in the victim's browser. Figure 2 below shows a code snippet from an example of a phishing page.
- **Active environment fingerprinting:** Phishing pages now query the browser environment, implementing heuristics to detect developer tools, automated sandbox configurations or headless security crawlers.
- **Defensive evasion loops:** When the payload detects a monitoring tool or security analyst is detected, the page shifts its behavior, invoking endless debugger loops or silently routing traffic to legitimate domains to preserve the longevity of the infrastructure. Figure 3 shows an example of code used for this type of monitoring.

Figure 2. Example of code in a phishing page to decrypt an obfuscated blob.

Figure 3. Example of code in a phishing page to evade detection.

### The PhaaS Economy

The effectiveness of these campaigns is amplified by the commercialization of specialized threat kits within the cybercriminal underground. We observed that the attackers use the same template to generate OAuth phishing pages impersonating different brands. We show examples of different brand impersonations in Figure 4.

Figure 4. Phishing pages generated from the same template targeting different brands (actual brand redacted).

This PhaaS ecosystem has two key characteristics:

- **Modular templates:** PhaaS platforms now offer plug-and-play OAuth components. A single underlying framework can be dynamically re-skinned with different corporate assets. We have observed attackers impersonating multiple popular document sharing platforms as part of campaigns.
- **Shared infrastructure:** Multiple seemingly distinct campaigns share identical tokens. We have observed identical data used for anti-bot tokens (example in Figure 5) and Cloudflare Real User Monitoring (RUM) tokens. This indicates that specialized developers are renting highly capable infrastructure to a broader array of less technical affiliates.

Figure 5. Code from a phishing campaign with a token used across multiple campaigns.

### LLMs as an Attack Accelerator

Generative AI has lowered the barrier of entry for executing high-fidelity, targeted identity operations. We have observed signs of websites generated with the help of LLMs, such as the example below in Figure 6. The code in these phishing pages suggests that attackers are using LLMs to impersonate legitimate pages and rapidly deploy attacks.

Figure 6. Evidence of LLM-generated resources on domain hosting device code campaign sieprevencion[.]cl.

The operational advantages provided by LLMs include:

- **High-fidelity brand impersonation:** Attackers leverage LLMs to overcome typical signs of impersonation, such as poor syntax, unnatural phrasing or layout inconsistencies. Generative models enable adversaries to rapidly produce context-specific localization, creating more convincing brand imitations that can mislead users.
- **Rapid deployment cycles:** Rather than relying solely on static templates or manual development, threat actors can leverage LLMs to generate functional landing page code tailored to specific target organizations. This allows attackers to build targeted, localized campaigns and test and deploy attacks at a velocity that reactive defense layers struggle to match.

### Expanding OAuth Ecosystem

OAuth adoption continues to grow beyond identity providers into infrastructure platforms, and every new platform that joins the ecosystem adds a new consent surface for attackers to exploit. A notable recent example is [Cloudflare's June 2026 launch of self-managed OAuth clients](https://blog.cloudflare.com/oauth-for-all/), which now allows third-party developers to build applications that act on behalf of users to access their Cloudflare accounts.

Cloudflare accounts control critical infrastructure such as DNS, CDN routing and edge compute. This means a token granted through a malicious OAuth app carries a far greater impact radius than one granting access to email or files. An attacker who tricks a developer into consenting could gain the ability to deploy malicious pages, redirect legitimate traffic or build phishing infrastructure on domains that most enterprise security tools inherently trust.

## How to Defend Against OAuth Attacks

Standard perimeter and client-side security controls fail against OAuth phishing attacks, particularly for the following reasons:

- Access tokens survive a password reset
- The attack bypasses MFA because the victim has already completed MFA during the legitimate flow
- Conditional Access and IP firewalls fail because OAuth grants access to any token presenter, regardless of origin

Unlike a typical login where a server might establish a persistent, multi-factor session bound to a specific user's browser, the server validates the token's cryptographic signature. However, the session lacks an inherent link to the user's initial authorization context. Additionally, because flows like device authorization intentionally decouple the initiating and authenticating devices, enforcing strict IP or device consistency checks would break the protocol's design.

Effective defenses must focus on account hijacking, permission hijacking and malicious redirects.

### Defenses for Account Hijacking

Attackers rely on manipulating victims into pasting sensitive codes into legitimate portals such as device login pages or messaging applications. Security tools can monitor for clipboard copy and paste events along with the source and target of these events. For example, if code is copied from an untrusted source, the tool can flag this anomaly and alert the user before token generation occurs.

### Defenses for Permission Hijacking

Organizations can combat consent phishing through strict name-checking and mandatory user consent rerouting. Security posture management tools must enforce policies that automatically block consent requests from apps with vague or impersonating names. Ultimately, enterprises should disable end-user consent for third-party integrations entirely, routing all requests through an admin consent workflow where security teams can review and prune excessive scopes before authorization.

### Defenses for Malicious Redirects

To prevent attackers from weaponizing OAuth callback URLs to deliver malware or steal credentials, organizations must mandate redirect destination audits. This requires a continuous, automated inventory of all registered applications to ensure every configured redirect\_uri points to verified domains. Any app attempting to register an external, recently created or unmanaged domain as a callback target must be automatically quarantined to neutralize redirect exploitation.

User awareness is the final line of defense against social engineering. Employees must treat OAuth consent screens with the same scrutiny as password fields. They should not grant permissions to apps with vague names or excessive scopes and avoid copy-paste authorization or device codes into unverified chat applications.

## Conclusion

OAuth-based phishing represents a fundamental shift in our threat landscape. Attackers no longer need to steal credentials when they can harvest tokens that bypass MFA entirely and persist through password resets.

Defending against this threat requires visibility where the attack happens:

- In the browser
- At the moment of authorization
- Before a token is ever issued

Organizations that wait for credential-based alerts or rely solely on post-authentication controls will find themselves unable to see these attacks. In our next blog, we’ll discuss how OAuth attacks are expected to evolve, especially with AI agents.

## Additional Resources

- [The OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749) — Internet Engineering Task Force (IETF)
- [The OAuth 2.1 Authorization Framework](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1) — IETF
- [What is the Evolution of Multifactor Authentication](https://uthentication) — Palo Alto Networks
- [Everybody’s Looking for SSOmething: A large-scale evaluation on the privacy of OAuth authentication on the web](https://petsymposium.org/popets/2023/popets-2023-0119.pdf) — Privacy Enhancing Techniques Symposium
- [Credential Phishing: What It Is and How to Prevent It](https://www.rsa.com/resources/blog/passwordless/credential-phishing-what-it-is-and-how-to-prevent-it/) — RSA
