# Image Classification

Train an image classifier on a public dataset using a CNN or transfer learning.

**Points: 11**

---

## Task

1. **Data (3 pts)** — Choose a public image dataset (e.g. CIFAR-10, Fashion-MNIST, a Kaggle subset, or a small custom public set). Document class counts, image size, and train/val/test split. Show a small sample grid.
2. **Model (5 pts)** — Train either:
   - a small CNN from scratch, **or**
   - a fine-tuned pretrained model (ResNet, MobileNet, EfficientNet, etc.).
3. **Training (3 pts)** — Document optimizer, learning rate, epochs, augmentation, and hardware. Use a fixed random seed.
4. **Evaluation (4 pts)** — Report accuracy (and F1 if classes are imbalanced). Include a confusion matrix and 3–5 correct/incorrect prediction examples.

## Deliverables

- Notebook or scripts + `requirements.txt`
- Metrics table + figures
- Short discussion of failure modes (blur, class confusion, etc.)

## Suggested public datasets

- CIFAR-10 / CIFAR-100  
- Fashion-MNIST  
- Oxford-IIIT Pets (if compute allows)
