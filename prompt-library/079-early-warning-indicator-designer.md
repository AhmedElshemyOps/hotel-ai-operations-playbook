# Early-Warning Indicator Designer

**Prompt ID:** `08-09-early-warning-indicator-designer`  
**Article:** 08  
**Global prompt:** 79  
**Category:** Predictive Maintenance  
**Department:** Engineering and quality teams  
**Risk:** High  
**Status:** Complete  
**Version:** 0.9.0

## When to use

Design candidate early-warning indicators from available operational data and define how they will be validated.

## Required inputs

- failure modes of interest
- available sensors/meters
- CMMS history
- normal operating ranges
- sampling frequency
- data ownership

## Expected outputs

- candidate indicators
- threshold hypotheses
- false-positive risks
- validation sample
- review cadence

## Copy-ready template

```text
ROLE
Act as a senior hotel predictive-maintenance and reliability support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Chief Engineer / Engineering Manager / Reliability Lead / Quality / Rooms Division / Procurement as applicable]
Accountable owner/approver: Reliability Lead / Chief Engineer

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Design candidate early-warning indicators from available operational data and define how they will be validated.
Property/location: [insert confirmed property and location]
Operating period / analysis window: [insert]
Asset/system/location scope: [insert]
Occupancy/load/environment context: [insert confirmed context]
Decision this analysis supports: [insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: failure modes of interest; available sensors/meters; CMMS history; normal operating ranges; sampling frequency; data ownership.
Approved sources: CMMS; controlled asset register; BMS/meter/sensor exports where approved; manufacturer documentation; approved PM program; verified inspection/test records; PMS for room impact; inventory/procurement records; controlled SOPs and applicable official requirements.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, owner and required source. Do not guess or backfill missing history.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: candidate indicators; threshold hypotheses; false-positive risks; validation sample; review cadence.
Separate CONFIRMED SIGNALS/FACTS, CALCULATIONS, ANOMALIES, HYPOTHESES, RECOMMENDATIONS and UNRESOLVED ITEMS.
Show the evidence behind every material conclusion, the confidence level, important confounders, the qualified human owner and the next verification step.
Where data sources conflict, show the conflict explicitly.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not deploy an alarm threshold as a safety control without engineering validation, testing and approved change control.
Do not expose unnecessary guest identity, employee records, credentials, access-control details or security-sensitive building information.
The output is decision support only and remains a draft until the accountable human verifies it against approved systems and authorizes any operational action.
```

## Human approval

Reliability Lead / Chief Engineer
