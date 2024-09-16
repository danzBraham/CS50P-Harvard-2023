import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a python file")

    try:
        line_counter = 0
        with open(filename, "r") as file:
            for line in file.readlines():
                if not line.isspace() and not line.lstrip().startswith("#"):
                    line_counter += 1
        print(line_counter)
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
