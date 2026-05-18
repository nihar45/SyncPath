# Development

Use Python 3.10 or later. Run `python -m unittest discover -s tests -v` from the repository root. Run CLI examples with `PYTHONPATH=src` when the package is not installed, or install with `pip install -e .` in a virtual environment.

Changes should include tests for modified behavior and should keep the simulator deterministic for a fixed seed.
