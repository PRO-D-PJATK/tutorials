# Experiment Tracking (MLflow / W&B)

Track ML experiments so every run is comparable and reproducible.

**Points: 15**

---

## Task

1. **Setup (3 pts)** — Choose **MLflow** (local or remote) **or** Weights & Biases. Document install and login/config (no secrets in Git).
2. **Instrument training (5 pts)** — For at least **two** model variants or hyperparameter settings, log:
   - parameters,
   - metrics (train/val),
   - at least one artefact (model file, confusion matrix plot, or predictions sample).
3. **Compare runs (4 pts)** — Produce a comparison table/screenshot from the tracking UI (or exported report). Explain which run wins and why.
4. **Reproducibility (3 pts)** — Record git commit / code version, dataset version or hash, and random seed. Show how to re-run the best config from logged params.

## Deliverables

- Instrumented training code
- Link or screenshots of the tracking project/UI
- Short write-up of the winning configuration
