import pymongo
from uptime import Uptime

class Database:
    def __init__(self, connection_string: str) -> None:
        self.mongo = pymongo.MongoClient(connection_string)
        self.database = self.mongo.uptime_db
        self.collection = self.database.uptimes

    def insert(self, uptime: Uptime):
        self.collection.insert_one(uptime.to_dict())