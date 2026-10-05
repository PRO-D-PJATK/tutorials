# Audio Classification

Classify audio clips using waveform or spectrogram features.

**Points: 12**

---

## Task

1. **Data (3 pts)** — Use a public audio dataset (e.g. UrbanSound8K subset, ESC-50 subset, Free Spoken Digit Dataset, or speech commands subset). Document sampling rate, duration, and class balance.
2. **Features (4 pts)** — Convert audio to a model-ready form:
   - Mel-spectrogram / MFCC, **or**
   - raw waveform model (if justified).  
   Show example waveforms and spectrograms.
3. **Model (4 pts)** — Train a classifier (CNN on spectrograms, simple RNN/transformer, or classical ML on MFCCs). Document architecture and training setup.
4. **Evaluation (4 pts)** — Accuracy / F1, confusion matrix, and 2–3 misclassified examples with a short error analysis (noise, overlap, short duration).

## Deliverables

- Code + `requirements.txt` (e.g. `librosa`, `torchaudio`, or equivalent)
- Feature/preprocessing notes
- Metrics and plots

## Suggested public datasets

- Free Spoken Digit Dataset (FSDD)  
- ESC-50 (use a subset if needed)  
- Speech Commands (subset of classes)
