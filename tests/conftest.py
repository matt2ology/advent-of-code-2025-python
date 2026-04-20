import pytest
from src.io import load_input_file


@pytest.fixture
def load_input_file_fixture():
    return load_input_file
