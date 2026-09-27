"""Build distributable archives from an explicit allowlist; no network or secrets."""
from pathlib import Path
import hashlib
import json
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]

def build():
    paths = json.loads((ROOT / 'package-files.json').read_text())
    entries = []
    for name in paths:
        p = ROOT / name
        if not name.startswith('skills/finhood-analyst/') or '..' in Path(name).parts:
            raise ValueError('Invalid package path')
        if p.is_symlink() or not p.is_file():
            raise ValueError(f'Missing or unsafe file: {name}')
        if ROOT not in p.resolve().parents:
            raise ValueError('Path escapes repository')
        entries.append((name, p.read_bytes()))
    dist = ROOT / 'dist'
    dist.mkdir(exist_ok=True)
    def write(name, files):
        with ZipFile(dist / name, 'w', ZIP_DEFLATED) as z:
            for path, data in sorted(files):
                info = ZipInfo(path, (2026, 9, 27, 0, 0, 0))
                info.compress_type = ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                z.writestr(info, data)
    license_bytes = (ROOT / 'LICENSE').read_bytes()
    write('finhood-analyst-skill.zip',
          [(p.removeprefix('skills/'), b) for p, b in entries]
          + [('finhood-analyst/LICENSE', license_bytes)])
    write('finhood-analyst-plugin.zip', entries + [
        ('.claude-plugin/plugin.json', (ROOT / '.claude-plugin/plugin.json').read_bytes()),
        ('LICENSE', license_bytes)])
    hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
              for p in sorted(dist.glob('*.zip'))}
    (dist / 'SHA256SUMS').write_text(''.join(f'{v}  {k}\n' for k, v in hashes.items()))
    return hashes

if __name__ == '__main__':
    print(json.dumps(build(), indent=2))
