# SyncPath

SyncPath is a reproducible network-resilience laboratory for evaluating mobile application operations during latency, packet loss, disconnects, and network handoffs. It compares delivery strategies under the same simulated workload and provides a documentation-grounded support assistant.

**Built as a reconstructed implementation based on the project requirements.** All measured results depend on the supplied scenario and random seed; simulation outcomes are not production guarantees.

## Quick start

```bash
python -m pip install -e .
python -m syncpath.cli run --scenario examples/handoff.json --strategy queue-retry --seed 17
python -m syncpath.cli compare --scenario examples/handoff.json --seed 17
python -m syncpath.cli ask 'How does idempotency protect against duplicates?'
python -m unittest discover -s tests -v
```

The base simulator and retrieval assistant use only Python's standard library. The local retrieval assistant runs without a hosted LLM. A future provider integration would require an explicitly configured endpoint and API key; no secrets are shipped.

See [architecture](docs/architecture.md), [configuration](docs/configuration.md), and [limits](docs/limitations.md).
