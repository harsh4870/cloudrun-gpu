# cloudrun-gpu
Run the LLM on Cloud Run GPU

### Prerequisites

* [Docker Desktop](https://www.docker.com/products/docker-desktop/)

#### Quick Demo

```
docker run -d -p 8080:8080 harshmanvar/cloud-run-gpu-llms:v1
```
Open `localhost:8080` in Browser

#### Build locally using docker

```
docker build -t cloudrun-llm-gpu .
```

#### Running locally

```
docker run -d -p 8080:8080 cloudrun-llm-gpu 
```

Open `localhost:8080` in Browser
