"""Display top-one document-retrieval evaluation."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from syncpath.rag.evaluation import evaluate_top1

if __name__=='__main__':
    result=evaluate_top1()
    print(f"top-1: {result['correct']}/{result['total']}")
    for query,expected,actual in result['cases']:
        print(f'{query}: expected={expected}, retrieved={actual}')
