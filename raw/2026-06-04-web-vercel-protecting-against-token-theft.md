---
source: "https://vercel.com/blog/protecting-against-token-theft"
title: "Protecting against token theft"
author: "unknown"
date_published: "unknown"
date_clipped: "2026-06-04"
category: "Security & Ethical Hacking"
source_type: "web"
---

# Protecting against token theft

Source: https://vercel.com/blog/protecting-against-token-theft

5 min read
Copy URL May 29, 2026 HTTP requests are inexpensive. Vercel charges ~$2/million, a fraction of a cent per call. But a single prompt to an agent on a frontier model can cost $2, making AI a million times more expensive, and inference theft one of the highest-margin businesses an attacker can run. We have seen this type of attack on our own APIs.
If you have AI endpoints exposed to the internet, the risk of abuse is high and can easily run up bills in the tens of thousands of dollars or more.
Protecting those endpoints requires verification to run on every AI request, not on the session or signup. Rate limits and auth walls aren't sufficient on their own because checks that run once per session get amortized away across thousands of stolen calls.
At Vercel, we gate every AI request through BotID deep analysis, and you can do the same on your own endpoints with a few lines of code.
Link to heading What inference theft is Inference theft is the unauthorized use of someone else's paid AI inference, either for free consumption or downstream resale. The operator pays per AI call; the attacker pays nothing for inference and then resells the tokens at a discount. This goes beyond rate-limit abuse to actual resale of a stolen resource in a market. 
Link to heading Which AI endpoints are at risk? Any internet-facing endpoint that gives a caller meaningful control over an LLM prompt is a target. The more general the endpoint, the higher the payout per stolen call.
AI playgrounds, like the AI SDK Playground , are the most dangerous shape because the caller has maximum control over the prompt, the model, and often the parameters. Stolen calls land cleanly into any standard client. 
Support bots and documentation assistants are less exposed when system prompts are fixed server-side, but attackers have learned how to talk the models around system prompts cheaply enough to make resale viable.
Resale value tracks how easily the stolen calls can be dropped into a provider-compatible client.
Link to heading Why web defenses don't mitigate inference theft IP rate limits and auth walls were built to defend against attacks with dramatically lower per-call economics, where gaming IPs and accounts weren't worth the cost.
The payoff from stolen inference is high enough that attackers will procure residential proxy IPs by the thousands and register throwaway accounts at whatever scale it takes to defeat your gate. Rate limits get diluted across the fleet of IP addresses, and real accounts pass authentication.
Link to heading The architecture of abuse Sophisticated attackers wrap your custom AI endpoint in an OpenAI- or Anthropic-compatible adapter and fan calls out through residential proxies. 
The adapter is the key component. It is a one-time engineering cost that presents the victim's idiosyncratic API as OpenAI- or Anthropic-compatible, so stolen inference can drop into any standard coding agent or SDK. Reselling at even five to ten percent of the list price, with zero marginal inference cost, can make for a generous-margin business. 
A recent example is Chipotlai Max , a forked coding agent that ships with a proxy turning Chipotle's customer-support chatbot into an OpenAI-compatible endpoint. The project openly solicits help in porting the same inference-theft approach to Home Depot, Lowe's, Target, and Starbucks.
The adapter also serves as the session boundary for the attacker's downstream users. They authenticate to the adapter, not to your endpoint. By the time a call hits your API, it has already crossed the boundary you were planning to defend. The check has to run on the call the adapter proxies, not on the session it sits behind.
Link to heading The shape of a real attack on our own endpoint On April 12, 2026, traffic to the Vercel docs AI chat endpoint spiked to roughly ten times normal volume on Anthropic's Claude Haiku 4.5 model. Traffic rose to 1,300 requests per minute at peak, which would have translated to an inference cost run rate of over ten thousand dollars per day.
The attack came in through residential proxies that obscured the real client IPs. Across hundreds of thousands of bot requests over two days, standard per-IP rate limits had nothing useful to act on.
Link to heading How to defend against inference theft Protecting AI endpoints against inference theft requires verification of every request. We use Vercel's BotID with deep analysis, called inside the route handler before the AI request lands.
Link to heading Verification has to run on every AI request If our gate had run at session start instead of per request, the attacker would have paid the bypass cost once and walked away with hundreds of thousands of stolen calls. Any check that runs per session amortizes the attacker's bypass cost across every subsequent inference call. Per-request gates force that ratio down to one, and even at high inference prices, defeating a check on every call isn't worth the cost.
This is where the cost asymmetry works in the defender's favor. Inference is the most expensive resource per call that the attacker steals, but verification is one of the cheapest protection costs per call. 
Link to heading Implementing request verification with BotID deep analysis Traditional image CAPTCHAs no longer hold up against modern attackers because the same AI models that make inference worth stealing can easily bypass them. 
We deploy Vercel BotID on our AI endpoints, gating every request. BotID is an invisible CAPTCHA with deep analysis powered by Kasada that uses client-side machine learning to distinguish humans from bots without a visible challenge, so it can run on every request rather than only at session start. 
BotID deep analysis detected and blocked more than ten thousand bot requests in the first minutes of the spike. Within twenty-four hours, request volume on the endpoint was flat at normal levels.
Server-side, checkBotId() runs inside the route handler and returns a classification for the request currently being served.
1 // app/api/ai-chat/route.ts 2 import { checkBotId } from 'botid/server' ; 3 import { NextRequest , NextResponse } from 'next/server' ; 4 
5 export async function POST ( request : NextRequest ) { 6 const verification = await checkBotId ( ) ; 7 if ( verification . isBot ) { 8 return NextResponse . json ( { error : 'Access denied' } , { status : 403 } ) ; 9 } 10 // Your existing AI SDK call path 11 } 
The route also has to be declared on the client. Without this, checkBotId() fails because BotID doesn't attach the challenge headers to the request:
1 // instrumentation-client.ts 2 import { initBotId } from 'botid/client/core' ; 3 
4 initBotId ( { 5 protect : [ { path : '/api/ai-chat' , method : 'POST' } ] , 6 } ) ; 
See the BotID docs for the next.config.ts wrapper and the full setup.
Link to heading Protect inference, not just access Inference will remain orders of magnitude more expensive than the requests it carries, so resale will remain profitable, and attackers will keep iterating. 
To protect your AI endpoints: 
Audit which of your AI endpoints are exposed
Prioritize by attack likelihood: more caller prompt control means an easier target
Gate every endpoint on every request
Protect your AI endpoints with Vercel BotID 
Stop bots from draining your AI budget: see how to gate your endpoints with Vercel BotID in a few steps.
Read the guide
