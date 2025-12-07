# Project 01 — Production‑Ready Containerized Flask API

## Overview

This project demonstrates how to take a Python backend service from local development to a production-style deployment using containers and CI/CD.

The goal is not to build a complex product, but to show real-world DevOps fundamentals:

- Clean Flask application structure
- Containerized runtime with Docker
- Local development with Docker Compose
- Automated testing
- CI pipeline with GitLab CI
- Container image publishing to GitLab Container Registry
- Production-style deployment using Docker Compose on a cloud VM

This project serves as the foundation for later projects involving serverless, Kubernetes, and MLOps.

## Tech Stack

**Application**
- Python 3.11
- Flask (application factory pattern)
- SQLAlchemy
- PostgreSQL

**Infrastructure & DevOps**
- Docker
- Docker Compose
- GitLab CI
- GitLab Container Registry

**Testing**
- pytest

## Architecture

### Local Development
```
Client
  ↓
Flask API (Docker)
  ↓
PostgreSQL (Docker)
```

### Production Deployment
```
Client
  ↓
Cloud VM (Docker Compose)
  ├── Flask API (container)
  └── PostgreSQL (container)
```

In later projects, this deployment model is intentionally expanded to ECS, Lambda, and Kubernetes to show deployment strategy range.

## Project Structure

```
project-01-container-api/
  app/
    main.py
    config.py
    db.py
    models.py
    schemas.py
    crud.py
  tests/
    test_health.py
  docker/
    docker-compose.local.yml
    docker-compose.prod.yml
  .gitlab-ci.yml
  Dockerfile
  requirements.txt
  README.md
```

## Application Features

### Health Check
```
GET /health
```

Response:
```json
{
  "status": "ok",
  "environment": "local"
}
```

### Items API
```
GET  /items
POST /items
```

Create item payload:
```json
{
  "title": "Example item",
  "description": "Created via Flask API"
}
```

## Local Development

### Prerequisites
- Docker
- Docker Compose

### Run locally
```bash
cd docker
docker compose -f docker-compose.local.yml up --build
```

The API will be available at:
- http://localhost:8000/health
- http://localhost:8000/items

## Testing

Unit tests are written using pytest.

Run tests locally:
```bash
pytest
```

Tests are also executed automatically as part of the CI pipeline.

## Docker Image

The application is packaged using a standard Docker build (no Buildah or alternative builders).

```bash
docker build -t project-01-container-api .
```

The container runs the Flask app using the application factory pattern:
```bash
flask --app app.main:create_app run
```

## CI/CD — GitLab CI

The GitLab CI pipeline performs the following steps:

### Pipeline Stages

**Test**
- Install Python dependencies
- Run unit tests with pytest

**Build**
- Build Docker image using `docker build`
- Authenticate with GitLab Container Registry
- Push image as `latest`

### Image Location
```
registry.gitlab.com/<namespace>/project-01-container-api:latest
```

This image is later consumed by the production deployment.

## Production Deployment

### Deployment Model

For simplicity and clarity, production uses:
- A single cloud VM
- Docker Compose
- GitLab Container Registry as the image source

### Run on server
```bash
docker compose -f docker-compose.prod.yml pull
docker compose -f docker-compose.prod.yml up -d
```

The API is exposed on port 80:
- http://\<server-ip\>/health
- http://\<server-ip\>/items

## Design Decisions

### Flask over FastAPI
Chosen to demonstrate a minimal, explicit WSGI-style service commonly found in legacy and production systems.

### Docker Compose for Prod (initially)
Keeps infrastructure simple while still reflecting real operational patterns.

### GitLab CI
Mirrors enterprise CI environments and integrates directly with GitLab Container Registry.

## What This Project Demonstrates

✅ Python backend development  
✅ Containerization best practices  
✅ Local vs production environment parity  
✅ Automated testing  
✅ CI pipelines  
✅ Registry-based image delivery  
✅ Deployment confidence without Kubernetes  

## Future Improvements

- Replace PostgreSQL container with managed database (RDS)
- Add database migrations (Alembic)
- Introduce authentication and authorization
- Deploy via ECS or Kubernetes
- Add structured logging and metrics
- Enable HTTPS via reverse proxy

## Positioning in the Larger Roadmap

This project is **Project 01** in a larger DevOps → MLOps progression:

1. **Containerized API** (this project)
2. Serverless API with AWS Lambda + Terraform
3. Kubernetes-based microservices
4. Batch ML pipelines (MLflow + orchestration)
5. Real-time ML serving and monitoring

Each project builds on the operational foundation established here.
