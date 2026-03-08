"""Delivery strategies, intentionally modeled as explicit policy objects."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Strategy:
    name: str
    queue_while_offline: bool
    retries: bool
    idempotent: bool

STRATEGIES = {
    'immediate': Strategy('immediate', False, False, False),
    'retry': Strategy('retry', False, True, False),
    'queue-retry': Strategy('queue-retry', True, True, False),
    'queue-retry-idempotent': Strategy('queue-retry-idempotent', True, True, True),
}

def resolve_strategy(name):
    try: return STRATEGIES[name]
    except KeyError as exc: raise ValueError(f'unknown strategy: {name}') from exc
