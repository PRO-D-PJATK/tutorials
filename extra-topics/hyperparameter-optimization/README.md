# Hyperparameter Optimization

Compare systematic HPO against manual defaults on a tabular or small ML task.

**Points: 11**

---

## Task

1. **Baseline (3 pts)** — Train a model with default/hand-chosen hyperparameters; record metric + time.
2. **Search space (3 pts)** — Define a clear search space (ranges/types) for ≥3 hyperparameters.
3. **HPO run (6 pts)** — Use Optuna, Ray Tune, or Hyperopt with a fixed budget (n trials or wall time). Use cross-validation or a held-out validation set. Log best params and learning curves / optimization history.
4. **Analysis (3 pts)** — Compare best HPO result vs baseline (metric and compute cost). Discuss overfitting to the validation set and whether gains justify cost.

## Deliverables

- HPO script with reproducible seed
- Trial history plot or table
- Final recommended configuration
