"""Structural checks only: never infer truth or score model behavior."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

from skills_ref import validate as validate_frontmatter

ROOT = Path(__file__).resolve().parents[1]
STATUSES = {'supported', 'contradicted', 'mixed', 'insufficient evidence', 'not checked', 'inapplicable'}


def require(record, fields):
    if not isinstance(record, dict) or set(fields.split()) - record.keys():
        raise ValueError(f'Missing required fields: {fields}')


def unique(records, key):
    result = {}
    for record in records:
        value = record.get(key)
        if not isinstance(value, str) or not value.strip() or value in result:
            raise ValueError(f'Invalid or duplicate {key}: {value}')
        result[value] = record
    return result


def local_file(root, name):
    if not isinstance(name, str) or not name or Path(name).is_absolute():
        raise ValueError(f'Invalid local path: {name}')
    path = (root / name).resolve()
    if not path.is_relative_to(root.resolve()) or not path.is_file():
        raise ValueError(f'Missing or escaping local file: {name}')
    return path


def check_hash(path, expected):
    if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        raise ValueError(f'Hash mismatch: {path.name}')


def check_links(folder):
    # shortcut: inline Markdown links only; extend if reference-style links are introduced.
    for path in folder.rglob('*.md'):
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
            link = urlsplit(target)
            if link.scheme or link.netloc:
                continue
            destination = local_file(folder, str((path.parent / unquote(link.path)).relative_to(folder))) if link.path else path
            if link.fragment:
                headings = re.findall(r'^#+ (.+)$', destination.read_text(), re.M)
                anchors = {re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings}
                if unquote(link.fragment) not in anchors:
                    raise ValueError(f'Missing anchor: {target}')


def validate_skill(folder, contracts=None):
    problems = validate_frontmatter(folder)
    if problems:
        raise ValueError('; '.join(problems))
    check_links(folder)
    for name in ('LICENSE', 'NOTICE.md', 'references/evidence-and-arguments.md', 'references/numbers-and-product-claims.md'):
        local_file(folder, name)
    if contracts:
        shared = contracts.read_text().split('## Shared essentials\n\n')[1].split('## Kagami')[0].strip()
        if shared not in (folder / 'SKILL.md').read_text():
            raise ValueError('Shared safeguards drifted from contracts')


def validate_corpus(folder):
    def read(name):
        return json.loads(local_file(folder, name).read_text())
    manifest = unique(read('manifest.json'), 'case_id')
    evidence = unique(read('evidence.json'), 'evidence_id')
    cases = unique([json.loads(p.read_text()) for p in sorted((folder / 'inputs').glob('*.json'))], 'case_id')
    annotations = [json.loads(p.read_text()) for p in sorted((folder / 'annotations').glob('*.json'))]
    unique(annotations, 'annotation_id')
    labels = unique(annotations, 'case_id')
    if set(cases) != set(manifest) or set(labels) != set(cases):
        raise ValueError('Case, manifest and annotation IDs must match')
    for ev in evidence.values():
        require(ev, 'evidence_id location title author source_date accessed_at artifact sha256 origin_id rights availability')
        for field in ('author', 'source_date', 'accessed_at'):
            if ev[field] is None and not ev.get(field + '_reason'):
                raise ValueError(f'Unknown {field} needs a reason')
        if ev['availability'] not in {'accessible', 'partial', 'unavailable'}:
            raise ValueError('Invalid evidence availability')
        if ev['availability'] == 'unavailable':
            if ev['artifact'] is not None or ev['sha256'] is not None or not ev.get('unavailable_reason'):
                raise ValueError('Unavailable evidence must have null artifact/hash and a reason')
        else:
            check_hash(local_file(folder / 'evidence', ev['artifact']), ev['sha256'])
    all_props = []
    for cid, case in cases.items():
        require(case, 'case_id skill task input context research_scope evidence')
        if case['skill'] != 'kagami' or not re.fullmatch(r'pilot-kagami-\d{3}', cid):
            raise ValueError('Invalid Kagami pilot identifier or skill')
        if not isinstance(case['input'], dict) or not case['input'] or not all(isinstance(v, str) and v for v in case['input'].values()):
            raise ValueError('Input must contain nonempty located text')
        require(case['context'], 'date purpose audience roles chronology constraints')
        require(case['research_scope'], 'mode web_available authorization')
        if case['research_scope']['mode'] not in {'clearly-public', 'supplied-evidence-only', 'authorized-public-search'} or not isinstance(case['research_scope']['web_available'], bool):
            raise ValueError('Invalid research scope')
        if case['research_scope']['mode'] == 'authorized-public-search' and not case['research_scope']['authorization']:
            raise ValueError('Public search requires recorded scope authorization')
        if not isinstance(case['evidence'], list) or len(set(case['evidence'])) != len(case['evidence']) or set(case['evidence']) - evidence.keys():
            raise ValueError('Invalid evidence references')
        row = manifest[cid]
        require(row, 'case_id split document_id family_id variant_of variant_change source_kind source_date source_location rights input_sha256 evidence_set_id categories')
        if row['split'] != 'pilot' or row['source_kind'] != 'original-synthetic':
            raise ValueError('This validator handles original synthetic pilots only')
        if row['variant_of'] is not None:
            parent = manifest.get(row['variant_of'])
            if not parent or parent is row or not row['variant_change'] or any(row[k] != parent[k] for k in ('split', 'family_id', 'document_id')):
                raise ValueError('Variant must retain parent split and cluster')
        elif row['variant_change'] is not None:
            raise ValueError('Variant change without parent')
        expected = folder / 'inputs' / f'{cid}.json'
        if local_file(folder, row['source_location']) != expected.resolve():
            raise ValueError('Input source location does not match case')
        check_hash(expected, row['input_sha256'])
        ann = labels[cid]
        require(ann, 'annotation_id case_id annotator_id annotator_role expertise rubric_version state propositions evidence_relationships reasoning_gaps answerability problem_labels acceptable_outputs forbidden_changes questions answer_key disagreements adjudication')
        if ann['state'] != 'draft' or ann['annotator_role'] != 'AI case author; not independent':
            raise ValueError('Author labels must remain provisional drafts')
        props = unique(ann['propositions'], 'proposition_id')
        if not props:
            raise ValueError('Missing propositions')
        all_props.extend(ann['propositions'])
        for prop in props.values():
            require(prop, 'proposition_id wording location claim_type critical critical_reason preserve')
            if prop['location'] not in case['input'] or prop['wording'] not in case['input'][prop['location']]:
                raise ValueError('Proposition wording/location must match original input')
            if prop['claim_type'] not in {'factual assertion', 'interpretation', 'opinion', 'prediction', 'aspiration', 'commitment'}:
                raise ValueError('Invalid claim type')
        if not ann['evidence_relationships']:
            raise ValueError('Missing evidence relationships')
        for rel in ann['evidence_relationships']:
            require(rel, 'proposition_id evidence_id location status establishes')
            if rel['proposition_id'] not in props or rel['status'] not in STATUSES:
                raise ValueError('Invalid proposition reference or evidence status')
            if rel['evidence_id'] is not None and rel['evidence_id'] not in case['evidence']:
                raise ValueError('Relationship cites evidence outside case')
            if rel['status'] in {'supported', 'contradicted', 'mixed'} and (rel['evidence_id'] is None or evidence[rel['evidence_id']]['availability'] == 'unavailable' or not rel['location']):
                raise ValueError('Factual verdict requires available located evidence')
    unique(all_props, 'proposition_id')
    return len(cases)


if __name__ == '__main__':
    try:
        validate_skill(ROOT / 'skills/kagami', ROOT / 'docs/contracts.md')
        count = validate_corpus(ROOT / 'eval/pilot/kagami')
    except (ValueError, KeyError, TypeError, OSError) as error:
        raise SystemExit(f'Validation failed: {error}')
    print(f'Validated Kagami package and {count} pilot records; no behavioral score implied.')
