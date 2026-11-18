# Validation and installation verification — 2026-11-18

[Phase 6](../MILESTONES.md#phase-6--automate-validation-and-verify-installation)
was checked on Linux with Git 2.53.0, uv 0.12.15 and CPython 3.11.10. The
validation snapshot included the working-tree changes on base `e336c1f`.
Installation tests used the public GitHub source.

## Repository checks

`sh eval/check.sh` passed in a clean temporary Python environment built from
`uv.lock`: 95 pytest tests, four skill packages, 90 pilot cases, repository
Markdown links and anchors, and all four `skills-ref` checks. Local staged and
unstaged whitespace checks passed. `sh -n eval/check.sh` and `actionlint` 1.7.12
passed. The GitHub-hosted workflow remains unrun. Its pull request job compares
the tested merge commit with its first parent, and its `main` push job compares
the new tip with the previous tip.

A new clone of a disposable commit containing the changes used
`git clone -c core.autocrlf=true`. An ordinary Markdown file checked out as
CRLF. All 228 pilot JSON and text files retained LF and matched the base blobs
byte-for-byte. An initial run found that the check script also needed LF, which
is now pinned in `.gitattributes`. The fresh checkout passed this command:

```sh
LC_ALL=C LANG=C PYTHONCOERCECLOCALE=0 PYTHONUTF8=0 sh eval/check.sh HEAD^
```

Python 3.11 reported `ANSI_X3.4-1968` with UTF-8 mode disabled before running
the command. The pinned `skills-ref` failed to decode Kagami under that setting
on its own. The check command enabled UTF-8 mode for all Python checks.

In the disposable clone, appending bytes to `pilot-kagami-011.txt` produced
`Hash mismatch: pilot-kagami-011.txt` from the validator. An untracked Markdown
file with a broken heading link produced `Missing anchor: #absent`. Trailing
whitespace separately failed in the unstaged, staged, and committed checks.
The original pilot files, recorded hashes, and dated verification records were
preserved.

## Public GitHub installations and updates

GitHub `main` resolved to `e336c1f930cc37ae8cb9c48905c359b0c870fb15`. Clean
profiles and projects used temporary directories. Codex's active profile path
was mounted over with a disposable directory in a separate mount namespace.
The Skills CLI and OpenCode ran in disposable projects. GitHub install and
update commands ran from those profiles and projects.

| Target and version | Clean installation | Discovery | Invocation | Reference loading | Public update |
| --- | --- | --- | --- | --- | --- | --- |
| Codex CLI 0.169.0 | Shared plugin v0.3.0. All four skill folders matched `main`. | Initialized `skills/list` returned four `amaterasu:*` skills. | The `$amaterasu:kagami` prompt targeted the installed skill. | Both references loaded via a two-file read-only tool after the nested shell sandbox failed. The review corrected the arithmetic. | Marketplace upgrade and reinstall completed. Installed payload bytes were identical before and after. |
| Claude Code | CLI unavailable. Shared-plugin route outstanding. | Outstanding. | Outstanding. | Outstanding. | Outstanding. |
| OpenCode 2.3.0 | Standalone Kagami matched `main`. | The standalone runtime resolved Kagami from the project. | `skill` completed with ID `kagami`. | Both reads completed with project reads allowed. The review distinguished a 1-percentage-point drop from a 50% relative drop. | Skills CLI reported up to date. Installed bytes were identical. |
| Pi | Skills CLI installed only Kagami and its files matched `main`. Pi CLI unavailable. | Outstanding. | Outstanding. | Outstanding. | Skills CLI reported up to date. Installed bytes were identical. |

The commands below use Skills CLI 1.9.0, the version returned by npm for
`@latest` during the check, with Node.js 26.9.0 and npm 11.20.0. The test
ran the npm-installed CLI entry point directly with the same arguments. `-y`
let the installer run unattended.

```sh
codex plugin marketplace add ThomasBury/amaterasu
codex plugin add amaterasu@amaterasu
codex plugin list --json --marketplace amaterasu
codex plugin marketplace upgrade amaterasu
codex plugin remove amaterasu@amaterasu
codex plugin add amaterasu@amaterasu

# In separate temporary projects
npx skills@1.9.0 add ThomasBury/amaterasu --skill kagami -a opencode -y
npx skills@1.9.0 add ThomasBury/amaterasu --skill kagami -a pi -y
# In each project
npx skills@1.9.0 update kagami --project -y
```

Public checks compared cached Codex skill folders and each standalone Kagami
folder with GitHub source bytes using `diff -qr`. SHA-256 digests for all Codex
payload files outside `.git` matched before and after the reinstall. Both
standalone locks recorded `main`'s commit and `skills/kagami/SKILL.md` as the
source path.

For the runtime review, both hosts received the fictional claim “Defects fell
from 2% to 1%, a 50-percentage-point decrease” and a request to read both
references. Codex used `codex exec --json --ephemeral --sandbox read-only`.
Shell reads failed inside the mount namespace, including on retry with the
legacy sandbox setting. A final attempt disabled shell tools and enabled a
disposable MCP reader limited to the two cached references. Its trace confirms
both reads and a completed review. Shell reference loading remains unverified.

OpenCode used `opencode --standalone run --format json`. The first attempt
resolved the skill but the path-specific test rule denied reference reads. A
new attempt allowed reads within the disposable project and continued to deny
external directory access, edits, shell commands, and web tools. Its trace
confirms both reference reads and a completed review.

## Controlled Git source update

A disposable bare repository started with `main` at public tag `v0.2.0`
(`d00f649ead578f1960aca583d70dedfa1f5c311e`). A test-only Git `insteadOf`
rule mapped `https://example.invalid/amaterasu.git` to the bare repository
via `file://`. Codex registered the Git URL with `--ref main`. Skills CLI
installed from the same Git URL with the other arguments above. Before the
update, all installed skill folders matched the `v0.2.0` tag.

The test moved the disposable `main` to `v0.3.0`
(`c1fdfe6c4297e9f67465bc74976c35164d97e6a2`) and ran the same update
commands as above. Codex reinstalled the shared plugin as `0.3.0`. The Skills
CLI updated both standalone copies and recorded the new commit in their lock
files. `SKILL.md` and `references/evidence-and-arguments.md` changed in the
installed Kagami packages and matched `v0.3.0`. Codex's installed plugin
manifest and all four skill folders also matched `v0.3.0`.

The verified public commands required no syntax changes. Phase 3's
[first-use record](first-use-verification.md) retains its original observations.
