def main():
    # Ask user's mass
    m = int(input("m: "))

    # Print the Energy
    print("E:", equation(m))


def equation(m):
    # Calculate equation
    return m * (300000000 ** 2)


main()
