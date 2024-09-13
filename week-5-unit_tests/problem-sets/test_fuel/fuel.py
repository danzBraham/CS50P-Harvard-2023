def main():
    # Ask user;s fraction
    fraction = input("Fraction: ")
    # Convert fraction to percentage
    percentage = convert(fraction)
    # Print the percentage of gauge
    print(gauge(percentage))


def convert(fraction):
    # Map numerator and denominator to integer
    num, denom = map(int, fraction.split("/"))
    # Check if denominator is zero
    if denom == 0:
        raise ZeroDivisionError("Denominator must not be zero")
    # Check if size of numerator greater than denominator
    if num > denom:
        # Raise an exception for invalid fraction
        raise ValueError("Invalid fraction format")
    # Calculate the percentage
    return round(num / denom * 100)


def gauge(percentage):
    # Check if the percentage is less than or equal to 1
    if percentage <= 1:
        return "E"
    # Check if the percentage is greater than or equal to 99
    if percentage >= 99:
        return "F"
    # For percentages between 1 and 99
    return f"{percentage}%"


if __name__ == "__main__":
    main()
