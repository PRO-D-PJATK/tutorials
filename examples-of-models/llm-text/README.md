# LLM / Text Modeling

Use a large language model (or a strong transformer text model) for a concrete NLP task.

**Points: 13**

---

## Task

1. **Problem & data (3 pts)** — Define a text task: classification, short summarization, Q&A on a small corpus, or information extraction. Use a public dataset or a clearly licensed sample. Document size, labels, and split.
2. **Approach (5 pts)** — Choose **one** primary approach and justify it:
   - **Prompting** a hosted or local LLM (zero-shot / few-shot), **or**
   - **Parameter-efficient fine-tuning** (LoRA/QLoRA) of an open model, **or**
   - Fine-tuning / feature extraction with a smaller encoder (BERT-family) if LLM fine-tuning is not feasible.
3. **Implementation (3 pts)** — Provide runnable code or Colab. Log model name/version, prompts (if any), temperature/decoding settings, and seed where relevant.
4. **Evaluation (4 pts)** — Use task-appropriate metrics (Accuracy/F1, or a small human rubric for generation). Include qualitative examples (good and bad outputs). Discuss cost, latency, and hallucination / error risks.

## Deliverables

- Code or notebook + dependency list
- Prompt templates or training config
- Metrics + error analysis

## Constraints

- Prefer **open-weight** or freely accessible models when possible.
- Do not commit API keys; use environment variables.
- Keep experiments small enough to reproduce on a student machine or free Colab tier.
