# teste-backend-music-recommender

This project is meant to provide the requested features from the music recommender backend test, files provided under the folder docs.

# Running

## with Docker
1. Make sure you have docker installed: [Installation Guide](https://docs.docker.com/engine/install/)
2. Make sure you have docker and docker compose are working
```bash
$ docker version
$ docker compose version
```
3. In the root of the project, run the following command:
```bash
$ docker compose up
```
4. Go to http://localhost:8001/api, you will see the browsable api from the django-rest-framework

5. Some changes to the source can be made without re-running the docker compose, but if you want to re-run it, delete the folder container created on the root of the project and run the following command:
```bash
$ docker compose up --build
```


## with poetry
1. Make sure you have poetry installed: [Installation Guide](https://python-poetry.org/docs/#installation)
2. Run the following:
```bash
$ poetry install
```
4. Start the poetry shell:
```bash
$ poetry shell
```
5. Create a file with the following env on the `teste_backend_music_recommender/.env`, you can use the example if you are running the database with the provided docker compose:
```env
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=localhost
DATABASE_PORT=5435
DATABASE_NAME=postgres
SECRET_KEY='somesupersecret'
```
6. [Optional] Start the database:
```bash
$ docker compose up -d postgres
```
7. Run the Migrations:
```bash
$ python manage.py migrate
```
6. Start the API:
```bash
$  python manage.py runserver 8000
```



# Tests
Tests can be run with the command:
```
$ bash entrypoint-test.sh
```
