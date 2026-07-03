---
source: "https://blog.developer.adobe.com/en/publish/2023/10/integrating-the-photoshop-api-with-python"
title: "Integrating the Photoshop API with Python"
author: "Adobe Developer Blog"
date_published: "2023-10-09"
date_clipped: "2026-07-03"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# Integrating the Photoshop API with Python

Source: https://blog.developer.adobe.com/en/publish/2023/10/integrating-the-photoshop-api-with-python

Integrating the Photoshop API with Python
How Python can interact with our powerful Photoshop API
︎
The
Photoshop API
is an incredibly powerful REST-based API for performing Photoshop tasks in the cloud and at scale.
I’ve been demonstrating its features on our blog over the past few months, generally using Node.js, but the API’s simplicity makes it available for any platform out there.
In this article, I’ll share an example of how Python can be used to interact with the Photoshop API. As a warning, I’m fairly new to Python, but one of the best aspects of the language is just how easy it is to pick up and start using it right away.
If you haven’t already done so, grab your
free trial credentials
so you can play with the API yourself. With that, let’s get started!
How the Photoshop APIs Work
In general, working with the different parts of the Photoshop APIs involves much the same steps:
Convert credentials into an access token
Determine input and output URLs (as the APIs work with cloud storage, this will depend on your storage system and their SDKs)
Call the API endpoint, passing in your URLs and other arguments required for that particular service
Check the result of the API call on a schedule to determine the status of the job
So Let’s break these down into individual Python examples.
Getting the Access Token
Again, assuming you have your credentials, getting an access token is as simple as a call to Adobe’s
ims
endpoint. Here's an example:
https://gist.github.com/cfjedimaster/d1c013dff6d4da8145fc39472e6e5dc3#file-plain-txt
Note that the assumption is that the credentials,
CLIENT_ID
and
CLIENT_SECRET
are available in environment variables. Running this script will dump out the result of the call:
https://gist.github.com/cfjedimaster/f88aa95f38f3fb8b9c562c0f1b209929#file-plain-txt
Typically you can just work with the
access_token
result of the call.
Testing the Access Token (Optional)
The next step is completely optional, and not generally recommended in production, but it may be a good idea while learning and testing.
The Photoshop API provides a method that
only
verifies the access token. This is handy as other calls will require working with cloud storage. The
hello
endpoint will do simply that: echo back a greeting if you've correctly performed authentication. Let's update the Python call with a new function testing that,
sayHello
:
https://gist.github.com/cfjedimaster/f79f7c3255ab606a537d570b4edfa541#file-plain-txt
All of our API calls will require two headers for authorization. The first,
Authorization
, includes the access token returned from the earlier request, while
x-api-key
uses the
CLIENT_ID
value from our credentials.
The result of this script is simply:
Response from hello endpoint: Welcome to the Photoshop API!
Starting a Job
The next thing to do is start a job of some sort. The Photoshop API has
many
features, but for today, let’s consider the
Remove Background
API which, you guessed it, removes the background from an image.
In order to do this, we need both a source for our input and a place to store the output.
The Photoshop APIs support cloud storage on Amazon S3, Dropbox, and Azure, and the particularities of each depend on their SDKs. For today, let’s just consider a simple S3 bucket. The Photoshop API team created a nice
Python demo
I can borrow from to simplify making those S3 URLs using the Python
boto3
package.
Let’s look at our updated script:
https://gist.github.com/cfjedimaster/6d8aa8897200329af4f630d187979934#file-plain-txt
There are two big changes here. First note the use of
get_presigned_url
. This lets us create a readable URL for our source image as well as a writeable URL for the output. You can see that towards the bottom of the script where
inputURL
and
uploadURL
are created.
Next, the
create_removebg_job
function is called with our credentials and URLs. In that function, look at
data
. This information is passed to the API and defines how it should operate. In general, every single part of the API will be a version of this, with just the parameters changing based on what operation is being used.
The end result of this call is a
job
that looks like this:
https://gist.github.com/cfjedimaster/406d5fc0f3585f051cfba20b9b7a9032#file-plain-txt
Checking Job Status
For the final part of our sample code, let’s check the job and keep checking it until it finishes.
Technically, you don’t need to do this in the same script. You could, for example, store the job result in a database and use a scheduled process to check the result at a later time. Since the “typical” call to the Photoshop API will finish rather quickly, it isn’t too difficult to add it to our script.
In the code sample below, I’m only sharing the portion where the job is created and how polling for the result is handled. All the code before this portion is the same as before:
https://gist.github.com/cfjedimaster/14d7b790ba86745d436a6baa964e43e6#file-plain-txt
Now we’re taking the URL from the job creation call and continuing to call it until the status of the response is either good or bad. In that loop, the response is also bring printed out. Here’s an example of what that looks like when done:
https://gist.github.com/cfjedimaster/73da087ab04cc918a148f59319a30835#file-plain-txt
Next Steps
If you would like to play with this code, you can find it on my repository here:
https://github.com/cfjedimaster/photoshop_api_preso/tree/main/demos/python
. Also, you can find a notebook version of it
here
, but be sure to note the requirements for credentials at the top.
Let us know how this works for you, and reach out on our
forums
with any questions!
