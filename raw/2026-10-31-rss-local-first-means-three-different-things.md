---
source: "https://hologram.page/blog/local-first-means-three-different-things"
title: "Local-First Means Three Different Things"
author: "Bart Blast"
date_published: "2026-10-28"
date_clipped: "2026-10-31"
category: "Software Architecture"
source_type: "rss"
discovered_via: "https://tldr.tech/dev/2026-10-29"
---

# Local-First Means Three Different Things

October 28, 2026

# Local-First Means Three Different Things

Bart Blast
Creator of Hologram

Before getting into definitions, here's what local-first feels like. Play with the two devices below for a minute. Add something on the first one. Then switch it offline and keep going. Change something on the second device too, then bring the first one back online.

Device 1

- Renew the passport
- Book the flights

Synced

Server

Device 2

- Renew the passport
- Book the flights

Synced

Nothing waited for a server. The first device didn't care that the network was gone, and when it came back, both ended up with the same list. A server was still in the middle, though. Every change went through it and its copy had the last word, which isn't how local-first was first described. More on that below.

That's what local-first means to me, and to most of the sync engines you'll run into. It's also only one of the meanings the word carries. Ask five developers what it means and you'll get at least three different answers. I've spent most of this year designing a local-first data layer, and talking about it is still harder than building it. Everyone uses the word for something different, and when I describe what I'm building, people hear whichever meaning they already have in mind. I touched on this in my [ElixirConf EU talk](https://youtu.be/qqpNovT7cys) in Málaga in April, before moving on to how sync engines work.

So this post is about that problem. Where the three meanings come from, why they split, and what local-first actually fixes.

## The Definition I Use

Local-first means your UI is never blocked by the network.

Your app reads from a local copy of the data. Writes land in that copy right away. The network works in the background, syncing changes with the server, your other devices and anyone else working on the same data, whenever it can. When it can't, you keep working.

My definition treats speed and offline as one problem, since no network is just the slowest network there is. It says nothing about who owns your data. Other people put offline or ownership at the center instead, and end up with a different definition.

## Three People, Three Meanings

### Ownership

The term comes from a 2019 essay by Martin Kleppmann, Adam Wiggins, Peter van Hardenberg and Mark McGranaghan at Ink & Switch, a research lab. It's called [Local-first software: You own your data, in spite of the cloud](https://www.inkandswitch.com/local-first/), and if you haven't read it, it's worth an evening.

It lists seven ideals, and the diagram further down shows all of them. The one the essay cares about most is ownership. Cloud apps hold your data hostage. Politely, but they do. If the company shuts down, changes the product or loses your account, your work goes with it. The essay asks for software where the copy on your device is the real one and the server is just another place it syncs to. Ideally one that can't even read what it stores.

### Offline

Then the sync engines picked up the word, and for most of them local-first means the app keeps working without a connection. On a plane, in a tunnel, in a hotel where the wifi technically exists.

The idea itself is older than the essay. Around 2013 there was an "offline-first" movement, built around tools like [CouchDB](https://couchdb.apache.org/) and [PouchDB](https://pouchdb.com/). There's a difference, though. Offline-first treats a lost connection as a problem to survive. Local-first doesn't treat it as special at all: the local copy is the main one, so being online or offline changes nothing.

### Speed

And then there's what most developers I talk to have in mind. Speed. You click, and the thing happens. No spinner, no "Saving...".

[Linear](https://linear.app/) did a lot for this one. People noticed it felt different from every other web app and went looking for why. Linear runs on a sync engine it built itself, with the data held on the client.

A regular web app. Every save waits for the server.

0/7

Data that lasts for decades
Security and privacy by default
You stay in control

The network is optional
Your data on all your devices
Seamless collaboration

No spinners

Click a circle to turn a meaning on or off

So when people argue about whether some tool is "really" local-first, they usually aren't disagreeing about the tool. They mean different things by the word.

## You've Probably Built Half of It Already

Here's the speed problem from the inside. Say you use [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/guides/optimistic-updates) and want adding a to-do to feel instant. The full version from its docs looks like this:

```
const addTodo = useMutation({
  mutationFn: (todo) => api.post("/todos", todo),
  onMutate: async (todo) => {
    await queryClient.cancelQueries({ queryKey: ["todos"] })
    const previous = queryClient.getQueryData(["todos"])
    queryClient.setQueryData(["todos"], (old) => [...old, todo])
    return { previous }
  },
  onError: (_error, _todo, context) => {
    queryClient.setQueryData(["todos"], context.previous)
  },
  onSettled: () => {
    queryClient.invalidateQueries({ queryKey: ["todos"] })
  },
})
```

Cancel the fetches in flight, keep a snapshot, write the new item into the cache, put the snapshot back if the server says no, then refetch to be sure. That's one mutation. Now do it for every mutation in your app, and keep all of them correct while the code changes around them.

That's an optimistic update, and users expect them now. Most of us write them by hand, one at a time.

TanStack's own answer is a newer library, [TanStack DB](https://tanstack.com/db). You write to local collections and read through live queries, and it handles the optimistic state and the rollback for you.

Local-first takes that idea all the way. Every write goes to a local database first, the UI renders from that database, and syncing is the database's job. You solve optimistic UI once, for the whole app, and the fetch calls, loading states, cache keys and rollbacks go away with it.

The nice part is that offline and multi-device come from the same work. Once writes land locally and sync later, it doesn't matter much whether "later" means 50 milliseconds or two days.

Waits for the server

Time until you saw it

0ms

Spent waiting so far: 0 ms

Local-first

Time until you saw it

0ms

Spent waiting so far: 0 ms

## Your Phone and Your Laptop Are Two Collaborators

"My app isn't collaborative, it's single-user." I hear this a lot.

But edit a note on your phone on the train, then edit the same note on your laptop before the phone has synced. Those two edits have to meet somewhere. The moment you have two devices, you have the collaboration problem, even with one user.

9:41

‹ Notes
Done

Synced

Notes

Synced

Click either screen to edit the note

Switch the phone to Tunnel, then change the title on one device and the body on the other. When the phone gets its signal back, both edits survive, because they touched different fields. Change the same field on both, and the later edit wins. That's a merge, and most of the time it's exactly what you want. Not always, and we'll get to that.

The usual answer is broadcasting. When something changes, the server pushes a message, over a WebSocket or server-sent events, and clients update. That works until a client is offline when the message goes out. It misses it, and when it reconnects it has no idea what it missed. So you add sequence numbers, a catch-up endpoint and some reconciliation code, and now you're writing a sync engine without meaning to.

A sync engine doesn't care which messages a client saw. Its job is that every client ends up with the same data, including the one that spent an hour in a tunnel. Broadcasts are still the right tool for things that shouldn't survive a reload, like cursors or who's typing. For the actual data, you want the engine.

## Why the Meanings Split

If the original vision is so good, why did most tools drop the ownership part?

Conflicts. If every device holds the real copy and no server is in charge, devices have to merge changes on their own. The tool for that is CRDTs, data structures built so that any two copies merge into the same result, whatever order the changes arrive in. They're clever, and they're great for things like collaborative text.

But a CRDT only promises that the copies end up the same. Whether the result makes sense for your app isn't its job. It knows nothing about your rules.

Take a flight with one seat left. Two people book it offline, on two different phones. Both bookings are fine on their own devices, and both get a confirmation. When the phones sync, the merge converges to a flight with two passengers in seat 14C. Every copy agrees, and one of those people finds out at the gate.

Book seat 14C on both phones, then reconnect.

9:41

‹ Trips

Flight 214

Warsaw to Chicago

Row 14

A
B

C
D

No signal

Anna's phone

9:41

‹ Trips

Flight 214

Warsaw to Chicago

Row 14

A
B

C
D

No signal

Ben's phone

When they sync

Real apps are full of rules like that. Unique email addresses, stock levels, a budget that can't go below zero, who's allowed to do what. Someone has to say no, and that someone needs to see everything. So most tools put a server back in charge, which is the "Server decides" option in the demo. The client writes locally, the server checks each write and gets the final word. End-to-end encryption still works in that model, but only for fields the server never has to check. A rule like one passenger per seat needs a server that can read the seat.

You keep speed and offline, and some of the ownership too: a full local copy, and encryption for what the server doesn't check. What you give up is a server you could do without. In this model it's the one copy every rule is checked against, so it can't go away. That's the split.

You can see it in how tools describe themselves. [Zero](https://zero.rocicorp.dev/docs/when-to-use), one of the most popular sync engines right now, says in its own docs that it isn't local-first, because it has an authoritative server. It uses the word the way the essay did. [Jazz](https://jazz.tools/blog/what-is-jazz) started as a CRDT framework, has just moved to a model with a server in charge, and still calls itself local-first.

Zero

Who's in charge
:   A server

Writes while offline
:   No

Calls itself local-first
:   No

Jazz

Who's in charge
:   A server

Writes while offline
:   Yes

Calls itself local-first
:   Yes

So two tools with the same design disagree about whether the word applies to them. Zero says no because it has a server in charge, Jazz says yes because you can still write offline. Both are reasonable readings of the essay.

## What It Costs

None of this is free.

Each client gets a slice

You can't send the whole database to every browser. Each client needs only the part it's allowed to see and actually uses. Working out that part, and keeping it right as permissions change, is one of the hard problems.

Old clients come back

Someone opens your app on a phone that spent a week in a drawer. It still runs last week's version, and it holds writes made against last week's schema. The server has to accept those writes or explain why not, and the app has to update itself without losing them.

Browser storage isn't forever

[Safari](https://webkit.org/blog/10218/full-third-party-cookie-blocking-and-more/), for example, can clear a site's storage after seven days of browsing without a visit to that site, so the copy on the server still matters.

Some actions should wait

Charging a card or sending money shouldn't happen optimistically. A good setup lets most of an app be local-first while a few actions still ask the server first.

## So What Does It Actually Fix?

The waiting.

The spinners, the "Saving...", the cache bugs, the hand-written optimistic updates. And the app that dies in a tunnel, because with local-first that's the same problem as the spinner. Whether it also gives you ownership depends on which of the three meanings you sign up for, and most tools today pick the other two.

I'm building local-first into Hologram, a full-stack framework where you write the whole app in Elixir and the browser part gets compiled to JavaScript. To be clear about which local-first: the one I defined at the start. Your app reads and writes local data and never waits for the network, offline included, while the server stays in charge of permissions and rules. Ownership isn't off the table either: the plan is end-to-end encryption for the entities or attributes you choose, with CRDTs where the server can't be the one to merge. Later posts in this series will show how it works there. If you don't want to wait, my [ElixirConf US talk](https://youtu.be/jdg_UrLp0bU) in Chicago in September shows it running.

The demos in this post are Hologram components, by the way.
