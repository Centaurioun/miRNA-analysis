# Agent Reports

Designated report-write location for MO and maintenance-orchestration subagents.

Purpose:

- let each subagent write its own markdown report into a defined directory
- preserve subagent findings for later reference when the main AI cannot directly inspect a child agent's full working context
- reduce loss of useful details when multiple subagents report back through summaries

This directory is not intended as a generic sink for any report created in the repository.

Recommended subdirectories:

- `recovery-maintenance/`
- `meta-orchestration/`

Recommended filename pattern:

- `YYYY-MM-DD_<run-id>_<agent-name>_<task-slug>_<status>.md`
