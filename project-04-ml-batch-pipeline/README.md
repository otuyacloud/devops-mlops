## Project 04 – End-to-End Batch ML Pipeline (MLflow + Orchestrator)

**Folder:** `project-04-ml-batch-pipeline/`
**Goal:** Move into **MLOps training side**: data → training → evaluation → model registry, using tools like MLflow + Prefect/Airflow.

### Core objective

* Choose a real dataset (Kaggle/UCI; e.g. churn, housing prices, credit risk).
* Build a **pipeline** that:
  1. Ingests raw data.
  2. Cleans/validates data.
  3. Does feature engineering.
  4. Trains one or more models.
  5. Evaluates & logs metrics.
  6. Registers the best model in a model registry (MLflow).
* Use a workflow orchestrator:
  * Prefect or Apache Airflow to run the pipeline on a schedule.
* Store artifacts (models, plots) in a bucket (local or S3) and log them in MLflow.

### Key tech

* Python (pandas, scikit-learn or similar)
* MLflow (tracking + model registry)
* Prefect **or** Airflow
* S3/minio or local storage for artifacts
* Docker to package pipeline jobs
* Optional: Terraform to provision S3 + compute environment

### Portfolio deliverables

* `app/`:
  * `pipelines/` (ETL, train, evaluate)
  * `mlflow/` config
* `orchestration/`:
  * Prefect flows or Airflow DAGs
* `README.md`:
  * Diagram of pipeline stages
  * Screenshots: MLflow experiments, runs, registered models; flow/DAG UI
* Talking point: “I treat ML workflows as production pipelines with versioning, tracking, and orchestration.”
