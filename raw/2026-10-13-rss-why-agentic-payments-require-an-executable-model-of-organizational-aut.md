---
source: "https://www.thoughtworks.com/insights/blog/generative-ai/why-agentic-payments-require-executable-model-organizational-authority"
title: "Why agentic payments require an executable model of organizational authority"
author: "Matt Kamelman"
date_published: "2026-10-12"
date_clipped: "2026-10-13"
category: "Software Architecture"
source_type: "rss"
---

# Why agentic payments require an executable model of organizational authority

AI agents are beginning to acquire the practical authority to spend money, but the infrastructure for doing so still needs to be developed.


Some of this is currently in the process of being built. The Linux Foundation, for instance, [recently launched the x402 Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-operational-launch-of-x402-foundation-to-standardize-internet-native-payments-for-ai-agents-and-applications) with 40 members, including Visa, Mastercard, American Express, Stripe, Coinbase, AWS, Google, Shopify and Adyen. The protocol embeds payments into ordinary web interactions, allowing agents and applications to pay for services through the same request and response cycle they use to exchange data. Elsewhere, Google’s [Agent Payments Protocol](https://developers.googleblog.com/developers-guide-to-ai-agent-protocols/), or AP2, addresses authorization through cryptographically signed mandates, Mastercard has introduced Agent Pay for Machines and Visa is integrating agent-initiated purchasing into its network. Natural, a new payments company built specifically for agents, has raised $30 million to provide wallets, accounts, cards, transfers, identity and transaction observability through a unified interface.


While there’s clear movement across the industry, for most organizations there’s still a question of turning the process of purchasing decisions and oversight into machine-readable infrastructure. Most enterprises have never made those systems explicit enough to do that; encoding the contextual richness of even the most ordinary transaction is difficult.

## Authorization cannot capture organizational judgment


The critical issue in this area is growing separation between the instruction to act and permission to spend.


AP2 uses mandates to represent what a person or organization intended, what purchase an agent subsequently assembled and what was finally paid. [Mastercard’s Verifiable Intent work and the FIDO Alliance’s](https://fidoalliance.org/fido-alliance-to-develop-standards-for-trusted-ai-agent-interactions/?) new working groups pursue a similar objective: creating cryptographic evidence that an agent’s action corresponds to an authenticated principal’s instruction. Natural ties stable agent identities to verifiable legal identities and advertises observability and dispute management around every payment.


Although these controls are necessary, none of them resolves the problem. Payment systems verify transactions, but enterprises need to govern what those transactions collectively commit the organization to. Ten individually permitted purchases may increase dependence on one supplier, expose sensitive data across multiple services, create overlapping contractual obligations or establish a commercial precedent that constrains future decisions.


This is harder to encode. The authority exercised by experienced employees includes accumulated knowledge of why certain spending rules exist and exceptions. Much of this will never have been formalized.


### An authority model


Once agents can transact, organizations need an authority model. This model should connect an agent’s identity to a legal principle, a business purpose, an owner, a budget, a defined class of counterparties and a time-bounded mandate. It should also represent existing commitments, contractual boundaries and the precedents created by prior actions. The system must preserve the reasoning and evidence that led to each transaction, while recognizing that a model-generated explanation is not the same thing as a faithful causal record.


Governing each payment is no longer sufficient. The authority model must also evaluate how the agent’s actions accumulate over time, including whether individually permitted transactions are creating contractual obligations, supplier dependencies, data exposure or other commitments beyond the intended mandate.

## A new attack surface appears before mass adoption


Security research is already exposing the weakness of treating agent intent as application state. Researchers testing AP2 have shown it’s possible to manipulate the context that informs a purchasing decision. The danger isn’t limited to stolen credentials. An attacker may leave the wallet, signature and payment rail functioning exactly as designed while corrupting the agent’s interpretation of what it was asked to do.


This changes the fraud model. Traditional controls look for an unauthorized user, an unusual merchant, a suspicious device or an anomalous amount. Agentic fraud may arrive as an apparently authorized transaction produced by compromised context. The payment could satisfy every conventional control and still be contrary to the principal’s real intent. It may also alter the organization’s wider position in ways that cannot be inferred from the transaction alone.


The response cannot be permanent human approval of every purchase; that would preserve accountability by removing the operational value of autonomy. Nor can it be a single budget limit placed around an agent. The appropriate control depends on the reversibility, value and uncertainty of the action.


Low-value purchases of well-defined digital services may operate within standing mandates and deterministic caps. A new supplier, a long-term contract, a transaction involving sensitive data or an unusual change in purchasing pattern should trigger additional verification. Irreversible or regulated actions may require explicit human approval regardless of value. Controls must also work across time, because a harmful sequence can be composed entirely of permissible individual transactions. An attacker doesn’t need to breach a spending limit if the same result can be produced through a series of small purchases, gradual supplier concentration or repeated disclosures of individually permissible data.


This is bounded autonomy applied to money. The objective isn’t deciding whether an agent is trusted, it’s to specify what this agent is allowed to decide, with which funds, under which conditions, for how long and with what route of escalation.

## The market may divide by governance model, not payment rail


The international picture complicates the idea of one universal agent-payments standard. Alipay has introduced an AI wallet and Token Pay infrastructure for agentic commerce in China. Its existing distribution gives it a different starting position from a new protocol trying to recruit merchants one by one. Recent reporting indicates that Alipay’s AI Pay handled 120 million transactions in a week through conversational purchasing experiences.


This doesn’t yet prove a clean geopolitical split. x402 itself includes KakaoPay and other organizations outside the United States, while card networks and cloud platforms operate across jurisdictions. It does show that agentic payments will inherit the institutional structure of existing payment systems. Identity rules, data localization, consumer protection, settlement assets and state oversight will shape which forms of agent authority are permissible.


The Bank of England has already warned that existing frameworks were not designed for autonomous agents and has raised the need for circuit breakers or kill switches. The IMF has similarly identified liability, accountability, fraud and operational concentration as material concerns in agentic payments. Regulators are not yet presenting a settled regime, but they’re no longer treating the subject as distant.


The likely fragmentation may therefore be deeper than competing technical protocols. Different markets may accept different answers to who can delegate authority, how consent must be represented, which data may travel with a transaction and who remains liable when an agent’s valid action produces an invalid outcome.

## Economic authority has to become executable


For enterprises, the immediate question isn’t whether to give every agent a wallet. It’s whether the organization understands its own economic authority well enough to express it in a form that software can enforce and people can audit.


That requires more than translating an approval matrix into policy code. Organizations will need to identify which parts of economic judgment are deterministic, which depend on current organizational context and which should remain human. A spending ceiling can be enforced directly. The significance of a new contractual precedent, growing reliance on one supplier or an unusual combination of otherwise acceptable purchases may require contextual evaluation and escalation.


Several capabilities have to work together. Agents need stable identities that map to accountable legal entities and human owners. Mandates need explicit purpose, duration, counterparty and cumulative spending constraints. Authorization must be evaluated both per action and across the history of a workflow. It must also account for commitments that do not appear as expenditure alone, including exclusivity, renewal obligations, data access, switching costs and supplier dependency. The organization needs independent records of requests, evidence, decisions, approvals, settlements and exceptions. Revocation and emergency stops must propagate quickly across agents, wallets and payment providers. Disputes, refunds and failed transactions need an accountable owner rather than an unattended queue.


This creates a knowledge problem as much as a control problem. Relevant precedent may sit in contracts, procurement systems, risk registers, past exceptions, correspondence and the experience of employees who have never been asked to make their reasoning explicit. If that knowledge cannot be assembled at the moment of decision, the agent may comply with every encoded rule and still act against the organization’s interests.


Procurement, finance, security, legal and engineering will all recognize parts of this problem. None of them owns it alone. That may be the most difficult aspect of the transition. Agent-native payment systems require organizational authority to become executable, but the technology cannot decide how that authority should be divided or recover institutional judgment the organization has never articulated.


The sensible starting points are narrow. Machine purchases of metered APIs, compute or data within a fixed budget have clear value, small transaction sizes and relatively observable outcomes. They create an environment in which organizations can test mandate design, anomaly detection, reconciliation and revocation without first delegating high-consequence commercial judgment.


Even there, transaction volume should not be mistaken for business value. A system capable of making thousands of tiny purchases can accumulate cost, dependency and data exposure faster than traditional review cycles can see them. The economics of an agent are not contained in what it spends. They include the commitments, information flows and operational dependencies its spending creates. Enterprise observability will therefore have to show not only where money went, but how the organization’s economic position changed as a result.

## Money makes the hidden architecture of authority visible


Agent-native payments are arriving through a mix of open protocols, existing networks and new financial infrastructure. There is enough activity to dismiss neither the category nor its risks. There is not yet enough evidence to claim that autonomous enterprise spending has become routine.


That uncertainty should not delay architectural work. Payment is one of the clearest places to define delegated authority because the consequences are measurable and the action creates a durable record. It is also where organizations may discover how much of their authority model has never been written down. Rules that appeared sufficient while experienced people were interpreting them may prove incomplete when software has to apply them directly.


The controls developed here may become useful far beyond commerce, wherever agents are permitted to make consequential decisions on behalf of an organization. The deeper architectural task is to make authority executable without pretending that all organizational judgment can be reduced to rules.


The payment rail will determine whether an agent can move money. An authorization mechanism will determine whether a transaction satisfies a mandate. Neither can determine, on its own, whether a sequence of valid actions is creating an economic position the organization would knowingly accept.


**Agentic payments are therefore exposing a problem enterprises already had but could leave implicit while humans carried the missing context. Once agents begin to spend, that hidden architecture of authority has to become visible, machine-readable and governable across time.**
