from db import get_connection


def add_plant(plant_name, plant_type, location, watering_frequency):
    """
    Adds a new plant to the database.
    """

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO plants
    (plant_name, plant_type, location, watering_frequency)

    VALUES (%s, %s, %s, %s);
    """

    cursor.execute(
        query,
        (plant_name, plant_type, location, watering_frequency)
    )

    connection.commit()

    print("✅ Plant added successfully!")

    cursor.close()
    connection.close()





def view_all_plants():
    """
    Fetches and returns all plants from the database.
    """

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT *
    FROM plants
    ORDER BY plant_id;
    """

    cursor.execute(query)

    plants = cursor.fetchall()

    cursor.close()
    connection.close()

    return plants




def update_plant_location(plant_id, new_location):
    """
    Updates the location of a plant.
    """

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    UPDATE plants
    SET location = %s
    WHERE plant_id = %s;
    """

    cursor.execute(query, (new_location, plant_id))

    connection.commit()

    print("✅ Plant location updated successfully!")

    cursor.close()
    connection.close()



def delete_plant(plant_id):
    """
    Deletes a plant from the database.
    """

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    DELETE FROM plants
    WHERE plant_id = %s;
    """

    cursor.execute(query, (plant_id,))

    connection.commit()

    print("🗑️ Plant deleted successfully!")

    cursor.close()
    connection.close()




def search_plants(keyword):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM plants
        WHERE
            LOWER(plant_name) LIKE LOWER(%s)
            OR LOWER(plant_type) LIKE LOWER(%s)
            OR LOWER(location) LIKE LOWER(%s)
        ORDER BY plant_id;
    """, (
        f"%{keyword}%",
        f"%{keyword}%",
        f"%{keyword}%"
    ))

    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return records

def filter_by_type(plant_type):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM plants
        WHERE LOWER(plant_type)=LOWER(%s)
        ORDER BY plant_id;
    """, (plant_type,))

    plants = cursor.fetchall()

    cursor.close()
    conn.close()

    return plants


def filter_by_location(location):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM plants
        WHERE LOWER(location)=LOWER(%s)
        ORDER BY plant_id;
    """, (location,))

    plants = cursor.fetchall()

    cursor.close()
    conn.close()

    return plants


def filter_by_frequency(days):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM plants
        WHERE watering_frequency=%s
        ORDER BY plant_id;
    """, (days,))

    plants = cursor.fetchall()

    cursor.close()
    conn.close()

    return plants