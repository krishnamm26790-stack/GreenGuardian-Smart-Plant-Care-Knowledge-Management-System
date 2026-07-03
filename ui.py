# ui.py

WIDTH = 60


def line():

    print("=" * WIDTH)


def divider():

    print("-" * WIDTH)


def title(text):

    line()
    print(text.center(WIDTH))
    line()


def success(message):

    print(f"\n✔ {message}\n")


def error(message):

    print(f"\n✖ {message}\n")


def info(message):

    print(f"\nℹ {message}\n")


def pause():

    input("\nPress Enter to continue...")



def get_int(prompt):

    while True:

        try:

            return int(input(prompt))

        except ValueError:

            error("Please enter a valid number.")


def get_string(prompt):

    while True:

        value = input(prompt).strip()

        if value == "":

            error("Input cannot be empty.")

        else:

            return value