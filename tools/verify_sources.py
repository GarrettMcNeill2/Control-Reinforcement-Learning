#!/usr/bin/env python3
"""Check copied source artifacts against the packaging manifest."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    manifest = json.loads((ROOT / 'docs/source-manifest.json').read_text())
    failed = []
    for item in manifest:
        path = ROOT / item['path']
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
            failed.append(item['path'])
    if failed:
        raise SystemExit('Source integrity check failed: ' + ', '.join(failed))
    print(f'PASS: {len(manifest)} copied artifacts match their recorded SHA-256 checksums.')

if __name__ == '__main__':
    main()
