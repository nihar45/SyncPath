# Python dependencies

SyncPath's simulator, CLI, built-in retrieval assistant, benchmarking scripts,
and unit tests currently use **only Python standard-library modules**.

- **Python:** 3.10 or later.
- **Runtime packages:** none beyond the standard library.
- **Build backend:** `setuptools>=68`, declared under `[build-system]` in
  `pyproject.toml`. This is used when installing/building, not at runtime.
- **Tests:** `unittest` (standard library); no third-party test runner required.

## Setup

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

The requirements file installs the local `syncpath-lab` project in editable
mode; it does **not** install third-party runtime packages. Do not commit a
`site-packages/` directory or generated virtual environment. Optional hosted
LLM integrations are not part of the current runtime and no provider SDK is
required.

This repository does not include a dependency lockfile. If dependencies are
added later, document them in `pyproject.toml`, update this inventory, and
review the supply chain before publishing.
