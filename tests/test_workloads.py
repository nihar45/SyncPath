import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'src'))
from syncpath.config import Scenario
from syncpath.workloads import expand

class WorkloadTests(unittest.TestCase):
    def test_90_operations_have_distinct_ids(self):
        s=Scenario.from_file(Path(__file__).parents[1]/'examples/handoff.json')
        expanded=expand(s,90)
        self.assertEqual(len(expanded.operations),90)
        self.assertEqual(len({o.id for o in expanded.operations}),90)
