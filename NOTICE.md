# Attribution and third-party material

Amaterasu's original documentation and future original implementations use the
[MIT license](LICENSE). That license does not relicense linked papers, websites,
datasets, code, or other third-party material. No papers, upstream code,
dictionaries, or benchmark datasets are bundled in this foundation.

The design draws on the publications and methods cited in the
[evidence register](docs/evidence.md). Summaries are original. Citations identify
intellectual sources; they do not imply endorsement or validation of Amaterasu.

The planned claim-level provenance and explicit verification-gap practices are
informed by [Serhii Korniienko's bullshit-detector](https://github.com/SerhiiKorniienko/bullshit-detector)
([MIT license](https://github.com/SerhiiKorniienko/bullshit-detector/blob/main/LICENSE)).
The foundation adapts these design ideas in its contracts; it copies no code or
skill prose. Its aggregate score and publishing workflow are excluded.

Other examined projects are comparison candidates, not dependencies:

| Project | Intended relationship | Licensing boundary |
| --- | --- | --- |
| [mycarta/bullshit-detector](https://github.com/mycarta/bullshit-detector) | Selective statistical reference only. | The inspected repository page displays an MIT license badge and Apache-2.0 in README. The supplied plan also reports MIT in LICENSE/package metadata. Resolve the discrepancy at a pinned revision before reuse. Nothing is bundled. |
| [Vale](https://github.com/vale-cli/vale) | Optional existing local style checker. | MIT; retain applicable notices if any material is later copied. |
| [De-Jargonizer](https://figshare.com/articles/software/Website/5194795) | Optional lexical comparator. | The supplied plan reports MIT for the software and dictionary deposits. Recheck each exact artifact before redistribution. |
| [ClaimBuster spotter](https://github.com/utaresearch/claimbuster-spotter) | Separate local claim-detection comparator where reproducible. | GPL-3.0; no code or model is bundled or relicensed as MIT. |

Before copying any upstream material, record the exact revision, author,
license, files used, and modifications here, and preserve required notices with
the distributed material. A standalone skill distribution must carry the MIT
notice and any applicable attribution within its own folder.

Future real-world evaluation inputs require documented permission or a license
allowing their intended use and redistribution. Public availability alone is
not permission. Private evaluation material stays outside public artifacts.

The development environment uses the official Apache-2.0 `skills-ref` reference
validator from [agentskills/agentskills](https://github.com/agentskills/agentskills),
pinned to revision `69ef37e9424c0a7ea9dd2293b559e43ec8176379`. It is installed
as a development dependency, not copied into the standalone skill. Its own
license remains applicable; the upstream tool is a demonstration validator,
not evidence of runtime safety or effectiveness.
