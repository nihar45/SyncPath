"""Input and outcome records shared by simulator components."""
from dataclasses import dataclass, field
from typing import Optional

@dataclass(frozen=True)
class Operation:
    id: str
    scheduled_at_ms: int
    payload: str
    method: str = "POST"

@dataclass(frozen=True)
class NetworkWindow:
    start_ms: int
    end_ms: int
    available: bool = True
    latency_ms: int = 75
    packet_loss: float = 0.0
    label: str = "normal"

@dataclass
class Attempt:
    operation_id: str
    at_ms: int
    delivered: bool
    acknowledged: bool
    reason: str

@dataclass
class RunResult:
    strategy: str
    attempts: list[Attempt] = field(default_factory=list)
    completed_ids: set[str] = field(default_factory=set)
    side_effect_ids: list[str] = field(default_factory=list)
    deadline_ms: int = 0

    @property
    def completion_rate(self):
        return len(self.completed_ids)

    @property
    def duplicate_effects(self):
        return len(self.side_effect_ids) - len(set(self.side_effect_ids))
