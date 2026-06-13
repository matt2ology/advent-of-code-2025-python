from collections.abc import Callable
from typing import TypeAlias

import pytest
from src.io import load_input_file

# use collections.abc.Callable instead
# Give the callable signature a name so tests and fixtures can share
# a single contract. This avoids repeating the type annotation in
# multiple places if additional fixtures are added later.
LoadInputFile: TypeAlias = Callable[[str], list[str]]


@pytest.fixture
def load_input_file_fixture() -> LoadInputFile:
    # Expose the production implementation through a fixture so tests
    # can depend on the interface and swap implementations more easily
    # when mocking or overriding behavior.
    return load_input_file
