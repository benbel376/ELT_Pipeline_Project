from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import sys
import os
import pandas as pd
import json
print(os.path.abspath("working.............................."))
sys.path.append(os.path.abspath("includes/python"))

from Loader import Loader
loader = Loader()


def run_data_migration(**context):
    try:
        columns = ['track_id','types','traveled_d','avg_speed','trajectory']
        path = "~/data/test.csv"
        conn, cur = loader.connect_to_server(
                            host="postgres", 
                            port=5432, 
                            user="warehouse", 
                            password="warehouse", 
                            dbName="warehouse")
        conn_mysql, cur_mysql = loader.connect_to_mysql_server(
                                host="mysql", 
                                user="root", 
                                password="mysql", 
                                port=3306, 
                                dbName="warehouse") 

        migration = loader.load_from_source(cur_mysql, "source", columns, 10, path)
        loader.create_table(cur, "includes/sql/create_source_table.sql", "warehouse")
        loader.insert_into_table(cur, conn, "warehouse", migration, "source")
        loader.close_connection(cur, conn)
    except Exception as e:
        print(e)
    
    


default_args = {"owner":"airflow","start_date":datetime(2021,3,7)}
with DAG(dag_id="workflow",default_args=default_args,schedule_interval='@daily', catchup=False) as dag:
   
    data_migration_task= PythonOperator(
        task_id = "data_migration_task",
        python_callable = run_data_migration,
        provide_context=True
        )

data_migration_task