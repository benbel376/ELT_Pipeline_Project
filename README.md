# ELT Pipeline Project
![image](https://user-images.githubusercontent.com/44437166/182762662-a21a8f0a-926c-420c-b2e9-48a8f44e5613.png)

**Table of content**

- [Overview](#overview)
- [Install](#install)
- [Introduction](#Introduction)
- [Files](#Files)

## Project Overview

### Introduction
This project aims to develop a data pipeline that transports a vehicle trajectory data from a csv file to a scalable warehouse, whare it can be transformed into more usable but not too specific forms using DBT.

This project can be used for any project that requires to work with the pNeuma's trajectory data. It can also be used for other csv to warehouse data transporting projects with some modifications to the extraction code and the dbt models.

### The Pipeline

![image](https://user-images.githubusercontent.com/44437166/180680935-6c8be686-a71a-4894-8b23-805f4ed9b85a.png)

1. Data is extracted from the original data source (from csv file). At this point there will be some restructuring of the original form so that it can fit into a pandas data frame.
2. Data is given to the data loader python script.
3. The data is written to the source table in the warehouse
4. From the source table, DBT will load the data
5. DBT will run SQL models on the loaded data to generate 2 dimension and 2 fact tables. These 4 tables are our final forms.
6. Our final data forms will be loaded into Redash and visualized
Airflow is going to play the role of orchestrating the process described above using a DAG script

### Files and Project Structure
> ### airflow_data
> contains the dag scripts and initialization docker-compose yaml files for ariflow orchestration
> ### dbt_transform
> contains the models and configuration file used by dbt to transform data.
> ### notebooks
> the extraction and loading scripts were tested here
> ### scripts
> contain all the required extracting and loading functions as well as sql script for table creation in a separate folder.


## Technologies Used
- **Airflow**: for archerstration
- **DBT**: for transformation
- **Python Libraries**: for extraction and loading scripts
  - Pandas: for loading csv file and processing
  - python-mysql-connector: for communicating with warehouse
- **Mysql**: for warehouse
- **Docker and Docker-compose**: for hosting the above applications

## Prerequisites
- Python 3.8
- RAM: above 4.
## Installation 

```
git clone https://github.com/benbel376/ELT_Pipeline_Project.git
cd ELT_Pipeline_Project
./setup.sh
```
## Results

## License
- [MIT License](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiMqbrwqaz5AhVPiqQKHa5uCtkQFnoECAYQAQ&url=https%3A%2F%2Fopensource.org%2Flicenses%2FMIT&usg=AOvVaw1MsEPekvPKCIceu2jiRDy4)

## Author

👤 **Biniyam Belayneh**

- GitHub: [Biniyam Belayneh](https://github.com/benbel376)
- LinkedIn: [Biniyam Belayneh](https://www.linkedin.com/in/biniyam-belayneh-demisse-42909617a/)
## Acknowledgement
- Thank you [10 academy](https://www.10academy.org/) for the project idea and resource provision
- Thank you [Start Data Engineering](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjhyZ-gqaz5AhWQ_aQKHbnaAQMQFnoECAgQAQ&url=https%3A%2F%2Fwww.startdataengineering.com%2F&usg=AOvVaw2E27rYT8jytFpiuh4LndRP) for awsome blog posts on data engineering
- Thank you [pNEUMA](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwia7NfCqaz5AhULzKQKHfz3BPoQFnoECAYQAw&url=https%3A%2F%2Fopen-traffic.epfl.ch%2F&usg=AOvVaw2UHwEsPYyGaAxHnrblo_bR) for data source
## Show your support

Give a ⭐ if you like this project!
