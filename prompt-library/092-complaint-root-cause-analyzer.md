# Complaint Root-Cause Analyzer

**Prompt ID:** `10-02-complaint-root-cause-analyzer`  
**Article:** 10  
**Global prompt:** 92  
**Category:** Service Recovery  
**Department:** Guest relations, duty management and quality  
**Risk:** Medium  
**Status:** Complete  
**Version:** 0.11.0

## When to use

Use after the case timeline and operational records are available and the team needs disciplined root-cause analysis rather than blame or speculation.

## Required inputs

- verified complaint timeline
- service/work-order/request logs
- applicable SOP/service standard
- staffing or capacity records where relevant
- previous related cases
- process owner observations
- known corrective actions

## Expected outputs

- problem statement
- cause-and-effect map
- verified causes vs hypotheses
- 5-Why analysis with evidence status
- control gaps
- recommended validation steps

## Copy-ready template

```text
ROLE
Act as a senior hotel guest-relations, service-recovery and operational-quality support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Guest Relations / Front Office / Duty Management / Quality / Operations as applicable]
Accountable owner/approver: Quality Manager / Process Owner

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Analyze a complaint after sufficient evidence exists and distinguish the immediate failure, contributing factors and validated root-cause status.
Property/location: [insert confirmed property and location]
Stay type / journey stage / complaint channel / operating period: [insert]
Guest-stated concern: [insert only what is necessary]
Departments/dependencies involved: [insert]
Decision or workflow this output supports: [insert]
Response or escalation deadline: [insert approved SLA if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: verified complaint timeline; service/work-order/request logs; applicable SOP/service standard; staffing or capacity records where relevant; previous related cases; process owner observations; known corrective actions.
Approved sources: PMS/CRS and confirmed stay facts; approved CRM/complaint or guest-request log; controlled complaint, escalation and compensation SOPs; verified department confirmations; CMMS/work orders when technical issues are involved; approved finance/refund records where applicable; approved authority matrix; original guest communication or review.
Treat the guest's description as GUEST-STATED INFORMATION unless independently verified by an approved record. Preserve the guest's words accurately when they matter, but do not convert allegation into confirmed fact.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, its owner and required verification source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: problem statement; cause-and-effect map; verified causes vs hypotheses; 5-Why analysis with evidence status; control gaps; recommended validation steps.
Separate CONFIRMED FACTS, GUEST-STATED CLAIMS/NEEDS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
For each operational action show OWNER, DUE TIME, DEPENDENCY and CLOSURE EVIDENCE where applicable.
For each guest-facing commitment show the supporting policy, system record or human approval; otherwise label it NOT YET AUTHORIZED / NOT YET CONFIRMED.
Where sources conflict, show the conflict and the safest verification action.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not convert correlation, one employee comment or one guest statement into a proven root cause. Do not assign employee fault or disciplinary conclusions. Label each cause as VERIFIED, CONTRIBUTING FACTOR, HYPOTHESIS or UNKNOWN.
Do not include unnecessary passport/ID data, payment-card information, credentials, private employee information, security-sensitive details, health data beyond the service need, or confidential contracts.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational, financial or guest-facing action.
```

## Human verification

Before operational use, verify complaint facts, current guest/stay status, authority limits, privacy need, open promises, departmental ownership and closure evidence. High-risk recovery, compensation, safety, legal, privacy, discrimination, security or CAPA decisions require the named qualified owner.
