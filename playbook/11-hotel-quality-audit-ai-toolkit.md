# Article 11 — Hotel Quality Audit AI Toolkit

## 10 Professional AI Prompts for Audit Planning, Evidence, Nonconformities, Trend Analysis, CAPA and Effectiveness Review

**Track C · Hotel & Serviced Apartment AI Operations Playbook · Quality Assurance chapter**

A hotel audit should not begin with a score. It should begin with a **requirement, a scope and an evidence plan**.

That distinction matters because hotel quality work is full of apparently simple observations that become unreliable when the evidence chain is weak. A room may look clean but fail a controlled readiness standard. A work order may be marked complete while the underlying defect remains. A guest complaint may suggest a service gap without proving which process failed. A department may improve its audit score because the sample changed rather than because performance improved.

AI can help a Quality Manager organize this complexity. It can map requirements to evidence, compare actual workflows with SOPs, detect repeated findings, prepare draft nonconformity statements and challenge whether a corrective action has enough proof behind it. But it must not manufacture audit evidence, invent a standard, decide that a person is at fault or close a nonconformity because the language sounds convincing.

The operating principle for this chapter is:

> **An audit finding must be traceable to a requirement, an observation and objective evidence. AI may structure that chain; the qualified auditor and accountable process owner retain judgment and authority.**

The ten prompts follow a controlled quality cycle:

> **Plan → Inspect → Compare → Classify → Record → Trend → Corroborate → Summarize → Challenge evidence → Verify effectiveness**

---

## 1. Quality auditing is a management-control system, not a checklist exercise

A checklist can be useful, but a checklist by itself is not an audit system. A professional audit asks what requirement applies, what evidence should exist, what sample is appropriate, what was actually observed and whether the evidence supports a conclusion.

The current ISO 19011:2026 guidance describes management-system auditing around principles that include integrity, fair presentation, due professional care, confidentiality, independence, an evidence-based approach and a risk-based approach. The standard also separates management of the audit programme from preparation, conduct and reporting of individual audits. This chapter does not claim that a hotel must use ISO 19011 or that this playbook provides certification guidance; it uses those principles as a useful professional reference for disciplined internal auditing.

In Dubai, hotel classification is also an operational reality rather than a theoretical quality concept. Dubai DET states that hotel establishments are licensed, inspected and classified and that hotel operators use the classification system to manage classification-related requirements. The exact regulatory criteria and the current official documents always take precedence over an AI-generated checklist.

For an operating hotel or serviced-apartment portfolio, the practical lesson is simple: **audit criteria must come from controlled sources, not from the model's memory.**

## 2. The Quality Audit HOTEL model

- **H — Hospitality role & human owner:** identify the auditor, Quality Manager, department head, General Manager, technical specialist or other accountable owner. Preserve auditor independence where required.
- **O — Operational objective & context:** define audit purpose, property, department, process, period, sample, guest-journey stage and decision supported.
- **T — Trusted inputs & sources of truth:** use current controlled SOPs, brand/service standards, regulator/classification requirements, PMS/CMMS/CRM records, inspection evidence, approved checklists and documented exceptions.
- **E — Expected output, exceptions & evidence:** require every finding to show criterion, observation, evidence, status and unresolved gaps. Keep facts, auditor judgments, hypotheses and recommendations separate.
- **L — Limits, privacy & leadership approval:** prohibit invented findings, unsupported blame, unauthorized regulatory interpretations and premature closure. Protect guest/employee information and route high-risk issues to qualified owners.

### Quality-audit source-of-truth matrix

| Audit question | Primary source of truth | AI rule |
|---|---|---|
| What requirement applies? | current controlled SOP / brand standard / approved regulatory source | never invent or use an obsolete revision |
| What happened in the sampled process? | direct observation + system/log evidence | state what was actually sampled |
| Was the room/apartment released? | PMS + housekeeping release workflow | cleaned is not automatically released |
| Was a technical defect closed? | CMMS + required verification | closure status is not proof of effectiveness |
| Was a guest request completed? | approved request/CRM record + outcome evidence | do not infer from silence |
| Is a finding repeated? | prior audit/NCR/CAPA register | normalize period/sample before trend claims |
| What severity applies? | approved finding/risk matrix | AI may map; auditor/authorized owner decides |
| Is root cause validated? | approved RCA/CAPA record | hypothesis stays hypothesis until accepted |
| Is CAPA implemented? | implementation evidence | action plan text is not implementation evidence |
| Is CAPA effective? | follow-up evidence + recurrence data | AI may recommend closure; authorized owner closes |

## 3. Fictional UAE 60-unit serviced-apartment quality case

Continue with the fictional 60-unit UAE serviced-apartment portfolio used throughout this playbook. The portfolio includes studios, one-bedroom and two-bedroom apartments serving leisure, corporate and extended-stay guests.

During a monthly quality review, management sees three signals:

1. Housekeeping inspection records show several repeat bathroom-sealant and amenity-placement findings.
2. Engineering data shows recurring fan-coil complaints in a small group of apartments.
3. Guest feedback shows repeated references to delayed updates when maintenance visits are required.

A weak AI audit might merge these into a single narrative: “Housekeeping and Engineering quality is poor.”

A controlled audit approach would ask:

- Which standards apply to each issue?
- What sample was inspected?
- Are the findings from the same units or different ones?
- Are the amenity observations minor presentation defects or controlled standard failures?
- Does the engineering pattern represent a repeat failure, a different component or simply higher occupancy exposure?
- Is the guest-feedback issue about repair quality, communication, or both?
- Which evidence proves recurrence?
- Which issue needs containment now, and which belongs in trend analysis?

The answer may be three different control problems: a housekeeping standardization issue, a technical asset-pattern issue and a cross-department communication issue. The audit should preserve those distinctions.

## 4. Plan the audit before entering the operation

Prompt 101 creates the audit plan. A useful plan defines objectives, scope, criteria, sample logic, methods, timetable, auditor responsibilities and evidence needs before the team begins fieldwork.

For a 60-unit operation, an audit plan could include a risk-based mix of:

- recently turned-over apartments;
- long-stay occupied units where access is permitted and appropriate;
- units with repeat defects;
- rooms prepared by different housekeeping shifts;
- a selection of completed work orders;
- a sample of guest requests and complaints;
- selected inventory/PAR records;
- one or more management-process samples such as handover or escalation.

The sample must be described honestly. Ten inspected units do not prove the condition of all sixty. AI should never convert a limited sample into a population-wide claim without a valid statistical basis.

## 5. A room audit must test controlled readiness, not personal taste

Prompt 102 converts the approved room/apartment standard into an evidence-ready checklist. The goal is to reduce vague observations such as “bathroom looks bad” or “room is not luxurious enough.”

A strong checklist item contains:

- requirement or standard;
- observation method;
- pass/fail/not-applicable rule;
- evidence field;
- criticality where defined;
- defect owner;
- release/escalation consequence where applicable.

Examples of inspectable zones can include entrance/access, sleeping area, bathroom, kitchen, appliances, HVAC comfort, lighting/electrical presentation, furniture condition, linen, amenities, safety information and cleanliness. The exact checklist must come from the property's approved standard and any applicable official requirements.

For serviced apartments, kitchen and appliance readiness deserves particular attention because the guest is living in the unit rather than simply sleeping in it. Missing cookware, a leaking washing machine or an intermittent refrigerator fault can create a much larger long-stay impact than a cosmetic defect.

## 6. Process compliance requires a requirement-to-evidence map

Prompt 103 is for auditing workflows rather than physical rooms. It compares what the current SOP says should happen with what the sampled records show actually happened.

For example, a room-not-ready process might require:

1. Front Office records the status.
2. Housekeeping provides the next verified readiness estimate.
3. Engineering blocks release if a technical defect remains.
4. The Duty Manager owns escalation after a defined threshold.
5. The guest receives an update at the agreed interval.

The audit should not ask, “Did the team follow the SOP?” as one broad question. It should test each required control against evidence. A process can be partly conforming and partly nonconforming.

Approved exceptions also matter. If management authorized a temporary deviation under a controlled exception process, the auditor should not automatically label that deviation as nonconformance without reviewing the exception authority and conditions.

## 7. Finding severity is not a language-generation task

Prompt 104 helps organize draft findings against an approved classification model. It should never invent a major/minor/critical scale if the property has not defined one.

A useful severity decision considers factors such as:

- guest or employee safety exposure;
- legal/regulatory/classification impact;
- service continuity;
- financial exposure;
- privacy/security impact;
- recurrence/systemic nature;
- number of units/processes affected;
- ability to contain immediately.

AI can show how the evidence maps to those factors. The final classification remains with the competent auditor or authorized quality owner.

A beautifully written finding with weak evidence is still a weak finding.

## 8. Nonconformity statements need three linked elements

Prompt 105 drafts the nonconformity report only after the criterion and evidence are established.

A robust nonconformity contains:

**Requirement:** what controlled requirement should have been met?

**Objective evidence:** what was observed, where, when and in what sample?

**Gap:** how did the evidence differ from the requirement?

Example structure:

> The housekeeping release standard requires the final bathroom inspection to be completed and recorded before a vacant-clean apartment is released. In 3 of 12 sampled turnover records dated [dates], the PMS release timestamp preceded the recorded bathroom inspection. Therefore, the required inspection evidence was not completed before release for those sampled records.

That is stronger than: “Housekeeping does not follow inspection procedures.” The second statement overgeneralizes the sample and assigns a broad conclusion unsupported by the evidence presented.

The nonconformity report should not jump directly to root cause. Root cause belongs to the investigation/CAPA stage unless the audit itself legitimately includes validated cause evidence.

## 9. Quality trends require denominators, stable definitions and comparable periods

Prompt 106 analyzes repeated findings over time. Counts alone can mislead.

Suppose monthly room-inspection findings change from 18 to 24. That looks worse until management notices that the audit sample increased from 60 inspections to 110.

An illustrative normalized finding rate can be calculated as:

**Finding rate = verified findings ÷ relevant audited opportunities × 100**

If Month A has 18 findings across 60 audited opportunities, the illustrative rate is **30%**. If Month B has 24 findings across 110 opportunities, the illustrative rate is approximately **21.8%**. The absolute number increased, but the normalized rate decreased.

This does not automatically prove improvement. The sample mix, severity and finding definitions also need review. The point is that AI should expose the denominator before claiming a trend.

Useful trend dimensions include:

- department;
- unit/asset;
- finding type;
- severity;
- repeat vs new;
- overdue vs closed;
- process step;
- shift/vendor where appropriate and fair;
- guest-impact link;
- effectiveness-failure recurrence.

## 10. Mystery guest reports are evidence inputs, not unquestionable truth

Prompt 107 reviews mystery-guest or external evaluator findings. These reports can be valuable because they show a guest-eye view of service, but they may mix objective requirements with subjective impressions.

Examples:

- “The agent did not use the guest's name after it was confirmed” may be testable against an approved service standard.
- “The lobby felt less luxurious than expected” may be subjective unless a defined standard exists.
- “The airport transfer was late” should be checked against the scheduled pickup, actual vehicle timestamps and applicable grace/operating rules.

AI should classify the nature of the observation, identify the applicable internal standard and recommend what corroborating evidence is needed. It should not dismiss subjective feedback; subjective experience can still be strategically important. It simply should not be mislabeled as objective nonconformity without criteria.

## 11. Department summaries should preserve bad news, not polish it away

Prompt 108 converts detailed audit evidence into a management summary. Executive summaries create risk when AI compresses the story so aggressively that open issues disappear.

A useful department audit summary includes:

- scope and sample;
- overall evidence quality;
- verified strengths;
- high-priority findings;
- repeat findings;
- overdue actions;
- systemic themes;
- guest/financial/safety impacts where verified;
- decisions required from management;
- actions that remain open.

Avoid unsupported department rankings unless the underlying audit programme provides comparable scopes, samples and scoring rules. A department with more findings may simply have been audited more deeply.

## 12. Evidence gaps should be visible before a finding is finalized

Prompt 109 is designed as a challenge function. Before an auditor finalizes a finding or closes an action, the prompt asks whether the file actually contains the necessary proof.

Typical evidence gaps include:

- missing requirement reference;
- obsolete SOP revision;
- screenshot without date/time/source;
- work-order closure with no post-repair verification;
- room photo with no unit/sample identification;
- verbal statement not corroborated where corroboration is required;
- finding marked closed with only an action-plan promise;
- trend claim without denominator;
- root cause copied from an earlier incident without new analysis;
- corrective action implemented but no effectiveness check.

The output should be a gap register, not a fabricated completion of the missing evidence.

## 13. Corrective action is not effective merely because it was completed

Prompt 110 separates **implementation** from **effectiveness**.

Imagine that repeat room-readiness failures lead to a corrective action: supervisors receive a new final-inspection checklist. The checklist may be distributed and training may be completed. Those facts prove implementation.

Effectiveness requires more. The quality team may need to verify, for example:

- subsequent sampled records show the inspection before release;
- repeat findings decline using a comparable measure;
- guest complaints linked to the same failure mode do not recur beyond the agreed monitoring threshold;
- supervisors use the checklist consistently;
- no new unintended problem was created.

Only then can the authorized owner decide whether the corrective action is effective and whether the CAPA may be closed.

## 14. Audit sampling should be risk-based and transparent

A hotel has too many transactions, rooms, requests and work orders to inspect everything. Sampling is therefore unavoidable in most internal audits.

The sample should be designed around the audit objective. A random or broad sample may be useful for general conformance. A targeted sample may be better when investigating a known repeat issue. Both can be valid if the method is declared honestly.

Useful sample dimensions include:

- different shifts;
- weekdays/weekends;
- high/low occupancy periods;
- different unit types;
- different team members or vendors where appropriate;
- new vs long-stay guests;
- normal vs exception workflows;
- repeat-problem units/assets;
- recently closed CAPA areas.

AI can help create a sampling proposal, but management should avoid false statistical precision. If the audit is not statistically representative, say so.

## 15. Quality scoring can help management—but it can also hide risk

A dashboard score can be useful when the scoring method is controlled. It becomes dangerous when one number hides critical findings.

A property might achieve 94% overall while still having one unresolved life-safety or privacy finding. The score must never neutralize the need to escalate critical issues.

If a weighted audit score is used, the methodology should define:

- categories;
- weights;
- critical-fail rules;
- not-applicable treatment;
- sample denominator;
- rounding;
- repeat-finding penalties if applicable;
- approval owner.

AI may calculate using the approved method. It should not design a flattering score after seeing the result.

## 16. Lean Six Sigma turns findings into process learning

Quality audits and Lean Six Sigma complement each other when used carefully.

**Define:** identify the repeated audit problem and guest/business impact.

**Measure:** establish comparable findings, denominators, process timing and defect definitions.

**Analyze:** test root-cause hypotheses using evidence rather than opinion.

**Improve:** implement controlled process, training, system, design or supplier changes.

**Control:** monitor repeat findings and effectiveness evidence after implementation.

A Pareto chart may show that a small number of defect categories account for much of the recurring audit burden. A process map may reveal that handover gaps create failures across departments. A control plan may specify what evidence must be checked weekly after CAPA.

The audit identifies the signal; improvement work changes the system.

## 17. KPI dashboard for audit governance

Useful audit-program KPIs can include:

| KPI | Purpose | Guardrail |
|---|---|---|
| Audit plan completion | whether scheduled audits occur | do not reward rushed low-quality audits |
| Finding rate per audited opportunity | normalized defect signal | keep sample definitions comparable |
| Repeat finding rate | recurrence/systemic weakness | define repeat consistently |
| Overdue CAPA rate | action governance | distinguish approved extensions |
| Evidence-gap rate | audit-file quality | do not hide gaps by lowering evidence requirements |
| Average closure age | action flow | closure must remain evidence-based |
| Effectiveness failure rate | weak CAPA detection | requires follow-up evidence |
| Critical finding open time | risk exposure | never average away critical items |
| Audit rework rate | audit quality | distinguish clarification from genuine rework |
| Management decision backlog | unresolved governance | define accountable owner |

The best audit dashboard creates management questions. It does not replace them.

## 18. Illustrative Before → Action → After → AED Saved model

Consider an illustrative scenario, not real hotel data.

**Before:** repeated room-readiness defects create 14 avoidable re-cleans per month. Assume, only for the example, an incremental internal handling cost of AED 55 per re-clean, including labor and coordination.

**Illustrative monthly avoidable cost:**

14 × AED 55 = **AED 770**

**Action:** the audit identifies that most repeats occur because the final inspection record is incomplete before room release. Management redesigns the release gate and monitors compliance.

**After:** the operation records 5 comparable re-cleans in a later comparable month.

**Illustrative avoided cost:**

(14 − 5) × AED 55 = **AED 495 per month**

The calculation is intentionally simple. Real financial claims should use Finance-approved cost assumptions, equivalent periods and verified operational volumes. The value of the audit may also include guest-experience, availability and risk benefits that are not captured in this example.

## 19. 30-day implementation plan

### Days 1–5 — Governance
- confirm audit owners and independence requirements;
- identify controlled standards and current revisions;
- approve finding/severity categories;
- define evidence rules and privacy limits;
- select the first audit scope.

### Days 6–10 — Evidence design
- build the requirement-to-evidence matrix;
- define sampling logic;
- prepare room/process checklists;
- test evidence naming and retention;
- configure the audit finding register.

### Days 11–15 — Pilot audit
- run a small audit using Prompts 101–105;
- compare AI-supported outputs with auditor judgment;
- identify hallucination or overclassification risks;
- revise prompt wording and approval gates.

### Days 16–20 — Trend and management reporting
- load controlled historical findings;
- normalize relevant measures;
- test Prompt 106 and Prompt 108;
- define management-review outputs.

### Days 21–25 — CAPA challenge
- use Prompt 109 on open/closed files;
- test Prompt 110 against completed CAPA;
- reopen only through authorized quality governance where evidence justifies it;
- record prompt weaknesses.

### Days 26–30 — Control
- approve prompt versions;
- assign review dates;
- publish the department AI register;
- monitor evidence-gap and repeat-finding KPIs;
- schedule the next audit-cycle review.

## 20. Management checklist

Before using AI-supported audit output operationally, verify:

- [ ] current requirement/standard revision is identified;
- [ ] audit scope and sample are stated;
- [ ] objective evidence is traceable;
- [ ] facts and auditor judgments are separated;
- [ ] finding severity follows the approved model;
- [ ] no unsupported blame is assigned;
- [ ] guest/employee information is minimized;
- [ ] regulatory or classification conclusions use current official sources;
- [ ] root-cause hypotheses are not presented as validated causes;
- [ ] corrective-action implementation is distinguished from effectiveness;
- [ ] closure authority is identified;
- [ ] critical findings are escalated outside normal scoring where policy requires it.

## 21. Connected knowledge across Ahmed Quality Ops

This quality-audit chapter is intentionally connected to the wider knowledge platform rather than isolated inside the Hotel AI series.

Use it together with:

- **Hotel Guest Complaint & Service Recovery AI Toolkit** when complaints become audit signals or CAPA inputs;
- **Housekeeping Management AI Toolkit** for room-release, inspection and reclean controls;
- **Engineering & Maintenance AI Toolkit** for technical evidence and work-order closure;
- **Predictive Maintenance AI Toolkit** for evidence quality behind anomaly and failure hypotheses;
- **SOP Exception & Escalation Management** for controlled deviations and unresolved findings;
- **SOP Roles, Authority & RACI** for finding ownership, approval and closure authority;
- **How to Write a Professional SOP Procedure** when audit findings lead to process redesign;
- **Tourism Quality & SOP AI Toolkit** for related tourism-process quality applications;
- **MICE Movement Control Room** when audit evidence involves complex group movements, hotel desks or operational handovers;
- **Tourism Transport & Dispatch AI Toolkit** when transfer evidence connects to hotel arrival/service failures.

A mature knowledge platform should allow the reader to move from a finding to the process, from the process to the authority model, from the authority model to CAPA, and from CAPA back to measurement.

## 22. Sources and evidence boundaries

Verified external context used in this chapter includes:

- **ISO 19011:2026 — Guidelines for auditing management systems.** ISO describes principles including integrity, fair presentation, due professional care, confidentiality, independence, evidence-based approach and risk-based approach, together with guidance for managing and conducting audits.
- **Dubai Department of Economy and Tourism — Hotel Classification.** DET states that Dubai hotel establishments are classified and inspected and provides official classification services and criteria through its hotel-classification system.

Official links:

- https://www.iso.org/standard/19011
- https://www.dubaidet.gov.ae/en/our-services/for-consumers-and-students/classify-a-hotel-establishment
- https://www.dubaidet.gov.ae/en/legislative-news/administrative-resolution-no-1-of-2018

The 60-unit UAE serviced-apartment scenario, KPI examples, finding rates and AED calculations in this chapter are **illustrative operating examples** and do not represent a specific hotel's actual performance or financial results.

---

# The 10 copy-ready prompts
## Prompt 101 — Quality Audit Planner

**Prompt ID:** `11-01-quality-audit-planner`  
**Department:** Quality Assurance  
**Primary user:** Quality Manager / Internal Auditor / Department Head  
**Risk level:** MEDIUM  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use

Build a risk-based hotel quality audit plan that defines scope, criteria, sample, evidence and accountable owners before fieldwork begins.

### Required inputs

- audit objective and scope
- current approved standards/SOPs
- property/department list
- recent findings/complaints/KPIs
- audit calendar and auditor availability

### Expected outputs

- audit scope and criteria
- risk-based sample plan
- evidence plan
- interview/observation plan
- schedule and owners
- pre-audit evidence gaps

### Copy-ready prompt

```text
ROLE
Act as a senior hotel quality and operations analyst supporting an accountable human auditor. Your role is decision support, evidence organization and controlled drafting—not autonomous audit authority.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Quality Manager / Internal Auditor / Department Head / Other]
Accountable human owner/approver: [Insert role and name if appropriate]
Audit independence or conflict-of-interest constraint: [Insert if applicable]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Build a risk-based hotel quality audit plan that defines scope, criteria, sample, evidence and accountable owners before fieldwork begins.
Property type/location: [Insert property and jurisdiction]
Department/process/unit: [Insert scope]
Audit period/date: [Insert]
Audit objective: [Insert]
Sampling approach: [Insert random / targeted / risk-based / full population as applicable]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied, current, approved sources.
Required inputs:
- audit objective and scope
- current approved standards/SOPs
- property/department list
- recent findings/complaints/KPIs
- audit calendar and auditor availability

For each source, record title/system, revision or extraction date, owner and scope.
If an essential source is missing, stale, contradictory or unverified, place it in an EVIDENCE GAP section. Do not fill the gap from general knowledge.
Official/regulatory/classification requirements must come from the current official source supplied or verified by the authorized human reviewer.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- audit scope and criteria
- risk-based sample plan
- evidence plan
- interview/observation plan
- schedule and owners
- pre-audit evidence gaps

Separate the response into:
1. CONFIRMED FACTS
2. AUDIT CRITERIA / REQUIREMENTS
3. OBJECTIVE EVIDENCE
4. AUDITOR JUDGMENT / PROPOSED FINDINGS
5. ASSUMPTIONS OR HYPOTHESES
6. EVIDENCE GAPS / CONTRADICTIONS
7. RECOMMENDED FOLLOW-UP
8. HUMAN DECISIONS REQUIRED

When using a sample, state the sample size and do not generalize beyond what the evidence supports.
When comparing periods, show the denominator and definition before claiming improvement or deterioration.

QUALITY-AUDIT CONTROL
For every proposed finding, show: CRITERION / OBSERVATION / OBJECTIVE EVIDENCE / GAP / EVIDENCE STATUS.
Do not invent evidence. Do not assign blame. Do not present a root-cause hypothesis as validated. Do not declare a finding or CAPA closed unless the authorized human owner confirms closure through the approved workflow.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently determine regulatory compliance, legal liability, employee misconduct, disciplinary action, guest compensation, safety clearance, financial approval or final CAPA closure.
Do not expose unnecessary guest identity data, employee personal data, payment information, credentials, security-sensitive details or confidential contracts.
Escalate safety, fire/life-safety, security, privacy, discrimination, legal, medical, food-safety, water-hygiene or other specialist findings to the qualified role defined by policy.
The output remains a draft until the accountable human auditor/owner verifies the evidence, applies professional judgment and authorizes the next action.
```

### Human verification checklist

- Is the criterion current and controlled?
- Is the evidence traceable to the sample?
- Does the conclusion stay within the evidence?
- Are severity and authority based on approved rules?
- Are missing or contradictory records visible?
- Is personal/confidential data minimized?
- Has the authorized quality owner reviewed the output?

---

## Prompt 102 — Room Audit Checklist

**Prompt ID:** `11-02-room-audit-checklist`  
**Department:** Quality Assurance  
**Primary user:** Quality Manager / Internal Auditor / Department Head  
**Risk level:** MEDIUM  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use

Build or review a room/apartment audit checklist that tests guest-ready condition against controlled standards without confusing appearance with verified compliance.

### Required inputs

- approved room/apartment standard
- housekeeping inspection checklist
- engineering safety/defect criteria
- amenity/inventory standard
- sample unit profile

### Expected outputs

- checklist by zone
- requirement/evidence fields
- critical vs routine items
- not-applicable logic
- photo/evidence guidance
- release escalation points

### Copy-ready prompt

```text
ROLE
Act as a senior hotel quality and operations analyst supporting an accountable human auditor. Your role is decision support, evidence organization and controlled drafting—not autonomous audit authority.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Quality Manager / Internal Auditor / Department Head / Other]
Accountable human owner/approver: [Insert role and name if appropriate]
Audit independence or conflict-of-interest constraint: [Insert if applicable]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Build or review a room/apartment audit checklist that tests guest-ready condition against controlled standards without confusing appearance with verified compliance.
Property type/location: [Insert property and jurisdiction]
Department/process/unit: [Insert scope]
Audit period/date: [Insert]
Audit objective: [Insert]
Sampling approach: [Insert random / targeted / risk-based / full population as applicable]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied, current, approved sources.
Required inputs:
- approved room/apartment standard
- housekeeping inspection checklist
- engineering safety/defect criteria
- amenity/inventory standard
- sample unit profile

For each source, record title/system, revision or extraction date, owner and scope.
If an essential source is missing, stale, contradictory or unverified, place it in an EVIDENCE GAP section. Do not fill the gap from general knowledge.
Official/regulatory/classification requirements must come from the current official source supplied or verified by the authorized human reviewer.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- checklist by zone
- requirement/evidence fields
- critical vs routine items
- not-applicable logic
- photo/evidence guidance
- release escalation points

Separate the response into:
1. CONFIRMED FACTS
2. AUDIT CRITERIA / REQUIREMENTS
3. OBJECTIVE EVIDENCE
4. AUDITOR JUDGMENT / PROPOSED FINDINGS
5. ASSUMPTIONS OR HYPOTHESES
6. EVIDENCE GAPS / CONTRADICTIONS
7. RECOMMENDED FOLLOW-UP
8. HUMAN DECISIONS REQUIRED

When using a sample, state the sample size and do not generalize beyond what the evidence supports.
When comparing periods, show the denominator and definition before claiming improvement or deterioration.

QUALITY-AUDIT CONTROL
For every proposed finding, show: CRITERION / OBSERVATION / OBJECTIVE EVIDENCE / GAP / EVIDENCE STATUS.
Do not invent evidence. Do not assign blame. Do not present a root-cause hypothesis as validated. Do not declare a finding or CAPA closed unless the authorized human owner confirms closure through the approved workflow.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently determine regulatory compliance, legal liability, employee misconduct, disciplinary action, guest compensation, safety clearance, financial approval or final CAPA closure.
Do not expose unnecessary guest identity data, employee personal data, payment information, credentials, security-sensitive details or confidential contracts.
Escalate safety, fire/life-safety, security, privacy, discrimination, legal, medical, food-safety, water-hygiene or other specialist findings to the qualified role defined by policy.
The output remains a draft until the accountable human auditor/owner verifies the evidence, applies professional judgment and authorizes the next action.
```

### Human verification checklist

- Is the criterion current and controlled?
- Is the evidence traceable to the sample?
- Does the conclusion stay within the evidence?
- Are severity and authority based on approved rules?
- Are missing or contradictory records visible?
- Is personal/confidential data minimized?
- Has the authorized quality owner reviewed the output?

---

## Prompt 103 — Process Compliance Review

**Prompt ID:** `11-03-process-compliance-review`  
**Department:** Quality Assurance  
**Primary user:** Quality Manager / Internal Auditor / Department Head  
**Risk level:** MEDIUM  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use

Compare a real hotel workflow with the current controlled SOP and identify verified conformities, nonconformities, evidence gaps and improvement observations.

### Required inputs

- current approved SOP/revision
- actual transaction or workflow evidence
- system timestamps/logs
- staff role matrix
- approved exceptions/waivers

### Expected outputs

- requirement-to-evidence matrix
- verified conformance
- potential nonconformance
- approved exception list
- evidence gaps
- follow-up questions

### Copy-ready prompt

```text
ROLE
Act as a senior hotel quality and operations analyst supporting an accountable human auditor. Your role is decision support, evidence organization and controlled drafting—not autonomous audit authority.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Quality Manager / Internal Auditor / Department Head / Other]
Accountable human owner/approver: [Insert role and name if appropriate]
Audit independence or conflict-of-interest constraint: [Insert if applicable]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Compare a real hotel workflow with the current controlled SOP and identify verified conformities, nonconformities, evidence gaps and improvement observations.
Property type/location: [Insert property and jurisdiction]
Department/process/unit: [Insert scope]
Audit period/date: [Insert]
Audit objective: [Insert]
Sampling approach: [Insert random / targeted / risk-based / full population as applicable]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied, current, approved sources.
Required inputs:
- current approved SOP/revision
- actual transaction or workflow evidence
- system timestamps/logs
- staff role matrix
- approved exceptions/waivers

For each source, record title/system, revision or extraction date, owner and scope.
If an essential source is missing, stale, contradictory or unverified, place it in an EVIDENCE GAP section. Do not fill the gap from general knowledge.
Official/regulatory/classification requirements must come from the current official source supplied or verified by the authorized human reviewer.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- requirement-to-evidence matrix
- verified conformance
- potential nonconformance
- approved exception list
- evidence gaps
- follow-up questions

Separate the response into:
1. CONFIRMED FACTS
2. AUDIT CRITERIA / REQUIREMENTS
3. OBJECTIVE EVIDENCE
4. AUDITOR JUDGMENT / PROPOSED FINDINGS
5. ASSUMPTIONS OR HYPOTHESES
6. EVIDENCE GAPS / CONTRADICTIONS
7. RECOMMENDED FOLLOW-UP
8. HUMAN DECISIONS REQUIRED

When using a sample, state the sample size and do not generalize beyond what the evidence supports.
When comparing periods, show the denominator and definition before claiming improvement or deterioration.

QUALITY-AUDIT CONTROL
For every proposed finding, show: CRITERION / OBSERVATION / OBJECTIVE EVIDENCE / GAP / EVIDENCE STATUS.
Do not invent evidence. Do not assign blame. Do not present a root-cause hypothesis as validated. Do not declare a finding or CAPA closed unless the authorized human owner confirms closure through the approved workflow.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently determine regulatory compliance, legal liability, employee misconduct, disciplinary action, guest compensation, safety clearance, financial approval or final CAPA closure.
Do not expose unnecessary guest identity data, employee personal data, payment information, credentials, security-sensitive details or confidential contracts.
Escalate safety, fire/life-safety, security, privacy, discrimination, legal, medical, food-safety, water-hygiene or other specialist findings to the qualified role defined by policy.
The output remains a draft until the accountable human auditor/owner verifies the evidence, applies professional judgment and authorizes the next action.
```

### Human verification checklist

- Is the criterion current and controlled?
- Is the evidence traceable to the sample?
- Does the conclusion stay within the evidence?
- Are severity and authority based on approved rules?
- Are missing or contradictory records visible?
- Is personal/confidential data minimized?
- Has the authorized quality owner reviewed the output?

---

## Prompt 104 — Audit Finding Classifier

**Prompt ID:** `11-04-audit-finding-classifier`  
**Department:** Quality Assurance  
**Primary user:** Quality Manager / Internal Auditor / Department Head  
**Risk level:** MEDIUM  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use

Classify draft audit findings using the property’s approved severity/risk model without allowing AI to invent severity, blame or closure status.

### Required inputs

- draft finding statements
- approved finding categories
- risk/severity matrix
- requirement references
- supporting evidence

### Expected outputs

- finding classification table
- risk rationale
- evidence sufficiency flag
- escalation requirement
- items requiring auditor judgment

### Copy-ready prompt

```text
ROLE
Act as a senior hotel quality and operations analyst supporting an accountable human auditor. Your role is decision support, evidence organization and controlled drafting—not autonomous audit authority.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Quality Manager / Internal Auditor / Department Head / Other]
Accountable human owner/approver: [Insert role and name if appropriate]
Audit independence or conflict-of-interest constraint: [Insert if applicable]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Classify draft audit findings using the property’s approved severity/risk model without allowing AI to invent severity, blame or closure status.
Property type/location: [Insert property and jurisdiction]
Department/process/unit: [Insert scope]
Audit period/date: [Insert]
Audit objective: [Insert]
Sampling approach: [Insert random / targeted / risk-based / full population as applicable]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied, current, approved sources.
Required inputs:
- draft finding statements
- approved finding categories
- risk/severity matrix
- requirement references
- supporting evidence

For each source, record title/system, revision or extraction date, owner and scope.
If an essential source is missing, stale, contradictory or unverified, place it in an EVIDENCE GAP section. Do not fill the gap from general knowledge.
Official/regulatory/classification requirements must come from the current official source supplied or verified by the authorized human reviewer.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- finding classification table
- risk rationale
- evidence sufficiency flag
- escalation requirement
- items requiring auditor judgment

Separate the response into:
1. CONFIRMED FACTS
2. AUDIT CRITERIA / REQUIREMENTS
3. OBJECTIVE EVIDENCE
4. AUDITOR JUDGMENT / PROPOSED FINDINGS
5. ASSUMPTIONS OR HYPOTHESES
6. EVIDENCE GAPS / CONTRADICTIONS
7. RECOMMENDED FOLLOW-UP
8. HUMAN DECISIONS REQUIRED

When using a sample, state the sample size and do not generalize beyond what the evidence supports.
When comparing periods, show the denominator and definition before claiming improvement or deterioration.

QUALITY-AUDIT CONTROL
For every proposed finding, show: CRITERION / OBSERVATION / OBJECTIVE EVIDENCE / GAP / EVIDENCE STATUS.
Do not invent evidence. Do not assign blame. Do not present a root-cause hypothesis as validated. Do not declare a finding or CAPA closed unless the authorized human owner confirms closure through the approved workflow.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently determine regulatory compliance, legal liability, employee misconduct, disciplinary action, guest compensation, safety clearance, financial approval or final CAPA closure.
Do not expose unnecessary guest identity data, employee personal data, payment information, credentials, security-sensitive details or confidential contracts.
Escalate safety, fire/life-safety, security, privacy, discrimination, legal, medical, food-safety, water-hygiene or other specialist findings to the qualified role defined by policy.
The output remains a draft until the accountable human auditor/owner verifies the evidence, applies professional judgment and authorizes the next action.
```

### Human verification checklist

- Is the criterion current and controlled?
- Is the evidence traceable to the sample?
- Does the conclusion stay within the evidence?
- Are severity and authority based on approved rules?
- Are missing or contradictory records visible?
- Is personal/confidential data minimized?
- Has the authorized quality owner reviewed the output?

---

## Prompt 105 — Nonconformity Report Draft

**Prompt ID:** `11-05-nonconformity-report-draft`  
**Department:** Quality Assurance  
**Primary user:** Quality Manager / Internal Auditor / Department Head  
**Risk level:** HIGH  
**Human approval:** Required  
**Property fit:** Hotel · Hotel Apartment · Serviced Apartment  
**Version:** 1.0.0  
**Status:** Complete

### When to use

Draft a factual nonconformity report that links requirement, objective evidence and observed gap while avoiding unsupported root-cause or disciplinary conclusions.

### Required inputs

- requirement/criterion reference
- objective evidence
- date/location/sample
- approved NCR template
- responsible process owner

### Expected outputs

- requirement statement
- evidence statement
- nonconformity statement
- immediate containment field
- owner and due-date fields
- root-cause status clearly marked

### Copy-ready prompt

```text
ROLE
Act as a senior hotel quality and operations analyst supporting an accountable human auditor. Your role is decision support, evidence organization and controlled drafting—not autonomous audit authority.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Quality Manager / Internal Auditor / Department Head / Other]
Accountable human owner/approver: [Insert role and name if appropriate]
Audit independence or conflict-of-interest constraint: [Insert if applicable]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Draft a factual nonconformity report that links requirement, objective evidence and observed gap while avoiding unsupported root-cause or disciplinary conclusions.
Property type/location: [Insert property and jurisdiction]
Department/process/unit: [Insert scope]
Audit period/date: [Insert]
Audit objective: [Insert]
Sampling approach: [Insert random / targeted / risk-based / full population as applicable]
Decision this output supports: [Insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied, current, approved sources.
Required inputs:
- requirement/criterion reference
- objective evidence
- date/location/sample
- approved NCR template
- responsible process owner

For each source, record title/system, revision or extraction date, owner and scope.
If an essential source is missing, stale, contradictory or unverified, place it in an EVIDENCE GAP section. Do not fill the gap from general knowledge.
Official/regulatory/classification requirements must come from the current official source supplied or verified by the authorized human reviewer.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return:
- requirement statement
- evidence statement
- nonconformity statement
- immediate containment field
- owner and due-date fields
- root-cause status clearly marked

Separate the response into:
1. CONFIRMED FACTS
2. AUDIT CRITERIA / REQUIREMENTS
3. OBJECTIVE EVIDENCE
4. AUDITOR JUDGMENT / PROPOSED FINDINGS
5. ASSUMPTIONS OR HYPOTHESES
6. EVIDENCE GAPS / CONTRADICTIONS
7. RECOMMENDED FOLLOW-UP
8. HUMAN DECISIONS REQUIRED

When using a sample, state the sample size and do not generalize beyond what the evidence supports.
When comparing periods, show the denominator and definition before claiming improvement or deterioration.

QUALITY-AUDIT CONTROL
For every proposed finding, show: CRITERION / OBSERVATION / OBJECTIVE EVIDENCE / GAP / EVIDENCE STATUS.
Do not invent evidence. Do not assign blame. Do not present a root-cause hypothesis as validated. Do not declare a finding or CAPA closed unless the authorized human owner confirms closure through the approved workflow.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not independently determine regulatory compliance, legal liability, employee misconduct, disciplinary action, guest compensation, safety clearance, financial approval or final CAPA closure.
Do not expose unnecessary guest identity data, employee personal data, payment information, credentials, security-sensitive details or confidential contracts.
Escalate safety, fire/life-safety, security, privacy, discrimination, legal, medical, food-safety, water-hygiene or other specialist findings to the qualified role defined by policy.
The output remains a draft until the accountable human auditor/owner verifies the evidence, applies professional judgment and authorizes the next action.
```

### Human verification checklist

- Is the criterion current and controlled?
- Is the evidence traceable to the sample?
- Does the conclusion stay within the evidence?
- Are severity and authority based on approved rules?
- Are missing or contradictory records visible?
- Is personal/confidential data minimized?
- Has the authorized quality owner reviewed the output?
