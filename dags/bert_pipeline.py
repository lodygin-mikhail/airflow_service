from datetime import datetime, timedelta

from airflow.providers.docker.operators.docker import DockerOperator
from airflow import DAG

default_args = {
    'owner': 'Mikhail',
    'start_date': datetime(2025, 11, 26),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id="bert_pipeline",
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule=timedelta(minutes=5),
    catchup=False,
    tags={'sentiment', 'worker', 'docker'},
):
    run_bert = DockerOperator(
        task_id="bert_run",
        image="bert_service:latest",
        command="python main.py",
        auto_remove="force",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
    )