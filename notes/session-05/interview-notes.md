# Session 05 personal interview notes

## Topic

SQL tuning.

## Concept in my own words

SQL tuning starts with evidence: query count, latency, rows examined, and an execution plan. An index is useful only when it matches the filter, join, and sort pattern and its maintenance cost is acceptable. ORM convenience can hide N+1 queries.

## Two-minute answer

I reproduce the slow list request with a fixed dataset and measure total latency, query count, and database time. I inspect the query plan and check for N+1 relationship loading, unnecessary columns, missing pagination, and a mismatch between the filter or sort order and available indexes. I make one small change, such as eager loading or a composite index, then repeat the same measurement. I also check write overhead, index size, and whether the improvement holds at realistic data volume.

## Checklist

- Query count before and after
- EXPLAIN output
- Filter and sort order
- Selectivity and index order
- Rows examined versus returned
- Write and storage cost

## Follow-ups

- Why can an index make writes slower?
- When is eager loading worse than a separate query?
