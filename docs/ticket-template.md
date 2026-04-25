# Argon Player Ticket Template

Use this template for each implementation ticket.

## 1) Ticket Header
- **ID:** AP-XXX
- **Title:**
- **Priority:** P0 / P1 / P2
- **Status:** Todo / In Progress / Blocked / Done
- **Depends on:**
- **Owner:** AI Agent (+ human reviewer)

## 2) Objective
Describe the user or system outcome this ticket should deliver.

## 3) Scope
### In scope
- 
- 

### Out of scope
- 
- 

## 4) Implementation Notes
- Key files/modules expected to change:
- Architectural considerations:
- Risk areas:
- Assumptions being made (explicitly list):
- Abuse/failure cases considered:

## 5) Acceptance Criteria (Done when)
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3
- [ ] Includes explicit degraded-mode behavior for at least one failure path

## 6) Test/Verification Plan
List explicit commands and expected outcomes.

- [ ] `command_here`
- [ ] `another_command_here`
- [ ] Negative-path check (error, timeout, or unavailable dependency)

## 7) Deliverables
- Code changes:
- Docs updates:
- Config/migration impact:

## 8) Rollback Plan
How to safely revert if issues are discovered.

## 9) Telemetry / SLO impact
- Metrics/logging added or changed:
- Expected impact on v1 SLOs:
- Dashboard/alert updates required:

## 10) AI Run Log
### Prompt used
```
(paste implementation prompt)
```

### Summary of changes produced by AI
- 
- 

### Human review notes
- 
- 

## 11) Completion Checklist
- [ ] Dependencies satisfied
- [ ] Acceptance criteria met
- [ ] Tests/checks passed
- [ ] Docs updated
- [ ] Ready for merge
