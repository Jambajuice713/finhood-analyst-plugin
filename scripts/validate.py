"""Offline release checks. Requires PyYAML; does not certify live MCP or Claude."""
from pathlib import Path
from zipfile import ZipFile
import hashlib
import json
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/finhood-analyst'
REF = SKILL / 'references'

def validate():
    failures = []
    def check(ok, msg):
        if not ok: failures.append(msg)
    paths = json.loads((ROOT / 'package-files.json').read_text())
    actual = sorted(p.relative_to(ROOT).as_posix() for p in SKILL.rglob('*') if p.is_file())
    check(sorted(paths) == actual, 'Skill files differ from fixed package allowlist')
    check(len(list((REF/'skills').glob('*/SKILL.md'))) == 13, 'Expected 13 procedures')
    for p in [ROOT/'.claude-plugin/plugin.json', *ROOT.glob('package-files.json'), *REF.rglob('*.json')]:
        try: json.loads(p.read_text())
        except Exception as e: failures.append(f'Invalid JSON {p.relative_to(ROOT)}: {e}')
    for p in ROOT.rglob('*'):
        if not p.is_file() or '.git' in p.parts or p.suffix in ('.zip','.bundle'):
            continue
        if p.suffix not in ('.md','.yaml','.json') and p.name not in ('.gitignore','LICENSE'):
            continue
        s=p.read_text()
        # Known private identity/session markers and common credential shapes.
        check(not re.search(r'\bFer\b|Fernando|CAMV|ffmeza|finhood-b2b|claude\.ai/code/session_|/Users/',s,re.I),
              f'Private marker: {p.relative_to(ROOT)}')
        check(not re.search(r'\b(?:ghp_|github_pat_|sk-proj-|AKIA)[A-Za-z0-9_-]{12,}',s),
              f'Credential pattern: {p.relative_to(ROOT)}')
        if p.suffix=='.yaml':
            try: yaml.safe_load(s)
            except Exception as e: failures.append(f'Invalid YAML {p}: {e}')
        if s.startswith('---\n'):
            try:
                front=yaml.safe_load(s.split('---',2)[1])
                check(isinstance(front,dict) and bool(front.get('name')) and bool(front.get('description')), f'Missing skill metadata: {p}')
                if p==SKILL/'SKILL.md':
                    check(set(front)=={'name','description'}, 'Unexpected entry skill metadata')
                    check(front['name']=='finhood-analyst', 'Wrong skill name')
            except Exception as e: failures.append(f'Invalid frontmatter {p}: {e}')
        # Resolve actual Markdown links from the containing file.
        for target in re.findall(r'\]\(([^)]+)\)',s):
            if target.startswith(('http:','https:','#','mailto:')): continue
            check((p.parent/target.split('#')[0]).exists(), f'Broken link {p.relative_to(ROOT)} -> {target}')
        # Existing reference documents use paths from references/ by convention.
        if REF in p.parents:
            for target in re.findall(r'`((?:policy|methodology|bindings|skills|schemas|agents|config)/[^`\s]+|manifest\.yaml)`',s):
                if '*' in target: continue
                check((REF/target.rstrip('/')).exists(), f'Broken reference {p.relative_to(ROOT)} -> {target}')
    manifest=json.loads((ROOT/'.claude-plugin/plugin.json').read_text())
    check(manifest['name']=='finhood-analyst' and manifest['version']=='0.2.1', 'Plugin version mismatch')
    check(not any((ROOT/x).exists() for x in ('.mcp.json','hooks','bin')), 'Unexpected executable/MCP configuration')
    expected_skill={p.removeprefix('skills/') for p in paths}|{'finhood-analyst/LICENSE'}
    expected_plugin=set(paths)|{'.claude-plugin/plugin.json','LICENSE'}
    for archive, expected in [('finhood-analyst-skill.zip',expected_skill),('finhood-analyst-plugin.zip',expected_plugin)]:
        try:
            with ZipFile(ROOT/'dist'/archive) as z:
                check(set(z.namelist())==expected, f'Wrong archive membership: {archive}')
                check(z.testzip() is None, f'Corrupt archive: {archive}')
                for member in z.namelist():
                    check(not member.startswith('/') and '..' not in Path(member).parts, f'Unsafe archive path: {member}')
                    source=(ROOT/'LICENSE') if member.endswith('/LICENSE') else ROOT/(('skills/'+member) if archive.endswith('skill.zip') else member)
                    check(z.read(member)==source.read_bytes(), f'Stale archive member: {member}')
        except Exception as e: failures.append(f'Archive error {archive}: {e}')
    sums=ROOT/'dist/SHA256SUMS'
    if sums.exists():
        for line in sums.read_text().splitlines():
            digest,name=line.split('  ',1)
            check(hashlib.sha256((ROOT/'dist'/name).read_bytes()).hexdigest()==digest, f'Hash mismatch {name}')
    check(not any((REF/'config/user-profile.example.json').read_text().find(x)>=0 for x in ('account_id','token','password')), 'Sensitive profile fields')
    if failures:
        print('\n'.join(failures))
        return False
    print('PASS: 13 procedures; JSON/YAML; privacy markers; internal references; archive membership, content and hashes.')
    print('Scope: static validation only. Live Claude import and Zesty account calls are separate.')
    return True

if __name__=='__main__':
    sys.exit(0 if validate() else 1)
