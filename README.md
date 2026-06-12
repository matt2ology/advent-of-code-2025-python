# advent-of-code-2025-python

Execute pytest

```shell
pytest tests
```

## Running Advent of Code Solutions

This project uses `src` as a Python package. Run solution files as modules from the project root:

```bash
python -m src.day_01
```

General format:

```bash
python -m src.day_xx
```

Examples:

```bash
python -m src.day_01
python -m src.day_02
python -m src.day_03
```

### Why not `python src/day_01.py`?

Running a file directly changes Python's import resolution
and can cause errors such as:

```text
ModuleNotFoundError: No module named 'src'
```

Using `python -m src.day_01` ensures that imports like:

```python
from src.base_day import BaseDay
from src.io import load_input_file
```

work correctly.
