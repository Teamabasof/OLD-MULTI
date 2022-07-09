from variables import DB_URL
import pymongo 
import os

DB_NAME = os.environ.get("DB_NAME","Cloud19")
mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["user"]


def insert(chat_id):
    user_id = int(chat_id)
    user_det = {"_id": user_id,"file_id": None, "caption": None}
    try:
      dbcol.insert_one(user_det)
    except:
      pass

def getid():
    values = []
    for key  in dbcol.find():
         id = key["_id"]
         values.append((id)) 
    return values
