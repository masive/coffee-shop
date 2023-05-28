import datetime
from datetime import date
from typing import Optional

from pydantic import BaseModel, root_validator


class Customer(BaseModel):
    customer_id: int
    customer_first_name: str
    birthdate: date
    is_birthday: bool = False

    @root_validator()
    def set_has_birthday(cls, values: dict) -> dict:
        current_date = values["birthdate"]
        if current_date == datetime.date.today():
            values |= {"is_birthday": True}
            return values
        return values
