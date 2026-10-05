# Responsible AI and Fairness

Measure and document fairness risks for a predictive model.

**Points: 13**

---

## Task

1. **Problem framing (3 pts)** — Pick a public dataset with a sensitive attribute suitable for analysis (use carefully; document ethical context). State the prediction target and who might be harmed by errors.
2. **Baseline model (3 pts)** — Train a simple model; report overall metrics.
3. **Fairness metrics (6 pts)** — Compute at least two group metrics (e.g. demographic parity difference, equalized odds / TPR–FPR gaps, calibration by group). Visualize disparities.
4. **Mitigation & documentation (3 pts)** — Try one mitigation (reweighing, threshold adjustment, or feature exclusion) **or** justify why mitigation was not applied. Write a short **model card** (intended use, limits, fairness findings).

## Deliverables

- Fairness analysis notebook/report
- Model card section
- Clear statement of limitations and data ethics

## Caution

Handle demographic attributes responsibly. Do not publish deanonymizing artefacts. Prefer well-known academic fairness datasets.
