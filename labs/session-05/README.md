# Session 05 lab

Capture a query count for one endpoint and document one index or eager-loading change that would reduce N+1 work.
## Practical exercise

Run the SQLite example, compare the N+1 query count with the joined query, and add an EXPLAIN query.

```powershell
python labs/session-05/sql_tuning.py
```

Expected output: `evidence/session-05/query-count.md`.
