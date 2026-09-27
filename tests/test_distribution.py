"""Check that a private local file cannot silently enter a public package."""
from pathlib import Path
import importlib.util
import tempfile
import shutil
import unittest
from zipfile import ZipFile

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('package_build', ROOT/'scripts/build.py')
builder=importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)

class DistributionTest(unittest.TestCase):
    def test_unlisted_private_data_excluded_and_build_reproducible(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'repo'
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns('.git','__pycache__'))
            previous=builder.ROOT
            try:
                builder.ROOT=root
                before=builder.build()
                secret=root/'skills/finhood-analyst/references/private-account.json'
                secret.write_text('{"synthetic_private_marker":"DO_NOT_PACKAGE"}')
                (root/'.env.local').write_text('SYNTHETIC_ONLY=DO_NOT_PACKAGE\n')
                after=builder.build()
                self.assertEqual(before,after)
                for path in (root/'dist').glob('*.zip'):
                    with ZipFile(path) as archive:
                        self.assertFalse(any(b'DO_NOT_PACKAGE' in archive.read(n) for n in archive.namelist()))
            finally:
                builder.ROOT=previous

if __name__=='__main__':
    unittest.main()
