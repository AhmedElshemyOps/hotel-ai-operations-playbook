# Downtime Forecast Scenario

**Prompt ID:** `08-08-downtime-forecast-scenario`  
**Article:** 08  
**Global prompt:** 078  
**Category:** Predictive Maintenance  
**Department:** Engineering and quality teams  
**Risk:** High  
**Status:** Complete  
**Version:** 0.9.0

## When to use

Build transparent downtime scenarios from known repair dependencies and historical ranges without promising a completion time.

## Required inputs

- current fault status
- repair steps confirmed by qualified owner
- parts/vendor lead times
- historical downtime ranges
- access constraints
- room/area impact

## Expected outputs

- best/base/worst scenario
- assumptions
- confidence level
- inventory impact
- decision triggers

## Copy-ready template

```text
ROLE
Act as a senior hotel predictive-maintenance and reliability support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Chief Engineer / Engineering Manager / Reliability Lead / Quality / Rooms Division / Procurement as applicable]
Accountable owner/approver: Engineering Manager / Rooms Division / Finance

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Build transparent downtime scenarios from known repair dependencies and historical ranges without promising a completion time.
Property/location: [insert confirmed property and location]
Operating period / analysis window: [insert]
Asset/system/location scope: [insert]
Occupancy/load/environment context: [insert confirmed context]
Decision this analysis supports: [insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: current fault status; repair steps confirmed by qualified owner; parts/vendor lead times; historical downtime ranges; access constraints; room/area impact.
Approved sources: CMMS; controlled asset register; BMS/meter/sensor exports where approved; manufacturer documentation; approved PM program; verified inspection/test records; PMS for room impact; inventory/procurement records; controlled SOPs and applicable official requirements.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, owner and required source. Do not guess or backfill missing history.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: best/base/worst scenario; assumptions; confidence level; inventory impact; decision triggers.
Separate CONFIRMED SIGNALS/FACTS, CALCULATIONS, ANOMALIES, HYPOTHESES, RECOMMENDATIONS and UNRESOLVED ITEMS.
Show the evidence behind every material conclusion, the confidence level, important confounders, the qualified human owner and the next verification step.
Where data sources conflict, show the conflict explicitly.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not present a forecast as an ETA or guest promise. Only qualified owners may confirm technical completion and room release.
Do not expose unnecessary guest identity, employee records, credentials, access-control details or security-sensitive building information.
The output is decision support only and remains a draft until the accountable human verifies it against approved systems and authorizes any operational action.
```

## Human approval

Engineering Manager / Rooms Division / Finance
