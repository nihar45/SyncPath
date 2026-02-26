"""Parsing and validation of scenario configuration."""
import json
from dataclasses import dataclass
from pathlib import Path
from .domain import NetworkWindow, Operation

@dataclass(frozen=True)
class Scenario:
    operations: tuple[Operation, ...]
    windows: tuple[NetworkWindow, ...]
    deadline_ms: int
    timeout_ms: int = 250
    max_retries: int = 4
    retry_delay_ms: int = 150

    @classmethod
    def from_dict(cls, data):
        operations = tuple(Operation(**item) for item in data['operations'])
        windows = tuple(NetworkWindow(**item) for item in data['windows'])
        value = cls(operations, windows, int(data['deadline_ms']), int(data.get('timeout_ms',250)),int(data.get('max_retries',4)),int(data.get('retry_delay_ms',150)))
        value.validate()
        return value

    @classmethod
    def from_file(cls, path):
        return cls.from_dict(json.loads(Path(path).read_text(encoding='utf-8')))

    def validate(self):
        if not self.operations: raise ValueError('scenario requires operations')
        if len(set(x.id for x in self.operations)) != len(self.operations): raise ValueError('operation IDs must be unique')
        if any(op.scheduled_at_ms < 0 for op in self.operations): raise ValueError('negative schedule')
        if not self.windows: raise ValueError('scenario requires network windows')
        sorted_windows = sorted(self.windows, key=lambda w:w.start_ms)
        for i, w in enumerate(sorted_windows):
            if w.start_ms < 0 or w.end_ms <= w.start_ms: raise ValueError('invalid window duration')
            if not 0 <= w.packet_loss <= 1 or w.latency_ms < 0: raise ValueError('invalid network parameters')
            if i and w.start_ms < sorted_windows[i-1].end_ms: raise ValueError('overlapping network windows')
        if self.deadline_ms <= 0 or self.timeout_ms <= 0 or self.retry_delay_ms <= 0 or self.max_retries < 0: raise ValueError('invalid timing or retries')
