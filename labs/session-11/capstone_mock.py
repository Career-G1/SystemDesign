"""Print a timed capstone interview checklist."""

checkpoints = [
    "0-5 min: clarify use cases and non-goals",
    "5-10 min: state traffic, storage, latency, availability, and growth assumptions",
    "10-15 min: draw the high-level architecture",
    "15-22 min: walk read, write, and failure paths",
    "22-27 min: identify bottlenecks, measurements, security, and cost",
    "27-30 min: summarize trade-offs and next steps",
]
for checkpoint in checkpoints:
    print(checkpoint)
print("write the result to evidence/session-11/capstone.md")
