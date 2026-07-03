---
source: "https://vercel.com/blog/dockerfile-on-vercel"
title: "Run any Dockerfile on Vercel"
author: "Vercel"
date_published: "2026-06-30"
date_clipped: "2026-07-03"
category: "DevOps & CI/CD"
source_type: "web"
---

# Run any Dockerfile on Vercel

Source: https://vercel.com/blog/dockerfile-on-vercel

You have a server in a container. Maybe it's a Go service, a Rails app, a Spring Boot API, or a web server behind nginx. It speaks HTTP. It listens on a port. It just needs somewhere to run.
Add a
Dockerfile.vercel
file to your project, and Vercel builds, stores, deploys, and autoscales the image on
Fluid compute
, so you pay only for the CPU your code uses. No daemon to run locally, registry to set up, or cluster to babysit.
Copy link to heading
How it works
Here is a small HTTP server in Go, listening on
$PORT
:
main.go
package
main
import
(
"fmt"
"net/http"
"os"
)
func
main
(
)
{
port
:=
os
.
Getenv
(
"PORT"
)
if
port
==
""
{
port
=
"80"
}
http
.
HandleFunc
(
"/"
,
func
(
w http
.
ResponseWriter
,
r
*
http
.
Request
)
{
fmt
.
Fprintln
(
w
,
"Hello from a container on Vercel 👋"
)
}
)
http
.
ListenAndServe
(
":"
+
port
,
nil
)
}
A minimal HTTP server that reads its port from $PORT and answers every request.
Add a
Dockerfile.vercel
file that builds it into a small image and runs it:
Dockerfile.vercel
FROM
golang:1.24-alpine
AS
build
WORKDIR
/src
COPY
. .
RUN
go build -o /server main.go
FROM
alpine:3.20
COPY
--from
=
build
/server /server
CMD
[
"/server"
]
A two-stage build that compiles the binary, then copies it into a minimal Alpine image that runs on boot.
Then deploy:
▲ vercel deploy
Vercel CLI
✓ Building image from Dockerfile.vercel
✓ Stored image
in
your project's registry
✓ Deployed to Fluid compute
Production: https://my-server.vercel.app
One command builds the image, stores it, and ships it to Fluid compute, then prints the production URL.
That is it. Two files, and you are live. Every
git push
rebuilds the image and hands you a fresh preview URL. Or run
vercel
to deploy without committing.
We used Go in this example, but any stack works. Rails, Spring Boot, Express, Laravel, ASP.NET, FastAPI, and a web server behind nginx all deploy the same way. The only rule is that your server listens on
$PORT
, which defaults to
80
. If it speaks HTTP, it deploys. Yes, even Java. And yes, even PHP.
Copy link to heading
What you get
A container on Vercel is a first-class citizen. It runs on the same platform, and the same compute, as your frontend and the rest of your
services on Vercel
.
A preview deployment for every push:
Every commit gets its own immutable URL you can open, share, and roll back to.
Autoscaling, in both directions:
Traffic arrives and you scale out. Traffic stops and your instances wind down. You never size a fleet or guess a concurrency number.
Active CPU pricing
: Fluid compute bills for the time your code is actually running, so an idle server, parked on a slow query or an upstream API, isn't burning CPU while it waits. You pay for execution time, not wall time.
Observability, included:
Logs, traces, and metrics for your container live in the same dashboard as everything else you ship.
One project, one domain:
Your container sits beside your frontend and your other services and talks to them privately over the Vercel network. Your full stack ships as one deploy.
Copy link to heading
Built to start fast
A container is only as good as the time it takes to answer its first request.
When Vercel builds your image, it stores it as an
optimized boot image
, a compressed snapshot of the container's disk tuned for fast startup.
When a container boots, we stream that snapshot and decompress it on demand, rather than downloading the whole image before anything runs. Your server can start handling requests before the full image is in place, so a larger image does not have to finish downloading first.
Once an instance is running, Fluid compute keeps it warm and serves many requests from it, rather than starting a fresh copy for each one. You get the responsiveness of a warm server and the bill of one that sleeps when idle.
Each container is a stateless process: it takes a request, returns a response, and keeps nothing in between. Persistent state lives in a backing service you attach, like a database or cache from the
Vercel Marketplace
. Because an instance holds nothing that has to survive, Vercel can add instances when traffic arrives and retire them when it stops. We're also working on shipping durable storage attached to containers soon.
Copy link to heading
Why now?
Our
first platform
let you deploy a Dockerfile with a single command. That was a decade ago, and the idea was right, but the infrastructure to make it great didn't exist yet.
We've spent the years since building the primitives to handle it well. They power everything you run on Vercel: Builds, Functions, Sandboxes, and now containers. It all scales with traffic, and you only pay for the CPU you use. A container is now a first-class citizen, running on the same system as everything else.
Framework detection is our front door. When we recognize your framework, we read your code and
derive the infrastructure your app needs
, because the code already describes what it should do. For most apps it's the fastest way to ship. A Dockerfile is for everything else: a service that needs a system library like FFmpeg or Chromium, a framework we do not auto-detect yet, or an app you want to bring exactly as it already runs. It is the universal way to say how a program should be built, so when there is no framework to read, we meet it directly.
Everything around your Dockerfile is zero configuration. You point at the image, and the build, the registry, the rollout, the scaling, and the URL all just happen.
Copy link to heading
Backends are back
Your backend now ships the way your frontend does: one push, one preview, one platform. We can't wait to see what you build.
Read the docs
or
deploy an example
to get started.
