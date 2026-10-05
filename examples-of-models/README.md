# Examples of Models (by Data Modality)

Short, self-contained assignment briefs for **different data modalities**. Each subfolder is one mini-project: pick a public dataset, train or adapt a suitable model, evaluate it, and document results.

Complete **one or more** subfolders as required by the course schedule. Each subfolder grades independently (**15 points** unless stated otherwise).

| Subfolder | Modality | Typical task |
|-----------|----------|--------------|
| [image-classification](image-classification/) | Images | Classify images with a CNN / transfer learning |
| [video-understanding](video-understanding/) | Video | Action / scene recognition from clips or frame sequences |
| [audio-classification](audio-classification/) | Audio | Classify sounds / speech from waveforms or spectrograms |
| [graph-learning](graph-learning/) | Graphs | Node or graph classification with a GNN or classical graph ML |
| [llm-text](llm-text/) | Text / LLM | Prompt or fine-tune/adapt an LLM for a text task |
| [generative-ai](generative-ai/) | Generative AI | Generate images/text/audio or embeddings with a generative model |

## Common rules (all subfolders)

1. Use **public** data; cite source and license.
2. Keep a reproducible environment (`requirements.txt` or `environment.yml` with pinned versions where practical).
3. Report metrics appropriate to the task; include at least one qualitative example (figure / sample output).
4. Write a short `README.md` in **your** submission repo: problem, data, model, results, limitations.
5. Prefer CPU-friendly or Colab-friendly setups unless the instructor provides GPU access.
