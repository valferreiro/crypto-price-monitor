from pathlib import Path

from src.database.mongodb import (
    close_mongodb_connection,
    get_mongodb_connection,
)
from src.database.mysql import get_mysql_connection


def initialize_mysql():
    connection = get_mysql_connection()
    cursor = None

    try:
        cursor = connection.cursor()

        schema_path = (
            Path(__file__).resolve().parents[2]
            / "sql"
            / "schema.sql"
        )

        schema = schema_path.read_text(encoding="utf-8")

        for statement in schema.split(";"):
            if statement.strip():
                cursor.execute(statement)

        connection.commit()

        print(
            "MySQL: base de datos y tablas inicializadas correctamente"
        )

    finally:
        if cursor is not None:
            cursor.close()

        connection.close()


def initialize_mongodb():
    _, database = get_mongodb_connection()

    collection = database["price_history"]

    collection.create_index(
        [("coin_id", 1), ("recorded_at", -1)]
    )

    collection.create_index("symbol")

    print(
        "MongoDB: base de datos y colecciones inicializadas correctamente"
    )


def main():
    try:
        initialize_mysql()
        initialize_mongodb()

        print("Inicialización de Bases de Datos Completada")

    finally:
        close_mongodb_connection()


if __name__ == "__main__":
    main()