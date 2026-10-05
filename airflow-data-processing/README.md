# Airflow Data Processing

Create two Apache Airflow DAGs for a small data pipeline: download & split, then clean & standardize. Prefer running Airflow via Docker Compose.

**Total: 16 points** (+ optional extras)

Reference: [Airflow with Docker Compose](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)

This folder also includes example `docker-compose.yml`, sample DAGs under `dags/`, and a CI workflow you may adapt.

---

## Prerequisites

1. Apache Airflow (local install **or** Docker Compose from this folder).
2. Python data libraries: `pandas`, `scikit-learn` (and `gspread` if you use Google Sheets).
3. Optional but recommended for full credit on cloud steps: Google Cloud / Sheets access (OAuth or service account).

---

## DAG 1 — Download and split (8 points)

**Goal:** Fetch a dataset and split it for modeling vs further fine-tuning / hold-out use.

1. **Download operator (4 points)**  
   - Task that downloads data from a public URL or reads a local `.csv` path available to the worker.

2. **Split operator (6 points)**  
   - Split into **70%** modeling set and **30%** fine-tuning / secondary set using `sklearn.model_selection.train_test_split`.  
   - Use a fixed `random_state` for reproducibility.

3. **Extra — persist to Google Sheets / cloud (+5 points)**  
   - Upload both splits to separate sheets or cloud locations (e.g. “Training Dataset”, “Fine-Tuning Dataset”).  
   - Configure OAuth 2.0 or a service account. Tip: `gspread`.

---

## DAG 2 — Clean and standardize (8 points)

**Goal:** Process the modeling split (from local artefacts of DAG 1 and/or Sheets/cloud).

1. **Load operator (1–2 points)**  
   - Retrieve the modeling dataset produced by DAG 1.

2. **Cleaning operator (4 points)**  
   - Handle missing values (drop or impute with a documented strategy).  
   - Detect and remove duplicates when appropriate.

3. **Standardization / normalization operator (4–6 points)**  
   - Scale features (e.g. `StandardScaler`) and/or rescale to a range (`MinMaxScaler`).  
   - Document which columns are transformed and why.

4. **Save operator (2 points)**  
   - Write the processed dataset back to local storage and/or Google Sheets / cloud.

---

## Quality requirements

- Comment DAGs so a reviewer can follow task order and data paths.
- Both DAGs must be configured correctly and run successfully in Airflow.
- Keep secrets out of Git (use env vars / Airflow connections / `.gitignore`).

---

## Deliverables

- Link to your DAG code (repository).
- Screenshots (or equivalent logs) showing successful runs of both DAGs.
- If you claim the Sheets/cloud extra points, include proof of uploaded artefacts.

Good luck!
