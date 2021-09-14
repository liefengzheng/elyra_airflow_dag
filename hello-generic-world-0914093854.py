from airflow import DAG

from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.utils.dates import days_ago

args = {
    "project_id": "hello-generic-world-0914093854",
}

dag = DAG(
    "hello-generic-world-0914093854",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="A generic pipeline tutorial",
    is_paused_upon_creation=False,
)


op_7ceed5ef_0222_44b9_be88_70398f7dff04 = KubernetesPodOperator(
    name="load_weather_data",
    namespace="default",
    image="amancevice/pandas:1.1.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://20.94.160.112:9000/ --cos-bucket elyra-bucket --cos-directory 'hello-generic-world-0914093854' --cos-dependencies-archive 'load_data-7ceed5ef-0222-44b9-be88-70398f7dff04.tar.gz' --file 'Local Disk/examples/pipelines/introduction-to-generic-pipelines/load_data.ipynb' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    task_id="load_weather_data",
    env_vars={
        "DATASET_URL": "https://dax-cdn.cdn.appdomain.cloud/dax-noaa-weather-data-jfk-airport/1.1.4/noaa-weather-data-jfk-airport.tar.gz",
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "30UjjBGEwGEwVH9aDXgi",
        "AWS_SECRET_ACCESS_KEY": "q5lFOhkafzWJ1TFI7JsRYdN09DYBEMxXMgplhSei",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "hello-generic-world-0914093854-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)


op_793c2b82_78c1_4d52_a5d6_163b62d8fe58 = KubernetesPodOperator(
    name="data_clean",
    namespace="default",
    image="amancevice/pandas:1.1.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://20.94.160.112:9000/ --cos-bucket elyra-bucket --cos-directory 'hello-generic-world-0914093854' --cos-dependencies-archive 'Part 1 - Data Cleaning-793c2b82-78c1-4d52-a5d6-163b62d8fe58.tar.gz' --file 'Local Disk/examples/pipelines/introduction-to-generic-pipelines/Part 1 - Data Cleaning.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv' "
    ],
    task_id="data_clean",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "30UjjBGEwGEwVH9aDXgi",
        "AWS_SECRET_ACCESS_KEY": "q5lFOhkafzWJ1TFI7JsRYdN09DYBEMxXMgplhSei",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "hello-generic-world-0914093854-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_793c2b82_78c1_4d52_a5d6_163b62d8fe58 << op_7ceed5ef_0222_44b9_be88_70398f7dff04
