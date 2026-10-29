# Amaterasu

Four planned communication skills for examining evidence, preserving meaning,
and choosing useful next steps. English-first, Markdown-first, and independently
usable.

**Status: foundation complete; skills not yet implemented or evaluated.** This
repository currently defines the evidence, behavior, and evaluation contracts.
It does not yet provide installable skills or demonstrated effectiveness.

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
session. The next phase is Kagami. Python evaluation utilities, uv, pytest,
`skills-ref`, and a lockfile will be introduced when there is executable work to
validate. No package or test harness is needed for this documentation phase.

Original project material is available under the [MIT license](LICENSE).
[NOTICE.md](NOTICE.md) records attribution and the boundary around third-party
material.
