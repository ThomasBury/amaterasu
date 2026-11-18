# Portability contract

All four skills have standalone folders and shared Claude/Codex plugin metadata.
See the [latest installation verification](../eval/phase-6-verification.md) for exact
checks and unavailable runtime verification. The
[2026-10-30 installation record](../eval/installation-verification.md) remains
historical evidence for its tested versions. Installation does not establish
behavioral effectiveness.

## Portable package

Each skill is a self-contained folder with `SKILL.md` and its relevant
`references/` files. The folder and frontmatter `name` will match: `kagami`,
`kotoba`, `kakehashi`, or `mamoru`. Frontmatter includes a concise description
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

## Documented routes and tested status

The [README](../README.md#install) pairs installation with first use. The
[installation guide](installation.md) covers alternate scopes, updates, and
troubleshooting. The [installation verification](../eval/phase-6-verification.md)
records the commands tested against the public GitHub source and the runtime results.

| Target | Documented delivery | Documentation | Tested version / status |
| --- | --- | --- | --- |
| Codex | Shared plugin for the user; Skills CLI/manual project or user folders. | [Plugin commands](https://learn.chatgpt.com/docs/developer-commands#codex-plugin), [skills](https://learn.chatgpt.com/docs/build-skills) | CLI 0.169.0: public install, discovery, and update verified. Kagami review completed using a read-only reference tool because the nested shell sandbox failed. |
| Claude Code | Shared plugin with project/user scope; standalone folders. | [Plugin CLI](https://code.claude.com/docs/en/plugins/cli-reference) | Host unavailable. Shared-plugin installation and runtime checks outstanding. |
| OpenCode 2 | Skills CLI or native skill folders; no extension required. | [V2 skills](https://opencode.ai/v2/docs/skills) | CLI 2.3.0: GitHub install, discovery, invocation, reference reads, and update verified. |
| Pi | Skills CLI or native skill folders; `/skill:kagami`. | [Skills](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md) | GitHub install and update verified with Skills CLI. Pi runtime unavailable. |

Skills CLI **1.9.0** installed Kagami from GitHub into separate OpenCode and Pi
projects. Earlier [local-copy checks](../eval/first-use-verification.md) used
1.7.4. User-scope installation and project/user precedence remain untested.

Hermes, OpenClaw, and manual Grok use remain foundation-era intended targets.
No new compatibility or installation claim is made for them in this phase.

## Required host checks

For each tested host/version, keep a separate record containing the skill
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

Use the six-scenario manual review on Codex and one representative review for
each other available host, using isolated installations where supported. Mark
unavailable checks explicitly; do not install missing hosts to fill a table or
change personal configuration. Report results per host/model configuration;
a compatible host does not imply equal behavior from every model. Grok manual
use does not imply native discovery, equivalent tool access, persistent
instructions, or equivalent performance.

Local Markdown files do not ensure private execution. A cloud-backed host can
transmit prompts to a provider. Genuinely local processing requires an appropriate
local model and host configuration, verified separately.
