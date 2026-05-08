import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'src'))
from syncpath.config import Scenario
from syncpath.simulator import run

class IdempotencyTests(unittest.TestCase):
    def test_ack_timeouts_do_not_reapply_on_idempotent_server(self):
        scenario=Scenario.from_file(Path(__file__).parents[1]/'examples/ack_timeout.json')
        normal=run(scenario,'retry',17)
        deduped=run(scenario,'queue-retry-idempotent',17)
        self.assertGreater(normal.duplicate_effects,0)
        self.assertEqual(deduped.duplicate_effects,0)
        self.assertEqual(len(deduped.side_effect_ids),1)
