"""Discrete-event operation scheduler and retry evaluator."""
import heapq
from .domain import Attempt, RunResult
from .network import Network
from .server import Server
from .strategies import resolve_strategy


def run(scenario, strategy='immediate', seed=0):
    policy = resolve_strategy(strategy) if isinstance(strategy, str) else strategy
    network = Network(scenario.windows, seed)
    server = Server(idempotent=policy.idempotent)
    result = RunResult(policy.name, deadline_ms=scenario.deadline_ms)
    # Stable ordering within each simulated timestamp.
    heap = [(o.scheduled_at_ms, index, o, 0) for index, o in enumerate(scenario.operations)]
    heapq.heapify(heap)
    ticket = len(heap)
    while heap:
        at_ms, _, op, retries = heapq.heappop(heap)
        if at_ms >= scenario.deadline_ms or op.id in result.completed_ids:
            continue
        window = network.at(at_ms)
        offline = window is None or not window.available
        if offline and policy.queue_while_offline:
            next_time = min((w.start_ms for w in network.windows if w.available and w.start_ms > at_ms), default=None)
            if next_time is not None and next_time < scenario.deadline_ms:
                heapq.heappush(heap, (next_time, ticket, op, retries)); ticket += 1
            else: result.attempts.append(Attempt(op.id, at_ms, False, False, 'deadline-or-no-network'))
            continue
        success, latency, reason = network.transmit(at_ms)
        ack = success and latency <= scenario.timeout_ms
        if success: server.receive(op)
        if ack: result.completed_ids.add(op.id)
        result.attempts.append(Attempt(op.id, at_ms, success, ack, reason if ack else ('ack-timeout' if success else reason)))
        if not ack and policy.retries and retries < scenario.max_retries:
            next_at = at_ms + max(scenario.retry_delay_ms * (2**retries), latency)
            if next_at < scenario.deadline_ms:
                heapq.heappush(heap, (next_at, ticket, op, retries+1)); ticket += 1
    result.side_effect_ids = server.applied
    return result
