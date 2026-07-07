---
source: "https://detect.fyi/the-blind-spot-in-the-watchtower-detections-for-when-someone-attacks-your-sentinel-897709f0dcd9"
title: "The Blind Spot in the Watchtower: Detections for When Someone Attacks Your Sentinel"
author: "detect.fyi"
date_published: "2026-07-06"
date_clipped: "2026-07-07"
category: "Security & Ethical Hacking"
source_type: "web"
---

# The Blind Spot in the Watchtower: Detections for When Someone Attacks Your Sentinel

Source: https://detect.fyi/the-blind-spot-in-the-watchtower-detections-for-when-someone-attacks-your-sentinel-897709f0dcd9

# The Blind Spot in the Watchtower: Detections for When Someone Attacks Your Sentinel

Your SIEM monitors everything in your environment, but it rarely monitors itself the first thing an attacker will try to access.Today, we’ll discuss all the possible ways to detect when someone tries to tamper your watchtower.

Think about how a burglar handles a house with cameras.

An amateur breaks in and gets caught on film. A professional finds the recorder first, unplugs it, and then takes their time. The theft still happens, but there is no record of it because the thing that was supposed to watch got dealt with before the real work began.

Your Microsoft Sentinel workspace is that recorder. A capable attacker in a well-run environment usually does not start with a loud attack your rules will catch. They start quietly by reaching for the recorder disabling the rule that would flag them, pausing the feed that supplies it, shortening retention or signing into your security portal from a place they should not be.

Here is the uncomfortable part, most SOC teams have hundreds of detections aimed outward, at laptops, identities, email and cloud services. Very few are aimed inward, at Sentinel itself. *The watchtower watches the whole valley and never looks down at its own foundations.*

This post fixes that. These few checks that make your SIEM watch itself, each catching a different way someone can blind your detection.

### Where Sentinel tracks changes to itself

For Sentinel to watch itself, it needs a record of the changes made to it. That record lives in three places, and each check below pulls from one of them.

**AzureActivity**is the broad log of who did what. When someone creates, changes or deletes something in Sentinel like a rule, a feed or a setting-it shows up here with the user name and IP address. This is the main sourcen and it comes from the Azure Activity connector which is free.**SentinelAudit**is the detailed change log for detection rules. It shows who changed a rule and what it looked like before and after. It only works after you turn on Sentinel’s health and audit feature, which is also free.**SentinelHealth**shows whether your rules are actually running. It also makes it clear when a rule is disabled and did not run. It uses the same health and audit feature switch.

One small habit that saves time: when you query the audit and health data, use the built-in shortcuts `_SentinelAudit()`

and `_SentinelHealth()`

instead of the raw table names. Microsoft keeps those shortcuts working even if the underlying tables change.

**One idea that makes every check sharper.**Keep a small watchlist of approved admins and automation accounts, so each check can quickly spot changes made by anyone else. Most of the time, your own team will be making legitimate updates, so this keeps the signal clean and the noise down. Build that list first and the detections become much sharper.

### 1.Someone switched off or deleted a detection rule

**What’s going on:**A detection rule is a tripwire. If someone switches it off, the attacker’s next move goes unseen. Your own team disables rules for valid reasons, so the real signal is not just that a rule changed it’s that a rule changed by someone outside your team.

`let AuthorizedAdmins = _GetWatchlist('Account')`

| project SearchKey;

_SentinelAudit()

| where TimeGenerated >ago(24h)

| where SentinelResourceType == "Analytic Rule"

| where Description in ("Analytics rule deleted","Create or update analytics rule.")

| extend Caller = tostring(ExtendedProperties.CallerName)

| where isnotempty(Caller)

| where Caller !in (AuthorizedAdmins)

| project TimeGenerated, Activity = Description,RuleName = SentinelResourceName, Caller

Load the list of approved people, then show every rule that was deleted or edited by anyone not on that list. If you get a result, it means someone touched your tripwires who had no business doing so.

**How to run it:**Run it as a scheduled rule every hour. If you do not have the watchlist yet, skip the list check and alert on any deletion instead-deleting a rule is rare enough that it is always worth reviewing.

### 2.Someone shortened retention or removed a table

**What’s going on:**Retention is how long your evidence stays available. If an attacker cannot delete today’s logs, the next best move is to shorten retention so the evidence quietly disappears over time. Removing a table is the blunt version the data simply stops being kept.

`let AuthorizedAdmins = _GetWatchlist('Account')`

| project SearchKey;

AzureActivity

| where OperationNameValue has_any (

"MICROSOFT.OPERATIONALINSIGHTS/WORKSPACES/TABLES/WRITE",

"MICROSOFT.OPERATIONALINSIGHTS/WORKSPACES/TABLES/DELETE")

| where ActivityStatusValue has_any ("Success", "Succeeded")

| extend props = parse_json(Properties)

| extend Action = extract(@"/([^/]+)$", 1, tostring(props.message))

| extend Table = extract(@"/([^/]+)$", 1, tostring(props.resource))

| where Caller !in (AuthorizedAdmins)

| project TimeGenerated, ActionPerformedUser=Caller, UserIP=CallerIpAddress,Operation = OperationNameValue, Action,Table, ResourceGroup

This check looks for changes to the workspace and to individual tables, since those changes control how long data is retained or whether a table exists at all. A retention change that lowers the value, especially without a matching change ticket is a quiet red flag that most people never look for.

### 3.Someone changed a feed or switched off a connector

**What’s going on:**Data connectors and data collection rules are the pipes that feed information into Sentinel. Turning off a connector or changing one of those pipes is like cutting the wire between a camera and its recorder. The camera still exists, but nothing reaches the tape. It is one of the stealthiest moves, because your rules still look enabled they are just no longer being fed.

`let AuthorizedAdmins = _GetWatchlist('Account')`

| project SearchKey;

AzureActivity

| where Caller !in (AuthorizedAdmins)

| where OperationNameValue has_any (

"MICROSOFT.INSIGHTS/DATACOLLECTIONRULES/WRITE",

"MICROSOFT.INSIGHTS/DATACOLLECTIONRULES/DELETE",

"MICROSOFT.SECURITYINSIGHTS/DATACONNECTORS/WRITE",

"MICROSOFT.SECURITYINSIGHTS/DATACONNECTORS/DELETE"

)

| where ActivityStatusValue has_any ("Success", "Succeeded")

| extend props = parse_json(Properties)

| extend RawResource = tostring(props.resource)

| extend DataCollectionRule = iff(

OperationNameValue has "DATACOLLECTIONRULES",

RawResource,

""

)

| extend DataConnector = iff(

OperationNameValue has "DATACONNECTORS",

extract(@"/([^/]+)$", 1, RawResource),

""

)

| extend Action = extract(@"/([^/]+)$", 1, tostring(props.message))

| project TimeGenerated,Action,PerformedUser=Caller, UserIP=CallerIpAddress,OperationNameValue,DataCollectionRule,DataConnector,ResourceGroup

**Make it stronger with a silence check:**The best version adds a second clue a table that suddenly goes quiet. If someone changes a feed and the table it powers drops to zero in the next few hours, that is a very strong sabotage signal. Watch your busiest tables for sudden silence.

**4.Someone granted themselves or others new access**

**What’s going on:**Think of this as the attacker’s very first move. Before a hacker can turn off your security rules, they have to give themselves permission to do it. If someone suddenly gets a new, high-level role in Microsoft Sentinel, that is a massive red flag. Unfortunately, it’s also the exact warning sign most security teams completely miss.

`let AuthorizedAdmins = _GetWatchlist('Account')`

| project SearchKey;

let RoleMap = datatable(RoleDefinitionId:string, RoleName:string)

[

"92aaf0da-9dab-42b6-94a3-d43ce8d16293", "Log Analytics Contributor",

"73c42c96-874c-492b-b04d-ab87d138a893", "Log Analytics Reader",

"ab8e14d6-4a74-4a29-9ba8-549422addade", "Sentinel Contributor",

"3e150937-b8fe-4cfb-8061-0eaf05ecd056", "Sentinel Responder",

"5e467623-bb1f-42f4-a55d-6e525e11384b", "Sentinel Reader",

"8e3af657-a8ff-443c-a75c-2fe8c4bcb635", "Owner",

"b24988ac-6180-42a0-ab88-20f7382dd24c", "Contributor",

"18d7d88d-d35e-4fb5-a5c3-7773c20a72d9", "User Access Administrator"

];

AzureActivity

| where OperationNameValue has_any (

"MICROSOFT.AUTHORIZATION/ROLEASSIGNMENTS/WRITE",

"MICROSOFT.AUTHORIZATION/ROLEASSIGNMENTS/DELETE"

)

| where Caller !in (AuthorizedAdmins)

| extend props = parse_json(Properties)

| extend requestBody = parse_json(tostring(props.requestbody))

| extend roleDefPath = tostring(requestBody.Properties.RoleDefinitionId)

| extend RoleDefinitionId = tostring(split(roleDefPath, "/")[-1])

| lookup RoleMap on RoleDefinitionId

| extend RoleName = coalesce(RoleName, "Unknown Role")

| extend PrincipalId = tostring(requestBody.Properties.PrincipalId)

| extend PrincipalType = tostring(requestBody.Properties.PrincipalType)

| extend Scope = tostring(requestBody.Properties.Scope)

| where isnotempty(PrincipalId)

| project TimeGenerated, OperationNameValue, Caller, PrincipalId, PrincipalType, RoleName, RoleDefinitionId, Scope, ResourceGroup

This alert flags anyone who changes access permissions on your Sentinel resources without approval.If an attacker quietly gives themselves control over your security tools, a major breach is about to happen. Catching this early is one of the most important things you can do to protect your network.

## Get Rohitashokgowd’s stories in your inbox

Join Medium for free to get updates from this writer.

**Worth pairing with identity-role changes too.** It’s also a good idea to look at identity role changes. The query above focuses on access to Azure resources. But if you also want to catch when someone is added to a powerful role (like Global Administrator), you should monitor the ** AuditLogs** table for “Add member to role” actions on important roles. These are two different areas resource access and directory roles and a strong SOC should keep an eye on both.

**5.Someone deleted the diagnostic settings feeding your logs**

**What’s going on:** Diagnostic settings are the plumbing that routes logs from a resource into Sentinel.If someone deletes a diagnostic setting, the logs don’t stop being created they just stop reaching Sentinel.This is a well known evasion technique. Microsoft even provides a detection template for it, which shows how serious it is. What this detection does is alert you when someone quietly cuts off the flow of logs into your SIEM.

`AzureActivity`

| where OperationNameValue =~ "MICROSOFT.INSIGHTS/DIAGNOSTICSETTINGS/DELETE"

| where ActivityStatusValue has_any ("Success", "Succeeded")

| extend props = parse_json(Properties)

| extend Action = extract(@"/([^/]+)$", 1, tostring(props.message))

| extend DiagnosticSettingName = tostring(split(tostring(props.resource), "/")[-1])

| project TimeGenerated, Caller, CallerIpAddress, DiagnosticSettingName, ResourceGroup, Operation = OperationNameValue,Action

Deleting a diagnostic setting is not something that happens often in normal operations, so every alert like this should be looked at and questioned.

**6.Someone accessed the security portal from an unexpected place**

**What’s going on:**Your SOC signs into Sentinel from known accounts, on managed devices, from predictable places. An attacker with stolen credentials does not match that pattern. The signal is access to your security tooling that looks wrong an unfamiliar country, an unmanaged device or an account with no reason to be there.

`let PortalApps = dynamic([`

"Azure Portal",

"Microsoft 365 Admin portal",

"Exchange Admin Center",

"Microsoft 365 Security and Compliance Center",

"Microsoft Teams Admin Portal Service",

"Microsoft Office 365 Portal"

]);

SigninLogs

| where AppDisplayName in~ (PortalApps) and ResultType == "0"

| extend

DeviceId = tostring(DeviceDetail.deviceId),

OS = tostring(DeviceDetail.operatingSystem),

ADjoined = tostring(DeviceDetail.trustType),

NamedLocation=tostring(parse_json(NetworkLocationDetails)[0].networkType)

| where NamedLocation !in ("trustedNamedLocation","namedNetwork")

| where ADjoined !in ("Azure AD registered","Azure AD joined" ,"Hybrid Azure AD joined")

| summarize by TimeGenerated,Identity,UserDisplayName,UserPrincipalName,Location,AppDisplayName,IPAddress

This looks at your own team’s successful sign-ins to the security portals and flags any from outside your trusted countries or from a device that is not managed. A detection engineer’s account appearing from an unexpected country on an unknown laptop is what a stolen password looks like.

**7.Someone changed automation, playbooks, watchlists or workbooks**

**What’s going on:**A security team relies on a lot of behind-the-scenes machinery to do its job. This includes automations that route alerts, playbooks that instantly respond to threats, watchlists that hold critical data and workbooks (dashboards) that display everything.

An attacker who knows what they are doing doesn’t even need to touch your security rules to mess with you. Instead, they can quietly disable the automation that isolates an infected device or tamper with a watchlist that your main rules depend on.

`let AuthorizedAdmins = _GetWatchlist('Account')`

| project SearchKey;

AzureActivity

| where Caller !in (AuthorizedAdmins)

| where OperationNameValue has_any (

"MICROSOFT.SECURITYINSIGHTS/AUTOMATIONRULES/WRITE",

"MICROSOFT.SECURITYINSIGHTS/AUTOMATIONRULES/DELETE",

"MICROSOFT.LOGIC/WORKFLOWS/WRITE",

"MICROSOFT.LOGIC/WORKFLOWS/DISABLE/ACTION",

"MICROSOFT.SECURITYINSIGHTS/WATCHLISTS/WRITE",

"MICROSOFT.SECURITYINSIGHTS/WATCHLISTS/DELETE",

"MICROSOFT.INSIGHTS/WORKBOOKS/WRITE",

"MICROSOFT.INSIGHTS/WORKBOOKS/DELETE"

)

| where ActivityStatusValue has_any ("Success", "Succeeded")

| extend props = parse_json(Properties)

| extend Resource = tostring(props.resource)

| extend Component = case(

OperationNameValue has "AUTOMATIONRULES", "Automation Rule",

OperationNameValue has "WORKFLOWS", "Playbook",

OperationNameValue has "WATCHLISTS", "Watchlist",

OperationNameValue has "WORKBOOKS", "Workbook",

"Other"

)

| extend ResourceName = case(

Component == "Automation Rule",extract(@"([^/]+)$", 1, Resource),

Component == "Watchlist",extract(@"([^/]+)$", 1, Resource),

Component == "Playbook",Resource,

Component == "Workbook",Resource,

Resource

)

| summarize arg_max(TimeGenerated, *) by Component, ResourceName

| project TimeGenerated, Caller, CallerIpAddress, Component, OperationNameValue, ResourceName

This alert monitors all four of these behind-the-scenes tools at the same time. If anyone outside your team changes them, it flags it immediately and tells you exactly what was touched.Keep a close eye on **playbooks**. If an attacker switches off a response playbook, it is incredibly damaging because it is completely silent. Your security rules will still fire and alerts will still pop up, but the automatic safety features like instantly blocking a hacked account or isolating a compromised computer will simply never happen.

### 8.Someone tampered with your incidents

**What’s going on:** The last place to hide is the incident queue itself. Someone with access can close the incident that describes their own activity, reassign it into a void, or quietly lower its severity so nobody looks. If detection is the smoke alarm, the incident queue is the fire log — and someone editing the fire log to say “no fire here” is a specific and chilling signal.

`let AuthorizedAdmins = _GetWatchlist('Account')`

| project SearchKey;

let IncidentActivity =

AzureActivity

| where Caller !in (AuthorizedAdmins)

| where OperationNameValue has "MICROSOFT.SECURITYINSIGHTS/INCIDENTS"

| where OperationNameValue has_any ("/WRITE", "/DELETE")

| where ActivityStatusValue has_any ("Success", "Succeeded")

| extend props = parse_json(Properties)

| extend Action = extract(@"/([^/]+)$", 1, tostring(props.message))

| extend IncidentNameID = extract(@"/([^/]+)$", 1, tostring(props.resource))

| summarize arg_max(TimeGenerated, *) by IncidentNameID

| project TimeGenerated, Caller, CallerIpAddress,Operation = OperationNameValue,IncidentNameID;

IncidentActivity

| join kind=leftouter (

SecurityIncident

| summarize arg_max(TimeGenerated, *) by IncidentName

| project IncidentName,IncidentNumber,Title,Severity,Status

) on $left.IncidentNameID == $right.IncidentName

| project TimeGenerated,Caller,CallerIpAddress,Operation,IncidentNumber,Title,Severity,Status,IncidentNameID

This flags anyone outside your team who creates, edits or incident closing, reassigning or changing its severity. The people allowed to work your queue are a small, known set. Anyone else editing incidents deserves an immediate question.

### 9.Someone went for the whole workspace or its safety locks

**What’s going on:** This is the nuclear option. Rather than pick off individual rules, an attacker deletes the entire Sentinel workspace or first removes the resource lock that protects it from deletion. Losing the workspace means losing everything at once. It is rare, it is catastrophic, and it should be your single loudest alarm.

`AzureActivity`

| where OperationNameValue has_any (

"MICROSOFT.OPERATIONALINSIGHTS/WORKSPACES/DELETE",

"MICROSOFT.AUTHORIZATION/LOCKS/DELETE")

| extend props = parse_json(Properties)

| extend Action = extract(@"/([^/]+)$", 1, tostring(props.message))

| extend ResourceName = extract(@"^([^/]+)", 1, tostring(props.resource))

| project TimeGenerated, Caller, CallerIpAddress,Operation = OperationNameValue, ResourceName, ResourceGroup

**A prevention tip, not just detection:** put a delete-lock on your Sentinel resource group and give only a tiny number of people the right to remove it. Azure also keeps a deleted workspace recoverable for 14 days good to know, but do not rely on it as your plan.

**How to switch these on without drowning in noise**

A few practical tips to make these useful instead of annoying:

**Start by building your list.** Most of these checks depend on a list called *Accounts**.* Take some time to list the few people and automation accounts that are actually allowed to change your detection setup. This one step makes a huge difference in reducing noise.

**Turn on health and auditing. **One of the checks relies on the _SentinelAudit() function, which only works after you enable auditing in Sentinel settings. It’s free and only takes a couple of minutes.

**Keep alerts rare but important.** These checks are meant to be high-signal and low-noise. Most of them should almost never trigger. That’s intentional. When they do fire, treat them as important set a high severity and make sure they go somewhere a real person will see them.

### The honest limitations

These detections are powerful, but they’re not perfect. Here are a few things to keep in mind:

**A strong attacker could disable them.** Someone with full control of your workspace could turn off these checks. To protect against that, send these alerts outside of the workspace like to email, another tenant or a separate system. That way, even if your workspace is compromised, you still get the warning.

**There can be small delays.** Activity logs are not instant. They can take a few minutes to show up. For most cases, that delay is acceptable.

**Your team makes changes all the time.** People will update rules, tweak settings and adjust data sources regularly. Without the approved admins list, these alerts will overwhelm you. With it, they become very precise and useful. This list isn’t optional it’s what makes the whole thing work.

## Closing

Go back to the burglar and the recorder.

The reason a professional reaches for the recorder first is that they assume nobody is watching it. It is the one device pointed at everything else and, almost always, with nothing pointed back at it.

Your Sentinel workspace has spent its whole life watching your environment. These nine checks are how you finally point something back at it so that the moment someone reaches for your recorder, that reach becomes the loudest thing they do.

**The watchtower should watch the valley. It should also, once in a while, look down at its own foundations.**

**Bonus:**If you want to back up your Sentinel configurations to Azure Storage automatically (without any manual effort), check this out-https://medium.com/@rohitashokgowd/back-up-your-microsoft-sentinel-configurations-to-azure-blob-storage-using-azure-automation-account-b8a1b224a5ac
