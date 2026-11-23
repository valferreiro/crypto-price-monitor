from src.database.mongodb import get_mongo_connection
from src.database.mysql import get_myslq_connection


def main():
    mongo_client = None
    mysql_connection = None

    try:
        mongo_client, mongo_db = get_mongo_connection()
        print("MongoDB conectado correstamente")
        print(f"Base de Datos: {mongo_db.name}")

        mysql_connection = get_myslq_connection()
        print("MySQL conectado correctamente")

    except Exception as error:  
        print(f"Error de conexión: {error}")

    finally:
        if mongo_client:
            mongo_client.close()

        if mysql_connection and mysql_connection.is_connected():
            mysql_connection.close()

if __name__ == "__main__":
    main()