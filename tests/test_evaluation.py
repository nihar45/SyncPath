import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'src'))
from syncpath.rag.evaluation import evaluate_top1

class EvaluationTests(unittest.TestCase):
    def test_retrieval_accuracy(self):
        result=evaluate_top1()
        self.assertGreaterEqual(result['correct'],4)
