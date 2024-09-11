def main():
    x = get_int("What's x? ")
    y = get_int("What's y? ")

    print(f"sum : {(sum(x, y))}")
    print(f"sub : {(substract(x, y))}")
    print(f"mult: {(mult(x, y))}")
    print(f"div : {(div(x, y)):.2f}")
    print(f"mod : {(mod(x, y)) }")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            pass


def sum(a, b):
    return a + b


def substract(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


def mod(a, b):
    return a % b


main()
