# Article 10 — Guest Complaint & Service Recovery AI Toolkit

## 10 Professional AI Prompts for Complaint Triage, Root Cause, Recovery, Compensation Control, Escalation, Closure and CAPA

**Track C · Hotel & Serviced Apartment AI Operations Playbook · Service Recovery chapter**

A complaint is not only a message that needs a polite reply. In a professional hotel operation, it is a **controlled service-recovery case**: an event with a guest statement, an operational timeline, evidence, ownership, authority limits, communication decisions and a closure standard.

That distinction matters because AI is exceptionally good at producing confident narratives from incomplete information. A model can easily turn “the guest says housekeeping did not come” into “housekeeping failed,” convert a closed work order into “the defect was fixed,” or recommend a free night without knowing the compensation matrix. The language may sound professional while the underlying decision is wrong.

The operating principle for this chapter is:

> **AI may organize the complaint, evidence, options and communication. Verified records and authorized people determine what happened, what may be promised and when the case is truly closed.**

The ten prompts follow a complaint-control cycle:

> **Triage → Investigate → Design recovery → Check authority → Escalate → Respond → Detect recurrence → Recover reputation → Verify closure → Prevent recurrence**

---

## 1. Complaint handling is an evidence workflow, not a writing exercise

A weak complaint process begins with: **“What should we reply?”** A stronger process first determines what the guest reported, what is verified, what remains unknown, whether an immediate safety/security/privacy/welfare escalation exists, who owns the operational correction, who has recovery authority, what may be communicated now, and what evidence will prove closure.

AI can consolidate timestamps, identify missing fields, compare a case with SOP requirements, prepare an escalation brief and draft a response after the decision is made. It should not silently replace investigation or authority.

## 2. The Service Recovery HOTEL model

- **H — Hospitality role & human owner:** identify the frontline owner, Duty Manager, Guest Relations Manager, Quality Manager, Finance approver, Engineering owner or specialist escalation role.
- **O — Operational objective & context:** define the complaint channel, stay stage, severity, time sensitivity, property context, service affected and decision required.
- **T — Trusted inputs & sources of truth:** use the original guest communication, PMS/CRS, approved complaint or request log, SOP, work orders, verified department confirmations, approved recovery policy and financial/authority records.
- **E — Expected output, exceptions & evidence:** separate guest-stated claims from verified facts; expose contradictions; define owners, deadlines and closure evidence; show what is still unconfirmed.
- **L — Limits, privacy & leadership approval:** minimize personal data, prohibit unsupported liability conclusions, restrict compensation authority and escalate high-risk domains to qualified owners.

### Service-recovery source-of-truth matrix

| Question | Primary source of truth | AI rule |
|---|---|---|
| What did the guest say? | original email/chat/call record or approved case note | preserve as guest-stated information |
| What reservation/stay applies? | PMS / CRS | verify dates, room/apartment and entitlement as needed |
| Was a request logged? | CRM / guest-request system | absence of a log is not proof the guest never asked |
| Was housekeeping/engineering action completed? | approved task log / CMMS + required verification | task closure is not automatically guest-impact closure |
| What service standard applied? | current controlled SOP / service standard | use the approved revision only |
| What compensation is allowed? | recovery policy + delegation matrix | AI cannot approve |
| Was money refunded/credited? | approved finance/PMS record | recommendation is not execution |
| Was the guest informed? | timestamped communication record | draft is not sent evidence |
| Is the case closed? | approved closure workflow + evidence | silence is not proof of closure |
| Is root cause validated? | Quality/process-owner investigation | separate verified cause from hypothesis |

## 3. Fictional UAE 60-unit serviced-apartment complaint case

Continue with the fictional 60-unit UAE serviced-apartment portfolio used throughout this playbook. A resident staying for six weeks reports at 21:10 that the bedroom is warm and says the AC “has not worked properly since yesterday.” Front Office logs the complaint. Engineering records show a fan-coil work order earlier that afternoon marked **completed**, but there is no post-repair temperature verification attached. The guest also says they called earlier in the day, but no call note can be found.

A weak AI response might conclude: “Engineering failed to fix the AC, apologize and offer a complimentary night.”

A controlled analysis separates the guest-stated claim, the verified work-order fact, the missing post-repair evidence, the immediate need to verify room condition, the recovery-authority question and the communication rule. Later analysis may identify a technical cause, handover failure, closure-control failure—or several contributing factors. The complaint workflow should not decide that in the first five minutes.

## 4. Triage must protect urgency without exaggerating severity

Prompt 091 turns the initial complaint into a controlled triage record. Useful fields include complaint category, guest-stated impact, verified current condition, stay stage, immediate risk trigger, operational owner, guest-contact owner, response deadline, escalation condition and evidence still required.

A missing towel and an alleged safety incident should not enter the same workflow. AI can flag the difference, but the escalation threshold must come from property policy and qualified management.

## 5. Root-cause analysis begins after evidence collection

Prompt 092 is deliberately separate from triage. A disciplined review distinguishes **immediate failure, contributing factor, root-cause hypothesis and validated root cause**. For the fictional AC case, “Engineering closed the work order too early” may initially be only a hypothesis. Later evidence might show that the repair was correct but the closure workflow lacked a guest-comfort verification step. That changes the corrective action completely.

## 6. Service recovery should restore trust without creating uncontrolled promises

Prompt 093 creates recovery options, not recovery authorization. Options may include immediate operational correction, clear update timing, alternative service arrangements, policy-permitted non-financial gestures, financial remedies requiring approval, manager follow-up or post-stay action.

The best recovery is not always the most expensive. AI can compare options against verified impact and feasibility; it must not decide a monetary amount is “fair” without policy, authority and human judgment.

## 7. Compensation control protects the guest and the operation

Prompt 094 checks a proposed action against the documented authority matrix. The output should show the exact recovery proposed, policy reference, approver authority, prior compensation, dependencies, whether higher approval is required and whether the guest may be told yet.

**An AI authority check is never itself the approval.**

## 8. Escalation summaries should shorten the case without hiding it

Prompt 095 produces a reliable executive brief: what happened according to whom, what is verified, actions taken, what remains open, why the case exceeds current authority, what decision is required and what deadline applies. Safety, security, privacy, discrimination, legal, medical or serious reputational concerns should be routed to the appropriate qualified owner, not softened into generic service-recovery language.

## 9. Empathy and factual admission are different

Prompt 096 drafts the guest response after the facts and approved next action are known. “I’m sorry this disrupted your evening; our Duty Manager is coordinating an immediate room check and will update you by 21:35” acknowledges impact without inventing technical fault. By contrast, “Engineering failed to repair your AC correctly” is unsafe if that has not been established.

Every commitment in the draft should be visible to the reviewer: callback time, room move, refund, amenity, technical visit or manager contact.

## 10. Recurring complaint analysis requires denominators

Prompt 097 moves the team from individual cases to system learning. Twelve housekeeping complaints this month versus eight last month do not automatically prove deterioration if occupied-room nights, capture rates or service volumes changed.

Where possible, compare complaint counts with a meaningful denominator such as occupied nights, arrivals, housekeeping services, work orders, guest requests or relevant transactions.

Illustrative formula:

**Complaint rate = verified relevant complaints ÷ relevant service opportunities × 1,000**

If 9 verified cleaning-related complaints occurred across 2,400 service opportunities, the illustrative rate is **3.75 complaints per 1,000 services**. The property must define the correct denominator for its own process.

## 11. Public review recovery needs a privacy boundary

Prompt 098 produces two outputs: a privacy-safe public response and a private internal action list. The public reply should not reveal room numbers, dates, payment details, health information, private communication or internal investigation findings merely to prove the property is “right.” Matching a reviewer to a reservation does not automatically make that identity appropriate to confirm publicly.

## 12. Closure means evidence, not silence

Prompt 099 protects a common weakness: closing the complaint because a reply was sent. Guest-facing closure, operational closure, financial closure and quality/CAPA closure may occur at different times. A guest case can be appropriately closed from a communication perspective while internal CAPA remains open, but the linkage must be preserved.

## 13. CAPA turns recovery into prevention

Prompt 100 distinguishes **containment, corrective action, preventive action and effectiveness check**. Completing training or rewriting an SOP is not proof of effectiveness. The property should define a follow-up measure such as recurrence rate, audit compliance, first-time-right performance or another process-relevant KPI.

## 14. Service Recovery KPI dashboard

| KPI | What it controls |
|---|---|
| First response time | speed of acknowledgement and ownership |
| Time to operational containment | speed of immediate protection/correction |
| Complaint closure time | end-to-end case control |
| Reopened complaint rate | quality of closure |
| Repeat complaint rate by theme | systemic recurrence |
| Escalation rate | cases exceeding frontline authority |
| Compensation approval compliance | authority control |
| Recovery commitment completion | whether promises were delivered |
| Root-cause validation completion | investigation discipline |
| CAPA overdue rate | improvement follow-through |
| CAPA effectiveness pass rate | whether fixes actually work |
| Public review response timeliness | reputation workflow control |

No KPI should reward hiding complaints. A lower complaint count may reflect worse capture, not better service.

## 15. Lean Six Sigma application

**Define:** specify the recurring complaint problem and guest/service impact.

**Measure:** capture category, service opportunity, timestamps, escalation, recovery, closure and recurrence using consistent definitions.

**Analyze:** stratify by process stage, apartment, asset, channel, time, stay type, department and validated cause. Use Pareto, 5 Whys or cause-and-effect tools without converting hypotheses into facts.

**Improve:** redesign the control—handover, SLA, checklist, system field, staffing rule, preventive-maintenance control, training standard or authority workflow.

**Control:** audit the new process, monitor recurrence and verify CAPA effectiveness.

AI accelerates synthesis; it does not replace reliable data definitions, Voice of Customer evidence or process-owner validation.

## 16. Before → Action → After → AED Saved

Financial value should be documented rather than invented.

**Before:** Finance verifies the historical monthly cost of recovery actions for one validated recurring failure mode.

**Action:** Quality and Operations implement the approved CAPA.

**After:** compare a controlled period using the same definition and denominator.

**AED Saved:** verified avoided/reduced cost, adjusted for comparable volume and confirmed by the accountable financial owner.

Do not assign arbitrary monetary value to reputation, guest emotion or future loyalty.

## 17. Service Recovery AI authority matrix

| Task | AI may | AI may not | Human authority |
|---|---|---|---|
| Complaint triage | structure facts, claims, urgency and gaps | decide liability or suppress escalation | Duty/Guest Relations Manager |
| Root-cause analysis | organize evidence and hypotheses | blame employee or declare unsupported cause | Quality / Process Owner |
| Recovery options | prepare policy-bounded alternatives | promise or approve compensation | Authorized manager |
| Compensation check | compare proposal with supplied policy | grant spending/refund authority | Delegated approver / Finance |
| Escalation brief | summarize case and decision need | make legal/safety/privacy determination | Manager + qualified specialist |
| Guest response | draft approved message | invent facts, remedy or closure | Guest Relations / Duty Manager |
| Pattern review | aggregate de-identified evidence | rank staff for blame or ignore denominator | Quality / Operations |
| Review response | draft privacy-safe public reply | expose private stay information | Reputation/Guest Experience owner |
| Case closure | test closure evidence | close case without required evidence | Case owner / Manager |
| CAPA | structure actions and validation | approve specialist change alone | Quality + Process/qualified owner |

## 18. 30-day implementation plan

**Days 1–5:** define complaint categories, escalation triggers, response SLAs, owners and mandatory evidence fields.

**Days 6–10:** pilot Prompt 091 on historical complaints and compare AI triage with manager decisions.

**Days 11–15:** test Prompts 092–094 with closed fictional or de-identified cases; validate root-cause labels and compensation holds.

**Days 16–20:** pilot escalation and response drafting. Require reviewers to highlight every factual claim and guest-facing commitment.

**Days 21–25:** run the repeat-pattern review with agreed denominators and select one recurring failure mode for deeper investigation.

**Days 26–30:** use Prompts 099–100 to audit closure quality and create one controlled CAPA with an effectiveness-check date.

## 19. Cross-website knowledge connections

Article 10 belongs inside the wider Ahmed Quality Ops knowledge network:

- **Guest Experience AI Toolkit** — proactive service and journey evidence before recovery.
- **Front Office AI Toolkit** — request triage, room-not-ready communication and handover.
- **Reservations AI Toolkit** — booking facts, cancellation/no-show terms and reservation disputes.
- **Hotel Apartment & Extended-Stay AI Toolkit** — recurring resident issues and service continuity.
- **Housekeeping Management AI Toolkit** — room readiness, reclean and lost-and-found complaints.
- **Engineering & Maintenance / Predictive Maintenance** — defect evidence and repeat failures.
- **Hotel Quality Audit AI Toolkit** — evidence-based compliance and control testing.
- **Hotel SOP & Process Design AI Toolkit** — converting lessons into controlled procedures.
- **Lean Six Sigma for Hotel Operations** — root cause, recurrence reduction and control.
- **Finance & Cost Control** — refunds, credits and verified recovery cost.
- **MICE operations** — group-level failures and compressed escalation windows.
- **Tourism transport and dispatch** — transfer delays, missed pickup and movement recovery.

Useful existing website connections include:

- /articles/tourism-ai-operations-playbook/index.html
- /articles/sop-exception-escalation-management/index.html
- /articles/sop-roles-authority-raci/index.html
- /articles/how-to-write-professional-sop-procedure/index.html
- /articles/article-abu-dhabi-mice-movement-control-room/index.html

When integrated into the live website, relevant older pages should also receive reciprocal links back to this service-recovery chapter.

## 20. Management checklist

- Is the guest statement separated from verified fact?
- Has immediate safety/security/privacy/welfare risk been checked?
- Does the case have one accountable owner and response deadline?
- Are operational correction and guest communication coordinated?
- Is every recovery offer within a documented authority path?
- Are facts and commitments reverified before the response is sent?
- Are public review responses privacy-safe?
- Does closure require evidence rather than silence?
- Are recurring themes analyzed with appropriate denominators?
- Is root cause labeled by evidence status?
- Does CAPA include an effectiveness check?
- Can management trace every material decision to a system, policy or authorized person?

## 21. Key takeaway

Strong service recovery is not the art of writing a better apology. It is the discipline of **protecting evidence, responding quickly, restoring service within authority, communicating truthfully, closing every promise and preventing the same failure from returning**.

AI is valuable when it makes that control loop faster and clearer. It becomes dangerous when it invents the facts, compensation, liability or closure.

---

# 22. The 10 copy-ready prompts

## Prompt 091 — Complaint Triage

**Risk:** Medium  
**Human owner:** Guest Relations Manager / Duty Manager

**When to use:** Use when a new complaint arrives and the team needs to separate guest-stated claims, verified facts, immediate risks and next actions before responding.

### Why this prompt matters

This prompt supports a controlled complaint or recovery workflow while preserving the distinction between guest-stated information, verified evidence, management authority and unresolved items.

### Required inputs

- complaint text or call notes
- PMS/CRS stay facts
- guest-request/CRM log
- relevant service timestamps
- department confirmations
- complaint/escalation SOP
- known safety/security/privacy flags

### Expected outputs

- triage classification
- confirmed facts vs guest-stated claims
- immediate action list
- owner and response deadline
- escalation triggers
- missing-evidence list

### Copy-ready prompt

```text
ROLE
Act as a senior hotel guest-relations, service-recovery and operational-quality support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Guest Relations / Front Office / Duty Management / Quality / Operations as applicable]
Accountable owner/approver: Guest Relations Manager / Duty Manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Turn a new guest complaint into a fact-controlled triage record with severity, ownership, response timing and escalation requirements.
Property/location: [insert confirmed property and location]
Stay type / journey stage / complaint channel / operating period: [insert]
Guest-stated concern: [insert only what is necessary]
Departments/dependencies involved: [insert]
Decision or workflow this output supports: [insert]
Response or escalation deadline: [insert approved SLA if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: complaint text or call notes; PMS/CRS stay facts; guest-request/CRM log; relevant service timestamps; department confirmations; complaint/escalation SOP; known safety/security/privacy flags.
Approved sources: PMS/CRS and confirmed stay facts; approved CRM/complaint or guest-request log; controlled complaint, escalation and compensation SOPs; verified department confirmations; CMMS/work orders when technical issues are involved; approved finance/refund records where applicable; approved authority matrix; original guest communication or review.
Treat the guest's description as GUEST-STATED INFORMATION unless independently verified by an approved record. Preserve the guest's words accurately when they matter, but do not convert allegation into confirmed fact.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, its owner and required verification source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: triage classification; confirmed facts vs guest-stated claims; immediate action list; owner and response deadline; escalation triggers; missing-evidence list.
Separate CONFIRMED FACTS, GUEST-STATED CLAIMS/NEEDS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
For each operational action show OWNER, DUE TIME, DEPENDENCY and CLOSURE EVIDENCE where applicable.
For each guest-facing commitment show the supporting policy, system record or human approval; otherwise label it NOT YET AUTHORIZED / NOT YET CONFIRMED.
Where sources conflict, show the conflict and the safest verification action.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not label the guest as truthful/untruthful, decide liability, promise compensation, suppress escalation or close the complaint. If safety, security, privacy, discrimination, medical, legal or serious welfare concerns appear, flag immediate human escalation without attempting to adjudicate them.
Do not include unnecessary passport/ID data, payment-card information, credentials, private employee information, security-sensitive details, health data beyond the service need, or confidential contracts.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational, financial or guest-facing action.
```

### Human verification

Before use, verify the original guest communication, case timeline, current operational status, authority matrix, privacy need, approved recovery decision and closure evidence. High-risk or specialist issues require the named qualified owner.

## Prompt 092 — Complaint Root-Cause Analyzer

**Risk:** Medium  
**Human owner:** Quality Manager / Process Owner

**When to use:** Use after the case timeline and operational records are available and the team needs disciplined root-cause analysis rather than blame or speculation.

### Why this prompt matters

This prompt supports a controlled complaint or recovery workflow while preserving the distinction between guest-stated information, verified evidence, management authority and unresolved items.

### Required inputs

- verified complaint timeline
- service/work-order/request logs
- applicable SOP/service standard
- staffing or capacity records where relevant
- previous related cases
- process owner observations
- known corrective actions

### Expected outputs

- problem statement
- cause-and-effect map
- verified causes vs hypotheses
- 5-Why analysis with evidence status
- control gaps
- recommended validation steps

### Copy-ready prompt

```text
ROLE
Act as a senior hotel guest-relations, service-recovery and operational-quality support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Guest Relations / Front Office / Duty Management / Quality / Operations as applicable]
Accountable owner/approver: Quality Manager / Process Owner

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Analyze a complaint after sufficient evidence exists and distinguish the immediate failure, contributing factors and validated root-cause status.
Property/location: [insert confirmed property and location]
Stay type / journey stage / complaint channel / operating period: [insert]
Guest-stated concern: [insert only what is necessary]
Departments/dependencies involved: [insert]
Decision or workflow this output supports: [insert]
Response or escalation deadline: [insert approved SLA if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: verified complaint timeline; service/work-order/request logs; applicable SOP/service standard; staffing or capacity records where relevant; previous related cases; process owner observations; known corrective actions.
Approved sources: PMS/CRS and confirmed stay facts; approved CRM/complaint or guest-request log; controlled complaint, escalation and compensation SOPs; verified department confirmations; CMMS/work orders when technical issues are involved; approved finance/refund records where applicable; approved authority matrix; original guest communication or review.
Treat the guest's description as GUEST-STATED INFORMATION unless independently verified by an approved record. Preserve the guest's words accurately when they matter, but do not convert allegation into confirmed fact.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, its owner and required verification source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: problem statement; cause-and-effect map; verified causes vs hypotheses; 5-Why analysis with evidence status; control gaps; recommended validation steps.
Separate CONFIRMED FACTS, GUEST-STATED CLAIMS/NEEDS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
For each operational action show OWNER, DUE TIME, DEPENDENCY and CLOSURE EVIDENCE where applicable.
For each guest-facing commitment show the supporting policy, system record or human approval; otherwise label it NOT YET AUTHORIZED / NOT YET CONFIRMED.
Where sources conflict, show the conflict and the safest verification action.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not convert correlation, one employee comment or one guest statement into a proven root cause. Do not assign employee fault or disciplinary conclusions. Label each cause as VERIFIED, CONTRIBUTING FACTOR, HYPOTHESIS or UNKNOWN.
Do not include unnecessary passport/ID data, payment-card information, credentials, private employee information, security-sensitive details, health data beyond the service need, or confidential contracts.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational, financial or guest-facing action.
```

### Human verification

Before use, verify the original guest communication, case timeline, current operational status, authority matrix, privacy need, approved recovery decision and closure evidence. High-risk or specialist issues require the named qualified owner.

## Prompt 093 — Service Recovery Options Draft

**Risk:** High  
**Human owner:** Duty Manager / Guest Relations Manager

**When to use:** Use when a complaint is understood well enough to design recovery options but a manager still needs to select and authorize the actual offer.

### Why this prompt matters

This prompt supports a controlled complaint or recovery workflow while preserving the distinction between guest-stated information, verified evidence, management authority and unresolved items.

### Required inputs

- verified complaint facts
- guest-stated desired resolution if provided
- current stay status
- approved recovery/compensation policy
- benefit/entitlement rules
- operational availability
- authority limits
- prior recovery already given

### Expected outputs

- recovery objective
- non-financial recovery options
- policy-bounded financial/benefit options
- feasibility and dependency checks
- approval requirements
- guest-communication notes

### Copy-ready prompt

```text
ROLE
Act as a senior hotel guest-relations, service-recovery and operational-quality support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Guest Relations / Front Office / Duty Management / Quality / Operations as applicable]
Accountable owner/approver: Duty Manager / Guest Relations Manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Prepare a ranked set of service-recovery options based on verified impact, current guest needs, operational feasibility and approved policy.
Property/location: [insert confirmed property and location]
Stay type / journey stage / complaint channel / operating period: [insert]
Guest-stated concern: [insert only what is necessary]
Departments/dependencies involved: [insert]
Decision or workflow this output supports: [insert]
Response or escalation deadline: [insert approved SLA if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: verified complaint facts; guest-stated desired resolution if provided; current stay status; approved recovery/compensation policy; benefit/entitlement rules; operational availability; authority limits; prior recovery already given.
Approved sources: PMS/CRS and confirmed stay facts; approved CRM/complaint or guest-request log; controlled complaint, escalation and compensation SOPs; verified department confirmations; CMMS/work orders when technical issues are involved; approved finance/refund records where applicable; approved authority matrix; original guest communication or review.
Treat the guest's description as GUEST-STATED INFORMATION unless independently verified by an approved record. Preserve the guest's words accurately when they matter, but do not convert allegation into confirmed fact.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, its owner and required verification source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: recovery objective; non-financial recovery options; policy-bounded financial/benefit options; feasibility and dependency checks; approval requirements; guest-communication notes.
Separate CONFIRMED FACTS, GUEST-STATED CLAIMS/NEEDS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
For each operational action show OWNER, DUE TIME, DEPENDENCY and CLOSURE EVIDENCE where applicable.
For each guest-facing commitment show the supporting policy, system record or human approval; otherwise label it NOT YET AUTHORIZED / NOT YET CONFIRMED.
Where sources conflict, show the conflict and the safest verification action.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not promise, approve or send compensation, refunds, upgrades, free nights, transport, gifts or financial credits. Do not invent policy ranges. If no approved policy or authority data is supplied, show options only as categories requiring manager determination.
Do not include unnecessary passport/ID data, payment-card information, credentials, private employee information, security-sensitive details, health data beyond the service need, or confidential contracts.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational, financial or guest-facing action.
```

### Human verification

Before use, verify the original guest communication, case timeline, current operational status, authority matrix, privacy need, approved recovery decision and closure evidence. High-risk or specialist issues require the named qualified owner.

## Prompt 094 — Compensation Authority Check

**Risk:** High  
**Human owner:** Authorized Duty/Operations Manager / Finance as applicable

**When to use:** Use before a manager communicates a proposed financial or entitlement-based recovery action to verify whether the proposal is within documented authority.

### Why this prompt matters

This prompt supports a controlled complaint or recovery workflow while preserving the distinction between guest-stated information, verified evidence, management authority and unresolved items.

### Required inputs

- proposed compensation
- approved authority matrix
- complaint/recovery policy
- reservation/rate/entitlement facts
- tax/finance treatment where relevant
- prior compensation on the case
- required approval chain

### Expected outputs

- authority check result
- supporting policy references
- within/outside authority flag
- missing approval/data
- required approver
- communication hold points

### Copy-ready prompt

```text
ROLE
Act as a senior hotel guest-relations, service-recovery and operational-quality support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Guest Relations / Front Office / Duty Management / Quality / Operations as applicable]
Accountable owner/approver: Authorized Duty/Operations Manager / Finance as applicable

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Check a proposed guest compensation or commercial recovery action against the current approval matrix, booking terms and documented authority.
Property/location: [insert confirmed property and location]
Stay type / journey stage / complaint channel / operating period: [insert]
Guest-stated concern: [insert only what is necessary]
Departments/dependencies involved: [insert]
Decision or workflow this output supports: [insert]
Response or escalation deadline: [insert approved SLA if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: proposed compensation; approved authority matrix; complaint/recovery policy; reservation/rate/entitlement facts; tax/finance treatment where relevant; prior compensation on the case; required approval chain.
Approved sources: PMS/CRS and confirmed stay facts; approved CRM/complaint or guest-request log; controlled complaint, escalation and compensation SOPs; verified department confirmations; CMMS/work orders when technical issues are involved; approved finance/refund records where applicable; approved authority matrix; original guest communication or review.
Treat the guest's description as GUEST-STATED INFORMATION unless independently verified by an approved record. Preserve the guest's words accurately when they matter, but do not convert allegation into confirmed fact.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, its owner and required verification source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: authority check result; supporting policy references; within/outside authority flag; missing approval/data; required approver; communication hold points.
Separate CONFIRMED FACTS, GUEST-STATED CLAIMS/NEEDS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
For each operational action show OWNER, DUE TIME, DEPENDENCY and CLOSURE EVIDENCE where applicable.
For each guest-facing commitment show the supporting policy, system record or human approval; otherwise label it NOT YET AUTHORIZED / NOT YET CONFIRMED.
Where sources conflict, show the conflict and the safest verification action.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
This is an authority check, not an approval. Never treat the AI output as permission to spend, refund, waive, upgrade or alter a reservation. If policy wording is ambiguous or missing, return HOLD FOR HUMAN REVIEW.
Do not include unnecessary passport/ID data, payment-card information, credentials, private employee information, security-sensitive details, health data beyond the service need, or confidential contracts.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational, financial or guest-facing action.
```

### Human verification

Before use, verify the original guest communication, case timeline, current operational status, authority matrix, privacy need, approved recovery decision and closure evidence. High-risk or specialist issues require the named qualified owner.

## Prompt 095 — Escalation Summary

**Risk:** High  
**Human owner:** Duty Manager / Operations Manager / Specialist Owner

**When to use:** Use when a case exceeds frontline authority, remains unresolved, involves multiple departments, or contains safety, security, privacy, legal, discrimination or reputational triggers.

### Why this prompt matters

This prompt supports a controlled complaint or recovery workflow while preserving the distinction between guest-stated information, verified evidence, management authority and unresolved items.

### Required inputs

- verified case chronology
- guest-stated issue
- actions already taken
- open risks
- department confirmations
- relevant policy/escalation triggers
- communications sent
- current guest status

### Expected outputs

- executive case summary
- risk/escalation reason
- facts and unresolved claims
- actions completed
- decision required
- recommended owner and urgency
- evidence attachments checklist

### Copy-ready prompt

```text
ROLE
Act as a senior hotel guest-relations, service-recovery and operational-quality support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Guest Relations / Front Office / Duty Management / Quality / Operations as applicable]
Accountable owner/approver: Duty Manager / Operations Manager / Specialist Owner

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Prepare a concise escalation brief for a serious, unresolved or cross-functional complaint without diluting risk or adding unsupported conclusions.
Property/location: [insert confirmed property and location]
Stay type / journey stage / complaint channel / operating period: [insert]
Guest-stated concern: [insert only what is necessary]
Departments/dependencies involved: [insert]
Decision or workflow this output supports: [insert]
Response or escalation deadline: [insert approved SLA if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: verified case chronology; guest-stated issue; actions already taken; open risks; department confirmations; relevant policy/escalation triggers; communications sent; current guest status.
Approved sources: PMS/CRS and confirmed stay facts; approved CRM/complaint or guest-request log; controlled complaint, escalation and compensation SOPs; verified department confirmations; CMMS/work orders when technical issues are involved; approved finance/refund records where applicable; approved authority matrix; original guest communication or review.
Treat the guest's description as GUEST-STATED INFORMATION unless independently verified by an approved record. Preserve the guest's words accurately when they matter, but do not convert allegation into confirmed fact.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, its owner and required verification source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: executive case summary; risk/escalation reason; facts and unresolved claims; actions completed; decision required; recommended owner and urgency; evidence attachments checklist.
Separate CONFIRMED FACTS, GUEST-STATED CLAIMS/NEEDS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
For each operational action show OWNER, DUE TIME, DEPENDENCY and CLOSURE EVIDENCE where applicable.
For each guest-facing commitment show the supporting policy, system record or human approval; otherwise label it NOT YET AUTHORIZED / NOT YET CONFIRMED.
Where sources conflict, show the conflict and the safest verification action.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not make legal conclusions, determine negligence, diagnose medical conditions, minimize safety/security/privacy issues or recommend hiding material facts. Preserve exact evidence and route specialized matters to the qualified function.
Do not include unnecessary passport/ID data, payment-card information, credentials, private employee information, security-sensitive details, health data beyond the service need, or confidential contracts.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational, financial or guest-facing action.
```

### Human verification

Before use, verify the original guest communication, case timeline, current operational status, authority matrix, privacy need, approved recovery decision and closure evidence. High-risk or specialist issues require the named qualified owner.

## Prompt 096 — Complaint Response Draft

**Risk:** Medium  
**Human owner:** Guest Relations / Duty Manager

**When to use:** Use after the case owner has verified what happened and, where applicable, approved the recovery action that may be communicated.

### Why this prompt matters

This prompt supports a controlled complaint or recovery workflow while preserving the distinction between guest-stated information, verified evidence, management authority and unresolved items.

### Required inputs

- verified complaint facts
- guest concern/request
- approved resolution or next step
- approved tone/brand guidance
- timing and contact channel
- facts that must not be disclosed
- manager instructions

### Expected outputs

- guest-facing response draft
- facts requiring final verification
- promises/commitments checklist
- internal follow-up notes
- alternative concise version if requested

### Copy-ready prompt

```text
ROLE
Act as a senior hotel guest-relations, service-recovery and operational-quality support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Guest Relations / Front Office / Duty Management / Quality / Operations as applicable]
Accountable owner/approver: Guest Relations / Duty Manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Draft a professional guest response using verified facts, approved recovery decisions and the property tone while avoiding unsupported promises or admissions.
Property/location: [insert confirmed property and location]
Stay type / journey stage / complaint channel / operating period: [insert]
Guest-stated concern: [insert only what is necessary]
Departments/dependencies involved: [insert]
Decision or workflow this output supports: [insert]
Response or escalation deadline: [insert approved SLA if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: verified complaint facts; guest concern/request; approved resolution or next step; approved tone/brand guidance; timing and contact channel; facts that must not be disclosed; manager instructions.
Approved sources: PMS/CRS and confirmed stay facts; approved CRM/complaint or guest-request log; controlled complaint, escalation and compensation SOPs; verified department confirmations; CMMS/work orders when technical issues are involved; approved finance/refund records where applicable; approved authority matrix; original guest communication or review.
Treat the guest's description as GUEST-STATED INFORMATION unless independently verified by an approved record. Preserve the guest's words accurately when they matter, but do not convert allegation into confirmed fact.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, its owner and required verification source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: guest-facing response draft; facts requiring final verification; promises/commitments checklist; internal follow-up notes; alternative concise version if requested.
Separate CONFIRMED FACTS, GUEST-STATED CLAIMS/NEEDS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
For each operational action show OWNER, DUE TIME, DEPENDENCY and CLOSURE EVIDENCE where applicable.
For each guest-facing commitment show the supporting policy, system record or human approval; otherwise label it NOT YET AUTHORIZED / NOT YET CONFIRMED.
Where sources conflict, show the conflict and the safest verification action.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not invent facts, state that a problem is resolved without evidence, disclose internal disciplinary/security information, admit legal liability, or add compensation that has not been approved. Keep empathy separate from factual admission.
Do not include unnecessary passport/ID data, payment-card information, credentials, private employee information, security-sensitive details, health data beyond the service need, or confidential contracts.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational, financial or guest-facing action.
```

### Human verification

Before use, verify the original guest communication, case timeline, current operational status, authority matrix, privacy need, approved recovery decision and closure evidence. High-risk or specialist issues require the named qualified owner.

## Prompt 097 — Repeat Complaint Pattern Review

**Risk:** Medium  
**Human owner:** Quality Manager / Guest Experience Manager

**When to use:** Use weekly or monthly when complaint volume is sufficient to examine recurrence by process, apartment/room, asset, channel, time, team or guest-journey stage.

### Why this prompt matters

This prompt supports a controlled complaint or recovery workflow while preserving the distinction between guest-stated information, verified evidence, management authority and unresolved items.

### Required inputs

- de-identified complaint dataset
- case categories
- timestamps
- closure times
- property/room/asset identifiers where appropriate
- root-cause status
- total stays/requests or other denominators
- service recovery data

### Expected outputs

- theme frequency table
- rates/denominators where available
- repeat-failure clusters
- evidence quality warnings
- Pareto-style priorities
- recommended investigation list

### Copy-ready prompt

```text
ROLE
Act as a senior hotel guest-relations, service-recovery and operational-quality support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Guest Relations / Front Office / Duty Management / Quality / Operations as applicable]
Accountable owner/approver: Quality Manager / Guest Experience Manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Analyze a set of complaints for recurring themes, process failure modes, concentration points and evidence-backed improvement priorities.
Property/location: [insert confirmed property and location]
Stay type / journey stage / complaint channel / operating period: [insert]
Guest-stated concern: [insert only what is necessary]
Departments/dependencies involved: [insert]
Decision or workflow this output supports: [insert]
Response or escalation deadline: [insert approved SLA if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: de-identified complaint dataset; case categories; timestamps; closure times; property/room/asset identifiers where appropriate; root-cause status; total stays/requests or other denominators; service recovery data.
Approved sources: PMS/CRS and confirmed stay facts; approved CRM/complaint or guest-request log; controlled complaint, escalation and compensation SOPs; verified department confirmations; CMMS/work orders when technical issues are involved; approved finance/refund records where applicable; approved authority matrix; original guest communication or review.
Treat the guest's description as GUEST-STATED INFORMATION unless independently verified by an approved record. Preserve the guest's words accurately when they matter, but do not convert allegation into confirmed fact.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, its owner and required verification source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: theme frequency table; rates/denominators where available; repeat-failure clusters; evidence quality warnings; Pareto-style priorities; recommended investigation list.
Separate CONFIRMED FACTS, GUEST-STATED CLAIMS/NEEDS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
For each operational action show OWNER, DUE TIME, DEPENDENCY and CLOSURE EVIDENCE where applicable.
For each guest-facing commitment show the supporting policy, system record or human approval; otherwise label it NOT YET AUTHORIZED / NOT YET CONFIRMED.
Where sources conflict, show the conflict and the safest verification action.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not infer systemic deterioration from raw counts without denominators or comparable periods. Do not rank employees for blame. Protect guest identity and label small-sample findings as weak signals.
Do not include unnecessary passport/ID data, payment-card information, credentials, private employee information, security-sensitive details, health data beyond the service need, or confidential contracts.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational, financial or guest-facing action.
```

### Human verification

Before use, verify the original guest communication, case timeline, current operational status, authority matrix, privacy need, approved recovery decision and closure evidence. High-risk or specialist issues require the named qualified owner.

## Prompt 098 — Negative Review Recovery Draft

**Risk:** Medium  
**Human owner:** Guest Experience / Reputation Manager

**When to use:** Use when an online review requires a public response and the property also needs to capture any unresolved operational issue behind it.

### Why this prompt matters

This prompt supports a controlled complaint or recovery workflow while preserving the distinction between guest-stated information, verified evidence, management authority and unresolved items.

### Required inputs

- review text
- platform/channel
- verified stay/case facts if legitimately matched
- approved brand response guidance
- approved resolution already taken
- open internal actions
- privacy rules

### Expected outputs

- public response draft
- claims not safe to address publicly
- internal action list
- manager follow-up need
- learning tags

### Copy-ready prompt

```text
ROLE
Act as a senior hotel guest-relations, service-recovery and operational-quality support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Guest Relations / Front Office / Duty Management / Quality / Operations as applicable]
Accountable owner/approver: Guest Experience / Reputation Manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Prepare a privacy-safe public response and an internal recovery checklist for a negative online review using only verified and appropriate information.
Property/location: [insert confirmed property and location]
Stay type / journey stage / complaint channel / operating period: [insert]
Guest-stated concern: [insert only what is necessary]
Departments/dependencies involved: [insert]
Decision or workflow this output supports: [insert]
Response or escalation deadline: [insert approved SLA if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: review text; platform/channel; verified stay/case facts if legitimately matched; approved brand response guidance; approved resolution already taken; open internal actions; privacy rules.
Approved sources: PMS/CRS and confirmed stay facts; approved CRM/complaint or guest-request log; controlled complaint, escalation and compensation SOPs; verified department confirmations; CMMS/work orders when technical issues are involved; approved finance/refund records where applicable; approved authority matrix; original guest communication or review.
Treat the guest's description as GUEST-STATED INFORMATION unless independently verified by an approved record. Preserve the guest's words accurately when they matter, but do not convert allegation into confirmed fact.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, its owner and required verification source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: public response draft; claims not safe to address publicly; internal action list; manager follow-up need; learning tags.
Separate CONFIRMED FACTS, GUEST-STATED CLAIMS/NEEDS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
For each operational action show OWNER, DUE TIME, DEPENDENCY and CLOSURE EVIDENCE where applicable.
For each guest-facing commitment show the supporting policy, system record or human approval; otherwise label it NOT YET AUTHORIZED / NOT YET CONFIRMED.
Where sources conflict, show the conflict and the safest verification action.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not reveal stay dates, room numbers, personal details, payment disputes, health information, internal investigation findings or information that confirms a reviewer identity unnecessarily. Do not argue, threaten, incentivize review removal or invent a resolution.
Do not include unnecessary passport/ID data, payment-card information, credentials, private employee information, security-sensitive details, health data beyond the service need, or confidential contracts.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational, financial or guest-facing action.
```

### Human verification

Before use, verify the original guest communication, case timeline, current operational status, authority matrix, privacy need, approved recovery decision and closure evidence. High-risk or specialist issues require the named qualified owner.

## Prompt 099 — Complaint Closure Checklist

**Risk:** Medium  
**Human owner:** Guest Relations Manager / Duty Manager

**When to use:** Use before marking a complaint closed in the approved case-management workflow.

### Why this prompt matters

This prompt supports a controlled complaint or recovery workflow while preserving the distinction between guest-stated information, verified evidence, management authority and unresolved items.

### Required inputs

- case chronology
- guest communications
- actions and work orders
- approved recovery record
- financial/compensation evidence if applicable
- guest follow-up evidence
- root-cause/CAPA link where required
- case owner status

### Expected outputs

- closure-ready yes/no assessment
- missing closure evidence
- open guest commitments
- open internal actions
- required approvals
- final case summary fields

### Copy-ready prompt

```text
ROLE
Act as a senior hotel guest-relations, service-recovery and operational-quality support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Guest Relations / Front Office / Duty Management / Quality / Operations as applicable]
Accountable owner/approver: Guest Relations Manager / Duty Manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Determine whether a complaint file has the evidence required for operational closure and identify any open loops before the case is closed.
Property/location: [insert confirmed property and location]
Stay type / journey stage / complaint channel / operating period: [insert]
Guest-stated concern: [insert only what is necessary]
Departments/dependencies involved: [insert]
Decision or workflow this output supports: [insert]
Response or escalation deadline: [insert approved SLA if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: case chronology; guest communications; actions and work orders; approved recovery record; financial/compensation evidence if applicable; guest follow-up evidence; root-cause/CAPA link where required; case owner status.
Approved sources: PMS/CRS and confirmed stay facts; approved CRM/complaint or guest-request log; controlled complaint, escalation and compensation SOPs; verified department confirmations; CMMS/work orders when technical issues are involved; approved finance/refund records where applicable; approved authority matrix; original guest communication or review.
Treat the guest's description as GUEST-STATED INFORMATION unless independently verified by an approved record. Preserve the guest's words accurately when they matter, but do not convert allegation into confirmed fact.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, its owner and required verification source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: closure-ready yes/no assessment; missing closure evidence; open guest commitments; open internal actions; required approvals; final case summary fields.
Separate CONFIRMED FACTS, GUEST-STATED CLAIMS/NEEDS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
For each operational action show OWNER, DUE TIME, DEPENDENCY and CLOSURE EVIDENCE where applicable.
For each guest-facing commitment show the supporting policy, system record or human approval; otherwise label it NOT YET AUTHORIZED / NOT YET CONFIRMED.
Where sources conflict, show the conflict and the safest verification action.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not close a case because the guest stopped replying or because a message was sent. Closure requires the property-defined evidence standard. Keep unresolved internal corrective actions linked even when the guest-facing case is appropriately closed.
Do not include unnecessary passport/ID data, payment-card information, credentials, private employee information, security-sensitive details, health data beyond the service need, or confidential contracts.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational, financial or guest-facing action.
```

### Human verification

Before use, verify the original guest communication, case timeline, current operational status, authority matrix, privacy need, approved recovery decision and closure evidence. High-risk or specialist issues require the named qualified owner.

## Prompt 100 — CAPA Builder

**Risk:** High  
**Human owner:** Quality Manager / Process Owner / Operations Manager

**When to use:** Use when the complaint reveals a systemic or material process failure that requires more than one-off guest recovery.

### Why this prompt matters

This prompt supports a controlled complaint or recovery workflow while preserving the distinction between guest-stated information, verified evidence, management authority and unresolved items.

### Required inputs

- validated problem statement
- verified root cause or explicitly labeled hypothesis
- immediate containment actions
- current SOP/control
- repeat-case evidence
- risk assessment
- owners/resources
- target KPI or effectiveness measure

### Expected outputs

- containment vs corrective vs preventive actions
- owner/deadline register
- SOP/training/system changes
- effectiveness measures
- verification date
- residual-risk/escalation notes

### Copy-ready prompt

```text
ROLE
Act as a senior hotel guest-relations, service-recovery and operational-quality support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Guest Relations / Front Office / Duty Management / Quality / Operations as applicable]
Accountable owner/approver: Quality Manager / Process Owner / Operations Manager

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Convert a validated complaint failure into a controlled corrective and preventive action plan with owners, deadlines, evidence and effectiveness checks.
Property/location: [insert confirmed property and location]
Stay type / journey stage / complaint channel / operating period: [insert]
Guest-stated concern: [insert only what is necessary]
Departments/dependencies involved: [insert]
Decision or workflow this output supports: [insert]
Response or escalation deadline: [insert approved SLA if applicable]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: validated problem statement; verified root cause or explicitly labeled hypothesis; immediate containment actions; current SOP/control; repeat-case evidence; risk assessment; owners/resources; target KPI or effectiveness measure.
Approved sources: PMS/CRS and confirmed stay facts; approved CRM/complaint or guest-request log; controlled complaint, escalation and compensation SOPs; verified department confirmations; CMMS/work orders when technical issues are involved; approved finance/refund records where applicable; approved authority matrix; original guest communication or review.
Treat the guest's description as GUEST-STATED INFORMATION unless independently verified by an approved record. Preserve the guest's words accurately when they matter, but do not convert allegation into confirmed fact.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, its owner and required verification source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: containment vs corrective vs preventive actions; owner/deadline register; SOP/training/system changes; effectiveness measures; verification date; residual-risk/escalation notes.
Separate CONFIRMED FACTS, GUEST-STATED CLAIMS/NEEDS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
For each operational action show OWNER, DUE TIME, DEPENDENCY and CLOSURE EVIDENCE where applicable.
For each guest-facing commitment show the supporting policy, system record or human approval; otherwise label it NOT YET AUTHORIZED / NOT YET CONFIRMED.
Where sources conflict, show the conflict and the safest verification action.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not present an unvalidated cause as the basis for permanent process change. Do not close CAPA on completion of tasks alone; require an effectiveness check. Safety, engineering, privacy, HR, legal and financial CAPA require the corresponding qualified owner.
Do not include unnecessary passport/ID data, payment-card information, credentials, private employee information, security-sensitive details, health data beyond the service need, or confidential contracts.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational, financial or guest-facing action.
```

### Human verification

Before use, verify the original guest communication, case timeline, current operational status, authority matrix, privacy need, approved recovery decision and closure evidence. High-risk or specialist issues require the named qualified owner.

---

## 23. Human verification checklist

Before any AI-generated service-recovery output enters a live workflow, confirm that the correct stay/case is identified; guest-stated claims remain labeled until verified; timestamps and records are current; serious specialist triggers are escalated; recovery authority is documented; the guest-facing message has no invented facts or unapproved commitments; each promised action has owner, deadline and closure evidence; public responses protect privacy; root-cause findings reflect evidence strength; and closure/CAPA follow the controlled workflow.

## 24. Trainer notes and practice exercises

Use fictional or properly de-identified cases. Ask learners to label each sentence in an AI output as **fact, guest-stated claim, hypothesis, recommendation, commitment or unresolved item**, then compare it with source systems and the authority matrix.

A second exercise should deliberately provide conflicting evidence—for example, a guest statement saying no one attended and a system log showing a technician entry without guest-confirmed closure. The correct AI behavior is to expose the conflict and request verification, not choose a side.

## 25. Evidence boundaries

The 60-unit UAE serviced-apartment case and numerical examples in this chapter are illustrative. They are not performance claims about a named property. Compensation levels, escalation thresholds, service SLAs and legal/privacy obligations vary by operator and jurisdiction and must come from current approved policies and qualified advisers.

## 26. Series navigation

**Previous:** [Article 09 — Guest Experience AI Toolkit](09-guest-experience-ai-toolkit.md)  
**Series:** [START HERE](../START-HERE.md)  
**Next:** [Article 11 — Hotel Quality Audit AI Toolkit](11-hotel-quality-audit-ai-toolkit.md)
