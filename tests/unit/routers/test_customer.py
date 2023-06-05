from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK

from app.main import app
from schemas.customer import Customers, BirthdayCustomer

test_client = TestClient(app)


@pytest.mark.unit
def test_customers_with_birthday__ok():
    customer = BirthdayCustomer(customer_id=12345, customer_first_name="Joe Doe")
    expected = Customers(customers=[customer])
    with patch("routers.customer._get_customers_with_birthdate") as mock:
        mock.return_value = [customer]
        response = test_client.get("/api/v1/customers/birthday")
    assert response.status_code == HTTP_200_OK
    assert response.json() == expected.dict(by_alias=True)
