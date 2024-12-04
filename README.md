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

#### Test on GCP Cloud Run CPU only

```
gcloud run deploy llm-cpu-only --image harshmanvar/cloud-run-gpu-llms:v1 --platform managed --region us-central1 --allow-unauthenticated --memory 16Gi --cpu 4 --timeout 600s --execution-environment=gen2
```

```
curl -X POST -d '{"prompt":"Is it working?"}' https://<replace-with-cloudrun-CPU-instance-url>
```

#### Test on GCP Cloud Run GPU only

```
gcloud beta run deploy llm-gpu-only --image harshmanvar/cloud-run-gpu-llms:v1 \
 --platform managed --region us-central1 --allow-unauthenticated \
 --memory 16Gi --cpu 4 --timeout 600s --execution-environment=gen2 \
 --gpu=1 --no-cpu-throttling  --gpu-type=nvidia-l4 --max-instances=1
```

```
curl -X POST -d '{"prompt":"Is it working?"}' https://<replace-with-cloudrun-GPU-instance-url>
```
