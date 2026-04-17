import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'src'))
from syncpath.config import Scenario

class ScenarioTests(unittest.TestCase):
    def test_example_valid(self):
        s=Scenario.from_file(Path(__file__).parents[1]/'examples/handoff.json')
        self.assertEqual(len(s.operations),5)

    def test_duplicate_ids_rejected(self):
        data={'operations':[{'id':'a','scheduled_at_ms':0,'payload':'x'},{'id':'a','scheduled_at_ms':1,'payload':'x'}],'windows':[{'start_ms':0,'end_ms':10}],'deadline_ms':10}
        with self.assertRaisesRegex(ValueError,'unique'):Scenario.from_dict(data)

    def test_overlap_rejected(self):
        data={'operations':[{'id':'a','scheduled_at_ms':0,'payload':'x'}],'windows':[{'start_ms':0,'end_ms':10},{'start_ms':9,'end_ms':20}],'deadline_ms':20}
        with self.assertRaisesRegex(ValueError,'overlapping'):Scenario.from_dict(data)
