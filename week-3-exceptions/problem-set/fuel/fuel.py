def main():
    # Get the fuel percentage from user input
    fuel = get_fuel("Fraction: ")

    # Determine the fuel status and print the result
    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(f"{fuel}%")


def get_fuel(gauge):
    while True:
        try:
            # Prompt the user for a fuel fraction
            fract = input(gauge)
            # Extract the numerator and denominator from the input
            num, denom = map(int, fract.split("/"))
            # Check if the fraction represents a valid fuel level
            if num <= denom:
                return round(num / denom * 100)
        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()
