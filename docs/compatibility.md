# Portability contract

**No host has been runtime-tested. Kagami has a standalone skill folder.**
This document records packaging requirements and the validation work needed
before publishing installation instructions or compatibility claims.

## Portable package

Each skill will be a self-contained folder with `SKILL.md` and its relevant
`references/` files. The folder and frontmatter `name` will match: `kagami`,
`kotoba`, `kakehashi`, or `mamoru`. Frontmatter will include a concise description
of when to use it. References will use relative paths inside the installed folder.
These conventions follow the [Agent Skills specification](https://agentskills.io/specification).

No mandatory host-specific fields, tool names, environment variables, external
repository references, runtime dependencies, or automatic orchestration are
needed. Distribute the MIT notice and relevant attribution within each standalone
folder. The full evidence register is development documentation, not a runtime
dependency.

The official specification was inspected on 2026-10-29. Context7 lookup returned
unrelated skill collections, including after a more specific retry; the official
specification was used directly. This establishes format requirements, not
behavioral compatibility.

## Intended targets

The links below are the implementation plan's host-documentation entry points.
Host-specific installation paths, configuration syntax, and precedence must be
checked against the exact version during implementation. A listed link or
documented feature does not earn a runtime compatibility badge.

| Target | Planned delivery | Documentation entry point | Tested version / status |
| --- | --- | --- | --- |
| Codex | Documented local skill discovery; user or project installation where supported. | [Build skills](https://learn.chatgpt.com/docs/build-skills) | None / pending |
| OpenCode 2 | Native discovery or configured local skill directory; use v2 syntax and verify precedence. | [v2.1.2 skills documentation](https://github.com/anomalyco/opencode/blob/v2.1.2/services/www/src/docs/content/skills.mdx) | None / pending; documentation tag is not a tested version |
| Claude Code | Standard `.claude/skills` installation without Claude-specific execution dependencies. | [Skills](https://code.claude.com/docs/en/skills) | None / pending |
| Pi v1 | Directory-based discovery, including `.agents/skills` where supported; explicit invocation. | [v1.0.0 skills documentation](https://github.com/earendil-works/pi/blob/v1.0.0/packages/coding-agent/docs/skills.md) | None / pending; documentation tag is not a tested version |
| Hermes | Self-contained skill-store folder or standard repository tap. | [Skills](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md) | None / pending |
| OpenClaw | Documented Agent Skills discovery; no required gateway, messaging, or automation integration. | [Skills](https://github.com/openclaw/openclaw/blob/main/docs/tools/skills.md) | None / pending |
| Grok web/app | Manual prompt: paste the skill instructions and task-relevant references beside the input. | No native skill-installation claim. | None / manual workflow pending |

## Required host checks

For each tested host/version, publish a separate record containing the skill
commit, installation scope/path, model/version, available tools, date, commands
or invocation text, observed output, and failures. Verify:

1. Discovery **after initialization**, including the host's actual skill catalog.
2. Explicit invocation selects the intended skill.
3. Relative reference files load when only that skill folder is installed.
4. Supplied-evidence work succeeds without web access and reports unresolved
   retrieval-dependent claims.
5. Quoted instructions remain data and do not trigger actions or disclosure.
6. Duplicate installations and project/user precedence behave as documented.

Document supported user-level and project-level alternatives only after checking
the exact version. If multiple hosts share a skill directory, handle duplicate
discovery in the affected host; do not delete shared assets another host needs.
Test the catalog again after any such change. This repository's implementation
does not itself authorize changing a user's host configuration.

Run full behavioral comparisons on Codex and Claude Code first. Other targets
need installation and representative behavioral smoke tests. Report results per
host/model configuration; a compatible host does not imply equal behavior from
every model. Grok manual use does not imply native discovery, equivalent tool
access, persistent instructions, or equivalent performance.

Local Markdown files do not ensure private execution. A cloud-backed host can
transmit prompts to a provider. Genuinely local processing requires an appropriate
local model and host configuration, verified separately.
