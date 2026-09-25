# System design cloud and GitHub map

This map separates the **learning concept**, the **application code**, and the **platform capability**. A cloud service is not a substitute for understanding the design trade-off.

| Need | Example code to inspect | GitHub evidence | AWS option | Google Cloud option |
|---|---|---|---|
| Measure p95/p99 latency | API and worker modules | timing script and baseline table | CloudWatch | Cloud Monitoring |
| Scale HTTP workers | service startup configuration | deployment diagram and replica assumptions | ECS or EKS | Cloud Run or GKE |
| Route traffic and terminate TLS | deployment configuration and ingress | request-flow diagram | Elastic Load Balancing | Cloud Load Balancing |
| Cache expensive results | service or repository layer | cache-key and TTL decision | ElastiCache | Memorystore |
| Tune relational queries | list endpoints, ORM models, migrations | EXPLAIN output and query-count test | RDS Performance Insights | Cloud SQL Query Insights |
| Run long-running work asynchronously | task endpoint and worker | 202 API contract and state model | SQS, SNS, EventBridge | Pub/Sub, Cloud Run Jobs |
| Protect credentials | configuration and auth modules | threat model, no secret values | Secrets Manager, IAM | Secret Manager, Workload Identity |
| Authenticate users | token validation and OAuth/OIDC verifier | authorization test matrix | Cognito, IAM | Identity Platform, IAM |
| Govern paid APIs | external API client and gateway | quota and cost assumptions | API Gateway | Apigee |
| Observe failures and cost | request and worker paths | dashboard/query screenshots with redaction | CloudWatch, X-Ray | Cloud Monitoring, Trace |
| Automate review and assignment | `.github/ISSUE_TEMPLATE`, PR workflow | issue, PR, and project links | GitHub Projects, Actions, Discussions |

## Recommended production boundary

For interview answers, start with a modular application and separate web and worker processes. Add a queue before adding microservices. Compare managed AWS and Google Cloud services for PostgreSQL, Redis, secrets, monitoring, and messaging without tying the lesson to one codebase.

## Cost and security rule

Every cloud choice should document its expected cost driver, failure mode, data classification, and rollback path. In examples, use placeholders, least privilege, and redacted evidence.
