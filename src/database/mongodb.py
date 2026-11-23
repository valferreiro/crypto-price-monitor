import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

def get_mongo_connection():
    uri = os.getenv("MONGO_URI")
    database_name = os.getenv("MONGODB_DATABASE")

    client = MongoClient(
        uri,
        serverSelectionTimeoutMS = 5000
    )

    client.admin.command("ping")

    database = client[database_name]

    return client, database