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