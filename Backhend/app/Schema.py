from pydantic import BaseModel
from datetime import datetime


class ProductResponse(BaseModel):
    id: int
    name: str
    category: str
    price: float
    updated_at: datetime

    class Config:
        from_attributes = True


class ProductPage(BaseModel):
    products: list[ProductResponse]
    next_cursor: str | None