def main():
    x = int(input("What's x? "))
    y = int(input("What's x? "))

    print((f"Sum: {x + y}"))
    print((f"Sub: {x - y}"))
    print((f"Mult: {x * y}"))
    print(f"Div: {(x / y):.2f}")
    print((f"Mod: {x % y}"))
    print("x squared is", square(x))


def square(n):
    return n ** 2


main()
