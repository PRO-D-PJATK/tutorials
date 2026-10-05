# MLOps CI/CD for Models

Automate tests and packaging for a small ML project so every change is checked before “release”.

**Points: 14**

---

## Task

1. **Project baseline (3 pts)** — A small training + inference script/module with pinned dependencies.
2. **Data & model tests (5 pts)** — CI jobs that run at least:
   - data schema / null checks on a sample,
   - a fast training smoke test (tiny data),
   - a prediction shape/type test on a saved model or stub.
3. **Pipeline (4 pts)** — GitHub Actions (or equivalent) on push/PR: lint or format (optional), tests, and artefact build (wheel, Docker image, or model tarball).
4. **Release checklist (3 pts)** — Document staging vs production criteria (metrics threshold, approval, rollback). Mark what is automated vs manual.

## Deliverables

- `.github/workflows/*.yml` (or other CI config)
- Test suite
- Short MLOps checklist in README
