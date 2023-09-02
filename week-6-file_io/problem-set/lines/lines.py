import sys


def main():
    # Check the number of command-line arguments
    arg_len = len(sys.argv)
    if arg_len < 2:
        sys.exit("Too few command-line arguments")
    elif arg_len > 2:
        sys.exit("Too many command-line arguments")

    # Get the filename from command-line argument
    filename = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    # Count the number of code lines in the file and then print
    print(count_code_lines(filename))


def count_code_lines(filename):
    # Initialize line count
    count_lines = 0

    try:
        # Open the file
        with open(filename) as file:
            # Iterate over each line in the file
            for row in file:
                # Check if the line is not empty and does not start with a comment
                if not row.isspace() and not row.lstrip().startswith("#"):
                    # Increment the line count
                    count_lines += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Return the line count
    return count_lines


if __name__ == "__main__":
    main()
