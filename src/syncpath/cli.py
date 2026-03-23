"""Command-line interface with local reproducibility defaults."""
import argparse
import json
from .config import Scenario
from .simulator import run
from .metrics import summarize
from .experiments import compare
from .reporting import render_table, render_json

def main(argv=None):
    parser=argparse.ArgumentParser(prog='syncpath',description='Network resilience lab')
    sub=parser.add_subparsers(dest='command',required=True)
    for command in ('run','compare'):
        p=sub.add_parser(command)
        p.add_argument('--scenario',required=True)
        p.add_argument('--seed',type=int,default=17)
        p.add_argument('--format',choices=['table','json'],default='table')
        if command=='run':p.add_argument('--strategy',default='immediate')
    ask=sub.add_parser('ask');ask.add_argument('question')
    args=parser.parse_args(argv)
    if args.command=='ask':
        from .rag.assistant import answer
        print(answer(args.question));return 0
    scenario=Scenario.from_file(args.scenario)
    rows=[summarize(run(scenario,args.strategy,args.seed),len(scenario.operations))] if args.command=='run' else compare(scenario,args.seed)
    print(render_json(rows) if args.format=='json' else render_table(rows))
    return 0

if __name__=='__main__':raise SystemExit(main())
