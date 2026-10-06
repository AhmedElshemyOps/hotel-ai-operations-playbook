# Prompt 003 — Missing-Information Detection

**Article:** 01 — The HOTEL Prompting Framework  
**Status:** Complete  
**Version:** 0.11.0

**Purpose:** Identify missing inputs that could affect service, safety, cost, timing or authority.

**Risk level:** Medium  
**Human approval required:** Yes

**Required inputs**

- draft request
- confirmed inputs
- source systems
- decision required
- deadline

**Expected outputs**

- critical missing data
- important missing data
- optional enhancements
- owner/source for each item

**Copy-ready HOTEL prompt**

```text
ROLE
Act as a senior hotel operations prompt architect supporting professional hotel and serviced-apartment teams.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Insert user role]
Accountable owner/approver: [Insert role]

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Identify missing inputs that could affect service, safety, cost, timing or authority
Property type/location: [Insert confirmed property context]
Department / guest-journey stage / operating period: [Insert confirmed context]
Decision or workflow this output supports: [Insert decision]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: draft request; confirmed inputs; source systems; decision required; deadline.
Approved sources: [PMS / RMS / CMMS / SOP / finance report / inventory system / approved policy / official source as relevant].
If an essential input is missing, stale, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: critical missing data; important missing data; optional enhancements; owner/source for each item.
Separate CONFIRMED FACTS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
Where inputs conflict, show the conflict and proposed verification action.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not solve the business task; stop after the information request and prioritization.
Do not include unnecessary personal data, payment data, credentials, security-sensitive information, confidential contracts or employee records.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational action.
```

**Trainer note:** Test the prompt with one normal case and one missing/contradictory-information case before approving it for repeat use.
