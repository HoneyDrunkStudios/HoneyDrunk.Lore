---
source: "https://jkm.dev/posts/how-2004-runescape-fit-a-multiplayer-rpg-into-56k-dialup/"
title: "How 2004 RuneScape fit a multiplayer RPG into 56k dial-up"
author: "jkm.dev"
date_published: "2026-05-28"
date_clipped: "2026-05-30"
category: "Game Development / Unity"
source_type: "web"
---

# How 2004 RuneScape fit a multiplayer RPG into 56k dial-up

Source: https://jkm.dev/posts/how-2004-runescape-fit-a-multiplayer-rpg-into-56k-dialup/

How 2004 RuneScape fit a multiplayer RPG into 56k dial-up 28 May 2026 Updated: 29 May 2026 Added correction regarding Ctrl key. In early versions this was “force run”, in a later
update it was changed to “invert movement mode”.
development 
runescape 
gaming 
networking In 2004 I played too much RuneScape on a 56k modem that died the moment Mum picked up the phone. A 3D world, up to a couple of thousand players on a server, dozens on screen at once - in the browser, on 5 kilobytes per second. It worked. Let’s follow a single step and see how.
As a child I was too preoccupied with picking flax and killing goblins to think about how this worked. The answer, however, is a sustained, almost obsessive exercise in not wasting bytes. So, let’s click one tile north of where we’re standing, and trace every byte that crosses the wire from that click, to the server, to the screen of another player.
Central fountain, Varrock Square 
Methodology # The detail in this post comes from a decompiled 2004 RuneScape 2 client. Snippets are rough translations from that decompile, tidied up in places for readability but with the logic intact.
The core principles aren’t identical across versions, but most of them run all the way from RuneScape Classic (2001) to present-day RuneScape 3 and, of course, Old School RuneScape .
If you played RuneScape in the early 2000s and are still in possession of a hard drive from that era, please check out the RuneScape Archive Project . They do great work to catalogue historic RuneScape versions which are otherwise lost to time, and every contribution is valuable.
Constraints # Let’s look at some of the constraints that Jagex were working with at the time.
Bandwidth. A 56k modem syncs at 56 kilo bits per second downstream, and less upstream, minus any protocol overheads and line noise. Call it 5 KB/s down and a lot less up. Broadband was available in British homes by 2000, but it wasn’t until the late 2000s that the majority of UK households had a broadband connection, so plenty of players were on dial-up. Java applet, in a browser, in 2004. Java applets ran in a security sandbox, which meant no raw native sockets and no UDP. Every byte travelled over a single TCP connection, in-order and with per-segment overhead. A 600ms server cycle. The RuneScape game server advances in discrete cycles (or ticks) of roughly 600 milliseconds. Every cycle, for every player , the server has to work out everything that player can now see and ship it before the next one. The cipher layer, briefly # After the login handshake completes, before any game packets are sent, a small encryption layer is set up. This one’s not about saving bytes; it’s the only encryption in the stack (outside of some RSA encryption in the login handshake), and it’s here because the opcode it protects is the very thing every later section depends on.
Every packet begins with an “opcode” byte: a small integer saying what kind of packet this is. That opcode (and only that opcode) is enciphered with a stream cipher called ISAAC . There are two streams in play - one for traffic from client to server, and one for the reverse direction. Both sides need both streams: the client enciphers what it’s about to send and deciphers what just arrived, and the server does the same in mirror image (per connected player).
Both streams are seeded from a shared four-integer key. The client generates two of those integers itself; the other two come from the server as part of the handshake. The server-to-client stream then uses the same seed with 50 added to each word - enough to keep the two directions from sharing a keystream:
this.outboundCipher = new ISAAC(seed);
for (int index = 0; index < 4; index++) {
seed[index] += 50;
}
this.inboundCipher = new ISAAC(seed);
Enciphering on the way out is one line:
public void putOpcode(int opcode) {
this.putByte(opcode + this.outboundCipher.value());
}
And on the way in, the mirror image:
this.currentOpcode = (this.currentOpcode - this.inboundCipher.value()) & 0xFF;
So the packet body isn’t encrypted, only the opcode. As we’ll see later, the opcode is what tells you how to read the rest of the packet, and where one packet ends and the next begins. Without it, the body is just a wall of bytes, so enciphering that one byte was the cheapest possible defence against third-party packet parsers.
Sending a walk request # We’re going to look at what happens when you click on a tile one square north, and how that gets transmitted to the server.
Before any networking occurs, the client runs a breadth-first search using the local collision map to build a path from where you are to where you clicked (an easy search, in this case), and then writes the packet for the server to read. The pathfinding is standard so I won’t go into it here.
The first part of the packet is the opcode, followed by a single byte containing the length of the packet body. As you’ll see, the number of bytes contained in the packet is dependent on the size of the path, so this “length” byte allows the server to know how far to read. Not all packets have this length byte, only packets which contain some variably sized body.
The start position takes 4 bytes (two shorts), each subsequent waypoint delta takes 2 bytes, and there’s a final byte for whether the Ctrl key is held. So the body length is 4 + 2 * (pathLength - 1) + 1 .
this.outboundStream.putOpcode(ClientToServerOpcodes.WALK_TILE);
this.outboundStream.putByte(4 + 2 * (pathLength - 1) + 1);
The packet contains the absolute position of the first waypoint in the path ( x and z sent as a two-byte “short” each), followed by the delta of each waypoint in the path against the first one - one signed byte per axis, which fits comfortably within the byte’s range of -128 to 127, as a single click can only ever land so far away.
The decision to send only a delta here, as 2 bytes per step, rather than absolute coordinates as 4 bytes per step is the first example we’ve seen of Jagex’s networking frugality. In absolute terms it only saves a few bytes for a single walk packet, but every additional waypoint costs 2 bytes instead of 4 - a 50% saving per waypoint.
int firstX = pathX[0];
int firstZ = pathZ[0];
this.outboundStream.putShort(this.playerPositionX + firstX);
this.outboundStream.putShort(this.playerPositionZ + firstZ);
for (int i = 1; i < pathLength; i++) {
this.outboundStream.putByte(this.pathX[i] - firstX);
this.outboundStream.putByte(this.pathZ[i] - firstZ);
}
It’s worth noting here that besides the opcode and the length byte, which make up the packet header, the order in which the individual parts of the packet body are written varied between versions as an anti-cheating measure.
For instance, in this revision this packet was written as (x, z, ...path) , in other revisions - such as #317 - it was written as (x, ...path, z) , and in others as (...path, x, z) .
Additionally, byte-mangling transformations would be applied: writing with different endianness, adding constant values to individual bytes, and negating values - again as an anti-cheating measure, again varying between revisions.
I’ve reordered the snippet above, and removed all byte-mangling, for clarity. In reality these measures would be applied on both the client and the server, and would be applied to most parts of the protocol.
Another frugal decision here is that pathX and pathZ do not contain every tile in the path, just the corners. Walking ten tiles in a straight line only sends one waypoint: the destination. The server already knows where you started, so it walks the line itself and validates against its own collision map.
The last part of this packet is a single byte to indicate whether the Ctrl key is held. In early versions of the game, this was used to force “run mode”, in later versions it inverts the current movement mode (runs to your clicked destination if “run” is off, or walks if it’s on):
this.outboundStream.putByte(this.keyStatus[Keys.CTRL] == 1 ? 1 : 0);
So we can see that our single step north takes seven bytes, including our opcode and length marker:
WALK_TILE packet byte layout A seven-byte client-to-server walk packet for a single step: one opcode byte, one length byte (value 5), a two-byte destination x short, a two-byte destination z short, and one run-toggle byte. The opcode and length form the header; the remaining five bytes form the body, whose size equals the length byte. 0 1 2 3 4 5 6 opcode enciphered length = 5 x x z z Ctrl run toggle destination x · 2-byte short destination z · 2-byte short header body · 5 bytes WALK_TILE packet byte layout The seven bytes of a single-step walk packet, stacked top to bottom: byte 0 opcode (enciphered), byte 1 length (value 5), bytes 2 and 3 a destination x two-byte short, bytes 4 and 5 a destination z two-byte short, and byte 6 a run-toggle byte. Bytes 0 and 1 are the header; bytes 2 to 6 are the body, whose size equals the length byte. 0 1 2 3 4 5 6 opcode enciphered length = 5 x 2-byte short x z 2-byte short z Ctrl run toggle header body As our path only contained a single step, we don’t enter the loop to send the “delta” waypoints, so we can cross-check our 5 -byte payload against the length marker:
4 + 2 * (pathLength - 1) + 1 = 4 + 2 * 0 + 1 = 5 Once the snippets above have run, the packet is in the client’s outbound stream. That stream is drained to the network roughly every 20ms.
Server receives the request # The server’s main loop wakes roughly once every 600ms. On each wake, it drains every player’s inbound buffer, runs whatever handlers the packets call for, and composes the outbound player updates that we’ll look at next. A packet that arrives just before a cycle is processed almost instantly; one that arrives just after waits nearly a full 600ms.
That 600ms cycle time sets the granularity for latency. The 20ms client flush and any other networking overheads all swim well under this time. That’s why the rest of this post is about bytes , not time : there is no latency to save.
Once the inbound buffer has been drained by the server, reading the packet is roughly the process above, but in reverse:
int opcode = player.inboundStream.takeOpcode();
if (opcode == ClientToServerOpcodes.WALK_TILE) {
int length = player.inboundStream.takeByte();
int deltaCount = (length - 4 - 1) / 2;
int[] firstWaypoint = new int[2];
firstWaypoint[0] = player.inboundStream.takeShort();
firstWaypoint[1] = player.inboundStream.takeShort();
int[][] waypointDeltas = new int[deltaCount][2];
for (int i = 0; i < deltaCount; i++) {
waypointDeltas[i][0] = player.inboundStream.takeByte();
waypointDeltas[i][1] = player.inboundStream.takeByte();
}
boolean holdingCtrl = player.inboundStream.takeByte() == 1;
player.processWalkTile(firstWaypoint, waypointDeltas, holdingCtrl);
}
As you can see, once we’ve identified the opcode, we can read the length byte and reverse the write logic to extract the number of deltas.
I mentioned earlier that not all packets contain this length byte. In fact, most don’t; the majority of packets have a fixed-length body. Reading those is even simpler. Take, for instance, the “item on item” packet - sent when a player “uses” one item in their inventory with another:
if (opcode == ClientToServerOpcodes.USE_ITEM_ON_ITEM) {
int sourceItemId = player.inboundStream.takeShort();
int sourceInterfaceId = player.inboundStream.takeShort();
int sourceInterfaceSlot = player.inboundStream.takeShort();
int targetItemId = player.inboundStream.takeShort();
int targetInterfaceId = player.inboundStream.takeShort();
int targetInterfaceSlot = player.inboundStream.takeShort();
player.processUseItemOnItem(/* ... */);
}
This packet has a fixed length of 12 bytes (6 shorts). The server is aware of this constant length, so there is no need to transmit a length marker as part of this packet.
The server cycle # There are a number of steps that make up a RuneScape server cycle, and the parts we are interested in happen in the following order:
read incoming packets process players (queued actions, triggers, movement, etc) build player updates (more on this in the next section) flush outbound packets There are other steps omitted here, such as processing NPCs, logins and logouts, and technicalities around when exactly actions occur (some happen when the packet is read, others are queued and happen later in the cycle). NPCs are updated via a structurally identical, slightly smaller update block in a separate packet.
The overall principle is clear: read , then do , then write .
Player updates # Before tracing the packet, it’s worth being explicit about the protocol’s foundation: the client holds its own mirror of every player it can see. A tracked list of nearby players, each with their last-known position, appearance, animation and chat state - plus the local player’s own state. The player update packet’s job is to keep that mirror in sync with the server’s authoritative version - which means, almost always, that an update is a delta against what the client already knows . “No change” is so cheap precisely because the client already has the data; the server just confirms it’s still valid.
Every cycle, the server sends each player a single composite “player update packet”. This single packet describes everything the client needs to know about every player it can see - including itself. The receiving client tears this information apart in four steps, and the order of those steps is as follows:
private void readPlayerUpdates(Packet packet) {
packet.accessMode(PacketAccess.BITS);
this.readLocalPlayer(packet);
// other players already tracked by the client
this.readOtherPlayers(packet);
// players newly in range, which the client should start tracking
this.readNewPlayers(packet);
packet.accessMode(PacketAccess.BYTES);
// detailed changes about players
this.readPlayerDetails(packet);
}
The first three steps are bit-packed - the stream is read a few bits at a time, not byte by byte. Only the fourth step in this sequence is byte-aligned. This split is deliberate: movement and registration are high-frequency, and tiny, so they get bits; the less frequent rich updates (a player changed equipment, swung a sword, or said something) get bytes.
Step 1: Local player # The logic to read a local player is simple, so I will let you read it and we can analyse it after:
private void readLocalPlayer(Packet packet) {
int updated = packet.takeBits(1);
// no local movement and no local detail changes
if (updated == 0) {
return;
}
int movementType = packet.takeBits(2);
// type 1: a walk
if (movementType == 1) {
int direction = packet.takeBits(3);
this.localPlayer.step(direction, false);
int detailUpdated = packet.takeBits(1);
if (detailUpdated == 1) {
this.trackPlayerDetails(this.localPlayer.id);
}
}
// type 0: no move, but a detail update follows
// type 2: a run - two directions back-to-back
// type 3: a teleport
}
Read that first if statement again. If the local player didn’t move, and nothing about them changed this cycle, their entire presence in the update packet is a single bit. Not a byte. A bit. The most common state of any given player on any given cycle - “no change” - was made the cheapest possible transmission.
If the local player did move, it’s a 1 bit, two bits to represent the type, three bits for the direction and a single bit for the “is there more detail coming?” flag. Seven bits, less than a single byte , for “I took a step.” Excluding the first “update required” flag and the movement type, it fits in four bits.
The other types are cheap, too. Excluding the three bit headers:
type 0 (no move, but details to come): no payload. Zero bits. type 2 (a run): two 3-bit directions, and a “more detail” flag bit. Seven bits. type 3 (a teleport): the height plane (2 bits), the x and z coordinates (7 bits each), the “more detail” flag bit, and a “jump” bit (used to tell the client whether it should attempt to animate this movement). Slightly more expensive, but still only eighteen bits - slightly over two whole bytes. Step 2: Tracked players # This is the same idea as above, applied to the crowd of already-tracked players.
One thing to note is that reading individual bits here continues immediately from the “local player” section above. That is to say, if the local player section is only 1 bit, the section below will begin reading from the 2nd bit - there’s no empty space to pad full bytes.
private void readOtherPlayers(Packet packet) {
int count = packet.takeBits(8);
for (int i = 0; i < count; i++) {
int updated = packet.takeBits(1);
if (updated == 0) {
continue;
}
// read movementType etc as above
}
}
An 8-bit count, then one bit per known player to say whether anything happened to them. Stand in a crowd of forty players where nobody’s moving, and that’s forty-eight bits (six bytes) to confirm that the entire scene is static. Any player who did take a step costs the same seven bits as the local player did in step 1.
This is the core trick. The default - “nothing changed” - is a single bit, the cheapest possible representation. Real bits are only spent on the things that actually moved. The server and the client share, baked in at compile time, an identical understanding of the protocol - including what the default is, and what counts as changed. Neither end ever has to detail “no change”; the absence of detail, gated behind the zero bit, is the message.
Step 3: New players in range # When someone walks into (or otherwise arrives in: logging in, teleporting, etc) your view for the first time, the server has to introduce them - who they are and where, relative to you:
private void readNewPlayers(Packet packet) {
// room for an 11-bit player id
while (packet.bitsRemaining > 10) {
int playerId = packet.takeBits(11);
// sentinel: no more players
if (playerId == 2047) {
break;
}
Player otherPlayer;
// ... allocate or look up the player ...
int updated = packet.takeBits(1);
if (updated == 1) {
this.trackPlayerDetails(playerId);
}
int teleported = packet.takeBits(1);
int deltaX = packet.takeBits(5);
if (deltaX >= 16) { deltaX -= 32; } // signed 5-bit value: -16 to +15
int deltaZ = packet.takeBits(5);
if (deltaZ >= 16) { deltaZ -= 32; }
otherPlayer.move(localPlayer.x + deltaX, localPlayer.z + deltaZ, teleported == 1);
}
}
An 11-bit player id ( 2047 is reserved as the “stop” sentinel, so the list doesn’t need a length header), one bit for whether a “more details” update is coming later, one bit for whether they teleported in, and then 10 bits for the position. The position is one of the details I love the most about this section.
Relative coordinates # A player’s absolute world coordinates are a pair of values in the thousands - RuneScape’s map is very large (thousands of tiles on each axis). Two 16-bit numbers, 32 bits total, to place someone anywhere on that map.
But the player update logic above doesn’t need a global position. It only needs to know where they are relative to the local player , because that’s all that can be seen. Another player who’s in range to be drawn is at most about fifteen tiles away. Fifteen fits nicely in a signed 5-bit number ( -16 to +15 ). So a newly-visible player’s location costs ten bits - five per axis - instead of thirty-two. The coordinate space is recentered on the local player, and clipped to what’s visible. The encoding is sized to exactly that clipped range and not a single bit more. The same logic appears in step 1’s teleport branch, where coordinates are expressed as two 7-bit values (enough to address the ~104-tile loaded area) rather than full world coordinates.
This is the pattern repeated everywhere: figure out the smallest set of values that could possibly be needed, then use exactly enough bits to represent that set. 
The bit cursor # At the start of this section, I mentioned that steps 1 through 3 read individual bits, while step 4 reads whole bytes. All of the “a few bits at a time” reading is one small method doing the bookkeeping. The convention is that bits fill each byte from the top down - the first bit sits at position 7, the last at position 0:
public int takeBits(int count) {
int value = 0;
for (int n = 0; n < count; n++) {
int bytePos = this.bitPosition / 8;
int bitInByte = 7 - (this.bitPosition % 8);
int bitValue = (this.buffer[bytePos] >> bitInByte) & 1;
value = (value << 1) | bitValue;
this.bitPosition++;
}
return value;
}
The above implementation is somewhat different to that shipped in the RuneScape client - I’ve simplified it to highlight the concept more clearly. The version shipped with the client is slightly more complex as it’s optimised for performance.
As you can see, the method above walks the buffer one bit at a time. Without this, every “three bits per direction” and “one bit per idle player” would need to be read as a byte, taking most of the protocol’s frugality with it - eight idle players would need eight bytes rather than one.
When the bit-packed steps finish, the cursor is rounded up to the next whole byte and step 4 takes over with conventional byte reads.
Step 4: Player detail changes # This fourth step is responsible for any detailed player updates, generally related to the appearance of the player. It only touches players flagged as “more detail to come” in one of the earlier steps.
The full list of update flags is:
facing entity facing tile forced public chat animation appearance changed: equipment, etc (more on this below) took a hit normal public chat graphical effect forced movement along a path Looking at the layout, the bottom two flags in the list are always (as far as I can tell) represented by bits in the high byte of the update type. These also tend to be the rarer updates, and I believe the assignment is a deliberate economic choice: only rare events require the second byte of the update type to be transmitted.
Later revisions add a “took a second hit this cycle” update - this is also always represented by a bit in the high byte, as further evidence that only rarer events require this extra byte for the update type.
Every player in the array of “more detail” updates is iterated over, and an “update type” flag is read:
private void readPlayerDetails(Packet packet) {
for (int i = 0; i < moreDetailPlayerCount; i++) {
int updateType = packet.takeByte();
if ((updateType & 0b1000_0000) != 0) {
updateType |= packet.takeByte() << 8;
}
// ...
}
}
We can see another byte efficiency trick in use here. The nine flags we just listed are too many to fit in a single byte when each flag is an individual bit, so the full update type needs two bytes to address. Rather than reading two bytes per player (using takeShort ), seven flags are packed into the first byte with a single marker bit, the most significant bit. When this marker bit is set, a second byte is read, shifted left by one byte and combined with the first to give a 16-bit value (of which 10 bits are meaningful: the 9 flags plus the marker).
The bits used for each flag, including the marker, are varied between versions as an anti-cheating measure.
After obtaining the full update type, it is checked for the presence of individual flags to apply certain details. Some of these are illustrated below:
if ((updateType & 0b0000_0100) != 0) {
// player is facing an entity (npc or another player)
player.targetEntityId = packet.takeShort();
}
if ((updateType & 0b0010_0000) != 0) {
// player is facing a tile
player.targetTileX = packet.takeShort();
player.targetTileZ = packet.takeShort();
}
if ((updateType & 0b0000_0010) != 0) {
// player is performing an animation
player.animationId = packet.takeShort();
player.animationDelay = packet.takeByte();
}
// ... other flags ...
// check the least significant bit of the high byte
if ((updateType & (0b0000_0001 << 8)) != 0) {
// a graphical effect is playing on the player
player.graphicalEffectId = packet.takeShort();
player.graphicalEffectHeight = packet.takeShort();
player.graphicalEffectDelay = packet.takeShort();
}
In the few examples above, you can see a number of the tricks we’ve seen so far. Multiple flag values are packed into the 8-bit or 16-bit update type. Different update mechanisms have different body sizes, as part of the agreed protocol between the client and server. The smallest data type appropriate for the values being represented is used. All of these decisions were made with the aim of minimising the amount of data required to transmit this information.
Appearance update # I won’t go into full detail around the “appearance” part of this packet, but it’s the only expensive one in the list. It contains:
name combat level body part information, including equipped items and NPC transmogs body part colour stand / walk animations gender head icons (prayer icons, PK skull) In total the appearance section costs between 44 and 80 bytes per player.
Why no bit packing? # It might seem inconsistent that the protocol abandons bit-level frugality just as it reaches the largest part of the packet, but step 4 is actually following the same rule as the rest - just landing on the other side of it. Bit packing trades CPU for bytes: you pay the cost of a bit cursor to reclaim the slack between a value’s real width and the byte it would otherwise sit in. It’s worth that trade only where the slack actually exists and repeats.
In steps 1, 2 and 3 it does, many times over. The default state - “no change” - is a single bit, and it repeats across every visible player every cycle, so the saving compounds across dozens of entities. Step 4 has neither half of that. There is no tiny default: a player either has no update at all (already gated by a single bit upstream) or a real one, whose smallest field, “facing an entity”, is already a two-byte short. A short has no slack to reclaim - it fills both its bytes - so bit packing would save nothing while still charging the cursor cost. The multiplier is gone too: step 4 only ever contains the handful of players who changed this cycle, not the whole crowd, so even if there were bits to save there’s almost nothing to multiply them by. The one place the trick still pays off is the update-type byte itself, with the marker bit buying a second byte only when needed - bit-packed within a byte, exactly where slack still exists.
The second reason is how the server composes this part of the packet, and it’s really the same point seen from the server’s side. Many fields in step 4 aren’t recomputed each cycle - I believe the appearance buffer, for example, is built once per player per change and held as a byte buffer the server splices into outgoing packets for any observer who needs it. The client certainly caches it that way, reusing it when a tracked player leaves visible range and re-enters; it would be strange for the server not to mirror that. What makes the splice cheap is that a byte-aligned blob is position-independent: wherever it lands in a given observer’s packet, it’s the same sequence of bytes, so inserting it is a plain array copy. Bit-align it and its offset would depend on everything written before it - which differs for every observer and every cycle - so the same cached blob would need a fresh shift-and-mask for every observer, every cycle, and the cache stops being worth keeping.
So the two halves of the packet are tuned for two different scarce resources. The bit-packed front is cheap to compute, impossible to cache, and exists to spare the client’s downstream dial-up. Nothing in it can be shared between observers: each sees a different crowd, positioned relative to itself. The byte-aligned back is expensive to compute but rarely changes, so it’s built once and spliced wherever it’s needed - and here the binding constraint isn’t the wire at all, but the server’s budget to assemble up to two thousand of these before the next cycle. The protocol switches representation at exactly the point where that constraint flips.
The bytes on the wire # Let’s add it up for the actual scenario: you take one step north, and we count what a nearby player’s client receives in that cycle’s player update packet. Say there are twenty other players in their view and, this cycle, only you moved.
Player-update packet, bit by bit The downstream player-update payload for one tick, laid out as six rows of eight bits (one row per byte). Bit 0 is pass 1, the local player, who did not move. Bits 1 to 8 are the pass 2 player count, spilling across the first byte boundary. Bits 9 to 15 are your seven-bit step. Bits 16 to 34 are nineteen idle players at one bit each, running across three rows. Bits 35 to 45 are the eleven-bit pass 3 new-player sentinel. Bits 46 and 47 are byte-alignment padding. Forty-eight bits total, six bytes, plus a one-byte opcode and two-byte length make nine bytes on the wire. one row = one byte (8 bits) · one cell = one bit byte 0 byte 1 byte 2 byte 3 byte 4 byte 5 Step 1 · local player — 1 bit (no move) Step 2 · player count — 8 bits Step 2 · your step — 7 bits (1+2+3+1) Step 2 · 19 idle players — 19 bits Step 3 · new-player sentinel — 11 bits byte-align padding — 2 bits (wasted) 48 bits = 6 bytes  · +1 opcode +2 length =  9 bytes Add the opcode byte and a length marker (two bytes, rather than the single-byte marker used for our walk packet - the length of the player update block can be greater than 255), and you’re at roughly nine bytes for the complete answer to “what did everyone around me just do?” on a cycle where one person took one step in a crowd of twenty-one. Your upstream walk packet was seven bytes; the update echoed back to you is about nine. Sixteen bytes, round trip, for a step - and the server sends that same nine-byte answer to every other player who can see you. At 5 KB/s you have headroom for hundreds of those per second, which is exactly the point - combat, crowds and chat all have to fit in the same pipeline.
For scale: the text of this post is a touch over 32 KB - more than three thousand of those nine-byte scene updates. The write-up describing the frugality is far larger than anything the protocol actually sends.
The complete round trip, end to end:
The journey of one step A sequence diagram with three participants: your client, the server, and another player's client. Your client pathfinds and writes a walk packet, then sends a seven-byte WALK_TILE packet up to the server, flushed roughly every 20 milliseconds. The server runs a roughly 600 millisecond cycle: read, process, build updates, flush. At the end of the cycle it sends an approximately nine-byte player-update packet down to the other player's client, which renders your step, and a copy of about nine bytes back to your own client, making the round trip. The net cost is seven bytes up, about nine bytes down per observer, and one 600 millisecond cycle of latency. Your client Server Other player WALK_TILE  7 B flushed every ~20 ms server cycle ≈ 600 ms player update  ~9 B your own copy  ~9 B 7 B  up ·  ~9 B  down per observer · one 600 ms cycle of latency The general lesson # The RuneScape client and the server it communicated with are not two systems exchanging messages. They work together as one system, which happens to be split across a TCP connection. Every economy in this protocol depends on both ends sharing knowledge that is never transmitted:
Both ends run the same pathfinder over the same collision map, so the client can send corners and the server can simply validate the path. Both ends agree, at compile time, that the default state of a player is “didn’t change”, so “didn’t change” can cost only one single bit. Both ends agree that visible means “within ~15 tiles”, so a position can be five bits per axis instead of sixteen. Both ends agree on a fixed table of what things can change, so a bitmask can stand in for a schema. None of this shared understanding is sent over the wire. It’s in the design . The protocol is small because the two programs were written together, by people treating the network as an implementation detail of a single application rather than a boundary separating two.
It’s tempting to read this as a relic - the way things had to be built before bandwidth became cheap. But the dividing line was never old versus new ; it’s what the system is for , and which constraint is actually binding. A modern web service is built the opposite way on purpose: loosely coupled, self-describing, versioned, verbose - the same scene update as JSON over HTTP would run to hundreds of bytes, its headers alone dwarfing the nine. That heft isn’t waste; it’s what buys the ability to change one side without redeploying the other, to serve many different clients, and to debug by reading the wire. Those are the right defaults when the thing pressing on you is teams and change velocity, not bytes.
What’s easy to miss is how much software written today still lives on RuneScape’s side of that line. A competitive shooter, a rollback fighting game, a market-data feed - anywhere both ends ship together and every byte is contested - reach for the same tightly co-designed, bit-packed, schema-baked-in approach. The decoupled style isn’t a feature of modern design - it’s a response to independent deployability . You move toward it or away from it depending on which constraint binds.
Push the other way - make every byte genuinely matter - and you get this instead: a data model and wire format co-designed so tightly that they exist as one artifact. One where the cleverness lives in everything you’ve arranged not to send. Studying this protocol is studying what engineering looks like under a hard, absolute limit.
Thanks # Thank you to Jagex for building something that not only has stood the test of time, but that is good enough to be worth taking apart and learning from twenty years later.
Thank you to the many, many members of the preservation and reverse-engineering communities I’ve worked with over the last fifteen years to build the understanding I have today.
The variable names and structure come from a decompiled and cleaned up RuneScape client; the design is entirely Jagex’s.
