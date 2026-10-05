# Video Understanding

Build a simple video recognition pipeline: classify short clips or frame sequences.

**Points: 16**

---

## Task

1. **Data (4 pts)** — Select a public video / action dataset or a **small curated subset** (e.g. a few classes from UCF-101, HMDB51, or a Kaggle action set). Document:
   - number of clips per class,
   - frame rate / resolution after preprocessing,
   - clip length (e.g. 16 frames).
2. **Representation (3 pts)** — Choose one approach and justify it:
   - frame sampling + 2D CNN + temporal aggregation, **or**
   - a lightweight 3D / video model, **or**
   - pretrained frame embeddings + classifier.
3. **Model & training (4 pts)** — Train a classifier; keep the setup Colab/GPU-friendly. Log hyperparameters and seed.
4. **Evaluation (4 pts)** — Report accuracy / F1. Show at least two qualitative examples (key frames + predicted vs true label). Discuss limitations (motion blur, short clips, class imbalance).

## Deliverables

- Code + environment file
- Preprocessing description (how frames are extracted)
- Metrics and example visualizations

## Notes

- Full UCF-101 training is **not** required — a reduced class subset is acceptable if clearly documented.
- Prefer storing extracted frames/features rather than huge raw videos in Git (use `.gitignore` + download script).
