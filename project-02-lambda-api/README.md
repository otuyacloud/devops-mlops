## Project 02 – Serverless Python API with AWS Lambda + API Gateway (Terraform)

**Folder:** `project-02-lambda-api/`
**Goal:** Demonstrate you can build **serverless backends** with infrastructure-as-code and CI/CD, using **Terraform** (not SAM/Serverless Framework).

### Core objective

* Build a simple **Notes API** (or similar CRUD).
* Run it as AWS Lambda functions behind API Gateway HTTP API.
* Use DynamoDB (or RDS via RDS Proxy) as storage.
* Provision everything with Terraform.
* Optional: introduce a basic CI pipeline to `terraform plan` / `apply`.

### Key tech

* AWS Lambda (Python)
* AWS API Gateway (HTTP API)
* AWS DynamoDB
* Terraform (core focus)
* CloudWatch Logs / basic monitoring

### Portfolio deliverables

* `infra/terraform/`:
  * Lambda, API Gateway, DynamoDB, IAM roles, permissions.
* `lambda/`:
  * `app.py` Lambda handler(s)
  * `requirements.txt`
* `README.md`:
  * High-level architecture (client → APIGW → Lambda → DynamoDB)
  * Example API calls (`curl` / Postman)
  * Screenshots of CloudWatch logs and Terraform plan/apply
* Talking point: “I can deploy services both as containers and as serverless functions, all managed via Terraform.”
