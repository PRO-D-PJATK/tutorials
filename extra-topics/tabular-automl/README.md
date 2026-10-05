# Tabular AutoML vs Hand-Tuned Baseline

Compare an AutoML tool with a carefully engineered baseline on the same tabular problem.

**Points: 10**

---

## Task

1. **Dataset (3 pts)** — Public tabular classification or regression task. Document target, leakage risks, and split.
2. **Hand-tuned baseline (4 pts)** — Strong baseline you control (e.g. gradient boosting with manual/feature engineering). Report metrics and training time.
3. **AutoML (5 pts)** — Run Auto-sklearn, AutoGluon, FLAML, TPOT, or a cloud AutoML trial with a fixed time budget. Document which models were tried.
4. **Comparison (3 pts)** — Table: metric, wall time, interpretability, operational complexity. Conclude when AutoML is worth it for this problem.

## Deliverables

- Both pipelines runnable (or Colab)
- Comparison table + short recommendation
- Limits of the AutoML setup (budget, search space)
