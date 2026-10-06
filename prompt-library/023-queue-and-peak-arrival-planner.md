# Prompt 023 — Queue and Peak Arrival Planner

**Article:** 03 — Front Office AI Toolkit  
**Status:** Complete  
**Version:** 0.11.0

**Risk:** Medium  
**When to use:** Before a forecast arrival peak, group movement or high-occupancy check-in window.  
**Human owner/approver:** Front Office Supervisor / Duty Manager

**Required inputs**
- arrival counts by time window
- desk staffing
- confirmed room readiness
- known groups/priority arrivals
- approved average processing assumptions if available

**Expected output**
- pressure-window table
- staffing/flow recommendations
- arrival dependencies
- contingency triggers

```text
H — HOSPITALITY ROLE & HUMAN OWNER
Act as a front-office operations support analyst for a hotel or serviced-apartment property.
Supported role: [Front Office Agent / Supervisor / Duty Manager]
Accountable owner: [Front Office Supervisor / Duty Manager]

O — OPERATIONAL OBJECTIVE & CONTEXT
Analyze the arrival pattern and prepare a peak-arrival operating plan. Use ranges when precise waiting-time evidence is unavailable.
Property: [type and location]
Operating date/time: [confirmed period]
Guest-journey stage: [pre-arrival / arrival / in-stay / departure]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only the supplied approved records. Relevant sources may include PMS/reservation record, approved housekeeping room status, CMMS close-out, guest-request system, approved policy/SOP, transport confirmation and authorized management instruction.

If a critical field is missing, stale or contradictory, do not guess. Mark it UNVERIFIED, name the source/owner needed, and state the next verification action.
Minimize personal data. Do not request or reproduce passport/ID numbers, full payment-card data, credentials, unnecessary contact data or unrelated sensitive notes.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return the requested operational output with four labels where relevant:
CONFIRMED FACT
REQUEST / PREFERENCE
UNRESOLVED / DEPENDENCY
RECOMMENDED ACTION

For every unresolved operational item show owner, next action, deadline/checkpoint and escalation condition.
pressure-window table
staffing/flow recommendations
arrival dependencies
contingency triggers

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not fabricate queue times or direct staff changes outside the manager’s authority.
Do not alter PMS status, reservation, payment, room assignment, guest entitlement or official record.
Do not invent times, prices, availability, benefits, compensation or policy.
Output is a draft until verified by Front Office Supervisor / Duty Manager.
```
