# Amaterasu

<p align="center">
  <img src="pics/amaterasu-smooth-logo.svg" alt="Amaterasu — Bring the hidden to light" width="640">
</p>

<p align="center">
  AI skills for checking claims, writing clearly, and understanding commitments.
</p>

<p align="center">
  <a href="#choose-a-skill">Choose a skill</a> ·
  <a href="#install">Install</a> ·
  <a href="#put-it-to-work">Examples</a> ·
  <a href="#why-amaterasu">The name</a> ·
  <a href="#evaluation-and-contributing">Evaluation</a>
</p>

An impressive proposal can leave its central claim unsupported. Simplifying a
report can erase uncertainty; polishing an email can turn “might” into “will.”
And a promise to recommend someone can be mistaken for a promise to promote them.

Amaterasu gives your AI assistant four focused workflows for these situations:
check what a claim means and what supports it, improve writing without changing
its substance, explain material across audiences, and clarify promises and
boundaries.

Each **skill** is a folder of readable instructions and references that your
assistant loads for a task. Bring a proposal, email, technical report, application,
or conversation. You do not need to write code to use the instructions.

## Choose a skill

| What you need | Skill | What to expect |
| --- | --- | --- |
| Check a claim, a number, or vague corporate language | [Kagami](skills/kagami/SKILL.md) · 鏡 · *mirror* | A claim-by-claim assessment that separates unclear meaning, missing evidence, and conflicting evidence, with sources and questions to resolve the gaps. |
| Write or revise something clearly | [Kotoba](skills/kotoba/SKILL.md) · 言葉 · *words* | A usable draft that preserves your facts, voice, uncertainty, and commitments. Missing information stays visible. |
| Explain material to a different audience | [Kakehashi](skills/kakehashi/SKILL.md) · 架け橋 · *bridge* | An explanation suited to the reader’s knowledge and decision, with technical meaning and limitations intact. |
| Understand a promise, request, or difficult exchange | [Mamoru](skills/mamoru/SKILL.md) · 守る · *protect* | A summary of commitments and documented conduct, unresolved details, and response options suited to the situation. |

Use one skill on its own. When useful, ask for a sequence: Kagami can examine a
proposal, then Kakehashi can explain those findings to a nontechnical reader.
The original wording, evidence, and unresolved questions travel with the handoff;
no skill starts another automatically.

## How it works

The instructions ask the assistant to start with your actual words and context,
keep meaning separate from evidence, and return something you can act on:
an assessment with sources, a draft, an explanation, or questions to clarify an
agreement.

For example, “Our AI doubles productivity” has a claim to examine, even when no
evidence is supplied. “We operationalize exponential synergy” needs clarification
before factual checking can begin. Making either sentence sound better cannot
supply the missing evidence or meaning.

Across all four skills, numbers, conditions, who said what, and uncertainty must
survive. Unfamiliar jargon is a reason to ask what it means. A confident tone,
prestigious title, or polished sentence cannot establish that a claim is true.
The skills assess communication without scoring people or diagnosing their intent.

## Install

You need an AI assistant that can load local skill folders. Amaterasu’s skills
are plain-text Markdown files; Python is only needed for the optional evaluation
tools.

Choose **one installation route per agent**. Installing a plugin and local copies
can make each skill appear twice. The GitHub plugin commands require a published
revision containing the metadata added here. See the
[installation record](eval/installation-verification.md) for tested routes and
remaining host checks.

### Claude Code plugin

```sh
claude plugin marketplace add ThomasBury/amaterasu
claude plugin install amaterasu@amaterasu
```

Start a new session and invoke `/amaterasu:kagami`, `/amaterasu:kotoba`,
`/amaterasu:kakehashi`, or `/amaterasu:mamoru`.

Third-party marketplaces do **not** automatically update by default. Open
`/plugin`, select **Marketplaces**, choose `amaterasu`, and enable auto-update
if wanted. For manual updates:

```sh
claude plugin marketplace update amaterasu
claude plugin update amaterasu@amaterasu
```

See [Claude's plugin guide](https://code.claude.com/docs/en/plugins/install).
Claude runtime verification remains pending.

### Codex plugin

```sh
codex plugin marketplace add ThomasBury/amaterasu
codex plugin add amaterasu@amaterasu
```

Start a new session and select a packaged skill from `/skills` or the `$` picker.
Use the name shown in the catalog. For an explicit refresh:

```sh
codex plugin marketplace upgrade amaterasu
codex plugin add amaterasu@amaterasu
```

Do not rely on startup updates until verified for your version. See
[OpenAI's plugin guide](https://developers.openai.com/plugins/build/plugins)
and the [tested status](docs/compatibility.md).

### Other agents, or editable local files

Run the [Skills CLI](https://github.com/vercel-labs/skills) in your destination
project. It requires Node.js/npm and downloads folders directly from GitHub;
Amaterasu does not require an npm package.

```sh
npx skills@latest add ThomasBury/amaterasu -a <agent>
```

Replace `<agent>` with `codex`, `claude-code`, `github-copilot`, `gemini-cli`,
`opencode`, or another supported agent. Omit `-a <agent>` to choose interactively.
Choose skills in the installer, add `--skill kagami` for just Kagami, or
`--skill '*'` for all four. Installation is project-local by default; `-g`
selects a user-level installation. Add `--copy` for editable copies instead of
links. Compare local edits before updating or replacing them.

```sh
npx skills@latest check
npx skills@latest update
```

Check the CLI's reported scope. If `update` does not track your project-local
copy, re-run its original `add` command. Re-run `add` to select new skills.

### ZIP or manual copying

#### 1. Get the files

[Download the ZIP](https://github.com/ThomasBury/amaterasu/archive/refs/heads/main.zip)
and extract it, or clone the repository:

```sh
git clone https://github.com/ThomasBury/amaterasu.git
cd amaterasu
```

#### 2. Copy the skills into your project

Copy the folders you want from `amaterasu/skills/` into the location for your
assistant. A project can be a folder where you keep documents as well as a code
repository. Keep each entire skill folder, including `references/`, `LICENSE`,
and `NOTICE.md`.

| Assistant | Destination inside your project | Explicit invocation |
| --- | --- | --- |
| [Codex CLI or IDE extension](https://learn.chatgpt.com/docs/build-skills) | `.agents/skills/` | `$kagami`, `$kotoba`, `$kakehashi`, `$mamoru` |
| [Claude Code in a local project](https://code.claude.com/docs/en/skills) | `.claude/skills/` | `/kagami`, `/kotoba`, `/kakehashi`, `/mamoru` |

For example, a Codex installation of Kagami should contain:

```text
my-project/
└── .agents/
    └── skills/
        └── kagami/
            ├── SKILL.md
            ├── references/
            ├── LICENSE
            └── NOTICE.md
```

You can copy the folders with your file manager. In a macOS or Linux terminal,
this example copies Kagami from the Amaterasu checkout into another project.
Replace `/path/to/my-project` with your project’s path:

```sh
mkdir -p "/path/to/my-project/.agents/skills"
cp -R skills/kagami "/path/to/my-project/.agents/skills/"
```

For Claude Code, use `.claude/skills/` instead. Repeat for any other skills you
want. If a destination skill already exists, compare it before replacing it.

#### 3. Select a skill

Open your assistant in the destination project. In Codex, use `/skills` or type
`$` to select the installed skill. In Claude Code, invoke it with `/kagami`, for
example. If it does not appear, restart the assistant and check the folder layout.

These paths follow the linked host documentation. See the
[installation record](eval/installation-verification.md) for observed results and the
[portability guide](docs/compatibility.md) for other intended hosts and the checks
required before claiming compatibility.

## Put it to work

Choose a prompt below and add your material. These examples use Codex’s `$name`
syntax for standalone copies. With the Claude plugin, replace it with
`/amaterasu:name`; with standalone Claude copies, use `/name`. With the Codex
plugin, select the matching packaged skill from its catalog before adding your task.

**Check a proposal with Kagami**

```text
$kagami Review this vendor proposal. Separate unclear wording from claims
that need evidence. Use only the attached sources and show what remains unchecked.
```

**Improve an email or application with Kotoba**

```text
$kotoba Rewrite this application paragraph for a hiring manager. Keep my voice
and the results I supplied. Leave missing dates or outcomes visible.
```

**Explain technical work with Kakehashi**

```text
$kakehashi Explain this test report to a product manager deciding whether to
launch. Preserve the test conditions and what the results cannot establish.
```

**Clarify a commitment with Mamoru**

```text
$mamoru Read these dated messages. What was promised, under which conditions,
and by whom? Help me draft a firm clarification without guessing anyone’s intent.
```

Supply the original text, intended audience, relevant dates, and available
sources. If a page or attachment is inaccessible, provide its text or an export.
Without web access, claims needing external sources remain unresolved.

For private or ambiguous material, the skills use supplied evidence unless you
authorize a suitably scoped public search. Local skill files do not make a cloud
assistant private: your model provider may still receive the material you submit.
Drafting a response does not authorize sending it, filing a complaint, or changing
an external record.

## Why Amaterasu?

Amaterasu takes its name from the sun goddess of Japanese mythology. In the
[story of her return from a cave](https://www.mlit.go.jp/tagengo-db/en/R1-00756.html),
a mirror helps draw her out and restore light to the world.

The project borrows that image of light and reflection. Kagami is the mirror for
examining claims; Kotoba attends to words; Kakehashi bridges understanding; Mamoru
protects boundaries and keeps commitments clear.

## Evaluation and contributing

To inspect the design, extend a skill, or test whether it helps, start with the
[evaluation guide](eval/README.md#choose-your-task). It covers local file checks,
case annotation, human review, and comparisons of assistant behavior. The
[annotation rubric](eval/annotation-rubric.md) explains how to judge outputs;
[skill contracts](docs/contracts.md) define the intended behavior, and the
[evidence register](docs/evidence.md) records the research behind the design.

Amaterasu is experimental. Its examples and automated checks do not establish
that the skills improve an assistant’s answers; independent effectiveness
evaluation is still needed. When reporting a problem, include a nonconfidential
example, the skill, your assistant and model, and what the response got wrong.

## License

Original project material is available under the [MIT license](LICENSE).
[NOTICE.md](NOTICE.md) records attribution and the terms applying to third-party
material.
