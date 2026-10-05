from airflow import Dataset
from airflow.decorators import task, dag
from datetime import datetime

# Create a dataset
my_dataset = Dataset("/home/piotr/Downloads/CollegeDistance.csv")

# DAG that publishes data to the dataset
@dag(schedule_interval="@daily", start_date=datetime(2023, 1, 1), catchup=False)
def producer_dag():
    @task(outlets=[my_dataset])  # Declare publication to the dataset
    def publish_data():
        print("Publishing data to dataset.")

    publish_data()

# DAG that subscribes to the dataset
@dag(schedule=[my_dataset], start_date=datetime(2023, 1, 1), catchup=False)
def consumer_dag():
    @task
    def consume_data():
        print("Consuming data from dataset.")

    consume_data()

producer_dag()
consumer_dag()
