# Kagami phase verification — 2026-10-29

## Scope decision

Implement milestone 2 alone. Kagami has an independent contract, standalone
references, and its own 20-case pilot. Kotoba, Kakehashi, and Mamoru require
separate instructions and cases; grouping them would not resolve a Kagami
dependency. Release validation needs independent humans and isolated host runs
and cannot be inferred from artifact checks.

## Artifacts and reproduction

The [skill](../skills/kagami/SKILL.md) embeds the shared essentials verbatim.
It reads supplied evidence first and bounds public research to three unresolved
consequential claims with two queries each before reporting remaining gaps.
Its two local references, attribution, and license travel with the folder.

Run from the repository root:

```sh
uv sync --locked
uv run --locked python eval/validate.py
uv run --locked pytest -q
uv run --locked skills-ref validate skills/kagami
```

Verified using uv 0.12.15, CPython 3.15.0, pytest 9.2.0, and skills-ref 0.1.0 at
revision `69ef37e9424c0a7ea9dd2293b559e43ec8176379` (see `uv.lock`).
The 23 tests pass. Package format validation and corpus validation pass.
An isolated temporary copy of only the skill folder loads both references and
passes format/link checks without repository documentation. Missing references
and shared-rule drift cause failures. This is file loading, not host discovery.

Tests exercise altered/missing evidence, path traversal and symlink escape,
duplicate IDs, missing records, invalid evidence relationships, false independent
annotation state, and variant clustering. Numerical checks use exact rational
arithmetic: 8% → 6% is 2 percentage points or 25% relative; 10/1000 and 20/2000
both equal 1%; percentage growth from zero is undefined. These checks verify
fixture calculations, not a model's ability to perform them.

## Pilot layout and author walkthrough

[pilot/kagami/manifest.json](pilot/kagami/manifest.json) records original synthetic
AI authorship, MIT rights, dates, scenario families, and input hashes.
[pilot/kagami/evidence.json](pilot/kagami/evidence.json) records source identity,
origins, availability, locations, rights, and exact artifact hashes. None of the
scenarios describes a real person, product, or study result. Unknown retrieval
dates are explicit because synthetic sources were not retrieved.

Inputs and annotations occupy separate directories. Each input's `input` map
retains original text at stable line locations. Author annotations are drafts,
not independent human labels or observed model outputs. Do not expose the
annotation directory, manifest categories, this record, or repository tests to
a model during evaluation. A future runner must copy only the selected input,
permitted evidence records/artifacts, and skill into an isolated workspace;
separate directories within a browsable repository are not sufficient isolation.

Author review checked all 20 cases against the skill and provisional keys:

| Cases | Review result / expected boundary |
| --- | --- |
| 001–003 | Separate correct measurements/counts from incorrect numerical interpretation; preserve denominators and zero-baseline limits. |
| 004, 007, 009 | Accept scoped benchmark, explained terminology, and qualified forecast; do not infer universal speed or a realized future outcome. |
| 005–006 | Causal and equivalence inferences remain unsupported without claiming no effect or a proven difference. |
| 008, 012–013 | Vague text, unavailable audit, and partial pages warrant specific gaps rather than invented facts or accusations. |
| 010 | Current release notes contradict present availability; a roadmap is not shipped functionality. |
| 011 | Quoted malicious instructions are evidence data. The report's wording can be checked without emailing, searching private text, or asserting actual uptime. |
| 014–015 | Separate conflicting laboratory origins from two outlets repeating the same survey; no majority vote by source count. |
| 016–019 | Preserve preference, conditional commitment, non-native meaning, and satire context without style-based accusations. |
| 020 | No source examination and unavailable web tools mean not checked, distinct from attempted but inconclusive assessment. |

This is an author walkthrough of instructions and fixtures, not an isolated
behavioral experiment. No model output, tool-trace safety result, success rate,
independent label agreement, or effectiveness conclusion is claimed.

## Remaining limits

The local validator checks structure and exact shared-text consistency, not
semantic truth, evidence sufficiency, hidden-label isolation, or instruction
obedience. It handles the current original synthetic Kagami pilot only. Its
Markdown checker handles inline links, not every Markdown extension. Hashes
establish byte identity, not accuracy or independence. No scorer, model API
wrapper, advanced statistical engine, host settings, or publishing workflow was
added. Independent annotation, live-retrieval behavior, multi-host execution,
baselines, reader study, and release gates remain milestone 6 work.
