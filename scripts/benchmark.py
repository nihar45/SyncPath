"""Run the 90-operation comparison and write machine-readable results."""
import json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from syncpath.config import Scenario
from syncpath.workloads import expand
from syncpath.experiments import compare

def main():
    root=Path(__file__).resolve().parents[1]
    s=expand(Scenario.from_file(root/'examples/handoff.json'),90)
    results=compare(s,seed=17)
    print(json.dumps(results,indent=2))

if __name__=='__main__':main()
