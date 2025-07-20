from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = "mongodb+srv://admin:admin@cluster0.0o5m4ap.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
mongo_client = AsyncIOMotorClient(MONGO_URI)
mongo_db = mongo_client["FastApi_crud"]
collection_product=mongo_db["Products"]
collection_order=mongo_db["Orders"]
