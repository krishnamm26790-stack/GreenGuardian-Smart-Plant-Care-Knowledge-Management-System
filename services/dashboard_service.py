from db import get_connection


def get_total_plants():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM plants;
    """)

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total


def get_total_health_logs():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM health_logs;
    """)

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total


def get_total_watering_logs():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM watering_logs;
    """)

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total


def plants_by_type():
    """
    Returns number of plants grouped by plant type.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT plant_type, COUNT(*)
        FROM plants
        GROUP BY plant_type
        ORDER BY COUNT(*) DESC;
    """)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


def plants_by_location():
    """
    Returns number of plants grouped by location.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT location, COUNT(*)
        FROM plants
        GROUP BY location
        ORDER BY COUNT(*) DESC;
    """)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


def watering_frequency_statistics():
    """
    Returns plant count according to watering frequency.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT watering_frequency, COUNT(*)
        FROM plants
        GROUP BY watering_frequency
        ORDER BY watering_frequency;
    """)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data