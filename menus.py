from tabulate import tabulate

import session

from ui import *

from services.plant_service import (
    add_plant,
    view_all_plants,
    update_plant,
    delete_plant,
    search_plants,
    filter_by_type,
    filter_by_location,
    filter_by_frequency
)

from services.watering_service import (
    record_watering,
    view_watering_history,
    delete_watering_log,
    plants_due_for_watering
)

from services._health_service import (
    record_health,
    view_health_history,
    delete_health_log
)

from services.knowledge_service import (
    view_all_knowledge
)

from services.dashboard_service import (
    get_total_plants,
    get_total_health_logs,
    get_total_watering_logs,
    plants_by_type,
    plants_by_location,
    watering_frequency_statistics
)
from services.export_service import (
    export_plants_csv,
    export_watering_csv,
    export_health_csv
)


def dashboard():

    while True:

        title("📊 GREEN GUARDIAN DASHBOARD")

        print(f"👤 Logged in as : {session.current_user}")
        print()

        print(f"🌱 Total Plants      : {get_total_plants()}")
        print(f"💧 Watering Records  : {get_total_watering_logs()}")
        print(f"❤️ Health Records    : {get_total_health_logs()}")

        divider()

        print("1. View Statistics")
        print("2. Back")

        choice = get_int("\nEnter your choice : ")

        if choice == 1:

            show_statistics()

        elif choice == 2:

            break

        else:

            error("Invalid choice.")


def show_statistics():

    title("📈 GARDEN STATISTICS")

    print("\n🌱 Plants by Type")
    print("-" * 35)

    for plant_type, count in plants_by_type():
        print(f"{plant_type:<20} : {count}")

    print("\n📍 Plants by Location")
    print("-" * 35)

    for location, count in plants_by_location():
        print(f"{location:<20} : {count}")

    print("\n💧 Watering Frequency")
    print("-" * 35)

    for days, count in watering_frequency_statistics():
        print(f"Every {days} day(s)".ljust(20), ":", count)

    pause()


def main_menu():

    while True:

        title("🌿 GREEN GUARDIAN")


        print("1. Dashboard")
        print("2. Plant Management")
        print("3. Watering Management")
        print("4. Health Monitoring")
        print("5. Plant Knowledge")
        print("6. Export Data")
        print("7. Exit")

        choice = get_int("\nEnter your choice : ")

        if choice == 1:

            dashboard()

        elif choice == 2:

            plant_menu()

        elif choice == 3:

            watering_menu()

        elif choice == 4:

            health_menu()

        elif choice == 5:

            knowledge_menu()

        elif choice == 6:

            export_menu()

        elif choice == 7:

             title("🌿 THANK YOU")

             print("""
        Thank you for using Green Guardian.

        Developed by:
        Krishna Mehra

        Happy Gardening 🌱
        """)

             break


def plant_menu():

    while True:

        title("🌱 PLANT MANAGEMENT")                         

        print("1. Add Plant")
        print("2. View Plants")
        print("3. Search Plant")                       
        print("4. Filter Plants")
        print("5. Update Plant")
        print("6. Delete Plant")
        print("7. Back")

        plant_choice = get_int("\nEnter your choice : ")

        if plant_choice == 1:

            plant_name = get_string("Plant Name : ")
            plant_type = get_string("Plant Type : ")
            location = get_string("Location : ")
            watering_frequency = get_int("Watering Frequency (days): ")

            add_plant(
                    plant_name,
                    session.current_user_id,
                    plant_type,
                    location,
                    watering_frequency
                )

            success(f'"{plant_name}" added successfully! 🌱')
            pause()

        elif plant_choice == 2:

            plants = view_all_plants(session.current_user_id)

            if plants:

                headers = [
                    "ID",
                    "Plant Name",
                    "Type",
                    "Location",
                    "Water Every (Days)"
                ]

                print()
                print(tabulate(plants, headers=headers, tablefmt="grid"))

            else:

                info("No plants found.")

            pause()

        elif plant_choice == 3:

            keyword = get_string("Enter plant name/type/location : ")

            plants = search_plants(session.current_user_id,keyword)

            if plants:

                headers = [
                    "ID",
                    "Plant Name",
                    "Type",
                    "Location",
                    "Water Every (Days)"
                ]

                print()
                print(tabulate(plants, headers=headers, tablefmt="grid"))

            else:

                info("No matching plants found.")

            pause()

        elif plant_choice == 4:

            filter_menu()

        elif plant_choice == 5:

            plant_id = get_int("Plant ID : ")
            new_location = get_string("New Location : ")

            update_plant(
                plant_id,
                new_location
            )

            success(f"Plant ID {plant_id} updated successfully.")
            pause()

        elif plant_choice == 6:

            plant_id = get_int("Plant ID : ")

            delete_plant(session.current_user_id,plant_id)

            success(f"Plant ID {plant_id} deleted successfully.")
            pause()

        elif plant_choice == 7:

            break

        else:

            error("Invalid choice.")




def filter_menu():

    while True:

        title("🔍 FILTER PLANTS")

        print("1. Filter by Type")
        print("2. Filter by Location")
        print("3. Filter by Watering Frequency")
        print("4. Back")

        choice = get_int("\nEnter your choice : ")

        headers = [
            "ID",
            "Plant Name",
            "Type",
            "Location",
            "Water Every (Days)"
        ]

        if choice == 1:

            plant_type = get_string("Plant Type : ")

            plants = filter_by_type(session.current_user_id,plant_type)

            if plants:
                print()
                print(tabulate(plants, headers=headers, tablefmt="grid"))
            else:
                info("No plants found.")

            pause()

        elif choice == 2:

            location = get_string("Location : ")

            plants = filter_by_location(session.current_user_id,location)

            if plants:
                print()
                print(tabulate(plants, headers=headers, tablefmt="grid"))
            else:
                info("No plants found.")

            pause()

        elif choice == 3:

            days = get_int("Water Every (Days): ")

            plants = filter_by_frequency(session.current_user_id,days)

            if plants:
                print()
                print(tabulate(plants, headers=headers, tablefmt="grid"))
            else:
                info("No plants found.")

            pause()

        elif choice == 4:

            break

        else:

            error("Invalid choice.")


def watering_menu():

    while True:

        title("💧 WATERING MANAGEMENT")

        print("1. Today's Reminders")
        print("2. Record Watering")
        print("3. View Watering History")
        print("4. Delete Watering Record")
        print("5. Back")

        water_choice = get_int("\nEnter your choice : ")

        if water_choice == 1:

            watering_reminder()

        elif water_choice == 2:

            plant_id = get_int("Plant ID : ")
            notes = get_string("Notes : ")

            record_watering(
                session.current_user_id,
                plant_id,
                notes
            )

            success(f"Watering recorded for Plant ID {plant_id}. 💧")
            pause()

        elif water_choice == 3:

            records = view_watering_history(session.current_user_id)

            if records:

                headers = [
                    "Plant",
                    "Watered On",
                    "Notes"
                ]

                print()
                print(tabulate(records, headers=headers, tablefmt="grid"))

            else:

                info("No watering records found.")

            pause()

        elif water_choice == 4:

            log_id = get_int("Log ID : ")

            delete_watering_log(session.current_user_id,log_id)
            success(f"Watering log {log_id} deleted.")

            pause()

        elif water_choice == 5:

            break

        else:

            error("Invalid choice.")



def health_menu():

    while True:

        title("❤️ HEALTH MONITORING")

        print("1. Record Health")
        print("2. View Health History")
        print("3. Delete Health Record")
        print("4. Back")

        health_choice = get_string("\nEnter your choice : ")

        if health_choice == 1:

            plant_id = get_int(("Plant ID : "))
            status = get_string("Status : ")
            notes = get_string("Notes : ")

            record_health(
                session.current_user_id,
                plant_id,
                status,
                notes
            )

        elif health_choice == 2:
            records = view_health_history(session.current_user_id)

            if records:

                headers = [
                    "Plant",
                    "Status",
                    "Observed On",
                    "Notes"
                ]

                print()
                print(tabulate(records, headers=headers, tablefmt="grid"))

            else:

                info("No health records found.")

            
        elif health_choice == 3:

            log_id = get_int(("Health Log ID : "))
            delete_health_log(session.current_user_id,log_id)
            success(f"Health log {log_id} deleted.")
            pause()

        elif health_choice == 4:

            break

        else:

            print("❌ Invalid Choice")


def knowledge_menu():

    while True:

        title("📚 PLANT KNOWLEDGE")

        records = view_all_knowledge(session.current_user_id)

        if records:

            headers = [
                "Plant Type",
                "Scientific Name",
                "Importance",
                "Uses",
                "Sunlight",
                "Watering Tips"
            ]

            print()
            print(tabulate(records, headers=headers, tablefmt="grid"))

        else:

            info("No knowledge available.")

        get_string("\nPress Enter to return to Main Menu...")
        break

def export_menu():

    while True:

        title("📤 EXPORT DATA")

        print("1. Export Plants")
        print("2. Export Watering Logs")
        print("3. Export Health Logs")
        print("4. Export Everything")
        print("5. Back")

        choice = get_int("\nEnter your choice : ")

        if choice == 1:

            path = export_plants_csv()
            success(f"Plants exported successfully!\nSaved to: {path}")
            pause()

        elif choice == 2:

            path = export_watering_csv()
            success(f"Watering logs exported successfully!\nSaved to: {path}")
            pause()

        elif choice == 3:

            path = export_health_csv()
            success(f"Health logs exported successfully!\nSaved to: {path}")
            pause()

        elif choice == 4:

            export_plants_csv()
            export_watering_csv()
            export_health_csv()

            success("All data exported successfully!")
            pause()

        elif choice == 5:

            break

        else:

            error("Invalid choice.")


def watering_reminder():

    title("💧 WATERING REMINDERS")

    plants = plants_due_for_watering(session.current_user_id)

    if not plants:

        print("🎉 Great!")
        print("No plants need watering today.")

        pause()
        return

    print(f"Plants Due Today : {len(plants)}")
    divider()

    for plant in plants:

        plant_id = plant[0]
        name = plant[1]
        location = plant[2]
        frequency = plant[3]
        last_watered = plant[4]

        print(f"🌱 {name}")
        print(f"📍 Location : {location}")
        print(f"💧 Every {frequency} day(s)")

        if last_watered:
            print(f"🕒 Last Watered : {last_watered}")
        else:
            print("🕒 Last Watered : Never")

        divider()

    pause()