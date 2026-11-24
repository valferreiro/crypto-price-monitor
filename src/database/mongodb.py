import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


def get_mongodb_connection():
    uri = os.getenv("MONGODB_URI")
    database_name = os.getenv("MONGODB_DATABASE")

    if not uri:
        raise ValueError("No se encontró MONGODB_URI en el archivo .env")

    if not database_name:
        raise ValueError(
            "No se encontró MONGODB_DATABASE en el archivo .env"
        )

    client = MongoClient(
        uri,
        serverSelectionTimeoutMS=5000,
    )

    client.admin.command("ping")

    database = client[database_name]

    return client, database