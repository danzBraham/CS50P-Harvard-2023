def main():
    n = get_number()
    print_square(n)


def get_number():
    while True:
        n = int(input("n: "))
        if n > 0:
            return n


def print_column(height):
    print("#\n" * height, end="")


def print_row(width):
    print("#" * width)


def print_square(n):
    # Method 1 Pythonic approach
    print(("#" * n + "\n") * n, end="")

    # Method 2
    # for _ in range(n):
        # print_row(n)


main()
