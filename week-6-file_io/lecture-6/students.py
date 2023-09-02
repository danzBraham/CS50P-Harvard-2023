import csv


# Write to students.csv
name = input("What's your name? ").title()
city = input("What's your city? ").title()

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "city"])
    writer.writerow({"name": name, "city": city})


print()

# Read from students.csv
students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)


for student in sorted(students, key=lambda s: s["name"]):
    print(f"Hello {student['name']} from {student['city']}")
