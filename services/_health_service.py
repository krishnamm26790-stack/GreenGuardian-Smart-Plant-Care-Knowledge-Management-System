from db import get_connection


def record_health(plant_id, status, notes):
    """
    Records a plant's health status.
    """

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO health_logs
    (plant_id, status, notes)
    VALUES (%s, %s, %s);
    """

    cursor.execute(
        query,
        (plant_id, status, notes)
    )

    connection.commit()

    print("🌿 Health record added successfully!")

    cursor.close()
    connection.close()




def view_health_history():
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
    ORDER BY health_log_id DESC;
    """

    cursor.execute(query)

    records = cursor.fetchall()

    cursor.close()
    connection.close()

    return records



def delete_health_log(health_log_id):
    """
    Deletes a health record.
    """

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    DELETE FROM health_logs
    WHERE health_log_id = %s;
    """

    cursor.execute(query, (health_log_id,))

    connection.commit()

    cursor.close()
    connection.close()

    print("🩺 Health record deleted successfully!")