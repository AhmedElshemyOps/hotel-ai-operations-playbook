# Article 12 — Hotel SOP & Process Design AI Toolkit

## 10 Professional AI Prompts for SOP Structure, Procedures, RACI, Exceptions, Evidence, KPIs and Document Revision

**Track C · Hotel & Serviced Apartment AI Operations Playbook · SOP & Process Design chapter**

A hotel SOP is not a document-writing exercise. It is a **control system for repeatable work**.

A beautifully written procedure can still fail if it describes an imagined process, assigns authority that management never approved, ignores exceptions, hides handoffs, or requires evidence that nobody actually records. Generative AI makes this risk more visible because it can produce fluent procedures faster than a hotel can validate them.

> **AI may help discover, structure, challenge and draft a hotel process. The process owner must verify how the work is actually performed, approve authority, test exceptions and control the released document.**

The ten prompts follow one complete process-design lifecycle:

> **Discover → Map → Assign authority → Draft → Build exceptions → Define evidence → Measure → Train → Audit → Revise**

This chapter continues the fictional 60-unit UAE serviced-apartment case used throughout the playbook. All property figures, costs and examples are illustrative unless specifically linked to a verified external source.

---

## 1. SOP design starts with the process, not the page

The easiest mistake in SOP work is to open a blank template and start writing steps. Professional process design begins earlier.

Before a procedure is drafted, management should understand the purpose of the process, its trigger, required inputs, intended output, real roles, systems, control points, records, normal completion condition, exceptions and decision authority.

ISO's guidance on the process approach describes processes as interrelated activities that use inputs to deliver intended results, supported by PDCA and risk-based thinking. ISO 10013:2021 separately provides guidance on developing and maintaining documented information that supports effective management-system processes. Those ideas fit hotel operations well: **the procedure should support the process, not become a substitute for understanding it.**

A hotel should therefore avoid asking AI, “Write an SOP for room-not-ready guests,” before the current operating reality is known. A better sequence is: observe, map, validate, then draft.

## 2. The SOP-design HOTEL model

**H — Hospitality role & human owner** — Who owns the process, performs it, approves the SOP and authorizes exceptions?

**O — Operational objective & context** — What outcome must the process achieve, in which property, department, shift and guest-journey stage?

**T — Trusted inputs & sources of truth** — Which current SOPs, policies, PMS/CMMS/RMS records, forms, contracts or controlled standards define the process?

**E — Expected output, exceptions & evidence** — What document structure is required, which records prove critical steps and what happens when the normal path fails?

**L — Limits, privacy & leadership approval** — What may AI not decide, which data must stay protected and who validates the process before publication?

For SOP work, every important instruction should connect to a role, decision, system or record. If it connects to none of them, management should challenge whether it is useful, observable or auditable.

## 3. Fictional UAE case: redesigning the room-not-ready process

Continue with the fictional 60-unit UAE serviced-apartment portfolio.

Management reviews several recent arrival cases and sees recurring friction when an apartment is not ready at the expected arrival time. The existing SOP contains one line:

> “If the room is not ready, inform the guest and contact housekeeping.”

That sentence leaves almost every operational control unanswered: how “not ready” is defined, which system owns status, who confirms the next realistic readiness time, what happens if Engineering is the blocker, how often the guest is updated, what Front Office may promise, when the Duty Manager becomes involved, what compensation authority exists and which record proves closure.

A redesigned process can separate four states:

1. **Cleaning in progress** — Housekeeping owns the next readiness update.
2. **Inspection pending** — the supervisor owns inspection and release evidence.
3. **Technical blocker** — Engineering owns the work-order status; Front Office must not invent a release time.
4. **Management exception** — the Duty Manager decides among approved recovery options.

AI can expose missing controls. The hotel team must still decide the real roles, thresholds and authority.

## 4. Process discovery should expose hidden work

Formal procedures often describe what management thinks happens. Actual work may include undocumented calls, WhatsApp messages, handwritten lists, verbal approvals, workarounds, duplicate system entry and unofficial escalation.

Before redesigning an SOP, interview and observe the people who perform the process. Ask what starts the work, what information is usually missing, which checks happen before action, where the team leaves the system and uses a workaround, what happens when the standard case fails, which decisions need approval and which record proves completion.

The purpose is not to legitimize every workaround. It is to make the current state visible before management designs the future state.

## 5. Build the SOP architecture before drafting paragraphs

Prompt 111 creates the document architecture. A hotel SOP normally benefits from a controlled structure: title and identifier; owner and approver; purpose; scope; definitions; roles and authority; triggers and prerequisites; procedure steps; decision points; exceptions and escalation; records/evidence; KPIs where useful; training; references; revision history; and next review date.

Not every procedure requires the same detail. Risk should determine the level of control.

A good architecture also keeps document types clear:

- **Policy** — what the organization requires or permits.
- **Procedure/SOP** — who does what, when and under which controls.
- **Work instruction** — detailed task execution.
- **Checklist/form** — verification or evidence.

AI should not merge these levels unless management intentionally wants a combined document.

## 6. A procedure step should be executable and auditable

Prompt 112 converts the validated process into procedure steps.

Weak instruction:

> “Handle the guest professionally.”

Controlled instruction:

> “Front Office checks the current PMS room status and the latest Housekeeping/Engineering dependency before giving the guest an estimated readiness update. If no verified estimate exists, the agent states that timing is being confirmed and escalates according to the approved threshold.”

The stronger version identifies role, action, trusted source, decision condition, prohibited assumption and escalation behavior.

A useful procedure table can include: Step | Role | Action | System/source | Decision/condition | Evidence | Escalation.

## 7. RACI should clarify authority, not decorate the SOP

Prompt 113 builds a RACI only after the actual process roles are known.

RACI means Responsible, Accountable, Consulted and Informed. Two common errors are damaging: assigning multiple Accountables to the same decision and assuming that a job title automatically grants compensation, financial, safety, pricing or employment authority.

The SOP should link RACI to the approved authority/delegation framework where necessary.

## 8. Exception design is where professional SOPs become operational

Prompt 114 addresses the point where weak SOPs often fail: the normal process cannot continue.

A useful exception matrix identifies the exception, detection method, immediate containment, owner, escalation trigger, authorized options and evidence required for closure.

“In case of any issue, contact the manager” is not an exception process. The exception should identify the issue class, interim action, owner, trigger and authority.

## 9. Evidence design turns an SOP into a controllable system

Prompt 115 asks one question for every critical instruction:

> **How will we know this step happened correctly?**

Evidence may be a PMS status change, inspection checklist, work-order closeout, timestamped communication, approval record, controlled form, system transaction, inventory count or training acknowledgement.

Do not create records simply to create paperwork. Evidence should support control, traceability, service recovery, compliance or improvement. Privacy and access rules still apply.

## 10. KPIs should test the process outcome, not reward shortcuts

Prompt 116 creates measures only after the process objective and controls are clear.

For a room-not-ready process, useful measures might include percentage of affected arrivals receiving an update within the approved interval, time from dependency confirmation to guest update, percentage of cases with a named blocker and owner, repeat-delay rate by verified cause category, and percentage of closed cases with closure evidence.

Every KPI needs a definition, denominator, source, owner, review frequency and anti-gaming guardrail. AI may propose indicators, but management approves targets.

## 11. Work instructions and checklists should stay connected to the SOP

Prompt 117 creates detailed work instructions for tasks where step-level precision is necessary. Prompt 118 converts approved requirements into a practical checklist.

The hierarchy can be:

**Policy → SOP → Work instruction → Checklist/form**

If the SOP changes, dependent work instructions and checklists may also require revision. This dependency is why Prompt 120 performs revision-impact analysis.

## 12. SOP audits should compare controlled design with actual practice

Prompt 119 is not a grammar checker. It compares the approved SOP with observed work, system records, incidents, complaints, employee feedback, linked policies, technology and the current authority model.

Possible findings include obsolete system names, hidden manual work, duplicated approvals, missing exception paths, undefined owners, unrealistic SLAs, records that are not actually generated, training mismatch and controls that are routinely bypassed.

The aim is to determine whether the document still controls the process effectively.

## 13. Revision control prevents a correct SOP from becoming a new risk

Prompt 120 reviews the impact of a proposed change before publication.

A single change can affect roles, approval authority, PMS/CMMS/RMS fields, forms, training, KPIs, vendor responsibilities, guest communication, checklists, audit criteria, linked SOPs and digital automation.

Changing room release from a paper inspection to a mobile checklist, for example, may also change who can release the room, which timestamp becomes evidence, how offline operation is handled and which record is retained.

## 14. Lean Six Sigma can strengthen SOP design

SOP work and Lean Six Sigma are complementary when the sequence is correct.

**Define** the guest/business problem and process boundary.  
**Measure** the real current process, timing, defects and rework.  
**Analyze** verified causes and failure points.  
**Improve** the process and controls.  
**Control** through SOPs, work instructions, training, measurement and audit.

The SOP should document a stabilized process, not freeze an inefficient workflow merely because “that is how we have always done it.”

## 15. SOP governance dashboard

Useful governance measures include SOP review completion, overdue controlled documents, exception frequency per process volume, repeat SOP-related finding rate, training completion, field-validation pass rate, undocumented-workaround count, obsolete-reference rate, overdue revision-impact actions and post-publication rework.

The dashboard should distinguish document completion from process effectiveness.

## 16. Illustrative Before → Action → After → AED Saved

Consider an illustrative workflow only.

**Before:** room-not-ready cases generate 18 duplicated calls/messages per month across Front Office, Housekeeping and Engineering. Assume, only for illustration, six minutes of avoidable coordination per duplicated contact and a blended internal labor value of AED 45/hour.

18 × 6 minutes = 108 minutes = 1.8 hours.  
1.8 × AED 45 = **AED 81/month** direct duplicated coordination cost.

**Action:** redesign the SOP around one status owner, one verified dependency field, a defined update interval and an escalation threshold.

**After:** comparable duplicated contacts fall from 18 to 6.

Avoided direct coordination time: 12 × 6 minutes = 72 minutes = 1.2 hours.  
1.2 × AED 45 = **AED 54/month** illustrative direct labor avoidance.

A real business case should use Finance-approved values, comparable periods and verified counts. Do not inflate small savings to make an SOP project appear more valuable.

## 17. 30-day implementation plan

**Days 1–5 — Process inventory:** identify high-risk/high-friction procedures, confirm document owners, collect current SOPs/policies/forms and define approval authority.

**Days 6–10 — Observe and map:** shadow the work, interview frontline roles, map inputs/outputs/handoffs, identify systems/evidence and document normal and exception paths.

**Days 11–15 — Draft and challenge:** use Prompts 111–115, separate policy/SOP/work-instruction/checklist needs, test RACI, authority and exception logic.

**Days 16–20 — Measures and training design:** use Prompts 116–118, define KPI sources/denominators, create job aids and build role-based training scenarios.

**Days 21–25 — Pilot:** test the SOP on a controlled scope, record confusion/workarounds/exceptions, compare documented vs observed steps and revise.

**Days 26–30 — Release and control:** approve the version, withdraw obsolete copies, publish linked forms, complete training, define the first audit date and review revision dependencies.

## 18. Management checklist

Before releasing an AI-assisted SOP, confirm:

- the process was observed or otherwise validated;
- the purpose and scope are clear;
- process inputs and outputs are defined;
- one accountable owner is identified for each critical decision;
- role authority matches the approved delegation model;
- system-of-record fields are current;
- normal and exception paths are documented;
- evidence records are necessary and available;
- privacy/security-sensitive information is minimized;
- KPIs have definitions and denominators;
- dependent forms/checklists/work instructions are linked;
- training and competence verification are defined;
- field testing has been completed;
- revision history and review date are controlled;
- obsolete versions can be withdrawn.

## 19. Connected knowledge across Ahmed Quality Ops

Use this chapter together with **SOP Roles, Authority & RACI**, **SOP Exception & Escalation Management**, **How to Write a Professional SOP Procedure**, **Hotel Quality Audit AI Toolkit**, **Hotel Operations Manager AI Toolkit**, **Front Office AI Toolkit**, **Housekeeping Management AI Toolkit**, **Engineering & Maintenance AI Toolkit**, **Guest Complaint & Service Recovery AI Toolkit**, **Tourism Quality & SOP AI Toolkit**, **MICE Movement Control Room** and **Tourism Transport & Dispatch AI Toolkit**.

The knowledge network should let the reader move from a process problem to the relevant SOP, authority model, audit method, quality control and AI toolkit without returning to a generic search page.

## 20. Sources and evidence boundaries

Verified external context used in this chapter includes:

- **ISO — The Process Approach in ISO 9001:2015.** ISO describes process management as interrelated activities using inputs to deliver intended results, supported by PDCA and risk-based thinking.
- **ISO 10013:2021 — Quality management systems — Guidance for documented information.** ISO provides guidance for developing and maintaining documented information needed to support effective management-system processes and recognizes digital documentation environments.

Official links:
- https://www.iso.org/iso/iso9001_2015_process_approach.pdf
- https://www.iso.org/standard/75736.html

The fictional UAE property, workflow data, costs, thresholds and examples are illustrative. Hotels must validate their own process, authority, regulatory requirements, technology and document-control rules.


---

# 21. The 10 copy-ready prompts


## Prompt 111 — SOP Structure Builder

**Prompt ID:** `12-01-sop-structure-builder`  
**Department:** Quality / Operations / Process Owner  
**Risk level:** MEDIUM  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use

Build a controlled SOP architecture from a verified hotel process before detailed procedure drafting begins.

### Required inputs

- process purpose and scope
- process trigger and output
- current roles and systems
- approved policy/standard requirements
- known exceptions and records

### Expected outputs

- recommended document structure
- missing sections/inputs
- linked document hierarchy
- owner/approver fields
- document-control requirements

### Copy-ready prompt

```text
ROLE
Act as a senior hotel process-design and quality analyst supporting an accountable human process owner. Your role is process discovery support, structured drafting, control challenge and evidence design—not autonomous policy or authority creation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Process Owner / Quality Manager / Department Head / Supervisor / Other]
Accountable human owner/approver: [Insert authorized role]
Document owner: [Insert role]
Authority/delegation source: [Insert approved matrix/policy or mark missing]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Build a controlled SOP architecture from a verified hotel process before detailed procedure drafting begins.
Property type/location: [Insert confirmed property and jurisdiction]
Department/process: [Insert]
Guest/staff journey stage: [Insert]
Process trigger and intended output: [Insert]
Document level: [Policy / SOP / Work Instruction / Checklist / Form]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved information.
Required inputs:
- process purpose and scope
- process trigger and output
- current roles and systems
- approved policy/standard requirements
- known exceptions and records

For each source, record the system/document title, revision or extraction date, owner and scope.
If the actual process has not been observed or otherwise validated, label the affected steps UNVALIDATED.
If an essential input is missing, stale, contradictory or unconfirmed, place it in an EVIDENCE / DESIGN GAP section. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- recommended document structure
- missing sections/inputs
- linked document hierarchy
- owner/approver fields
- document-control requirements

Separate the response into:
1. CONFIRMED CURRENT-STATE FACTS
2. APPROVED REQUIREMENTS / POLICY
3. PROPOSED FUTURE-STATE DESIGN
4. EXCEPTIONS / ESCALATIONS
5. EVIDENCE / RECORDS
6. ASSUMPTIONS OR HYPOTHESES
7. GAPS / CONTRADICTIONS
8. HUMAN DECISIONS REQUIRED

For each critical step show, where relevant: ROLE / ACTION / SOURCE OR SYSTEM / DECISION CONDITION / REQUIRED EVIDENCE / ESCALATION.
Do not convert an AI recommendation into a controlled instruction until the process owner verifies it.

PROCESS-DESIGN CONTROL
Check for: unclear trigger; missing output; duplicate approval; undefined accountability; hidden handoff; missing exception path; impossible SLA; obsolete system reference; unnecessary record; privacy exposure; KPI without denominator; dependent document not updated.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not invent a process step merely to make the structure look complete.
Do not independently create legal, safety, security, financial, compensation, pricing, employment or regulatory authority.
Do not include unnecessary guest identity data, payment data, credentials, employee-sensitive data, security procedures or confidential contracts.
The output remains a draft until the process owner validates the workflow in the field and the authorized document approver releases the controlled revision.
```

### Human verification checklist

- Has the real process been observed or otherwise validated?
- Are role and authority assignments approved rather than inferred?
- Are normal, exception and escalation paths explicit?
- Are systems and records current?
- Are evidence requirements practical and necessary?
- Are privacy and security-sensitive data minimized?
- Are dependent documents/forms/training identified?
- Has the authorized process/document owner approved the output?

**Professional hotel trainer's note:** Test the design using one normal scenario, one exception scenario and one missing-information scenario before releasing the document.

---


## Prompt 112 — Procedure Draft Builder

**Prompt ID:** `12-02-procedure-draft-builder`  
**Department:** Quality / Operations / Process Owner  
**Risk level:** MEDIUM  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use

Convert a validated hotel process map into executable, auditable procedure steps with roles, systems, decisions and evidence.

### Required inputs

- validated current/future-state process map
- approved roles and authority
- system-of-record fields
- decision points and SLAs
- exception rules and evidence

### Expected outputs

- step-by-step procedure table
- role/action/source/evidence mapping
- decision logic
- exceptions/escalations
- unresolved validation points

### Copy-ready prompt

```text
ROLE
Act as a senior hotel process-design and quality analyst supporting an accountable human process owner. Your role is process discovery support, structured drafting, control challenge and evidence design—not autonomous policy or authority creation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Process Owner / Quality Manager / Department Head / Supervisor / Other]
Accountable human owner/approver: [Insert authorized role]
Document owner: [Insert role]
Authority/delegation source: [Insert approved matrix/policy or mark missing]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Convert a validated hotel process map into executable, auditable procedure steps with roles, systems, decisions and evidence.
Property type/location: [Insert confirmed property and jurisdiction]
Department/process: [Insert]
Guest/staff journey stage: [Insert]
Process trigger and intended output: [Insert]
Document level: [Policy / SOP / Work Instruction / Checklist / Form]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved information.
Required inputs:
- validated current/future-state process map
- approved roles and authority
- system-of-record fields
- decision points and SLAs
- exception rules and evidence

For each source, record the system/document title, revision or extraction date, owner and scope.
If the actual process has not been observed or otherwise validated, label the affected steps UNVALIDATED.
If an essential input is missing, stale, contradictory or unconfirmed, place it in an EVIDENCE / DESIGN GAP section. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- step-by-step procedure table
- role/action/source/evidence mapping
- decision logic
- exceptions/escalations
- unresolved validation points

Separate the response into:
1. CONFIRMED CURRENT-STATE FACTS
2. APPROVED REQUIREMENTS / POLICY
3. PROPOSED FUTURE-STATE DESIGN
4. EXCEPTIONS / ESCALATIONS
5. EVIDENCE / RECORDS
6. ASSUMPTIONS OR HYPOTHESES
7. GAPS / CONTRADICTIONS
8. HUMAN DECISIONS REQUIRED

For each critical step show, where relevant: ROLE / ACTION / SOURCE OR SYSTEM / DECISION CONDITION / REQUIRED EVIDENCE / ESCALATION.
Do not convert an AI recommendation into a controlled instruction until the process owner verifies it.

PROCESS-DESIGN CONTROL
Check for: unclear trigger; missing output; duplicate approval; undefined accountability; hidden handoff; missing exception path; impossible SLA; obsolete system reference; unnecessary record; privacy exposure; KPI without denominator; dependent document not updated.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not draft unobserved steps as facts. Mark every unvalidated step for process-owner confirmation.
Do not independently create legal, safety, security, financial, compensation, pricing, employment or regulatory authority.
Do not include unnecessary guest identity data, payment data, credentials, employee-sensitive data, security procedures or confidential contracts.
The output remains a draft until the process owner validates the workflow in the field and the authorized document approver releases the controlled revision.
```

### Human verification checklist

- Has the real process been observed or otherwise validated?
- Are role and authority assignments approved rather than inferred?
- Are normal, exception and escalation paths explicit?
- Are systems and records current?
- Are evidence requirements practical and necessary?
- Are privacy and security-sensitive data minimized?
- Are dependent documents/forms/training identified?
- Has the authorized process/document owner approved the output?

**Professional hotel trainer's note:** Test the design using one normal scenario, one exception scenario and one missing-information scenario before releasing the document.

---


## Prompt 113 — RACI Designer

**Prompt ID:** `12-03-raci-designer`  
**Department:** Quality / Operations / Process Owner  
**Risk level:** HIGH  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use

Design a RACI and authority-support view for a hotel process without assigning authority that management has not approved.

### Required inputs

- validated process steps
- approved organization roles
- delegation/authority matrix
- handoff points
- exception decisions

### Expected outputs

- RACI matrix
- single-accountability conflicts
- authority gaps
- consult/inform overload
- decisions needing delegation confirmation

### Copy-ready prompt

```text
ROLE
Act as a senior hotel process-design and quality analyst supporting an accountable human process owner. Your role is process discovery support, structured drafting, control challenge and evidence design—not autonomous policy or authority creation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Process Owner / Quality Manager / Department Head / Supervisor / Other]
Accountable human owner/approver: [Insert authorized role]
Document owner: [Insert role]
Authority/delegation source: [Insert approved matrix/policy or mark missing]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Design a RACI and authority-support view for a hotel process without assigning authority that management has not approved.
Property type/location: [Insert confirmed property and jurisdiction]
Department/process: [Insert]
Guest/staff journey stage: [Insert]
Process trigger and intended output: [Insert]
Document level: [Policy / SOP / Work Instruction / Checklist / Form]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved information.
Required inputs:
- validated process steps
- approved organization roles
- delegation/authority matrix
- handoff points
- exception decisions

For each source, record the system/document title, revision or extraction date, owner and scope.
If the actual process has not been observed or otherwise validated, label the affected steps UNVALIDATED.
If an essential input is missing, stale, contradictory or unconfirmed, place it in an EVIDENCE / DESIGN GAP section. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- RACI matrix
- single-accountability conflicts
- authority gaps
- consult/inform overload
- decisions needing delegation confirmation

Separate the response into:
1. CONFIRMED CURRENT-STATE FACTS
2. APPROVED REQUIREMENTS / POLICY
3. PROPOSED FUTURE-STATE DESIGN
4. EXCEPTIONS / ESCALATIONS
5. EVIDENCE / RECORDS
6. ASSUMPTIONS OR HYPOTHESES
7. GAPS / CONTRADICTIONS
8. HUMAN DECISIONS REQUIRED

For each critical step show, where relevant: ROLE / ACTION / SOURCE OR SYSTEM / DECISION CONDITION / REQUIRED EVIDENCE / ESCALATION.
Do not convert an AI recommendation into a controlled instruction until the process owner verifies it.

PROCESS-DESIGN CONTROL
Check for: unclear trigger; missing output; duplicate approval; undefined accountability; hidden handoff; missing exception path; impossible SLA; obsolete system reference; unnecessary record; privacy exposure; KPI without denominator; dependent document not updated.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not infer compensation, safety, pricing, employment or financial authority from job titles alone.
Do not independently create legal, safety, security, financial, compensation, pricing, employment or regulatory authority.
Do not include unnecessary guest identity data, payment data, credentials, employee-sensitive data, security procedures or confidential contracts.
The output remains a draft until the process owner validates the workflow in the field and the authorized document approver releases the controlled revision.
```

### Human verification checklist

- Has the real process been observed or otherwise validated?
- Are role and authority assignments approved rather than inferred?
- Are normal, exception and escalation paths explicit?
- Are systems and records current?
- Are evidence requirements practical and necessary?
- Are privacy and security-sensitive data minimized?
- Are dependent documents/forms/training identified?
- Has the authorized process/document owner approved the output?

**Professional hotel trainer's note:** Test the design using one normal scenario, one exception scenario and one missing-information scenario before releasing the document.

---


## Prompt 114 — Exception and Escalation Matrix

**Prompt ID:** `12-04-exception-and-escalation-matrix`  
**Department:** Quality / Operations / Process Owner  
**Risk level:** HIGH  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use

Turn known process failures and deviations into controlled exception paths with containment, owners, triggers and authorized options.

### Required inputs

- normal process
- known exception scenarios
- approved escalation thresholds
- authority/delegation rules
- service/safety/privacy constraints

### Expected outputs

- exception matrix
- containment actions
- escalation triggers
- authorized options
- evidence/closure requirements

### Copy-ready prompt

```text
ROLE
Act as a senior hotel process-design and quality analyst supporting an accountable human process owner. Your role is process discovery support, structured drafting, control challenge and evidence design—not autonomous policy or authority creation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Process Owner / Quality Manager / Department Head / Supervisor / Other]
Accountable human owner/approver: [Insert authorized role]
Document owner: [Insert role]
Authority/delegation source: [Insert approved matrix/policy or mark missing]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Turn known process failures and deviations into controlled exception paths with containment, owners, triggers and authorized options.
Property type/location: [Insert confirmed property and jurisdiction]
Department/process: [Insert]
Guest/staff journey stage: [Insert]
Process trigger and intended output: [Insert]
Document level: [Policy / SOP / Work Instruction / Checklist / Form]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved information.
Required inputs:
- normal process
- known exception scenarios
- approved escalation thresholds
- authority/delegation rules
- service/safety/privacy constraints

For each source, record the system/document title, revision or extraction date, owner and scope.
If the actual process has not been observed or otherwise validated, label the affected steps UNVALIDATED.
If an essential input is missing, stale, contradictory or unconfirmed, place it in an EVIDENCE / DESIGN GAP section. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- exception matrix
- containment actions
- escalation triggers
- authorized options
- evidence/closure requirements

Separate the response into:
1. CONFIRMED CURRENT-STATE FACTS
2. APPROVED REQUIREMENTS / POLICY
3. PROPOSED FUTURE-STATE DESIGN
4. EXCEPTIONS / ESCALATIONS
5. EVIDENCE / RECORDS
6. ASSUMPTIONS OR HYPOTHESES
7. GAPS / CONTRADICTIONS
8. HUMAN DECISIONS REQUIRED

For each critical step show, where relevant: ROLE / ACTION / SOURCE OR SYSTEM / DECISION CONDITION / REQUIRED EVIDENCE / ESCALATION.
Do not convert an AI recommendation into a controlled instruction until the process owner verifies it.

PROCESS-DESIGN CONTROL
Check for: unclear trigger; missing output; duplicate approval; undefined accountability; hidden handoff; missing exception path; impossible SLA; obsolete system reference; unnecessary record; privacy exposure; KPI without denominator; dependent document not updated.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not invent emergency, safety, compensation or legal escalation rules. Use only approved policy or flag the gap.
Do not independently create legal, safety, security, financial, compensation, pricing, employment or regulatory authority.
Do not include unnecessary guest identity data, payment data, credentials, employee-sensitive data, security procedures or confidential contracts.
The output remains a draft until the process owner validates the workflow in the field and the authorized document approver releases the controlled revision.
```

### Human verification checklist

- Has the real process been observed or otherwise validated?
- Are role and authority assignments approved rather than inferred?
- Are normal, exception and escalation paths explicit?
- Are systems and records current?
- Are evidence requirements practical and necessary?
- Are privacy and security-sensitive data minimized?
- Are dependent documents/forms/training identified?
- Has the authorized process/document owner approved the output?

**Professional hotel trainer's note:** Test the design using one normal scenario, one exception scenario and one missing-information scenario before releasing the document.

---


## Prompt 115 — SOP Evidence Record Designer

**Prompt ID:** `12-05-sop-evidence-record-designer`  
**Department:** Quality / Operations / Process Owner  
**Risk level:** MEDIUM  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use

Define the minimum evidence needed to prove critical hotel process steps without creating unnecessary paperwork or privacy exposure.

### Required inputs

- critical process steps
- risk/control points
- systems used
- existing forms/records
- retention/privacy requirements

### Expected outputs

- step-to-evidence matrix
- system-of-record recommendation
- missing record gaps
- privacy minimization notes
- retention/ownership questions

### Copy-ready prompt

```text
ROLE
Act as a senior hotel process-design and quality analyst supporting an accountable human process owner. Your role is process discovery support, structured drafting, control challenge and evidence design—not autonomous policy or authority creation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Process Owner / Quality Manager / Department Head / Supervisor / Other]
Accountable human owner/approver: [Insert authorized role]
Document owner: [Insert role]
Authority/delegation source: [Insert approved matrix/policy or mark missing]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Define the minimum evidence needed to prove critical hotel process steps without creating unnecessary paperwork or privacy exposure.
Property type/location: [Insert confirmed property and jurisdiction]
Department/process: [Insert]
Guest/staff journey stage: [Insert]
Process trigger and intended output: [Insert]
Document level: [Policy / SOP / Work Instruction / Checklist / Form]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved information.
Required inputs:
- critical process steps
- risk/control points
- systems used
- existing forms/records
- retention/privacy requirements

For each source, record the system/document title, revision or extraction date, owner and scope.
If the actual process has not been observed or otherwise validated, label the affected steps UNVALIDATED.
If an essential input is missing, stale, contradictory or unconfirmed, place it in an EVIDENCE / DESIGN GAP section. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- step-to-evidence matrix
- system-of-record recommendation
- missing record gaps
- privacy minimization notes
- retention/ownership questions

Separate the response into:
1. CONFIRMED CURRENT-STATE FACTS
2. APPROVED REQUIREMENTS / POLICY
3. PROPOSED FUTURE-STATE DESIGN
4. EXCEPTIONS / ESCALATIONS
5. EVIDENCE / RECORDS
6. ASSUMPTIONS OR HYPOTHESES
7. GAPS / CONTRADICTIONS
8. HUMAN DECISIONS REQUIRED

For each critical step show, where relevant: ROLE / ACTION / SOURCE OR SYSTEM / DECISION CONDITION / REQUIRED EVIDENCE / ESCALATION.
Do not convert an AI recommendation into a controlled instruction until the process owner verifies it.

PROCESS-DESIGN CONTROL
Check for: unclear trigger; missing output; duplicate approval; undefined accountability; hidden handoff; missing exception path; impossible SLA; obsolete system reference; unnecessary record; privacy exposure; KPI without denominator; dependent document not updated.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not request sensitive guest or employee data unless it is necessary, authorized and appropriate for the process.
Do not independently create legal, safety, security, financial, compensation, pricing, employment or regulatory authority.
Do not include unnecessary guest identity data, payment data, credentials, employee-sensitive data, security procedures or confidential contracts.
The output remains a draft until the process owner validates the workflow in the field and the authorized document approver releases the controlled revision.
```

### Human verification checklist

- Has the real process been observed or otherwise validated?
- Are role and authority assignments approved rather than inferred?
- Are normal, exception and escalation paths explicit?
- Are systems and records current?
- Are evidence requirements practical and necessary?
- Are privacy and security-sensitive data minimized?
- Are dependent documents/forms/training identified?
- Has the authorized process/document owner approved the output?

**Professional hotel trainer's note:** Test the design using one normal scenario, one exception scenario and one missing-information scenario before releasing the document.

---


## Prompt 116 — SOP KPI Designer

**Prompt ID:** `12-06-sop-kpi-designer`  
**Department:** Quality / Operations / Process Owner  
**Risk level:** MEDIUM  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use

Design process KPIs that measure the intended hotel outcome without rewarding shortcuts or hiding exceptions.

### Required inputs

- process objective
- critical controls
- available system data
- process volume/denominators
- known failure modes

### Expected outputs

- KPI definitions
- numerator/denominator
- source and frequency
- owner/threshold questions
- anti-gaming guardrails

### Copy-ready prompt

```text
ROLE
Act as a senior hotel process-design and quality analyst supporting an accountable human process owner. Your role is process discovery support, structured drafting, control challenge and evidence design—not autonomous policy or authority creation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Process Owner / Quality Manager / Department Head / Supervisor / Other]
Accountable human owner/approver: [Insert authorized role]
Document owner: [Insert role]
Authority/delegation source: [Insert approved matrix/policy or mark missing]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Design process KPIs that measure the intended hotel outcome without rewarding shortcuts or hiding exceptions.
Property type/location: [Insert confirmed property and jurisdiction]
Department/process: [Insert]
Guest/staff journey stage: [Insert]
Process trigger and intended output: [Insert]
Document level: [Policy / SOP / Work Instruction / Checklist / Form]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved information.
Required inputs:
- process objective
- critical controls
- available system data
- process volume/denominators
- known failure modes

For each source, record the system/document title, revision or extraction date, owner and scope.
If the actual process has not been observed or otherwise validated, label the affected steps UNVALIDATED.
If an essential input is missing, stale, contradictory or unconfirmed, place it in an EVIDENCE / DESIGN GAP section. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- KPI definitions
- numerator/denominator
- source and frequency
- owner/threshold questions
- anti-gaming guardrails

Separate the response into:
1. CONFIRMED CURRENT-STATE FACTS
2. APPROVED REQUIREMENTS / POLICY
3. PROPOSED FUTURE-STATE DESIGN
4. EXCEPTIONS / ESCALATIONS
5. EVIDENCE / RECORDS
6. ASSUMPTIONS OR HYPOTHESES
7. GAPS / CONTRADICTIONS
8. HUMAN DECISIONS REQUIRED

For each critical step show, where relevant: ROLE / ACTION / SOURCE OR SYSTEM / DECISION CONDITION / REQUIRED EVIDENCE / ESCALATION.
Do not convert an AI recommendation into a controlled instruction until the process owner verifies it.

PROCESS-DESIGN CONTROL
Check for: unclear trigger; missing output; duplicate approval; undefined accountability; hidden handoff; missing exception path; impossible SLA; obsolete system reference; unnecessary record; privacy exposure; KPI without denominator; dependent document not updated.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not invent targets. Separate proposed indicators from management-approved thresholds.
Do not independently create legal, safety, security, financial, compensation, pricing, employment or regulatory authority.
Do not include unnecessary guest identity data, payment data, credentials, employee-sensitive data, security procedures or confidential contracts.
The output remains a draft until the process owner validates the workflow in the field and the authorized document approver releases the controlled revision.
```

### Human verification checklist

- Has the real process been observed or otherwise validated?
- Are role and authority assignments approved rather than inferred?
- Are normal, exception and escalation paths explicit?
- Are systems and records current?
- Are evidence requirements practical and necessary?
- Are privacy and security-sensitive data minimized?
- Are dependent documents/forms/training identified?
- Has the authorized process/document owner approved the output?

**Professional hotel trainer's note:** Test the design using one normal scenario, one exception scenario and one missing-information scenario before releasing the document.

---


## Prompt 117 — Work Instruction Builder

**Prompt ID:** `12-07-work-instruction-builder`  
**Department:** Quality / Operations / Process Owner  
**Risk level:** MEDIUM  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use

Create a detailed work instruction for a specific hotel task that sits underneath an approved SOP.

### Required inputs

- approved SOP step
- task objective
- tools/equipment/system
- sequence and quality criteria
- safety/access constraints

### Expected outputs

- task sequence
- preconditions
- quality checks
- stop/escalate conditions
- required evidence

### Copy-ready prompt

```text
ROLE
Act as a senior hotel process-design and quality analyst supporting an accountable human process owner. Your role is process discovery support, structured drafting, control challenge and evidence design—not autonomous policy or authority creation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Process Owner / Quality Manager / Department Head / Supervisor / Other]
Accountable human owner/approver: [Insert authorized role]
Document owner: [Insert role]
Authority/delegation source: [Insert approved matrix/policy or mark missing]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Create a detailed work instruction for a specific hotel task that sits underneath an approved SOP.
Property type/location: [Insert confirmed property and jurisdiction]
Department/process: [Insert]
Guest/staff journey stage: [Insert]
Process trigger and intended output: [Insert]
Document level: [Policy / SOP / Work Instruction / Checklist / Form]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved information.
Required inputs:
- approved SOP step
- task objective
- tools/equipment/system
- sequence and quality criteria
- safety/access constraints

For each source, record the system/document title, revision or extraction date, owner and scope.
If the actual process has not been observed or otherwise validated, label the affected steps UNVALIDATED.
If an essential input is missing, stale, contradictory or unconfirmed, place it in an EVIDENCE / DESIGN GAP section. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- task sequence
- preconditions
- quality checks
- stop/escalate conditions
- required evidence

Separate the response into:
1. CONFIRMED CURRENT-STATE FACTS
2. APPROVED REQUIREMENTS / POLICY
3. PROPOSED FUTURE-STATE DESIGN
4. EXCEPTIONS / ESCALATIONS
5. EVIDENCE / RECORDS
6. ASSUMPTIONS OR HYPOTHESES
7. GAPS / CONTRADICTIONS
8. HUMAN DECISIONS REQUIRED

For each critical step show, where relevant: ROLE / ACTION / SOURCE OR SYSTEM / DECISION CONDITION / REQUIRED EVIDENCE / ESCALATION.
Do not convert an AI recommendation into a controlled instruction until the process owner verifies it.

PROCESS-DESIGN CONTROL
Check for: unclear trigger; missing output; duplicate approval; undefined accountability; hidden handoff; missing exception path; impossible SLA; obsolete system reference; unnecessary record; privacy exposure; KPI without denominator; dependent document not updated.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not provide technical, safety-critical or regulated instructions beyond the approved competent-person procedure supplied.
Do not independently create legal, safety, security, financial, compensation, pricing, employment or regulatory authority.
Do not include unnecessary guest identity data, payment data, credentials, employee-sensitive data, security procedures or confidential contracts.
The output remains a draft until the process owner validates the workflow in the field and the authorized document approver releases the controlled revision.
```

### Human verification checklist

- Has the real process been observed or otherwise validated?
- Are role and authority assignments approved rather than inferred?
- Are normal, exception and escalation paths explicit?
- Are systems and records current?
- Are evidence requirements practical and necessary?
- Are privacy and security-sensitive data minimized?
- Are dependent documents/forms/training identified?
- Has the authorized process/document owner approved the output?

**Professional hotel trainer's note:** Test the design using one normal scenario, one exception scenario and one missing-information scenario before releasing the document.

---


## Prompt 118 — Checklist Generator

**Prompt ID:** `12-08-checklist-generator`  
**Department:** Quality / Operations / Process Owner  
**Risk level:** MEDIUM  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use

Convert approved hotel SOP requirements into a practical execution or verification checklist with clear evidence and not-applicable logic.

### Required inputs

- approved SOP/standard
- critical steps
- inspection criteria
- evidence needs
- role and timing

### Expected outputs

- checklist items
- pass/fail/NA rules
- evidence fields
- critical fail flags
- sign-off/owner fields

### Copy-ready prompt

```text
ROLE
Act as a senior hotel process-design and quality analyst supporting an accountable human process owner. Your role is process discovery support, structured drafting, control challenge and evidence design—not autonomous policy or authority creation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Process Owner / Quality Manager / Department Head / Supervisor / Other]
Accountable human owner/approver: [Insert authorized role]
Document owner: [Insert role]
Authority/delegation source: [Insert approved matrix/policy or mark missing]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Convert approved hotel SOP requirements into a practical execution or verification checklist with clear evidence and not-applicable logic.
Property type/location: [Insert confirmed property and jurisdiction]
Department/process: [Insert]
Guest/staff journey stage: [Insert]
Process trigger and intended output: [Insert]
Document level: [Policy / SOP / Work Instruction / Checklist / Form]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved information.
Required inputs:
- approved SOP/standard
- critical steps
- inspection criteria
- evidence needs
- role and timing

For each source, record the system/document title, revision or extraction date, owner and scope.
If the actual process has not been observed or otherwise validated, label the affected steps UNVALIDATED.
If an essential input is missing, stale, contradictory or unconfirmed, place it in an EVIDENCE / DESIGN GAP section. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- checklist items
- pass/fail/NA rules
- evidence fields
- critical fail flags
- sign-off/owner fields

Separate the response into:
1. CONFIRMED CURRENT-STATE FACTS
2. APPROVED REQUIREMENTS / POLICY
3. PROPOSED FUTURE-STATE DESIGN
4. EXCEPTIONS / ESCALATIONS
5. EVIDENCE / RECORDS
6. ASSUMPTIONS OR HYPOTHESES
7. GAPS / CONTRADICTIONS
8. HUMAN DECISIONS REQUIRED

For each critical step show, where relevant: ROLE / ACTION / SOURCE OR SYSTEM / DECISION CONDITION / REQUIRED EVIDENCE / ESCALATION.
Do not convert an AI recommendation into a controlled instruction until the process owner verifies it.

PROCESS-DESIGN CONTROL
Check for: unclear trigger; missing output; duplicate approval; undefined accountability; hidden handoff; missing exception path; impossible SLA; obsolete system reference; unnecessary record; privacy exposure; KPI without denominator; dependent document not updated.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not convert subjective language into invented pass/fail criteria. Flag undefined standards.
Do not independently create legal, safety, security, financial, compensation, pricing, employment or regulatory authority.
Do not include unnecessary guest identity data, payment data, credentials, employee-sensitive data, security procedures or confidential contracts.
The output remains a draft until the process owner validates the workflow in the field and the authorized document approver releases the controlled revision.
```

### Human verification checklist

- Has the real process been observed or otherwise validated?
- Are role and authority assignments approved rather than inferred?
- Are normal, exception and escalation paths explicit?
- Are systems and records current?
- Are evidence requirements practical and necessary?
- Are privacy and security-sensitive data minimized?
- Are dependent documents/forms/training identified?
- Has the authorized process/document owner approved the output?

**Professional hotel trainer's note:** Test the design using one normal scenario, one exception scenario and one missing-information scenario before releasing the document.

---


## Prompt 119 — SOP Gap Audit

**Prompt ID:** `12-09-sop-gap-audit`  
**Department:** Quality / Operations / Process Owner  
**Risk level:** MEDIUM  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use

Compare a controlled hotel SOP with observed practice, system records and recent exceptions to identify obsolete, missing or impractical controls.

### Required inputs

- current approved SOP
- observation/interview notes
- system screenshots/exports
- recent incidents/complaints
- linked policies/forms

### Expected outputs

- gap matrix
- obsolete references
- hidden workarounds
- control/authority gaps
- revision priorities

### Copy-ready prompt

```text
ROLE
Act as a senior hotel process-design and quality analyst supporting an accountable human process owner. Your role is process discovery support, structured drafting, control challenge and evidence design—not autonomous policy or authority creation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Process Owner / Quality Manager / Department Head / Supervisor / Other]
Accountable human owner/approver: [Insert authorized role]
Document owner: [Insert role]
Authority/delegation source: [Insert approved matrix/policy or mark missing]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Compare a controlled hotel SOP with observed practice, system records and recent exceptions to identify obsolete, missing or impractical controls.
Property type/location: [Insert confirmed property and jurisdiction]
Department/process: [Insert]
Guest/staff journey stage: [Insert]
Process trigger and intended output: [Insert]
Document level: [Policy / SOP / Work Instruction / Checklist / Form]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved information.
Required inputs:
- current approved SOP
- observation/interview notes
- system screenshots/exports
- recent incidents/complaints
- linked policies/forms

For each source, record the system/document title, revision or extraction date, owner and scope.
If the actual process has not been observed or otherwise validated, label the affected steps UNVALIDATED.
If an essential input is missing, stale, contradictory or unconfirmed, place it in an EVIDENCE / DESIGN GAP section. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- gap matrix
- obsolete references
- hidden workarounds
- control/authority gaps
- revision priorities

Separate the response into:
1. CONFIRMED CURRENT-STATE FACTS
2. APPROVED REQUIREMENTS / POLICY
3. PROPOSED FUTURE-STATE DESIGN
4. EXCEPTIONS / ESCALATIONS
5. EVIDENCE / RECORDS
6. ASSUMPTIONS OR HYPOTHESES
7. GAPS / CONTRADICTIONS
8. HUMAN DECISIONS REQUIRED

For each critical step show, where relevant: ROLE / ACTION / SOURCE OR SYSTEM / DECISION CONDITION / REQUIRED EVIDENCE / ESCALATION.
Do not convert an AI recommendation into a controlled instruction until the process owner verifies it.

PROCESS-DESIGN CONTROL
Check for: unclear trigger; missing output; duplicate approval; undefined accountability; hidden handoff; missing exception path; impossible SLA; obsolete system reference; unnecessary record; privacy exposure; KPI without denominator; dependent document not updated.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not treat employee comments alone as proof of nonconformance; separate observation, evidence and interpretation.
Do not independently create legal, safety, security, financial, compensation, pricing, employment or regulatory authority.
Do not include unnecessary guest identity data, payment data, credentials, employee-sensitive data, security procedures or confidential contracts.
The output remains a draft until the process owner validates the workflow in the field and the authorized document approver releases the controlled revision.
```

### Human verification checklist

- Has the real process been observed or otherwise validated?
- Are role and authority assignments approved rather than inferred?
- Are normal, exception and escalation paths explicit?
- Are systems and records current?
- Are evidence requirements practical and necessary?
- Are privacy and security-sensitive data minimized?
- Are dependent documents/forms/training identified?
- Has the authorized process/document owner approved the output?

**Professional hotel trainer's note:** Test the design using one normal scenario, one exception scenario and one missing-information scenario before releasing the document.

---


## Prompt 120 — Document Revision Impact Review

**Prompt ID:** `12-10-document-revision-impact-review`  
**Department:** Quality / Operations / Process Owner  
**Risk level:** HIGH  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use

Assess the operational impact of a proposed SOP revision before release so dependent roles, systems, forms, training and KPIs are updated together.

### Required inputs

- current and proposed revisions
- change rationale
- linked documents/forms
- systems/workflows
- training and authority dependencies

### Expected outputs

- change-impact matrix
- affected roles/systems
- training updates
- dependent-document actions
- release/withdrawal checklist

### Copy-ready prompt

```text
ROLE
Act as a senior hotel process-design and quality analyst supporting an accountable human process owner. Your role is process discovery support, structured drafting, control challenge and evidence design—not autonomous policy or authority creation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Process Owner / Quality Manager / Department Head / Supervisor / Other]
Accountable human owner/approver: [Insert authorized role]
Document owner: [Insert role]
Authority/delegation source: [Insert approved matrix/policy or mark missing]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Assess the operational impact of a proposed SOP revision before release so dependent roles, systems, forms, training and KPIs are updated together.
Property type/location: [Insert confirmed property and jurisdiction]
Department/process: [Insert]
Guest/staff journey stage: [Insert]
Process trigger and intended output: [Insert]
Document level: [Policy / SOP / Work Instruction / Checklist / Form]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved information.
Required inputs:
- current and proposed revisions
- change rationale
- linked documents/forms
- systems/workflows
- training and authority dependencies

For each source, record the system/document title, revision or extraction date, owner and scope.
If the actual process has not been observed or otherwise validated, label the affected steps UNVALIDATED.
If an essential input is missing, stale, contradictory or unconfirmed, place it in an EVIDENCE / DESIGN GAP section. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- change-impact matrix
- affected roles/systems
- training updates
- dependent-document actions
- release/withdrawal checklist

Separate the response into:
1. CONFIRMED CURRENT-STATE FACTS
2. APPROVED REQUIREMENTS / POLICY
3. PROPOSED FUTURE-STATE DESIGN
4. EXCEPTIONS / ESCALATIONS
5. EVIDENCE / RECORDS
6. ASSUMPTIONS OR HYPOTHESES
7. GAPS / CONTRADICTIONS
8. HUMAN DECISIONS REQUIRED

For each critical step show, where relevant: ROLE / ACTION / SOURCE OR SYSTEM / DECISION CONDITION / REQUIRED EVIDENCE / ESCALATION.
Do not convert an AI recommendation into a controlled instruction until the process owner verifies it.

PROCESS-DESIGN CONTROL
Check for: unclear trigger; missing output; duplicate approval; undefined accountability; hidden handoff; missing exception path; impossible SLA; obsolete system reference; unnecessary record; privacy exposure; KPI without denominator; dependent document not updated.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not approve the revision. Identify impacts and decisions for the document owner and authorized approver.
Do not independently create legal, safety, security, financial, compensation, pricing, employment or regulatory authority.
Do not include unnecessary guest identity data, payment data, credentials, employee-sensitive data, security procedures or confidential contracts.
The output remains a draft until the process owner validates the workflow in the field and the authorized document approver releases the controlled revision.
```

### Human verification checklist

- Has the real process been observed or otherwise validated?
- Are role and authority assignments approved rather than inferred?
- Are normal, exception and escalation paths explicit?
- Are systems and records current?
- Are evidence requirements practical and necessary?
- Are privacy and security-sensitive data minimized?
- Are dependent documents/forms/training identified?
- Has the authorized process/document owner approved the output?

**Professional hotel trainer's note:** Test the design using one normal scenario, one exception scenario and one missing-information scenario before releasing the document.

---
