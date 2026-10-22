#!/usr/bin/env python3
"""Read-only inventory and heuristic dependency scan of a ZIP archive.

Does NOT execute archived scripts or validate numerical results.
"""
import argparse
import csv
import hashlib
import json
import re
from pathlib import Path
from zipfile import ZipFile, BadZipFile

ABS_PATH = re.compile(r"/mnt/data/[A-Za-z0-9_./+\-]+")
FILE_REF = re.compile(r"(?<![\w/])([A-Za-z][A-Za-z0-9_.-]*\.(?:json|npz|py|zip|txt|csv|dat))")
STAMP = re.compile(r"_\d{8}_\d{6}_\d{3}(?=\.)")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive', type=Path)
    parser.add_argument('--out', type=Path, default=Path('audit_results'))
    args = parser.parse_args()
    if not args.archive.is_file():
        parser.error('ZIP archive not found')
    args.out.mkdir(parents=True, exist_ok=True)
    sha = hashlib.sha256()
    with args.archive.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            sha.update(chunk)
    inventory, findings = [], []
    try:
        with ZipFile(args.archive) as z:
            names = {Path(info.filename).name for info in z.infolist() if not info.is_dir()}
            aliases = {STAMP.sub('', name) for name in names}
            for info in z.infolist():
                if info.is_dir():
                    continue
                ext = Path(info.filename).suffix.lower()
                inventory.append({'path':info.filename,'bytes':info.file_size,'extension':ext})
                if ext != '.py':
                    continue
                if info.file_size > 10_000_000:
                    findings.append({'script':info.filename,'kind':'skipped_large_script','value':str(info.file_size),'note':'Manual review required'})
                    continue
                code = z.read(info).decode('utf-8', errors='replace')
                for match in sorted(set(ABS_PATH.findall(code))):
                    findings.append({'script':info.filename,'kind':'absolute_path','value':match,'note':'Manual dependency check required'})
                for ref in sorted(set(FILE_REF.findall(code))):
                    if ref not in names:
                        note = 'timestamp alias exists' if ref in aliases else 'not found by basename in ZIP; may be generated/external'
                        findings.append({'script':info.filename,'kind':'unresolved_literal_reference','value':ref,'note':note})
    except BadZipFile as exc:
        parser.error(f'Invalid ZIP: {exc}')
    with (args.out/'inventory.csv').open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['path','bytes','extension']); w.writeheader(); w.writerows(inventory)
    with (args.out/'static_findings.csv').open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['script','kind','value','note']); w.writeheader(); w.writerows(findings)
    summary = {'archive':args.archive.name,'sha256':sha.hexdigest(),'file_count':len(inventory),'python_count':sum(x['extension']=='.py' for x in inventory),'static_findings':len(findings),'warning':'Heuristic scan only; no scripts executed and no numbers reproduced'}
    (args.out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary,indent=2))

if __name__ == '__main__':
    main()
