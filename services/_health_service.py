from db import get_connection


def record_health(user_id,plant_id, status, notes):
    """
    Records a plant's health status.
    """

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO health_logs (plant_id, status, notes)
    SELECT plant_id, %s, %s
    FROM plants
    WHERE plant_id = %s
    AND user_id = %s;
    """

    cursor.execute(
        query,
        ( status, notes, plant_id, user_id)
    )

    connection.commit()

    print("🌿 Health record added successfully!")

    cursor.close()
    connection.close()




def view_health_history(user_id):
    """
    Fetches complete health history.
    """

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT
        health_logs.health_log_id,
        plants.plant_name,
        health_logs.status,
        health_logs.observed_on,
        health_logs.notes
    FROM health_logs
    JOIN plants
    ON plants.plant_id = health_logs.plant_id
    WHERE plants.user_id = %s
    ORDER BY health_log_id DESC;
    """

    cursor.execute(query, (user_id,))

    records = cursor.fetchall()

    cursor.close()
    connection.close()

    return records



def delete_health_log(user_id,health_log_id):
    """
    Deletes a health record.
    """

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    DELETE FROM health_logs
    WHERE health_log_id = %s AND plant_id IN (
        SELECT h.log_id
        FROM health_logs h
        JOIN plants p
        ON h.plant_id = p.plant_id
        WHERE h.log_id = %s
        AND p.user_id = %s
);
    """

    cursor.execute(query, (health_log_id, user_id))

    connection.commit()

    cursor.close()
    connection.close()

    print("🩺 Health record deleted successfully!")