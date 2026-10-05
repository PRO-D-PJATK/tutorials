# Tutor6

---

### Task: "Create and Publish a Dockerized API with a Predictive Model"

#### Objectives:
1. Develop a simple API application that uses a predictive model.
2. Dockerize the application and run it locally.
3. Push the Docker image to DockerHub for public use.

---

### Instructions:

#### 1. Prerequisites
Make sure you have the following installed:
- Docker (https://www.docker.com/get-started)
- Python 3.x
- A DockerHub account (https://hub.docker.com/)

Log in to DockerHub via the terminal:
```bash
docker login
```

---

#### 2. Create the Application
1. Create a project directory:
   ```bash
   mkdir predictive-api && cd predictive-api
   ```

2. Install Python dependencies locally (optional, for testing):
   ```bash
   pip install fastapi uvicorn scikit-learn
   ```

3. Create a Python script for the API. Save it as `app.py` for your model, you can use existing model and just copy to Docker image:

Example:
   ```python
   from fastapi import FastAPI, HTTPException
   from pydantic import BaseModel
   from sklearn.linear_model import LinearRegression
   import numpy as np

   # Initialize FastAPI app
   app = FastAPI()

   # Example predictive model (Linear Regression)
   model = LinearRegression()
   X_train = np.array([[1], [2], [3], [4], [5]])
   y_train = np.array([2, 4, 6, 8, 10])  # Simple 2x function
   model.fit(X_train, y_train)

   # Request body model
   class PredictionRequest(BaseModel):
       input_value: float

   @app.get("/")
   def root():
       return {"message": "Welcome to the Predictive Model API!"}

   @app.post("/predict/")
   def predict(request: PredictionRequest):
       try:
           input_array = np.array([[request.input_value]])
           prediction = model.predict(input_array)
           return {"input": request.input_value, "prediction": prediction[0]}
       except Exception as e:
           raise HTTPException(status_code=500, detail=str(e))
   ```

4. Create a `requirements.txt` file:
   ```
   fastapi==0.95.2
   uvicorn==0.22.0
   scikit-learn==1.3.1
   numpy==1.25.2
   ```

---

#### 3. Create a Dockerfile
Add the following content to a `Dockerfile`:
```dockerfile
# Use an official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

#### 4. Build and Run the Docker Image
1. Build the Docker image:
   ```bash
   docker build -t your_dockerhub_username/predictive-api .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 your_dockerhub_username/predictive-api
   ```

3. Test the API locally:
   - Open your browser at [http://localhost:8000](http://localhost:8000) for the root endpoint.
   - Use a tool like Postman or `curl` to test the `/predict/` endpoint. Example:
     ```bash
     curl -X POST "http://localhost:8000/predict/" -H "Content-Type: application/json" -d '{"input_value": 3.5}'
     ```

---

#### 5. Push to DockerHub
1. Tag the image:
   ```bash
   docker tag your_dockerhub_username/predictive-api:latest your_dockerhub_username/predictive-api:v1
   ```

2. Push the image to DockerHub:
   ```bash
   docker push your_dockerhub_username/predictive-api:v1
   ```

3. Verify the image is available on DockerHub.

---

#### 6. Test Public Usage
Share your DockerHub image URL with others so they can run your container:
```bash
docker run -p 8000:8000 your_dockerhub_username/predictive-api:v1
```

---

### Optional Enhancements
- Replace the Linear Regression model with a more complex one, such as a pre-trained ML model from `sklearn` or `tensorflow`.
- Add input validation or multiple endpoints for different types of predictions.
- Automate the build and deployment process using GitHub Actions or another CI/CD tool.

Good luck! 🚀
