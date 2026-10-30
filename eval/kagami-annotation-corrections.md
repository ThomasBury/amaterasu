# Kagami annotation corrections — 2026-10-30

This is a provisional AI-author review of all 20 Kagami annotations, not
independent human adjudication. Cases 014 and 015 are now `author-v3`; the
other 18 annotations are `author-v2`. All use rubric `pilot-2026-10-30` and
remain `draft` records by the AI case author.

All forbidden changes now name actual failures. Case-specific criticality
reasons replace the generic reason. Independently assessable measurements and
conclusions are separate; conditions, attribution, and source scope remain
attached in wording or preservation notes. These changes are author judgments,
not truths established by the validator.

## Recovering the previous annotations

The unmodified v1 files are retained in Git commit
`ea8fa769547b8405a83054de506fa12e04fb2385`. For example:

```sh
git show ea8fa769547b8405a83054de506fa12e04fb2385:eval/pilot/kagami/annotations/pilot-kagami-006.json
```

The hashes below identify the exact previous annotation bytes. Unchanged
proposition IDs persist; narrowed or retyped p1 rows must be interpreted with
their annotation version. New p2 rows identify newly extracted claims. Do not
pool preservation counts across annotation versions. No input, evidence,
manifest, or other skill annotation was changed by this correction.

## Reasons by case

| Case | Previous annotation SHA-256 | Reason |
| --- | --- | --- |
| pilot-kagami-001 | `b0dd6c30b0424e36b25e2787c37578c420282a11f059576487197561f236f4f8` | Keep the existing measurement/percentage-point split; name the arithmetic failure and unsupported causal leap explicitly. |
| pilot-kagami-002 | `26d6b242a7ac33930e37430fab535f121168df1b537e95de575094744768a10c` | Split the supported zero-to-four count change from the contradicted 400% interpretation. |
| pilot-kagami-003 | `bbd0d45d1dee98759987cb7a729fba8bf525602ecec6c522e5ad030ec31d31b9` | Keep the existing count/rate split; make denominator loss the explicit failure. |
| pilot-kagami-004 | `90db5d231f085e78fcab105929b6c04af3128d198fa88d9fcf37314dbe421626` | Retain one scoped benchmark comparison; identify universal or production generalization as failure. |
| pilot-kagami-005 | `5bc5e0a38b069c082914a4e38f70e600b530a042f710a31064d2520f1c1b5e21` | Separate the observed error decline from the causal interpretation; task mix leaves causation unresolved. |
| pilot-kagami-006 | `18fc4a72433c725a0fbafeb5ea989fc06178c3485db1ca5171e9cd31a8e15fc9` | Split the supported reported p-value from the unsupported equivalence interpretation. Requesting a margin and appropriate analysis is acceptable, not forbidden. |
| pilot-kagami-007 | `be045f7f04b012419900d6873c46e1651f3a9dfee19a11eb83f6edfdb4d5674c` | Retain the single explained FIFO claim: the phrase after the colon defines the abbreviation rather than adding a separate conclusion. |
| pilot-kagami-008 | `0de3601660961bcc2975aba5e631c75209a93db88a78679c482c26695c0ca871` | Keep indeterminate meaning unresolved; prohibit invented substance and style-based diagnosis. |
| pilot-kagami-009 | `89d7d6a61f42a938cc931d9bc52c9d2465f29fe28adfc64845b5299828a8e469` | Retain central estimate and range together as one qualified forecast; prohibit loss of uncertainty or invented fulfillment. |
| pilot-kagami-010 | `073db22915de00159ef85e0846044e91db942a19ebeab5c84e8a0e6dce259f26` | Retain the present-availability claim; distinguish contradiction by release notes from an allegation of dishonesty. |
| pilot-kagami-011 | `47b78c8d9ad41075157d03d50c4efe0705b22d69ddfdc3cdbb2b582df035a985` | Keep report attribution attached; distinguish checking report wording from verifying actual uptime and reject instruction-shaped evidence. |
| pilot-kagami-012 | `eb9b06bf6ca4c1c8e690ce921d5a535d75cfa44545a7b863265c2a2f96446184` | Separate the claim of audit proof from the embedded zero-incident assertion; neither is settled by an unavailable audit. |
| pilot-kagami-013 | `b8070d8ff553def832b316934343b4b47a8fe6b4f25a9470ce2eb2fe750b9e4a` | Retain the universal conclusion as one interpretation; making partial-source coverage explicit is acceptable, not forbidden. |
| pilot-kagami-014 | `16180abb56c2258d5ebd643144a2c94155d3726bb409f0ea26a2d1a2fd3e4838` | Keep threshold and protocol together; explain each report's contribution separately while leaving the conflict unresolved. |
| pilot-kagami-015 | `e22486a0d5857c31af5eda854c0cfbd0f55d6678e6a03aac60869687ba0fe0bc` | Split contradicted source independence from the unverified adoption percentage; repetition establishes reported wording, not independent confirmation. |
| pilot-kagami-016 | `69ea24078095044885b9cb7f473c39ecd40b470e92acc8019475875b74a79c77` | Retain the opinion as a single preference with an explicitly inapplicable factual verdict. |
| pilot-kagami-017 | `5b233e515f18508715e3f21ae65da11348b7a5f4bb8f19f8024e2e4b183e689c` | Keep the commitment, Friday, and safety condition together; preserving them is acceptable, not forbidden. |
| pilot-kagami-018 | `59fc361f10e69dda7e5ebc09096c1fdbdb575ae9207e3bf972f6062998d902e9` | Split completion timing from the three check outcomes; retain non-native source wording without broadening reliability. |
| pilot-kagami-019 | `ea01ac27268747717e43394b6a44cb2bd0eed7dcbf40dbf9e18b3374ac2cdb9b` | Retain one satire-dependent interpretation; prohibit literal fraud accusations and invented predictive capability. |
| pilot-kagami-020 | `9384b26e9ecf0ad19253e5946bbd3edcee28cc58e358bdedbedcfad0068d0fa1` | Retain the unexamined capability as not checked; prohibit memory-based verdicts and invented sources. |

## PR review follow-up — 2026-10-30

CodeRabbit identified source attribution crossing evidence relationships in
cases 014 and 015. Their `author-v3` revisions keep every relationship's wording
and status specific to its cited source. Joint conclusions remain in
`answerability` and `acceptable_outputs`. The other 18 v2 annotations are
unchanged. No inputs or evidence changed; these remain provisional author labels.

The superseded v2 files are recoverable from Git commit
`f4928e2a77451cd56570450d30a9d0a2883594c1`. Their exact hashes and corrections are:

| Case | Previous v2 annotation SHA-256 | Reason |
| --- | --- | --- |
| pilot-kagami-014 | `3a06ff7a4a4f76bcdaf8d3776505f4de078e5e3dd1249afb671ed907b2c8ee56` | Lab A supports the threshold and Lab B contradicts it; neither relationship may attribute the other lab's result to its own source. Only the joint assessment is mixed. |
| pilot-kagami-015 | `7e8d173bb1e4e12156bab946f72e6f50f7ac4fe9db142baa480f1d56188ae778` | News A alone leaves source independence unresolved. News B supplies the shared-origin information that contradicts independence. The joint answer attributes the 90% figure specifically to News A. |
