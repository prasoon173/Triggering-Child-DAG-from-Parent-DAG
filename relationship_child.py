from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago
import datetime

default_dag_args={
    'owner':'airflow',
    'email_on_failure':False,
    'email_on_retries':False,
    'start_date':days_ago(1),
    'retries':1,
    'retry_delay':datetime.timedelta(minutes=5)
}

with DAG(
    'dag-to-trigger',
    schedule_interval=None,
    default_args=default_dag_args
)as dag:
    dag_task=DummyOperator(
        task_id='dag-task'
    )
