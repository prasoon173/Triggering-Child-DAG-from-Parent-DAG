from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from airflow.utils.dates import days_ago
import datetime

default_dag_args = {
    'owner': 'airflow',
    'start_date' : days_ago(1),
    'email_on_failure':False,
    'email_on_retries': False,
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=1)
}

with DAG (
    'Parent_dag',
    schedule_interval="@once",
    default_args=default_dag_args
)as dag:
    start=DummyOperator(
        task_id='start'
    )
    dag_1=TriggerDagRunOperator(
        task_id='dag_1',
        trigger_dag_id='dag-to-trigger',
        conf={"message":"Triggering Child DAG from Parent DAG"}
    )
    dag_2=TriggerDagRunOperator(
        task_id='dag_2',
        trigger_dag_id='dag-to-trigger',
        conf={"message":"Triggering Child DAG from Parent DAG"}
    )
    some_other_task=DummyOperator(
        task_id='some-other-task'
    )
    end=DummyOperator(
        task_id='end'
    )

    start>>dag_1>>some_other_task>>dag_2>>end
