# Agent Support Files

This directory stores shared support artifacts for workspace agents that should not themselves live in `.github/agents/`.

Current contents:

- `subagent-report-template.md` for structured orchestration reports
- `reports/` as the designated write location for MO and maintenance-orchestration subagent report files

Notes:

- Agents in `.github/agents/` may reference files here.
- The `reports/` directory exists so subagents have a defined place to persist their own markdown reports for auditability and later reference by the main AI.
- This directory is for shared support material, not agent definitions.
