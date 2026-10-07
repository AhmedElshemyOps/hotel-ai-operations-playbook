# Article 16 — Hotel Procurement AI Toolkit

## 10 Professional AI Prompts for Requisitions, RFQs, Bid Evaluation, Total Cost, Negotiation, Contracts, Supplier Risk and Performance

**Track C · Hotel & Serviced Apartment AI Operations Playbook · Procurement chapter**

Hotel procurement is where service requirements become commercial commitments. The quality of that process affects guest experience, operating continuity, asset reliability, cash flow, compliance and cost.

The operating principle for this chapter is:

> **AI may structure procurement evidence, normalize bids and challenge assumptions. It must not award suppliers, make binding commitments, manipulate evaluation criteria or bypass the hotel's approved authority.**

The ten prompts follow one procurement-control cycle:

> **Need → Specification → Source → Normalize → Evaluate → Negotiate → Approve → Contract → Monitor → Review**

This chapter continues the fictional 60-unit UAE serviced-apartment case. All property/supplier calculations are illustrative unless explicitly identified as external verified context.

---


## 1. Procurement is a control process, not a price hunt

Hotel procurement sits between operations, quality, finance, engineering, guest experience and supplier markets.

A weak buying decision can appear inexpensive on the purchase order and become expensive after delivery through:

- incorrect specifications;
- repeated failures;
- emergency replacement;
- guest complaints;
- late delivery;
- warranty disputes;
- high consumable use;
- installation cost;
- operational downtime;
- poor after-sales service.

The procurement question is therefore not:

> “Who is cheapest?”

It is:

> “Which compliant option creates the best approved value for the required service level and risk profile, using a fair and auditable process?”

AI can help organize that decision. It must not become the decision authority.

---

## 2. The HOTEL framework for procurement

**H — Hospitality role & human owner**  
Procurement controls the sourcing process. The user department owns the operational requirement. Engineering or another specialist owns technical suitability where relevant. Finance verifies budget and financial analysis. Legal reviews contractual risk where required. The authorized DOA holder approves commitment.

**O — Operational objective & context**  
Define what the hotel actually needs, when it is needed, where it will be used, the service/quality level and the commercial boundary.

**T — Trusted inputs & sources of truth**  
Use approved requisitions, specifications, RFQs, supplier quotations, supplier master data, technical evaluations, contracts, POs, receiving records and approved budgets.

**E — Expected output, evidence & exceptions**  
Require normalized comparison, assumptions, deviations, clarification items, risk, scoring logic and approvals.

**L — Limits, privacy & leadership approval**  
AI cannot award business, negotiate binding terms, invent supplier facts or bypass procurement policy.

---

## 3. Fictional UAE case: towels for a 60-unit serviced-apartment portfolio

Assume the fictional 60-unit portfolio needs a replacement batch of premium bath towels.

Supplier A quotes **AED 80 per pack**.

Supplier B quotes **AED 84 per pack**.

A price-only view selects Supplier A.

But management discovers that the bids are not equivalent.

Illustrative assumptions:

| Cost/condition | Supplier A | Supplier B |
|---|---:|---:|
| Quoted unit price | AED 80 | AED 84 |
| Freight per unit | AED 5 | Included |
| Expected early replacement | 8% | 2% |
| Warranty | Limited | Stronger |
| Lead time | 35 days | 18 days |
| Sample/laundry test | Marginal | Passed |

For 500 units, the initial landed-cost illustration is:

Supplier A: **500 × (80 + 5) = AED 42,500**

Supplier B: **500 × 84 = AED 42,000**

Even before quality-related replacement, the apparently cheaper unit price is not the cheaper landed cost.

If the approved quality test also indicates a higher replacement rate, total cost may move further.

This is illustrative—not a real supplier comparison.

The lesson is operational:

> **Never let AI compare the headline number before it normalizes the commercial scope.**

---

## 4. Requisition quality is the first procurement control

Prompt 151 checks the purchase request before sourcing starts.

A poor requisition creates downstream waste.

Examples:

- “buy 10 TVs” with no size/specification;
- “replace AC compressor” without asset reference;
- “cleaning chemicals” without approved product/usage requirements;
- “guest amenities” without packaging or brand-standard requirements;
- urgent date with no explanation;
- quantity inconsistent with PAR or consumption history.

AI can identify what is missing.

It should not invent the specification to make the request look complete.

---

## 5. RFQ design determines whether bids can be compared

Prompt 152 structures the RFQ.

A good RFQ gives suppliers the same commercial question.

It should make clear:

- item/service description;
- quantity;
- unit of measure;
- mandatory specification;
- acceptable alternatives;
- delivery location;
- delivery deadline;
- installation requirements;
- warranty/service;
- quotation validity;
- payment/commercial response fields;
- required documents;
- evaluation process where appropriate.

If suppliers answer different questions, the hotel cannot fairly compare the answers.

---

## 6. Normalize bids before scoring

Prompt 153 is one of the highest-value procurement controls.

Imagine:

Supplier X includes freight and installation.

Supplier Y excludes both.

Supplier Z proposes a technically different product.

A raw price table is misleading.

Normalize:

- currency;
- quantity;
- unit;
- tax;
- freight;
- installation;
- consumables;
- warranty;
- lead time;
- payment terms;
- scope exclusions;
- substitutions.

Where a difference cannot be normalized, show it as an unresolved deviation rather than forcing false comparability.

---

## 7. Supplier scoring: criteria before outcome

Prompt 154 builds a weighted evaluation.

A hotel may choose criteria such as:

- technical compliance;
- quality;
- commercial value;
- lead time;
- service capability;
- warranty;
- historical performance;
- sustainability/compliance;
- business continuity.

The weights must be approved according to the procurement process.

AI must not adjust weights after seeing which supplier wins.

That creates outcome-driven scoring rather than evaluation.

---

## 8. Total cost of ownership

Prompt 155 expands the decision beyond purchase price.

For equipment, FF&E or recurring operating supplies, TCO may include:

**Acquisition**
- unit price;
- freight;
- customs where applicable;
- installation;
- commissioning.

**Operation**
- energy;
- water;
- consumables;
- licenses;
- labor.

**Reliability**
- maintenance;
- spare parts;
- downtime;
- replacement.

**End of life**
- disposal;
- removal;
- residual value where relevant.

The model must expose assumptions.

An AI-generated 5-year TCO with invented failure rates is worse than no model at all.

---

## 9. Negotiation preparation, not autonomous negotiation

Prompt 156 prepares the human negotiator.

Useful outputs include:

- commercial gaps;
- target points;
- questions;
- concessions to request;
- non-price value;
- alternative options;
- escalation limits;
- items requiring approval.

AI should never tell a supplier that a deal is accepted unless an authorized person actually accepts it.

Procurement authority remains human.

---

## 10. Contract and SLA review

Prompt 157 creates a structured commercial review.

It can flag areas such as:

- scope mismatch;
- price schedule;
- payment terms;
- delivery;
- acceptance;
- warranty;
- service response;
- KPI/SLA;
- penalties/service credits;
- renewal;
- termination;
- confidentiality;
- insurance;
- liability;
- data/privacy;
- governing-law clauses for Legal review.

The AI does not provide the legal conclusion.

It identifies what qualified reviewers need to examine.

---

## 11. Supplier risk and continuity

Prompt 158 looks beyond today's quote.

A low-cost supplier can become a high operational risk if the hotel depends on:

- one factory;
- one importer;
- one critical technician;
- long international lead time;
- a single spare part;
- one proprietary consumable;
- weak replacement capacity.

Criticality should influence sourcing and contingency planning.

A supplier risk review must also avoid unsupported allegations. Use verified evidence and clearly label missing information.

---

## 12. Supplier performance after award

Prompt 159 turns procurement into a closed loop.

Possible KPIs:

| KPI | Example definition |
|---|---|
| On-time delivery | Deliveries on/before confirmed date ÷ due deliveries |
| Quality acceptance | Accepted quantity ÷ received quantity |
| PO accuracy | Correct invoice/PO transactions ÷ total |
| SLA response | Cases within SLA ÷ SLA cases |
| Corrective-action closure | Actions closed by due date ÷ due actions |
| Contract compliance | Verified compliant requirements ÷ sampled requirements |

A supplier should not receive a poor score because of a hotel-caused delay.

Evidence and responsibility matter.

---

## 13. Savings need a controlled definition

Procurement teams can accidentally overstate savings.

Possible categories include:

- negotiated price reduction;
- cost avoidance;
- demand reduction;
- specification optimization;
- process saving;
- TCO benefit.

These are not identical.

A negotiated quote reduction may be reportable as a sourcing benefit under an approved method. It does not automatically equal cash saved in the P&L.

Finance should approve the benefit methodology.

The prompt library therefore separates:

**quoted difference → negotiated value → approved benefit → realized/verified financial effect**

---

## 14. Sustainable procurement without unsupported claims

Article 14 established the ESG controls.

Procurement can incorporate sustainability through approved criteria such as:

- packaging;
- material content;
- energy/water performance;
- repairability;
- product life;
- take-back;
- local sourcing where relevant;
- supplier certifications;
- environmental or social evidence.

But a green logo or supplier marketing statement is not automatically verified evidence.

ISO 20400:2017 provides guidance on integrating sustainability into procurement and remains current after ISO's 2023 review.

---

## 15. Ethical procurement and conflicts

AI does not remove human procurement ethics.

Controls should include:

- conflict-of-interest declaration;
- gifts/hospitality rules;
- confidentiality;
- equal information to bidders where required;
- bid-access controls;
- evaluation traceability;
- segregation of duties;
- approval thresholds;
- exception documentation.

If a user asks AI to manipulate a score to justify a preferred supplier, the correct response is to stop.

---

## 16. 30-day procurement-control implementation plan

**Days 1–5 — Define control**
- map requisition-to-PO process;
- confirm DOA;
- identify approved supplier master;
- confirm standard RFQ and evaluation templates;
- document single-source/exception rules.

**Days 6–10 — Improve inputs**
- standardize requisition fields;
- define category specifications;
- create bid-normalization sheet;
- define clarification log.

**Days 11–15 — Strengthen evaluation**
- approve scoring criteria;
- create TCO template;
- define technical/commercial sign-offs;
- establish conflict declarations.

**Days 16–20 — Control contracts**
- build contract/SLA checklist;
- create renewal calendar;
- map Legal/Finance review triggers;
- define award record.

**Days 21–25 — Measure suppliers**
- create supplier scorecard;
- define quality/delivery KPIs;
- establish corrective-action workflow;
- identify critical suppliers.

**Days 26–30 — Management review**
- review spend/pipeline;
- review risks and expiring contracts;
- review validated benefits;
- assign actions and owners.

---

## 17. Before → Action → After → AED Saved

A procurement improvement story should show:

**Before**  
Approved comparable baseline price/cost and demand.

**Action**  
Documented sourcing, negotiation, specification or demand intervention.

**After**  
Actual approved purchase/consumption outcome.

**AED Saved / Benefit**  
Calculated under the organization's approved methodology and validated by Finance.

Do not label a supplier's opening quote minus final quote as realized cash saving without the approved methodology.

---

## 18. Management checklist

Before approving an AI-supported procurement recommendation, ask:

- Is the business need approved?
- Is the specification complete?
- Are bids genuinely comparable?
- Are exclusions visible?
- Are weights approved?
- Is technical evaluation separate from commercial analysis?
- Is TCO based on verified assumptions?
- Is the budget confirmed?
- Are conflicts declared?
- Are required supplier checks complete?
- Has Legal reviewed relevant contract risk?
- Is the approver within DOA?
- Are savings defined under the approved Finance method?

If not, the decision is not ready.

---

## 19. Key takeaway

Professional procurement is not the automation of supplier selection.

It is the disciplined management of evidence and authority:

> **need → specification → fair sourcing → normalized evidence → evaluation → authorized decision → controlled contract → measured supplier performance**

AI can make that chain faster and clearer.

It must not break it.


---

## 20. Ten professional prompt templates

### Prompt 151 — Purchase Requisition Quality Checker

**When to use:** Check whether a hotel purchase request is complete, justified and ready to enter the sourcing process.

**Required inputs**
- approved requisition/request
- business need and quantity
- specification or scope
- budget/cost-center information
- required-by date and requester

**Expected outputs**
- completeness check
- missing-information list
- specification/quantity conflicts
- approval-route requirements

**Risk level:** Medium

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel procurement and commercial analysis assistant supporting Procurement, Finance, Operations and the relevant technical/user department. You do not replace the authorized buyer, budget owner, technical evaluator, Finance approver, Legal counsel or delegation-of-authority holder.

OPERATIONAL OBJECTIVE
Complete the task: Purchase Requisition Quality Checker. Use the supplied evidence to support a transparent and auditable hotel procurement decision.

PROPERTY CONTEXT
Property / portfolio: [NAME]
Location: [CITY / COUNTRY]
Property type: [HOTEL / SERVICED APARTMENT]
Category: [F&B / HOUSEKEEPING / ENGINEERING / IT / OS&E / FF&E / SERVICE / OTHER]
Request / RFQ / contract reference: [REFERENCE]
Required-by date: [DATE]
Approval framework: [DOA / PROCUREMENT POLICY / BUDGET RULE]

TRUSTED INPUTS
Use only:
- [APPROVED REQUISITION / RFQ / SPECIFICATION]
- [SUPPLIER QUOTATIONS OR PROPOSALS]
- [APPROVED BUDGET / COST CENTER]
- [TECHNICAL EVALUATION]
- [CONTRACT / SLA / COMMERCIAL TERMS]
- [PO / RECEIVING / QUALITY / PERFORMANCE RECORDS]
- [APPROVED SUPPLIER MASTER / DUE-DILIGENCE EVIDENCE]
- [OTHER VERIFIED SOURCE]

ANALYSIS / METHOD
1. Confirm the requirement, quantity, unit of measure, scope and commercial boundary.
2. Separate mandatory requirements from preferences.
3. Normalize quotations before comparing price or score.
4. Identify exclusions, substitutions, tax, freight, installation, warranty, lead-time and payment-term differences.
5. Show every formula, weight and assumption used in scoring or total-cost analysis.
6. Separate supplier-stated claims from hotel-verified evidence.
7. Separate UNIT PRICE, LANDED COST, TOTAL COST OF OWNERSHIP and VERIFIED SAVING.
8. Flag conflicts of interest, single-source conditions, policy exceptions or missing approvals for human review.
9. Do not change evaluation weights after seeing supplier results unless the authorized process formally approves and records the change.
10. Keep technical, commercial, Legal, Finance and operational approvals distinct.

OUTPUT
Return:
A. Executive summary
B. Data/completeness check
C. Normalized evidence table
D. Commercial/technical deviations
E. Risks and unresolved clarifications
F. Calculation/score/assumption register
G. Recommended next step — not an unauthorized award
H. Required approvers
I. Actions, owner and due date
J. Audit trail / evidence gaps

LIMITS
Risk level: Medium.
Do not fabricate quotations, supplier capability, compliance status, market price, savings, warranty, lead time or contractual obligations.
Do not select or award a supplier on behalf of the authorized committee/manager.
Do not commit price, volume, payment, contract or exclusivity terms.
Do not provide legal conclusions; flag clauses for qualified Legal review.
Do not expose confidential bids or supplier information outside the authorized workflow.

HUMAN REVIEW
Procurement verifies sourcing process and commercial comparison.
The user/technical department verifies specifications and technical suitability.
Finance verifies budget, cost model and financial-benefit claims.
Legal reviews contractual/legal terms where required.
The authorized DOA holder or evaluation committee approves award/commitment.

STOP RULE
If quotations are not comparable, a mandatory specification is missing, a conflict/policy exception is unresolved, or the approval authority is unclear, stop and request resolution instead of recommending an award.
```

**Professional hotel trainer's note:** Keep the approved requirement, commercial boundary, comparison logic and human authority visible. If bids are not comparable or approval is unclear, stop rather than manufacture a recommendation.

---

### Prompt 152 — RFQ & Specification Builder

**When to use:** Turn an approved hotel requirement into a comparable RFQ without inventing technical or brand specifications.

**Required inputs**
- approved requirement
- technical/user specification
- quantity and delivery location
- service/warranty expectations
- commercial instructions

**Expected outputs**
- RFQ structure
- mandatory vs optional requirements
- supplier response schedule
- clarification questions and exclusions

**Risk level:** Medium

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel procurement and commercial analysis assistant supporting Procurement, Finance, Operations and the relevant technical/user department. You do not replace the authorized buyer, budget owner, technical evaluator, Finance approver, Legal counsel or delegation-of-authority holder.

OPERATIONAL OBJECTIVE
Complete the task: RFQ & Specification Builder. Use the supplied evidence to support a transparent and auditable hotel procurement decision.

PROPERTY CONTEXT
Property / portfolio: [NAME]
Location: [CITY / COUNTRY]
Property type: [HOTEL / SERVICED APARTMENT]
Category: [F&B / HOUSEKEEPING / ENGINEERING / IT / OS&E / FF&E / SERVICE / OTHER]
Request / RFQ / contract reference: [REFERENCE]
Required-by date: [DATE]
Approval framework: [DOA / PROCUREMENT POLICY / BUDGET RULE]

TRUSTED INPUTS
Use only:
- [APPROVED REQUISITION / RFQ / SPECIFICATION]
- [SUPPLIER QUOTATIONS OR PROPOSALS]
- [APPROVED BUDGET / COST CENTER]
- [TECHNICAL EVALUATION]
- [CONTRACT / SLA / COMMERCIAL TERMS]
- [PO / RECEIVING / QUALITY / PERFORMANCE RECORDS]
- [APPROVED SUPPLIER MASTER / DUE-DILIGENCE EVIDENCE]
- [OTHER VERIFIED SOURCE]

ANALYSIS / METHOD
1. Confirm the requirement, quantity, unit of measure, scope and commercial boundary.
2. Separate mandatory requirements from preferences.
3. Normalize quotations before comparing price or score.
4. Identify exclusions, substitutions, tax, freight, installation, warranty, lead-time and payment-term differences.
5. Show every formula, weight and assumption used in scoring or total-cost analysis.
6. Separate supplier-stated claims from hotel-verified evidence.
7. Separate UNIT PRICE, LANDED COST, TOTAL COST OF OWNERSHIP and VERIFIED SAVING.
8. Flag conflicts of interest, single-source conditions, policy exceptions or missing approvals for human review.
9. Do not change evaluation weights after seeing supplier results unless the authorized process formally approves and records the change.
10. Keep technical, commercial, Legal, Finance and operational approvals distinct.

OUTPUT
Return:
A. Executive summary
B. Data/completeness check
C. Normalized evidence table
D. Commercial/technical deviations
E. Risks and unresolved clarifications
F. Calculation/score/assumption register
G. Recommended next step — not an unauthorized award
H. Required approvers
I. Actions, owner and due date
J. Audit trail / evidence gaps

LIMITS
Risk level: Medium.
Do not fabricate quotations, supplier capability, compliance status, market price, savings, warranty, lead time or contractual obligations.
Do not select or award a supplier on behalf of the authorized committee/manager.
Do not commit price, volume, payment, contract or exclusivity terms.
Do not provide legal conclusions; flag clauses for qualified Legal review.
Do not expose confidential bids or supplier information outside the authorized workflow.

HUMAN REVIEW
Procurement verifies sourcing process and commercial comparison.
The user/technical department verifies specifications and technical suitability.
Finance verifies budget, cost model and financial-benefit claims.
Legal reviews contractual/legal terms where required.
The authorized DOA holder or evaluation committee approves award/commitment.

STOP RULE
If quotations are not comparable, a mandatory specification is missing, a conflict/policy exception is unresolved, or the approval authority is unclear, stop and request resolution instead of recommending an award.
```

**Professional hotel trainer's note:** Keep the approved requirement, commercial boundary, comparison logic and human authority visible. If bids are not comparable or approval is unclear, stop rather than manufacture a recommendation.

---

### Prompt 153 — Bid Normalization & Comparison Analyzer

**When to use:** Normalize supplier quotations so management compares equivalent scope, quantities, taxes, freight, warranty and commercial terms.

**Required inputs**
- supplier quotations
- approved RFQ
- quantity and unit-of-measure rules
- delivery/incoterm assumptions where applicable
- tax/payment/warranty terms

**Expected outputs**
- normalized comparison table
- scope/exclusion differences
- commercial deviations
- unresolved clarification items

**Risk level:** High

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel procurement and commercial analysis assistant supporting Procurement, Finance, Operations and the relevant technical/user department. You do not replace the authorized buyer, budget owner, technical evaluator, Finance approver, Legal counsel or delegation-of-authority holder.

OPERATIONAL OBJECTIVE
Complete the task: Bid Normalization & Comparison Analyzer. Use the supplied evidence to support a transparent and auditable hotel procurement decision.

PROPERTY CONTEXT
Property / portfolio: [NAME]
Location: [CITY / COUNTRY]
Property type: [HOTEL / SERVICED APARTMENT]
Category: [F&B / HOUSEKEEPING / ENGINEERING / IT / OS&E / FF&E / SERVICE / OTHER]
Request / RFQ / contract reference: [REFERENCE]
Required-by date: [DATE]
Approval framework: [DOA / PROCUREMENT POLICY / BUDGET RULE]

TRUSTED INPUTS
Use only:
- [APPROVED REQUISITION / RFQ / SPECIFICATION]
- [SUPPLIER QUOTATIONS OR PROPOSALS]
- [APPROVED BUDGET / COST CENTER]
- [TECHNICAL EVALUATION]
- [CONTRACT / SLA / COMMERCIAL TERMS]
- [PO / RECEIVING / QUALITY / PERFORMANCE RECORDS]
- [APPROVED SUPPLIER MASTER / DUE-DILIGENCE EVIDENCE]
- [OTHER VERIFIED SOURCE]

ANALYSIS / METHOD
1. Confirm the requirement, quantity, unit of measure, scope and commercial boundary.
2. Separate mandatory requirements from preferences.
3. Normalize quotations before comparing price or score.
4. Identify exclusions, substitutions, tax, freight, installation, warranty, lead-time and payment-term differences.
5. Show every formula, weight and assumption used in scoring or total-cost analysis.
6. Separate supplier-stated claims from hotel-verified evidence.
7. Separate UNIT PRICE, LANDED COST, TOTAL COST OF OWNERSHIP and VERIFIED SAVING.
8. Flag conflicts of interest, single-source conditions, policy exceptions or missing approvals for human review.
9. Do not change evaluation weights after seeing supplier results unless the authorized process formally approves and records the change.
10. Keep technical, commercial, Legal, Finance and operational approvals distinct.

OUTPUT
Return:
A. Executive summary
B. Data/completeness check
C. Normalized evidence table
D. Commercial/technical deviations
E. Risks and unresolved clarifications
F. Calculation/score/assumption register
G. Recommended next step — not an unauthorized award
H. Required approvers
I. Actions, owner and due date
J. Audit trail / evidence gaps

LIMITS
Risk level: High.
Do not fabricate quotations, supplier capability, compliance status, market price, savings, warranty, lead time or contractual obligations.
Do not select or award a supplier on behalf of the authorized committee/manager.
Do not commit price, volume, payment, contract or exclusivity terms.
Do not provide legal conclusions; flag clauses for qualified Legal review.
Do not expose confidential bids or supplier information outside the authorized workflow.

HUMAN REVIEW
Procurement verifies sourcing process and commercial comparison.
The user/technical department verifies specifications and technical suitability.
Finance verifies budget, cost model and financial-benefit claims.
Legal reviews contractual/legal terms where required.
The authorized DOA holder or evaluation committee approves award/commitment.

STOP RULE
If quotations are not comparable, a mandatory specification is missing, a conflict/policy exception is unresolved, or the approval authority is unclear, stop and request resolution instead of recommending an award.
```

**Professional hotel trainer's note:** Keep the approved requirement, commercial boundary, comparison logic and human authority visible. If bids are not comparable or approval is unclear, stop rather than manufacture a recommendation.

---

### Prompt 154 — Supplier Evaluation & Weighted Scoring Builder

**When to use:** Create an evidence-based supplier evaluation using approved criteria and weights rather than AI preference.

**Required inputs**
- approved evaluation criteria
- approved weights
- normalized bids
- technical evaluation
- supplier evidence and due diligence

**Expected outputs**
- weighted scorecard
- evidence by criterion
- sensitivity/weight notes
- human evaluation and approval gaps

**Risk level:** High

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel procurement and commercial analysis assistant supporting Procurement, Finance, Operations and the relevant technical/user department. You do not replace the authorized buyer, budget owner, technical evaluator, Finance approver, Legal counsel or delegation-of-authority holder.

OPERATIONAL OBJECTIVE
Complete the task: Supplier Evaluation & Weighted Scoring Builder. Use the supplied evidence to support a transparent and auditable hotel procurement decision.

PROPERTY CONTEXT
Property / portfolio: [NAME]
Location: [CITY / COUNTRY]
Property type: [HOTEL / SERVICED APARTMENT]
Category: [F&B / HOUSEKEEPING / ENGINEERING / IT / OS&E / FF&E / SERVICE / OTHER]
Request / RFQ / contract reference: [REFERENCE]
Required-by date: [DATE]
Approval framework: [DOA / PROCUREMENT POLICY / BUDGET RULE]

TRUSTED INPUTS
Use only:
- [APPROVED REQUISITION / RFQ / SPECIFICATION]
- [SUPPLIER QUOTATIONS OR PROPOSALS]
- [APPROVED BUDGET / COST CENTER]
- [TECHNICAL EVALUATION]
- [CONTRACT / SLA / COMMERCIAL TERMS]
- [PO / RECEIVING / QUALITY / PERFORMANCE RECORDS]
- [APPROVED SUPPLIER MASTER / DUE-DILIGENCE EVIDENCE]
- [OTHER VERIFIED SOURCE]

ANALYSIS / METHOD
1. Confirm the requirement, quantity, unit of measure, scope and commercial boundary.
2. Separate mandatory requirements from preferences.
3. Normalize quotations before comparing price or score.
4. Identify exclusions, substitutions, tax, freight, installation, warranty, lead-time and payment-term differences.
5. Show every formula, weight and assumption used in scoring or total-cost analysis.
6. Separate supplier-stated claims from hotel-verified evidence.
7. Separate UNIT PRICE, LANDED COST, TOTAL COST OF OWNERSHIP and VERIFIED SAVING.
8. Flag conflicts of interest, single-source conditions, policy exceptions or missing approvals for human review.
9. Do not change evaluation weights after seeing supplier results unless the authorized process formally approves and records the change.
10. Keep technical, commercial, Legal, Finance and operational approvals distinct.

OUTPUT
Return:
A. Executive summary
B. Data/completeness check
C. Normalized evidence table
D. Commercial/technical deviations
E. Risks and unresolved clarifications
F. Calculation/score/assumption register
G. Recommended next step — not an unauthorized award
H. Required approvers
I. Actions, owner and due date
J. Audit trail / evidence gaps

LIMITS
Risk level: High.
Do not fabricate quotations, supplier capability, compliance status, market price, savings, warranty, lead time or contractual obligations.
Do not select or award a supplier on behalf of the authorized committee/manager.
Do not commit price, volume, payment, contract or exclusivity terms.
Do not provide legal conclusions; flag clauses for qualified Legal review.
Do not expose confidential bids or supplier information outside the authorized workflow.

HUMAN REVIEW
Procurement verifies sourcing process and commercial comparison.
The user/technical department verifies specifications and technical suitability.
Finance verifies budget, cost model and financial-benefit claims.
Legal reviews contractual/legal terms where required.
The authorized DOA holder or evaluation committee approves award/commitment.

STOP RULE
If quotations are not comparable, a mandatory specification is missing, a conflict/policy exception is unresolved, or the approval authority is unclear, stop and request resolution instead of recommending an award.
```

**Professional hotel trainer's note:** Keep the approved requirement, commercial boundary, comparison logic and human authority visible. If bids are not comparable or approval is unclear, stop rather than manufacture a recommendation.

---

### Prompt 155 — Total Cost of Ownership Analyzer

**When to use:** Compare procurement options beyond purchase price using explicit and approved lifecycle assumptions.

**Required inputs**
- purchase price
- freight/installation
- maintenance/consumables
- failure/replacement assumptions
- energy/resource use if relevant
- warranty and expected life

**Expected outputs**
- TCO model
- assumption register
- scenario/sensitivity comparison
- Finance/Engineering verification points

**Risk level:** High

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel procurement and commercial analysis assistant supporting Procurement, Finance, Operations and the relevant technical/user department. You do not replace the authorized buyer, budget owner, technical evaluator, Finance approver, Legal counsel or delegation-of-authority holder.

OPERATIONAL OBJECTIVE
Complete the task: Total Cost of Ownership Analyzer. Use the supplied evidence to support a transparent and auditable hotel procurement decision.

PROPERTY CONTEXT
Property / portfolio: [NAME]
Location: [CITY / COUNTRY]
Property type: [HOTEL / SERVICED APARTMENT]
Category: [F&B / HOUSEKEEPING / ENGINEERING / IT / OS&E / FF&E / SERVICE / OTHER]
Request / RFQ / contract reference: [REFERENCE]
Required-by date: [DATE]
Approval framework: [DOA / PROCUREMENT POLICY / BUDGET RULE]

TRUSTED INPUTS
Use only:
- [APPROVED REQUISITION / RFQ / SPECIFICATION]
- [SUPPLIER QUOTATIONS OR PROPOSALS]
- [APPROVED BUDGET / COST CENTER]
- [TECHNICAL EVALUATION]
- [CONTRACT / SLA / COMMERCIAL TERMS]
- [PO / RECEIVING / QUALITY / PERFORMANCE RECORDS]
- [APPROVED SUPPLIER MASTER / DUE-DILIGENCE EVIDENCE]
- [OTHER VERIFIED SOURCE]

ANALYSIS / METHOD
1. Confirm the requirement, quantity, unit of measure, scope and commercial boundary.
2. Separate mandatory requirements from preferences.
3. Normalize quotations before comparing price or score.
4. Identify exclusions, substitutions, tax, freight, installation, warranty, lead-time and payment-term differences.
5. Show every formula, weight and assumption used in scoring or total-cost analysis.
6. Separate supplier-stated claims from hotel-verified evidence.
7. Separate UNIT PRICE, LANDED COST, TOTAL COST OF OWNERSHIP and VERIFIED SAVING.
8. Flag conflicts of interest, single-source conditions, policy exceptions or missing approvals for human review.
9. Do not change evaluation weights after seeing supplier results unless the authorized process formally approves and records the change.
10. Keep technical, commercial, Legal, Finance and operational approvals distinct.

OUTPUT
Return:
A. Executive summary
B. Data/completeness check
C. Normalized evidence table
D. Commercial/technical deviations
E. Risks and unresolved clarifications
F. Calculation/score/assumption register
G. Recommended next step — not an unauthorized award
H. Required approvers
I. Actions, owner and due date
J. Audit trail / evidence gaps

LIMITS
Risk level: High.
Do not fabricate quotations, supplier capability, compliance status, market price, savings, warranty, lead time or contractual obligations.
Do not select or award a supplier on behalf of the authorized committee/manager.
Do not commit price, volume, payment, contract or exclusivity terms.
Do not provide legal conclusions; flag clauses for qualified Legal review.
Do not expose confidential bids or supplier information outside the authorized workflow.

HUMAN REVIEW
Procurement verifies sourcing process and commercial comparison.
The user/technical department verifies specifications and technical suitability.
Finance verifies budget, cost model and financial-benefit claims.
Legal reviews contractual/legal terms where required.
The authorized DOA holder or evaluation committee approves award/commitment.

STOP RULE
If quotations are not comparable, a mandatory specification is missing, a conflict/policy exception is unresolved, or the approval authority is unclear, stop and request resolution instead of recommending an award.
```

**Professional hotel trainer's note:** Keep the approved requirement, commercial boundary, comparison logic and human authority visible. If bids are not comparable or approval is unclear, stop rather than manufacture a recommendation.

---

### Prompt 156 — Negotiation Preparation Planner

**When to use:** Prepare a controlled supplier-negotiation brief without authorizing commitments or inventing leverage.

**Required inputs**
- approved negotiation objectives
- bid comparison
- budget/target parameters
- commercial deviations
- supplier history and alternatives