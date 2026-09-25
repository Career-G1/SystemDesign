# System Design Interview Learning

This repository is a practical, general-purpose system-design interview learning workspace. Each lesson connects:

1. **Concept** - the interview-level system-design idea.
2. **Example code** - where the idea appears in a representative application.
3. **Cloud platform** - the AWS or Google Cloud service that would support it in production.
4. **Evidence** - a short note, measurement, diagram, test, or code lab committed to GitHub.

The existing workbooks are the curriculum:

- `CareerG1 System Design Plan (Sept-Nov 2026).xlsx` - the original 11-session schedule and topic source.
- `SOC Audit & Project Management (15-Min Sessions).xlsx` - security, audit, and project-management sessions.

## GitHub learning workflow

For every lesson:

1. Create or assign the matching GitHub Issue from `.github/ISSUE_TEMPLATE/`.
2. Read the linked Wiki page or `docs/` lesson.
3. Inspect the listed example code paths or create a small local example.
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
- Example system area
- Cloud service
- Evidence link
- Status

## Sessions

| Session | Topic | Primary system-design area | Cloud/platform mapping |
|---|---|---|---|
| 01 | Performance vs scalability | API and agent graph | CloudWatch, Google Cloud Monitoring |
| 02 | CAP and consistency | Postgres, Redis, JWT | Amazon RDS, ElastiCache, Cloud SQL, Memorystore |
| 03 | Load balancing and horizontal scaling | workers, rate limits, persistence | ECS/EKS or GKE, Elastic Load Balancing, Cloud Load Balancing |
| 04 | Caching | service and repository layer | ElastiCache, Memorystore, Cloud Monitoring |
| 05 | SQL tuning | list endpoints and ORM queries | Amazon RDS Performance Insights, Cloud SQL Query Insights |
| 06 | Replication and sharding | tenant and relational data | Amazon RDS read replicas, Cloud SQL replicas, Spanner |
| 07 | SQL vs NoSQL | relational data, JSON, key-value data | DynamoDB, ElastiCache, Firestore, Memorystore |
| 08 | Message queues | long-running tasks | Amazon SQS/SNS, EventBridge, Pub/Sub, Cloud Run Jobs |
| 09 | REST, RPC, idempotency | API endpoints and schemas | API Gateway, Application Load Balancer, Apigee |
| 10 | OAuth, JWT, credentials, rate limiting | authentication and security | Amazon Cognito, Secrets Manager, IAM, Identity Platform, Secret Manager |
| 11 | Capstone mock design | whole system | AWS or Google Cloud architecture and cost model |

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

Never commit credentials, tokens, private keys, or real user data. Use placeholders in learning examples and discuss GitHub Secrets, AWS Secrets Manager, Google Secret Manager, and workload identities as interview topics.

## First assignment

Start with **Session 01 - Performance vs scalability**. The goal is to explain the concept, state assumptions, compare trade-offs, identify bottlenecks, and answer the interview question clearly. Study Session 10 later as general security interview preparation.
