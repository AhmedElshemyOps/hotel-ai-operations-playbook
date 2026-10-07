# Article 17 — Hotel Inventory & PAR Management AI Toolkit

## 10 Professional AI Prompts for PAR Levels, Reorder Points, Slow Stock, Stockouts, Linen, Amenities, Critical Spares, Variance, Expiry and Inventory KPIs

**Track C · Hotel & Serviced Apartment AI Operations Playbook · Inventory & PAR chapter**

Inventory is one of the clearest examples of why operational AI needs both mathematics and governance. A formula can recommend a number; only a controlled operating process can make that number reliable.

Core rule:

> **PAR is an operating target. Reorder point is a replenishment trigger. Safety stock protects against defined uncertainty. None should be invented by AI.**

Control cycle:

> **Classify → Set PAR → Forecast usage → Set reorder point → Receive/issue → Count → Investigate variance → Manage aging/expiry → Protect critical stock → Review**

The examples continue the fictional 60-unit UAE serviced-apartment portfolio and are illustrative.

---


## 1. Inventory is a service-control system, not a storeroom number

A hotel can have too much inventory and still suffer stockouts.

It can also reduce stock value and create a service failure.

The objective is therefore not simply “hold less stock.”

It is:

> **Hold the right verified quantity, in the right location, at the right time, with the right replenishment trigger and the right control evidence.**

Inventory connects guest readiness, housekeeping, engineering reliability, procurement, cash flow and operational resilience.

---

## 2. The HOTEL framework for inventory

**H — Hospitality role & human owner**  
Stores controls custody and transactions. Department owners define operational need. Procurement controls replenishment sourcing. Engineering verifies critical spares. Finance controls valuation/write-off. Management approves material policy changes.

**O — Operational objective & context**  
Define category, SKU, UOM, location, demand driver, service requirement, lead time, pack size, expiry and criticality.

**T — Trusted inputs & sources of truth**  
Use the approved item master, inventory ledger, physical counts, receipts, issues, transfers, purchase orders, PMS/operational data and verified supplier lead times.

**E — Expected output, evidence & exceptions**  
Require formulas, reconciliation, demand assumptions, stock-risk exceptions and approval requirements.

**L — Limits, privacy & leadership approval**  
AI cannot invent stock, adjust the ledger, write off inventory, accuse staff or place purchase orders.

---

## 3. PAR, reorder point and safety stock are different controls

Hotels often use “PAR” as if it means every inventory threshold.

That creates confusion.

**PAR level** is an approved operating stock target designed to support the service cycle.

**Reorder point** is the inventory position at which replenishment should be triggered.

A simple conceptual model is:

> Reorder point = expected demand during lead time + approved safety stock

**Safety stock** protects against defined uncertainty such as demand or lead-time variability.

**Minimum order quantity** is a supplier/commercial constraint.

**Current stock** is simply what the records or physical count say exists now.

AI should not merge these concepts.

---

## 4. Fictional UAE case: guest amenities

Assume the fictional 60-unit serviced-apartment portfolio issues an average of **0.70 amenity sets per occupied room night**.

For an illustrative planning week:

- forecast occupied room nights: 300;
- expected consumption: 300 × 0.70 = **210 sets**;
- verified replenishment lead-time demand: 150 sets;
- approved safety stock: 60 sets.

Illustrative reorder point:

> **150 + 60 = 210 sets**

If the current inventory position is 195 sets, the trigger has been crossed.

That does not automatically mean “order 210.”

The order quantity still depends on:

- open purchase orders;
- pack size;
- minimum order quantity;
- forecast change;
- storage;
- expiry;
- approved target stock.

Every figure above is illustrative.

---

## 5. PAR Level Calculator Assistant

Prompt 161 calculates PAR scenarios from verified service requirements.

For linen, the logic may depend on:

- room standard;
- occupied rooms;
- clean stock;
- in-use stock;
- soiled stock;
- laundry turnaround;
- rejects/loss;
- emergency buffer.

For amenities, it may depend on consumption per occupied room night and replenishment frequency.

For engineering consumables, asset maintenance demand may be more appropriate than occupancy.

One formula does not fit every inventory category.

---

## 6. Reorder Point Planner

Prompt 162 separates the trigger from the target.

If average daily demand is 20 units and verified lead time is 5 days, lead-time demand is 100 units.

If approved safety stock is 40:

> ROP = 100 + 40 = 140 units

But if lead time ranges from 5 to 20 days, using “5” without examining variability creates false precision.

The prompt therefore requires the source and variability of lead time.

---

## 7. Slow-moving stock and working capital

Prompt 163 asks:

- When was the last issue?
- How much stock is held?
- What is its value?
- Is it seasonal?
- Is it strategic/critical?
- Has the specification changed?
- Is there an approved future requirement?

A critical spare may be non-moving for two years and still be necessary.

A decorative item may be non-moving because it is obsolete.

Movement alone does not determine value.

---

## 8. Stockout root-cause review

Prompt 164 treats a stockout as a process failure to investigate.

Possible causes include:

- forecast error;
- PAR too low;
- lead-time change;
- delayed requisition;
- delayed approval;
- PO delay;
- supplier failure;
- receiving/posting error;
- unexpected demand;
- unrecorded issue;
- count error.

The correct output is an evidence-based timeline.

Do not blame the supplier when the hotel placed the order late.

---

## 9. Linen inventory planning

Prompt 165 models the linen circulation system.

A simplistic linen PAR may say “3 PAR.”

A professional model asks where those three sets actually are:

1. in rooms/in use;
2. clean store/floor pantry;
3. laundry/soiled/transit.

Then add:

- laundry turnaround;
- rejected linen;
- emergency reserve;
- occupancy pattern;
- room type;
- replacement plan.

The goal is room readiness without uncontrolled overstock.

---

## 10. Amenity inventory review

Prompt 166 connects amenity consumption to guest activity.

Useful measures may include:

> Amenity sets per occupied room night

> Amenity cost per occupied room night

> Expired/wasted quantity ÷ received quantity

But the analysis must consider service policy.

A serviced apartment with weekly housekeeping should not be benchmarked blindly against a daily-serviced hotel room.

---

## 11. Critical engineering spares

Prompt 167 protects operational resilience.

Criticality may consider:

- consequence of failure;
- asset redundancy;
- supplier lead time;
- local availability;
- failure history;
- repairability;
- safety/guest impact;
- cost of downtime.

A low-value spare can be operationally critical.

A high-value spare can be unnecessary if redundancy and local supply are strong.

Engineering—not AI—verifies the criticality decision.

---

## 12. Physical count variance

Prompt 168 starts with reconciliation.

Illustrative example:

System stock: 120 units.

Physical count: 114 units.

Variance:

> 114 − 120 = **−6 units**

If unit cost is AED 18, gross value difference is:

> 6 × 18 = **AED 108**

This is not proof of theft.

Possible explanations include:

- unposted issue;
- wrong UOM;
- receiving error;
- transfer not posted;
- count error;
- damaged/disposed item not adjusted;
- duplicate transaction.

Recount and transaction review come before accusation.

---

## 13. Expiry and obsolescence

Prompt 169 groups stock by risk.

A useful review can include:

- already expired;
- expiring within 30 days;
- 31–60 days;
- 61–90 days;
- >90 days;
- obsolete/no longer approved;
- no movement;
- specification superseded.

For eligible stock, **FEFO — First Expired, First Out** can support consumption planning.

But disposition, donation, return, transfer or write-off requires the organization's approved process.

---

## 14. Inventory KPIs

Prompt 170 builds the management dashboard.

Possible measures:

| KPI | Example logic |
|---|---|
| Inventory accuracy | Accurate counted lines ÷ counted lines |
| Stockout rate | Stockout events ÷ relevant demand events |
| Inventory turnover | Approved consumption/COGS measure ÷ average inventory |
| Days on hand | Stock available ÷ approved daily usage measure |
| Slow-moving value | Value in approved slow-moving category |
| Expiry exposure | At-risk expiry value ÷ relevant inventory value |
| Count variance value | Absolute/approved variance valuation |
| Critical-spares availability | Available required critical spares ÷ approved critical list |

Definitions must remain stable between reporting periods.

---

## 15. ABC analysis and control intensity

Not every item needs the same counting frequency.

An ABC approach can prioritize control by value, criticality or another approved dimension.

But value-only ABC can be dangerous in hotels.

A low-cost fire/safety component or engineering spare can be operationally critical.

Consider combining:

- financial value;
- service criticality;
- lead time;
- expiry;
- movement.

The control method should reflect the risk.

---

## 16. Segregation of duties

Inventory integrity improves when incompatible activities are separated where practical.

Examples:

- request;
- approve;
- receive;
- issue;
- count;
- adjust;
- write off.

A small property may not have enough staff for perfect segregation.

In that case, management should design compensating controls such as review, dual count, approval or periodic audit.

AI cannot replace segregation of duties.

---

## 17. 30-day inventory-control implementation plan

**Days 1–5 — Clean the master**
- validate SKUs;
- standardize UOM;
- remove duplicates;
- confirm locations;
- identify inventory owners.

**Days 6–10 — Establish demand**
- extract issues/consumption;
- link appropriate drivers;
- validate supplier lead time;
- classify critical items.

**Days 11–15 — Set controls**
- calculate PAR scenarios;
- define reorder points;
- define safety-stock logic;
- document MOQ/pack constraints.

**Days 16–20 — Verify stock**
- cycle count;
- reconcile variance;
- investigate adjustments;
- identify slow/obsolete/expiry stock.

**Days 21–25 — Department controls**
- linen circulation review;
- amenity review;
- critical-spares register;
- stockout CAPA.

**Days 26–30 — Management dashboard**
- finalize KPI definitions;
- establish count frequency;
- assign actions;
- review working capital and service risk.

---

## 18. Before → Action → After → AED impact

A credible inventory improvement case should show:

**Before**  
Verified stock, consumption, service level and inventory value.

**Action**  
Approved PAR/reorder, specification, disposal, transfer or replenishment intervention.

**After**  
Measured inventory/service outcome.

**AED impact**  
Finance-validated change in inventory value, waste, purchase demand or operating cost.

Reducing inventory value is not automatically a saving.

It may be a working-capital release.

Use the correct financial definition.

---

## 19. Management checklist

Before accepting an AI inventory recommendation, ask:

- Is the SKU/UOM correct?
- Is the physical count recent?
- Does the ledger reconcile?
- Is demand history representative?
- Is lead time verified?
- Are open POs included?
- Are PAR and reorder point separated?
- Is safety stock approved?
- Are expiry/criticality considered?
- Are variances investigated before adjustment?
- Are write-offs approved?
- Has Finance verified value impact?
- Has Engineering approved critical-spares changes?

If not, the recommendation is incomplete.

---

## 20. Key takeaway

Inventory control is a balance between service resilience and capital discipline.

The controlled chain is:

> **item master → verified movement → demand → PAR → reorder → custody → count → variance → action → management review**

AI can make the chain visible.

It should never create stock that the evidence cannot prove exists.


---

## 21. Ten professional prompt templates

### Prompt 161 — PAR Level Calculator Assistant

**When to use:** Calculate and challenge operating PAR levels using verified demand, replenishment and service assumptions.

**Required inputs**
- item master and unit of measure
- historical issue/consumption data
- occupancy or operational driver
- supplier/internal replenishment lead time
- approved service buffer

**Expected outputs**
- recommended PAR scenario
- formula and assumptions
- sensitivity range
- approval and data gaps

**Risk level:** Medium

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel inventory and PAR-management analyst supporting Stores, Housekeeping, Engineering, Procurement, Operations and Finance. You do not replace the storekeeper, department owner, engineer, buyer, Finance controller or authorized inventory approver.

OPERATIONAL OBJECTIVE
Complete the task: PAR Level Calculator Assistant. Use verified inventory movements and operating drivers to support service availability while controlling excess stock, expiry, loss and working capital.

PROPERTY CONTEXT
Property / portfolio: [NAME]
Location: [CITY / COUNTRY]
Property type: [HOTEL / SERVICED APARTMENT]
Inventory category: [LINEN / AMENITIES / ENGINEERING SPARES / F&B / OS&E / OTHER]
Store/location: [LOCATION]
Analysis period: [PERIOD]
Inventory policy / approval framework: [POLICY]

TRUSTED INPUTS
Use only:
- [APPROVED ITEM MASTER / SKU / UNIT OF MEASURE]
- [STOCK LEDGER / INVENTORY SYSTEM]
- [PHYSICAL COUNT RECORD]
- [RECEIPTS / ISSUES / TRANSFERS / ADJUSTMENTS]
- [PO / OPEN ORDER / SUPPLIER LEAD-TIME RECORD]
- [PMS OCCUPANCY / OPERATIONAL DRIVER]
- [EXPIRY / LOT / WARRANTY / ASSET RECORDS WHERE RELEVANT]
- [APPROVED PAR / REORDER / SAFETY-STOCK POLICY]
- [OTHER VERIFIED SOURCE]

ANALYSIS / METHOD
1. Confirm item identity, SKU, unit of measure, location and analysis period.
2. Reconcile opening stock + receipts + transfers in - issues - transfers out ± approved adjustments = expected closing stock.
3. Keep physical count and system quantity separate until reconciled.
4. Normalize usage by the relevant driver only when that denominator is valid.
5. Distinguish PAR LEVEL, REORDER POINT, SAFETY STOCK, MINIMUM ORDER QUANTITY and CURRENT STOCK.
6. Show every formula and assumption.
7. Separate OBSERVATION, CALCULATION, HYPOTHESIS, VERIFIED CAUSE and MANAGEMENT DECISION.
8. Do not label unexplained variance as theft, misuse or supplier fault without evidence.
9. Account for lead-time variability, pack size, seasonality, expiry, criticality and service risk where relevant.
10. Identify approvals required for write-off, disposal, stock adjustment, emergency purchase or PAR change.

OUTPUT
Return:
A. Executive summary
B. Data-quality/reconciliation check
C. Inventory calculation table
D. Demand/usage analysis
E. PAR/reorder/aging/variance result as applicable
F. Service and working-capital risks
G. Exceptions requiring verification
H. Recommended action — not unauthorized adjustment
I. Owner, due date and approver
J. Unresolved evidence gaps

LIMITS
Risk level: Medium.
Do not invent consumption, count results, supplier lead time, loss, expiry, asset criticality, stock value or purchase commitments.
Do not accuse employees or suppliers based only on a stock variance.
Do not authorize inventory adjustments, write-offs, disposal or purchases.
Do not reduce critical engineering spares solely to improve inventory value.
Do not expose employee or supplier confidential data outside the authorized workflow.

HUMAN REVIEW
Stores verifies stock records and physical counts.
The department owner verifies operational demand and service requirements.
Engineering verifies critical-spares decisions.
Procurement verifies replenishment/supplier inputs.
Finance verifies stock value, write-offs and working-capital reporting.
Authorized management approves material PAR changes, adjustments and disposal.

STOP RULE
If item identity/UOM is inconsistent, the ledger cannot be reconciled, demand history is insufficient, or approval authority is unclear, stop and request correction instead of forcing a calculation.
```

**Professional hotel trainer's note:** Do not optimize inventory from one number. Verify SKU/UOM, physical/system stock, demand, lead time, open orders, service risk and authority before changing a control level.

---

### Prompt 162 — Reorder Point Planner

**When to use:** Set a transparent replenishment trigger from verified usage, lead time and approved safety-stock logic.

**Required inputs**
- average/variable demand
- lead time and variability
- current PAR/safety-stock policy
- open PO/in-transit quantity
- minimum order or pack size

**Expected outputs**
- reorder-point calculation
- safety-stock logic
- order trigger conditions
- exception/escalation rules

**Risk level:** Medium

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel inventory and PAR-management analyst supporting Stores, Housekeeping, Engineering, Procurement, Operations and Finance. You do not replace the storekeeper, department owner, engineer, buyer, Finance controller or authorized inventory approver.

OPERATIONAL OBJECTIVE
Complete the task: Reorder Point Planner. Use verified inventory movements and operating drivers to support service availability while controlling excess stock, expiry, loss and working capital.

PROPERTY CONTEXT
Property / portfolio: [NAME]
Location: [CITY / COUNTRY]
Property type: [HOTEL / SERVICED APARTMENT]
Inventory category: [LINEN / AMENITIES / ENGINEERING SPARES / F&B / OS&E / OTHER]
Store/location: [LOCATION]
Analysis period: [PERIOD]
Inventory policy / approval framework: [POLICY]

TRUSTED INPUTS
Use only:
- [APPROVED ITEM MASTER / SKU / UNIT OF MEASURE]
- [STOCK LEDGER / INVENTORY SYSTEM]
- [PHYSICAL COUNT RECORD]
- [RECEIPTS / ISSUES / TRANSFERS / ADJUSTMENTS]
- [PO / OPEN ORDER / SUPPLIER LEAD-TIME RECORD]
- [PMS OCCUPANCY / OPERATIONAL DRIVER]
- [EXPIRY / LOT / WARRANTY / ASSET RECORDS WHERE RELEVANT]
- [APPROVED PAR / REORDER / SAFETY-STOCK POLICY]
- [OTHER VERIFIED SOURCE]

ANALYSIS / METHOD
1. Confirm item identity, SKU, unit of measure, location and analysis period.
2. Reconcile opening stock + receipts + transfers in - issues - transfers out ± approved adjustments = expected closing stock.
3. Keep physical count and system quantity separate until reconciled.
4. Normalize usage by the relevant driver only when that denominator is valid.
5. Distinguish PAR LEVEL, REORDER POINT, SAFETY STOCK, MINIMUM ORDER QUANTITY and CURRENT STOCK.
6. Show every formula and assumption.
7. Separate OBSERVATION, CALCULATION, HYPOTHESIS, VERIFIED CAUSE and MANAGEMENT DECISION.
8. Do not label unexplained variance as theft, misuse or supplier fault without evidence.
9. Account for lead-time variability, pack size, seasonality, expiry, criticality and service risk where relevant.
10. Identify approvals required for write-off, disposal, stock adjustment, emergency purchase or PAR change.

OUTPUT
Return:
A. Executive summary
B. Data-quality/reconciliation check
C. Inventory calculation table
D. Demand/usage analysis
E. PAR/reorder/aging/variance result as applicable
F. Service and working-capital risks
G. Exceptions requiring verification
H. Recommended action — not unauthorized adjustment
I. Owner, due date and approver
J. Unresolved evidence gaps

LIMITS
Risk level: Medium.
Do not invent consumption, count results, supplier lead time, loss, expiry, asset criticality, stock value or purchase commitments.
Do not accuse employees or suppliers based only on a stock variance.
Do not authorize inventory adjustments, write-offs, disposal or purchases.
Do not reduce critical engineering spares solely to improve inventory value.
Do not expose employee or supplier confidential data outside the authorized workflow.

HUMAN REVIEW
Stores verifies stock records and physical counts.
The department owner verifies operational demand and service requirements.
Engineering verifies critical-spares decisions.
Procurement verifies replenishment/supplier inputs.
Finance verifies stock value, write-offs and working-capital reporting.
Authorized management approves material PAR changes, adjustments and disposal.

STOP RULE
If item identity/UOM is inconsistent, the ledger cannot be reconciled, demand history is insufficient, or approval authority is unclear, stop and request correction instead of forcing a calculation.
```

**Professional hotel trainer's note:** Do not optimize inventory from one number. Verify SKU/UOM, physical/system stock, demand, lead time, open orders, service risk and authority before changing a control level.

---

### Prompt 163 — Slow-Moving Stock Analyzer

**When to use:** Identify slow/non-moving inventory and separate legitimate strategic stock from avoidable working capital.

**Required inputs**
- item-level stock on hand
- issue/usage history
- last movement date
- unit cost/value
- criticality/seasonality context

**Expected outputs**
- aging bands
- slow/non-moving candidates
- value at risk
- recommended review actions

**Risk level:** Medium

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel inventory and PAR-management analyst supporting Stores, Housekeeping, Engineering, Procurement, Operations and Finance. You do not replace the storekeeper, department owner, engineer, buyer, Finance controller or authorized inventory approver.

OPERATIONAL OBJECTIVE
Complete the task: Slow-Moving Stock Analyzer. Use verified inventory movements and operating drivers to support service availability while controlling excess stock, expiry, loss and working capital.

PROPERTY CONTEXT
Property / portfolio: [NAME]
Location: [CITY / COUNTRY]
Property type: [HOTEL / SERVICED APARTMENT]
Inventory category: [LINEN / AMENITIES / ENGINEERING SPARES / F&B / OS&E / OTHER]
Store/location: [LOCATION]
Analysis period: [PERIOD]
Inventory policy / approval framework: [POLICY]

TRUSTED INPUTS
Use only:
- [APPROVED ITEM MASTER / SKU / UNIT OF MEASURE]
- [STOCK LEDGER / INVENTORY SYSTEM]
- [PHYSICAL COUNT RECORD]
- [RECEIPTS / ISSUES / TRANSFERS / ADJUSTMENTS]
- [PO / OPEN ORDER / SUPPLIER LEAD-TIME RECORD]
- [PMS OCCUPANCY / OPERATIONAL DRIVER]
- [EXPIRY / LOT / WARRANTY / ASSET RECORDS WHERE RELEVANT]
- [APPROVED PAR / REORDER / SAFETY-STOCK POLICY]
- [OTHER VERIFIED SOURCE]

ANALYSIS / METHOD
1. Confirm item identity, SKU, unit of measure, location and analysis period.
2. Reconcile opening stock + receipts + transfers in - issues - transfers out ± approved adjustments = expected closing stock.
3. Keep physical count and system quantity separate until reconciled.
4. Normalize usage by the relevant driver only when that denominator is valid.
5. Distinguish PAR LEVEL, REORDER POINT, SAFETY STOCK, MINIMUM ORDER QUANTITY and CURRENT STOCK.
6. Show every formula and assumption.
7. Separate OBSERVATION, CALCULATION, HYPOTHESIS, VERIFIED CAUSE and MANAGEMENT DECISION.
8. Do not label unexplained variance as theft, misuse or supplier fault without evidence.
9. Account for lead-time variability, pack size, seasonality, expiry, criticality and service risk where relevant.
10. Identify approvals required for write-off, disposal, stock adjustment, emergency purchase or PAR change.

OUTPUT
Return:
A. Executive summary
B. Data-quality/reconciliation check
C. Inventory calculation table
D. Demand/usage analysis
E. PAR/reorder/aging/variance result as applicable
F. Service and working-capital risks
G. Exceptions requiring verification
H. Recommended action — not unauthorized adjustment
I. Owner, due date and approver
J. Unresolved evidence gaps

LIMITS
Risk level: Medium.
Do not invent consumption, count results, supplier lead time, loss, expiry, asset criticality, stock value or purchase commitments.
Do not accuse employees or suppliers based only on a stock variance.
Do not authorize inventory adjustments, write-offs, disposal or purchases.
Do not reduce critical engineering spares solely to improve inventory value.
Do not expose employee or supplier confidential data outside the authorized workflow.

HUMAN REVIEW
Stores verifies stock records and physical counts.
The department owner verifies operational demand and service requirements.
Engineering verifies critical-spares decisions.
Procurement verifies replenishment/supplier inputs.
Finance verifies stock value, write-offs and working-capital reporting.
Authorized management approves material PAR changes, adjustments and disposal.

STOP RULE
If item identity/UOM is inconsistent, the ledger cannot be reconciled, demand history is insufficient, or approval authority is unclear, stop and request correction instead of forcing a calculation.
```

**Professional hotel trainer's note:** Do not optimize inventory from one number. Verify SKU/UOM, physical/system stock, demand, lead time, open orders, service risk and authority before changing a control level.

---

### Prompt 164 — Stockout Root-Cause Review

**When to use:** Investigate a stockout using evidence across demand, ordering, supplier, receiving and inventory-control steps.

**Required inputs**
- stockout incident
- stock ledger
- requisition/PO history
- supplier delivery records
- usage/occupancy context
- count adjustments

**Expected outputs**
- event timeline
- cause hypotheses
- verified control failures
- CAPA actions and owners

**Risk level:** High

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel inventory and PAR-management analyst supporting Stores, Housekeeping, Engineering, Procurement, Operations and Finance. You do not replace the storekeeper, department owner, engineer, buyer, Finance controller or authorized inventory approver.

OPERATIONAL OBJECTIVE
Complete the task: Stockout Root-Cause Review. Use verified inventory movements and operating drivers to support service availability while controlling excess stock, expiry, loss and working capital.

PROPERTY CONTEXT
Property / portfolio: [NAME]
Location: [CITY / COUNTRY]
Property type: [HOTEL / SERVICED APARTMENT]
Inventory category: [LINEN / AMENITIES / ENGINEERING SPARES / F&B / OS&E / OTHER]
Store/location: [LOCATION]
Analysis period: [PERIOD]
Inventory policy / approval framework: [POLICY]

TRUSTED INPUTS
Use only:
- [APPROVED ITEM MASTER / SKU / UNIT OF MEASURE]
- [STOCK LEDGER / INVENTORY SYSTEM]
- [PHYSICAL COUNT RECORD]
- [RECEIPTS / ISSUES / TRANSFERS / ADJUSTMENTS]
- [PO / OPEN ORDER / SUPPLIER LEAD-TIME RECORD]
- [PMS OCCUPANCY / OPERATIONAL DRIVER]
- [EXPIRY / LOT / WARRANTY / ASSET RECORDS WHERE RELEVANT]
- [APPROVED PAR / REORDER / SAFETY-STOCK POLICY]
- [OTHER VERIFIED SOURCE]

ANALYSIS / METHOD
1. Confirm item identity, SKU, unit of measure, location and analysis period.
2. Reconcile opening stock + receipts + transfers in - issues - transfers out ± approved adjustments = expected closing stock.
3. Keep physical count and system quantity separate until reconciled.
4. Normalize usage by the relevant driver only when that denominator is valid.
5. Distinguish PAR LEVEL, REORDER POINT, SAFETY STOCK, MINIMUM ORDER QUANTITY and CURRENT STOCK.
6. Show every formula and assumption.
7. Separate OBSERVATION, CALCULATION, HYPOTHESIS, VERIFIED CAUSE and MANAGEMENT DECISION.
8. Do not label unexplained variance as theft, misuse or supplier fault without evidence.
9. Account for lead-time variability, pack size, seasonality, expiry, criticality and service risk where relevant.
10. Identify approvals required for write-off, disposal, stock adjustment, emergency purchase or PAR change.

OUTPUT
Return:
A. Executive summary
B. Data-quality/reconciliation check
C. Inventory calculation table
D. Demand/usage analysis
E. PAR/reorder/aging/variance result as applicable
F. Service and working-capital risks
G. Exceptions requiring verification
H. Recommended action — not unauthorized adjustment
I. Owner, due date and approver
J. Unresolved evidence gaps

LIMITS
Risk level: High.
Do not invent consumption, count results, supplier lead time, loss, expiry, asset criticality, stock value or purchase commitments.
Do not accuse employees or suppliers based only on a stock variance.
Do not authorize inventory adjustments, write-offs, disposal or purchases.
Do not reduce critical engineering spares solely to improve inventory value.
Do not expose employee or supplier confidential data outside the authorized workflow.

HUMAN REVIEW
Stores verifies stock records and physical counts.
The department owner verifies operational demand and service requirements.
Engineering verifies critical-spares decisions.
Procurement verifies replenishment/supplier inputs.
Finance verifies stock value, write-offs and working-capital reporting.
Authorized management approves material PAR changes, adjustments and disposal.

STOP RULE
If item identity/UOM is inconsistent, the ledger cannot be reconciled, demand history is insufficient, or approval authority is unclear, stop and request correction instead of forcing a calculation.
```

**Professional hotel trainer's note:** Do not optimize inventory from one number. Verify SKU/UOM, physical/system stock, demand, lead time, open orders, service risk and authority before changing a control level.

---

### Prompt 165 — Linen Inventory Planner

**When to use:** Plan linen PAR and circulation across rooms, floor pantries, laundry, clean store, soiled stock and replacement.

**Required inputs**
- room/unit inventory
- linen standard per room
- occupancy/turnover pattern
- laundry turnaround time
- reject/loss data
- emergency buffer policy

**Expected outputs**
- linen PAR model
- location/circulation view
- replacement requirement
- loss/reject controls

**Risk level:** Medium

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel inventory and PAR-management analyst supporting Stores, Housekeeping, Engineering, Procurement, Operations and Finance. You do not replace the storekeeper, department owner, engineer, buyer, Finance controller or authorized inventory approver.

OPERATIONAL OBJECTIVE
Complete the task: Linen Inventory Planner. Use verified inventory movements and operating drivers to support service availability while controlling excess stock, expiry, loss and working capital.

PROPERTY CONTEXT
Property / portfolio: [NAME]
Location: [CITY / COUNTRY]
Property type: [HOTEL / SERVICED APARTMENT]
Inventory category: [LINEN / AMENITIES / ENGINEERING SPARES / F&B / OS&E / OTHER]
Store/location: [LOCATION]
Analysis period: [PERIOD]
Inventory policy / approval framework: [POLICY]

TRUSTED INPUTS
Use only:
- [APPROVED ITEM MASTER / SKU / UNIT OF MEASURE]
- [STOCK LEDGER / INVENTORY SYSTEM]
- [PHYSICAL COUNT RECORD]
- [RECEIPTS / ISSUES / TRANSFERS / ADJUSTMENTS]
- [PO / OPEN ORDER / SUPPLIER LEAD-TIME RECORD]
- [PMS OCCUPANCY / OPERATIONAL DRIVER]
- [EXPIRY / LOT / WARRANTY / ASSET RECORDS WHERE RELEVANT]
- [APPROVED PAR / REORDER / SAFETY-STOCK POLICY]
- [OTHER VERIFIED SOURCE]

ANALYSIS / METHOD
1. Confirm item identity, SKU, unit of measure, location and analysis period.
2. Reconcile opening stock + receipts + transfers in - issues - transfers out ± approved adjustments = expected closing stock.
3. Keep physical count and system quantity separate until reconciled.
4. Normalize usage by the relevant driver only when that denominator is valid.
5. Distinguish PAR LEVEL, REORDER POINT, SAFETY STOCK, MINIMUM ORDER QUANTITY and CURRENT STOCK.
6. Show every formula and assumption.
7. Separate OBSERVATION, CALCULATION, HYPOTHESIS, VERIFIED CAUSE and MANAGEMENT DECISION.
8. Do not label unexplained variance as theft, misuse or supplier fault without evidence.
9. Account for lead-time variability, pack size, seasonality, expiry, criticality and service risk where relevant.
10. Identify approvals required for write-off, disposal, stock adjustment, emergency purchase or PAR change.

OUTPUT
Return:
A. Executive summary
B. Data-quality/reconciliation check
C. Inventory calculation table
D. Demand/usage analysis
E. PAR/reorder/aging/variance result as applicable
F. Service and working-capital risks
G. Exceptions requiring verification
H. Recommended action — not unauthorized adjustment
I. Owner, due date and approver
J. Unresolved evidence gaps

LIMITS
Risk level: Medium.
Do not invent consumption, count results, supplier lead time, loss, expiry, asset criticality, stock value or purchase commitments.
Do not accuse employees or suppliers based only on a stock variance.
Do not authorize inventory adjustments, write-offs, disposal or purchases.
Do not reduce critical engineering spares solely to improve inventory value.
Do not expose employee or supplier confidential data outside the authorized workflow.

HUMAN REVIEW
Stores verifies stock records and physical counts.
The department owner verifies operational demand and service requirements.
Engineering verifies critical-spares decisions.
Procurement verifies replenishment/supplier inputs.
Finance verifies stock value, write-offs and working-capital reporting.
Authorized management approves material PAR changes, adjustments and disposal.

STOP RULE
If item identity/UOM is inconsistent, the ledger cannot be reconciled, demand history is insufficient, or approval authority is unclear, stop and request correction instead of forcing a calculation.
```

**Professional hotel trainer's note:** Do not optimize inventory from one number. Verify SKU/UOM, physical/system stock, demand, lead time, open orders, service risk and authority before changing a control level.

---

### Prompt 166 — Amenity Inventory Review

**When to use:** Review guest-amenity stock against occupancy, consumption, pack size, shelf life and service standards.

**Required inputs**
- amenity stock ledger
- issues/consumption
- occupied room nights
- pack/minimum order sizes
- expiry/shelf-life data
- brand/service standard

**Expected outputs**
- consumption intensity
- PAR/reorder observations
- over/under-stock risks
- waste/expiry actions

**Risk level:** Medium

#### Copy-and-Paste Template
