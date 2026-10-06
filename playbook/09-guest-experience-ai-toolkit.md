# Article 09 — Guest Experience AI Toolkit

## 10 Professional AI Prompts for Guest Journeys, Personalization, Pre-Arrival Planning, Accessibility, Touchpoint Audits and Experience Improvement

**Track C · Hotel & Serviced Apartment AI Operations Playbook · Guest Experience chapter**

Guest experience is often described as emotion, hospitality and memorable service. Operationally, however, it is also a **chain of promises, handovers, timestamps, preferences, physical touchpoints and recovery decisions**.

A guest may interact with Reservations before arrival, a transfer provider at the airport, Front Office at check-in, Housekeeping during the stay, Engineering when a defect appears, Guest Relations for a special request, Finance at checkout and a digital review channel after departure. The guest experiences one stay. The organization experiences many departments.

AI can help connect those fragments. It can summarize a journey, detect unresolved requests, prepare communication, organize verified preferences and turn recurring friction into an improvement backlog. But guest experience is also one of the easiest areas for AI to become intrusive, overconfident or operationally unsafe. A model can invent a preference, assume sentiment, expose personal information, promise an upgrade, misstate accessibility capability or convert an unverified note into a permanent profile.

The operating principle for this chapter is:

> **AI may help the hotel understand and coordinate the guest journey. Verified guest statements, approved systems, service standards and accountable people control the promise.**

The ten prompts follow a guest-experience control cycle:

> **Review journey → Personalize verified requests → Prepare arrival → Review the live stay → Follow up → Govern preferences → Plan special occasions → Protect accessibility → Audit touchpoints → Prioritize improvement**

---

## 1. Guest experience is a cross-department operating system

A strong guest journey cannot be owned by Guest Relations alone. Many failures happen at the seams between departments: a special request is captured by Reservations but not handed to Housekeeping; Engineering closes a work order but Front Office is not told; a transfer delay is known by Transport but the arrival team still expects the original time; a long-stay resident repeats the same request because the preference was recorded inconsistently.

AI is useful when it makes these dependencies visible. It is not useful when it simply produces polished language around incomplete operations.

A professional guest-experience AI workflow asks four questions before drafting anything:

1. **What is confirmed?**
2. **What is only reported, assumed or inferred?**
3. **Who owns the next operational action?**
4. **What may be communicated to the guest now?**

## 2. The Guest Experience HOTEL model

- **H — Hospitality role & human owner:** define the Guest Experience Manager, Duty Manager, Front Office, Reservations, Quality, Housekeeping, Engineering or other role accountable for the output.
- **O — Operational objective & context:** identify journey stage, stay type, property, channel, time sensitivity, guest request and operational dependencies.
- **T — Trusted inputs & sources of truth:** use the PMS, approved CRM or guest-request log, controlled SOPs, verified department confirmations, CMMS where technical work matters, approved service standards and current property information.
- **E — Expected output, exceptions & evidence:** separate facts, guest-stated preferences, assumptions, risks, unresolved items and next actions. Every promise should be traceable to evidence or approval.
- **L — Limits, privacy & leadership approval:** minimize personal data, prohibit sensitive inference, distinguish preference from entitlement and require qualified approval for compensation, accessibility commitments, financial decisions and high-impact service promises.

### Guest-experience source-of-truth matrix

| Question | Primary source of truth | AI rule |
|---|---|---|
| What did the guest book? | PMS / CRS / confirmed reservation | do not rely on memory or chat alone |
| What did the guest request? | approved request/CRM record + guest statement | distinguish request from confirmed delivery |
| What preference is known? | approved profile with source/date | no inference from nationality, name or prior assumptions |
| Is a room/apartment ready? | PMS + approved housekeeping release | never invent readiness |
| Is a defect resolved? | CMMS/Engineering closure + required room checks | closure note is not automatically room release |
| What benefit is the guest entitled to? | approved rate/loyalty/corporate policy | do not upgrade entitlement by assumption |
| Was a service delivered? | timestamped operational record / verified owner | absence of complaint is not proof of delivery |
| Is an accessibility feature available? | verified property inventory/technical information | never assume or overstate capability |
| Was compensation approved? | approved authority record | AI cannot approve |
| What feedback was provided? | survey/review/approved guest-feedback record | separate direct feedback/theme from interpretation |

## 3. Fictional UAE 60-unit serviced-apartment case

Continue with the fictional 60-unit UAE serviced-apartment portfolio used throughout the playbook. The property hosts leisure guests, project teams, corporate residents and families staying from several nights to several months.

During one operating week:
- a corporate resident arriving late has requested a quiet apartment and airport transfer;
- a family has requested a baby cot and early access but only the cot is confirmed;
- a returning resident previously preferred weekly housekeeping on Saturday mornings, but the preference record is six months old;
- an apartment has a recently closed AC work order and needs operational verification before any reassurance is given;
- a guest has voluntarily stated that step-free access is required;
- a birthday setup has been requested, but there is no approved complimentary budget in the record;
- two surveys mention slow response to in-stay requests, yet the request log has incomplete closure timestamps.

A weak AI system might combine these notes and tell staff to prepare the returning guest's “usual” service, upgrade the birthday guest, guarantee early check-in and confirm an accessible route. A controlled system instead separates confirmed service facts, guest-stated preferences or needs, unconfirmed operational promises and evidence gaps.

That distinction is the foundation of responsible personalization.

## 4. A guest journey review should expose friction, not invent emotion

Journey mapping shows what happened across discovery, booking, pre-arrival, arrival, check-in, stay, issue handling, checkout and post-stay follow-up.

AI can consolidate timestamps and handovers into one view. It should not state that a guest was angry, disappointed or delighted unless that sentiment is directly expressed or supported by an approved feedback source. Better operational language is: “The guest contacted the property three times before closure,” or “The request remained open beyond the approved target.”

That makes the output auditable and useful for improvement.

## 5. Personalization starts with permission and provenance

Personalization becomes risky when hotels store every incidental detail forever. A preference should be **relevant, sourced, reviewable and proportionate**.

A useful preference record includes the preference statement, source, date captured, whether it was one-time or recurring, operational owner, review or expiry date where appropriate, and privacy restrictions.

“Guest requested extra pillows for this stay” is not automatically “guest always prefers extra pillows.” A dining-information request should not be converted into a permanent sensitive profile. A responsible AI system preserves exactly what the guest said and avoids unnecessary inference.

## 6. Pre-arrival communication is a promise-control process

The best pre-arrival message is not the longest one. It is the message that gives the guest useful, current information without creating commitments the operation cannot support.

A professional planner checks reservation and dates, room/apartment type, arrival time if known, verified transfer details, confirmed requests, requests awaiting approval, check-in requirements, accurate property information and relevant contact channels.

Dynamic facts—such as room readiness, transfer ETA or upgrade availability—must be reverified before sending.

## 7. In-stay review is about closing loops

One housekeeping delay, one unresolved appliance question and one missing callback can collectively create a poor stay. Prompt 084 creates an active-stay control view: open item, owner, due time, dependency, last guest contact, next verification and closure evidence.

The goal is proactive coordination without surveillance-style profiling.

## 8. Post-stay follow-up should not rewrite history

A polite thank-you message is still wrong if it claims that a problem was resolved when the records do not prove closure. Post-stay work should separate guest-facing acknowledgement, internal unresolved actions, learning for future stays, approved CRM updates and cases requiring manager follow-up.

Marketing follow-up and service-recovery closure are different workflows and may have different consent requirements.

## 9. Special occasions need the same controls as any other operation

Birthdays, anniversaries and celebrations create cost, timing, food, access and supplier dependencies. A beautiful AI-generated plan is worthless if an item has not been approved, the room cannot be accessed, decoration conflicts with safety rules or a benefit has been promised without authority.

Prompt 087 produces a task-and-approval plan, not an automatic promise.

## 10. Accessibility is a high-risk guest-experience domain

Accessibility requests require precision and respect. The guest should define the need in their own terms. AI should help coordinate verified features and actions—not diagnose a condition or decide what the guest must need.

If the hotel cannot verify a requested feature, the correct output is **unconfirmed — verify before promising**. The same rule applies to transport, evacuation, bathroom features, route access, lifts, mobility equipment, sensory support and other accessibility-related details.

## 11. Touchpoint audits separate design from execution

A touchpoint can fail because the process is badly designed or because a good process was not followed. These require different actions.

For each audited touchpoint compare:

**Standard → Actual evidence → Gap → Failure type → Owner → Corrective action → Validation measure**

This is where Guest Experience connects directly to Quality and SOP design.

## 12. Feedback themes need denominators and evidence

If five reviews mention slow response, that is a signal. It is not enough by itself to state that service response is deteriorating. Examine the time period, total responses, request volumes, channels, closure times and whether the feedback relates to the same process.

AI can cluster themes, but outputs should show sample size, missing denominators and source limitations.

## 13. The experience backlog converts listening into action

A useful improvement backlog contains the problem statement, journey stage, guest impact, frequency or sample basis, root-cause status, proposed action, accountable owner, effort, dependencies, KPI and validation date.

AI can rank evidence and make dependencies visible. It must not manufacture ROI or guest-satisfaction uplift.

## 14. Guest Experience KPI dashboard

| KPI | Purpose |
|---|---|
| Request response time | responsiveness |
| Request closure time | end-to-end control |
| Reopened/repeated request rate | closure quality |
| Pre-arrival request confirmation rate | promise readiness |
| Room-not-ready communication timeliness | arrival control |
| Guest follow-up completion | closed-loop service |
| Complaint recurrence by theme | systemic friction |
| Touchpoint compliance | service-standard execution |
| Preference record age/completeness | personalization governance |
| Accessibility-request verification completion | high-risk readiness |
| Post-stay unresolved case count | closure discipline |

## 15. Lean Six Sigma application

**Define:** identify a guest-experience problem such as repeated request follow-up, slow room-ready communication or recurring handover gaps.

**Measure:** capture timestamps, request categories, touchpoints, recurrence, escalation, guest feedback and closure evidence.

**Analyze:** stratify by journey stage, department, channel, stay type, time, dependency and failure mode.

**Improve:** redesign the handover, SOP, staffing rule, checklist, system field or service standard.

**Control:** monitor recurrence, audit evidence quality and confirm that the improvement remains effective.

AI accelerates synthesis and hypothesis generation. It does not replace Voice of Customer evidence or process-owner validation.

## 16. Before → Action → After → AED Saved

Guest-experience improvements can create financial value, but savings should not be invented.

Illustrative example: the property identifies repeated late delivery of approved welcome amenities. The team changes the pre-arrival handover and introduces a confirmation checkpoint. After a controlled period, it measures fewer emergency purchases, fewer recovery gestures and less staff rework.

**Before:** verified rework and recovery cost.  
**Action:** controlled process change.  
**After:** verified reduction over a comparable period.  
**AED Saved:** actual avoided cost, documented by Finance or the accountable owner.

Do not assign a revenue value to guest happiness without evidence.

## 17. Guest Experience AI authority matrix

| Task | AI may | AI may not | Human authority |
|---|---|---|---|
| Journey review | consolidate verified evidence | invent guest emotion | Guest Experience / Quality |
| Personalization | draft from verified preferences | infer sensitive traits | Guest Relations / CRM owner |
| Pre-arrival message | draft confirmed information | promise readiness/upgrades | Front Office / Reservations |
| In-stay review | flag open loops | authorize compensation | Duty Manager |
| Post-stay follow-up | draft message | claim unverified closure | Guest Relations / Manager |
| Preference summary | organize approved preferences | create hidden profiling | CRM/Data owner |
| Special occasion | plan tasks/contingencies | approve cost/complimentary items | Authorized manager |
| Accessibility review | coordinate stated needs | diagnose or overstate capability | Duty/Rooms + qualified owners |
| Touchpoint audit | compare standard vs evidence | create HR finding from anecdote | Quality / Process owner |
| Improvement backlog | prioritize evidence | manufacture ROI | Operations / GM / Finance as relevant |

## 18. 30-day implementation plan

**Days 1–5:** define journey stages, approved guest-data sources, guest-request statuses and authority boundaries.

**Days 6–10:** pilot Prompts 081–083 on historical stays; compare AI summaries with PMS/CRM records and manager review.

**Days 11–15:** pilot Prompts 084–086; clean stale preference records and establish provenance/review rules.

**Days 16–20:** test special-occasion and accessibility workflows with fictional scenarios, including unavailable features and approval exceptions.

**Days 21–25:** audit two high-volume touchpoints using Prompt 089 and classify design versus execution failures.

**Days 26–30:** build the first controlled improvement backlog with Prompt 090, assign owners and define validation dates.

## 19. Cross-website knowledge connections

Article 09 belongs inside the wider Ahmed Quality Ops knowledge network, not only this series. Relevant connections include:

- **Front Office AI Toolkit** — arrival readiness, request triage, VIP handling and communication.
- **Reservations AI Toolkit** — pre-arrival requests, booking facts, corporate entitlements and exceptions.
- **Hotel Apartment & Extended-Stay AI Toolkit** — long-stay preferences, recurring service and resident lifecycle.
- **Housekeeping Management AI Toolkit** — room release, recurring housekeeping and amenities.
- **Engineering & Maintenance / Predictive Maintenance** — technical defects and proactive service impact.
- **Guest Complaint & Service Recovery AI Toolkit** — escalation and recovery when experience breaks down.
- **Hotel Quality Audit AI Toolkit** — touchpoint evidence and service-standard compliance.
- **Hotel SOP & Process Design / RACI / Exception Escalation** — ownership, authority and closed-loop workflows.
- **MICE operations** — group arrivals, event touchpoints and compressed service windows.
- **Tourism transport and dispatch** — airport pickup and movement experience before hotel arrival.
- **Tourism AI Operations Playbook** — wider tourism guest-journey and responsible-AI methods.

Useful existing website connections include:
- /articles/tourism-ai-operations-playbook/index.html
- /articles/sop-exception-escalation-management/index.html
- /articles/sop-roles-authority-raci/index.html
- /articles/how-to-write-professional-sop-procedure/index.html
- /articles/article-abu-dhabi-mice-movement-control-room/index.html

When website integration is performed, relevant older articles should receive reciprocal links back to this Guest Experience chapter.

## 20. Management checklist

- Is each guest promise supported by a verified source or approval?
- Are requests separated from confirmed delivery?
- Are preferences sourced, dated and proportionate?
- Are sensitive traits never inferred?
- Are dynamic facts rechecked before guest communication?
- Does every open in-stay request have an owner and next action?
- Are special occasions controlled for cost, access and safety?
- Are accessibility commitments verified rather than assumed?
- Do feedback analyses show sample size and evidence limits?
- Does the improvement backlog have owners, measures and validation dates?
- Can the team trace a guest-facing statement back to a system, policy or authorized human?

## 21. Key takeaway

Guest experience does not improve because AI writes warmer messages. It improves when the hotel **connects verified information, closes operational loops, remembers only what it should remember and makes promises it can actually keep**.

AI is most valuable as a coordination and evidence tool. The guest remains a person, not a profile; the PMS/CRM/SOP remains the operational record; and accountable hotel professionals remain responsible for the promise.

---

# 22. The 10 copy-ready prompts


## Prompt 081 — Guest Journey Review

**Risk:** Medium  
**Human owner:** Guest Experience Manager / Rooms Division Manager

**When to use:** Review the end-to-end guest journey using verified operational evidence and identify friction, gaps and ownership actions.

### Why this prompt matters

This prompt converts guest-experience information into a controlled operational view. It protects the distinction between what the guest said, what the hotel has verified, what is still pending and what requires human authority.

### Required inputs

- stay/journey timeline
- PMS reservation and stay facts
- guest requests and approved CRM notes
- service logs/work orders
- feedback/review data
- current SOPs and service standards

### Expected outputs

- journey-stage map
- confirmed friction points
- evidence gaps
- owner/action register
- priority recommendations

### Copy-ready prompt

```text
ROLE
Act as a senior hotel guest-experience and service-design support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Guest Experience / Guest Relations / Front Office / Reservations / Quality / Duty Management as applicable]
Accountable owner/approver: Guest Experience Manager / Rooms Division Manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Review the end-to-end guest journey using verified operational evidence and identify friction, gaps and ownership actions.
Property/location: [insert confirmed property and location]
Journey stage / stay type / operating period: [insert]
Guest request or experience problem: [insert only what is necessary]
Departments/dependencies involved: [insert]
Decision or workflow this output supports: [insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: stay/journey timeline; PMS reservation and stay facts; guest requests and approved CRM notes; service logs/work orders; feedback/review data; current SOPs and service standards.
Approved sources: PMS/CRS; approved CRM or guest-request log; controlled SOP/service standards; verified department confirmations; CMMS where technical issues matter; approved loyalty/corporate entitlement sources; approved property information.
Treat guest statements as guest-stated information, not independently verified facts unless the distinction does not matter for service delivery.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, its owner and required verification source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: journey-stage map; confirmed friction points; evidence gaps; owner/action register; priority recommendations.
Separate CONFIRMED FACTS, GUEST-STATED PREFERENCES/NEEDS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
For every guest-facing promise, show the supporting source/approval or label it NOT YET CONFIRMED.
Where sources conflict, show the conflict and the safest verification action.
Include owner, due time, dependency and closure evidence for operational actions where applicable.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not infer guest sentiment, preferences or causes from incomplete evidence. Do not expose unnecessary personal data.
Do not include unnecessary passport/ID data, payment data, credentials, private employee information, security-sensitive details or confidential contracts.
Do not authorize compensation, upgrades, rate changes, refunds, room release, safety decisions or other actions outside the approved authority matrix.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational action.
```

### Human verification

Before use, verify the source records, current operating status, privacy need, guest entitlement, departmental ownership and any guest-facing promise. High-impact or sensitive outputs require the named accountable owner.


## Prompt 082 — Guest Request Personalization Draft

**Risk:** Medium  
**Human owner:** Guest Relations / Front Office Manager

**When to use:** Turn a verified guest request or preference into a personalized service plan or message without inventing entitlement or sensitive traits.

### Why this prompt matters

This prompt converts guest-experience information into a controlled operational view. It protects the distinction between what the guest said, what the hotel has verified, what is still pending and what requires human authority.

### Required inputs

- verified request text
- approved guest profile/preferences
- reservation/stay context
- available services
- entitlement/benefit rules
- communication channel

### Expected outputs

- personalized response draft
- service action plan
- verification questions
- constraints/entitlement flags
- handover notes

### Copy-ready prompt

```text
ROLE
Act as a senior hotel guest-experience and service-design support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Guest Experience / Guest Relations / Front Office / Reservations / Quality / Duty Management as applicable]
Accountable owner/approver: Guest Relations / Front Office Manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Turn a verified guest request or preference into a personalized service plan or message without inventing entitlement or sensitive traits.
Property/location: [insert confirmed property and location]
Journey stage / stay type / operating period: [insert]
Guest request or experience problem: [insert only what is necessary]
Departments/dependencies involved: [insert]
Decision or workflow this output supports: [insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: verified request text; approved guest profile/preferences; reservation/stay context; available services; entitlement/benefit rules; communication channel.
Approved sources: PMS/CRS; approved CRM or guest-request log; controlled SOP/service standards; verified department confirmations; CMMS where technical issues matter; approved loyalty/corporate entitlement sources; approved property information.
Treat guest statements as guest-stated information, not independently verified facts unless the distinction does not matter for service delivery.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, its owner and required verification source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: personalized response draft; service action plan; verification questions; constraints/entitlement flags; handover notes.
Separate CONFIRMED FACTS, GUEST-STATED PREFERENCES/NEEDS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
For every guest-facing promise, show the supporting source/approval or label it NOT YET CONFIRMED.
Where sources conflict, show the conflict and the safest verification action.
Include owner, due time, dependency and closure evidence for operational actions where applicable.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not infer religion, health status, nationality-based preferences, family status, spending power or other sensitive traits. Do not promise upgrades, amenities, rates or benefits that are not confirmed.
Do not include unnecessary passport/ID data, payment data, credentials, private employee information, security-sensitive details or confidential contracts.
Do not authorize compensation, upgrades, rate changes, refunds, room release, safety decisions or other actions outside the approved authority matrix.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational action.
```

### Human verification

Before use, verify the source records, current operating status, privacy need, guest entitlement, departmental ownership and any guest-facing promise. High-impact or sensitive outputs require the named accountable owner.


## Prompt 083 — Pre-Arrival Communication Planner

**Risk:** Medium  
**Human owner:** Guest Experience / Front Office / Reservations Manager

**When to use:** Build a coordinated pre-arrival communication plan using confirmed booking facts, requests and property information.

### Why this prompt matters

This prompt converts guest-experience information into a controlled operational view. It protects the distinction between what the guest said, what the hotel has verified, what is still pending and what requires human authority.

### Required inputs

- confirmed reservation
- arrival/departure details
- room/apartment type
- verified requests
- approved hotel information
- transfer/arrival information if applicable

### Expected outputs

- communication timeline
- message drafts
- missing-information questions
- department actions
- guest-promise risk flags

### Copy-ready prompt

```text
ROLE
Act as a senior hotel guest-experience and service-design support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Guest Experience / Guest Relations / Front Office / Reservations / Quality / Duty Management as applicable]
Accountable owner/approver: Guest Experience / Front Office / Reservations Manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Build a coordinated pre-arrival communication plan using confirmed booking facts, requests and property information.
Property/location: [insert confirmed property and location]
Journey stage / stay type / operating period: [insert]
Guest request or experience problem: [insert only what is necessary]
Departments/dependencies involved: [insert]
Decision or workflow this output supports: [insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: confirmed reservation; arrival/departure details; room/apartment type; verified requests; approved hotel information; transfer/arrival information if applicable.
Approved sources: PMS/CRS; approved CRM or guest-request log; controlled SOP/service standards; verified department confirmations; CMMS where technical issues matter; approved loyalty/corporate entitlement sources; approved property information.
Treat guest statements as guest-stated information, not independently verified facts unless the distinction does not matter for service delivery.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, its owner and required verification source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: communication timeline; message drafts; missing-information questions; department actions; guest-promise risk flags.
Separate CONFIRMED FACTS, GUEST-STATED PREFERENCES/NEEDS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
For every guest-facing promise, show the supporting source/approval or label it NOT YET CONFIRMED.
Where sources conflict, show the conflict and the safest verification action.
Include owner, due time, dependency and closure evidence for operational actions where applicable.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not invent room readiness, transfer timing, upgrade status, access instructions or special arrangements. Verify dynamic information immediately before sending.
Do not include unnecessary passport/ID data, payment data, credentials, private employee information, security-sensitive details or confidential contracts.
Do not authorize compensation, upgrades, rate changes, refunds, room release, safety decisions or other actions outside the approved authority matrix.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational action.
```

### Human verification

Before use, verify the source records, current operating status, privacy need, guest entitlement, departmental ownership and any guest-facing promise. High-impact or sensitive outputs require the named accountable owner.


## Prompt 084 — In-Stay Experience Review

**Risk:** Medium  
**Human owner:** Guest Experience Manager / Duty Manager

**When to use:** Review an active stay for unresolved requests, repeated friction and proactive service opportunities without creating surveillance-style profiling.

### Why this prompt matters

This prompt converts guest-experience information into a controlled operational view. It protects the distinction between what the guest said, what the hotel has verified, what is still pending and what requires human authority.

### Required inputs

- active-stay facts
- open/closed guest requests
- maintenance/housekeeping dependencies
- approved feedback notes
- service timestamps
- current entitlements

### Expected outputs

- open-issue summary
- repeat-friction flags
- proactive follow-up opportunities
- owner/deadline list
- guest-contact recommendation

### Copy-ready prompt

```text
ROLE
Act as a senior hotel guest-experience and service-design support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Guest Experience / Guest Relations / Front Office / Reservations / Quality / Duty Management as applicable]
Accountable owner/approver: Guest Experience Manager / Duty Manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Review an active stay for unresolved requests, repeated friction and proactive service opportunities without creating surveillance-style profiling.
Property/location: [insert confirmed property and location]
Journey stage / stay type / operating period: [insert]
Guest request or experience problem: [insert only what is necessary]
Departments/dependencies involved: [insert]
Decision or workflow this output supports: [insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: active-stay facts; open/closed guest requests; maintenance/housekeeping dependencies; approved feedback notes; service timestamps; current entitlements.
Approved sources: PMS/CRS; approved CRM or guest-request log; controlled SOP/service standards; verified department confirmations; CMMS where technical issues matter; approved loyalty/corporate entitlement sources; approved property information.
Treat guest statements as guest-stated information, not independently verified facts unless the distinction does not matter for service delivery.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, its owner and required verification source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: open-issue summary; repeat-friction flags; proactive follow-up opportunities; owner/deadline list; guest-contact recommendation.
Separate CONFIRMED FACTS, GUEST-STATED PREFERENCES/NEEDS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
For every guest-facing promise, show the supporting source/approval or label it NOT YET CONFIRMED.
Where sources conflict, show the conflict and the safest verification action.
Include owner, due time, dependency and closure evidence for operational actions where applicable.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Use only service-relevant information. Do not create psychological profiles, infer private behavior or recommend intrusive monitoring.
Do not include unnecessary passport/ID data, payment data, credentials, private employee information, security-sensitive details or confidential contracts.
Do not authorize compensation, upgrades, rate changes, refunds, room release, safety decisions or other actions outside the approved authority matrix.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational action.
```

### Human verification

Before use, verify the source records, current operating status, privacy need, guest entitlement, departmental ownership and any guest-facing promise. High-impact or sensitive outputs require the named accountable owner.


## Prompt 085 — Post-Stay Follow-Up Draft

**Risk:** Low  
**Human owner:** Guest Relations / Marketing or CRM Owner

**When to use:** Prepare a post-stay follow-up message and internal follow-up actions from verified stay outcomes and guest feedback.

### Why this prompt matters

This prompt converts guest-experience information into a controlled operational view. It protects the distinction between what the guest said, what the hotel has verified, what is still pending and what requires human authority.

### Required inputs

- verified stay completion
- approved feedback
- open issues/closures
- approved brand tone
- consent/communication rules
- loyalty or corporate context if confirmed

### Expected outputs

- guest message draft
- internal closure checks
- unresolved-item flags
- learning points
- CRM update recommendation

### Copy-ready prompt

```text
ROLE
Act as a senior hotel guest-experience and service-design support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Guest Experience / Guest Relations / Front Office / Reservations / Quality / Duty Management as applicable]
Accountable owner/approver: Guest Relations / Marketing or CRM Owner

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Prepare a post-stay follow-up message and internal follow-up actions from verified stay outcomes and guest feedback.
Property/location: [insert confirmed property and location]
Journey stage / stay type / operating period: [insert]
Guest request or experience problem: [insert only what is necessary]
Departments/dependencies involved: [insert]
Decision or workflow this output supports: [insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: verified stay completion; approved feedback; open issues/closures; approved brand tone; consent/communication rules; loyalty or corporate context if confirmed.
Approved sources: PMS/CRS; approved CRM or guest-request log; controlled SOP/service standards; verified department confirmations; CMMS where technical issues matter; approved loyalty/corporate entitlement sources; approved property information.
Treat guest statements as guest-stated information, not independently verified facts unless the distinction does not matter for service delivery.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, its owner and required verification source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: guest message draft; internal closure checks; unresolved-item flags; learning points; CRM update recommendation.
Separate CONFIRMED FACTS, GUEST-STATED PREFERENCES/NEEDS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
For every guest-facing promise, show the supporting source/approval or label it NOT YET CONFIRMED.
Where sources conflict, show the conflict and the safest verification action.
Include owner, due time, dependency and closure evidence for operational actions where applicable.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not state that an issue was resolved unless closure is verified. Do not include confidential internal findings in the guest-facing message.
Do not include unnecessary passport/ID data, payment data, credentials, private employee information, security-sensitive details or confidential contracts.
Do not authorize compensation, upgrades, rate changes, refunds, room release, safety decisions or other actions outside the approved authority matrix.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational action.
```

### Human verification

Before use, verify the source records, current operating status, privacy need, guest entitlement, departmental ownership and any guest-facing promise. High-impact or sensitive outputs require the named accountable owner.


## Prompt 086 — Guest Preference Summary

**Risk:** Medium  
**Human owner:** Guest Experience / CRM Data Owner

**When to use:** Convert verified service preferences into a minimal, operationally useful summary with provenance and review dates.

### Why this prompt matters

This prompt converts guest-experience information into a controlled operational view. It protects the distinction between what the guest said, what the hotel has verified, what is still pending and what requires human authority.

### Required inputs

- approved preference records
- source/date of each preference
- current stay context
- consent/privacy rules
- expiry/review rules

### Expected outputs

- preference summary
- source/provenance table
- stale/conflicting items
- do-not-store flags
- next-review date

### Copy-ready prompt

```text
ROLE
Act as a senior hotel guest-experience and service-design support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Guest Experience / Guest Relations / Front Office / Reservations / Quality / Duty Management as applicable]
Accountable owner/approver: Guest Experience / CRM Data Owner

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Convert verified service preferences into a minimal, operationally useful summary with provenance and review dates.
Property/location: [insert confirmed property and location]
Journey stage / stay type / operating period: [insert]
Guest request or experience problem: [insert only what is necessary]
Departments/dependencies involved: [insert]
Decision or workflow this output supports: [insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: approved preference records; source/date of each preference; current stay context; consent/privacy rules; expiry/review rules.
Approved sources: PMS/CRS; approved CRM or guest-request log; controlled SOP/service standards; verified department confirmations; CMMS where technical issues matter; approved loyalty/corporate entitlement sources; approved property information.
Treat guest statements as guest-stated information, not independently verified facts unless the distinction does not matter for service delivery.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, its owner and required verification source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: preference summary; source/provenance table; stale/conflicting items; do-not-store flags; next-review date.
Separate CONFIRMED FACTS, GUEST-STATED PREFERENCES/NEEDS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
For every guest-facing promise, show the supporting source/approval or label it NOT YET CONFIRMED.
Where sources conflict, show the conflict and the safest verification action.
Include owner, due time, dependency and closure evidence for operational actions where applicable.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not infer sensitive traits or turn one-time requests into permanent preferences. Minimize retention and follow property privacy rules.
Do not include unnecessary passport/ID data, payment data, credentials, private employee information, security-sensitive details or confidential contracts.
Do not authorize compensation, upgrades, rate changes, refunds, room release, safety decisions or other actions outside the approved authority matrix.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational action.
```

### Human verification

Before use, verify the source records, current operating status, privacy need, guest entitlement, departmental ownership and any guest-facing promise. High-impact or sensitive outputs require the named accountable owner.


## Prompt 087 — Special Occasion Planning Support

**Risk:** Medium  
**Human owner:** Guest Experience Manager / Duty Manager

**When to use:** Coordinate a special-occasion service plan from verified guest requests, budget/authority and operational capacity.

### Why this prompt matters

This prompt converts guest-experience information into a controlled operational view. It protects the distinction between what the guest said, what the hotel has verified, what is still pending and what requires human authority.

### Required inputs

- occasion/request
- confirmed dates/timing
- approved budget/entitlement
- available services/vendors
- dietary/accessibility requirements when voluntarily provided and necessary
- department owners

### Expected outputs

- occasion plan
- task/owner timeline
- guest-facing confirmation draft
- contingencies
- approval and cost flags

### Copy-ready prompt

```text
ROLE
Act as a senior hotel guest-experience and service-design support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Guest Experience / Guest Relations / Front Office / Reservations / Quality / Duty Management as applicable]
Accountable owner/approver: Guest Experience Manager / Duty Manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Coordinate a special-occasion service plan from verified guest requests, budget/authority and operational capacity.
Property/location: [insert confirmed property and location]
Journey stage / stay type / operating period: [insert]
Guest request or experience problem: [insert only what is necessary]
Departments/dependencies involved: [insert]
Decision or workflow this output supports: [insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: occasion/request; confirmed dates/timing; approved budget/entitlement; available services/vendors; dietary/accessibility requirements when voluntarily provided and necessary; department owners.
Approved sources: PMS/CRS; approved CRM or guest-request log; controlled SOP/service standards; verified department confirmations; CMMS where technical issues matter; approved loyalty/corporate entitlement sources; approved property information.
Treat guest statements as guest-stated information, not independently verified facts unless the distinction does not matter for service delivery.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, its owner and required verification source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: occasion plan; task/owner timeline; guest-facing confirmation draft; contingencies; approval and cost flags.
Separate CONFIRMED FACTS, GUEST-STATED PREFERENCES/NEEDS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
For every guest-facing promise, show the supporting source/approval or label it NOT YET CONFIRMED.
Where sources conflict, show the conflict and the safest verification action.
Include owner, due time, dependency and closure evidence for operational actions where applicable.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not promise complimentary items, upgrades, decorations, external vendors or spending without approval. Treat sensitive details as need-to-know.
Do not include unnecessary passport/ID data, payment data, credentials, private employee information, security-sensitive details or confidential contracts.
Do not authorize compensation, upgrades, rate changes, refunds, room release, safety decisions or other actions outside the approved authority matrix.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational action.
```

### Human verification

Before use, verify the source records, current operating status, privacy need, guest entitlement, departmental ownership and any guest-facing promise. High-impact or sensitive outputs require the named accountable owner.


## Prompt 088 — Accessibility Request Review

**Risk:** High  
**Human owner:** Duty Manager / Accessibility or Rooms Owner

**When to use:** Translate a voluntarily disclosed accessibility request into a verified operational coordination plan while avoiding medical assumptions.

### Why this prompt matters

This prompt converts guest-experience information into a controlled operational view. It protects the distinction between what the guest said, what the hotel has verified, what is still pending and what requires human authority.

### Required inputs

- guest-stated need/request
- approved accessible-room/features data
- property access information
- transport/route facts if applicable
- department confirmations
- emergency/safety procedures

### Expected outputs

- requirement summary in guest language
- verification questions
- department action plan
- unconfirmed-capability flags
- handover and escalation

### Copy-ready prompt

```text
ROLE
Act as a senior hotel guest-experience and service-design support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Guest Experience / Guest Relations / Front Office / Reservations / Quality / Duty Management as applicable]
Accountable owner/approver: Duty Manager / Accessibility or Rooms Owner

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Translate a voluntarily disclosed accessibility request into a verified operational coordination plan while avoiding medical assumptions.
Property/location: [insert confirmed property and location]
Journey stage / stay type / operating period: [insert]
Guest request or experience problem: [insert only what is necessary]
Departments/dependencies involved: [insert]
Decision or workflow this output supports: [insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: guest-stated need/request; approved accessible-room/features data; property access information; transport/route facts if applicable; department confirmations; emergency/safety procedures.
Approved sources: PMS/CRS; approved CRM or guest-request log; controlled SOP/service standards; verified department confirmations; CMMS where technical issues matter; approved loyalty/corporate entitlement sources; approved property information.
Treat guest statements as guest-stated information, not independently verified facts unless the distinction does not matter for service delivery.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, its owner and required verification source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: requirement summary in guest language; verification questions; department action plan; unconfirmed-capability flags; handover and escalation.
Separate CONFIRMED FACTS, GUEST-STATED PREFERENCES/NEEDS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
For every guest-facing promise, show the supporting source/approval or label it NOT YET CONFIRMED.
Where sources conflict, show the conflict and the safest verification action.
Include owner, due time, dependency and closure evidence for operational actions where applicable.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not diagnose a medical condition or decide what the guest needs beyond what they state. Never claim an accessible feature, evacuation capability or transport arrangement without verification.
Do not include unnecessary passport/ID data, payment data, credentials, private employee information, security-sensitive details or confidential contracts.
Do not authorize compensation, upgrades, rate changes, refunds, room release, safety decisions or other actions outside the approved authority matrix.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational action.
```

### Human verification

Before use, verify the source records, current operating status, privacy need, guest entitlement, departmental ownership and any guest-facing promise. High-impact or sensitive outputs require the named accountable owner.


## Prompt 089 — Service Touchpoint Audit

**Risk:** Medium  
**Human owner:** Quality / Guest Experience Manager

**When to use:** Audit selected guest touchpoints against approved service standards and actual evidence, separating design failure from execution failure.

### Why this prompt matters

This prompt converts guest-experience information into a controlled operational view. It protects the distinction between what the guest said, what the hotel has verified, what is still pending and what requires human authority.

### Required inputs

- guest journey/touchpoint list
- approved standards/SOPs
- observations or timestamped records
- feedback data
- department ownership
- exceptions

### Expected outputs

- touchpoint scorecard
- standard-vs-evidence gaps
- failure classification
- priority actions
- measurement plan

### Copy-ready prompt

```text
ROLE
Act as a senior hotel guest-experience and service-design support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Guest Experience / Guest Relations / Front Office / Reservations / Quality / Duty Management as applicable]
Accountable owner/approver: Quality / Guest Experience Manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Audit selected guest touchpoints against approved service standards and actual evidence, separating design failure from execution failure.
Property/location: [insert confirmed property and location]
Journey stage / stay type / operating period: [insert]
Guest request or experience problem: [insert only what is necessary]
Departments/dependencies involved: [insert]
Decision or workflow this output supports: [insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: guest journey/touchpoint list; approved standards/SOPs; observations or timestamped records; feedback data; department ownership; exceptions.
Approved sources: PMS/CRS; approved CRM or guest-request log; controlled SOP/service standards; verified department confirmations; CMMS where technical issues matter; approved loyalty/corporate entitlement sources; approved property information.
Treat guest statements as guest-stated information, not independently verified facts unless the distinction does not matter for service delivery.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, its owner and required verification source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: touchpoint scorecard; standard-vs-evidence gaps; failure classification; priority actions; measurement plan.
Separate CONFIRMED FACTS, GUEST-STATED PREFERENCES/NEEDS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
For every guest-facing promise, show the supporting source/approval or label it NOT YET CONFIRMED.
Where sources conflict, show the conflict and the safest verification action.
Include owner, due time, dependency and closure evidence for operational actions where applicable.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not score employees from anecdotal evidence or convert subjective impressions into disciplinary findings. Use the audit for process improvement unless a separate approved HR process applies.
Do not include unnecessary passport/ID data, payment data, credentials, private employee information, security-sensitive details or confidential contracts.
Do not authorize compensation, upgrades, rate changes, refunds, room release, safety decisions or other actions outside the approved authority matrix.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational action.
```

### Human verification

Before use, verify the source records, current operating status, privacy need, guest entitlement, departmental ownership and any guest-facing promise. High-impact or sensitive outputs require the named accountable owner.


## Prompt 090 — Guest Experience Improvement Backlog

**Risk:** Medium  
**Human owner:** Guest Experience Manager / Operations Manager

**When to use:** Convert verified guest-experience findings into a prioritized improvement backlog with owners, evidence, effort and expected impact.

### Why this prompt matters

This prompt converts guest-experience information into a controlled operational view. It protects the distinction between what the guest said, what the hotel has verified, what is still pending and what requires human authority.

### Required inputs

- verified findings
- complaint/feedback themes
- journey audits
- operational constraints
- estimated effort/cost
- owners and dependencies
- current KPIs

### Expected outputs

- prioritized backlog
- impact/effort rationale
- quick wins vs structural work
- owner/deadline register
- validation metrics

### Copy-ready prompt

```text
ROLE
Act as a senior hotel guest-experience and service-design support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Guest Experience / Guest Relations / Front Office / Reservations / Quality / Duty Management as applicable]
Accountable owner/approver: Guest Experience Manager / Operations Manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Convert verified guest-experience findings into a prioritized improvement backlog with owners, evidence, effort and expected impact.
Property/location: [insert confirmed property and location]
Journey stage / stay type / operating period: [insert]
Guest request or experience problem: [insert only what is necessary]
Departments/dependencies involved: [insert]
Decision or workflow this output supports: [insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: verified findings; complaint/feedback themes; journey audits; operational constraints; estimated effort/cost; owners and dependencies; current KPIs.
Approved sources: PMS/CRS; approved CRM or guest-request log; controlled SOP/service standards; verified department confirmations; CMMS where technical issues matter; approved loyalty/corporate entitlement sources; approved property information.
Treat guest statements as guest-stated information, not independently verified facts unless the distinction does not matter for service delivery.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, its owner and required verification source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: prioritized backlog; impact/effort rationale; quick wins vs structural work; owner/deadline register; validation metrics.
Separate CONFIRMED FACTS, GUEST-STATED PREFERENCES/NEEDS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
For every guest-facing promise, show the supporting source/approval or label it NOT YET CONFIRMED.
Where sources conflict, show the conflict and the safest verification action.
Include owner, due time, dependency and closure evidence for operational actions where applicable.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not manufacture ROI, guest-satisfaction uplift or savings. Label estimates and require owners to validate feasibility, cost and authority.
Do not include unnecessary passport/ID data, payment data, credentials, private employee information, security-sensitive details or confidential contracts.
Do not authorize compensation, upgrades, rate changes, refunds, room release, safety decisions or other actions outside the approved authority matrix.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational action.
```

### Human verification

Before use, verify the source records, current operating status, privacy need, guest entitlement, departmental ownership and any guest-facing promise. High-impact or sensitive outputs require the named accountable owner.


---

## 23. Human verification checklist for all ten prompts

Before operational use, confirm:

- the correct guest/stay record is being used;
- unnecessary personal data has been removed;
- any preference has a source and date;
- guest statements are not silently converted into verified operational facts;
- room, transfer, engineering, housekeeping and other dynamic status information is current;
- entitlements, complimentary items and financial decisions are verified against policy;
- accessibility-related statements are confirmed by the responsible property/technical owner;
- the output does not infer sensitive traits or create inappropriate profiling;
- unresolved items have owners and next actions;
- guest-facing messages contain no promise the hotel cannot currently support;
- closure is evidenced, not assumed;
- the final decision sits with the authorized human role.

## 24. Trainer notes

When teaching this chapter, test the prompts with deliberately imperfect data. Remove a room-readiness confirmation, insert two conflicting preference records, provide an old transfer time, or describe an accessibility request for a feature that has not been verified. A professional prompt should become **more cautious as evidence quality falls**.

The most important training question is not, “Did the AI produce a nice message?” It is:

> **Did the AI protect the hotel from making an unsupported promise while still helping the team deliver thoughtful service?**

## 25. Evidence boundary

The 60-unit UAE serviced-apartment examples in this chapter are fictional and illustrative. Calculations, response times, cost examples and improvement scenarios should be replaced with verified property data before operational or financial use.
