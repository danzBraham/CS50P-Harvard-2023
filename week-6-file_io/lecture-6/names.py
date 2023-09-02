# Write to file
# name = input("what's your name? ").capitalize()

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")


# Read from file
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello {name}")
