import sys


def main():
    arg = "r"

    if len(sys.argv) == 2:
        arg = sys.argv[1]

    if arg == "w":
        name = input("What's your name? ").title()
        with open("names.txt", "a") as file:
            file.write(f"{name}\n")

        sys.exit(0)

    if arg == "r":
        with open("names.txt") as file:
            for line in sorted(file, reverse=True):
                print(f"Hello {line.rstrip()}")

        sys.exit(0)


if __name__ == "__main__":
    main()
