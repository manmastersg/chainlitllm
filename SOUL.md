# SOUL.md — Agent Operating Principles

## Code Change Protocol (MANDATORY)

**Before making ANY code changes**, the agent MUST:

1. **State the plan** — Describe exactly what files will be changed, what will be modified in each, and why.
2. **Seek explicit approval** — Ask the user for confirmation before proceeding. Do not proceed until the user says yes.
3. **Checkpoint first** — Create a git checkpoint (stash, commit, or tag) before touching any file, so changes can be cleanly reverted.

This applies to:
- Editing source files (.py, .tsx, .ts, .js, .css, .html, .json, .yaml, .toml, .cfg, .md, etc.)
- Creating or deleting files
- Running destructive or irreversible commands (rm, git reset --hard, pnpm build --force, etc.)

This does NOT apply to:
- Read-only operations (cat, grep, find, git log, git show, read_file, search_files, etc.)
- Navigating or inspecting the browser
- Running the dev server or test suites
