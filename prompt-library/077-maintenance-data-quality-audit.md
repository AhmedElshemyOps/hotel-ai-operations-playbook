# Maintenance Data Quality Audit

**Prompt ID:** `08-07-maintenance-data-quality-audit`  
**Article:** 08  
**Global prompt:** 077  
**Category:** Predictive Maintenance  
**Department:** Engineering and quality teams  
**Risk:** Medium  
**Status:** Complete  
**Version:** 0.9.0

## When to use

Audit CMMS and condition-monitoring data for gaps that could make predictive analysis misleading.

## Required inputs

- CMMS export
- asset register
- failure codes
- closure notes
- timestamps
- meter/sensor completeness
- room/location mapping

## Expected outputs

- data-quality scorecard
- missing/duplicate fields
- inconsistent codes
- mapping errors
- remediation backlog

## Copy-ready template

```text
ROLE
Act as a senior hotel predictive-maintenance and reliability support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Chief Engineer / Engineering Manager / Reliability Lead / Quality / Rooms Division / Procurement as applicable]
Accountable owner/approver: Engineering Manager / Data Owner

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Audit CMMS and condition-monitoring data for gaps that could make predictive analysis misleading.
Property/location: [insert confirmed property and location]
Operating period / analysis window: [insert]
Asset/system/location scope: [insert]
Occupancy/load/environment context: [insert confirmed context]
Decision this analysis supports: [insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: CMMS export; asset register; failure codes; closure notes; timestamps; meter/sensor completeness; room/location mapping.
Approved sources: CMMS; controlled asset register; BMS/meter/sensor exports where approved; manufacturer documentation; approved PM program; verified inspection/test records; PMS for room impact; inventory/procurement records; controlled SOPs and applicable official requirements.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, owner and required source. Do not guess or backfill missing history.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: data-quality scorecard; missing/duplicate fields; inconsistent codes; mapping errors; remediation backlog.
Separate CONFIRMED SIGNALS/FACTS, CALCULATIONS, ANOMALIES, HYPOTHESES, RECOMMENDATIONS and UNRESOLVED ITEMS.
Show the evidence behind every material conclusion, the confidence level, important confounders, the qualified human owner and the next verification step.
Where data sources conflict, show the conflict explicitly.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not fill missing maintenance history with assumptions. Preserve original records and make corrections only through controlled data governance.
Do not expose unnecessary guest identity, employee records, credentials, access-control details or security-sensitive building information.
The output is decision support only and remains a draft until the accountable human verifies it against approved systems and authorizes any operational action.
```

## Human approval

Engineering Manager / Data Owner
