"""
Minimal MLflow starter: two sklearn runs on a built-in dataset.

Usage:
  export MLFLOW_TRACKING_URI=./mlruns
  python train.py
  mlflow ui --backend-store-uri ./mlruns --port 5000

Extend this script for your own public dataset and model variants.
"""

from __future__ import annotations

import argparse

import mlflow
import mlflow.sklearn
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="MLflow demo training script")
    p.add_argument("--experiment", default="thesis-mlflow-demo")
    p.add_argument("--test-size", type=float, default=0.25)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument(
        "--register-best",
        action="store_true",
        help="Register the better of the two demo runs in the Model Registry",
    )
    p.add_argument(
        "--model-name",
        default="breast-cancer-clf",
        help="Registry model name when --register-best is set",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()
    mlflow.set_experiment(args.experiment)

    X, y = load_breast_cancer(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=args.test_size, random_state=args.seed, stratify=y
    )

    candidates: list[tuple[str, object, dict]] = [
        (
            "logistic_regression",
            LogisticRegression(max_iter=500, random_state=args.seed),
            {"model": "logistic_regression", "max_iter": 500},
        ),
        (
            "random_forest",
            RandomForestClassifier(
                n_estimators=100, max_depth=5, random_state=args.seed
            ),
            {
                "model": "random_forest",
                "n_estimators": 100,
                "max_depth": 5,
            },
        ),
    ]

    best_run_id: str | None = None
    best_f1 = -1.0

    for run_name, model, params in candidates:
        with mlflow.start_run(run_name=run_name) as run:
            mlflow.log_params(params)
            mlflow.log_param("seed", args.seed)
            mlflow.log_param("test_size", args.test_size)

            model.fit(X_train, y_train)
            pred = model.predict(X_test)
            acc = accuracy_score(y_test, pred)
            f1 = f1_score(y_test, pred)

            mlflow.log_metric("accuracy", acc)
            mlflow.log_metric("f1", f1)
            mlflow.sklearn.log_model(model, artifact_path="model")

            print(f"{run_name}: accuracy={acc:.4f} f1={f1:.4f} run_id={run.info.run_id}")

            if f1 > best_f1:
                best_f1 = f1
                best_run_id = run.info.run_id

    if args.register_best and best_run_id is not None:
        model_uri = f"runs:/{best_run_id}/model"
        mv = mlflow.register_model(model_uri, args.model_name)
        print(
            f"Registered {args.model_name} version={mv.version} "
            f"from run_id={best_run_id} (f1={best_f1:.4f})"
        )


if __name__ == "__main__":
    main()
