def main():
    mass = get_int("m: ")
    print(f"E: {equation(mass)}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


def equation(mass):
    return mass * 300000000**2


main()
