from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

with DAG(
    "DockerOperator_DAG_example",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    DockerOperator(
        task_id="your_taskname",
        image="your_docker_image_name",
        auto_remove="success",  
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge"
    )