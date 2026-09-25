"""
Build "SOC Audit & Project Management (15-Min Sessions).xlsx".

Same shape and styling as build_careerg1_sdp_plan.py: flat tables, banded rows,
a Status dropdown, frozen panes, autofilter. Difference is the time budget -
every row here is ONE 15-minute sitting, not 30.

Written for two audiences at once, which is why every sheet has both a plain
English column and a CareerG1 column:
  - "general"  -> the industry standard as an auditor or PM would state it
  - "project"  -> what that actually means inside CareerG1 (FastAPI + SQLAlchemy
                  + Postgres + Redis + Docker + Vite/React + Google OAuth/JWT +
                  LangGraph on Azure OpenAI with Tavily search)

Standards referenced are the real, current ones:
  SOC  - AICPA SSAE 18, AT-C 205/320, 2017 Trust Services Criteria (rev. 2022)
  PM   - PMBOK Guide 7th ed. (2021), PMBOK 6th ed. process groups, PRINCE2,
         ISO 21502:2020, Scrum Guide 2020, Agile Manifesto
Management is deliberately the smallest sheet - it was asked for as a small part.
"""

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

OUT = (
    r"C:\Users\mouni\OneDrive\Desktop\system"
    r"\SOC Audit & Project Management (15-Min Sessions).xlsx"
)

FULL_NAME = "Manoj Kasula"
MINUTES = 15
BREAKDOWN = "7 min read / 5 min do / 3 min recall"

# ---------------------------------------------------------------- styling ---
HDR_FILL = PatternFill("solid", fgColor="1F3864")
HDR_FONT = Font(bold=True, color="FFFFFF", size=11, name="Calibri")
BAND_FILL = PatternFill("solid", fgColor="EEF3FA")
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
TOP_WRAP = Alignment(horizontal="left", vertical="top", wrap_text=True)
CENTER = Alignment(horizontal="center", vertical="top", wrap_text=True)
HDR_AL = Alignment(horizontal="center", vertical="center", wrap_text=True)
BOLD = Font(bold=True, size=11, name="Calibri")

PRI_FILL = {
    "Must": PatternFill("solid", fgColor="FFC7CE"),
    "Should": PatternFill("solid", fgColor="FFEB9C"),
    "Nice": PatternFill("solid", fgColor="C6EFCE"),
}
PRI_FONT = {
    "Must": Font(bold=True, color="9C0006", size=11, name="Calibri"),
    "Should": Font(bold=True, color="9C6500", size=11, name="Calibri"),
    "Nice": Font(bold=True, color="006100", size=11, name="Calibri"),
}

STATUS_LIST = '"Not started,In progress,Done,Needs revision"'

wb = Workbook()


def write_header(ws, headers):
    for i, (name, width) in enumerate(headers, start=1):
        c = ws.cell(row=1, column=i, value=name)
        c.fill = HDR_FILL
        c.font = HDR_FONT
        c.alignment = HDR_AL
        c.border = BORDER
        ws.column_dimensions[get_column_letter(i)].width = width
    ws.row_dimensions[1].height = 34


def write_rows(ws, headers, rows, center_cols=(), bold_cols=(), pri_col=None):
    """Write a banded, bordered table. Returns the last row index."""
    r = 2
    for n, row in enumerate(rows, start=1):
        for c_idx, val in enumerate(row, start=1):
            c = ws.cell(row=r, column=c_idx, value=val)
            c.border = BORDER
            c.alignment = CENTER if c_idx in center_cols else TOP_WRAP
            if n % 2 == 0:
                c.fill = BAND_FILL
            if c_idx in bold_cols:
                c.font = BOLD
        if pri_col:
            pri = ws.cell(row=r, column=pri_col).value
            if pri in PRI_FILL:
                ws.cell(row=r, column=pri_col).fill = PRI_FILL[pri]
                ws.cell(row=r, column=pri_col).font = PRI_FONT[pri]
        r += 1
    return r - 1


def finish(ws, last_row, n_cols, status_col=None, freeze="A2"):
    if status_col:
        dv = DataValidation(
            type="list", formula1=STATUS_LIST, allow_blank=True, showDropDown=False
        )
        ws.add_data_validation(dv)
        col = get_column_letter(status_col)
        dv.add(f"{col}2:{col}{last_row}")
    ws.freeze_panes = freeze
    ws.auto_filter.ref = f"A1:{get_column_letter(n_cols)}{last_row}"
    ws.sheet_view.showGridLines = False
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.print_title_rows = "1:1"


def total_row(ws, last_row, n_cols, count, minutes_col, label_col, label):
    r = last_row + 1
    for c_idx in range(1, n_cols + 1):
        c = ws.cell(row=r, column=c_idx)
        c.font = BOLD
        c.fill = PatternFill("solid", fgColor="D9E2F3")
        c.border = BORDER
        c.alignment = CENTER
    ws.cell(row=r, column=1, value="TOTAL")
    col = get_column_letter(minutes_col)
    ws.cell(row=r, column=minutes_col, value=f"=SUM({col}2:{col}{last_row})")
    ws.cell(row=r, column=label_col, value=label)
    ws.cell(row=r, column=label_col).alignment = TOP_WRAP
    return r


# ===================================================== SHEET 1: START HERE ===
ws1 = wb.active
ws1.title = "Start Here"
S1_HEADERS = [("#", 5), ("Read This First", 34), ("What It Means", 104)]
START = [
    (1, "What this file is",
     "Two exam-style topics in one workbook: SOC auditing (how an auditor checks "
     "that your software is safe to trust) and Project Management (how work is "
     "planned and delivered to industry standards). A small Management sheet is "
     "included at the end because it was asked for as a small part."),
    (2, "The 15-minute rule",
     "Every single row on every sheet is sized for ONE 15-minute sitting: "
     f"{BREAKDOWN}. Do one row, tick Status, close the laptop. Do not try to read "
     "a whole sheet in one go - that is how plans die."),
    (3, "How to use it, day 1",
     "Open 'SOC Basics', do row 1. Open 'PM Basics', do row 1. That is 30 minutes "
     "and you now understand what both words mean. Everything after that is depth."),
    (4, "General vs project",
     "Two columns repeat everywhere. 'In_Simple_Words' is the general, "
     "industry-standard answer - true at any company, safe to say in an interview. "
     "'In_CareerG1' is the same idea pointed at your own codebase, so you can give "
     "a real example instead of a textbook one."),
    (5, "Which sheet is which",
     "SOC Basics = the vocabulary. SOC - Software Features = the actual audit "
     "checklist, one software feature per row (this is the main sheet). PM Basics = "
     "the standards (PMBOK, PRINCE2, ISO, Scrum). PM on CareerG1 = run your own "
     "project properly. Management = people side, kept short. Glossary = every "
     "short form spelled out."),
    (6, "Priority column",
     "Must = you will be asked this, or it is a real audit finding if missing. "
     "Should = expected of a mid-level engineer or PM. Nice = good to know, "
     "safe to skip on a deadline. Filter on Must if you only have an hour."),
    (7, "Status column",
     "Dropdown on every sheet: Not started / In progress / Done / Needs revision. "
     "Use 'Needs revision' honestly - it is the only column that tells you where to "
     "come back to."),
    (8, "If someone asks you to explain this",
     "One sentence: SOC is an outside auditor checking that the controls you claim "
     "to have actually work, and project management is the agreed way of planning, "
     "tracking and closing the work - both exist so that other people can trust "
     "your system without reading your code."),
    (9, "Standards this file follows",
     "SOC: AICPA SSAE 18, AT-C 205 and AT-C 320, 2017 Trust Services Criteria "
     "(revised 2022). PM: PMBOK Guide 7th edition (2021) plus the 6th edition "
     "process groups still used in exams, PRINCE2, ISO 21502:2020, Scrum Guide "
     "2020, Agile Manifesto. Nothing here is invented terminology."),
    (10, "Owner",
     f"{FULL_NAME}. Re-generate any time by running build_soc_pm_plan.py - edit "
     "the content lists in that file rather than hand-fixing many cells."),
]
write_header(ws1, S1_HEADERS)
last = write_rows(ws1, S1_HEADERS, START, center_cols=(1,), bold_cols=(2,))
ws1.freeze_panes = "A2"
ws1.sheet_view.showGridLines = False
ws1.page_setup.orientation = "landscape"
ws1.page_setup.fitToWidth = 1
ws1.sheet_properties.pageSetUpPr.fitToPage = True

# ==================================================== SHEET 2: SOC BASICS ===
# Vocabulary first. You cannot audit a feature until these words are automatic.
SOC_BASICS = [
    ("What SOC stands for",
     "System and Organization Controls. A report written by an independent "
     "licensed CPA firm that says whether the controls a company claims to have "
     "are really designed well and really working.",
     "A customer asks 'is your app safe?'. Instead of you saying yes, an outside "
     "auditor says it for you, in a report your customer's own auditor accepts.",
     "It is the standard way software companies prove trust without letting "
     "customers inspect their servers. No SOC 2 report often means no enterprise deal.",
     "AICPA - SSAE 18",
     "What is a SOC report and who writes it?",
     "Must"),
    ("SOC 1 vs SOC 2 vs SOC 3",
     "SOC 1 is about controls that affect your customer's FINANCIAL numbers. "
     "SOC 2 is about security and operations of the system. SOC 3 is a short, "
     "public, marketing-safe summary of SOC 2 with no test detail.",
     "Payroll processor -> SOC 1, because it changes your books. A cloud app "
     "holding user data -> SOC 2. The badge on a public website -> SOC 3.",
     "Picking the wrong one wastes months. Engineers almost always live in SOC 2.",
     "AT-C 320 (SOC 1), AT-C 205 (SOC 2/3)",
     "Your client handles our invoices. Which SOC report do you ask for?",
     "Must"),
    ("Type 1 vs Type 2",
     "Type 1 = a photograph. On one single date, were the controls DESIGNED "
     "properly? Type 2 = a video. Over a period, usually 3 to 12 months, did the "
     "controls actually OPERATE properly? Type 2 needs evidence from the whole period.",
     "Type 1: 'you have a locked door'. Type 2: 'the door was locked every night "
     "for six months, here are the logs'.",
     "Type 1 is a starter report. Customers who care will ask for Type 2. Almost "
     "every audit finding is a Type 2 finding, because that is where reality shows up.",
     "2017 TSC / SSAE 18",
     "Why is a Type 2 report worth more than a Type 1?",
     "Must"),
    ("The 5 Trust Services Criteria",
     "Security, Availability, Processing Integrity, Confidentiality, Privacy. "
     "Security is compulsory in every SOC 2. The other four are optional and you "
     "choose them based on what you promise customers.",
     "An app that promises 99.9% uptime adds Availability. An app storing resumes "
     "and personal details adds Confidentiality and Privacy.",
     "These five words decide the whole scope of your audit. Adding one you do not "
     "need means dozens of extra controls to evidence.",
     "2017 TSC (rev. 2022)",
     "Which Trust Services Criteria would you include, and why those?",
     "Must"),
    ("Common Criteria CC1 to CC9",
     "The Security criterion split into nine groups: CC1 control environment "
     "(tone at the top), CC2 communication, CC3 risk assessment, CC4 monitoring, "
     "CC5 control activities, CC6 logical and physical access, CC7 system "
     "operations, CC8 change management, CC9 risk mitigation and vendors.",
     "As an engineer you mostly touch CC6 (who can log in to what), CC7 "
     "(monitoring, incidents, backups) and CC8 (how code reaches production).",
     "Every technical control you will ever be asked for maps to CC6, CC7 or CC8. "
     "Knowing those three numbers makes you sound fluent instantly.",
     "2017 TSC Common Criteria",
     "Where does code review sit in the Common Criteria?",
     "Must"),
    ("Control, policy, procedure",
     "A POLICY is the rule you promise ('all code is reviewed'). A PROCEDURE is "
     "the steps to follow it. A CONTROL is the specific check that makes it happen "
     "and can be tested ('GitHub branch protection blocks merge without 1 approval').",
     "Policy: 'access is removed when people leave'. Control: 'the offboarding "
     "ticket has a mandatory revoke-access step, and HR closes it within 24 hours'.",
     "Auditors test controls, not policies. A beautiful policy with no control "
     "behind it is the single most common SOC 2 failure.",
     "COSO framework (underpins CC1)",
     "What is the difference between a policy and a control?",
     "Must"),
    ("Evidence and sampling",
     "Evidence is proof a control ran: screenshots, tickets, logs, approvals, "
     "config exports. An auditor cannot check all 5,000 deploys, so they take a "
     "SAMPLE - maybe 25 - and if all 25 pass, they accept the whole population.",
     "'Show me 25 randomly chosen pull requests from the last 6 months and prove "
     "each had an approval before merge.'",
     "If one of those 25 has no approval, that is an exception on the report. This "
     "is why controls must be automated - humans forget 1 time in 25.",
     "AT-C 205, AICPA sampling guidance",
     "How does an auditor test a control they cannot inspect fully?",
     "Must"),
    ("Exception and opinion types",
     "An EXCEPTION is one instance where the control did not work. Enough of them "
     "and the opinion changes: UNQUALIFIED (clean, what you want), QUALIFIED "
     "(mostly fine except this), ADVERSE (controls are not effective), DISCLAIMER "
     "(auditor could not form an opinion).",
     "Two of 25 sampled terminated employees still had active accounts -> "
     "exception on CC6, likely a qualified opinion on access control.",
     "'Unqualified' sounds negative in normal English but it is the best result. "
     "Mixing this up in an interview is memorable for the wrong reason.",
     "AT-C 205",
     "Is an unqualified opinion good or bad?",
     "Must"),
    ("Management assertion and system description",
     "Before the auditor tests anything, the company's own management writes a "
     "signed statement describing the system and asserting the controls are "
     "suitably designed and operating. The auditor then tests that assertion.",
     "Section 2 of any SOC 2 report is management's description - the auditor's "
     "opinion in Section 1 is an opinion ABOUT that description.",
     "It means the company is legally on the hook for what it claims, not just the "
     "auditor. Engineers get asked to fact-check the system description.",
     "SSAE 18 requirement",
     "Whose claim is the auditor actually testing?",
     "Should"),
    ("Observation period and bridge letter",
     "The observation (or review) period is the window a Type 2 covers, e.g. "
     "1 Jan to 30 Jun. A BRIDGE LETTER, also called a gap letter, is a short "
     "company-signed note covering the gap between the period end and today.",
     "Your report ends 30 June, a customer asks in September. You send the report "
     "plus a bridge letter saying nothing material changed July to September.",
     "There is always a gap - reports are historical. Knowing the fix is a bridge "
     "letter is a genuinely practical answer.",
     "AICPA practice guidance",
     "Our report ended 4 months ago. What do you send the customer?",
     "Should"),
    ("CUECs - complementary user entity controls",
     "Controls the report assumes YOU, the customer, will perform. The provider is "
     "only secure if you do your half.",
     "A cloud provider's report says 'user entities are responsible for enabling "
     "MFA and managing their own user permissions'. If you skip that, the "
     "provider's clean report does not protect you.",
     "This is where shared-responsibility arguments are won. Read the CUEC list of "
     "any vendor report you accept.",
     "2017 TSC / SOC 2 reporting",
     "You read a vendor's clean SOC 2. What must you still do yourself?",
     "Should"),
    ("Subservice organizations: carve-out vs inclusive",
     "Your providers' providers. CARVE-OUT excludes them and just says they exist "
     "(you then read their own report). INCLUSIVE pulls their controls into your "
     "report and tests them too. Carve-out is far more common.",
     "You run on Azure. Your SOC 2 carves Azure out and points to Azure's own "
     "report, rather than your auditor testing Microsoft's data centres.",
     "Explains why one report is never enough - trust is a chain, and you have to "
     "collect a report per link.",
     "SSAE 18 (a key change from SSAE 16)",
     "How does your report handle the cloud provider underneath you?",
     "Should"),
    ("Readiness assessment / gap analysis",
     "A practice run before the real audit. Someone lists every required control, "
     "checks what you actually have, and gives you the gap list to fix first.",
     "Readiness finds you have no formal access review and no documented incident "
     "response. You fix both before the clock on the observation period starts.",
     "Going straight to a Type 2 without readiness is how companies collect a page "
     "of exceptions. Cheap step, saves the expensive one.",
     "Common practice, not a formal AICPA stage",
     "Where would you start if we had no SOC 2 at all today?",
     "Should"),
    ("SOC 2 vs ISO 27001 vs other frameworks",
     "SOC 2 is a US attestation REPORT with an auditor's opinion, written per "
     "company and re-done yearly. ISO 27001 is an international CERTIFICATE for "
     "having a working information security management system. Very overlapping "
     "controls, different deliverable.",
     "US customers usually ask for SOC 2. European and Asian enterprise customers "
     "often ask for ISO 27001. Many companies get both off one control set.",
     "Shows you understand compliance as a business tool rather than a checkbox, "
     "which is exactly the senior-sounding answer.",
     "AICPA vs ISO/IEC 27001:2022",
     "SOC 2 or ISO 27001 - which do we need?",
     "Nice"),
    ("Continuous monitoring and automation",
     "Instead of screenshotting evidence once a year, tools watch your cloud, code "
     "host and HR system all the time and collect evidence automatically.",
     "A compliance tool alerts the moment an S3-style bucket turns public or a "
     "repo loses branch protection, rather than the auditor finding it in month 11.",
     "This is where the industry has moved. Manual evidence collection does not "
     "scale past one audit cycle.",
     "Trend, supported under CC4 monitoring",
     "How would you avoid a month of screenshot-gathering next year?",
     "Nice"),
]
ws2 = wb.create_sheet("SOC Basics")
S2_HEADERS = [
    ("No", 5),
    ("Topic", 34),
    ("In_Simple_Words", 74),
    ("Real_Life_Example", 62),
    ("Why_It_Matters", 62),
    ("Standard_Reference", 26),
    ("Interview_Question", 50),
    ("Priority", 10),
    ("15_Min_Breakdown", 20),
    ("Est_Minutes", 11),
    ("Status", 14),
]
write_header(ws2, S2_HEADERS)
rows2 = [
    (i, t[0], t[1], t[2], t[3], t[4], t[5], t[6], BREAKDOWN, MINUTES, "Not started")
    for i, t in enumerate(SOC_BASICS, start=1)
]
last2 = write_rows(ws2, S2_HEADERS, rows2, center_cols=(1, 8, 10), bold_cols=(2,), pri_col=8)
total_row(ws2, last2, len(S2_HEADERS), len(rows2), 10, 7,
          f"{len(rows2)} sittings = {len(rows2) * MINUTES / 60:.2f} hours")
finish(ws2, last2, len(S2_HEADERS), status_col=11, freeze="C2")

# ======================================= SHEET 3: SOC - SOFTWARE FEATURES ===
# The main sheet. One auditable software feature per row: what the auditor asks,
# what you hand over, which criterion it satisfies, and where it lives in CareerG1.
FEATURES = [
    ("Access control", "Role-based access control (RBAC) in the app",
     "Can a normal user reach an admin-only screen or API?",
     "Export of roles and permissions; a screenshot of a normal user being denied; "
     "the authorisation code path",
     "CC6.1, CC6.3",
     "Every user gets only the buttons and data their role allows - nothing more.",
     "Check every FastAPI route under backend/app/api/endpoints/ has a dependency "
     "that verifies the caller's role, not just that a token exists.",
     "Any logged-in student could call an admin endpoint and read other people's data.",
     "Must"),
    ("Access control", "Object-level authorisation (no IDOR)",
     "If I change the id in the URL, do I see someone else's record?",
     "Test showing user A gets 403 on user B's resource; the ownership filter in the query",
     "CC6.1",
     "Owning the login is not the same as owning the data. Each request must prove "
     "this row belongs to this user.",
     "GET /resume/{id} and roadmap endpoints must filter by the JWT's user id in the "
     "SQLAlchemy query, not trust the id in the path.",
     "The classic real-world breach: student 101 reads student 102's resume by typing 102.",
     "Must"),
    ("Authentication", "Login, SSO and MFA",
     "How do users prove who they are, and is a second factor required?",
     "Auth configuration; identity provider settings; screenshot of the MFA prompt",
     "CC6.1",
     "A password alone is one stolen sticky note away from a breach. A second factor "
     "or a trusted identity provider fixes that.",
     "CareerG1 uses Google OAuth, so Google enforces the password rules and MFA - say "
     "that out loud in an audit, it is a strength. Admin access to Azure and the DB "
     "needs its own MFA.",
     "Credential stuffing works on any app that accepts passwords with no second factor.",
     "Must"),
    ("Authentication", "Session and token lifetime, revocation",
     "How long is a token valid, and can you kill a session immediately?",
     "Token expiry config; the revocation or denylist mechanism; a log of a forced logout",
     "CC6.1, CC6.2",
     "A token is a key. Short expiry limits damage; revocation lets you change the "
     "lock when a key is stolen.",
     "JWTs in backend/app/core/jwt.py are self-contained, so they stay valid until "
     "expiry - a Redis denylist keyed on token id (jti) is the standard fix, and this "
     "is the one place you need strong consistency.",
     "A leaked long-lived token cannot be stopped; the attacker stays in until it expires.",
     "Must"),
    ("Access control", "Joiner-mover-leaver and quarterly access review",
     "Show me that everyone who left lost access, and who reviewed the list.",
     "Offboarding tickets with revoke steps; a signed quarterly review of all accounts; "
     "current user list per system",
     "CC6.2, CC6.3",
     "When someone joins, they get the right access. When they change role, old access "
     "is removed. When they leave, everything is switched off the same day.",
     "List every system that grants access - GitHub, Azure portal, Postgres, Redis, "
     "Tavily, the app's own admin role - and review them on a fixed date each quarter.",
     "Dormant accounts of ex-staff are the most commonly reported SOC 2 exception.",
     "Must"),
    ("Encryption", "Encryption in transit (TLS)",
     "Is all traffic HTTPS, with a modern TLS version and no plain HTTP fallback?",
     "TLS scan result; the HTTPS redirect config; certificate details and expiry",
     "CC6.7",
     "Data is sealed while travelling, so nobody on the network in between can read it.",
     "Terminate TLS at the load balancer or reverse proxy in front of uvicorn, force "
     "an HTTP-to-HTTPS redirect, and make sure the React app calls https only.",
     "Tokens and personal data readable on any shared or public network.",
     "Must"),
    ("Encryption", "Encryption at rest",
     "Are the database, backups and file storage encrypted on disk?",
     "Cloud console screenshot showing encryption enabled; key management settings",
     "CC6.1, C1.1",
     "If somebody walks off with the disk or a backup file, it is unreadable without keys.",
     "Enable it on the managed Postgres instance AND on backup snapshots - people "
     "routinely encrypt the database and forget the backups. Uploaded resumes count too.",
     "A stolen or misplaced backup becomes a full data breach.",
     "Must"),
    ("Secrets", "Secrets management - no credentials in code",
     "Show me where API keys live and prove none are in the repository history.",
     "Secret manager config; secret-scanning results; proof of key rotation",
     "CC6.1, CC6.3",
     "Passwords and API keys live in a locked vault the app reads at startup, never "
     "typed into code or committed to git.",
     "The Azure OpenAI key, Tavily key, Postgres URL, Google OAuth client secret and "
     "JWT signing key must all come from environment or a vault. Scan git history - "
     "a key committed once is leaked forever, even if a later commit removes it.",
     "A leaked Azure OpenAI key becomes somebody else's bill and your quota outage.",
     "Must"),
    ("Logging", "Audit logging of security events",
     "Who did what, when? Show me logs of logins, permission changes and data access.",
     "Log samples for each event type; retention setting; proof logs cannot be edited",
     "CC6.1, CC7.2",
     "A tamper-proof diary of important actions, so after an incident you can tell "
     "what really happened instead of guessing.",
     "Log authentication success and failure, role changes, admin actions, and every "
     "agent run that spends tokens. Log the user id and never the token, the resume "
     "text, or the prompt contents.",
     "Without logs you cannot prove what an attacker touched - or prove they touched nothing.",
     "Must"),
    ("Change management", "Code review and branch protection",
     "Prove no code reaches production without an independent approval.",
     "Branch protection settings; 25 sampled merged PRs each with an approval and a "
     "linked ticket",
     "CC8.1",
     "Somebody other than the author has to look at a change before it goes live, and "
     "the tool enforces it rather than trusting memory.",
     "Turn on branch protection on main: require 1 approval, require CI to pass, block "
     "force-push. If you are the only developer, document that and compensate with "
     "mandatory CI checks plus a self-review checklist - auditors accept a stated, "
     "consistent compensating control.",
     "This is the single most-sampled control in SOC 2. One unapproved merge in the "
     "sample is an exception.",
     "Must"),
    ("Change management", "CI/CD pipeline and separation of duties",
     "Can a developer deploy to production by hand, bypassing the pipeline?",
     "Pipeline definition; deploy history; list of who holds production credentials",
     "CC8.1, CC6.3",
     "Deployments go through one automated, logged road. No side doors, no laptops "
     "pushing to production.",
     "Build the Docker image in CI, tag it, and deploy that tag - never docker build on "
     "a production host. Every deploy then has an automatic record of what and when.",
     "Untracked manual deploys mean the running code is not the reviewed code.",
     "Must"),
    ("Change management", "Environment separation and test data",
     "Are dev, staging and production separate, and is real user data used in testing?",
     "Infrastructure showing separate databases and credentials; the data-masking step",
     "CC8.1, C1.1",
     "Experiments cannot touch real customers, and real personal data never gets copied "
     "into a test environment.",
     "Separate Postgres databases and separate Azure OpenAI keys per environment. Never "
     "restore a production dump of real resumes into local development - mask it first.",
     "A test script wiping the live table, or personal data spread across laptops.",
     "Must"),
    ("Availability", "Backups with a tested restore",
     "When did you last RESTORE a backup, not just take one?",
     "Backup schedule and success logs; a dated restore test record with the outcome",
     "A1.2, CC7.5",
     "Copies are taken automatically on a schedule, AND somebody has actually proved a "
     "copy can be turned back into a working system.",
     "Schedule automated Postgres backups, keep them off the same host, and do one "
     "documented restore into a scratch database. Redis holds cache and rate-limit "
     "counters, so it can be rebuilt - say that, it shows you know what is precious.",
     "Untested backups fail exactly when you need them. An auditor treats 'never "
     "restored' as no backup at all.",
     "Must"),
    ("Availability", "RPO and RTO agreed and written down",
     "How much data can you afford to lose, and how fast must you be back?",
     "The documented targets; incident records showing actual times achieved",
     "A1.1, A1.2",
     "RPO = how far back you would have to rewind (data lost). RTO = how long users "
     "would be down. Numbers, agreed in advance.",
     "For CareerG1, losing offers and placements is unacceptable, so pick a short RPO "
     "for Postgres. Losing cached market research is fine - it can be recomputed. "
     "Different data, different targets.",
     "Without numbers, every outage becomes an argument instead of a plan.",
     "Should"),
    ("Availability", "Monitoring, alerting and health checks",
     "Who gets told when the system breaks, and how fast?",
     "Dashboards; alert rules; a real alert with the time someone acknowledged it",
     "CC7.1, CC7.2, A1.1",
     "Machines watch the system constantly and wake a human when something is wrong - "
     "before the customer calls.",
     "Expose a /health endpoint for the load balancer, track error rates and p95 latency "
     "on the agent endpoints, and alert on Azure OpenAI spend and Tavily quota. Alert on "
     "p95 or p99, never the average.",
     "Finding out about downtime from an angry user is a monitoring finding, not bad luck.",
     "Must"),
    ("Incident response", "Documented incident response plan",
     "Walk me through your last incident: who was called, what was decided, what changed?",
     "The written plan with roles and severity levels; incident tickets; a post-mortem",
     "CC7.3, CC7.4, CC7.5",
     "A written plan for when things go wrong: how to spot it, who leads, who tells "
     "customers, and what you fix afterwards so it does not repeat.",
     "One page is enough at your size: severity levels, your own phone number, how to "
     "roll back a Docker tag, how to rotate a leaked key, and a blameless post-mortem "
     "template.",
     "Improvising during an outage costs hours and usually makes it worse.",
     "Must"),
    ("Vulnerability mgmt", "Dependency and container scanning, patching SLA",
     "How do you learn a library you use has a critical flaw, and how fast do you patch?",
     "Scanner output; the patching timeframe policy; tickets showing fixes inside it",
     "CC7.1, CC7.2",
     "Something automatically checks your libraries and images against known-flaw lists, "
     "and you have an agreed deadline to fix by severity.",
     "Run dependency scanning on requirements and package.json plus an image scan in CI. "
     "The LangChain, FastAPI and React trees are large - unscanned is not an option.",
     "Most breaches use a known flaw with a patch already available.",
     "Must"),
    ("Vulnerability mgmt", "Penetration test and remediation",
     "When was the last external test, and did you fix what it found?",
     "Pen test report; the remediation tracker showing each finding closed",
     "CC4.1, CC7.1",
     "You pay skilled outsiders to attack the app on purpose, then fix what they find "
     "and prove you fixed it.",
     "Annual is the norm. Point them at the auth flow, the resume upload, and the agent "
     "endpoints, since those touch personal data and paid third parties.",
     "A pen test with no closed findings is worse than none - it proves you knew.",
     "Should"),
    ("Data protection", "Data classification and PII inventory",
     "What personal data do you hold, where exactly is it, and who can read it?",
     "A data inventory or map; classification labels; the access list per store",
     "C1.1, P1.1, P2.1",
     "A written list of what data you hold, how sensitive each kind is, and where it sits. "
     "You cannot protect what you have never listed.",
     "CareerG1 is PII-heavy and this is the row to take seriously: resumes contain names, "
     "phone numbers, addresses, education and employment history. Offers and placements "
     "are sensitive too. List every place they land - Postgres, uploaded files, logs, and "
     "anything sent to Azure OpenAI.",
     "You cannot answer a deletion request or a breach question about data you never mapped.",
     "Must"),
    ("Data protection", "Retention and deletion, including a real delete path",
     "If a user asks you to delete their account, what actually gets deleted?",
     "Retention schedule; the deletion code path; proof of deletion in backups and logs",
     "C1.2, P4.2",
     "Data is kept only as long as there is a reason, and 'delete my account' truly "
     "removes it - not just hides it.",
     "Cascade the delete across resumes, roadmaps, agent run history and uploaded files. "
     "Decide and document what happens to backups and log lines, because that is where "
     "deleted data quietly survives.",
     "A delete button that only sets a flag is a misrepresentation to users and a privacy finding.",
     "Must"),
    ("Data protection", "Consent, privacy notice and purpose limitation",
     "Did users agree to what you do with their data, including sending it to an AI provider?",
     "Privacy notice text; consent record with timestamp; the list of third parties named",
     "P1.1, P2.1, P3.1",
     "You tell users plainly what you collect, why, and who else sees it - and you only "
     "use it for that stated reason.",
     "Your privacy notice must say resume content is processed by a third-party AI service "
     "to generate roadmaps and market research. Users uploading a CV do not automatically "
     "expect that.",
     "Undisclosed third-party processing of personal data is a privacy finding and a legal "
     "exposure, not just an audit one.",
     "Must"),
    ("Third parties", "Vendor risk management - collect their SOC 2",
     "List your subprocessors and show the due diligence you did on each.",
     "Vendor register; each vendor's SOC 2 or ISO certificate; signed DPA; annual re-review",
     "CC9.2",
     "Anyone you hand data or uptime to is part of your risk. You check them before "
     "trusting them, and re-check yearly.",
     "Your register: Microsoft Azure (hosting and Azure OpenAI), Tavily (search), Google "
     "(OAuth), your host and CI provider. Get each one's report, confirm data handling and "
     "retention, and read their CUEC list.",
     "Your report is only as strong as the weakest vendor you never checked.",
     "Must"),
    ("Third parties", "AI-specific: what leaves your system in a prompt",
     "What exactly is sent to the model provider, is it retained, is it used for training?",
     "The provider's data-handling terms; the prompt-building code; a redaction step",
     "C1.1, CC9.2, P3.1",
     "Every prompt is an outbound data transfer. Whatever you paste into a model, you "
     "have shared with that provider.",
     "This is CareerG1's sharpest edge: LangGraph nodes put resume text into prompts. "
     "Confirm the Azure OpenAI terms on retention and training, strip or minimise "
     "identifiers before sending, and never log full prompt bodies.",
     "Auditors and enterprise customers now ask this first. 'We send the whole resume and "
     "never checked' is a finding.",
     "Must"),
    ("Resilience", "Rate limiting and abuse protection",
     "What stops one user or script from exhausting the system or your budget?",
     "Rate limit config; logs of throttled requests; the limits per endpoint",
     "CC6.6, A1.1",
     "A cap on how often one caller can hit you, so a single user cannot take the service "
     "down or drain your money.",
     "You already have a Redis rate limiter - good, and Redis is the right place because "
     "in-process counters break the moment you run a second uvicorn replica. Put the "
     "tightest limits on the agent endpoints, since each call spends real tokens.",
     "One loop in a script becomes a live outage and a very large provider bill.",
     "Must"),
    ("Secure coding", "Input validation and injection prevention",
     "How do you stop SQL injection, XSS and prompt injection?",
     "Schema definitions; the ORM query layer; output encoding; a test for each class",
     "CC6.6, CC7.1, PI1.2",
     "Never trust what arrives. Check the shape and type of every input, and keep data "
     "separate from commands.",
     "Pydantic models on FastAPI give you validation for free - use strict types instead of "
     "dicts. SQLAlchemy parameterises queries, so avoid raw SQL string building. React "
     "escapes by default, so avoid dangerouslySetInnerHTML. Add one more: a resume is "
     "untrusted text going into a prompt, so treat prompt injection as a real input class.",
     "The oldest flaws in the book still work on any endpoint that skipped validation.",
     "Must"),
    ("Secure coding", "Error handling that does not leak",
     "What does a user see when the server fails?",
     "Error handler code; a sample 500 response; log configuration",
     "CC6.6, CC7.2",
     "Users get a polite, generic message. Stack traces, queries and keys stay in your "
     "logs where only you can see them.",
     "Make sure FastAPI does not run with debug on in production, and that Azure OpenAI or "
     "database errors are caught and translated rather than returned raw.",
     "A leaked stack trace hands an attacker your library versions, file paths and query shapes.",
     "Should"),
    ("Processing integrity", "Correct, complete and timely processing",
     "How do you know the output was right and nothing was silently dropped?",
     "Validation rules; reconciliation or count checks; failed-job handling and retries",
     "PI1.1, PI1.2, PI1.3",
     "The system does the right calculation on the right data, finishes the job, and tells "
     "somebody when it does not.",
     "A LangGraph run can fail halfway. Persist run state, make retries idempotent, and "
     "surface a clear failed status instead of showing the user a half-built roadmap as if "
     "it were complete.",
     "Silent partial failures are worse than loud ones - users act on wrong output.",
     "Should"),
    ("Governance", "Risk assessment, done and documented annually",
     "Show me your risk register and what you did about the top risks.",
     "The dated risk assessment; the register with owners and treatments; evidence of action",
     "CC3.1, CC3.2, CC9.1",
     "Once a year you sit down, list what could go wrong, score it by likelihood and "
     "impact, and decide what to do about the worst ones.",
     "Your real top risks: Azure OpenAI cost runaway, resume PII exposure, single Postgres "
     "instance with no tested restore, and a leaked API key. Score and treat those four.",
     "CC3 is where auditors check you THINK about security, not just buy tools.",
     "Must"),
    ("Governance", "Security policies, approved and acknowledged",
     "Show the policy set, who approved it, and who has read it.",
     "Signed policy documents with dates; acknowledgement records; annual review evidence",
     "CC1.1, CC2.2, CC5.3",
     "The written rules exist, somebody senior signed them, everyone has confirmed they "
     "read them, and they get reviewed each year.",
     "The usual minimum set: information security, access control, change management, "
     "incident response, business continuity, acceptable use, and vendor management.",
     "Unapproved or unread policies are treated as non-existent.",
     "Should"),
    ("Governance", "Security awareness training and background checks",
     "Did everyone complete security training this year?",
     "Training completion records; onboarding checklist; background check evidence",
     "CC1.4, CC2.2",
     "People are trained to spot phishing and handle data properly, and new hires are "
     "checked before they get access.",
     "Even solo, keep a dated record that you completed training - it is a two-minute "
     "evidence item that auditors always ask for.",
     "Phishing is still the most common way in, and training is the cheapest control here.",
     "Should"),
]
ws3 = wb.create_sheet("SOC - Software Features")
S3_HEADERS = [
    ("No", 5),
    ("Area", 20),
    ("Software_Feature_To_Audit", 40),
    ("What_The_Auditor_Asks", 60),
    ("Evidence_You_Hand_Over", 62),
    ("SOC2_Criteria", 16),
    ("In_Simple_Words", 66),
    ("In_CareerG1_Do_This", 82),
    ("Risk_If_Missing", 62),
    ("Priority", 10),
    ("Est_Minutes", 11),
    ("Status", 14),
]
write_header(ws3, S3_HEADERS)
rows3 = [
    (i, f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[8], MINUTES, "Not started")
    for i, f in enumerate(FEATURES, start=1)
]
last3 = write_rows(ws3, S3_HEADERS, rows3, center_cols=(1, 6, 10, 11), bold_cols=(3,), pri_col=10)
total_row(ws3, last3, len(S3_HEADERS), len(rows3), 11, 9,
          f"{len(rows3)} features = {len(rows3) * MINUTES / 60:.2f} hours")
finish(ws3, last3, len(S3_HEADERS), status_col=12, freeze="D2")

# ===================================================== SHEET 4: PM BASICS ===
PM_BASICS = [
    ("PMI", "What a project even is",
     "A temporary piece of work with a start and an end that creates something new. "
     "Not the same as OPERATIONS, which is ongoing and repeating.",
     "Building CareerG1 is a project. Answering support tickets for CareerG1 forever "
     "is operations.",
     "Half of bad project management is treating never-ending work as a project, or "
     "running a real project with no end defined.",
     "Project, operations, deliverable, programme, portfolio",
     "What makes something a project rather than normal work?",
     "Must"),
    ("PMI", "The iron triangle and what 'done' costs",
     "Scope, time and cost are tied together, with quality in the middle. Change one "
     "and at least one other has to move.",
     "'Can we add two features and still ship Friday?' Only if cost goes up or "
     "something else drops. That sentence is the whole job.",
     "It is the single most useful thing to say in a status meeting, and it stops you "
     "silently absorbing scope by working weekends.",
     "Scope creep, triple constraint, trade-off",
     "Your sponsor wants more scope in the same deadline. What do you say?",
     "Must"),
    ("PMBOK 6", "The 5 process groups",
     "Initiating, Planning, Executing, Monitoring & Controlling, Closing. Groups of "
     "activity, not calendar phases - you re-plan while executing.",
     "Initiating = the charter. Planning = the schedule. Executing = the build. "
     "M&C = the status report. Closing = handover and lessons learned.",
     "Still the backbone of PM exams and interviews, and the vocabulary most managers "
     "learned. Closing is the one everybody skips.",
     "Process group, phase gate, tailoring",
     "Name the five process groups. Which gets skipped most?",
     "Must"),
    ("PMBOK 6", "The 10 knowledge areas",
     "Integration, Scope, Schedule, Cost, Quality, Resource, Communications, Risk, "
     "Procurement, Stakeholder. A checklist of everything a PM is responsible for.",
     "Run down the list on any project and you will find the one nobody owns - "
     "usually Communications or Stakeholder.",
     "A quick audit tool. If you can name these ten you can find the gap in any "
     "project in about five minutes.",
     "Knowledge area, scope baseline, RACI",
     "Which knowledge area is most often neglected, and why?",
     "Should"),
    ("PMBOK 7", "The shift to 12 principles and 8 performance domains",
     "The 7th edition (2021) moved from 'follow these processes' to 'deliver value, "
     "guided by principles'. 12 principles include stewardship, team, stakeholders, "
     "value, systems thinking, leadership, tailoring, quality, complexity, risk, "
     "adaptability, change. 8 performance domains replace the knowledge areas.",
     "Old question: 'did you follow the process?' New question: 'did this deliver "
     "value, and did you tailor the approach to fit?'",
     "This is the current standard. Knowing that PMBOK 7 is principle-based while 6 "
     "was process-based is exactly the detail that shows you read the real thing.",
     "Value delivery, tailoring, performance domain",
     "How does PMBOK 7 differ from PMBOK 6?",
     "Must"),
    ("PRINCE2", "7 principles, 7 themes, 7 processes",
     "A structured method, strong in the UK, Europe and government. Principles "
     "include continued business justification and manage by exception. Themes "
     "include business case, risk, change, progress. Processes run from starting up "
     "to closing a project.",
     "'Manage by exception' means the board sets tolerances and only hears from you "
     "when you are about to breach them - no weekly hand-holding.",
     "Two ideas are worth stealing even if you never use PRINCE2: continued business "
     "justification (kill projects that stopped making sense) and manage by exception.",
     "Business case, tolerance, stage boundary, product-based planning",
     "What does 'manage by exception' mean in practice?",
     "Should"),
    ("ISO", "ISO 21502:2020",
     "The international guidance standard for project management practices. ISO "
     "21500:2021 now covers context and concepts. Guidance, not a certification you "
     "pass like ISO 27001.",
     "Used when a contract or a multinational client says 'aligned to ISO project "
     "management practice' rather than naming PMI or PRINCE2.",
     "Worth one line in an interview: it shows you know standards exist beyond the "
     "American and British ones.",
     "Governance, assurance, project life cycle",
     "Name an international PM standard that is not PMBOK or PRINCE2.",
     "Nice"),
    ("Agile", "The Agile Manifesto - 4 values, 12 principles",
     "2001. Individuals and interactions over processes and tools; working software "
     "over comprehensive documentation; customer collaboration over contract "
     "negotiation; responding to change over following a plan.",
     "Note 'over', not 'instead of'. The right-hand items still have value - that "
     "half of the sentence is the half people drop.",
     "Agile is misquoted constantly to mean 'no documents, no plan'. Quoting the "
     "'over, not instead of' line correctly marks you as someone who read it.",
     "Iteration, increment, working software",
     "Does Agile mean no documentation?",
     "Must"),
    ("Scrum", "Scrum Guide 2020: 3 accountabilities, 5 events, 3 artifacts",
     "Accountabilities: Product Owner, Scrum Master, Developers. Events: the Sprint, "
     "Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective. Artifacts: "
     "Product Backlog, Sprint Backlog, Increment - each with a commitment (Product "
     "Goal, Sprint Goal, Definition of Done).",
     "Sprint Review = show the work to stakeholders. Retrospective = the team "
     "improves how it works. Different meetings, different purpose, both get merged "
     "or skipped in practice.",
     "The most commonly claimed and least accurately known framework. Say 'three "
     "accountabilities, not roles' and 'the Sprint is itself an event' - both are "
     "2020 Guide precision.",
     "Sprint, backlog refinement, Definition of Done, increment",
     "What is the difference between a Sprint Review and a Retrospective?",
     "Must"),
    ("Scrum", "Estimation: story points, planning poker, velocity",
     "Estimate relative SIZE, not hours. Points are compared to each other. Velocity "
     "is how many points the team actually finished per sprint, measured not promised.",
     "A team averaging 20 points a sprint plans about 20, not 35 because someone is "
     "hopeful. Three-point estimation (optimistic, likely, pessimistic) is the "
     "classic non-agile equivalent.",
     "The honest version of planning. Velocity is a forecasting tool for the team, "
     "and comparing velocity between teams is the classic misuse.",
     "Story point, velocity, PERT, planning poker, t-shirt sizing",
     "Why estimate in points instead of hours? Can you compare two teams' velocity?",
     "Should"),
    ("Kanban", "Flow, WIP limits and lead time",
     "Visualise the work, limit how many items are in progress at once, and measure "
     "how long an item takes end to end. No fixed sprints needed.",
     "A three-person team with nine things 'in progress' finishes nothing. Cap it at "
     "three and things start completing.",
     "The most practical fix for a stalled team, and it needs no ceremony. Starting "
     "work is easy; finishing it is the constraint.",
     "WIP limit, lead time, cycle time, cumulative flow",
     "Your team is always busy but nothing ships. What do you change?",
     "Must"),
    ("Planning", "WBS - work breakdown structure",
     "Break the deliverable down until each piece is small enough to estimate and "
     "own. Decompose the OUTCOME, not people's job titles.",
     "CareerG1 -> Auth -> Google OAuth flow -> token refresh endpoint. Now it is "
     "estimable and assignable.",
     "Anything you cannot break down, you do not understand yet - which makes the WBS "
     "a thinking tool, not paperwork.",
     "Work package, 100% rule, decomposition",
     "How small should a work package be?",
     "Must"),
    ("Planning", "Critical path, dependencies and float",
     "Find the longest chain of tasks that must happen in order - that chain sets "
     "your end date. Tasks off it have FLOAT, meaning slack to slip without hurting.",
     "If the database migration must finish before the API, which must finish before "
     "the UI, that chain is your deadline. Polishing a logo in parallel has float.",
     "Tells you where to spend attention and overtime. Crashing a task that is not on "
     "the critical path buys you nothing.",
     "Critical path, float/slack, lag, fast-tracking, crashing",
     "Everything is late. Which task do you rescue first?",
     "Must"),
    ("Control", "RAID log: risks, assumptions, issues, dependencies",
     "One living table. A RISK might happen. An ISSUE already happened. An ASSUMPTION "
     "is something you are betting on without proof. A DEPENDENCY is something you "
     "need from someone else.",
     "Risk: 'the AI provider may raise prices'. Issue: 'the provider raised prices "
     "last week'. The response is completely different.",
     "The cheapest control in project management, and confusing risk with issue is "
     "the most common status-report error.",
     "Risk register, mitigation, contingency, issue log",
     "What is the difference between a risk and an issue?",
     "Must"),
    ("Control", "Risk scoring and the four responses",
     "Score each risk by likelihood x impact to rank it. Then choose: AVOID (change "
     "the plan), MITIGATE (reduce it), TRANSFER (insure or outsource it), ACCEPT "
     "(note it and move on). Threats can also be escalated.",
     "Runaway AI spend: mitigate with caching and hard budget alerts. Provider "
     "outage: accept, but write the fallback. Both are decisions, not worries.",
     "Turns anxiety into a ranked list with owners. A risk with no owner and no chosen "
     "response is just a complaint.",
     "Qualitative/quantitative analysis, risk appetite, contingency reserve",
     "Name the four risk responses and give an example of each.",
     "Must"),
    ("Control", "Change control and baselines",
     "Freeze an agreed version of scope, schedule and cost - the BASELINE. After "
     "that, changes come as a written request, get assessed for impact, and are "
     "approved or rejected before work starts.",
     "'Just add this one field' costs two days. Through change control it is a "
     "decision with a price tag. Without it, it is a quiet slip.",
     "Scope creep is never one big change - it is thirty small ones nobody priced.",
     "Baseline, change request, CCB, impact assessment",
     "How do you stop scope creep without saying no to everything?",
     "Must"),
    ("Control", "Earned value basics: CPI and SPI",
     "Compare planned value, earned value and actual cost. CPI = EV / AC (under 1 "
     "means over budget). SPI = EV / PV (under 1 means behind schedule).",
     "CPI 0.8 means you are getting 80 paise of value per rupee spent. It is a number "
     "you can put in front of a sponsor.",
     "'We are 60% done' is an opinion. CPI and SPI are measurements - which is why "
     "they appear in every PM exam.",
     "PV, EV, AC, CPI, SPI, variance",
     "CPI is 0.8 and SPI is 1.1. What is happening on this project?",
     "Should"),
    ("People", "Stakeholders: register and power-interest grid",
     "List everyone affected, then map them by how much POWER they have against how "
     "much INTEREST they have, and communicate accordingly.",
     "High power, low interest = keep satisfied with short summaries. High power, "
     "high interest = manage closely, involve early. Low/low = monitor.",
     "Most projects fail politically, not technically. The person you forgot to "
     "inform is the person who blocks the launch.",
     "Stakeholder register, salience, engagement plan",
     "Who gets the detailed weekly report and who gets one slide?",
     "Must"),
    ("People", "RACI - who is Responsible, Accountable, Consulted, Informed",
     "Responsible does the work. Accountable is the single person answerable and "
     "signs off. Consulted gives input before. Informed is told after. Exactly ONE "
     "Accountable per row.",
     "Deploy to production: Responsible = engineer, Accountable = tech lead, "
     "Consulted = security, Informed = support team.",
     "Two Accountables means nobody is accountable. This one table resolves most "
     "'I thought you were doing it' failures.",
     "RACI, ownership, escalation path",
     "Can two people be Accountable for the same deliverable?",
     "Must"),
    ("Quality", "Definition of Done vs acceptance criteria",
     "ACCEPTANCE CRITERIA are specific to one item: what must be true for this "
     "feature to be accepted. DEFINITION OF DONE applies to every item: tested, "
     "reviewed, documented, deployed.",
     "Acceptance criteria for login: 'invalid password shows an error'. DoD for "
     "everything: 'code reviewed, tests pass, migration written, deployed to staging'.",
     "A shared DoD is what stops 'done' meaning 'it works on my laptop'. It is also "
     "your bridge to the SOC change-management control.",
     "DoD, acceptance criteria, done-done, technical debt",
     "Your developer says it is done. What does done mean here?",
     "Must"),
    ("Closing", "Closure, handover and lessons learned",
     "Confirm deliverables are accepted, hand over documentation and support, release "
     "the team, archive records, and capture what you would do differently.",
     "The retrospective nobody schedules because everyone has moved to the next "
     "project - which is why the same mistake shows up again next quarter.",
     "Skipping closure is why organisations repeat mistakes for years. It is also the "
     "step that produces the evidence an auditor will ask you for later.",
     "Administrative closure, handover, post-implementation review",
     "What are the last things you do before calling a project finished?",
     "Should"),
    ("Adjacent", "Where ITIL, CMMI and SAFe fit",
     "ITIL is for running services after launch (incidents, changes, service levels). "
     "CMMI measures process maturity 1 to 5. SAFe scales agile across many teams.",
     "You build with Scrum, then run with ITIL. SAFe appears once there are dozens of "
     "teams; below that it is usually overhead.",
     "Knowing which framework answers which question stops you applying an "
     "enterprise process to a five-person team.",
     "Service management, maturity level, programme increment",
     "We have shipped. Which framework governs what happens next?",
     "Nice"),
]
ws4 = wb.create_sheet("PM Basics")
S4_HEADERS = [
    ("No", 5),
    ("Standard", 14),
    ("Topic", 40),
    ("In_Simple_Words", 76),
    ("Real_Life_Example", 62),
    ("Why_It_Matters", 62),
    ("Key_Terms_To_Remember", 40),
    ("Interview_Question", 54),
    ("Priority", 10),
    ("15_Min_Breakdown", 20),
    ("Est_Minutes", 11),
    ("Status", 14),
]
write_header(ws4, S4_HEADERS)
rows4 = [
    (i, t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], BREAKDOWN, MINUTES, "Not started")
    for i, t in enumerate(PM_BASICS, start=1)
]
last4 = write_rows(ws4, S4_HEADERS, rows4, center_cols=(1, 2, 9, 11), bold_cols=(3,), pri_col=9)
total_row(ws4, last4, len(S4_HEADERS), len(rows4), 11, 8,
          f"{len(rows4)} sittings = {len(rows4) * MINUTES / 60:.2f} hours")
finish(ws4, last4, len(S4_HEADERS), status_col=12, freeze="D2")

# ================================================ SHEET 5: PM ON CAREERG1 ===
# The project-specific half. Each row is a real artifact you can produce in 15 min.
PM_PROJECT = [
    ("Initiating", "Project charter, one page",
     "The short document that says why this project exists, what it will deliver, "
     "who decides, and when it ends.",
     "Write it for CareerG1: goal is a working placement and career-guidance platform; "
     "deliverables are auth, job search, resume tools, roadmap agents; success is a "
     "student completing the flow end to end; you are both sponsor and PM, so say so "
     "explicitly rather than leaving it blank.",
     "New doc: docs/charter.md",
     "Must"),
    ("Initiating", "Stakeholder register",
     "The list of everyone who cares, plus what each one needs from you.",
     "Students (the users), placement or college staff (the reason it exists), you "
     "(builder and owner), and your vendors - Azure OpenAI, Tavily, Google OAuth, your "
     "host. Vendors are stakeholders because their outage becomes your outage.",
     "New doc: docs/stakeholders.md",
     "Must"),
    ("Planning", "WBS for the CareerG1 stack",
     "Break the product into work packages small enough to estimate.",
     "Level 1: Auth, Jobs, Resume, Agents, Frontend, Infra. Then break Agents into "
     "LangGraph orchestration, market researcher node, roadmap node, persistence, cost "
     "controls. Stop when a package is a day or two of work.",
     "Mirrors backend/app/ and the frontend tree",
     "Must"),
    ("Planning", "Backlog with acceptance criteria",
     "Turn the WBS into items a developer can pick up, each with a clear test for done.",
     "Write acceptance criteria for your three riskiest items: token refresh, resume "
     "upload and parse, and an agent run that fails halfway. Those three are where "
     "ambiguity will cost you most.",
     "GitHub Issues or Projects",
     "Must"),
    ("Planning", "Development approach and cadence",
     "Decide, in writing, how you will work - and keep it honest for a solo project.",
     "Kanban with a WIP limit of 2 fits a solo developer better than two-week sprints "
     "with ceremonies you will hold alone. Keep one fixed weekly review slot. Say "
     "'Kanban with WIP limit 2' rather than claiming Scrum you do not run.",
     "docs/ways-of-working.md",
     "Must"),
    ("Planning", "Milestones and a realistic schedule",
     "A handful of dated checkpoints, not a 200-line Gantt chart.",
     "Pick 4 to 6 milestones with dates and work backwards. Identify the critical path "
     "- migrations before API before UI - and be explicit about what has float.",
     "docs/roadmap.md",
     "Should"),
    ("Control", "RAID log with CareerG1's real risks",
     "The living table of risks, assumptions, issues and dependencies.",
     "Seed it with the four that are genuinely true today: (1) Azure OpenAI spend "
     "runaway - mitigate with caching plus budget alerts; (2) resume PII exposure - "
     "mitigate with access controls and minimising what goes into prompts; (3) single "
     "Postgres with no tested restore - mitigate by doing one restore; (4) Tavily or "
     "provider quota exhaustion - accept, but write the fallback path.",
     "docs/raid.md - review it weekly",
     "Must"),
    ("Control", "Definition of Done for a CareerG1 feature",
     "The one checklist every item must pass, so 'done' means the same thing twice.",
     "Proposed DoD: tests pass in CI; migration written and applied; secrets from env "
     "not code; the endpoint is authorised and rate-limited; no PII in logs; README or "
     "docs updated; deployed to staging. Notice this DoD alone satisfies several SOC "
     "controls - that is the point of writing it down.",
     "Pin it in the repo README",
     "Must"),
    ("Control", "Change and release management",
     "How a code change safely becomes a running system, with a record of each step.",
     "Branch protection on main, CI must pass, conventional commits, tagged Docker "
     "images, and a one-line CHANGELOG entry per release. This is your PM release "
     "process and your SOC CC8.1 evidence in a single mechanism.",
     "GitHub settings + CI config",
     "Must"),
    ("Control", "Cost tracking as a project metric",
     "Track spend against value delivered, not just time.",
     "Your cost driver is per-request AI and search spend, which is unusual and worth "
     "calling out. Track tokens and cost per agent run weekly, and set a hard monthly "
     "budget alert. Caching market research is simultaneously a performance win and a "
     "cost control.",
     "Azure cost alerts + a weekly note",
     "Must"),
    ("Monitoring", "A weekly status you would show a sponsor",
     "Four lines: done, next, risks, decisions needed. Every week, same format.",
     "Even solo this is worth 5 minutes - it is the artifact that proves you can "
     "report upward, and it is exactly what a PM interviewer asks to see.",
     "docs/status/YYYY-WW.md",
     "Should"),
    ("Closing", "Lessons learned per milestone",
     "Capture what worked and what did not while you still remember it.",
     "Do it at each milestone rather than at the end, because a long project has no "
     "end. Three bullets is enough: kept, dropped, changed.",
     "docs/lessons.md",
     "Should"),
]
ws5 = wb.create_sheet("PM on CareerG1")
S5_HEADERS = [
    ("No", 5),
    ("PM_Area", 14),
    ("What_To_Produce", 40),
    ("In_Simple_Words", 66),
    ("CareerG1_Specific_Content", 100),
    ("Where_It_Lives", 32),
    ("Priority", 10),
    ("Est_Minutes", 11),
    ("Status", 14),
]
write_header(ws5, S5_HEADERS)
rows5 = [
    (i, t[0], t[1], t[2], t[3], t[4], t[5], MINUTES, "Not started")
    for i, t in enumerate(PM_PROJECT, start=1)
]
last5 = write_rows(ws5, S5_HEADERS, rows5, center_cols=(1, 2, 7, 8), bold_cols=(3,), pri_col=7)
total_row(ws5, last5, len(S5_HEADERS), len(rows5), 8, 5,
          f"{len(rows5)} artifacts = {len(rows5) * MINUTES / 60:.2f} hours")
finish(ws5, last5, len(S5_HEADERS), status_col=9, freeze="D2")

# ==================================================== SHEET 6: MANAGEMENT ===
# Deliberately the shortest sheet - requested as a small part.
MGMT = [
    ("Manager vs leader",
     "A manager makes sure the agreed work gets done - plans, resources, deadlines. A "
     "leader changes what people want to do - direction, motivation, trust. Most good "
     "people do both, at different moments.",
     "Assigning the sprint is management. Convincing the team the rewrite is worth it "
     "is leadership.",
     "Should"),
    ("Delegation without dumping",
     "Hand over the OUTCOME and the authority to decide, not a list of keystrokes. "
     "Agree what 'done' looks like and when you will check in, then get out of the way.",
     "'Own search relevance, ship by Friday, ask me if you need a schema change' beats "
     "a twelve-step instruction list.",
     "Should"),
    ("1:1s that are worth attending",
     "A short regular private conversation owned by the report, not a status update. "
     "Blockers, growth, and anything they will not say in a group.",
     "Thirty minutes, every two weeks, same slot, never cancelled. Cancelling it "
     "repeatedly says more than anything you say in it.",
     "Should"),
    ("Goals: SMART and OKRs",
     "SMART = Specific, Measurable, Achievable, Relevant, Time-bound. OKRs = one "
     "ambitious Objective plus 2-4 measurable Key Results. Both exist to stop goals "
     "like 'improve performance'.",
     "Bad: 'make the app faster'. Good: 'cut p95 latency on /agents from 8s to 3s by "
     "30 November'.",
     "Must"),
    ("Feedback using SBI",
     "Situation, Behaviour, Impact. Describe when it happened, what was actually done, "
     "and the effect - then stop. No character judgments, no 'you always'.",
     "'In Tuesday's review, the migration was merged without an approval, which meant "
     "nobody caught the missing index.' Specific and arguable, not a personal attack.",
     "Must"),
    ("Team stages - Tuckman",
     "Forming, Storming, Norming, Performing, Adjourning. New teams argue before they "
     "gel. That storming phase is normal, not a hiring mistake.",
     "Knowing it is a stage stops you panicking in week three of a new team.",
     "Nice"),
    ("Conflict handling",
     "Five responses (Thomas-Kilmann): compete, collaborate, compromise, avoid, "
     "accommodate. None is always right - match it to how much the outcome and the "
     "relationship matter.",
     "A security flaw is compete or collaborate. Tabs versus spaces is accommodate, "
     "and arguing it costs more than losing it.",
     "Should"),
    ("Motivation basics",
     "Herzberg: pay and conditions stop people being unhappy but do not make them "
     "motivated - that comes from achievement, recognition, growth and autonomy.",
     "A raise does not fix boring work, which is why people leave jobs that pay well.",
     "Nice"),
    ("Prioritisation under pressure",
     "Eisenhower: urgent+important do now, important not urgent schedule (this is "
     "where real progress lives), urgent not important delegate, neither drop. MoSCoW "
     "is the same idea for scope.",
     "Backups and access reviews are always important and never urgent - until the day "
     "they are the only thing that matters.",
     "Must"),
    ("Escalation done well",
     "Escalate early with a recommendation, not late with a problem. State the issue, "
     "the impact, what you have tried, and what you want decided.",
     "'The provider quota blocks launch. I suggest caching plus a paid tier at this "
     "cost. I need a decision by Thursday.' That is a decision request, not a complaint.",
     "Must"),
]
ws6 = wb.create_sheet("Management (small part)")
S6_HEADERS = [
    ("No", 5),
    ("Topic", 32),
    ("In_Simple_Words", 84),
    ("Real_Life_Example", 76),
    ("Priority", 10),
    ("Est_Minutes", 11),
    ("Status", 14),
]
write_header(ws6, S6_HEADERS)
rows6 = [
    (i, t[0], t[1], t[2], t[3], MINUTES, "Not started")
    for i, t in enumerate(MGMT, start=1)
]
last6 = write_rows(ws6, S6_HEADERS, rows6, center_cols=(1, 5, 6), bold_cols=(2,), pri_col=5)
total_row(ws6, last6, len(S6_HEADERS), len(rows6), 6, 4,
          f"{len(rows6)} sittings = {len(rows6) * MINUTES / 60:.2f} hours")
finish(ws6, last6, len(S6_HEADERS), status_col=7, freeze="C2")

# ====================================================== SHEET 7: GLOSSARY ===
GLOSSARY = [
    ("SOC", "System and Organization Controls", "An audit report proving your controls work.", "SOC"),
    ("AICPA", "American Institute of Certified Public Accountants", "The body that writes the SOC rules.", "SOC"),
    ("SSAE 18", "Statement on Standards for Attestation Engagements No. 18", "The current rulebook auditors follow for SOC reports.", "SOC"),
    ("TSC", "Trust Services Criteria", "The five subject areas a SOC 2 can cover.", "SOC"),
    ("CC", "Common Criteria", "The nine control groups inside the Security criterion (CC1-CC9).", "SOC"),
    ("CUEC", "Complementary User Entity Control", "Something the report assumes YOU will do at your end.", "SOC"),
    ("Type 1 / Type 2", "-", "Type 1 = designed right on one date. Type 2 = worked right over a period.", "SOC"),
    ("Unqualified opinion", "-", "The clean, good result. Confusingly, it sounds negative.", "SOC"),
    ("Exception", "-", "One instance where a control did not work.", "SOC"),
    ("Bridge letter", "Gap letter", "A note covering the time between the report period end and today.", "SOC"),
    ("Carve-out", "-", "Your report excludes a sub-provider and points to their own report.", "SOC"),
    ("PII", "Personally Identifiable Information", "Data that identifies a person - a resume is full of it.", "SOC"),
    ("DPA", "Data Processing Agreement", "The contract saying how a vendor may handle your users' data.", "SOC"),
    ("RBAC", "Role-Based Access Control", "Permissions granted by role, not per person.", "SOC"),
    ("MFA", "Multi-Factor Authentication", "A password plus a second proof, like a phone code.", "SOC"),
    ("IDOR", "Insecure Direct Object Reference", "Changing an id in the URL and seeing someone else's data.", "SOC"),
    ("RPO / RTO", "Recovery Point / Recovery Time Objective", "How much data you may lose / how fast you must be back.", "SOC"),
    ("SoD", "Separation of Duties", "The person who writes a change is not the only one who approves it.", "SOC"),
    ("ISO 27001", "-", "International certificate for running an information security system.", "SOC"),
    ("PMI", "Project Management Institute", "The US body behind PMBOK and the PMP certification.", "PM"),
    ("PMBOK", "Project Management Body of Knowledge", "PMI's guide. 6th ed. = processes, 7th ed. = principles.", "PM"),
    ("PMP", "Project Management Professional", "PMI's main project manager certification.", "PM"),
    ("PRINCE2", "PRojects IN Controlled Environments", "UK/European structured method: 7 principles, themes, processes.", "PM"),
    ("ISO 21502", "-", "International guidance standard for project management.", "PM"),
    ("WBS", "Work Breakdown Structure", "Breaking the deliverable into small ownable pieces.", "PM"),
    ("RAID", "Risks, Assumptions, Issues, Dependencies", "The one table that tracks what could or did go wrong.", "PM"),
    ("RACI", "Responsible, Accountable, Consulted, Informed", "Who does it, who owns it, who is asked, who is told.", "PM"),
    ("Critical path", "-", "The longest chain of dependent tasks - it sets your end date.", "PM"),
    ("Float / slack", "-", "How long a task can slip without moving the end date.", "PM"),
    ("Baseline", "-", "The frozen agreed scope, schedule and cost you measure against.", "PM"),
    ("CCB", "Change Control Board", "The group that approves or rejects scope changes.", "PM"),
    ("Scope creep", "-", "Scope growing quietly through many small unpriced additions.", "PM"),
    ("EVM", "Earned Value Management", "Measuring progress in value earned, not time spent.", "PM"),
    ("CPI / SPI", "Cost / Schedule Performance Index", "Below 1 = over budget / behind schedule.", "PM"),
    ("DoD", "Definition of Done", "The shared checklist that makes 'done' mean the same thing every time.", "PM"),
    ("WIP", "Work In Progress", "Items started but not finished. Cap it to actually finish things.", "PM"),
    ("Velocity", "-", "Points a team actually completes per sprint. Never compare teams.", "PM"),
    ("MoSCoW", "Must, Should, Could, Won't", "A way to prioritise scope by agreement, not volume.", "PM"),
    ("ITIL", "IT Infrastructure Library", "Framework for running services after launch.", "PM"),
    ("CMMI", "Capability Maturity Model Integration", "Rates process maturity from 1 to 5.", "PM"),
    ("SAFe", "Scaled Agile Framework", "Agile stretched across many teams at enterprise scale.", "PM"),
    ("OKR", "Objectives and Key Results", "One ambitious goal plus a few measurable results.", "Management"),
    ("SMART", "Specific, Measurable, Achievable, Relevant, Time-bound", "The test for whether a goal is actually a goal.", "Management"),
    ("SBI", "Situation, Behaviour, Impact", "A feedback format that describes facts, not character.", "Management"),
    ("1:1", "One-to-one", "A short regular private meeting owned by the report.", "Management"),
]
ws7 = wb.create_sheet("Glossary")
S7_HEADERS = [
    ("Short_Form", 22),
    ("Full_Form", 52),
    ("In_Simple_Words", 84),
    ("Topic", 14),
]
write_header(ws7, S7_HEADERS)
last7 = write_rows(ws7, S7_HEADERS, GLOSSARY, center_cols=(4,), bold_cols=(1,))
ws7.freeze_panes = "A2"
ws7.auto_filter.ref = f"A1:D{last7}"
ws7.sheet_view.showGridLines = False
ws7.page_setup.orientation = "landscape"
ws7.page_setup.fitToWidth = 1
ws7.sheet_properties.pageSetUpPr.fitToPage = True
ws7.print_title_rows = "1:1"

# -------------------------------------------------------------------- save ---
wb.properties.title = "SOC Audit & Project Management - 15 Minute Sessions"
wb.properties.creator = FULL_NAME
wb.properties.description = (
    "SOC auditing of software features, project management to industry standards, "
    "and a small management section. Every row is one 15-minute sitting."
)
wb.save(OUT)

_rows = [len(START), len(rows2), len(rows3), len(rows4), len(rows5), len(rows6), len(GLOSSARY)]
_timed = len(rows2) + len(rows3) + len(rows4) + len(rows5) + len(rows6)
print(f"Saved: {OUT}")
print(f"Sheets: {len(wb.sheetnames)} -> {wb.sheetnames}")
print(f"Rows per sheet: {_rows}")
print(f"Timed sittings: {_timed} x {MINUTES} min = {_timed * MINUTES / 60:.2f} hours")
