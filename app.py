from services.auth_service import (
    register_user,
    login_user
)

import session

from ui import *

from menus import main_menu

                                                                                 
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

            main_menu()

            session.current_user = None

        else:

            error("Invalid username or password.")

    elif choice == 3:

        title("🌿 THANK YOU")

        print("See you again!")

        break

    else:

        error("Invalid choice.")