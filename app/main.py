from fastapi import FastAPI
from app.routers.orders import order
from app.routers.products import product

app = FastAPI()

# Include routers
app.include_router(product.router, prefix="/products", tags=["Products"])
app.include_router(order.router, prefix="/orders", tags=["Orders"])