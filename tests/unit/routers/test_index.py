import pytest
from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK
from src.main import app

test_client = TestClient(app)


@pytest.mark.unit
def test_index__ok():
    response = test_client.get("/index")
    assert response.status_code == HTTP_200_OK
    assert response.json() == {"result": "success", "message": "Hi from coffe-shopp"}
