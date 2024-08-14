import pymongo

class MongoDBClient:
    def __init__(self, uri, database_name):
        self.client = pymongo.MongoClient(uri)
        self.database = self.client[database_name]

    def insert_record(self, collection_name, record):
        collection = self.database[collection_name]
        collection.insert_one(record)

    def fetch_records(self, collection_name, query={}):
        collection = self.database[collection_name]
        return collection.find(query)
