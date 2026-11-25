from threading import Lock

from mysql.connector.pooling import MySQLConnectionPool

from src.config import config

# Pool compartido de MySQL
_mysql_pool = None
_mysql_pool_lock = Lock()


def get_mysql_pool():
    """Crea el pool una sola vez y lo reutiliza."""

    global _mysql_pool

    if _mysql_pool is None:
        with _mysql_pool_lock:
            if _mysql_pool is None:
                if not all([
                    config.MYSQL_HOST,
                    config.MYSQL_USER,
                    config.MYSQL_DATABASE,
                ]):
                    raise ValueError(
                        "La configuración de MySQL no está completa"
                    )

                _mysql_pool = MySQLConnectionPool(
                    pool_name="crypto_monitor_pool",
                    pool_size=5,
                    host=config.MYSQL_HOST,
                    port=config.MYSQL_PORT,
                    user=config.MYSQL_USER,
                    password=config.MYSQL_PASSWORD,
                    database=config.MYSQL_DATABASE,
                )

    return _mysql_pool


def get_mysql_connection():
    """Obtiene una conexión disponible del pool."""

    return get_mysql_pool().get_connection()