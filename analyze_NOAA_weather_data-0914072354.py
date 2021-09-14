from airflow import DAG

from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.utils.dates import days_ago

args = {
    "project_id": "analyze_NOAA_weather_data-0914072354",
}

dag = DAG(
    "analyze_NOAA_weather_data-0914072354",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Tutorial pipeline for generic components",
    is_paused_upon_creation=False,
)


op_c88d9c0b_a5d5_45ab_88d6_eb6ce24ffdbb = KubernetesPodOperator(
    name="load_data",
    namespace="default",
    image="docker.io/amancevice/pandas:1.1.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://20.94.160.112:9000/ --cos-bucket elyra-bucket --cos-directory 'analyze_NOAA_weather_data-0914072354' --cos-dependencies-archive 'load_data-c88d9c0b-a5d5-45ab-88d6-eb6ce24ffdbb.tar.gz' --file 'Local Disk/examples/pipelines/dax_noaa_weather_data/load_data.ipynb' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    task_id="load_data",
    env_vars={
        "DATASET_URL": "https://dax-cdn.cdn.appdomain.cloud/dax-noaa-weather-data-jfk-airport/1.1.4/noaa-weather-data-jfk-airport.tar.gz",
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "30UjjBGEwGEwVH9aDXgi",
        "AWS_SECRET_ACCESS_KEY": "q5lFOhkafzWJ1TFI7JsRYdN09DYBEMxXMgplhSei",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "analyze_NOAA_weather_data-0914072354-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)


op_e07e1b7f_568b_4bc3_9fc6_da372fd58daf = KubernetesPodOperator(
    name="Part_1___Data_Cleaning",
    namespace="default",
    image="docker.io/amancevice/pandas:1.1.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://20.94.160.112:9000/ --cos-bucket elyra-bucket --cos-directory 'analyze_NOAA_weather_data-0914072354' --cos-dependencies-archive 'Part 1 - Data Cleaning-e07e1b7f-568b-4bc3-9fc6-da372fd58daf.tar.gz' --file 'Local Disk/examples/pipelines/dax_noaa_weather_data/Part 1 - Data Cleaning.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv' "
    ],
    task_id="Part_1___Data_Cleaning",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "30UjjBGEwGEwVH9aDXgi",
        "AWS_SECRET_ACCESS_KEY": "q5lFOhkafzWJ1TFI7JsRYdN09DYBEMxXMgplhSei",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "analyze_NOAA_weather_data-0914072354-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_e07e1b7f_568b_4bc3_9fc6_da372fd58daf << op_c88d9c0b_a5d5_45ab_88d6_eb6ce24ffdbb


op_982e672a_4ae5_4608_bcb0_ce309868415a = KubernetesPodOperator(
    name="Part_2___Data_Analysis",
    namespace="default",
    image="docker.io/amancevice/pandas:1.1.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://20.94.160.112:9000/ --cos-bucket elyra-bucket --cos-directory 'analyze_NOAA_weather_data-0914072354' --cos-dependencies-archive 'Part 2 - Data Analysis-982e672a-4ae5-4608-bcb0-ce309868415a.tar.gz' --file 'Local Disk/examples/pipelines/dax_noaa_weather_data/Part 2 - Data Analysis.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv;data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    task_id="Part_2___Data_Analysis",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "30UjjBGEwGEwVH9aDXgi",
        "AWS_SECRET_ACCESS_KEY": "q5lFOhkafzWJ1TFI7JsRYdN09DYBEMxXMgplhSei",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "analyze_NOAA_weather_data-0914072354-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_982e672a_4ae5_4608_bcb0_ce309868415a << op_e07e1b7f_568b_4bc3_9fc6_da372fd58daf


op_b00e4654_a2b0_417c_8f93_8a03bec95945 = KubernetesPodOperator(
    name="Part_3___Time_Series_Forecasting",
    namespace="default",
    image="docker.io/amancevice/pandas:1.1.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.1.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --cos-endpoint http://20.94.160.112:9000/ --cos-bucket elyra-bucket --cos-directory 'analyze_NOAA_weather_data-0914072354' --cos-dependencies-archive 'Part 3 - Time Series Forecasting-b00e4654-a2b0-417c-8f93-8a03bec95945.tar.gz' --file 'Local Disk/examples/pipelines/dax_noaa_weather_data/Part 3 - Time Series Forecasting.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv;data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    task_id="Part_3___Time_Series_Forecasting",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "30UjjBGEwGEwVH9aDXgi",
        "AWS_SECRET_ACCESS_KEY": "q5lFOhkafzWJ1TFI7JsRYdN09DYBEMxXMgplhSei",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "analyze_NOAA_weather_data-0914072354-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_b00e4654_a2b0_417c_8f93_8a03bec95945 << op_e07e1b7f_568b_4bc3_9fc6_da372fd58daf
