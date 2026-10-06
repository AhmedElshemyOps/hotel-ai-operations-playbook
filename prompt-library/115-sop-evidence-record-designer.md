# Prompt 115 — SOP Evidence Record Designer

**Prompt ID:** `12-05-sop-evidence-record-designer`

**Risk level:** Medium

## When to use

Define the minimum evidence needed to prove critical hotel process steps without creating unnecessary paperwork or privacy exposure.

## Required inputs

- critical process steps
- risk/control points
- systems used
- existing forms/records
- retention/privacy requirements

## Expected outputs

- step-to-evidence matrix
- system-of-record recommendation
- missing record gaps
- privacy minimization notes
- retention/ownership questions

## Copy-ready prompt

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

## Human review

This output remains a draft until the accountable process/document owner validates it against approved sources and releases it through document control.
