# Stream Scraping (Collecting from Streams)

Ingest records from a **streaming source** (real or simulated): WebSocket, Kafka/Redpanda, MQTT, SSE, or a public firehose-style API.

**Points: 10**

---

## Task

1. **Source (2 pts)** — Select a stream (e.g. public WebSocket demo, Wikipedia recent changes stream, IoT sample broker, or a local producer you write). Document protocol and message schema.
2. **Collector (4 pts)** — Write a consumer that:
   - connects to the stream,
   - parses messages,
   - writes them to disk/DB as an append-only log (e.g. JSONL / Parquet partitions) with event timestamps.
3. **Run window (2 pts)** — Collect for a defined window (e.g. 5–15 minutes) or N messages. Report volume, throughput, and drop/error counts.
4. **Post-processing (2 pts)** — Build a small cleaned batch from the log (dedupe by event id if present, schema enforcement). Show head/tail samples.

## Deliverables

- Producer (if simulated) + consumer code
- Sample of captured stream data
- Notes on backpressure, reconnects, and at-least-once vs exactly-once expectations

## Notes

- Prefer simulation if public streams are unstable or require paid keys.
- Do not scrape private chats or authenticated personal feeds without explicit permission.
