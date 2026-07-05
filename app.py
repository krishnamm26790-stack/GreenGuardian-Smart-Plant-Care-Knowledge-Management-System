from services.auth_service import (
    register_user,
    login_user
)

import session

from ui import *

from menus import main_menu

from services.watering_service import get_due_today_count


while True:

    title("🔐 GREEN GUARDIAN LOGIN")

    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = get_int("\nEnter your choice : ")

    if choice == 1:

        username = get_string("Username : ")
        password = get_string("Password : ")

        if register_user(username, password):

            success("Registration successful!")

        else:

            error("Username already exists!")

    elif choice == 2:

        username = get_string("Username : ")
        password = get_string("Password : ")

        user = login_user(username, password)

        if user:

            session.current_user = user[1]

            success(f"Welcome {session.current_user}!")

            # Check if any plants need watering today
            due_count = get_due_today_count()

            if due_count > 0:

                print()
                print(f"⚠ {due_count} plant(s) need watering today!")

                view = get_string("View reminders now? (Y/N): ")

                if view.lower() == "y":

                    # Import here to avoid circular import
                    from menus import watering_reminder

                    watering_reminder()

            # Open Main Menu
            main_menu()

            # Logout when exiting main menu
            session.current_user = None

        else:

            error("Invalid username or password.")

    elif choice == 3:

        title("🌿 THANK YOU")

        print("See you again!")

        break

    else:

        error("Invalid choice.")