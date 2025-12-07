## Project 05 – Real-Time ML Model Serving (K8s and/or Lambda) with Monitoring

**Folder:** `project-05-ml-realtime-serving/`
**Goal:** Show the **serving side** of MLOps: online inference, rollout, monitoring, and (optionally) two deployment styles (K8s + Lambda).

### Core objective

* Take a trained model from Project 04 (or similar).
* Expose it via a `/predict` API:
  * Option A: containerized FastAPI service on Kubernetes.
  * Option B: lightweight Lambda function behind API Gateway.
* Implement:
  * Input validation + error handling.
  * Logging of requests & predictions.
  * Metrics: latency, error rate, request counts, maybe simple drift proxies.
* Integrate with model registry:
  * Load “Production” model version from MLflow registry or a versioned artifact.
* Automate deployment:
  * CI builds new serving image / function for new model versions.
  * Deploys to staging → canary or rolling deploy → prod.

### Key tech

* FastAPI (or Flask) for model API
* Docker / K8s (reusing EKS from Project 03) **or** AWS Lambda + API Gateway
* MLflow or similar for model versioning
* Prometheus + Grafana or CloudWatch metrics
* Terraform (if deploying infra changes, especially for Lambda side)

### Portfolio deliverables

* `app/`:
  * `serve_model/` (API code loading model)
* `k8s/` or `infra/terraform/` for Lambda version:
  * Deployment/Service/Ingress for K8s version
  * Or Lambda + API Gateway config
* `README.md`:
  * Diagram: client → API → model → logs/metrics
  * Example monitoring graphs
  * Explanation of how model versions are rolled out
* Talking point: “I deployed ML models as real-time APIs, handled monitoring, and treated model updates like application releases.”
