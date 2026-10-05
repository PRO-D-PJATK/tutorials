# Data Engineering Fundamentals

Design a small **batch data pipeline**: ingest raw data, transform it into analytics-ready tables, store results, and document quality checks. Focus on engineering practices (schemas, idempotency, orchestration readiness), not on fancy models.

**Total: 17 points** (difficulty-weighted; scale 5–20)

---

## Objectives

1. Ingest data from at least one external source (API, public CSV/Parquet URL, or database dump).
2. Apply layered storage: **raw → cleaned → curated** (medallion-style or equivalent).
3. Enforce a schema and basic data-quality checks.
4. Automate the pipeline with a runnable script / Makefile / orchestrator entrypoint.
5. Document lineage: where data comes from, what transforms run, where outputs land.

---

## Recommended stack (pick one coherent set)

| Layer | Options |
|-------|---------|
| Storage | Local folders + Parquet/CSV, SQLite, PostgreSQL, DuckDB |
| Transform | pandas, Polars, SQL, dbt (optional) |
| Orchestration readiness | CLI script now; structure so Airflow/Kedro can wrap it later |
| Quality | Great Expectations / pandera / custom assert checks |

You may use tools from other tutorials (Airflow, Kedro), but this assignment must stand alone with a clear `README`.

---

## Part A — Ingestion (5 points)

1. Choose a **public** dataset or API (cite license / terms).
2. Implement an ingest step that writes an immutable **raw** snapshot (do not overwrite silently — version by date or run id).
3. Log source URL, download time, and row/file counts.

---

## Part B — Transformation layers (8 points)

Maintain at least three layers, e.g.:

1. **Raw** — as ingested.
2. **Cleaned** — typed columns, deduplicated, nulls handled, standardized timestamps (UTC/ISO).
3. **Curated / mart** — analytics-ready table(s) with clear grain (one row = …).

Document each transform in code comments or a short `docs/transforms.md`.

---

## Part C — Schema and data quality (6 points)

1. Define an explicit schema for the curated table (column names, types, nullability, primary/business key).
2. Implement at least **three** automated checks, for example:
   - no duplicate business keys,
   - value ranges / enums,
   - freshness (max timestamp not older than N days) **or** non-empty partitions,
   - referential consistency if you have more than one table.
3. Fail the pipeline (non-zero exit) when a critical check fails; write a human-readable quality report.

---

## Part D — Automation and ops hygiene (6 points)

1. Single entrypoint, e.g. `python -m pipeline.run` or `make pipeline`.
2. Config via env vars / `.env.example` (no secrets in Git).
3. Idempotent re-runs: re-running the same run id should not corrupt curated data.
4. `README.md` with: architecture diagram (simple Mermaid or ASCII), how to run, output locations, known limitations.

---

## Deliverables

- Repository URL.
- Runnable pipeline producing curated outputs + quality report.
- Schema definition and transform documentation.

---

## Optional extensions (+ up to 5 bonus if announced by the instructor)

- Incremental loads (only new partitions).
- dbt models on top of curated tables.
- Publish metrics to a simple dashboard or Markdown report generated each run.
- Wrap the same pipeline as an Airflow DAG or Kedro pipeline (link to those tutorials).
