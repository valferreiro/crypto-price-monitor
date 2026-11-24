from src.database.mongodb import get_mongodb_connection
from src.database.mysql import get_mysql_connection


def main():
    mongo_client = None
    mysql_connection = None

    try:
        # Conexión a MongoDB
        mongo_client, mongo_db = get_mongodb_connection()
        print("MongoDB conectado correctamente")
        print(f"Base de datos: {mongo_db.name}")

        # Conexión a MySQL
        mysql_connection = get_mysql_connection()
        print("MySQL conectado correctamente")

    except Exception as error:
        print(f"Error de conexión: {error}")

    finally:
        if mongo_client is not None:
            mongo_client.close()

        if mysql_connection is not None and mysql_connection.is_connected():
            mysql_connection.close()


if __name__ == "__main__":
    main()
