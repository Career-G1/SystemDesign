# CareerG1 System Design Learning

This repository is a practical system-design learning workspace for CareerG1. Each lesson connects:

1. **Concept** - the interview-level system-design idea.
2. **CareerG1 code** - where the idea appears in the application.
3. **Cloud platform** - the Azure/GitHub service that would support it in production.
4. **Evidence** - a short note, measurement, diagram, test, or code lab committed to GitHub.

The existing workbooks are the curriculum:

- `CareerG1 System Design Plan (Sept-Nov 2026).xlsx` - 11 Saturday sessions.
- `SOC Audit & Project Management (15-Min Sessions).xlsx` - security, audit, and project-management sessions.

## GitHub learning workflow

For every lesson:

1. Create or assign the matching GitHub Issue from `.github/ISSUE_TEMPLATE/`.
2. Read the linked Wiki page or `docs/` lesson.
3. Inspect the listed CareerG1 code paths.
4. Complete the code lab or measurement.
5. Add evidence under `evidence/session-XX/`.
6. Open a pull request and use the checklist.
7. Close the issue only after the acceptance criteria are met.

Use a GitHub Project with these columns:

**Backlog -> Reading -> Code Investigation -> Lab in Progress -> Review -> Done**

Recommended fields:

- Session
- Track
- Priority
- CareerG1 area
- Cloud service
- Evidence link
- Status

## Sessions

| Session | Topic | Primary CareerG1 area | Cloud/platform mapping |
|---|---|---|---|
| 01 | Performance vs scalability | API and agent graph | Azure Monitor, Application Insights |
| 02 | CAP and consistency | Postgres, Redis, JWT | Azure Database for PostgreSQL, Azure Cache for Redis |
| 03 | Load balancing and horizontal scaling | uvicorn, rate limits, persistence | Azure Container Apps or AKS, Azure Front Door |
| 04 | Caching | salary research, job search | Azure Cache for Redis, Application Insights |
| 05 | SQL tuning | jobs and roadmap endpoints | Azure Database for PostgreSQL, Query Performance Insight |
| 06 | Replication and sharding | college/student data | PostgreSQL read replicas, Azure database scaling |
| 07 | SQL vs NoSQL | Redis and JSONB | Azure Cache for Redis, PostgreSQL JSONB |
| 08 | Message queues | long-running agent runs | Azure Service Bus, Container Apps Jobs |
| 09 | REST, RPC, idempotency | API endpoints and schemas | API Management, Application Insights |
| 10 | OAuth, JWT, secrets, rate limiting | auth and security modules | Microsoft Entra ID, Key Vault, API Management |
| 11 | Capstone mock design | whole system | Azure architecture and cost model |

The detailed mapping is in [`docs/cloud-platform-map.md`](docs/cloud-platform-map.md).

## Repository layout

```text
.github/
  ISSUE_TEMPLATE/       lesson and code-investigation issues
  pull_request_template.md
  workflows/             optional validation workflow
docs/
  system-design-learning.md
  cloud-platform-map.md
  github-operating-model.md
wiki/
  Home.md
  Session-01.md ... Session-11.md
labs/
  session-01/ ... session-11/
evidence/
  session-XX/
```

## Important safety rule

Never commit `.env`, API keys, OAuth secrets, database passwords, tokens, or production data. Use GitHub Actions secrets, Azure Key Vault, and redacted sample values. Rotate any credential that has ever been committed.

## First assignment

Start with **Session 10 - Auth, secrets, and rate limiting**, even if you study the sessions in order. Then complete Session 01. The first session establishes vocabulary; Session 10 protects the project and cloud account.
