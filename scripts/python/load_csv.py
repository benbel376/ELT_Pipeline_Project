import os
import pandas as pd
from mysql.connector import Error
import mysql.connector as connector

class WarehouseAdmin():
    
    def __init__(self):
        pass
        
    def connect_to_db(self,host, user, password, dbName=None):
        """
        A function that allows you to connect to SQL database
        """
        db = connector.connect(host=host, user=user,
                          password=password,
                             database=dbName, buffered=True)
        cursor = db.cursor()
        return db, cursor

    def connect_to_server(self,host, user, password):
        """
        connect to a server
        """
        mydb = connector.connector.connect(
                                host=host,
                                user=user,
                                password=password
                                )
        return mydb

    def createDB(self, dbName: str) -> None:
        """
        A function to create SQL database
        """
        mydb, cursor = DBConnect()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {dbName};")
        mydb.commit()
        cursor.close()

    def createTables(self, dbName: str) -> None:
        """
        A function to create SQL table
        """
        mydb, cursor = DBConnect(dbName)
        sqlFile = '../airflow/dags/__pycache__/schema.sql'
        fd = open(sqlFile, 'r')
        readsqlFile = fd.read()
        fd.close()
        sqlCommands = readsqlFile.split(';')
        for command in sqlCommands:
            try:
                result = cursor.execute(command)
            except Exception as e:
                print('command skipped: ', command)
                print(e)
        mydb.commit()
        cursor.close()

    def insert_into_warehouse(dbName: str, df: pd.DataFrame, table_name: str) -> None:
        """
        A function to insert values in SQL table
        """
        mydb, cursor = DBConnect(dbName)
        for _, row in df.iterrows():
            sqlQuery = f"""INSERT INTO {table_name} 
            (track_id, type, traveled_d, avg_speed, lat, lon,
                        speed, lon_acc, lat_acc, time)
                  VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

            data = (row[0], row[1], row[2], row[3], (row[4]), (row[5]), row[6], row[7], row[8], row[9])
            try:
                cursor.execute(sqlQuery, data)
                mydb.commit()
                print('Data inserted successfully')
            except Exception as e:
                mydb.rollback()
                print('Error: ', e)

if __name__=="__main__":
    wr = WarehouseAdmin()
    wr.createDB(dbName='DWH')
    df = pd.read_csv("../data/extracted.csv")
    df.drop(["Unnamed: 0"], axis=1, inplace=True)
    wr.createTables(dbName='DWH')
    wr.insert_into_warehouse(dbName = 'DWH', df = df, table_name='elt')