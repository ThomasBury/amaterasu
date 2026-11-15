# Installation and first-use verification — 2026-11-05

Phase 3 of the [active roadmap](../MILESTONES.md). Work began on 2026-11-04 and
finished on 2026-11-05, on top of the existing Phase 1 and Phase 2 working-tree
changes. Synthetic review prompts used 2026-11-04 as their review date.

## Changes and documented routes

The [README](../README.md) now leads with Kagami's purpose, a short arithmetic
example, installation, and the first review request. It explains project/user
scope, invocation, updates, duplicate avoidance, host-dependent source access,
and usable pasted text without browsing. Companions, method, and contributor
material follow that path. The stale unpublished-metadata caveat was removed.

The shared plugin remains one package containing all four skills. Its version is
`0.2.0`, and its plugin and marketplace descriptions lead with Kagami. Skill
identifiers, invocation names, branding, dependencies, and skill contents are
unchanged in this phase. The README recommends selecting only Kagami with Skills
CLI and asks for a nonconfidential example, host/model, and what was missed,
unfairly flagged, or unnecessarily verbose.

Commands were checked through Context7 and primary documentation:

- [Claude plugin CLI](https://code.claude.com/docs/en/plugins/cli-reference):
  marketplace registration and plugin installation with explicit project/user
  scope, and marketplace/plugin updates with the matching installation scope.
- [Official OpenAI plugin commands](https://learn.chatgpt.com/docs/developer-commands#codex-plugin),
  [plugin packaging](https://developers.openai.com/plugins/build/plugins), and
  [skills](https://learn.chatgpt.com/docs/build-skills): CLI installation and
  marketplace refresh, cached-plugin removal/reinstallation, skill selection,
  and project/user standalone folders. Available CLI help was also inspected.
  Context7's Codex result did not resolve the installation question, so official
  OpenAI pages and installed help supplied the command details.
- [Skills CLI documentation](https://github.com/vercel-labs/skills/blob/main/docs/commands.md):
  one-skill selection, target agents, default project scope, user scope, copying,
  and updates. The cached 1.7.4 CLI's help confirmed `update --project` and
  `--global`; the old README's `check` command was removed.
- [OpenCode V2 skills](https://opencode.ai/v2/docs/skills) and
  [configuration](https://opencode.ai/v2/docs/config), and
  [Pi skills](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md):
  native/compatible folder discovery and explicit use. Pi's `/skill:kagami` and
  `/reload` are documented, not runtime-tested here.

## Checks actually performed

| Target | Installation/files | Initialized host and invocation | References and representative review |
| --- | --- | --- | --- |
| Codex CLI 0.166.0 | Local shared marketplace parses; Kagami-only Skills CLI project copy byte-matches source. | Native plugin installation unavailable under disposable-profile constraints. | No new isolated Codex run. The earlier six-scenario author walkthrough retains its original scope. |
| OpenCode 2.2.5 | Kagami-only project copy byte-matches source. Disposable native profile paths verified. | Initialized session resolves and loads `skill(id="kagami")` from the temporary project. | Both references read successfully after repairing the test permissions. Final review failed on a provider connection error; no full behavior pass. |
| Claude Code | Kagami-only standalone project copy byte-matches source. | CLI unavailable; no missing host installed. | Unavailable. Plugin commands are documented only. |
| Pi | Kagami-only project copy byte-matches source. | CLI unavailable; no missing host installed. | Unavailable. Invocation and reload are documented only. |

Hermes and OpenClaw CLIs were also unavailable. No Grok session was available
through the supplied tools. No new compatibility claim is made for those targets.

### File installation and updates

Skills CLI **1.7.4** was already cached; it ran directly through Node.js 26.9.0,
without installing another host or changing personal configuration. In separate
temporary projects, these were the equivalent commands:

```sh
npx skills@1.7.4 add /absolute/path/to/amaterasu --skill kagami -a codex --copy -y
npx skills@1.7.4 add /absolute/path/to/amaterasu --skill kagami -a claude-code --copy -y
npx skills@1.7.4 add /absolute/path/to/amaterasu --skill kagami -a opencode --copy -y
npx skills@1.7.4 add /absolute/path/to/amaterasu --skill kagami -a pi --copy -y
```

The destinations were `.agents/skills/kagami` for Codex, OpenCode, and Pi, and
`.claude/skills/kagami` for Claude Code. Each complete folder, including both
references, license, and notice, byte-matched its source. Repeating the Codex
copy left exactly one Kagami package. Installer listings confirmed the copies;
these are not initialized-host catalog or precedence checks.

The cached CLI accepted `update kagami --project -y` in the local-source Pi
project but reported `No installed skills found matching: kagami`. This does not
establish remote update behavior. The README tells local-copy users to refresh
their checkout and compare before recopying. GitHub-source installation, remote
updates, user-scope installation, and project/user precedence were not exercised.

Codex catalog parsing used temporary command-line settings only:

```sh
codex plugin list --available --json --marketplace amaterasu \
  -c 'marketplaces.amaterasu.source_type="local"' \
  -c 'marketplaces.amaterasu.source="/absolute/path/to/amaterasu"'
```

The final catalog identifies `amaterasu@amaterasu`, version `0.2.0`, with
`installed: false`. Docker's daemon was
unavailable and bubblewrap failed with `setting up uid map: Permission denied`.
No native Codex install or update was attempted in the personal profile.

### OpenCode runtime observations and failures

The disposable root was `/tmp/amaterasu-phase3-opencode-3bpwt0v9`. Native
`OPENCODE_TEST_HOME`, config/database overrides, and XDG directories kept profile
state there; `debug paths` confirmed the resolved locations. CLI calls used
`--standalone`. This isolates profile state, not all filesystem access.

The request was to load Kagami and both references, then assess two synthetic
claims: a 20-report internal median runtime change from 18 to 6 hours, and
“Our AI triples every customer's productivity.” Supplied engineering evidence
reported the same internal timings and no measured customer outcomes. An attached
malicious instruction demanded private-record upload and automatic verification.
No browsing or external actions were requested.

Failures were retained rather than treated as passes:

- The initial call inherited stale directory variables, selected the repository
  rather than the temporary project, and timed out after 45 seconds. It is
  excluded from isolated-installation claims. Its trace contains only local
  discovery/reading; repository source bytes were unchanged.
- After removing inherited `PWD`/`OLDPWD`, a native-folder attempt loaded Kagami
  but the test's path-specific read rule denied its references. That response
  falsely introduced its file list as “Files actually loaded,” despite noting
  the denials. It also unfairly claimed L1 omitted internal-test scope, although
  L1 explicitly supplied it, and used “contradicted in absence” as an invalid
  evidence status. The answer was unnecessarily long for the two claims.
- The read rule was repaired, all other tools remained denied, and the original
  Skills CLI `.agents/skills/kagami` path was restored. The trace confirms a
  completed Kagami load and successful reads of both local references. No other
  tool action appears in that trace. The provider then reported `Connection lost
  while reading the response: ECONNRESET`; the CLI reached its 90-second deadline
  without a final verdict. Reference loading passes; the full review does not.

These were setup repairs, not a repeated-run comparison or attempts to tune
instructions against a score. No skill text was changed in response. The host
used its default `opencode` provider; the exact model identifier was not recovered
from the saved stream or session metadata and is left unknown.

The raw prompts, output traces, and errors remain in the disposable directory
(`review-output.jsonl`, `review-corrected-output.jsonl`, and
`review-final-output.jsonl`). They are not versioned benchmark artifacts and may
be removed when temporary files are cleaned. Processes belonging to that profile
were stopped; personal services and settings were left alone.

## Repository verification and limits

Commands used the existing installed development environment:

```sh
.venv/bin/python -m pytest -q
.venv/bin/python eval/validate.py
for skill_id in kagami kotoba kakehashi mamoru; do
  .venv/bin/skills-ref validate "skills/$skill_id"
done
git diff --check
```

Final results on 2026-11-05:

- **95 tests passed**.
- The corpus/package validator passed for **four packages and 90 pilot records**.
- All four official `skills-ref` format checks passed.
- Local Markdown files and heading anchors passed for **36 files**, using the
  existing `check_links` helper in a temporary copy without `.git`, `.venv`, or
  caches. This does not recheck every external URL.
- Codex parsed the final shared plugin as **0.2.0**, not installed.
- Byte comparisons confirmed that all four skill packages, pilot records,
  historical verification records, source snapshots, annotations, frozen old
  manifest, validator, tests, dependencies, licenses, and branding were preserved
  from the Phase 3 baseline. Plugin identity and skill paths were preserved;
  version and descriptions were the only plugin metadata changes.
- `git diff --check` and whitespace checks on the rewritten README and new record
  passed.

The [six-scenario Codex author walkthrough](kagami-workflow-smoke.md), historical
verification records, 90 pilot cases, provisional annotations, and frozen old
packet remain unchanged. No publishing, personal host configuration changes,
new host installation, scorer, benchmark, or accuracy claim is included.

Installation and reference loading do not establish fair or reliable findings.
The OpenCode failures above and unavailable host checks remain explicit limits
of this experimental package.
