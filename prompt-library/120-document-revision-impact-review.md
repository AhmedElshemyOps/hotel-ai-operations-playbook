# Prompt 120 — Document Revision Impact Review

**Prompt ID:** `12-10-document-revision-impact-review`

**Risk level:** High

## When to use

Assess the operational impact of a proposed SOP revision before release so dependent roles, systems, forms, training and KPIs are updated together.

## Required inputs

- current and proposed revisions
- change rationale
- linked documents/forms
- systems/workflows
- training and authority dependencies

## Expected outputs

- change-impact matrix
- affected roles/systems
- training updates
- dependent-document actions
- release/withdrawal checklist

## Copy-ready prompt

```text
ROLE
Act as a senior hotel process-design and quality analyst supporting an accountable human process owner.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Process Owner / Quality Manager / Department Head / Supervisor / Other]
Accountable human owner/approver: [Insert authorized role]
Document owner: [Insert role]
Authority/delegation source: [Insert approved matrix/policy or mark missing]

O — OPERATIONAL OBJECTIVE & CONTEXT
Objective: Assess the operational impact of a proposed SOP revision before release so dependent roles, systems, forms, training and KPIs are updated together.
Property type/location: [Insert confirmed property and jurisdiction]
Department/process: [Insert]
Document level: [Policy / SOP / Work Instruction / Checklist / Form]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Use only current and approved information. Provide the current and proposed revisions, change rationale, linked documents/forms, affected systems/workflows, training requirements and authority dependencies.
If an essential input is missing, stale or contradictory, place it in a DESIGN GAP section. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return a change-impact matrix, affected roles/systems, training updates, dependent-document actions and a release/withdrawal checklist.
Separate confirmed facts, proposed design, assumptions, gaps and human decisions required.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not approve the revision. Identify impacts and decisions for the document owner and authorized approver.
Do not independently create legal, safety, security, financial, compensation, pricing, employment or regulatory authority.
The output remains a draft until the authorized document approver releases the controlled revision.
```

## Human review

The process/document owner must verify the revision impact, dependent documents, training, systems and withdrawal plan before release.
