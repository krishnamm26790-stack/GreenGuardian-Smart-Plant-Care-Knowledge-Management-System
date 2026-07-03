from db import get_connection


def view_all_knowledge():

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT
        plant_type,
        scientific_name,
        importance,
        uses,
        sunlight_requirement,
        watering_tips
    FROM plant_knowledge
    ORDER BY plant_type;
    """

    cursor.execute(query)

    records = cursor.fetchall()

    cursor.close()
    connection.close()

    return records