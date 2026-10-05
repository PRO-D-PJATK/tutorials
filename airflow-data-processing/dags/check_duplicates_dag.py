import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests

# Dataset URL
DATASET_URL = "https://vincentarelbundock.github.io/Rdatasets/csv/AER/CollegeDistance.csv"
CSV_FILE_PATH = "/opt/airflow/dags/files/CollegeDistance.csv"

# Download the dataset
def download_dataset():
    response = requests.get(DATASET_URL)
    with open(CSV_FILE_PATH, "wb") as file:
        file.write(response.content)
    print(f"Dataset downloaded to {CSV_FILE_PATH}")

# Check for and remove duplicates
def check_and_remove_duplicates():
    # Load data
    df = pd.read_csv(CSV_FILE_PATH)

    # Inspect duplicates
    num_duplicates = df.duplicated().sum()
    if num_duplicates > 0:
        print(f"Found {num_duplicates} duplicates. Removing them.")
        df = df.drop_duplicates()
        df.to_csv(CSV_FILE_PATH, index=False)
    else:
        print("No duplicates found.")

    print(f"Data processed and saved to {CSV_FILE_PATH}")

# DAG configuration
with DAG(
        "check_duplicates_dag",
        #start_date=datetime(2023, 1, 1),
        schedule_interval=None,
        catchup=False,
) as dag:

    # Task: download dataset
    download_task = PythonOperator(
        task_id="download_dataset",
        python_callable=download_dataset
    )

    # Task: check and remove duplicates
    check_duplicates_task = PythonOperator(
        task_id="check_and_remove_duplicates",
        python_callable=check_and_remove_duplicates
    )

    # Task dependencies
    download_task >> check_duplicates_task
