import inflect


def main():
    names = []

    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            break

    p = inflect.engine()
    print(f"\nAdieu, adieu, to {p.join(names)}")


if __name__ == "__main__":
    main()
