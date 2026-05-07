"""Generate repeatable larger workloads with no external dependencies."""
from dataclasses import replace
from .domain import Operation

def expand(scenario, count=90, gap_ms=60):
    if count < 1 or gap_ms < 1: raise ValueError('count and gap must be positive')
    ops=tuple(Operation(f'op-{i+1:03d}',i*gap_ms,scenario.operations[i%len(scenario.operations)].payload) for i in range(count))
    return replace(scenario,operations=ops)
