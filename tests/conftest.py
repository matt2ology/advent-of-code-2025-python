import pytest
from src.io import load_input


@pytest.fixture
def load_input_file():
    return load_input
