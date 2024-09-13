def main():
    name = input("What's your name? ")
    print(greet(name))


def greet(to="world"):
    return f"hello {to}"


if __name__ == "__main__":
    main()
