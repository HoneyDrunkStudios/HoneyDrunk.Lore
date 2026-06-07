---
source: "https://docs.unity.com/en-us/cloud/automation/basic-concepts"
title: "Basic concepts - Unity Pipeline Automation"
author: "Unity Docs"
date_published: "2026-06-04"
date_clipped: "2026-06-07"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# Basic concepts - Unity Pipeline Automation

Source: https://docs.unity.com/en-us/cloud/automation/basic-concepts

Unity Cloud Documentation Unity Pipeline Automation (beta) Basic concepts This page provides an overview of the key elements of Unity Pipeline Automation. Read time 4 minutes Last updated 3 days ago Unity Pipeline Automation is a tool that helps you to create, trigger, and monitor RT3D pipelines using services and technology made by Unity and key third parties.
You can achieve all of this from our web app but also extend that functionality using our web API.
Below are basic concepts that will help you better understand how Pipeline Automation works. 
Apps 
To get started, identify the processes or workflows you want to automate.
The scope of automation depends on the tools and services available in the Pipeline Automation service through apps.
An app is a single tool or service, such as Unity Asset Transformer or Unity Asset Manager. The list of available apps will expand over time. 
Actions 
Apps contain actions that integrate with the tool or service they represent. These actions are executed in pipeline steps.
For example, the Asset Manager app has an action that enables you to upload files to an asset in Asset Manager.
You can combine actions from different apps in your pipeline. 
You can configure an action's behavior using its input parameters, which can reference data within your pipeline.
When an action completes, it provides output parameters which can be referenced by subsequent steps in the pipeline.
For example, you can configure Unity Asset Transformer to ingest a specific asset for transformation and then reference the transformed output file. 
Actions are versioned to ensure updates from app creators don’t break your pipelines.
For example, if an action is updated to have a new required input parameter, your pipeline will continue to use the older version to function as expected. 
Some actions require compute resources and can be configured to use a hardware profile that's appropriate for your pipeline.
For small assets, choose a profile with low memory capacity. For larger assets, select one with higher memory capacity. 
Events 
Apps also contain events that integrate with the tool or service they represent. Pipeline Automation triggers a pipeline when an event is detected.
You can filter events to trigger only in specific scenarios. Events contain output parameters related to what occurred in the event and you can trigger a pipeline using this information.
For example, the Asset Manager app has an event for when a new asset is created. You can configure it to trigger only for a specific project and use the event details about the asset creation to run a pipeline. 
Pipelines 
Pipeline Automation mainly involves creating pipelines that perform a set of actions in your development process when triggered. You can automate pipelines to reduce repetitive tasks, minimize human error, and scale operations.
Pipelines have names, descriptions, and are versioned to prevent breaking changes with integrations.
You can trigger pipelines in the Pipeline Automation web app, by API, on a schedule, or when an app detects an event.
All members of your Unity organization can run pipelines, but only Automation Developers can create them. 
The following are a few examples of pipelines: 
Optimize 3D assets for VR 
Create a build from a version control repository and deploy it to test 
Pipeline parameters 
When a pipeline is triggered, it may require certain parameters to be passed to it.
Pipeline parameters enable your pipelines to be more flexible, dynamic, and reusable.
If you have a pipeline that converts 3D models to a specific format like .glb , you could instead consider having a pipeline parameter for users to specify a file format to convert the model to.
Pipeline parameters can be referenced by any step within the pipeline. 
Steps 
Pipelines consist of steps. A step runs an action from an app and specifies how and when to run it. You can also use steps to run other pipelines or suspend the pipeline until you resume it again. 
Action input parameters 
When you select an action for a pipeline step, you must provide its required input parameters for successful execution.
For example, when using Unity Asset Transformer to transform an asset, you must specify the asset's file location so that Unity Asset Transformer can import it.
Parameters can be static values, dynamic values that reference other parameters, or a combination of both. 
Step dependencies 
You can configure a step to run after certain other steps within the same pipeline have completed their execution.
This flexibility enables pipelines to be structured as Directed Acyclic Graphs (DAGs).
You can configure pipelines to have sequential steps, parallel steps, and groups of steps. 
Hardware resources 
If an action requires hardware resources, then it will provide a set of hardware profiles for various use cases.
A hardware profile specifies limits for the following resources: 
CPU type and number of cores 
GPU type and number of cores 
Amount of memory 
Automations 
An automation automatically triggers one of your pipelines either on a schedule or when a certain event occurs under the right conditions.
You can toggle automations on or off, if you do not want them to automatically run.
Only members with the Automation Developer role can create automations. 
To create an automation: 
Choose a trigger type. 
Select a pipeline to trigger. 
Provide the required pipeline parameters. 
Trigger on a schedule 
You can configure an automation to run on a schedule that follows the cron format .
For example, you can run a CI/CD pipeline daily at midnight. 
Trigger when an event occurs 
You can configure an automation to run when a certain event occurs in an app.
Events contain output parameters which can be referenced when configuring the pipeline parameters in the automation.
For example, when a new asset is created in Asset Manager, the event provides details about this asset that can be passed to one of your asset pipelines. 
Automation bot 
Automation bots are service accounts that help Automations to trigger pipelines configured to run on a schedule or when an event is detected. The service account must have the organization or project roles and permissions required to perform Unity-related actions in the pipeline. For example, for an automation bot to perform Asset Manager actions across projects, you can assign the Asset Manager Admin organization role to its service account. 
Jobs 
When a pipeline is triggered it creates a new job using the provided pipeline parameters.
The job executes the steps defined in the pipeline. Jobs have statuses that indicate their current states, such as, running, finished, or failed.
They also contain details about the pipeline parameters used to trigger it, as well as the output data. 
Job steps 
When a job executes pipeline steps, it generates logs for debugging. Each step has a status that represents its current state, such as running, finished, or failed. Job steps contain details about the parameters used to run it, as well as the output data. 
Job File Storage 
A shared temporary file storage is automatically mounted at the start of each job. Actions can use this storage to create various RT3D artifacts such as 3D models, images, and JSON files. Actions can also use storage to download files, so tools like Unity Asset Transformer and Blender can ingest and process them.
When the job ends, this temporary file storage is unmounted and its contents are purged. To preserve files after the job completes, transfer them to another system such as Asset Manager, Unity Version Control, or an S3 bucket. 
Some actions require input parameters that point to a file location. This refers to the temporary file storage created for the job. To determine the correct value, check if a previous action provides an output parameter with a file location you can use. For example, to import a file into Blender you can point to an output parameter of a file downloaded from Asset Manager. Copyright © 2026 Unity Technologies Legal Privacy Policy Cookies Do Not Sell or Share My Personal Information Your Privacy Choices (Cookie Settings) "Unity", Unity logos, and other Unity trademarks are trademarks or registered trademarks of Unity Technologies or its affiliates in the U.S and elsewhere ( more info here ). Other names or brands are trademarks of their respective owners.
Some pages are machine-translated for convenience, and may contain inaccuracies. In the event of conflicting information, the English version is authoritative.
