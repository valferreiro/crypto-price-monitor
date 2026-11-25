from pymongo import MongoClient

from src.config import config

# Cliente y base de datos compartidos
_mongodb_client = None
_mongodb_database = None


def get_mongodb_connection():
    """Obtiene el cliente y la base de datos reutilizables."""

    global _mongodb_client, _mongodb_database

    if _mongodb_client is None:
        if not config.MONGODB_URI:
            raise ValueError("Falta MONGODB_URI en el archivo .env")

        if not config.MONGODB_DATABASE:
            raise ValueError("Falta MONGODB_DATABASE en el archivo .env")

        client = MongoClient(
            config.MONGODB_URI,
            serverSelectionTimeoutMS=5000,
            maxPoolSize=20,
        )

        try:
            client.admin.command("ping")
        except Exception:
            client.close()
            raise

        _mongodb_client = client
        _mongodb_database = client[config.MONGODB_DATABASE]

    return _mongodb_client, _mongodb_database


def get_mongodb_collection(collection_name: str):
    """Obtiene una colección de la base de datos compartida."""

    if not collection_name:
        raise ValueError("El nombre de la colección no puede estar vacío")

    _, database = get_mongodb_connection()

    return database[collection_name]


def close_mongodb_connection():
    """Cierra el cliente compartido cuando termina la aplicación."""

    global _mongodb_client, _mongodb_database

    if _mongodb_client is not None:
        _mongodb_client.close()
        _mongodb_client = None
        _mongodb_database = None