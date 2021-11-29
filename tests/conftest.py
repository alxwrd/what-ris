
import pytest

from fastapi.testclient import TestClient

import ris


@pytest.fixture
def test_client():
    return TestClient(ris.api.app)

