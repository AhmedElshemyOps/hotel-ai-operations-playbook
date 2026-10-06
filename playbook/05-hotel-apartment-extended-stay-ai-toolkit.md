# Article 05 — Hotel Apartment & Extended-Stay AI Toolkit

## 10 Professional AI Prompts for Long-Stay Readiness, Resident Service, Housekeeping, Utilities, Defects and Move-In / Move-Out Control

**Track C · Hotel & Serviced Apartment AI Operations Playbook · Serviced Apartments chapter**

A hotel room is usually managed around a short stay. A serviced apartment is managed around a **living cycle**.

That difference changes the operating model. A long-stay resident may use a kitchen every day, accumulate maintenance needs over weeks, depend on recurring housekeeping rather than daily room servicing, receive corporate billing, require access continuity, consume utilities over a meaningful period and build an ongoing relationship with Front Office, Housekeeping, Engineering and Guest Relations. The operational question is no longer only, “Is the room ready tonight?” It becomes, “Can this apartment remain controlled, safe, functional and serviceable throughout the stay?”

AI can help teams consolidate this complexity. It can turn scattered work orders, housekeeping notes, resident requests, inspection records and utility observations into a structured management view. But it can also create risk if it turns a resident preference into an entitlement, labels a unit “ready” without a verified inspection, diagnoses a utility spike from one number, or invents a promised completion time.

The control principle for this chapter is:

> **AI may coordinate the evidence around the resident lifecycle. The property’s controlled systems, inspections and authorized people still determine readiness, entitlement, technical status, financial action and closure.**

The ten prompts follow the extended-stay operating cycle:

> **Prepare arrival → Verify apartment → Verify kitchen/assets → Plan recurring service → Communicate → Review utilities → Control move-in/out → Analyze complaints → Learn from defects → Personalize safely**

---

## 1. Why serviced-apartment operations need a different AI toolkit

Extended stay combines hotel service with elements of residential operations. The unit is not simply turned over and forgotten until departure. It remains an active operating environment for days, weeks or months. That creates more interfaces and more opportunities for small inconsistencies to become expensive failures.

A missing frying pan may be a minor amenity issue during a one-night hotel stay, but a material usability problem for a resident staying six weeks. A recurring air-conditioning complaint may look like three separate service tickets unless someone links the history. A housekeeping frequency may be written differently in the corporate agreement, the reservation notes and the resident communication. A move-out inspection may affect inventory, maintenance, access control and finance at the same time.

The purpose of AI here is therefore not “automation for automation’s sake.” It is **continuity across a longer operating timeline**.

## 2. HOTEL framework for extended stay

The common HOTEL model becomes especially useful because long-stay operations cross departments.

- **H — Hospitality role & human owner:** identify who owns the final decision—Operations, Front Office, Housekeeping, Engineering, Finance or Guest Relations.
- **O — Operational objective & context:** include the stage of stay, duration, unit type, corporate/direct/OTA context and service window.
- **T — Trusted inputs & sources of truth:** use PMS/CRS, approved contracts, inspections, CMMS, inventory, approved utility records, access-control logs and controlled communication history.
- **E — Expected output, exceptions & evidence:** require fact/request/unknown labels, named owners, deadlines, closure evidence and escalation triggers.
- **L — Limits, privacy & leadership approval:** prevent unsupported promises, privacy overreach, unauthorized charges, unverified apartment release and technical diagnosis by AI.

### Extended-stay source-of-truth matrix

| Operating question | Primary approved source | AI role |
|---|---|---|
| Is the stay confirmed? | PMS/CRS / approved booking record | summarize, flag conflicts |
| Is the apartment ready? | approved inspection + PMS status + blocking work-order status | consolidate; human releases |
| What housekeeping is included? | confirmed package/contract + approved service policy | compare; do not invent |
| Is an appliance defect closed? | CMMS/work order + verified completion/inspection | summarize; do not assume closure |
| What inventory belongs in the unit? | controlled inventory/PAR/asset standard | compare against inspection |
| Is a utility spike real? | verified meter/utility data + approved baseline | flag anomaly; do not diagnose cause |
| Is a resident preference confirmed? | documented resident preference/approved profile | use only explicit preferences |
| Can a charge/deposit be adjusted? | finance record + authority matrix/policy | prepare case; authorized human decides |
| Are keys/cards/access returned? | controlled access/key register | report recorded status only |

## 3. The extended-stay control loop

| Stage | Management question | Prompt |
|---|---|---|
| Pre-arrival | Are all long-stay dependencies ready? | 041 |
| Unit release | Is the apartment genuinely ready for occupancy? | 042 |
| Kitchen/assets | Are daily-living essentials present and functional? | 043 |
| Recurring service | What housekeeping plan is actually confirmed and feasible? | 044 |
| Communication | What can we safely tell the resident now? | 045 |
| Utilities | Is the observed usage unusual enough to investigate? | 046 |
| Move-in/out | What must be inspected, recorded and handed over? | 047 |
| Complaint | Is the issue isolated or a repeated service failure? | 048 |
| Defect learning | What does the unit’s history show? | 049 |
| Personalization | What useful service adjustments are safe and feasible? | 050 |

## 4. Fictional UAE 60-unit portfolio case

Continue with the fictional 60-unit UAE serviced-apartment portfolio used throughout this playbook. A corporate resident is scheduled to move into a one-bedroom apartment for 45 nights. The PMS shows a confirmed stay. Housekeeping has completed its clean. Engineering has one open work order relating to the dishwasher. The corporate rate includes housekeeping twice per week, but a copied reservation note says “daily cleaning requested.” A welcome message draft says the apartment will be ready at 14:00, while the latest inspection has not yet been signed off.

Separately, the previous resident reported intermittent cooling performance. The CMMS shows two related work orders during the last month, both marked closed, but the latest inspection note does not contain a temperature check. The new resident has also requested a quiet apartment and later housekeeping visits.

A weak AI assistant could easily produce: “Apartment ready at 14:00, daily housekeeping confirmed, dishwasher to be fixed shortly, quiet apartment allocated.” Every part sounds helpful. Several parts may be false.

A controlled output looks different:

| Item | Evidence | Classification | Required control |
|---|---|---|---|
| 45-night stay | PMS confirmed | CONFIRMED FACT | none |
| Apartment clean | HK inspection complete | CONFIRMED FACT | still requires full readiness release |
| Dishwasher | open work order | BLOCKING/REVIEW ITEM | Engineering verifies severity and closure |
| Daily housekeeping | request conflicts with twice-weekly entitlement | CONFLICT | Operations/Reservations verify entitlement |
| 14:00 readiness | message draft only | UNVERIFIED PROMISE | do not send until release confirmed |
| Cooling history | two closed work orders + incomplete latest evidence | REPEAT-RISK SIGNAL | Engineering/Quality review before release |
| Quiet unit | explicit preference | PREFERENCE, NOT ENTITLEMENT | consider if operationally feasible |
| Later cleaning | explicit preference | PREFERENCE | Housekeeping confirms feasible service window |

AI has not solved the case. It has made the case manageable.

## 5. Apartment readiness is more than housekeeping status

A long-stay apartment can be visibly clean and still not be operationally ready. Readiness may include:

- housekeeping completion;
- essential appliance functionality;
- known maintenance defects and risk classification;
- hot water/cooling/power availability where part of the inspection standard;
- inventory and kitchen essentials;
- key/card/access readiness;
- approved amenities and long-stay inclusions;
- unresolved safety/security observations;
- prior-defect history relevant to release;
- evidence that blocking work is actually closed.

Prompt 042 therefore does not answer “ready/not ready” from one dataset. It builds a **release control table** and routes the final release to the accountable property role.

## 6. Recurring housekeeping: entitlement, preference and capacity

Long-stay housekeeping is a classic source of guest dissatisfaction because three different concepts get mixed together:

1. **Entitlement** — what the confirmed package or contract includes.
2. **Preference** — when or how the resident would prefer service.
3. **Capacity** — what the operation can deliver within the approved service model.

AI is useful for building a service calendar and identifying conflicts, but it should not convert “I prefer cleaning every day” into “daily housekeeping confirmed.” Prompt 044 therefore keeps entitlement separate from preference and requires Housekeeping to validate the actual schedule.

## 7. Kitchens, appliances and the lived experience

In a traditional hotel, a failed appliance may affect a limited set of amenities. In a serviced apartment, appliances are part of the resident’s daily routine. Refrigerator, washing machine, hob, microwave, kettle, dishwasher and other unit-specific equipment may directly affect the usability of the product.

Prompt 043 turns the approved property standard into a controlled inspection view. It should never invent what the apartment “should” contain from generic hotel knowledge. The property’s approved unit standard, inventory/PAR list and asset records remain authoritative.

## 8. Utility anomalies: detect before diagnosing

AI can be valuable for spotting unusual electricity, water or cooling usage, especially across a portfolio. But an anomaly is not a diagnosis.

A high reading might reflect occupancy, a meter issue, weather conditions, maintenance activity, a leak, equipment inefficiency, a billing-period mismatch or another cause. Without verified context, the model should produce **hypotheses and a verification plan**, not a claim such as “the air conditioner is faulty.”

A simple internal comparison may use:

`Observed consumption – approved baseline = variance`

and

`Variance / approved baseline × 100 = variance %`

But the baseline must be defined by the property. The prompt should not invent a benchmark or declare a threshold abnormal without an approved rule.

## 9. Move-in and move-out as controlled handovers

Move-in and move-out should be treated like operational handovers rather than informal checklists. The process may touch:

- apartment condition;
- inventory and assets;
- keys/cards/access;
- open defects;
- approved billing/deposit workflow;
- resident claims or observations;
- housekeeping status;
- engineering follow-up;
- final ownership of unresolved items.

Prompt 047 structures the evidence but does not decide liability, approve charges or determine whether a deposit should be retained. Those decisions stay with the authorized human and finance/policy workflow.

## 10. Complaint analysis across a long stay

Extended-stay complaints often need longitudinal analysis. A resident may report “the AC keeps failing,” while the operations system contains several individually closed tickets. Looking at each ticket alone can hide the repeat pattern.

Prompt 048 reconstructs the chronology and asks whether the evidence shows recurrence, delayed response, incomplete closure, cross-department dependency or communication failure. It still avoids declaring root cause without validation.

This is where the toolkit connects strongly to the later **Guest Complaint & Service Recovery**, **Quality Audit**, **SOP & Process Design** and **Lean Six Sigma** chapters.

## 11. Defect history as a quality signal

Prompt 049 is designed to stop teams from repeatedly solving the same symptom without seeing the unit history. The useful output is not simply “five defects.” It is a pattern view:

- category;
- asset/unit;
- dates;
- closure evidence;
- recurrence interval;
- resident impact;
- repeated temporary fix;
- unresolved diagnostic questions.

That provides a better starting point for Engineering and Quality to decide whether a deeper root-cause investigation is justified.

## 12. Personalization without profiling

A long stay creates more opportunities to personalize service, but also more privacy risk. Personalization should come from **explicit, operationally relevant preferences**, not speculative inference.

Safe examples may include a resident’s explicitly stated preferred housekeeping window, pillow request, communication language or previously requested service—provided the property is authorized to retain and use that preference.

Unsafe behavior includes inferring religion, health status, relationship status, income, nationality-based preferences or other sensitive traits from names, behavior or external data. Prompt 050 therefore separates confirmed preference from optional service suggestion and requires feasibility plus privacy review.

## 13. AI authority matrix for serviced apartments

| AI-supported task | AI may | AI must not | Human authority |
|---|---|---|---|
| Arrival planning | consolidate confirmed dependencies | promise readiness | Operations/Front Office |
| Apartment review | expose blocking items | release unit | Duty/Operations manager |
| Housekeeping plan | draft schedule from entitlements/preferences | change entitlement | Housekeeping/Operations |
| Resident message | draft from verified facts | invent timing/waiver/benefit | Front Office/Guest Relations |
| Utility review | flag anomaly/hypotheses | diagnose fault or accuse resident | Engineering/Finance/Sustainability |
| Move-out | organize condition/inventory evidence | assign liability/charge | authorized Ops/Finance |
| Complaint analysis | build chronology/pattern | approve compensation | Duty/Guest Relations manager |
| Defect history | summarize recurrence | close work order | Engineering |
| Personalization | suggest from explicit preferences | infer sensitive traits | Guest Relations/Operations |

## 14. KPI and management dashboard

Useful measures should come from verified internal data. Examples include:

| KPI | What it can reveal |
|---|---|
| Apartments with unresolved blocking item before planned arrival | readiness risk |
| Long-stay service-plan conflicts detected pre-arrival | entitlement-control quality |
| Repeat defects per unit/asset category | reliability opportunity |
| Work orders reopened within defined period | closure quality |
| Housekeeping services missed/rescheduled | service consistency |
| Extended-stay complaints by recurring category | resident experience trend |
| Move-out exceptions without named owner | handover/control weakness |
| Utility anomalies investigated to verified outcome | monitoring discipline |
| Personalization requests fulfilled from explicit preference | service responsiveness |

Do not invent target percentages. Establish a baseline, define the operational definition and then improve against the property’s verified data.

## 15. Lean Six Sigma application

Extended-stay operations are well suited to process improvement because the longer guest lifecycle reveals repeated defects.

**Define:** choose one measurable issue, such as repeat appliance defects, missed housekeeping service or apartment-release exceptions.

**Measure:** use a consistent definition and verified system records.

**Analyze:** stratify by apartment, asset, defect category, contractor, shift, stay length or process stage. Treat AI-generated themes as hypotheses, not causes.

**Improve:** redesign inspection, preventive maintenance, service scheduling, escalation, stock/PAR or communication controls.

**Control:** monitor the chosen measure and require evidence of closure.

AI can accelerate classification and pattern detection; the improvement owner validates causality.

## 16. 30-day implementation plan

**Days 1–7 — Define the extended-stay sources of truth.** Map PMS, CMMS, housekeeping inspection, inventory/PAR, access-control, utility and approved contract/policy sources. Define who can release a unit and who can approve financial exceptions.

**Days 8–14 — Pilot readiness and recurring service.** Start with Prompts 041–044. Compare AI output against actual supervisor review and record false flags, missed dependencies and unclear source fields.

**Days 15–21 — Add utility, complaint and defect intelligence.** Pilot Prompts 046, 048 and 049 with Engineering/Quality review. Do not allow AI-generated cause statements to become work-order diagnoses without verification.

**Days 22–30 — Standardize move-in/out and personalization controls.** Introduce Prompts 047 and 050, finalize privacy rules, connect the workflow to SOPs and define dashboard measures.

## 17. Before → Action → After → AED protected

**Before:** a 45-night resident is due to arrive. Housekeeping is complete, but a dishwasher work order remains open, the cooling history shows repeat tickets, housekeeping frequency is unclear and an unverified 14:00 promise appears in a draft message.

**Action:** the Operations team uses the toolkit to create one readiness view, separate confirmed entitlements from preferences, identify the blocking/verification queue, review defect history and assign owners before guest communication is sent.

**After:** the resident-facing message reflects verified facts, Engineering and Housekeeping own their open dependencies, and the apartment is released only through the approved human process.

**AED saved/protected:** calculate only from verified avoided relocation cost, refunds/compensation, emergency maintenance, revenue loss, repeat labor, utility waste or inventory loss. Do not publish an invented savings number.

## 18. Cross-website knowledge connections

This chapter should not sit alone. On the website, connect it contextually to:

- **Reservations AI Toolkit** — booking terms, long-stay inclusions and corporate reservations;
- **Front Office AI Toolkit** — arrival, access, guest requests and handover;
- **Housekeeping Management AI Toolkit** — recurring cleaning, linen and inspection control;
- **Engineering & Maintenance AI Toolkit** — defects, work orders and closure evidence;
- **Predictive Maintenance AI Toolkit** — recurring asset patterns;
- **Guest Experience AI Toolkit** and **Guest Complaint & Service Recovery AI Toolkit** — resident communication, complaints and recovery;
- **Hotel SOP & Process Design AI Toolkit** plus existing SOP/RACI/escalation articles — authority and workflow design;
- **Hotel ESG & Sustainability** and **Energy & Utility Management** — consumption, waste and utility anomaly review;
- **Inventory & PAR Management** — kitchenware, amenities, linen and asset control;
- **Finance & Cost Control** — deposits, charges and cost-of-defect evidence;
- relevant **tourism transfer/dispatch** content when airport pickup or resident movement is part of the stay;
- relevant **MICE/corporate movement** content when extended-stay groups or project teams create coordinated arrival/departure requirements.

The linking rule is reciprocal: when these connected articles are published or revised, they should link back to this extended-stay chapter where the reader needs the serviced-apartment operating view.

## 19. Extended-stay manager checklist

Before operational use, confirm that:

- apartment release authority is documented;
- housekeeping entitlement is separated from preference;
- open work orders cannot be hidden by a “clean” room status;
- asset/inventory standards are controlled documents;
- utility anomalies are investigated before cause is assigned;
- move-in/out records distinguish observation from liability decision;
- resident messages contain only verified promises;
- complaint analysis includes the full stay chronology where relevant;
- repeat defects are visible across work orders;
- sensitive personal data is minimized;
- personalization uses explicit preferences rather than inferred traits;
- every open item has an owner and closure evidence.

---

# The 10 copy-ready Hotel Apartment & Extended-Stay AI prompts

## Prompt 041 — Extended-Stay Arrival Planner

**Risk:** Medium  
**Human owner:** Hotel Apartment Operations Manager / Front Office Supervisor  
**When to use:** Before a long-stay or corporate resident arrival, consolidate readiness across reservation, apartment condition, access, housekeeping, maintenance, billing and documented service requirements.

### Why this prompt matters

Before a long-stay or corporate resident arrival, consolidate readiness across reservation, apartment condition, access, housekeeping, maintenance, billing and documented service requirements. In an extended-stay environment, the same issue can affect several departments over a longer timeline. This prompt forces the AI to preserve evidence, expose uncertainty and route the final action to the accountable human rather than silently converting an observation into an operational decision.

### Copy-ready prompt

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as an extended-stay hotel and serviced-apartment operations support analyst.
Supported role: [Hotel Apartment Operations / Front Office / Housekeeping / Engineering / Guest Relations as applicable]
Accountable human owner: Hotel Apartment Operations Manager / Front Office Supervisor

O — OPERATIONAL OBJECTIVE & CONTEXT
Before a long-stay or corporate resident arrival, consolidate readiness across reservation, apartment condition, access, housekeeping, maintenance, billing and documented service requirements.
Property: [serviced apartment / hotel apartment / extended-stay property, location]
Unit/stay context: [unit type, stay stage, stay duration, segment, relevant dates]
Decision deadline or service window: [time/date if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved records. Depending on the task, valid sources may include PMS/CRS, approved booking or corporate terms, controlled SOPs, housekeeping inspections, CMMS/work orders, inventory/asset records, approved utility or meter records, access-control records, finance-status indicators and documented resident communications.
Required inputs:
- confirmed reservation/PMS record
- approved corporate or booking terms
- apartment readiness inspection
- open CMMS/work-order status
- housekeeping readiness record
- access/key/card status
- approved billing/payment-status indicator
- confirmed transport or arrival details if applicable

If a critical source is missing, stale, contradictory or unverified, label the item UNVERIFIED and state exactly which system or accountable owner must confirm it. Do not infer entitlement, apartment readiness, maintenance completion, financial status, utility cause, resident preference or service availability from incomplete evidence.
Minimize personal data. Do not reproduce passport/ID numbers, payment-card data, credentials, access codes, medical information or unrelated sensitive resident/employee notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Produce:
- arrival readiness dashboard
- confirmed facts versus requests
- open dependency list
- owner/deadline/escalation table

Separate CONFIRMED FACT, REQUEST/CLAIM, UNVERIFIED/CONFLICT and RECOMMENDED ACTION. For every open operational item show: owner, next action, checkpoint/deadline, evidence required for closure and escalation trigger.
Where patterns or causes are suggested, label them HYPOTHESIS until verified by the relevant department. Preserve chronology and source references when provided.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently release an apartment, change room/unit status, approve a refund/waiver/charge, alter a reservation, promise maintenance completion, change housekeeping entitlement, diagnose a technical cause, assign liability, or create a resident benefit. Do not treat AI-generated language as proof that work was completed.
Risk classification: Medium.
Final operational action requires verification/approval by: Hotel Apartment Operations Manager / Front Office Supervisor.
AI output is decision support and a draft—not the PMS, CMMS, inspection record, financial record or authorization.
```

### Human verification

Before using the output operationally, verify the current system-of-record data, resolve any UNVERIFIED/CONFLICT items, confirm authority for the intended action and record the final decision in the approved hotel system.

## Prompt 042 — Apartment Readiness Review

**Risk:** High  
**Human owner:** Hotel Apartment Operations Manager / Duty Manager  
**When to use:** Review whether an apartment is operationally ready for occupancy without treating an AI summary as permission to release the unit.

### Why this prompt matters

Review whether an apartment is operationally ready for occupancy without treating an AI summary as permission to release the unit. In an extended-stay environment, the same issue can affect several departments over a longer timeline. This prompt forces the AI to preserve evidence, expose uncertainty and route the final action to the accountable human rather than silently converting an observation into an operational decision.

### Copy-ready prompt

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as an extended-stay hotel and serviced-apartment operations support analyst.
Supported role: [Hotel Apartment Operations / Front Office / Housekeeping / Engineering / Guest Relations as applicable]
Accountable human owner: Hotel Apartment Operations Manager / Duty Manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Review whether an apartment is operationally ready for occupancy without treating an AI summary as permission to release the unit.
Property: [serviced apartment / hotel apartment / extended-stay property, location]
Unit/stay context: [unit type, stay stage, stay duration, segment, relevant dates]
Decision deadline or service window: [time/date if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved records. Depending on the task, valid sources may include PMS/CRS, approved booking or corporate terms, controlled SOPs, housekeeping inspections, CMMS/work orders, inventory/asset records, approved utility or meter records, access-control records, finance-status indicators and documented resident communications.
Required inputs:
- PMS room/unit status
- housekeeping inspection
- engineering/CMMS status
- inventory/amenity checklist
- safety/security checklist where approved
- photographic or inspection evidence where permitted

If a critical source is missing, stale, contradictory or unverified, label the item UNVERIFIED and state exactly which system or accountable owner must confirm it. Do not infer entitlement, apartment readiness, maintenance completion, financial status, utility cause, resident preference or service availability from incomplete evidence.
Minimize personal data. Do not reproduce passport/ID numbers, payment-card data, credentials, access codes, medical information or unrelated sensitive resident/employee notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Produce:
- readiness control table
- blocking defects
- non-blocking observations
- verification and release queue

Separate CONFIRMED FACT, REQUEST/CLAIM, UNVERIFIED/CONFLICT and RECOMMENDED ACTION. For every open operational item show: owner, next action, checkpoint/deadline, evidence required for closure and escalation trigger.
Where patterns or causes are suggested, label them HYPOTHESIS until verified by the relevant department. Preserve chronology and source references when provided.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently release an apartment, change room/unit status, approve a refund/waiver/charge, alter a reservation, promise maintenance completion, change housekeeping entitlement, diagnose a technical cause, assign liability, or create a resident benefit. Do not treat AI-generated language as proof that work was completed.
Risk classification: High.
Final operational action requires verification/approval by: Hotel Apartment Operations Manager / Duty Manager.
AI output is decision support and a draft—not the PMS, CMMS, inspection record, financial record or authorization.
```

### Human verification

Before using the output operationally, verify the current system-of-record data, resolve any UNVERIFIED/CONFLICT items, confirm authority for the intended action and record the final decision in the approved hotel system.

## Prompt 043 — Kitchen and Appliance Checklist

**Risk:** Medium  
**Human owner:** Housekeeping Supervisor / Engineering Supervisor  
**When to use:** Create or review a kitchen and appliance readiness checklist for a serviced apartment using approved property standards and recorded inspection evidence.

### Why this prompt matters

Create or review a kitchen and appliance readiness checklist for a serviced apartment using approved property standards and recorded inspection evidence. In an extended-stay environment, the same issue can affect several departments over a longer timeline. This prompt forces the AI to preserve evidence, expose uncertainty and route the final action to the accountable human rather than silently converting an observation into an operational decision.

### Copy-ready prompt

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as an extended-stay hotel and serviced-apartment operations support analyst.
Supported role: [Hotel Apartment Operations / Front Office / Housekeeping / Engineering / Guest Relations as applicable]
Accountable human owner: Housekeeping Supervisor / Engineering Supervisor

O — OPERATIONAL OBJECTIVE & CONTEXT
Create or review a kitchen and appliance readiness checklist for a serviced apartment using approved property standards and recorded inspection evidence.
Property: [serviced apartment / hotel apartment / extended-stay property, location]
Unit/stay context: [unit type, stay stage, stay duration, segment, relevant dates]
Decision deadline or service window: [time/date if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved records. Depending on the task, valid sources may include PMS/CRS, approved booking or corporate terms, controlled SOPs, housekeeping inspections, CMMS/work orders, inventory/asset records, approved utility or meter records, access-control records, finance-status indicators and documented resident communications.
Required inputs:
- approved apartment standard
- asset/appliance list
- housekeeping checklist
- engineering inspection or work-order data
- inventory/par list

If a critical source is missing, stale, contradictory or unverified, label the item UNVERIFIED and state exactly which system or accountable owner must confirm it. Do not infer entitlement, apartment readiness, maintenance completion, financial status, utility cause, resident preference or service availability from incomplete evidence.
Minimize personal data. Do not reproduce passport/ID numbers, payment-card data, credentials, access codes, medical information or unrelated sensitive resident/employee notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Produce:
- kitchen/appliance checklist
- missing or defective item list
- ownership by Housekeeping/Engineering/Inventory
- closure evidence requirements

Separate CONFIRMED FACT, REQUEST/CLAIM, UNVERIFIED/CONFLICT and RECOMMENDED ACTION. For every open operational item show: owner, next action, checkpoint/deadline, evidence required for closure and escalation trigger.
Where patterns or causes are suggested, label them HYPOTHESIS until verified by the relevant department. Preserve chronology and source references when provided.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently release an apartment, change room/unit status, approve a refund/waiver/charge, alter a reservation, promise maintenance completion, change housekeeping entitlement, diagnose a technical cause, assign liability, or create a resident benefit. Do not treat AI-generated language as proof that work was completed.
Risk classification: Medium.
Final operational action requires verification/approval by: Housekeeping Supervisor / Engineering Supervisor.
AI output is decision support and a draft—not the PMS, CMMS, inspection record, financial record or authorization.
```

### Human verification

Before using the output operationally, verify the current system-of-record data, resolve any UNVERIFIED/CONFLICT items, confirm authority for the intended action and record the final decision in the approved hotel system.

## Prompt 044 — Long-Stay Housekeeping Planner

**Risk:** Medium  
**Human owner:** Housekeeping Manager / Hotel Apartment Operations Manager  
**When to use:** Prepare a long-stay housekeeping service plan that respects the confirmed service package, resident preferences, access constraints and operational capacity.

### Why this prompt matters

Prepare a long-stay housekeeping service plan that respects the confirmed service package, resident preferences, access constraints and operational capacity. In an extended-stay environment, the same issue can affect several departments over a longer timeline. This prompt forces the AI to preserve evidence, expose uncertainty and route the final action to the accountable human rather than silently converting an observation into an operational decision.

### Copy-ready prompt

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as an extended-stay hotel and serviced-apartment operations support analyst.
Supported role: [Hotel Apartment Operations / Front Office / Housekeeping / Engineering / Guest Relations as applicable]
Accountable human owner: Housekeeping Manager / Hotel Apartment Operations Manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Prepare a long-stay housekeeping service plan that respects the confirmed service package, resident preferences, access constraints and operational capacity.
Property: [serviced apartment / hotel apartment / extended-stay property, location]
Unit/stay context: [unit type, stay stage, stay duration, segment, relevant dates]
Decision deadline or service window: [time/date if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved records. Depending on the task, valid sources may include PMS/CRS, approved booking or corporate terms, controlled SOPs, housekeeping inspections, CMMS/work orders, inventory/asset records, approved utility or meter records, access-control records, finance-status indicators and documented resident communications.
Required inputs:
- confirmed length of stay
- approved housekeeping entitlement/frequency
- resident preference record
- do-not-disturb/access restrictions
- housekeeping roster/capacity
- linen/amenity standards

If a critical source is missing, stale, contradictory or unverified, label the item UNVERIFIED and state exactly which system or accountable owner must confirm it. Do not infer entitlement, apartment readiness, maintenance completion, financial status, utility cause, resident preference or service availability from incomplete evidence.
Minimize personal data. Do not reproduce passport/ID numbers, payment-card data, credentials, access codes, medical information or unrelated sensitive resident/employee notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Produce:
- service calendar
- confirmed versus requested services
- capacity conflicts
- resident communication points and escalation triggers

Separate CONFIRMED FACT, REQUEST/CLAIM, UNVERIFIED/CONFLICT and RECOMMENDED ACTION. For every open operational item show: owner, next action, checkpoint/deadline, evidence required for closure and escalation trigger.
Where patterns or causes are suggested, label them HYPOTHESIS until verified by the relevant department. Preserve chronology and source references when provided.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently release an apartment, change room/unit status, approve a refund/waiver/charge, alter a reservation, promise maintenance completion, change housekeeping entitlement, diagnose a technical cause, assign liability, or create a resident benefit. Do not treat AI-generated language as proof that work was completed.
Risk classification: Medium.
Final operational action requires verification/approval by: Housekeeping Manager / Hotel Apartment Operations Manager.
AI output is decision support and a draft—not the PMS, CMMS, inspection record, financial record or authorization.
```

### Human verification

Before using the output operationally, verify the current system-of-record data, resolve any UNVERIFIED/CONFLICT items, confirm authority for the intended action and record the final decision in the approved hotel system.

## Prompt 045 — Resident Communication Draft

**Risk:** Medium  
**Human owner:** Front Office / Guest Relations Supervisor  
**When to use:** Draft clear resident communication for an extended stay using confirmed operational facts while avoiding unsupported promises about service, charges, access, maintenance or timing.

### Why this prompt matters

Draft clear resident communication for an extended stay using confirmed operational facts while avoiding unsupported promises about service, charges, access, maintenance or timing. In an extended-stay environment, the same issue can affect several departments over a longer timeline. This prompt forces the AI to preserve evidence, expose uncertainty and route the final action to the accountable human rather than silently converting an observation into an operational decision.

### Copy-ready prompt

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as an extended-stay hotel and serviced-apartment operations support analyst.
Supported role: [Hotel Apartment Operations / Front Office / Housekeeping / Engineering / Guest Relations as applicable]
Accountable human owner: Front Office / Guest Relations Supervisor

O — OPERATIONAL OBJECTIVE & CONTEXT
Draft clear resident communication for an extended stay using confirmed operational facts while avoiding unsupported promises about service, charges, access, maintenance or timing.
Property: [serviced apartment / hotel apartment / extended-stay property, location]
Unit/stay context: [unit type, stay stage, stay duration, segment, relevant dates]
Decision deadline or service window: [time/date if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved records. Depending on the task, valid sources may include PMS/CRS, approved booking or corporate terms, controlled SOPs, housekeeping inspections, CMMS/work orders, inventory/asset records, approved utility or meter records, access-control records, finance-status indicators and documented resident communications.
Required inputs:
- verified resident case summary
- approved policy/SOP
- confirmed service status
- authorized decision/offer if any
- approved communication tone/language

If a critical source is missing, stale, contradictory or unverified, label the item UNVERIFIED and state exactly which system or accountable owner must confirm it. Do not infer entitlement, apartment readiness, maintenance completion, financial status, utility cause, resident preference or service availability from incomplete evidence.
Minimize personal data. Do not reproduce passport/ID numbers, payment-card data, credentials, access codes, medical information or unrelated sensitive resident/employee notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Produce:
- resident-ready draft
- facts used
- unverified items withheld
- human review checklist

Separate CONFIRMED FACT, REQUEST/CLAIM, UNVERIFIED/CONFLICT and RECOMMENDED ACTION. For every open operational item show: owner, next action, checkpoint/deadline, evidence required for closure and escalation trigger.
Where patterns or causes are suggested, label them HYPOTHESIS until verified by the relevant department. Preserve chronology and source references when provided.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently release an apartment, change room/unit status, approve a refund/waiver/charge, alter a reservation, promise maintenance completion, change housekeeping entitlement, diagnose a technical cause, assign liability, or create a resident benefit. Do not treat AI-generated language as proof that work was completed.
Risk classification: Medium.
Final operational action requires verification/approval by: Front Office / Guest Relations Supervisor.
AI output is decision support and a draft—not the PMS, CMMS, inspection record, financial record or authorization.
```

### Human verification

Before using the output operationally, verify the current system-of-record data, resolve any UNVERIFIED/CONFLICT items, confirm authority for the intended action and record the final decision in the approved hotel system.

## Prompt 046 — Utility Anomaly Review

**Risk:** High  
**Human owner:** Engineering Manager / Finance or Sustainability Owner  
**When to use:** Review a possible electricity, water or cooling-usage anomaly in a serviced apartment and prepare a fact-based investigation plan without diagnosing cause from consumption data alone.

### Why this prompt matters

Review a possible electricity, water or cooling-usage anomaly in a serviced apartment and prepare a fact-based investigation plan without diagnosing cause from consumption data alone. In an extended-stay environment, the same issue can affect several departments over a longer timeline. This prompt forces the AI to preserve evidence, expose uncertainty and route the final action to the accountable human rather than silently converting an observation into an operational decision.

### Copy-ready prompt

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as an extended-stay hotel and serviced-apartment operations support analyst.
Supported role: [Hotel Apartment Operations / Front Office / Housekeeping / Engineering / Guest Relations as applicable]
Accountable human owner: Engineering Manager / Finance or Sustainability Owner

O — OPERATIONAL OBJECTIVE & CONTEXT
Review a possible electricity, water or cooling-usage anomaly in a serviced apartment and prepare a fact-based investigation plan without diagnosing cause from consumption data alone.
Property: [serviced apartment / hotel apartment / extended-stay property, location]
Unit/stay context: [unit type, stay stage, stay duration, segment, relevant dates]
Decision deadline or service window: [time/date if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved records. Depending on the task, valid sources may include PMS/CRS, approved booking or corporate terms, controlled SOPs, housekeeping inspections, CMMS/work orders, inventory/asset records, approved utility or meter records, access-control records, finance-status indicators and documented resident communications.
Required inputs:
- verified meter/utility readings
- billing period and unit identifiers
- occupancy/stay dates where operationally necessary
- maintenance/work-order history
- known shutdown/maintenance events
- approved baseline/comparison method

If a critical source is missing, stale, contradictory or unverified, label the item UNVERIFIED and state exactly which system or accountable owner must confirm it. Do not infer entitlement, apartment readiness, maintenance completion, financial status, utility cause, resident preference or service availability from incomplete evidence.
Minimize personal data. Do not reproduce passport/ID numbers, payment-card data, credentials, access codes, medical information or unrelated sensitive resident/employee notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Produce:
- anomaly summary
- data-quality checks
- possible hypotheses clearly labeled
- verification plan and escalation owners

Separate CONFIRMED FACT, REQUEST/CLAIM, UNVERIFIED/CONFLICT and RECOMMENDED ACTION. For every open operational item show: owner, next action, checkpoint/deadline, evidence required for closure and escalation trigger.
Where patterns or causes are suggested, label them HYPOTHESIS until verified by the relevant department. Preserve chronology and source references when provided.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently release an apartment, change room/unit status, approve a refund/waiver/charge, alter a reservation, promise maintenance completion, change housekeeping entitlement, diagnose a technical cause, assign liability, or create a resident benefit. Do not treat AI-generated language as proof that work was completed.
Risk classification: High.
Final operational action requires verification/approval by: Engineering Manager / Finance or Sustainability Owner.
AI output is decision support and a draft—not the PMS, CMMS, inspection record, financial record or authorization.
```

### Human verification

Before using the output operationally, verify the current system-of-record data, resolve any UNVERIFIED/CONFLICT items, confirm authority for the intended action and record the final decision in the approved hotel system.

## Prompt 047 — Move-In / Move-Out Checklist

**Risk:** High  
**Human owner:** Hotel Apartment Operations Manager / Duty Manager  
**When to use:** Build a controlled move-in or move-out checklist for an extended-stay apartment covering condition, inventory, access, billing handoff, keys/cards and unresolved operational items.

### Why this prompt matters

Build a controlled move-in or move-out checklist for an extended-stay apartment covering condition, inventory, access, billing handoff, keys/cards and unresolved operational items. In an extended-stay environment, the same issue can affect several departments over a longer timeline. This prompt forces the AI to preserve evidence, expose uncertainty and route the final action to the accountable human rather than silently converting an observation into an operational decision.

### Copy-ready prompt

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as an extended-stay hotel and serviced-apartment operations support analyst.
Supported role: [Hotel Apartment Operations / Front Office / Housekeeping / Engineering / Guest Relations as applicable]
Accountable human owner: Hotel Apartment Operations Manager / Duty Manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Build a controlled move-in or move-out checklist for an extended-stay apartment covering condition, inventory, access, billing handoff, keys/cards and unresolved operational items.
Property: [serviced apartment / hotel apartment / extended-stay property, location]
Unit/stay context: [unit type, stay stage, stay duration, segment, relevant dates]
Decision deadline or service window: [time/date if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved records. Depending on the task, valid sources may include PMS/CRS, approved booking or corporate terms, controlled SOPs, housekeeping inspections, CMMS/work orders, inventory/asset records, approved utility or meter records, access-control records, finance-status indicators and documented resident communications.
Required inputs:
- confirmed booking/stay dates
- approved condition checklist
- inventory/asset list
- access/key/card register
- open maintenance items
- approved billing or deposit workflow
- documented exceptions

If a critical source is missing, stale, contradictory or unverified, label the item UNVERIFIED and state exactly which system or accountable owner must confirm it. Do not infer entitlement, apartment readiness, maintenance completion, financial status, utility cause, resident preference or service availability from incomplete evidence.
Minimize personal data. Do not reproduce passport/ID numbers, payment-card data, credentials, access codes, medical information or unrelated sensitive resident/employee notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Produce:
- move-in/out control checklist
- condition/inventory exceptions
- open financial/operational dependencies
- handover and closure evidence

Separate CONFIRMED FACT, REQUEST/CLAIM, UNVERIFIED/CONFLICT and RECOMMENDED ACTION. For every open operational item show: owner, next action, checkpoint/deadline, evidence required for closure and escalation trigger.
Where patterns or causes are suggested, label them HYPOTHESIS until verified by the relevant department. Preserve chronology and source references when provided.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently release an apartment, change room/unit status, approve a refund/waiver/charge, alter a reservation, promise maintenance completion, change housekeeping entitlement, diagnose a technical cause, assign liability, or create a resident benefit. Do not treat AI-generated language as proof that work was completed.
Risk classification: High.
Final operational action requires verification/approval by: Hotel Apartment Operations Manager / Duty Manager.
AI output is decision support and a draft—not the PMS, CMMS, inspection record, financial record or authorization.
```

### Human verification

Before using the output operationally, verify the current system-of-record data, resolve any UNVERIFIED/CONFLICT items, confirm authority for the intended action and record the final decision in the approved hotel system.

## Prompt 048 — Extended-Stay Complaint Analyzer

**Risk:** High  
**Human owner:** Guest Relations Manager / Duty Manager  
**When to use:** Analyze an extended-stay complaint chronologically, distinguish recurring failure from isolated incident, and prepare evidence, recovery options and root-cause questions for authorized review.

### Why this prompt matters

Analyze an extended-stay complaint chronologically, distinguish recurring failure from isolated incident, and prepare evidence, recovery options and root-cause questions for authorized review. In an extended-stay environment, the same issue can affect several departments over a longer timeline. This prompt forces the AI to preserve evidence, expose uncertainty and route the final action to the accountable human rather than silently converting an observation into an operational decision.

### Copy-ready prompt

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as an extended-stay hotel and serviced-apartment operations support analyst.
Supported role: [Hotel Apartment Operations / Front Office / Housekeeping / Engineering / Guest Relations as applicable]
Accountable human owner: Guest Relations Manager / Duty Manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Analyze an extended-stay complaint chronologically, distinguish recurring failure from isolated incident, and prepare evidence, recovery options and root-cause questions for authorized review.
Property: [serviced apartment / hotel apartment / extended-stay property, location]
Unit/stay context: [unit type, stay stage, stay duration, segment, relevant dates]
Decision deadline or service window: [time/date if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved records. Depending on the task, valid sources may include PMS/CRS, approved booking or corporate terms, controlled SOPs, housekeeping inspections, CMMS/work orders, inventory/asset records, approved utility or meter records, access-control records, finance-status indicators and documented resident communications.
Required inputs:
- complaint/contact log
- work orders/service requests
- housekeeping/service history
- approved compensation/authority matrix
- resident communication record
- relevant SOP/SLA

If a critical source is missing, stale, contradictory or unverified, label the item UNVERIFIED and state exactly which system or accountable owner must confirm it. Do not infer entitlement, apartment readiness, maintenance completion, financial status, utility cause, resident preference or service availability from incomplete evidence.
Minimize personal data. Do not reproduce passport/ID numbers, payment-card data, credentials, access codes, medical information or unrelated sensitive resident/employee notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Produce:
- complaint chronology
- facts versus claims/unknowns
- repeat-failure pattern
- recovery/escalation brief without unauthorized compensation

Separate CONFIRMED FACT, REQUEST/CLAIM, UNVERIFIED/CONFLICT and RECOMMENDED ACTION. For every open operational item show: owner, next action, checkpoint/deadline, evidence required for closure and escalation trigger.
Where patterns or causes are suggested, label them HYPOTHESIS until verified by the relevant department. Preserve chronology and source references when provided.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently release an apartment, change room/unit status, approve a refund/waiver/charge, alter a reservation, promise maintenance completion, change housekeeping entitlement, diagnose a technical cause, assign liability, or create a resident benefit. Do not treat AI-generated language as proof that work was completed.
Risk classification: High.
Final operational action requires verification/approval by: Guest Relations Manager / Duty Manager.
AI output is decision support and a draft—not the PMS, CMMS, inspection record, financial record or authorization.
```

### Human verification

Before using the output operationally, verify the current system-of-record data, resolve any UNVERIFIED/CONFLICT items, confirm authority for the intended action and record the final decision in the approved hotel system.

## Prompt 049 — Apartment Defect History Summary

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

## Prompt 050 — Long-Stay Service Personalization

**Risk:** Medium  
**Human owner:** Guest Relations / Hotel Apartment Operations Manager  
**When to use:** Identify safe, operationally feasible personalization opportunities for a long-stay resident using explicit preferences and approved service options, without inferring sensitive traits or creating entitlements.

### Why this prompt matters

Identify safe, operationally feasible personalization opportunities for a long-stay resident using explicit preferences and approved service options, without inferring sensitive traits or creating entitlements. In an extended-stay environment, the same issue can affect several departments over a longer timeline. This prompt forces the AI to preserve evidence, expose uncertainty and route the final action to the accountable human rather than silently converting an observation into an operational decision.

### Copy-ready prompt

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as an extended-stay hotel and serviced-apartment operations support analyst.
Supported role: [Hotel Apartment Operations / Front Office / Housekeeping / Engineering / Guest Relations as applicable]
Accountable human owner: Guest Relations / Hotel Apartment Operations Manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Identify safe, operationally feasible personalization opportunities for a long-stay resident using explicit preferences and approved service options, without inferring sensitive traits or creating entitlements.
Property: [serviced apartment / hotel apartment / extended-stay property, location]
Unit/stay context: [unit type, stay stage, stay duration, segment, relevant dates]
Decision deadline or service window: [time/date if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved records. Depending on the task, valid sources may include PMS/CRS, approved booking or corporate terms, controlled SOPs, housekeeping inspections, CMMS/work orders, inventory/asset records, approved utility or meter records, access-control records, finance-status indicators and documented resident communications.
Required inputs:
- confirmed stay profile and duration
- explicitly recorded resident preferences
- approved service catalogue/benefits
- service history
- operational constraints
- authorized loyalty/corporate benefits if applicable

If a critical source is missing, stale, contradictory or unverified, label the item UNVERIFIED and state exactly which system or accountable owner must confirm it. Do not infer entitlement, apartment readiness, maintenance completion, financial status, utility cause, resident preference or service availability from incomplete evidence.
Minimize personal data. Do not reproduce passport/ID numbers, payment-card data, credentials, access codes, medical information or unrelated sensitive resident/employee notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Produce:
- personalization opportunity list
- confirmed preference versus suggestion labels
- feasibility/owner table
- privacy and approval checks

Separate CONFIRMED FACT, REQUEST/CLAIM, UNVERIFIED/CONFLICT and RECOMMENDED ACTION. For every open operational item show: owner, next action, checkpoint/deadline, evidence required for closure and escalation trigger.
Where patterns or causes are suggested, label them HYPOTHESIS until verified by the relevant department. Preserve chronology and source references when provided.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently release an apartment, change room/unit status, approve a refund/waiver/charge, alter a reservation, promise maintenance completion, change housekeeping entitlement, diagnose a technical cause, assign liability, or create a resident benefit. Do not treat AI-generated language as proof that work was completed.
Risk classification: Medium.
Final operational action requires verification/approval by: Guest Relations / Hotel Apartment Operations Manager.
AI output is decision support and a draft—not the PMS, CMMS, inspection record, financial record or authorization.
```

### Human verification

Before using the output operationally, verify the current system-of-record data, resolve any UNVERIFIED/CONFLICT items, confirm authority for the intended action and record the final decision in the approved hotel system.

---

## Key takeaway

The strongest use of AI in serviced apartments is **operational continuity**. Long stays create more history, more dependencies and more chances for a small inconsistency to become a recurring guest problem. The HOTEL framework helps AI organize that complexity without replacing the systems, inspections and accountable people that define what is actually true.

**Previous:** Article 04 — Reservations AI Toolkit  
**Series:** Hotel & Serviced Apartment AI Operations Playbook  
**Next:** Article 06 — Housekeeping Management AI Toolkit