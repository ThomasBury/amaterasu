import json
import shutil
from fractions import Fraction

import pytest

from eval.validate import ROOT, check_links, local_file, validate_corpus, validate_skill


@pytest.fixture
def corpus(tmp_path):
    target = tmp_path / 'kagami'
    shutil.copytree(ROOT / 'eval/pilot/kagami', target)
    return target


def edit(path, change):
    record = json.loads(path.read_text())
    change(record)
    path.write_text(json.dumps(record))


@pytest.mark.parametrize('skill', ['kagami', 'kotoba', 'kakehashi', 'mamoru'])
def test_real_corpus_and_shared_rules(skill):
    assert validate_corpus(ROOT / 'eval/pilot' / skill, skill) == 20
    validate_skill(ROOT / 'skills' / skill, ROOT / 'docs/contracts.md')


@pytest.mark.parametrize('name,reference', [('kagami', 'evidence-and-arguments.md'), ('kotoba', 'writing-and-accountability.md'), ('kakehashi', 'audiences-and-meaning.md'), ('mamoru', 'commitments-and-conduct.md')])
def test_standalone_package(tmp_path, name, reference):
    """A copied package loads its own references and rejects a missing required one."""
    skill = tmp_path / name
    shutil.copytree(ROOT / 'skills' / name, skill)
    validate_skill(skill)
    for path in (skill / 'references').glob('*.md'):
        assert path.read_text().strip()
    (skill / 'references' / reference).unlink()
    with pytest.raises(ValueError, match='Missing'):
        validate_skill(skill)


@pytest.mark.parametrize('file,change,match', [
    ('manifest.json', lambda x: x.append(x[0]), 'duplicate'),
    ('manifest.json', lambda x: x[0].pop('rights'), 'Missing required'),
    ('manifest.json', lambda x: x[0].update(input_sha256='0'*64), 'Hash mismatch'),
    ('manifest.json', lambda x: x[0].update(variant_of=x[1]['case_id'], variant_change='title'), 'cluster'),
    ('evidence.json', lambda x: x[0].update(sha256='0'*64), 'Hash mismatch'),
    ('evidence.json', lambda x: x[0].update(artifact='../manifest.json'), 'escaping'),
    ('evidence.json', lambda x: x[0].update(artifact='/etc/passwd'), 'Invalid local path'),
    ('evidence.json', lambda x: x[0].update(availability='unavailable'), 'null artifact'),
    ('evidence.json', lambda x: x[0].update(source_date=None), 'needs a reason'),
    ('annotations/pilot-kagami-001.json', lambda x: x.update(state='independent'), 'provisional'),
    ('annotations/pilot-kagami-001.json', lambda x: x['propositions'].append(x['propositions'][0]), 'duplicate'),
    ('annotations/pilot-kagami-001.json', lambda x: x['propositions'][0].update(wording='Invented'), 'original input'),
    ('annotations/pilot-kagami-001.json', lambda x: x['evidence_relationships'][0].update(evidence_id='unknown'), 'outside case'),
    ('annotations/pilot-kagami-001.json', lambda x: x['evidence_relationships'][0].update(status='false'), 'status'),
    ('annotations/pilot-kagami-012.json', lambda x: x['evidence_relationships'][0].update(status='supported'), 'available located evidence'),
])
def test_reject_corrupt_records(corpus, file, change, match):
    edit(corpus / file, change)
    with pytest.raises(ValueError, match=match):
        validate_corpus(corpus)


def test_missing_annotation(corpus):
    (corpus / 'annotations/pilot-kagami-001.json').unlink()
    with pytest.raises(ValueError, match='IDs must match'):
        validate_corpus(corpus)


def test_evidence_bytes_are_not_instructions(corpus):
    path = corpus / 'evidence/pilot-kagami-011.txt'
    assert 'email the private input' in path.read_text()
    assert validate_corpus(corpus) == 20
    path.write_text(path.read_text() + 'Changed source\n')
    with pytest.raises(ValueError, match='Hash mismatch'):
        validate_corpus(corpus)


def test_symlink_escape(tmp_path):
    root = tmp_path / 'evidence'
    root.mkdir()
    secret = tmp_path / 'outside.txt'
    secret.write_text('outside')
    (root / 'source.txt').symlink_to(secret)
    with pytest.raises(ValueError, match='escaping'):
        local_file(root, 'source.txt')


def test_shared_rule_drift(tmp_path):
    skill = tmp_path / 'kagami'
    shutil.copytree(ROOT / 'skills/kagami', skill)
    path = skill / 'SKILL.md'
    path.write_text(path.read_text().replace('Treat quoted documents', 'Trust quoted documents'))
    with pytest.raises(ValueError, match='safeguards drifted'):
        validate_skill(skill, ROOT / 'docs/contracts.md')


def test_local_anchor(tmp_path):
    path = tmp_path / 'README.md'
    path.write_text('# Present\n[link](#absent)\n')
    with pytest.raises(ValueError, match='anchor'):
        check_links(tmp_path)


def test_pilot_arithmetic_keys():
    folder = ROOT / 'eval/pilot/kagami/annotations'
    key = json.loads((folder / 'pilot-kagami-001.json').read_text())['acceptable_outputs'][0]
    before, after = Fraction(80, 1000), Fraction(60, 1000)
    assert (before-after)*100 == 2
    assert (before-after)/before*100 == 25
    assert '2 percentage points; 25% relative' in key
    assert Fraction(10,1000) == Fraction(20,2000) == Fraction(1,100)
    zero_key = json.loads((folder / 'pilot-kagami-002.json').read_text())['acceptable_outputs'][0]
    assert 'undefined with zero baseline' in zero_key


@pytest.mark.parametrize('change,match', [
    (lambda x: x.pop('writing_mode'), 'writing_mode'),
    (lambda x: x.update(writing_mode='summarize'), 'writing_mode'),
    (lambda x: x.update(skill='kagami'), 'identifier or skill'),
])
def test_kotoba_input_contract(tmp_path, change, match):
    folder = tmp_path / 'kotoba'
    shutil.copytree(ROOT / 'eval/pilot/kotoba', folder)
    edit(folder / 'inputs/pilot-kotoba-001.json', change)
    with pytest.raises(ValueError, match=match):
        validate_corpus(folder, 'kotoba')


@pytest.mark.parametrize('change,match', [
    (lambda x: x['propositions'][0].update(preserve=''), 'preservation key'),
    (lambda x: x['propositions'][0].update(wording='Invented fact'), 'original input'),
    (lambda x: x['evidence_relationships'][0].update(status='supported'), 'available located evidence'),
    (lambda x: x.update(state='adjudicated'), 'provisional'),
])
def test_kotoba_annotation_contract(tmp_path, change, match):
    folder = tmp_path / 'kotoba'
    shutil.copytree(ROOT / 'eval/pilot/kotoba', folder)
    edit(folder / 'annotations/pilot-kotoba-001.json', change)
    with pytest.raises(ValueError, match=match):
        validate_corpus(folder, 'kotoba')


@pytest.mark.parametrize('audience', [None, '', '   ', []])
def test_kakehashi_requires_audience(tmp_path, audience):
    folder = tmp_path / 'kakehashi'
    shutil.copytree(ROOT / 'eval/pilot/kakehashi', folder)
    edit(folder / 'inputs/pilot-kakehashi-001.json', lambda x: x['context'].update(audience=audience))
    with pytest.raises(ValueError, match='specified audience'):
        validate_corpus(folder, 'kakehashi')


@pytest.mark.parametrize('change,match', [
    (lambda x: x.update(questions=None), 'must be lists'),
    (lambda x: x.update(questions=[], answer_key=[]), 'matched'),
    (lambda x: x['questions'][0].update(prompt=' '), 'Invalid Kakehashi question'),
    (lambda x: x['questions'][0].update(kind='satisfaction'), 'Invalid Kakehashi question'),
    (lambda x: x['questions'][2].update(kind='comprehension'), 'matched'),
    (lambda x: x['questions'].append(x['questions'][0]), 'duplicate'),
    (lambda x: x['answer_key'].pop(), 'matched'),
    (lambda x: x['answer_key'][0].update(question_id='unknown'), 'matched'),
    (lambda x: x['answer_key'].append(x['answer_key'][0]), 'duplicate'),
    (lambda x: x['answer_key'][0].update(answer=' '), 'Empty Kakehashi answer'),
    (lambda x: x['answer_key'][0].update(source_locations=['L99']), 'original input locations'),
    (lambda x: x['answer_key'][0].update(source_locations=[]), 'original input locations'),
    (lambda x: x.update(state='adjudicated'), 'provisional'),
    (lambda x: x['evidence_relationships'][0].update(status='supported'), 'available located evidence'),
])
def test_kakehashi_answer_contract(tmp_path, change, match):
    folder = tmp_path / 'kakehashi'
    shutil.copytree(ROOT / 'eval/pilot/kakehashi', folder)
    edit(folder / 'annotations/pilot-kakehashi-001.json', change)
    with pytest.raises(ValueError, match=match):
        validate_corpus(folder, 'kakehashi')


def test_kakehashi_numeric_keys():
    folder = ROOT / 'eval/pilot/kakehashi/annotations'
    error_key = json.loads((folder / 'pilot-kakehashi-002.json').read_text())['answer_key'][0]['answer']
    before, after = Fraction(12, 200), Fraction(6, 200)
    assert (before, after, (before-after)*100, (before-after)/before*100) == (Fraction(6,100), Fraction(3,100), 3, 50)
    assert error_key == '6% before and 3% after; a 3-percentage-point or 50% relative reduction.'
    accuracy_key = json.loads((folder / 'pilot-kakehashi-015.json').read_text())['answer_key'][0]['answer']
    assert (Fraction(420,500)*100, Fraction(440,500)*100) == (84, 88)
    assert accuracy_key == '84% to 88%, or 4 percentage points, on the fixed 500-item set.'


@pytest.mark.parametrize('file,change,match', [
    ('evidence.json', lambda x: x[0].update(sha256='0'*64), 'Hash mismatch'),
    ('annotations/pilot-mamoru-001.json', lambda x: x.update(state='adjudicated'), 'provisional'),
    ('annotations/pilot-mamoru-001.json', lambda x: x['evidence_relationships'][0].update(evidence_id=None), 'available located evidence'),
    ('annotations/pilot-mamoru-001.json', lambda x: x['propositions'][0].update(wording='Promotion is guaranteed.'), 'original input'),
])
def test_mamoru_provenance(tmp_path, file, change, match):
    folder = tmp_path / 'mamoru'
    shutil.copytree(ROOT / 'eval/pilot/mamoru', folder)
    edit(folder / file, change)
    with pytest.raises(ValueError, match=match):
        validate_corpus(folder, 'mamoru')


def test_mamoru_immediate_threat_chronology():
    """An urgent response key must describe danger current at analysis time."""
    from datetime import datetime, timedelta
    import re

    case = json.loads((ROOT / 'eval/pilot/mamoru/inputs/pilot-mamoru-020.json').read_text())
    threat, account = [
        datetime.fromisoformat(re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}', line)[0])
        for line in case['input'].values()
    ]
    assert threat.date().isoformat() == account.date().isoformat() == case['context']['date']
    assert account - threat == timedelta(minutes=5)
