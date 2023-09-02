def main():
    height = int(input("height: "))
    pyramid(height)


def pyramid(n):
    for i in range(n):
        print((" " * (n - i)) + ("#" * (i + 1)), end="")
        print("#" * i, end="")
        print()


if __name__ == "__main__":
    main()
