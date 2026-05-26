---
source: "https://www.itpro.com/security/github-internal-repositories-exfiltrated-via-malicious-vs-code-extension"
title: "GitHub internal repositories exfiltrated via malicious VS Code extension (5 minute read)"
author: "TLDR DevOps"
date_published: "Mon, 25 May 2026 00:00:00 GMT"
date_clipped: "2026-05-26"
category: "DevOps & CI/CD"
source_type: "rss"
discovered_via: "https://tldr.tech/devops/2026-05-25"
source_role: "primary-via-tldr"
---

# GitHub internal repositories exfiltrated via malicious VS Code extension (5 minute read)

Source: https://www.itpro.com/security/github-internal-repositories-exfiltrated-via-malicious-vs-code-extension

Home 
Security 
GitHub internal repositories exfiltrated via malicious VS Code extension 
The breach has been claimed by the TeamPCP hacking group, which said it is offering the data for sale
By
Emma Woollacott 
published
21 May 2026
in News 
When you purchase through links on our site, we may earn an affiliate commission. Here’s how it works .
(Image credit: Getty Images) 
Share 
Copy link
Facebook
X
Linkedin
Bluesky
Share this article
Join the conversation
Follow us
Add us as a preferred source on Google
Newsletter
Subscribe to our newsletter
GitHub has confirmed that around 3,800 internal repositories have been breached, after a developer unwittingly installed a malicious VS Code extension.
The Microsoft-owned code repository and DevOps platform said the breach was detected on Monday, but that the activity involved exfiltration of GitHub-internal repositories only.
"We have no evidence of impact to customer information stored outside of GitHub's internal repositories, such as our customers' own enterprises, organizations, and repositories," said the firm's chief information security officer, Alexis Wales.
"Some of GitHub's internal repositories contain information from customers, for example, excerpts of support interactions. If any impact is discovered, we will notify customers via established incident response and notification channels."
Latest Videos From GitHub said it started rotating critical secrets as soon as it discovered the breach, with the highest-impact credentials prioritized first. It is now analyzing logs, validating secret rotation, and monitoring its infrastructure for any follow-on activity, it said, promising a fuller report once it's finished its investigation.
GitHub hasn't explicitly named the attacker, but made reference to a claim by the TeamPCP hacker group that it had accessed around 3,800 repositories, saying that the number was consistent with its investigation so far.
TeamPCP , which first appeared late last year, is the group linked to the Mini Shai-Hulud worm, and carries out supply chain attacks by stealing CI/CD credentials and using them to publish infected versions of further packages.
window.sliceComponents = window.sliceComponents || {};
externalsScriptLoaded.then(() => {
window.reliablePageLoad.then(() => {
var componentContainer = document.querySelector("#slice-container-newsletterForm-articleInbodyContent-vPviULBfXJueZWNnALYACA");
if (componentContainer) {
var data = {"layout":"inbodyContent","header":"Get the ITPro daily newsletter","tagline":"Sign up today and you will receive a free copy of our Future Focus 2025 report - the leading guidance on AI, cybersecurity and other IT challenges as per 700+ senior executives","formFooterText":"By submitting your information you agree to the Terms & Conditions and Privacy Policy and are aged 16 or over.","usDisclaimerFooterText":"By signing up, you agree to our Terms of services and acknowledge that you have read our Privacy Notice . You also agree to receive marketing emails from us that may include promotions from our trusted partners and sponsors, which you can unsubscribe from at any time.","successMessage":{"body":"Thank you for signing up. You will receive a confirmation email shortly."},"failureMessage":"There was a problem. Please refresh the page and try again.","method":"POST","inputs":[{"type":"hidden","name":"NAME"},{"type":"email","name":"MAIL","placeholder":"Your Email Address","required":true},{"type":"hidden","name":"NEWSLETTER_CODE","value":"ITP_STD"},{"type":"hidden","name":"LANG","value":"EN"},{"type":"hidden","name":"SOURCE","value":"60"},{"type":"hidden","name":"COUNTRY"},{"type":"checkbox","name":"CONTACT_OTHER_BRANDS","label":{"text":"Contact me with news and offers from other Future brands"}},{"type":"checkbox","name":"CONTACT_PARTNERS","label":{"text":"Receive email from us on behalf of our trusted partners or sponsors"}},{"type":"submit","value":"Sign me up","required":true}],"endpoint":"https:\/\/newsletter-subscribe.futureplc.com\/v2\/submission\/submit","analytics":[{"analyticsType":"widgetViewed"}],"ariaLabels":{}};
var triggerHydrate = function() {
window.sliceComponents.newsletterForm.hydrate(data, componentContainer);
}
if (window.lazyObserveElement) {
window.lazyObserveElement(componentContainer, triggerHydrate);
} else {
triggerHydrate();
}
}
}).catch(err => console.error('%c FTE ','background: #9306F9; color: #ffffff','Hydration Script has failed for newsletterForm-articleInbodyContent-vPviULBfXJueZWNnALYACA Slice', err));
}).catch(err => console.error('%c FTE ','background: #9306F9; color: #ffffff','Externals script failed to load', err));
Get the ITPro daily newsletter Sign up today and you will receive a free copy of our Future Focus 2025 report - the leading guidance on AI, cybersecurity and other IT challenges as per 700+ senior executives
Contact me with news and offers from other Future brands Receive email from us on behalf of our trusted partners or sponsors By submitting your information you agree to the Terms & Conditions and Privacy Policy and are aged 16 or over. The group has reportedly not asked for a ransom for the GitHub data, but is offering the stolen data for sale for $50,000, saying that if it doesn't receive an offer, it will leak it for free.
"This is another reminder that developers are now permanent targets in software supply chain attacks. TeamPCP has shown how a motivated attacker can move through the tools developers trust every day – open source packages, extensions, accounts, and credentials – rather than trying to break in through the front door," said Ilkka Turunen, Field CTO at Sonatype.
"Combined with the acceleration we're already seeing from AI-assisted vulnerability discovery, the window between compromise and exploitation is collapsing. The old assumption was that defenders would have time to identify, prioritize, and respond. That margin is disappearing."
The news came just a day after the Nx Console VS Code extension, which has 2.2 million installs, was briefly backdoored, with the malicious version collecting credentials silently when a developer opened a workspace. The issue was handled swiftly, with the extension pulled within 18 minutes on the VS Code Marketplace and 36 minutes on Open VSX.
"The community's ability to catch and remove malicious packages is real. For extensions with millions of installs, it's also insufficient," commented Shaun Brown technical product marketer at Aikido Security.
"Caught in 18 minutes and prevented exposure are not the same thing. Minimum package and extension ages are the best way to protect your devices from similar attacks today."
if (window.sliceHydrationLazy) {
window.sliceHydrationLazy("authorBio-vPviULBfXJueZWNnALYACA", "authorBio", JSON.stringify({"layout":"default","border":false,"separator":true,"name":"Emma Woollacott","authorLink":{"text":"Emma Woollacott","href":"https:\/\/www.itpro.com\/author\/emma-woollacott"},"image":{"src":"https:\/\/cdn.mos.cms.futurecdn.net\/aWfskavxoVSMDy6cDWtYmJ.jpg","alt":"Emma Woollacott","srcSetSizes":[140],"sizes":{"default":"100px","700px":"140px"},"fullscreen":false,"lazyLoading":true,"addSEOMetaData":false,"removeNativeWidthRestriction":false,"dataBordeauxImageCheckAttr":false,"noCredit":false},"socialLinks":{"socialButtons":[{"iconName":"TWITTER","href":"https:\/\/twitter.com\/EmmaWoollacott"},{"iconName":"LINKEDIN","href":"https:\/\/www.linkedin.com\/in\/emma-woollacott-6a641812"}],"socialNavAriaLabel":"Social Links Navigation"},"biography":" Emma Woollacott is a freelance journalist writing for publications including the BBC, Private Eye, Forbes, Raconteur and specialist technology titles. ","collapsible":{"enabled":true,"maxHeight":250,"readMoreText":"Read more","readLessText":"Read less"}}), "https://slice.vanilla.futurecdn.net/13-4-23/js/authorBio.js");
} else {
console.error('%c FTE ','background: #9306F9; color: #ffffff','no lazy slice hydration function available');
}
Emma Woollacott Social Links Navigation Emma Woollacott is a freelance journalist writing for publications including the BBC, Private Eye, Forbes, Raconteur and specialist technology titles.
Latest 
SPONSORED_HEADLINE
SPONSORED 
SPONSORED_STRAPLINE
SPONSORED_DISCLAIMER 
Wasabi ramps up EMEA channel push with focus on cyber resilience
News 
The cloud storage vendor is expanding partner tools and integrations as AI-driven data growth and ransomware threats continue to rise
AI forces bigger software players to adapt pricing to compete
Industry Insights 
Software companies adding AI capabilities will need to upgrade monetization stacks designed for subscriptions rather than usage-based billing
You might also like 
Millions of developers could be impacted by flaws in Visual Studio Code extensions – here's what you need to know and how to protect yourself
News 
The VS Code vulnerabilities highlight broader IDE security risks, said OX Security
Small businesses can't get cyber strategies up and running – here's why
News 
SMBs are turning to outside help to shore up security as internal strategies fall flat
Using AI to code? Watch your security debt
news 
Black Duck research shows faster development may be causing risks for companies
Organizations warned of "significant lag" in deepfake protection investment
news 
Defenses are failing to keep up with the rapidly growing attack vector, with most organizations being overconfident
Teens arrested over nursery chain Kido hack
news 
The ransom attack caused widespread shock when the hackers published children's personal data
Middlesbrough Council boosts cybersecurity spending, strategy in response to repeated cyberattacks
News 
Councils across the UK have publicly struggled with maintaining services in the face of major cyber disruption
Foreign states ramp up cyberattacks on EU with AI-driven phishing and DDoS campaigns
News 
ENISA warns of hacktivism, especially through DDoS attacks
Cybersecurity leaders must stop seeing resilience as a "tick box exercise" to achieve meaningful protection, says Gartner expert
News 
Collaboration between departments and a better understanding of organizational metrics are key to addressing security blindspots
View More ▸
