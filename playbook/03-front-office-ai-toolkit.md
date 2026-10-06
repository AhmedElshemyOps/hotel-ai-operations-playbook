# Article 03 — Front Office AI Toolkit

## 10 Professional AI Prompts for Arrival Readiness, Check-In, Guest Requests, Exceptions and Front-Desk Control

**Track C · Hotel & Serviced Apartment AI Operations Playbook · Front Office chapter**

The front desk is where hotel data becomes a guest promise. A reservation becomes an arrival. A room-status code becomes a key handover. A maintenance delay becomes a conversation. A policy becomes an explanation. A guest request becomes a cross-department action that someone must own and close.

That makes Front Office one of the most useful—and one of the most sensitive—places to apply generative AI.

AI can help a front-office team prepare arrival briefs, organize peak check-in periods, draft multilingual messages, structure handovers, triage requests and analyze recurring exceptions. But the same tool can create operational risk if it invents a room-readiness time, exposes personal information, promises an upgrade that was never approved, changes the meaning of a cancellation condition, or treats an AI-generated summary as if it were the PMS.

The operating principle for this chapter is therefore simple:

> **AI can prepare the conversation and organize the evidence. The hotel's approved systems and accountable people still control the promise.**

The ten prompts in this chapter follow the front-office journey:

> **Prepare → Welcome → Absorb the peak → Manage delay → Triage requests → Prepare departure → Handover → Protect priority arrivals → Learn from exceptions → Communicate across languages**

---

## 1. Front Office is a control point, not only a reception desk

In a hotel or serviced-apartment operation, Front Office sits at the intersection of Reservations, Housekeeping, Engineering, Guest Relations, Security, Revenue and Finance. The team may not own every process, but it frequently owns the guest-facing consequence when another process is late or incomplete.

Consider a room-not-ready case. The visible event happens at reception, but the cause may sit elsewhere: a late departure, housekeeping capacity, an engineering defect, a room move, a status mismatch, an inspection failure or a special setup that has not been completed. If AI is asked only to “write a nice apology,” it may improve the wording while leaving the operating failure untouched.

A professional AI workflow should therefore work in two layers:

1. **Guest communication layer** — clear, empathetic and policy-aligned wording.
2. **Operational control layer** — confirmed status, owner, dependency, next checkpoint and escalation path.

This distinction is central to every prompt in this chapter.

---

## 2. Apply the HOTEL framework at the desk

The HOTEL framework remains the common architecture:

- **H — Hospitality role & human owner**
- **O — Operational objective & context**
- **T — Trusted inputs & sources of truth**
- **E — Expected output, exceptions & evidence**
- **L — Limits, privacy & leadership approval**

For Front Office, the most important control is that the **PMS and approved operational records remain authoritative**. AI should not be asked to decide whether a room is ready from a chat message, infer whether payment has cleared, determine whether an upgrade is complimentary, or guess a guest's entitlement.

A useful front-office prompt explicitly names the relevant source:

| Front-office question | Primary source of truth |
|---|---|
| Is the reservation confirmed? | PMS / approved reservation system |
| Is the apartment ready? | PMS room status plus approved housekeeping release process |
| Is an engineering defect closed? | CMMS / approved maintenance close-out |
| What rate or package was booked? | PMS / reservation record |
| What benefit is included? | Approved package, loyalty or contract terms |
| Has payment been authorized? | Approved payment/PMS workflow—not AI |
| Can a fee be waived? | Approved policy and authorized human role |
| What did the guest request? | Approved guest-request/CRM record |

If two sources disagree, AI should expose the conflict. It should not silently select the version that sounds most plausible.

---

## 3. The Front Office AI Control Loop

The ten prompts create a practical operating rhythm.

| Stage | Management question | Prompt |
|---|---|---|
| Pre-arrival | Are today's arrivals operationally ready? | 021 Arrival Readiness Brief |
| Check-in | How should confirmed information be communicated? | 022 Check-In Communication Draft |
| Peak | Where will arrival pressure occur and how should the team prepare? | 023 Queue and Peak Arrival Planner |
| Delay | What can we say and do when a room is not ready? | 024 Room-Not-Ready Response |
| In-stay | Which guest request goes where, by when and with what escalation? | 025 Guest Request Triage |
| Departure | Which departures need action before checkout? | 026 Checkout Readiness Planner |
| Shift change | What must pass to the next desk team? | 027 Front Desk Handover |
| Priority arrival | What must be verified for an approved VIP/priority arrival? | 028 VIP Arrival Checklist Builder |
| Improvement | What patterns are recurring in the exception log? | 029 Front Office Exception Log Analyzer |
| Language | How do we translate a confirmed message without changing its meaning? | 030 Multilingual Guest Message Draft |

The loop is deliberately broader than messaging. Front Office AI should improve **readiness, coordination and evidence**, not merely tone.

---

## 4. Fictional UAE case: seven arrivals and one difficult morning

Continue with the fictional 60-unit UAE serviced-apartment property used throughout the playbook.

At 09:00, seven arrivals are expected:

- two standard leisure arrivals after 15:00;
- one family requesting adjacent apartments;
- one corporate long-stay guest requesting access at 11:00;
- one approved priority guest with a 13:00 arrival;
- two late-evening arrivals with airport transfers.

At the same time:

- Apartment 1208 is clean but awaiting Engineering close-out;
- Apartment 1410 has not yet passed supervisor inspection;
- the corporate arrival's apartment is expected to be ready early, but no approved release exists yet;
- the family adjacency request is recorded but not guaranteed;
- one airport transfer has a confirmed driver and one has only a booking reference;
- the previous shift left an unresolved request for a baby cot.

A weak AI prompt might produce: “All arrivals are on track except one room awaiting maintenance.” That sounds efficient but hides uncertainty.

A controlled Arrival Readiness Brief should instead distinguish:

**READY** — reservation and room readiness confirmed through approved sources.  
**DEPENDENCY** — arrival can proceed only after another department closes a task.  
**REQUEST / NOT GUARANTEED** — preference is recorded but not an entitlement.  
**UNVERIFIED** — a service is expected but lacks current confirmation.  
**ESCALATE** — deadline or guest impact requires management attention.

This classification prevents optimism from becoming a promise.

---

## 5. Arrival readiness is more than a list of names

A professional arrival brief should help the shift leader answer:

- Which arrivals are due in the next two to four hours?
- Which units are fully released?
- Which units depend on housekeeping, engineering or inspection?
- Which requests are guaranteed, approved, requested or merely noted?
- Which arrivals have transport, accessibility, family or long-stay dependencies?
- What is the next verification time?
- Who owns each unresolved item?

Personal data should be minimized. The operational brief usually does not need passport numbers, full payment details or unnecessary identity documents. Use reservation references or the minimum guest identifier required by the approved workflow.

For the 11:00 corporate arrival, for example, the correct output is not “Early check-in confirmed” unless the authorized system and role confirm it. A safer output is:

> **Early-access request: pending.** Apartment 1208 is clean; Engineering close-out remains open. Front Office to re-check approved room status at 10:15. Do not promise access until release is confirmed.

That one sentence protects the guest promise, the team and the audit trail.

---

## 6. Peak arrival planning: predict pressure without pretending certainty

AI can be useful when many arrivals cluster around the same time. Provide an arrival manifest stripped to the minimum necessary fields, historical processing assumptions approved by the property, desk staffing, known group/VIP activity and room-readiness status.

The output can identify likely pressure windows and recommend operational preparation such as:

- opening an additional desk position;
- pre-checking registration completeness where policy allows;
- assigning one colleague to queue hosting;
- separating key collection from complex reservation cases;
- pre-verifying room readiness for arrivals inside the peak window;
- ensuring luggage support is available;
- identifying arrivals with unresolved payment, documentation or room dependencies for human review.

But AI should not fabricate a precise waiting time if the hotel has no validated queue model. “Potential 16:00–17:00 pressure window” is more responsible than “Guests will wait 11 minutes.”

---

## 7. Room not ready: never let AI invent the next promise

Room-not-ready cases are a classic example of why hospitality prompting needs limits.

The guest may ask: “When will it be ready?” If Housekeeping has not given an approved release time, the model should not infer one from the average cleaning duration. It may draft language that acknowledges the delay and commits to a **next update time**, which is different from promising a room-ready time.

For example:

> “Your apartment is still completing its final readiness process. I do not want to give you an inaccurate completion time. I will personally update you again by 14:20, or earlier if the apartment is released.”

That wording is operationally stronger than an invented estimate.

The AI can also prepare an internal control block:

- current confirmed status;
- blocking dependency;
- owner;
- next checkpoint;
- approved waiting option;
- compensation authority if applicable;
- escalation threshold.

AI drafts. The authorized employee decides what can actually be offered.

---

## 8. Guest request triage: turn messages into owned work

Front desks receive requests through phone, WhatsApp, chat, email, in-person conversation and internal systems. Requests can disappear when they remain as messages instead of becoming controlled work.

Prompt 025 converts an approved request list into a triage view using dimensions such as:

- safety/health urgency;
- guest currently blocked;
- service-level deadline;
- department owner;
- access dependency;
- cost or approval requirement;
- repeat request;
- escalation threshold.

A request for an extra towel is not treated like a water leak. A request to extend checkout is not treated as confirmed until availability, policy and authority are checked. A maintenance request requiring apartment access should show the access condition rather than telling Engineering simply to “go to the room.”

The goal is a closed loop:

> **Request received → classified → assigned → acknowledged → completed → verified → closed**

AI can structure that loop, but the service system should record the official status.

---

## 9. Checkout readiness: prevent avoidable friction at departure

Checkout can expose unresolved balances, transport timing, luggage requests, late-checkout expectations, open maintenance cases, missing access items and invoice requirements.

Prompt 026 prepares a departure control list from approved data. It should highlight—not decide—items requiring authorized review.

For an extended-stay apartment, the checklist may include:

- confirmed departure time;
- approved late checkout, if any;
- invoice/billing instruction status;
- transport confirmation;
- luggage request;
- open guest case requiring closure;
- apartment access/key/card process;
- housekeeping/inspection trigger after departure;
- any approved property-specific departure requirement.

It must not accuse a guest of damage, determine charges, or expose financial details beyond the authorized workflow.

---

## 10. Front-desk handover: preserve exceptions, not noise

A good handover does not repeat everything that happened during the shift. It transfers what the next team needs to control.

Prompt 027 should organize handover items into:

**Guest-impacting open items**  
**Arrivals/departures requiring attention**  
**Room-status dependencies**  
**Engineering/housekeeping follow-ups**  
**Approved recovery actions still open**  
**Transport or supplier dependencies**  
**Deadlines and next checkpoints**  
**Items requiring manager authority**

Every open item needs an owner and next action. “Guest complained about AC” is history. “Apartment 1407 repeat AC complaint; Engineering WO-482 open; technician due 19:15; Front Office to update guest by 19:30; Duty Manager to review room-move option if unresolved” is operational control.

---

## 11. Priority and VIP arrivals: precision beats decoration

VIP preparation often creates long checklists that mix confirmed requirements, preferences and assumptions. AI can help build a concise readiness checklist, but the model should not infer preferences from nationality, status, past stereotypes or incomplete notes.

Use only approved profile information and current instructions. Separate:

- **confirmed entitlement**;
- **approved setup**;
- **recorded preference**;
- **pending request**;
- **internal dependency**.

The checklist can cover room inspection, approved amenities, transport, welcome ownership, billing instructions, privacy considerations and escalation contacts. Sensitive profile details should be limited to people who need them operationally.

---

## 12. Learn from the exception log

Prompt 029 turns Front Office from a reaction point into a learning system.

Feed the model a sanitized exception log containing categories such as room not ready, key/access issue, billing clarification, transport delay, room-status mismatch, repeated guest request, maintenance complaint or communication failure. Ask it to identify frequency, recurrence, time patterns, affected journey stages and departments requiring investigation.

The model should separate:

- **observed pattern** — directly supported by records;
- **possible cause** — hypothesis requiring evidence;
- **recommended investigation** — what to check next.

For example, if room-not-ready cases cluster on Fridays, AI should not conclude “Housekeeping is understaffed.” It can say the pattern is concentrated on Fridays and recommend comparing departure volume, staffing, late checkouts, engineering holds and inspection cycle times.

That is evidence-led improvement rather than automated blame.

---

## 13. Multilingual communication: translate meaning, not authority

Hotels frequently need messages in Arabic, English, French, Russian, Dutch and many other languages. Generative AI can be extremely useful here, but translation can accidentally change operational meaning.

Prompt 030 therefore works from a **confirmed source message**. The instruction should preserve:

- dates and times;
- prices and currencies;
- policy meaning;
- what is confirmed versus requested;
- escalation contact;
- prohibited promises.

The model should return the translation plus a short “meaning-preservation check” highlighting any phrase that may be ambiguous.

For high-impact messages—payment, cancellation, safety, legal terms, medical situations or significant compensation—the hotel should apply stronger human review or approved translation procedures.

---

## 14. Privacy and data minimization at Front Office

Front Office handles some of the property's most sensitive information. The fact that data exists in a PMS does not mean it should be copied into an AI prompt.

Avoid unnecessary inclusion of:

- passport or Emirates ID images/numbers;
- full payment-card data;
- credentials or access codes;
- medical details unless an approved workflow genuinely requires them;
- personal contact data unrelated to the task;
- sensitive VIP notes;
- other guests' information;
- confidential corporate rates or contracts when not required.

Use reservation references, masked identifiers and aggregated data wherever possible. Follow the hotel's approved AI/data policy and applicable privacy requirements. The UAE's federal personal-data protection framework reinforces the need for lawful, controlled handling of personal data; hotel-specific implementation should be reviewed by the organization's responsible legal/privacy roles.

---

## 15. Front Office AI Authority Matrix

| Task | AI role | Human authority |
|---|---|---|
| Draft welcome/check-in message | Draft | Front Office verifies and sends |
| Summarize arrival readiness | Support | Shift leader verifies against systems |
| Mark room ready | **No authority** | Approved operational workflow |
| Promise upgrade | **No authority** | Authorized role + inventory/policy |
| Waive fee | **No authority** | Authorized employee/manager |
| Translate confirmed message | Draft/translate | Employee verifies meaning |
| Prioritize guest requests | Recommend | Front Office/manager decides |
| Change reservation | **No authority** | Authorized reservation/PMS action |
| Determine compensation | Recommend only if policy permits | Authorized manager |
| Analyze exception trends | Analyze | Manager validates and investigates |

This matrix should be adapted to the property's own delegation-of-authority policy.

---

## 16. Implementation: introduce Front Office AI in 30 days

### Week 1 — Control the inputs
Map the approved systems and data fields for arrivals, room status, guest requests, handovers and exceptions. Define what may and may not enter the AI workflow.

### Week 2 — Pilot low-risk support
Start with arrival briefs, handover formatting and translation of already-approved messages. Require human review before use.

### Week 3 — Add operational triage
Pilot guest-request triage and peak-arrival planning. Compare AI output with actual shift-leader decisions. Record misses and false priorities.

### Week 4 — Measure and standardize
Review whether the workflow reduced preparation time, missed handover items or unresolved requests without increasing errors or privacy exposure. Update prompts before wider adoption.

Useful implementation measures include:

- handover items without owner;
- missed arrival dependencies;
- guest requests overdue;
- room-status conflicts detected;
- AI drafts corrected before sending;
- unauthorized promises prevented;
- time spent preparing arrival brief;
- recurring exception categories.

Do not measure success only by “minutes saved.” A faster wrong message is not an improvement.

---

## 17. Ten professional prompts

The following prompts are designed as controlled templates. Replace bracketed fields only with information approved for the task.

### Prompt 021 — Arrival Readiness Brief

**Risk:** Medium  
**When to use:** Before each arrival wave or shift briefing.  
**Human owner/approver:** Front Office Supervisor / Duty Manager

**Required inputs**
- approved arrival list
- current PMS reservation/room status
- approved housekeeping release status
- open engineering dependencies
- confirmed transport/special requests

**Expected output**
- arrival readiness table
- red/amber watch list
- unverified items
- owner and next-check time

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as a front-office operations support analyst for a hotel or serviced-apartment property.
Supported role: [Front Office Agent / Supervisor / Duty Manager]
Accountable owner: [Front Office Supervisor / Duty Manager]

O — OPERATIONAL OBJECTIVE & CONTEXT
Prepare an arrival-readiness brief. Classify each arrival as READY, DEPENDENCY, REQUEST/NOT GUARANTEED, UNVERIFIED or ESCALATE.
Property: [type and location]
Operating date/time: [confirmed period]
Guest-journey stage: [pre-arrival / arrival / in-stay / departure]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied approved records. Relevant sources may include PMS/reservation record, approved housekeeping room status, CMMS close-out, guest-request system, approved policy/SOP, transport confirmation and authorized management instruction.

If a critical field is missing, stale or contradictory, do not guess. Mark it UNVERIFIED, name the source/owner needed, and state the next verification action.
Minimize personal data. Do not request or reproduce passport/ID numbers, full payment-card data, credentials, unnecessary contact data or unrelated sensitive notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return the requested operational output with four labels where relevant:
CONFIRMED FACT
REQUEST / PREFERENCE
UNRESOLVED / DEPENDENCY
RECOMMENDED ACTION

For every unresolved operational item show owner, next action, deadline/checkpoint and escalation condition.
arrival readiness table
red/amber watch list
unverified items
owner and next-check time

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Never state that early check-in, adjacency, upgrade, transport or room readiness is confirmed unless the approved source confirms it.
Do not alter PMS status, reservation, payment, room assignment, guest entitlement or official record.
Do not invent times, prices, availability, benefits, compensation or policy.
Output is a draft until verified by Front Office Supervisor / Duty Manager.
```

### Prompt 022 — Check-In Communication Draft

**Risk:** Low–Medium  
**When to use:** When confirmed check-in information must be communicated clearly to a guest.  
**Human owner/approver:** Front Office Agent / Supervisor

**Required inputs**
- confirmed reservation details needed for message
- approved check-in time/location/process
- confirmed inclusions
- approved property contact/instructions

**Expected output**
- guest-ready message
- facts used
- items deliberately omitted
- verification note

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as a front-office operations support analyst for a hotel or serviced-apartment property.
Supported role: [Front Office Agent / Supervisor / Duty Manager]
Accountable owner: [Front Office Agent / Supervisor]

O — OPERATIONAL OBJECTIVE & CONTEXT
Draft a concise, warm check-in communication using only confirmed information. Match the requested language and tone.
Property: [type and location]
Operating date/time: [confirmed period]
Guest-journey stage: [pre-arrival / arrival / in-stay / departure]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied approved records. Relevant sources may include PMS/reservation record, approved housekeeping room status, CMMS close-out, guest-request system, approved policy/SOP, transport confirmation and authorized management instruction.

If a critical field is missing, stale or contradictory, do not guess. Mark it UNVERIFIED, name the source/owner needed, and state the next verification action.
Minimize personal data. Do not request or reproduce passport/ID numbers, full payment-card data, credentials, unnecessary contact data or unrelated sensitive notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return the requested operational output with four labels where relevant:
CONFIRMED FACT
REQUEST / PREFERENCE
UNRESOLVED / DEPENDENCY
RECOMMENDED ACTION

For every unresolved operational item show owner, next action, deadline/checkpoint and escalation condition.
guest-ready message
facts used
items deliberately omitted
verification note

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not add unconfirmed benefits, room number, upgrade, early access, fees or payment instructions.
Do not alter PMS status, reservation, payment, room assignment, guest entitlement or official record.
Do not invent times, prices, availability, benefits, compensation or policy.
Output is a draft until verified by Front Office Agent / Supervisor.
```

### Prompt 023 — Queue and Peak Arrival Planner

**Risk:** Medium  
**When to use:** Before a forecast arrival peak, group movement or high-occupancy check-in window.  
**Human owner/approver:** Front Office Supervisor / Duty Manager

**Required inputs**
- arrival counts by time window
- desk staffing
- confirmed room readiness
- known groups/priority arrivals
- approved average processing assumptions if available

**Expected output**
- pressure-window table
- staffing/flow recommendations
- arrival dependencies
- contingency triggers

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as a front-office operations support analyst for a hotel or serviced-apartment property.
Supported role: [Front Office Agent / Supervisor / Duty Manager]
Accountable owner: [Front Office Supervisor / Duty Manager]

O — OPERATIONAL OBJECTIVE & CONTEXT
Analyze the arrival pattern and prepare a peak-arrival operating plan. Use ranges when precise waiting-time evidence is unavailable.
Property: [type and location]
Operating date/time: [confirmed period]
Guest-journey stage: [pre-arrival / arrival / in-stay / departure]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied approved records. Relevant sources may include PMS/reservation record, approved housekeeping room status, CMMS close-out, guest-request system, approved policy/SOP, transport confirmation and authorized management instruction.

If a critical field is missing, stale or contradictory, do not guess. Mark it UNVERIFIED, name the source/owner needed, and state the next verification action.
Minimize personal data. Do not request or reproduce passport/ID numbers, full payment-card data, credentials, unnecessary contact data or unrelated sensitive notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return the requested operational output with four labels where relevant:
CONFIRMED FACT
REQUEST / PREFERENCE
UNRESOLVED / DEPENDENCY
RECOMMENDED ACTION

For every unresolved operational item show owner, next action, deadline/checkpoint and escalation condition.
pressure-window table
staffing/flow recommendations
arrival dependencies
contingency triggers

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not fabricate queue times or direct staff changes outside the manager’s authority.
Do not alter PMS status, reservation, payment, room assignment, guest entitlement or official record.
Do not invent times, prices, availability, benefits, compensation or policy.
Output is a draft until verified by Front Office Supervisor / Duty Manager.
```

### Prompt 024 — Room-Not-Ready Response

**Risk:** Medium–High  
**When to use:** When a guest arrives but the assigned room/apartment is not yet released.  
**Human owner/approver:** Duty Manager / authorized Front Office leader

**Required inputs**
- confirmed current room status
- blocking dependency
- approved next update time
- approved waiting alternatives
- compensation/upgrade authority policy

**Expected output**
- guest-facing draft
- internal control block
- next update commitment
- escalation condition

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as a front-office operations support analyst for a hotel or serviced-apartment property.
Supported role: [Front Office Agent / Supervisor / Duty Manager]
Accountable owner: [Duty Manager / authorized Front Office leader]

O — OPERATIONAL OBJECTIVE & CONTEXT
Prepare a guest response and internal control note for a room-not-ready case. If readiness time is unconfirmed, promise a next update—not an invented completion time.
Property: [type and location]
Operating date/time: [confirmed period]
Guest-journey stage: [pre-arrival / arrival / in-stay / departure]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied approved records. Relevant sources may include PMS/reservation record, approved housekeeping room status, CMMS close-out, guest-request system, approved policy/SOP, transport confirmation and authorized management instruction.

If a critical field is missing, stale or contradictory, do not guess. Mark it UNVERIFIED, name the source/owner needed, and state the next verification action.
Minimize personal data. Do not request or reproduce passport/ID numbers, full payment-card data, credentials, unnecessary contact data or unrelated sensitive notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return the requested operational output with four labels where relevant:
CONFIRMED FACT
REQUEST / PREFERENCE
UNRESOLVED / DEPENDENCY
RECOMMENDED ACTION

For every unresolved operational item show owner, next action, deadline/checkpoint and escalation condition.
guest-facing draft
internal control block
next update commitment
escalation condition

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not promise a room-ready time, upgrade, compensation, refund, transport or alternative room unless explicitly approved.
Do not alter PMS status, reservation, payment, room assignment, guest entitlement or official record.
Do not invent times, prices, availability, benefits, compensation or policy.
Output is a draft until verified by Duty Manager / authorized Front Office leader.
```

### Prompt 025 — Guest Request Triage

**Risk:** Medium  
**When to use:** When multiple in-stay requests need routing, priority and closure control.  
**Human owner/approver:** Front Office Supervisor / Duty Manager

**Required inputs**
- sanitized guest-request list
- request timestamps
- approved service-level targets
- department ownership rules
- open status/previous actions

**Expected output**
- priority queue
- department owner
- deadline/checkpoint
- access/approval dependency
- overdue/escalation flags

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as a front-office operations support analyst for a hotel or serviced-apartment property.
Supported role: [Front Office Agent / Supervisor / Duty Manager]
Accountable owner: [Front Office Supervisor / Duty Manager]

O — OPERATIONAL OBJECTIVE & CONTEXT
Triage guest requests by safety/urgency, guest blockage, SLA, repeat status and dependency. Produce a closed-loop action view.
Property: [type and location]
Operating date/time: [confirmed period]
Guest-journey stage: [pre-arrival / arrival / in-stay / departure]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied approved records. Relevant sources may include PMS/reservation record, approved housekeeping room status, CMMS close-out, guest-request system, approved policy/SOP, transport confirmation and authorized management instruction.

If a critical field is missing, stale or contradictory, do not guess. Mark it UNVERIFIED, name the source/owner needed, and state the next verification action.
Minimize personal data. Do not request or reproduce passport/ID numbers, full payment-card data, credentials, unnecessary contact data or unrelated sensitive notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return the requested operational output with four labels where relevant:
CONFIRMED FACT
REQUEST / PREFERENCE
UNRESOLVED / DEPENDENCY
RECOMMENDED ACTION

For every unresolved operational item show owner, next action, deadline/checkpoint and escalation condition.
priority queue
department owner
deadline/checkpoint
access/approval dependency
overdue/escalation flags

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not interpret a request as an entitlement or authorize late checkout, charges, refunds, room moves or technical access.
Do not alter PMS status, reservation, payment, room assignment, guest entitlement or official record.
Do not invent times, prices, availability, benefits, compensation or policy.
Output is a draft until verified by Front Office Supervisor / Duty Manager.
```

### Prompt 026 — Checkout Readiness Planner

**Risk:** Medium  
**When to use:** Before departure waves or for complex/extended-stay departures.  
**Human owner/approver:** Front Office Supervisor / Duty Manager

**Required inputs**
- approved departure list
- confirmed checkout/late-checkout status
- billing/invoice workflow status
- transport/luggage confirmations
- open guest cases

**Expected output**
- departure watch list
- open dependencies
- guest-contact actions
- post-departure operational triggers

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as a front-office operations support analyst for a hotel or serviced-apartment property.
Supported role: [Front Office Agent / Supervisor / Duty Manager]
Accountable owner: [Front Office Supervisor / Duty Manager]

O — OPERATIONAL OBJECTIVE & CONTEXT
Prepare a checkout-readiness plan and flag items requiring authorized review before departure.
Property: [type and location]
Operating date/time: [confirmed period]
Guest-journey stage: [pre-arrival / arrival / in-stay / departure]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied approved records. Relevant sources may include PMS/reservation record, approved housekeeping room status, CMMS close-out, guest-request system, approved policy/SOP, transport confirmation and authorized management instruction.

If a critical field is missing, stale or contradictory, do not guess. Mark it UNVERIFIED, name the source/owner needed, and state the next verification action.
Minimize personal data. Do not request or reproduce passport/ID numbers, full payment-card data, credentials, unnecessary contact data or unrelated sensitive notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return the requested operational output with four labels where relevant:
CONFIRMED FACT
REQUEST / PREFERENCE
UNRESOLVED / DEPENDENCY
RECOMMENDED ACTION

For every unresolved operational item show owner, next action, deadline/checkpoint and escalation condition.
departure watch list
open dependencies
guest-contact actions
post-departure operational triggers

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not determine damage, charges, payment status or fee waivers independently.
Do not alter PMS status, reservation, payment, room assignment, guest entitlement or official record.
Do not invent times, prices, availability, benefits, compensation or policy.
Output is a draft until verified by Front Office Supervisor / Duty Manager.
```

### Prompt 027 — Front Desk Handover

**Risk:** Medium  
**When to use:** At every shift change.  
**Human owner/approver:** Outgoing and incoming Front Office Supervisors

**Required inputs**
- open guest cases
- arrival/departure watch items
- room-status dependencies
- open work orders relevant to guests
- approved recovery actions
- transport/deadline items

**Expected output**
- must-act-next-shift list
- open guest-impact items
- deadlines/checkpoints
- manager-authority items
- closed items excluded from follow-up

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as a front-office operations support analyst for a hotel or serviced-apartment property.
Supported role: [Front Office Agent / Supervisor / Duty Manager]
Accountable owner: [Outgoing and incoming Front Office Supervisors]

O — OPERATIONAL OBJECTIVE & CONTEXT
Convert shift records into a concise handover. Preserve unresolved exceptions, ownership and next action; remove non-actionable noise.
Property: [type and location]
Operating date/time: [confirmed period]
Guest-journey stage: [pre-arrival / arrival / in-stay / departure]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied approved records. Relevant sources may include PMS/reservation record, approved housekeeping room status, CMMS close-out, guest-request system, approved policy/SOP, transport confirmation and authorized management instruction.

If a critical field is missing, stale or contradictory, do not guess. Mark it UNVERIFIED, name the source/owner needed, and state the next verification action.
Minimize personal data. Do not request or reproduce passport/ID numbers, full payment-card data, credentials, unnecessary contact data or unrelated sensitive notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return the requested operational output with four labels where relevant:
CONFIRMED FACT
REQUEST / PREFERENCE
UNRESOLVED / DEPENDENCY
RECOMMENDED ACTION

For every unresolved operational item show owner, next action, deadline/checkpoint and escalation condition.
must-act-next-shift list
open guest-impact items
deadlines/checkpoints
manager-authority items
closed items excluded from follow-up

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not mark an issue closed merely because no new message exists.
Do not alter PMS status, reservation, payment, room assignment, guest entitlement or official record.
Do not invent times, prices, availability, benefits, compensation or policy.
Output is a draft until verified by Outgoing and incoming Front Office Supervisors.
```

### Prompt 028 — VIP Arrival Checklist Builder

**Risk:** Medium–High  
**When to use:** For approved VIP, priority, executive or high-touch arrivals.  
**Human owner/approver:** Duty Manager / Guest Relations or designated owner

**Required inputs**
- approved VIP/priority designation
- confirmed entitlements
- approved preferences
- room/inspection status
- transport/setup instructions
- authorized billing notes

**Expected output**
- readiness checklist
- confirmed vs preference labels
- department dependencies
- final verification gate

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as a front-office operations support analyst for a hotel or serviced-apartment property.
Supported role: [Front Office Agent / Supervisor / Duty Manager]
Accountable owner: [Duty Manager / Guest Relations or designated owner]

O — OPERATIONAL OBJECTIVE & CONTEXT
Build a minimum-necessary VIP/priority arrival checklist. Separate entitlement, approved setup, recorded preference and pending request.
Property: [type and location]
Operating date/time: [confirmed period]
Guest-journey stage: [pre-arrival / arrival / in-stay / departure]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied approved records. Relevant sources may include PMS/reservation record, approved housekeeping room status, CMMS close-out, guest-request system, approved policy/SOP, transport confirmation and authorized management instruction.

If a critical field is missing, stale or contradictory, do not guess. Mark it UNVERIFIED, name the source/owner needed, and state the next verification action.
Minimize personal data. Do not request or reproduce passport/ID numbers, full payment-card data, credentials, unnecessary contact data or unrelated sensitive notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return the requested operational output with four labels where relevant:
CONFIRMED FACT
REQUEST / PREFERENCE
UNRESOLVED / DEPENDENCY
RECOMMENDED ACTION

For every unresolved operational item show owner, next action, deadline/checkpoint and escalation condition.
readiness checklist
confirmed vs preference labels
department dependencies
final verification gate

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not infer preferences from nationality, status or past stereotypes; do not expose sensitive profile details beyond operational need.
Do not alter PMS status, reservation, payment, room assignment, guest entitlement or official record.
Do not invent times, prices, availability, benefits, compensation or policy.
Output is a draft until verified by Duty Manager / Guest Relations or designated owner.
```

### Prompt 029 — Front Office Exception Log Analyzer

**Risk:** Medium  
**When to use:** Weekly/monthly or after a high-volume period to identify recurring front-office failure patterns.  
**Human owner/approver:** Front Office Manager / Quality or Operations Manager

**Required inputs**
- sanitized exception log
- category/time/journey-stage fields
- room-status events where relevant
- resolution time
- department dependency

**Expected output**
- frequency/Pareto view
- repeat patterns
- confirmed observations
- root-cause hypotheses clearly labeled
- investigation plan

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as a front-office operations support analyst for a hotel or serviced-apartment property.
Supported role: [Front Office Agent / Supervisor / Duty Manager]
Accountable owner: [Front Office Manager / Quality or Operations Manager]

O — OPERATIONAL OBJECTIVE & CONTEXT
Analyze the exception log for recurring patterns. Separate observation from causal hypothesis and recommend evidence needed to test each hypothesis.
Property: [type and location]
Operating date/time: [confirmed period]
Guest-journey stage: [pre-arrival / arrival / in-stay / departure]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied approved records. Relevant sources may include PMS/reservation record, approved housekeeping room status, CMMS close-out, guest-request system, approved policy/SOP, transport confirmation and authorized management instruction.

If a critical field is missing, stale or contradictory, do not guess. Mark it UNVERIFIED, name the source/owner needed, and state the next verification action.
Minimize personal data. Do not request or reproduce passport/ID numbers, full payment-card data, credentials, unnecessary contact data or unrelated sensitive notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return the requested operational output with four labels where relevant:
CONFIRMED FACT
REQUEST / PREFERENCE
UNRESOLVED / DEPENDENCY
RECOMMENDED ACTION

For every unresolved operational item show owner, next action, deadline/checkpoint and escalation condition.
frequency/Pareto view
repeat patterns
confirmed observations
root-cause hypotheses clearly labeled
investigation plan

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not blame individuals/departments or claim causation from correlation.
Do not alter PMS status, reservation, payment, room assignment, guest entitlement or official record.
Do not invent times, prices, availability, benefits, compensation or policy.
Output is a draft until verified by Front Office Manager / Quality or Operations Manager.
```

### Prompt 030 — Multilingual Guest Message Draft

**Risk:** Medium  
**When to use:** When a confirmed hotel message must be translated/adapted for a guest.  
**Human owner/approver:** Front Office Agent / Supervisor; specialist review where required

**Required inputs**
- approved source-language message
- target language
- confirmed dates/times/prices/policy text
- tone requirement

**Expected output**
- translated guest message
- meaning-preservation check
- ambiguous phrases requiring human review

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as a front-office operations support analyst for a hotel or serviced-apartment property.
Supported role: [Front Office Agent / Supervisor / Duty Manager]
Accountable owner: [Front Office Agent / Supervisor; specialist review where required]

O — OPERATIONAL OBJECTIVE & CONTEXT
Translate/adapt the approved message while preserving operational meaning, confirmation status, dates, prices, conditions and escalation contact.
Property: [type and location]
Operating date/time: [confirmed period]
Guest-journey stage: [pre-arrival / arrival / in-stay / departure]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied approved records. Relevant sources may include PMS/reservation record, approved housekeeping room status, CMMS close-out, guest-request system, approved policy/SOP, transport confirmation and authorized management instruction.

If a critical field is missing, stale or contradictory, do not guess. Mark it UNVERIFIED, name the source/owner needed, and state the next verification action.
Minimize personal data. Do not request or reproduce passport/ID numbers, full payment-card data, credentials, unnecessary contact data or unrelated sensitive notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return the requested operational output with four labels where relevant:
CONFIRMED FACT
REQUEST / PREFERENCE
UNRESOLVED / DEPENDENCY
RECOMMENDED ACTION

For every unresolved operational item show owner, next action, deadline/checkpoint and escalation condition.
translated guest message
meaning-preservation check
ambiguous phrases requiring human review

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not soften, strengthen or alter policy/financial meaning; high-impact safety, legal, payment or cancellation messages require enhanced human review.
Do not alter PMS status, reservation, payment, room assignment, guest entitlement or official record.
Do not invent times, prices, availability, benefits, compensation or policy.
Output is a draft until verified by Front Office Agent / Supervisor; specialist review where required.
```

---

## 18. Verification checklist before using any Front Office AI output

Before an AI-assisted front-office output reaches a guest or changes the team's actions, verify:

- the reservation/status information against the approved system;
- room readiness through the approved release process;
- all times, prices, inclusions and policies;
- whether a request is a preference, entitlement or pending approval;
- whether the person sending the message has authority to make the promise;
- whether unnecessary personal data has been removed;
- whether another guest's information could be exposed;
- whether open dependencies have an owner and checkpoint;
- whether translated wording preserves the original meaning;
- whether the official system/record has been updated by an authorized person where required.

---

## 19. What good Front Office AI looks like

Good Front Office AI is almost invisible to the guest. The guest should experience a team that is prepared, consistent and clear—not a chatbot pretending to run the hotel.

The operational test is not “Did AI write a better message?” It is:

> **Did the team make fewer unsupported promises, identify dependencies earlier, preserve privacy, close requests more reliably and hand over a cleaner operating picture?**

When those controls improve, AI is supporting hospitality rather than replacing it.

---

## 20. Key takeaway

Front Office is where operational uncertainty can quickly become a guest expectation. That makes disciplined prompting essential.

Use AI to organize evidence, prepare communication, identify missing information, structure queues and preserve handovers. Keep the PMS and approved operational systems as the source of truth. Keep room release, financial decisions, guest entitlements and service-recovery authority with authorized people.

The formula for this chapter is:

> **Confirmed data + clear ownership + controlled communication + human authority = safer Front Office AI.**

---

## Sources and evidence boundaries

This chapter is an operational framework, not legal advice. Property-specific SOPs, PMS workflows, brand standards, delegation-of-authority rules and privacy policies remain controlling. UAE privacy requirements should be interpreted and implemented by the organization's responsible legal/privacy roles. The 60-unit UAE serviced-apartment scenario is fictional and is used only for training and workflow design.

Reference frameworks used across the playbook include the UAE personal-data protection framework, NIST AI Risk Management Framework / Generative AI Profile, and ISO/IEC 42001 AI management-system principles.
---

## Continue the Playbook

**Previous:** Article 02 — Hotel Operations Manager AI Toolkit  
**Next:** Article 04 — Reservations AI Toolkit  
**Framework:** HOTEL — Hospitality role, Operational objective, Trusted inputs, Expected output, Limits