import os
import psycopg2


def get_connection():

    database_url = os.getenv("DATABASE_URL")

    if database_url:
        return psycopg2.connect(database_url)

    return psycopg2.connect(
        host="localhost",
        database="greenguardiandb",
        user="postgres",
        password="YourStrongPassword123",
        port="5432"
    )