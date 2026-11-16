# Installation and maintenance

For one installation route and a first review on each host, start with the
[README](../README.md#install). Choose one route per host. The Claude Code and
Codex plugins include all four skills.

## Claude Code plugin

For user-wide availability, substitute `--scope user` on both installation
commands in the README. Use the matching scope when you update. For a project
installation, run these commands in that project.

```sh
claude plugin marketplace update amaterasu
claude plugin update amaterasu@amaterasu --scope project
```

Start a new session after updating. Third-party marketplace auto-update is
optional. [Claude Code plugin commands](https://code.claude.com/docs/en/plugins/cli-reference)

## Codex plugin

For a manual update, refresh the marketplace and reinstall the cached plugin.

```sh
codex plugin marketplace upgrade amaterasu
codex plugin remove amaterasu@amaterasu
codex plugin add amaterasu@amaterasu
```

Start a new session after updating. Use a standalone skill for a project-only
installation. [Codex plugin commands](https://learn.chatgpt.com/docs/developer-commands#codex-plugin)
and [plugin guide](https://developers.openai.com/plugins/build/plugins).

## Standalone skills

The [Skills CLI](https://github.com/vercel-labs/skills) requires Node.js and npm.
The README shows project installations for OpenCode and Pi. Substitute
`-a codex` or `-a claude-code` for standalone installations in those hosts.
Add `-g` for a user installation or `--copy` for an editable copy. In Claude Code,
invoke the standalone skill with `/kagami`.

Compare and save local edits before updating a project installation.

```sh
npx skills@latest update kagami --project
```

Use `--global` in place of `--project` for a user installation. For a local
checkout or manual copy, update the checkout and compare the installed folder
with the new version before copying it again.

## Manual installation

Clone the repository or [download the ZIP](https://github.com/ThomasBury/amaterasu/archive/refs/heads/main.zip).
Copy the entire skill folder, such as `skills/kagami/`, into the appropriate
location. Keep `SKILL.md`, `references/`, `LICENSE`, and `NOTICE.md` together.

| Host | Project folder | User folder |
| --- | --- | --- |
| Codex | `.agents/skills/` | `~/.agents/skills/` |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| OpenCode | `.agents/skills/` | `~/.agents/skills/` |
| Pi | `.agents/skills/` | `~/.agents/skills/` |

## Find a missing or duplicate skill

- Start a new session after installation or updates. In Pi, you can use `/reload`.
  See [OpenCode skills](https://opencode.ai/v2/docs/skills) and [Pi skills](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md).
- For a project installation, start in that project. If a standalone skill is
  missing, check its destination and confirm that the complete folder was copied.
- If Kagami appears twice, check for a plugin and a standalone copy, or for both
  project and user copies. When hosts share a skill folder, adjust discovery in
  the affected host to preserve the copy used by the other host.

The installation record distinguishes a successful file copy from discovery and
use in an initialized host. See [tested versions and results](../eval/first-use-verification.md)
and the [portability contract](compatibility.md).
