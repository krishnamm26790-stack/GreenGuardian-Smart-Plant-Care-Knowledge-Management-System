import csv
import os

from db import get_connection


EXPORT_FOLDER = "exports"


def create_export_folder():
    """
    Creates the exports folder if it does not exist.
    """

    if not os.path.exists(EXPORT_FOLDER):
        os.makedirs(EXPORT_FOLDER)


def export_plants_csv():
    """
    Exports all plants to a CSV file.
    """

    create_export_folder()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            plant_id,
            plant_name,
            plant_type,
            location,
            watering_frequency,
            quantity,
            notes
        FROM plants
        ORDER BY plant_id;
    """)

    plants = cursor.fetchall()

    file_path = os.path.join(EXPORT_FOLDER, "plants.csv")

    with open(file_path, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Plant ID",
            "Plant Name",
            "Plant Type",
            "Location",
            "Water Every (Days)",
            "Quantity",
            "Notes"
        ])

        writer.writerows(plants)

    cursor.close()
    conn.close()

    return file_path


def export_watering_csv():
    """
    Exports watering history to a CSV file.
    """

    create_export_folder()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            w.log_id,
            p.plant_name,
            w.watered_on,
            w.notes
        FROM watering_logs w
        JOIN plants p
            ON w.plant_id = p.plant_id
        ORDER BY w.watered_on DESC;
    """)

    records = cursor.fetchall()

    file_path = os.path.join(EXPORT_FOLDER, "watering_logs.csv")

    with open(file_path, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Log ID",
            "Plant",
            "Watered On",
            "Notes"
        ])

        writer.writerows(records)

    cursor.close()
    conn.close()

    return file_path


def export_health_csv():
    """
    Exports health history to a CSV file.
    """

    create_export_folder()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            h.log_id,
            p.plant_name,
            h.status,
            h.observed_on,
            h.notes
        FROM health_logs h
        JOIN plants p
            ON h.plant_id = p.plant_id
        ORDER BY h.observed_on DESC;
    """)

    records = cursor.fetchall()

    file_path = os.path.join(EXPORT_FOLDER, "health_logs.csv")

    with open(file_path, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Log ID",
            "Plant",
            "Status",
            "Observed On",
            "Notes"
        ])

        writer.writerows(records)

    cursor.close()
    conn.close()

    return file_path