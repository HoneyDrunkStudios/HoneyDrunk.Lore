---
source: "https://www.datadoghq.com/blog/ci-cd-threat-matrix/"
title: "CI/CD security: threat modeling using a MITRE-style threat matrix"
author: "Juvenal Araujo, Julie Agnes-Sparks Bowen Chen"
date_published: "2026-04-08"
date_clipped: "2026-06-01"
category: "DevOps & CI/CD"
source_type: "web"
---

# CI/CD security: threat modeling using a MITRE-style threat matrix

Source: https://www.datadoghq.com/blog/ci-cd-threat-matrix/

The Monitor CI/CD security: threat modeling using a MITRE-style threat matrix security cloud siem threat detection Published
Apr 8, 2026 Read time
6m
Juvenal Araujo
Julie Agnes-Sparks
Bowen Chen
*:not(.content-image-wrapper)]:tablet:col-span-12 [&>*:not(.content-image-wrapper)]:desktop-sm:col-span-7 [&>.interactive-diagram-component]:tablet:col-span-12 [&>.interactive-diagram-component]:desktop-sm:col-span-8 [&>form-wrapper]:tablet:col-span-12 [&>form-wrapper]:desktop-sm:col-span-8 [&>.expressive-code]:tablet:col-span-12 [&>.expressive-code]:desktop-sm:col-span-8 [&>.table-component]:tablet:col-span-12 [&>.table-component]:desktop-sm:col-span-8 [&>.dato-code-block-wrapper]:tablet:col-span-12 [&>.dato-code-block-wrapper]:desktop-sm:col-span-8 [&>.dast-content]:col-span-full"> *:not(.content-image-wrapper)]:tablet:col-span-12 [&>*:not(.content-image-wrapper)]:desktop-sm:col-span-7 [&>.dato-code-block-wrapper]:desktop-sm:col-span-8 [&>.table-component]:desktop-sm:col-span-8" data-astro-cid-twmmywjp> Source code management (SCM) and CI/CD pipelines have become the industry standard for automating software delivery. But from the time a code change enters your SCM until it’s deployed, it’s susceptible to changes and reconfigurations that can go so far as to modify the pipeline itself. If you’re not proactively securing your CI/CD system, attackers can use it to grant themselves permissions, access secrets, and ship malicious code.
In this blog series, we’ll first cover possible attack paths using a threat matrix based on the MITRE ATT&CK® framework that is specifically mapped to CI/CD systems. We’ll also provide you with a mental framework , known as a threat model, with the goal of understanding how your system would respond to these different attack pathways and what detection methods you can implement to mitigate them.
In Part 2 , we’ll put these ideas into practice by threat modeling GitHub as an SCM tool. We’ll also take a look at historical attacks on GitHub environments and the detection opportunities you can leverage to secure them.
What is CI/CD security? 
CI/CD security refers to integrating security tools and best practices into your CI/CD pipeline to better prevent, detect, and respond to attacks that target your pipeline’s trust boundaries. This includes access to secrets, configuration files, artifact delivery, and other sensitive inputs and data.
Securing the CI/CD trust boundary involves three main components:
The SCM tool acts as the central repository for version control. Because it triggers the pipeline and hosts configuration files (pipeline-as-code), it acts as a critical trust boundary. Examples include GitHub, GitLab, and Bitbucket.
Continuous integration (CI) automates the building and testing of code changes and integrates them into a shared repository of binaries or artifacts. Examples include Jenkins, GitHub Actions, GitLab CI/CD, CircleCI, and Azure DevOps.
Continuous deployment (CD) automatically deploys validated code changes to production. CD is often packaged into CI tools, including many of the previously listed examples. Dedicated CD tools include AWS CodeDeploy and Argo CD.
*:first-child]:bg-white block tablet:p-9 desktop-sm:p-12 rounded-3xl bg-white max-h-[calc(100vh-6rem)] overflow-y-auto" data-astro-cid-d4yttbaw> Close dialog 
Typically, SCM tools are not considered to be part of the CI/CD pipeline. However, most modern CI/CD systems are defined using configuration files (such as `.github/workflows/*.yml`) stored in the SCM repository. Since these files and scripts directly influence what the pipeline executes, in this blog we will be including the SCM within our CI/CD security boundary. 
Pushing code changes to SCM tools, which trigger automated builds, tests, and deployments, is commonplace in our delivery workflows. But what happens when this workflow becomes compromised?
From an attacker’s viewpoint, gaining write access to your SCM tool allows them to view and tamper with your source code, transitively access tools with elevated permissions, and misconfigure your CI/CD pipeline to ship malicious code under the guise of normal commits. Acquiring this access is often easier than you might think. It can occur via compromised developer credentials—especially if your SCM access policies are overly permissive—or through third-party integrations. These vulnerabilities often serve as an entry point for supply chain attacks such as the Shai-Hulud worms covered in our Datadog Security Labs research blog.
In the next section, we’ll discuss how attackers can compromise your software delivery pipeline using a MITRE-style threat matrix that we’ve compiled to cover the CI/CD threat landscape.
The threat matrix for CI/CD security 
MITRE ATT&CK is a framework that documents observed tactics and behaviors used by adversaries. It groups these techniques by their occurrence at different stages of an attack. Each cell within the matrix represents an approach used by attackers for a given tactic (the corresponding column)—for example, “Implant Internal Image (T1525)” as a method of persistence.
Normally, the MITRE ATT&CK Matrix encompasses all known cyberattacks agnostic of technology. However, we’ve compiled a threat matrix that specifically focuses on attack pathways limited to CI/CD systems. This matrix is based on historical attacks, our own security practices at Datadog, as well as third-party sources such as Hiroki Suezawa’s threat matrix for CI/CD pipelines , the Microsoft DevOps threat matrix , and the OWASP top 10 CI/CD security risks .
Reconnaissance Initial Access Execution Persistence Privilege Escalation Defense Evasion Credential Access Lateral Movement Exfiltration Impact Scan CI/CD infrastructure Public repositories Connect to CI/CD pipeline resources Compromise CI/CD server Access higher privilege accounts Compilation manipulation Access cloud metadata (Monorepo) Get credentials to different folders Clone Git repositories Cryptomining via pipeline resources Collect info from public repositories Systems with unpatched vulnerabilities Dependency tampering Dependency tampering Push code from pipelines to protected branches Impant CI/CD runner images Env variables stored in CI/CD Compromise build artifacts Exfiltrate data from production envs Denial of service on local CI/CD pipelines Extract CI workflows or repo settings using PRs Compromise CI/CD supply cahin Modify production application images Implant Ci/CD runner images Create higher privilege accounts Modify CI/CD caches Fetch credentials from a vault Exploit other internal resources unrelated to CI/CD Exfiltrate pipeline logs Denial of service on non-CI/CD resources Valid CI/CD user account Inject code to IaC configuration Inject code to IaC configuration Reconfigure branch protections Read credentials file Compromise other CI/CD pipelines from privileged escalation Downstream poisoning Valid Git account Inject code to source code Inject code to source code Manipulate service logs Registry injection Run a DDOS against 3rd parties using pipeline resources Valid admin account for underlying compute resources Modify CI/CD configurations Modify CI/CD configurations Webhooks that trigger actions or configuration changes Modify the configuration of production environments Create new accounts or applications 
Using the threat matrix, you can map out the most expected attack paths and apply them when threat modeling or assessing the countermeasures your systems have in place. For example, consider the following attack path:
Reconnaissance: An attacker scans your organization’s public code repositories to identify entry points into your CI/CD system.
Initial access: They find a vulnerable permissions configuration that enables them to execute code within the CI when submitting a pull request. (CI runs on PRs with write permissions). They open a PR to your organization’s public repository.
Execution: The PR includes a malicious change to your pipeline configuration file (e.g., .gitlab-ci.yml ).
Credential access: The configuration change enables the attacker to read sensitive information stored in your CI environment, such as your GitHub token, AWS access key ID, AWS secret access key, and other environment variables.
Exfiltration: This information then enables them to access private repositories and exfiltrate proprietary code and production data.
Impact: For additional profit, the attacker uses the exfiltrated cloud credentials to deploy cryptomining workloads.
Threat modeling for CI/CD 
When working to secure applications, systems, or other parts of your environment that contain sensitive information and processes, it’s important to establish a threat model. A threat model is a structured representation of everything that pertains to the security of the object that you’re attempting to secure. This includes the existing system, potential threats to the system, and how the system is poised to respond to these threats.
Using the CI/CD threat matrix, you can map different attack paths onto your existing system to identify weak trust boundaries and gaps in security coverage. There are many methods for threat modeling, such as this process outlined by OWASP . In our case, we’ll use a simplified detection-based threat model method based on this guidance from the NCSC , with the goal of ideating detections for different attack pathways.
Inputs: What are the inputs, personas, and infrastructure within and interacting with our system?
Risks: What’s at risk if an attacker controls these inputs (or previously inputted data)?
Attack: How can an attacker materialize these risks? (Refer to the CI/CD threat matrix.)
Log source: What logs can help confirm that an attack is happening?
Detection: How can we ideate detection workflows based on the attack pathway, identities, and relevant log sources?
Identify threats to your CI/CD systems 
In this post, we discussed the main components within the CI/CD trust boundary and covered how to map out potential attack vectors using a CI/CD threat matrix. Datadog’s security offerings can help you detect compromised credentials and attempts to exfiltrate sensitive data. Check out our Cloud Security documentation to learn more.
In the next part of this series , we’ll take a deeper dive into how you can better secure GitHub and GitHub Actions. We’ll apply the threat model discussed here to a GitHub environment to develop specific detection methods. We’ll also analyze historical attacks on GitHub ecosystems and discuss steps you can take to safeguard your environment from these attacks.
To see how you can start identifying threats and securing your own CI/CD pipelines, sign up for a free 14-day Datadog trial .
g>rect]:fill-grey-500 [&_path]:!fill-white w-7 h-7 tablet:w-8 tablet:h-8 desktop-sm:w-9 desktop-sm:h-9 group-hover:[&>g>rect]:fill-black">
g>rect]:fill-grey-500 [&_path]:!fill-white w-7 h-7 tablet:w-8 tablet:h-8 desktop-sm:w-9 desktop-sm:h-9 group-hover:[&>g>rect]:fill-[#FF4500]">
g>rect]:fill-grey-500 [&_path]:!fill-white w-7 h-7 tablet:w-8 tablet:h-8 desktop-sm:w-9 desktop-sm:h-9 group-hover:[&>g>rect]:fill-[#0A66C2]">
Part 1 CI/CD security: threat modeling using a MITRE-style threat matrix
&]:border-purple-600 active:border-purple-600 [.active>&]:text-purple-600 group-has-[.active]:text-purple-600 group-has-[.active]:border-purple-600 active:text-purple-800 [.active>&]:font-bold group-has-[.active]:font-bold group-has-[.active]:hover:border-purple-700 group-has-[.active]:hover:text-purple-700 [.active]:hover:border-purple-700 [.active>&]:hover:text-purple-700 [.active]:active:border-purple-800 [.active>&]:active:text-purple-800">
What is CI/CD security?
&]:border-purple-600 active:border-purple-600 [.active>&]:text-purple-600 group-has-[.active]:text-purple-600 group-has-[.active]:border-purple-600 active:text-purple-800 [.active>&]:font-bold group-has-[.active]:font-bold group-has-[.active]:hover:border-purple-700 group-has-[.active]:hover:text-purple-700 [.active]:hover:border-purple-700 [.active>&]:hover:text-purple-700 [.active]:active:border-purple-800 [.active>&]:active:text-purple-800">
The threat matrix for CI/CD security 
&]:border-purple-600 active:border-purple-600 [.active>&]:text-purple-600 group-has-[.active]:text-purple-600 group-has-[.active]:border-purple-600 active:text-purple-800 [.active>&]:font-bold group-has-[.active]:font-bold group-has-[.active]:hover:border-purple-700 group-has-[.active]:hover:text-purple-700 [.active]:hover:border-purple-700 [.active>&]:hover:text-purple-700 [.active]:active:border-purple-800 [.active>&]:active:text-purple-800">
Threat modeling for CI/CD 
&]:border-purple-600 active:border-purple-600 [.active>&]:text-purple-600 group-has-[.active]:text-purple-600 group-has-[.active]:border-purple-600 active:text-purple-800 [.active>&]:font-bold group-has-[.active]:font-bold group-has-[.active]:hover:border-purple-700 group-has-[.active]:hover:text-purple-700 [.active]:hover:border-purple-700 [.active>&]:hover:text-purple-700 [.active]:active:border-purple-800 [.active>&]:active:text-purple-800">
Identify threats to your CI/CD systems
Part 2 CI/CD security: How to secure your GitHub ecosystem
Close feedback prompt 
Did you find this article helpful?
Article thumbs up 
Article thumbs down 
Further reading 
White Paper: DevSecOps Maturity Model
Get a blueprint for assessing and advancing your DevSecOps practices.
Download to learn more Related jobs at Datadog We're always looking for talented people to collaborate with Featured positions
We have positions
View all Start monitoring your metrics in minutes find out how
