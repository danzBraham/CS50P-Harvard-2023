import csv
import sys
from tabulate import tabulate


def main():
    arg_len = len(sys.argv)
    if arg_len < 2:
        sys.exit("Too few command-line arguments")
    if arg_len > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        pizzas = []
        with open(filename) as file:
            reader = csv.DictReader(file)
            for row in reader:
                pizzas.append(row)
        print(tabulate(pizzas, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
