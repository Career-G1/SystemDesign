# How to learn system design through GitHub

## The unit of learning

One GitHub Issue represents one 30-minute system-design session. The issue is not only a reading task. It must produce evidence that can be reviewed:

- a measurement,
- a code-path explanation,
- a small implementation,
- a diagram,
- a test,
- or a written trade-off decision.

## Issue lifecycle

### Before the session

- Assign the issue to yourself or a study partner.
- Add it to the GitHub Project.
- Set the session, priority, and cloud-service fields.

### During the session

- Read only the linked primer section.
- Inspect the example code paths named in the issue, or create a small local example if no application is available.
- Run the lab or write the requested artifact.
- Record assumptions and unknowns in the issue.

### After the session

- Commit evidence in `evidence/session-XX/`.
- Link the commit or pull request in the issue.
- Answer the interview question in a Discussion.
- Move the card to Review and request review from a study partner.

## What belongs in code

Use small, general examples when the lesson has a measurable behavior:

- latency and throughput: load-test or timing harness;
- caching: cache-aside helper and hit/miss tests;
- SQL tuning: query-count test and migration/index example;
- queues: producer/consumer contract and idempotency test;
- REST: idempotency-key middleware or contract test;
- auth: token validation and authorization tests.

Do not turn every lesson into production refactoring. A learning lab should be isolated, small, repeatable, technology-neutral where possible, and safe to delete.

## What belongs in documentation

Use the Wiki or `docs/` for:

- definitions and diagrams;
- trade-offs and rejected alternatives;
- cloud-service choices;
- interview answers;
- operational checklists;
- links to code and evidence.

The Wiki is the friendly reading surface. `docs/` is the version-controlled source of truth for decisions and reusable guidance.

## Suggested labels

`system-design`, `interview-prep`, `session-01` through `session-11`, `code-lab`, `azure`, `security`, `needs-review`, `blocked`.
