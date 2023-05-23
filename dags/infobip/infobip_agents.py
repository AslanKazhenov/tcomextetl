import sys
from datetime import datetime, timedelta

import pendulum
from airflow.operators.python import PythonOperator
from airflow.models import DAG
from airflow.models import Variable

sys.path.append('.')

from dags.docker_runner import ExternalEtlDockerRunner as Runner
from dags.infobip.infobip_common import prepare_command_args

with DAG(
        dag_id='infobip_agents',
        catchup=False,
        start_date=pendulum.datetime(2023, 2, 1, tz=f'{Variable.get("TZ")}'),
        schedule_interval='@daily',
        tags=['infobip']
     ) as dag:

    command_args = PythonOperator(
        task_id='command_args',
        python_callable=prepare_command_args,
        dag=dag,
        do_xcom_push=False
    )

    infobip_agents = Runner(
        task_id='infobip_agents',
        luigi_module='infobip',
        luigi_task='InfobipAgents',
        luigi_params="--all-data",
        env_vars={'INFOBIP_USER': Variable.get('INFOBIP_USER'),
                  'INFOBIP_PASSWORD': Variable.get('INFOBIP_PASSWORD')},
        pool='infobip',
        do_xcom_push=False
    )

    command_args >> infobip_agents