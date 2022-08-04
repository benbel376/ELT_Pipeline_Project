import os
import sys
from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime as dt
from datetime import timedelta
print(os.path.abspath("working.............................."))
sys.path.append(os.path.abspath("includes"))
from python import redash_migrator as exporter 


default_args = {"owner":"airflow","start_date":datetime(2021,3,7)}
dag = DAG(
    'redash_query_exporter_dag',
    default_args=default_args,
    description='Export redash queries',
    schedule_interval='@once',
)

export_queries = PythonOperator(
    task_id='export_query',
    python_callable=exporter.get_queries,
    op_kwargs={
      'redash_url': 'http://redash:5000',
      'api_key': '7361djagduAkjUrpwUHE1zUh2qYrthrhGQzDrkio'
    },
    dag=dag
)

export_queries