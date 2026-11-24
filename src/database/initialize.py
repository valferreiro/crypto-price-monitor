from pathlib import Path

from src.database.mongodb import get_mongodb_connection
from src.database.mysql import get_mysql_connection


def initialize_mysql():
    connection = get_mysql_connection()
    cursor = connection.cursor()

    try:
        schema_path = Path(__file__).resolve().parents[2] / "sql" / "schema.sql"
        schema = schema_path.read_text(encoding = "utf-8")

        for statement in schema.split(";"):
            if statement.strip():
                cursor.execute(statement)

        connection.commit()
        print("MySQL: base de datos y tablas inicializadas correctamente")

    finally:
        cursor.close()
        connection.close()

def initialize_mongodb():
    client, database = get_mongodb_connection()
    
    try:
        collection = database["price_history"]

        collection.create_index(
            [("coin_id", 1), ("recorded_at", -1)]
        )

        collection.create_index("symbol")

        print("MongoDB: base de datos y colecciones inicializadas correctamente")

    finally:
        client.close()

def main():
    initialize_mysql()
    initialize_mongodb()

    print("Inicialización de Bases de Datos Completada")

if __name__ == "__main__":
    main()