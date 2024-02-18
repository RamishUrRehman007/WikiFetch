# WikiFetch

![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-CC2927?style=for-the-badge&logo=sqlalchemy)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

WikiFetch is a powerful application designed to fetch articles from Wikipedia, process the data, and integrate it into an application. Leveraging the capabilities of FastAPI, SQLAlchemy, PostgreSQL, and Docker, WikiFetch facilitates the retrieval and management of information, making it easily accessible and manageable for further application use.

## Project Overview

WikiFetch utilizes a combination of advanced technologies to streamline the process of fetching, processing, and storing articles from Wikipedia. By harnessing the power of these technologies, the application ensures efficient data handling and robust database management, catering to the needs of developers and content managers alike.

## Technologies

- **SQLAlchemy**: A Python SQL toolkit and Object Relational Mapper that provides full power and flexibility of SQL.
- **PostgreSQL**: An advanced object-relational database management system emphasizing extensibility and standards compliance.
- **Docker**: A platform used for developing, deploying, and running applications using containerization technology.
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Getting Started

Follow these steps to get WikiFetch up and running on your local machine.

### Prerequisites

Ensure you have the following installed before you proceed:

- [Docker](https://www.docker.com/products/docker-desktop)
- [Git](https://git-scm.com/downloads)

### Setup and Installation

#### Step 1: Clone the Repository

Clone the WikiFetch repository to your local machine:

```bash
git clone https://github.com/RamishUrRehman007/WikiFetch.git
```

#### Step 2: Setup Database and Application

Run the following Docker Build commands to setup database and application

```bash
docker-compose up -d postgres
docker-compose exec postgres sh -c '/mnt/migration.sh -d wiki_fetch_dev'
docker-compose up
```
![docker build](images/docker_build.PNG)

#### Step 3: Fetch Wikipedia Articles

Since everything is in Docker container, so let access to container and run article_main.py to get wikipedia articles.

```bash
docker exec -it wiki_fetch-api bash
python wiki_fetch/articles_main.py
```
![docker containers](images/docker_containers.PNG)

### Accessing the Application

Run "http://localhost:10000/" on your browser to check if it is successful

![swagger status success](images/swagger_status_success.PNG)

Run "localhost/swagger" on your browser to interact with backend API to get all the articles stored in DB already.

![all articles endpoint](images/all_articles_endpoint.PNG)


### Validation

Run "python -m unittest test_filter_articles.py" in same Docker Container to check the filter logic
```bash
docker exec -it wiki_fetch-api bash
python -m unittest wiki_fetch/test_filter_articles.py
```
