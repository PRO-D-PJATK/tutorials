# Generative AI Mini-Project

Build a small generative pipeline: create new content (text, image, audio) or generative embeddings with a clear evaluation of quality and risks.

**Points: 14**

---

## Task

1. **Use case (3 pts)** — State a concrete generative goal, e.g.:
   - image generation / editing (diffusion),
   - text generation with constraints (style, length, format),
   - synthetic data generation for augmentation,
   - music / sound generation (short clips),
   - multimodal generation (caption → image or image → caption).
2. **Model & pipeline (5 pts)** — Use a public generative model or API. Document:
   - model name/version,
   - prompts / conditioning inputs,
   - decoding or sampler settings,
   - safety filters if any.
3. **Outputs (3 pts)** — Produce a small gallery/table of generations (at least 5 samples) with the prompts/seeds used.
4. **Evaluation & ethics (4 pts)** — Combine:
   - automatic metric **or** structured human rubric (relevance, quality, diversity),
   - discussion of risks (copyright, bias, hallucination, deepfake misuse),
   - limitations of your setup.

## Deliverables

- Code/notebook + environment notes
- Sample outputs (images/audio snippets/text) — keep repository size reasonable
- Short ethics/limitations section in the README

## Notes

- Prefer open models (e.g. small diffusion checkpoints, open LLMs) when hardware allows.
- Never commit secrets. Respect dataset and model licenses.
- If using hosted APIs, log approximate cost and rate limits.
