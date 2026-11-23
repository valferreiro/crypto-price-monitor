import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_myslq_connection():
    connection = mysql.connector.connect(
        host = os.getenv("MYSQL.HOST"),
        port = int(os.getenv("MYSQL_PORT", 3306)),  # noqa: PLW1508
        user = os.getenv("MYSQL_USER"),
        password = os.getenv("MYSLQ_PASSSWORD"),
    )

    return connection