from pydantic import BaseModel,Field
from typing import List,Optional

#Product Model
class Size(BaseModel):
    size: str
    quantity: int

class Product(BaseModel):
    name: str
    price: float
    sizes: List[Size]

class ProductCreateResponse(BaseModel):
    id: str

class ProductPrice(BaseModel):
    id: str
    name: str
    price: float

class PageInfo(BaseModel):
    next: int
    limit: int
    previous: int
class PaginatedResponse(BaseModel):
    data: List[ProductPrice]
    page: PageInfo


#orders Model
class Items(BaseModel):
    productId: str
    qwt: int=Field(..., gt=0, description="Quantity must be greater than 0")

class OrderCreate(BaseModel):
    items: List[Items]


class OrderResponse(BaseModel):
    id: str
