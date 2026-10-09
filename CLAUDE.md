# CLAUDE.md: Rules for Claude

## Rule 1: Keep PROJECT_CONTEXT.md current (highest priority)

`PROJECT_CONTEXT.md` is the single source of truth for this project.

**Before every new task**
- Read `PROJECT_CONTEXT.md` first. It should contain everything needed to start working: architecture, stack, key decisions, conventions, current status, and known constraints.
- Don't re-explore the whole codebase for things the context file already covers.

**After every major change**
- Update `PROJECT_CONTEXT.md` in the same task, before calling the work done.
- A "major change" includes: new feature or module, architecture or dependency change, new or changed API/contract/schema, config or deployment change, important bug fix with lessons, or a decision that affects future work.

**Keep it short and accurate**
- If something is removed, deprecated, replaced, or no longer used, delete it from the file. Don't leave it struck through or marked "old".
- Rewrite sections to describe the current state only, not the history. Git holds the history.
- Merge duplicate or overlapping points instead of appending new ones.
- Everything that matters must be in the file. Everything that doesn't should not be.
- Prefer concise bullets, exact names, paths, and commands over long prose.

**Suggested structure**
1. Project overview (what it is, goal)
2. Tech stack and versions
3. Architecture and folder map
4. Key decisions and conventions
5. Setup, build, test, and deploy commands
6. Current status and next steps
7. Known issues and constraints

---

## MinerCreator register rules

- Semantic V2 is fail-closed: `register-miner-v2.sh` / `register_gates_v2.py`. Never `cast send registerMiner` / `updateMiner` / `deregisterMiner` directly. Never `--skip-gates` / `--no-llm` / `ALLOW_UNSAFE_REGISTER` unless the user explicitly sets an emergency.
- Manual `set_sample_status.py approved` does **not** unlock gas.
- One miner = one publisher/source. Host YAMLs on Omni SSH (`upload-host.sh`); paste.rs off unless `ALLOW_PASTE_FALLBACK=true`.
- Cursor gate rule: `.cursor/rules/miner-register-gates.mdc` (repo root).
