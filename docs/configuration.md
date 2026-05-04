# Configuration

A scenario supplies `operations`, `windows`, and `deadline_ms`. Optional parameters are `timeout_ms`, `max_retries`, and `retry_delay_ms`.

Each operation has an `id`, `scheduled_at_ms`, and `payload`. Each window has `start_ms`, `end_ms`, `available`, `latency_ms`, `packet_loss`, and an optional label. Windows must not overlap.

The same `--seed` makes a strategy reproducible. Loss is simulated with a local pseudorandom generator. Comparisons share a seed, but may consume random draws differently because strategies submit different attempts.
