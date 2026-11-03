/* Reproducible test fixtures built through the actual extension APIs; no AI calls. */
const fs = require('node:fs');
const path = require('node:path');
(async () => {
  const extension = process.argv[2];
  const output = process.argv[3];
  const P = require(path.join(extension, 'src/packed.js'));
  const I = require(path.join(extension, 'src/icm.js'));
  const input = JSON.parse(fs.readFileSync(path.join(extension, 'examples/icm-input.json'), 'utf8'));
  const workspace = await I.workspace(input.collection, input.plan, {timestamp: input.timestamp});
  const original = workspace.units[0].bytes;
  fs.writeFileSync(path.join(output, 'original.mg8'), original);
  const extra = P.json({g8son_version: '1.0', file_id: 'interop-added-file', gates: [
    {gate_id: 'interop-added-gate', type: 'human.review', conditions: ['Retain the source marker provenance.']}
  ]});
  fs.writeFileSync(path.join(output, 'updated.mg8'), await P.addGates(original,
    [{name: 'interop-added.g8son', bytes: extra}], input.timestamp));
  const source = await P.readUnit(original);
  const gateFiles = Object.fromEntries(source.manifest.gates.map(p => [p, source.members[p]]));
  const state = P.parseJSON(source.members[source.manifest.state[0]]);
  const units = [];
  for (let n = 1; n <= 12; n++) {
    units.push({name: 'unit-'+n+'.mg8', bytes: await P.createUnit({
      unit_id: 'interop-unit-'+n, state, gateFiles, timestamp: input.timestamp
    })});
  }
  for (const n of [4, 6, 8, 12]) {
    fs.writeFileSync(path.join(output, 'ordered-'+n+'.mg8pk'),
      await P.createPackage({package_id: 'interop-package-'+n, units: units.slice(0,n)}));
  }
})().catch(error => {console.error(error); process.exit(1);});
