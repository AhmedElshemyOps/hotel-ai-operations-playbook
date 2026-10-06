# Article 13 — Lean Six Sigma for Hotel Operations AI Toolkit

## 10 Professional AI Prompts for DMAIC, VOC/CTQ, Pareto, Root Cause, FMEA, COPQ, Capability and Control

**Track C · Hotel & Serviced Apartment AI Operations Playbook · Lean Six Sigma chapter**

Hotels generate operational variation every day: arrival peaks, late departures, room-readiness delays, repeat defects, complaint categories, housekeeping rework, maintenance revisits, utility spikes, inventory shortages, long-stay exceptions and service-recovery cases.

That does not mean every variation deserves a Six Sigma project.

Lean Six Sigma becomes useful when management can define a real process problem, measure it consistently, understand what matters to the guest or business, test causes rather than guess them, improve the process and hold the gain.

The operating principle for this chapter is:

> **AI may accelerate structured problem-solving. It must not manufacture data, convert correlation into causation, invent statistical significance, create financial savings, or replace the process owner’s judgment.**

The ten prompts follow one improvement cycle:

> **Charter → VOC/CTQ → Measure → Prioritize → Hypothesize → Analyze risk → Quantify waste → Test capability → Control → Prioritize the next improvement**

This chapter continues the fictional 60-unit UAE serviced-apartment case used throughout the playbook. All property figures, costs and performance examples are illustrative unless specifically linked to a verified external source.

---

## 1. Lean Six Sigma in hotels: improve the process, not the PowerPoint

Hospitality teams often know Lean Six Sigma through tool names: DMAIC, Pareto, fishbone, FMEA, control charts, capability, 5S and kaizen. The risk is turning those tools into presentation exercises.

A hotel improvement project should begin with an operational question:

- What is failing or varying?
- Who experiences the impact?
- What process creates the outcome?
- How do we define a defect?
- What is the denominator?
- Is the measurement trustworthy?
- What causes are plausible?
- Which causes can we actually test?
- What change can be piloted?
- How will we know the improvement held?

ASQ describes DMAIC as a structured method for improving existing processes that do not meet performance standards or customer expectations, with Define, Measure, Analyze, Improve and Control building on one another. Its Measure phase emphasizes understanding the real process, validating measurement and establishing a trustworthy baseline. In hotels this matters because operational data are often split across PMS, CMMS, CRM, housekeeping records and manual handovers.

The most useful role for AI is therefore not “be my Black Belt and tell me the answer.” It is to structure the problem, challenge definitions, expose missing data, organize observations, calculate transparently, generate testable hypotheses, compare evidence and document the control plan.

## 2. The Lean Six Sigma HOTEL model

**H — Hospitality role & human owner**  
Who sponsors the project? Who owns the process? Who provides subject-matter expertise? Who reviews statistics? Who validates financial benefits?

**O — Operational objective & context**  
Which process, department, property, guest journey, period and population are being studied? Is this a DMAIC project, kaizen event, routine quality review or new-process design problem?

**T — Trusted inputs & sources of truth**  
Which PMS, CMMS, Finance, CRM, housekeeping, survey or approved operational records define the baseline? Are definitions stable? Are timestamps, units, exclusions and denominators known?

**E — Expected output, exceptions & evidence**  
What decision must the analysis support? What formula or method is being used? Which assumptions and data-quality issues must remain visible?

**L — Limits, privacy & leadership approval**  
What may AI not conclude or authorize? Which analyses require qualified statistical, financial, engineering, HR, safety or legal review?

The improvement system should never allow a language model to convert a neat table into authority.

## 3. Fictional UAE case: room readiness as a DMAIC project

Continue with the fictional 60-unit serviced-apartment operation.

Management believes room-readiness delays are creating guest dissatisfaction, coordination work and occasional compensation. The weak project statement would be:

> “Housekeeping is too slow. Improve room readiness.”

That statement is not ready for DMAIC. It assumes a cause, blames one department and provides no measurable definition.

A stronger draft statement would say that, during a defined study period, a measured proportion of relevant arrivals was not released by an approved readiness threshold, with the baseline and denominator to be confirmed from PMS, housekeeping and engineering records before the charter is approved.

The team may later discover several contributors: late departures, cleaning workload, inspection queues, engineering blockers, linen constraints, room moves, access issues, inaccurate ETA assumptions, weak handover or inconsistent status updates.

The point of DMAIC is to discover which factors actually matter.

## 4. Define: the charter prevents the project from becoming everything

Prompt 121 builds the DMAIC charter.

A professional charter should contain the problem statement, customer impact, measurable baseline field, target field, in/out-of-scope boundaries, start/end points, sponsor, process owner, improvement lead, stakeholders, timeline, constraints, initial risks, benefit hypothesis and data gaps.

“Reduce operational problems across the hotel” is not a project.

“Reduce repeat work orders for a defined asset family” may be.

Scope protects the team from endless analysis.

## 5. Voice of the Customer is not the same as a list of comments

Prompt 122 converts verified VOC into CTQs.

Hospitality organizations collect guest voice through surveys, reviews, complaint logs, call/chat records, corporate-client feedback, long-stay reviews, mystery guest programs and account meetings.

The danger is treating a set of comments as representative when it may be self-selected.

If several guests say “communication was slow” during maintenance cases, that observation can support a theme. It does not prove all maintenance cases have the problem.

A CTQ might become: percentage of guest-impacting work orders where a verified status update is sent within the approved interval.

Now the team needs a start event, timestamp, interval, denominator, exclusions, source system and process owner.

## 6. Defect definitions determine whether the data mean anything

Before a Pareto, capability calculation or trend chart is useful, the team needs a stable defect definition.

“Room readiness failure” could mean not released by 14:00, not released by confirmed arrival, not released by contractual check-in, released with a blocking defect, a guest wait due to status mismatch, or a room reclean after inspection failure.

These are not interchangeable.

Definition drift also affects complaint categories, repeat maintenance, first-time fix, reclean, no-show, SLA breach, compensation and utility anomalies.

AI should challenge definition drift before comparing periods.

## 7. Measure: denominators matter more than impressive percentages

A hotel may report “20 room-readiness complaints this month.” That number is incomplete.

Twenty out of how many relevant arrivals?

Useful denominators include per 100 arrivals, occupied room nights, work orders, departures, housekeeping services, audited opportunities or another exposure measure matched to the process.

AI can calculate rates. The process owner must approve the operational definition.

## 8. Pareto analysis: focus, not mythology

Prompt 123 supports Pareto analysis.

A Pareto chart is useful because it compares categories rather than letting the most recent issue dominate attention. But the 80/20 idea should not become a target that the data are forced to fit.

The analyst should also ask whether frequency is the right measure. A low-frequency life-safety defect cannot be deprioritized because it sits low on a frequency Pareto. Cost, downtime, severity or risk views may be needed alongside frequency.

## 9. Analyze: hypotheses are not root causes

Prompt 124 builds a root-cause hypothesis register.

A root cause should survive a test.

For a room-readiness delay, possible hypotheses might include same-day turnover volume, late departures, engineering visibility, inspection capacity, linen timing, unreliable ETA data or workload allocation.

Each hypothesis should include evidence for, evidence against, required data, proposed test, confounders and subject-matter owner.

AI is excellent at generating possibilities. It is not evidence that those possibilities are true.

## 10. Fishbone: organize causes without creating groupthink

Prompt 125 facilitates a fishbone session.

Cause families can include People, Process, Technology/System, Materials/Inventory, Equipment, Environment, Measurement and Management/Policy. The categories should fit the process instead of copying a manufacturing template mechanically.

The facilitator should preserve minority views, contradictions, unknown branches and questions needing evidence.

The fishbone is a hypothesis map, not a voting contest.

## 11. FMEA: prioritize failure risk without outsourcing judgment

Prompt 126 drafts a process FMEA.

Hotels contain many handoff failures: reservation notes not reaching Front Office, fixed engineering defects not reflected in room status, cleaned rooms not inspected, guest requests without owners, compensation promises above authority or transport changes not reaching hotel arrival planning.

A draft FMEA can organize Process step → Failure mode → Effect → Cause → Prevention control → Detection control → Owner.

If the property uses Severity, Occurrence and Detection scores, AI should not invent them. A safety-sensitive failure may require specialist review regardless of RPN.

AI can ask better questions. It cannot accept risk.

## 12. Cost of Poor Quality: quantify waste without inventing savings

Prompt 127 structures COPQ.

Hotel COPQ may include reclean labor, repeated engineering visits, outsourced emergency repairs, room downtime, guest compensation, refunds, replacement items, express laundry, wasted amenities, duplicated administrative handling, overtime and avoidable recovery cost.

The model should distinguish hard savings, cost avoidance, capacity benefit and revenue impact.

AI should never present all four as “cash saved.”

## 13. Illustrative COPQ calculation

Use an illustrative example only.

Assume the fictional property records 18 repeat housekeeping recleans at AED 45 incremental handling cost, 7 repeat engineering visits at AED 85 incremental cost, and 3 service-recovery credits averaging AED 120.

Recleans: 18 × 45 = **AED 810**

Repeat visits: 7 × 85 = **AED 595**

Recovery credits: 3 × 120 = **AED 360**

Illustrative monthly COPQ = **AED 1,765**

This is not a benchmark or real-property claim. Finance should validate costs, exclusions and potential overlap.

## 14. Capability: a mean is not a capable process

Prompt 128 is intentionally conservative.

Before capability analysis, ask whether the CTQ is appropriate, specification limits are real requirements, the process is sufficiently stable, the measurement system is adequate, process segmentation is understood, assumptions are suitable and sample size is adequate.

A management target is not automatically a specification limit. A control limit is not a specification limit.

AI can prepare a capability review plan. Statistical interpretation should be reviewed by someone competent in the method.

## 15. Control charts: do not confuse common and special causes

A process can move up and down every day without being “out of control.” Conversely, an average may look stable while a special-cause signal is emerging.

A hotel might monitor room-ready time, check-in duration, work-order response time, reclean rate, complaint update interval, linen loss or occupancy-normalized utility consumption.

The chart type depends on the data. The purpose is to distinguish signal from routine variation, not to create decorative analytics.

## 16. Improve: pilot before scaling

Before full rollout, define the pilot area, owner, start/end dates, expected mechanism, measures, balancing measures, risks, training, rollback condition, guest-protection rule and evidence required.

Improvement is experimentation with controls.

## 17. Control: hold the gain or the project is not finished

Prompt 129 creates the control plan.

A useful control plan connects the CTQ, metric definition, source, owner, review frequency, approved threshold, reaction plan, evidence record, SOP and audit linkage.

Control planning prevents the improvement from living only in a project file.

## 18. Kaizen: prioritize manageable improvements without ignoring risk

Prompt 130 prioritizes a backlog.

A prioritization matrix may consider guest impact, defect reduction, effort, implementation time, dependency complexity, reversibility, data confidence, staff burden, financial impact and strategic alignment.

Risk is a gate, not just another weighted score. Privacy, safety and regulatory issues must not be pushed down because they have low ROI.

## 19. Lean waste in hotel operations

Hotel examples include waiting for verified status, excess employee motion to locate supplies, unnecessary transportation of items, duplicate data entry, excess or expiring inventory, recleans and repeat repairs, unused reports and frontline expertise that is never incorporated into process design.

Some apparently “extra” work is necessary control work. Validate before removing it.

## 20. AI failure modes in Lean Six Sigma

Common AI failure modes include false precision, definition drift, cause inflation, statistical-method mismatch, benefit inflation, confirmation bias and data leakage.

The control is simple: **make the method, data, assumptions and human reviewer visible.**

## 21. KPI dashboard for an improvement program

Useful governance KPIs include active DMAIC projects, projects with validated baseline, projects with approved CTQ, validated root causes, pilot success rate, sustained-control rate, Finance-verified benefits, COPQ reduction, overdue control actions and data-quality defects.

A dashboard should not reward project volume.

## 22. 30-day implementation plan

**Days 1–5 — Select and define:** choose one process problem, identify sponsor/process owner, draft the charter, define boundaries and list data gaps.

**Days 6–10 — Measure:** validate defect/denominator definitions, map the current process, verify extraction, capture VOC/CTQs and build the first Pareto.

**Days 11–15 — Analyze:** stratify the data, run cause workshops, draft an FMEA and identify tests that can confirm or reject hypotheses.

**Days 16–20 — Quantify and design:** structure COPQ, review capability prerequisites, select a pilot and define balancing measures.

**Days 21–25 — Pilot:** implement the approved pilot, capture before/after data, observe unintended effects and keep exceptions visible.

**Days 26–30 — Control:** build the control plan, transfer approved changes into SOP/training, prioritize the next kaizen backlog and validate benefits where applicable.

## 23. Management checklist

Before accepting an AI-supported Lean Six Sigma output, verify the problem is measurable, process boundaries are clear, defect definition is stable, denominator matches exposure, data sources are traceable, VOC limitations are visible, CTQs have definitions, calculations show assumptions, Pareto categories are consistent, root causes are tested, FMEA scoring follows the approved scale, capability prerequisites are met, COPQ avoids double counting, Finance validates financial benefits, pilots have balancing measures, control plans have owners, sensitive data are minimized and final decisions remain human.

## 24. Connected knowledge across Ahmed Quality Ops

Use this chapter with Hotel Quality Audit AI Toolkit, Hotel SOP & Process Design AI Toolkit, Hotel Complaint & Service Recovery AI Toolkit, Housekeeping Management AI Toolkit, Engineering & Maintenance AI Toolkit, Predictive Maintenance AI Toolkit, Hotel KPI & Dashboard AI Toolkit, SOP Exception & Escalation Management, SOP Roles/Authority/RACI and the Tourism Quality & SOP AI Toolkit.

The knowledge flow should be:

> **Audit detects → DMAIC learns → process changes → SOP controls → KPI monitors → audit verifies**

## 25. Sources and evidence boundaries

External methodology context is grounded in ASQ’s DMAIC and Six Sigma resources. The 60-unit UAE scenario, costs, defect counts and calculations in this chapter are illustrative operating examples and do not represent a specific hotel's actual performance.

## 26. The 10 copy-ready prompts

The prompt library below uses the HOTEL framework and explicit Lean Six Sigma guardrails.

## Prompt 121 — DMAIC Project Charter Builder

**Prompt ID:** `13-01-dmaic-project-charter-builder`  
**Department:** Quality / Process Improvement  
**Risk level:** Medium  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use
Define a hotel improvement project before analysis begins, with a measurable problem, scope, customer impact, baseline, goal, team and decision rights.

**Example:** A 60-unit serviced-apartment operation wants to reduce room-readiness delays without turning the project into a general 'fix housekeeping' initiative.

### Required inputs
- verified problem statement
- process scope and boundaries
- baseline metric and denominator
- VOC/guest or stakeholder impact
- business impact
- project sponsor and process owner
- known constraints and timeline

### Expected outputs
- DMAIC charter
- problem and goal statements
- in/out-of-scope boundaries
- baseline and target fields
- stakeholder/team map
- initial risks and evidence gaps

### Copy-ready prompt

```text
ROLE
Act as a senior Lean Six Sigma and hotel operations improvement analyst supporting an accountable human process owner. Your role is structured problem-solving, data challenge and improvement support—not autonomous operational, statistical, financial or safety authority.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Process Improvement Lead / Quality Manager / Department Head / Black Belt / Green Belt / Other]
Accountable process owner/sponsor: [Insert authorized role]
Qualified statistical/technical reviewer when required: [Insert role]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Define a hotel improvement project before analysis begins, with a measurable problem, scope, customer impact, baseline, goal, team and decision rights.
Property type/location: [Insert confirmed property and jurisdiction]
Process/department: [Insert]
Project phase: [Define / Measure / Analyze / Improve / Control]
Study period and population: [Insert]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved hotel records.
Required inputs:
- verified problem statement
- process scope and boundaries
- baseline metric and denominator
- VOC/guest or stakeholder impact
- business impact
- project sponsor and process owner
- known constraints and timeline

For every dataset or source record, state the system/document, extraction or revision date, owner, unit of analysis and relevant denominator.
If definitions changed between periods, expose the change before comparing results.
If an essential input is missing, stale, contradictory, biased or unverified, place it in a DATA / EVIDENCE GAP section. Do not guess or manufacture observations.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- DMAIC charter
- problem and goal statements
- in/out-of-scope boundaries
- baseline and target fields
- stakeholder/team map
- initial risks and evidence gaps

Separate the response into CONFIRMED FACTS; OPERATIONAL DEFINITIONS; CALCULATIONS / OBSERVED PATTERNS; HYPOTHESES; RECOMMENDATIONS; DATA / EVIDENCE GAPS; RISKS / EXCEPTIONS; HUMAN DECISIONS REQUIRED.
Show formulas, denominators, filters, exclusions and assumptions whenever a calculation is used.
Do not treat correlation as causation, a small sample as population truth, or an average as evidence of process stability.
Where a statistical method is proposed, state the prerequisites and ask for qualified review if those prerequisites are uncertain.

LEAN SIX SIGMA CONTROL
Do not invent a baseline, target, savings figure or root cause. If the problem statement is not measurable, rewrite it as a draft and list the evidence needed before approval.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently authorize guest compensation, staffing or disciplinary action, pricing, budget release, safety acceptance, regulatory conclusions, technical return-to-service or final project benefits.
Do not expose unnecessary guest identity data, employee personal data, payment information, credentials, security-sensitive details or confidential contracts.
Statistical conclusions that affect material financial, safety, regulatory or employment decisions require review by the accountable qualified role.
The output remains a draft until the process owner verifies the evidence and authorizes the next action.
```

### Human verification checklist
- Are the process, defect and denominator definitions approved?
- Is the dataset current, traceable and suitable for the method?
- Are assumptions separated from observed facts?
- Are hypotheses clearly labelled until tested?
- Are statistical prerequisites visible?
- Are financial, safety or regulatory conclusions reviewed by the qualified owner?
- Has the accountable process owner approved the next action?


## Prompt 122 — VOC to CTQ Converter

**Prompt ID:** `13-02-voc-to-ctq-converter`  
**Department:** Quality / Process Improvement  
**Risk level:** Medium  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use
Translate verified guest, client or internal-customer needs into measurable critical-to-quality requirements without treating every comment as equally representative.

**Example:** Guests frequently say 'communication was slow' during maintenance cases; the team needs a measurable CTQ rather than a vague satisfaction statement.

### Required inputs
- approved VOC sources
- sample period and population
- verbatim themes or coded feedback
- service promise/standard
- available operational measures
- segment/context definitions

### Expected outputs
- VOC theme table
- need-to-CTQ translation
- operational definition for each CTQ
- candidate measure and denominator
- evidence gaps
- validation questions

### Copy-ready prompt

```text
ROLE
Act as a senior Lean Six Sigma and hotel operations improvement analyst supporting an accountable human process owner. Your role is structured problem-solving, data challenge and improvement support—not autonomous operational, statistical, financial or safety authority.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Process Improvement Lead / Quality Manager / Department Head / Black Belt / Green Belt / Other]
Accountable process owner/sponsor: [Insert authorized role]
Qualified statistical/technical reviewer when required: [Insert role]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Translate verified guest, client or internal-customer needs into measurable critical-to-quality requirements without treating every comment as equally representative.
Property type/location: [Insert confirmed property and jurisdiction]
Process/department: [Insert]
Project phase: [Define / Measure / Analyze / Improve / Control]
Study period and population: [Insert]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved hotel records.
Required inputs:
- approved VOC sources
- sample period and population
- verbatim themes or coded feedback
- service promise/standard
- available operational measures
- segment/context definitions

For every dataset or source record, state the system/document, extraction or revision date, owner, unit of analysis and relevant denominator.
If definitions changed between periods, expose the change before comparing results.
If an essential input is missing, stale, contradictory, biased or unverified, place it in a DATA / EVIDENCE GAP section. Do not guess or manufacture observations.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- VOC theme table
- need-to-CTQ translation
- operational definition for each CTQ
- candidate measure and denominator
- evidence gaps
- validation questions

Separate the response into CONFIRMED FACTS; OPERATIONAL DEFINITIONS; CALCULATIONS / OBSERVED PATTERNS; HYPOTHESES; RECOMMENDATIONS; DATA / EVIDENCE GAPS; RISKS / EXCEPTIONS; HUMAN DECISIONS REQUIRED.
Show formulas, denominators, filters, exclusions and assumptions whenever a calculation is used.
Do not treat correlation as causation, a small sample as population truth, or an average as evidence of process stability.
Where a statistical method is proposed, state the prerequisites and ask for qualified review if those prerequisites are uncertain.

LEAN SIX SIGMA CONTROL
Keep stated guest needs separate from analyst interpretation. Do not infer population-wide importance from a small or biased sample.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently authorize guest compensation, staffing or disciplinary action, pricing, budget release, safety acceptance, regulatory conclusions, technical return-to-service or final project benefits.
Do not expose unnecessary guest identity data, employee personal data, payment information, credentials, security-sensitive details or confidential contracts.
Statistical conclusions that affect material financial, safety, regulatory or employment decisions require review by the accountable qualified role.
The output remains a draft until the process owner verifies the evidence and authorizes the next action.
```

### Human verification checklist
- Are the process, defect and denominator definitions approved?
- Is the dataset current, traceable and suitable for the method?
- Are assumptions separated from observed facts?
- Are hypotheses clearly labelled until tested?
- Are statistical prerequisites visible?
- Are financial, safety or regulatory conclusions reviewed by the qualified owner?
- Has the accountable process owner approved the next action?


## Prompt 123 — Pareto Analyzer

**Prompt ID:** `13-03-pareto-analyzer`  
**Department:** Quality / Process Improvement  
**Risk level:** Medium  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use
Identify the few categories contributing most to a defined hotel defect, complaint, delay or rework burden using consistent categories and denominators.

**Example:** The hotel wants to know whether AC, plumbing, housekeeping, access or communication issues account for most repeat service-recovery workload.

### Required inputs
- clean event-level dataset or approved summary
- category definitions
- time period
- denominator/exposure where relevant
- cost or severity field if used
- data-quality notes

### Expected outputs
- ranked frequency table
- cumulative contribution
- cost/severity Pareto if justified
- category-definition warnings
- recommended focus areas
- questions for validation

### Copy-ready prompt

```text
ROLE
Act as a senior Lean Six Sigma and hotel operations improvement analyst supporting an accountable human process owner. Your role is structured problem-solving, data challenge and improvement support—not autonomous operational, statistical, financial or safety authority.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Process Improvement Lead / Quality Manager / Department Head / Black Belt / Green Belt / Other]
Accountable process owner/sponsor: [Insert authorized role]
Qualified statistical/technical reviewer when required: [Insert role]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Identify the few categories contributing most to a defined hotel defect, complaint, delay or rework burden using consistent categories and denominators.
Property type/location: [Insert confirmed property and jurisdiction]
Process/department: [Insert]
Project phase: [Define / Measure / Analyze / Improve / Control]
Study period and population: [Insert]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved hotel records.
Required inputs:
- clean event-level dataset or approved summary
- category definitions
- time period
- denominator/exposure where relevant
- cost or severity field if used
- data-quality notes

For every dataset or source record, state the system/document, extraction or revision date, owner, unit of analysis and relevant denominator.
If definitions changed between periods, expose the change before comparing results.
If an essential input is missing, stale, contradictory, biased or unverified, place it in a DATA / EVIDENCE GAP section. Do not guess or manufacture observations.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- ranked frequency table
- cumulative contribution
- cost/severity Pareto if justified
- category-definition warnings
- recommended focus areas
- questions for validation

Separate the response into CONFIRMED FACTS; OPERATIONAL DEFINITIONS; CALCULATIONS / OBSERVED PATTERNS; HYPOTHESES; RECOMMENDATIONS; DATA / EVIDENCE GAPS; RISKS / EXCEPTIONS; HUMAN DECISIONS REQUIRED.
Show formulas, denominators, filters, exclusions and assumptions whenever a calculation is used.
Do not treat correlation as causation, a small sample as population truth, or an average as evidence of process stability.
Where a statistical method is proposed, state the prerequisites and ask for qualified review if those prerequisites are uncertain.

LEAN SIX SIGMA CONTROL
Do not combine unlike categories merely to create an 80/20 story. State whether the Pareto is based on count, cost, time, severity or another measure.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently authorize guest compensation, staffing or disciplinary action, pricing, budget release, safety acceptance, regulatory conclusions, technical return-to-service or final project benefits.
Do not expose unnecessary guest identity data, employee personal data, payment information, credentials, security-sensitive details or confidential contracts.
Statistical conclusions that affect material financial, safety, regulatory or employment decisions require review by the accountable qualified role.
The output remains a draft until the process owner verifies the evidence and authorizes the next action.
```

### Human verification checklist
- Are the process, defect and denominator definitions approved?
- Is the dataset current, traceable and suitable for the method?
- Are assumptions separated from observed facts?
- Are hypotheses clearly labelled until tested?
- Are statistical prerequisites visible?
- Are financial, safety or regulatory conclusions reviewed by the qualified owner?
- Has the accountable process owner approved the next action?


## Prompt 124 — Root-Cause Hypothesis Builder

**Prompt ID:** `13-04-root-cause-hypothesis-builder`  
**Department:** Quality / Process Improvement  
**Risk level:** Medium  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use
Generate testable root-cause hypotheses from a verified problem pattern without presenting plausible explanations as proven causes.

**Example:** Room-not-ready delays are concentrated on high-turnover days; the team needs hypotheses about staffing, sequence, engineering blocks, late departures and inspection capacity.

### Required inputs
- validated problem definition
- process map
- stratified data
- timeline
- known changes
- subject-matter observations
- prior tests or findings

### Expected outputs
- hypothesis register
- evidence for/against each hypothesis
- required test or observation
- confounders
- priority for investigation
- human SME questions

### Copy-ready prompt

```text
ROLE
Act as a senior Lean Six Sigma and hotel operations improvement analyst supporting an accountable human process owner. Your role is structured problem-solving, data challenge and improvement support—not autonomous operational, statistical, financial or safety authority.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Process Improvement Lead / Quality Manager / Department Head / Black Belt / Green Belt / Other]
Accountable process owner/sponsor: [Insert authorized role]
Qualified statistical/technical reviewer when required: [Insert role]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Generate testable root-cause hypotheses from a verified problem pattern without presenting plausible explanations as proven causes.
Property type/location: [Insert confirmed property and jurisdiction]
Process/department: [Insert]
Project phase: [Define / Measure / Analyze / Improve / Control]
Study period and population: [Insert]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved hotel records.
Required inputs:
- validated problem definition
- process map
- stratified data
- timeline
- known changes
- subject-matter observations
- prior tests or findings

For every dataset or source record, state the system/document, extraction or revision date, owner, unit of analysis and relevant denominator.
If definitions changed between periods, expose the change before comparing results.
If an essential input is missing, stale, contradictory, biased or unverified, place it in a DATA / EVIDENCE GAP section. Do not guess or manufacture observations.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- hypothesis register
- evidence for/against each hypothesis
- required test or observation
- confounders
- priority for investigation
- human SME questions

Separate the response into CONFIRMED FACTS; OPERATIONAL DEFINITIONS; CALCULATIONS / OBSERVED PATTERNS; HYPOTHESES; RECOMMENDATIONS; DATA / EVIDENCE GAPS; RISKS / EXCEPTIONS; HUMAN DECISIONS REQUIRED.
Show formulas, denominators, filters, exclusions and assumptions whenever a calculation is used.
Do not treat correlation as causation, a small sample as population truth, or an average as evidence of process stability.
Where a statistical method is proposed, state the prerequisites and ask for qualified review if those prerequisites are uncertain.

LEAN SIX SIGMA CONTROL
Every proposed cause must remain HYPOTHESIS until supported by evidence. Do not assign individual blame from outcome data.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently authorize guest compensation, staffing or disciplinary action, pricing, budget release, safety acceptance, regulatory conclusions, technical return-to-service or final project benefits.
Do not expose unnecessary guest identity data, employee personal data, payment information, credentials, security-sensitive details or confidential contracts.
Statistical conclusions that affect material financial, safety, regulatory or employment decisions require review by the accountable qualified role.
The output remains a draft until the process owner verifies the evidence and authorizes the next action.
```

### Human verification checklist
- Are the process, defect and denominator definitions approved?
- Is the dataset current, traceable and suitable for the method?
- Are assumptions separated from observed facts?
- Are hypotheses clearly labelled until tested?
- Are statistical prerequisites visible?
- Are financial, safety or regulatory conclusions reviewed by the qualified owner?
- Has the accountable process owner approved the next action?


## Prompt 125 — Fishbone Facilitator

**Prompt ID:** `13-05-fishbone-facilitator`  
**Department:** Quality / Process Improvement  
**Risk level:** Low  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use
Facilitate a structured cause-and-effect workshop that captures possible causes across people, process, technology, materials, environment, measurement and management controls.

**Example:** A cross-functional team investigates repeat apartment-readiness failures involving Housekeeping, Engineering, Front Office and Inventory.

### Required inputs
- problem statement
- process scope
- workshop participants
- observations
- known constraints
- existing data
- categories appropriate to the process

### Expected outputs
- fishbone cause branches
- duplicate/overlapping causes
- evidence status
- questions to test causes
- parking-lot items
- next-step investigation list

### Copy-ready prompt

```text
ROLE
Act as a senior Lean Six Sigma and hotel operations improvement analyst supporting an accountable human process owner. Your role is structured problem-solving, data challenge and improvement support—not autonomous operational, statistical, financial or safety authority.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Process Improvement Lead / Quality Manager / Department Head / Black Belt / Green Belt / Other]
Accountable process owner/sponsor: [Insert authorized role]
Qualified statistical/technical reviewer when required: [Insert role]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Facilitate a structured cause-and-effect workshop that captures possible causes across people, process, technology, materials, environment, measurement and management controls.
Property type/location: [Insert confirmed property and jurisdiction]
Process/department: [Insert]
Project phase: [Define / Measure / Analyze / Improve / Control]
Study period and population: [Insert]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved hotel records.
Required inputs:
- problem statement
- process scope
- workshop participants
- observations
- known constraints
- existing data
- categories appropriate to the process

For every dataset or source record, state the system/document, extraction or revision date, owner, unit of analysis and relevant denominator.
If definitions changed between periods, expose the change before comparing results.
If an essential input is missing, stale, contradictory, biased or unverified, place it in a DATA / EVIDENCE GAP section. Do not guess or manufacture observations.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- fishbone cause branches
- duplicate/overlapping causes
- evidence status
- questions to test causes
- parking-lot items
- next-step investigation list

Separate the response into CONFIRMED FACTS; OPERATIONAL DEFINITIONS; CALCULATIONS / OBSERVED PATTERNS; HYPOTHESES; RECOMMENDATIONS; DATA / EVIDENCE GAPS; RISKS / EXCEPTIONS; HUMAN DECISIONS REQUIRED.
Show formulas, denominators, filters, exclusions and assumptions whenever a calculation is used.
Do not treat correlation as causation, a small sample as population truth, or an average as evidence of process stability.
Where a statistical method is proposed, state the prerequisites and ask for qualified review if those prerequisites are uncertain.

LEAN SIX SIGMA CONTROL
Use the fishbone to organize possibilities, not to validate causes. Preserve minority observations and contradictions instead of forcing consensus.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently authorize guest compensation, staffing or disciplinary action, pricing, budget release, safety acceptance, regulatory conclusions, technical return-to-service or final project benefits.
Do not expose unnecessary guest identity data, employee personal data, payment information, credentials, security-sensitive details or confidential contracts.
Statistical conclusions that affect material financial, safety, regulatory or employment decisions require review by the accountable qualified role.
The output remains a draft until the process owner verifies the evidence and authorizes the next action.
```

### Human verification checklist
- Are the process, defect and denominator definitions approved?
- Is the dataset current, traceable and suitable for the method?
- Are assumptions separated from observed facts?
- Are hypotheses clearly labelled until tested?
- Are statistical prerequisites visible?
- Are financial, safety or regulatory conclusions reviewed by the qualified owner?
- Has the accountable process owner approved the next action?


## Prompt 126 — FMEA Draft Assistant

**Prompt ID:** `13-06-fmea-draft-assistant`  
**Department:** Quality / Process Improvement  
**Risk level:** High  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use
Draft a process FMEA from a verified workflow by identifying potential failure modes, effects, causes and current controls for human scoring and action prioritization.

**Example:** Management reviews the room-release process to identify how status conflicts, missed inspections, engineering blocks or access errors can fail before guest arrival.

### Required inputs
- validated process steps
- failure history
- guest/safety/business effects
- current prevention/detection controls
- approved scoring scale
- process owners
- known regulatory/safety constraints

### Expected outputs
- draft FMEA table
- failure modes by step
- effects and causes
- current controls
- unscored or human-scored severity/occurrence/detection fields
- recommended control questions

### Copy-ready prompt

```text
ROLE
Act as a senior Lean Six Sigma and hotel operations improvement analyst supporting an accountable human process owner. Your role is structured problem-solving, data challenge and improvement support—not autonomous operational, statistical, financial or safety authority.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Process Improvement Lead / Quality Manager / Department Head / Black Belt / Green Belt / Other]
Accountable process owner/sponsor: [Insert authorized role]
Qualified statistical/technical reviewer when required: [Insert role]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Draft a process FMEA from a verified workflow by identifying potential failure modes, effects, causes and current controls for human scoring and action prioritization.
Property type/location: [Insert confirmed property and jurisdiction]
Process/department: [Insert]
Project phase: [Define / Measure / Analyze / Improve / Control]
Study period and population: [Insert]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved hotel records.
Required inputs:
- validated process steps
- failure history
- guest/safety/business effects
- current prevention/detection controls
- approved scoring scale
- process owners
- known regulatory/safety constraints

For every dataset or source record, state the system/document, extraction or revision date, owner, unit of analysis and relevant denominator.
If definitions changed between periods, expose the change before comparing results.
If an essential input is missing, stale, contradictory, biased or unverified, place it in a DATA / EVIDENCE GAP section. Do not guess or manufacture observations.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- draft FMEA table
- failure modes by step
- effects and causes
- current controls
- unscored or human-scored severity/occurrence/detection fields
- recommended control questions

Separate the response into CONFIRMED FACTS; OPERATIONAL DEFINITIONS; CALCULATIONS / OBSERVED PATTERNS; HYPOTHESES; RECOMMENDATIONS; DATA / EVIDENCE GAPS; RISKS / EXCEPTIONS; HUMAN DECISIONS REQUIRED.
Show formulas, denominators, filters, exclusions and assumptions whenever a calculation is used.
Do not treat correlation as causation, a small sample as population truth, or an average as evidence of process stability.
Where a statistical method is proposed, state the prerequisites and ask for qualified review if those prerequisites are uncertain.

LEAN SIX SIGMA CONTROL
AI must not invent S/O/D scores, RPN thresholds, safety acceptability or risk acceptance. Qualified owners apply the approved scoring method and authorize actions.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently authorize guest compensation, staffing or disciplinary action, pricing, budget release, safety acceptance, regulatory conclusions, technical return-to-service or final project benefits.
Do not expose unnecessary guest identity data, employee personal data, payment information, credentials, security-sensitive details or confidential contracts.
Statistical conclusions that affect material financial, safety, regulatory or employment decisions require review by the accountable qualified role.
The output remains a draft until the process owner verifies the evidence and authorizes the next action.
```

### Human verification checklist
- Are the process, defect and denominator definitions approved?
- Is the dataset current, traceable and suitable for the method?
- Are assumptions separated from observed facts?
- Are hypotheses clearly labelled until tested?
- Are statistical prerequisites visible?
- Are financial, safety or regulatory conclusions reviewed by the qualified owner?
- Has the accountable process owner approved the next action?


## Prompt 127 — Cost of Poor Quality Analyzer

**Prompt ID:** `13-07-cost-of-poor-quality-analyzer`  
**Department:** Quality / Process Improvement  
**Risk level:** High  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use
Structure an evidence-based cost-of-poor-quality model for hotel defects, rework, refunds, wasted labor, downtime or lost capacity without fabricating financial benefits.

**Example:** The property wants to estimate the monthly cost of repeat recleans, maintenance revisits and guest compensation linked to a recurring readiness defect.

### Required inputs
- defect/rework volumes
- Finance-approved cost assumptions
- labor time
- refund/compensation records
- downtime or out-of-order data
- period and denominator
- exclusions and uncertainty

### Expected outputs
- COPQ categories
- calculation table
- verified vs estimated costs
- sensitivity range
- data gaps
- Finance-review questions

### Copy-ready prompt

```text
ROLE
Act as a senior Lean Six Sigma and hotel operations improvement analyst supporting an accountable human process owner. Your role is structured problem-solving, data challenge and improvement support—not autonomous operational, statistical, financial or safety authority.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Process Improvement Lead / Quality Manager / Department Head / Black Belt / Green Belt / Other]
Accountable process owner/sponsor: [Insert authorized role]
Qualified statistical/technical reviewer when required: [Insert role]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Structure an evidence-based cost-of-poor-quality model for hotel defects, rework, refunds, wasted labor, downtime or lost capacity without fabricating financial benefits.
Property type/location: [Insert confirmed property and jurisdiction]
Process/department: [Insert]
Project phase: [Define / Measure / Analyze / Improve / Control]
Study period and population: [Insert]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved hotel records.
Required inputs:
- defect/rework volumes
- Finance-approved cost assumptions
- labor time
- refund/compensation records
- downtime or out-of-order data
- period and denominator
- exclusions and uncertainty

For every dataset or source record, state the system/document, extraction or revision date, owner, unit of analysis and relevant denominator.
If definitions changed between periods, expose the change before comparing results.
If an essential input is missing, stale, contradictory, biased or unverified, place it in a DATA / EVIDENCE GAP section. Do not guess or manufacture observations.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- COPQ categories
- calculation table
- verified vs estimated costs
- sensitivity range
- data gaps
- Finance-review questions

Separate the response into CONFIRMED FACTS; OPERATIONAL DEFINITIONS; CALCULATIONS / OBSERVED PATTERNS; HYPOTHESES; RECOMMENDATIONS; DATA / EVIDENCE GAPS; RISKS / EXCEPTIONS; HUMAN DECISIONS REQUIRED.
Show formulas, denominators, filters, exclusions and assumptions whenever a calculation is used.
Do not treat correlation as causation, a small sample as population truth, or an average as evidence of process stability.
Where a statistical method is proposed, state the prerequisites and ask for qualified review if those prerequisites are uncertain.

LEAN SIX SIGMA CONTROL
Label every assumption. Do not classify revenue opportunity as realized savings, double-count costs, or claim benefits until Finance validates the method.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently authorize guest compensation, staffing or disciplinary action, pricing, budget release, safety acceptance, regulatory conclusions, technical return-to-service or final project benefits.
Do not expose unnecessary guest identity data, employee personal data, payment information, credentials, security-sensitive details or confidential contracts.
Statistical conclusions that affect material financial, safety, regulatory or employment decisions require review by the accountable qualified role.
The output remains a draft until the process owner verifies the evidence and authorizes the next action.
```

### Human verification checklist
- Are the process, defect and denominator definitions approved?
- Is the dataset current, traceable and suitable for the method?
- Are assumptions separated from observed facts?
- Are hypotheses clearly labelled until tested?
- Are statistical prerequisites visible?
- Are financial, safety or regulatory conclusions reviewed by the qualified owner?
- Has the accountable process owner approved the next action?


## Prompt 128 — Process Capability Review Planner

**Prompt ID:** `13-08-process-capability-review-planner`  
**Department:** Quality / Process Improvement  
**Risk level:** High  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use
Plan a valid capability review for a stable, measurable hotel process and determine whether capability statistics are appropriate before calculating them.

**Example:** A hotel wants to assess whether check-in completion time consistently meets a defined service specification rather than merely reporting an average.

### Required inputs
- CTQ/specification limits
- measurement definition
- time-ordered observations
- measurement-system information
- process segmentation
- stability evidence
- sample size

### Expected outputs
- capability-readiness assessment
- data/stability checks
- appropriate capability approach
- stratification plan
- warnings against invalid Cp/Cpk use
- human statistical review questions

### Copy-ready prompt

```text
ROLE
Act as a senior Lean Six Sigma and hotel operations improvement analyst supporting an accountable human process owner. Your role is structured problem-solving, data challenge and improvement support—not autonomous operational, statistical, financial or safety authority.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Process Improvement Lead / Quality Manager / Department Head / Black Belt / Green Belt / Other]
Accountable process owner/sponsor: [Insert authorized role]
Qualified statistical/technical reviewer when required: [Insert role]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Plan a valid capability review for a stable, measurable hotel process and determine whether capability statistics are appropriate before calculating them.
Property type/location: [Insert confirmed property and jurisdiction]
Process/department: [Insert]
Project phase: [Define / Measure / Analyze / Improve / Control]
Study period and population: [Insert]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved hotel records.
Required inputs:
- CTQ/specification limits
- measurement definition
- time-ordered observations
- measurement-system information
- process segmentation
- stability evidence
- sample size

For every dataset or source record, state the system/document, extraction or revision date, owner, unit of analysis and relevant denominator.
If definitions changed between periods, expose the change before comparing results.
If an essential input is missing, stale, contradictory, biased or unverified, place it in a DATA / EVIDENCE GAP section. Do not guess or manufacture observations.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- capability-readiness assessment
- data/stability checks
- appropriate capability approach
- stratification plan
- warnings against invalid Cp/Cpk use
- human statistical review questions

Separate the response into CONFIRMED FACTS; OPERATIONAL DEFINITIONS; CALCULATIONS / OBSERVED PATTERNS; HYPOTHESES; RECOMMENDATIONS; DATA / EVIDENCE GAPS; RISKS / EXCEPTIONS; HUMAN DECISIONS REQUIRED.
Show formulas, denominators, filters, exclusions and assumptions whenever a calculation is used.
Do not treat correlation as causation, a small sample as population truth, or an average as evidence of process stability.
Where a statistical method is proposed, state the prerequisites and ask for qualified review if those prerequisites are uncertain.

LEAN SIX SIGMA CONTROL
Do not calculate or interpret Cp/Cpk/Pp/Ppk unless the prerequisites and supplied data support it. Distinguish specification limits from management targets and control limits.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently authorize guest compensation, staffing or disciplinary action, pricing, budget release, safety acceptance, regulatory conclusions, technical return-to-service or final project benefits.
Do not expose unnecessary guest identity data, employee personal data, payment information, credentials, security-sensitive details or confidential contracts.
Statistical conclusions that affect material financial, safety, regulatory or employment decisions require review by the accountable qualified role.
The output remains a draft until the process owner verifies the evidence and authorizes the next action.
```

### Human verification checklist
- Are the process, defect and denominator definitions approved?
- Is the dataset current, traceable and suitable for the method?
- Are assumptions separated from observed facts?
- Are hypotheses clearly labelled until tested?
- Are statistical prerequisites visible?
- Are financial, safety or regulatory conclusions reviewed by the qualified owner?
- Has the accountable process owner approved the next action?


## Prompt 129 — Control Plan Builder

**Prompt ID:** `13-09-control-plan-builder`  
**Department:** Quality / Process Improvement  
**Risk level:** Medium  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use
Convert an approved improvement into a sustainable hotel control plan with measures, ownership, frequency, reaction limits, evidence and escalation.

**Example:** After improving the room-release gate, the hotel needs a weekly control plan to detect missed inspections and repeat readiness defects.

### Required inputs
- approved future-state process
- validated CTQs/KPIs
- known failure modes
- control method
- owners
- review frequency
- reaction/escalation rules
- document/SOP changes

### Expected outputs
- control-plan table
- metric definitions
- owner and frequency
- reaction plan
- evidence/record requirement
- handover to SOP/training/audit

### Copy-ready prompt

```text
ROLE
Act as a senior Lean Six Sigma and hotel operations improvement analyst supporting an accountable human process owner. Your role is structured problem-solving, data challenge and improvement support—not autonomous operational, statistical, financial or safety authority.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Process Improvement Lead / Quality Manager / Department Head / Black Belt / Green Belt / Other]
Accountable process owner/sponsor: [Insert authorized role]
Qualified statistical/technical reviewer when required: [Insert role]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Convert an approved improvement into a sustainable hotel control plan with measures, ownership, frequency, reaction limits, evidence and escalation.
Property type/location: [Insert confirmed property and jurisdiction]
Process/department: [Insert]
Project phase: [Define / Measure / Analyze / Improve / Control]
Study period and population: [Insert]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved hotel records.
Required inputs:
- approved future-state process
- validated CTQs/KPIs
- known failure modes
- control method
- owners
- review frequency
- reaction/escalation rules
- document/SOP changes

For every dataset or source record, state the system/document, extraction or revision date, owner, unit of analysis and relevant denominator.
If definitions changed between periods, expose the change before comparing results.
If an essential input is missing, stale, contradictory, biased or unverified, place it in a DATA / EVIDENCE GAP section. Do not guess or manufacture observations.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- control-plan table
- metric definitions
- owner and frequency
- reaction plan
- evidence/record requirement
- handover to SOP/training/audit

Separate the response into CONFIRMED FACTS; OPERATIONAL DEFINITIONS; CALCULATIONS / OBSERVED PATTERNS; HYPOTHESES; RECOMMENDATIONS; DATA / EVIDENCE GAPS; RISKS / EXCEPTIONS; HUMAN DECISIONS REQUIRED.
Show formulas, denominators, filters, exclusions and assumptions whenever a calculation is used.
Do not treat correlation as causation, a small sample as population truth, or an average as evidence of process stability.
Where a statistical method is proposed, state the prerequisites and ask for qualified review if those prerequisites are uncertain.

LEAN SIX SIGMA CONTROL
Do not invent control limits or reaction thresholds. Use only thresholds approved by the process owner or statistically validated through the defined method.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently authorize guest compensation, staffing or disciplinary action, pricing, budget release, safety acceptance, regulatory conclusions, technical return-to-service or final project benefits.
Do not expose unnecessary guest identity data, employee personal data, payment information, credentials, security-sensitive details or confidential contracts.
Statistical conclusions that affect material financial, safety, regulatory or employment decisions require review by the accountable qualified role.
The output remains a draft until the process owner verifies the evidence and authorizes the next action.
```

### Human verification checklist
- Are the process, defect and denominator definitions approved?
- Is the dataset current, traceable and suitable for the method?
- Are assumptions separated from observed facts?
- Are hypotheses clearly labelled until tested?
- Are statistical prerequisites visible?
- Are financial, safety or regulatory conclusions reviewed by the qualified owner?
- Has the accountable process owner approved the next action?


## Prompt 130 — Kaizen Opportunity Prioritizer

**Prompt ID:** `13-10-kaizen-opportunity-prioritizer`  
**Department:** Quality / Process Improvement  
**Risk level:** Medium  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use
Prioritize small hotel improvement opportunities using evidence, guest impact, effort, risk, reversibility and owner capacity without turning an AI ranking into management approval.

**Example:** Operations has 18 improvement ideas across housekeeping, maintenance, arrivals and long-stay service and needs a transparent pilot sequence.

### Required inputs
- improvement backlog
- problem evidence
- guest/business impact
- estimated effort
- risk/safety implications
- dependencies
- owner capacity
- strategic priorities

### Expected outputs
- prioritized opportunity matrix
- quick-win candidates
- do-not-rush items
- evidence gaps
- dependency map
- recommended pilot sequence

### Copy-ready prompt

```text
ROLE
Act as a senior Lean Six Sigma and hotel operations improvement analyst supporting an accountable human process owner. Your role is structured problem-solving, data challenge and improvement support—not autonomous operational, statistical, financial or safety authority.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Process Improvement Lead / Quality Manager / Department Head / Black Belt / Green Belt / Other]
Accountable process owner/sponsor: [Insert authorized role]
Qualified statistical/technical reviewer when required: [Insert role]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Prioritize small hotel improvement opportunities using evidence, guest impact, effort, risk, reversibility and owner capacity without turning an AI ranking into management approval.
Property type/location: [Insert confirmed property and jurisdiction]
Process/department: [Insert]
Project phase: [Define / Measure / Analyze / Improve / Control]
Study period and population: [Insert]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only supplied, current and approved hotel records.
Required inputs:
- improvement backlog
- problem evidence
- guest/business impact
- estimated effort
- risk/safety implications
- dependencies
- owner capacity
- strategic priorities

For every dataset or source record, state the system/document, extraction or revision date, owner, unit of analysis and relevant denominator.
If definitions changed between periods, expose the change before comparing results.
If an essential input is missing, stale, contradictory, biased or unverified, place it in a DATA / EVIDENCE GAP section. Do not guess or manufacture observations.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- prioritized opportunity matrix
- quick-win candidates
- do-not-rush items
- evidence gaps
- dependency map
- recommended pilot sequence

Separate the response into CONFIRMED FACTS; OPERATIONAL DEFINITIONS; CALCULATIONS / OBSERVED PATTERNS; HYPOTHESES; RECOMMENDATIONS; DATA / EVIDENCE GAPS; RISKS / EXCEPTIONS; HUMAN DECISIONS REQUIRED.
Show formulas, denominators, filters, exclusions and assumptions whenever a calculation is used.
Do not treat correlation as causation, a small sample as population truth, or an average as evidence of process stability.
Where a statistical method is proposed, state the prerequisites and ask for qualified review if those prerequisites are uncertain.

LEAN SIX SIGMA CONTROL
Safety, legal, privacy and regulatory issues must not be deprioritized because they score poorly on convenience or ROI. Final prioritization belongs to accountable management.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently authorize guest compensation, staffing or disciplinary action, pricing, budget release, safety acceptance, regulatory conclusions, technical return-to-service or final project benefits.
Do not expose unnecessary guest identity data, employee personal data, payment information, credentials, security-sensitive details or confidential contracts.
Statistical conclusions that affect material financial, safety, regulatory or employment decisions require review by the accountable qualified role.
The output remains a draft until the process owner verifies the evidence and authorizes the next action.
```

### Human verification checklist
- Are the process, defect and denominator definitions approved?
- Is the dataset current, traceable and suitable for the method?
- Are assumptions separated from observed facts?
- Are hypotheses clearly labelled until tested?
- Are statistical prerequisites visible?
- Are financial, safety or regulatory conclusions reviewed by the qualified owner?
- Has the accountable process owner approved the next action?


---

## 27. Key takeaway

Lean Six Sigma gives hotel teams a disciplined way to move from frustration to evidence. AI can make that discipline faster, but speed is only useful when the evidence remains visible.

> **Use AI to structure the question and challenge the data. Use Lean Six Sigma to test the process. Use accountable hotel professionals to approve the conclusion and sustain the change.**
