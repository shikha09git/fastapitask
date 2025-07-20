from fastapi import APIRouter, Query, status
from app.model.helper_fun import product_helper
from app.model.models import Product,ProductCreateResponse,PaginatedResponse
from app.db.db import collection_product

router = APIRouter()



@router.post("/", response_model=ProductCreateResponse, status_code=status.HTTP_201_CREATED)
async def create_product(product: Product):
    result = await collection_product.insert_one(product.dict())
    return {"id":str(result.inserted_id)}


@router.get("/", response_model=PaginatedResponse, status_code=status.HTTP_200_OK)
async def get_products(skip: int = Query(0, ge=0),limit: int = Query(10, ge=0),):
    total = await collection_product.count_documents({})
    products = []
    cursor = collection_product.find().skip(skip).limit(limit)
    async for product in cursor:
        products.append(product_helper(product))
    print(products)
    return {
        "data": products,
        "page": {
            "next": skip + limit,
            "limit": limit,
            "previous": max(skip - limit, 0)
        }
    }





