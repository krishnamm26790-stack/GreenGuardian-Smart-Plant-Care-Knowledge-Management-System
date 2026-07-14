from db import get_connection


def get_total_plants(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM plants
        WHERE user_id = %s;           
    """,(user_id,))

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total


def get_total_health_logs(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
            SELECT COUNT(*)
            FROM health_logs h
            JOIN plants p
            ON h.plant_id=p.plant_id
            WHERE p.user_id=%s;
            """,(user_id,))

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total


def get_total_watering_logs(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM watering_logs w
        JOIN plants p
        ON w.plant_id=p.plant_id
        WHERE p.user_id=%s;
    """,(user_id,))

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total


def plants_by_type(user_id):
    """
    Returns number of plants grouped by plant type.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT plant_type, COUNT(*)
        FROM plants
        WHERE user_id = %s
        GROUP BY plant_type
        ORDER BY COUNT(*) DESC;
    """,(user_id,))

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


def plants_by_location(user_id):
    """
    Returns number of plants grouped by location.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT location, COUNT(*)
        FROM plants
        WHERE user_id = %s
        GROUP BY location
        ORDER BY COUNT(*) DESC;
    """,(user_id,))

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


def watering_frequency_statistics(user_id):
    """
    Returns plant count according to watering frequency.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT watering_frequency, COUNT(*)
        FROM plants
        WHERE user_id = %s
        GROUP BY watering_frequency
        ORDER BY watering_frequency;
    """,(user_id,))

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data