# Article 01 — The HOTEL Prompting Framework

## How to Write Professional AI Prompts for Hotel & Serviced Apartment Operations

**Track C · Hotel & Serviced Apartment AI Operations Playbook · Foundation chapter**

A hotel does not need artificial intelligence to sound clever. It needs AI to help people perform real work with fewer omissions, clearer evidence, better handovers and more consistent decisions—without allowing a language model to invent operational facts or cross an employee’s authority.

That distinction is the foundation of this playbook.

A front-office agent asking AI to improve the wording of a pre-arrival message, an engineer asking it to classify 600 work orders, a revenue manager asking it to challenge a forecast, and a general manager asking it to summarize a monthly business review are all “using AI.” But the source systems, risk, expertise and approval requirements are completely different.

The **HOTEL prompting framework** turns those differences into a repeatable operating method. It is designed for hotels, resorts, serviced apartments and extended-stay operations, with particular attention to the realities of UAE hospitality: high service expectations, multilingual guests, long-stay residents, asset-intensive apartments, cooling and utility costs, third-party distribution, corporate accounts and tightly connected departments.

The goal is not to make every prompt long. The goal is to make every important prompt **controlled**.

> **Core principle:** AI output is working material. It does not become an operational fact, commitment, approval or system update until the accountable hotel professional verifies it against the correct source of truth.

---

## 1. Why hotel prompting needs a professional method

Generic prompting advice often starts with phrases such as “give the AI a role,” “add context,” or “ask for a table.” Those techniques can improve writing, but hotel operations require more than good formatting.

A hotel runs through linked systems and responsibilities. The PMS may contain the reservation and room status. The RMS may contain a pricing recommendation. The CMMS or engineering log may contain the maintenance history. Finance validates actual cost. A controlled SOP defines an approved process. A duty manager may have authority to waive one charge but not another. A housekeeping supervisor can confirm room readiness; a language model cannot.

If a prompt ignores those boundaries, a polished answer can still be operationally wrong.

Consider a simple request:

> “Prepare tomorrow’s VIP arrival plan.”

A model can easily produce a beautiful checklist. But what if the flight time changed? What if the room is blocked for maintenance? What if the airport transfer has not been confirmed? What if the guest profile contains sensitive information? What if the requested complimentary upgrade exceeds the front-office agent’s authority?

A professional prompt therefore needs to control five things:

1. **who owns the result;**
2. **what operational decision is being supported;**
3. **which sources are trusted;**
4. **what output, evidence and exceptions are required;**
5. **what AI is not allowed to decide or expose.**

Those five controls form **HOTEL**.

---

## 2. The HOTEL prompting framework

### H — Hospitality role & human owner

Start with the hotel role being supported and the human role accountable for the output.

Weak:

> Act as a hotel expert.

Controlled:

> Act as a hotel quality analyst supporting the Operations Manager. Analyse the supplied defect records and propose investigation priorities. The Operations Manager owns corrective-action approval.

The difference is important. The first instruction gives the model a vague persona. The second defines **support scope and authority**.

For high-impact workflows, state both:

- **supported user:** the person using the output;
- **accountable owner:** the person authorized to approve or act.

These may be the same person, but they should never be assumed to be the same.

### O — Operational objective & context

The model needs the real operating problem, not just a topic.

Useful context may include:

- property type;
- city/country;
- number of rooms or apartments;
- department;
- guest-journey stage;
- business date and service window;
- occupancy or arrival/departure context;
- extended-stay versus transient mix;
- service level;
- dependencies;
- known exceptions;
- decision deadline.

A 60-unit serviced-apartment building in Abu Dhabi should not be analysed as though it were a 700-room convention hotel. A long-stay housekeeping plan is different from a one-night turnover plan. A late-night AC failure requires different escalation logic from a preventive-maintenance review.

The “O” forces the prompt to describe the **operating reality around the task**.

### T — Trusted inputs & sources of truth

This is one of the most important controls in the entire playbook.

AI should not quietly turn incomplete notes into “facts.” The prompt should identify the systems and documents the hotel treats as authoritative.

Typical examples:

| Information | Preferred source of truth |
|---|---|
| Reservation status | PMS / confirmed booking record |
| Room status | PMS plus authorized housekeeping status |
| Rate recommendation | RMS / approved revenue process |
| Posted financial actual | Finance system / approved report |
| Work-order history | CMMS / engineering system |
| SOP requirement | Controlled document repository |
| Stock balance | Approved inventory system/count |
| Utility consumption | Meter, bill or approved utility dataset |
| Guest complaint record | CRM / approved complaint log |
| Employee schedule | Approved roster |

A professional prompt should say what to do when evidence is missing or contradictory:

> Do not guess. Show the conflict, identify the owner of the missing information, name the expected source, and stop any conclusion that depends on it.

That one rule can prevent a large amount of false precision.

### E — Expected output, exceptions & evidence

The output must be designed for the workflow that receives it.

A duty-manager handover may need exceptions first. A general-manager briefing may need five decisions and their financial impact. A maintenance analysis may need a Pareto table, repeated asset IDs and an evidence-gap section. A guest communication draft may need one short message and no internal analysis.

Specify:

- required sections;
- priority order;
- table fields;
- length and tone;
- facts versus assumptions;
- confidence or evidence labels where useful;
- unresolved questions;
- exception rules;
- escalation point;
- rejected-output conditions.

A strong hotel prompt does not only define “what good looks like.” It also defines **what the model should do when normal conditions are not met**.

### L — Limits, privacy & leadership approval

The final letter defines the boundary.

Depending on the use case, limits can include:

- do not authorize compensation;
- do not cancel or modify reservations;
- do not change rates;
- do not close safety incidents;
- do not diagnose technical equipment as a substitute for a qualified engineer;
- do not make employment decisions;
- do not expose unnecessary personal data;
- do not process payment-card information, passwords or credentials;
- do not reveal confidential contracts or security-sensitive procedures;
- do not describe live status as confirmed unless it comes from the approved system.

The UAE’s federal Personal Data Protection Law provides a national framework for the confidentiality and protection of personal data and sets obligations around processing and data governance. Hotel AI workflows should therefore apply data minimisation and approved-tool rules rather than treating a prompt box as a neutral place to paste guest or employee information.

The same governance logic is consistent with broader AI-risk approaches. NIST’s AI Risk Management Framework and its Generative AI Profile emphasize structured governance, risk mapping, measurement and management; ISO/IEC 42001 provides an AI management-system model built around accountable, continually improved controls.

This playbook does not claim that using HOTEL makes an organization legally or standards compliant. It uses the same management principle: **important AI use should be owned, documented, reviewed and improved.**

---

## 3. HOTEL in one sentence

A professional hotel prompt identifies the **Hospitality role and human owner**, defines the **Operational objective and context**, restricts the model to **Trusted inputs and sources of truth**, specifies the **Expected output, evidence and exception behavior**, and preserves **Limits, privacy and leadership approval**.

That is the framework behind all 260 prompts in this repository.

---

## 4. The UAE 60-unit serviced-apartment example

Throughout the playbook we use a fictional 60-unit UAE serviced-apartment operation. The scenario is intentionally fictional so we can demonstrate operational methods without implying access to a real company’s confidential data.

Assume the property has:

- 60 units: studios, one-bedroom and two-bedroom apartments;
- leisure, corporate and extended-stay demand;
- front office, housekeeping, maintenance, reservations, finance and management teams;
- PMS, work-order records, inventory records and finance reports;
- OTA, direct and corporate bookings;
- high cooling dependency and in-room appliances;
- guest communication in multiple languages.

An Operations Manager asks:

> “Use AI to tell me which apartments are creating the most problems.”

That request is too vague. “Problems” could mean complaints, maintenance spend, utility consumption, housekeeping rework, out-of-service nights or revenue loss.

Using HOTEL, the request becomes controlled:

**H:** Support the Operations Manager. Engineering Manager validates technical conclusions; Finance validates cost figures.

**O:** Rank apartments for investigation over the last 90 days using maintenance recurrence, guest-detected defects, out-of-service nights and verified repair cost.

**T:** Use CMMS/work-order export, approved complaint log, PMS out-of-service history and finance-validated repair costs. Do not use informal staff opinions as evidence.

**E:** Return confirmed facts, a ranked table, repeated-failure patterns, data gaps, hypotheses requiring investigation, and recommended next checks. Do not call a correlation a root cause.

**L:** Do not make technical diagnoses, blame employees, authorize replacements or disclose guest identities. Engineering and Operations approve actions.

The model is now supporting a specific management workflow rather than generating an impressive but ambiguous analysis.

---

## 5. Hotel AI risk is task-dependent

Not every prompt needs the same governance burden. This playbook uses three practical risk levels.

### LOW — content assistance

Examples:

- rewrite an internal announcement;
- structure training notes;
- format a checklist from an already approved SOP;
- brainstorm non-binding meeting questions.

Human review is still expected, but the output does not directly change a guest, employee, financial, safety or contractual outcome.

### MEDIUM — operational analysis or recommendation

Examples:

- analyse complaint categories;
- summarize shift handovers;
- identify repeated maintenance defects;
- propose an inventory review;
- draft a guest response that a human will approve.

These tasks require verified inputs and an accountable reviewer.

### HIGH — sensitive or authority-linked support

Examples:

- revenue/pricing recommendations;
- compensation decisions;
- safety-related maintenance analysis;
- employee-performance analysis;
- legal/privacy-sensitive matters;
- financial forecasting used for approval;
- security incidents.

High-risk does not mean “AI prohibited” in every organization. It means the workflow requires stronger controls, approved tooling, expert review and clear authority. Some actions should remain explicitly outside AI authority.

---

## 6. Build an AI authority matrix before scaling

Hotels already use authorization levels for refunds, discounts, room moves, purchasing and capital expenditure. AI should fit inside the same discipline.

A simple authority matrix might state:

| Task | AI role | Human role |
|---|---|---|
| Draft guest reply | Draft | Agent reviews and sends |
| Summarize complaint log | Analyse | Quality/Operations validates |
| Suggest compensation options | Support only | Authorized manager decides |
| Change reservation | No direct authority | Authorized user/system action |
| Recommend rate scenario | Support | Revenue leader approves |
| Diagnose recurring AC pattern | Pattern support | Qualified engineer validates |
| Close a safety incident | No | Authorized safety/management role |
| Approve supplier | Compare evidence | Procurement/management approves |

This prevents an important failure mode: a hotel gradually treating AI recommendations as decisions simply because employees trust the tool.

---

## 7. A controlled prompt lifecycle

A professional prompt is not “finished” when it produces a good answer once.

Use this lifecycle:

### Step 1 — Select the real task

Define one workflow and the decision it supports. Avoid “help me manage my hotel.”

### Step 2 — Map source systems

List the records that contain the facts. If there is no trusted data source, solve the data problem before trying to automate the analysis.

### Step 3 — Minimize the data

Use only the information needed for the task. An apartment number may be needed; a guest passport number almost never is. Replace identifiable information with anonymous IDs where possible.

### Step 4 — Build the HOTEL prompt

Write the five control blocks. Add task-specific limits and the human approver.

### Step 5 — Test normal and exception cases

Do not test only the happy path. Try missing data, contradictory statuses, late changes, outliers and authority limits.

### Step 6 — Challenge the output

Ask whether the model invented anything, hid uncertainty, made an unauthorized decision, overgeneralized from a small dataset, or presented correlation as causation.

### Step 7 — Human verification

Check the output against the PMS, CMMS, RMS, finance record, SOP or other approved source.

### Step 8 — Approve the prompt version

If the prompt becomes repeatable operational work, give it an owner, version, risk level and review date.

### Step 9 — Monitor failures

Record meaningful errors, near misses and misuse. Update the prompt or control when the process, system or risk changes.

This is why the repository includes a prompt register, risk assessment, approval form and incident template rather than only a list of instructions.

---

## 8. What the HOTEL framework should never hide

A useful AI output should make uncertainty visible.

For operational analysis, require four labels:

**CONFIRMED FACTS** — supported by supplied trusted records.

**ASSUMPTIONS** — conditions used for analysis but not yet confirmed.

**RECOMMENDATIONS** — proposed actions or next checks.

**UNRESOLVED ITEMS** — missing, contradictory or stale information.

This simple separation is especially important in hospitality because information changes quickly. Room status, arrival times, maintenance availability, rates, guest requests, staffing and supplier confirmations can all change during the day.

AI should never convert “latest note available to the model” into “current operational truth.”

---

## 9. Prompt quality is not prompt length

Long prompts can still be poor. Short prompts can be excellent when the workflow is simple and controlled.

Evaluate prompt quality using six tests:

1. **Decision clarity** — Is the business task specific?
2. **Evidence clarity** — Are sources of truth named?
3. **Missing-data behavior** — Does the model stop rather than invent?
4. **Output usability** — Can the receiving role act on the structure?
5. **Authority clarity** — Is human approval explicit?
6. **Privacy discipline** — Is unnecessary data excluded?

If those six conditions are present, the prompt is usually far more operationally useful than a long “expert persona” instruction filled with decorative language.

---

## 10. The first 10 foundation prompts

The prompts below are the controls used to design, improve and approve the remaining 250 prompts in the playbook. They are intentionally cross-functional.
### Prompt 01 — General Hotel Prompt Builder

**Purpose:** Turn a rough hotel request into a controlled HOTEL-format prompt.

**Risk level:** Medium  
**Human approval required:** Yes

**Required inputs**

- rough request
- department
- property type
- audience
- verified facts
- constraints
- deadline
- approver

**Expected outputs**

- improved prompt
- missing information
- risk flags
- source-of-truth plan
- approval point

**Copy-ready HOTEL prompt**

```text
ROLE
Act as a senior hotel operations prompt architect supporting professional hotel and serviced-apartment teams.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Insert user role]
Accountable owner/approver: [Insert role]

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Turn a rough hotel request into a controlled HOTEL-format prompt
Property type/location: [Insert confirmed property context]
Department / guest-journey stage / operating period: [Insert confirmed context]
Decision or workflow this output supports: [Insert decision]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: rough request; department; property type; audience; verified facts; constraints; deadline; approver.
Approved sources: [PMS / RMS / CMMS / SOP / finance report / inventory system / approved policy / official source as relevant].
If an essential input is missing, stale, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: improved prompt; missing information; risk flags; source-of-truth plan; approval point.
Separate CONFIRMED FACTS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
Where inputs conflict, show the conflict and proposed verification action.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not add operational facts that were not supplied.
Do not include unnecessary personal data, payment data, credentials, security-sensitive information, confidential contracts or employee records.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational action.
```

**Trainer note:** Test the prompt with one normal case and one missing/contradictory-information case before approving it for repeat use.


### Prompt 02 — Prompt Improvement and Rewriting

**Purpose:** Diagnose and rebuild an existing hotel prompt so it is specific, reviewable and safe.

**Risk level:** Medium  
**Human approval required:** Yes

**Required inputs**

- original prompt
- intended task
- known failure
- approved inputs
- prohibited data
- desired output

**Expected outputs**

- weakness analysis
- revised prompt
- change log
- test cases
- reviewer checklist

**Copy-ready HOTEL prompt**

```text
ROLE
Act as a senior hotel operations prompt architect supporting professional hotel and serviced-apartment teams.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Insert user role]
Accountable owner/approver: [Insert role]

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Diagnose and rebuild an existing hotel prompt so it is specific, reviewable and safe
Property type/location: [Insert confirmed property context]
Department / guest-journey stage / operating period: [Insert confirmed context]
Decision or workflow this output supports: [Insert decision]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: original prompt; intended task; known failure; approved inputs; prohibited data; desired output.
Approved sources: [PMS / RMS / CMMS / SOP / finance report / inventory system / approved policy / official source as relevant].
If an essential input is missing, stale, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: weakness analysis; revised prompt; change log; test cases; reviewer checklist.
Separate CONFIRMED FACTS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
Where inputs conflict, show the conflict and proposed verification action.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Preserve the legitimate objective while removing ambiguity and unsafe authority.
Do not include unnecessary personal data, payment data, credentials, security-sensitive information, confidential contracts or employee records.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational action.
```

**Trainer note:** Test the prompt with one normal case and one missing/contradictory-information case before approving it for repeat use.


### Prompt 03 — Missing-Information Detection

**Purpose:** Identify missing inputs that could affect service, safety, cost, timing or authority.

**Risk level:** Medium  
**Human approval required:** Yes

**Required inputs**

- draft request
- confirmed inputs
- source systems
- decision required
- deadline

**Expected outputs**

- critical missing data
- important missing data
- optional enhancements
- owner/source for each item

**Copy-ready HOTEL prompt**

```text
ROLE
Act as a senior hotel operations prompt architect supporting professional hotel and serviced-apartment teams.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Insert user role]
Accountable owner/approver: [Insert role]

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Identify missing inputs that could affect service, safety, cost, timing or authority
Property type/location: [Insert confirmed property context]
Department / guest-journey stage / operating period: [Insert confirmed context]
Decision or workflow this output supports: [Insert decision]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: draft request; confirmed inputs; source systems; decision required; deadline.
Approved sources: [PMS / RMS / CMMS / SOP / finance report / inventory system / approved policy / official source as relevant].
If an essential input is missing, stale, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: critical missing data; important missing data; optional enhancements; owner/source for each item.
Separate CONFIRMED FACTS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
Where inputs conflict, show the conflict and proposed verification action.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not solve the business task; stop after the information request and prioritization.
Do not include unnecessary personal data, payment data, credentials, security-sensitive information, confidential contracts or employee records.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational action.
```

**Trainer note:** Test the prompt with one normal case and one missing/contradictory-information case before approving it for repeat use.


### Prompt 04 — Hotel Operating Context Builder

**Purpose:** Convert scattered notes into a precise hotel operating context.

**Risk level:** Medium  
**Human approval required:** Yes

**Required inputs**

- property type
- location
- department
- guest journey stage
- occupancy context
- service window
- dependencies
- known exceptions

**Expected outputs**

- context statement
- boundary conditions
- dependencies
- assumptions requiring approval

**Copy-ready HOTEL prompt**

```text
ROLE
Act as a senior hotel operations prompt architect supporting professional hotel and serviced-apartment teams.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Insert user role]
Accountable owner/approver: [Insert role]

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Convert scattered notes into a precise hotel operating context
Property type/location: [Insert confirmed property context]
Department / guest-journey stage / operating period: [Insert confirmed context]
Decision or workflow this output supports: [Insert decision]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: property type; location; department; guest journey stage; occupancy context; service window; dependencies; known exceptions.
Approved sources: [PMS / RMS / CMMS / SOP / finance report / inventory system / approved policy / official source as relevant].
If an essential input is missing, stale, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: context statement; boundary conditions; dependencies; assumptions requiring approval.
Separate CONFIRMED FACTS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
Where inputs conflict, show the conflict and proposed verification action.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not present changing property conditions as confirmed unless sourced.
Do not include unnecessary personal data, payment data, credentials, security-sensitive information, confidential contracts or employee records.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational action.
```

**Trainer note:** Test the prompt with one normal case and one missing/contradictory-information case before approving it for repeat use.


### Prompt 05 — Guest and Stakeholder Profile Definition

**Purpose:** Create an operationally useful audience profile without stereotypes or unnecessary personal data.

**Risk level:** Medium  
**Human approval required:** Yes

**Required inputs**

- guest/stakeholder type
- language
- service level
- needs
- accessibility requirements
- trip purpose
- communication channel

**Expected outputs**

- needs summary
- communication implications
- operational implications
- unanswered questions

**Copy-ready HOTEL prompt**

```text
ROLE
Act as a senior hotel operations prompt architect supporting professional hotel and serviced-apartment teams.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Insert user role]
Accountable owner/approver: [Insert role]

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Create an operationally useful audience profile without stereotypes or unnecessary personal data
Property type/location: [Insert confirmed property context]
Department / guest-journey stage / operating period: [Insert confirmed context]
Decision or workflow this output supports: [Insert decision]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: guest/stakeholder type; language; service level; needs; accessibility requirements; trip purpose; communication channel.
Approved sources: [PMS / RMS / CMMS / SOP / finance report / inventory system / approved policy / official source as relevant].
If an essential input is missing, stale, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: needs summary; communication implications; operational implications; unanswered questions.
Separate CONFIRMED FACTS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
Where inputs conflict, show the conflict and proposed verification action.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Avoid assumptions based on nationality, age, disability, religion or spending level.
Do not include unnecessary personal data, payment data, credentials, security-sensitive information, confidential contracts or employee records.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational action.
```

**Trainer note:** Test the prompt with one normal case and one missing/contradictory-information case before approving it for repeat use.


### Prompt 06 — Output-Format Specification

**Purpose:** Design the exact output structure an AI should follow for a hotel workflow.

**Risk level:** Medium  
**Human approval required:** Yes

**Required inputs**

- business task
- receiving role
- channel
- required sections
- fields
- priority logic
- examples

**Expected outputs**

- numbered output specification
- mandatory fields
- optional fields
- validation rules
- rejected-output conditions

**Copy-ready HOTEL prompt**

```text
ROLE
Act as a senior hotel operations prompt architect supporting professional hotel and serviced-apartment teams.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Insert user role]
Accountable owner/approver: [Insert role]

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Design the exact output structure an AI should follow for a hotel workflow
Property type/location: [Insert confirmed property context]
Department / guest-journey stage / operating period: [Insert confirmed context]
Decision or workflow this output supports: [Insert decision]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: business task; receiving role; channel; required sections; fields; priority logic; examples.
Approved sources: [PMS / RMS / CMMS / SOP / finance report / inventory system / approved policy / official source as relevant].
If an essential input is missing, stale, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: numbered output specification; mandatory fields; optional fields; validation rules; rejected-output conditions.
Separate CONFIRMED FACTS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
Where inputs conflict, show the conflict and proposed verification action.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not write the final business content; define the controlled format.
Do not include unnecessary personal data, payment data, credentials, security-sensitive information, confidential contracts or employee records.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational action.
```

**Trainer note:** Test the prompt with one normal case and one missing/contradictory-information case before approving it for repeat use.


### Prompt 07 — Source-of-Truth and Evidence Planner

**Purpose:** Define which hotel systems and documents must support a task.

**Risk level:** Medium  
**Human approval required:** Yes

**Required inputs**

- task
- decisions
- candidate systems
- document owners
- data freshness
- approval rules

**Expected outputs**

- source hierarchy
- evidence gaps
- conflict rules
- verification actions
- data freshness requirements

**Copy-ready HOTEL prompt**

```text
ROLE
Act as a senior hotel operations prompt architect supporting professional hotel and serviced-apartment teams.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Insert user role]
Accountable owner/approver: [Insert role]

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Define which hotel systems and documents must support a task
Property type/location: [Insert confirmed property context]
Department / guest-journey stage / operating period: [Insert confirmed context]
Decision or workflow this output supports: [Insert decision]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: task; decisions; candidate systems; document owners; data freshness; approval rules.
Approved sources: [PMS / RMS / CMMS / SOP / finance report / inventory system / approved policy / official source as relevant].
If an essential input is missing, stale, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: source hierarchy; evidence gaps; conflict rules; verification actions; data freshness requirements.
Separate CONFIRMED FACTS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
Where inputs conflict, show the conflict and proposed verification action.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not treat emails or chat messages as authoritative when a controlled system exists.
Do not include unnecessary personal data, payment data, credentials, security-sensitive information, confidential contracts or employee records.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational action.
```

**Trainer note:** Test the prompt with one normal case and one missing/contradictory-information case before approving it for repeat use.


### Prompt 08 — Exception and Escalation Prompt Builder

**Purpose:** Add explicit exception handling and escalation logic to an AI-supported workflow.

**Risk level:** Medium  
**Human approval required:** Yes

**Required inputs**

- normal process
- known exceptions
- thresholds
- roles
- authority limits
- escalation contacts by role

**Expected outputs**

- exception categories
- trigger conditions
- stabilization actions
- escalation path
- evidence record

**Copy-ready HOTEL prompt**

```text
ROLE
Act as a senior hotel operations prompt architect supporting professional hotel and serviced-apartment teams.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Insert user role]
Accountable owner/approver: [Insert role]

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Add explicit exception handling and escalation logic to an AI-supported workflow
Property type/location: [Insert confirmed property context]
Department / guest-journey stage / operating period: [Insert confirmed context]
Decision or workflow this output supports: [Insert decision]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: normal process; known exceptions; thresholds; roles; authority limits; escalation contacts by role.
Approved sources: [PMS / RMS / CMMS / SOP / finance report / inventory system / approved policy / official source as relevant].
If an essential input is missing, stale, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: exception categories; trigger conditions; stabilization actions; escalation path; evidence record.
Separate CONFIRMED FACTS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
Where inputs conflict, show the conflict and proposed verification action.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not invent escalation contacts or authority limits.
Do not include unnecessary personal data, payment data, credentials, security-sensitive information, confidential contracts or employee records.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational action.
```

**Trainer note:** Test the prompt with one normal case and one missing/contradictory-information case before approving it for repeat use.


### Prompt 09 — Prompt Risk and Authority Classifier

**Purpose:** Classify an AI hotel use case by operational risk and required human authority.

**Risk level:** Medium  
**Human approval required:** Yes

**Required inputs**

- use case
- data involved
- guest impact
- financial impact
- safety impact
- decision authority

**Expected outputs**

- risk level
- reason
- prohibited actions
- minimum reviewer
- approval requirement
- controls

**Copy-ready HOTEL prompt**

```text
ROLE
Act as a senior hotel operations prompt architect supporting professional hotel and serviced-apartment teams.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Insert user role]
Accountable owner/approver: [Insert role]

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Classify an AI hotel use case by operational risk and required human authority
Property type/location: [Insert confirmed property context]
Department / guest-journey stage / operating period: [Insert confirmed context]
Decision or workflow this output supports: [Insert decision]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: use case; data involved; guest impact; financial impact; safety impact; decision authority.
Approved sources: [PMS / RMS / CMMS / SOP / finance report / inventory system / approved policy / official source as relevant].
If an essential input is missing, stale, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: risk level; reason; prohibited actions; minimum reviewer; approval requirement; controls.
Separate CONFIRMED FACTS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
Where inputs conflict, show the conflict and proposed verification action.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not downgrade safety, privacy, financial or legal risk for convenience.
Do not include unnecessary personal data, payment data, credentials, security-sensitive information, confidential contracts or employee records.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational action.
```

**Trainer note:** Test the prompt with one normal case and one missing/contradictory-information case before approving it for repeat use.


### Prompt 10 — Prompt Verification and Approval Checklist

**Purpose:** Create a repeatable verification checklist before AI output enters hotel operations.

**Risk level:** Medium  
**Human approval required:** Yes

**Required inputs**

- prompt
- output
- sources used
- department
- decision
- approver
- known risks

**Expected outputs**

- fact checks
- system checks
- privacy checks
- authority checks
- exception checks
- approval record

**Copy-ready HOTEL prompt**

```text
ROLE
Act as a senior hotel operations prompt architect supporting professional hotel and serviced-apartment teams.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Insert user role]
Accountable owner/approver: [Insert role]

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Create a repeatable verification checklist before AI output enters hotel operations
Property type/location: [Insert confirmed property context]
Department / guest-journey stage / operating period: [Insert confirmed context]
Decision or workflow this output supports: [Insert decision]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: prompt; output; sources used; department; decision; approver; known risks.
Approved sources: [PMS / RMS / CMMS / SOP / finance report / inventory system / approved policy / official source as relevant].
If an essential input is missing, stale, contradictory or unconfirmed, stop and list what is required, its owner and source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: fact checks; system checks; privacy checks; authority checks; exception checks; approval record.
Separate CONFIRMED FACTS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
Where inputs conflict, show the conflict and proposed verification action.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not mark an output approved; only define the verification and approval steps.
Do not include unnecessary personal data, payment data, credentials, security-sensitive information, confidential contracts or employee records.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational action.
```

**Trainer note:** Test the prompt with one normal case and one missing/contradictory-information case before approving it for repeat use.

---

## 11. Prompt verification checklist

Before operational use, ask:

- Is the accountable human owner named?
- Is the operating objective specific?
- Are the approved sources of truth identified?
- Is the information current enough for the decision?
- Are facts separated from assumptions and recommendations?
- Does the prompt expose missing or contradictory inputs?
- Are guest and employee data minimized?
- Are payment, credential and security data excluded?
- Does the output remain inside the user’s financial, safety and operational authority?
- Does a qualified person review technical, financial, legal, privacy, safety or employment-sensitive conclusions?
- Is the final action recorded in the hotel’s normal system rather than only in an AI conversation?

If the answer to an important question is “no,” the prompt is not operationally ready.

---

## 12. Management implementation: the first 30 days

### Week 1 — Inventory existing AI use

Ask every department where employees already use generative AI. Do not begin with punishment. The goal is visibility: guest messages, translations, complaint replies, spreadsheet analysis, SOP drafting, marketing, engineering summaries and revenue work may already be happening informally.

### Week 2 — Classify tasks and sources

Assign LOW, MEDIUM or HIGH risk. Map the PMS, RMS, CMMS, finance, inventory and controlled-document sources needed for each task. Identify prohibited data.

### Week 3 — Pilot three controlled prompts

Choose useful but manageable workflows. Examples: shift-handover summary, complaint categorization and preventive-maintenance backlog review. Test normal and exception cases.

### Week 4 — Approve, train and measure

Version the successful prompts. Train the users. Track rework, time saved, missing-data detection, hallucination/error events and user adoption. Stop any prompt that creates more risk or rework than value.

The target is not “maximum AI usage.” The target is **better controlled work**.

---

## 13. How Article 01 connects to the remaining 25 chapters

Article 01 is the control layer. The following toolkits apply HOTEL to specific departments and management problems: operations management, front office, reservations, extended stay, housekeeping, engineering, predictive maintenance, guest experience, service recovery, quality audit, SOP design, Lean Six Sigma, ESG, utilities, procurement, inventory, revenue, sales, OTA/distribution, finance, dashboards, workforce, general management, the hotel control tower and responsible AI governance.
Each chapter adds 10 prompts, bringing the full library to **260 prompts**.

The same discipline applies everywhere:

> **Use AI to structure, analyse, draft and challenge. Use hotel systems and accountable professionals to confirm, authorize and act.**

---

## 14. Key takeaway

The value of hotel AI does not come from writing increasingly clever prompts. It comes from connecting AI to the same operating controls that make a hotel reliable: ownership, source records, exception handling, authority, privacy, evidence and review.

The HOTEL framework turns that idea into a repeatable method:

**H — Hospitality role & human owner**  
**O — Operational objective & context**  
**T — Trusted inputs & sources of truth**  
**E — Expected output, exceptions & evidence**  
**L — Limits, privacy & leadership approval**

If those five controls are clear, AI can become a useful layer inside hotel operations without pretending to be the PMS, the engineer, the revenue manager, the finance controller or the general manager.

---

## Sources and further reading

1. **UAE Government — Data protection laws.** Overview of Federal Decree-Law No. 45 of 2021 concerning the Protection of Personal Data and UAE data-governance responsibilities. https://u.ae/en/about-the-uae/digital-uae/data/data-protection-laws
2. **UAE Legislation — Federal Decree-Law No. 45 of 2021 Concerning the Protection of Personal Data.** https://uaelegislation.gov.ae/en/legislations/1972/download
3. **NIST — AI Risk Management Framework.** Voluntary framework for managing AI risks; NIST also publishes a Generative AI Profile. https://www.nist.gov/itl/ai-risk-management-framework
4. **NIST AI 600-1 — Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile.** July 2024, updated publication page in 2026. https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
5. **ISO — ISO/IEC 42001 AI management systems.** Overview of the management-system approach to accountable AI governance and continuous improvement. https://www.iso.org/artificial-intelligence/ai-management-systems

### Evidence boundary

This chapter provides an original operational prompting framework and training guidance. It is not legal, cybersecurity, engineering, revenue-management or privacy advice. Organizations should apply their own policies, approved AI tools, contracts, security controls and qualified professional review. The fictional 60-unit serviced-apartment case is illustrative and does not represent a specific hotel company.