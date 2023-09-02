import csv
import sys
from tabulate import tabulate


def main():
    # Check the number of command-line arguments
    arg_len = len(sys.argv)
    if arg_len < 2:
        sys.exit("Too few command-line arguments")
    elif arg_len > 2:
        sys.exit("Too many command-line arguments")

    # Get the filename from command-line argument
    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    # Tabulate menu and then print
    print(tabulate_menu(filename))


def tabulate_menu(filename):
    # Initialize list
    menus = []

    try:
        # Open the CSV file
        with open(filename) as file:
            # Create a CSV reader object
            reader = csv.DictReader(file)
            # Iterate over each row in the CSV file
            for row in reader:
                # Append each row (menu) to the menus list
                menus.append(row)
    except FileNotFoundError:
        # Handle the case where the file does not exist
        sys.exit("File does not exist")

    # Return tabulated menu
    return tabulate(menus, headers="keys", tablefmt="grid")


if __name__ == "__main__":
    main()
