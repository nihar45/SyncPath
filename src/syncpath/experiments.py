"""Reproducible strategy comparison across a common scenario."""
from .simulator import run
from .metrics import summarize
from .strategies import STRATEGIES

def compare(scenario, seed=0):
    return [summarize(run(scenario, name, seed),len(scenario.operations)) for name in STRATEGIES]
