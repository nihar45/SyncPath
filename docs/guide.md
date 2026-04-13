# Network resilience guide

## Offline queue

When there is no network, wait for the next available window rather than dropping every request. Queued requests must still respect deadlines.

## Retry policy

Use bounded exponential backoff for transient failures. A retry after a lost acknowledgment may repeat a successfully delivered request.

## Idempotency

Send a stable operation identifier and deduplicate on the server. A stable identifier is essential; changing it on each retry defeats deduplication.

## Acknowledgments

Distinguish acknowledged completions from server-applied effects. Timeouts can make the client uncertain whether a remote write happened.

## Network handoffs

A Wi-Fi-to-cellular transition can interrupt an in-flight operation and cause temporary unavailability.
