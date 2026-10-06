# Article 04 — Reservations AI Toolkit

## 10 Professional AI Prompts for Booking Quality, Modifications, Cancellations, Allocation, Corporate Reservations and Exception Control

**Track C · Hotel & Serviced Apartment AI Operations Playbook · Reservations chapter**

A reservation is more than a name and an arrival date. It is a compact operating contract connecting inventory, price, room type, occupancy, cancellation conditions, payment or billing arrangements, channel rules, special requests and the promises the property will later be expected to deliver.

That makes Reservations an excellent use case for AI—and a dangerous place to use AI casually. A model can summarize a booking in seconds, but it can also turn a request into an entitlement, interpret the wrong cancellation rule, assume two similar bookings are duplicates, or suggest a room-type solution without understanding live inventory. The damage may not appear until check-in, when Front Office inherits a promise that was never operationally valid.

The control principle for this chapter is:

> **AI may organize reservation evidence and prepare a decision. The approved reservation system, commercial terms and authorized human still determine what is confirmed.**

The ten prompts follow the reservation-control cycle:

> **Validate → Review change → Explain terms → Review no-show → Support allocation → Structure requests → Detect duplicates → Handover → Validate corporate terms → Escalate**

---

## 1. Why reservation quality is an operations issue

Reservation errors travel downstream. An incorrect room type becomes a Front Office conflict. A missed child occupancy detail can affect bedding and capacity. An unverified airport-transfer note becomes an arrival failure. A corporate inclusion copied from an old booking can become a billing dispute. A vague cancellation explanation can become a complaint.

For that reason, the objective of Reservations AI should not be “answer faster.” It should be **reduce ambiguity before the booking reaches the next operating stage**.

A useful AI workflow can compare supplied records, extract requests, expose contradictions, prepare a structured handover and identify which cases need human intervention. It should not silently resolve a conflict by choosing whichever field looks most likely.

## 2. HOTEL framework for reservations

The common HOTEL framework applies directly:

- **H — Hospitality role & human owner:** name the reservations role and the person accountable for the final action.
- **O — Operational objective & context:** define the booking stage, stay dates, channel, segment and decision deadline.
- **T — Trusted inputs & sources of truth:** anchor analysis to PMS/CRS, approved channel records, rate plans, contracts, policies and controlled communication logs.
- **E — Expected output, exceptions & evidence:** require facts, conflicts, unknowns, next actions and closure evidence.
- **L — Limits, privacy & leadership approval:** prohibit unauthorized changes, commercial promises and unnecessary exposure of guest data.

### Reservation source-of-truth matrix

| Question | Primary approved source | AI role |
|---|---|---|
| Is the booking confirmed? | PMS/CRS or approved reservation system | Summarize; flag conflict |
| What rate/room type was booked? | Confirmed reservation + approved rate plan | Compare; do not invent |
| What cancellation terms apply? | Confirmed rate/booking terms | Explain; do not rewrite |
| Is a corporate inclusion valid? | Current approved contract/rate sheet | Validate against booking |
| Is payment complete? | Approved payment-status workflow | Report supplied status only |
| Is a request guaranteed? | Confirmed booking/approved entitlement | Separate entitlement from preference |
| Is inventory available for a change? | Authorized live inventory source | Analyze supplied snapshot; human confirms |
| Can a fee be waived? | Authority matrix + approved policy | Escalate; do not authorize |

The word **current** matters. A screenshot, copied email or last week's inventory can be useful evidence, but it should not automatically override the live controlled system.

## 3. The reservations AI control loop

| Stage | Control question | Prompt |
|---|---|---|
| Booking quality | Is the file complete and internally consistent? | 031 |
| Modification | What changes and approvals does the request trigger? | 032 |
| Cancellation | How can confirmed terms be explained accurately? | 033 |
| No-show | What evidence exists and what still requires a decision? | 034 |
| Inventory pressure | What room-type options can management review? | 035 |
| Requests | Which notes are entitlements, preferences or operational needs? | 036 |
| Duplication | Which bookings look similar enough for manual review? | 037 |
| Shift change | What open reservation work must transfer ownership? | 038 |
| Corporate | Does the booking match approved account terms? | 039 |
| Exception | What does the authorized decision-maker need to decide? | 040 |

## 4. Fictional UAE case: one booking, five possible failures

Use the fictional 60-unit UAE serviced-apartment portfolio from the previous chapters. A corporate booker creates a 21-night reservation for a one-bedroom apartment. The booking notes mention airport pickup, early arrival, breakfast and company billing. A second reservation with a similar guest name appears through an OTA for overlapping dates.

The team now has several questions. Is early arrival guaranteed or merely requested? Is breakfast included in the current corporate agreement? Does company billing cover accommodation only or incidentals as well? Is the OTA reservation a duplicate or an intentional booking for another traveler? Is airport pickup actually confirmed with Transport?

A weak AI response might “clean up” the file and conclude that the corporate booking includes all four services and that the OTA record should be cancelled as a duplicate. That would be fast—and operationally reckless.

A controlled workflow produces a verification queue instead:

| Item | Current evidence | Classification | Next action |
|---|---|---|---|
| 21-night 1BR stay | PMS confirmed | CONFIRMED FACT | none |
| Early arrival | note only | REQUEST / NOT GUARANTEED | check approved availability/process |
| Breakfast | booking note conflicts with current contract | CONFLICT | Sales/Reservations verify contract |
| Company billing | account indicator present; scope unclear | UNVERIFIED | Finance/contract owner confirms scope |
| OTA overlap | similar name/dates | POSSIBLE DUPLICATE | manually compare IDs/source/booker |
| Airport pickup | request recorded; supplier confirmation absent | UNVERIFIED | verify transport confirmation |

The difference is important: AI has made the case easier to manage without pretending to possess authority it does not have.

## 5. Risk classification in Reservations

Many reservation tasks move from MEDIUM to HIGH risk because they affect money, inventory, contractual terms or a guest's confirmed stay.

**MEDIUM** examples include extracting requests, preparing a handover or checking file completeness. The output still needs review, but the AI is mainly organizing information.

**HIGH** examples include modifications, cancellation/no-show interpretation, room-type allocation, duplicate handling and corporate billing terms. A mistake can create a charge dispute, revenue leakage, inventory displacement or a broken guest promise.

The practical rule is that AI can prepare the case, but the authorized employee executes the reservation action in the approved system.

## 6. Modification control: compare before you change

A professional modification review should show **before**, **requested**, **impact**, **unknown**, and **approval required**. This is more reliable than asking an AI model, “Can we change this booking?”

For example, changing a stay from three nights to five may affect more than dates. It can change availability, rate conditions, package eligibility, corporate terms, tax/fee calculations, room continuity and cancellation conditions. The AI should surface those dependencies rather than answer yes or no from incomplete information.

## 7. Cancellation and no-show: explain policy without becoming the policy

Guest-facing clarity is useful, particularly when rate terms are technical. But rewriting a cancellation rule must not change its meaning. The safest workflow supplies the exact confirmed booking/rate terms, relevant timestamps and approved policy, then asks AI to create a plain-language explanation while preserving the original conditions.

No-show handling needs even stronger controls. An AI summary should build a chronology of confirmed facts and evidence gaps. It should not authorize a charge, cancellation or reinstatement merely because a narrative says the guest did not arrive.

## 8. Duplicate detection: probability is not proof

Duplicate detection is a strong AI use case because models can compare patterns across names, dates, room types, sources and booking timestamps. But false positives are expensive. A spouse, colleague or family member may have a similar name; a traveler may intentionally hold two rooms; a corporate booker may create related reservations.

Therefore Prompt 037 produces **possible duplicate clusters for manual review**, never an instruction to cancel.

## 9. Special requests: protect the difference between request and entitlement

Reservation notes often contain phrases such as “high floor,” “early check-in,” “airport pickup,” “baby cot,” “quiet room,” “connecting rooms” or “late checkout.” Some may be confirmed paid services, some operational requirements, and some preferences subject to availability.

The AI should classify them rather than flatten them into a checklist of promises. This is also where Reservations connects directly to Front Office, Housekeeping, Engineering, Transport and Guest Experience.

## 10. Corporate reservations: contract before memory

Corporate accounts are especially vulnerable to institutional memory: “We normally give this company breakfast,” “they usually have late checkout,” or “Finance knows their billing.” Those statements may be operationally familiar but are not substitutes for the current approved contract or rate sheet.

Prompt 039 forces a contract-to-booking comparison and routes discrepancies to the appropriate owner. This supports Sales and Finance without allowing AI to invent negotiated terms.

## 11. Cross-website knowledge connections

Reservations should not live as an isolated knowledge pillar. On the Ahmed Quality Ops website, this chapter should connect contextually to the broader operating system:

- **The Tourism AI Operations Playbook** — for the wider responsible-AI and tourism prompting architecture: `/articles/tourism-ai-operations-playbook/index.html`
- **SOP Exception & Escalation Management** — when a reservation moves outside normal policy or frontline authority: `/articles/sop-exception-escalation-management/index.html`
- **SOP Roles, Authority & RACI** — when the problem is not missing information but unclear decision ownership: `/articles/sop-roles-authority-raci/index.html`
- **Professional SOP Procedure Design** — when recurring reservation failures need a controlled process rather than repeated case-by-case fixes: `/articles/how-to-write-professional-sop-procedure/index.html`
- **MICE operations content** — for group arrivals, rooming-list dependencies and movement coordination where accommodation connects to event operations.
- **Transport/dispatch knowledge** — when airport transfers or movement services are attached to a reservation; the reservation record should reference a confirmed transport workflow rather than assume fulfillment.

Future hotel chapters should link back here whenever they rely on reservation truth: Front Office for arrival promises, Revenue for rate/inventory decisions, OTA/Distribution for channel records, Corporate Sales for negotiated terms, Finance for billing controls and Guest Experience for service recovery.

This creates a knowledge network: **reservation → arrival → stay → service → exception → evidence → improvement**, rather than a set of disconnected articles.

## 12. Management KPIs for an AI-supported reservations workflow

AI should be evaluated against operational quality, not the number of generated messages. Useful measures include:

| KPI | What it reveals |
|---|---|
| Reservation files with unresolved critical fields before arrival | upstream data quality |
| Modification cases returned for missing evidence | process discipline / input quality |
| Confirmed-vs-requested special-request mismatches | promise-control quality |
| Possible duplicates reviewed before action | protection against false cancellation |
| Corporate booking variances detected pre-arrival | contract-control effectiveness |
| Reservation exceptions with named owner/deadline | accountability |
| Handover items closed within agreed SLA | continuity between shifts |
| Repeat reservation-error categories | improvement opportunities |

Do not invent benchmark percentages. Establish the property's baseline, define the measurement method, then improve from verified internal data.

## 13. Lean Six Sigma application

Reservations is well suited to a DMAIC-style improvement project because many defects are measurable.

**Define:** choose a defect such as incomplete special-request classification, corporate-rate mismatch or unresolved modification at arrival.

**Measure:** establish a clean operational definition and collect verified cases.

**Analyze:** stratify by channel, shift, rate plan, booking source, process step or defect category. Do not assume the AI's thematic summary is the root cause.

**Improve:** redesign the input fields, verification checkpoint, authority rule, handover or SOP.

**Control:** monitor the defect and maintain a clear exception path.

AI can accelerate coding, summarization and hypothesis generation, but the improvement team validates the data and causal conclusion.

## 14. 30-day implementation plan

**Days 1–7 — Control the inputs.** Define approved sources for booking, rate, cancellation, corporate terms, payment-status indicators and special requests. Remove unnecessary personal data from AI workflows.

**Days 8–14 — Pilot low-to-medium risk.** Start with Prompt 031, 036 and 038: file quality, request extraction and handover. Compare AI output with supervisor review.

**Days 15–21 — Introduce high-risk decision support.** Pilot modification, cancellation, duplicate, allocation and corporate validation with mandatory supervisor approval and a documented authority matrix.

**Days 22–30 — Measure and standardize.** Review recurring errors, update prompt instructions, define KPIs, connect the workflow to SOPs and train the team on what AI is explicitly not authorized to do.

## 15. Before → Action → After → value protected

**Before:** a corporate reservation contains unclear billing, a possible duplicate and an early-arrival note. The next shift reads the notes differently and Front Office discovers the gaps at arrival.

**Action:** the Reservations team uses the controlled prompts to separate confirmed facts from requests, compare contract terms, flag the possible duplicate, verify the transfer and hand over unresolved decisions with owners.

**After:** Front Office receives a cleaner file, the commercial questions reach authorized owners before arrival and no booking is cancelled or modified based only on AI inference.

**AED saved/protected:** calculate only from verified avoided refunds, rate leakage, compensation, chargebacks, room displacement or labor rework. Do not publish an invented savings figure.

## 16. Reservations manager checklist

Before operationalizing these prompts, confirm that:

- PMS/CRS remains the booking system of record;
- current rate, policy and contract sources are defined;
- AI cannot execute reservation changes;
- payment-card and identity data are excluded from unapproved tools;
- request versus entitlement labels are standardized;
- duplicate cases require manual verification;
- cancellation/no-show actions follow the authority matrix;
- corporate terms come from current controlled documents;
- handovers preserve open ownership and deadlines;
- final actions are recorded back in the approved system.

---

# The 10 copy-ready Reservations AI prompts

## Prompt 031 — Reservation File Quality Check

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

## Prompt 032 — Booking Modification Review

**Risk:** High  
**Human owner:** Reservations Supervisor / Revenue or authorized manager  
**When to use:** When a guest, agent or corporate booker requests a date, occupancy, room-type, name or package change.

### Why this prompt matters

Compare an existing confirmed booking with a requested modification and identify operational, rate, inventory and policy dependencies without executing the change. In reservations, a polished answer is not enough: the team needs traceability back to the booking record, rate or contract that actually governs the case. The prompt therefore exposes uncertainty and preserves the approval boundary before a guest-facing or system action occurs.

### Copy-ready prompt

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as a reservations operations support analyst for a hotel or serviced-apartment property.
Supported role: [Reservations Agent / Supervisor / Manager]
Accountable human owner: Reservations Supervisor / Revenue or authorized manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Compare an existing confirmed booking with a requested modification and identify operational, rate, inventory and policy dependencies without executing the change.
Property: [hotel / serviced apartment, location]
Stay/booking context: [dates, channel, segment, room type, relevant operational context]
Decision deadline: [time/date if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied approved records. Primary sources may include PMS/CRS, original booking confirmation, authorized channel/extranet record, approved rate plan, contract/rate sheet, inventory snapshot, payment-status indicator, controlled SOP/policy and documented communication log.
Required inputs:
- current PMS/CRS booking
- original confirmation
- requested modification
- approved rate/cancellation/modification terms
- current authorized inventory/rate information

If records conflict, show the conflict explicitly. If a critical field is missing, stale or unverified, label it UNVERIFIED and state which system/owner must confirm it. Never infer a rate, entitlement, availability, payment status, room status or contractual term from memory.
Minimize personal data. Do not reproduce passport/ID numbers, payment-card data, credentials or unrelated sensitive notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Produce:
- before-versus-requested comparison
- impact/dependency list
- items requiring repricing or approval
- safe response draft

Separate the output into CONFIRMED FACT, REQUEST/CLAIM, UNVERIFIED/CONFLICT, and RECOMMENDED ACTION where relevant. For each open item show owner, next action, deadline/checkpoint, evidence needed for closure and escalation trigger.
Do not execute or imply that the modification is accepted. Flag repricing, availability, penalty, occupancy and entitlement dependencies.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not create, modify, cancel, reinstate, merge, allocate, charge, refund, waive, upgrade or confirm a reservation. Do not promise availability, price, benefit, room type, early check-in, late checkout, compensation or exception unless an approved source and authorized human decision explicitly support it.
Risk classification: High.
Final operational action requires verification/approval by: Reservations Supervisor / Revenue or authorized manager.
AI output is decision support and a draft—not the PMS/CRS record, contractual confirmation or authorization.
```

### Human verification before action

Confirm the relevant PMS/CRS record is current; resolve any source conflict; verify the applicable policy, rate or contract; check that the proposed action is within the employee's authority; and record the final approved action in the proper operational system.

## Prompt 033 — Cancellation Policy Explanation Draft

**Risk:** High  
**Human owner:** Reservations Supervisor / authorized commercial role  
**When to use:** When explaining cancellation conditions before or after a cancellation request.

### Why this prompt matters

Translate the confirmed cancellation terms into clear guest-facing language without changing the contractual meaning or deciding whether a fee should be waived. In reservations, a polished answer is not enough: the team needs traceability back to the booking record, rate or contract that actually governs the case. The prompt therefore exposes uncertainty and preserves the approval boundary before a guest-facing or system action occurs.

### Copy-ready prompt

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as a reservations operations support analyst for a hotel or serviced-apartment property.
Supported role: [Reservations Agent / Supervisor / Manager]
Accountable human owner: Reservations Supervisor / authorized commercial role

O — OPERATIONAL OBJECTIVE & CONTEXT
Translate the confirmed cancellation terms into clear guest-facing language without changing the contractual meaning or deciding whether a fee should be waived.
Property: [hotel / serviced apartment, location]
Stay/booking context: [dates, channel, segment, room type, relevant operational context]
Decision deadline: [time/date if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied approved records. Primary sources may include PMS/CRS, original booking confirmation, authorized channel/extranet record, approved rate plan, contract/rate sheet, inventory snapshot, payment-status indicator, controlled SOP/policy and documented communication log.
Required inputs:
- confirmed reservation terms
- approved cancellation policy/rate-plan terms
- booking channel record
- relevant timestamps

If records conflict, show the conflict explicitly. If a critical field is missing, stale or unverified, label it UNVERIFIED and state which system/owner must confirm it. Never infer a rate, entitlement, availability, payment status, room status or contractual term from memory.
Minimize personal data. Do not reproduce passport/ID numbers, payment-card data, credentials or unrelated sensitive notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Produce:
- plain-language explanation
- confirmed deadline/condition table
- unknowns requiring verification
- neutral response draft

Separate the output into CONFIRMED FACT, REQUEST/CLAIM, UNVERIFIED/CONFLICT, and RECOMMENDED ACTION where relevant. For each open item show owner, next action, deadline/checkpoint, evidence needed for closure and escalation trigger.
Do not calculate or waive a fee unless the supplied approved rule and authorized calculation inputs make the amount deterministic; otherwise route for review.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not create, modify, cancel, reinstate, merge, allocate, charge, refund, waive, upgrade or confirm a reservation. Do not promise availability, price, benefit, room type, early check-in, late checkout, compensation or exception unless an approved source and authorized human decision explicitly support it.
Risk classification: High.
Final operational action requires verification/approval by: Reservations Supervisor / authorized commercial role.
AI output is decision support and a draft—not the PMS/CRS record, contractual confirmation or authorization.
```

### Human verification before action

Confirm the relevant PMS/CRS record is current; resolve any source conflict; verify the applicable policy, rate or contract; check that the proposed action is within the employee's authority; and record the final approved action in the proper operational system.

## Prompt 034 — No-Show Review

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

## Prompt 035 — Room-Type Allocation Support

**Risk:** High  
**Human owner:** Rooms Division / Reservations / Revenue authorized owner  
**When to use:** During pre-arrival planning, room-type pressure or oversell-risk review.

### Why this prompt matters

Analyze room-type demand and constraints and propose allocation options without assigning a specific unit, changing inventory or promising an upgrade. In reservations, a polished answer is not enough: the team needs traceability back to the booking record, rate or contract that actually governs the case. The prompt therefore exposes uncertainty and preserves the approval boundary before a guest-facing or system action occurs.

### Copy-ready prompt

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as a reservations operations support analyst for a hotel or serviced-apartment property.
Supported role: [Reservations Agent / Supervisor / Manager]
Accountable human owner: Rooms Division / Reservations / Revenue authorized owner

O — OPERATIONAL OBJECTIVE & CONTEXT
Analyze room-type demand and constraints and propose allocation options without assigning a specific unit, changing inventory or promising an upgrade.
Property: [hotel / serviced apartment, location]
Stay/booking context: [dates, channel, segment, room type, relevant operational context]
Decision deadline: [time/date if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied approved records. Primary sources may include PMS/CRS, original booking confirmation, authorized channel/extranet record, approved rate plan, contract/rate sheet, inventory snapshot, payment-status indicator, controlled SOP/policy and documented communication log.
Required inputs:
- PMS/CRS room-type bookings
- approved inventory snapshot
- out-of-order/out-of-service status
- confirmed accessibility/operational requirements
- approved upgrade/room-move rules

If records conflict, show the conflict explicitly. If a critical field is missing, stale or unverified, label it UNVERIFIED and state which system/owner must confirm it. Never infer a rate, entitlement, availability, payment status, room status or contractual term from memory.
Minimize personal data. Do not reproduce passport/ID numbers, payment-card data, credentials or unrelated sensitive notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Produce:
- demand-versus-available view
- constraint list
- allocation options
- escalation triggers

Separate the output into CONFIRMED FACT, REQUEST/CLAIM, UNVERIFIED/CONFLICT, and RECOMMENDED ACTION where relevant. For each open item show owner, next action, deadline/checkpoint, evidence needed for closure and escalation trigger.
Do not assign unit numbers, move inventory, oversell, downgrade, upgrade or displace another booking. Treat output as planning options only.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not create, modify, cancel, reinstate, merge, allocate, charge, refund, waive, upgrade or confirm a reservation. Do not promise availability, price, benefit, room type, early check-in, late checkout, compensation or exception unless an approved source and authorized human decision explicitly support it.
Risk classification: High.
Final operational action requires verification/approval by: Rooms Division / Reservations / Revenue authorized owner.
AI output is decision support and a draft—not the PMS/CRS record, contractual confirmation or authorization.
```

### Human verification before action

Confirm the relevant PMS/CRS record is current; resolve any source conflict; verify the applicable policy, rate or contract; check that the proposed action is within the employee's authority; and record the final approved action in the proper operational system.

## Prompt 036 — Special Request Extraction

**Risk:** Medium  
**Human owner:** Reservations Supervisor / Front Office Supervisor  
**When to use:** When preparing arrivals or cleaning imported reservation notes.

### Why this prompt matters

Extract guest requests from approved reservation text and classify each as confirmed inclusion, preference/request, operational requirement or unverified item. In reservations, a polished answer is not enough: the team needs traceability back to the booking record, rate or contract that actually governs the case. The prompt therefore exposes uncertainty and preserves the approval boundary before a guest-facing or system action occurs.

### Copy-ready prompt

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as a reservations operations support analyst for a hotel or serviced-apartment property.
Supported role: [Reservations Agent / Supervisor / Manager]
Accountable human owner: Reservations Supervisor / Front Office Supervisor

O — OPERATIONAL OBJECTIVE & CONTEXT
Extract guest requests from approved reservation text and classify each as confirmed inclusion, preference/request, operational requirement or unverified item.
Property: [hotel / serviced apartment, location]
Stay/booking context: [dates, channel, segment, room type, relevant operational context]
Decision deadline: [time/date if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied approved records. Primary sources may include PMS/CRS, original booking confirmation, authorized channel/extranet record, approved rate plan, contract/rate sheet, inventory snapshot, payment-status indicator, controlled SOP/policy and documented communication log.
Required inputs:
- approved reservation notes
- booking confirmation
- package inclusions
- approved guest-request categories
- relevant operational policy

If records conflict, show the conflict explicitly. If a critical field is missing, stale or unverified, label it UNVERIFIED and state which system/owner must confirm it. Never infer a rate, entitlement, availability, payment status, room status or contractual term from memory.
Minimize personal data. Do not reproduce passport/ID numbers, payment-card data, credentials or unrelated sensitive notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Produce:
- structured request register
- entitlement versus preference labels
- department routing
- verification needs

Separate the output into CONFIRMED FACT, REQUEST/CLAIM, UNVERIFIED/CONFLICT, and RECOMMENDED ACTION where relevant. For each open item show owner, next action, deadline/checkpoint, evidence needed for closure and escalation trigger.
Never convert a preference such as high floor, adjacency or early arrival into a guaranteed entitlement unless the approved record says it is guaranteed.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not create, modify, cancel, reinstate, merge, allocate, charge, refund, waive, upgrade or confirm a reservation. Do not promise availability, price, benefit, room type, early check-in, late checkout, compensation or exception unless an approved source and authorized human decision explicitly support it.
Risk classification: Medium.
Final operational action requires verification/approval by: Reservations Supervisor / Front Office Supervisor.
AI output is decision support and a draft—not the PMS/CRS record, contractual confirmation or authorization.
```

### Human verification before action

Confirm the relevant PMS/CRS record is current; resolve any source conflict; verify the applicable policy, rate or contract; check that the proposed action is within the employee's authority; and record the final approved action in the proper operational system.

## Prompt 037 — Duplicate Booking Detector

**Risk:** High  
**Human owner:** Reservations Supervisor  
**When to use:** When similar reservations, names, dates or contact details suggest possible duplication.

### Why this prompt matters

Identify probable duplicate reservations using supplied booking attributes and produce a review queue without cancelling, merging or altering any booking. In reservations, a polished answer is not enough: the team needs traceability back to the booking record, rate or contract that actually governs the case. The prompt therefore exposes uncertainty and preserves the approval boundary before a guest-facing or system action occurs.

### Copy-ready prompt

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as a reservations operations support analyst for a hotel or serviced-apartment property.
Supported role: [Reservations Agent / Supervisor / Manager]
Accountable human owner: Reservations Supervisor

O — OPERATIONAL OBJECTIVE & CONTEXT
Identify probable duplicate reservations using supplied booking attributes and produce a review queue without cancelling, merging or altering any booking.
Property: [hotel / serviced apartment, location]
Stay/booking context: [dates, channel, segment, room type, relevant operational context]
Decision deadline: [time/date if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied approved records. Primary sources may include PMS/CRS, original booking confirmation, authorized channel/extranet record, approved rate plan, contract/rate sheet, inventory snapshot, payment-status indicator, controlled SOP/policy and documented communication log.
Required inputs:
- reservation IDs
- stay dates
- room types
- guest/booker identifiers minimized where possible
- channel/source
- booking timestamps

If records conflict, show the conflict explicitly. If a critical field is missing, stale or unverified, label it UNVERIFIED and state which system/owner must confirm it. Never infer a rate, entitlement, availability, payment status, room status or contractual term from memory.
Minimize personal data. Do not reproduce passport/ID numbers, payment-card data, credentials or unrelated sensitive notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Produce:
- possible-duplicate clusters
- matching evidence
- confidence rationale
- manual review actions

Separate the output into CONFIRMED FACT, REQUEST/CLAIM, UNVERIFIED/CONFLICT, and RECOMMENDED ACTION where relevant. For each open item show owner, next action, deadline/checkpoint, evidence needed for closure and escalation trigger.
Similarity is not proof. Never cancel, merge or contact the guest as a duplicate without human review of the underlying reservations.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not create, modify, cancel, reinstate, merge, allocate, charge, refund, waive, upgrade or confirm a reservation. Do not promise availability, price, benefit, room type, early check-in, late checkout, compensation or exception unless an approved source and authorized human decision explicitly support it.
Risk classification: High.
Final operational action requires verification/approval by: Reservations Supervisor.
AI output is decision support and a draft—not the PMS/CRS record, contractual confirmation or authorization.
```

### Human verification before action

Confirm the relevant PMS/CRS record is current; resolve any source conflict; verify the applicable policy, rate or contract; check that the proposed action is within the employee's authority; and record the final approved action in the proper operational system.

## Prompt 038 — Reservation Handover Summary

**Risk:** Medium  
**Human owner:** Outgoing and incoming Reservations Supervisors  
**When to use:** At shift change or transfer of responsibility between reservations teams.

### Why this prompt matters

Convert open reservation work into a concise handover showing facts, pending actions, owners, deadlines and escalation conditions. In reservations, a polished answer is not enough: the team needs traceability back to the booking record, rate or contract that actually governs the case. The prompt therefore exposes uncertainty and preserves the approval boundary before a guest-facing or system action occurs.

### Copy-ready prompt

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as a reservations operations support analyst for a hotel or serviced-apartment property.
Supported role: [Reservations Agent / Supervisor / Manager]
Accountable human owner: Outgoing and incoming Reservations Supervisors

O — OPERATIONAL OBJECTIVE & CONTEXT
Convert open reservation work into a concise handover showing facts, pending actions, owners, deadlines and escalation conditions.
Property: [hotel / serviced apartment, location]
Stay/booking context: [dates, channel, segment, room type, relevant operational context]
Decision deadline: [time/date if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied approved records. Primary sources may include PMS/CRS, original booking confirmation, authorized channel/extranet record, approved rate plan, contract/rate sheet, inventory snapshot, payment-status indicator, controlled SOP/policy and documented communication log.
Required inputs:
- open reservation queue
- modification/cancellation cases
- unresolved channel messages
- corporate/group follow-ups
- approved action log

If records conflict, show the conflict explicitly. If a critical field is missing, stale or unverified, label it UNVERIFIED and state which system/owner must confirm it. Never infer a rate, entitlement, availability, payment status, room status or contractual term from memory.
Minimize personal data. Do not reproduce passport/ID numbers, payment-card data, credentials or unrelated sensitive notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Produce:
- priority handover table
- pending decisions
- owner/deadline list
- verification reminders

Separate the output into CONFIRMED FACT, REQUEST/CLAIM, UNVERIFIED/CONFLICT, and RECOMMENDED ACTION where relevant. For each open item show owner, next action, deadline/checkpoint, evidence needed for closure and escalation trigger.
Do not drop unresolved items because they appear low priority. Preserve ownership, next action and evidence required for closure.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not create, modify, cancel, reinstate, merge, allocate, charge, refund, waive, upgrade or confirm a reservation. Do not promise availability, price, benefit, room type, early check-in, late checkout, compensation or exception unless an approved source and authorized human decision explicitly support it.
Risk classification: Medium.
Final operational action requires verification/approval by: Outgoing and incoming Reservations Supervisors.
AI output is decision support and a draft—not the PMS/CRS record, contractual confirmation or authorization.
```

### Human verification before action

Confirm the relevant PMS/CRS record is current; resolve any source conflict; verify the applicable policy, rate or contract; check that the proposed action is within the employee's authority; and record the final approved action in the proper operational system.

## Prompt 039 — Corporate Booking Validation

**Risk:** High  
**Human owner:** Reservations Supervisor / Sales / Finance authorized owner  
**When to use:** For corporate, long-stay or contracted-account reservations before confirmation or arrival.

### Why this prompt matters

Validate a corporate reservation against supplied approved account terms without inventing negotiated rates, inclusions, credit status or billing authority. In reservations, a polished answer is not enough: the team needs traceability back to the booking record, rate or contract that actually governs the case. The prompt therefore exposes uncertainty and preserves the approval boundary before a guest-facing or system action occurs.

### Copy-ready prompt

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as a reservations operations support analyst for a hotel or serviced-apartment property.
Supported role: [Reservations Agent / Supervisor / Manager]
Accountable human owner: Reservations Supervisor / Sales / Finance authorized owner

O — OPERATIONAL OBJECTIVE & CONTEXT
Validate a corporate reservation against supplied approved account terms without inventing negotiated rates, inclusions, credit status or billing authority.
Property: [hotel / serviced apartment, location]
Stay/booking context: [dates, channel, segment, room type, relevant operational context]
Decision deadline: [time/date if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied approved records. Primary sources may include PMS/CRS, original booking confirmation, authorized channel/extranet record, approved rate plan, contract/rate sheet, inventory snapshot, payment-status indicator, controlled SOP/policy and documented communication log.
Required inputs:
- PMS/CRS booking
- approved corporate contract/rate sheet
- authorized billing/credit indicator
- approved inclusions
- stay details

If records conflict, show the conflict explicitly. If a critical field is missing, stale or unverified, label it UNVERIFIED and state which system/owner must confirm it. Never infer a rate, entitlement, availability, payment status, room status or contractual term from memory.
Minimize personal data. Do not reproduce passport/ID numbers, payment-card data, credentials or unrelated sensitive notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Produce:
- contract-to-booking comparison
- variance list
- billing/inclusion checkpoints
- approval queue

Separate the output into CONFIRMED FACT, REQUEST/CLAIM, UNVERIFIED/CONFLICT, and RECOMMENDED ACTION where relevant. For each open item show owner, next action, deadline/checkpoint, evidence needed for closure and escalation trigger.
Do not infer negotiated terms from prior stays or guest statements. Use only the current approved account/contract evidence supplied.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not create, modify, cancel, reinstate, merge, allocate, charge, refund, waive, upgrade or confirm a reservation. Do not promise availability, price, benefit, room type, early check-in, late checkout, compensation or exception unless an approved source and authorized human decision explicitly support it.
Risk classification: High.
Final operational action requires verification/approval by: Reservations Supervisor / Sales / Finance authorized owner.
AI output is decision support and a draft—not the PMS/CRS record, contractual confirmation or authorization.
```

### Human verification before action

Confirm the relevant PMS/CRS record is current; resolve any source conflict; verify the applicable policy, rate or contract; check that the proposed action is within the employee's authority; and record the final approved action in the proper operational system.

## Prompt 040 — Reservation Exception Escalation

**Risk:** High  
**Human owner:** Reservations Manager / Duty Manager / authorized commercial owner  
**When to use:** When a reservation cannot be resolved within normal SOP or frontline authority.

### Why this prompt matters

Turn a reservation exception into a decision-ready escalation brief with evidence, guest impact, options and authority boundary. In reservations, a polished answer is not enough: the team needs traceability back to the booking record, rate or contract that actually governs the case. The prompt therefore exposes uncertainty and preserves the approval boundary before a guest-facing or system action occurs.

### Copy-ready prompt

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as a reservations operations support analyst for a hotel or serviced-apartment property.
Supported role: [Reservations Agent / Supervisor / Manager]
Accountable human owner: Reservations Manager / Duty Manager / authorized commercial owner

O — OPERATIONAL OBJECTIVE & CONTEXT
Turn a reservation exception into a decision-ready escalation brief with evidence, guest impact, options and authority boundary.
Property: [hotel / serviced apartment, location]
Stay/booking context: [dates, channel, segment, room type, relevant operational context]
Decision deadline: [time/date if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied approved records. Primary sources may include PMS/CRS, original booking confirmation, authorized channel/extranet record, approved rate plan, contract/rate sheet, inventory snapshot, payment-status indicator, controlled SOP/policy and documented communication log.
Required inputs:
- reservation record
- exception description
- approved policy/SOP
- contact/action log
- inventory/rate/contract evidence relevant to case

If records conflict, show the conflict explicitly. If a critical field is missing, stale or unverified, label it UNVERIFIED and state which system/owner must confirm it. Never infer a rate, entitlement, availability, payment status, room status or contractual term from memory.
Minimize personal data. Do not reproduce passport/ID numbers, payment-card data, credentials or unrelated sensitive notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Produce:
- escalation brief
- facts versus unknowns
- guest/operational impact
- options with approval owner

Separate the output into CONFIRMED FACT, REQUEST/CLAIM, UNVERIFIED/CONFLICT, and RECOMMENDED ACTION where relevant. For each open item show owner, next action, deadline/checkpoint, evidence needed for closure and escalation trigger.
Do not choose a commercial remedy outside the stated authority matrix. Present options and route the decision to the authorized role.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not create, modify, cancel, reinstate, merge, allocate, charge, refund, waive, upgrade or confirm a reservation. Do not promise availability, price, benefit, room type, early check-in, late checkout, compensation or exception unless an approved source and authorized human decision explicitly support it.
Risk classification: High.
Final operational action requires verification/approval by: Reservations Manager / Duty Manager / authorized commercial owner.
AI output is decision support and a draft—not the PMS/CRS record, contractual confirmation or authorization.
```

### Human verification before action

Confirm the relevant PMS/CRS record is current; resolve any source conflict; verify the applicable policy, rate or contract; check that the proposed action is within the employee's authority; and record the final approved action in the proper operational system.

---

## Final human-verification checklist

Before using any AI-generated reservation output operationally, verify:

1. Is the reservation identity/reference correct?
2. Is the PMS/CRS record current?
3. Are the rate, room type, stay dates and occupancy confirmed?
4. Are requests clearly separated from guaranteed inclusions?
5. Are cancellation/modification/no-show terms taken from the correct approved source?
6. Are corporate terms current and applicable to this booking?
7. Are payment or billing statements limited to approved status information?
8. Are duplicate indicators manually verified?
9. Does the employee have authority for the proposed action?
10. Has the final approved action been recorded in the proper system?

## Key takeaway

Reservations AI is most valuable before a problem reaches the guest. Its job is to make the booking **clearer, more complete, more traceable and easier to govern**. It should not become a shadow reservation system.

> **Use AI to find the question that still needs an answer—not to manufacture the answer that the system or authorized person has not yet confirmed.**

## Series navigation

**Previous:** Article 03 — Front Office AI Toolkit  
**Series:** Hotel & Serviced Apartment AI Operations Playbook  
**Next:** Article 05 — Hotel Apartment & Extended-Stay AI Toolkit