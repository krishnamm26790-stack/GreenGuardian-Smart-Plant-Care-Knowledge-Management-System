from db import get_connection

def record_watering(user_id, plant_id, notes):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO watering_logs (plant_id, notes)
        SELECT plant_id, %s
        FROM plants
        WHERE plant_id = %s
        AND user_id = %s;
    """, (
        notes,
        plant_id,
        user_id
    ))

    connection.commit()

    print("💧 Watering recorded successfully!")

    cursor.close()
    connection.close()




def view_watering_history(user_id):
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
    WHERE p.user_id = %s
    ORDER BY w.watered_on DESC, w.log_id DESC;
    """

    cursor.execute(query, (user_id,))

    records = cursor.fetchall()

    cursor.close()
    connection.close()

    return records



def delete_watering_log(user_id,log_id):
    """
    Deletes a watering record.
    """

    connection = get_connection()
    cursor = connection.cursor()

    query = """
DELETE FROM watering_logs
WHERE log_id IN (
    SELECT w.log_id
    FROM watering_logs w
    JOIN plants p
        ON w.plant_id = p.plant_id
    WHERE w.log_id = %s
    AND p.user_id = %s
);
    """

    cursor.execute(query, (log_id,user_id))

    if cursor.rowcount == 0:
        print("❌ Watering record not found.")
    else:
        connection.commit()
        print("🗑️ Watering record deleted successfully!")

    cursor.close()
    connection.close()


def plants_due_for_watering(user_id):
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

WHERE p.user_id = %s

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

    cursor.execute(query, (user_id,))

    plants = cursor.fetchall()

    cursor.close()
    connection.close()

    return plants

def get_due_today_count(user_id):
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

WHERE p.user_id = %s
AND
(
    w.last_watered IS NULL

    OR

    CURRENT_DATE >=
    (w.last_watered + p.watering_frequency)
)
    """

    cursor.execute(query, (user_id,))
    print("USER ID RECEIVED:", user_id)

    total = cursor.fetchone()[0]
    print("TOTAL:", total)

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