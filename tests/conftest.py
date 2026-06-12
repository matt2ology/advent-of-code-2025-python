import pytest
from src.io import load_input_file


@pytest.fixture
def load_input_file_fixture():
    """
    Provide the `load_input_file` function as a pytest fixture.

    This allows tests to receive the file-loading utility through
    dependency injection rather than importing it directly.

    Returns:
        Callable[[str], list[str]]: Function that loads and returns
        the contents of an input file as a list of strings.
    """
    # Return the application utility function so tests can call it
    # with different input filenames as needed.
    return load_input_file
