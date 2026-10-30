"""Compare sequential and concurrent latency against a local stub."""

from concurrent.futures import ThreadPoolExecutor
from statistics import median
from time import perf_counter, sleep


def request() -> float:
    started = perf_counter()
    sleep(0.005)
    return (perf_counter() - started) * 1000


def percentiles(values: list[float]) -> tuple[float, float, float]:
    ordered = sorted(values)
    pick = lambda fraction: ordered[min(len(ordered) - 1, int(len(ordered) * fraction))]
    return median(ordered), pick(0.95), pick(0.99)


def run(concurrency: int, total: int) -> None:
    started = perf_counter()
    if concurrency == 1:
        latencies = [request() for _ in range(total)]
    else:
        with ThreadPoolExecutor(max_workers=concurrency) as pool:
            latencies = list(pool.map(lambda _: request(), range(total)))
    elapsed = perf_counter() - started
    p50, p95, p99 = percentiles(latencies)
    print(
        f"concurrency={concurrency} requests={total} "
        f"p50_ms={p50:.2f} p95_ms={p95:.2f} p99_ms={p99:.2f} "
        f"throughput_rps={total / elapsed:.2f}"
    )


if __name__ == "__main__":
    run(concurrency=1, total=100)
    run(concurrency=10, total=100)
