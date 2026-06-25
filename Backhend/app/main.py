from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from datetime import datetime

from app.database import engine, get_db
from app.models import Base, Product

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/products")
def get_products(
    limit: int = Query(20, le=100),
    cursor: str | None = None,
    category: str | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(Product)

    # Category filter
    if category:
        query = query.filter(Product.category == category)

    # Cursor pagination
    if cursor:
        timestamp_str, product_id = cursor.split("|")

        timestamp = datetime.fromisoformat(timestamp_str)

        query = query.filter(
            or_(
                Product.updated_at < timestamp,
                and_(
                    Product.updated_at == timestamp,
                    Product.id < int(product_id)
                )
            )
        )

    # Fetch products
    products = (
        query
        .order_by(
            Product.updated_at.desc(),
            Product.id.desc()
        )
        .limit(limit)
        .all()
    )

    # Generate next cursor
    next_cursor = None

    if products:
        last = products[-1]
        next_cursor = f"{last.updated_at.isoformat()}|{last.id}"

    return {
        "products": products,
        "next_cursor": next_cursor
    }