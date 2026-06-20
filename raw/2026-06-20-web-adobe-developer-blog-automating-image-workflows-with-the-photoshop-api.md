---
source: "https://blog.developer.adobe.com/en/publish/2023/05/automating-image-workflows-with-the-photoshop-api"
title: "Automating Image Workflows with the Photoshop API"
author: "Adobe Developer Blog"
date_published: "unknown"
date_clipped: "2026-06-20"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# Automating Image Workflows with the Photoshop API

Source: https://blog.developer.adobe.com/en/publish/2023/05/automating-image-workflows-with-the-photoshop-api

Automating Image Workflows with the Photoshop API 
Recently we discussed how developers could make use of the Photoshop API . In that post, we shared a simple Node.js script that would call one of the APIs using a file stored in Azure. It was simple — get an access token, start an API job with an input document, poll for completion, and then check the result. Simple is good though as it means it’s easy to integrate into custom workflows. In today’s post, we’ll do just that.
Our workflow 
Let’s begin by defining what our workflow is going to do. Imagine we are using a cloud storage provider, in this case, Dropbox, to store photos. Our workflow is going to monitor this folder and trigger when new pictures are added.
When the picture is added, we will grab the file and send it to an endpoint that runs the Lightroom “AutoTone” feature. This feature attempts to correct exposure, contrast, and other issues in photos. As an example (that we stole right from the docs ), here’s a before and after showing the impact of the corrections:
︎
Once the API is done, we will then store the result in another folder in Dropbox. We could overwrite the original, but most likely people will want both copies so they can make a final check to see which they prefer.
The worfklow platform 
For our workflow, we will use Pipedream . Pipedream is a low-code/no-code solution for building generic workflows. It’s in the same space as Microsoft PowerAutomate and Workfront Fusion. (And you can expect to see examples from us soon on those platforms as well.) Pipedream really helps developers by making the more difficult, or even boring, aspects of a project “plug and play”. As an example, when defining what starts a workflow, a trigger, Pipedream comes with a huge set of pre-built code blocks. When we start demonstrating how we built our workflow, you’ll see that in action. Pipedream has a free tier so those of you reading who want to follow along can do so after signing up.
If you’ve never used Pipedream before, check out their excellent Pipedream University for an introduction to how it works. They also have excellent docs . Finally, your friendly author here has written about Pipedream as well.
With that out of the way, let’s get building!
Step one — The trigger 
Pipedream workflows start with a trigger that represents the “event” that should kick off our process. Pipedream has many, many of these triggers built-in (and you can write your own), and luckily, a “New File” in Dropbox trigger is supported:
︎
After selecting the “New File” trigger, you are given a simple interface to configure it:
︎
On top is the authentication aspect. Here you can connect Pipedream to your Dropbox account. Best of all, once you’ve done that one time, you can reuse that connection in multiple workflows.
Next, make note of the Path value. You can type in here and Pipedream will attempt to autocomplete based on your account, or simply enter a path. We’re going to use /PSAPI_Input as the folder that expects to get images.
The next two settings can be ignored, but the final setting, Include Link , should be toggled to true. We're going to need that link so we can tell the API how to fetch the data.
Here’s the final configured trigger for our workflow:
︎
To recap, at this point we’ve configured the workflow to fire automatically as soon as a file is added to a particular folder in our Dropbox account.
Step two — Get an upload URL 
When the Photoshop API runs, it expects at minimum two things — an input URL and output URL. Basically, where to read it’s input and where to store the result. Our input is going to be the new file added to Dropbox. Our output is going to be the location of the image corrected by Lightroom.
To support this, we need to ask Dropbox to generate a special URL that can be used to store data. Pipedream has a lot of Dropbox actions built in, but unfortunately does not have this particular one. Fortunately, Pipedream does let you create a step with custom code where it’s already handled the authentication for you. Remember that in the trigger, we specified an existing Dropbox account. Because we did this, we can then write code and let Pipedream handle authentication.
By consulting the Dropbox API , we find the get_temporary_upload_link endpoint which is exactly what we need.
In Pipedream, we add a new step and select “Use any Dropbox API in Node.js”. This gives us boilerplate code hitting one sample endpoint:
https://gist.github.com/cfjedimaster/867a554f8f046ac357c89ae156441aae#file-script-js 
Most importantly — note the authentication information is automatically provided. All we need to do then is to edit the endpoint and set our input:
https://gist.github.com/cfjedimaster/cf4932ba1d66887a7a75e3a5e9169d0e#file-script-js 
Note we are using a path that’s a different folder, /PSAPI_Output . The value after that, ${steps.trigger.event.name} , demonstrates using information from earlier in our workflow, specifically the filename of the event that triggered our workflow, the name of the file itself.
The code ends by returning the result of the API call, which in our case is going to be a special URL we can use with our API call.
Step three — Getting an access token 
In our previous blog post , we discussed how to get credentials for the Photoshop API and how then to use them in code to get an access token. In Pipedream, we can add a step to our workflow to run custom code. You saw that in the previous step when we hit the Dropbox API. Pipedream supports both Node.js and Python so you’ve got a few options there. We will add a new code step and name it getAccessToken . This step will be responsible for using our credentials to generate a JWT and exchange that for an access token.
In that previous blog post, the code made use of the @adobe/jwt-auth package to simplify the process. However, this package does not work as an ES6 import which Pipedream supports. Luckily we can swap out to another NPM package, jsonwebtoken . Let’s take a look at the code:
https://gist.github.com/cfjedimaster/54fbfc2c4a8e90ffda5f6007ddb13714#file-script-js 
So a couple of things here. First, every Node Pipedream code step uses a form like so:
https://gist.github.com/cfjedimaster/a12dd06e92a801ae7572616709f04303#file-script-js 
The run function is called automatically and passed data from any previous steps as well as a handler ( $ ) for other operations we won't need. Basically, we will put our imports on top and our logic inside.
You can see a set of variables being copied from the environment as — not surprisingly — Pipedream lets us define custom environment variables as well.
The next block of code generates our JWT. This is mostly boilerplate but pay special attention to the jwtOptions part. This variable, "https://ims-na1.adobelogin.com/s/ent_ccas_sdk": true, , is what sets the scope for our token and is required to work with the APIs.
After the JWT is created, it can be sent to a generic Adobe endpoint to generate an access token. The final bit of logic is to return that token. If you remember in the previous step, anything we return can be used later. You’ll see this in action soon.
Step four — Calling the Lightroom Autotone API 
Now it’s time to get down to business. Our trigger gave us a link to the new image. The next code step generated a link for us to upload the final result. We then got an access token. We’ve got everything needed to start the process. Once again we’ll add a Node.js step to our workflow. Here it is in action.
https://gist.github.com/cfjedimaster/605a25a51602bd91eaeafb0bbd68d02a#file-script-js 
The Autotone API requires a few parameters, in this case, an input and output value. In our case, we pass in the link from the trigger and the special upload URL generated earlier.
And that’s it! The result of this call is a link to the job which we return at the end.
Step five — Do nothing 
Ok, not exactly nothing , but here’s an interesting question. This entire workflow runs automatically with no human interaction. The previous step kicks off a process that, when done, will save the result to Dropbox. Do we need to do anything else? Not really. It’s absolutely possible the API may fail for some reason. It’s possible something else could go wrong as well. It’s also possible we may want to alert someone about the change, perhaps via email. Honestly, it’s up to you.
In our sample workflow, we decided to simply check the job and wait for it to finish. Here’s that code step, and it’s pretty similar to our previous blog post. We check the job, wait, and check it again.
https://gist.github.com/cfjedimaster/207617f3a824c5cb6ef22f43983a9a1b#file-script-js 
This is where we end the workflow, but we could, and probably should, add logic to check the result of the job and do something. Perhaps on a good result, we do nothing, but on error, we then send an email. (And by the way, Pipedream makes sending emails ludicrously easy.) What’s nice though is that we can decide that later.
One really nice feature of Pipedream is that it makes it easy to check when workflows have run. For example, here’s a list of past executions:
︎
The errors you see there came from me playing with the API and figuring out how it worked. You can also click on any of them and see the data that flowed throughout it.
The result 
With the workflow in place, we uploaded a new image to a Dropbox folder, watched the workflow firing in an open tab, and when done, checked the result. Here’s before:
︎
And here’s after:
︎
The result is crisper, and absolutely an improvement! You can create your own copy of my workflow here: https://pipedream.com/new?h=tch_3xxfJA . If you want to learn more, visit our docs and share what you’ve built!
