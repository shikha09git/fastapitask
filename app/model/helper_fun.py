from bson import ObjectId
from app.db.db import collection_product
def product_helper(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "price": product["price"],
        "sizes": product["sizes"],
    }


async def get_product_by_id(productId: str):
    try:
        obj_id = ObjectId(productId)
    except Exception:
        return None
    return await collection_product.find_one({"_id": obj_id})

async def get_product_info(product_id: str):
    try:
        product = await collection_product.find_one({"_id": ObjectId(product_id)})
        if product:
            return {
                "name": product.get("name"),
                "id": str(product["_id"]),
            }
    except Exception:
        pass
    return None

async def update_product_quantity(product_id: str, size_index: int, new_qty: int):
    from app.db.db import collection_product
    await collection_product.update_one(
        {"_id": ObjectId(product_id)},
        {"$set": {f"sizes.{size_index}.quantity": new_qty}}
    )