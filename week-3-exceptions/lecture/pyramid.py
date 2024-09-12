def main():
    height = get_int("Height: ")
    pyramid(height)


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


def pyramid(n):
    for i in range(n):
        print((" " * (n - i)) + ("#" * (i + 1)), end="")
        print("#" * i, end="")
        print()


if __name__ == "__main__":
    main()
