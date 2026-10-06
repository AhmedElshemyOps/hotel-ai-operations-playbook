# Prompt 049 — Apartment Defect History Summary

**Article:** 05 — Hotel Apartment & Extended-Stay AI Toolkit  
**Status:** Complete  
**Version:** 0.11.0

**Risk:** Medium  
**Human owner:** Engineering Manager / Quality Manager  
**When to use:** Summarize recurring defect history for a serviced apartment to support maintenance planning, quality review and root-cause investigation.

### Why this prompt matters

Summarize recurring defect history for a serviced apartment to support maintenance planning, quality review and root-cause investigation. In an extended-stay environment, the same issue can affect several departments over a longer timeline. This prompt forces the AI to preserve evidence, expose uncertainty and route the final action to the accountable human rather than silently converting an observation into an operational decision.

### Copy-ready prompt

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as an extended-stay hotel and serviced-apartment operations support analyst.
Supported role: [Hotel Apartment Operations / Front Office / Housekeeping / Engineering / Guest Relations as applicable]
Accountable human owner: Engineering Manager / Quality Manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Summarize recurring defect history for a serviced apartment to support maintenance planning, quality review and root-cause investigation.
Property: [serviced apartment / hotel apartment / extended-stay property, location]
Unit/stay context: [unit type, stay stage, stay duration, segment, relevant dates]
Decision deadline or service window: [time/date if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved records. Depending on the task, valid sources may include PMS/CRS, approved booking or corporate terms, controlled SOPs, housekeeping inspections, CMMS/work orders, inventory/asset records, approved utility or meter records, access-control records, finance-status indicators and documented resident communications.
Required inputs:
- CMMS/work-order history
- inspection records
- guest/resident defect reports
- asset identifiers and maintenance dates
- out-of-service history if available

If a critical source is missing, stale, contradictory or unverified, label the item UNVERIFIED and state exactly which system or accountable owner must confirm it. Do not infer entitlement, apartment readiness, maintenance completion, financial status, utility cause, resident preference or service availability from incomplete evidence.
Minimize personal data. Do not reproduce passport/ID numbers, payment-card data, credentials, access codes, medical information or unrelated sensitive resident/employee notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Produce:
- defect history timeline
- repeat-category summary
- evidence gaps
- root-cause hypotheses and verification actions

Separate CONFIRMED FACT, REQUEST/CLAIM, UNVERIFIED/CONFLICT and RECOMMENDED ACTION. For every open operational item show: owner, next action, checkpoint/deadline, evidence required for closure and escalation trigger.
Where patterns or causes are suggested, label them HYPOTHESIS until verified by the relevant department. Preserve chronology and source references when provided.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently release an apartment, change room/unit status, approve a refund/waiver/charge, alter a reservation, promise maintenance completion, change housekeeping entitlement, diagnose a technical cause, assign liability, or create a resident benefit. Do not treat AI-generated language as proof that work was completed.
Risk classification: Medium.
Final operational action requires verification/approval by: Engineering Manager / Quality Manager.
AI output is decision support and a draft—not the PMS, CMMS, inspection record, financial record or authorization.
```

### Human verification

Before using the output operationally, verify the current system-of-record data, resolve any UNVERIFIED/CONFLICT items, confirm authority for the intended action and record the final decision in the approved hotel system.
