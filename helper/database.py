import motor.motor_asyncio, datetime
from variables import DB_URL
import os

mongo = pymongo.MongoClient(DB_URL)


class Database:
    
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.dcol = self.db.users
        self.grp = self.db.groups
        
    def new_user(self, id):
        return dict(
            id = id,
            join_date = datetime.date.today().isoformat()
        )        

    async def add_user(self, id):
        user = self.new_user(id)
        await self.dcol.insert_one(user)

    async def is_user_exist(self, id):
        user = await self.dcol.find_one({'id':int(id)})
        return bool(user)

 
db = Database(DB_URL, "Cloud19")









