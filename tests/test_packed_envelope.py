"""Envelope conformance only; archive interoperability is verified by product tests."""
import copy
import json
from pathlib import Path
import unittest
from jsonschema import Draft7Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT/'schema/packed-container.schema.json').read_text())
VALIDATOR = Draft7Validator(SCHEMA)

class EnvelopeTests(unittest.TestCase):
    def envelope(self, kind='unit'):
        return {'profile': 'mg8-packed/1.0' if kind == 'unit' else 'mg8pk-packed/1.0',
                'kind': kind, 'manifest': 'manifest.json',
                'integrity': {'manifest.json': 'a'*64, 'flow.ork': '0'*64}}

    def test_schema_is_valid(self):
        Draft7Validator.check_schema(SCHEMA)

    def test_unit_and_package_envelopes(self):
        for kind in ['unit', 'package']:
            with self.subTest(kind=kind):
                self.assertFalse(list(VALIDATOR.iter_errors(self.envelope(kind))))

    def test_mismatched_kind_version_or_manifest_rejected(self):
        for key, value in [('profile','mg8-packed/99'), ('kind','package'),
                           ('manifest','elsewhere.json')]:
            obj=self.envelope();obj[key]=value
            with self.subTest(key=key):
                self.assertTrue(list(VALIDATOR.iter_errors(obj)))

    def test_paths_outside_portable_subset_rejected(self):
        for path in ['../escape', '/absolute', 'a/../b', './x', 'a//b', 'a/./b',
                     'C:/x', 'a\\b', 'folder/', 'a\x00b', 'container.json', 'é.txt']:
            obj=self.envelope();obj['integrity']={path:'0'*64}
            with self.subTest(path=repr(path)):
                self.assertTrue(list(VALIDATOR.iter_errors(obj)))

    def test_missing_or_extra_fields_rejected(self):
        for key in self.envelope():
            obj=self.envelope();del obj[key]
            self.assertTrue(list(VALIDATOR.iter_errors(obj)))
        obj=self.envelope();obj['executable']='anything'
        self.assertTrue(list(VALIDATOR.iter_errors(obj)))

    def test_bad_hashes_and_empty_integrity_rejected(self):
        for value in ['', 'a'*63, 'G'*64, 'A'*64, None, 12]:
            obj=self.envelope();obj['integrity']['manifest.json']=value
            self.assertTrue(list(VALIDATOR.iter_errors(obj)))
        obj=self.envelope();obj['integrity']={}
        self.assertTrue(list(VALIDATOR.iter_errors(obj)))

if __name__ == '__main__':
    unittest.main()
