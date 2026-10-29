# Evidence register and reuse decisions

Reviewed for the foundation on **2026-10-29**. These are original summaries of
design sources, not a systematic review, a replication, or evidence that
Amaterasu works. No cited study directly validates these four skills.

## How to read the register

- **Empirical:** observations or experiments address a defined question in a
  particular population and setting. Association alone does not establish cause.
- **Operational:** a documented procedure used in practice. Adoption does not
  establish the procedure's isolated effect.
- **Theoretical:** a framework or reasoned proposal rather than an evaluated
  intervention for this task.
- **Uncertain for this application:** transfer to an AI-assisted communication
  skill has not been established. This applies to every method below, even when
  its original setting has empirical support.

“Inspected” means the identified abstract, excerpt, or source passages were
examined; it does not imply a full methodological audit. Access failures remain
visible. Details carried from the supplied implementation plan are labeled as
such and must be checked before downstream reuse depends on them.

## Mandatory publications

### Littrell (2026): corporate bullshit receptivity

**Evidence: empirical; uncertain for this application.** Four studies, total
N = 1,018, develop a receptivity scale and relate it to reasoning and workplace
judgments. The workplace decision measure includes situational judgment tests.
The paper calls for validation against objective performance and cautions about
generalization beyond Western, English-speaking contexts.

**Design consequence:** distinguish meaningful corporate terminology from empty
rhetoric. The scale does not validate automated text classification, employee
intelligence or integrity judgments, hiring decisions, or causal claims about
organizational performance. Amaterasu will not rank employees.

Sources: [published paper](https://doi.org/10.1016/j.paid.2026.113699);
[author manuscript](https://www.researchgate.net/publication/400597536_The_Corporate_Bullshit_Receptivity_Scale_Development_validation_and_associations_with_workplace_outcomes).
Inspected manuscript abstract, Study 3 decision-making measure (pp. 27–28), and
Limitations (p. 36); publisher DOI access failed.

### Petrocelli (2026): organizational practices

**Evidence: theoretical synthesis informed by empirical research and
organizational examples; uncertain for this application.** The paper offers
proposed practices for contexts requiring accuracy while recognizing legitimate
roles for aspiration and ambiguity. Its organizational practices must not be
described as directly field-validated interventions.

**Design consequence:** adapt evidence labeling, clarification, and examination
of prior claims as proposed practices. Do not promise that these practices
improve organizational outcomes or infer a speaker's indifference to truth from
style alone.

Sources: [publisher abstract](https://www.sciencedirect.com/science/article/pii/S0090261626000124)
and [author-hosted paper](https://www.johnvpetrocelli.com/_files/ugd/de1109_257c791efd2e4285bef1b25ee3ef1a10.pdf).
The indexed publisher abstract was inspected; direct publisher and PDF retrieval
failed. The supplied plan's account of explicit field-validation limitations
has not been independently checked against the full paper in this phase.

### Cruz and Lombrozo (2025): jargon and explanations

**Evidence: empirical; uncertain for this application.** Nine preregistered
experiments, N = 6,698, distinguish satisfaction with explanations from their
comprehensibility. Added jargon can inflate evaluations of deficient
explanations. Follow-up questions and self-generated explanations can reduce
those inflated evaluations.

**Design consequence:** preserve useful technical terms and test understanding
separately from perceived sophistication. These findings do not show that
removing jargon always improves communication or that an AI rewrite preserves
meaning. Measure comprehension rather than asking the model to rate itself.

Source: [author-hosted paper](https://cognition.princeton.edu/sites/g/files/toruqf3386/files/documents/s41562-025-02227-0.pdf),
abstract, Results/preregistration, and discussion of Studies 3A–4, pp. 1–2,
inspected.

### Accessible commentary

[Chuniversiteit's commentary](https://chuniversiteit.nl/blog/science/corporate-bullshit)
(19 April 2026) provides accessible framing. **Evidence: theoretical/commentary;
uncertain for this application.** The page was inspected, but its organizational
consequences are not substitutes for the original studies. Do not turn its
interpretations of associations into causal conclusions.

## Methods and transfer limits

All design consequences in this table are Amaterasu's proposed adaptations.
Method names are tools for explanation, not labels that establish truth.

| Method and source | Evidence assessment | Application and boundary | Source access on review date |
| --- | --- | --- | --- |
| [Toulmin, The Uses of Argument](https://assets.cambridge.org/97805218/27485/frontmatter/9780521827485_frontmatter.pdf) (1958; updated edition 2003) | Theoretical; uncertain for this application. | Map claim, grounds, connecting assumption, qualifications, and exceptions. Explain the reasoning gap. This is not an automatic truth detector. | Publisher frontmatter inspected; it is not the full chapter explaining the model. Detailed method is a design adaptation, not a validated classifier. |
| [Lateral-reading field study](https://eric.ed.gov/?id=EJ1372738) | Empirical, according to the supplied plan; uncertain for this application. | Investigate a source outside its own site and trace evidence to its origin. Repetition is not independence. | ERIC retrieval timed out; study details remain unverified in this phase. |
| [Oswald et al., lateral reading and search](https://pubmed.ncbi.nlm.nih.gov/42406504/) (2026) | Empirical randomized intervention; uncertain for this application. | Use external source investigation, with modest expectations. The abstract reports small effects, some not distinguishable from zero; between-group differences were not distinguishable at two weeks. Do not claim established persistence. | PubMed abstract inspected. |
| [Platt, Strong Inference](https://pages.cs.wisc.edu/~markhill/science64_strong_inference.pdf) (1964) | Theoretical scientific reasoning practice; uncertain for this application. | Compare plausible explanations and ask what observations could weaken each. Amaterasu's implementation is unvalidated. Statistical nonsignificance does not itself prove no effect or equivalence. | Transcription of the original paper inspected; transcription warns about punctuation fidelity. |
| [Army main-point-first guidance](https://tjaglcs.army.mil/Periodicals/The-Army-Lawyer/tal-2019-issue-1/Post/5907/No-2-Find-Your-Yoda) (2019 issue) | Operational; uncertain for this application. | BLUF means bottom line up front: lead a decision brief with the finding or requested decision, immediately retaining material qualifications. Do not force every genre into this structure. | “Rule #9: Make the complex simple” passage inspected. |
| [SBAR systematic review](https://bmjopen.bmj.com/content/8/8/e022202) (2018) | Empirical healthcare synthesis, reported as heterogeneous and limited in quality; uncertain for this application. | Optional situation, background, assessment, recommendation structure for handoffs or risk reports. Corporate effects need separate measurement. | Direct retrieval returned 403; the evidence-strength assessment is retained from the supplied plan, not a new full-text review. |
| [FAA report on ATC messages and pilot readback](https://www.faa.gov/sites/faa.gov/files/data_research/research/med_humanfacs/oamtechreports/200625.pdf) (2006) | Empirical operational observations; uncertain for this application. | Closed-loop communication checks receipt and interpretation and permits correction. The report relates message complexity to readback errors in aviation; it does not validate corporate AI assistance or prove that acknowledgment is comprehension. | Report abstract and operational setting inspected. |
| [Talevski et al., teach-back review](https://pubmed.ncbi.nlm.nih.gov/32287296/) (2020) | Empirical healthcare synthesis; heterogeneous studies; uncertain for this application. | Invite recipients to explain implications in their own words. Teach-back tests understanding; it is not interchangeable with acknowledging or repeating an instruction. | Abstract inspected; 20 studies with varied quality, settings, and outcomes. |
| [AHRQ DESC](https://www.ahrq.gov/teamstepps-program/curriculum/mutual/overview/index.html) (reviewed 2023) | Operational; uncertain for this application. | Describe conduct, express concerns, suggest alternatives, and state consequences in terms of practical impact. Use as an optional response structure; isolated effects and workplace transfer remain uncertain. | DESC section inspected. |
| [AHRQ Two-Challenge Rule](https://www.ahrq.gov/teamstepps-program/curriculum/mutual/tools/rule.html) | Operational; uncertain for this application. | Reserve repeated safety challenges for consequential safety concerns in appropriate settings. Do not turn routine disagreement into mandatory escalation. | Tool page available; no independent effect evaluation performed. |
| [Weger et al., active listening](https://doi.org/10.1080/10904018.2013.813234) (2014) | Empirical interpersonal experiment; uncertain for this application. | Paraphrase and ask open questions. Some perceived-understanding benefits do not establish safety in threats or power imbalances. Acknowledge a concern without asserting agreement. | DOI retrieval failed; indexed publisher methods/results passages inspected. |
| [FBI crisis-negotiator training](https://leb.fbi.gov/articles/focus/focus-on-training-an-evaluation-tool-for-crisis-negotiators) (2015) | Operational; uncertain for this application. | Active-listening practice informs response options. Crisis practice is not proof that a particular wording will de-escalate a workplace conflict. | Training and active-listening passages inspected. |

## Boundaries around people and conduct

| Source | Evidence assessment | Boundary | Source access on review date |
| --- | --- | --- | --- |
| [Frazier et al., psychological safety meta-analysis](https://doi.org/10.1111/peps.12183) (2017) | Empirical synthesis; uncertain for this application. | Psychological safety is an organizational condition. Courteous wording alone cannot be claimed to create it. | Publisher page available; no new full methodological audit. |
| [Einarsen et al., NAQ-R research](https://doi.org/10.1080/02678370902815673) (2009) | Empirical questionnaire validation, per supplied plan; uncertain for this application. | A validated workplace-exposure questionnaire does not validate diagnosing bullying from an isolated message. Describe observed conduct without diagnosing its author. | DOI retrieval returned 403; detailed validation claims not independently rechecked. |
| [Bond and DePaulo, deception judgments](https://pubmed.ncbi.nlm.nih.gov/16859438/) (2006) and [Levine and Serota reanalysis](https://journals.sagepub.com/doi/10.1177/00936502251316927) (2025) | Empirical synthesis/reanalysis; uncertain for this application. | Style is insufficient evidence of deception. Experimental conditions and truth/lie base rates constrain interpretation. Do not transfer human detection rates to these skills. | PubMed record and reanalysis abstract inspected; no replication. |

These boundaries do not require withholding recognition of explicit threats or
documented repeated humiliation. They require distinguishing the conduct,
available evidence, possible interpretations, and unknown intent.

## Existing implementations

Evaluation reports below are upstream reports, not Amaterasu results. No baseline
has been installed or run. Software tests establish different things from
reader comprehension or correct evidence assessment.

| Implementation | Capabilities and evidence | Decision and exclusions |
| --- | --- | --- |
| [SerhiiKorniienko/bullshit-detector](https://github.com/SerhiiKorniienko/bullshit-detector) | MIT. The supplied plan describes Markdown skills, Python ingestion/report helpers, web verification, verdicts, and an overall score. Its inspected [2026-09-03 results](https://github.com/SerhiiKorniienko/bullshit-detector/blob/main/eval/RESULTS.md) report 480 curated claims in ten cases, extraction recall 0.704, and known-false catch rate 0.692. Labels were agent-curated and awaiting owner review. Retrieval was not frozen. The report identifies skill commit `e585a78` and a 0.14.0/0.14.1 run-label discrepancy. **Operational implementation; empirical but preliminary evaluation; uncertain transfer.** | Adapt claim-level provenance and explicit verification gaps with attribution. Use as an evaluation baseline. Exclude aggregate scoring, publishing machinery, and inferences of malicious intent from formatting. Freeze a full revision and inputs before comparison. |
| [mycarta/bullshit-detector](https://github.com/mycarta/bullshit-detector) | Statistical screening modules cover correlations, p-values, GRIM/GRIMMER, power, and related checks. Repository README inspected; the supplied plan additionally reports NumPy/SciPy, tests, and worked audits. The page displays an MIT badge but Apache-2.0 in README. The supplied plan also reports MIT in LICENSE/package metadata and warns about probability descriptions in [spurious.py](https://github.com/mycarta/bullshit-detector/blob/master/src/bullshit_detector/spurious.py). Direct LICENSE and calculation-file retrieval failed. **Operational software; uncertain for this application.** | Reference and evaluate selected functions only after validating assumptions and resolving licensing at a pinned revision. Do not bundle v1 or recreate advanced statistical auditing. A null-model probability is not the probability that a particular finding is false. |
| [Vale](https://docs.vale.sh/) ([repository](https://github.com/vale-cli/vale)) | MIT Go CLI for configurable, markup-aware prose linting. Documentation describes style consistency, not evidence assessment. **Operational software; uncertain comprehension benefit.** | Optional use when a project already has Vale. No mandatory install, replacement linter, or word blacklist. Limit baseline comparisons to terminology/style consistency. |
| [De-Jargonizer software](https://figshare.com/articles/software/Website/5194795), [dictionary](https://doi.org/10.6084/m9.figshare.5194798.v3), and [study](https://doi.org/10.1371/journal.pone.0181742) (2017) | The supplied plan reports archived ASP.NET/C# code, dictionary lookup, weighted scoring in three vocabulary bands, and MIT-labeled deposits. The inspected study describes frequency-list comparisons and 5,000 abstract/summary pairs. Deposits were inaccessible; code and license inspection were not repeated. **Operational lexical proxy plus empirical evaluation; uncertain for truth or audience understanding.** | Optional lexical baseline, never a runtime service. Do not reproduce the website or treat rare words as evidence of poor explanations. Recheck exact deposit licenses before any redistribution. |
| [ClaimBuster spotter](https://github.com/utaresearch/claimbuster-spotter) and [research](https://doi.org/10.1145/3689212) | Inspected repository lists SVM, bidirectional LSTM, and adversarial transformer approaches under GPL-3.0. Its task is check-worthiness, not truth verification. The supplied plan flags deprecated setup documentation. **Operational software and empirical claim-spotting research; uncertain for other tasks.** | Use as a local claim-detection comparator only where reproducible. No production API dependency, proprietary-data submission, or new model training. Record unavailable setups rather than inventing a result. |

See [NOTICE.md](../NOTICE.md) for distribution boundaries. The expected advantage
is a testable hypothesis: fewer false accusations, better preservation of
qualifications and commitments, better comprehension, and useful responses
across roles. The [evaluation protocol](../eval/README.md) must test it. Failure
to show an advantage should lead to simplification or removal of the affected
functionality, not stronger marketing language.
