from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy import Index

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    category = Column(String, nullable=False)

    price = Column(Float, nullable=False)

    created_at = Column(DateTime, nullable=False)

    updated_at = Column(DateTime, nullable=False)


Index(
    "idx_products_updated_id",
    Product.updated_at.desc(),
    Product.id.desc()
)

Index(
    "idx_products_category_updated_id",
    Product.category,
    Product.updated_at.desc(),
    Product.id.desc()
)