# Installation verification — 2026-10-30

This phase adds distribution metadata and documentation. It does not change the
four skills, pilot cases, or provisional annotations. No effectiveness result is
claimed. The next evaluation phase remains the bounded 12-input comparison.

## Tested configurations and results

| Check | Configuration | Result |
| --- | --- | --- |
| Shared marketplace and plugin manifest parsing | Codex CLI 0.165.0, local source | Pass: available `amaterasu@amaterasu`, version `0.1.0`, not installed |
| Skill discovery | Skills CLI 1.7.4, local checkout | Pass: exactly four skills |
| Project installation and listing | Skills CLI 1.7.4, target `codex` | Pass: four complete folders in `.agents/skills/` |
| Project installation and listing | Skills CLI 1.7.4, target `claude-code`, `--copy` | Pass: four complete folders in `.claude/skills/` |
| Package contents | Both installations | Pass: every installed file byte-matches its source, including references, licenses, and notices; no evaluation folder installed |
| Reinstallation | Both installations | Pass: exactly four destination folders remain |
| Selecting one skill | Skills CLI 1.7.4, target `codex`, `--skill kagami` | Pass: only Kagami installed |
| Update checking | Skills CLI 1.7.4, local source | Reports `No project skills to update`; reinstall the local source to refresh it |
| Native plugin installation, initialized host catalog, invocation, reference loading, offline supplied-evidence behavior, precedence, startup/manual updates | Codex | Pending: disposable profile isolation unavailable |
| Native plugin and behavioral checks | Claude Code | Pending: CLI unavailable; frozen transfer packet prepared |
| GitHub-source plugin install and remote updates | Both hosts | Pending: metadata has not been published in a GitHub revision |

Tests ran on Linux with Node.js 26.9.0 and npm through mise. The Skills CLI
listing is an installer catalog, not an initialized assistant's skill catalog.
Reinstallation without duplicate destination folders does not establish host
deduplication or project/user precedence.

Codex parsing used temporary command-line configuration, without adding a
marketplace to personal settings:

```sh
codex plugin list --available --json --marketplace amaterasu \
  -c 'marketplaces.amaterasu.source_type="local"' \
  -c 'marketplaces.amaterasu.source="/absolute/path/to/amaterasu"'
```

Skills CLI checks ran in fresh directories under
`/tmp/amaterasu-install-hcgq8u0w`. Substitute an absolute checkout path and run
each installation in a separate empty project:

```sh
npx --yes skills@1.7.4 add /absolute/path/to/amaterasu --list
npx --yes skills@1.7.4 add /absolute/path/to/amaterasu --skill '*' -a codex -y
npx --yes skills@1.7.4 list -a codex
npx --yes skills@1.7.4 add /absolute/path/to/amaterasu --skill '*' -a claude-code --copy -y
npx --yes skills@1.7.4 list -a claude-code
npx --yes skills@1.7.4 add /absolute/path/to/amaterasu --skill kagami -a codex -y
```

An assert-based smoke check compared the destination name sets and all source
file bytes for both four-skill installations, repeated each install, and checked
the single-skill destination. All assertions passed. Local-source installation
used copies on this tested CLI; the README does not promise a link strategy.

## Repository checks

Run the locked validator, pytest suite, four `skills-ref validate` commands from
the [evaluation guide](README.md#run-local-file-checks), and `git diff --check`.
The added packaging regression check rejects omitted or duplicated manifest
skill paths, broken standalone packages, missing license/notice files, and
inconsistent marketplace/plugin names or source root.

Results: validator passed for four packages and 90 pilot records; **92 pytest
tests passed**; all four `skills-ref` format checks passed; `git diff --check`
passed. A targeted link check verified 59 local file links/anchors across the
changed documentation and new verification/transfer instructions. Frozen packet
file hashes were checked against the working tree.

## Remaining host work

Docker's daemon was unavailable. A direct bubblewrap isolation probe failed with
`setting up uid map: Permission denied`. Full Codex plugin installation was
therefore not attempted in the personal profile. Catalog parsing passed; it must
not be reported as an installation or behavior pass. No model turn was run.

Use the [Claude transfer instructions](claude-installation-checks.md) and
[frozen file manifest](claude-installation-packet.json). The same isolated-host
checks are still needed for Codex, using its catalog picker and recorded exact
invocation. Run the supplied-evidence test without search tools, retaining
provider access only as required by the chosen model. A successful result is a
smoke test, not a blinded comparison or an effectiveness claim.

Plugin source `./` packages the repository root. Unlike standalone Skills CLI
installs, a plugin cache may include evaluation annotations. Future blinded
comparisons must use a minimal frozen package containing only skills and plugin
metadata, with labels kept inaccessible; do not point an evaluation assistant at
this full checkout or an unfiltered plugin cache.

The prepared transfer archive is `/tmp/amaterasu-claude-installation.zip` (21
files: the 19 frozen package files plus manifest and transfer instructions).
SHA-256: `ab151b530cc7fc32d9a1bfd1e5839cc4f9fc2c7ee154989a90d909f5f0742a0c`.
It contains no evaluation inputs or annotation records. The tracked manifest and
instructions remain available after temporary files are cleaned up; assemble a
new archive from those listed paths if needed and record its new archive hash.

No publishing, personal host configuration changes, SkillOpt integration,
automated scorer, full benchmark, or reader study was performed.
