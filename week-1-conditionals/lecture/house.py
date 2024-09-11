name = input("What's your name? ")

# match name:
#     case "Zidan":
#         print("London")
#     case "Abraham":
#         print("London")
#     case "John":
#         print("London")
#     case "Shelby":
#         print("Birmingham")
#     case _:
#         print("Who?")

# More succint and efficient
match name:
    case "Zidan" | "John" | "Abraham":
        print("London")
    case "Shelby":
        print("Birmingham")
    case _:
        print("Who?")
