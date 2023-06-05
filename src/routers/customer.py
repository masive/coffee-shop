from typing import Union

from fastapi import APIRouter
from pydantic import parse_obj_as
from sqlalchemy import text
from starlette.responses import JSONResponse

from routers.helpers import execute_query
from schemas.customer import BirthdayCustomer, Customers

router = APIRouter()


@router.get("/customers/birthday", response_model=Customers)
async def get_customers_with_birthday() -> Union[Customers, JSONResponse]:
    """
    Retrieves customers with a birthday on the current date.
    :return: List of customers with a birthday on the current date
    """
    birthday_customers: list[BirthdayCustomer] = _get_customers_with_birthdate()
    customers = Customers(customers=birthday_customers)
    return customers


def _get_customers_with_birthdate() -> list[BirthdayCustomer]:
    """
    Retrieves a customers with a birthday on the current date.
    :return: A list of customers with a birthday on the current date.
    """
    query = text(
        "SELECT customer_id, customer_first_name FROM customer "
        "WHERE EXTRACT(DAY FROM birthdate) = EXTRACT(DAY FROM CURRENT_DATE)"
    )
    customers_args: list = execute_query(query)
    return parse_obj_as(list[BirthdayCustomer], customers_args)
