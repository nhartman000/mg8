"""Opt-in Python/JavaScript implementation interoperability; no model calls.

Set TEXPORT_APP_ROOT and TEXPORT_EXTENSION_ROOT to independent source checkouts.
Default schema-only CI skips these tests rather than inventing cross-repo evidence.
"""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

APP = os.environ.get('TEXPORT_APP_ROOT', '')
EXT = os.environ.get('TEXPORT_EXTENSION_ROOT', '')

@unittest.skipUnless(APP and EXT, 'Set both TEXporT implementation source roots')
class PackedInteropTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.path.insert(0, APP)
        from texport import packed
        cls.packed = packed
        cls.js = str(Path(EXT)/'src/packed.js')
        cls.fixture_directory = tempfile.TemporaryDirectory(dir=os.environ.get('TMPDIR'))
        cls.addClassCleanup(cls.fixture_directory.cleanup)
        cls.fixtures = Path(cls.fixture_directory.name)
        run = subprocess.run(['node', str(Path(__file__).with_name('packed_interop_fixture.cjs')),
                              EXT, str(cls.fixtures)], capture_output=True, text=True, timeout=60)
        if run.returncode:
            raise RuntimeError(run.stdout+'\n'+run.stderr)

    def node(self, code, *args):
        run = subprocess.run(['node', '-e', code, self.js, *map(str,args)], capture_output=True,
                             text=True, timeout=60)
        self.assertEqual(run.returncode, 0, run.stdout+'\n'+run.stderr)
        return run.stdout

    def test_python_units_and_packages_are_readable_in_javascript(self):
        with tempfile.TemporaryDirectory(dir=os.environ.get('TMPDIR')) as directory:
            d=Path(directory)
            unit=(Path(APP)/'examples/packed/example.mg8').read_bytes()
            (d/'source.mg8').write_bytes(unit)
            (d/'source.mg8pk').write_bytes((Path(APP)/'examples/packed/four.mg8pk').read_bytes())
            self.node("const P=require(process.argv[1]),fs=require('fs');(async()=>{await P.readUnit(fs.readFileSync(process.argv[2]));await P.readPackage(fs.readFileSync(process.argv[3]));console.log('accepted Python unit and package')})().catch(e=>{console.error(e);process.exit(1)})",d/'source.mg8',d/'source.mg8pk')

    def test_javascript_units_and_packages_are_readable_in_python(self):
        for name in ['original.mg8','updated.mg8','ordered-4.mg8pk','ordered-6.mg8pk','ordered-8.mg8pk','ordered-12.mg8pk']:
            with self.subTest(name=name):
                result=self.packed.read((self.fixtures/name).read_bytes())
                if name.endswith('.mg8pk'):
                    self.assertEqual(len(result['manifest']['units']),int(name.split('-')[1].split('.')[0]))
                else:
                    self.assertTrue(result['manifest']['gates'])

    def test_both_writers_use_canonical_member_schemas(self):
        from jsonschema import Draft7Validator, FormatChecker
        root = Path(__file__).resolve().parents[1]
        schemas = {kind: json.loads((root/'compatibility/schemas'/f'{kind}.json').read_text())
                   for kind in ['mg8','g8son','qson']}
        envelope = json.loads((root/'schema/packed-container.schema.json').read_text())
        paths = [Path(APP)/'examples/packed/example.mg8', self.fixtures/'original.mg8']
        for path in paths:
            with self.subTest(writer=str(path)):
                unit = self.packed.read(path.read_bytes())
                Draft7Validator(envelope).validate(unit['container'])
                Draft7Validator(schemas['mg8']).validate(unit['manifest'])
                for resource in unit['manifest']['gates']:
                    Draft7Validator(schemas['g8son']).validate(self.packed.loads(unit['members'][resource]))
                Draft7Validator(schemas['qson'], format_checker=FormatChecker()).validate(
                    self.packed.loads(unit['members'][unit['manifest']['trace']]))

    def test_gate_import_round_trip_preserves_exact_sources_and_audit(self):
        with tempfile.TemporaryDirectory(dir=os.environ.get('TMPDIR')) as directory:
            d=Path(directory)
            original=(Path(APP)/'examples/packed/example.mg8').read_bytes()
            gate=(Path(APP)/'examples/packed/extra.g8son').read_bytes()
            (d/'original.mg8').write_bytes(original);(d/'extra.g8son').write_bytes(gate)
            self.node("const P=require(process.argv[1]),fs=require('fs');(async()=>{const b=await P.addGates(fs.readFileSync(process.argv[2]),[{name:'extra.g8son',bytes:fs.readFileSync(process.argv[3])}]);fs.writeFileSync(process.argv[4],b)})().catch(e=>{console.error(e);process.exit(1)})", d/'original.mg8',d/'extra.g8son',d/'js-updated.mg8')
            before=self.packed.read(original);after=self.packed.read((d/'js-updated.mg8').read_bytes())
            self.assertEqual(after['members']['gates/extra.g8son'],gate)
            for path in before['manifest']['gates']+before['manifest']['state']:
                self.assertEqual(after['members'][path],before['members'][path])
            old=self.packed.loads(before['members'][before['manifest']['trace']])['events']
            new=self.packed.loads(after['members'][after['manifest']['trace']])['events']
            self.assertEqual(new[:-1],old)
            self.assertEqual(new[-1]['event_type'],'review')
            self.assertEqual((d/'original.mg8').read_bytes(),original)
            self.assertEqual((d/'extra.g8son').read_bytes(),gate)
            # An independently authored second gate is imported by Python, then read by JS.
            obj=self.packed.loads(gate);obj['file_id']+='-two'
            for g in obj['gates']:g['gate_id']+='-two'
            second=self.packed.dump(obj)
            updated=self.packed.add_gates((d/'js-updated.mg8').read_bytes(),{'second.g8son':second})
            (d/'python-updated.mg8').write_bytes(updated)
            self.node("const P=require(process.argv[1]),fs=require('fs');P.readUnit(fs.readFileSync(process.argv[2])).then(u=>{if(!u.members['gates/second.g8son'])throw Error('missing gate')}).catch(e=>{console.error(e);process.exit(1)})",d/'python-updated.mg8')

if __name__=='__main__':unittest.main()
