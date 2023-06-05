from pydantic import BaseModel, Field


class BirthdayCustomer(BaseModel):
    customer_id: int
    customer_first_name: str


class Customers(BaseModel):
    """A list of customers."""

    birthday_customers: list[BirthdayCustomer] = Field(alias="customers")
