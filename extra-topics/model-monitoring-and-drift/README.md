# Model Monitoring and Drift

Detect when production-like data drifts and when model quality degrades.

**Points: 15**

---

## Task

1. **Baseline (3 pts)** — Train a model on a public dataset; freeze a reference distribution (features + predictions/labels).
2. **Simulate drift (4 pts)** — Create a “live” batch that shifts covariates and/or label prevalence (document how).
3. **Detect (5 pts)** — Implement at least two monitors, e.g.:
   - input drift (PSI, KS, or embedding distance),
   - prediction drift,
   - performance drop when labels are available.
4. **Alert & report (3 pts)** — Define thresholds; emit a Markdown/HTML report or console alert when breached. Propose a remediation action (retrain, investigate data source, rollback).

## Deliverables

- Monitoring script/notebook
- Drift report with plots
- Threshold policy documented in README
