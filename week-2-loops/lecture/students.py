# List
# students = ["Zidan", "Abraham", "John", "Shelby"]
# Method 1
# for student in students:
#     print(student)
# Method 2
# for i in range(len(students)):
#     print(f"{i + 1}. {students[i]}")


# Dictionary
# students = {
#     "Zidan": "Manchester",
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
    {"name": "John", "city": "Newcastle", "star": None},
]

for student in students:
    print(student["name"], student["city"], student["star"], sep=" | ")
