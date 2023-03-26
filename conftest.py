from pathlib import Path

import pytest


@pytest.fixture
def resources_path():
    path = Path(__file__)
    return path.parent / "tests" / "resources"
