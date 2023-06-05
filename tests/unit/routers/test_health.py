import pytest
from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK

from app.main import app

test_client = TestClient(app)


@pytest.mark.unit
def test_health__ok():
    response = test_client.get("/api/v1/health")
    assert response.status_code == HTTP_200_OK
    assert response.json() == {"message": "Ok"}
