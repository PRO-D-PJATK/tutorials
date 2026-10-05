# Live Stream Analytics

Analyze data **while it is flowing**: maintain running aggregates, windows, and simple alerts on a stream (real or simulated).

**Points: 18**

This topic complements [data-scraping/stream-scraping](../data-scraping/stream-scraping/) (collecting). Here the focus is **online analytics**, not just storage.

---

## Task

1. **Streaming input (3 pts)** — Consume a live or simulated event stream (Kafka, Redpanda, WebSocket, SSE, or in-process generator). Document event schema.
2. **Windowed analytics (6 pts)** — Compute at least two live metrics using tumbling or sliding windows, e.g.:
   - events per minute,
   - running mean / p95 of a numeric field,
   - top-K categories in the last N minutes.
   Implement with a stream library (Faust, Flink, Spark Structured Streaming, bytewax, `river`, or a well-structured Python consumer with explicit window logic).
3. **Live sink / dashboard (3 pts)** — Continuously update a sink: console dashboard, Prometheus metrics, Streamlit/Gradio refreshing view, or append-only analytics table queried live.
4. **Alerting (3 pts)** — Trigger an alert when a threshold is crossed (e.g. spike in error rate or volume). Log alert time and triggering window stats.

## Deliverables

- Runnable stream job + how to start producer/consumer
- Screenshot or log excerpt of live metrics updating
- Alert example and threshold policy

## Suggested stack options

- Python generator + `river` / custom windows (simplest)
- Kafka + ksqlDB / Faust
- Spark Structured Streaming (if already in your environment)

## Stretch (optional)

- Watermarks / late events handling
- Exactly-once sinks
- Compare batch-of-microbatches vs true event-at-a-time results
