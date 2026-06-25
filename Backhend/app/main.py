from fastapi import FastAPI, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from datetime import datetime

from app.database import engine, get_db
from app.models import Base, Product
from app.Schema import ProductPage

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Product Catalog API",
        "total_products": "200000+"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/products", response_model=ProductPage)
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
        try:
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

        except Exception:
            raise HTTPException(
                status_code=400,
                detail="Invalid cursor format"
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


@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    product.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(product)

    return product