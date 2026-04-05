"""Lightweight documentation corpus with stable citation identifiers."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Passage:
    id: str
    title: str
    text: str
    source: str

PASSAGES = [
    Passage('NET-001','Offline queue','When a device is offline, queuing defers a write until connectivity resumes. A deadline bounds how long the operation can wait.','docs/guide.md#offline-queue'),
    Passage('NET-002','Retry policy','Retries improve completion after transient loss but cannot guarantee delivery. Retry limits and exponential backoff prevent unlimited work.','docs/guide.md#retry-policy'),
    Passage('NET-003','Idempotency','Idempotency keys let the server recognize repeat submissions of the same logical operation and avoid duplicate business effects.','docs/guide.md#idempotency'),
    Passage('NET-004','Acknowledgments','A write may reach the server even when its acknowledgment times out. Client completion and server-side effects should be measured separately.','docs/guide.md#acknowledgments'),
    Passage('NET-005','Network handoffs','Switches between Wi-Fi and cellular can create a disconnected interval. An operation may need to wait or retry after a handoff.','docs/guide.md#network-handoffs'),
]
