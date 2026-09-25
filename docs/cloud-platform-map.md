# CareerG1 cloud and GitHub map

This map separates the **learning concept**, the **application code**, and the **platform capability**. A cloud service is not a substitute for understanding the design trade-off.

| Need | CareerG1 code to inspect | GitHub evidence | Azure/platform option |
|---|---|---|---|
| Measure p95/p99 latency | `backend/app/api/endpoints/agents.py`, `backend/app/agents/graph.py` | timing script and baseline table | Application Insights, Azure Monitor |
| Scale HTTP workers | `backend/entrypoint.sh`, API startup configuration | deployment diagram and replica assumptions | Azure Container Apps or AKS |
| Route traffic and terminate TLS | deployment configuration and ingress | request-flow diagram | Azure Front Door, Application Gateway |
| Cache expensive research | `backend/app/services/salary_research.py`, job search service | cache-key and TTL decision | Azure Cache for Redis |
| Tune relational queries | jobs and roadmap endpoints, Alembic migrations | EXPLAIN output and query-count test | Azure Database for PostgreSQL |
| Run long AI work asynchronously | `backend/app/api/endpoints/agents.py`, `backend/app/agents/graph.py` | 202 API contract and state model | Azure Service Bus, Container Apps Jobs |
| Protect secrets | `.env` references and auth modules | secret-scanning result, no secret values | Azure Key Vault, managed identity |
| Authenticate users | `backend/app/core/jwt.py`, OAuth verifier | authorization test matrix | Microsoft Entra ID or Google OAuth with Key Vault |
| Govern AI APIs | Azure OpenAI/Tavily integration | quota and cost assumptions | Azure API Management, Azure OpenAI |
| Observe failures and cost | request, agent, and worker paths | dashboard/query screenshots with redaction | Application Insights, Log Analytics |
| Automate review and assignment | `.github/ISSUE_TEMPLATE`, PR workflow | issue, PR, and project links | GitHub Projects, Actions, Discussions |

## Recommended production boundary

Keep the first deployment as a modular application with separate web and worker processes. Add a queue before adding microservices. Use managed Azure services for Postgres, Redis, secrets, monitoring, and messaging so the learning effort stays focused on system behavior rather than operating databases.

## Cost and security rule

Every cloud choice must document its expected cost driver, failure mode, data classification, and rollback path. Use a development subscription/resource group, budgets, least-privilege identities, and redacted evidence.
