"""
Build "CareerG1 System Design Plan (Sept-Nov 2026).xlsx".

Shape mirrors "GCLP F26 Presentation Groups.xlsx": one flat table, a slug id
column, a track column, a Full Name column, and schedule columns. The "Week N"
columns are replaced by real Saturday dates.

Budget: 30 minutes per Saturday, 11 Saturdays = 5.5 hours total. That forces
exactly one topic per Saturday, so the 11 chosen topics are the highest-value
intersection of (asked in almost every backend/system-design interview) and
(actually changes the CareerG1 codebase). Everything else is preserved on the
Backlog sheet rather than deleted.

Topics come from github.com/donnemartin/system-design-primer, scoped to the
CareerG1 stack: FastAPI + uvicorn, SQLAlchemy + Alembic + Postgres, Redis,
Docker Compose, Vite/React frontend, Google OAuth + JWT, LangGraph/LangChain
agents on Azure OpenAI with Tavily search.
"""

import datetime

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

OUT = r"C:\Users\mouni\OneDrive\Desktop\system\CareerG1 System Design Plan (Sept-Nov 2026).xlsx"
PRIMER = "https://github.com/donnemartin/system-design-primer"

# Derived from the account email (manojkasula6@gmail.com). Change here and
# re-run, or just edit column F in the sheet.
FULL_NAME = "Manoj Kasula"

MINUTES_PER_SATURDAY = 30

# ---------------------------------------------------------------- schedule ---
START = datetime.date(2026, 9, 19)   # first Saturday on/after today (13-Sep-2026)
END = datetime.date(2026, 11, 30)


def saturdays(start, end):
    d, out = start, []
    while d <= end:
        if d.weekday() == 5:
            out.append(d)
        d += datetime.timedelta(days=1)
    return out


SATS = saturdays(START, END)

# ---------------------------------------------------------------- content ---
# One topic per Saturday. Every field is sized for a single 30-minute sitting:
# ~15 min reading, ~10 min doing, ~5 min recall.
TOPICS = [
    dict(
        slug="Scale_Vocabulary",
        track="Foundations",
        main_topic="Performance vs Scalability, Latency vs Throughput",
        primer_section="Performance vs scalability; Latency vs throughput",
        must_know="Performance = slow for a single user. Scalability = fine for one, slow for many. Latency = time for one operation. Throughput = operations per second. Always quote p95/p99, never the average.",
        why="CareerG1 is slow for two unrelated reasons and conflating them wastes your effort: one LangGraph run is slow because of external LLM I/O (performance), while many students hitting /agents at once is a worker-starvation problem (scalability). Every later session depends on you telling these apart.",
        files="backend/app/api/endpoints/agents.py; backend/app/agents/graph.py",
        importance="Must",
        question="Your API is slow. How do you decide whether that is a performance problem or a scalability problem?",
        breakdown="15 min read / 10 min label / 5 min recall",
        action="Write one line per endpoint group (auth, jobs, resume, agents) labelling it performance-bound or scalability-bound.",
    ),
    dict(
        slug="CAP_And_Consistency",
        track="Availability & Consistency",
        main_topic="CAP Theorem & Consistency Patterns",
        primer_section="Availability vs consistency > CAP theorem; Consistency patterns",
        must_know="Networks partition, so you pick CP or AP - 'CA' is not on the menu. Weak / eventual / strong consistency and what each feels like to a user. Read-after-write is the exception you almost always have to special-case.",
        why="CareerG1 already mixes both and you should be able to defend it out loud: Postgres holds offers and placements (CP - a wrong offer beats an error page being unacceptable), Redis holds rate-limit counters and cached search (AP - a stale counter is harmless). A revoked JWT needs strong consistency; a regenerated roadmap does not.",
        files="backend/app/db/session.py; backend/app/models/offer.py; backend/app/core/jwt.py; backend/app/core/rate_limit.py",
        importance="Must",
        question="Explain CAP without drawing the triangle. Which parts of your system are CP and which are AP?",
        breakdown="15 min read / 10 min tag / 5 min recall",
        action="List every CareerG1 data store and tag it CP or AP with a one-line reason.",
    ),
    dict(
        slug="Load_Balancing",
        track="Networking & Delivery",
        main_topic="Load Balancer (L4 vs L7) & Horizontal Scaling",
        primer_section="Load balancer; Horizontal scaling",
        must_know="L4 balances on IP/port, L7 reads headers and paths. SSL termination and health checks live here. Horizontal scaling only works if servers are stateless - sticky sessions are a workaround, not a design.",
        why="The moment you run a second uvicorn replica, anything held in process memory breaks. CareerG1 has at least two such places: the rate limiter and in-flight agent run state. Finding them now is what makes every later scaling story true instead of aspirational.",
        files="backend/app/core/rate_limit.py; backend/app/agents/persistence.py; backend/entrypoint.sh",
        importance="Must",
        question="Why are sticky sessions a design smell? How does the load balancer know a replica is unhealthy?",
        breakdown="15 min read / 10 min hunt / 5 min recall",
        action="Search the backend for state held in module-level or process memory and list what would break with 2 replicas.",
    ),
    dict(
        slug="Caching",
        track="Caching",
        main_topic="Caching: Cache-Aside, TTL & Invalidation",
        primer_section="Cache > Caching at the object level; When to update the cache (cache-aside, write-through, write-behind, refresh-ahead)",
        must_know="Cache-aside (lazy load) is the default; write-through trades write latency for consistency. Cache the assembled object, not raw query rows. Invalidation is the hard part, not lookup. Thundering herd on a hot key expiry is the classic bug.",
        why="This is CareerG1's biggest money win. Every uncached call spends real Azure OpenAI tokens and Tavily quota, and market research for 'data analyst, Hyderabad' is near-identical across students - it should be computed once, not once per request.",
        files="backend/app/services/salary_research.py; backend/app/agents/nodes/market_researcher.py; backend/app/services/job_search.py",
        importance="Must",
        question="Compare cache-aside and write-through. How do you stop a thundering herd when a hot key expires?",
        breakdown="15 min read / 10 min design / 5 min recall",
        action="Pick your single most expensive service call and write down its cache key format, TTL, and invalidation trigger.",
    ),
    dict(
        slug="SQL_Tuning",
        track="Databases (RDBMS)",
        main_topic="SQL Tuning: Indexes, EXPLAIN & the N+1 Problem",
        primer_section="Database > SQL tuning; Denormalization",
        must_know="B-tree, composite and covering indexes, and why column order matters. Read an EXPLAIN ANALYZE plan for a sequential scan. The N+1 problem and eager loading. Unindexed foreign keys are the most common real-world cause of slow queries.",
        why="Cheapest real win in the whole plan. SQLAlchemy relationship access in endpoints/jobs.py and endpoints/roadmap.py almost certainly fires one query per row, and your foreign keys are probably unindexed. This is a measurable speedup for about an hour of work.",
        files="backend/app/api/endpoints/jobs.py; backend/app/api/endpoints/roadmap.py; backend/app/db/session.py; alembic/",
        importance="Must",
        question="What is the N+1 problem and how do you fix it in an ORM? Walk me through an EXPLAIN plan.",
        breakdown="10 min read / 15 min measure / 5 min recall",
        action="Set SQLAlchemy echo=True, call GET /jobs once, and count the queries actually issued. Write the number down.",
    ),
    dict(
        slug="Replication_And_Sharding",
        track="Databases (Scaling)",
        main_topic="Replication, Federation & Sharding",
        primer_section="Database > Master-slave replication; Master-master replication; Federation; Sharding",
        must_know="Master-slave scales reads; replication lag is why a user may not see their own write. Federation splits by function, sharding splits by key. Choosing a shard key, hot spots, and why resharding live is painful.",
        why="CareerG1 is read-heavy on dashboards and multi-tenant by college, which hands you an obvious federation boundary and an obvious shard key. Deciding this before you have data is far cheaper than after, and interviewers push hard on shard-key choice.",
        files="backend/app/models/college.py; backend/app/models/student.py; backend/app/api/endpoints/placements.py",
        importance="Must",
        question="Pick a shard key for a multi-tenant product and defend it. What happens when one tenant is 100x bigger than the rest?",
        breakdown="15 min read / 10 min write / 5 min recall",
        action="Write 3 sentences: your CareerG1 shard key, the federation split you would make, and the hot-spot risk you are accepting.",
    ),
    dict(
        slug="SQL_Or_NoSQL",
        track="Databases (NoSQL)",
        main_topic="SQL vs NoSQL & Key-Value Stores (Redis)",
        primer_section="Database > NoSQL > Key-value store; Document store; SQL or NoSQL",
        must_know="SQL for structured, relational, transactional data with complex joins. NoSQL for semi-structured data, flexible schema, very high write throughput. Redis is an O(1) key-value store with TTL and an eviction policy. Postgres JSONB gives you document semantics without a second database.",
        why="Redis is already in your .env and almost certainly under-used - it is the right home for rate-limit buckets, OAuth state and cached Tavily results. The interview skill being tested is defending 'Postgres + JSONB + Redis' and talking yourself OUT of adding Mongo.",
        files=".env (DATABASE_URL, REDIS_URL); backend/app/agents/schemas.py; backend/app/models/agent_roadmap.py",
        importance="Must",
        question="Would you use SQL or NoSQL here? Now talk me out of adding a second database.",
        breakdown="15 min read / 10 min list / 5 min recall",
        action="List everything in CareerG1 that belongs in Redis, then pick one and write its exact key format plus TTL.",
    ),
    dict(
        slug="Message_Queues",
        track="Asynchronism",
        main_topic="Message Queues & Async Task Processing",
        primer_section="Asynchronism > Message queues; Task queues; Back pressure",
        must_know="Producer, queue, consumer. Return 202 with a job id instead of blocking the request. At-least-once delivery means consumers must be idempotent. Dead letter queues. Bounded queues and 429 + Retry-After as back pressure.",
        why="The single most important change CareerG1 needs. A full agent graph run is far too long for a synchronous HTTP request, and today it occupies a worker that /auth/login also needs. It is also the most impressive thing you can put on your resume from this project.",
        files="backend/app/api/endpoints/agents.py; backend/app/agents/graph.py; backend/app/models/ai.py",
        importance="Must",
        question="Design an async pipeline for a long-running AI task. How do you make the consumer idempotent under at-least-once delivery?",
        breakdown="15 min read / 10 min spec / 5 min recall",
        action="Write the API contract: POST /agents/run returns 202 + run_id, GET /agents/runs/{run_id} returns status. Include the job states.",
    ),
    dict(
        slug="REST_API_Design",
        track="Communication",
        main_topic="REST vs RPC, Idempotency & API Design",
        primer_section="Communication > Representational state transfer (REST); Remote procedure call (RPC)",
        must_know="REST is resources and a uniform interface; RPC is calling a procedure and couples you to the implementation. GET/PUT/DELETE are idempotent, POST is not - which is exactly why retries are dangerous. Cursor pagination, versioning, and one single error shape.",
        why="Your api/endpoints/* is REST but likely inconsistent: mixed error shapes, no pagination on list endpoints, no /v1 prefix, unsafe retries. Interviewers probe exactly these, and fixing them is what makes the codebase read as professional rather than student work.",
        files="backend/app/api/endpoints/*; backend/app/schemas/*; backend/app/main.py",
        importance="Must",
        question="Which HTTP verbs are idempotent and why does that matter for retries? How do you version a public API?",
        breakdown="15 min read / 10 min audit / 5 min recall",
        action="Scan your endpoint list and mark every route using the wrong verb, missing pagination, or returning a one-off error shape.",
    ),
    dict(
        slug="Auth_And_Rate_Limiting",
        track="Security",
        main_topic="Auth (OAuth 2.0 + JWT), Secrets & Rate Limiting",
        primer_section="Security (applied: OAuth 2.0 / OIDC / JWT, rate limiting)",
        must_know="Authorization code flow with PKCE and why PKCE exists. Always verify issuer, audience, expiry AND signature. Short access token plus refresh rotation, because a stateless JWT cannot be un-issued. Token bucket rate limiting in Redis. Never commit secrets.",
        why="Most urgent item in the plan, not just the most examinable. Your .env holds JWT_SECRET, SECRET_KEY, AZURE_OPENAI_KEY, GOOGLE_CLIENT_SECRET, TAVILY_API_KEY and the Postgres password in plaintext. Also: because every AI endpoint costs money, the limit you actually need is spend-per-student, not requests-per-second.",
        files=".env; backend/app/core/jwt.py; backend/app/core/oauth_verifier.py; backend/app/core/authz.py; backend/app/core/rate_limit.py",
        importance="Must",
        question="How do you revoke a stateless JWT? Walk through the OAuth authorization code flow with PKCE.",
        breakdown="10 min read / 15 min fix / 5 min recall",
        action="Add .env to .gitignore and rotate every key currently sitting in it. Do this one first, before the reading.",
    ),
    dict(
        slug="Capstone_Mock",
        track="System Design Practice",
        main_topic="The 4-Step Framework & Design CareerG1 Out Loud",
        primer_section="How to approach a system design interview question; System design interview questions with solutions",
        must_know="Step 1 use cases, constraints, assumptions. Step 2 high-level design. Step 3 core components. Step 4 scale it and name the bottlenecks. State assumptions out loud. A candidate who opens with 'we'll use Kafka' fails even with the right answer.",
        why="This is your story and the session that converts the other ten into interview answers. Being able to design AND honestly critique CareerG1 for 30 minutes - naming its current weaknesses and what you would fix first - is worth more than any memorised template.",
        files="(whole project)",
        importance="Must",
        question="Tell me about a system you built. Where does it break at 100x, and what would you fix first?",
        breakdown="30 min timed mock, spoken out loud",
        action="Whiteboard CareerG1 through all 4 steps in 30 minutes, recorded, then name your top 3 bottlenecks.",
    ),
]

assert len(TOPICS) == len(SATS), f"{len(TOPICS)} topics vs {len(SATS)} Saturdays"

# Everything cut to fit 30 min/Saturday. Kept so nothing is silently dropped.
BACKLOG = [
    ("Appendix > Powers of two table; Latency numbers every programmer should know",
     "Back-of-envelope estimation", "Read once before Session 02 - it is a 10 min skim and it makes every capacity answer sharper."),
    ("Availability vs consistency > Availability patterns",
     "Fail-over (active-passive / active-active), replication, availability in nines",
     "Pair with Session 02 if you get a spare Saturday. CareerG1 is currently a SPOF at every layer."),
    ("Domain name system", "DNS records, TTL, latency/geo routing",
     "Low interview frequency for backend roles. Read when you actually set up api./app. subdomains."),
    ("Content delivery network", "Push vs pull CDN, edge TTL, cache busting",
     "Worth 20 min once the Vite bundle and generated PDFs go to production."),
    ("Reverse proxy (web server); Load balancer vs reverse proxy",
     "TLS termination, gzip, upload limits, proxy vs LB",
     "Read alongside Session 03. Needed the day you put Nginx/Traefik in front of uvicorn."),
    ("Application layer; Microservices", "Web tier vs app tier, service boundaries, monolith-first",
     "High interview value. This is the API-vs-agent-worker split for CareerG1 - promote it if you gain time."),
    ("Application layer > Service discovery", "Registries, heartbeats, liveness vs readiness",
     "entrypoint.sh does this by hand today. Read before any move to Kubernetes."),
    ("Database > Relational database management system (RDBMS)", "ACID in detail",
     "Folded into Session 02 and 05 at a shallow level. Read the full definition if asked to define ACID cold."),
    ("Database > NoSQL > Wide column store; Graph database",
     "Column families, BigTable/Cassandra model, nodes and edges",
     "Skimmed in Session 07. The graph model is the natural fit for skill_gap traversal."),
    ("Cache > Client caching; CDN caching; Web server caching; Database caching",
     "The full cache layer stack and HTTP cache headers",
     "Session 04 covers application caching only. Add ETag/Cache-Control headers when you have an hour."),
    ("Cache > Caching at the database query level", "Query-key caching and why invalidation is hard",
     "Deliberately deprioritised - Session 04 teaches you to cache objects instead."),
    ("Asynchronism > Back pressure", "Bounded queues, 429 + Retry-After, circuit breakers, bulkheads",
     "Mentioned in Session 08. Read properly before you ship the queue, or it will grow unbounded."),
    ("Communication > Hypertext transfer protocol (HTTP)",
     "Verbs, status codes, keep-alive, connection pooling",
     "Partly in Session 09. Connection pooling on outbound Azure OpenAI calls is a real CareerG1 fix."),
    ("Communication > Transmission control protocol (TCP); User datagram protocol (UDP)",
     "Handshake, ordered delivery, when UDP wins",
     "Commonly asked as a warm-up question. 15 min of reading covers it."),
    ("Communication > HTTP (extension)", "Long polling vs Server-Sent Events vs WebSockets",
     "Needed for token-by-token mock-interview streaming. SSE is almost certainly your answer."),
    ("Security", "OWASP Top 10, input sanitisation, encryption at rest and in transit, least privilege",
     "Session 10 covers auth, secrets and rate limiting only. Read the rest before any real deployment."),
    ("Appendix > Real world architectures; Company engineering blogs",
     "Observability: structured logs, four golden signals, distributed tracing",
     "LANGCHAIN_TRACING_V2 already gives you agent traces - extend to the full request path later."),
    ("System design interview questions with solutions",
     "Pastebin/Bit.ly, Twitter timeline, web crawler, Mint.com, KV store, Amazon ranking, scale to millions on AWS",
     "The highest-value thing to add if you ever get more than 30 min. 'Web crawler' maps onto your market_researcher; 'scale to millions on AWS' is your deployment story."),
    ("Object-oriented design questions with solutions",
     "LRU cache, hash map, call center, parking lot, chat server, deck of cards, circular array",
     "Usually a separate coding round. LRU cache is the one to do first - it connects straight back to Session 04."),
    ("Database > Federation (deep dive); consistent hashing",
     "Resharding without downtime, consistent hashing ring",
     "Session 06 covers shard-key choice only. Consistent hashing comes up in senior loops."),
]

# ---------------------------------------------------------------- styling ---
HDR_FILL = PatternFill("solid", fgColor="1F3864")
HDR_FONT = Font(bold=True, color="FFFFFF", size=11, name="Calibri")
BAND_FILL = PatternFill("solid", fgColor="EEF3FA")
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
TOP_WRAP = Alignment(horizontal="left", vertical="top", wrap_text=True)
CENTER = Alignment(horizontal="center", vertical="top", wrap_text=True)
HDR_AL = Alignment(horizontal="center", vertical="center", wrap_text=True)

MUST_FILL = PatternFill("solid", fgColor="FFC7CE")
MUST_FONT = Font(bold=True, color="9C0006", size=11, name="Calibri")

HEADERS = [
    ("Session", 30),
    ("Track", 22),
    ("Session_No", 10),
    ("Saturday_Date", 15),
    ("Month", 12),
    ("Full Name", 18),
    ("Main_Topic", 42),
    ("Primer_Section", 46),
    ("Must_Know_In_30_Min", 66),
    ("Why_It_Matters_For_CareerG1", 72),
    ("CareerG1_Files_To_Touch", 44),
    ("Interview_Importance", 13),
    ("Top_Interview_Question", 54),
    ("30_Min_Breakdown", 22),
    ("Action_Before_You_Close_The_Laptop", 58),
    ("Est_Minutes", 11),
    ("Status", 14),
]

wb = Workbook()


def write_header(ws, headers):
    for i, (name, width) in enumerate(headers, start=1):
        c = ws.cell(row=1, column=i, value=name)
        c.fill = HDR_FILL
        c.font = HDR_FONT
        c.alignment = HDR_AL
        c.border = BORDER
        ws.column_dimensions[get_column_letter(i)].width = width
    ws.row_dimensions[1].height = 32


# ============================================================ SHEET 1 ======
ws = wb.active
ws.title = "Study Plan"
write_header(ws, HEADERS)

r = 2
for idx, (t, sat) in enumerate(zip(TOPICS, SATS), start=1):
    row = [
        f"Session_{idx:02d}_{t['slug']}",
        t["track"],
        idx,
        sat,
        sat.strftime("%B"),          # full month name
        FULL_NAME,
        t["main_topic"],
        t["primer_section"],
        t["must_know"],
        t["why"],
        t["files"],
        t["importance"],
        t["question"],
        t["breakdown"],
        t["action"],
        MINUTES_PER_SATURDAY,
        "Not started",
    ]
    for c_idx, val in enumerate(row, start=1):
        c = ws.cell(row=r, column=c_idx, value=val)
        c.border = BORDER
        c.alignment = CENTER if c_idx in (3, 4, 5, 12, 16) else TOP_WRAP
        if idx % 2 == 0:
            c.fill = BAND_FILL
    ws.cell(row=r, column=4).number_format = "ddd dd-mmm-yyyy"
    ws.cell(row=r, column=7).font = Font(bold=True, size=11, name="Calibri")
    ws.cell(row=r, column=12).fill = MUST_FILL
    ws.cell(row=r, column=12).font = MUST_FONT
    r += 1

last_row = r - 1

total = ws.cell(row=r, column=1, value="TOTAL")
for c_idx in range(1, len(HEADERS) + 1):
    c = ws.cell(row=r, column=c_idx)
    c.font = Font(bold=True, size=11, name="Calibri")
    c.fill = PatternFill("solid", fgColor="D9E2F3")
    c.border = BORDER
    c.alignment = CENTER
ws.cell(row=r, column=3, value=len(TOPICS))
ws.cell(row=r, column=16, value=f"=SUM(P2:P{last_row})")
ws.cell(row=r, column=15, value=f"= {len(TOPICS) * MINUTES_PER_SATURDAY / 60:.1f} hours across the whole plan")
ws.cell(row=r, column=15).alignment = TOP_WRAP

ws.freeze_panes = "G2"
ws.auto_filter.ref = f"A1:{get_column_letter(len(HEADERS))}{last_row}"

dv = DataValidation(
    type="list",
    formula1='"Not started,In progress,Done,Needs revision"',
    allow_blank=True,
    showDropDown=False,
)
ws.add_data_validation(dv)
dv.add(f"Q2:Q{last_row}")

ws.sheet_view.showGridLines = False
ws.page_setup.orientation = "landscape"
ws.page_setup.fitToWidth = 1
ws.sheet_properties.pageSetUpPr.fitToPage = True
ws.print_title_rows = "1:1"

# ============================================================ SHEET 2 ======
ws2 = wb.create_sheet("Backlog (cut for time)")
BL_HEADERS = [
    ("Primer_Section", 58),
    ("Topic", 52),
    ("Why_It_Is_Not_In_The_11_Saturdays", 86),
    ("Status", 14),
]
write_header(ws2, BL_HEADERS)
r2 = 2
for primer_sec, topic, note in BACKLOG:
    for c_idx, val in enumerate((primer_sec, topic, note, "Not started"), start=1):
        c = ws2.cell(row=r2, column=c_idx, value=val)
        c.border = BORDER
        c.alignment = CENTER if c_idx == 4 else TOP_WRAP
        if r2 % 2 == 1:
            c.fill = BAND_FILL
    r2 += 1
dv2 = DataValidation(
    type="list",
    formula1='"Not started,In progress,Done,Needs revision"',
    allow_blank=True,
    showDropDown=False,
)
ws2.add_data_validation(dv2)
dv2.add(f"D2:D{r2-1}")
ws2.freeze_panes = "A2"
ws2.auto_filter.ref = f"A1:D{r2-1}"
ws2.sheet_view.showGridLines = False

# ============================================================ SHEET 3 ======
# Proves the plan is measured against the primer's whole index, not cherry-picked.
ws3 = wb.create_sheet("Primer Coverage")
PRIMER_INDEX = [
    ("System design topics: start here", "Pre-read", "Scalability video + article, before Session 01"),
    ("Performance vs scalability", "Session 01", "Covered"),
    ("Latency vs throughput", "Session 01", "Covered"),
    ("Availability vs consistency > CAP theorem", "Session 02", "Covered"),
    ("Consistency patterns", "Session 02", "Covered"),
    ("Availability patterns (fail-over, replication, nines)", "Backlog", "Cut for time"),
    ("Domain name system", "Backlog", "Cut for time"),
    ("Content delivery network (push / pull)", "Backlog", "Cut for time"),
    ("Load balancer (L4 / L7) + horizontal scaling", "Session 03", "Covered"),
    ("Reverse proxy (web server)", "Backlog", "Cut for time"),
    ("Application layer > Microservices", "Backlog", "Cut for time - promote if you gain a Saturday"),
    ("Application layer > Service discovery", "Backlog", "Cut for time"),
    ("Database > RDBMS + ACID", "Session 02 / 05", "Partial - shallow only"),
    ("Database > Master-slave / master-master replication", "Session 06", "Covered"),
    ("Database > Federation", "Session 06", "Covered"),
    ("Database > Sharding", "Session 06", "Covered"),
    ("Database > Denormalization", "Session 05", "Partial"),
    ("Database > SQL tuning", "Session 05", "Covered"),
    ("Database > NoSQL > Key-value store", "Session 07", "Covered"),
    ("Database > NoSQL > Document store", "Session 07", "Partial"),
    ("Database > NoSQL > Wide column store", "Backlog", "Cut for time"),
    ("Database > NoSQL > Graph database", "Backlog", "Cut for time"),
    ("Database > SQL or NoSQL", "Session 07", "Covered"),
    ("Cache > Application caching", "Session 04", "Covered"),
    ("Cache > Client / CDN / web server / DB caching", "Backlog", "Cut for time"),
    ("Cache > Query level vs object level", "Session 04", "Partial - object level only"),
    ("Cache > When to update (aside / through / behind / refresh-ahead)", "Session 04", "Covered"),
    ("Asynchronism > Message queues", "Session 08", "Covered"),
    ("Asynchronism > Task queues", "Session 08", "Covered"),
    ("Asynchronism > Back pressure", "Session 08 / Backlog", "Partial - mentioned only"),
    ("Communication > HTTP", "Backlog", "Cut for time"),
    ("Communication > TCP", "Backlog", "Cut for time"),
    ("Communication > UDP", "Backlog", "Cut for time"),
    ("Communication > RPC", "Session 09", "Covered"),
    ("Communication > REST", "Session 09", "Covered"),
    ("Communication > SSE / WebSockets / long polling", "Backlog", "Cut for time"),
    ("Security (OAuth 2.0, JWT, secrets, rate limiting)", "Session 10", "Covered"),
    ("Security (OWASP Top 10, sanitisation, encryption)", "Backlog", "Cut for time"),
    ("Appendix > Powers of two; Latency numbers", "Backlog", "Cut for time - 10 min skim"),
    ("Appendix > Real world architectures / engineering blogs", "Backlog", "Cut for time"),
    ("How to approach a system design interview question", "Session 11", "Covered"),
    ("System design questions with solutions (8 problems)", "Session 11 / Backlog", "Partial - framework only, no solved problems"),
    ("Object-oriented design questions with solutions (7 problems)", "Backlog", "Cut for time"),
]
write_header(ws3, [("Primer Index Topic", 60), ("Where", 22), ("Coverage", 46)])
for i, (topic, where, cov) in enumerate(PRIMER_INDEX, start=2):
    for c_idx, val in enumerate((topic, where, cov), start=1):
        c = ws3.cell(row=i, column=c_idx, value=val)
        c.border = BORDER
        c.alignment = TOP_WRAP if c_idx != 2 else CENTER
        if i % 2 == 0:
            c.fill = BAND_FILL
    if where == "Backlog":
        ws3.cell(row=i, column=2).font = Font(color="9C6500", size=11, name="Calibri")
ws3.freeze_panes = "A2"
ws3.auto_filter.ref = f"A1:C{len(PRIMER_INDEX) + 1}"
ws3.sheet_view.showGridLines = False

covered = sum(1 for _, w, _ in PRIMER_INDEX if w.startswith("Session"))
backlogged = sum(1 for _, w, _ in PRIMER_INDEX if w == "Backlog")

# ============================================================ SHEET 4 ======
ws4 = wb.create_sheet("How To Use")
ws4.column_dimensions["A"].width = 30
ws4.column_dimensions["B"].width = 118

NOTES = [
    ("CareerG1 System Design Plan", None),
    ("Source repo", f"{PRIMER} - every Main_Topic maps to a section of that repo's index. See the 'Primer Coverage' sheet."),
    ("Project", r"C:\Users\mouni\OneDrive\Desktop\CR\CareerG1 - FastAPI + uvicorn, SQLAlchemy + Alembic + Postgres, Redis, Docker, Vite/React frontend, Google OAuth + JWT, LangGraph agents on Azure OpenAI with Tavily search."),
    ("Schedule", "Saturdays only, 19-Sep-2026 to 28-Nov-2026 = 11 sessions. 05-Sep and 12-Sep are already past (today is 13-Sep-2026), so the plan starts on the next Saturday."),
    ("Time budget", f"{MINUTES_PER_SATURDAY} minutes per Saturday. 11 x {MINUTES_PER_SATURDAY} min = {len(TOPICS) * MINUTES_PER_SATURDAY / 60:.1f} hours total. That is what forced one topic per Saturday."),
    ("Full Name", f"Set to '{FULL_NAME}', taken from your account email. Edit column F if that is wrong."),
    (None, None),
    ("Read this before you start", None),
    ("What 5.5 hours buys", "Enough to hold a competent conversation about all 11 topics and to name the right tradeoff when asked. It is NOT enough to make you proficient, and it is not enough to actually refactor CareerG1."),
    ("What it does not buy", "The build work is separate. The Action column is a 10-15 minute note or measurement, deliberately not a refactor - a queue migration or an index sweep is hours of work, not minutes."),
    ("If you get more time", "Take from the Backlog sheet in this order: (1) Application layer & microservices, (2) the primer's solved problems - especially web crawler and scale-to-millions, (3) LRU cache as an OOD exercise."),
    (None, None),
    ("How to run a 30-minute Saturday", None),
    ("0-15 min - Read", "Open the exact Primer_Section for the row. Read only that. Do not wander into adjacent sections."),
    ("15-25 min - Do", "Do the Action_Before_You_Close_The_Laptop cell. Every one is a written artifact or a measurement, so you finish with something on disk."),
    ("25-30 min - Recall", "Answer Top_Interview_Question out loud from memory, no notes. If you cannot, set Status to 'Needs revision'."),
    ("Next Saturday", "Spend the first 5 minutes re-answering any 'Needs revision' question before starting the new topic."),
    (None, None),
    ("Notes on the topic order", None),
    ("Why this order", "Sessions 01-02 give you the vocabulary everything else is phrased in. 03-07 follow the request path (traffic, cache, database). 08-10 are the three things CareerG1 most needs. 11 is the rehearsal that turns the other ten into answers."),
    ("Do Session 10 early if you can", "Not for interview reasons. Your .env holds JWT_SECRET, SECRET_KEY, AZURE_OPENAI_KEY, GOOGLE_CLIENT_SECRET, TAVILY_API_KEY and the Postgres password in plaintext. If that file has ever been pushed anywhere, rotate those keys now rather than on 21-Nov."),
    ("Biggest project wins", "Session 05 (indexes and N+1) is the cheapest measurable speedup. Session 08 (message queues) is the biggest architectural improvement and your strongest resume story."),
    ("Coverage honesty", f"{covered} primer index topics are covered in the 11 Saturdays; {backlogged} are on the Backlog sheet. Nothing was silently dropped - check 'Primer Coverage' to see exactly what was cut."),
]
rr = 1
for label, text in NOTES:
    if label is None and text is None:
        rr += 1
        continue
    a = ws4.cell(row=rr, column=1, value=label)
    if text is None:
        a.font = Font(bold=True, size=13, color="1F3864", name="Calibri")
    else:
        a.font = Font(bold=True, size=11, name="Calibri")
        b = ws4.cell(row=rr, column=2, value=text)
        b.alignment = TOP_WRAP
    a.alignment = TOP_WRAP
    rr += 1
ws4.sheet_view.showGridLines = False

wb.save(OUT)

print(f"saved: {OUT}")
print(f"sessions={len(TOPICS)} min_each={MINUTES_PER_SATURDAY} "
      f"total={len(TOPICS) * MINUTES_PER_SATURDAY} min "
      f"({len(TOPICS) * MINUTES_PER_SATURDAY / 60:.1f} h)")
print(f"backlog={len(BACKLOG)} | primer index: covered={covered} backlog={backlogged} "
      f"of {len(PRIMER_INDEX)}")
print(f"dates: {SATS[0]} -> {SATS[-1]}")
