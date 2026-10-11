const fs = require('fs');
const content = fs.readFileSync('03_scripts/graph_builder.py', 'utf8');
const idx = content.indexOf('const SPHERES_DATA = [');
console.log('SPHERES_DATA Index:', idx);
if (idx !== -1) {
    console.log(content.substring(idx, idx + 1800));
}
