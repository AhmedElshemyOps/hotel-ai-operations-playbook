# Prompt 055 — Linen PAR Review

**Article:** 06 — Housekeeping Management AI Toolkit  
**Status:** Complete  
**Version:** 0.11.0

**Risk:** Medium  
**Human owner:** Housekeeping Manager / Laundry Manager / Inventory Controller

**When to use:** Review linen PAR adequacy using occupancy, laundry cycle, out-of-service linen, replacement lead time and operating buffer without inventing stock or purchase authority.

### Why this prompt matters

Housekeeping decisions often sit at the intersection of room status, guest timing, quality, engineering, inventory and workforce constraints. A useful AI output must make those dependencies visible without turning a recommendation into an operational fact.

### Copy-ready prompt

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as a senior housekeeping operations support analyst for a hotel, hotel apartment or serviced-apartment operation.
Supported role: [Housekeeping Manager / Supervisor / Room Attendant Coordinator / Quality / Front Office / Engineering as applicable]
Accountable human owner: Housekeeping Manager / Laundry Manager / Inventory Controller

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Review linen PAR adequacy using occupancy, laundry cycle, out-of-service linen, replacement lead time and operating buffer without inventing stock or purchase authority.
Property/location: [insert confirmed property and location]
Operating date/shift: [insert]
Room/apartment mix: [insert]
Occupancy / arrivals / departures / stayovers: [insert confirmed figures if relevant]
Service standards / SLA / priority rules: [insert approved standard]
Decision deadline: [insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only current, supplied and approved hotel records.
Required inputs:
- current linen counts
- approved PAR standard
- occupancy/forecast
- laundry turnaround time
- discard/damage log
- purchase lead time
- emergency buffer policy

Source hierarchy: PMS/housekeeping system and approved inspection records first; CMMS/work orders for technical status; controlled SOP/quality standard for requirements; approved inventory/laundry records for stock; approved roster/workforce system for staffing.
If an essential source is missing, stale or contradictory, label the item UNVERIFIED or CONFLICT and state who must confirm it. Do not infer that a room is ready merely because cleaning is marked complete.
Minimize personal data. Do not reproduce passport/ID numbers, payment data, access credentials, medical details, unrelated employee notes or security-sensitive information.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- PAR gap table
- risk days/items
- illustrative requirement calculation
- data-quality issues
- recommended review/actions

Separate the output into CONFIRMED FACTS, UNVERIFIED/CONFLICTS, OPERATIONAL RISKS, RECOMMENDED ACTIONS and ESCALATIONS.
For each open item include owner, next action, target time, evidence required for closure and escalation trigger.
Where you identify a possible cause or performance explanation, label it HYPOTHESIS until verified.
Show calculations and assumptions explicitly where quantities, PAR, productivity or consumption are involved.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
AI must not independently:
- change PMS or housekeeping room status;
- release a room/apartment for sale or arrival;
- override DND, privacy or access-control rules;
- close maintenance defects without verified evidence;
- approve compensation, charges, purchases or staffing changes;
- rank, discipline or make employment decisions about employees;
- determine ownership or authorize release of lost property;
- invent completion times, inspection results, stock counts or guest entitlements.

Risk classification: Medium
Final operational action requires verification/approval by: Housekeeping Manager / Laundry Manager / Inventory Controller.
AI output is decision support and a draft, not the system of record or operational authorization.
```

### Human verification

Before using the output, verify current room/task status, inspection evidence, any linked engineering or inventory record, and the relevant authority. Record the final action in the approved hotel system.
