from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="simple_dag",
    schedule_interval="*/5 * * * *",
    start_date=datetime(2022, 2, 5)
) as dag:
    first_task = BashOperator(
        task_id="print_name",
        bash_command="echo irfan"
    )

    second_task = BashOperator(
        task_id="print_date",
        bash_command="date",
    )

    first_task >> second_task