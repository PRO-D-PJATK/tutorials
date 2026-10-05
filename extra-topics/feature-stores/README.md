# Feature Stores (Basics)

Build a minimal feature store workflow: define features, materialize them, and train a model without training–serving skew.

**Points: 15**

---

## Task

1. **Feature definitions (4 pts)** — On a public tabular/event dataset, define at least **three** features (aggregations allowed, e.g. rolling counts). Document entity keys and feature freshness.
2. **Store / registry (4 pts)** — Use Feast **or** a simplified registry (Parquet + metadata YAML) that can retrieve features by entity id + timestamp.
3. **Point-in-time correctness (4 pts)** — Demonstrate that training rows use only information available at prediction time (no leakage). Show one failing “leaky” example and the corrected join.
4. **Model use (3 pts)** — Train a simple model on retrieved features and document the offline vs online retrieval path (even if “online” is a local API mock).

## Deliverables

- Feature definitions + materialization script
- Evidence of point-in-time joins
- Short architecture note (offline store / online path)
