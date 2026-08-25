from motor.motor_asyncio import AsyncIOMotorClient
from info import DATABASE_URI

class Database:
    def __init__(self, uri, db_name):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[db_name]
        self.col = self.db.user
        self.config_col = self.db.configuration

    async def update_top_messages(self, user_id, message_text):
        user = await self.col.find_one({"user_id": user_id, "messages.text": message_text})
        
        if not user:
            await self.col.update_one(
                {"user_id": user_id},
                {"$push": {"messages": {"text": message_text, "count": 1}}},
                upsert=True
            )
        else:
            await self.col.update_one(
                {"user_id": user_id, "messages.text": message_text},
                {"$inc": {"messages.$.count": 1}}
            )

    async def get_top_messages(self, limit=30):
        pipeline = [
            {"$unwind": "$messages"},
            {"$group": {"_id": "$messages.text", "count": {"$sum": "$messages.count"}}},
            {"$sort": {"count": -1}},
            {"$limit": limit}
        ]
        results = await self.col.aggregate(pipeline).to_list(limit)
        return [result['_id'] for result in results]
    
    async def delete_all_messages(self):
        await self.col.delete_many({})

    async def set_global_shortener_stages(self, stages):
        """Persist the owner-selected shortener stages for every group."""
        await self.config_col.update_one(
            {"_id": "global_shortener_stages"},
            {"$set": {"stages": sorted(stages)}},
            upsert=True,
        )

    async def get_global_shortener_stages(self):
        config = await self.config_col.find_one({"_id": "global_shortener_stages"})
        return config.get("stages") if config else None

    async def clear_global_shortener_stages(self):
        await self.config_col.delete_one({"_id": "global_shortener_stages"})

    async def set_global_verify_gaps(self, two_gap, three_gap):
        await self.config_col.update_one(
            {"_id": "global_verification_timing"},
            {"$set": {"two_gap": int(two_gap), "three_gap": int(three_gap)}},
            upsert=True,
        )

    async def get_global_verify_gaps(self):
        config = await self.config_col.find_one({"_id": "global_verification_timing"})
        return (config.get("two_gap"), config.get("three_gap")) if config else None

    async def clear_global_verify_gaps(self):
        await self.config_col.delete_one({"_id": "global_verification_timing"})

mdb = Database(DATABASE_URI, "admin_database")
