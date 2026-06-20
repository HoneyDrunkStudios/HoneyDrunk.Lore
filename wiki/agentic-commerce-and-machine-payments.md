# Agentic Commerce and Machine Payments

## Decision-useful summary
Agentic commerce moves AI from passive assistance toward software agents that can make machine-to-machine purchasing, routing, and usage decisions under credential, spending, identity, and audit controls. The durable signal for HoneyDrunk is not "let agents buy things"; it is that payment and API platforms are preparing rails for autonomous microtransactions, which means business systems must be modernized for high-frequency, policy-constrained, auditable agent actions before real autonomy is safe. [source: raw/2026-06-20-web-thoughtworks-the-reality-of-agentic-commerce-moving-from-passive-ai-co.md]

## Source-backed claims
- Thoughtworks frames Mastercard Agent Pay for Machines as evidence that enterprise AI is moving from copilot-style assistance toward autonomous machine payments and software agents that perform high-velocity microtransactions with other systems. Source: `raw/2026-06-20-web-thoughtworks-the-reality-of-agentic-commerce-moving-from-passive-ai-co.md`. confidence: 1 Thoughtworks source, last-confirmed 2026-06-20.
- The source says payment and merchant platforms are moving toward multi-rail machine-to-machine transaction infrastructure, blending card rails, account-to-account open banking, stablecoins, tokenization, and API systems for high-frequency agent demand. Source: `raw/2026-06-20-web-thoughtworks-the-reality-of-agentic-commerce-moving-from-passive-ai-co.md`. confidence: 1 source, last-confirmed 2026-06-20.
- Thoughtworks argues the hard enterprise blocker is often legacy infrastructure built for human-initiated transactions and batch processing, not only payment rail availability. Source: `raw/2026-06-20-web-thoughtworks-the-reality-of-agentic-commerce-moving-from-passive-ai-co.md`. confidence: 1 source, last-confirmed 2026-06-20.
- The source identifies verifiable intent, deterministic controls, pre-approved spending limits, cryptographic identity verification, and audit trails as the guardrail set that finance leaders need before handing wallet-like authority to code. Source: `raw/2026-06-20-web-thoughtworks-the-reality-of-agentic-commerce-moving-from-passive-ai-co.md`. confidence: 1 source, last-confirmed 2026-06-20.

## Typed entities
- concept: agentic commerce
- concept: machine-to-machine payments
- product/framework: Mastercard Agent Pay for Machines
- company/platform: Mastercard
- company/platform: Visa
- company/platform: Stripe
- company/platform: Adyen
- company/platform: Checkout.com
- concept: Visa Token Service
- payment rail: card network
- payment rail: account-to-account open banking
- payment rail: stablecoin
- control: pre-approved spending limit
- control: cryptographic identity verification
- control: auditable payment trail

## Explicit relationships
- Agentic commerce depends-on verifiable intent, spend controls, identity, auditability, and modern transactional APIs.
- Machine-to-machine micropayments can complement logistics, compute, data, and API consumption workflows when agents need to buy small units at high frequency.
- Legacy batch-oriented backends contradict high-frequency autonomous transaction flows.
- Agent payment authority depends-on deterministic policy and finance review; prompt-level instructions are not enough.

## HoneyDrunk implications
- Do not allow HoneyDrunk agents to spend money or trigger paid services autonomously until budget, approval, identity, receipt, reconciliation, and rollback policies are explicit.
- For future agent-run SaaS or infrastructure tasks, record cost-causing tool calls as payment-like events with actor, scope, purpose, limit, and receipt.
- Evaluate usage-based billing and machine-payment designs together with fraud, quota, idempotency, and tenant-isolation controls.

## Confidence and quality notes
- Thoughtworks is a practice/market signal, not payment-network documentation. Verify product details with primary Mastercard/Visa/processor docs before implementation.
- Privacy filter: no private payment data or credentials were present in the source.
