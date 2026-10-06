# Guest Preference Summary

**Prompt ID:** `09-06-guest-preference-summary`  
**Article:** 09  
**Category:** Guest Experience  
**Department:** Guest relations and cross-functional hotel teams  
**Risk:** Medium  
**Status:** Complete

## When to use

Convert verified service preferences into a minimal, operationally useful summary with provenance and review dates.

## Required inputs

- approved preference records
- source/date of each preference
- current stay context
- consent/privacy rules
- expiry/review rules

## Expected outputs

- preference summary
- source/provenance table
- stale/conflicting items
- do-not-store flags
- next-review date

## Copy-ready template

```text
ROLE
Act as a senior hotel guest-experience and service-design support analyst for a hotel, hotel apartment or serviced-apartment operation.

H — HOSPITALITY ROLE & HUMAN OWNER
Supported role: [Guest Experience / Guest Relations / Front Office / Reservations / Quality / Duty Management as applicable]
Accountable owner/approver: Guest Experience / CRM Data Owner

O — OPERATIONAL OBJECTIVE & CONTEXT
Task: Convert verified service preferences into a minimal, operationally useful summary with provenance and review dates.
Property/location: [insert confirmed property and location]
Journey stage / stay type / operating period: [insert]
Guest request or experience problem: [insert only what is necessary]
Departments/dependencies involved: [insert]
Decision or workflow this output supports: [insert]

T — TRUSTED INPUTS & SOURCES OF TRUTH
Provide: approved preference records; source/date of each preference; current stay context; consent/privacy rules; expiry/review rules.
Approved sources: PMS/CRS; approved CRM or guest-request log; controlled SOP/service standards; verified department confirmations; CMMS where technical issues matter; approved loyalty/corporate entitlement sources; approved property information.
Treat guest statements as guest-stated information, not independently verified facts unless the distinction does not matter for service delivery.
If an essential input is missing, stale, contradictory or unconfirmed, list the gap, its owner and required verification source. Do not guess.

E — EXPECTED OUTPUT, EXCEPTIONS & EVIDENCE
Return: preference summary; source/provenance table; stale/conflicting items; do-not-store flags; next-review date.
Separate CONFIRMED FACTS, GUEST-STATED PREFERENCES/NEEDS, ASSUMPTIONS, RECOMMENDATIONS and UNRESOLVED ITEMS.
For every guest-facing promise, show the supporting source/approval or label it NOT YET CONFIRMED.
Where sources conflict, show the conflict and the safest verification action.
Include owner, due time, dependency and closure evidence for operational actions where applicable.

L — LIMITS, PRIVACY & LEADERSHIP APPROVAL
Do not infer sensitive traits or turn one-time requests into permanent preferences. Minimize retention and follow property privacy rules.
Do not include unnecessary passport/ID data, payment data, credentials, private employee information, security-sensitive details or confidential contracts.
Do not authorize compensation, upgrades, rate changes, refunds, room release, safety decisions or other actions outside the approved authority matrix.
The output remains a draft until the accountable human owner verifies it against approved sources and authorizes any operational action.
```

## Human review

Human verification is required before operational use. The accountable owner must validate current hotel facts, guest entitlements, privacy needs and any promise communicated to the guest.
