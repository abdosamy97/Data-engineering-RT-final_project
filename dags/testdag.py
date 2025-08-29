from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'AbdelrahmanSamy',
    'depends_on_past': False,
    'email': ['abdobesso1001@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'test_dag_asamy',
    default_args=default_args,
    description='A simple test DAG',
    schedule_interval=timedelta(days=1), 
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=['test'],
) as dag:

    task1 = BashOperator(
        task_id='print_hello',
        bash_command='echo "Hello from Airflow DAG!"'
    )

    task2 = BashOperator(
        task_id='print_date',
        bash_command='date'
    )

    task1 >> task2