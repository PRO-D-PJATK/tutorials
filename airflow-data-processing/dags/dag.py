from datetime import datetime
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

# Example function used by PythonOperator
def my_function():
    print("Hello from Airflow!")

# DAG definition
with DAG(
        "my_first_dag",
        default_args={"owner": "airflow", "start_date": datetime(2023, 1, 1)},
        schedule_interval="@daily",
        catchup=False,
) as dag:

    start = DummyOperator(task_id="start")
    python_task = PythonOperator(task_id="python_task", python_callable=my_function)
    end = DummyOperator(task_id="end")

    start >> python_task >> end
