def main():
    x = get_int("What's x? ")
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


def is_even(n):
    # You can use this most elegant way in python or any other programming language:
    return n % 2 == 0

    # Or you can use this "Pythonic" way which is only for python:
    # return True if n % 2 == 0 else False


main()
