# load/load_to_mongodb.py
from config.mongo_config import get_mongo_collection

def load_to_mongodb(projects):
    collection = get_mongo_collection()
    collection.delete_many({})  # Clean slate
    collection.insert_many(projects)
    print(f" {len(projects)} records loaded into MongoDB.")
