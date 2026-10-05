# Dockerized Predictive API

Build a small predictive application (API or CLI), run it in Docker, publish the image to Docker Hub, and document how others can use it.

**Total: 20 points** (+ optional 10)

Docs: [Get started with Docker](https://www.docker.com/get-started) · [Docker Hub](https://hub.docker.com/)

---

## Objectives

1. Implement a predictive script/API that accepts structured input and returns a prediction.
2. Package it in an optimized Docker image and run it locally.
3. Publish the image to Docker Hub.
4. Provide a complete project `README.md` (clone, local run, Docker run, Hub pull).

---

## Prerequisites

- Docker
- Python 3.x
- Docker Hub account

```bash
docker login
```

---

## Part A — Predictive application (5 points)

Create a project directory (e.g. `predictive-api`) with:

- A prediction entrypoint using **FastAPI**, **Flask**, or a **CLI**.
- Input in **JSON** and/or **CSV**; clear output with the predicted value(s).
- You may reuse an existing trained model (copy weights/artefacts into the image) or train a simple model inside the app for the demo.

Example FastAPI sketch (`app.py`):

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.linear_model import LinearRegression
import numpy as np

app = FastAPI()

model = LinearRegression()
X_train = np.array([[1], [2], [3], [4], [5]])
y_train = np.array([2, 4, 6, 8, 10])
model.fit(X_train, y_train)

class PredictionRequest(BaseModel):
    input_value: float

@app.get("/")
def root():
    return {"message": "Welcome to the Predictive Model API!"}

@app.post("/predict/")
def predict(request: PredictionRequest):
    try:
        prediction = model.predict(np.array([[request.input_value]]))
        return {"input": request.input_value, "prediction": float(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

Example `requirements.txt`:

```
fastapi==0.95.2
uvicorn==0.22.0
scikit-learn==1.3.1
numpy==1.25.2
```

---

## Part B — Dockerfile and local container run (5 points)

Provide a `Dockerfile` that:

- Uses a slim base image where practical.
- Installs only required dependencies.
- Exposes the service port (e.g. `8000`).
- Starts the app with a clear `CMD`.

Example:

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:

```bash
docker build -t your_dockerhub_username/predictive-api .
docker run -p 8000:8000 your_dockerhub_username/predictive-api
```

Smoke-test (API example):

```bash
curl -X POST "http://localhost:8000/predict/" \
  -H "Content-Type: application/json" \
  -d '{"input_value": 3.5}'
```

---

## Part C — Publish to Docker Hub (5 points)

```bash
docker tag your_dockerhub_username/predictive-api:latest your_dockerhub_username/predictive-api:v1
docker push your_dockerhub_username/predictive-api:v1
```

Verify the image is visible on Docker Hub. Others should be able to run:

```bash
docker run -p 8000:8000 your_dockerhub_username/predictive-api:v1
```

---

## Part D — Repository documentation (5 points)

GitHub repository must include application code, model artefacts (if any), `Dockerfile`, and a `README.md` covering:

1. How to clone the repository.
2. How to run the application locally (without Docker).
3. How to build and run with Docker.
4. How to pull and run the image from Docker Hub.

---

## Optional bonus (+10 points)

Write an **Airflow DAG** that automatically **builds and publishes** the Docker image (CI-style automation of Parts B–C).

---

## Suggested enhancements (not graded separately)

- Stronger / pre-trained model instead of the toy regressor.
- Input validation and multiple prediction endpoints.
- GitHub Actions (or similar) for build & push.
