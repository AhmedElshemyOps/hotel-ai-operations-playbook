# Repeat Failure Correlation Review

**Prompt ID:** `08-06-repeat-failure-correlation-review`  
**Article:** 08  
**Global prompt:** 076  
**Category:** Predictive Maintenance  
**Department:** Engineering and quality teams  
**Risk:** Medium  
**Status:** Complete  
**Version:** 0.9.0

## When to use

Explore whether repeat failures correlate with location, load, part, vendor, shift, environment or maintenance history.

## Required inputs

- work-order history
- asset/location IDs
- parts
- vendor/technician categories
- load/environment data
- PM dates

## Expected outputs

- correlation matrix
- strong/weak relationships
- confounders
- verification questions
- candidate investigations

## Copy-ready template

```text
ROLE
Act as a senior hotel predictive-maintenance and reliability support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Chief Engineer / Engineering Manager / Reliability Lead / Quality / Rooms Division / Procurement as applicable]
Accountable owner/approver: Engineering Manager / Quality Manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Explore whether repeat failures correlate with location, load, part, vendor, shift, environment or maintenance history.
Property/location: [insert confirmed property and location]
Operating period / analysis window: [insert]
Asset/system/location scope: [insert]
Occupancy/load/environment context: [insert confirmed context]
Decision this analysis supports: [insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: work-order history; asset/location IDs; parts; vendor/technician categories; load/environment data; PM dates.
Approved sources: CMMS; controlled asset register; BMS/meter/sensor exports where approved; manufacturer documentation; approved PM program; verified inspection/test records; PMS for room impact; inventory/procurement records; controlled SOPs and applicable official requirements.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, owner and required source. Do not guess or backfill missing history.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: correlation matrix; strong/weak relationships; confounders; verification questions; candidate investigations.
Separate CONFIRMED SIGNALS/FACTS, CALCULATIONS, ANOMALIES, HYPOTHESES, RECOMMENDATIONS and UNRESOLVED ITEMS.
Show the evidence behind every material conclusion, the confidence level, important confounders, the qualified human owner and the next verification step.
Where data sources conflict, show the conflict explicitly.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Correlation is not causation. Do not blame a person, vendor, part or process without validated investigation.
Do not expose unnecessary guest identity, employee records, credentials, access-control details or security-sensitive building information.
The output is decision support only and remains a draft until the accountable human verifies it against approved systems and authorizes any operational action.
```

## Human approval

Engineering Manager / Quality Manager
