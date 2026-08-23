---
source: "https://www.githubstatus.com/incidents/zkxwbgr0cnmx"
title: "GitHub.com Incident (5 minute read)"
author: "unknown"
date_published: "2026-08-19"
date_clipped: "2026-08-23"
category: "DevOps & CI/CD"
source_type: "rss"
discovered_via: "https://tldr.tech/devops/2026-08-19"
source_role: "primary-via-tldr"
---

# GitHub.com Incident (5 minute read)

Source: https://www.githubstatus.com/incidents/zkxwbgr0cnmx

GitHub Status - Incident with GitHub.com
GitHub Octicon logo
Help
Community
Status
GitHub.com
Subscribe to Updates Subscribe
x
Get email notifications whenever GitHub creates , updates or resolves an incident.
Email address:
Enter OTP:
Resend OTP in: seconds
Didn't receive the OTP?
Resend OTP
By subscribing you agree to our Privacy Policy . This site is protected by reCAPTCHA and the Google Privacy Policy and Terms of Service apply.
Get text message notifications whenever GitHub creates or resolves an incident.
Country code:
Afghanistan (+93)
Albania (+355)
Algeria (+213)
American Samoa (+1)
Andorra (+376)
Angola (+244)
Anguilla (+1)
Antigua and Barbuda (+1)
Argentina (+54)
Armenia (+374)
Aruba (+297)
Australia/Cocos/Christmas Island (+61)
Austria (+43)
Azerbaijan (+994)
Bahamas (+1)
Bahrain (+973)
Bangladesh (+880)
Barbados (+1)
Belarus (+375)
Belgium (+32)
Belize (+501)
Benin (+229)
Bermuda (+1)
Bolivia (+591)
Bosnia and Herzegovina (+387)
Botswana (+267)
Brazil (+55)
Brunei (+673)
Bulgaria (+359)
Burkina Faso (+226)
Burundi (+257)
Cambodia (+855)
Cameroon (+237)
Canada (+1)
Cape Verde (+238)
Cayman Islands (+1)
Central Africa (+236)
Chad (+235)
Chile (+56)
China (+86)
Colombia (+57)
Comoros (+269)
Congo (+242)
Congo, Dem Rep (+243)
Costa Rica (+506)
Croatia (+385)
Cyprus (+357)
Czech Republic (+420)
Denmark (+45)
Djibouti (+253)
Dominica (+1)
Dominican Republic (+1)
Egypt (+20)
El Salvador (+503)
Equatorial Guinea (+240)
Estonia (+372)
Ethiopia (+251)
Faroe Islands (+298)
Fiji (+679)
Finland/Aland Islands (+358)
France (+33)
French Guiana (+594)
French Polynesia (+689)
Gabon (+241)
Gambia (+220)
Georgia (+995)
Germany (+49)
Ghana (+233)
Gibraltar (+350)
Greece (+30)
Greenland (+299)
Grenada (+1)
Guadeloupe (+590)
Guam (+1)
Guatemala (+502)
Guinea (+224)
Guyana (+592)
Haiti (+509)
Honduras (+504)
Hong Kong (+852)
Hungary (+36)
Iceland (+354)
India (+91)
Indonesia (+62)
Iraq (+964)
Ireland (+353)
Israel (+972)
Italy (+39)
Jamaica (+1)
Japan (+81)
Jordan (+962)
Kenya (+254)
Korea, Republic of (+82)
Kosovo (+383)
Kuwait (+965)
Kyrgyzstan (+996)
Laos (+856)
Latvia (+371)
Lebanon (+961)
Lesotho (+266)
Liberia (+231)
Libya (+218)
Liechtenstein (+423)
Lithuania (+370)
Luxembourg (+352)
Macao (+853)
Macedonia (+389)
Madagascar (+261)
Malawi (+265)
Malaysia (+60)
Maldives (+960)
Mali (+223)
Malta (+356)
Martinique (+596)
Mauritania (+222)
Mauritius (+230)
Mexico (+52)
Monaco (+377)
Mongolia (+976)
Montenegro (+382)
Montserrat (+1)
Morocco/Western Sahara (+212)
Mozambique (+258)
Namibia (+264)
Nepal (+977)
Netherlands (+31)
New Zealand (+64)
Nicaragua (+505)
Niger (+227)
Nigeria (+234)
Norway (+47)
Oman (+968)
Pakistan (+92)
Palestinian Territory (+970)
Panama (+507)
Paraguay (+595)
Peru (+51)
Philippines (+63)
Poland (+48)
Portugal (+351)
Puerto Rico (+1)
Qatar (+974)
Reunion/Mayotte (+262)
Romania (+40)
Russia/Kazakhstan (+7)
Rwanda (+250)
Samoa (+685)
San Marino (+378)
Saudi Arabia (+966)
Senegal (+221)
Serbia (+381)
Seychelles (+248)
Sierra Leone (+232)
Singapore (+65)
Slovakia (+421)
Slovenia (+386)
South Africa (+27)
Spain (+34)
Sri Lanka (+94)
St Kitts and Nevis (+1)
St Lucia (+1)
St Vincent Grenadines (+1)
Sudan (+249)
Suriname (+597)
Swaziland (+268)
Sweden (+46)
Switzerland (+41)
Taiwan (+886)
Tajikistan (+992)
Tanzania (+255)
Thailand (+66)
Togo (+228)
Tonga (+676)
Trinidad and Tobago (+1)
Tunisia (+216)
Turkey (+90)
Turks and Caicos Islands (+1)
Uganda (+256)
Ukraine (+380)
United Arab Emirates (+971)
United Kingdom (+44)
United States (+1)
Uruguay (+598)
Uzbekistan (+998)
Venezuela (+58)
Vietnam (+84)
Virgin Islands, British (+1)
Virgin Islands, U.S. (+1)
Yemen (+967)
Zambia (+260)
Zimbabwe (+263)
Phone number:
Change number
Enter OTP:
Resend OTP in: 30 seconds
Didn't receive the OTP?
Resend OTP
Message and data rates may apply. By subscribing you agree to our Privacy Policy , the Atlassian Terms of Service , and the Atlassian Privacy Policy . This site is protected by reCAPTCHA and the Google Privacy Policy and Terms of Service apply.
Get incident updates and maintenance status messages in Slack.
Subscribe via Slack
By subscribing you acknowledge our Privacy Policy . In addition, you agree to the Atlassian Cloud Terms of Service and acknowledge Atlassian's Privacy Policy .
Get webhook notifications whenever GitHub creates an incident, updates an incident, resolves an incident or changes a component status.
Webhook URL:
The URL we should send the webhooks to
Email address:
We'll send you email if your endpoint fails
By subscribing you agree to our Privacy Policy . This site is protected by reCAPTCHA and the Google Privacy Policy and Terms of Service apply.
Visit our support site .
Get the Atom Feed or RSS Feed .
Incident with GitHub.com
Incident
Report for GitHub
Resolved
On August 17, 2026, from 13:28–21:15 UTC (7h 47m), GitHub.com experienced elevated errors and latency across Issues, Pull Requests, APIs, Actions, and Copilot. At peak, web/API error rates were approximately 20%, while archive and raw-content downloads reached approximately 50%. SAML/OIDC authentication, SCIM, and Team Sync were also affected, as well as Actions workflows in GHEC with Data Residency that depend on public workflow step definitions hosted on GitHub.com. Most services recovered by 16:36 UTC as our Central US datacenter recovered; Actions was degraded until approximately 18:03 UTC; and Copilot Token Service fully recovered by 21:02.
Some of the failing traffic was moved from Central US to Northern Virginia where it was served successfully until the network failure in Central US was debugged and resolved. Delayed replies to a single internal endpoint triggered a latent retry bug in VS Code that amplified traffic by approximately 10x and caused delayed recovery for the Copilot Token Service.
The immediate cause of the failure was network saturation on load balancers in Central US due to a new peak in traffic. Originally this was caused by an Istio sidecar pod reaching its concurrency limits and failing to auto scale correctly because of a misconfigured policy that watched host service but not sidecar limits. One failure cascaded to more and eventually four HAProxy nodes exhausted their flow limits, degrading the gateway auth path and causing widespread authentication latency and failures. The problem was worsened by optimistic retry logic which overloaded internal load balancers. Pausing HAProxy on those nodes simultaneously produced immediate broad recovery.
The retry storm in Northern VA was fixed by 1) temporarily reducing gateway retry logic with a PR and 2) blocking inbound Copilot Token Service token requests at the load balancers with a 403, and then gradually ramping back up traffic per-site to allow callers to succeed.
Residual Copilot authentication failures continued because client retry behavior amplified load: a failed token operation could generate many extra requests and enter a retry loop. Copilot Token Service traffic increased from a normal 7–9K RPS to 70–100K RPS. Reducing gateway authentication retries and blocking retry-triggering responses stabilized Copilot Token Service and completed recovery.
Complicating factors that impeded recovery included a number of scraping attacks on codeload endpoints.
To prevent recurrence, our follow-up actions include:
- Correcting autoscaling policies to account for service-mesh sidecar concurrency and capacity.
- Auditing Istio request, concurrency, and scaling limits across affected services.
- Reviewing retry limits and backoff behavior across gateways and clients.
- Addressing the VS Code retry behavior that amplified Copilot token traffic.
- Improving load-balancer capacity monitoring and regional failover safeguards.
Posted Aug 17 , 2026 - 21:15 UTC
Update
We are continuing to apply mitigations to address sporadic Copilot authentication failures in some applications. We expect full recovery within the next 30 minutes. Copilot usage via the GitHub CLI and GitHub App are unaffected.
Posted Aug 17 , 2026 - 20:45 UTC
Update
Issues is operating normally.
Posted Aug 17 , 2026 - 20:22 UTC
Update
We are continuing to investigate sporadic failures affecting Copilot authentication in some applications. Copilot usage via the GitHub CLI and GitHub App are unaffected.
Posted Aug 17 , 2026 - 20:08 UTC
Update
We are continuing to investigate sporadic authentication failures. We have partially disabled authentication token retries and have seen improvement, and we are monitoring impact before fully applying this mitigation.
Posted Aug 17 , 2026 - 19:13 UTC
Update
API Requests is operating normally.
Posted Aug 17 , 2026 - 19:01 UTC
Update
API Requests is experiencing degraded availability. We are continuing to investigate.
Posted Aug 17 , 2026 - 18:48 UTC
Update
The degradation affecting Git Operations has been mitigated. We are monitoring to ensure stability.
Posted Aug 17 , 2026 - 18:23 UTC
Update
We identified the problematic component and have taken corrective actions, but we are seeing residual impact in the form of sporadic authentication failures. We are continuing to apply additional mitigations and investigate the remaining impact.
Posted Aug 17 , 2026 - 18:11 UTC
Update
Issues is experiencing degraded performance. We are continuing to investigate.
Posted Aug 17 , 2026 - 17:36 UTC
Update
We identified the problematic component and have taken corrective actions, but we are seeing residual impact across numerous services. We are continuing to apply additional mitigations and investigate the remaining impact.
Posted Aug 17 , 2026 - 17:34 UTC
Update
Git Operations is experiencing degraded performance. We are continuing to investigate.
Posted Aug 17 , 2026 - 17:30 UTC
Update
The degradation affecting API Requests, Actions, Git Operations, Issues, Pages, Pull Requests and Webhooks has been mitigated. We are monitoring to ensure stability.
Posted Aug 17 , 2026 - 16:59 UTC
Update
We identified the problematic component and have taken corrective actions. There are strong signs of recovery but we are still working to completely restore service, with error rates still remaining slightly elevated. We will post further updates as recovery continues.
Posted Aug 17 , 2026 - 16:36 UTC
Update
We are experiencing high error rates around 20% for web experiences and api traffic. Archive downloads and raw repository content downloads are experiencing an approximate 50% error rate. SAML and OIDC authentication, SCIM, and Team Sync are also impacted. We are still working to identify the root cause and will continue to post updates as we learn more and perform mitigation.
Posted Aug 17 , 2026 - 16:16 UTC
Update
We are experiencing high error rates around 20% for web experiences and api traffic. Archive downloads and raw repository content downloads are experiencing an approximate 50% error rate. SAML and OIDC authentication, SCIM, and Team Sync are also impacted. We are currently performing mitigations and will post updates as we progress.
Posted Aug 17 , 2026 - 15:42 UTC
Update
Webhooks is experiencing degraded performance. We are continuing to investigate.
Posted Aug 17 , 2026 - 15:40 UTC
Update
Git Operations is experiencing degraded performance. We are continuing to investigate.
Posted Aug 17 , 2026 - 15:21 UTC
Update
Pages is experiencing degraded performance. We are continuing to investigate.
Posted Aug 17 , 2026 - 15:10 UTC
Update
API Requests is experiencing degraded availability. We are continuing to investigate.
Posted Aug 17 , 2026 - 15:01 UTC
Update
Webhooks is experiencing degraded availability. We are continuing to investigate.
Posted Aug 17 , 2026 - 14:58 UTC
Update
We are experiencing high error rates around 20% for web experiences and api traffic. Archive downloads and raw repository content downloads are experiencing an approximate 50% error rate. SAML and OIDC authentication, SCIM, and Team Sync are also impacted. We are currently performing mitigations based on our investigation thus far and are monitoring for improvement.
Posted Aug 17 , 2026 - 14:58 UTC
Update
Actions is experiencing degraded availability. We are continuing to investigate.
Posted Aug 17 , 2026 - 14:58 UTC
Update
Pull Requests is experiencing degraded availability. We are continuing to investigate.
Posted Aug 17 , 2026 - 14:54 UTC
Update
Issues is experiencing degraded availability. We are continuing to investigate.
Posted Aug 17 , 2026 - 14:49 UTC
Update
Pull Requests is experiencing degraded availability. We are continuing to investigate.
Posted Aug 17 , 2026 - 14:45 UTC
Update
Copilot is experiencing degraded availability. We are continuing to investigate.
Posted Aug 17 , 2026 - 14:31 UTC
Update
We are experiencing high error rates around 20% for web experiences and api traffic. Archive downloads and raw repository content downloads are experiencing an approximate 50% error rate. SAML and OIDC authentication, SCIM, and Team Sync are also impacted. Investigations are on-going and we will continue to provide updates as we discover more information.
Posted Aug 17 , 2026 - 14:24 UTC
Update
We are experiencing high error rates around 20% for web experiences and api traffic. Archive downloads and raw repository content downloads are experiencing an approximate 50% error rate. Investigations are on-going into the root cause, and updates will continue to be provided as we investigate.
Posted Aug 17 , 2026 - 14:04 UTC
Update
Pull Requests is experiencing degraded performance. We are continuing to investigate.
Posted Aug 17 , 2026 - 13:58 UTC
Update
Issues is experiencing degraded performance. We are continuing to investigate.
Posted Aug 17 , 2026 - 13:46 UTC
Update
We are seeing an approximate 20% error rate across numerous experiences including Pull Requests, Issues, and others. Investigations are currently under way and we will be posting updates as they become available
Posted Aug 17 , 2026 - 13:45 UTC
Update
Webhooks is experiencing degraded performance. We are continuing to investigate.
Posted Aug 17 , 2026 - 13:44 UTC
Update
Actions is experiencing degraded performance. We are continuing to investigate.
Posted Aug 17 , 2026 - 13:42 UTC
Update
API Requests is experiencing degraded performance. We are continuing to investigate.
Posted Aug 17 , 2026 - 13:41 UTC
Investigating
We are investigating reports of impacted performance for some GitHub services.
Posted Aug 17 , 2026 - 13:40 UTC
This incident affected: Git Operations, Webhooks, API Requests, Issues, Pull Requests, Actions, Pages, and Copilot.
← Current Status
Powered by Atlassian Statuspage
Subscribe to our developer newsletter
Get tips, technical guides, and best practices. Twice a month. Right in your
inbox.
Subscribe
Product
Features
Enterprise
Copilot
Security
Pricing
Team
Resources
Roadmap
Compare GitHub
Platform
Developer API
Partners
Education
GitHub CLI
GitHub Desktop
GitHub Mobile
Support
Docs
Community Forum
Professional Services
Skills
Contact GitHub
Company
About
Customer
stories
Blog
The ReadME Project
Careers
Newsroom
Inclusion
Social Impact
Shop
©
GitHub, Inc.
Terms
Privacy ( Updated 08/2022 )
GitHub X
GitHub Facebook
GitHub LinkedIn
GitHub YouTube
Twitch
TikTok
GitHub.com
×
Subscribe to Incident
Subscribe to updates for Incident with GitHub.com via email and/or text message. You'll receive email notifications when incidents are updated, and text message notifications whenever GitHub creates or resolves an incident.
VIA EMAIL:
VIA SMS:
Afghanistan (+93)
Albania (+355)
Algeria (+213)
American Samoa (+1)
Andorra (+376)
Angola (+244)
Anguilla (+1)
Antigua and Barbuda (+1)
Argentina (+54)
Armenia (+374)
Aruba (+297)
Australia/Cocos/Christmas Island (+61)
Austria (+43)
Azerbaijan (+994)
Bahamas (+1)
Bahrain (+973)
Bangladesh (+880)
Barbados (+1)
Belarus (+375)
Belgium (+32)
Belize (+501)
Benin (+229)
Bermuda (+1)
Bolivia (+591)
Bosnia and Herzegovina (+387)
Botswana (+267)
Brazil (+55)
Brunei (+673)
Bulgaria (+359)
Burkina Faso (+226)
Burundi (+257)
Cambodia (+855)
Cameroon (+237)
Canada (+1)
Cape Verde (+238)
Cayman Islands (+1)
Central Africa (+236)
Chad (+235)
Chile (+56)
China (+86)
Colombia (+57)
Comoros (+269)
Congo (+242)
Congo, Dem Rep (+243)
Costa Rica (+506)
Croatia (+385)
Cyprus (+357)
Czech Republic (+420)
Denmark (+45)
Djibouti (+253)
Dominica (+1)
Dominican Republic (+1)
Egypt (+20)
El Salvador (+503)
Equatorial Guinea (+240)
Estonia (+372)
Ethiopia (+251)
Faroe Islands (+298)
Fiji (+679)
Finland/Aland Islands (+358)
France (+33)
French Guiana (+594)
French Polynesia (+689)
Gabon (+241)
Gambia (+220)
Georgia (+995)
Germany (+49)
Ghana (+233)
Gibraltar (+350)
Greece (+30)
Greenland (+299)
Grenada (+1)
Guadeloupe (+590)
Guam (+1)
Guatemala (+502)
Guinea (+224)
Guyana (+592)
Haiti (+509)
Honduras (+504)
Hong Kong (+852)
Hungary (+36)
Iceland (+354)
India (+91)
Indonesia (+62)
Iraq (+964)
Ireland (+353)
Israel (+972)
Italy (+39)
Jamaica (+1)
Japan (+81)
Jordan (+962)
Kenya (+254)
Korea, Republic of (+82)
Kosovo (+383)
Kuwait (+965)
Kyrgyzstan (+996)
Laos (+856)
Latvia (+371)
Lebanon (+961)
Lesotho (+266)
Liberia (+231)
Libya (+218)
Liechtenstein (+423)
Lithuania (+370)
Luxembourg (+352)
Macao (+853)
Macedonia (+389)
Madagascar (+261)
Malawi (+265)
Malaysia (+60)
Maldives (+960)
Mali (+223)
Malta (+356)
Martinique (+596)
Mauritania (+222)
Mauritius (+230)
Mexico (+52)
Monaco (+377)
Mongolia (+976)
Montenegro (+382)
Montserrat (+1)
Morocco/Western Sahara (+212)
Mozambique (+258)
Namibia (+264)
Nepal (+977)
Netherlands (+31)
New Zealand (+64)
Nicaragua (+505)
Niger (+227)
Nigeria (+234)
Norway (+47)
Oman (+968)
Pakistan (+92)
Palestinian Territory (+970)
Panama (+507)
Paraguay (+595)
Peru (+51)
Philippines (+63)
Poland (+48)
Portugal (+351)
Puerto Rico (+1)
Qatar (+974)
Reunion/Mayotte (+262)
Romania (+40)
Russia/Kazakhstan (+7)
Rwanda (+250)
Samoa (+685)
San Marino (+378)
Saudi Arabia (+966)
Senegal (+221)
Serbia (+381)
Seychelles (+248)
Sierra Leone (+232)
Singapore (+65)
Slovakia (+421)
Slovenia (+386)
South Africa (+27)
Spain (+34)
Sri Lanka (+94)
St Kitts and Nevis (+1)
St Lucia (+1)
St Vincent Grenadines (+1)
Sudan (+249)
Suriname (+597)
Swaziland (+268)
Sweden (+46)
Switzerland (+41)
Taiwan (+886)
Tajikistan (+992)
Tanzania (+255)
Thailand (+66)
Togo (+228)
Tonga (+676)
Trinidad and Tobago (+1)
Tunisia (+216)
Turkey (+90)
Turks and Caicos Islands (+1)
Uganda (+256)
Ukraine (+380)
United Arab Emirates (+971)
United Kingdom (+44)
United States (+1)
Uruguay (+598)
Uzbekistan (+998)
Venezuela (+58)
Vietnam (+84)
Virgin Islands, British (+1)
Virgin Islands, U.S. (+1)
Yemen (+967)
Zambia (+260)
Zimbabwe (+263)
Enter mobile number
Edit number
Send OTP
Enter the OTP sent
Resend OTP
in 30 seconds
To receive SMS updates, please verify your number. To proceed with just email click ‘Subscribe’
Subscribe to Incident
Message and data rates may apply. By subscribing you agree to our Privacy Policy , the Atlassian Terms of Service , and the Atlassian Privacy Policy . This site is protected by reCAPTCHA and the Google Privacy Policy and Terms of Service apply.
