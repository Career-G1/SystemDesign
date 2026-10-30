# Session 01 lab

Build a safe local benchmark that compares one request at a time with concurrent requests. Record p50, p95, p99, error rate, and throughput. Keep the target configurable and default it to a local stub.

Expected output: `evidence/session-01/baseline.md`.

## Run it

```powershell
python labs/session-01/benchmark.py
```

Compare the sequential and concurrent p95/p99 results and copy the output into the evidence file.
