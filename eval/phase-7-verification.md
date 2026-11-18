# Phase 7 comparison verification — 2026-11-18

[Phase 7](../MILESTONES.md#phase-7--compare-all-four-skills-with-an-ordinary-prompt)
compares one answer with and without the relevant skill for each of eight cases.
The [blinded review packet](phase-7-review.md) contains the prompts, eight answer
pairs, and the reviewer scorecard.

## Frozen inputs

Source excerpts retain their original line labels and wording. The chronology
case uses the original task and both excerpts from the regression. The seven
pilot prompts use the original tasks with the relevant audience and decision
context and a supplied-material-only limit. The two Mamoru evidence files match
the embedded source lines and are shown once. Pilot files and annotations were
preserved. Hashes cover the exact UTF-8 prompt bytes, including the final line
break, before any comparison run.

| Packet pair | Case | Prompt SHA-256 |
| --- | --- | --- |
| 01 | [pilot-mamoru-001](pilot/mamoru/inputs/pilot-mamoru-001.json) | `203d5173a6b74d2f067d81d952a8c6ef67ef4fbb9b9476da7a3e131bb28ba006` |
| 02 | [pilot-kagami-023](pilot/kagami/inputs/pilot-kagami-023.json) | `179a86e012fc5a83d1742dca88c04370772f36bbedad1acab61d96736705dc24` |
| 03 | [pilot-kotoba-003](pilot/kotoba/inputs/pilot-kotoba-003.json) | `57bda5c3b6405260ffd4a6807bbda6062dd2d7e208e1f4d21d8b7ecca8ab2f7f` |
| 04 | [Chronology regression](kagami-workflow-smoke.md#chronology-and-added-material) | `2dbe01c5acc4c41731c5e8a1c28a074154380294ef95341f454f0f7556709b6d` |
| 05 | [pilot-mamoru-012](pilot/mamoru/inputs/pilot-mamoru-012.json) | `7f6a2dc194843848d780c494d54fd21728040332d908659350554a9f666e9c3f` |
| 06 | [pilot-kakehashi-001](pilot/kakehashi/inputs/pilot-kakehashi-001.json) | `d94bf8f905624065d2b15020df94b6def1ee5397ed728cac9c87866facb3092a` |
| 07 | [pilot-kotoba-013](pilot/kotoba/inputs/pilot-kotoba-013.json) | `067866d0809a7765be2a9652a7de97e0debe76d8c3a41a51397918c8ab715365` |
| 08 | [pilot-kakehashi-017](pilot/kakehashi/inputs/pilot-kakehashi-017.json) | `8795321b8c98b0a4afdcd4981965a4c328500efa6f6cc2b35b9e8bddb4230ea2` |

## Run setup

The review packet uses Codex CLI 0.170.0 with `gpt-6.2-sol` at high
reasoning effort, matching the Phase 5 regression model and effort. Both
conditions use an ephemeral thread in an empty workspace with a disposable
Codex profile. The repository and personal skill directory are masked from the
process. The two conditions use the same user prompt bytes, read-only shell
sandbox setting, no approvals, and disabled shell, web search, plugins, and
connected apps.

Both conditions receive this developer instruction:

```text
The task and source excerpts are in the user message. Use only the supplied excerpts as evidence. Return the requested answer without referring to these instructions.
```

In the skill condition, the developer message also includes the tested skill's
`SKILL.md` and its packaged references. This tests the instructions
with their references already loaded. The Phase 6 record covers native
discovery and reference retrieval on available hosts. A separate one-word
control confirmed that the disposable profile could start a fresh thread and
apply a developer instruction. [Phase 6 verification](phase-6-verification.md)

## Codex generation and review status

All 16 authorized Codex sessions completed. The traces contain 16 unique
thread IDs, one completed turn per session, and zero tool calls. Both arms
of each pair received identical prompt bytes. One session emitted a progress
message before its final answer. The packet includes only the verbatim final
answers. Pair order and the A/B order within each pair were randomized
independently.

The original Codex CLI 0.169.0 runs completed, but recreating the local Python
environment removed their private condition key and traces. The replacement
runs used the same frozen prompt bytes, skill files, model, reasoning effort,
and isolation. The original packet is retained locally for reference.

The replacement key, traces, and skill hashes are in the local, ignored
`.phase7-private/` directory. Give the reviewer the packet alone. Its SHA-256
is `d6d6ea61454aed1c0ce4225f3a76801f21eb2c65d6f72aba0d18b945d7fb346c`.

| Skill | Complete pairs | Independent judgments |
| --- | --- | --- |
| Kagami | 2 of 2 | Pending |
| Kotoba | 2 of 2 | Pending |
| Kakehashi | 2 of 2 | Pending |
| Mamoru | 2 of 2 | Pending |

The criterion results, examples, regressions, and proposed wording depend on
the independent reviewer's judgments.

## NVIDIA SkillEvaluator

The agent skill and CLI 1.0.1 ran from a disposable workspace during the
original comparison. The recorded static results below use the
working-tree skill packages. [NVIDIA agent guide](https://docs.nvidia.com/skills/skillevaluator/agent-skill)

| Skill | Static quality | Keyless Tier 1 | Codex, Claude Code, OpenCode |
| --- | --- | --- | --- |
| Kagami | 87.0/100 (B) | Pass, 9 of 9 | Predicted to load on all three |
| Kotoba | 86.0/100 (B) | Pass, 9 of 9 | Predicted to load on all three |
| Kakehashi | 86.0/100 (B) | Fail, 8 of 9 | Predicted to load on all three |
| Mamoru | 86.0/100 (B) | Pass, 9 of 9 | Predicted to load on all three |

`tier1 <skill-dir> --no-llm` initially reported incomplete security checks when
its managed scanner process exited with code 2. The reruns pointed
`SKILLEVALUATOR_SKILLSPECTOR_PATH` to the executable built from the same pinned
SkillSpector 2.13.4 wheel and used Gitleaks 8.30.0. All applicable checks then
completed. The JSON reports were lost when the disposable workspace was removed.

SkillSpector flagged `Do not judge` across lines 66–67 of Kakehashi's reference
as a high-severity anti-refusal instruction. In context, the sentence says that
agreement or exact wording alone is a poor test of what a reader understood.
The skill also explicitly asks the assistant to retain important qualifications.
This appears to be a false positive. The table records the CLI's failure verdict.
[Flagged reference](../skills/kakehashi/references/audiences-and-meaning.md)

`quality-check` flagged long descriptions, missing in-package examples, and
missing recommended author and tag metadata in all four packages. It also
flagged Kagami's cross-link between references. Both files are directly linked
from Kagami's `SKILL.md`. The harness check uses versioned loader rules. Its
Codex 0.166.0 and OpenCode 1.19.5 profiles warned that the local versions
(0.169.0 and 2.3.0) differ from the profiled versions.

`tier3 validate --strict` passed for the four datasets in `datasets/` under
the disposable workspace. Each dataset contains the two frozen cases for that
skill and task checks written from the source excerpts. NVIDIA classifies the
coverage as provisional because its policy calls for at least 10 cases and one
case where the skill should stay inactive. The Phase 7 comparison uses the
eight cases specified in the milestone.

The Tier 2 and Tier 3 readiness checks found no model provider credential.
The Tier 3 check also found that Bubblewrap could not start inside the default
command sandbox. NVIDIA's matching live runs and judge did not run. The 16
answers above came from the separate Codex setup. [Provider requirements](https://docs.nvidia.com/skills/skillevaluator/configuration)

## Repository checks

`sh eval/check.sh` passed in a disposable locked Python 3.11.10 environment.
It ran 95 tests, validated four skill packages and 90 pilot cases, checked
repository Markdown links and anchors, and passed all four `skills-ref` checks.
Staged and unstaged whitespace checks passed. The pilot files match `HEAD`.
