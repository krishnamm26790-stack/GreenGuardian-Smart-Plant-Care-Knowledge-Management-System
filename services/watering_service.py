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