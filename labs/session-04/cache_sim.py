"""Measure cache-aside hits, misses, and source calls."""

source_calls = 0
cache: dict[str, str] = {}


def read(key: str) -> str:
    global source_calls
    if key in cache:
        print(f"hit  {key}")
        return cache[key]
    source_calls += 1
    value = f"value-for-{key}"
    cache[key] = value
    print(f"miss {key}")
    return value


read("user:1")
read("user:1")
read("user:2")
print(f"source_calls={source_calls} cache_entries={len(cache)}")
