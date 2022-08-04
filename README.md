# ELT Pipeline Project
![image](https://user-images.githubusercontent.com/44437166/180681713-ea7f8116-baf7-41ca-9990-6c69a040b5e0.png)

**Table of content**

- [Overview](#overview)
- [Install](#install)
- [Introduction](#Introduction)
- [Files](#Files)

## Project Overview

This project aims to develop a data pipeline that transports a vehicle trajectory data from a csv file to a scalable warehouse, whare it can be transformed into more usable but not too specific forms using DBT.

This project can be used for any project that requires to work with the pNeuma's trajectory data. It can also be used for other csv to warehouse data transporting projects with some modifications to the extraction code and the dbt models.

The project has the following general outline


![image](https://user-images.githubusercontent.com/44437166/180680935-6c8be686-a71a-4894-8b23-805f4ed9b85a.png)

## Introduction
Explanation for each step shown above
1. Data is extracted from the original data source (from csv file). At this point there will be some restructuring of the original form so that it can fit into a pandas data frame.
2. Data is given to the data loader python script.
3. The data is written to the source table in the warehouse
4. From the source table, DBT will load the data
5. DBT will run SQL models on the loaded data to generate 2 dimension and 2 fact tables. These 4 tables are our final forms.
6. Our final data forms will be loaded into Redash and visualized
Airflow is going to play the role of orchestrating the process described above using a DAG script

## Files
> ### airflow_data
> contains the dag scripts and initialization docker-compose yaml files for ariflow orchestration
> ### dbt_transform
> contains the models and configuration file used by dbt to transform data.
> ### notebooks
> the extraction and loading scripts were tested here
> ### scripts
> contain all the required extracting and loading functions as well as sql script for table creation in a separate folder.

## Install

```
git clone https://github.com/benbel376/ELT_Pipeline_Project.git
cd ELT_Pipeline_Project
./setup

```

## Author

👤 **Biniyam Belayneh**

- GitHub: [Biniyam Belayneh](https://github.com/benbel376)
- LinkedIn: [Biniyam Belayneh](https://www.linkedin.com/in/biniyam-belayneh-demisse-42909617a/)

## Show your support

Give a ⭐ if you like this project!
