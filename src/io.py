from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def load_input_file(filename: str) -> list[str]:
    file_path = BASE_DIR / "input" / filename

    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    return file_path.read_text(encoding="utf-8").splitlines()
