# Session 07 personal interview notes

## Topic

SQL or NoSQL.

## Concept in my own words

The access pattern should drive the data model. Relational storage is a strong default when relationships, transactions, and flexible queries matter. Key-value or document storage is attractive when access patterns are known and predictable, but it can move query and consistency complexity into the application.

## Two-minute answer

I list the important reads and writes before choosing a database. I use relational storage when the feature needs transactions, relationships, constraints, or evolving queries. I use a key-value or document model when the access pattern is known, the item boundary is clear, and independent scaling is valuable. I would start with a relational database plus a cache when that meets the requirements, because every additional database adds operations, backups, migrations, observability, and consistency work.

## Decision starter

| Access pattern | Candidate | Reason |
|---|---|---|
| Transactional ownership | SQL | Constraints and transactions |
| Hot lookup | Key-value/cache | Predictable key read |
| Flexible document | Document store | Aggregate-shaped reads |

## Follow-ups

- Which query would break your chosen key design?
- What operational burden does the second database add?
