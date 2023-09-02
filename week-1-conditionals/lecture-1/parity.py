def main():
    x = int(input("What's x? "))
    if (iseven(x)):
        print("Even")
    else:
        print("Odd")


def iseven(n):
    # You can use this most elegant way in python or any other programming language:
    return n % 2 == 0

    # Or you can use this "Pythonic" way which is only for python:
    # return True if n % 2 == 0 else False


main()
