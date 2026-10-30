# Session 01 benchmark

## Command

```powershell
python labs\session-01\benchmark.py
```

## Results

| Concurrency | p50 | p95 | p99 | Throughput |
|---:|---:|---:|---:|---:|
| 1 | 5.39 ms | 5.69 ms | 5.79 ms | 184.69 req/s |
| 10 | 5.34 ms | 5.68 ms | 5.76 ms | 1678.76 req/s |

## Interpretation

Concurrency increased throughput because requests could run at the same time. The local stub kept latency nearly constant, but a real service could become constrained by CPU, database connections, memory, or an external dependency.

## What I would measure next

I would measure CPU, memory, database latency, connection-pool usage, dependency latency, and error rate under increasing concurrency.

## Interview answer

Performance describes how quickly one request completes. Scalability describes how the system behaves when traffic and concurrent users increase. I would measure p50, p95, p99, throughput, errors, and resource saturation. Then I would identify the first bottleneck before choosing caching, query optimization, horizontal scaling, or asynchronous processing.
