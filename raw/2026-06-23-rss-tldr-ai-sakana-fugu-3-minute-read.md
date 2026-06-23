---
source: "https://threadreaderapp.com/thread/2068862070062485867.html"
title: "Sakana Fugu (3 minute read)"
author: "TLDR AI"
date_published: "Mon, 22 Jun 2026 00:00:00 GMT"
date_clipped: "2026-06-23"
category: "AI / LLM Research & Tooling"
source_type: "rss"
discovered_via: "https://tldr.tech/ai/2026-06-22"
source_role: "primary-via-tldr"
---

# Sakana Fugu (3 minute read)

Source: https://threadreaderapp.com/thread/2068862070062485867.html

Thread by @SakanaAILabs on Thread Reader App – Thread Reader App 
Thread Reader
Share this page! 
× 
Post 
Share 
share-email#click" href="mailto:?subject=Thread%20by%20@SakanaAILabs%20on%20Thread%20Reader%20App&body=@SakanaAILabs:%20Introducing%20Sakana%20Fugu:%20A%20full%20multi-agent%20orchestration%20system%20accessible%20via%20a%20single%20model%20API.%20Our%20%E2%80%98Fugu%20Ultra%E2%80%99%20model%20matches%20the%20performance%20of%20Fable%20and%20Mythos,%20delivering%20frontier%20capability%20w...%E2%80%A6%0A%0Ahttps://threadreaderapp.com/thread/2068862070062485867.html"
data-category="sharebuttons" data-action="share-by-email" data-label="">
Email 
Enter URL or ID to Unroll 
× 
Unroll Thread 
You can paste full URL like: https://x.com/threadreaderapp/status/1644127596119195649 
or just the ID like: 1644127596119195649 
How to get URL link on X (Twitter) App 
On the Twitter thread, click on or icon on the bottom
Click again on or Share Via icon
Click on Copy Link to Tweet
Paste it above and click "Unroll Thread"! 
More info at Twitter Help 
twitter-profile#error" > 
Sakana AI 
Subscribe
@SakanaAILabs 
Jun 22 • 
10 tweets • 8 min read • 
Read on X
Scrolly 
Bookmark 
Gift Link
Save as PDF 
thread#showTweet" data-screenname="SakanaAILabs" data-tweet="2068861630327443966" dir="auto">
Introducing Sakana Fugu: A full multi-agent orchestration system accessible via a single model API.
Our ‘Fugu Ultra’ model matches the performance of Fable and Mythos, delivering frontier capability without the risk of export controls.
Try it: 🐡 sakana.ai/fugu 
thread#showTweet" data-screenname="SakanaAILabs" data-tweet="2068862070062485867" dir="auto">
Fugu stands shoulder-to-shoulder with leading models like Fable and Mythos across the industry's most rigorous engineering, scientific, and reasoning benchmarks.
Read the full blog: sakana.ai/fugu-release 
Beyond Bigger Models: Why are Orchestration Models the Next Frontier
Progress in AI has been driven largely by giant, monolithic models. But the most powerful systems of the future will be collaborative ecosystems.
Today, this orchestration is no longer just a technical optimization. It has become a geopolitical and operational imperative.
For an organization or a nation, relying on a single company's model for critical infrastructure, finance, or governance is a material vulnerability. This risk is no longer a hypothetical possibility, but a reality.
As we have seen with recent export controls imposed on models like Fable and Mythos, access can disappear overnight.
Collective intelligence is the practical hedge against this concentration of power. Because Fugu orchestrates an underlying pool of swappable agents, it simply routes around vendor restrictions.
By orchestrating the world’s models, we are delivering the resilient blueprint required for true AI sovereignty. 
thread#showTweet" data-screenname="SakanaAILabs" data-tweet="2068862344684581023" dir="auto">
How does it work?
Sakana Fugu is itself an LLM, trained to call various LLMs in an agent pool, including instances of itself recursively. Fugu dynamically orchestrates the world's best models to tackle complex, multi-step tasks.
As shown in this figure, Fugu is a multi-agent system that behaves like a single model. You send a request to one endpoint, and Fugu decides how to handle it internally.
Fugu manages model selection, delegation, verification, and synthesis automatically. It solves tasks directly when that is enough, or coordinates a team of expert models when a problem calls for more. The complexity of a multi-agent system never reaches your code.
At launch, Sakana Fugu comes in two models accessed via a single OpenAI-compatible API:
• Fugu balances strong performance with low latency for everyday work. It fits naturally into tools like Codex for coding, as well as chatbots and interactive services. You can also opt specific agents out of its pool for data compliance.
• Fugu Ultra is our flagship model tuned for maximum answer quality on hard, multi-step problems. It coordinates a deeper pool of expert agents for demanding work like AI research, cybersecurity analysis, and patent investigations. 
thread#showTweet" data-screenname="SakanaAILabs" data-tweet="2069079051239874657" dir="auto">
Benchmarks tell only part of the story.
Fugu’s real value shows up in long, messy, real-world workflows. During our beta with 500 users, we saw Fugu Ultra drive meaningful progress in fully automated tasks from data science to complete cybersecurity assessments.
Our early users saw Fugu explore, interpret failures, and sustain progress with almost zero human intervention. The feedback has been incredible. Here is what they are saying: 
thread#showTweet" data-screenname="SakanaAILabs" data-tweet="2069084332879462779" dir="auto">
Use Case 1: Autonomous ML Research
Can an AI autonomously improve another AI’s training recipe?
We tasked Fugu Ultra with improving a small GPT model using AutoResearch. Over 14 hours on a single H100 GPU, Fugu ran > 100 experiments. It iteratively edited the training code, ran tests, and kept any changes that successfully lowered the validation error rate.
Watch the animation. The callouts track every time Fugu Ultra autonomously discovered a new improvement across batch size, model depth, learning rates, and optimizer settings.
We pitted Fugu against three frontier models (Gemini 3.1 Pro, Opus 4.8, and GPT 5.5). To keep the focus purely on agentic behavior rather than brand wars, we anonymized them as Models A, B, and C.
The Results:
• Fugu Ultra (bold red) finished with the best mean performance (0.9774).
• Fugu Ultra also achieved the best single run of the entire experiment (0.9748), leading every single baseline.
For long horizon, agentic ML research, using Fugu to dynamically orchestrate a pool of strong models significantly outperforms relying on any individual monolithic model. 
thread#showTweet" data-screenname="SakanaAILabs" data-tweet="2069086336955646322" dir="auto">
Use Case 2: Financial Time Series Prediction
Can an AI agent navigate sequential, no-look-ahead market decisions?
Just for fun, we tested Fugu Ultra on 50 weeks of historical data for an anonymized equity (STOCK_X). Starting with $10,000, the agent processes weekly market data (prices, volume, moving averages, volatility) and decides whether to buy, hold, or sell.
After each action, the next week's price is revealed. The model must adapt purely from feedback, without ever seeing the future.
The Results across five identical 50-week runs:
• Fugu Ultra grew the portfolio to $11,943.22 (a +19.43% mean return).
• The other frontier models (Models A, B, and C) all capped out at less than a +15% return.
(Mandatory disclaimer: Past performance does not guarantee future results, and results may not transfer to other assets, time periods, or live markets.) 
thread#showTweet" data-screenname="SakanaAILabs" data-tweet="2069088009790861312" dir="auto">
Use Case 3: One-Shot Blindfold Chess
Can an AI hold an entire game state in memory without drifting?
To test Fugu Ultra’s persona stability and sustained memory, we had it play 4 back-to-back games of blindfold chess. Every model played the same way: no board shown, requiring them to hold the full game state entirely in memory.
We matched Fugu Ultra against 3 leading frontier models and a 2100-Elo Stockfish engine.
The Results: Fugu Ultra outplayed all 4 opponents. Where the other models eventually drifted or lost track of the board state, Fugu remained accurate, ending every single game in checkmate.
Watch the full sequence below to see Fugu capitalize the moment the other models slip. 
thread#showTweet" data-screenname="SakanaAILabs" data-tweet="2069089571208679469" dir="auto">
Use Case 4: Computer Aided Design of Mechanical Iris
Can an AI generate precise, functional mechanical designs?
We tasked Fugu Ultra with creating a mechanical iris in CAD, similar to a camera aperture where multiple blades must move together to cleanly open and close a central hole.
Watch the animation below. We show both the detailed CAD and a simplified structural view for Fugu and the three frontier baselines.
The Results:
• Fugu Ultra generated a highly functional design. The blades rotate correctly around outer pins to fully open and close the aperture.
• Models A, B, and C failed the physical logic, resulting in gaps, weak linkages, and incomplete closure.
When a task demands exact spatial precision and structural reasoning, relying on a single model is simply not enough. 
thread#showTweet" data-screenname="SakanaAILabs" data-tweet="2069264211822403772" dir="auto">
Use Case 5: Rubik’s Cube Solver
Can an AI write complex algorithmic solvers from scratch?
We tasked Fugu Ultra and three frontier models with writing a Rubik’s Cube solver in pure Python from a single prompt. No off-the-shelf solving libraries were allowed. We then ran the resulting programs locally on 300 randomly scrambled cubes.
In this example, Fugu Ultra’s solver reaches the goal in 19 moves compared to Model A (best of the three models)’s 21 moves.
The Results:
• Fugu Ultra and Model A generated solvers that successfully ran and solved all 300 cubes.
• Models B and C shipped sophisticated-looking code that completely crashed on execution (0/300).
• Fugu Ultra was strictly more efficient, averaging 19.72 moves versus Model A’s 19.76, and never requiring a single move more than Model A across all 300 scrambles.
For code generation that actually executes and optimizes for efficiency, dynamically orchestrating multiple agents beats relying on a single monolithic model. 
thread#showTweet" data-screenname="SakanaAILabs" data-tweet="2069265784250290234" dir="auto">
Use Case 6: Classical Japanese Kana Reading Order
It would not be a Sakana AI launch without a uniquely Japanese challenge. Can an AI decipher the chaotic layout of a 400-year-old letter?
We tested whether the models could recover the reading order of "scattered writing" (chirashigaki) in a letter from 1610. This letter is held by the Keio Institute of Oriental Classics. Given character bounding boxes and a rough set of rules, the models had to write code to predict the exact order the characters should be read.
In the clip below, the green line is the expert ground truth. The red line is the AI’s prediction.
The Results:
• Fugu Ultra achieved a 0.80 accuracy score, tracing the highly complex path almost exactly.
• Models A and B scored a dismal 0.24, jumping wildly and incorrectly all over the page.
• Model C failed to produce a working predictor at all.
You might not decode 17th-century calligraphy every day, but this proves Fugu’s unparalleled ability to handle extreme spatial reasoning and completely novel, non-linear logic. 
• • •
Missing some Tweet in this thread? You can try to
force a refresh 
Post 
Share 
share-email#click" href="mailto:?subject=Thread%20by%20@SakanaAILabs%20on%20Thread%20Reader%20App&body=@SakanaAILabs:%20Introducing%20Sakana%20Fugu:%20A%20full%20multi-agent%20orchestration%20system%20accessible%20via%20a%20single%20model%20API.%20Our%20%E2%80%98Fugu%20Ultra%E2%80%99%20model%20matches%20the%20performance%20of%20Fable%20and%20Mythos,%20delivering%20frontier%20capability%20w...%E2%80%A6%0A%0Ahttps://threadreaderapp.com/thread/2068862070062485867.html"
data-category="sharebuttons" data-action="share-by-email" data-label="">
Email 
Keep Current with
Sakana AI 
twitter-profile#error" >
Stay in touch and get notified when new unrolls are available from this author!
Add to "My Authors"
Read all threads 
This Thread may be Removed Anytime! 
Twitter may remove this content at anytime! Save it as PDF for later use!
Save this thread as PDF
Try unrolling a thread yourself! 
Follow @ThreadReaderApp to mention us! 
From a Twitter thread mention us with a keyword "unroll"
@threadreaderapp unroll 
Practice here first or read more on our help page !
More from @SakanaAILabs 
link#goto" >
twitter-profile#error" > 
Sakana AI 
@SakanaAILabs 
Jul 1, 2025 
We’re excited to introduce AB-MCTS!
Our new inference-time scaling algorithm enables collective intelligence for AI by allowing multiple frontier models (like Gemini 2.5 Pro, o4-mini, DeepSeek-R1-0528) to cooperate.
Blog: sakana.ai/ab-mcts 
Paper: arxiv.org/abs/2503.04412 
Inspired by the power of human collective intelligence, where the greatest achievements arise from the collaboration of diverse minds, we believe the same principle applies to AI. Individual frontier models like ChatGPT, Gemini, and DeepSeek are remarkably advanced, each possessing unique strengths and biases stemming from their training, which we view as valuable resources for collective problem-solving.
AB-MCTS (Adaptive Branching Monte Carlo Tree Search) harnesses these individualities, allowing multiple models to cooperate and engage in effective trial-and-error, solving challenging problems for any single AI. Our initial results on the ARC-AGI-2 benchmark are promising, with AB-MCTS combining o4-mini + Gemini-2.5-Pro + R1-0528, current frontier AI models, significantly outperforming individual models by a substantial margin.
This research builds on our 2024 work on evolutionary model merging, shifting focus from “mixing to create” to “mixing to use” existing, powerful AIs. At Sakana AI, we remain committed to pioneering novel AI systems by applying nature-inspired principles such as evolution and collective intelligence. We believe this work represents a step toward a future where AI systems collaboratively tackle complex challenges, much like a team of human experts, unlocking new problem-solving capabilities and moving beyond single-model limitations.
Algorithm (TreeQuest): github.com/SakanaAI/treeq… 
ARC-AGI Experiments: github.com/SakanaAI/ab-mc… 
The AB-MCTS combination of o4-mini + Gemini-2.5-Pro + R1-0528, current frontier AI models, achieves strong performance on the ARC-AGI-2 benchmark, outperforming individual models by a large margin.
We open-sourced our implementation of AB-MCTS:
github.com/SakanaAI/treeq… 
Many ARC-AGI-2 examples that were unsolvable by any single LLM were solved by combining multiple LLMs. In some cases, an initially incorrect attempt by o4-mini is used by R1-0528 and Gemini-2.5-Pro as a hint to get to the correct solution.
ARC-AGI-2 code:
github.com/SakanaAI/ab-mc… 
Read 4 tweets 
Did Thread Reader help you today? 
Support us! We are indie developers!
This site is made by just two indie developers on a laptop doing marketing, support and development! Read more about the story .
Become a Premium Member ($3/month or $30/year) and get exclusive features!
Become Premium 
Don't want to be a Premium member but still want to support us? 
Make a small donation by buying us coffee ($5) or help with server cost ($10)
Donate via Paypal 
Or Donate anonymously using crypto!
Ethereum 
0xfe58350B80634f60Fa6Dc149a72b4DFbc17D341E 
copy 
Bitcoin 
3ATGMxNzCUFzxpMCHL5sWSt4DVtS8UqXpi 
copy 
Thank you for your support! 
Follow Us! 
Post 
Share 
Send Email! 
× 
Email the whole thread instead of just a link!
Separate emails with commas 
Message 
Here's a great thread you should read right now! 
share-email#send_email">Send Thread As Email! 
Email Successfully Sent!
Help |
About |
TOS |
Privacy
