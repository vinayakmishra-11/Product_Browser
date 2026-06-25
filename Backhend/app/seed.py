from faker import Faker
from datetime import datetime, timedelta
import random

from app.database import SessionLocal
from app.models import Product

fake = Faker()

db = SessionLocal()

categories = [
    "Electronics",
    "Books",
    "Fashion",
    "Sports",
    "Home"
]

products = []

base_time = datetime.now()

for i in range(200000):

    created = base_time - timedelta(
        seconds=random.randint(0, 31536000)
    )

    products.append(
        {
            "name": fake.word(),
            "category": random.choice(categories),
            "price": round(random.uniform(100, 10000), 2),
            "created_at": created,
            "updated_at": created
        }
    )

print("Generated data")

db.bulk_insert_mappings(
    Product,
    products
)

db.commit()

print("Inserted 200000 products")