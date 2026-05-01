import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'src'))
from syncpath.rag.retriever import retrieve
from syncpath.rag.assistant import answer

class RetrievalTests(unittest.TestCase):
    def test_idempotency_relevant(self):
        self.assertEqual(retrieve('How does idempotency work?')[0].id,'NET-003')
    def test_unknown_topic_abstains(self):
        self.assertIn('could not find',answer('quartz orchard nebula'))
    def test_answer_cites_source(self):
        self.assertIn('NET-003',answer('idempotency'))
