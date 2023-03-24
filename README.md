# Dog Cat Classification API

## Tools

* API: [fastapi](https://github.com/tiangolo/fastapi)

## Directory structure
This is how the project directory is structured:
```
├── app
│   ├── app
│   │   ├── config.py
│   │   ├── main.py
│   │   ├── utils.py
|   |
|   ├── Dockerfile
|   ├── docker_build.sh
|   ├── docker_run_it.sh
|   ├── docker_run_server.sh
```

## Run
1. Install dependencies
```
pip install -r requirements.txt
```

2. Run the server
```
uvicorn app.main:app --host 0.0.0.0 --port 80
```
* Add `--reload` flag to enable live mode.
* Go to `localhost:{port}/docs` for [Swagger UI](https://swagger.io/tools/swagger-ui/), check [document](https://fastapi.tiangolo.com/#interactive-api-docs) for more information.

## Docker
Directory structure in docker container:
```
├── /app
│   ├── app
│   │   ├── config.py
│   │   ├── main.py
│   │   ├── utils.py

```

1. Run the service

```
docker compose up --build -d
```

2. Run manually

Build the image:
```
bash docker_build.sh
```

Run the container

```
bash docker_run_server.sh
```
