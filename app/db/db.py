from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
mongo_client = AsyncIOMotorClient(MONGO_URI)
mongo_db = mongo_client["FastApi_crud"]
collection_product=mongo_db["Products"]
collection_order=mongo_db["Orders"]
