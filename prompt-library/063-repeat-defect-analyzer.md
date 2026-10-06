# Prompt 063 — Repeat Defect Analyzer

**Article:** 07 — Engineering & Maintenance AI Toolkit  
**Risk level:** Medium  
**Human owner:** Engineering Manager / Quality Manager  
**Status:** Complete  
**Version:** 0.8.0

## When to use

Analyze repeat defects across rooms, apartments and assets to identify patterns and verification hypotheses without declaring root cause from correlation alone.

## Required inputs

- CMMS work-order history
- defect codes and free text
- asset/room identifiers
- dates and recurrence
- parts replaced
- technician notes
- guest complaints where relevant
- inspection or commissioning records

## Expected outputs

- repeat-defect clusters
- frequency/recency view
- possible contributing factors
- verification plan
- recommended owners

## Copy-ready prompt

```text
ROLE
Act as a senior hotel engineering operations support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Engineering Manager / Duty Engineer / Technician Coordinator / Rooms Division / Procurement / Quality as applicable]
Accountable owner/approver: Engineering Manager / Quality Manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Analyze repeat defects across rooms, apartments and assets to identify patterns and verification hypotheses without declaring root cause from correlation alone.
Property/location: [insert confirmed property and location]
Operating date/shift/period: [insert]
Asset, room, area or system scope: [insert]
Guest/operational impact: [insert confirmed impact only]
Decision deadline: [insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: CMMS work-order history; defect codes and free text; asset/room identifiers; dates and recurrence; parts replaced; technician notes; guest complaints where relevant; inspection or commissioning records.
Approved sources: CMMS; approved asset register; PMS where room status matters; controlled engineering SOPs; manufacturer/approved technical documentation; approved permits; inventory/procurement records; verified inspection records; official regulatory or authority requirements where applicable.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, owner and required source before giving a recommendation. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: repeat-defect clusters; frequency/recency view; possible contributing factors; verification plan; recommended owners.
Separate CONFIRMED FACTS, CALCULATIONS, ASSUMPTIONS/HYPOTHESES, RECOMMENDATIONS and UNRESOLVED ITEMS.
For each proposed action, show the evidence used, responsible human owner, required dependency and closure evidence.
Where systems conflict, show the conflict explicitly and identify the verification step.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not label a technician, vendor or component as the root cause without verified evidence. Separate correlation, hypothesis and confirmed cause.
Do not expose unnecessary guest identity, employee records, credentials, access-control details or security-sensitive building information.
The output is decision support only and remains a draft until the accountable human verifies it against approved systems and authorizes the action.
```

## Human verification

Verify the output against approved CMMS/PMS/asset records, applicable technical documentation and current operating conditions. A qualified human retains technical and operational authority.
