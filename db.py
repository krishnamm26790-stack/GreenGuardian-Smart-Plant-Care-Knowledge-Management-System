import psycopg2


def get_connection():
    """
    Creates and returns a PostgreSQL database connection.
    """

    return psycopg2.connect(
        host="localhost",
        database="greenguardiandb",
        user="postgres",
        password="YourStrongPassword123",
        port="5432"
    )



