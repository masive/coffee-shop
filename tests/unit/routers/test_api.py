import pytest
from datetime import datetime
from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK
from src.main import app

test_client = TestClient(app)


@pytest.mark.unit
def test_health__ok():
    response = test_client.get("/health")
    assert response.status_code == HTTP_200_OK
    assert response.json() == {"message": "Ok"}


@pytest.mark.unit
def test_customers_with_birthday__ok():
    expected = {
        "customer_id": 12345,
        "customer_first_name": "Joe Doe",
        "birthdate": str(datetime.today().date()),
        "is_birthday": True
    }
    response = test_client.get("/customers/birthday")
    assert response.status_code == HTTP_200_OK
    assert response.json() == expected
