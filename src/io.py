from pathlib import Path

# Project root directory (resolved from this file's location, two levels up)
BASE_DIR = Path(__file__).resolve().parent.parent


def load_input_file(filename: str) -> list[str]:
    """
    Load an input file from the project's input directory.

    Args:
        filename (str): Name of the file located in the ``input`` directory.

    Raises:
        FileNotFoundError: If the specified input file does not exist.

    Returns:
        list[str]: A list of lines from the file with
            trailing newline characters removed.
    """
    file_path = BASE_DIR / "input" / filename

    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    return file_path.read_text(encoding="utf-8").splitlines()
