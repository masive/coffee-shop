from datetime import datetime

import pytest
from freezegun import freeze_time
from pydantic import ValidationError

from schemas.customer import BirthdayCustomer


@pytest.mark.unit
class TestCustomer:
    @freeze_time("1950-05-29")
    @pytest.mark.parametrize(
        "birthdate,expected",
        [
            (datetime.strptime("1950-05-29", "%Y-%m-%d").date(), True),
            (datetime.strptime("1950-07-30", "%Y-%m-%d").date(), False),
        ],
        ids=["Happy birthday!", "Sorry today is not your birthday!"],
    )
    def test_customer__valid_args(self, birthdate, expected):
        args = {
            "customer_id": 12345,
            "customer_first_name": "Joe Doe",
            "birthdate": birthdate,
        }
        customer = BirthdayCustomer(**args)
        assert customer.customer_id == 12345
        assert customer.customer_first_name == "Joe Doe"

    @pytest.mark.parametrize(
        "args,expected_error",
        [
            (
                {
                    "customer_first_name": "Joe Doe",
                    "birthdate": datetime.strptime("1950-05-29", "%Y-%m-%d").date(),
                },
                ValueError,
            ),
            (
                {
                    "customer_id": 12345,
                    "birthdate": datetime.strptime("1950-05-29", "%Y-%m-%d").date(),
                },
                ValueError,
            ),
            (
                {
                    "customer_id": None,
                    "customer_first_name": "Joe Doe",
                    "birthdate": datetime.strptime("1950-05-29", "%Y-%m-%d").date(),
                },
                ValidationError,
            ),
        ],
        ids=[
            "Missing customer_id",
            "Missing customer_first_name",
            "Invalid None customer_id",
        ],
    )
    def test_customer__invalid_args(self, args, expected_error):
        with pytest.raises(expected_error):
            _ = BirthdayCustomer(**args)
