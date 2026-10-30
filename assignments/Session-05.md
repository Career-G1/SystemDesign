# [Session 05] SQL tuning

Explain indexes, composite index order, EXPLAIN, and the ORM N+1 problem. Capture a query-count baseline and propose one improvement.

## Evidence

- `notes/session-05/`
- `evidence/session-05/query-count.md`

## Acceptance criteria

- [ ] I can identify an N+1 query pattern.
- [ ] I can explain why an index helps and when it does not.
- [ ] I compared RDS Performance Insights and Cloud SQL Query Insights.
- [ ] I answered the interview question aloud.

## Detailed assignment

1. Explain primary, unique, single-column, composite, covering, and partial indexes.
2. State how composite index order affects filtering, sorting, and selectivity.
3. Find or create an ORM N+1 example and record the query count for a fixed dataset.
4. Capture an EXPLAIN or EXPLAIN ANALYZE result before the change.
5. Apply the smallest fix: eager loading, projection, pagination, a rewrite, or an index.
6. Repeat the measurement and report latency, query count, rows examined, and write/storage cost.
7. Explain when an index is harmful.

## Ready-to-copy Issue details

- **Question:** How would you investigate and improve a slow list endpoint?
- **Evidence:** `notes/session-05/interview-notes.md` and `evidence/session-05/query-count.md`.
- **Reviewer prompt:** Ask why the proposed index order matches the actual access pattern.
