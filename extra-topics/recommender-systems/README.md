# Recommender Systems

Build a small recommender on public interaction data.

**Points: 15**

---

## Task

1. **Data (3 pts)** — Use a public ratings/interactions set (e.g. MovieLens 100K, a books subset). Document sparsity and train/test split policy (time-based if timestamps exist).
2. **Models (6 pts)** — Implement at least **two** approaches, e.g.:
   - collaborative filtering (user/item KNN or matrix factorization),
   - content-based (item features / TF-IDF),
   - simple popularity baseline.
3. **Metrics (4 pts)** — Report ranking metrics suitable for recommenders (Precision@K, Recall@K, or NDCG@K). Compare against the popularity baseline.
4. **Qualitative check (2 pts)** — Show example recommendations for 2–3 users and comment on diversity / obviousness.

## Deliverables

- Code + evaluation results
- Example recommendation lists
- Discussion of cold-start limitations
