from src.database.mongodb import get_mongodb_connection
from src.database.mysql import get_mysql_connection

MYSQL_INSERT_QUERY = """
    INSERT INTO price_history (
        coin_id,
        symbol,
        name,
        price,
        currency,
        recorded_at,
        source,
        market_cap,
        total_volume,
        price_change_percentage_24h
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""


def save_prices_mysql(prices: list[dict]) -> int:
    """Guarda las capturas de precios en MySQL."""

    if not prices:
        return 0

    connection = None
    cursor = None

    try:
        connection = get_mysql_connection()
        cursor = connection.cursor()

        records = [
            (
                price["coin_id"],
                price["symbol"],
                price["name"],
                price["price"],
                price["currency"],
                price["recorded_at"],
                price["source"],
                price.get("market_cap"),
                price.get("total_volume"),
                price.get("price_change_percentage_24h"),
            )
            for price in prices
        ]

        cursor.executemany(MYSQL_INSERT_QUERY, records)
        connection.commit()

        return cursor.rowcount

    except Exception:
        if connection is not None:
            connection.rollback()
        raise

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()


def save_prices_mongodb(prices: list[dict]) -> int:
    """Guarda las capturas de precios en MongoDB."""

    if not prices:
        return 0

    mongo_client = None

    try:
        mongo_client, database = get_mongodb_connection()

        collection = database["price_history"]

        collection.create_index(
            [("coin_id", 1), ("recorded_at", -1)]
        )

        collection.create_index("symbol")

        result = collection.insert_many(prices)

        return len(result.inserted_ids)

    finally:
        if mongo_client is not None:
            mongo_client.close()


def store_prices(prices: list[dict]) -> dict:
    """Almacena las capturas en MySQL y MongoDB."""

    if not prices:
        return {
            "mysql": 0,
            "mongodb": 0,
        }

    mysql_count = save_prices_mysql(prices)
    mongodb_count = save_prices_mongodb(prices)

    return {
        "mysql": mysql_count,
        "mongodb": mongodb_count,
    }
