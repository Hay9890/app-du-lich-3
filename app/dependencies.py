from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "Database"

client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]
def get_user_collection():
    return db.users
def get_otp_collection():
    return db["password_otps"]