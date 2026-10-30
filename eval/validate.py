"""Validate skill packages and synthetic pilots without scoring model behavior.

Checks cover local files, provenance, identifiers, and annotation structure.
They do not establish factual truth, label quality, or skill effectiveness.
"""

import hashlib
import json
import re
from collections.abc import Iterable
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlsplit

from skills_ref import validate as validate_frontmatter

ROOT = Path(__file__).resolve().parents[1]
SKILL_REFERENCES = {
    'kagami': ('evidence-and-arguments.md', 'numbers-and-product-claims.md'),
    'kotoba': ('writing-and-accountability.md',),
    'kakehashi': ('audiences-and-meaning.md',),
    'mamoru': ('commitments-and-conduct.md',),
}
STATUSES = {
    'supported', 'contradicted', 'mixed', 'insufficient evidence',
    'not checked', 'inapplicable',
}
SUBSTANCE_LABELS = {'clear', 'vague-but-repairable', 'no-determinate-proposition'}


def require(record: object, fields: str) -> None:
    """Require a dictionary containing the named fields.

    Parameters
    ----------
    record : object
        Value to check. Field values are not validated here.
    fields : str
        Whitespace-separated required field names.

    Raises
    ------
    ValueError
        If the record is not a dictionary or a required field is absent.
    """
    if not isinstance(record, dict) or set(fields.split()) - record.keys():
        raise ValueError(f'Missing required fields: {fields}')


def unique(
    records: Iterable[dict[str, Any]], key: str,
) -> dict[str, dict[str, Any]]:
    """Index records by a unique, nonblank string field.

    Parameters
    ----------
    records : iterable of dict
        Records to index in iteration order.
    key : str
        Field containing each record's identifier.

    Returns
    -------
    dict of str to dict
        Original records indexed by their unmodified identifiers.

    Raises
    ------
    ValueError
        If an identifier is absent, blank, not a string, or duplicated.
    """
    indexed = {}
    for record in records:
        identifier = record.get(key)
        if (
            not isinstance(identifier, str)
            or not identifier.strip()
            or identifier in indexed
        ):
            raise ValueError(f'Invalid or duplicate {key}: {identifier}')
        indexed[identifier] = record
    return indexed


def local_file(root: Path, name: str) -> Path:
    """Resolve an existing file confined to a local directory.

    Parameters
    ----------
    root : pathlib.Path
        Directory within which the resolved file must remain.
    name : str
        Nonempty relative file path, resolved against ``root``.

    Returns
    -------
    pathlib.Path
        Absolute resolved path to the file.

    Raises
    ------
    ValueError
        If the name is invalid, the file is missing, or the resolved path
        escapes the root, including through a symbolic link.
    """
    if not isinstance(name, str) or not name or Path(name).is_absolute():
        raise ValueError(f'Invalid local path: {name}')
    path = (root / name).resolve()
    if not path.is_relative_to(root.resolve()) or not path.is_file():
        raise ValueError(f'Missing or escaping local file: {name}')
    return path


def check_hash(path: Path, expected: str) -> None:
    """Compare file bytes with a recorded SHA-256 digest.

    Parameters
    ----------
    path : pathlib.Path
        File whose bytes should be checked.
    expected : str
        Expected hexadecimal SHA-256 digest.

    Raises
    ------
    ValueError
        If the digest differs from the recorded value.
    OSError
        If the file cannot be read.
    """
    if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        raise ValueError(f'Hash mismatch: {path.name}')


def check_links(folder: Path) -> None:
    """Check local inline Markdown links and heading anchors recursively.

    Parameters
    ----------
    folder : pathlib.Path
        Package directory containing Markdown files and local link targets.

    Raises
    ------
    ValueError
        If a local target is missing, escapes the package, or lacks the anchor.
    OSError
        If a Markdown file or link target cannot be read.

    Notes
    -----
    External URLs are skipped. Anchors use lowercase heading text with
    punctuation removed and spaces replaced by hyphens; duplicate-heading
    suffixes and renderer-specific anchor rules are not implemented.
    """
    # ponytail: inline Markdown links only; extend if reference-style links are introduced.
    for path in folder.rglob('*.md'):
        targets = re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text())
        for target in targets:
            link = urlsplit(target)
            if link.scheme or link.netloc:
                continue
            destination = path
            if link.path:
                relative_path = (path.parent / unquote(link.path)).relative_to(folder)
                destination = local_file(folder, str(relative_path))
            if link.fragment:
                headings = re.findall(r'^#+ (.+)$', destination.read_text(), re.MULTILINE)
                anchors = {
                    re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
                    for heading in headings
                }
                if unquote(link.fragment) not in anchors:
                    raise ValueError(f'Missing anchor: {target}')


def validate_skill(folder: Path, contracts: Path | None = None) -> None:
    """Validate package format, local references, and optional shared rules.

    Parameters
    ----------
    folder : pathlib.Path
        Standalone skill package directory.
    contracts : pathlib.Path, optional
        Contract document whose shared safeguards must appear in ``SKILL.md``.
        Omit to validate a standalone package without repository documentation.

    Raises
    ------
    ValueError
        If package format, references, or shared safeguards are invalid.
    IndexError
        If the supplied contract lacks the expected shared-section delimiters.
    OSError
        If a required file cannot be read.
    """
    problems = validate_frontmatter(folder)
    if problems:
        raise ValueError('; '.join(problems))
    check_links(folder)
    if folder.name not in SKILL_REFERENCES:
        raise ValueError('Unsupported skill package')
    required_files = (
        'LICENSE', 'NOTICE.md',
        *(f'references/{name}' for name in SKILL_REFERENCES[folder.name]),
    )
    for name in required_files:
        local_file(folder, name)
    if contracts:
        shared = (
            contracts.read_text()
            .split('## Shared essentials\n\n')[1]
            .split('## Kagami')[0]
            .strip()
        )
        if shared not in (folder / 'SKILL.md').read_text():
            raise ValueError('Shared safeguards drifted from contracts')


def _validate_evidence(record: dict[str, Any], folder: Path) -> None:
    """Check evidence metadata, availability, and artifact integrity.

    Parameters
    ----------
    record : dict
        Evidence record with provenance and availability fields.
    folder : pathlib.Path
        Pilot directory containing the ``evidence`` directory.

    Raises
    ------
    ValueError
        If metadata is incomplete, availability is invalid, or the artifact
        path or digest fails validation.
    OSError
        If an evidence artifact cannot be read.
    """
    require(
        record,
        'evidence_id location title author source_date accessed_at artifact '
        'sha256 origin_id rights availability',
    )
    for field in ('author', 'source_date', 'accessed_at'):
        if record[field] is None and not record.get(f'{field}_reason'):
            raise ValueError(f'Unknown {field} needs a reason')
    if record['availability'] not in {'accessible', 'partial', 'unavailable'}:
        raise ValueError('Invalid evidence availability')
    if record['availability'] == 'unavailable':
        if (
            record['artifact'] is not None
            or record['sha256'] is not None
            or not record.get('unavailable_reason')
        ):
            raise ValueError('Unavailable evidence must have null artifact/hash and a reason')
    else:
        check_hash(local_file(folder / 'evidence', record['artifact']), record['sha256'])


def _validate_case(
    case: dict[str, Any], case_id: str, skill: str,
    evidence: dict[str, dict[str, Any]],
) -> None:
    """Check a pilot input's identity, context, research scope, and evidence IDs.

    Parameters
    ----------
    case : dict
        Pilot input record.
    case_id : str
        Identifier under which the case was indexed.
    skill : str
        Expected skill name.
    evidence : dict of str to dict
        Corpus evidence records indexed by identifier.

    Raises
    ------
    ValueError
        If required fields or skill-specific input constraints are invalid.
    TypeError
        If evidence identifiers cannot be used in a set.
    """
    require(case, 'case_id skill task input context research_scope evidence')
    if case['skill'] != skill or not re.fullmatch(rf'pilot-{skill}-\d{{3}}', case_id):
        raise ValueError('Invalid pilot identifier or skill')
    if skill == 'kotoba' and case.get('writing_mode') not in {'draft', 'revision'}:
        raise ValueError('Kotoba requires draft or revision writing_mode')
    source = case['input']
    if (
        not isinstance(source, dict)
        or not source
        or not all(isinstance(text, str) and text for text in source.values())
    ):
        raise ValueError('Input must contain nonempty located text')
    require(case['context'], 'date purpose audience roles chronology constraints')
    audience = case['context']['audience']
    if skill == 'kakehashi' and (not isinstance(audience, str) or not audience.strip()):
        raise ValueError('Kakehashi requires a specified audience')
    scope = case['research_scope']
    require(scope, 'mode web_available authorization')
    if (
        scope['mode'] not in {
            'clearly-public', 'supplied-evidence-only', 'authorized-public-search',
        }
        or not isinstance(scope['web_available'], bool)
    ):
        raise ValueError('Invalid research scope')
    if scope['mode'] == 'authorized-public-search' and not scope['authorization']:
        raise ValueError('Public search requires recorded scope authorization')
    evidence_ids = case['evidence']
    if (
        not isinstance(evidence_ids, list)
        or len(set(evidence_ids)) != len(evidence_ids)
        or set(evidence_ids) - evidence.keys()
    ):
        raise ValueError('Invalid evidence references')


def _validate_manifest(
    row: dict[str, Any], manifest: dict[str, dict[str, Any]],
    folder: Path, case_id: str,
) -> None:
    """Check synthetic provenance, variant clustering, and original input bytes.

    Parameters
    ----------
    row : dict
        Manifest entry for the current case.
    manifest : dict of str to dict
        All manifest entries, including possible variant parents.
    folder : pathlib.Path
        Pilot directory containing the original input files.
    case_id : str
        Identifier of the current case.

    Raises
    ------
    ValueError
        If provenance, variant relationships, source path, or hash is invalid.
    KeyError
        If a variant parent lacks a required cluster field.
    OSError
        If the original input cannot be read.
    """
    require(
        row,
        'case_id split document_id family_id variant_of variant_change source_kind '
        'source_date source_location rights input_sha256 evidence_set_id categories',
    )
    if row['split'] != 'pilot' or row['source_kind'] != 'original-synthetic':
        raise ValueError('This validator handles original synthetic pilots only')
    if row['variant_of'] is not None:
        parent = manifest.get(row['variant_of'])
        if (
            not parent
            or parent is row
            or not row['variant_change']
            or any(row[field] != parent[field] for field in ('split', 'family_id', 'document_id'))
        ):
            raise ValueError('Variant must retain parent split and cluster')
    elif row['variant_change'] is not None:
        raise ValueError('Variant change without parent')
    expected = folder / 'inputs' / f'{case_id}.json'
    if local_file(folder, row['source_location']) != expected.resolve():
        raise ValueError('Input source location does not match case')
    check_hash(expected, row['input_sha256'])


def _validate_questions(annotation: dict[str, Any], source: dict[str, str]) -> None:
    """Check Kakehashi questions and source-linked answer keys.

    Parameters
    ----------
    annotation : dict
        Annotation containing questions and answer keys.
    source : dict of str to str
        Original input text indexed by location.

    Raises
    ------
    ValueError
        If questions or answers are malformed, duplicated, unmatched, missing
        a required question kind, or cite an unknown input location.
    """
    if (
        not isinstance(annotation['questions'], list)
        or not isinstance(annotation['answer_key'], list)
    ):
        raise ValueError('Kakehashi questions and answer keys must be lists')
    for question in annotation['questions']:
        require(question, 'question_id kind prompt')
        if (
            question['kind'] not in {'comprehension', 'scope', 'action'}
            or not isinstance(question['prompt'], str)
            or not question['prompt'].strip()
        ):
            raise ValueError('Invalid Kakehashi question')
    questions = unique(annotation['questions'], 'question_id')
    for answer in annotation['answer_key']:
        require(answer, 'question_id answer source_locations')
        if not isinstance(answer['answer'], str) or not answer['answer'].strip():
            raise ValueError('Empty Kakehashi answer')
        locations = answer['source_locations']
        if (
            not isinstance(locations, list)
            or not locations
            or any(
                not isinstance(location, str) or location not in source
                for location in locations
            )
        ):
            raise ValueError('Answer key must cite original input locations')
    answers = unique(annotation['answer_key'], 'question_id')
    question_kinds = {question['kind'] for question in questions.values()}
    if answers.keys() != questions.keys() or question_kinds != {'comprehension', 'scope', 'action'}:
        raise ValueError('Kakehashi requires matched comprehension, scope and action keys')


def _validate_annotation(
    annotation: dict[str, Any], case: dict[str, Any], skill: str,
    evidence: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    """Check provisional propositions and their evidence relationships.

    Parameters
    ----------
    annotation : dict
        AI-author annotation for the case.
    case : dict
        Validated input record with located text and evidence identifiers.
    skill : str
        Skill name used to select additional annotation checks.
    evidence : dict of str to dict
        Validated corpus evidence records indexed by identifier.

    Returns
    -------
    list of dict
        Original propositions for the corpus-wide identifier check.

    Raises
    ------
    ValueError
        If author labels are not provisional, propositions alter the original
        input, or evidence relationships or skill-specific answers are invalid.
    """
    require(
        annotation,
        'annotation_id case_id annotator_id annotator_role expertise rubric_version '
        'state propositions evidence_relationships reasoning_gaps answerability '
        'problem_labels acceptable_outputs forbidden_changes questions answer_key '
        'disagreements adjudication',
    )
    if (
        annotation['state'] != 'draft'
        or annotation['annotator_role'] != 'AI case author; not independent'
    ):
        raise ValueError('Author labels must remain provisional drafts')
    if skill == 'kakehashi':
        _validate_questions(annotation, case['input'])
    propositions = unique(annotation['propositions'], 'proposition_id')
    if not propositions:
        raise ValueError('Missing propositions')
    for proposition in propositions.values():
        require(
            proposition,
            'proposition_id wording location claim_type critical critical_reason preserve',
        )
        if (
            not isinstance(proposition['critical'], bool)
            or not isinstance(proposition['preserve'], str)
            or not proposition['preserve'].strip()
        ):
            raise ValueError('Proposition needs a boolean critical flag and preservation key')
        if not isinstance(proposition['wording'], str) or not proposition['wording'].strip():
            raise ValueError('Proposition needs nonblank string wording')
        if proposition['critical'] and (
            not isinstance(proposition['critical_reason'], str)
            or not proposition['critical_reason'].strip()
        ):
            raise ValueError('Critical proposition needs a nonblank reason')
        if (
            proposition['location'] not in case['input']
            or proposition['wording'] not in case['input'][proposition['location']]
        ):
            raise ValueError('Proposition wording/location must match original input')
        if skill == 'kagami' and proposition.get('substance') not in SUBSTANCE_LABELS:
            raise ValueError('Kagami proposition needs a valid substance label')
        if proposition['claim_type'] not in {
            'factual assertion', 'interpretation', 'opinion', 'indeterminate',
            'prediction', 'aspiration', 'commitment',
        }:
            raise ValueError('Invalid claim type')
        if skill == 'kagami' and (
            (proposition['substance'] == 'no-determinate-proposition')
            != (proposition['claim_type'] == 'indeterminate')
        ):
            raise ValueError('Substance and claim type drifted')
    if not annotation['evidence_relationships']:
        raise ValueError('Missing evidence relationships')
    for relationship in annotation['evidence_relationships']:
        require(relationship, 'proposition_id evidence_id location status establishes')
        if (
            relationship['proposition_id'] not in propositions
            or relationship['status'] not in STATUSES
        ):
            raise ValueError('Invalid proposition reference or evidence status')
        evidence_id = relationship['evidence_id']
        if evidence_id is not None and evidence_id not in case['evidence']:
            raise ValueError('Relationship cites evidence outside case')
        if relationship['status'] in {'supported', 'contradicted', 'mixed'} and (
            evidence_id is None
            or evidence[evidence_id]['availability'] == 'unavailable'
            or not relationship['location']
        ):
            raise ValueError('Factual verdict requires available located evidence')
        proposition = propositions[relationship['proposition_id']]
        if (
            skill == 'kagami'
            and proposition['substance'] == 'no-determinate-proposition'
            and relationship['status'] != 'inapplicable'
        ):
            raise ValueError('No determinate proposition requires inapplicable evidence status')
    related_propositions = {
        relationship['proposition_id'] for relationship in annotation['evidence_relationships']
    }
    if propositions.keys() != related_propositions:
        raise ValueError('Every proposition needs an explicit evidence relationship')
    return annotation['propositions']


def validate_corpus(folder: Path, skill: str = 'kagami') -> int:
    """Validate synthetic pilot provenance and annotation structure.

    Parameters
    ----------
    folder : pathlib.Path
        Pilot directory containing manifests, inputs, evidence, and annotations.
    skill : str, default 'kagami'
        Expected skill name from ``SKILL_REFERENCES``.

    Returns
    -------
    int
        Number of validated pilot cases.

    Raises
    ------
    ValueError
        If JSON is invalid or a structural, provenance, or integrity check fails.
    KeyError
        If a referenced record lacks a field needed for validation.
    TypeError
        If a field has an incompatible type for the operation performed.
    OSError
        If a required file cannot be read.

    Notes
    -----
    Only original synthetic pilot records with provisional AI-author labels are
    accepted. Passing does not establish annotation quality or model behavior.
    """
    if skill not in SKILL_REFERENCES:
        raise ValueError('Unsupported pilot skill')
    manifest = unique(json.loads(local_file(folder, 'manifest.json').read_text()), 'case_id')
    evidence = unique(json.loads(local_file(folder, 'evidence.json').read_text()), 'evidence_id')
    cases = unique(
        (json.loads(path.read_text()) for path in sorted((folder / 'inputs').glob('*.json'))),
        'case_id',
    )
    annotations = [
        json.loads(path.read_text())
        for path in sorted((folder / 'annotations').glob('*.json'))
    ]
    unique(annotations, 'annotation_id')
    labels = unique(annotations, 'case_id')
    if cases.keys() != manifest.keys() or labels.keys() != cases.keys():
        raise ValueError('Case, manifest and annotation IDs must match')

    for record in evidence.values():
        _validate_evidence(record, folder)

    all_propositions = []
    for case_id, case in cases.items():
        _validate_case(case, case_id, skill, evidence)
        _validate_manifest(manifest[case_id], manifest, folder, case_id)
        all_propositions.extend(_validate_annotation(labels[case_id], case, skill, evidence))
    unique(all_propositions, 'proposition_id')
    return len(cases)


if __name__ == '__main__':
    try:
        count = 0
        for skill in SKILL_REFERENCES:
            validate_skill(ROOT / 'skills' / skill, ROOT / 'docs/contracts.md')
            count += validate_corpus(ROOT / 'eval/pilot' / skill, skill)
    except (ValueError, KeyError, TypeError, OSError) as error:
        raise SystemExit(f'Validation failed: {error}')
    print(
        f'Validated {len(SKILL_REFERENCES)} skill packages and {count} pilot records; '
        'no behavioral score implied.'
    )
