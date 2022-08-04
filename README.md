[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


![image](https://user-images.githubusercontent.com/44437166/182869355-8a837116-8b9b-44d7-8ad8-73ac4e38836a.png)

<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Sensor Data ELT</h3>

  <p align="center">
    A fully dockerized ELT pipeline using MySQL, PostgreSQL, Airflow, DBT, Redash and Superset.
    <br />
    <a href="https://sensordataelt.herokuapp.com/index.html"><strong>Explore the docs »</strong><a>
    <br />
    <br />
    ·
    <a href="https://github.com/eandualem/sensor_data_elt/issues">Report Bug</a>
    ·
    <a href="https://github.com/eandualem/sensor_data_elt/issues">Request Feature</a>
    .
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

### Objective
The objective of this project was to create a scalable end to end data pipeline that transports a vehicle trajectory data from csv file to a warehouse, where it will be transforemed into a suitable form for further processing.

### The Pipeline
![image](https://user-images.githubusercontent.com/44437166/182868458-c9a8efbd-9f64-41b7-af37-6b2298ee5c26.png)


### Built With

Tech Stack used in this project
* [PostgreSQL](https://www.postgresql.org/)
* [Apache Airflow](https://jquery.com)
* [dbt](https://laravel.com)
* [Redash](https://laravel.com)



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Make sure you have docker installed on local machine.
* Docker
* DockerCompose
  
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/benbel376/ELT_pipeline_project
   ```
2. Datawarehouse
   ```sh
   cd ELT_pipeline_project/docker
   ```
3. Run
   ```sh
    docker-compose -f docker-compose-postgres.yml up
    docker-compose -f docker-compose-airflow.yml up
    docker-compose -f docker-compose-redash.yml up
   ```
4. Can access and Modefy the default configrations for each tool using the dockerfiles files.


<!-- USAGE EXAMPLES -->
## Usage
![image](https://user-images.githubusercontent.com/44437166/182867684-65a5e5a6-07ec-45af-a6d7-bf7d6e68e0fd.png)
![image](https://user-images.githubusercontent.com/44437166/182867704-5123c587-24dd-4404-86b8-a14c5a3d0bc8.png)
![image](https://user-images.githubusercontent.com/44437166/182867733-8a32a593-108d-44ae-8e80-8d5357ca2860.png)
![image](https://user-images.githubusercontent.com/44437166/182867759-39e45b73-7a30-4ee1-a559-113e950f23e8.png)
![image](https://user-images.githubusercontent.com/44437166/182867777-48803c67-2d36-429c-870b-eda6c149029d.png)


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Biniyam Belayneh - biniyambelayneh376@gmail.com

Project Link: [https://github.com/benbel376/ELT_pipeline_project](https://github.com/benbel376/ELT_pipeline_project)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [10 Academy](https://www.10academy.org/)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/eandualem/sensor_data_elt.svg?style=for-the-badge
[contributors-url]: https://github.com/eandualem/sensor_data_elt/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/eandualem/sensor_data_elt.svg?style=for-the-badge
[forks-url]: https://github.com/eandualem/sensor_data_elt/network/members
[stars-shield]: https://img.shields.io/github/stars/eandualem/sensor_data_elt.svg?style=for-the-badge
[stars-url]: https://github.com/eandualem/sensor_data_elt/stargazers
[issues-shield]: https://img.shields.io/github/issues/eandualem/sensor_data_elt.svg?style=for-the-badge
[issues-url]: https://github.com/eandualem/sensor_data_elt/issues
[license-shield]: https://img.shields.io/github/license/eandualem/sensor_data_elt.svg?style=for-the-badge
[license-url]: https://github.com/eandualem/sensor_data_elt/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/elias-andualem-94a9a7195/
[product-screenshot]: images/architecture.png

