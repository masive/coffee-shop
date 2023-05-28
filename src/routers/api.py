from datetime import datetime
from typing import Union

from fastapi import APIRouter
from starlette.responses import JSONResponse
from schemas.customer import Customer

router = APIRouter()


@router.get("/health")
async def ping() -> JSONResponse:
    """
    Endpoint for basic health check.
    :return: A JSON response containing a message indicating the server's status.
    """
    content = {"message": "Ok"}
    return JSONResponse(content=content)


@router.get("/customers/birthday", response_model=Customer)
async def get_customers_with_birthday() -> Union[Customer, JSONResponse]:
    """
    Retrieves customers with a birthday on the current date.
    :return: List of customers with a birthday on the current date
    """
    customer = Customer(
        customer_id=12345,
        customer_first_name="Joe Doe",
        birthdate=datetime.today()
    )
    return customer
