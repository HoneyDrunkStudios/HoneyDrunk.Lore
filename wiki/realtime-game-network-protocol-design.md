# Realtime Game Network Protocol Design

## Decision-useful summary
The RuneScape 2004 networking teardown is a compact case study in bandwidth-constrained realtime multiplayer design. The durable lesson is not "always bit-pack everything"; it is that tightly co-designed client/server systems can send very little when both sides share pathfinding rules, default states, visible ranges, and update schemas. For HoneyDrunk, this is useful when evaluating realtime games, spectator systems, or agent simulations where independent deployability is less important than latency, bandwidth, and deterministic shared state. [source: raw/2026-05-30-web-jkm-dev-how-2004-runescape-fit-a-multiplayer-rpg-into-56k-dial-up.md]

## Claims
- 2004 RuneScape fit browser-based 3D multiplayer over dial-up by treating the client and server as two halves of one tightly co-designed application, using a single TCP connection, a roughly 600 ms server tick, compact opcodes, and update packets built around deltas rather than self-describing messages. confidence: 1 reverse-engineering source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-jkm-dev-how-2004-runescape-fit-a-multiplayer-rpg-into-56k-dial-up.md]
- The walk request example sends the absolute first waypoint, waypoint deltas, and a movement-mode byte; straight paths omit intermediate tiles because client and server share collision/pathfinding assumptions and the server validates the path. confidence: 1 source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-jkm-dev-how-2004-runescape-fit-a-multiplayer-rpg-into-56k-dial-up.md]
- Player update packets make "no change" extremely cheap: tracked players commonly cost one bit per tick unless they moved or need detail updates, while newly visible players are encoded relative to the local player rather than as global coordinates. confidence: 1 source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-jkm-dev-how-2004-runescape-fit-a-multiplayer-rpg-into-56k-dial-up.md]
- RuneScape used bit packing where the savings repeated across many players/cycles, but retained byte-aligned detail blobs for less frequent richer updates because cached byte buffers are cheaper to splice for many observers. confidence: 1 source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-jkm-dev-how-2004-runescape-fit-a-multiplayer-rpg-into-56k-dial-up.md]
- The source argues verbose, self-describing web protocols are not "worse"; they buy independent deployability, readable debugging, and multi-client evolution. Tight bit-packed protocols are appropriate when both ends ship together and bytes are the binding constraint. confidence: 1 source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-jkm-dev-how-2004-runescape-fit-a-multiplayer-rpg-into-56k-dial-up.md]

## Typed entities
- game: RuneScape 2 / 2004 RuneScape
- company: Jagex
- protocol concept: bit-packed player update packet
- protocol concept: opcode
- protocol concept: relative coordinate encoding
- protocol concept: delta update
- protocol concept: fixed-length packet body
- protocol concept: variable-length packet body
- cryptographic component: ISAAC stream cipher for opcodes
- runtime constraint: 56k dial-up
- runtime constraint: Java applet sandbox
- runtime constraint: single TCP connection
- timing model: roughly 600 ms server cycle
- community/project: RuneScape Archive Project

## Explicit relationships
- RuneScape client and server use shared collision/pathfinding rules to reduce transmitted path data.
- Delta updates depend-on the client retaining a local mirror of visible players.
- Relative coordinates supersede absolute world coordinates when only local visibility matters.
- Bit packing depends-on high-frequency small fields; byte-aligned cached blobs supersede bit packing when reusable detail payloads dominate server assembly cost.
- Tight protocol co-design contradicts independent client/server deployability, but improves bandwidth efficiency under hard network limits.
- [[gamedev-production-and-community-signals]] uses this case study as production architecture signal for realtime game constraints.

## HoneyDrunk implications
- For any HoneyDrunk realtime multiplayer prototype, decide early whether client/server are tightly versioned together or independently deployed; that choice should drive protocol shape.
- Use shared simulation knowledge deliberately: defaults, visible ranges, and fixed schemas can reduce bandwidth, but only when versioning and anti-cheat needs are understood.
- Benchmark protocol choices against actual target constraints instead of defaulting to JSON/HTTP or premature bit packing.

## Confidence and quality notes
- Quality posture: useful reverse-engineering case study, not official Jagex documentation. Treat exact implementation details as historical analysis; treat the design principles as decision-useful.
- Privacy filter: no private data copied.
