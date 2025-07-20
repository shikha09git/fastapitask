from fastapi import APIRouter,HTTPException,Query,Path,status
from app.model.helper_fun import get_product_by_id,get_product_info,update_product_quantity
from app.model.models import OrderResponse,OrderCreate
from app.db.db import collection_order

router = APIRouter()

@router.post("/",response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order(order:OrderCreate):
    user_id = "user123"
    total_price=0.0
    for item in order.items:
        product = await get_product_by_id(item.productId)
        if not product:
            raise HTTPException(status_code=404, detail=f"Product {item.productId} not found")
        total_price+=product["price"]*item.qwt
    new_order = {
        "userId": user_id,
        "items": [item.dict() for item in order.items],
        "total":total_price
    }

    res=await collection_order.insert_one(new_order)
    for item in order.items:
        product = await get_product_by_id(item.productId)
        new_qty = product["sizes"][0]["quantity"] - item.qwt
        print(new_qty)
        await update_product_quantity(item.productId, 0, new_qty)

    return {"id": str(res.inserted_id)}

@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_orders_by_user(user_id: str = Path(...),limit: int = Query(10, gt=0),skip: int = Query(0, ge=0)):
    cursor = collection_order.find({"userId": user_id}).skip(skip).limit(limit)
    orders = []

    async for order in cursor:
        enriched_items = []
        for item in order["items"]:
            product = await get_product_info(item["productId"])
            if product:
                enriched_items.append({
                    "productDetails": product,
                    "qty": item["qwt"]
                })

        orders.append({
            "orderId": str(order["_id"]),
            "items": enriched_items,
            "total": order.get("total", 0)
        })

    return {
        "data": orders,
        "page": {
            "next": skip + limit,
            "limit": limit,
            "previous": max(skip - limit, 0)
        }
    }