from typing import Annotated

from pydantic import BaseModel, field_validator
from fastapi import UploadFile, File, Form


class HashSchema(BaseModel):
    hashed: Annotated[bytes, File(...)]


class PictureSchema(BaseModel):
    title: str
    description: str
    price: int


    @field_validator('description')
    def validate_description(v):
        if v == '':
            v = 'Description is empty.'

        return v
