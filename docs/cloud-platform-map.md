# System design cloud and GitHub map

This map separates the **learning concept**, the **application code**, and the **platform capability**. A cloud service is not a substitute for understanding the design trade-off.

| Need | Example code to inspect | GitHub evidence | Azure/platform option |
|---|---|---|---|
| Measure p95/p99 latency | `backend/app/api/endpoints/agents.py`, `backend/app/agents/graph.py` | timing script and baseline table | Application Insights, Azure Monitor |
| Scale HTTP workers | `backend/entrypoint.sh`, API startup configuration | deployment diagram and replica assumptions | Azure Container Apps or AKS |
| Route traffic and terminate TLS | deployment configuration and ingress | request-flow diagram | Azure Front Door, Application Gateway |
| Cache expensive results | service or repository layer | cache-key and TTL decision | Azure Cache for Redis |
| Tune relational queries | jobs and roadmap endpoints, Alembic migrations | EXPLAIN output and query-count test | Azure Database for PostgreSQL |
| Run long-running work asynchronously | task endpoint and worker | 202 API contract and state model | Azure Service Bus, Container Apps Jobs |
| Protect credentials | configuration and auth modules | threat model, no secret values | Azure Key Vault, managed identity |
| Authenticate users | token validation and OAuth/OIDC verifier | authorization test matrix | Microsoft Entra ID, API Management |
| Govern paid APIs | external API client and gateway | quota and cost assumptions | Azure API Management |
| Observe failures and cost | request, agent, and worker paths | dashboard/query screenshots with redaction | Application Insights, Log Analytics |
| Automate review and assignment | `.github/ISSUE_TEMPLATE`, PR workflow | issue, PR, and project links | GitHub Projects, Actions, Discussions |

## Recommended production boundary

For interview answers, start with a modular application and separate web and worker processes. Add a queue before adding microservices. Compare managed Azure services for PostgreSQL, Redis, secrets, monitoring, and messaging without tying the lesson to one codebase.

## Cost and security rule

Every cloud choice should document its expected cost driver, failure mode, data classification, and rollback path. In examples, use placeholders, least privilege, and redacted evidence.
