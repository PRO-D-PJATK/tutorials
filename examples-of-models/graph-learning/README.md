# Graph Learning

Solve a graph machine-learning task: node classification, link prediction, or whole-graph classification.

**Points: 15**

---

## Task

1. **Data (4 pts)** — Choose a public graph dataset (e.g. Cora, Citeseer, PubMed via PyTorch Geometric / DGL tutorials, or a molecular graph set such as MUTAG). Document:
   - nodes, edges, features, labels,
   - train/val/test protocol used by the benchmark.
2. **Model (5 pts)** — Implement one of:
   - GCN / GraphSAGE / GAT (or similar GNN), **or**
   - a classical baseline (e.g. logistic regression on node features **without** graph structure) **plus** a graph-aware model for comparison.
3. **Training (3 pts)** — Document hyperparameters, seed, and early stopping if used.
4. **Evaluation (3 pts)** — Report the official metric for the task (accuracy / F1 / AUC). Briefly discuss how graph structure helped (or did not) versus a feature-only baseline.

## Deliverables

- Code + environment file (`torch` + PyG/DGL as needed)
- Dataset description and metric table
- Short reflection on inductive vs transductive setting (if applicable)

## Suggested public datasets

- Cora / CiteSeer / PubMed (citation networks)  
- MUTAG / PROTEINS (graph classification)  
- A small custom knowledge-graph sample — only if fully documented and public
