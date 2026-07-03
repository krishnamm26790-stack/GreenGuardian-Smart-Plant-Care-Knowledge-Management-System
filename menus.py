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

        print("=" * 45)
        print("🌿      GREEN GUARDIAN SYSTEM")
        print("=" * 45)

        print("1. Plant Management")
        print("2. Watering Management")
        print("3. Health Monitoring")
        print("4. Plant Knowledge")
        print("5. Exit")

        choice = input("\nEnter your choice : ")

        if choice == "1":
            plant_menu()

        elif choice == "2":
            watering_menu()

        elif choice == "3":
            health_menu()

        elif choice == "4":
            knowledge_menu()

        elif choice == "5":
            print("\n👋 Thank you!")
            break

        else:
            print("❌ Invalid Choice")


def plant_menu():

    while True:

        print("\n🌱 Plant Management")

        print("1. Add Plant")
        print("2. View Plants")
        print("3. Update Plant")
        print("4. Delete Plant")
        print("5. Back")

        plant_choice = input("\nEnter your choice : ")

        if plant_choice == "1":

            plant_name = input("Plant Name : ")
            plant_type = input("Plant Type : ")
            location = input("Location : ")
            watering_frequency = int(input("Watering Frequency (days): "))

            add_plant(
                plant_name,
                plant_type,
                location,
                watering_frequency
            )

        elif plant_choice == "2":

            plants = view_all_plants()

            print("\n🌿 Plant List\n")

            for plant in plants:

                print("----------------------------")
                print(f"ID : {plant[0]}")
                print(f"Name : {plant[1]}")
                print(f"Type : {plant[2]}")
                print(f"Location : {plant[3]}")
                print(f"Water Every : {plant[4]} day(s)")

        elif plant_choice == "3":

            plant_id = int(input("Plant ID : "))
            new_location = input("New Location : ")

            update_plant_location(
                plant_id,
                new_location
            )

        elif plant_choice == "4":

            plant_id = int(input("Plant ID : "))
            delete_plant(plant_id)

        elif plant_choice == "5":
            break

        else:
            print("❌ Invalid Choice")


def watering_menu():

    while True:

        print("\n💧 Watering Management")

        print("1. Record Watering")
        print("2. View Watering History")
        print("3. Delete Watering Record")
        print("4. Back")

        water_choice = input("\nEnter your choice : ")

        if water_choice == "1":

            plant_id = int(input("Plant ID : "))
            notes = input("Notes : ")

            record_watering(
                plant_id,
                notes
            )

        elif water_choice == "2":

            records = view_watering_history()

            print("\n💧 Watering History\n")

            for plant_name, watered_on, notes in records:

                print("----------------------------")
                print(f"🌿 Plant : {plant_name}")
                print(f"📅 Date : {watered_on}")
                print(f"📝 Notes : {notes}")

        elif water_choice == "3":

            log_id = int(input("Log ID : "))

            delete_watering_log(log_id)

        elif water_choice == "4":

            break

        else:

            print("❌ Invalid Choice")



def health_menu():

    while True:

        print("\n❤️ Health Monitoring")

        print("1. Record Health")
        print("2. View Health History")
        print("3. Delete Health Record")
        print("4. Back")

        health_choice = input("\nEnter your choice : ")

        if health_choice == "1":

            plant_id = int(input("Plant ID : "))
            status = input("Status : ")
            notes = input("Notes : ")

            record_health(
                plant_id,
                status,
                notes
            )

        elif health_choice == "2":

            records = view_health_history()

            print("\n❤️ Health History\n")

            for plant_name, status, observed_on, notes in records:

                print("----------------------------")
                print(f"🌱 Plant : {plant_name}")
                print(f"💚 Status : {status}")
                print(f"📅 Date : {observed_on}")
                print(f"📝 Notes : {notes}")

        elif health_choice == "3":

            log_id = int(input("Health Log ID : "))
            delete_health_log(log_id)

        elif health_choice == "4":

            break

        else:

            print("❌ Invalid Choice")


def knowledge_menu():

    while True:

        print("\n📚 Plant Knowledge")

        records = view_all_knowledge()

        for (
            plant_type,
            scientific_name,
            importance,
            uses,
            sunlight_requirement,
            watering_tips
        ) in records:

            print("------------------------------")
            print(f"🌱 Plant Type : {plant_type}")
            print(f"🔬 Scientific Name : {scientific_name}")
            print(f"⭐ Importance : {importance}")
            print(f"🍃 Uses : {uses}")
            print(f"☀️ Sunlight : {sunlight_requirement}")
            print(f"💧 Watering Tips : {watering_tips}")

        input("\nPress Enter to return to Main Menu...")
        break