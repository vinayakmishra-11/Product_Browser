
Project Overview 

Backend API for browsing 200,000+ products with category filtering and cursor based pagination.

TechStack
FastAPI
PostgreSQL
SQLAlchemy

API ENdpoints 
GET /
GET /health
GET /products
PUT /products/{id}

# API Testing Guide

Base URL:

https://product-browser-yb1f.onrender.com

## 1. Root Endpoint

Returns basic API information.

Request:

GET /

Example:

https://product-browser-yb1f.onrender.com/

Expected Response:

{
"message": "Product Catalog API",
"total_products": "200000+"
}

---

## 2. Health Check

Used to verify that the API is running.

Request:

GET /health

Example:

https://product-browser-yb1f.onrender.com/health

Expected Response:

{
"status": "healthy"
}

---

## 3. Get Products (First Page)

Returns the first page of products sorted by newest updates first.

Request:

GET /products

Example:

https://product-browser-yb1f.onrender.com/products

Expected Response:

{
"products": [...],
"next_cursor": "2026-06-25T12:52:25.658649|194876"
}

---

## 4. Get Products With Custom Limit

Returns a custom number of products.

Request:

GET /products?limit=10

Example:

https://product-browser-yb1f.onrender.com/products?limit=10

---

## 5. Filter Products By Category

Returns products belonging to a specific category.

Request:

GET /products?category=Books

Example:

https://product-browser-yb1f.onrender.com/products?category=Books

Supported Categories:

* Books
* Electronics
* Fashion
* Sports
* Home

---

## 6. Cursor Pagination (Next Page)

Use the next_cursor returned from the previous response.

Request:

GET /products?cursor=<cursor>

Example:

https://product-browser-yb1f.onrender.com/products?cursor=2026-06-25T12:52:25.658649%7C194876

Note:
The "|" character should be URL encoded as "%7C".

---

## 7. Category Filter + Cursor Pagination

Request:

GET /products?category=Books&cursor=<cursor>

Example:

https://product-browser-yb1f.onrender.com/products?category=Books&cursor=2026-06-25T12:52:25.658649%7C194876

---

## 8. Update Product

Updates the updated_at timestamp of a product.

Request:

PUT /products/{product_id}

Example:

PUT https://product-browser-yb1f.onrender.com/products/1

Expected Response:

{
"id": 1,
"name": "...",
"category": "...",
"price": ...,
"updated_at": "..."
}

---

## Interactive API Documentation

Swagger UI:

https://product-browser-yb1f.onrender.com/docs



Category Are 
Books
Electronics
Fashion
Home
Sports