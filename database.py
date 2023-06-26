import motor.motor_asyncio

# MongoDB configuration
MONGODB_URL = 'mongodb+srv://tnbots:tnbots@cluster0.lkuiies.mongodb.net/?retryWrites=true&w=majority'
DATABASE_NAME = 'telegram_bot'
COLLECTION_NAME = 'users'

class Database:
    def __init__(self):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
        self.db = self.client[DATABASE_NAME]
        self.col = self.db[COLLECTION_NAME]

    async def save_user(self, user_id):
        existing_user = await self.col.find_one({"user_id": user_id})
        if existing_user:
            await self.col.update_one({"user_id": user_id}, {"$set": {"user_id": user_id}})
        else:
            await self.col.insert_one({"user_id": user_id})

    async def count_users(self):
        total_users = await self.col.count_documents({})
        return total_users

    async def delete_user(self, user_id):
        result = await self.collection.delete_one({"user_id": user_id})
        return result.deleted_count

    # db = Database()
    # # Delete a user with user_id '123'
    # deleted_count = await db.delete_user('123')
    # print(f"Deleted {deleted_count} document(s).")


db = Database()
