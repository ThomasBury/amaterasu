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


def test_real_corpus_and_shared_rules():
    assert validate_corpus(ROOT / 'eval/pilot/kagami') == 20
    validate_skill(ROOT / 'skills/kagami', ROOT / 'docs/contracts.md')


def test_standalone_package(tmp_path):
    skill = tmp_path / 'kagami'
    shutil.copytree(ROOT / 'skills/kagami', skill)
    validate_skill(skill)
    for reference in (skill / 'references').glob('*.md'):
        assert reference.read_text().strip()
    (skill / 'references/evidence-and-arguments.md').unlink()
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
