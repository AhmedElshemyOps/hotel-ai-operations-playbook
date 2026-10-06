# The HOTEL Prompting Framework

The HOTEL framework is the shared control architecture for every prompt in this repository.

## H — Hospitality role & human owner
State the hotel role the AI is supporting and the human role that owns the decision. AI should never silently inherit authority.

## O — Operational objective & context
Define the property type, location, department, guest-journey stage, operating date or period, service conditions, constraints and decision required.

## T — Trusted inputs & sources of truth
List the systems and documents that may be relied on: PMS, RMS, CRS, CMMS, CRM, controlled SOP, finance ledger, approved rate sheet, inventory system, utility meter, guest-feedback platform or official source. Missing evidence stays missing.

## E — Expected output, exceptions & evidence
Specify the exact output format. Require confirmed facts, assumptions, recommendations and unresolved items to be separated. State what the AI must do when inputs conflict or an exception occurs.

## L — Limits, privacy & leadership approval
State prohibited actions and prohibited data. Define who verifies the result and who has authority to approve the final operational action.

## Minimum prompt acceptance test
A professional hotel prompt should answer: Who owns the task? What decision is being supported? What property context matters? Which sources are approved? What is missing? What format is expected? What exceptions require escalation? What may the AI not do? Who approves the result?

## Prompt lifecycle

1. Select a real operating task.
2. Map approved sources of truth.
3. Minimize sensitive data.
4. Build the HOTEL prompt.
5. Test normal and exception cases.
6. Challenge assumptions and authority.
7. Verify against systems of record.
8. Approve and version the prompt.
9. Monitor failures and revise.

## Risk classification

- **LOW:** content assistance with no direct operational commitment.
- **MEDIUM:** operational analysis, drafting or recommendations requiring verified inputs and human review.
- **HIGH:** financial, safety, privacy, employment, security, pricing or authority-linked support requiring stronger controls and qualified approval.
