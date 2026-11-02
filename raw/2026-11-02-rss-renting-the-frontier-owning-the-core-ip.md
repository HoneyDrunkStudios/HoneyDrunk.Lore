---
source: "https://www.thoughtworks.com/insights/blog/generative-ai/renting-the-frontier--owning-the-core-ip--how-we-cut-ai-forecast"
title: "Renting the frontier, owning the core IP"
author: "Andy Nolan"
date_published: "2026-10-15"
date_clipped: "2026-11-02"
category: "Software Architecture"
source_type: "rss"
---

# Renting the frontier, owning the core IP

**TL;DR**

By September 2026, Thoughtworks was spending $450K a month on frontier model APIs for internal use alone, and the bill was growing about 27% a month.

![](https://www.thoughtworks.com/content/dam/thoughtworks/images/infographic/monthly-growth-chart.png)

**So, we built a token sourcing strategy:** A deliberate choice, workload by workload, of which models we use and where they run, balancing cost, IP protection and regional regulation. Built on our own traffic data, and proven with actual hardware, the strategy was approved and funded to give every Thoughtworker expanded access to AI.

Against the "do-nothing" forecast, the strategy cuts the worst-case bill by 55% in 2027 and by 72% in 2028. Doing nothing is forecast at $16M in 2028, and up to $40M if growth doesn't slow; the strategy lands between $6.8M and $11M at 70–90% confidence. Our approach provides leadership with a range they can forecast against, and confidence to scale AI with the right controls in place.

![](https://www.thoughtworks.com/content/dam/thoughtworks/images/infographic/rent_the_frontier_own_the_ip.png)

The strategy rents frontier models for the work that needs frontier-level reasoning. It runs open-weight models, on capacity we choose, for the work that carries our IP or runs at a volume where owning the capacity costs less.

**This article covers the problem most organizations face: **Scaling AI while managing cost, IP and regulation in balance, the process we followed, and why we think any enterprise should follow it.

## Where your tokens come from

Every organization now has a token sourcing strategy. Most have not written it down. It reads: buy everything from a handful of AI labs, at their prices, on their terms, and trust them to protect and respect the critical IP you send their way on a daily basis. That was a reasonable default two years ago. It is a questionable one now for two reasons: cost and IP protection.

Thoughtworks' monthly spend on frontier model APIs grew more than eightfold over the first nine months of 2026, as AI use spread from a handful of early adopters towards everyone in the organization. Without intervention, the annual bill was on course for tens of millions of dollars by 2028.

Besides spending, there is a second more subtle issue. Every prompt sent to a third-party model provider is something of value: source code, delivery methods. As more of the company's work runs through models owned by someone else, more of its know-how sits outside its control. When we looked, we owned none of the intelligence we depended on.

[Sovereignty](https://www.thoughtworks.com/what-we-do/enterprise-ai/ai-factory/ai-sovereignty) used to mean where the data sits. It now means who owns your intelligence. An enterprise that routes all of its work through a handful of AI labs carries a concentration risk it would not accept from any other supplier.

Each model provider can see how its customers use it, even when it does not train on their data. Microsoft's chief executive, [Satya Nadella, wrote in July 2026](https://snscratchpad.com/posts/reverse-information-paradox/) that models learn from the prompts, tools and corrections their customers supply, and that "every correction is distilled into institutional know-how". The AI labs are now building businesses in the markets their customers serve. None of this requires bad faith. It is what any supplier does with a clear view of demand.

Both problems, cost and IP protection, have the same cause: all of the intelligence is rented from suppliers the enterprise does not control. The answer is not to stop renting. Frontier models are worth their price for some work. The answer is to decide, workload by workload, which AI you rent and which you own.

Enterprises are already making that decision. A [September 2026 survey by Enterprise Technology Research](https://techstrong.ai/articles/open-weight-ai-models-expected-to-capture-41-of-enterprise-token-usage/) found that open-weight models now carry 34% of enterprise AI token usage, up from 23% a year earlier, with 41% expected within twelve months, and 69% of production users cited cost savings.

There are so many options available to enterprises today, you just need to spend the time to consciously think about your [token sourcing strategy](https://www.thoughtworks.com/what-we-do/enterprise-ai/ai-factory/token-economics). What follows is how we made the decision for ourselves.

## Rent the frontier, own the rest

A deliberate token sourcing strategy chooses a model per workload, based on six questions:

**Domain differentiation (vertical axis):**

How unique is the task to us?

What if a competitor used the same model?

How much does a better model change the result?

**Security and sovereignty (horizontal axis):**

Can the data leave our environment?

Where must it run?

What if the provider changed terms or switched off?

Those two sets of questions place a workload on a grid, the heat map of the [hybrid AI](https://www.thoughtworks.com/what-we-do/enterprise-ai/ai-factory/hybrid-ai-strategy) estate shown below. The vertical axis is how much the model differentiates us: commodity compute for stable, high-volume work; frontier-level reasoning, where the best model wins; or custom tuning, where the model learns from our data. The horizontal axis is how much [security and sovereignty](https://www.thoughtworks.com/what-we-do/enterprise-ai/ai-factory/ai-sovereignty) the work needs: a vendor-hosted API, our own cloud account in our region, or a governed enclave on infrastructure we run.

![](https://www.thoughtworks.com/content/dam/thoughtworks/documents/blog/machine-learning-and-ai/tw_blog_token_sourcing_image1.png)

The nine cells run from the cheapest capable API, swapped as prices change, to a fine-tuned open model on our own infrastructure, with full control and full upkeep. For a given workload, the highest score on a given axis determines the right position in the grid. There is no single right place for all workloads. Each organization ends up with its own distribution and mix of workloads across the grid.

![](https://www.thoughtworks.com/content/dam/thoughtworks/documents/blog/machine-learning-and-ai/tw_blog_token_sourcing_image2.png)

Frontier models earn their price on the third question: high-complexity reasoning, strategy, creative work, anything new. Open-weight models take the rest: the domain-specific, sensitive and high-volume work. Anyone can download their weights and run them on infrastructure they control. Out of the box they are generally not as capable as a frontier model, and that is fine, because they do not have to be. The best benchmark for any model is your business. So by post-training open-weight models on your specific task you can close the performance gaps. The result is a model that does your work well, runs where you choose, and stays yours.

We have tested this twice as an NVIDIA early access partner. Our results with [Nemotron 3.5 Lightning](https://www.thoughtworks.com/insights/blog/generative-ai/putting-nvidia-nemotron-3-5-lightning-test) and [Nemotron 3.5 Super VL](https://research.thoughtworks.com/library/nemotron-3-5-super-vl-test) show adapters trained in hours on domain-specific tasks, and models optimized roughly halving GPU cost per output token.

That is why open-weight models belong in every token sourcing strategy. They are not a replacement for the frontier. They are the only way to run the domain-specific, sensitive and high-volume work at a cost you control, on infrastructure you choose, without handing the work itself to a supplier. A strategy that sources only from frontier labs has decided the cost and ownership questions by default.

## How we built the strategy

We built the strategy on our own AI usage data, with the methods and tooling our AI Factory team offers clients. It took six steps, each run on measured traffic rather than on assumptions. Any enterprise that routes its AI requests through a gateway can repeat them.

**Start from the gateway logs.**Every request already passed through our AI gateway, so the logs told us who used which model, for what kind of work, at what hour and with how much reused context. Eighteen months of logs, covering thousands of users on frontier and open-weight models, gave us the baseline.**Map every workload to the grid.**For each workload we asked how much intelligence it needed, where its data was allowed to go, what IP its prompts carried and what it cost at volume. Regional rules set hard limits: EU traffic stays in EU regions under GDPR, and staff in China cannot use the frontier models the rest of the firm uses. The answers placed each workload in a cell of the heat map, and the cell set its sourcing option.**Segment the users and model the demand.**We grouped people by how they use AI: a few hundred heavy users who drive most of the spend, the three heaviest AI workloads, which together carried about 27% of the bill, and the long tail of everyone else. Then we modeled what demand looks like as access grows to 10,000 users and our AI products ramp up.**Benchmark the real traffic.**We replayed our traffic profile against frontier and open-weight models, and across the three hosting methods: serverless, where you pay per token with no capacity reserved; managed inference, dedicated capacity that someone else operates; and infrastructure as a service, rented GPUs which we operate ourselves. Each combination gave us a performance profile: quality on our work, tokens per task, throughput and cost.[Crusoe](https://www.crusoe.ai/)supplied the compute, our AI Factory team made it operable, and Agent/works governed which model served each task.**Simulate the uncertainty.**Nobody knows how much token demand will grow, or what models and GPUs will cost next year. So we ran Monte Carlo simulations: thousands of possible futures, each with its own demand curve and price path, and costed every sourcing option in every one of them. The output for each option is a cost range, from likely to worst case, and the probability of staying within budget.**Decide the mix.**We decided to source tokens from frontier providers for the work that needs frontier models, from serverless providers for access to open-weight models, from dedicated managed inference nodes for workloads that have reached scale, and from rented GPUs where we need better price and performance than the other options give.

Three findings from the benchmarks that shaped the mix.

**Utilization, not list price, decides the cost.**A dedicated server running flat out beats serverless on cost per token. But interactive demand follows business hours and drops to near zero at weekends. For spiky demand, serverless wins because you're not paying for idle compute.**Dedicated capacity earns its place on volume or IP.**It pays when a workload's volume will keep a server busy, or when the IP it carries has to stay in-house.**Managed or rented is a trade between price and people.**Managed inference gives the lower per-token price without a dedicated inference team. Rented GPUs give control over location, architecture and throughput, but need people to run them.

## What the numbers showed

The token source strategy provided leadership with the opportunity to control token spend, control cost and protect IP.

![](https://www.thoughtworks.com/content/dam/thoughtworks/documents/blog/machine-learning-and-ai/tw_blog_token_sourcing_image4.png)

**Do nothing:**spend keeps climbing with adoption, and the range of outcomes widens every year. By 2028 the gap between the likely case and the worst case is larger than the entire bill under the strategy.**Token sourcing strategy:**spend levels off at a fraction of the do-nothing forecast, with every Thoughtworker using AI, and the range stays narrow from one year to the next.

The tighter range matters as much as the lower number. A narrow range is something finance, risk, security and technology leadership can approve. A range that spans tens of millions is not acceptable. Running the simulation is what produces the probability ranges, and the frequent model review loop described below is what keeps spend inside it.

## Our approach

The strategy the C-suite approved gives every Thoughtworker AI access through one platform, sources the tokens behind it from the most cost-effective mix of models and providers, and keeps adjusting that mix as we measure real demand. It has four parts.

**One platform.**[Agent/works, the AI gateway and control plane we launched in June 2026](https://www.thoughtworks.com/en-us/what-we-do/enterprise-ai/agent/works/), is the one way in: each person and application reaches frontier and open-weight models through the same gateway, with one key. People choose a tier, high, medium or light, not a model or a provider. Approved models and regional constraints are enforced centrally. The gateway decides which model and provider serve each tier, so we can change what sits behind a tier without users changing anything, and move traffic between frontier, serverless and self-hosted capacity. Every request is metered and attributed to a person, a workload and a business unit, with budgets per person and per unit, and spend charged back to the unit that creates it. The same data feeds the forecasts and the model reviews.**Cost-effective model mix.**Three fixed tiers give users a curated list of current models that balance cost and quality. The top tier is a frontier model, for the highest-judgment work: complex agentic coding, strategy and research. The middle tier is a state-of-the-art open-weight model for the bulk of daily use: drafting, summarizing, code assistance and analysis. The light tier is a high-efficiency open-weight model for high-volume, low-complexity work: classification, extraction and routing. To begin with, the mix changes only slightly: the top tier stays on the frontier and the lower tiers move to open-weight alternatives.**Adjust as we learn.**Prices change faster than infrastructure. New models often cost less than the ones they replace, regional rules limit which providers we can use, new hardware changes the economics of self-hosting, and people who are light users today may be heavy users in a year. So the tiers stay fixed and what sits behind them is reviewed regularly: measure actual usage, replay the traffic profile on new models and providers, decide the mix by tier and region, then reconfigure the gateway or run optimized models on GPUs. The review is triggered by changes in workload characteristics, major price changes and model releases. Having three sources, frontier providers, token-as-a-service providers and rented or owned GPUs, is what makes the adjustment possible.**Adoption and enablement.**Wider access only stays affordable if people understand how their choices drive cost. Before access opens, every Thoughtworker hears what is changing and why, business unit leaders are briefed on what chargeback means before the first bill arrives, and policy sets the rules for key hygiene, client work and data residency. As access opens, cohorts are onboarded at a controlled pace with token-literacy training on how tokens drive cost and how to choose the right tier, and people see their own usage against their budget.

**That is what gave leadership the confidence to decide:** a purchasing decision backed by measured traffic, a review loop that holds spend within the predicted variance, and a plan to upskill people and manage the change rather than mandate it.

## The pattern any enterprise can follow

The pattern is one any enterprise can follow. Start from your gateway logs, because they already hold your usage pattern. Place every workload on the grid, with regional rules, IP, intelligence and cost as the axes. Segment your users and model demand as adoption grows. Benchmark your real traffic, not a spreadsheet, across models and hosting options. Simulate demand and price uncertainty so leadership signs a range, not a single number. Put curated models behind one gateway with fixed tiers, and review what sits behind each tier as prices, models and usage change. Keep the work that carries your IP on models you control.

**Rent the frontier. Own the rest.**
