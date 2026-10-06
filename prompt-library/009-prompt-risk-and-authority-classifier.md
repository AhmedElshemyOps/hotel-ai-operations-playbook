# Prompt 009 — Prompt Risk and Authority Classifier

**Article:** 01 — The HOTEL Prompting Framework  
**Status:** Complete  
**Version:** 0.11.0

**Purpose:** Classify an AI hotel use case by operational risk and required human authority.

**Risk level:** Medium  
**Human approval required:** Yes

**Required inputs**

- use case
- data involved
- guest impact
- financial impact
- safety impact
- decision authority

**Expected outputs**

- risk level
- reason
- prohibited actions
- minimum reviewer
- approval requirement
- controls

**Copy-ready HOTEL prompt**

```text
ROLE
Act as a senior hotel operations prompt architect supporting professional hotel and serviced-apartment teams.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Insert user role]
Accountable owner/approver: [Insert role]

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Classify an AI hotel use case by operational risk and required human authority
Property type/location: [Insert confirmed property context]
Department / guest-journey stage / operating period: [Insert confirmed context]
Decision or workflow this output supports: [Insert decision]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: use case; data involved; guest impact; financial impact; safety impact; decision authority.
Approved sources: [PMS / RMS / CMMS / SOP / finance report / inventory system / approved policy / official source as relevant].
If an essential input is missing, stale, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: risk level; reason; prohibited actions; minimum reviewer; approval requirement; controls.
Separate CONFIRMED FACTS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
Where inputs conflict, show the conflict and proposed verification action.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not downgrade safety, privacy, financial or legal risk for convenience.
Do not include unnecessary personal data, payment data, credentials, security-sensitive information, confidential contracts or employee records.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational action.
```

**Trainer note:** Test the prompt with one normal case and one missing/contradictory-information case before approving it for repeat use.
