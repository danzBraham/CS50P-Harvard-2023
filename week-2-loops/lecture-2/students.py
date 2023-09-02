# List
# students = ["Zidan", "Abraham", "John", "Shelby"]
# for i in range(len(students)):
#     print(i + 1, students[i])


# Dictionary
# students = {
#     "Zidan": "London",
#     "Abraham": "London",
#     "John": "London",
#     "Shelby": "Birmingham",
# }

# for student in students:
#     print(f"{student} live in {students[student]}")


# List of Dictionary
students = [
    {"name": "Zidan", "city": "London", "star": 5},
    {"name": "Abraham", "city": "London", "star": 4},
    {"name": "Shelby", "city": "Birmingham", "star": 4},
]

for student in students:
    print(student["name"], student["star"], sep=", ")
