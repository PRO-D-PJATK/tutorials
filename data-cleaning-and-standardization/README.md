# Data Cleaning and Standardization

Prepare a thesis-related dataset for later analysis or modeling: load it into a database, clean it, then standardize/normalize it with reusable, well-structured code. Work in **one repository** across both parts of the assignment.

**Total: 14 points** (7 + 7)

---

## General expectations

1. **Database selection** — Choose a dataset aligned with your future diploma thesis. It should need real cleaning, but stay manageable for this course.
2. **Data cleaning** — Handle missing values, wrong types, duplicates, and outliers.
3. **Data standardization** — Harmonize formats, categories, dates; scale numerical features where needed.
4. **Reproducibility** — Paths, credentials, and local settings go in a config file excluded via `.gitignore`.
5. **Version control** — Meaningful commits, feature branches, and peer-reviewed pull requests.

---

## Part 1 — Setup, database, and cleaning (7 points)

### 1. Git repository setup (2 points)

- Create a private GitHub repository with a clear `README.md`.
- Do main work on a feature branch; merge to `main` via pull request after peer review.
- Add `.gitignore` that excludes the database dump and secrets (e.g. `.env`, `config.json`).
- Document project goal, data source, and local setup in `README.md`.

### 2. Database usage (2 points)

- Choose a database fitting the topic (MySQL, PostgreSQL, MongoDB, SQLite, etc.).
- Connect using credentials stored outside Git.
- Load the dataset from a local or remote source into the database.

### 3. Data cleaning (3 points)

- Handle missing data (imputation, removal, or justified defaults).
- Detect and handle outliers; remove duplicates.
- Correct column data types (numeric, categorical, datetime).
- Comment each cleaning step with a short rationale.

---

## Part 2 — Standardization, DB updates, and code quality (7 points)

Continue in the **same repository** (e.g. rename / tag work as the standardization stage). Prefer a dedicated branch such as `data-standardization`.

### 1. Git updates and structure (2 points)

- Feature branch → peer-reviewed PR → merge to `main`.
- Consistent, informative commit messages.
- Refactor layout if needed (`data_cleaning.py`, `data_standardization.py`, modules/folders).

### 2. Database interaction and updates (2 points)

- Persist cleaned (and then standardized) data with appropriate `INSERT` / `UPDATE` / `DELETE` (or equivalent).
- Automate load / update scripts; keep credentials out of Git.
- Prefer efficient queries for retrieve and update paths.

### 3. Standardization and code quality (3 points)

- **Normalization / standardization** of numeric features (e.g. Min–Max, Z-score).
- **Categorical consistency** (unified labels / encodings as appropriate).
- **Date/time** in a single format (e.g. ISO 8601).
- Modular, reusable functions; avoid duplication.
- Robust error handling (connection failures, import errors).
- Clear comments and an updated `README.md` with run instructions.

---

## Deliverables

- Repository URL.
- Evidence of PRs / peer review for both parts.
- Runnable scripts and documentation sufficient to reproduce cleaning and standardization locally.
