import csv
import sys


def main():
    arg_len = len(sys.argv)
    if arg_len < 3:
        sys.exit("Too few command-line arguments")
    if arg_len > 3:
        sys.exit("Too many command-line arguments")

    file_inp = sys.argv[1]
    file_out = sys.argv[2]

    if not file_inp.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(file_inp) as inp, open(file_out, "w") as out:
            reader = csv.DictReader(inp)
            writer = csv.DictWriter(out, fieldnames=["first", "last", "house"])
            writer.writeheader()

            for row in reader:
                last, first = row["name"].split(",")
                first = first.lstrip()
                writer.writerow({"first": first, "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {file_inp}")


if __name__ == "__main__":
    main()
