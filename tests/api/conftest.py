from fastapi.testclient import TestClient
from src.main import app
import pytest


@pytest.fixture(scope="session")
def test_client():
    return TestClient(app)
