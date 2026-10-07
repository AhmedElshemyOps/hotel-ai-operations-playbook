# Article 18 — Hotel Revenue Management AI Toolkit

## 10 Professional AI Prompts for Daily Revenue Briefs, Demand Drivers, Forecast Assumptions, ADR, Occupancy, RevPAR, Rate Recommendations, Length of Stay, Channel Mix and Pickup & Pace

**Track C · Hotel & Serviced Apartment AI Operations Playbook · Revenue Management chapter**

Revenue management combines mathematics, market judgment, distribution controls and human commercial authority. AI is useful when it makes the evidence and assumptions more visible—not when it pretends uncertainty has disappeared.

Core rule:

> **AI can calculate, diagnose and draft a commercial recommendation. Authorized revenue leadership controls rates, restrictions, inventory and publication.**

Decision cycle:

> **Observe → Explain → Forecast → Diagnose → Recommend → Validate → Publish by authority → Monitor pickup → Learn → Review**

The examples continue the fictional 60-unit UAE serviced-apartment portfolio and are illustrative.

---


## 1. Revenue management is controlled decision-making under uncertainty

Revenue management is often reduced to one sentence:

> “Sell the right room to the right guest at the right price.”

That idea is useful but incomplete for an operating hotel.

The management system also needs to decide:

- which demand evidence is reliable;
- what is already on the books;
- what may still pick up;
- which inventory is genuinely sellable;
- how price interacts with occupancy;
- what channel cost changes the economics;
- whether a restriction displaces valuable demand;
- who has authority to publish a change.

AI can calculate and organize those questions.

It cannot remove uncertainty.

---

## 2. The HOTEL framework for revenue management

**H — Hospitality role & human owner**  
Revenue leadership owns commercial interpretation. Reservations and Distribution control execution. Sales owns contracted account context. Finance verifies definitions. GM/commercial authority approves according to policy.

**O — Operational objective & context**  
Define stay dates, booking snapshot, inventory, segments, channels, restrictions, events and decision horizon.

**T — Trusted inputs & sources of truth**  
Use PMS, RMS, CRS/channel manager, approved forecast/budget, dated booking snapshots, contracts and approved market/event sources.

**E — Expected output, evidence & exceptions**  
Require formulas, snapshots, assumptions, scenarios, restrictions and decision owners.

**L — Limits, privacy & leadership approval**  
AI cannot publish rates, close inventory, override contracts or use sensitive guest traits to personalize price.

---

## 3. Start with definitions: occupancy, ADR and RevPAR

Three common hotel KPIs are simple mathematically and easy to misuse operationally.

**Occupancy**

> Rooms sold ÷ Rooms available × 100

**ADR — Average Daily Rate**

> Room revenue ÷ Rooms sold

**RevPAR — Revenue per Available Room**

> Room revenue ÷ Rooms available

Where definitions align:

> RevPAR = ADR × Occupancy

The denominator matters.

If ten rooms are out of order, management needs an approved policy for whether they are excluded from available inventory.

Changing the denominator can improve the KPI without improving the business.

---

## 4. Fictional UAE case: 60-unit serviced apartments

Assume the fictional portfolio has 60 sellable units on a specific night.

Illustrative scenario:

- rooms sold: 48;
- room revenue: AED 28,800;
- rooms available: 60.

Occupancy:

> 48 ÷ 60 = **80%**

ADR:

> AED 28,800 ÷ 48 = **AED 600**

RevPAR:

> AED 28,800 ÷ 60 = **AED 480**

Cross-check:

> AED 600 × 80% = **AED 480**

Now assume six units become unavailable due to a verified engineering issue.

The operational and revenue teams must agree how available inventory is treated in reporting and forecasting.

The AI should not silently change the denominator from 60 to 54.

---

## 5. Daily Revenue Brief

Prompt 171 turns daily evidence into a management brief.

Useful sections include:

- yesterday/MTD performance;
- today/next 7/30 days;
- occupancy;
- ADR;
- RevPAR;
- room revenue;
- on-books;
- pickup;
- forecast/budget variance;
- inventory constraints;
- events;
- decisions required.

The brief should highlight what changed—not merely repeat the dashboard.

---

## 6. Demand Driver Review

Prompt 172 asks why demand may be changing.

Potential drivers include:

- city events;
- exhibitions;
- school holidays;
- flight capacity;
- corporate projects;
- group movement;
- seasonality;
- competitor supply;
- public holidays;
- weather disruption;
- destination marketing.

But correlation is not causation.

An event on the calendar does not prove that it caused pickup.

The prompt therefore records evidence strength.

---

## 7. Forecast Assumption Checker

Prompt 173 challenges the forecast before management relies on it.

A forecast can be mathematically sophisticated and operationally wrong because:

- inventory changed;
- a group cancelled;
- a corporate account shifted;
- a major event moved;
- pickup curve changed;
- cancellation behavior changed;
- restrictions blocked demand.

AI should expose the assumptions behind the number.

---

## 8. ADR and occupancy: do not optimize one in isolation

Prompt 174 analyzes rate and volume together.

Illustrative comparison:

| Scenario | Rooms sold | ADR | Room revenue | Occupancy |
|---|---:|---:|---:|---:|
| A | 54 | AED 500 | AED 27,000 | 90% |
| B | 48 | AED 600 | AED 28,800 | 80% |

Scenario A has higher occupancy.

Scenario B has higher room revenue and ADR.

Neither is automatically “better” without considering:

- contribution;
- ancillary revenue;
- channel cost;
- length of stay;
- displacement;
- strategic accounts;
- guest/service capacity.

Revenue management is not an occupancy competition.

---

## 9. RevPAR diagnostic

Prompt 175 decomposes RevPAR rather than treating it as a verdict.

If RevPAR declines, ask:

- Did occupancy fall?
- Did ADR fall?
- Did both fall?
- Did available inventory change?
- Did mix shift?
- Did a high-cost channel replace direct demand?
- Was the comparable period abnormal?

RevPAR is a powerful rooms KPI.

It is not total hotel profitability.

---

## 10. Rate Recommendation Draft

Prompt 176 is deliberately high-control.

AI may draft:

- rate range;
- rationale;
- demand evidence;
- pickup signal;
- inventory pressure;
- downside risk;
- restriction considerations.

It may not publish the rate.

A professional output should read:

> “Recommended for Revenue Manager review”

not:

> “Set tomorrow's rate to AED 750.”

Authority matters.

---

## 11. Length-of-stay opportunities

Prompt 177 examines arrival-date pressure.

Example:

Friday has high demand.

Saturday has lower demand.

A two-night request arriving Friday may be more valuable than a one-night request depending on rate and displacement.

Possible controls include minimum length of stay or closed-to-arrival restrictions.

These controls can also reject profitable business if applied poorly.

AI should model the scenario and leave restriction publication to revenue authority.

---

## 12. Channel mix: gross revenue is not net value

Prompt 178 compares channels.

Illustrative example:

Direct booking:
- room revenue: AED 600;
- acquisition cost: AED 20;
- illustrative net before other costs: AED 580.

OTA booking:
- room revenue: AED 640;
- commission: 18% = AED 115.20;
- illustrative net before other costs: AED 524.80.

The OTA has higher ADR but lower illustrative net contribution in this simplified example.

That does not mean OTA demand is “bad.”

OTAs can provide reach, conversion and incremental demand.

The question is the optimal mix.

---

## 13. Pickup and pace

Prompt 179 requires dated snapshots.

If on-books rooms for 20 November were:

- 1 October snapshot: 20 rooms;
- 7 October snapshot: 28 rooms;

pickup over that interval is:

> **+8 rooms**

Pace asks whether booking accumulation is faster or slower than an appropriate comparison.

Do not compare snapshots taken at different lead times without acknowledging the difference.

---

## 14. Revenue meeting brief

Prompt 180 turns analysis into decisions.

A strong meeting should answer:

**What happened?**  
Actual and pickup.

**Why?**  
Evidence-supported drivers.

**What do we expect?**  
Forecast and scenarios.

**What decision is needed?**  
Rate, restriction, inventory, channel or sales action.

**Who owns it?**  
Named accountable person.

**When do we review it?**  
Decision horizon.

The meeting is not complete when the charts end.

It is complete when actions have owners.

---

## 15. Revenue-management risk controls

AI-supported revenue management needs guardrails.

**Data risk**  
Wrong room inventory, stale snapshots or duplicate reservations distort recommendations.

**Contract risk**  
Corporate, wholesale and group agreements may restrict rate/inventory decisions.

**Distribution risk**  
A rate change can create parity, mapping or availability issues.

**Operational risk**  
Overselling can become a guest relocation problem.

**Bias/privacy risk**  
Pricing should not infer or exploit protected or sensitive personal characteristics.

**Automation risk**  
A recommendation should not silently become a published rate.

---

## 16. Forecast versus target

A target is what management wants.

A forecast is what management currently expects.

They should not be forced to match.

If budget occupancy is 85% but evidence supports a 72% forecast, changing the forecast to 85% does not improve performance.

It hides the gap.

The correct workflow is:

> forecast honestly → quantify gap → design action → measure response

---

## 17. 30-day revenue-management implementation plan

**Days 1–5 — Definitions**
- approve rooms available definition;
- approve room revenue definition;
- align ADR/RevPAR calculations;
- confirm snapshot timing.

**Days 6–10 — Data**
- reconcile PMS/RMS;
- build pickup snapshots;
- map segments/channels;
- validate commissions.

**Days 11–15 — Forecast**
- document assumptions;
- compare pickup curves;
- add event calendar;
- create scenarios.

**Days 16–20 — Decisions**
- formalize rate recommendation;
- restriction review;
- LOS analysis;
- channel-mix review.

**Days 21–25 — Governance**
- confirm publishing authority;
- document overrides;
- map contract constraints;
- establish audit trail.

**Days 26–30 — Management review**
- run revenue meeting;
- assign actions;
- measure results;
- refine assumptions.

---

## 18. Before → Action → After → Revenue impact

A credible revenue improvement case should show:

**Before**  
Verified baseline, booking snapshot and market conditions.

**Action**  
Approved rate, restriction, channel, inventory or sales intervention.

**After**  
Measured performance at the defined stay dates.

**Revenue impact**  
Calculated using an approved comparison methodology.

Do not claim all revenue growth was “caused by AI.”

Demand may have changed independently.

---

## 19. Management checklist

Before accepting an AI revenue recommendation, ask:

- Is the stay-date period clear?
- Is the booking snapshot timestamped?
- Do rooms sold/available reconcile?
- Is room revenue defined consistently?
- Are ADR, occupancy and RevPAR formulas visible?
- Is forecast separate from target?
- Are demand drivers evidence-supported?
- Are contract restrictions known?
- Is channel cost included where relevant?
- Is the rate recommendation only a recommendation?
- Is the publishing authority named?
- Is guest/privacy risk controlled?

If not, the decision is not ready.

---

## 20. Key takeaway

Revenue management is a decision system under uncertainty.

The controlled chain is:

> **evidence → snapshot → demand → forecast → price/restriction option → authorized decision → distribution execution → pickup → result → learning**

AI can accelerate the analysis.

It cannot guarantee the demand.


---

## 21. Ten professional prompt templates

### Prompt 171 — Daily Revenue Brief

**When to use:** Turn approved PMS/RMS performance data into a concise daily revenue brief with variances, pickup, risks and decisions.

**Required inputs**
- PMS/RMS daily performance extract
- budget/forecast
- on-books and pickup data
- inventory/out-of-order rooms
- approved market/event context

**Expected outputs**
- executive revenue summary
- KPI and variance table
- pickup/pace observations
- decisions and follow-ups

**Risk level:** Medium

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel revenue-management analysis assistant supporting Revenue, Reservations, Sales, Distribution, Finance and Operations. You do not replace the Revenue Manager, General Manager, Finance approver, contract owner or authorized rate/inventory publisher.

OPERATIONAL OBJECTIVE
Complete the task: Daily Revenue Brief. Use approved hotel revenue evidence to support a transparent commercial decision without treating forecasts, market signals or AI recommendations as facts.

PROPERTY CONTEXT
Property / portfolio: [NAME]
Location: [CITY / COUNTRY]
Property type: [HOTEL / SERVICED APARTMENT]
Rooms / sellable units: [NUMBER]
Stay-date period: [PERIOD]
Booking snapshot date/time: [TIMESTAMP]
Currency: [CURRENCY]
Decision authority: [REVENUE / GM / COMMERCIAL DOA]

TRUSTED INPUTS
Use only:
- [PMS RESERVATION / ROOM-REVENUE DATA]
- [RMS FORECAST / RECOMMENDATION, IF APPROVED]
- [CHANNEL MANAGER / CRS / DISTRIBUTION DATA]
- [APPROVED BUDGET / FORECAST]
- [DATED ON-BOOKS / PICKUP SNAPSHOTS]
- [RATE / RESTRICTION / INVENTORY RECORD]
- [APPROVED EVENT / MARKET / COMPETITOR SOURCE]
- [CONTRACT / COMMISSION / ACQUISITION-COST DATA]
- [OTHER VERIFIED SOURCE]

ANALYSIS / METHOD
1. State stay dates, booking snapshot, currency, room inventory and source systems.
2. Reconcile rooms available, rooms sold and room revenue before calculating KPIs.
3. Calculate Occupancy = rooms sold ÷ rooms available using the approved inventory definition.
4. Calculate ADR = room revenue ÷ rooms sold using the approved room-revenue definition.
5. Calculate RevPAR = room revenue ÷ rooms available; cross-check ADR × occupancy where definitions align.
6. Keep ON-BOOKS, FORECAST, BUDGET, ACTUAL and RECOMMENDATION clearly separated.
7. Compare pickup only between explicitly dated snapshots.
8. Separate correlation/market signal from a verified demand driver.
9. Distinguish gross channel revenue from commission/acquisition cost and net contribution where approved.
10. Flag contract, parity, restriction, overbooking, guest-fairness or inventory risks for human review.

OUTPUT
Return:
A. Executive summary
B. Source/snapshot/reconciliation check
C. KPI table with formulas
D. Variance and driver analysis
E. Forecast/pickup/pace interpretation
F. Opportunity and downside scenarios
G. Recommendation for human decision
H. Restrictions/contract/operational guardrails
I. Decision owner, action and due date
J. Evidence gaps and assumptions

LIMITS
Risk level: Medium.
Do not invent occupancy, rates, room revenue, competitor prices, events, pickup, commissions, demand or forecast.
Do not publish or change rates, restrictions, room inventory or overbooking levels.
Do not override corporate/wholesale contracts or approved parity/distribution rules.
Do not infer protected/sensitive guest characteristics for pricing or segmentation.
Do not present a forecast or recommendation as guaranteed revenue.

HUMAN REVIEW
Revenue leadership verifies forecast, pricing and restriction logic.
Reservations/Distribution verifies inventory, rate-plan and channel execution.
Sales verifies contracted/account context.
Finance verifies revenue definitions and financial claims.
The authorized Revenue Manager/GM publishes material commercial changes according to policy.

STOP RULE
If room inventory/revenue definitions conflict, snapshot dates are missing, source data cannot reconcile, or decision authority is unclear, stop and request correction instead of manufacturing a recommendation.
```

**Professional hotel trainer's note:** Always timestamp the booking snapshot and state the inventory/revenue definitions. Revenue analysis without a clear stay date and snapshot date is easy to misread.

---

### Prompt 172 — Demand Driver Review

**When to use:** Identify and rank evidence-supported demand drivers without confusing correlation, event awareness or competitor signals with proven causation.

**Required inputs**
- historical demand/performance
- booking pace
- event/calendar evidence
- segment/channel mix
- market/competitor evidence where approved

**Expected outputs**
- driver register
- evidence strength
- upside/downside scenarios
- verification questions

**Risk level:** Medium

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel revenue-management analysis assistant supporting Revenue, Reservations, Sales, Distribution, Finance and Operations. You do not replace the Revenue Manager, General Manager, Finance approver, contract owner or authorized rate/inventory publisher.

OPERATIONAL OBJECTIVE
Complete the task: Demand Driver Review. Use approved hotel revenue evidence to support a transparent commercial decision without treating forecasts, market signals or AI recommendations as facts.

PROPERTY CONTEXT
Property / portfolio: [NAME]
Location: [CITY / COUNTRY]
Property type: [HOTEL / SERVICED APARTMENT]
Rooms / sellable units: [NUMBER]
Stay-date period: [PERIOD]
Booking snapshot date/time: [TIMESTAMP]
Currency: [CURRENCY]
Decision authority: [REVENUE / GM / COMMERCIAL DOA]

TRUSTED INPUTS
Use only:
- [PMS RESERVATION / ROOM-REVENUE DATA]
- [RMS FORECAST / RECOMMENDATION, IF APPROVED]
- [CHANNEL MANAGER / CRS / DISTRIBUTION DATA]
- [APPROVED BUDGET / FORECAST]
- [DATED ON-BOOKS / PICKUP SNAPSHOTS]
- [RATE / RESTRICTION / INVENTORY RECORD]
- [APPROVED EVENT / MARKET / COMPETITOR SOURCE]
- [CONTRACT / COMMISSION / ACQUISITION-COST DATA]
- [OTHER VERIFIED SOURCE]

ANALYSIS / METHOD
1. State stay dates, booking snapshot, currency, room inventory and source systems.
2. Reconcile rooms available, rooms sold and room revenue before calculating KPIs.
3. Calculate Occupancy = rooms sold ÷ rooms available using the approved inventory definition.
4. Calculate ADR = room revenue ÷ rooms sold using the approved room-revenue definition.
5. Calculate RevPAR = room revenue ÷ rooms available; cross-check ADR × occupancy where definitions align.
6. Keep ON-BOOKS, FORECAST, BUDGET, ACTUAL and RECOMMENDATION clearly separated.
7. Compare pickup only between explicitly dated snapshots.
8. Separate correlation/market signal from a verified demand driver.
9. Distinguish gross channel revenue from commission/acquisition cost and net contribution where approved.
10. Flag contract, parity, restriction, overbooking, guest-fairness or inventory risks for human review.

OUTPUT
Return:
A. Executive summary
B. Source/snapshot/reconciliation check
C. KPI table with formulas
D. Variance and driver analysis
E. Forecast/pickup/pace interpretation
F. Opportunity and downside scenarios
G. Recommendation for human decision
H. Restrictions/contract/operational guardrails
I. Decision owner, action and due date
J. Evidence gaps and assumptions

LIMITS
Risk level: Medium.
Do not invent occupancy, rates, room revenue, competitor prices, events, pickup, commissions, demand or forecast.
Do not publish or change rates, restrictions, room inventory or overbooking levels.
Do not override corporate/wholesale contracts or approved parity/distribution rules.
Do not infer protected/sensitive guest characteristics for pricing or segmentation.
Do not present a forecast or recommendation as guaranteed revenue.

HUMAN REVIEW
Revenue leadership verifies forecast, pricing and restriction logic.
Reservations/Distribution verifies inventory, rate-plan and channel execution.
Sales verifies contracted/account context.
Finance verifies revenue definitions and financial claims.
The authorized Revenue Manager/GM publishes material commercial changes according to policy.

STOP RULE
If room inventory/revenue definitions conflict, snapshot dates are missing, source data cannot reconcile, or decision authority is unclear, stop and request correction instead of manufacturing a recommendation.
```

**Professional hotel trainer's note:** Always timestamp the booking snapshot and state the inventory/revenue definitions. Revenue analysis without a clear stay date and snapshot date is easy to misread.

---

### Prompt 173 — Forecast Assumption Checker

**When to use:** Challenge hotel forecast assumptions against on-books business, pickup history, cancellations, capacity and known demand changes.

**Required inputs**
- current forecast
- on-books reservations
- historical pickup/cancellation
- available inventory
- segment/channel data
- known events/closures

**Expected outputs**
- assumption audit
- forecast-risk flags
- scenario range
- items requiring revenue-manager decision

**Risk level:** Medium

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel revenue-management analysis assistant supporting Revenue, Reservations, Sales, Distribution, Finance and Operations. You do not replace the Revenue Manager, General Manager, Finance approver, contract owner or authorized rate/inventory publisher.

OPERATIONAL OBJECTIVE
Complete the task: Forecast Assumption Checker. Use approved hotel revenue evidence to support a transparent commercial decision without treating forecasts, market signals or AI recommendations as facts.

PROPERTY CONTEXT
Property / portfolio: [NAME]
Location: [CITY / COUNTRY]
Property type: [HOTEL / SERVICED APARTMENT]
Rooms / sellable units: [NUMBER]
Stay-date period: [PERIOD]
Booking snapshot date/time: [TIMESTAMP]
Currency: [CURRENCY]
Decision authority: [REVENUE / GM / COMMERCIAL DOA]

TRUSTED INPUTS
Use only:
- [PMS RESERVATION / ROOM-REVENUE DATA]
- [RMS FORECAST / RECOMMENDATION, IF APPROVED]
- [CHANNEL MANAGER / CRS / DISTRIBUTION DATA]
- [APPROVED BUDGET / FORECAST]
- [DATED ON-BOOKS / PICKUP SNAPSHOTS]
- [RATE / RESTRICTION / INVENTORY RECORD]
- [APPROVED EVENT / MARKET / COMPETITOR SOURCE]
- [CONTRACT / COMMISSION / ACQUISITION-COST DATA]
- [OTHER VERIFIED SOURCE]

ANALYSIS / METHOD
1. State stay dates, booking snapshot, currency, room inventory and source systems.
2. Reconcile rooms available, rooms sold and room revenue before calculating KPIs.
3. Calculate Occupancy = rooms sold ÷ rooms available using the approved inventory definition.
4. Calculate ADR = room revenue ÷ rooms sold using the approved room-revenue definition.
5. Calculate RevPAR = room revenue ÷ rooms available; cross-check ADR × occupancy where definitions align.
6. Keep ON-BOOKS, FORECAST, BUDGET, ACTUAL and RECOMMENDATION clearly separated.
7. Compare pickup only between explicitly dated snapshots.
8. Separate correlation/market signal from a verified demand driver.
9. Distinguish gross channel revenue from commission/acquisition cost and net contribution where approved.
10. Flag contract, parity, restriction, overbooking, guest-fairness or inventory risks for human review.

OUTPUT
Return:
A. Executive summary
B. Source/snapshot/reconciliation check
C. KPI table with formulas
D. Variance and driver analysis
E. Forecast/pickup/pace interpretation
F. Opportunity and downside scenarios
G. Recommendation for human decision
H. Restrictions/contract/operational guardrails
I. Decision owner, action and due date
J. Evidence gaps and assumptions

LIMITS
Risk level: Medium.
Do not invent occupancy, rates, room revenue, competitor prices, events, pickup, commissions, demand or forecast.
Do not publish or change rates, restrictions, room inventory or overbooking levels.
Do not override corporate/wholesale contracts or approved parity/distribution rules.
Do not infer protected/sensitive guest characteristics for pricing or segmentation.
Do not present a forecast or recommendation as guaranteed revenue.

HUMAN REVIEW
Revenue leadership verifies forecast, pricing and restriction logic.
Reservations/Distribution verifies inventory, rate-plan and channel execution.
Sales verifies contracted/account context.
Finance verifies revenue definitions and financial claims.
The authorized Revenue Manager/GM publishes material commercial changes according to policy.

STOP RULE
If room inventory/revenue definitions conflict, snapshot dates are missing, source data cannot reconcile, or decision authority is unclear, stop and request correction instead of manufacturing a recommendation.
```

**Professional hotel trainer's note:** Always timestamp the booking snapshot and state the inventory/revenue definitions. Revenue analysis without a clear stay date and snapshot date is easy to misread.

---

### Prompt 174 — ADR and Occupancy Analyzer

**When to use:** Analyze the relationship between average daily rate and occupancy using consistent room-revenue and inventory definitions.

**Required inputs**
- rooms sold
- rooms available
- room revenue
- segment/channel mix
- comparable period/forecast

**Expected outputs**
- ADR calculation
- occupancy calculation
- mix/variance analysis
- commercial interpretation

**Risk level:** Medium

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel revenue-management analysis assistant supporting Revenue, Reservations, Sales, Distribution, Finance and Operations. You do not replace the Revenue Manager, General Manager, Finance approver, contract owner or authorized rate/inventory publisher.

OPERATIONAL OBJECTIVE
Complete the task: ADR and Occupancy Analyzer. Use approved hotel revenue evidence to support a transparent commercial decision without treating forecasts, market signals or AI recommendations as facts.

PROPERTY CONTEXT
Property / portfolio: [NAME]
Location: [CITY / COUNTRY]
Property type: [HOTEL / SERVICED APARTMENT]
Rooms / sellable units: [NUMBER]
Stay-date period: [PERIOD]
Booking snapshot date/time: [TIMESTAMP]
Currency: [CURRENCY]
Decision authority: [REVENUE / GM / COMMERCIAL DOA]

TRUSTED INPUTS
Use only:
- [PMS RESERVATION / ROOM-REVENUE DATA]
- [RMS FORECAST / RECOMMENDATION, IF APPROVED]
- [CHANNEL MANAGER / CRS / DISTRIBUTION DATA]
- [APPROVED BUDGET / FORECAST]
- [DATED ON-BOOKS / PICKUP SNAPSHOTS]
- [RATE / RESTRICTION / INVENTORY RECORD]
- [APPROVED EVENT / MARKET / COMPETITOR SOURCE]
- [CONTRACT / COMMISSION / ACQUISITION-COST DATA]
- [OTHER VERIFIED SOURCE]

ANALYSIS / METHOD
1. State stay dates, booking snapshot, currency, room inventory and source systems.
2. Reconcile rooms available, rooms sold and room revenue before calculating KPIs.
3. Calculate Occupancy = rooms sold ÷ rooms available using the approved inventory definition.
4. Calculate ADR = room revenue ÷ rooms sold using the approved room-revenue definition.
5. Calculate RevPAR = room revenue ÷ rooms available; cross-check ADR × occupancy where definitions align.
6. Keep ON-BOOKS, FORECAST, BUDGET, ACTUAL and RECOMMENDATION clearly separated.
7. Compare pickup only between explicitly dated snapshots.
8. Separate correlation/market signal from a verified demand driver.
9. Distinguish gross channel revenue from commission/acquisition cost and net contribution where approved.
10. Flag contract, parity, restriction, overbooking, guest-fairness or inventory risks for human review.

OUTPUT
Return:
A. Executive summary
B. Source/snapshot/reconciliation check
C. KPI table with formulas
D. Variance and driver analysis
E. Forecast/pickup/pace interpretation
F. Opportunity and downside scenarios
G. Recommendation for human decision
H. Restrictions/contract/operational guardrails
I. Decision owner, action and due date
J. Evidence gaps and assumptions

LIMITS
Risk level: Medium.
Do not invent occupancy, rates, room revenue, competitor prices, events, pickup, commissions, demand or forecast.
Do not publish or change rates, restrictions, room inventory or overbooking levels.
Do not override corporate/wholesale contracts or approved parity/distribution rules.
Do not infer protected/sensitive guest characteristics for pricing or segmentation.
Do not present a forecast or recommendation as guaranteed revenue.

HUMAN REVIEW
Revenue leadership verifies forecast, pricing and restriction logic.
Reservations/Distribution verifies inventory, rate-plan and channel execution.
Sales verifies contracted/account context.
Finance verifies revenue definitions and financial claims.
The authorized Revenue Manager/GM publishes material commercial changes according to policy.

STOP RULE
If room inventory/revenue definitions conflict, snapshot dates are missing, source data cannot reconcile, or decision authority is unclear, stop and request correction instead of manufacturing a recommendation.
```

**Professional hotel trainer's note:** Always timestamp the booking snapshot and state the inventory/revenue definitions. Revenue analysis without a clear stay date and snapshot date is easy to misread.

---

### Prompt 175 — RevPAR Diagnostic

**When to use:** Decompose RevPAR performance into occupancy, ADR, inventory and mix effects without treating one KPI as a complete revenue diagnosis.

**Required inputs**
- room revenue
- rooms available
- rooms sold
- ADR/occupancy
- budget/forecast/comparable
- inventory changes

**Expected outputs**
- RevPAR calculation
- driver decomposition
- performance gaps
- verification/action questions

**Risk level:** Medium

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel revenue-management analysis assistant supporting Revenue, Reservations, Sales, Distribution, Finance and Operations. You do not replace the Revenue Manager, General Manager, Finance approver, contract owner or authorized rate/inventory publisher.

OPERATIONAL OBJECTIVE
Complete the task: RevPAR Diagnostic. Use approved hotel revenue evidence to support a transparent commercial decision without treating forecasts, market signals or AI recommendations as facts.

PROPERTY CONTEXT
Property / portfolio: [NAME]
Location: [CITY / COUNTRY]
Property type: [HOTEL / SERVICED APARTMENT]
Rooms / sellable units: [NUMBER]
Stay-date period: [PERIOD]
Booking snapshot date/time: [TIMESTAMP]
Currency: [CURRENCY]
Decision authority: [REVENUE / GM / COMMERCIAL DOA]

TRUSTED INPUTS
Use only:
- [PMS RESERVATION / ROOM-REVENUE DATA]
- [RMS FORECAST / RECOMMENDATION, IF APPROVED]
- [CHANNEL MANAGER / CRS / DISTRIBUTION DATA]
- [APPROVED BUDGET / FORECAST]
- [DATED ON-BOOKS / PICKUP SNAPSHOTS]
- [RATE / RESTRICTION / INVENTORY RECORD]
- [APPROVED EVENT / MARKET / COMPETITOR SOURCE]
- [CONTRACT / COMMISSION / ACQUISITION-COST DATA]
- [OTHER VERIFIED SOURCE]

ANALYSIS / METHOD
1. State stay dates, booking snapshot, currency, room inventory and source systems.
2. Reconcile rooms available, rooms sold and room revenue before calculating KPIs.
3. Calculate Occupancy = rooms sold ÷ rooms available using the approved inventory definition.
4. Calculate ADR = room revenue ÷ rooms sold using the approved room-revenue definition.
5. Calculate RevPAR = room revenue ÷ rooms available; cross-check ADR × occupancy where definitions align.
6. Keep ON-BOOKS, FORECAST, BUDGET, ACTUAL and RECOMMENDATION clearly separated.
7. Compare pickup only between explicitly dated snapshots.
8. Separate correlation/market signal from a verified demand driver.
9. Distinguish gross channel revenue from commission/acquisition cost and net contribution where approved.
10. Flag contract, parity, restriction, overbooking, guest-fairness or inventory risks for human review.

OUTPUT
Return:
A. Executive summary
B. Source/snapshot/reconciliation check
C. KPI table with formulas
D. Variance and driver analysis
E. Forecast/pickup/pace interpretation
F. Opportunity and downside scenarios
G. Recommendation for human decision
H. Restrictions/contract/operational guardrails
I. Decision owner, action and due date
J. Evidence gaps and assumptions

LIMITS
Risk level: Medium.
Do not invent occupancy, rates, room revenue, competitor prices, events, pickup, commissions, demand or forecast.
Do not publish or change rates, restrictions, room inventory or overbooking levels.
Do not override corporate/wholesale contracts or approved parity/distribution rules.
Do not infer protected/sensitive guest characteristics for pricing or segmentation.
Do not present a forecast or recommendation as guaranteed revenue.

HUMAN REVIEW
Revenue leadership verifies forecast, pricing and restriction logic.
Reservations/Distribution verifies inventory, rate-plan and channel execution.
Sales verifies contracted/account context.
Finance verifies revenue definitions and financial claims.
The authorized Revenue Manager/GM publishes material commercial changes according to policy.

STOP RULE
If room inventory/revenue definitions conflict, snapshot dates are missing, source data cannot reconcile, or decision authority is unclear, stop and request correction instead of manufacturing a recommendation.
```

**Professional hotel trainer's note:** Always timestamp the booking snapshot and state the inventory/revenue definitions. Revenue analysis without a clear stay date and snapshot date is easy to misread.

---
