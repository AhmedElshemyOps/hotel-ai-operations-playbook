# Prompt 031 — Reservation File Quality Check

**Article:** 04 — Reservations AI Toolkit  
**Status:** Complete  
**Version:** 0.11.0

**Risk:** Medium  
**Human owner:** Reservations Supervisor  
**When to use:** Before daily arrival review or after a booking is created/imported.

### Why this prompt matters

Before arrival review, audit a reservation file for missing, conflicting or unverified operational fields. In reservations, a polished answer is not enough: the team needs traceability back to the booking record, rate or contract that actually governs the case. The prompt therefore exposes uncertainty and preserves the approval boundary before a guest-facing or system action occurs.

### Copy-ready prompt

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as a reservations operations support analyst for a hotel or serviced-apartment property.
Supported role: [Reservations Agent / Supervisor / Manager]
Accountable human owner: Reservations Supervisor

O — OPERATIONAL OBJECTIVE & CONTEXT
Before arrival review, audit a reservation file for missing, conflicting or unverified operational fields.
Property: [hotel / serviced apartment, location]
Stay/booking context: [dates, channel, segment, room type, relevant operational context]
Decision deadline: [time/date if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied approved records. Primary sources may include PMS/CRS, original booking confirmation, authorized channel/extranet record, approved rate plan, contract/rate sheet, inventory snapshot, payment-status indicator, controlled SOP/policy and documented communication log.
Required inputs:
- PMS/CRS reservation record
- channel or direct booking confirmation
- approved rate/package terms
- payment-status indicator without card data
- recorded guest requests

If records conflict, show the conflict explicitly. If a critical field is missing, stale or unverified, label it UNVERIFIED and state which system/owner must confirm it. Never infer a rate, entitlement, availability, payment status, room status or contractual term from memory.
Minimize personal data. Do not reproduce passport/ID numbers, payment-card data, credentials or unrelated sensitive notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Produce:
- reservation quality table
- missing/conflicting fields
- verification queue
- owner and deadline

Separate the output into CONFIRMED FACT, REQUEST/CLAIM, UNVERIFIED/CONFLICT, and RECOMMENDED ACTION where relevant. For each open item show owner, next action, deadline/checkpoint, evidence needed for closure and escalation trigger.
Do not mark a field correct merely because it is populated; test consistency across supplied records.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not create, modify, cancel, reinstate, merge, allocate, charge, refund, waive, upgrade or confirm a reservation. Do not promise availability, price, benefit, room type, early check-in, late checkout, compensation or exception unless an approved source and authorized human decision explicitly support it.
Risk classification: Medium.
Final operational action requires verification/approval by: Reservations Supervisor.
AI output is decision support and a draft—not the PMS/CRS record, contractual confirmation or authorization.
```

### Human verification before action

Confirm the relevant PMS/CRS record is current; resolve any source conflict; verify the applicable policy, rate or contract; check that the proposed action is within the employee's authority; and record the final approved action in the proper operational system.
