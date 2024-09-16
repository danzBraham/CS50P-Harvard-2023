import csv
import sys


def main():
    arg = "r"

    if len(sys.argv) == 2:
        arg = sys.argv[1]

    if arg == "w":
        name = input("What's your name? ").title()
        city = input("What's your city? ").title()

        with open("students.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "city"])
            writer.writerow({"name": name, "city": city})

        sys.exit(0)

    if arg == "r":
        students = []

        with open("students.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)

        for student in sorted(students, key=lambda student: student["name"]):
            print(f"Hello {student['name']} from {student['city']}")

        sys.exit(0)


if __name__ == "__main__":
    main()
