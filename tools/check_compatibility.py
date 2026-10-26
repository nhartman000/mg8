#!/usr/bin/env python3
"""Offline structural checks, not execution/semantic conformance certification."""
import hashlib
import json
import re
from pathlib import Path

from jsonschema import Draft7Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
FORMATS = {'MG8', 'ORK', 'BONIT', 'GST', 'G8SON', 'QSON'}


def require(condition, message):
    # Explicit exceptions keep verification active under python -O too.
    if not condition:
        raise ValueError(message)


def load(relative):
    return json.loads((ROOT / relative).read_text(encoding='utf-8'))


def main():
    registry_path = ROOT / 'registry/compatibility.json'
    registry = load('registry/compatibility.json')
    human = (ROOT / 'docs/COMPATIBILITY.md').read_text(encoding='utf-8')
    require(hashlib.sha256(registry_path.read_bytes()).hexdigest() in human,
            'human matrix registry hash is stale')
    authority = {row['format']: row for row in registry['authority']}
    require(len(authority) == len(registry['authority']) == len(FORMATS)
            and set(authority) == FORMATS, 'duplicate or missing format authority')
    for row in authority.values():
        require(re.fullmatch(r'[0-9a-f]{40}', row['revision']) is not None,
                'authority revision must be a full commit SHA')
        expected = f"https://github.com/{row['authority']}/blob/{row['revision']}/{row['path']}"
        require(row['source_url'] == expected and expected in human,
                'authority source URL missing or inconsistent')
    for kind in ('MG8', 'G8SON', 'QSON'):
        path = ROOT / 'compatibility/schemas' / (kind.lower() + '.json')
        require(hashlib.sha256(path.read_bytes()).hexdigest() == authority[kind]['sha256'],
                kind + ' pinned schema digest mismatch')
        Draft7Validator.check_schema(json.loads(path.read_text(encoding='utf-8')))
    # These authorities are in this checkout. GST remains a pinned external
    # conceptual document: no invented universal GST/ORK/BONIT schema test.
    for kind in ('ORK', 'BONIT'):
        row = authority[kind]
        require(hashlib.sha256((ROOT / row['path']).read_bytes()).hexdigest() == row['sha256'],
                kind + ' authority document digest mismatch')

    cases = load('compatibility/cases.json')
    require(len(cases['cases']) == cases['expected_case_count'] == 5,
            'fixture count changed without reviewing coverage')
    require(len({c['fixture'] for c in cases['cases']}) == len(cases['cases']),
            'duplicate fixture case')
    require(sum(c['expected_conformant'] is True for c in cases['cases']) == 3,
            'expected three canonical positives and two legacy mismatches')
    for case in cases['cases']:
        require(type(case['expected_conformant']) is bool, 'expected result must be Boolean')
        document = load('compatibility/' + case['fixture'])
        schema = load('compatibility/' + case['schema'])
        errors = list(Draft7Validator(schema, format_checker=FormatChecker()).iter_errors(document))
        actual = not errors
        require(actual == case['expected_conformant'],
                repr((case, [e.message for e in errors])))
        print(('CONFORMANT' if actual else 'EXPECTED_PROFILE_MISMATCH') + ': ' + case['fixture'])

    profiles = registry['profiles']
    require(len({p['id'] for p in profiles}) == len(profiles) == 6,
            'duplicate or missing named profile')
    repos = load('registry/repositories.json')['repositories']
    require(len({r['subsystem'] for r in repos}) == len(repos), 'duplicate subsystem')
    by_repo = {r['repository']: r for r in repos}
    for repo in repos:
        require(re.fullmatch(r'[0-9a-f]{40}', repo['inspected_revision']) is not None,
                'repository revision must be a full commit SHA')
    for profile in profiles:
        require(set(profile['formats']) == FORMATS, 'missing format/profile cell')
        require(profile['repository'] in by_repo, 'unknown profile repository')
        require(profile['revision'] == by_repo[profile['repository']]['inspected_revision'],
                'profile and repository baseline pins disagree')
        require(profile['source_paths'], 'profile needs pinned source paths')
        require(profile['id'] in human and profile['revision'] in human,
                'human matrix missing profile pin')
        section = human.split('### ' + profile['id'] + '\n', 1)
        require(len(section) == 2, 'human matrix missing named profile section')
        cells = section[1].split('\n##', 1)[0]
        for kind, boundary in profile['formats'].items():
            require(f'| {kind} | {boundary} |' in cells,
                    profile['id'] + ': human matrix cell differs from registry')
        for path in profile['source_paths']:
            url = f"https://github.com/{profile['repository']}/blob/{profile['revision']}/{path}"
            require(url in human, 'human matrix missing pinned profile source')
    require(authority['G8SON']['branch'] == '000', 'G8SON authority branch is 000')
    require(registry['status_axes']['mapping'] == {'UNKNOWN': 'INTERMEDIATE'},
            'unknown must never map to PASS')
    print('PASS: pinned schema/document bytes, six-format named-profile cells, baseline pins and explicit legacy mismatches')
    print('Scope: structural fixtures only; source links do not prove runtime or semantic conformance.')


if __name__ == '__main__':
    main()
