import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve('.');
const failures = [];

function walk(dir) {
  for (const name of fs.readdirSync(dir)) {
    if (name === 'node_modules' || name === '.git') continue;
    const full = path.join(dir, name);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) walk(full);
    else if (full.endsWith('.html')) checkHtml(full);
  }
}

function checkHtml(file) {
  const html = fs.readFileSync(file, 'utf8');
  for (const match of html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)) {
    try {
      JSON.parse(match[1]);
    } catch (error) {
      failures.push(`${path.relative(root, file)}: invalid JSON-LD: ${error.message}`);
    }
  }
  for (const match of html.matchAll(/(?:href|src)="([^"]+)"/g)) {
    let url = match[1];
    if (/^(https?:|tel:|mailto:|#|data:)/.test(url)) continue;
    url = url.split('#')[0].split('?')[0];
    if (!url) continue;
    const target = path.normalize(path.join(path.dirname(file), url));
    if (!fs.existsSync(target)) failures.push(`${path.relative(root, file)}: missing ${match[1]}`);
  }
}

walk(root);

if (failures.length) {
  console.error(failures.slice(0, 100).join('\n'));
  process.exit(1);
}

console.log('static validation passed');
