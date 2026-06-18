---
source: "https://www.bleepingcomputer.com/news/security/malicious-jetbrains-marketplace-plugins-steal-ai-api-keys-from-developers"
title: "Malicious JetBrains Marketplace plugins steal AI API keys from developers"
author: "Lawrence Abrams"
date_published: "2026-06-16"
date_clipped: "2026-06-18"
category: "Security & Ethical Hacking"
source_type: "web"
---

# Malicious JetBrains Marketplace plugins steal AI API keys from developers

Source: https://www.bleepingcomputer.com/news/security/malicious-jetbrains-marketplace-plugins-steal-ai-api-keys-from-developers

Malicious JetBrains Marketplace plugins steal AI API keys from developers
By Lawrence Abrams
June 16, 2026
05:54 PM
0
At least 15 malicious plugins found on the JetBrains Marketplace were designed to steal AI API keys from developers.
The campaign, discovered by Aikido Security, includes plugins that act as AI coding assistants, code-review tools, and Git utilities powered by popular AI services such as OpenAI, DeepSeek, and SiliconFlow.
"We detected a coordinated malware campaign on the JetBrains Marketplace," warns Aikido .
"At least 15 IDE plugins, published under seven vendor accounts, share the same hidden behavior. Each one exfiltrates the AI provider API key that you stored into its settings, and together they have been installed close to 70,000 times."
According to Aikido, the malicious plugins were first published in October 2025, with new plugins continuing to be published as recently as June 10, 2026.
The researchers say the plugins function as advertised, but secretly transmit AI API keys entered by users into the plugin settings back to the attackers.
According to the report, the theft occurs when a user clicks "Apply" after entering an API key, causing the credential to be sent to a hardcoded server at 39.107.60[.]51 over HTTP at this URL:
hxxp://39.107.60[.]51/api/software/key
The researchers found that all 15 plugins share similar code that were submitted as different Marketplace plugins.
Aikido also discovered functionality that allows the remote server to provide AI API keys to paid users.
While it is unclear where these API keys are coming from, Aikido theorizes that the plugin operators may be harvesting credentials from the free users and then providing them to the paid users.
"The plugins also run a paid tier. After a user pays a small fee through the donation wall built into the plugin, the server sends an API key back down to the client, and the plugin starts using that key for its model calls instead of your own, which is bizarre, since no legitimate operator would simply hand a user a working and unrestricted key to a paid AI provider," says Aikido.
BleepingComputer downloaded and analyzed the latest version of the DeepSeek AI Assist plugin (plugin ID: ord.cp.code.ai.kit) and independently confirmed that it still contains the credential theft code described in Aikido's report.
At the time of writing, the plugin remained available for download through the JetBrains Marketplace.
The campaign plugins discovered by Aikido are:
DeepSeek Junit Test (org.sm.yms.toolkit)
DeepSeek Git Commit (com.json.simple.kit)
DeepSeek FindBugs (org.bug.find.tools)
DeepSeek AI Chat (org.translate.ai.simple)
DeepSeek Dev AI (com.yy.test.ai.simple)
DeepSeek AI Coding (com.dev.ai.toolkit)
AI FindBugs (com.json.view.simple)
AI Git Commitor (com.my.git.ai.kit)
AI Coder Review (org.check.ai.ds)
DeepSeek Coder AI (com.review.tool.code)
AI Coder Assistant (org.code.assist.dev.tool)
DeepSeek Code Review (com.coder.ai.dpt)
CodeGPT AI Assistant (com.my.code.tools)
DeepSeek AI Assist (ord.cp.code.ai.kit)
Coding Simple Tool (com.dp.git.ai.tool)
The two most downloaded plugins are DeepSeek AI Assist (27,727 downloads) and CodeGPT AI Assistant (25,571 downloads).
However, the researchers warn that download counts can be manipulated and should not necessarily be treated as unique installations.
While malicious packages are commonly discovered on repositories such as npm and PyPI, reports of credential-stealing plugins distributed through the JetBrains Marketplace are far less common.
BleepingComputer contacted JetBrains about the malicious plugins, but has not received a response as of publication.
Test every layer before attackers do
Security teams log 54% of successful attacks and alert on just 14%. The rest move through your environment unseen.
The Picus whitepaper shows how breach and attack simulation tests your SIEM and EDR rules so threats stop slipping by detection.
Get the whitepaper
Related Articles:
Vibe coders are gonna vibe code: How CISOs are tackling code sprawl
Why AI-driven threats are exposing the limits of MSP security stacks
XBOW tests Anthropic's Mythos Preview for offensive security
Why the browser is now the front line for AI security
How Varonis Atlas integrates Claude Compliance API for AI governance
