from src.database.mongodb import (
    close_mongodb_connection,
    get_mongodb_connection,
)
from src.database.mysql import get_mysql_connection


def main():
    mysql_connection = None

    try:
        # Conexión a MongoDB
        _, mongo_db = get_mongodb_connection()
        print("MongoDB conectado correctamente")
        print(f"Base de datos: {mongo_db.name}")

        # Conexión a MySQL
        mysql_connection = get_mysql_connection()
        print("MySQL conectado correctamente")

    except Exception as error:  # noqa: BLE001
        print(f"Error de conexión: {error}")

    finally:
        close_mongodb_connection()

        if mysql_connection is not None:
            mysql_connection.close()


if __name__ == "__main__":
    main()