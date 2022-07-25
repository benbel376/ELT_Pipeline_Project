# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 01:54:51 2021

@author: viswa
"""
try:
    from airflow import DAG
    from datetime import datetime,timedelta
    from airflow.operators.bash_operator import BashOperator
    from airflow.operators.python_operator import PythonOperator
    import sys
    import os
    sys.path.append(os.path.abspath("includes"))
    from hello import hello
    print("done")
except Exception as e:
    print(f"error: {e}")


default_args = {"owner":"airflow","start_date":datetime(2021,3,7)}
with DAG(dag_id="workflow",default_args=default_args,schedule_interval='@daily') as dag:
   
    pre_process = PythonOperator(
        task_id = "pre_process",
        python_callable = hello
        )
    
    pre_process