# Using while loop
# i = 0
# while i < 3:
#     print("meow")
#     i += 1


# Using for loop
# for _ in range(3):
#     print("meow")


# Using pythonic way
# print("meow\n" * 3, end="")


# while True:
#     n = int(input("n: "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")


def main():
    n = get_number()
    meow(n)


def get_number():
    while True:
        try:
            n = int(input("n: "))
            if n > 0:
                return n
        except ValueError:
            pass


def meow(n):
    for _ in range(n):
        print("meow")


if __name__ == "__main__":
    main()
