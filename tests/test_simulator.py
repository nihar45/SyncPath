import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'src'))
from syncpath.config import Scenario
from syncpath.simulator import run

class SimulatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.scenario=Scenario.from_file(Path(__file__).parents[1]/'examples/handoff.json')
    def test_retry_queue_improves_completion(self):
        immediate=run(self.scenario,'immediate',17)
        queued=run(self.scenario,'queue-retry-idempotent',17)
        self.assertGreaterEqual(len(queued.completed_ids),len(immediate.completed_ids))
    def test_idempotent_no_duplicate_effects(self):
        result=run(self.scenario,'queue-retry-idempotent',17)
        self.assertEqual(result.duplicate_effects,0)
    def test_repeatable(self):
        a=run(self.scenario,'retry',25);b=run(self.scenario,'retry',25)
        self.assertEqual(a.attempts,b.attempts)
