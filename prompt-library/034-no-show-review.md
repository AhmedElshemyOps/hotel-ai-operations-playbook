# Prompt 034 — No-Show Review

**Article:** 04 — Reservations AI Toolkit  
**Status:** Complete  
**Version:** 0.11.0

**Risk:** High  
**Human owner:** Duty Manager / Reservations Supervisor / Finance as policy requires  
**When to use:** After a reservation appears to qualify for no-show handling.

### Why this prompt matters

Structure a no-show case review using confirmed arrival, contact, channel and policy evidence while keeping charge or reinstatement decisions with authorized staff. In reservations, a polished answer is not enough: the team needs traceability back to the booking record, rate or contract that actually governs the case. The prompt therefore exposes uncertainty and preserves the approval boundary before a guest-facing or system action occurs.

### Copy-ready prompt

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as a reservations operations support analyst for a hotel or serviced-apartment property.
Supported role: [Reservations Agent / Supervisor / Manager]
Accountable human owner: Duty Manager / Reservations Supervisor / Finance as policy requires

O — OPERATIONAL OBJECTIVE & CONTEXT
Structure a no-show case review using confirmed arrival, contact, channel and policy evidence while keeping charge or reinstatement decisions with authorized staff.
Property: [hotel / serviced apartment, location]
Stay/booking context: [dates, channel, segment, room type, relevant operational context]
Decision deadline: [time/date if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied approved records. Primary sources may include PMS/CRS, original booking confirmation, authorized channel/extranet record, approved rate plan, contract/rate sheet, inventory snapshot, payment-status indicator, controlled SOP/policy and documented communication log.
Required inputs:
- PMS reservation/status
- approved no-show policy
- channel terms
- approved contact log
- arrival/transport evidence if relevant

If records conflict, show the conflict explicitly. If a critical field is missing, stale or unverified, label it UNVERIFIED and state which system/owner must confirm it. Never infer a rate, entitlement, availability, payment status, room status or contractual term from memory.
Minimize personal data. Do not reproduce passport/ID numbers, payment-card data, credentials or unrelated sensitive notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Produce:
- fact chronology
- evidence gaps
- policy checkpoints
- decision items for authorized reviewer

Separate the output into CONFIRMED FACT, REQUEST/CLAIM, UNVERIFIED/CONFLICT, and RECOMMENDED ACTION where relevant. For each open item show owner, next action, deadline/checkpoint, evidence needed for closure and escalation trigger.
Do not classify a guest as a no-show or authorize a charge solely from absence in a narrative. Require the approved operational and policy evidence.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not create, modify, cancel, reinstate, merge, allocate, charge, refund, waive, upgrade or confirm a reservation. Do not promise availability, price, benefit, room type, early check-in, late checkout, compensation or exception unless an approved source and authorized human decision explicitly support it.
Risk classification: High.
Final operational action requires verification/approval by: Duty Manager / Reservations Supervisor / Finance as policy requires.
AI output is decision support and a draft—not the PMS/CRS record, contractual confirmation or authorization.
```

### Human verification before action

Confirm the relevant PMS/CRS record is current; resolve any source conflict; verify the applicable policy, rate or contract; check that the proposed action is within the employee's authority; and record the final approved action in the proper operational system.
