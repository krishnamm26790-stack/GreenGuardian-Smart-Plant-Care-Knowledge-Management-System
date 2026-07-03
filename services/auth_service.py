import hashlib
from db import get_connection


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, password):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE username=%s",
        (username,)
    )

    if cur.fetchone():
        conn.close()
        return False

    password_hash = hash_password(password)

    cur.execute(
        "INSERT INTO users(username,password_hash) VALUES(%s,%s)",
        (username, password_hash)
    )

    conn.commit()
    conn.close()

    return True


def login_user(username, password):
    conn = get_connection()
    cur = conn.cursor()

    password_hash = hash_password(password)

    cur.execute(
        """
        SELECT user_id,username
        FROM users
        WHERE username=%s
        AND password_hash=%s
        """,
        (username, password_hash)
    )

    user = cur.fetchone()

    conn.close()

    return user