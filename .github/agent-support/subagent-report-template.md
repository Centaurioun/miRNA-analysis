# Subagent Report Template

Use this template when an orchestrator asks a subagent to persist a structured report for auditability and handoff quality.

## Metadata

- Report ID:
- Task slug:
- Run ID:
- Parent run or orchestration ID:
- Attempt number:
- Agent:
- Delegated by:
- Workstream or role:
- Execution start:
- Execution end:
- Status: `completed` / `partial` / `blocked`
- Confidence: `high` / `medium` / `low`
- Freshness status: `current` / `superseded` / `draft`
- Supersedes:
- Superseded by:
- Requested report path:
- Report file creation verified by orchestrator: `yes` / `no` / `unknown`

## Objective and Scope

- Objective:
- In scope:
- Out of scope:

## Execution Outcome

- Requested task:
- Actual task completed:
- Completion status:
- What was not completed:
- Why not completed:

## Inputs Used

- Files inspected:
- Requested but unavailable files:
- Prompts or instructions:
- Tools:
- Requested but unavailable tools:
- Environment constraints:
- Assumptions:
- Fallbacks used:
- Related reports:

## Evidence References

- File reference 1:
- File reference 2:

## Key Findings

- Finding 1:
- Finding 2:

## Decisions Made

- Decision:
  - Rationale:

## Evidence Quality

- Strongest evidence used:
- Weakest evidence relied upon:
- Confidence by major finding:

## Outputs Produced

- Files written:
- Files proposed but not written:
- Handoff owner:
- Ready for agent closure after output capture: `yes` / `no`

## Open Issues and Risks

- Risk 1:
- Risk 2:

## Recommended Next Actions

- Action 1:
- Action 2:

## Escalations Needed

- What the main AI or orchestrator must still decide:

## Short Summary for Main AI

- Bullet 1
- Bullet 2
- Bullet 3

## Report Lifecycle

- Review needed by:
- Notes on freshness or supersession:

## Report Hygiene Rules

- One report file per agent or role
- Do not append to another agent's report
- If the task changes materially, create a new report instead of silently mutating an old one
- If the task is complete and outputs are captured, the delegating orchestrator or main AI should close the finished agent instead of leaving it open by default
