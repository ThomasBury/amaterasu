# Amaterasu

<p>
  <img src="pics/amaterasu-smooth-logo.svg" alt="Amaterasu — Bring the hidden to light" width="560">
</p>

Four communication skills in development for examining evidence, preserving meaning,
and choosing useful next steps. English-first, Markdown-first, and independently
usable.

**Status: all four skill packages implemented; Mamoru expert review and independent effectiveness evaluation are pending.**
The standalone [Kagami](skills/kagami/SKILL.md),
[Kotoba](skills/kotoba/SKILL.md),
[Kakehashi](skills/kakehashi/SKILL.md), and [Mamoru](skills/mamoru/SKILL.md) skills include local references. Each has 20
synthetic pilot cases with provisional AI-author labels only. Mamoru’s workplace-expert
review is pending. No host compatibility or effectiveness is claimed.

| Skill | Tagline | Intended use |
| --- | --- | --- |
| Kagami (`kagami`) | Reflect claims against reality. | Examine factual support, reasoning, numbers, and product claims. |
| Kotoba (`kotoba`) | Make every word count. | Draft and revise professional communication without inventing facts or promises. |
| Kakehashi (`kakehashi`) | Bridge expertise without losing meaning. | Explain across audiences while preserving technical scope and limitations. |
| Mamoru (`mamoru`) | Protect fairness. Hold promises accountable. | Clarify commitments and conduct, and prepare proportionate responses. |

The intended benefit is better reasoning and understanding. Vocabulary,
confidence, prestige, and writing style are not evidence that a person is
dishonest or that a claim is empty. None of the cited literature directly
validates Amaterasu.

## Evaluate the skills

Start with the [step-by-step evaluation guide](eval/README.md#choose-your-task).
It explains how to review Mamoru's 20 cases, run local file checks, and prepare
an evaluation of the assistant's behavior. Each path lists what you need, what
to record, and when you are done. The full evaluation still needs independent
reviewers, host testing, and scoring tools.

## Read the foundation

- [Skill contracts](docs/contracts.md): activation, inputs, methods, outputs,
  safeguards, and optional compositions.
- [Evidence register](docs/evidence.md): research strength, limitations, source
  access, and upstream reuse decisions.
- [Evaluation protocol](eval/README.md) and [annotation rubric](eval/annotation-rubric.md):
  independent labeling, comparisons, and proposed acceptance gates.
- [Portability contract](docs/compatibility.md): intended hosts and the evidence
  required before claiming compatibility.
- [Milestones](MILESTONES.md): completed work, next phase, and verification.

## Boundaries

Clearly public material may receive public-source research. Private or ambiguous
material uses supplied evidence unless the user authorizes a suitably scoped
public search. Internal quotations and identifiers must never enter search
queries. Analysis must disclose missing inputs, unavailable evidence, and
unexamined claims.

Drafting a response does not authorize sending it, filing a complaint, or
changing an external record. The project excludes employee rankings, aggregate
credibility scores, deception or personality diagnosis, persistent workplace
dossiers, autonomous escalation, and automatic skill chains.

Markdown skills will have no required runtime dependencies. They will use the
host's existing readers, search, and calculation tools. Supplied-evidence work
will not require a verification service. A cloud-backed host can still transmit
prompts to its model provider; local processing requires a suitable local model
and host configuration.

## Development and license

Work proceeds in independently reviewable phases, with one completed phase per
session. Mamoru implementation is ready for workplace-expert review; milestone 5
remains open until that review is recorded. Release validation stays separate
because it requires independent annotation and host testing. Development dependencies are locked; skills
have no runtime dependency on Python. Run:

```sh
uv sync --locked
uv run --locked python eval/validate.py
uv run --locked pytest -q
uv run --locked skills-ref validate skills/kagami
uv run --locked skills-ref validate skills/kotoba
uv run --locked skills-ref validate skills/kakehashi
uv run --locked skills-ref validate skills/mamoru
```

See the [Kagami](eval/kagami-verification.md),
[Kotoba](eval/kotoba-verification.md),
[Kakehashi](eval/kakehashi-verification.md), and [Mamoru](eval/mamoru-verification.md) pilot records for scope and limits.
To review or transfer a skill, copy its entire folder including references
and license. Host discovery and installation instructions await host-specific tests.

Original project material is available under the [MIT license](LICENSE).
[NOTICE.md](NOTICE.md) records attribution and the boundary around third-party
material.
