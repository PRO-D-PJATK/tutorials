# Kedro Pipelines for Reproducible Data Science

Build a small **Kedro** project that turns raw data into a trained model through named datasets, modular pipelines, and configuration — without hard-coded paths.

**Total: 15 points**

Docs: [Kedro documentation](https://docs.kedro.org/)

---

## Objectives

1. Scaffold a Kedro project and understand its layout (`conf/`, `data/`, `src/`, `pipelines/`).
2. Register datasets in the catalog (`catalog.yml`) instead of reading files with ad-hoc paths.
3. Implement a pipeline with at least **three nodes** (e.g. load → clean/features → train/evaluate).
4. Run the pipeline with `kedro run` and document parameters / environments.

---

## Prerequisites

- Python 3.9+
- `pip install kedro kedro-datasets pandas scikit-learn`
- Basic familiarity with pandas and a simple ML model (classification or regression)

---

## Part A — Project setup (4 points)

1. Create a new Kedro project (starter of your choice, e.g. `spaceflights` starter **or** empty/`astro-airflow` is not required — a minimal starter is enough):

   ```bash
   kedro new --name=thesis_kedro_demo
   cd thesis_kedro_demo
   pip install -r requirements.txt
   ```

2. In `README.md`, briefly describe:
   - what the project predicts / produces,
   - which dataset you use (public URL + license note),
   - how to install and run.

3. Keep secrets and local overrides out of Git (use `conf/local/` + `.gitignore` as Kedro suggests).

---

## Part B — Data catalog (4 points)

1. Place a raw dataset under `data/01_raw/` (or download it in a documented first step).
2. Declare at least:
   - one **raw** dataset,
   - one **intermediate** / cleaned dataset,
   - one **model** or metrics artefact  
   in `conf/base/catalog.yml` using appropriate dataset types (`pandas.CSVDataset`, `pickle.PickleDataset`, etc.).
3. Do **not** hard-code absolute paths in node code — nodes must receive data via Kedro inputs/outputs only.

---

## Part C — Pipeline nodes (8 points)

Implement a pipeline (one or more pipeline modules) with nodes that:

1. **Load / validate** raw data (shape checks, required columns).
2. **Transform** data (cleaning and/or feature engineering). Optional: parameters in `parameters.yml` (e.g. test size, random seed).
3. **Train and evaluate** a simple model; save metrics (e.g. accuracy / RMSE) as a catalog entry or JSON/YAML report under `data/08_reporting/`.

Requirements:

- Each node is a pure-ish function with typed inputs/outputs declared in the pipeline.
- Use `kedro run` successfully end-to-end.
- Optional: `kedro viz` screenshot or exported pipeline diagram in the repository.

---

## Part D — Configuration and reproducibility (4 points)

1. Put tunable values in `conf/base/parameters.yml` (seed, split ratio, model hyperparameter).
2. Document how to run:

   ```bash
   kedro run
   kedro run --pipeline=<name>   # if you split pipelines
   ```

3. Add a short “Reproducibility” section: Python version, Kedro version, how to recreate the environment.

---

## Deliverables

- GitHub repository with the Kedro project.
- Working `kedro run`.
- Clear `README.md` with setup + run instructions.
- Catalog + parameters committed (no secrets).

---

## Suggested extensions (optional, not graded)

- Split into `data_processing` and `model` pipelines.
- Add a second environment (`conf/test/`) with a tiny sample CSV.
- Hook the pipeline into CI (`kedro run` on push).
