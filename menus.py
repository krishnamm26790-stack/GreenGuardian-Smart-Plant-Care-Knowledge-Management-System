from tabulate import tabulate


from ui import *

from services.plant_service import (
    add_plant,
    view_all_plants,
    update_plant_location,
    delete_plant
)

from services.watering_service import (
    record_watering,
    view_watering_history,
    delete_watering_log
)

from services._health_service import (
    record_health,
    view_health_history,
    delete_health_log
)

from services.knowledge_service import (
    view_all_knowledge
)


def main_menu():

    while True:

        title("🌿 GREEN GUARDIAN")


        print("1. Plant Management")
        print("2. Watering Management")
        print("3. Health Monitoring")
        print("4. Plant Knowledge")
        print("5. Exit")

        choice = get_string("\nEnter your choice : ")

        if choice == "1":
            plant_menu()

        elif choice == "2":
            watering_menu()

        elif choice == "3":
            health_menu()

        elif choice == "4":
            knowledge_menu()

        elif choice == "5":
            title("🌿 THANK YOU")

            print("""
            Thank you for using Green Guardian.

            Developed by:
            Krishna Mehra

            Happy Gardening 🌱
            """)
            break

        else:
            error("Invalid choice.")


def plant_menu():

    while True:

        title("🌱 PLANT MANAGEMENT")

        print("1. Add Plant")
        print("2. View Plants")
        print("3. Update Plant")
        print("4. Delete Plant")
        print("5. Back")

        plant_choice = get_string("\nEnter your choice : ")

        if plant_choice == "1":

            plant_name = get_string("Plant Name : ")
            plant_type = get_string("Plant Type : ")
            location = get_string("Location : ")
            watering_frequency = get_int(("Watering Frequency (days): "))

            add_plant(
                plant_name,
                plant_type,
                location,
                watering_frequency
            )
            success("Plant added successfully!")
            pause()

        elif plant_choice == "2":

            plants = view_all_plants()

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



        elif plant_choice == "3":

            plant_id = get_int(("Plant ID : "))
            new_location = get_string("New Location : ")

            update_plant_location(
                plant_id,
                new_location
            )
            success("Plant updated successfully!")
            pause()

        elif plant_choice == "4":

            plant_id = get_int(("Plant ID : "))
            delete_plant(plant_id)


            success("Plant deleted successfully!")
            pause()

        elif plant_choice == "5":
            break

        else:
            error("Invalid choice.")


def watering_menu():

    while True:

        title("💧 WATERING MANAGEMENT")

        print("1. Record Watering")
        print("2. View Watering History")
        print("3. Delete Watering Record")
        print("4. Back")

        water_choice = get_string("\nEnter your choice : ")

        if water_choice == "1":

            plant_id = get_int(("Plant ID : "))
            notes = get_string("Notes : ")

            record_watering(
                plant_id,
                notes
            )

        elif water_choice == "2":
            records = view_watering_history()

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

            

        elif water_choice == "3":

            log_id = get_int(("Log ID : "))

            delete_watering_log(log_id)

        elif water_choice == "4":

            break

        else:

            print("❌ Invalid Choice")



def health_menu():

    while True:

        title("❤️ HEALTH MONITORING")

        print("1. Record Health")
        print("2. View Health History")
        print("3. Delete Health Record")
        print("4. Back")

        health_choice = get_string("\nEnter your choice : ")

        if health_choice == "1":

            plant_id = get_int(("Plant ID : "))
            status = get_string("Status : ")
            notes = get_string("Notes : ")

            record_health(
                plant_id,
                status,
                notes
            )

        elif health_choice == "2":
            records = view_health_history()

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

            
        elif health_choice == "3":

            log_id = get_int(("Health Log ID : "))
            delete_health_log(log_id)

        elif health_choice == "4":

            break

        else:

            print("❌ Invalid Choice")


def knowledge_menu():

    while True:

        title("📚 PLANT KNOWLEDGE")

        records = view_all_knowledge()

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