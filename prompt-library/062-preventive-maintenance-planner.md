# Prompt 062 — Preventive Maintenance Planner

**Article:** 07 — Engineering & Maintenance AI Toolkit  
**Risk level:** High  
**Human owner:** Chief Engineer / Engineering Manager  
**Status:** Complete  
**Version:** 0.8.0

## When to use

Build a preventive-maintenance planning view from approved asset registers, manufacturer guidance, CMMS history and operating windows.

## Required inputs

- approved asset register
- current PM schedule
- manufacturer or approved maintenance requirements
- CMMS completion history
- asset criticality
- occupancy/event windows
- qualified labor availability
- required parts/permits/access

## Expected outputs

- PM due/overdue view
- operational-window proposal
- resource/dependency list
- risk flags
- human approval points

## Copy-ready prompt

```text
ROLE
Act as a senior hotel engineering operations support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Engineering Manager / Duty Engineer / Technician Coordinator / Rooms Division / Procurement / Quality as applicable]
Accountable owner/approver: Chief Engineer / Engineering Manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Build a preventive-maintenance planning view from approved asset registers, manufacturer guidance, CMMS history and operating windows.
Property/location: [insert confirmed property and location]
Operating date/shift/period: [insert]
Asset, room, area or system scope: [insert]
Guest/operational impact: [insert confirmed impact only]
Decision deadline: [insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: approved asset register; current PM schedule; manufacturer or approved maintenance requirements; CMMS completion history; asset criticality; occupancy/event windows; qualified labor availability; required parts/permits/access.
Approved sources: CMMS; approved asset register; PMS where room status matters; controlled engineering SOPs; manufacturer/approved technical documentation; approved permits; inventory/procurement records; verified inspection records; official regulatory or authority requirements where applicable.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, owner and required source before giving a recommendation. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: PM due/overdue view; operational-window proposal; resource/dependency list; risk flags; human approval points.
Separate CONFIRMED FACTS, CALCULATIONS, ASSUMPTIONS/HYPOTHESES, RECOMMENDATIONS and UNRESOLVED ITEMS.
For each proposed action, show the evidence used, responsible human owner, required dependency and closure evidence.
Where systems conflict, show the conflict explicitly and identify the verification step.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not invent maintenance intervals or replace manufacturer, statutory, insurer, authority or engineering requirements. Never recommend deferring a safety-critical PM solely for occupancy or revenue reasons.
Do not expose unnecessary guest identity, employee records, credentials, access-control details or security-sensitive building information.
The output is decision support only and remains a draft until the accountable human verifies it against approved systems and authorizes the action.
```

## Human verification

Verify the output against approved CMMS/PMS/asset records, applicable technical documentation and current operating conditions. A qualified human retains technical and operational authority.
