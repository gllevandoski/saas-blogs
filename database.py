from dotenv import load_dotenv
from os import getenv


load_dotenv()
MONGO_URI = getenv("MONGO_URI")
MONGO_DBNAME = getenv("MONGO_DBNAME")


def boot_db():
    from pymongo import MongoClient
    client = MongoClient(host=MONGO_URI)
    db = client[MONGO_DBNAME]
    return db


database = boot_db()
