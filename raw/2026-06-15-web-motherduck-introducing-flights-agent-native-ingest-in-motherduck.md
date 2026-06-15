---
source: "https://motherduck.com/blog/flights-agent-native-ingest/"
title: "Introducing Flights: Agent-Native Ingest in MotherDuck"
author: "MotherDuck"
date_published: "2026-06-10"
date_clipped: "2026-06-15"
category: "Workflow Automation"
source_type: "web"
---

# Introducing Flights: Agent-Native Ingest in MotherDuck

Source: https://motherduck.com/blog/flights-agent-native-ingest/

## Old duck, new interfaces

Data movement has been technically "solved" for a long time–it's only recently that modern data stack vendors delivered freedom from the brittle ETL code we used to live with. Customers got simple point-and-click UIs and durability, and the code got abstracted away.

In the agent era, code is the most important primitive. Agents doing data work need code-first interfaces to build effectively, and a flexible yet secure environment in which to operate.

We've taken this to heart with Flights, which support a growing list of agent-friendly interfaces while executing inside a general-purpose Python runtime. Anything you can `pip install`

, you can build. Flights are tightly integrated with MotherDuck databases–they connect the Python runtime to your Ducklings (compute instances) using the DuckDB Python client.

### Building Flights with the MCP server

Connect any MCP-capable agent (Claude, Cursor, ChatGPT, your own) to the MotherDuck MCP server and the agent gets the full Flights surface as tools: create, run, schedule, update, inspect logs, version, delete. It also gets `get_flight_guide`

, a built-in instruction set, so the same prompt produces a working Flight whether it's the agent's first or hundredth.

The MCP server is also the interface for creating Dives, so a single chat can take a raw source through ingestion and into a live dashboard or data app. Secrets stay in MotherDuck and are injected into the Flight at runtime; your agent never sees them.

### Using SQL table functions

Every Flight operation has a matching SQL table function. Create, run, schedule, list, inspect logs, version, delete: all of it is a `SELECT`

away. Anything that speaks SQL can manage Flights: a DuckDB client, your BI tool, dbt, even another Flight.

The table functions make Flights accessible from wherever you, or your agents, are working. For example, create a Flight by calling `MD_CREATE_FLIGHT`

with the Python source inline:

```
SELECT * FROM md_create_flight(
name := 'daily_signups',
access_token_name := 'prod_token',
schedule_cron := '0 9 * * *',
source_code := $$
import duckdb
def main():
duckdb.connect("md:").execute("""
INSERT INTO analytics.signups
SELECT * FROM 'https://api.example.com/signups.json'
""")
$$
);
```


### With the Flights UI

You can also manage Flights visually from within the MotherDuck UI. Write or paste in your Python code, set a schedule, and trigger Flight runs instantly.

The UI includes the same tools as the SQL table functions: logging, run history, versions, environment variables, and the `requirements.txt`

file for your Python environment.
