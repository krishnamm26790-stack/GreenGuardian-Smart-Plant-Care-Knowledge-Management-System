from db import get_connection


def record_watering(plant_id, notes):
    """
    Records a watering event for a plant.
    """

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO watering_logs
    (plant_id, notes)

    VALUES (%s, %s);
    """

    cursor.execute(query, (plant_id, notes))

    connection.commit()

    print("💧 Watering recorded successfully!")

    cursor.close()
    connection.close()




def view_watering_history():
    """
    Returns all watering history with plant names.
    """

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT
        w.log_id,
        p.plant_name,
        w.watered_on,
        w.notes
    FROM watering_logs w
    INNER JOIN plants p
        ON w.plant_id = p.plant_id
    ORDER BY w.watered_on DESC, w.log_id DESC;
    """

    cursor.execute(query)

    records = cursor.fetchall()

    cursor.close()
    connection.close()

    return records



def delete_watering_log(log_id):
    """
    Deletes a watering record.
    """

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    DELETE FROM watering_logs
    WHERE log_id = %s;
    """

    cursor.execute(query, (log_id,))

    if cursor.rowcount == 0:
        print("❌ Watering record not found.")
    else:
        connection.commit()
        print("🗑️ Watering record deleted successfully!")

    cursor.close()
    connection.close()


def plants_due_for_watering():
    """
    Returns all plants that need watering today.
    """

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT
        p.plant_id,
        p.plant_name,
        p.location,
        p.watering_frequency,
        MAX(w.watered_on) AS last_watered

    FROM plants p

    LEFT JOIN watering_logs w
        ON p.plant_id = w.plant_id

    GROUP BY
        p.plant_id,
        p.plant_name,
        p.location,
        p.watering_frequency

    HAVING

        MAX(w.watered_on) IS NULL

        OR

        CURRENT_DATE >=
        MAX(w.watered_on) + p.watering_frequency

    ORDER BY p.plant_name;
    """

    cursor.execute(query)

    plants = cursor.fetchall()

    cursor.close()
    connection.close()

    return plants

def get_due_today_count():
    """
    Returns the number of plants that need watering today.
    """

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT COUNT(*)
    FROM plants p

    LEFT JOIN
    (
        SELECT
            plant_id,
            MAX(watered_on) AS last_watered
        FROM watering_logs
        GROUP BY plant_id
    ) w

    ON p.plant_id = w.plant_id

    WHERE

        w.last_watered IS NULL

        OR

        CURRENT_DATE >=
        (w.last_watered + p.watering_frequency);
    """

    cursor.execute(query)

    total = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return total

def get_all_plants():
    """
    Returns all plants for dropdown.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT plant_id, plant_name
        FROM plants
        ORDER BY plant_name;
    """)

    plants = cursor.fetchall()

    cursor.close()
    conn.close()

    return plants