---
source: "https://thenewstack.io/agentjacking-sentry-mcp-attack"
title: "A public Sentry key is all it takes to hijack Claude Code, Cursor, and Codex (4 minute read)"
author: "TLDR InfoSec"
date_published: "Tue, 23 Jun 2026 00:00:00 GMT"
date_clipped: "2026-06-23"
category: "Security & Ethical Hacking"
source_type: "rss"
discovered_via: "https://tldr.tech/infosec/2026-06-23"
source_role: "primary-via-tldr"
---

# A public Sentry key is all it takes to hijack Claude Code, Cursor, and Codex (4 minute read)

Source: https://thenewstack.io/agentjacking-sentry-mcp-attack

A public Sentry key is all it takes to hijack Claude Code, Cursor, and Codex - The New Stack 
TNS
OK
SUBSCRIBE
Join our community of software engineering leaders and aspirational developers. Always 
stay in-the-know by getting the most important news and exclusive content delivered 
fresh to your inbox to learn more about at-scale software development.
EMAIL ADDRESS 
REQUIRED
SUBSCRIBE 
RESUBSCRIPTION REQUIRED 
It seems that you've previously unsubscribed from our newsletter
in the past. Click the button below to open the re-subscribe form 
in a new tab. When you're done, simply close that tab and continue 
with this form to complete your subscription.
RE-SUBSCRIBE 
The New Stack does not sell your information or share it with 
unaffiliated third parties. By continuing, you agree to our 
Terms of Use and
Privacy Policy .
Welcome and thank you for joining The New Stack community!
Please answer a few simple questions to help us deliver the news and resources you are interested in.
FIRST NAME 
REQUIRED
LAST NAME 
REQUIRED
COMPANY NAME 
REQUIRED
COUNTRY 
REQUIRED
Select ... 
United States 
Canada 
India 
United Kingdom 
Germany 
France 
--- 
Afghanistan 
Albania 
Algeria 
American Samoa 
Andorra 
Angola 
Anguilla 
Antarctica 
Antigua and Barbuda 
Argentina 
Armenia 
Aruba 
Asia/Pacific Region 
Australia 
Austria 
Azerbaijan 
Bahamas 
Bahrain 
Bangladesh 
Barbados 
Belarus 
Belgium 
Belize 
Benin 
Bermuda 
Bhutan 
Bolivia 
Bonaire, Sint Eustatius and Saba 
Bosnia and Herzegovina 
Botswana 
Bouvet Island 
Brazil 
British Indian Ocean Territory 
Brunei Darussalam 
Bulgaria 
Burkina Faso 
Burundi 
Cambodia 
Cameroon 
Canada 
Cape Verde 
Cayman Islands 
Central African Republic 
Chad 
Chile 
China 
Christmas Island 
Cocos (Keeling) Islands 
Colombia 
Comoros 
Congo 
Congo, The Democratic Republic of the 
Cook Islands 
Costa Rica 
Croatia 
Cuba 
Curaçao 
Cyprus 
Czech Republic 
Côte d'Ivoire 
Denmark 
Djibouti 
Dominica 
Dominican Republic 
Ecuador 
Egypt 
El Salvador 
Equatorial Guinea 
Eritrea 
Estonia 
Ethiopia 
Falkland Islands (Malvinas) 
Faroe Islands 
Fiji 
Finland 
France 
French Guiana 
French Polynesia 
French Southern Territories 
Gabon 
Gambia 
Georgia 
Germany 
Ghana 
Gibraltar 
Greece 
Greenland 
Grenada 
Guadeloupe 
Guam 
Guatemala 
Guernsey 
Guinea 
Guinea-Bissau 
Guyana 
Haiti 
Heard Island and Mcdonald Islands 
Holy See (Vatican City State) 
Honduras 
Hong Kong 
Hungary 
Iceland 
India 
Indonesia 
Iran, Islamic Republic Of 
Iraq 
Ireland 
Isle of Man 
Israel 
Italy 
Jamaica 
Japan 
Jersey 
Jordan 
Kazakhstan 
Kenya 
Kiribati 
Korea, Republic of 
Kuwait 
Kyrgyzstan 
Laos 
Latvia 
Lebanon 
Lesotho 
Liberia 
Libyan Arab Jamahiriya 
Liechtenstein 
Lithuania 
Luxembourg 
Macao 
Madagascar 
Malawi 
Malaysia 
Maldives 
Mali 
Malta 
Marshall Islands 
Martinique 
Mauritania 
Mauritius 
Mayotte 
Mexico 
Micronesia, Federated States of 
Moldova, Republic of 
Monaco 
Mongolia 
Montenegro 
Montserrat 
Morocco 
Mozambique 
Myanmar 
Namibia 
Nauru 
Nepal 
Netherlands 
Netherlands Antilles 
New Caledonia 
New Zealand 
Nicaragua 
Niger 
Nigeria 
Niue 
Norfolk Island 
North Korea 
North Macedonia 
Northern Mariana Islands 
Norway 
Oman 
Pakistan 
Palau 
Palestinian Territory, Occupied 
Panama 
Papua New Guinea 
Paraguay 
Peru 
Philippines 
Pitcairn Islands 
Poland 
Portugal 
Puerto Rico 
Qatar 
Reunion 
Romania 
Russian Federation 
Rwanda 
Saint Barthélemy 
Saint Helena 
Saint Kitts and Nevis 
Saint Lucia 
Saint Martin 
Saint Martin 
Saint Pierre and Miquelon 
Saint Vincent and the Grenadines 
Samoa 
San Marino 
Sao Tome and Principe 
Saudi Arabia 
Senegal 
Serbia 
Serbia and Montenegro 
Seychelles 
Sierra Leone 
Singapore 
Sint Maarten 
Slovakia 
Slovenia 
Solomon Islands 
Somalia 
South Africa 
South Georgia and the South Sandwich Islands 
South Sudan 
Spain 
Sri Lanka 
Sudan 
Suriname 
Svalbard and Jan Mayen 
Swaziland 
Sweden 
Switzerland 
Syrian Arab Republic 
Taiwan 
Tajikistan 
Tanzania, United Republic of 
Thailand 
Timor-Leste 
Togo 
Tokelau 
Tonga 
Trinidad and Tobago 
Tunisia 
Turkey 
Turkmenistan 
Turks and Caicos Islands 
Tuvalu 
Uganda 
Ukraine 
United Arab Emirates 
United Kingdom 
United States 
United States Minor Outlying Islands 
Uruguay 
Uzbekistan 
Vanuatu 
Venezuela 
Vietnam 
Virgin Islands, British 
Virgin Islands, U.S. 
Wallis and Futuna 
Western Sahara 
Yemen 
Zambia 
Zimbabwe 
Åland Islands 
ZIPCODE 
REQUIRED
Great to meet you!
Tell us a bit about your job so we can cover the topics you find most relevant.
What is your job level? 
REQUIRED
-->
Select ... 
C-Level 
VP/Director 
Manager/Supervisor 
Mid Level or Senior Non-Managerial Staff 
Entry Level/Junior Staff 
Freelancer/Contractor 
Student/Intern 
Other ... 
Which of these most closely describes your job role? 
REQUIRED
Select ... 
Developer/Software Engineer 
SysAdmin/Operations/SRE 
Architect 
Security Professional 
DevOps Engineer/Team 
Community Manager/Developer Advocate 
IT management, including CIO/CISO/CTO 
Business Development/Marketing/Sales 
Enthusiast/Hobbyist 
Other ... 
How many employees are in the organization you work with? 
REQUIRED
Select ... 
Self-employed 
2-10 
11-50 
51-250 
251-1,000 
1,001-10,000 
> 10,000 
I am not working 
What option best describes the type of organization you work for? 
REQUIRED
Select ... 
“End user” organization that primarily uses IT products and services to support their business deliverables 
Hardware / software vendor or supplier 
Cloud service provider or managed service provider 
System integrator or IT consulting firm 
Other ... 
Which of the following best describes your organization's primary industry? 
REQUIRED
Select ... 
Advertising/Marketing 
Aerospace/Aviation 
Agriculture 
Automotive 
Biotech/Pharmaceutical 
Business Services (accounting, consulting, etc.) 
Computers/Information Technology 
Construction 
Education 
Facilities/Service Industry 
Finance/Financial Services (banking, insurance, etc.) 
Government 
Healthcare 
Human Resources 
Legal 
Life sciences (biotech, pharmaceuticals, etc.) 
Manufacturing 
Media 
Non-profit 
Real Estate 
Retail/Consumer Goods 
Telecommunications 
Transportation/Logistics 
Travel/Hospitality/Entertainment 
Utility/Energy 
Other ... 
LINKEDIN PROFILE URL 
Welcome!
We’re so glad you’re here. You can expect all the best TNS content to arrive 
Monday through Friday to keep you on top of the news and at the top of your game.
What’s next?
Check your inbox for a confirmation email where you can adjust your preferences 
and even join additional groups.
Follow TNS on your favorite social media networks.
-->
Become a TNS follower on LinkedIn .
Check out the latest featured and trending stories while you wait for your 
first TNS newsletter.
PREV 
1 of 2 
NEXT 
VOXPOP
As a JavaScript developer, what non-React tools do you use most often? 
✓ 
Angular 
0% 
✓ 
Astro 
0% 
✓ 
Svelte 
0% 
✓ 
Vue.js 
0% 
✓ 
Other 
0% 
✓ 
I only use React 
0% 
✓ 
I don't use JavaScript 
0% 
Thanks for your opinion! Subscribe below to get the final results, published 
exclusively in our TNS Update newsletter:
SUBMIT 
NEW! Try Stackie AI
ARCHITECTURE
Cloud Native Ecosystem 
Containers 
Databases 
Edge Computing 
Infrastructure as Code 
Linux 
Microservices 
Open Source 
Networking 
Storage 
ENGINEERING
AI 
AI Engineering 
API Management 
Backend development 
Data 
Frontend Development 
Large Language Models 
Security 
Software Development 
WebAssembly 
OPERATIONS
AI Operations 
CI/CD 
Cloud Services 
DevOps 
Kubernetes 
Observability 
Operations 
Platform Engineering 
PROGRAMMING
C++ 
Developer tools 
Go 
Java 
JavaScript 
Programming Languages 
Python 
Rust 
TypeScript 
CHANNELS
Podcasts 
Ebooks 
Events 
Webinars 
Newsletter 
TNS RSS Feeds 
THE NEW STACK
About / Contact 
Sponsors 
Advertise With Us 
Contributions 
PODCASTS 
EBOOKS 
EVENTS 
WEBINARS 
NEWSLETTER 
CONTRIBUTE 
ARCHITECTURE
ENGINEERING
OPERATIONS
PROGRAMMING
Cloud Native Ecosystem 
Containers 
Databases 
Edge Computing 
Infrastructure as Code 
Linux 
Microservices 
Open Source 
Networking 
Storage 
Agentic development hinges on verification. For cloud-native software, that is a runtime problem.
Jun 11th 2026 10:00am, by 
Arjun Iyer 
Vendor neutrality isn’t magic: A hard look at the OpenTelemetry ecosystem
May 29th 2026 10:00am, by 
Adriana Villela and Josh Lee 
How Jaeger hit 8.6× compression on 10 million spans with ClickHouse
May 24th 2026 11:00am, by 
Mahad Zaryab 
After becoming cloud computing’s telemetry standard, OpenTelemetry graduates into the AI infrastructure era
May 21st 2026 10:00am, by 
Paul Sawers 
Why agent harnesses fail inside cloud-native systems
May 13th 2026 9:00am, by 
Arjun Iyer 
AWS can now mathematically prove your VMs are isolated
Jun 10th 2026 12:46pm, by 
Frederic Lardinois 
Microsoft wants to make service mesh invisible
Apr 8th 2026 1:11pm, by 
Frederic Lardinois 
Edera spent years calling KVM less secure. Here's why it changed its mind.
Mar 25th 2026 2:22pm, by 
Steven J. Vaughan-Nichols 
Minimus aims to solve one of open-source's long-festering problems
Mar 24th 2026 3:00am, by 
Adrian Bridgwater 
How to deploy Pi-Hole with Docker and stop ads on every device on your LAN
Mar 23rd 2026 7:44am, by 
Jack Wallen 
Neoclouds, sovereign AI and Postgres: The new operating model for regulated enterprises
Jun 18th 2026 11:00am, by 
Max Romanenko 
The database storage problem is solved. Here’s what comes next.
Jun 18th 2026 10:00am, by 
Craig Kerstiens 
Why AI retrieval and ranking need more than vector search
Jun 13th 2026 2:00pm, by 
Bonnie Chase 
When your data model is the bottleneck: lessons from Medium’s feature store
Jun 9th 2026 10:40am, by 
Cynthia Dunlop 
For years, Apache Cassandra handed this work to your team — 6.0 takes it back
Jun 8th 2026 10:00am, by 
Anil Inamdar 
Google Gemma 4 12B nearly matches 26B benchmarks — and runs on your laptop
Jun 4th 2026 3:30pm, by 
Meredith Shubel 
How to get operational data off the factory floor without creating an IT breach
Jun 3rd 2026 3:55pm, by 
Alex Wilhelm 
Edge-forward: Akamai eyes sweet spot between centralized & decentralized AI inference
Apr 1st 2026 7:00am, by 
Adrian Bridgwater 
Developers are coding to a moving target, and nobody knows where AI lands next
Mar 3rd 2026 7:33am, by 
Adrian Bridgwater 
Cloudflare’s new Markdown support shows how the web is evolving for AI agents
Mar 2nd 2026 4:30am, by 
David Eastman 
Why Terraform is green when your cloud is broken
Apr 28th 2026 9:00am, by 
Joe Karlsson 
The one Slack message that proved our elite engineering team was flying blind
Apr 26th 2026 11:00am, by 
Joe Karlsson 
The operational gap is real, and it's getting wider
Mar 26th 2026 8:00am, by 
Yevgeny Pats 
Why "automated" infrastructure might cost more than you think
Feb 24th 2026 4:00am, by 
Justyn Roberts 
Why 40% of AI projects will be canceled by 2027 (and how to stay in the other 60%)
Feb 13th 2026 6:00am, by 
Alex Drag 
Why Linux creator Linus Torvalds gets angry hearing "99% of code is AI"
May 29th 2026 10:34am, by 
B. Cameron Gain 
Sparky Linux 9 brings a rolling release to Debian
Mar 30th 2026 8:00am, by 
Jack Wallen 
Edera spent years calling KVM less secure. Here's why it changed its mind.
Mar 25th 2026 2:22pm, by 
Steven J. Vaughan-Nichols 
Your Kubernetes isn't ready for AI workloads, and drift is the reason
Mar 25th 2026 8:43am, by 
TNS Staff 
Linux kernel scale is swamping an already-flawed CVE system
Mar 20th 2026 4:30am, by 
Jed Salazar 
Tetrate launches open source marketplace to simplify Envoy adoption
Mar 11th 2026 10:52am, by 
Adrian Bridgwater 
OpenTelemetry roadmap: Sampling rates and collector improvements ahead
Feb 24th 2026 11:00am, by 
B. Cameron Gain 
Merging To Test Is Killing Your Microservices Velocity
Dec 16th 2025 7:00am, by 
Arjun Iyer 
IBM’s Confluent Acquisition Is About Event-Driven AI
Dec 11th 2025 6:00am, by 
Joab Jackson 
Deploy Agentic AI Workflows With Kubernetes and Terraform
Nov 26th 2025 9:00am, by 
Oladimeji Sowole 
"An agent is an LLM and a harness": What Nvidia really thinks about OpenClaw
Jun 21st 2026 11:00am, by 
David Eastman 
Backporting bug fixes is dead, Project Valkey now sends in the bots
Jun 20th 2026 10:21am, by 
Adrian Bridgwater 
Fable 5 ban: 4 open models responded before Anthropic could restore access
Jun 18th 2026 9:34am, by 
Janakiram MSV 
Microsoft pulled 73 GitHub repos after malware attack — but still won’t say who’s compromised
Jun 10th 2026 12:40pm, by 
Meredith Shubel 
Databricks wants to kill the "email me a file" problem for AI agent skills
Jun 10th 2026 10:00am, by 
Frederic Lardinois 
From system of record to system of control: How NetBox Labs is making network engineers “masters of intent.”
Apr 28th 2026 11:00am, by 
Doug Sillars 
Beyond the VPN: Cloudflare Mesh builds a private network for the age of AI agents
Apr 14th 2026 11:04am, by 
Adrian Bridgwater 
Model Flop Utilization is the metric Aria Networks says will define the AI infrastructure era
Apr 7th 2026 9:00am, by 
Adrian Bridgwater 
How to deploy Pi-Hole with Docker and stop ads on every device on your LAN
Mar 23rd 2026 7:44am, by 
Jack Wallen 
Why flat Kubernetes networks fail at scale
Mar 20th 2026 7:00am, by 
Reza Ramezanpour 
Why Postgres wants NVMe on the hot path, and S3 everywhere else
Apr 17th 2026 9:00am, by 
Alasdair Brown 
Scaling Btrfs to petabytes in production: a 74% cost reduction story
Mar 18th 2026 5:00am, by 
Motiejus Jakštys 
What is KubeVirt and why it’s growing
Mar 17th 2026 9:00am, by 
Tiago Castro 
S3 is the new network: Rethinking data architecture for the cloud era
Feb 2nd 2026 4:00am, by 
Max Liu 
Agoda’s secret to 50x scale: Getting the database basics right
Jan 28th 2026 7:00am, by 
Cynthia Dunlop 
AI 
AI Engineering 
API Management 
Backend development 
Data 
Frontend Development 
Large Language Models 
Security 
Software Development 
WebAssembly 
Backporting bug fixes is dead, Project Valkey now sends in the bots 
Jun 20th 2026 10:21am, by 
Adrian Bridgwater 
Checkmarx's new SAST engine isn't about the LLM. It's about what happens after. 
Jun 19th 2026 12:00pm, by 
Darryl K. Taft 
Anthropic overhauled Claude Design to fix the handoff. A designer and an engineer disagree on whether it worked. 
Jun 19th 2026 9:35am, by 
Meredith Shubel 
MCP gets its missing enterprise authorization layer 
Jun 18th 2026 2:21pm, by 
Frederic Lardinois 
Cursor, GitLab and Zed agree GitHub is breaking. They disagree on how to rebuild it. 
Jun 18th 2026 1:32pm, by 
Paul Sawers 
Gemini CLI vs. Antigravity: What works, not the spec sheet 
Jun 20th 2026 12:00pm, by 
Jessica Wachtel 
"Time to clean up human slop": Why AI now reviews code better than your teammate. 
Jun 19th 2026 1:30pm, by 
Adrian Bridgwater 
Cursor, GitLab and Zed agree GitHub is breaking. They disagree on how to rebuild it. 
Jun 18th 2026 1:32pm, by 
Paul Sawers 
Your AI pipeline is broken, and your dashboards don't know it 
Jun 18th 2026 9:00am, by 
Emmanuel Akita 
Cohere sold sovereign AI to enterprises, now it's targeting developers with its first coding model 
Jun 15th 2026 10:54am, by 
Paul Sawers 
Anthropic's $300M Stainless deal lands hardest on OpenAI and Google 
May 23rd 2026 10:00am, by 
Janakiram MSV 
The API portal is the clearest signal of whether your company can handle AI agents 
May 12th 2026 1:23pm, by 
Charles Humble 
AI teams are spending months on web scrapers that SerpApi replaces with one API call 
May 12th 2026 10:00am, by 
Carly Page 
Why JSON Schema matters more than ever in the age of generative AI 
Apr 28th 2026 1:00pm, by 
Charles Humble 
SmartBear's Swagger update targets the API drift problem AI coding tools created 
Apr 19th 2026 10:00am, by 
Darryl K. Taft 
Why PHP performance keeps getting bumped from the roadmap 
May 6th 2026 10:00am, by 
Matthew Weier O’Phinney 
Why Postgres wants NVMe on the hot path, and S3 everywhere else 
Apr 17th 2026 9:00am, by 
Alasdair Brown 
Expo bets big on React Native’s agentic future 
Apr 16th 2026 11:37am, by 
Paul Sawers 
From clobbered drafts to real-time sync 
Apr 14th 2026 10:00am, by 
David Moore 
Moving beyond the “magic scaling sauce” myth 
Apr 2nd 2026 9:30am, by 
TNS Staff 
The database storage problem is solved. Here’s what comes next. 
Jun 18th 2026 10:00am, by 
Craig Kerstiens 
“A data lake of nuance for AI agents to swim in”: AWS Context gets shipshape on reasoning  
Jun 17th 2026 2:00pm, by 
Adrian Bridgwater 
Your AI isn't broken. Your data is. 
Jun 17th 2026 9:00am, by 
Darryl K. Taft 
The siloed-data era is over. Here's what comes next for AI agents. 
Jun 16th 2026 10:00am, by 
TNS Staff 
"The manual model breaks": What happens when agents write to production data 
Jun 11th 2026 1:35pm, by 
Adrian Bridgwater 
Anthropic overhauled Claude Design to fix the handoff. A designer and an engineer disagree on whether it worked. 
Jun 19th 2026 9:35am, by 
Meredith Shubel 
Google wants to make the web agent-ready 
May 19th 2026 1:45pm, by 
Frederic Lardinois 
Expo bets big on React Native’s agentic future 
Apr 16th 2026 11:37am, by 
Paul Sawers 
Digital Experience Monitoring belongs in the modern developer workflow 
Apr 3rd 2026 10:00am, by 
Kayla Bondy 
WebMCP turns any Chrome web page into an MCP server for AI agents 
Mar 17th 2026 11:50am, by 
David Eastman 
Checkmarx's new SAST engine isn't about the LLM. It's about what happens after. 
Jun 19th 2026 12:00pm, by 
Darryl K. Taft 
Your AI pipeline is broken, and your dashboards don't know it 
Jun 18th 2026 9:00am, by 
Emmanuel Akita 
We’ve been measuring AI wrong; why economically valuable work is the new benchmark 
Jun 15th 2026 9:42am, by 
Adrian Bridgwater 
Fable 5 vs Opus 4.8: The real stakes, not the spec sheet 
Jun 13th 2026 11:00am, by 
Jessica Wachtel 
Cleaner AI training data, fewer bugs: Sonar's SonarSweep explained 
Jun 11th 2026 8:00am, by 
Joe Tyler 
A public Sentry key is all it takes to hijack Claude Code, Cursor, and Codex 
Jun 21st 2026 1:00pm, by 
Janakiram MSV 
Checkmarx's new SAST engine isn't about the LLM. It's about what happens after. 
Jun 19th 2026 12:00pm, by 
Darryl K. Taft 
MCP gets its missing enterprise authorization layer 
Jun 18th 2026 2:21pm, by 
Frederic Lardinois 
Chainguard Agent Skills matures 
Jun 17th 2026 12:00pm, by 
Steven J. Vaughan-Nichols 
“Agents need boring infrastructure around them”: Why we need to take an interest in 'invisible' AI 
Jun 17th 2026 9:44am, by 
Adrian Bridgwater 
Losing Fable made the best case yet for AI models you can run yourself 
Jun 20th 2026 6:30am, by 
Matthew Burns 
"Time to clean up human slop": Why AI now reviews code better than your teammate. 
Jun 19th 2026 1:30pm, by 
Adrian Bridgwater 
"I think this is costing us more than we realize": what permissionless ownership really asks of you 
Jun 19th 2026 10:30am, by 
Nicolás Vázquez 
Gusto Cofounder: An AI agent that runs payroll, HR, and benefits without waiting to be asked 
Jun 18th 2026 4:40pm, by 
Adrian Bridgwater 
Kiro goes mobile: AWS brings agentic coding supervision to the iPhone 
Jun 17th 2026 1:00pm, by 
Darryl K. Taft 
Edge-forward: Akamai eyes sweet spot between centralized & decentralized AI inference 
Apr 1st 2026 7:00am, by 
Adrian Bridgwater 
WebAssembly is now outperforming containers at the edge 
Mar 29th 2026 9:00am, by 
B. Cameron Gain 
WebAssembly could solve AI agents' most dangerous security gap 
Mar 24th 2026 9:01am, by 
B. Cameron Gain 
How WebAssembly plugins simplify Kubernetes extensibility 
Mar 3rd 2026 2:00pm, by 
B. Cameron Gain 
WebAssembly is everywhere. Here's how it works 
Feb 25th 2026 11:00am, by 
Jessica Wachtel 
AI Operations 
CI/CD 
Cloud Services 
DevOps 
Kubernetes 
Observability 
Operations 
Platform Engineering 
PagerDuty's CAIO says most AI incident tools are missing a critical layer 
Jun 14th 2026 11:00am, by 
João Freitas 
Observability overload is drowning engineers 
Jun 10th 2026 1:27pm, by 
Alex Wilhelm 
The tokenmaxxing party is over, and Revenium is mopping up 
Jun 9th 2026 6:00am, by 
Chris J. Preimesberger 
Why Anthropic just doubled Claude Cowork limits at no charge 
Jun 8th 2026 1:35pm, by 
Adrian Bridgwater 
From Jupyter Notebook to production: How to ship AI systems that actually work 
Jun 6th 2026 7:00am, by 
Zziwa Raymond Ian 
AI teams now deploy 1,000 times a month. Your pipeline wasn't built for that. 
Jun 7th 2026 12:30pm, by 
Paul Stovell 
GitLab 19.0 trades its string section for a full DevSecOps orchestra 
May 25th 2026 12:00pm, by 
Adrian Bridgwater 
CI wasn't built for coding agents. Here's what comes next. 
May 21st 2026 10:30am, by 
Anirudh Ramanathan 
As agentic dev tools boom, workflow auditability becomes the constraint 
May 12th 2026 8:00am, by 
Brian Wald 
The agent code explosion is here. We need to rethink our pipelines, fast. 
May 4th 2026 10:00am, by 
Arjun Iyer 
AI agents need infrastructure: Why Europe’s regional cloud strategy matters 
Jun 11th 2026 10:00am, by 
Kevin Cochrane 
Why CPUs still matter in the age of AI agents 
Jun 3rd 2026 2:54pm, by 
Frederic Lardinois 
Why AWS scrapped OpenSearch's architecture to chase agent workloads 
May 28th 2026 2:30pm, by 
Frederic Lardinois 
AI agents need to spend money — Stripe and iWallet are building the rails 
May 5th 2026 7:43am, by 
John Biggs 
AWS lands OpenAI on Bedrock, but Trainium is the real story 
Apr 29th 2026 10:54am, by 
Janakiram MSV 
Backporting bug fixes is dead, Project Valkey now sends in the bots 
Jun 20th 2026 10:21am, by 
Adrian Bridgwater 
"Time to clean up human slop": Why AI now reviews code better than your teammate. 
Jun 19th 2026 1:30pm, by 
Adrian Bridgwater 
AWS puts an AI bouncer at the merge queue 
Jun 17th 2026 11:00am, by 
Darryl K. Taft 
From Jupyter Notebook to production: How to ship AI systems that actually work 
Jun 6th 2026 7:00am, by 
Zziwa Raymond Ian 
The DIY platform trap that's burning out engineering teams 
May 31st 2026 11:00am, by 
Darin Zook 
Loops are replacing prompts. Verification is about to be your biggest problem. 
Jun 13th 2026 12:00pm, by 
Arjun Iyer 
Why the need for humans won't disappear in the age of autonomous databases 
Jun 4th 2026 1:18pm, by 
Chris J. Preimesberger 
How to secure Kubernetes in the age of AI workloads 
Jun 4th 2026 12:45pm, by 
Mary Branscombe 
Cloud native application challenges: installing the walking skeleton 
May 13th 2026 9:00am, by 
Manning Book Authors 
Why Prometheus couldn't see Cilium metrics at 2 a.m. 
May 10th 2026 10:00am, by 
Rishi Mondal 
Your AI pipeline is broken, and your dashboards don't know it 
Jun 18th 2026 9:00am, by 
Emmanuel Akita 
Observability overload is drowning engineers 
Jun 10th 2026 1:27pm, by 
Alex Wilhelm 
The tokenmaxxing party is over, and Revenium is mopping up 
Jun 9th 2026 6:00am, by 
Chris J. Preimesberger 
Vendor neutrality isn’t magic: A hard look at the OpenTelemetry ecosystem 
May 29th 2026 10:00am, by 
Adriana Villela and Josh Lee 
Debugging the undebuggable: building observability into probabilistic AI systems 
May 28th 2026 7:00am, by 
Oladimeji Sowole 
The reason enterprise outages almost never start where ops teams think 
May 26th 2026 9:43am, by 
Jennifer Riggins 
I buried 20 problems in a fake P&L to see if Claude for Small Business could find them 
May 22nd 2026 9:00am, by 
Jessica Wachtel 
OpenAI brings Codex to the ChatGPT mobile app 
May 14th 2026 4:13pm, by 
Frederic Lardinois 
GitLab is betting a 19th-century economic theory will shape its AI era 
May 14th 2026 1:21pm, by 
Paul Sawers 
The new FinOps problem isn't cloud bills 
May 12th 2026 7:24pm, by 
Frederic Lardinois 
Loops are replacing prompts. Verification is about to be your biggest problem. 
Jun 13th 2026 12:00pm, by 
Arjun Iyer 
Git real: AI agents aren't just for solo developers anymore 
Jun 9th 2026 3:58pm, by 
Janakiram MSV 
Netlify CTO Dana Lawson: Writing code is no longer the job 
Jun 6th 2026 10:00am, by 
Jennifer Riggins 
Why agentic AI makes the ops platform the most important layer in the enterprise 
Jun 4th 2026 2:35pm, by 
TNS Staff 
The DIY platform trap that's burning out engineering teams 
May 31st 2026 11:00am, by 
Darin Zook 
C++ 
Developer tools 
Go 
Java 
JavaScript 
Programming Languages 
Python 
Rust 
TypeScript 
Open source USearch library jumpstarts ScyllaDB vector search 
Feb 5th 2026 12:00pm, by 
Jelani Harper 
AWS WAF vs. Google Cloud Armor: A Multicloud Security Showdown 
Nov 25th 2025 10:00am, by 
Advait Patel 
Goodbye Dashboards: Agents Deliver Answers, Not Just Reports 
Nov 23rd 2025 9:00am, by 
Ketan Karkhanis 
Rust vs. C++: a Modern Take on Performance and Safety 
Oct 22nd 2025 2:00pm, by 
Zziwa Raymond Ian 
Building a Real-Time System Monitor in Rust Terminal 
Oct 15th 2025 7:05am, by 
Tinega Onchari 
Your agent wants to search like a 2010 quant 
Jun 21st 2026 12:00pm, by 
Jon Bratseth 
Gemini CLI vs. Antigravity: What works, not the spec sheet 
Jun 20th 2026 12:00pm, by 
Jessica Wachtel 
Anthropic overhauled Claude Design to fix the handoff. A designer and an engineer disagree on whether it worked. 
Jun 19th 2026 9:35am, by 
Meredith Shubel 
Kiro goes mobile: AWS brings agentic coding supervision to the iPhone 
Jun 17th 2026 1:00pm, by 
Darryl K. Taft 
Vercel launches eve, an open-source framework that treats agents as directories 
Jun 17th 2026 12:59pm, by 
Frederic Lardinois 
Go Experts: 'I Don't Want to Maintain AI-Generated Code' 
Sep 28th 2025 6:00am, by 
David Cassel 
How To Run Kubernetes Commands in Go: Steps and Best Practices  
Jun 27th 2025 8:00am, by 
Sunny Yadav 
Prepare Your Mac for Go Development 
Apr 12th 2025 7:00am, by 
Damon M. Garn 
Pagoda: A Web Development Starter Kit for Go Programmers 
Mar 19th 2025 6:10am, by 
Loraine Lawson 
Microsoft TypeScript Devs Explain Why They Chose Go Over Rust, C# 
Mar 18th 2025 7:00am, by 
David Cassel 
Transform your AI coding agent into a deterministic Java Spring expert 
Jun 11th 2026 9:00am, by 
Raquel Pau 
Spring is 23 years old. AI just made it a security emergency. 
Jun 9th 2026 2:48pm, by 
Darryl K. Taft 
In the AI age, Java is more relevant than ever 
Apr 8th 2026 5:30pm, by 
Mary Branscombe 
Java 26 lands without an LTS badge. Here's why developers should care anyway. 
Mar 18th 2026 9:35am, by 
Darryl K. Taft 
62% of enterprises now use Java to power AI apps 
Feb 10th 2026 12:58pm, by 
Darryl K. Taft 
Cloudflare aqui-hires VoidZero: Did a piece of the open web just stabilize, or become more brittle? 
Jun 5th 2026 3:01pm, by 
Adrian Bridgwater 
"Real maturity problems": Not every developer is thrilled with Bun after Anthropic acquisition 
May 5th 2026 1:03pm, by 
Adrian Bridgwater 
TypeScript 6.0 RC arrives as a bridge to a faster future 
Mar 14th 2026 9:00am, by 
Darryl K. Taft 
WebAssembly is everywhere. Here's how it works 
Feb 25th 2026 11:00am, by 
Jessica Wachtel 
Wasm vs. JavaScript: Who wins at a million rows? 
Feb 22nd 2026 6:00am, by 
Jessica Wachtel 
Who will maintain the web when PHP's veterans retire? 
Apr 16th 2026 2:53pm, by 
Darryl K. Taft 
Will AI force code to evolve or make it extinct? 
Mar 22nd 2026 6:00am, by 
David Cassel 
Java 26 lands without an LTS badge. Here's why developers should care anyway. 
Mar 18th 2026 9:35am, by 
Darryl K. Taft 
TypeScript 6.0 RC arrives as a bridge to a faster future 
Mar 14th 2026 9:00am, by 
Darryl K. Taft 
Nearly half of all companies now use Rust in production, survey finds 
Mar 6th 2026 10:45am, by 
Darryl K. Taft 
How to build an AI-powered private document search app with RAG, ChromaDB, and memory 
Apr 10th 2026 12:00pm, by 
Teri Eyenike 
In the AI age, Java is more relevant than ever 
Apr 8th 2026 5:30pm, by 
Mary Branscombe 
OpenAI acquires Astral to bring open source Python developer tools to Codex — but details are still fuzzy 
Mar 20th 2026 7:33am, by 
Meredith Shubel 
Python virtual environments: isolation without the chaos 
Feb 16th 2026 7:00am, by 
Jessica Wachtel 
Statistical language R is making a comeback against Python 
Feb 12th 2026 2:57pm, by 
Darryl K. Taft 
The Rust sidecar pattern that fixes Python AI's biggest weakness 
May 14th 2026 9:00am, by 
Boris Chabeda 
Nearly half of all companies now use Rust in production, survey finds 
Mar 6th 2026 10:45am, by 
Darryl K. Taft 
Wasm vs. JavaScript: Who wins at a million rows? 
Feb 22nd 2026 6:00am, by 
Jessica Wachtel 
Open source USearch library jumpstarts ScyllaDB vector search 
Feb 5th 2026 12:00pm, by 
Jelani Harper 
The 'weird' things that happened when Clickhouse replaced C++ with Rust 
Feb 4th 2026 7:26am, by 
B. Cameron Gain 
From clobbered drafts to real-time sync 
Apr 14th 2026 10:00am, by 
David Moore 
TypeScript 6.0 RC arrives as a bridge to a faster future 
Mar 14th 2026 9:00am, by 
Darryl K. Taft 
Mastra empowers web devs to build AI agents in TypeScript 
Jan 28th 2026 11:00am, by 
Loraine Lawson 
Inferno Vet Creates Frontend Framework Built With AI in Mind 
Dec 10th 2025 11:00am, by 
Loraine Lawson 
JavaScript Utility Library Lodash Changing Governance Model 
Nov 1st 2025 7:00am, by 
Loraine Lawson 
2026-06-21 13:00:00 
A public Sentry key is all it takes to hijack Claude Code, Cursor, and Codex 
AI Agents 
/ 
Model Context Protocol (MCP) 
/ 
Security 
A public Sentry key is all it takes to hijack Claude Code, Cursor, and Codex 
A security firm says a single fake Sentry error can hijack AI coding agents through MCP and run attacker code on a developer's own machine. 
Jun 21st, 2026 1:00pm by 
Janakiram MSV 
On June 17, the Threat Labs team at Tenet Security, an AI-agent security startup newly out of stealth, documented an attack it calls agentjacking . 
The whole attack rides on a routine request to fix unresolved errors in Sentry , the error-monitoring service thousands of teams wire into their applications. And a single fake error report can turn an AI coding agent into a code-execution engine on a developer’s own machine. No malware changes hands, and no password is stolen.
And a single fake error report can turn an AI coding agent into a code-execution engine on a developer’s own machine. No malware changes hands, and no password is stolen.
Think of the attack as a forged repair note slipped into a building’s work-order system. The contractor on call trusts the system, reads the note as an instruction, and never asks who filed it. The Model Context Protocol connects coding agents to outside services the same way. The agent treats whatever those services return as guidance worth acting on.
Why the agent cannot tell data from an instruction 
To understand why this works, we need to look at what a Sentry DSN was designed to do. A DSN, or Data Source Name, is a write-only credential. Sentry documents it as safe to embed in frontend JavaScript, so an application can report errors without exposing the rest of the project. By design, it is public, and the ingest endpoint asks for nothing more than the DSN itself.
That arrangement was safe while humans read the error reports. An AI agent reading the same reports turns the design decision into an opening for attackers. Anyone who finds a DSN can post a crafted event that Sentry processes like a genuine crash. The DSN turns up by inspecting a site’s JavaScript, running a Censys query, or searching GitHub code.
That arrangement was safe while humans read the error reports. An AI agent reading the same reports turns the design decision into an opening for attackers. 
The agent cannot tell the data it reads from an instruction to act. A command planted where an agent will read it, even somewhere no human would look, such as an error log, may simply run. This is a limit of the models themselves, not something a config change can fix.
The public DSN and the agent’s trust in MCP output are a lethal combination, because each is harmless alone and dangerous together. The credential lets an attacker write into the data an agent reads, and the agent supplies the privileges to act on it.
How the attack unfolds 
Here is how the chain unfolds: Every step is ordinary on its own, and nothing in it looks like an exploit.
1. Find the DSN 
The attacker starts by finding a target’s DSN. Sentry documents it as safe to expose, so it sits in the JavaScript of countless production sites. It surfaces through a Censys query or a GitHub code search.
2. Post a crafted event 
With the DSN, the attacker sends one error event to Sentry’s ingest endpoint. No authentication beyond the DSN is required. The attacker controls the whole payload, from the message and tags to the context keys and stack trace. Sentry returns HTTP 200 and files the event alongside real crashes.
3. Disguise the command as a resolution 
The crafted event carries markdown in its message and context fields. When the Sentry MCP server hands the event to an agent, the markdown renders as headings, code blocks, and a fabricated resolution section. The section matches Sentry’s own template, and inside it sits an npx command the attacker wants run.
4. Steer the agent 
A developer asks the agent to fix unresolved Sentry issues. Thousands of teams make that request every day. The agent pulls the injected event through MCP and reads the fake resolution as trusted guidance. From there it is steered toward the suggested command rather than the source code.
5. Run the command 
The agent runs the command with the developer’s own privileges on the developer’s own machine. In Tenet’s tests, the package came from the public npm registry and self-identified as a security scan, which kept the demonstration inside responsible-disclosure limits.
6. Reach the secrets 
Once running, the package confirmed it could read environment variables, cloud configuration files, and credential stores, then signaled a Tenet-controlled server that the exposure was real. AWS keys, GitHub tokens, and git credentials were all within reach from that single foothold.
What Tenet proved at scale 
Imagine a developer clearing a backlog of Sentry issues in one pass on a Friday afternoon, the routine that every step of this attack depends on. Tenet built its validation around exactly that moment and then measured how far it reached.
Tenet reported 2,388 organizations with injectable DSNs found through passive reconnaissance, of which 71 rank in the Tranco top-1M list of busiest sites . The same conditions exist in thousands of other projects that were never tested.
Claude Code, Cursor, and Codex all acted on the injected errors, and the team logged more than 100 confirmed executions across separate organizations.
Ron Bobrov , a Tenet researcher, reported an 85% success rate across the controlled validation waves. Claude Code, Cursor, and Codex all acted on the injected errors, and the team logged more than 100 confirmed executions across separate organizations. Tenet sells the agent-runtime defense it concludes is necessary. The figures are best read as their own controlled test results rather than independent measurements.
Tenet confirmed execution on a machine belonging to a developer inside a $250 billion Fortune 100 technology company, one of the largest on earth. The same campaign reached agents running in sandboxed CI pipelines, inside WSL on managed Windows machines, and behind corporate VPNs, on macOS and Windows alike.
One captured environment running Claude Code held a live AWS secret access key. It also held identifiers for other connected agents, so a single foothold opened far more than one machine. According to Tenet, the build was current, captured in early June 2026 rather than from a stale lab setup.
Inside an enterprise, the danger is everything the agent can already reach. A single injected error exposed CI/CD credentials, private repository URLs, and cloud infrastructure tokens to an attacker. Those are the same credentials a platform team spends its days protecting.
Why no security control sees it 
What makes agentjacking hard to stop is that every step in it is authorized. The attacker never touches the victim’s infrastructure, the developer never approves any code, and the agent does exactly what it was asked to do. Tenet calls this the Authorized Intent Chain, and it is why EDR, WAF, IAM, VPNs, and firewalls register nothing worth flagging.
What makes agentjacking hard to stop is that every step in it is authorized… EDR, WAF, IAM, VPNs, and firewalls register nothing worth flagging.
Prompt-layer defenses did not help the agents either. The researchers said the agents ran the payload even when system prompts and skills told them to ignore untrusted data. That points to a limit in how current models handle tool output, not a setting a team can switch off.
Sentry, the model vendors, and the runtime 
Once the attack works, someone still has to stop it, and that is harder than it sounds. Three layers sit between the injected error and the damage. Two are the platform that emits the data and the model vendors whose agents act on it. The third is the runtime around the agent, where each action is decided.
Defense layer Effect on agentjacking Reason Sentry platform Limited A content filter blocks a known payload string, yet the ingest endpoint stays open by design Model vendors Partial at best Agents ran the payload despite system-prompt and skill instructions to ignore untrusted data Agent runtime Most direct The runtime sees each action before it executes and can gate commands sourced from external data Network and endpoint controls None EDR, WAF, IAM, and VPNs see only authorized actions, so nothing trips an alert 
Sentry’s response to the disclosure is what keeps this attack open. Tenet disclosed the issue on June 3, and Sentry acknowledged it the same day. Sentry declined to fix it at the source.
The company called the attack class “technically not defensible” and pointed to middleware that model vendors run instead. It did ship a global content filter for the specific string in Tenet’s proof of concept, which stops that one payload without closing the path.
Who owns the fix 
That puts the runtime in the spotlight, the layer around the agent where every action is decided. Sentry treats its open endpoint as a feature, and the model will not reliably refuse the instruction. So the fix cannot come from either of them alone. 
The fight now is over who owns that fix, and how it settles will matter to teams more than the proof of concept did.
Beyond Sentry 
In summary, the weakness Tenet demonstrated does not belong solely to Sentry. Any MCP integration that returns externally influenced data to an agent carries the same exposure. As more tools connect through MCP, the surface attackers can reach through trusted telemetry will widen. The prompt injection that security teams have warned about for a year now has a clear path from a publicly available credential to code execution.
If teams keep wiring agents to external services without a control that inspects what those services return, injected data will keep finding a route to execution. Tenet has open-sourced a set of drop-in configurations called agent-jackstop that harden Cursor and Claude Code against this class of injection. They give teams a concrete starting point while the larger question is argued out.
An agent that clears a Sentry backlog in seconds will also run whatever a trusted tool hands it. That makes the runtime around the agent the next real boundary in software supply chain security. Enterprises already vet third-party libraries before trusting them. Treating every MCP integration the same way is what keeps agentjacking from turning a team’s own telemetry against it.
TRENDING STORIES 
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube 
channel to stream all our podcasts, interviews, demos, and more.
SUBSCRIBE
Group 
Created with Sketch. 
Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent... 
Read more from Janakiram MSV 
SHARE THIS STORY 
-->
TRENDING STORIES 
SHARE THIS STORY 
-->
TRENDING STORIES 
TNS DAILY NEWSLETTER 
Receive a free roundup of the most recent TNS articles in your inbox each day. 
SUBSCRIBE
The New Stack does not sell your information or share it with 
unaffiliated third parties. By continuing, you agree to our 
Terms of Use and
Privacy Policy .
ARCHITECTURE
Cloud Native Ecosystem 
Containers 
Databases 
Edge Computing 
Infrastructure as Code 
Linux 
Microservices 
Open Source 
Networking 
Storage 
ENGINEERING
AI 
AI Engineering 
API Management 
Backend development 
Data 
Frontend Development 
Large Language Models 
Security 
Software Development 
WebAssembly 
OPERATIONS
AI Operations 
CI/CD 
Cloud Services 
DevOps 
Kubernetes 
Observability 
Operations 
Platform Engineering 
CHANNELS
Podcasts 
Ebooks 
Events 
Webinars 
Newsletter 
TNS RSS Feeds 
THE NEW STACK
About / Contact 
Sponsors 
Advertise With Us 
Contributions 
roadmap.sh 
Community created roadmaps, articles, resources and journeys for 
developers to help you choose your path and grow in your career.
Frontend Developer Roadmap
Backend Developer Roadmap
Devops Roadmap
© The New Stack 2026 
Disclosures 
Terms of Use 
Advertising Terms & Conditions 
Privacy Policy 
Cookie Policy 
FOLLOW TNS
-->
