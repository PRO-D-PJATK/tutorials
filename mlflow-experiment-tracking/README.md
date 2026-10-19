# MLflow Experiment Tracking and Model Registry

Build a small **MLflow**-instrumented training project: log parameters, metrics, and artefacts for comparable runs, then register a winning model. Prefer a local Tracking UI (file store or SQLite); a remote server is optional.

**Total: 15 points**

Docs: [MLflow Tracking](https://mlflow.org/docs/latest/tracking.html) · [Model Registry](https://mlflow.org/docs/latest/model-registry.html)

This folder includes a minimal `train.py` starter and `requirements.txt` you may adapt.

---

## Objectives

1. Run MLflow Tracking locally and open the UI.
2. Instrument training so every run logs **params**, **metrics**, and at least one **artefact**.
3. Compare at least **two** model variants / hyperparameter settings in the UI (or via the API).
4. Register the best model in the **Model Registry** (or document an equivalent versioned artefact workflow if Registry is unavailable).
5. Show how to **re-run** the winning configuration from logged metadata.

---

## Prerequisites

- Python 3.9+
- `pip install -r requirements.txt` (from this folder) **or** `pip install mlflow scikit-learn pandas matplotlib`
- Basic familiarity with a simple supervised model (classification or regression)
- A **public** dataset (cite URL + license in your README)

---

## Part A — Tracking setup (3 points)

1. Create a project repository with:
   - training script(s),
   - `requirements.txt` (pinned versions preferred),
   - `README.md` describing the prediction task, dataset, and how to run.
2. Configure MLflow tracking, e.g. local file store or SQLite:

   ```bash
   export MLFLOW_TRACKING_URI=./mlruns   # or sqlite:///mlflow.db
   mlflow ui --backend-store-uri "$MLFLOW_TRACKING_URI" --port 5000
   ```

3. Document in the README: Tracking URI, how to start the UI, and that **secrets stay out of Git** (`.gitignore` for `.env`, credentials, large raw dumps if needed).

---

## Part B — Instrumented training runs (5 points)

Using the Tracking API (`mlflow.start_run`, autolog **or** explicit `log_param` / `log_metric` / `log_artifact` / `sklearn` flavour):

1. Train **at least two** comparable runs that differ by model family **or** hyperparameters (e.g. `max_depth`, `C`, `n_estimators`).
2. For **each** run, log:
   - parameters (including `random_state` / seed),
   - train and validation (or CV) metrics appropriate to the task,
   - at least one artefact (saved model, confusion matrix / residual plot, or predictions sample).
3. Use a named experiment (e.g. `thesis-mlflow-demo`), not only the default experiment.
4. Keep the evaluation protocol fair: same split / same preprocessing across compared runs (fixed seed).

You may start from `train.py` in this folder and extend it.

---

## Part C — Model Registry (4 points)

1. Register the **best** run’s model in the MLflow Model Registry (name + version).
2. Assign a stage or alias appropriate to your MLflow version (e.g. `Staging` / `Production`, or a registry alias such as `champion`).
3. In the README (or a short report), explain **promotion criteria** in one short paragraph (e.g. “Production only if validation F1 ≥ baseline + 0.02”).
4. If Registry cannot run in your environment, document the blocker and instead version the model file + `run_id` in a clear folder layout — partial credit only; prefer a working Registry.

---

## Part D — Compare, select, reproduce (3 points)

1. Produce a **comparison** (UI screenshot **or** table exported via MLflow API / CLI) of the logged runs.
2. State which run wins and **why** (metric + any trade-off such as complexity).
3. Reproducibility section must include:
   - how to recover params from the winning `run_id`,
   - dataset URL / hash or version note,
   - git commit (or “dirty tree” note) used for the winning run,
   - exact commands to re-train that configuration.

Example:

```bash
mlflow runs describe --run-id <RUN_ID>
python train.py --config-from-run <RUN_ID>   # or equivalent flags matching logged params
```

---

## Quality requirements

- Comments / README clear enough for a reviewer to reproduce without asking you.
- No API keys or passwords in Git.
- Metrics must match the stated task (do not report only training score if you claim generalization).
- Prefer public data and cite the license.

---

## Deliverables

- GitHub repository with instrumented training code.
- Evidence of the Tracking UI (screenshot or exported comparison).
- Registered model (or documented fallback) with promotion rule.
- `README.md` with setup, run, UI, and reproducibility instructions.

---

## Suggested extensions (optional, not graded)

- Remote Tracking Server + artifact store (S3/MinIO).
- `mlflow models serve` for a local scoring API.
- Nested runs for hyperparameter search (e.g. with Optuna).
- Link this project to a Kedro or Airflow step that triggers training and logs to MLflow.
