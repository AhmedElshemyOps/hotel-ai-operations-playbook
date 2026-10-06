# Prompt 068 — Room Out-of-Service Risk Review

**Article:** 07 — Engineering & Maintenance AI Toolkit  
**Risk level:** High  
**Human owner:** Engineering Manager / Rooms Division / Revenue  
**Status:** Complete  
**Version:** 0.8.0

## When to use

Review rooms or apartments blocked by technical defects and expose operational, guest and revenue dependencies without allowing AI to release a unit.

## Required inputs

- PMS room status
- CMMS defect/work-order status
- engineering inspection
- estimated repair window from qualified owner
- arrival/occupancy context
- parts/vendor dependency
- temporary controls
- approved room-blocking policy

## Expected outputs

- room-block portfolio
- risk/priority view
- dependency and ETA confidence
- verification gaps
- release prerequisites

## Copy-ready prompt

```text
ROLE
Act as a senior hotel engineering operations support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Engineering Manager / Duty Engineer / Technician Coordinator / Rooms Division / Procurement / Quality as applicable]
Accountable owner/approver: Engineering Manager / Rooms Division / Revenue

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Review rooms or apartments blocked by technical defects and expose operational, guest and revenue dependencies without allowing AI to release a unit.
Property/location: [insert confirmed property and location]
Operating date/shift/period: [insert]
Asset, room, area or system scope: [insert]
Guest/operational impact: [insert confirmed impact only]
Decision deadline: [insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: PMS room status; CMMS defect/work-order status; engineering inspection; estimated repair window from qualified owner; arrival/occupancy context; parts/vendor dependency; temporary controls; approved room-blocking policy.
Approved sources: CMMS; approved asset register; PMS where room status matters; controlled engineering SOPs; manufacturer/approved technical documentation; approved permits; inventory/procurement records; verified inspection records; official regulatory or authority requirements where applicable.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, owner and required source before giving a recommendation. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: room-block portfolio; risk/priority view; dependency and ETA confidence; verification gaps; release prerequisites.
Separate CONFIRMED FACTS, CALCULATIONS, ASSUMPTIONS/HYPOTHESES, RECOMMENDATIONS and UNRESOLVED ITEMS.
For each proposed action, show the evidence used, responsible human owner, required dependency and closure evidence.
Where systems conflict, show the conflict explicitly and identify the verification step.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not release, downgrade or return a room to inventory. Do not invent repair ETAs. A unit remains blocked until the authorized engineering/rooms workflow confirms all release conditions.
Do not expose unnecessary guest identity, employee records, credentials, access-control details or security-sensitive building information.
The output is decision support only and remains a draft until the accountable human verifies it against approved systems and authorizes the action.
```

## Human verification

Verify the output against approved CMMS/PMS/asset records, applicable technical documentation and current operating conditions. A qualified human retains technical and operational authority.
