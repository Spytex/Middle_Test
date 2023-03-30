import pytest
from main import Loader


@pytest.fixture()
def loader():
    return Loader()

