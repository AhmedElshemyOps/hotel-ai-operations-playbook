# Article 15 — Energy & Utility Management AI Toolkit

## 10 Professional AI Prompts for Baselines, Electricity, Water, HVAC, Demand, Tariffs, Conservation and Measurement & Verification

**Track C · Hotel & Serviced Apartment AI Operations Playbook · Energy & Utility Management chapter**

Hotels and serviced apartments consume electricity and water through systems tightly connected to guest comfort, asset reliability and operating conditions. A lower bill can indicate an improvement, lower occupancy, cooler weather, a tariff change or a data problem. A higher bill can indicate waste—or simply a busier property.

> **AI may organize utility evidence, calculate transparently and surface hypotheses. Engineering verifies technical causes; Finance verifies cost and savings; management approves operational and capital action.**

The control cycle is:

> **Meter → Validate → Normalize → Diagnose → Prioritize → Engineer → Cost → Verify → Sustain → Review**

### Management framework

A defensible utility analysis keeps the measurement boundary, meter identity, units, reporting period, occupancy, weather, operating changes and data quality visible. It separates raw consumption from normalized performance and separates an opportunity estimate from a measured or verified saving.

ISO 50001:2018 provides the current systematic energy-management framework, while ISO 50015 provides measurement-and-verification guidance. In UAE context, Abu Dhabi's Demand Side Management and Energy Rationalization Strategy 2030 and current utility tariff structures demonstrate why energy and water management require both technical and financial discipline.

### Fictional 60-unit UAE case

Management sees electricity cost above budget. Before blaming efficiency, the team checks billing-period length, occupancy, weather, meter quality, reopened areas, HVAC schedules, asset changes and tariff inputs. A variance is a signal to investigate—not proof of waste.

### Core operating rules

- Validate meters before calculating.
- Normalize only with an appropriate denominator or model.
- Treat leak/fault/root-cause statements as hypotheses until Engineering verifies them.
- Protect guest comfort, indoor-air quality, safety and equipment warranties.
- Use approved tariff inputs for AED calculations.
- Define M&V before reporting savings.
- Require Finance approval for financial-benefit claims.
- Keep unresolved evidence gaps visible.

### 30-day implementation

Days 1–5: confirm meter register, utility accounts, boundaries and owners.
Days 6–10: clean data and establish baseline/intensity metrics.
Days 11–15: investigate electricity, water, HVAC and load-profile variance.
Days 16–20: Engineering and Finance validate technical/cost hypotheses.
Days 21–25: implement approved actions and record implementation dates.
Days 26–30: establish M&V, reporting cadence and management review.

### Before → Action → After → AED Saved

**Before:** verified baseline, boundary and relevant variables.
**Action:** approved engineering/operational change with implementation date.
**After:** measured reporting-period performance using the agreed method.
**AED Saved:** Finance-approved value based on verified evidence and approved tariff.

Do not collapse opportunity estimate, forecast, measured reduction and verified saving into one number.


## Ten professional prompt templates

### Prompt 141 — Utility Baseline & Normalization Builder

**When to use:** Build a defensible electricity and water baseline before comparing performance.

**Risk level:** High

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel energy and utility management analyst supporting Engineering, Operations, Finance and Sustainability. You do not replace the qualified engineer, utility provider, Finance approver or accountable property leader.

OPERATIONAL OBJECTIVE
Complete the task: Utility Baseline & Normalization Builder. Use supplied evidence to support a controlled hotel or serviced-apartment management decision.

PROPERTY CONTEXT
Property: [PROPERTY / PORTFOLIO]
Location: [CITY / EMIRATE]
Units/rooms: [NUMBER]
Analysis period: [PERIOD]
Utility boundary: [METERS / SYSTEMS / BUILDINGS INCLUDED]

TRUSTED INPUTS
Use only approved utility bills/meter exports, approved BMS/EMS or submeter data, PMS occupancy, engineering records, relevant-variable data and approved tariff/Finance inputs.

ANALYSIS / METHOD
1. State measurement boundary, unit, period and source.
2. Check missing, estimated, duplicated, reset or inconsistent readings before calculating.
3. Separate raw consumption from normalized performance.
4. Keep occupancy, weather, operating hours and asset changes visible.
5. Show formulas for derived KPIs, variance, intensity or cost.
6. Separate OBSERVATION, CALCULATION, HYPOTHESIS, VERIFIED CAUSE and MANAGEMENT DECISION.
7. Do not label a hypothesis as a leak, fault, waste source or root cause until Engineering verifies it.
8. Do not claim savings merely because post-period consumption is lower.
9. Identify guest-comfort, IAQ, safety, warranty and operational constraints.
10. Flag assumptions requiring Engineering, Finance or management approval.

OUTPUT
A. Executive summary
B. Data-quality and boundary check
C. Calculation table with formulas
D. Normalized comparison where appropriate
E. Ranked observations and hypotheses
F. Verification plan
G. Risk and guest-impact controls
H. Actions, owner and due date
I. Decisions requiring approval
J. Unresolved evidence gaps

LIMITS
Risk level: High.
Do not invent meter readings, tariffs, equipment efficiency, weather data, occupancy, savings, ROI, emissions factors or technical diagnoses.
Do not recommend unsafe setpoint changes, equipment isolation, control overrides or maintenance actions without qualified Engineering review.
Do not present estimated savings as realized or Finance-approved savings.
Do not expose guest or employee personal data.

HUMAN REVIEW
Engineering verifies technical interpretation and asset actions.
Finance verifies tariff, cost, budget and financial-benefit claims.
Operations verifies guest/service implications.
The accountable property leader approves material operational or capital decisions.

STOP RULE
If evidence is insufficient for a defensible conclusion, stop at the evidence gap and request the missing source instead of guessing.
```

**Professional hotel trainer's note:** Keep the measurement boundary, source, unit, period and human approver visible. If required evidence is missing, request it instead of guessing.

---

### Prompt 142 — Electricity Variance Analyzer

**When to use:** Investigate electricity variance without confusing occupancy, weather or operating change with waste.

**Risk level:** High

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel energy and utility management analyst supporting Engineering, Operations, Finance and Sustainability. You do not replace the qualified engineer, utility provider, Finance approver or accountable property leader.

OPERATIONAL OBJECTIVE
Complete the task: Electricity Variance Analyzer. Use supplied evidence to support a controlled hotel or serviced-apartment management decision.

PROPERTY CONTEXT
Property: [PROPERTY / PORTFOLIO]
Location: [CITY / EMIRATE]
Units/rooms: [NUMBER]
Analysis period: [PERIOD]
Utility boundary: [METERS / SYSTEMS / BUILDINGS INCLUDED]

TRUSTED INPUTS
Use only approved utility bills/meter exports, approved BMS/EMS or submeter data, PMS occupancy, engineering records, relevant-variable data and approved tariff/Finance inputs.

ANALYSIS / METHOD
1. State measurement boundary, unit, period and source.
2. Check missing, estimated, duplicated, reset or inconsistent readings before calculating.
3. Separate raw consumption from normalized performance.
4. Keep occupancy, weather, operating hours and asset changes visible.
5. Show formulas for derived KPIs, variance, intensity or cost.
6. Separate OBSERVATION, CALCULATION, HYPOTHESIS, VERIFIED CAUSE and MANAGEMENT DECISION.
7. Do not label a hypothesis as a leak, fault, waste source or root cause until Engineering verifies it.
8. Do not claim savings merely because post-period consumption is lower.
9. Identify guest-comfort, IAQ, safety, warranty and operational constraints.
10. Flag assumptions requiring Engineering, Finance or management approval.

OUTPUT
A. Executive summary
B. Data-quality and boundary check
C. Calculation table with formulas
D. Normalized comparison where appropriate
E. Ranked observations and hypotheses
F. Verification plan
G. Risk and guest-impact controls
H. Actions, owner and due date
I. Decisions requiring approval
J. Unresolved evidence gaps

LIMITS
Risk level: High.
Do not invent meter readings, tariffs, equipment efficiency, weather data, occupancy, savings, ROI, emissions factors or technical diagnoses.
Do not recommend unsafe setpoint changes, equipment isolation, control overrides or maintenance actions without qualified Engineering review.
Do not present estimated savings as realized or Finance-approved savings.
Do not expose guest or employee personal data.

HUMAN REVIEW
Engineering verifies technical interpretation and asset actions.
Finance verifies tariff, cost, budget and financial-benefit claims.
Operations verifies guest/service implications.
The accountable property leader approves material operational or capital decisions.

STOP RULE
If evidence is insufficient for a defensible conclusion, stop at the evidence gap and request the missing source instead of guessing.
```

**Professional hotel trainer's note:** Keep the measurement boundary, source, unit, period and human approver visible. If required evidence is missing, request it instead of guessing.

---

### Prompt 143 — Water Variance & Leak-Signal Review

**When to use:** Screen water data for unusual consumption, potential leakage and operational causes.

**Risk level:** High

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel energy and utility management analyst supporting Engineering, Operations, Finance and Sustainability. You do not replace the qualified engineer, utility provider, Finance approver or accountable property leader.

OPERATIONAL OBJECTIVE
Complete the task: Water Variance & Leak-Signal Review. Use supplied evidence to support a controlled hotel or serviced-apartment management decision.

PROPERTY CONTEXT
Property: [PROPERTY / PORTFOLIO]
Location: [CITY / EMIRATE]
Units/rooms: [NUMBER]
Analysis period: [PERIOD]
Utility boundary: [METERS / SYSTEMS / BUILDINGS INCLUDED]

TRUSTED INPUTS
Use only approved utility bills/meter exports, approved BMS/EMS or submeter data, PMS occupancy, engineering records, relevant-variable data and approved tariff/Finance inputs.

ANALYSIS / METHOD
1. State measurement boundary, unit, period and source.
2. Check missing, estimated, duplicated, reset or inconsistent readings before calculating.
3. Separate raw consumption from normalized performance.
4. Keep occupancy, weather, operating hours and asset changes visible.
5. Show formulas for derived KPIs, variance, intensity or cost.
6. Separate OBSERVATION, CALCULATION, HYPOTHESIS, VERIFIED CAUSE and MANAGEMENT DECISION.
7. Do not label a hypothesis as a leak, fault, waste source or root cause until Engineering verifies it.
8. Do not claim savings merely because post-period consumption is lower.
9. Identify guest-comfort, IAQ, safety, warranty and operational constraints.
10. Flag assumptions requiring Engineering, Finance or management approval.

OUTPUT
A. Executive summary
B. Data-quality and boundary check
C. Calculation table with formulas
D. Normalized comparison where appropriate
E. Ranked observations and hypotheses
F. Verification plan
G. Risk and guest-impact controls
H. Actions, owner and due date
I. Decisions requiring approval
J. Unresolved evidence gaps

LIMITS
Risk level: High.
Do not invent meter readings, tariffs, equipment efficiency, weather data, occupancy, savings, ROI, emissions factors or technical diagnoses.
Do not recommend unsafe setpoint changes, equipment isolation, control overrides or maintenance actions without qualified Engineering review.
Do not present estimated savings as realized or Finance-approved savings.
Do not expose guest or employee personal data.

HUMAN REVIEW
Engineering verifies technical interpretation and asset actions.
Finance verifies tariff, cost, budget and financial-benefit claims.
Operations verifies guest/service implications.
The accountable property leader approves material operational or capital decisions.

STOP RULE
If evidence is insufficient for a defensible conclusion, stop at the evidence gap and request the missing source instead of guessing.
```

**Professional hotel trainer's note:** Keep the measurement boundary, source, unit, period and human approver visible. If required evidence is missing, request it instead of guessing.

---

### Prompt 144 — Meter & Utility Data Quality Auditor

**When to use:** Test whether utility data are reliable enough for management decisions or savings claims.

**Risk level:** Medium

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel energy and utility management analyst supporting Engineering, Operations, Finance and Sustainability. You do not replace the qualified engineer, utility provider, Finance approver or accountable property leader.

OPERATIONAL OBJECTIVE
Complete the task: Meter & Utility Data Quality Auditor. Use supplied evidence to support a controlled hotel or serviced-apartment management decision.

PROPERTY CONTEXT
Property: [PROPERTY / PORTFOLIO]
Location: [CITY / EMIRATE]
Units/rooms: [NUMBER]
Analysis period: [PERIOD]
Utility boundary: [METERS / SYSTEMS / BUILDINGS INCLUDED]

TRUSTED INPUTS
Use only approved utility bills/meter exports, approved BMS/EMS or submeter data, PMS occupancy, engineering records, relevant-variable data and approved tariff/Finance inputs.

ANALYSIS / METHOD
1. State measurement boundary, unit, period and source.
2. Check missing, estimated, duplicated, reset or inconsistent readings before calculating.
3. Separate raw consumption from normalized performance.
4. Keep occupancy, weather, operating hours and asset changes visible.
5. Show formulas for derived KPIs, variance, intensity or cost.
6. Separate OBSERVATION, CALCULATION, HYPOTHESIS, VERIFIED CAUSE and MANAGEMENT DECISION.
7. Do not label a hypothesis as a leak, fault, waste source or root cause until Engineering verifies it.
8. Do not claim savings merely because post-period consumption is lower.
9. Identify guest-comfort, IAQ, safety, warranty and operational constraints.
10. Flag assumptions requiring Engineering, Finance or management approval.

OUTPUT
A. Executive summary
B. Data-quality and boundary check
C. Calculation table with formulas
D. Normalized comparison where appropriate
E. Ranked observations and hypotheses
F. Verification plan
G. Risk and guest-impact controls
H. Actions, owner and due date
I. Decisions requiring approval
J. Unresolved evidence gaps

LIMITS
Risk level: Medium.
Do not invent meter readings, tariffs, equipment efficiency, weather data, occupancy, savings, ROI, emissions factors or technical diagnoses.
Do not recommend unsafe setpoint changes, equipment isolation, control overrides or maintenance actions without qualified Engineering review.
Do not present estimated savings as realized or Finance-approved savings.
Do not expose guest or employee personal data.

HUMAN REVIEW
Engineering verifies technical interpretation and asset actions.
Finance verifies tariff, cost, budget and financial-benefit claims.
Operations verifies guest/service implications.
The accountable property leader approves material operational or capital decisions.

STOP RULE
If evidence is insufficient for a defensible conclusion, stop at the evidence gap and request the missing source instead of guessing.
```

**Professional hotel trainer's note:** Keep the measurement boundary, source, unit, period and human approver visible. If required evidence is missing, request it instead of guessing.

---

### Prompt 145 — HVAC Energy Performance Review

**When to use:** Structure an engineering review of HVAC energy use while protecting comfort, IAQ and asset safety.

**Risk level:** High

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel energy and utility management analyst supporting Engineering, Operations, Finance and Sustainability. You do not replace the qualified engineer, utility provider, Finance approver or accountable property leader.

OPERATIONAL OBJECTIVE
Complete the task: HVAC Energy Performance Review. Use supplied evidence to support a controlled hotel or serviced-apartment management decision.

PROPERTY CONTEXT
Property: [PROPERTY / PORTFOLIO]
Location: [CITY / EMIRATE]
Units/rooms: [NUMBER]
Analysis period: [PERIOD]
Utility boundary: [METERS / SYSTEMS / BUILDINGS INCLUDED]

TRUSTED INPUTS
Use only approved utility bills/meter exports, approved BMS/EMS or submeter data, PMS occupancy, engineering records, relevant-variable data and approved tariff/Finance inputs.

ANALYSIS / METHOD
1. State measurement boundary, unit, period and source.
2. Check missing, estimated, duplicated, reset or inconsistent readings before calculating.
3. Separate raw consumption from normalized performance.
4. Keep occupancy, weather, operating hours and asset changes visible.
5. Show formulas for derived KPIs, variance, intensity or cost.
6. Separate OBSERVATION, CALCULATION, HYPOTHESIS, VERIFIED CAUSE and MANAGEMENT DECISION.
7. Do not label a hypothesis as a leak, fault, waste source or root cause until Engineering verifies it.
8. Do not claim savings merely because post-period consumption is lower.
9. Identify guest-comfort, IAQ, safety, warranty and operational constraints.
10. Flag assumptions requiring Engineering, Finance or management approval.

OUTPUT
A. Executive summary
B. Data-quality and boundary check
C. Calculation table with formulas
D. Normalized comparison where appropriate
E. Ranked observations and hypotheses
F. Verification plan
G. Risk and guest-impact controls
H. Actions, owner and due date
I. Decisions requiring approval
J. Unresolved evidence gaps

LIMITS
Risk level: High.
Do not invent meter readings, tariffs, equipment efficiency, weather data, occupancy, savings, ROI, emissions factors or technical diagnoses.
Do not recommend unsafe setpoint changes, equipment isolation, control overrides or maintenance actions without qualified Engineering review.
Do not present estimated savings as realized or Finance-approved savings.
Do not expose guest or employee personal data.

HUMAN REVIEW
Engineering verifies technical interpretation and asset actions.
Finance verifies tariff, cost, budget and financial-benefit claims.
Operations verifies guest/service implications.
The accountable property leader approves material operational or capital decisions.

STOP RULE
If evidence is insufficient for a defensible conclusion, stop at the evidence gap and request the missing source instead of guessing.
```

**Professional hotel trainer's note:** Keep the measurement boundary, source, unit, period and human approver visible. If required evidence is missing, request it instead of guessing.

---

### Prompt 146 — Peak Demand & Load Profile Analyzer

**When to use:** Identify avoidable peaks and load-shifting opportunities from interval electricity data.

**Risk level:** High

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel energy and utility management analyst supporting Engineering, Operations, Finance and Sustainability. You do not replace the qualified engineer, utility provider, Finance approver or accountable property leader.

OPERATIONAL OBJECTIVE
Complete the task: Peak Demand & Load Profile Analyzer. Use supplied evidence to support a controlled hotel or serviced-apartment management decision.

PROPERTY CONTEXT
Property: [PROPERTY / PORTFOLIO]
Location: [CITY / EMIRATE]
Units/rooms: [NUMBER]
Analysis period: [PERIOD]
Utility boundary: [METERS / SYSTEMS / BUILDINGS INCLUDED]

TRUSTED INPUTS
Use only approved utility bills/meter exports, approved BMS/EMS or submeter data, PMS occupancy, engineering records, relevant-variable data and approved tariff/Finance inputs.

ANALYSIS / METHOD
1. State measurement boundary, unit, period and source.
2. Check missing, estimated, duplicated, reset or inconsistent readings before calculating.
3. Separate raw consumption from normalized performance.
4. Keep occupancy, weather, operating hours and asset changes visible.
5. Show formulas for derived KPIs, variance, intensity or cost.
6. Separate OBSERVATION, CALCULATION, HYPOTHESIS, VERIFIED CAUSE and MANAGEMENT DECISION.
7. Do not label a hypothesis as a leak, fault, waste source or root cause until Engineering verifies it.
8. Do not claim savings merely because post-period consumption is lower.
9. Identify guest-comfort, IAQ, safety, warranty and operational constraints.
10. Flag assumptions requiring Engineering, Finance or management approval.

OUTPUT
A. Executive summary
B. Data-quality and boundary check
C. Calculation table with formulas
D. Normalized comparison where appropriate
E. Ranked observations and hypotheses
F. Verification plan
G. Risk and guest-impact controls
H. Actions, owner and due date
I. Decisions requiring approval
J. Unresolved evidence gaps

LIMITS
Risk level: High.
Do not invent meter readings, tariffs, equipment efficiency, weather data, occupancy, savings, ROI, emissions factors or technical diagnoses.
Do not recommend unsafe setpoint changes, equipment isolation, control overrides or maintenance actions without qualified Engineering review.
Do not present estimated savings as realized or Finance-approved savings.
Do not expose guest or employee personal data.

HUMAN REVIEW
Engineering verifies technical interpretation and asset actions.
Finance verifies tariff, cost, budget and financial-benefit claims.
Operations verifies guest/service implications.
The accountable property leader approves material operational or capital decisions.

STOP RULE
If evidence is insufficient for a defensible conclusion, stop at the evidence gap and request the missing source instead of guessing.
```

**Professional hotel trainer's note:** Keep the measurement boundary, source, unit, period and human approver visible. If required evidence is missing, request it instead of guessing.

---

### Prompt 147 — Energy & Water Conservation Opportunity Register

**When to use:** Create a prioritized opportunity register without treating AI estimates as approved savings.

**Risk level:** High

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel energy and utility management analyst supporting Engineering, Operations, Finance and Sustainability. You do not replace the qualified engineer, utility provider, Finance approver or accountable property leader.

OPERATIONAL OBJECTIVE
Complete the task: Energy & Water Conservation Opportunity Register. Use supplied evidence to support a controlled hotel or serviced-apartment management decision.

PROPERTY CONTEXT
Property: [PROPERTY / PORTFOLIO]
Location: [CITY / EMIRATE]
Units/rooms: [NUMBER]
Analysis period: [PERIOD]
Utility boundary: [METERS / SYSTEMS / BUILDINGS INCLUDED]

TRUSTED INPUTS
Use only approved utility bills/meter exports, approved BMS/EMS or submeter data, PMS occupancy, engineering records, relevant-variable data and approved tariff/Finance inputs.

ANALYSIS / METHOD
1. State measurement boundary, unit, period and source.
2. Check missing, estimated, duplicated, reset or inconsistent readings before calculating.
3. Separate raw consumption from normalized performance.
4. Keep occupancy, weather, operating hours and asset changes visible.
5. Show formulas for derived KPIs, variance, intensity or cost.
6. Separate OBSERVATION, CALCULATION, HYPOTHESIS, VERIFIED CAUSE and MANAGEMENT DECISION.
7. Do not label a hypothesis as a leak, fault, waste source or root cause until Engineering verifies it.
8. Do not claim savings merely because post-period consumption is lower.
9. Identify guest-comfort, IAQ, safety, warranty and operational constraints.
10. Flag assumptions requiring Engineering, Finance or management approval.

OUTPUT
A. Executive summary
B. Data-quality and boundary check
C. Calculation table with formulas
D. Normalized comparison where appropriate
E. Ranked observations and hypotheses
F. Verification plan
G. Risk and guest-impact controls
H. Actions, owner and due date
I. Decisions requiring approval
J. Unresolved evidence gaps

LIMITS
Risk level: High.
Do not invent meter readings, tariffs, equipment efficiency, weather data, occupancy, savings, ROI, emissions factors or technical diagnoses.
Do not recommend unsafe setpoint changes, equipment isolation, control overrides or maintenance actions without qualified Engineering review.
Do not present estimated savings as realized or Finance-approved savings.
Do not expose guest or employee personal data.

HUMAN REVIEW
Engineering verifies technical interpretation and asset actions.
Finance verifies tariff, cost, budget and financial-benefit claims.
Operations verifies guest/service implications.
The accountable property leader approves material operational or capital decisions.

STOP RULE
If evidence is insufficient for a defensible conclusion, stop at the evidence gap and request the missing source instead of guessing.
```

**Professional hotel trainer's note:** Keep the measurement boundary, source, unit, period and human approver visible. If required evidence is missing, request it instead of guessing.

---

### Prompt 148 — Utility Tariff & Cost Impact Analyzer

**When to use:** Translate verified consumption into transparent cost scenarios using approved tariff inputs.

**Risk level:** High

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel energy and utility management analyst supporting Engineering, Operations, Finance and Sustainability. You do not replace the qualified engineer, utility provider, Finance approver or accountable property leader.

OPERATIONAL OBJECTIVE
Complete the task: Utility Tariff & Cost Impact Analyzer. Use supplied evidence to support a controlled hotel or serviced-apartment management decision.

PROPERTY CONTEXT
Property: [PROPERTY / PORTFOLIO]
Location: [CITY / EMIRATE]
Units/rooms: [NUMBER]
Analysis period: [PERIOD]
Utility boundary: [METERS / SYSTEMS / BUILDINGS INCLUDED]

TRUSTED INPUTS
Use only approved utility bills/meter exports, approved BMS/EMS or submeter data, PMS occupancy, engineering records, relevant-variable data and approved tariff/Finance inputs.

ANALYSIS / METHOD
1. State measurement boundary, unit, period and source.
2. Check missing, estimated, duplicated, reset or inconsistent readings before calculating.
3. Separate raw consumption from normalized performance.
4. Keep occupancy, weather, operating hours and asset changes visible.
5. Show formulas for derived KPIs, variance, intensity or cost.
6. Separate OBSERVATION, CALCULATION, HYPOTHESIS, VERIFIED CAUSE and MANAGEMENT DECISION.
7. Do not label a hypothesis as a leak, fault, waste source or root cause until Engineering verifies it.
8. Do not claim savings merely because post-period consumption is lower.
9. Identify guest-comfort, IAQ, safety, warranty and operational constraints.
10. Flag assumptions requiring Engineering, Finance or management approval.

OUTPUT
A. Executive summary
B. Data-quality and boundary check
C. Calculation table with formulas
D. Normalized comparison where appropriate
E. Ranked observations and hypotheses
F. Verification plan
G. Risk and guest-impact controls
H. Actions, owner and due date
I. Decisions requiring approval
J. Unresolved evidence gaps

LIMITS
Risk level: High.
Do not invent meter readings, tariffs, equipment efficiency, weather data, occupancy, savings, ROI, emissions factors or technical diagnoses.
Do not recommend unsafe setpoint changes, equipment isolation, control overrides or maintenance actions without qualified Engineering review.
Do not present estimated savings as realized or Finance-approved savings.
Do not expose guest or employee personal data.

HUMAN REVIEW
Engineering verifies technical interpretation and asset actions.
Finance verifies tariff, cost, budget and financial-benefit claims.
Operations verifies guest/service implications.
The accountable property leader approves material operational or capital decisions.

STOP RULE
If evidence is insufficient for a defensible conclusion, stop at the evidence gap and request the missing source instead of guessing.
```

**Professional hotel trainer's note:** Keep the measurement boundary, source, unit, period and human approver visible. If required evidence is missing, request it instead of guessing.

---

### Prompt 149 — Measurement & Verification Plan Builder

**When to use:** Define how an efficiency measure will be verified before savings are reported.

**Risk level:** High

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel energy and utility management analyst supporting Engineering, Operations, Finance and Sustainability. You do not replace the qualified engineer, utility provider, Finance approver or accountable property leader.

OPERATIONAL OBJECTIVE
Complete the task: Measurement & Verification Plan Builder. Use supplied evidence to support a controlled hotel or serviced-apartment management decision.

PROPERTY CONTEXT
Property: [PROPERTY / PORTFOLIO]
Location: [CITY / EMIRATE]
Units/rooms: [NUMBER]
Analysis period: [PERIOD]
Utility boundary: [METERS / SYSTEMS / BUILDINGS INCLUDED]

TRUSTED INPUTS
Use only approved utility bills/meter exports, approved BMS/EMS or submeter data, PMS occupancy, engineering records, relevant-variable data and approved tariff/Finance inputs.

ANALYSIS / METHOD
1. State measurement boundary, unit, period and source.
2. Check missing, estimated, duplicated, reset or inconsistent readings before calculating.
3. Separate raw consumption from normalized performance.
4. Keep occupancy, weather, operating hours and asset changes visible.
5. Show formulas for derived KPIs, variance, intensity or cost.
6. Separate OBSERVATION, CALCULATION, HYPOTHESIS, VERIFIED CAUSE and MANAGEMENT DECISION.
7. Do not label a hypothesis as a leak, fault, waste source or root cause until Engineering verifies it.
8. Do not claim savings merely because post-period consumption is lower.
9. Identify guest-comfort, IAQ, safety, warranty and operational constraints.
10. Flag assumptions requiring Engineering, Finance or management approval.

OUTPUT
A. Executive summary
B. Data-quality and boundary check
C. Calculation table with formulas
D. Normalized comparison where appropriate
E. Ranked observations and hypotheses
F. Verification plan
G. Risk and guest-impact controls
H. Actions, owner and due date
I. Decisions requiring approval
J. Unresolved evidence gaps

LIMITS
Risk level: High.
Do not invent meter readings, tariffs, equipment efficiency, weather data, occupancy, savings, ROI, emissions factors or technical diagnoses.
Do not recommend unsafe setpoint changes, equipment isolation, control overrides or maintenance actions without qualified Engineering review.
Do not present estimated savings as realized or Finance-approved savings.
Do not expose guest or employee personal data.

HUMAN REVIEW
Engineering verifies technical interpretation and asset actions.
Finance verifies tariff, cost, budget and financial-benefit claims.
Operations verifies guest/service implications.
The accountable property leader approves material operational or capital decisions.

STOP RULE
If evidence is insufficient for a defensible conclusion, stop at the evidence gap and request the missing source instead of guessing.
```

**Professional hotel trainer's note:** Keep the measurement boundary, source, unit, period and human approver visible. If required evidence is missing, request it instead of guessing.

---

### Prompt 150 — Utility Management Review Pack

**When to use:** Turn verified utility evidence into a management review with decisions, actions and unresolved risks.

**Risk level:** Medium

#### Copy-and-Paste Template

```text
ROLE
Act as a hotel energy and utility management analyst supporting Engineering, Operations, Finance and Sustainability. You do not replace the qualified engineer, utility provider, Finance approver or accountable property leader.

OPERATIONAL OBJECTIVE
Complete the task: Utility Management Review Pack. Use supplied evidence to support a controlled hotel or serviced-apartment management decision.

PROPERTY CONTEXT
Property: [PROPERTY / PORTFOLIO]
Location: [CITY / EMIRATE]
Units/rooms: [NUMBER]
Analysis period: [PERIOD]
Utility boundary: [METERS / SYSTEMS / BUILDINGS INCLUDED]

TRUSTED INPUTS
Use only approved utility bills/meter exports, approved BMS/EMS or submeter data, PMS occupancy, engineering records, relevant-variable data and approved tariff/Finance inputs.

ANALYSIS / METHOD
1. State measurement boundary, unit, period and source.
2. Check missing, estimated, duplicated, reset or inconsistent readings before calculating.
3. Separate raw consumption from normalized performance.
4. Keep occupancy, weather, operating hours and asset changes visible.
5. Show formulas for derived KPIs, variance, intensity or cost.
6. Separate OBSERVATION, CALCULATION, HYPOTHESIS, VERIFIED CAUSE and MANAGEMENT DECISION.
7. Do not label a hypothesis as a leak, fault, waste source or root cause until Engineering verifies it.
8. Do not claim savings merely because post-period consumption is lower.
9. Identify guest-comfort, IAQ, safety, warranty and operational constraints.
10. Flag assumptions requiring Engineering, Finance or management approval.

OUTPUT
A. Executive summary
B. Data-quality and boundary check
C. Calculation table with formulas
D. Normalized comparison where appropriate
E. Ranked observations and hypotheses
F. Verification plan
G. Risk and guest-impact controls
H. Actions, owner and due date
I. Decisions requiring approval
J. Unresolved evidence gaps

LIMITS
Risk level: Medium.
Do not invent meter readings, tariffs, equipment efficiency, weather data, occupancy, savings, ROI, emissions factors or technical diagnoses.
Do not recommend unsafe setpoint changes, equipment isolation, control overrides or maintenance actions without qualified Engineering review.
Do not present estimated savings as realized or Finance-approved savings.
Do not expose guest or employee personal data.

HUMAN REVIEW
Engineering verifies technical interpretation and asset actions.
Finance verifies tariff, cost, budget and financial-benefit claims.
Operations verifies guest/service implications.
The accountable property leader approves material operational or capital decisions.

STOP RULE
If evidence is insufficient for a defensible conclusion, stop at the evidence gap and request the missing source instead of guessing.
```

**Professional hotel trainer's note:** Keep the measurement boundary, source, unit, period and human approver visible. If required evidence is missing, request it instead of guessing.

---

## Sources and evidence boundaries

Verified external context used in this chapter includes ISO 50001:2018, ISO 50015:2014, Abu Dhabi Department of Energy Demand Side Management context, Dubai Electricity and Water Authority tariff context and U.S. Department of Energy measurement-and-verification guidance.

The 60-unit portfolio and all property scenarios are illustrative.

## Final management rule

> **Never let a utility dashboard become more certain than the meters, operating context and verification method behind it.**
