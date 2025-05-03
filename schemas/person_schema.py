from pydantic import BaseModel, Field
from datetime import date
from typing import Optional


class PersonCreateSchema(BaseModel):
    first_name: str = Field(..., description="The first name of the person", example="John")
    last_name: str = Field(..., description="The last name of the person", example="Doe")
    passport_number: Optional[str] = Field(None, description="The passport number of the person", example="1234567890")
    birth_date: date = Field(..., description="The birth date of the person", example="1990-01-01")
    birth_country: str = Field(..., description="The birth country of the person", example="Colombia")


class PersonSchema(PersonCreateSchema):
    id: int = Field(..., description="The id of the person", example=1)


class PersonCreatedResponseSchema(BaseModel):
    message: str = Field(..., description="The message of the person", example="Person created")
