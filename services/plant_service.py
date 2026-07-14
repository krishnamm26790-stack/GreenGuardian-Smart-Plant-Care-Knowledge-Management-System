from db import get_connection


def add_plant(plant_name, user_id, plant_type, location, watering_frequency):
    """
    Adds a new plant to the database.
    """

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO plants
    (user_id, plant_name, plant_type, location, watering_frequency)

    VALUES (%s,%s, %s, %s, %s);
    """

    cursor.execute(
        query,
        (user_id,plant_name, plant_type, location, watering_frequency)
    )

    connection.commit()

    print("✅ Plant added successfully!")

    cursor.close()
    connection.close()





def view_all_plants(user_id):
    """
    Fetches and returns all plants from the database.
    """

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT *
    FROM plants
    WHERE user_id = %s
    ORDER BY plant_id;
    """

    cursor.execute(query , (user_id,))

    plants = cursor.fetchall()

    cursor.close()
    connection.close()

    return plants


def get_plant_by_id(user_id,plant_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM plants
        WHERE plant_id=%s
        AND user_id=%s           
    """, (plant_id,user_id))

    plant = cursor.fetchone()

    cursor.close()
    conn.close()

    return plant




def update_plant(
    user_id,
    plant_id,
    plant_name,
    plant_type,
    location,
    watering_frequency
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE plants
        SET
            plant_name=%s,
            plant_type=%s,
            location=%s,
            watering_frequency=%s
        WHERE plant_id=%s
        AND user_id=%s
    """, (
        plant_name,
        plant_type,
        location,
        watering_frequency,
        plant_id,
        user_id
    ))

    conn.commit()

    cursor.close()
    conn.close()



def delete_plant(user_id,plant_id):
    """
    Deletes a plant from the database.
    """

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    DELETE FROM plants
    WHERE plant_id = %s
    AND user_id = %s;
    """

    cursor.execute(query, (plant_id,user_id))

    connection.commit()

    print("🗑️ Plant deleted successfully!")

    cursor.close()
    connection.close()




def search_plants(user_id,keyword):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM plants
        WHERE user_id = %s
        AND (
            LOWER(plant_name) LIKE LOWER(%s)
            OR LOWER(plant_type) LIKE LOWER(%s)
            OR LOWER(location) LIKE LOWER(%s)
            )
        ORDER BY plant_id;
    """, (
        user_id,
        f"%{keyword}%",
        f"%{keyword}%",
        f"%{keyword}%"
    ))

    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return records

def filter_by_type(user_id,plant_type):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM plants
        WHERE user_id =%s 
        AND LOWER(plant_type)=LOWER(%s)
        ORDER BY plant_id;
    """, (user_id,plant_type,))

    plants = cursor.fetchall()

    cursor.close()
    conn.close()

    return plants


def filter_by_location(user_id,location):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM plants
        WHERE user_id = %s
        AND LOWER(location)=LOWER(%s)
        ORDER BY plant_id;
    """, (user_id,location,))

    plants = cursor.fetchall()

    cursor.close()
    conn.close()

    return plants


def filter_by_frequency(user_id,days):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM plants
        WHERE user_id = %s
        AND watering_frequency=%s
        ORDER BY plant_id;
    """, (user_id,days,))

    plants = cursor.fetchall()

    cursor.close()
    conn.close()

    return plants

