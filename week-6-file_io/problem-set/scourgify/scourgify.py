import csv
import sys


def main():
    # Check the number of command-line arguments
    arg_len = len(sys.argv)
    if arg_len < 3:
        sys.exit("Too few command-line arguments")
    elif arg_len > 3:
        sys.exit("Too many command-line arguments")

    # Get the input filename from command-line argument
    infile = sys.argv[1]
    if not infile.endswith(".csv"):
        sys.exit("Not a CSV file")

    # Get the output filename from command-line argument
    outfile = sys.argv[2]

    # Format csv file
    format_csv(infile, outfile)


def format_csv(infile, outfile):
    # List to store the formatted rows
    formatted_rows = []

    try:
        # Open the input file for reading
        with open(infile) as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Format the row and append it to the list
                last, first = row["name"].split(",")
                formatted_rows.append(
                    {
                        "first": first.lstrip(),
                        "last": last,
                        "house": row["house"],
                    }
                )
    except FileNotFoundError:
        sys.exit(f"Could not read {infile}")

    # Write the formatted rows to the output file
    with open(outfile, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for f in formatted_rows:
            writer.writerow(f)


if __name__ == "__main__":
    main()
