# [Session 07] SQL or NoSQL

Compare relational, document, key-value, and graph models. Decide when a simple relational database plus cache is better than adding another database.

## Evidence

- `notes/session-07/`
- `evidence/session-07/data-store-decision.md`

## Acceptance criteria

- [ ] I chose a data model from access patterns.
- [ ] I documented one key format and TTL.
- [ ] I compared DynamoDB/ElastiCache with Firestore/Memorystore.
- [ ] I answered the interview question aloud.

## Detailed assignment

1. Compare relational, document, key-value, wide-column, search, and graph models.
2. Write the top five reads and writes for one feature before choosing a store.
3. Decide what belongs in a relational database, cache, document store, or key-value store.
4. Explain normalization, denormalization, secondary indexes, and duplicated-data cost.
5. Document one key format, TTL, size assumption, and access pattern.
6. Explain why relational database plus cache may be safer than adding another database.
7. Compare DynamoDB/ElastiCache with Firestore/Memorystore.

## Ready-to-copy Issue details

- **Question:** How do you choose between SQL and NoSQL for a new feature?
- **Evidence:** `notes/session-07/interview-notes.md` and `evidence/session-07/data-store-decision.md`.
- **Reviewer prompt:** Ask which access pattern would force a different data model.
