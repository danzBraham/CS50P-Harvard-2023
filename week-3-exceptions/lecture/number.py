def main():
    x = get_integer("What's x? ")
    print(f"x is {x}")


def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


if __name__ == "__main__":
    main()
