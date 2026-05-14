import sys,tempfile,unittest,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'src'))
from syncpath.export import write_json,write_csv

class ExportTests(unittest.TestCase):
    def test_export_both_formats(self):
        with tempfile.TemporaryDirectory() as directory:
            rows=[{'strategy':'immediate','operations':1}]
            j=Path(directory)/'results.json';c=Path(directory)/'results.csv'
            write_json(rows,j);write_csv(rows,c)
            self.assertEqual(json.loads(j.read_text()),rows)
            self.assertIn('strategy,operations',c.read_text())
